"""Exact inertia enclosures of the form-defined infinite H0+xH1, 0<=x<1/4."""
from fractions import Fraction as F
import json
import numpy as np
from scipy.linalg import eigh_tridiagonal

def coefficients(n,K,delta,x):
    return 4*K*(1-2*x)*n*n-4*delta*(1-2*x), -2*delta*(1-2*x)+4*K*x*n*(n+1)

def count_below(L,K,delta,x,E):
    if not 0<=x<F(1,4):raise ValueError('Outside form-coercive interval')
    tail=4*K*(1-4*x)*(L+1)**2-8*delta
    if E>=tail:raise ValueError('Tail not positive')
    boundary=coefficients(L,K,delta,x)[1];beta=boundary**2/(tail-E)
    counts=[]
    for shift in (F(0),beta):
        neg=0;pivot=None
        for n in range(-L,L+1):
            d,_=coefficients(n,K,delta,x);v=d-E-(shift if abs(n)==L else 0)
            if pivot is not None:v-=coefficients(n-1,K,delta,x)[1]**2/pivot
            if v==0:raise ArithmeticError('Zero pivot')
            pivot=v;neg+=v<0
        counts.append(neg)
    if counts[0]!=counts[1]:raise ValueError(('Tail sandwich inconclusive',counts))
    return counts[0]

if __name__=='__main__':
    for delta in (F(1),F('31.607246')):
      for S in (20,50,120):
        K=F(1);x=delta/(S*(S+1));L=30
        diag=[float(coefficients(n,K,delta,x)[0]) for n in range(-L,L+1)]
        off=[float(coefficients(n,K,delta,x)[1]) for n in range(-L,L)]
        proposal=eigh_tridiagonal(diag,off,select='i',select_range=(0,6),tol=1e-12)[0]
        intervals=[]
        for j,v in enumerate(proposal):
            a=F(str(v))-F(1,10**9);b=F(str(v))+F(1,10**9)
            assert (count_below(L,K,delta,x,a),count_below(L,K,delta,x,b))==(j,j+1)
            intervals.append((a,b))
        print(json.dumps(dict(S=S,K=str(K),delta=str(delta),x=str(x),L=L,energy_intervals=[[str(a),str(b)] for a,b in intervals],gap_intervals=[[str(a-intervals[0][1]),str(b-intervals[0][0])] for a,b in intervals[1:]])),flush=True)
