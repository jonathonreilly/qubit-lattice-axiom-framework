#!/usr/bin/env python3
"""Independently reconstruct ALL relative-lapse coefficients from literal stencils.

Actual 2x2 Gaussian-rational matrix entries; no import from Laurent constructor.
Keys of matrices: (row position, row spin, col position, col spin, imaginary bit).
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json,time,resource
P=Path(__file__).resolve().parent
ZERO=(0,0,0)
SIGMA=[[(0,1,0,1),(1,0,0,1)],[(0,1,1,-1),(1,0,1,1)],[(0,0,0,1),(1,1,0,-1)]]
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def unit(j,n=1):return tuple(n if i==j else 0 for i in range(3))
def addterm(out,key,c):
    out[key]+=c
    if not out[key]:del out[key]
def block(out,a,b,s,c,imag=0):
    entries=SIGMA[s-1] if s else [(0,0,0,1),(1,1,0,1)]
    for r,t,i,v in entries:
        n=i+imag;addterm(out,(a,r,b,t,n%2),c*v*(-1 if n>=2 else 1))
def energy():
    out=defaultdict(F)
    for a in product([-1,1],repeat=3):
        for j in range(3):
            for sign in [-1,1]:
                b=plus(a,unit(j,sign));c=F(-sign,32)
                block(out,a,b,j+1,c,1)
                block(out,b,a,j+1,-c,1)
    return out
def multiply_local(A,B):
    out=defaultdict(F)
    for (a,r,b,s,i),v in A.items():
        for (c,t,d,u,j),w in B.items():
            if b!=c or s!=t:continue
            n=i+j;addterm(out,(a,r,d,u,n%2),v*w*(-1 if n>=2 else 1))
    return out
def H_times(A,left):
    out=defaultdict(F)
    for (a,r,b,s,i),v in A.items():
        for j in range(3):
            for sign in [-1,1]:
                for c,d,k,w in SIGMA[j]:
                    n=i+k+1;z=v*w*F(-sign,2)*(-1 if n//2%2 else 1)
                    if left and d==r:addterm(out,(minus(a,unit(j,sign)),c,b,s,n%2),z)
                    if not left and s==c:addterm(out,(a,r,plus(b,unit(j,sign)),d,n%2),z)
    return out
def current(j):
    out=defaultdict(F)
    # Pdd=(phi^T pi); weighted site anticommutator, then divide by2 for P^B.
    choices=[[-1,1] if k!=j else [0,1] for k in range(3)]
    for a in product(*choices):
        for sign in [-1,1]:
            b=plus(a,unit(j,2*sign));c=F(-sign,128)
            block(out,a,b,0,c,1);block(out,b,a,0,-c,1)
    # Qb=(A H+H A+H A*+A* H)/4; Q=body diagonal average; P^B=(Pdd+Q)/2.
    for a in product([-1,1],repeat=3):
        b=plus(a,unit(j));A=defaultdict(F);block(A,b,a,j+1,F(1,64));block(A,a,b,j+1,F(1,64))
        for mat in [H_times(A,True),H_times(A,False)]:
            for k,v in mat.items():addterm(out,k,v)
    return out
def load_laurent():
    out=defaultdict(F)
    for ex,s,i,vs in json.loads((P/'defect.json').read_text())[0]:
        a,b,c=ex[:3],ex[3:6],ex[6:];d=minus(b,a);r=minus(ZERO,a);t=minus(c,a)
        tmp=defaultdict(F);block(tmp,r,t,s,F(vs),i)
        for k,v in tmp.items():addterm(out,(d,)+k,v)
    return out
def main():
    start=time.monotonic();E=energy();out=defaultdict(F)
    # All pairs which can share an intermediate endpoint, derived without enumerating a radius.
    for (a,r,b,s,i),v in E.items():
        for (c,t,e,u,j),w in E.items():
            if s!=t:continue
            d=minus(b,c);n=i+j+1;z=-v*w*(-1 if n//2%2 else 1)
            addterm(out,(d,a,r,plus(e,d),u,n%2),z)
            addterm(out,(minus(ZERO,d),minus(a,d),r,e,u,n%2),-z)
    comm=dict(out)
    for j in range(3):
        d=unit(j)
        for (a,r,b,s,i),v in current(j).items():
            addterm(out,(d,a,r,b,s,i),v)
            addterm(out,(minus(ZERO,d),minus(a,d),r,minus(b,d),s,i),-v)
    actual=load_laurent()
    assert dict(out)==dict(actual), f'Whole-coefficient mismatch {len(out)} versus {len(actual)}'
    delta=unit(0,2);blocks={(a,b) for (d,a,r,b,s,i) in comm if d==delta}
    witness=comm.get((delta,(-1,-1,-1),0,(1,-1,-1),0,1),0)
    assert witness==F(1,1024)
    stats={'energy_matrix_entries':len(E),'commutator_matrix_coefficients':len(comm),'defect_matrix_coefficients':len(out),'nonzero_relative_lapse_displacements':len({key[0] for key in out}),'delta2_nonzero_spatial_blocks':len(blocks),'delta2_witness_imaginary':str(witness),'all_relative_lapse_coefficients_match':True,'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    (P/'position_results.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats,indent=2))
if __name__=='__main__':main()
