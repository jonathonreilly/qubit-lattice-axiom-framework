#!/usr/bin/env python3
"""Literal native finite-covariance check for different source polynomials."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from collections import Counter
from functools import lru_cache
from itertools import product,combinations
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as s
from block12_clifford import A0,C0,ODD
from block12_separate import SeparateAlgebra,CLASSES,kernel,norms
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
    env={A0:float(np.mean(np.abs(freq)**-2)),C0:float(np.mean(np.abs(freq)**-1)),
         ODD[1]:float(np.mean(np.abs(freq))),ODD[3]:float(np.mean(np.abs(freq)**3))}
    legs=[]
    for ax in range(3):
        for direction in (1,-1):
            r=[0,0,0];r[ax]=direction%L;legs.append((ax,direction,ix[tuple(r)]))
    a=np.eye(M)[:,0];vectors=[a,K@a];channels={}
    p={'P':(3.,-1.,.125),'O':(2.,-2/3,1/12)};q={'P':(2.,-.5,1/24),'O':(7/4,-1/3,1/32)}
    def local_x(coeff,d,kd):
        p0,p1,p2=coeff
        return [((),-p0-2*p2),((0,d),-1j*p1),((1,d),p2),((0,kd),p2)]
    for A in combinations(range(6),2):
        d=np.zeros(M)
        for j in A:d[legs[j][2]]=-K[0,legs[j][2]]
        index=len(vectors);vectors.extend((d,K@d,6*np.linalg.solve(K,d)))
        kind='O' if legs[A[0]][0]==legs[A[1]][0] else 'P'
        x=local_x(p[kind],index,index+1);xq=local_x(q[kind],index,index+1)
        v=[((index+2,)+word,-c) for word,c in x]+[((index+2,)+word,c) for word,c in xq]
        v.extend([((index,),-2j*q[kind][1]),((index+1,),2*q[kind][2])])
        channels[A]=(kind,x,v,[((0,)+word,c) for word,c in v],index)
    vectors=np.stack(vectors);dot=vectors@vectors.T;kap=vectors@Gamma@vectors.T;cov=dot+1j*kap
    @lru_cache(None)
    def wick(word):
        if not word:return 1
        if len(word)%2:return 0
        return sum((-1)**(j-1)*cov[word[0],word[j]]*wick(word[1:j]+word[j+1:]) for j in range(1,len(word)))
    def inner(x,y):return sum(np.conjugate(c)*d*wick(w[::-1]+v) for w,c in x for v,d in y)
    tableerr=0.;nomerr=0.;normerr=0.;total=0.;prediction=0.;seen=set();count=0
    for A,(kindA,xA,vA,gvA,idxA) in channels.items():
        for C,(kindC,xC,vC,gvC,idxC) in channels.items():
            if set(A)&set(C) and A!=C:continue
            m=sum(legs[i][0]==legs[j][0] and legs[i][1]!=legs[j][1] for i in A for j in C)
            if A==C:m=0
            key=(kindA,kindC,m,A==C)
            if key not in seen:
                alg=SeparateAlgebra(kindA,kindC,m);bank=[idxA+2,idxC+2,0,1,idxA,idxA+1,idxC,idxC+1]
                # For self fixtures use A labels on both slots: C is the same physical vector.
                if A==C:bank=[idxA+2,idxA+2,0,1,idxA,idxA+1,idxA,idxA+1]
                for j,k in product(range(8),repeat=2):
                    if A==C and (j not in (0,2,3,4,5) or k not in (0,2,3,4,5)):
                        continue  # self check uses one slot; distinct C is not relabeled as A
                    expected=[float(z.subs(env)) for z in alg.table(j,k)]
                    actual=[dot[bank[j],bank[k]],kap[bank[j],bank[k]]]
                    tableerr=max(tableerr,max(abs(x-y) for x,y in zip(actual,expected)))
                seen.add(key)
            if A==C:continue
            count+=1;actual=(inner(xC,xA)-inner(xC,gvA)).real
            expected=float(kernel(kindA,kindC,m,p[kindA],p[kindC],q[kindA]).subs(env))
            nomerr=max(nomerr,abs(actual-expected));total+=actual;prediction+=expected
        nx,nv=norms(kindA,p[kindA],q[kindA]);normerr=max(normerr,abs(inner(xA,xA)-complex(nx.subs(env))),abs(inner(vA,vA)-complex(nv.subs(env))))
    assert count==90 and tableerr<5e-11 and nomerr<5e-11 and normerr<5e-11,(count,tableerr,nomerr,normerr)
    dropped=0.
    for A,(ka,xa,va,gva,ia) in channels.items():
        local=[((0,ia),-2j*q[ka][1]),((0,ia+1),2*q[ka][2])]
        for C,(kc,xc,vc,gvc,ic) in channels.items():
            if not set(A)&set(C):dropped+=(inner(xc,xa)-inner(xc,local)).real
    assert abs(dropped-total)>1
    return {'status':'passed','ordered_pairs':count,'norm_checks':30,'table_fixture_classes':len(seen),
            'max_table_absolute_error':tableerr,'max_kernel_absolute_error':nomerr,'max_norm_absolute_error':normerr,
            'complete_nominal_direct':total,'complete_nominal_formula':prediction,
            'omitted_W_p_minus_q_mutant_rejected':True,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('block12_clifford.py','block12_nominal.py','block12_separate.py')},
            'scope':'finite native covariance algebra check; no infinite alpha sign or source re-audit'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_SEPARATE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
