# UMI sequencing for ZIKV 

**Author**: Katarina Braun  
**Date**: 2019-02-27  
**Materials**: Catalog numbers for reagents and materials are listed within the protocol. 

1. [Amplicon preparation](##Amplicon-preparation)
2. [Library preparation and QC](##Library-preparation-and-QC) 
3. [Sequencing](##Sequencing)
4. [Analyzing UMI-labeled amplicon reads](##An-overview-to-analyzing-amplicon-reads-labeled-with-a-unique-molecular-identifier)

**Purpose**: To label individual RNA templates with unique molecular identifiers (UMIs), which will be bioinformatically processed post-sequencing to capture nucleotide substitutions that were introduced during library preparation and sequencing. Raw sequence reads labeled with identical UMI are pooled and merged to generate one consensus sequence, which minimizes *method-SNPs* and retains *true SNPs*. This allows us to get a really accurate approximation of the size and makeup of the population of input RNA molecules. This is necessary for high-confidence and low-frequency SNP calls as well as for tracking barcoded viruses over time and between hosts. 

As an alternative to UMI-sequencing, many groups have shown that sequencing in replicate (2-3x) and keeping variant calls seen in all replicates is a very effective strategy to reduce method errors. 

## Amplicon preparation 

Notes: 
- *This protocols assumes are you starting with high-quality, purified vRNA*. 
- If possible, we recommend quantifying vRNA copy number. Bioinformatic analysis of UMI-labeled reads is optimized near 30X-coverage *per input template*. 
- Confidence intervals of SNP frequency calls increase substantially when the total number of RNA molecules going into the RT is less than or equal to 100 copies.

### Reverse Transcription

SSIV (Cat #: Fischer 18091050)

**Primers**: 
- "ZIKV_RT_UMI":  5'GGAGTTCAGACGTGTGCTCTTCCGATCTNNNNNNNNNNNNCCCCCGCAAGTAGCAAGGCCTG3' 
    - contains 12-bp UMI 
    - we order these primers order 'hand-mixed' from IDT

1. Combine RNA + primers + dNTPs into a 0.5 ml RNase-free tube

Anneal primer | ul/tube | [stock] | [final] |
--------------|---------|---------|--------|
vRNA | up to 10ul | | |
dNTP mix | 1ul | 2uM | 0.5uM|
DEPC-treated water | bring to 13ul | - | - |

Total volume = 13ul 

2. Mix and briefly centrifuge to collect liquid from tube walls and cap. 
3. Place tube in 65C heat block for 5 minutes (**denature**). Place on ice for at least one minute (**Anneal**). 
4. Add the following master mix to bring final volume to 20ul: 

RT mix | ul/tube | [stock] | [final] |
-------|---------|---------|---------|
SSIV 5x buffer | 4ul | 4x | 1x |
DTT | 1ul | 100mM | 5mM | 
RNAse out | 1ul | 40 u/ul | 2 u/ul |
SSIV | 1ul | 200 u/ul | 10 u\ul |

Total volume = 20ul

5. Mix and briefly centrifuge to collect liquid from tube walls and cap. 
6. Add RT mix to annealed RNA. 
7. Incubate combined reaction mixture at 50C for 60 mins then 55C for 60 mins (**cDNA synthesis**). 
8. Inactive RT by incubating at 80C for 10 mins (**terminate the reaction**). 
9. Add 1ul RNaseH, incubate at 37C for 20 mins (**remove vRNA**). 
10. Input cDNA into PCR#1 or store at -20C. 

### cDNA Bead Cleanup 

RNAclean XP beads (Cat #: Beckman Coulter A63987)

1. Vortex a 1 ml aliquote of RNAclean XP beads. Allow to come to room temperature, 30 minutes before use. 
2. Transfer cDNA to 1.7 ml RNAse-free tubes.
3. Resuspend the beads. Add 20ul of beads (1x) to each 20ul cDNA reaction. 
4. Mix thoroughly, 15x. Let the tube incubate at room temperature for 20 minutes before proceeding to the next step. 
5. Place the tubes onto a magnetic rack and allow the beads to settle on the magnet. Times vary, depends on bead volume, wait until liquid is clear. Remove and discard clear supernatant. Take care to not aspirate more than trace amounts of beads during this step. 
6. Dispense 200 ul of freshly made 80% ethanol into the tube and incubate for 30 secs at room temperature. Aspirate and discard ethanol. Repeat ethanol washing twice (3x total). It is important to perform these steps with the tube situated on the magnetic rack. Do not disturb the separated magnetic beads. Be sure to remove all of the ethanol from the bottom of the tube with a P20. 
7. Let the beads air-dry (until the beads are not longer shiny) on the rack with the cap open. The tube(s) should air-dry until the last visible traces of ethanol evaporate. Over drying the sample may result in reduced recovery. 
8. Remove the tube(s) from the rack and resuspend beads in ~10ul EB or clean water. Place the tube on the rack and leave until elutant clears. Transfer elutant to a new tube while the tube is situated on the magnet. Do not transfer beads. 

Note: The bead to cDNA ratio may need to be optimized depending on the RNA template. 

### PCR1. Introduce partial MiSeq adaptors. 

Phusion MM (Cat #: NEB M9531S)

1. Thaw and vortex phusion reagents (enzyme should always stay on ice) before use. 
2. Prepare master mixes over ice if possible. 
3. Add template cDNA to each tube and pipette up and down to mix. 

**Primers**: 
- "AdaptF_Zika_131F": 5'TCTTTCCCTACACGACGCTCTTCCGATCT — TGGTTGGCAATACGAGCGATGGTT3'
- "AdapR": 5'GTGACTGGAGTTCAGACGTGTGCTCTTCC3'

reagents | 1x volume 
---------|----------
2x Phusion MM | 10ul 
forward primer | 1ul (0.5uM)
reverse primer | 1ul (0.5uM)
cDNA | up to 2ul (should not take up more than 10% total reaction volume)
DEPC-water | bring to 20ul total reaction volume 

* reaction can be scaled-up if needed 

cycling conditions | cycles | temp (C) | time (seconds)
-------------------|--------| ----------|---------------
initial denaturation | 1x | 98 | 30 secs 
denature | 10-20x | 98 | 10 secs
anneal | 10-20x | 63 (specific to listed primers) | 30 secs
extend | 10-20x | 72 | 30 secs 
final extension | 1x | 72 | 5 minutes 
hold | - | 4 | infinite 

Note: Variables that may require optimization, depending on your template and primers -- annealing temp, number of PCR cycles. 

### PCR1 DNA bead cleanup. 

AMPure XP for PCR purification (Cat #: Beckman Coulter A63881)

1. Vortex 1 ml aliquot of beads. Allow beads to come to room temp for 30 minutes before use. Make sure beads are well-resuspended before use. 
2. Transfer PCR1 reactions into 1.7ml tubes. 
3. Add 18ul of beads to 20ul PCR1 (0.9x). This may vary depending on template length. 
4. Mix thoroughly. Incubate at room temp, off of the magnet, for 5 minutes. 
5. Place tube on the magnet for 5 minutes and allow beads to fully separate from solution. 
6. Slowly aspirate cleared solution and discard. This step should be done with tube(s) on the magnet. Careful to not disturb the beads while they have formed a collection on the side of the tube. 
7. Dispense 500ul of freshly-made 70-80% ethanol into the tube and incubate for 30 seconds at room temp. Aspirate ethanol and discard. Repeat for a total of 2 washes. It is important to do this on the magnet and again be careful to not disturb the beads. Be sure to remove all ethnaol from the bottom of the tube with a P20. 
8. Allow tube(s) to air-dry ~10 mins on the rack with cap open to allow residual ethanol to evaporate. To not overdry -- this will result in lower recovery. 
9. Remove tube from magnet and resuspend beads in 10-12ul clean water or EB. Place the tube back on the magnet rack for ~5 mins. Pipette clear elutant from the tube into a clean tube. 

Note: The bead to cDNA ratio may need to be optimized depending on the RNA template. 

### PCR2. Introduce remaining Illumina and flowcell adaptors as well as indices for sample demultiplexing.  

Phusion MM (Cat #: NEB M9531S)

1. Thaw and vortex phusion reagents (enzyme should always stay on ice) before use. 
2. Prepare master mixes over ice if possible. 
3. Add template cDNA to each tube and pipette up and down to mix. 

**Primers**: 
- "PCR2_index#(1-25)_fwd": 5'CAAGCAGAAGACGGCATACGAGATNNNNNNG TGACTGGAGTTCAGACGTGTGCTCTTCC3'
- "PCR2_rev": 5'AATGATACGGCGACCACCGAGATCTACACTCTT TCCCTACACGACGCTCTTCC'

reagents | 1x volume 
---------|----------
2x Phusion MM | 10ul 
forward primer | 1ul (0.5uM)
reverse primer | 1ul (0.5uM)
PCR1 product | up to 8ul 
DEPC-water | bring to 20ul total reaction volume 

* reaction can be scaled-up if needed 

cycling conditions | cycles | temp (C) | time (seconds)
-------------------|--------| ----------|---------------
initial denaturation | 1x | 98 | 30 secs 
denature | 30-34x | 98 | 10 secs
anneal | 30-34x | 72 (specific to listed primers) | 30 secs
extend | 30-34x | 72 | 30 secs 
final extension | 1x | 72 | 5 minutes 
hold | - | 4 | infinite 

Note: Variables that may require optimization, depending on your template and primers -- annealing temp, number of PCR cycles. 

### Reconditioning cycle to break daisy-chained products

reagents | 1x volume 
---------|----------
2x Phusion MM | 4
forward primer | 0.5ul (0.5uM)
reverse primer | 0.5ul (0.5uM)
PCR1 product | 20ul reaction from above 

* use the same primers as above, make sure to not multiple indices to the same sample 

Total reaction volume with reconditioning reagents: 25ul 

cycling conditions | cycles | temp (C) | time (seconds)
-------------------|--------| ----------|---------------
initial denaturation | 1x | 98 | 30 secs 
denature | 1x | 98 | 10 secs
anneal | 1x | 63 (specific to listed primers) | 30 secs
extend | 1x | 72 | 30 secs 
final extension | 1x | 72 | 5 minutes 
hold | - | 4 | infinite 

**Expected product length**: 252 bps 

![List of indexed PCR2 fwd primers](images/UMI_indexed_primers) 

### Gel cleanup and extraction. 

QIAquick gel extraction kit (Cat #: Qiagen 28115)

1. Pour a 1.2% agarose gel. 
2. Load 25ul of sample + dye into well. 
3. Run at 110V for 35 mins. 
4. Image gel. 
5. Extract desired bands. 

Perform gel extraction according to QIAquick gel extraction manufacturer protocol. Elute in 10-12ul of elution buffer or clean water. See `QIAquick_gel_extraction.md` for details. 

## Library preparation and QC 

Qubit dsDNA HS Assay Kit (Cat #: ThermoFisher Q32854)  
BioAnalyze chips + reagents (hsDNA) (Cat #: Agilent 5067-1505 and 5067-1504)

1. Qubit to quantify amplicons, according to manufacterer instructions. As long as there is at least 0.5ng/ul of clean product, there should be enough to deep sequence. 
2. BioAnalyze (hsDNA) to confirm average fragment length of the amplicons and ensure there is no/little primer-dimer product. Follow manufacturer instructions. 
    - a few tips: make sure gel-dye is no more than 30 days old, make sure pressure applicator is set to 1ml, is at the bottom rung and plate is set to C, make sure the gasket is making a strong seal with the chip. 
3. Depending on how the traces and Qubit values, an additional bead clean-up may be recommended. 

![Example of a desirable BioAnalyzer trace](images/example_trace)  
![Example of a trace with daisy-chaining](images/daisy-chain_trace) 

4. Samples can be loaded separately. However, if there are >10 samples we recommend pooling samples equimolarly and qubiting and bioanalyzing the pool. 

## Sequencing

500-cycle cartridge: 
PhiX: 

1. Pool samples equimolarly into a 4nM pool. 
2. Denature dsDNA using a 0.2N NaOH. 
3. Dilute 4nM pool to a 8-12pM in 600ul library using Hyb or HT1 buffer. 
4. Spike the diluted library with ~30% PhiX (depending on what else is in the run). 
5. Load a 250x250 v2 cartridge and flow cell for paired-end sequencing. 

## An overview to analyzing amplicon reads labeled with a unique molecular identifier 

![An intro to analyzing UMI-labeled Illumina reads](images/UMI_analysis)

For bioinformatic protocols see [this](https://github.com/katarinabraun/UMItools) repository. 

