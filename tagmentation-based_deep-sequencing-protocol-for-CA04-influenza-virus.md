# Tagmentation-based deep sequencing protocol for CA04 influenza virus

### A few important considerations:  
- This protocol assumes you are starting with relatively high-quality viral RNA.
- When possible, quantify viral RNA (copies/µl) by QRT-PCR or Qubit. We have found SNP calls are more accurate and reliable when starting with >1,000 RNA template molecules that go into reverse transcription. 
- When working with vRNA, it is important to work in a clean space (has had minimal contact with amplified nucleic acids and is clened often to minimize RNAse contamination). 
- We clean all pipetters, pipette boxes, and working surfaces with a 10% bleach solution and then a 70% ethanol solution before and after each of the below steps. This helps minimize cross-contaminaton between samples and off-target amplification. 

## Reverse transcription

**Materials** 
- SSIV VILO Master Mix: Invitrogen 11756050
- RNase OUT: Invitrogen 10777019
- RNase H: NEB M0297S
- RNAse-free tubes (not necessary): ThermoFisher 50591363
- Primer. Uni12primer: Ordered from IDT at 100µM. Diluted to 10µM working stock. 
    - AGCRAAAGCAGG
- Ultrapure water. 

**Protocol**
1. Add RNase OUT to DEPC-treated water (10ul to 1ml or equivalent)
2. Add the following components to an empty RNAse-free tube on ice.

Reagent | ul/tube (ul) | Master Mix (ul) (10x)
--- | --- | ---
SSIV VILO Master Mix | 4 |44
Template RNA | 10 | add independently
RT Primer, 2uM | 1 | 11
DEPC-treated H2O (with 1:10000 RNase OUT) | 5 | 55

3. Mix and briefly centrifuge
4. Incubate at 25C for 10 minutes. (Anneal primers).
5. Incubate at 50C for 30 minutes. (Reverse transcribe RNA to cDNA).
6. Incubate at 85C for 5 minutes. (Inactivate the SSIV VILO enzyme).
7. To remove RNA, add 1ul of RNAseH, incubate at 37C for 20 minutes. (Remove the RNA). 
8. Use cDNA for PCR amplification right away or store at -20C. 

**Note:** Avoid excess freeze/thaw cycles of viral RNA when possible. We like to make vRNA aliquots at the first thaw if we know we are going to go back to the original sample for additional sequencing or other assays. 

## PCR, second strand synthesis

**Materials**
- Phusion High-Fidelity PCR Master Mix: NEB 50994945
- 0.2 ml TempAssure PCR 8-Tube flex-free strips: Fisher Scientific NC9989922
- Ultrapure water. 
- Primers. Ordered from IDT at 100µM. Diluted to 10µM working stock. 
    - [Universal Hoffman primer (binds and amplifies UTR of all segments](https://link.springer.com/content/pdf/10.1007%2Fs007050170002.pdf)
        - \- *or* -
    - Segment-specific primers (sequence and annealing temps are listed in table below)

**Protocol**
1. Thaw Phusion and keep on ice when not pipetting. 
2. Label tubes prior to making master mixes. 
3. Prepare one master mix per segment (over ice if possible), and aliquot. 
4. Aliquot cDNA. 
5. Pipette thoroughly to mix. 

Per each Segment 8x| 1x (ul) | MM 10x (+10% extra)
|---|---|---|---|
2x Phusion MM | 10 | 110
PCR_fwd (10uM) | 1 | 11
PCR_rev (10uM) | 1 | 11
cDNA | 2 | Add individually |
Water | 6ul | 66

*Total Reaction Volume*: 18ul MM in each tube. Add 2ul cDNA to bring the total reaction volume to 20ul. 

**Cycling conditions**
Per each Segment | Temp C | Time 
|---|---|---|
Initial denaturation | 98 | 30 seconds
x35 (denature, anneal, extend) | 98 | 10 seconds
| | xx | 30 seconds
| | 72 | 120 seconds
Final Extension | 72 | 5 minutes
Hold | 4 | forever

**Segment specific primers**
Primer | Sequence (5'-3') | Orientation | Segment | Annealing temp (C) |
|---|---|---|---|---|
PB2_CA04_F | ATA TAC GCG TAG CGA AAG CAG GTC AA | Forward |  PB2 | 67 |
PB2_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGT CG | Reverse | PB2 | 67 |
PB1_CA04_F | ATA TAC GCG TAG CGA AAG CAG GCA AA | Forward | PB1 | 67|
PB1_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGC AT | Reverse | PB1 | 67|
PA_CA04_F | ATA TAC GCG TAG CGA AAG CAG GTA CT | Forward | PA | 63|
PA_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGT AC | Reverse | PA | 63|
HA_CA04_F_v1 | ATA TAC GCG TAG CGA AAG CAG GGG AA | Forward | HA | 61|
HA_CA04_R_v1 | ATA TAC GCG TAG TAG AAA CAA GGT GT | Reverse | HA | 61|
HA_CA04_F-v2 | AG CAA AAG CAG GGG AAA ACA A | Forward | HA | 61|
HA_CA04_R-v2 | AG TAG AAA CAA GGG TGT TTT TC | Reverse | HA | 61|
NP_CA04_F | ATA TAC GCG TAG CAA AAG CAG GGT AG | Forward | NP | 67|
NP_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGG TA | Reverse | NP | 67|
NA_CA04_F | ATA TAC GCG TAG CAA AAG CAG GAT TT | Forward | NA | 66|
NA_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGA GT | Reverse | NA | 66|
M_CA04_F | ATA TAC GCG TAG CAA AAG CAG GTA GA | Forward | M | 65|
M_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGT AG | Reverse | M | 65|
NS_CA04_F | ATA TAG GCG TAG CAA AAG CAG GGT GA | Forward | NS | 69|
NS_CA04_R | ATA TAC GCG TAG TAG AAA CAA GGG TG | Reverse | NS | 69|

## Gel purification / Extraction and Quantification by Qubit Fluorometer 

**Materials**
- Agarose powder and TAE: standard
- SYBR Safe: Invitrogen S33102
- 5x or 6x gel dye: ThermoFisher R0611 or equivalent
- 100bp ladder: NEB N0467S or equivalent
- QIAquick Gel Extraction Kit: Qiagen 28115 
- Qubit hsDNA Kit: ThermoFisher Q32854 

**Protocol** 

1. Make 1% agaose gel. We make 90ml gels, so add 0.9mg of agaose power fo 90ml of TAE. Microwave until clear. When agarose is cool enough touch, add 9µl of SYBR Safe and pour into gel box. Gels are okay at 4C for one week after they are poured. 
2. Add gel dye (5x or 6x) to samples and load samples into gel. Load 5-10µl of 100bp ladder in at least one well in order to accurately extract the band of interest. 
3. Run gel at 100V for 35 minutes. 
4. Image gel and extract bands of interest. Expected band sizes are outlined in table below. 
5. Extract bands of interest using scalpel and place in labeled 1.5ml eppendorf tubes. 
6. Proceed with QIAquick Gel Extraction Protcol as per manufacturer's instructions (outlined briefly below):
    - Excise band and weigh. 
    - Add 3 volumes Buffer QG to 1 gel volume. Max amount per spin column is ~400mg. 
    - Incubate at 50C for 10 mins or until gel is completely dissolved. Vortex every 2-3 minutes to help the gel dissolve. 
    - Add 1 gel volume of isopropanol to the sample and vortex to mix. 
    - Transfer dissolved gel solution to a QIAquick spin column in a 2ml collection tube. Spin at 13,000 rpm for 1 min. Discard flow-through. If sample is >800 µl, load and spin again. 
    - Add 500µl Buffer QG to the column, centrifuge 13,000 rpm for 1 min, discard flow-through. 
    - Add 750µl Buffer PE (make sure you have added ethanol to the solution), incubate for 2-5 minutes at room temp to maximize yield, spin at 13,000 rpm for 1 min, discard flow-through. Repeat spin once more to discard excess Buffer PE. 
    - Place QIAquick column in a clean 1.5ml eppendorf tube. 
    - Add 12µl of clean water or elution buffer to the QIAquick membrane, incubate for 3-4 minutes at room temperature to maximize yield. Centrifuge at 13,000 rpm for 1 min. Collect and store flow-through. 
7. Quantify product via hsDNA Qubit according to manufacturer instructions. Outlined briefly below: 
    - Allow Qubit standards to come to room temperature for 30 mins before use. 
    - Add 190µl of Qubit solution (dye + buffer) to two Qubit tubes (must be Qubit tubes) and label as standard 1 and standard 2. Add 10µl of standards to each tube. Vortex to mix. 
    - Aliquot 199µl of Qubit solution (dye + buffer) to n Qubit tubes where n = number of samples to quantify. Add 1µl of samples to each tube. Vortex to mix. 
    - Quantify by hsDNA fluorometer. Calibrate using standards before use. Measure in ng/µl. 

Segment | Approximate expected length (bps) | 
----|------|
PB2 | ~2,500 |
PB1 | ~2,400 | 
PA | ~2,200 | 
HA | ~1,900 | 
NP | ~1,700 |
NA | ~1,700 | 
M | ~1,200 |
NS | ~950 |

## Library preparation using the Nextera XT protcol

**Materials** 
- Qubit hsDNA Kit: ThermoFisher Q32854 
- Nextera XT Index Kit v2 Set A: Illumina FC-131-2001 (can use other index sets (A-D) to load up to 382 unique samples)
- Nextera XT DNA Libray Preparation Kit: Illumina FC-131-1024 (24 samples) or Illumina FC-131-1096 (96 samples)
- AMPure XP for PCR Purification: Beckman Coulter A63880
- 100% ethanol: standard. 

Illumina's Nextera DNA Library Prep Reference Guide can be found [here](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_nextera/nexteradna/nextera-dna-library-prep-reference-guide-15027987-01.pdf). 

**Protocol** 
1. At this point, if we are doing whole-genome sequencing, we will pools segments prior to tagmentation and indexing. To do this, if segment samples are >1ng/µl, we dilute them down to 1ng/µl then pool by adding 1µl of each segment to the pooled sample. We repeat Qubit quantification of these pools once more -- concentrations are usually 0.5ng - 1ng/µl. Add 1ng of these pools to a total of 5µl of water (you want 1ng segment or equimolar pool per 5µl volume before you proceed to tagmentation). 
    - We use an Excel spreadsheet to assist with these calculations and are happy to share this sheet if it would be helpful. 
2. Tagmentation (shear DNA and add short adapter sequences to the end of these products). 
    - Remove the ATM, TD, and input DNA from the -20 and thaw on ice. 
    - Ensure that the NT is at room temp. Ensure there is no precipitate. We usually get the NT out after the tubes go on the thermocycler. 
    - Adequately mix all reagents by gently inverting the tubes 3-5 times and briefly spin down in a microcentrifugee. 
    - Label a plate / tubes. 
    - Add 10µl of TD (tagment DNA) buffer to each tube, change tips between samples.
    - Add 5µl of input DNA at 0.2ng/µl (1ng total) to each sample well. 
    - Add 5µl of ATM (Amplicon Tagment Mix) to the wells containing input DNA and TD buffer, change tips between samples. 
    - Gently vortex to mix. There should be a total of volume of 20µl at this point.
    - Put tubes on thermocycler: 

Tagmentation 1 | Temp C | Time 
|---|---|---|
step 1 | 55C | 5 mins
step 2 | 10C | hold

- Once the sample reaches 10C, add 5µl of NT (neutralize tagment) buffer to each well. Make sure to add NT immediately after the sample reaches 10C. 
- Gently vortex and spin down. 
- Incubate for 5 minutes at room temp. Total volume is now 25ul. 

3. Limited cycle PCR amplification to append indices. 
    - Remove index primers and NPM from the -20C and thaw at room temp. Allow approx 20 mins to do so. Invert 3-5x to mix. 
    - Add 15µl of NPM (Nextera PCR Master Mix) to each sample tube.
    - Add 5µl of index 2 primers (i5) (white caps), changing tips between tubes.
    - Add 5µl of index 1 primers (i7) (orange caps), changing tips between tubes. 
        - (you can do this using a plate and a multichannel pipetter)
    - Replace caps of indices with new ones to avoid cross contamination. 
    - Gently vortex and spin down. Total volume is now 50ul. 
    - Put tubes on thermocycler for tagmentation 2: 

Tagmentation 2 | Temp C | Time 
|---|---|---|
step 1 | 72C | 3 mins
denaturation | 95C | 30 seconds
15 cycles | 95C | 10 seconds
||55C | 30 seconds 
|| 72C | 30 seconds
| final extension | 72C | 5 mins
| hold | 4C | forever 

- Safe stopping point. Can be stored at 4C for up to 2 days. 

4. Purify the product using AMPure XP beads: clean-up followed by size exclusion
Clean-up
    - Add 25µl Ampure beads to your 50µl product for a 0.5x bead clean-up to remove small fragments. 
    - Incubate at room temperature for 5 minutes. 
    - Place the tubes on the magnet for 5 minutes. 
    - Wash the beads twice with 200µl 80% EtOH (freshly made).
    - Remove and discard the EtOH, and air dry the pellet at room temperature for 10 minutes or until the pellet is no longer shiny. 
    - Resuspend the pellet in 10µL buffer RSB (resuspension buffer). Pipette up and down 10x to ensure the pellet is well resuspended. 
    - Place the tube back on the magnet to pellet the beads. Transfer the supernatant to a clean micro centrifuge tube, take care to ensure that no beads are transferred. 
5. Purify the product using AMPure XP beads: Size exclusion. 
    - Add 90µl buyer EB (or RSB) to the 10µl of eluted DNA. 
    - Add 70µl of Ampure XP beads (0.7x).
    - Incubate at room temperature for 5 minutes.
    - Place the tube on a magnet for 3-5 minutes. 
    - Wash beads twice with 200µL 80% EtOH. 
    - Remove and discard EtOH and air dry the pellet at room temperature for 10 mins or until the pellet is no longer shiny. 
    - Add 10µL of EB (elution buffer). Pipette up and down 10x to ensure the pellet is well resuspended. 
    - Place the tube back on the magnet for to pellet the beads. Transfer the supernatant to a clean micro centrifuge tube, take care to ensure that no beads are transferred. 

**Index Assignment**: [Here](https://www.illumina.com/documents/products/technotes/technote-nextera-rapid-capture-low-plex-pooling-guidelines.pdf) is a guide for assigning indices and pooling. 

Here is an example Index assigment for 30 genomes (8 pooled segment each) and their assigned indices:

Genome ID | i5 (S5XX / threemid / white cap) | i7 (N7XX / fivemid / orange cap) | i5 sequence | i7 sequence |  
|---|---| ---| ---|---|
1 | 502 | 701 | ACTTAGCA |	TCGCCTTA |
2 | 502|	702	|ACTTAGCA|	CTAGTACG|
3|502|	703	|ACTTAGCA|	TTCTGCCT|
4|502	|704	|ACTTAGCA|	GCTCAGGA|
5|502|	705	|ACTTAGCA	|AGGAGTCC|
6|503|	706|	AGAGAACA|	CATGCCTA|
7|503	|707|	AGAGAACA	|GTAGAGAG|
8|503|	710	|AGAGAACA	|CAGCCTCG|
9|503	|711|	AGAGAACA|	TGCCTCTT|
10 |503|	712	|AGAGAACA	|TCCTCTAC|
11|505|	714	|TCGATTAG|	TCATGAGC|
12|505|	715	|TCGATTAG	|CCTGAGAT
13|505|	701|	TCGATTAG|	TCGCCTTA|
14|505|	702	|TCGATTAG	|CTAGTACG|
15|505|	703	|TCGATTAG|	TTCTGCCT|
16|506	|704	|TGTTCTAG|	GCTCAGGA|
17|506	|705	|TGTTCTAG	|AGGAGTCC|
18|506|	706	|TGTTCTAG|	CATGCCTA|
19|506|	707	|TGTTCTAG|	GTAGAGAG|
20|506|	710	|TGTTCTAG|	CAGCCTCG|
21|507|	711	|GGAACTTA|	TGCCTCTT|
22|507|	712	|GGAACTTA|	TCCTCTAC|
23|507|	714	|GGAACTTA|	TCATGAGC|
24|507|	715	|GGAACTTA|	CCTGAGAT|
25|507	|701	|GGAACTTA	|TCGCCTTA|
26|508|	702	|TAGGTCTA|	CTAGTACG|
27|508	|703|	TAGGTCTA|	TTCTGCCT|
28|508	|704|	TAGGTCTA|	GCTCAGGA|
29|508|	705	|TAGGTCTA|	AGGAGTCC|
30|508|	706	|TAGGTCTA|	CATGCCTA|

** If you have segments that are very low concentration or not detectable by Qubit (<0.05 ng/µl), you can tagement them separately. Just input 5µl into the tagmentation step and, if needed, bump up PCR cycles to 25x. Then you can pool individual low-concentration samples with their genomes following tagmentation and indexing. 

## Quality control: Qubit and BioAnalyzing 

**Materials**
- Qubit hsDNA Kit: ThermoFisher Q32854 
- hsDNA BioAnalyzing: Agilent 5067-4627

**Protocol** 
1. Quantify each sample after you complete tagmentation, indexing and bead cleanups. Use manufacturer protcol -- hsDNA Qubit. Quantify in ng/µl. 
2. BioAnalyze to determine average fragment length according to hsDNA Agilent Protocol, outlined briefly below: 
    - Allow all reagents to come to room temperature for 30 mins before use.
    - Make fresh gel-dye (add 15µl of blue dye to red tube, vortex, and spin filter at 22,000 rpm +/- 10% for 15 mins). This is good for 6 weeks after it is made. 
    - Add 9µl of gel-dye to "G" well. Plunge syringe, starting at 1mL, slowly and steadily. Lock into lowest position for 60 seconds, then release, plunger to pop up to at least 0.4ml (if not you probably didn't generate enough pressure to fill microfluidic channels).
    - Add 9µl of gel-dye to other gel wells (n=3). 
    - Add 5µl of marker (green tube) to all other wells, including the ladder well. 
    - Add 1µl of ladder sample (yellow tube) to ladder well. 
    - Add 1µl of sample to sample wells (n=11). If samples are very concentrated (>5ng if amplicon seq or >30ng if tagementation seq) dilute so you don't drown out marker signal. 
    - Run according to hsDNA Agilent protcol and extract average fragment length of peak. 
    - Average fragment should be 500 - 800 bps. If average fragment is higher than this, you might have trouble getting efficient clustering. 
    - Look for samples with low-peaks. This might be primer dimer and may indicate the sample needs to be cleaned up again, either by bead cleanup or gel extraction. 

`You can probably stop at this stage if you are sending your samples off to be sequenced, other wise I have outlined the basic steps of loading an Illumina sequencing run below.`

3. Pool samples equimolarly to make a 4nM pool. There are many ways of doing this. We use an Excel sheet to assist with these calculations and are happy to share this sheet if it would be helpful to anyone. [Here](https://support.illumina.com/content/dam/illumina-support/documents/documentation/system_documentation/miseq/miseq-denature-dilute-libraries-guide-15039740-10.pdf) is Illumina's Denature and Dilute Library Guide. 
4. We usually confirm that the final pool is within 10% of 4nM by repeating Qubiting (and possibly BioAnalyzing if you are worried) of the final pool: (concentration in ng/µl) \ ((660g/mol)(average size (bp)) * 1,000,000 = final pool nM 

## Loading a sequencing library on the Illumina MiSeq 

**Materials**
- MiSeq Reagent Kit v3 (600 cycle): Illumina MS-102-3003 (this is a good option, but the v2 2x150 or 2x250 options will also work well)
- PhiX Control v3: Illumina FC-110-3001
- NaOH, freshly diluted to 0.2N: standard
- Tris-HCl, pH 8.5, 0.1% tween 20: FisherScientific Teknova T7724

**Protocol**

The below protcol is to prep at 16pM library spiked with 1% PhiX. This will need to be adjusted depending on sequencing chemistry, library type etc. 

In general, bumping up the loading concentration will increase yield, but at the cost of read quality. 1% PhiX is typically sufficient for fragmentation-based libraries, but may need to be increased substantially when sequencing amplicon libraries or libraries that will be low diversity. 

[Here](https://www.illumina.com/content/dam/illumina-marketing/documents/products/other/miseq-overclustering-primer-770-2014-038.pdf) and [here](https://genohub.com/loading-concentrations-optimal-cluster-density/) are PDFs outlining Illumina's notes on optimizing cluster density. 

1. Dilute freshy NaOH - 800µl ultrapure water + 200µl 1.0N to achieve 0.2N NaOH. Invert the tube to mix. 
2. Prep PhiX
    - Create 4nM PhiX control in 5ul 
        - 2ul of 10nM PhiX control (from Illumina tube) + 3ul of 10mM Tris-HCl, pH 8.5, with 0.1% tween 20
    - Denature 4nM PhiX control 
        - 5ul 4nM PhiX library + 5ul 0.2N NaOH @ 5 mins @ room temp 
    - Create 20pM library 
        - Add 990ul HT1 = 1ml of 20pM PhiX library 
    - Create 16pM PhiX library 
        - 480ul 20pM PhiX + 120ul HT1 = 600ul 16pM PhiX 
3. Prep Library
    - Pool 4nM library in 250µl (see “sample sheet slide”). Bring up final volume with RSB, not water. Pipetted >1µl of each sample. Qubit the final library to ensure that you created a 4nM library. 
    - Denature 4nM library
    - 5µl of 4nM library + 5µl 0.2N NaOH @ 5 mins @ room temp
    - Create 20pM library
        - Add 990µl cold HT1 to 10µl denatured library = 1ml of dilute denatured library 
    - Create 16pM library 
        - 480µl 20pM library + 120µl cold HT1 = 600µl of 16pM library 
4. Prep final library (16pM with 30% PhiX control) 
    - 6µl 16pM PhiX + 594ul 16pM library = 600µl 16pM library + 1% PhiX control 
5. Load 600µl into loading well of cartridge. 
