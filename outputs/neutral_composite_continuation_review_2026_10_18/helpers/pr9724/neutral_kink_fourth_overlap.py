from pathlib import Path
import sys,json,time

from neutral_kink_core import band,h,bits
from collections import defaultdict
import numpy as np
rows=[]
for L in [12]:
 H1,H2,H3,states,source=band(L,third=True);lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)];ecache={}
 def energy(state):
  if state not in ecache:
   ds=[state//p%8 for p in powers];ecache[state]=sum(2*(bits[ds[j]]^bits[ds[(j+1)%L]]).bit_count() for j in range(L))
  return ecache[state]
 def V(vec):
  out=defaultdict(complex)
  for state,amp in vec.items():
   if abs(amp)<1e-13:continue
   for power in powers:
    old=state//power%8
    for new in np.flatnonzero(h[:,old]):out[state+(int(new)-old)*power]+=h[new,old]*amp
  return {x:a for x,a in out.items() if abs(a)>1e-12}
 def R(vec,k=1):return {x:a/(8-energy(x))**k for x,a in vec.items() if energy(x)!=8}
 def P(vec):
  out=np.zeros(len(states),complex)
  for x,a in vec.items():
   if x in lookup:out[lookup[x]]=a
  return out
 def PV(vec):
  out=np.zeros(len(states),complex)
  for i,state in enumerate(states):
   for power in powers:
    old=state//power%8
    for new in np.flatnonzero(h[:,old]):out[i]+=h[new,old]*vec.get(state+(int(new)-old)*power,0)
  return out
 def D(vec):return {states[i]:a for i,a in enumerate(vec) if abs(a)>1e-12}
 for mode in [0,1,2]:
  q=2*np.pi*mode/L;d=defaultdict(complex)
  for a in range(8):
   for b in range(8):
    if (bits[a]^bits[b]) not in [6,9]:continue
    for j in range(L):
     st=sum((b if k in [j,(j+1)%L] else a)*powers[k] for k in range(L));d[st]+=np.exp(1j*q*(j+.5))/np.sqrt(16*L)
  dv=P(d);v=V(d);rv=R(v);r2v=R(v,2);r3v=R(v,3)
  term=PV(R(V(R(V(rv)))))
  md=P(V(R(V(rv),2)))+P(V(R(V(r2v))))
  n3=P(V(r3v));n2=P(V(r2v));b2=H2@dv-L/2*dv
  n2b=P(V(R(V(D(b2)),2)))
  k4=term-.5*(H1@md)+.5*(H1@(H1@n3))-.5*(n2b+H2@n2-L/2*n2)
  # Build common invariant source space through cubic order using the physical d.
  s=np.zeros(len(states),complex)
  for a in range(8):
   vac=sum(a*p for p in powers)
   for j,power in enumerate(powers):
    for new in np.flatnonzero(h[:,a]):
     idx=lookup.get(vac+(int(new)-a)*power)
     if idx is not None:s[idx]+=h[new,a]*np.exp(1j*q*j)/np.sqrt(8*L)
  Q=[];cur=s/np.linalg.norm(s)
  for i in range(L+2):
   Q.append(cur);w=H1@cur
   for _ in range(2):
    for old in Q:w-=old*np.vdot(old,w)
   norm=np.linalg.norm(w)
   if norm<1e-10:break
   cur=w/norm
  W=np.column_stack(Q+[dv]);leak=k4-W@(W.conj().T@k4)
  overlaps=[]
  for ell in range(2,L//2+1):
   de=np.zeros(len(states),complex)
   for a in range(8):
    for b in range(8):
     if (bits[a]^bits[b]) not in [6,9]:continue
     for j in range(L):
      st=sum((b if (k-j)%L<ell else a)*powers[k] for k in range(L));de[lookup[st]]+=np.exp(1j*q*(j+(ell-1)/2))
   norm=np.linalg.norm(de)
   if norm>1e-10:
    de/=norm;val=np.vdot(de,leak);overlaps.append([ell,float(val.real),float(val.imag)])
  row=dict(overlaps=overlaps,L=L,mode=mode,diag=float(np.vdot(dv,k4).real),outside=float(np.linalg.norm(leak)),H1_outside=float(np.linalg.norm(H1@leak)),H2_minus_d_outside=float(np.linalg.norm((H2@leak)+2*leak)))
  rows.append(row);print(row,flush=True)
Path(Path(__file__).with_suffix('.json')).write_text(json.dumps(rows,indent=2))
