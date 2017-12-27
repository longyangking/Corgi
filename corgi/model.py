# Definition of model based on Hamiltonian dynamics

import numpy as np 
from .simulation import simulation

class Hamiltonian:
    '''
    The dynamic description of system is based on Hamiltonian definition
    '''
    def __init__(sel,energy,np,nq,nr,randomfuns=None):
        self.energy = energy  # the function to define the system energy

        self.nq = nq    # number of generalized momentum
        self.np = np    # number of generalized positions
        self.nr = nr    # number of random coefficients

        self.randomfuns = randomfuns

    def montecarlo(self):
        pass