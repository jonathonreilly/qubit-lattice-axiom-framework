"""More resolved neutral spectral benchmark using existing conserved Y-pair symmetries."""
import sys,json,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer
P=Path(__file__).resolve().parent
D=basis((3,3,3));st=[]
for y in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[1] in [y,y+1]);st.append(D['reduce_term'](m,m,-1))
R=reducer(22,st,(1,1));terms=np.array([R['reduce'](t) for t in D['terms']],np.int64);H=lambda v:apply(v,*terms.T.copy())
s=np.load(P/'stationary_3x3x3_plus.npz');gfull=s['vectors'][:,0];e0=s['values'][0]
j=np.arange(R['dimension'],dtype=np.int64);r=np.zeros_like(j)
for k,f in enumerate(R['free']):r|=((j>>k)&1)<<f
from neutral_extra_sector import mul
groups=[(0,0,1),*st,mul(*st)];g=np.zeros(len(j))
for f,z,c in groups:
 parity=np.zeros_like(j)
 for b in range(22):
  if z>>b&1:parity^=(r>>b)&1
 g+=c*(1-2*parity)*gfull[r^f]/2
pn=float(g@g);g/=np.linalg.norm(g);del gfull,s,r,j
res=float(np.linalg.norm(H(g)-e0*g));assert abs(pn-1)<1e-10 and res<1e-9
idx={x:i for i,x in enumerate(D['sites'])};ct=[]
for a in range(3):
 l=[1,1,1];rr=[1,1,1];l[a]-=1;rr[a]+=1;m=(1<<idx[tuple(l)])|(1<<idx[tuple(rr)])
 ct.append(R['reduce'](D['reduce_term'](m if a!=2 else 0,m if a!=0 else 0,-1 if a==1 else 1)))
ct=np.array(ct,np.int64);C=lambda v:apply(v,*ct.T.copy());cg=C(g);v=cg-g*(g@cg);norm=np.linalg.norm(v)
prev=np.zeros_like(g);q=v/norm;beta=0;aa=[];bb=[];targets=[];rows=[];start=time.time()
for k in range(256):
 w=H(q)-e0*q-beta*prev;alpha=float(q@w);w-=alpha*q;w-=g*(g@w);nxt=float(np.linalg.norm(w));aa.append(alpha)
 if k in [63,127,255]:
  T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);en,u=np.linalg.eigh(T);weights=norm**2*u[0]**2
  chosen=np.flatnonzero((en>1e-6)&(weights>1e-8))[:3]
  rows.append(dict(steps=k+1,regularized_eta01=float(np.sum(weights*en/(en**2+.01))),nodes=[dict(gap=float(en[i]),weight=float(weights[i])) for i in chosen]))
  for i in chosen:targets.append((k+1,float(en[i]),u[:,i].copy()))
 if k<255:bb.append(nxt)
 prev,q=q,w/nxt;beta=nxt
# Two-pass reconstruction; no storage of all Krylov vectors.
vecs=np.zeros((len(targets),len(g)));prev=np.zeros_like(g);q=v/norm
for k in range(256):
 for i,(steps,en,coeff) in enumerate(targets):
  if k<steps:vecs[i]+=coeff[k]*q
 if k<255:
  w=H(q)-e0*q-(bb[k-1]*prev if k else 0)-aa[k]*q;w-=g*(g@w)
  prev,q=q,w/bb[k]
checks=[]
for vec,(steps,en,coeff) in zip(vecs,targets):
 raw=float(np.linalg.norm(vec));vec/=raw;hv=H(vec)-e0*vec;ray=float(vec@hv)
 checks.append(dict(steps=steps,tridiagonal_gap=en,rayleigh_gap=ray,residual=float(np.linalg.norm(hv-ray*vec)),raw_norm=raw,source_weight=float((vec@v)**2),ground_overlap=float(vec@g)))
out=dict(projection_norm_squared=pn,ground_residual=res,dimension=R['dimension'],krylov_rows=rows,reconstructed=checks,elapsed=time.time()-start,scope='Same finite27site state and H, extra exact symmetries, no bulk pole conclusion')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

np.savez_compressed(P/'stationary_extra_vectors.npz',ground=g,energy=e0,vectors=vecs[-3:])
