# CMV_UL54 QPCR Protocol
## Materials needed:
Express QPCR Supermix Universal (LifeTechnologies catalog # 11785-200)

CMV_UL54 PrimeTime assay mix

DEPC water

QPCR reaction plate

## QPCR Reaction Set-up

1. Clean workspace thoroughly before beginning QPCR set-up
2. Prepare the following master mix according to the chart, making enough mix for each sample and standard to be tested in duplicate:

    Reagent | Stock concentration | Volume for 20 ul rxn | 40 x mix
    --- | --- | --- | ---
    CMV_UL54 PrimeTime mix | 20x | 1 ul | 40 ul
    QPCR Supermix Universal | 2x | 10 ul | 400 ul
    DEPC water | - | 4 ul | 160 ul
    Sample DNA | - | 5 ul | -

3. Prepare the CMV DNA standards as per CMV_standard_preparation protocol
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

