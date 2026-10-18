#!/usr/bin/env python3
"""Finite native qubit Hamiltonian controls; no empirical or bulk scalar claim."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
from scipy.sparse.linalg import eigsh
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_probe.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_sectors.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_response_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_native_scalar.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_low_spectrum.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_translation_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_spacegroup_model.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_spacegroup_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_ground.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_spacegroup.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_spacegroup_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cube_map_independent.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_independent_check.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_response.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_original_source.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_cube_response_check.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_cube_low_spectrum.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_spacegroup_data_response_before_Q_projection_fix.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_data_ground.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_data_observables.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_spacegroup_data_response.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_cube_sectors.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_cube_probe.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_cube_native_scalar.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_spacegroup_data_low.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_data_response_rejected_nodes.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/neutral_rect_data_original_source_rejected_nodes.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/IDENTITIES.json', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/REPRODUCTION.md']
PACK=ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0,str(PACK))
from neutral_rect_model import sector,op,mult
from neutral_spacegroup_model import translation_tables,orbits,orbit_op
from collections import defaultdict

def comm(a,b):
 out=defaultdict(float)
 for u in a:
  for v in b:
   x,z,c=mult(u,v);out[x,z]+=c
   x,z,c=mult(v,u);out[x,z]-=c
 return [(x,z,c) for (x,z),c in out.items() if c]

def run():
 d=sector(2);W=np.zeros((256,d['dim']))
 for j in range(d['dim']):
  v={d['solve'](j):1.}
  for x,z,p in d['all_generators']:
   out=dict(v)
   for s,c in v.items():out[s^x]=out.get(s^x,0)+p*(-1)**((s&z).bit_count())*c
   v={s:c for s,c in out.items() if c}
  norm=sum(c*c for c in v.values())**.5
  for s,c in v.items():W[s,j]=c/norm
 physical=op(sum(d['physical_H'],[]),256);reduced=op(sum(d['H'],[]),d['dim']);rng=np.random.default_rng(318);v=rng.normal(size=d['dim']);v/=np.linalg.norm(v)
 error=float(np.linalg.norm(physical@(W@v)-W@(reduced@v)));assert error<1e-12 and np.linalg.norm(W.T@W-np.eye(d['dim']))<1e-12
 d=sector(3);T,R,C=translation_tables(d);data=orbits(d['dim'],T,R,C);H=orbit_op(sum(d['H'],[]),data)
 E,V=eigsh(H,k=16,which='SA',tol=1e-12,ncv=40,v0=np.random.default_rng(319).normal(size=H.shape[0]));g=V[:,0]
 # Compose non-invariant Ha before spatial projection, never after it.
 ht=sum(d['H'],[]);qt=[]
 for a in d['H']:qt+=comm(a,comm(ht,a))
 S=orbit_op(d['S'],data);Q=orbit_op(qt,data);B=orbit_op([(x,z,c*(1 if a==2 else -.5)) for a,terms in enumerate(d['H']) for x,z,c in terms],data)
 rows=[]
 for name,O in [('S',S),('Q',Q),('B',B)]:
  src=O@g;mean=g@src;src-=mean*g;weights=(V.T@src)**2
  rows.append(dict(source=name,mean=float(mean),variance=float(src@src),lines=[dict(gap=float(E[i]-E[0]),weight=float(weights[i]),residual=float(np.linalg.norm(H@V[:,i]-E[i]*V[:,i]))) for i in range(1,len(E)) if weights[i]>1e-8]))
 sline=min(rows[0]['lines'],key=lambda r:r['gap']);qline=min(rows[1]['lines'],key=lambda r:r['gap']);bline=min(rows[2]['lines'],key=lambda r:r['gap'])
 assert abs(E[0]+38.19164989239814)<1e-9
 assert abs(sline['gap']-3.763565915973)<1e-8 and abs(sline['weight']-58.3365873118)<1e-6
 assert abs(qline['gap']-sline['gap'])<1e-9 and abs(qline['weight']-7094.98109499)<1e-5
 assert abs(bline['gap']-1.423237955386)<1e-8
 assert max(x['residual'] for row in rows for x in row['lines'])<1e-8
 identities=json.loads((PACK/'cubic_results/IDENTITIES.json').read_text())
 for name,digest in identities['source_sha256'].items():assert hashlib.sha256((PACK/name).read_bytes()).hexdigest()==digest,name
 for name,digest in identities['result_sha256'].items():assert hashlib.sha256((PACK/'cubic_results'/name).read_bytes()).hexdigest()==digest,name
 result=dict(status='PASS',physical8site_intertwiner_error=error,cube27_ground=float(E[0]),cube27_reduced_dimension=H.shape[0],responses=rows,frozen_large_results='SHA256 verified; not replayed by this short runner',scope='Supplied nativeH finite model development; physicalmeasurement, lightmass and thermodynamiclimit open')
 out=ROOT/'outputs/native_cubic_scalar_response/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
