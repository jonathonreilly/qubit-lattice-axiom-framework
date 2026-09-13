#!/usr/bin/env python3
"""Direct finite native covariance contractions of all90 ordered trial kernels.

No Clifford normal-ordering helper is used for the numerical contractions.
Finite AP radial moments replace infinite inputs in this identity check.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from collections import Counter
from functools import lru_cache
from itertools import product,combinations
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as s
from block12_clifford import ODD
from block12_nominal import CLASSES,kernel,norm_formulas
HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();L=8;points=list(product(range(L),repeat=3));ix={r:j for j,r in enumerate(points)};M=L**3
    K=np.zeros((M,M))
    for r in points:
        for ax in range(3):
            v=list(r);v[ax]=(v[ax]+1)%L
            sign=(-1)**sum(r[:ax])*(-1 if r[ax]==L-1 else 1)
            K[ix[r],ix[tuple(v)]]=sign;K[ix[tuple(v)],ix[r]]=-sign
    freq,U=np.linalg.eigh(1j*K);Gamma=(K@(U*(1/np.abs(freq)))@U.conj().T).real
    mu=float(np.mean(np.abs(freq)));nu=float(np.mean(np.abs(freq)**3))
    legs=[]
    for ax in range(3):
        for direction in (1,-1):
            r=[0,0,0];r[ax]=direction%L;legs.append((ax,direction,ix[tuple(r)]))
    a=np.eye(M)[:,0];vectors=[a,K@a];channels={};p={'P':(3.,-1.,.125),'O':(2.,-2/3,1/12)}
    for A in combinations(range(6),2):
        d=np.zeros(M)
        for j in A:d[legs[j][2]]=-K[0,legs[j][2]]
        index=len(vectors);vectors.extend((d,K@d));kind='O' if legs[A[0]][0]==legs[A[1]][0] else 'P'
        p0,p1,p2=p[kind]
        x=[((),-p0-2*p2),((0,index),-1j*p1),((1,index),p2),((0,index+1),p2)]
        v=[((index,),-2j*p1),((index+1,),2*p2)]
        gv=[((0,)+word,c) for word,c in v]
        channels[A]=(kind,x,v,gv)
    vectors=np.stack(vectors);cov=vectors@(np.eye(M)+1j*Gamma)@vectors.T
    @lru_cache(None)
    def wick(word):
        if not word:return 1
        if len(word)%2:return 0
        return sum((-1)**(j-1)*cov[word[0],word[j]]*wick(word[1:j]+word[j+1:]) for j in range(1,len(word)))
    def inner(x,y):return sum(np.conjugate(c)*d*wick(w[::-1]+v) for w,c in x for v,d in y)
    histogram=Counter();maxerr=0.;total=0.;predicted=0.
    for A,(kindA,xA,vA,gvA) in channels.items():
        for C,(kindC,xC,vC,gvC) in channels.items():
            if set(A)&set(C):continue
            m=sum(legs[i][0]==legs[j][0] for i in A for j in C)
            histogram[(kindA,kindC,m)]+=1
            actual=(inner(xC,xA)-inner(xC,gvA)).real
            expected=float(kernel(kindA,kindC,m,p[kindA],p[kindC]).subs({ODD[1]:mu,ODD[3]:nu}))
            maxerr=max(maxerr,abs(actual-expected));total+=actual;predicted+=expected
    assert histogram==Counter({(a,c,m):count for a,c,m,count in CLASSES}),histogram
    assert maxerr<2e-11,(maxerr,total,predicted)
    normerr=0.
    for A,(kind,x,v,gv) in channels.items():
        nx,nv=norm_formulas(kind,p[kind])
        normerr=max(normerr,abs(inner(x,x)-complex(nx.subs({ODD[1]:mu,ODD[3]:nu}))),abs(inner(v,v)-complex(nv.subs({ODD[1]:mu,ODD[3]:nu}))))
    assert normerr<2e-11,normerr
    # An omitted opposite-match term must be detected by this fixture.
    mutant=float(kernel('P','P',0,p['P'],p['P']).subs({ODD[1]:mu,ODD[3]:nu}))
    original=float(kernel('P','P',2,p['P'],p['P']).subs({ODD[1]:mu,ODD[3]:nu}))
    assert abs(mutant-original)>1e-3
    return {'status':'passed','ordered_pairs':90,'channel_norm_checks':30,
            'max_kernel_absolute_error':maxerr,'max_norm_absolute_error':normerr,
            'signed_nominal_direct':total,'signed_nominal_formula':predicted,
            'omitted_opposite_match_mutant_rejected':True,'seconds':time.monotonic()-start,
            'scope':'finite native AP covariance identity check; no infinite native scalar sign or independent source review',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('block12_clifford.py','block12_nominal.py')}}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_CROSS_NOMINAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
