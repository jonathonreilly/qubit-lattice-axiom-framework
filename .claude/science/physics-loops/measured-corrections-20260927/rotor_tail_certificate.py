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

if __name__=='__main__':
    for delta in (F(1),F('31.607246')):
        K=F(1);L=20;n=np.arange(-L,L+1,dtype=float)
        proposals=eigh_tridiagonal(4*n*n-4*float(delta),np.full(2*L,-2*float(delta)),select='i',select_range=(0,6),tol=1e-12)[0]
        radius=F(1,10**9);intervals=[]
        for j,E in enumerate(proposals):
            lo=F(str(E))-radius;hi=F(str(E))+radius
            assert (count_below(L,K,delta,lo),count_below(L,K,delta,hi))==(j,j+1)
            intervals.append((lo,hi))
        print(json.dumps(dict(K=str(K),delta=str(delta),L=L,energy_intervals=[[str(a),str(b)] for a,b in intervals],gap_intervals=[[str(a-intervals[0][1]),str(b-intervals[0][0])] for a,b in intervals[1:]],maximum_energy_width=str(2*radius),maximum_gap_width=str(4*radius))),flush=True)

AUDIT_TIMEOUT_SEC = 180
