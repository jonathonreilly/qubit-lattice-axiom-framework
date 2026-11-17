#!/usr/bin/env python3
"""Exact integer dimension inventory (bookkeeping, never proof evidence).
Horizontal doubled-spin cap J, horizontal Casimir sum E=sum j2*(j2+2).
All allowed vertical spins and middle intertwiners are included.
"""
from leakage import base, np, Path
from numba import njit
import itertools,json

@njit
def histogram(energy,W,maxE):
    # Pair the opposite columns. Sum the other two columns by convolution.
    L=len(energy);out=np.zeros(maxE+1,np.int64)
    for a in range(L):
      for c in range(L):
        shift=energy[a]+energy[c]
        if shift>maxE:continue
        h=np.zeros(maxE-shift+1,np.int64)
        for b in range(L):
            e=energy[b]
            if e<len(h):h[e]+=W[a,b]*W[b,c]
        for e in range(len(h)):
            if h[e]:
                for f in range(len(h)-e):
                    if h[f]:out[shift+e+f]+=h[e]*h[f]
    return out

def choices(J):
    hs=np.array(list(itertools.product(range(J+1),repeat=3)),np.int16)
    options={};W=np.zeros((len(hs),len(hs)),np.int64)
    for a,h in enumerate(hs):
      for b,k in enumerate(hs):
        opt=[]
        for s in range(abs(int(h[0]-k[0])),int(h[0]+k[0])+1,2):
          for t in range(abs(int(h[2]-k[2])),int(h[2]+k[2])+1,2):
            for r in range(abs(int(h[1]-k[1])),int(h[1]+k[1])+1,2):
                if base.triangle(s,t,r):opt.append((s,t,r))
        options[a,b]=opt;W[a,b]=len(opt)
    maxopt=int(W.max());opts=np.zeros((len(hs),len(hs),maxopt,3),np.int16)
    for (a,b),opt in options.items():
        if opt:opts[a,b,:len(opt)]=opt
    return hs,W,opts

if __name__=='__main__':
    records=[]
    for J in (1,2,3,4):
        hs,W,_=choices(J);en=np.sum(hs*(hs+2),axis=1)
        h=histogram(en,W,200);cs=np.cumsum(h)
        item={'J':J,'exact_states_by_E':{str(E):int(cs[E]) for E in (24,30,36,40,44,48,52,56,60,70,80,100,120,140,160,180,200)},'full_dimension':int(np.trace((W@W)@(W@W)))}
        records.append(item);print(json.dumps(item),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps({'grade':'inventory only','records':records},indent=2)+'\n')
