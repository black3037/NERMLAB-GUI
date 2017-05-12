from __future__ import division
import numpy as np
"""
Copyright Derek Black 2016

Required Modules:
Numpy
Itertools

Topics include:
Gradient Decent
Linear Regression
Cost Functions
Normal Equations

This module is for single and  multi-variant problems.
It utilzies two methods: Gradient Decent to Optimize the cost function
and normal equations to automatically find the optimized thetas for 
a minimized cost function.

How to use iLinearRegression:
iLinearRegression is an iterative method for solving linear regression problems.
The i in LinearRegression stands for iterative.
iLinearRegression utilizes a method called Gradient Decent to find values of theta
for a minimized cost function. The function returns the optimized values of theta.
This function is for single variant systems.
	
Ex. theta = iLinearRegression([1,2,3],[10,12,15],1500,alpha=0.4)
The returned values can now be used in the equation 'y= theta0 + theat1*x' for
the appropriate best fit linear model.

LinearRegression is a normal equation based linear regression method that works for multi-variant systems.
The user inputs his training sets of size m, as well as the out y.
The function will return a list of optimized thetas.

"""

def hypothesis(t0,t1,x,y):
    return (t0 + t1*x - y)

# Define the cost function
def costfunction(x, y, theta):
    # Training examples
    m = x.shape[0]
    # Compute the cost
    cost = (1./(2*m))*(x*theta-y).T*(x*theta-y)
    
    return cost.flat[0]


def iLinearRegression(x, y, theta, iteration, alpha):
    # Allocate empty lists to iterate over
    theta_iter = [] 
    cost_iter = []  
    
    m = x.shape[0] # Training size

    # Loop over number of iterations to calculate optimal thetas and cost
    for i in range(iteration):
        #update theta
        theta = theta-(alpha/m)*x.T*(x*theta-y)
        theta_iter.append(theta)
        cost_iter.append(costfunction(x,y,theta))

    return theta
				
def LinearRegression(*argv):
	import numpy as np
	from numpy.linalg import inv
	from itertools import chain
	
	"""
	To use LinearRegression, enter your training data x, and output y (type: list)
	ex. LinearRegression(x1,x2,x3,x4........,xn,y)
		where x and y = [data]

	"""
	
	# Initialize Variables
	ones = []
	popmat = []
	
	# Generate ones vector for x0, training setting data column 1
	for i in range(len(argv[0])):
		ones.append(1)
		
	popmat.append(ones)
	
	# *************************************************************************
	# Gather features and output from user to matrix
	# *************************************************************************
	i = -1
	for arg in argv:
		i += 1
		popmat.append(arg)
		if i == (len(argv) - 2):
			break
		
	# Convert x and y matricies to proper dimenions
	y = np.transpose(np.matrix(argv[-1]))		
	x = np.transpose(np.matrix(popmat))
	
	# Calculate the optimal thetas
	thetas = inv(np.transpose(x)*x)*np.transpose(x)*y
	
	convth = thetas.tolist()
	optimized_thetas = list(chain.from_iterable(convth))

	
	return optimized_thetas
