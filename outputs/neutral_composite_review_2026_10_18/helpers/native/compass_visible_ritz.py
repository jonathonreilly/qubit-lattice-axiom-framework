"""Reconstruct actual full-H vectors for visible Lanczos nodes and check residuals."""
import json
from pathlib import Path
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;d=basis((3,3,3));terms=np.array(d['terms'],np.int64);H=lambda v:apply(v,*terms.T.copy());idx={x:i for i,x in enumerate(d['sites'])};ct=[]
for a in range(3):
 l=[1,1,1];r=[1,1,1];l[a]-=1;r[a]+=1;mask=(1<<idx[tuple(l)])|(1<<idx[tuple(r)])
 ct.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,-1 if a==1 else 1))
s=np.load(P/'stationary_3x3x3_plus.npz');g=s['vectors'][:,0];e0=s['values'][0];cg=apply(g,*np.array(ct,np.int64).T.copy());v=cg-g*np.dot(g,cg)
r=json.loads((P/'stationary_response.json').read_text())['responses']['C'];a=np.array(r['lanczos_alpha']);b=np.array(r['lanczos_beta']);T=np.diag(a)+np.diag(b,1)+np.diag(b,-1);en,u=np.linalg.eigh(T)
chosen=np.flatnonzero(u[0]**2*np.dot(v,v)>1e-6)[:3];q=v/np.linalg.norm(v);prev=np.zeros_like(q);vectors=np.zeros((len(chosen),len(q)))
for j in range(64):
 vectors+=u[j,chosen,None]*q[None,:]
 if j==63:break
 w=H(q)-e0*q-a[j]*q-(b[j-1]*prev if j else 0);w-=g*np.dot(g,w);prev,q=q,w/b[j]
rows=[]
for i,k in enumerate(chosen):
 x=vectors[i];x/=np.linalg.norm(x);hx=H(x);ray=np.dot(x,hx);res=np.linalg.norm(hx-ray*x)
 rows.append(dict(lanczos_gap=float(en[k]),actual_rayleigh_gap=float(ray-e0),full_residual=float(res),source_weight=float(np.dot(x,v)**2),initial_overlap=float(np.dot(x,g)),norm=float(np.linalg.norm(x))))
np.savez_compressed(P/'stationary_visible_vectors.npz',vectors=vectors)
out=dict(rows=rows,scope='Actual finite selected-sector full-H residual checks; residual implies nearby finite eigenvalue, not thermodynamic particle/pole or unique mode')
(P/'stationary_visible_ritz.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
