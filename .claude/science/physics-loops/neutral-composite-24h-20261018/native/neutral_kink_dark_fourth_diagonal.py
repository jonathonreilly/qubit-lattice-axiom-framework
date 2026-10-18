from pathlib import Path
"""Fourth-order diagonal side-state coefficient using complete virtual paths."""
from collections import defaultdict
import numpy as np,json,time
from neutral_kink_core import band,h,bits
rows=[]
for L in [12,16]:
 start=time.monotonic();H1,H2,states,_=band(L);lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)];ecache={}
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
 def R(vec,ref):return {x:a/(ref-energy(x)) for x,a in vec.items() if energy(x)!=ref}
 vac={sum(a*p for p in powers):1/np.sqrt(8) for a in range(8)}
 w=R(V(vac),0);vw=V(w);E4=sum(abs(a)**2/(-energy(x)) for x,a in vw.items() if energy(x)!=0)+(L/2)*sum(abs(a)**2 for a in w.values())
 for ell in [2,3,4,5,6]:
  mode=0
  momentum=2*np.pi*mode/L;d=defaultdict(complex)
  for a in range(8):
   for b in range(8):
    if (bits[a]^bits[b]) not in [6,9]:continue
    for j in range(L):
     state=sum((b if (k-j)%L<ell else a)*powers[k] for k in range(L));d[state]+=np.exp(1j*momentum*(j+.5))/np.sqrt(16*L)
  norm=np.sqrt(sum(abs(a)**2 for a in d.values()));d={x:a/norm for x,a in d.items()}
  dv=np.zeros(len(states),complex)
  for x,a in d.items():dv[lookup[x]]=a
  assert abs(np.vdot(dv,dv)-1)<1e-12 and np.linalg.norm(H1@dv)<1e-12
  b2d=H2@dv-(L/2)*dv;bd={states[i]:a for i,a in enumerate(b2d) if abs(a)>1e-12}
  w=R(V(d),8);vw=V(w);wb=R(V(bd),8)
  term1=sum(abs(a)**2/(8-energy(x)) for x,a in vw.items() if energy(x)!=8)
  folded=sum(np.conjugate(a)*wb.get(x,0) for x,a in w.items()).real
  k4=term1-folded
  row=dict(L=L,ell=ell,mode=mode,q=momentum,K4_diagonal=float(k4),ground_E4=float(E4),gap_fourth_diagonal=float(k4-E4),Q1_support=len(w),second_hop_support=len(vw),seconds=time.monotonic()-start,scope='Finite canonical fourth-order diagonal; resonance self-energy and offdiagonal effects separate')
  rows.append(row);open(Path(__file__).with_suffix('.json'),'w').write(json.dumps(rows,indent=2));print(row,flush=True)
