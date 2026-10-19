"""Central native composite spectrum in a chosen stationary open-grid sector."""
import json,time
from pathlib import Path
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;d=basis((3,3,3));terms=np.array(d['terms'],np.int64)
H=lambda v:apply(v,*terms.T.copy())
idx={x:i for i,x in enumerate(d['sites'])};center=(1,1,1);rawC=[];rawE=[]
for a in range(3):
 l=list(center);r=list(center);l[a]-=1;r[a]+=1
 mask=(1<<idx[tuple(l)])|(1<<idx[tuple(r)])
 rawC.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,-1 if a==1 else 1))
 for y in [l,r]:
  mask=(1<<idx[center])|(1<<idx[tuple(y)])
  # Store twice local e, hence integer coefficients.
  rawE.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
c=np.array(rawC,np.int64);ee=np.array(rawE,np.int64);C=lambda v:apply(v,*c.T.copy());E=lambda v:apply(v,*ee.T.copy())/2
saved=np.load(P/'stationary_3x3x3_plus.npz');levels=saved['values'];vec=saved['vectors'];g=vec[:,0];e0=levels[0];hg=H(g)
responses={}
for name,O in [('C',C),('e',E)]:
 og=O(g);mean=np.dot(g,og);v=og-mean*g;weight=np.dot(v,v);lv=H(v)-e0*v
 centroid=np.dot(v,lv)/weight;variance=np.dot(lv,lv)/weight-centroid**2
 acceleration=-2*np.dot(hg,H(og))+2*np.dot(hg,O(hg))
 prev=np.zeros_like(v);q=v/np.sqrt(weight);beta=0.;aa=[];bb=[];resolvents={}
 for k in range(64):
  w=H(q)-e0*q-beta*prev;alpha=np.dot(q,w);w-=alpha*q
  # Remove computed initial eigenstate to prevent elastic contamination.
  w-=g*np.dot(g,w)
  nxt=np.linalg.norm(w);aa.append(float(alpha))
  if k in [15,31,63]:
   T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1)
   en,u=np.linalg.eigh(T)
   resolvents[str(k+1)]={str(eta):float(weight*np.sum(u[0]**2*en/(en**2+eta**2))) for eta in [.1,.5,1.]}
  if k<63:bb.append(float(nxt))
  prev,q=q,w/nxt;beta=nxt
 responses[name]=dict(mean=float(mean),connected_source_weight=float(weight),centroid=float(centroid),variance=float(variance),initial_acceleration=float(acceleration),low_level_weights=[float(np.dot(vec[:,j],og)**2) for j in range(1,4)],lanczos_alpha=aa,lanczos_beta=bb,regularized_inverse_moments=resolvents)
out=dict(energies=levels.tolist(),responses=responses,scope='Selected allplus stationary open27-site finite system, no bulk pole or globalground selection; Lanczos regularized inverse moments are numerical diagnostics, not certified susceptibilities')
(P/'stationary_response.json').write_text(json.dumps(out,indent=2)+'\n');print({k:{q:v for q,v in r.items() if not q.startswith('lanczos')} for k,r in responses.items()},flush=True)
