from pathlib import Path
import numpy as np,json
rows=[]
for q in [0,np.pi/6,np.pi/3,1.5,np.pi/2,1.6,2*np.pi/3]:
 u=np.cos(q);c=np.cos(q/2);bulk=-13/96;v=(1-479*u)/(192*(1+u));hop=-3*u/32
 exists=abs(v)>abs(hop)
 row=dict(q=q,boundary_defect=v,hop=hop,bulk=bulk,exists=bool(exists))
 if exists:
  e=bulk+v+hop*hop/v;r=hop/v;Z=1-r*r
  N=200;H=np.diag(np.full(N,bulk));H[0,0]+=v;H+=np.diag(np.full(N-1,hop),1)+np.diag(np.full(N-1,hop),-1)
  ev,U=np.linalg.eigh(H);idx=np.argmin(abs(ev-e));assert abs(ev[idx]-e)<1e-12;assert abs(U[0,idx]**2-Z)<1e-10
  row.update(shift=e,amplitude_ratio=r,boundary_weight=Z,width_coefficient=Z*9*(1-2*u)**2/(32*c**3),readout_residue_coefficient=Z*2*u*u/(c*c))
 rows.append(row)
print(json.dumps(rows,indent=2));open(Path(__file__).with_suffix('.json'),'w').write(json.dumps(dict(rows=rows,scope='Conditional on native-derived dark halfline coefficients; not yet all-channel or all-order certificate'),indent=2))
