"""Small actual-K2 smooth-split completion control; no author/helper imports."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import time,resource,signal,json,hashlib
from pathlib import Path
from itertools import product,combinations
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch'] and not(rt/'STOP_REQUESTED.json').exists()
resource.setrlimit(resource.RLIMIT_CPU,(10,15));signal.alarm(120);start=time.monotonic();cpu=time.process_time()
import numpy as np
L=9;V=L**3;kap=.8;lam=1.3
axes=((1,0,0),(0,1,0),(0,0,1));planes=list(combinations(range(3),2))
def add(x,y):return tuple((a+b)%L for a,b in zip(x,y))
def scale(x,s):return tuple(s*a for a in x)
rows=[];lookup={}
for c in product(range(L),repeat=3):
 es=[frozenset((add(c,e),add(c,scale(e,-1)))) for e in axes]+[frozenset((c,add(c,add(axes[i],scale(axes[j],s))))) for i,j in planes for s in (1,-1)]
 for a,e in enumerate(es):lookup[e]=len(rows);rows.append((c,a,e))
eta={(0,0,0),(2,0,0),(0,4,4),(2,4,4)};pins=[j for j,(_,_,e) in enumerate(rows) if e&eta];assert len(pins)==70
K=np.empty((L,L,L,9,9),complex);inv=np.empty_like(K);chi=np.empty((L,L,L))
E=np.array([[1,-1,0],[1,1,-2]],float)/np.sqrt(np.array([[2],[6]]))
for ns in product(range(L),repeat=3):
 k=np.array([2*np.pi*(n if n<=L//2 else n-L)/L for n in ns]);ell=4*np.sum(np.sin(k/2)**2);r=np.linalg.norm(k)
 # C-infinity step: zero below kap, one above2kap.
 t=(r-kap)/kap
 c=0. if t<=0 else 1. if t>=1 else np.exp(-1/t)/(np.exp(-1/t)+np.exp(-1/(1-t)))
 chi[ns]=c;q=np.zeros((5,9),complex);q[:2,:3]=E
 for p,(i,j) in enumerate(planes):
  for rr,s in enumerate((1,-1)):q[p+2,3+2*p+rr]=-s*(np.exp(-1j*s*k[j])+np.exp(-1j*k[i]))/2
 mat=2*np.eye(9)+q.conj().T@(np.array([-2+ell]*2+[-1+ell]*3)[:,None]*q)
 vals,U=np.linalg.eigh(mat);active=vals>1e-9;K[ns]=mat;inv[ns]=(U[:,active]/vals[active])@U[:,active].conj().T
Gker=np.fft.ifftn(chi[...,None,None]*inv,axes=(0,1,2))
cs=np.array([rows[j][0] for j in pins]);aa=np.array([rows[j][1] for j in pins]);d=(cs[:,None,:]-cs[None,:,:])%L
M=Gker[d[:,:,0],d[:,:,1],d[:,:,2],aa[:,None],aa[None,:]]
A=M+np.eye(len(pins))/lam
rng=np.random.default_rng(17419)
r=rng.normal(size=len(pins))+1j*rng.normal(size=len(pins));w=np.linalg.solve(A,r)
imp=np.zeros((L,L,L,9),complex)
for j,val in zip(pins,w):c,a,_=rows[j];imp[c+(a,)]=val
# Unitary FFT fixes all finite-volume normalization factors.
impk=np.fft.fftn(imp,axes=(0,1,2),norm='ortho')
vk=-np.einsum('...ab,...b->...a',inv,np.sqrt(chi)[...,None]*impk)
v=np.fft.ifftn(vk,axes=(0,1,2),norm='ortho')
rootv=np.fft.ifftn(np.sqrt(chi)[...,None]*vk,axes=(0,1,2),norm='ortho')
res=r+np.array([rootv[rows[j][0]+(rows[j][1],)] for j in pins])
energy=float(np.einsum('...a,...ab,...b->...',vk.conj(),K,vk).real.sum())
minimum=energy+lam*float(np.vdot(res,res).real);formula=float(np.vdot(r,w).real)
assert abs(minimum-formula)<1e-10
# An arbitrary actual forbidden-edge vector checks the retained kinetic term.
f=rng.normal(size=(L,L,L,9))+1j*rng.normal(size=(L,L,L,9))
for j in pins:c,a,_=rows[j];f[c+(a,)]=0
f/=np.linalg.norm(f);fk=np.fft.fftn(f,axes=(0,1,2),norm='ortho')
pk=(1-chi)[...,None]*fk;p=np.fft.ifftn(pk,axes=(0,1,2),norm='ortho')
rp=np.array([p[rows[j][0]+(rows[j][1],)] for j in pins])
full=float(np.einsum('...a,...ab,...b->...',fk.conj(),K,fk).real.sum())
low=float(np.einsum('...a,...ab,...b->...',fk.conj(),(1-chi)[...,None,None]*K,fk).real.sum())
cap=float(np.vdot(rp,np.linalg.solve(A,rp)).real)
assert full>=low+cap-1e-12
out={'scope':'Actual9-band K2 finite-volume filtered completion identity; floating support for analytic all-N lemma, not a phase/EOS check','L':L,'pins':len(pins),'cutoff':kap,'lambda':lam,'transition_modes':int(np.sum((chi>0)&(chi<1))),'completion_minimum':minimum,'inverse_formula':formula,'identity_absolute_error':abs(minimum-formula),'arbitrary_pinned_vector_energy':full,'retained_low_energy':low,'regularized_capacity':cap,'remaining_nonnegative_margin':full-low-cap,'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time()-cpu,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('filtered_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
