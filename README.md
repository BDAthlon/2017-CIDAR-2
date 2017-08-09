# 2017-CIDAR-2

This is a simple program that allows one to attempt to create a biochemical model using user-input initial concentrations and reaction constants, in order to hit particular regions in the concentration vs. time plot of the product concentration.

As of now, the UI is still based in the command line interface, with the user able to input not only the constants needed for the simulation to run, but also the number of circular regions they would like generated, as a sort of adjustable difficulty.

The simulations are currently constrained to only run for 40 seconds as a control, but this can easily be changed in future revisions.

The simulation model itself was made using an example on the PySB website as the base, while the rest was done using calls to matplotlib and NumPy functions.