"""Spatial transition densities of reconstructed finite-grid neutral vectors."""
import json
from pathlib import Path
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;d=basis((3,3,3));idx={x:i for i,x in enumerate(d['sites'])};g=np.load(P/'stationary_3x3x3_plus.npz')['vectors'][:,0];modes=np.load(P/'stationary_visible_vectors.npz')['vectors'];energy=[];composite=[]
for x,i in idx.items():
 et=[]
 for a in range(3):
  for delta in [-1,1]:
   y=list(x);y[a]+=delta
   if tuple(y) not in idx:continue
   mask=(1<<i)|(1<<idx[tuple(y)])
   et.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
 terms=np.array(et,np.int64);E=lambda v:apply(v,*terms.T.copy())/2
 eg=E(g);cg=2*E(eg)-len(et)/2*g
 energy.append(modes@eg);composite.append(modes@cg)
energy=np.array(energy).T;composite=np.array(composite).T;rows=[]
for j in range(len(modes)):
 assert abs(sum(energy[j]))<1e-9
 row=dict(mode=j,energy_amplitudes=energy[j].tolist(),composite_amplitudes=composite[j].tolist(),uniform_energy_amplitude=float(sum(energy[j])))
 for name,v in [('energy',energy[j]),('composite',composite[j])]:
  weight=v*v;row[name+'_transition_participation']=float(sum(weight)**2/sum(weight**2))
 rows.append(row)
out=dict(sites=d['sites'],rows=rows,scope='Transition-density support on one finite open cube, not particle wavefunctions, localization lengths, bulk dispersion or universal coupling')
(P/'stationary_mode_form_factors.json').write_text(json.dumps(out,indent=2)+'\n');print([{'mode':r['mode'],'energy_participation':r['energy_transition_participation'],'composite_participation':r['composite_transition_participation'],'uniform_energy':r['uniform_energy_amplitude']} for r in rows],flush=True)
