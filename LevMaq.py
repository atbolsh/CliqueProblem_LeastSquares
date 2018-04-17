import math
from copy import deepcopy

import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv
from numpy.linalg import svd
from numpy.linalg import norm

from scipy.optimize import least_squares

import matplotlib.pyplot as plt


#Just fills the main diagonal
def graphToH(G):
    """For a connectivity matrix G, returns the corresponding H2."""
    H2 = deepcopy(G)
    np.fill_diagonal(H2, 1)
    return H2

#Gets the prototypical error matrix.
def getM(H2):
    """Matrix of all the holes"""
    return np.ones(H2.shape) - H2

def getm(H2):
    """returns ones of the right size"""
    return np.ones(H2.shape[0])

#Useful for norms below 2.
def ReLu(x):
    """Rectified Linear Unit"""
    return np.maximum(x, 0)


#We keep the vectors normalized, to avoid falling into the origin.
#This one traps y on the unit sphere.
def renormL2(y):
    return y/norm(y)

#This one traps y on the unit cube.
def renormCube(y):
    return y/np.max(np.fabs(y))


def projection(a, b):
    """Compute the projection of a onto b."""
    d = np.dot(a, b)
    s = np.sum(b*b)
    return b*d/s

def energy(x, M, n = 1):
    return np.sum((np.outer(x, x)*M)**n)


def seek(x, H2, target, n = 1, cutoff=1e-6):
    """The main loop"""
    M  = getM(H2)
    m  = getm(H2)
    N = H2.shape[0]
    errors = []
    u = np.sqrt(target)
    # The thing to set to 0. We have error, renormalization, and target clique size.
    F = lambda y : np.array([energy(y, M, n), 0.5*np.sum(y*y) - 0.5, u*np.sum(y) - target])
    # Jacobian
    J = lambda y : np.vstack((n*(y**(n-1))*np.matmul(M, y**n), y, u*np.ones(N)))
    z = least_squares(F, x, gtol=cutoff, xtol=cutoff, ftol=cutoff)
    print z
    return z.x


