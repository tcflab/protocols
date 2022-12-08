# SPV_RhPV QPCR Protocol
## Materials needed:
Taqman Fast Advanced Master Mix (LifeTechnologies catalog # 444457)

Assay specific DNA standard and primers and probe (see below)

DEPC water

QPCR reaction plate

## QPCR Reaction Set-up

1. Clean workspace thoroughly before beginning QPCR set-up
2. Prepare the following master mix according to the chart, making enough mix for each sample and standard to be tested in duplicate:

    Reagent | Stock concentration | Volume for 20 ul rxn | 40 x mix
    --- | --- | --- | ---
    Forward primer | 10uM | 1 ul | 40 ul
    Reverse primer | 10uM | 1 ul | 40 ul
    Probe primer | 10uM | 0.4 ul | 16 ul
    Taqman Fast Advanced MM | 2x | 10 ul | 400 ul
    DEPC water | - | 2.6 ul | 104 ul
    Sample DNA | - | 5 ul | -

3. Prepare a 1:10 dilution series of the DNA standard as described in the CMV_standard_preparation protocol
4. Aliquot 15 ul master mix to each well that will be used in the reaction plate
5. Add 5 ul of the standards and negative control to the appropriate wells
6. Add 5 ul of each sample to the appropriate wells
7. Seal plate and spin down briefly before running on QPCR instrument
8. Run the following cycling conditions on the QPCR instrument 

    (Note: These conditions have been tested/optimized on LightCycler plate-based instruments. It is possible they may need to be adjusted for other instruments)

   Step | Number of cycles | Temperature | Time | Notes
   --- | --- | --- | --- | ---
   **Activation** | 1 | 95 C | 5 minutes | 
   **Amplification** | 50 | 95 C | 15 seconds | ramp rate = 3 C/second
    |  | | 60 C | 1 minute | ramp rate = 3 C/second
     |  | | 72 C | 1 second | ramp rate = 3 C/second, single acquisition
    **Cool** | 1 | 40 C | 30 seconds

## SPV QPCR assay reagents

*Note: this assay targets the 3’ region of the VP2 gene. All primer and probe sequences are listed from 5’-3’.*

SPV_3VP2_forward:
GAGCACGCTAACTGCTTGTTG

SPV_3VP2_reverse:
GCTGTTAGTGGTGGGAATGTG

SPV_3VP2_probe:
6-fam-ACAGGGTCTAGCATTAGCACAGCC-BHQ1

## RhPV QPCR assay reagents
*Note: This assay targets the VP2 gene. Primer and probe sequences are listed from 5'-3'.*

RhPV_forward:
GGAACGGGTAGCAGCATTAGT

RhPV_reverse:
TGAGAGACACCTTCTAGAGAC

RhPV_probe:
6-fam-ATCAGTTTCCCTCAGTGCAAGCCG-BHQ1