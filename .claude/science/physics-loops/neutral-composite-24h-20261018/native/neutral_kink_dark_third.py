from pathlib import Path
import sys,numpy as np,json

from neutral_kink_core import band,bits
rows=[]
for L in [12,16]:
 H1,H2,H3,states,_=band(L,third=True);lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)]
 for mode in [0,1,2]:
  q=2*np.pi*mode/L
  for ell in range(1,L//2+1):
   d=np.zeros(len(states),complex)
   for a in range(8):
    for b in range(8):
     if (bits[a]^bits[b]) not in [6,9]:continue
     for j in range(L):
      st=sum((b if (k-j)%L<ell else a)*powers[k] for k in range(L));d[lookup[st]]+=np.exp(1j*q*(j+(ell-1)/2))
   if np.linalg.norm(d)<1e-10:continue
   d/=np.linalg.norm(d);e2=np.vdot(d,H2@d).real
   row=dict(H3norm=float(np.linalg.norm(H3@d)),L=L,mode=mode,ell=ell,H1norm=float(np.linalg.norm(H1@d)),H2mean=float(e2),H2res=float(np.linalg.norm(H2@d-e2*d)));rows.append(row);print(row,flush=True)
Path(Path(__file__).with_suffix('.json')).write_text(json.dumps(rows,indent=2))
