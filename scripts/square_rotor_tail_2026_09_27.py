"""Exact inertia brackets for infinite rotor via bounded boundary self-energy."""
from fractions import Fraction as F
import json
from scipy.linalg import eigh_tridiagonal
import numpy as np

def finite_count(L,K,delta,E,beta):
    negative=0;pivot=None
    for n in range(-L,L+1):
        v=4*K*n*n-4*delta-E-(beta if abs(n)==L else 0)
        if pivot is not None:v-=4*delta*delta/pivot
        if v==0:raise ArithmeticError('Zero pivot; endpoint must change')
        pivot=v;negative+=v<0
    return negative

def count_below(L,K,delta,E):
    tail=4*K*(L+1)**2-8*delta
    if E>=tail:raise ValueError('Tail positivity not established')
    beta=4*delta*delta/(tail-E)
    lower=finite_count(L,K,delta,E,F(0))
    upper=finite_count(L,K,delta,E,beta)
    if lower!=upper:raise ValueError(('Boundary enclosure inconclusive',lower,upper))
    return lower
