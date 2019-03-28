# In Vitro Transcript Production Protocol

### Author: Andrea Weiler
### Date: 2019-03-26

### Purpose: This is a protocol for producing in vitro transcribed RNA to be used as a standard for QRT-PCR assays. This protocol assumes that you have your sequence of interest in a plasmid containing an appropriate transcription start site. You will also need to know the exact sequence of the transcript from the transcription start site to the restriction site used to linearize the plasmid.

## Materials needed:
Proteinase K, 4mg/ml (Sigma-Aldrich P2308)

15% SDS

Phenol/chloroform/isoamyl alcohol 24:24:1 (Fisher Scientific AAJ60331AE)

Chloroform (Sigma-Aldrich 132950)

Pellet paint NF co-precipitant (Novagen/EMD 70748)

3M NaOAc, pH 5.2

100% Ethanol - molecular grade

70% Ethanol - molecular grade

Isopropanol

RNase-Out (Lifetechnologies 10777-019)

MEGAscript T7 (or appropriate kit for your plasmid's start site) Kit (Lifetechnologies 1333)


# Procedure

## Restriction Digest (to linearize plasmid)
1. Digest ~ 2 ug plasmid using a an enzyme that only cuts once in the plasmid, downstream of your sequence of interest. Perform digest using recommended conditions for your enzyme in 30 ul total volume
2. To ensure that digest is complete incubate digest at reaction temperature for 4 hours, then inactivate enzyme if it is susceptible to heat inactivation
3. Confirm that digest was complete by running 5 ul of digest on a 1% agarose gel, alongside uncut plasmid

*It is critical that digest is complete in order to accurately quantify RNA that is produced
4. Add 1 ul of 15% SDS and 1 ul of Proteinase K to restriction digest
5. Incubate digest at 50C for 30 minutes

## Phenol/Chloroform Extraction and Ethanol Precipitation
1. To make digest easier to work with, add 175 ul DEPC water to product, giving a 200 ul sample
2. Add 200 ul phenol/chloroform and vortex on high for 1 minute
3. Spin sample at full speed in a microcentrifuge for 2 minutes
4. Transfer upper aqueous layer to a fresh tube. **when doing these phenol chloroform extractions it is critical to only transfer the upper layer and not carry over any of the organic layer**
5. Add 200 ul chloroform and vortex on high for 1 minute
6. Spin again at full speed for 2 minutes
7. Transfer upper aqueous layer to another fresh tube
8. Thaw pellet paint and allow to warm to room temp
9. Add 2 ul pellet paint to sample, followed by 0.1 volume (~20 ul) 3 M NaOAc, pH 5.2
10. Add 2 volumes (400 ul) of 100 % EtOH.
11. Vortex briefly and incubate at room temp for 2 minutes
12. Pellet DNA by spinning at top speed in a microcentrifuge for 5 minutes
13. Remove the supernatant without disturbing the dark blue pellet
14. Wash pellet with 1 ml 70 % EtOH, vortex briefly and spin as in step 12
15. Remove supernatant and wash with 100 % EtOH, vortexing and spinning again for 5 minutes
16. Remove supernatant and allow pellet to dry
17. Re-suspend the pellet in 22 ul DEPC water

## Transcription Reaction 
1. Thaw the frozen reagents for the reaction, place the enzyme mix on ice
2. Once reaction buffer is thawed, vortex well to made sure it is completely in solution
3. Once thawed, spin down the ribonucleotides and place them on ice
4. Assemble transcription reaction at room temp, adding reagents according to the table:

Component | |Volume
--- | --- | ---
ATP solution | | 2 ul
CTP solution | | 2 ul
GTP solution | | 2 ul
UTP solution | | 2 ul
10x reaction buffer | | 3 ul
~ 1 ug linear DNA template | | X ul
DEPC water | | 17 - X ul
Enzyme mix | | 2 ul

**Total reaction volume:            30 ul**

5. Mix thoroughly by pipetting up and down gently then spin briefly to collect reaction at bottom of the tube
6. Incubate reaction at 37C for 4 hours
7. Briefly spin down reaction to remove droplets from lid, then add 1 ul Turbo DNase and mix well
8. Incubate at 37C for an additional 15 minutes
9. Stop reaction by adding 115 ul DEPC water and 15 ul ammonium acetate stop solution and mix thouroughly

## RNA Clean up: Phenol/Chloroform extration and Isopropanaol precipitation

1. Add equal volume phenol/chloroform (160 ul) to reaction
2. Vortex on high for 1 minute
3. Spin at top speed in a microcentrifuge for 2 minutes
4. Transfer the upper aqueous layer to a fresh tube 
5. Repeat steps 1-4
6. Add equal volume chloroform (160 ul) 
7. Vortex 1 minute on high
8. Spin at top speed in a microcentrifuge for 2 minutes
9. Transfer upper aqueous layer to a new tube
10. Add equal volume (160 ul) isopropanol
11. Mix and let sit at room temperature for 2-5 minutes
12. Spin at top speed in microcentrifuge for 10 minutes
13. Remove supernatant using a pipet and dissolve pellet in 100 ul RNase-out treated water

## Calculate the concentration of the transcript
1. Use spectrophotometer to measure A260 (three times) 
2. Use Qubit High Sensitivity RNA kit to confirm the concentration of the transcript
3. Use the following equation to determine the copy equivalents/ul: 
 
 Copy Eq/µl= (concentration in ng/µl)(6.022 × 1023 copy Eq/mol)/(molecular weight in g/mol)(1 × 109 ng/g) 

 Note: we determine the mass of the transcript using the exact sequence and an online calculator. A good one is provided by Northwestern U. : http://biotools.nubic.northwestern.edu/OligoCalc.html

 ## Further characterization of the transcript
 1. In addition to quantifying the IVT we also use the Bioanalyzer to confirm that there is a single band at approximately the correct use. Use the RNA 6000 Pico kit to test the undiluted transcript, following instructions in the kit. This will show the size of the RNA and should confirm that all of the RNA is a single size (do not trust the quantification from the bioanalyzer).
 2. We test the IVT by QRT-PCR. Be sure to test multiple independent dilution series in duplicate.

