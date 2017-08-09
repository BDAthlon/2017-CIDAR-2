from pysb import *
from pysb.integrate import odesolve
from pylab import linspace, plot, xlabel, ylabel, show

import numpy as np
import matplotlib.pyplot as plt

# A simple model with a reversible binding rule

Model()

# Declare the monomers
Monomer('L', ['s'])
Monomer('R', ['s'])

# Declare the parameters
numCircles = int(raw_input("Enter the number of circles you want to try to hit\n"))
L0 = raw_input("Enter initial concentration of reactive species 1\n")
R0 = raw_input("Enter initial concentration of reactive species 2\n")
k_f = raw_input("Enter reaction forward rate constant\n")
k_r = raw_input("Enter reaction reverse rate constant\n")

Parameter('L_0', int(L0))
Parameter('R_0', int(R0))
Parameter('kf', float(k_f))
Parameter('kr', float(k_r))

# Declare the initial conditions
Initial(L(s=None), L_0)
Initial(R(s=None), R_0)

# Declare the binding rule
Rule('L_binds_R', L(s=None) + R(s=None) <> L(s=1) % R(s=1), kf, kr)

# Observe the complex
Observable('LR', L(s=1) % R(s=1) )

def generateCircles(circleCount):
	circles_coords = np.random.rand(circleCount, 2)
	circles_coords[:,0] *= 400
	circles_coords[:,1] *= 100
	fig, ax = plt.subplots()
	for i in range(circleCount):
		ax.add_artist(plt.Circle((circles_coords[i][0], circles_coords[i][1]), 10, color='green'))


if __name__ == '__main__':
    # Simulate the model through 40 seconds
    time = linspace(0, 400, 100)
    plt.figure()
    generateCircles(numCircles)
    print "Simulating..."
    x = odesolve(model, time)
    # Plot the trajectory of LR
    plot(time, x['LR'])
    xlabel('Time (seconds)')
    ylabel('Concentration of Product')
    show()