"""Mixed native C/local-energy spectral response by polarization."""
import json
from pathlib import Path
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;d=basis((3,3,3));terms=np.array(d['terms'],np.int64);H=lambda v:apply(v,*terms.T.copy());idx={x:i for i,x in enumerate(d['sites'])};ct=[];et=[]
for a in range(3):
 l=[1,1,1];r=[1,1,1];l[a]-=1;r[a]+=1
 for dest,ends in [(ct,[tuple(l),tuple(r)]),(et,[(1,1,1),tuple(l)]),(et,[(1,1,1),tuple(r)])]:
  mask=sum(1<<idx[x] for x in ends);coef=(-1 if a==1 else 1)*(1 if dest is ct else -1)
  dest.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,coef))
s=np.load(P/'stationary_3x3x3_plus.npz');g=s['vectors'][:,0];e0=s['values'][0]
C=lambda v:apply(v,*np.array(ct,np.int64).T.copy());E=lambda v:apply(v,*np.array(et,np.int64).T.copy())/2
cg=C(g);eg=E(g);vc=cg-g*np.dot(g,cg);ve=eg-g*np.dot(g,eg)
# Interior operator identity, tested on an independent random vector.
r=np.random.default_rng(871).normal(size=len(g));r/=np.linalg.norm(r)
identity_error=np.linalg.norm(C(r)-2*E(E(r))+3*r);assert identity_error<1e-12
def quadrature(v):
 weight=np.dot(v,v);q=v/np.sqrt(weight);prev=np.zeros_like(q);beta=0.;aa=[];bb=[];out={}
 for k in range(64):
  w=H(q)-e0*q-beta*prev;alpha=np.dot(q,w);w-=alpha*q;w-=g*np.dot(g,w);nxt=np.linalg.norm(w);aa.append(alpha)
  if k in [15,31,63]:
   T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);en,u=np.linalg.eigh(T)
   out[str(k+1)]={str(eta):float(weight*np.sum(u[0]**2*en/(en**2+eta**2))) for eta in [.1,.5,1.]}
  if k<63:bb.append(nxt)
  prev,q=q,w/nxt;beta=nxt
 return out
plus=quadrature(vc+ve);minus=quadrature(vc-ve)
mixed={n:{eta:(plus[n][eta]-minus[n][eta])/4 for eta in plus[n]} for n in plus}
prior=json.loads((P/'stationary_response.json').read_text())['responses']
for eta,m in mixed['64'].items():
 cc=prior['C']['regularized_inverse_moments']['64'][eta];ee=prior['e']['regularized_inverse_moments']['64'][eta]
 assert m*m<=cc*ee+1e-10
out=dict(equal_time_covariance=float(np.dot(vc,ve)),normalized_equal_time_overlap=float(np.dot(vc,ve)/np.linalg.norm(vc)/np.linalg.norm(ve)),interior_identity_error=float(identity_error),mixed_regularized_inverse_moments=mixed,scope='Finite selected-sector mixed spectral functional, not universal scalar coupling or independent empirical prediction; probe response does not add term to autonomous H')
(P/'stationary_mixed.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
