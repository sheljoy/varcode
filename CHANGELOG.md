# Change Log

## [v0.4.2](https://github.com/hammerlab/varcode/tree/v0.4.2) (2016-02-25)
**Implemented enhancements:**

- VariantCollection.high\_priority\_effect != Variant.top\_effect [\#58](https://github.com/hammerlab/varcode/issues/58)
- Improves the documentation for varcode [\#110](https://github.com/hammerlab/varcode/pull/110) ([armish](https://github.com/armish))
- Convert effect-type section into a sorted table [\#104](https://github.com/hammerlab/varcode/pull/104) ([armish](https://github.com/armish))
- Start highlighting Python syntax in README [\#103](https://github.com/hammerlab/varcode/pull/103) ([armish](https://github.com/armish))

**Fixed bugs:**

- Varcode requires pandas \>= 0.13.1, however it uses 0.15 functionality \#12 [\#92](https://github.com/hammerlab/varcode/issues/92)
- Varcode version 0.3.10 cannot be imported when installed through pip [\#90](https://github.com/hammerlab/varcode/issues/90)
- pip installing Varcode doesn't seem to work lately [\#84](https://github.com/hammerlab/varcode/issues/84)
- AttributeError: 'FrameShiftTruncation' object has no attribute 'aa\_alt' [\#70](https://github.com/hammerlab/varcode/issues/70)
- Use find\_packages correctly [\#85](https://github.com/hammerlab/varcode/pull/85) ([tavinathanson](https://github.com/tavinathanson))

**Closed issues:**

- memoize a bit less [\#131](https://github.com/hammerlab/varcode/issues/131)
- Intragenic variants do not have a short\_description field [\#129](https://github.com/hammerlab/varcode/issues/129)
- move read\_evidence module and Locus class to varlens [\#124](https://github.com/hammerlab/varcode/issues/124)
- Support Structural Variants [\#122](https://github.com/hammerlab/varcode/issues/122)
- PrematureStop called as Silent [\#116](https://github.com/hammerlab/varcode/issues/116)
- PrematureStop called as a Deletion [\#111](https://github.com/hammerlab/varcode/issues/111)
- UnboundLocalError in in\_frame\_coding\_effect.py [\#107](https://github.com/hammerlab/varcode/issues/107)
- Double mutations in a MAF file cause error [\#105](https://github.com/hammerlab/varcode/issues/105)
- varcode.load\_vcf\_fast used 0.16.1 Pandas options [\#101](https://github.com/hammerlab/varcode/issues/101)
- Configuring datacache default cache directory [\#98](https://github.com/hammerlab/varcode/issues/98)
- Improve the README to include some examples of working with Varcode in IPython [\#95](https://github.com/hammerlab/varcode/issues/95)
- support loading VCFs over HTTP [\#91](https://github.com/hammerlab/varcode/issues/91)
- Travis should include setup.py testing [\#86](https://github.com/hammerlab/varcode/issues/86)
- Make Variants pickle-able [\#77](https://github.com/hammerlab/varcode/issues/77)
- modifies\_coding\_sequence is always false [\#64](https://github.com/hammerlab/varcode/issues/64)
- AssertionError: aa\_ref and aa\_alt can't both be empty string [\#63](https://github.com/hammerlab/varcode/issues/63)
- Too many open files on error on getting top effect [\#62](https://github.com/hammerlab/varcode/issues/62)
- KeyError: 'reference' in load\_vcf [\#60](https://github.com/hammerlab/varcode/issues/60)
- Issue with n\_skip? [\#56](https://github.com/hammerlab/varcode/issues/56)
- Optional random seed argument for generating random variants [\#48](https://github.com/hammerlab/varcode/issues/48)
- An argument for using == and not \>= for requirements? [\#43](https://github.com/hammerlab/varcode/issues/43)
- deploy a test coverage tool [\#38](https://github.com/hammerlab/varcode/issues/38)
- Replace raise\_on\_error parameter to property of VariantCollection [\#36](https://github.com/hammerlab/varcode/issues/36)
- assertion error in infer\_coding\_effect [\#33](https://github.com/hammerlab/varcode/issues/33)
- add a memoized "highest\_priority\_effect" property to Variant [\#31](https://github.com/hammerlab/varcode/issues/31)
- support deep reloading varcode module [\#25](https://github.com/hammerlab/varcode/issues/25)
- handle multiallelic variants [\#22](https://github.com/hammerlab/varcode/issues/22)
- vcf.load\_vcf should provide an option to load all variants, regardless of whether filter is PASS [\#21](https://github.com/hammerlab/varcode/issues/21)
- empty variant collection when loading strelka vcf [\#16](https://github.com/hammerlab/varcode/issues/16)
- Incorrect handling of variants which run past the beginning/end of an exon's boundary [\#14](https://github.com/hammerlab/varcode/issues/14)
- Reference amino acid sequence sometimes empty for coding variants [\#12](https://github.com/hammerlab/varcode/issues/12)
- handle single-sample VCFs with INFO fields containing list values of size \> 1 [\#9](https://github.com/hammerlab/varcode/issues/9)
- Do FrameShift \(or StopGain\) mutations affect splicing? [\#6](https://github.com/hammerlab/varcode/issues/6)
- What to do with mutations that span the 5' UTR / CDS boundary? [\#5](https://github.com/hammerlab/varcode/issues/5)
- Annotate essential splice site mutations [\#1](https://github.com/hammerlab/varcode/issues/1)

**Merged pull requests:**

- Modest change to filtering of coding mutations include ExonicSpliceSite  [\#137](https://github.com/hammerlab/varcode/pull/137) ([iskandr](https://github.com/iskandr))
- Version bump [\#135](https://github.com/hammerlab/varcode/pull/135) ([tavinathanson](https://github.com/tavinathanson))
- Fix conda install on Travis [\#134](https://github.com/hammerlab/varcode/pull/134) ([iskandr](https://github.com/iskandr))
- Don't memoize EffectCollection.top\_priority\_effect\(\) [\#132](https://github.com/hammerlab/varcode/pull/132) ([timodonnell](https://github.com/timodonnell))
- All effects should have a default `short\_description` field [\#130](https://github.com/hammerlab/varcode/pull/130) ([armish](https://github.com/armish))
- Remove read\_evidence and locus modules [\#125](https://github.com/hammerlab/varcode/pull/125) ([timodonnell](https://github.com/timodonnell))
- Include a link to the iPython notebook in README.md [\#121](https://github.com/hammerlab/varcode/pull/121) ([armish](https://github.com/armish))
- Add varcode to Travis [\#120](https://github.com/hammerlab/varcode/pull/120) ([tavinathanson](https://github.com/tavinathanson))
- Minor problem in Variant.\_\_init\_\_ [\#119](https://github.com/hammerlab/varcode/pull/119) ([iskandr](https://github.com/iskandr))
- Update Varcode to work with new multi-species PyEnsembl  [\#118](https://github.com/hammerlab/varcode/pull/118) ([iskandr](https://github.com/iskandr))
- Fix \#116 and call PrematureStop when stop codon is added in the middle of an insertion [\#117](https://github.com/hammerlab/varcode/pull/117) ([leekaiinthesky](https://github.com/leekaiinthesky))
- Warn when variants in MAF file have wrong end position [\#115](https://github.com/hammerlab/varcode/pull/115) ([iskandr](https://github.com/iskandr))
- Bump pyensembl/varcode version [\#114](https://github.com/hammerlab/varcode/pull/114) ([tavinathanson](https://github.com/tavinathanson))
- fix logic for determining whether the protein length decreases [\#112](https://github.com/hammerlab/varcode/pull/112) ([leekaiinthesky](https://github.com/leekaiinthesky))
- decreasing 3' splice site to distance 3 from boundary [\#109](https://github.com/hammerlab/varcode/pull/109) ([iskandr](https://github.com/iskandr))
- fixed typo in effect inference, added breaking variant to unit tests [\#108](https://github.com/hammerlab/varcode/pull/108) ([iskandr](https://github.com/iskandr))
- Allow Varcode to work with mouse data via Genome [\#106](https://github.com/hammerlab/varcode/pull/106) ([tavinathanson](https://github.com/tavinathanson))
- Manually set compression in read\_vcf\_into\_dataframe [\#102](https://github.com/hammerlab/varcode/pull/102) ([timodonnell](https://github.com/timodonnell))
- Added examples to README [\#100](https://github.com/hammerlab/varcode/pull/100) ([iskandr](https://github.com/iskandr))
- depend on pandas \>= 0.15 [\#99](https://github.com/hammerlab/varcode/pull/99) ([iskandr](https://github.com/iskandr))
-  Faster VCFs loading, support HTTP, and refactored variant metadata [\#94](https://github.com/hammerlab/varcode/pull/94) ([timodonnell](https://github.com/timodonnell))
- Support for regular varcode variant instances in read evidence module [\#87](https://github.com/hammerlab/varcode/pull/87) ([timodonnell](https://github.com/timodonnell))
- Read and write json files [\#82](https://github.com/hammerlab/varcode/pull/82) ([iskandr](https://github.com/iskandr))
- JSON serialization for VariantCollection. [\#81](https://github.com/hammerlab/varcode/pull/81) ([timodonnell](https://github.com/timodonnell))
- Add short\_description field to intergenic variants [\#80](https://github.com/hammerlab/varcode/pull/80) ([timodonnell](https://github.com/timodonnell))
- Speed up PileupCollection.group\_by\_allele [\#79](https://github.com/hammerlab/varcode/pull/79) ([timodonnell](https://github.com/timodonnell))
- Variant serialization [\#78](https://github.com/hammerlab/varcode/pull/78) ([timodonnell](https://github.com/timodonnell))
- added option for genome name in load\_vcf [\#76](https://github.com/hammerlab/varcode/pull/76) ([iskandr](https://github.com/iskandr))
- Fix variant.effects\(\) to always return an EffectCollection [\#75](https://github.com/hammerlab/varcode/pull/75) ([timodonnell](https://github.com/timodonnell))
- Bump pysam dependency [\#74](https://github.com/hammerlab/varcode/pull/74) ([timodonnell](https://github.com/timodonnell))
- Cufflinks RNA filtering [\#73](https://github.com/hammerlab/varcode/pull/73) ([iskandr](https://github.com/iskandr))
- Read evidence tweaks [\#72](https://github.com/hammerlab/varcode/pull/72) ([timodonnell](https://github.com/timodonnell))
- Filter effect collection by expression [\#67](https://github.com/hammerlab/varcode/pull/67) ([iskandr](https://github.com/iskandr))
- Created EpitopeCollection, refactored effects, fix assertion failure while annotating silent stop codon [\#66](https://github.com/hammerlab/varcode/pull/66) ([iskandr](https://github.com/iskandr))
- Created EpitopeCollection, refactored effects [\#65](https://github.com/hammerlab/varcode/pull/65) ([iskandr](https://github.com/iskandr))
- include substitution in high priority effects [\#61](https://github.com/hammerlab/varcode/pull/61) ([arahuja](https://github.com/arahuja))
- don't annotate StopLoss variants that are immediately followed by another stop codon [\#57](https://github.com/hammerlab/varcode/pull/57) ([iskandr](https://github.com/iskandr))
- Refactor coding effect [\#55](https://github.com/hammerlab/varcode/pull/55) ([iskandr](https://github.com/iskandr))
- Add read\_evidence module [\#53](https://github.com/hammerlab/varcode/pull/53) ([timodonnell](https://github.com/timodonnell))
- Use transcript protein sequence [\#45](https://github.com/hammerlab/varcode/pull/45) ([iskandr](https://github.com/iskandr))
- Add contributing md [\#41](https://github.com/hammerlab/varcode/pull/41) ([iskandr](https://github.com/iskandr))
- Small coding effect refactoring and fixes [\#39](https://github.com/hammerlab/varcode/pull/39) ([iskandr](https://github.com/iskandr))
- Test problematic variants [\#37](https://github.com/hammerlab/varcode/pull/37) ([iskandr](https://github.com/iskandr))
- Typechecks and test fixes [\#35](https://github.com/hammerlab/varcode/pull/35) ([timodonnell](https://github.com/timodonnell))
- Fix maf parsing [\#34](https://github.com/hammerlab/varcode/pull/34) ([iskandr](https://github.com/iskandr))
- parse multiple alleles into distinct Variant records [\#29](https://github.com/hammerlab/varcode/pull/29) ([iskandr](https://github.com/iskandr))
- PEP8 & pyflakes fixes [\#28](https://github.com/hammerlab/varcode/pull/28) ([iskandr](https://github.com/iskandr))
- Remove pyfaidx [\#27](https://github.com/hammerlab/varcode/pull/27) ([iskandr](https://github.com/iskandr))
- Variant collection tweaks [\#24](https://github.com/hammerlab/varcode/pull/24) ([timodonnell](https://github.com/timodonnell))
- Improved vcf parsing [\#23](https://github.com/hammerlab/varcode/pull/23) ([timodonnell](https://github.com/timodonnell))
- Associate EnsemblRelease with each Variant object [\#20](https://github.com/hammerlab/varcode/pull/20) ([iskandr](https://github.com/iskandr))
- Variant collection filtering [\#19](https://github.com/hammerlab/varcode/pull/19) ([iskandr](https://github.com/iskandr))
- added IntronicSpliceSite, SpliceDonor, SpliceAcceptor effects [\#17](https://github.com/hammerlab/varcode/pull/17) ([iskandr](https://github.com/iskandr))
- collect effect annotation errors in dictionary, only look up overlapping... [\#13](https://github.com/hammerlab/varcode/pull/13) ([iskandr](https://github.com/iskandr))
- don't flatten INFO dictionary of VCF, lists are part of the field format [\#11](https://github.com/hammerlab/varcode/pull/11) ([iskandr](https://github.com/iskandr))
- Small fixes [\#10](https://github.com/hammerlab/varcode/pull/10) ([timodonnell](https://github.com/timodonnell))
- Add support for Python 3 [\#8](https://github.com/hammerlab/varcode/pull/8) ([timodonnell](https://github.com/timodonnell))
- Refactor core logic [\#7](https://github.com/hammerlab/varcode/pull/7) ([iskandr](https://github.com/iskandr))
- Classes for protein/transcript variant effects [\#3](https://github.com/hammerlab/varcode/pull/3) ([iskandr](https://github.com/iskandr))



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*