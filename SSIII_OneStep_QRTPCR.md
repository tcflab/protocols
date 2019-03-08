# SuperScript III One-step VL QRT-PCR Protocol

## Author: Andrea Weiler
## Date: Feburary 28, 2019

### Materials needed:
RNase-out (Lifetechnologies 10777-019)

Superscript III Platinum One-step QRT-PCR kit (Lifetechnologies  11732088)

RNase-free non-stick tubes (Lifetechnologies AM12350)

2 ml microcentrifuge tubes

DEPC treated water

Assay specific in vitro transcript (IVT)

Assay specific primers and probe 

Lightcycler 480 multiwell plate 96 with sealing foil (Roche 04729692001)

LightCycler 480 or LC96

## **Method**

1. Clean workspace thouroughly with 10% bleach
2. Label 2 ml tubes for the master mix and water. 
3. Add RNase-out to DEPC trated water at a 1:100 dilution. Using 6.5 ul RNase-out in 650 ul DEPC water is plenty for this protocol.
4. Label 10 non-stick tubes to be used for the standards, and add RNase-out treated water according to chart below.

Label | 0 | 1 | 2 | 3 | 4| 5 | 6 | 7 | 8 | 9
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Purpose | 1st dilution | STD 1 | STD2 | STD 3 | STD4 | STD 5 | STD 6 | STD 7 | STD 8 | STD 9
___ | discard | 1.50E+07 | 1.50E+06 | 1.50E+05 | 1.50E+05 | 1.50 E+03 | 1.50E+02 | 1.50E+01 | 5.00E+00 | 3.00E+00
Volume water | 45 ul | 45 ul | 45 ul | 45 ul | 45 ul | 45 ul | 45 ul | 45 ul | 10 ul | 20 ul 
5. Prepare appropriate volume of master mix according to chart. Make enough master mix for the number of samples being tested + standards + 10%. ( Remember that we typically test both samples and standards in duplicate)

Reagent | Concentration | 20 ul reaction 
--- | --- | ---
RNase-out treated DEPC water |   _____    | 2.6 ul
Reaction buffer | 2x * | 10.8 ul
Primer/random hexamer mix | 20 uM each primer, 250 ug/ml hexamer | 0.6 ul
Probe | 10 uM | 0.2 ul
SSIII enzyme mix |    _____  | 0.8 ul
RNA template | | 5 ul

 *The 2x reaction buffer comes with magnesium sulfate at a concentration of 6 mM. The final concentration of salt is assay dependent. Both our SIV and ZIKV VL assays require additional magnesium sulfate, with the 2x buffer containing 10 mM magnesium.

6. Prepare a 1:10 dilution series to make standards 1-7. Add 5 ul of the IVT stock (3e8 copies/ul) to the tube labeled **0**. Using a p100 or p200 pipet up and down 8 - 10 times to mix, then transfer 5 ul from tube **0** to tube **1**. Mix this tube the same way and continue this dilution series to tube **7**. Tubes **8** and **9** are both 5 ul dilutions from tube **7**.

7. Distribute 15 ul of the master mix to each well being using on the 96 well Lightcycler plate.

8. Add 5 ul of the standards and each sample to the appropriate wells of the plate. 

9. Cover plate with sealing foil. Be sure to use roller to make sure the seal is applied well. 

10. Briefly centrifuge plate to make sure all components are in the bottom of the well. 

11. Run plate on LC96 or LC480 with the following cycling conditions:

* Make sure the instrument is set to collect data in the correct channel. Most commonly this is the Fam channel (~560nm)

Step | Cycles | Temperature | Duration | Ramp rate
--- | --- | --- | --- | ---
Reverse transcription | 1 | 37C | 15 minutes | 4.4C/sec
| | | 50C | 30 minutes | 4.4C/sec
Activation | 1 | 95C | 2 minutes | 4.4C/sec
Amplification | 50 | 95C | 15 seconds | 3C/sec
| | | 62C* | 1 minute | 2.2C/sec
Cool | 1 | 37C | 30 seconds | 2.2C/sec

*the annealing temperature is assay specific
