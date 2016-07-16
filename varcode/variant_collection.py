# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division, absolute_import
import json
from collections import Counter, defaultdict

from typechecks import require_iterable_of
import pandas as pd

from .collection import Collection
from .effect_collection import EffectCollection
from .common import memoize
from .variant import Variant

class VariantCollection(Collection):
    def __init__(
            self,
            variants,
            sources=[],
            distinct=True,
            sort_key=None,
            metadata_by_sources={}):
        """
        Construct a VariantCollection from a list of Variant records.

        Parameters
        ----------
        variants : iterable
            Variant objects contained in this VariantCollection

        sources : list or set of str
            File path(s) from which we loaded variants, though the current
            VariantCollection may only contain a subset of them.

        distinct : bool
            Don't keep repeated variants

        sort_key : callable

        metadata_by_sources : dict
            Dictionary mapping each source name (e.g. VCF path) to a dictionary
            from metadata attributes to values.
        """
        require_iterable_of(variants, Variant)

        if sort_key is None:
            # pylint: disable=function-redefined
            sort_key = Variant.ascending_position_sort_key

        Collection.__init__(
            self,
            elements=variants,
            sources=sources,
            distinct=distinct,
            sort_key=sort_key)
        self.metadata_by_sources = metadata_by_sources

    @property
    def metadata(self):
        """
        The most common usage of a VariantCollection is loading a single VCF,
        in which case it's annoying to have to always specify that path
        when accessing metadata fields. This property is meant to both maintain
        backward compatibility with old versions of Varcode and make the common
        case easier.
        """
        if len(self.sources) > 1:
            raise ValueError(
                ("This variant collection has multiple sources, "
                 "use metadata_by_sources instead."))
        print(self.metadata_by_sources)
        return self.metadata_by_sources[self.sources[0]]

    def effects(self, raise_on_error=True):
        """
        Parameters
        ----------
        raise_on_error : bool, optional
            If exception is raised while determining effect of variant on a
            transcript, should it be raised? This default is True, meaning
            errors result in raised exceptions, otherwise they are only logged.

        """
        return EffectCollection([
            effect
            for variant in self
            for effect in variant.effects(raise_on_error=raise_on_error)
        ])

    def gene_counts(self):
        """
        Count how many variants overlap each gene name.
        """
        counter = Counter()
        for variant in self:
            for gene_name in variant.gene_names:
                counter[gene_name] += 1
        return counter

    @memoize
    def reference_names(self):
        """
        All distinct reference names used by Variants in this
        collection.
        """
        return set(variant.reference_name for variant in self)

    def groupby_gene_name(self):
        """
        Group variants by the gene names they overlap, which may put each
        variant in multiple groups.
        """
        return self.multi_groupby(lambda x: x.gene_names)

    def groupby_gene_id(self):
        return self.multi_groupby(lambda x: x.gene_ids)

    def detailed_string(self):
        lines = []
        gene_groups = self.groupby_gene_id()
        for gene_id, variant_group in sorted(gene_groups.items()):
            # in case we are combining variants with different Ensembl releases
            # use them all to gather gene names
            gene_names = {
                variant.ensembl.gene_name_of_gene_id(gene_id)
                for variant in variant_group
            }
            gene_name_str = ", ".join(sorted(gene_names))
            lines.append("  -- %s (%s):" % (gene_name_str, gene_id))
            for variant in variant_group:
                lines.append("  ---- %s" % variant)
        header = self.short_string()
        joined_lines = "\n".join(lines)
        return "%s\n%s" % (header, joined_lines)

    def clone_with_new_elements(self, new_elements):
        """
        Create another VariantCollection of the same class and with
        same state (including metadata) but possibly different entries.

        Warning: metadata is a dictionary keyed by variants. This method
        leaves that dictionary as-is, which may result in extraneous entries
        or missing entries.
        """
        return self.__class__(
            new_elements,
            sources=self.sources,
            distinct=self.distinct,
            metadata=self.metadata)

    def filter_by_transcript_expression(
            self,
            transcript_expression_dict,
            min_expression_value=0.0):
        """
        Filters variants down to those which have overlap a transcript whose
        expression value in the transcript_expression_dict argument is greater
        than min_expression_value.

        Parameters
        ----------
        transcript_expression_dict : dict
            Dictionary mapping Ensembl transcript IDs to expression estimates
            (either FPKM or TPM)

        min_expression_value : float
            Threshold above which we'll keep an effect in the result collection
        """
        return self.filter_any_above_threshold(
            multi_key_fn=lambda variant: variant.transcript_ids,
            value_dict=transcript_expression_dict,
            threshold=min_expression_value)

    def filter_by_gene_expression(
            self,
            gene_expression_dict,
            min_expression_value=0.0):
        """
        Filters variants down to those which have overlap a gene whose
        expression value in the transcript_expression_dict argument is greater
        than min_expression_value.

        Parameters
        ----------
        gene_expression_dict : dict
            Dictionary mapping Ensembl gene IDs to expression estimates
            (either FPKM or TPM)

        min_expression_value : float
            Threshold above which we'll keep an effect in the result collection
        """
        return self.filter_any_above_threshold(
            multi_key_fn=lambda effect: effect.gene_ids,
            value_dict=gene_expression_dict,
            threshold=min_expression_value)

    def to_json(self):
        """
        Returns a string giving this variant collection serialized in JSON
        format.
        """
        return json.dumps(self.__getstate__())

    def write_json_file(self, path):
        """
        Serialize this VariantCollection to a JSON representation and write it
        out to a text file.
        """
        with open(path, "w") as f:
            f.write(self.to_json())

    @classmethod
    def from_dict(cls, state):
        """
        Deserialize a VariantCollection encoded as a Python dict.
        """
        instance = cls.__new__(cls)
        instance.__setstate__(state)
        return instance

    @classmethod
    def from_json(cls, serialized):
        """
        Construct a VariantCollection from a JSON string.
        """
        return cls.from_dict(json.loads(serialized))

    @classmethod
    def read_json_file(cls, path):
        """
        Construct a VariantCollection from a JSON file.
        """
        with open(path, 'r') as f:
            json_string = f.read()
        return cls.from_json(json_string)

    def __getstate__(self):
        result = dict(self.__dict__)
        result['elements'] = [
            (e.__getstate__(), self.metadata.get(e)) for e in self]
        del result['metadata']
        return result

    def __setstate__(self, state):
        self.elements = []
        self.metadata = {}
        for (variant_data, meta_entry) in state.pop('elements'):
            variant = Variant.from_dict(variant_data)
            self.elements.append(variant)
            if meta_entry is not None:
                self.metadata[variant] = meta_entry
        self.__dict__.update(state)

    def exactly_equal(self, other):
        '''
        Comparison between VariantCollection instances that takes into account
        the info field of Variant instances.

        Returns
        ----------
        True if the variants in this collection equal the variants in the other
        collection. The Variant.info fields are included in the comparison.
        '''
        return (
            self.__class__ == other.__class__ and
            len(self) == len(other) and
            all(x.exactly_equal(y) for (x, y) in zip(self, other)))

    @classmethod
    def _merge_metadata_dictionaries(cls, dictionaries, combined_variants=None):
        """
        Helper function for combining variant collections: given multiple
        dictionaries mapping:
             source name -> (variant -> (attribute -> value))

        Returns dictionary with union of all variants and sources.
        """
        # three levels of nested dictionaries!
        #   {source name: {variant: {attribute: value}}}
        combined_dictionary = defaultdict(defaultdict(dict))
        if combined_variants is None:
            combined_variants = set.union(*[
                d.values().keys() for d in dictionaries])
        for source_name, variant_to_metadata_dict in dictionaries:
            for variant in combined_variants:
                metadata_dict = variant_to_metadata_dict.get(variant, {})
                combined_dictionary[source_name][variant].update(metadata_dict)
        return combined_dictionary

    @classmethod
    def _combine_variant_collections(
            cls, combine_fn, variant_collections, distinct=True, sort_key=None):
        combined_variants = combine_fn(*variant_collections)
        combined_metadata = cls._merge_metadata_dictionaries(
            dictionaries=[vc.metadata_by_sources for vc in variant_collections],
            combined_variants=combined_variants)
        combined_sources = list(set.union(*[vc.sources for vc in variant_collections]))
        return cls(
            variants=combined_variants,
            sources=combined_sources,
            distinct=distinct,
            sort_key=sort_key,
            metadata_by_sources=combined_metadata)

    @classmethod
    def union(cls, variant_collections, distinct=True, sort_key=None):
        """
        Returns the union of variants in a several VariantCollection objects.
        """
        return cls._combine_variant_collections(
            combine_fn=set.union,
            variant_collections=variant_collections,
            distinct=distinct,
            sort_key=sort_key)

    @classmethod
    def intersection(cls, variant_collections, distinct=True, sort_key=None):
        """
        Returns the intersection of variants in several VariantCollection objects.
        """
        return cls._combine_variant_collections(
            combine_fn=set.intersection,
            variant_collections=variant_collections,
            distinct=distinct,
            sort_key=sort_key)

    def to_dataframe(self):
        """Build a DataFrame from this variant collection"""
        def row_from_variant(variant):
            return {
                "chr": variant.contig,
                "start": variant.original_pos,
                "ref": variant.original_ref,
                "alt": variant.original_alt,
                "gene_name": ";".join(variant.gene_names),
                "gene_id": ";".join(variant.gene_ids)
            }
        return pd.DataFrame.from_records([row_from_variant(v) for v in self])
