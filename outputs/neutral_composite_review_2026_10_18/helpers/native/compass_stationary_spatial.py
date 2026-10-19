"""Full-grid central C versus each existing local-energy source; conserved-sum control."""
import json
from pathlib import Path
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;d=basis((3,3,3));terms=np.array(d['terms'],np.int64);H=lambda v:apply(v,*terms.T.copy());idx={x:i for i,x in enumerate(d['sites'])}
s=np.load(P/'stationary_3x3x3_plus.npz');g=s['vectors'][:,0];e0=s['values'][0];ct=[]
for a in range(3):
 l=[1,1,1];r=[1,1,1];l[a]-=1;r[a]+=1;mask=(1<<idx[tuple(l)])|(1<<idx[tuple(r)])
 ct.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,-1 if a==1 else 1))
cg=apply(g,*np.array(ct,np.int64).T.copy());v=cg-g*np.dot(g,cg);norm=np.linalg.norm(v)
sources=np.empty((27,len(g)))
for x,i in idx.items():
 et=[]
 for a in range(3):
  for delta in [-1,1]:
   y=list(x);y[a]+=delta
   if tuple(y) not in idx:continue
   mask=(1<<i)|(1<<idx[tuple(y)])
   et.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
 eg=apply(g,*np.array(et,np.int64).T.copy())/2;sources[i]=eg-g*np.dot(g,eg)
uniform_error=np.linalg.norm(sources.sum(axis=0));assert uniform_error<1e-9
prev=np.zeros_like(v);q=v/norm;beta=0.;aa=[];bb=[];overlaps=[];rows={}
for k in range(64):
 overlaps.append(sources@q)
 w=H(q)-e0*q-beta*prev;alpha=np.dot(q,w);w-=alpha*q;w-=g*np.dot(g,w);nxt=np.linalg.norm(w);aa.append(alpha)
 if k in [15,31,63]:
  T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);en,u=np.linalg.eigh(T);row={}
  for eta in [.1,.5,1.]:
   frow=(u[0]*en/(en**2+eta**2))@u.T
   vals=norm*(frow@np.array(overlaps));assert abs(sum(vals))<1e-9
   row[str(eta)]=vals.tolist()
  rows[str(k+1)]=row
 if k<63:bb.append(nxt)
 prev,q=q,w/nxt;beta=nxt
mixed=json.loads((P/'stationary_mixed.json').read_text())
for eta in rows['64']:
 assert abs(rows['64'][eta][idx[(1,1,1)]]-mixed['mixed_regularized_inverse_moments']['64'][eta])<1e-8
out=dict(sites=d['sites'],uniform_connected_source_norm=float(uniform_error),spatial_regularized_inverse_moments=rows,scope='Finite open27site selected-sector centralC/energy cross response. Nonzero separated response is not a long-range law or universal gravity coupling.')
(P/'stationary_spatial.json').write_text(json.dumps(out,indent=2)+'\n');print(dict(uniform_error=float(uniform_error),eta01_values=rows['64']['0.1'],max_32_64_difference=max(abs(np.array(rows['32']['0.1'])-np.array(rows['64']['0.1'])))),flush=True)
