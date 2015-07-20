from __future__ import absolute_import

from nose.tools import eq_

from varcode import load_vcf, load_vcf_fast, Variant, Substitution
from pyensembl import Genome, GenomeSource
from . import data_path

MOUSE_GTF_PATH = "ftp://ftp.ensembl.org/pub/release-81/gtf/mus_musculus/Mus_musculus.GRCm38.81.gtf.gz"
MOUSE_TRANSCRIPT_FASTA_PATH = "ftp://ftp.ensembl.org/pub/release-81/fasta/mus_musculus/cdna/Mus_musculus.GRCm38.cdna.all.fa.gz"
MOUSE_PROTEIN_FASTA_PATH = "ftp://ftp.ensembl.org/pub/release-81/fasta/mus_musculus/pep/Mus_musculus.GRCm38.pep.all.fa.gz"

MOUSE_VCF = data_path("mouse_vcf_dbsnp_chr1_partial.vcf")

def test_load_vcf_mouse():
    genome = Genome("GRCm38",
                    GenomeSource(gtf_path=MOUSE_GTF_PATH,
                                 transcript_fasta_path=MOUSE_TRANSCRIPT_FASTA_PATH,
                                 protein_fasta_path=MOUSE_PROTEIN_FASTA_PATH))
    variants = load_vcf(MOUSE_VCF, genome=genome)
    eq_(len(variants), 217)
    variants = load_vcf_fast(MOUSE_VCF, genome=genome)
    eq_(len(variants), 217)

def test_specific_variant_mouse():
    genome = Genome("GRCm38",
                    GenomeSource(gtf_path=MOUSE_GTF_PATH,
                                 transcript_fasta_path=MOUSE_TRANSCRIPT_FASTA_PATH,
                                 protein_fasta_path=MOUSE_PROTEIN_FASTA_PATH))
    # Exon #2 at http://useast.ensembl.org/Mus_musculus/Transcript/Exons?
    # db=core;g=ENSMUSG00000017167;r=11:101170523-101190724;t=ENSMUST00000103109
    variant = Variant(contig=11, start=101177240, ref="G", alt="T", ensembl=genome)
    effects = variant.effects()
    eq_(len(effects), 2)
    substitution_effects = [effect for effect in effects if isinstance(effect, Substitution)]
    eq_(len(substitution_effects), 1)
    substitution_effect = substitution_effects[0]
    # The coding sequence through the sub:
    # ATGATGAGTCTCCGGCTCTTCAGCATCCTGCTCGCCACG
    # GTGGTCTCTGGAGCTTGGGGCTGGGGCTACTACGGTTGC
    # (The final G is the sub: the 77th nucleotide)
    # TGC (C) -> TTC (F)
    # 78 / 3 = 26
    # 0-base = 25
    eq_(substitution_effect.mutant_protein_sequence[25], "F")
    eq_(substitution_effect.original_protein_sequence[25], "C")
