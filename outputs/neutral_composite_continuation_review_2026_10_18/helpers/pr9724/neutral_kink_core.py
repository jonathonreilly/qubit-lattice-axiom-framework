"""First-order native two-wall band, positive-rung periodic tube; candidate test."""
from pathlib import Path
import sys,itertools,json,numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

from neutral_rung_model import h,Ds
bits=[(b<<1)|(b.bit_count()%2) for b in range(8)] # only Hamming distances used; equivalent bit order
pairs=[(a,b) for a in range(8) for b in range(a+1,8) if (bits[a]^bits[b]).bit_count()==2]
def band(L,third=False):
 powers=[8**j for j in range(L)];states=[];length=[]
 for a,b in pairs:
  for start in range(L):
   for ell in range(1,L):
    ds=[a]*L
    for j in range(ell):ds[(start+j)%L]=b
    states.append(sum(d*p for d,p in zip(ds,powers)));length.append(min(ell,L-ell))
 lookup={v:i for i,v in enumerate(states)};assert len(lookup)==24*L*(L-1)
 rr=[];cc=[];vv=[];qr=[];qc=[];qv=[];qstates={};source=np.zeros(len(states))
 for c,state in enumerate(states):
  for j,power in enumerate(powers):
   old=(state//power)%8
   for new in np.flatnonzero(h[:,old]):
    dest=state+(int(new)-old)*power
    r=lookup.get(dest)
    if r is not None:rr.append(r);cc.append(c);vv.append(h[new,old])
    else:
     qi=qstates.setdefault(dest,len(qstates));qr.append(c);qc.append(qi);qv.append(h[new,old])
 for a in range(8):
  vac=sum(a*p for p in powers)
  for j,power in enumerate(powers):
   for new in np.flatnonzero(h[:,a]):
    r=lookup.get(vac+(int(new)-a)*power)
    if r is not None:source[r]+=h[new,a]/np.sqrt(8*L)
 H=coo_matrix((vv,(rr,cc)),shape=(len(states),len(states))).tocsr();assert (H-H.T).nnz==0
 Q=coo_matrix((qv,(qr,qc)),shape=(len(states),len(qstates))).tocsr()
 energies=[]
 for state in qstates:
  ds=[(state//p)%8 for p in powers];energies.append(sum(2*(bits[ds[j]]^bits[ds[(j+1)%L]]).bit_count() for j in range(L)))
 assert all(x!=8 for x in energies)
 from scipy.sparse import diags,identity
 H2=Q@diags(1/(8-np.array(energies)))@Q.T+(L/2)*identity(len(states))
 if not third:return H,H2,states,source
 rr=[];cc=[];vv=[]
 for state,c in qstates.items():
  for j,power in enumerate(powers):
   old=(state//power)%8
   for new in np.flatnonzero(h[:,old]):
    dest=state+(int(new)-old)*power;r=qstates.get(dest)
    if r is not None:rr.append(r);cc.append(c);vv.append(h[new,old])
 VQ=coo_matrix((vv,(rr,cc)),shape=(len(qstates),len(qstates))).tocsr()
 den=1/(8-np.array(energies));B=Q@diags(den);metric=Q@diags(den**2)@Q.T
 H3=B@VQ@B.T-(metric@H+H@metric)/2
 return H,H2,H3,states,source
