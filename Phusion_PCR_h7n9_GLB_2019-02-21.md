# Phusion PCR h7n9 samples
## Date 2/21/2019
## Author - Gabrielle Barry

## Purpose
* The purpose of this protocol is to amplify gene segments from H7N9 samples from Yoshi's lab so they can be sequenced. 

## Materials
* Phusion High-Fidelity PCR Master Mix (NEB #50994945)
* forward and reverse primers for each segment
* DEPC H2O
* 0.2 ml TempAssure PCR 8-Tube flex-free strips (Fisher Scientific NC9989922)

## Protocol
1. Thaw Phusion and keep on ice
2. Label tubes prior to making master mixes
3. Prepare one master mix per segment (over ice if possible), and aliquot
4. Aliquot cDNA
5. Pipette up and down to mix

Per each Segment 8x| 1x (ul) | MM 9x (+10% extra) | MM 10x (+10% extra)
|---|---|---|---|
2x Phusion MM | 10 | 99 | 110
PCR_fwd (10uM) | 1 | 9.9 | 11
PCR_rev (10uM) | 1 | 9.9 | 11
cDNA | 2 | Add individually | Add individually |
Water | 6ul | 59.4 | 66

    Total Reaction Volume: 18ul MM in each tube. Add 2ul cDNA to bring the total reaction volume to 20ul. 

## Cycling Conditions
Per each Segment | Temp C | Time 
|---|---|---|
Initial denaturation | 98 | 30 seconds
x35 (denature, anneal, extend) | 98 | 10 seconds
| | xx | 30 seconds
| | 72 | 120 seconds
Final Extension | 72 | 5 minutes
Hold | 4 | forever

Segment | Primers | Expected Amplicon Length | Thermocycler, number, row | Annealing Temp C
|---|---|---|---|---|
PB2 | speH7N9-PB2-F, speH7N9-PB2-R | ~2280 | thermocycler 3, rows 1-2 | 68
PB1 | speH7N9-PB1-F, speH7N9-PB1-R | ~2274 | thermocycler 3, rows 5-12 | 72
PA | speH7N9-PA-F3, PA-u13+20R | ~2151 | thermocycler 3, rows 5-12 | 72
HA | speH7N9-HA-F2, speH7N9-HA-R2 | ~1695 | thermocycler 3, 3-4 | 71
NP | speH7N9-NP-F, speH7N9-NP-R | ~1497 | thermocycler 1, rows 5-6 | 61
NA | speH7N9-NA-F, speH7N9-NA-R | ~982 | thermocycler 1, 7-8 | 63
M | speH7N9-M-F, speH7N9-M-R | ~982 | thermocycler 1, rows 1-2 | 51
NS | speH7N9-NS-F2, speH7N9-NS-R2 | ~838 | thermocycler 1, rows 9-12 | 64

## Primers
Primer | Sequence (5'-3') | Orientation | Purpose
|---|---|---|---|
speH7N9-PB2-F | AGCGAAAGCAGGTCAAATATATTCAAT | Forward | Primers for GD/3 PB2 Segment
speH7N9-PB2-R | AGTAGAAACAAGGTCGTTTTTAAACAAT | Reverse
speH7N9-PB1-F | AGCGAAAGCAGGCAAACCATTTGA | Forward | Primers for the GD/3 PA Segment
speH7N9-PB1-R | AGTAGAAACAAGGCATTTTTTCATGAAGG | Reverse | 
speH7N9-PA-F3 | AGCGAAAGCAGGTACTGATTCAAAATG | Forward | Primers for the GD/3 PA segment
PA-u13+20R | AGCGAAAGCAGGTACTGATTCAAAATG | Reverse | 
speH7N9-HA-F2 | AGCAAAAGCAGGGGATACAAAATG | Forward | Primers for the GD/3 HA segment
speH7N9-HA-R2 | AGCAAAAGCAGGGGATACAAAATG | Reverse | 
speH7N9-NP-F | AGCAAAAGCAGGGTAGATAATCACTCAC | Forward | Primers for the GD/3 NP segment
speH7N9-NP-R | AGTAGAAACAAGGGTATTTTTCT | Reverse | 
speH7N9-NA-F | AGCAAAAGCAGGGTCAAG | Forward | Primers for the GD/3 NA segment
speH7N9-NA-R | AGTAGAAACAAGGGTCTTTTTCTTC | Reverse | 
speH7N9-M-F | AGCAAAAGCAGGTAGATGTTTAAAG | Forward | Primers for the GD/3 M segment
speH7N9-M-R | AGCAAAAGCAGGTAGATGTTTAAAG | Reverse | 
speH7N9-NS-F2 | AGCAAAAGCAGGGTGACAAAAACATAATG | Forward | Primers for the GD/3 NS segment
speH7N9-NS-R2 | AGCAAAAGCAGGGTGACAAAAACATAATG | Reverse | 