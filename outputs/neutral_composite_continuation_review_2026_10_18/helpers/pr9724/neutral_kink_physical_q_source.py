"""Derive centered Fourier NNN composite source from its actual diagonal entries."""
from pathlib import Path
import numpy as np,json
from neutral_kink_core import band,bits,h
rows=[]
for L in [8,12,16]:
 H1,H2,states,s0=band(L);lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)];sH=H1@s0
 digits=np.array([[state//p%8 for p in powers] for state in states]);colors=np.array(bits)[digits]
 delta=np.array([[-2*(int(colors[i,j])^int(colors[i,(j+2)%L])).bit_count() for j in range(L)] for i in range(len(states))])
 for mode in range(L//2):
  q=2*np.pi*mode/L;u=np.cos(q);sq=np.zeros(len(states),complex)
  for a in range(8):
   vac=sum(a*p for p in powers)
   for j,power in enumerate(powers):
    for new in np.flatnonzero(h[:,a]):
     idx=lookup.get(vac+(int(new)-a)*power)
     if idx is not None:sq[idx]+=h[new,a]*np.exp(1j*q*j)/np.sqrt(8*L)
  deltaq=delta@np.exp(1j*q*(np.arange(L)+1))
  first=-deltaq*s0/8;second=deltaq*sH/64
  e1=np.linalg.norm(first-u*sq);e2=np.linalg.norm(second+u*(H1@sq)/4)
  assert max(e1,e2)<1e-10,(L,mode,e1,e2)
  rows.append(dict(L=L,mode=mode,q=q,first_identity_error=float(e1),second_identity_error=float(e2),leading_form_factor=float(u)))
Path(Path(__file__).with_suffix('.json')).write_text(json.dumps(rows,indent=2));print('physical Fourier source checks',len(rows),'maxerror',max(max(x['first_identity_error'],x['second_identity_error']) for x in rows))
