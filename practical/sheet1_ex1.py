import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# number of iterations to run MCMC


# set p as the posterior distribution (the distribution we want to sample from)


# initial condition
x = []


# iterate
for step in :
	# propose a step
	d = np.random.

	# calculate the ratio of posterior probabilities
	ratio =

	if ratio > 1.:
		# accept the new step
	else:
		# accept with probability = ratio