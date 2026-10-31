#!/usr/bin/env python3
"""Labelled post-hoc narrower shells; original failed predicate is immutable."""
import json
import math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import i1e

u=40.; eps=.1; t=1.3*u; f=1/27
q=1-2*math.sin(.55)**2*math.sin(.37)**2
v=math.sqrt(1-q*q)
def raw(h,angular):
    lo,hi=2*math.asin((.45-h)/2),2*math.asin((.45+h)/2)
    x,w=leggauss(240); th=(hi+lo)/2+(hi-lo)*x/2
    c,s=np.cos(th),np.sin(th)
    radius=np.sqrt(1-2*f*(1-f)*(1-c)); z=t*radius
    logh=np.log(2*i1e(z)/z)+z
    base=np.exp(-u*(5*(1-c)+(1+eps)*(1-q*c))+t*(1-f+f*c)-logh)
    a=u*(1+eps)*v*s
    if angular:
        nz,nw=leggauss(160)
        orient=np.exp(-a[:,None]*nz[None,:])@(nw/2)
    else: orient=np.sinh(a)/a
    return float(np.sum(w*(hi-lo)/2*(2/math.pi)*s*s*base*orient))
hs=[.00375,.001875,.0009375]
values=[raw(h,False) for h in hs]
other=[raw(h,True) for h in hs]
ratios=[values[i]/values[i+1] for i in range(2)]
predicates=[dict(name='full_Haar_angular_comparison',passed=all(abs(a-b)/a<2e-9 for a,b in zip(values,other))),
            *[dict(name=f'narrow_ratio_{i}',passed=1.85<r<2.15) for i,r in enumerate(ratios)]]
res=dict(posthoc=True,u=u,widths=hs,raw_shell_integrals=values,angular_integrals=other,
         ratios=ratios,predicates=predicates,passed=sum(p['passed'] for p in predicates),total=len(predicates),
         interpretation='Supports narrower-shell limiting mechanism; does not replace original 23/24 result')
Path(__file__).with_name('covariant_complement_posthoc_results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
raise SystemExit(0 if res['passed']==res['total'] else 1)
