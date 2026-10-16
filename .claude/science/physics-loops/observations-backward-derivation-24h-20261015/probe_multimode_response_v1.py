#!/usr/bin/env python3
"""Finite passive adaptive-mode constraints; no empirical data."""
from pathlib import Path
import sympy as s
import numpy as np
import json,hashlib

def main():
    rows=[]
    def ck(n,b,**kw):
        assert bool(b),n
        rows.append(dict(name=n,passed=True,**kw))
    x1,x2,sp,sq=s.symbols('x1 x2 sp sq')
    mat=s.Matrix([[1/(sp-x1),1/(sq-x1)],[1/(sp-x2),1/(sq-x2)]])
    formula=-(x2-x1)*(sq-sp)/((sp-x1)*(sq-x1)*(sp-x2)*(sq-x2))
    ck('two-column Cauchy determinant sign',s.factor(mat.det()-formula)==0)
    q,w1,w2,g1,g2,C1,C2,k,lam=s.symbols('q w1 w2 g1 g2 C1 C2 k lam')
    V=k*q*q/2+C1*w1*w1/2+C2*w2*w2/2+g1*w1*q*q/2+g2*w2*q*q/2+lam*q**4
    square=C1*(w1+g1*q*q/(2*C1))**2/2+C2*(w2+g2*q*q/(2*C2))**2/2+k*q*q/2+(lam-g1*g1/(8*C1)-g2*g2/(8*C2))*q**4
    ck('multimode stability completion',s.expand(V-square)==0)
    xs=[s.Rational(1,5),s.Rational(4,5)];ys=[s.Rational(6,5),s.Rational(9,5)]
    pole_sets=[[],[(3,s.Rational(2,3))],[(3,s.Rational(2,3)),(5,s.Rational(3,7))],
               [(3,s.Rational(2,3)),(5,s.Rational(3,7)),(7,s.Rational(1,4))]]
    for modes in pole_sets:
        B=lambda x:s.Rational(7,5)-sum(a/(pole-x) for pole,a in modes)
        L=s.Matrix([[-(B(x)-B(y))/(x-y) for y in ys] for x in xs])
        pairs=0
        for i,(sp,ap) in enumerate(modes):
            for sq,aq in modes[i+1:]:
                pairs+=ap*aq*(xs[1]-xs[0])*(ys[1]-ys[0])*(sq-sp)**2/(s.prod((sp-x)*(sq-x) for x in xs)*s.prod((sp-y)*(sq-y) for y in ys))
        det=s.factor(L.det())
        ck('exact pole-pair determinant '+str(len(modes)),s.factor(det-pairs)==0 and (det==0 if len(modes)<2 else det>0),determinant=str(det))
        Ms=[sum(a/s.Rational(pole)**(n+1) for pole,a in modes) for n in [1,2,3]]
        variance=s.factor(Ms[0]*Ms[2]-Ms[1]**2)
        ck('nonconstant spectral moment constraint '+str(len(modes)),variance==0 if len(modes)<2 else variance>0)
    v,u=s.symbols('v u',real=True);b11,b12,b21,b22=s.symbols('b11 b12 b21 b22')
    L=s.Matrix([[b11,b12],[b21,b22]])
    ck('common real affine scale preserves determinant sign',s.expand((v*L).det()-v*v*L.det())==0)
    # Finite measurement uncertainty with shared point errors, no independence.
    rng=np.random.default_rng(1517);max_ratio=0.
    base=np.array([.2,.8,1.2,1.8]);B=lambda x:1.4-(2/3)/(3-x)-(3/7)/(5-x)
    true=np.array([B(x) for x in base]);eps=np.array([.001,.002,.0015,.0007])
    def lmat(values):
        return np.array([[-(values[i]-values[j+2])/(base[i]-base[j+2]) for j in range(2)] for i in range(2)])
    exact=lmat(true)
    e=np.array([[(eps[i]+eps[j+2])/abs(base[i]-base[j+2]) for j in range(2)] for i in range(2)])
    for j in range(200):
        measured=true+eps*rng.uniform(-1,1,4);lh=lmat(measured)
        E=abs(lh[0,0])*e[1,1]+abs(lh[1,1])*e[0,0]+e[0,0]*e[1,1]+abs(lh[0,1])*e[1,0]+abs(lh[1,0])*e[0,1]+e[0,1]*e[1,0]
        err=abs(np.linalg.det(lh)-np.linalg.det(exact));assert err<=E+1e-15
        max_ratio=max(max_ratio,err/E)
    ck('correlated point errors obey finite determinant certificate',True,controls=200,largest_error_to_bound_ratio=max_ratio)
    # A negative-residue two-pole response violates the passive-class sign.
    bad=lambda x:s.Rational(7,5)-s.Rational(2,3)/(3-x)+s.Rational(3,7)/(5-x)
    badL=s.Matrix([[-(bad(x)-bad(y))/(x-y) for y in ys] for x in xs])
    ck('negative-residue countercandidate violates sign',badL.det()<0)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK17_v1.md')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,
      'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
      'empirical_validation':False,
      'scope':'Necessary passive finite multimode adaptive response; no selected mode count, physical spectrum, periodic preparation or measured response derived.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
