#!/usr/bin/env python3
"""Exact certificate for the non-geometric counterexample in the paired note."""
from itertools import product
from pathlib import Path
import json
import sympy as sp

D=(1,1,2,3)
JUMPS=((0,1,1,-1),(1,-1,0,0),(1,0,1,-1),(1,1,-1,0))
WEIGHTS=(3,1,1,3)

def matrix(q):
    states=[v for v in product((-1,0,1),repeat=4) if sum(x*y for x,y in zip(D,v))==q]
    index={v:i for i,v in enumerate(states)}
    H=sp.diag(*(sp.Rational(sum(x*x for x in v),5) for v in states))
    for j,w in zip(JUMPS,WEIGHTS):
        assert sum(x*y for x,y in zip(D,j))==0
        for i,v in enumerate(states):
            for sign in (-1,1):
                target=tuple(x+sign*y for x,y in zip(v,j))
                k=index.get(target)
                if k is not None:H[k,i]-=w
    assert H==H.T
    return states,H

def main():
    states0,H0=matrix(0);states1,H1=matrix(1)
    threshold=-sp.Rational(137,20)
    positive=H0-threshold*sp.eye(len(states0))
    minors=[positive[:i,:i].det() for i in range(1,len(states0)+1)]
    assert all(x>0 for x in minors)
    v=sp.Matrix([4,4,1,3,5,5,3,5,3])
    norm=(v.T*v)[0]; numerator=(v.T*H1*v)[0]; rayleigh=numerator/norm
    assert rayleigh < threshold
    # Independent direct sum over edges checks the quadratic-form value.
    direct=sum(sp.Rational(sum(a*a for a in s),5)*v[i]**2 for i,s in enumerate(states1))
    for i,s in enumerate(states1):
        for j,w in zip(JUMPS,WEIGHTS):
            target=tuple(x+y for x,y in zip(s,j))
            if target in states1:direct-=2*w*v[i]*v[states1.index(target)]
    assert direct==numerator
    result={'scope':'supplied non-geometric four-coordinate system only',
            'd':D,'jumps':JUMPS,'weights':WEIGHTS,'zero_states':states0,'charged_states':states1,
            'zero_shift_leading_minors':list(map(str,minors)),
            'threshold':str(threshold),'trial_vector':list(map(int,v)),
            'trial_squared_norm':str(norm),'trial_numerator':str(numerator),
            'charged_rayleigh':str(rayleigh),'strict_margin':str(threshold-rayleigh),
            'result':'E(charge=1) < E(charge=0), by positive definiteness and a variational trial'}
    Path(__file__).with_name('BLOCK2_EXACT_SECTOR_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
