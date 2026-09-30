"""Independent reviewer diagnostics; no author-runner imports, no theorem by sampling."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import itertools, math, json, resource, time, sys
from fractions import Fraction as Q
import numpy as np
resource.setrlimit(resource.RLIMIT_CPU,(30,31))
t0=time.process_time()
rng=np.random.default_rng(9302026)
results={}
# Unequal and zero length intervals, enumerate all allocations rather than primary convolution.
def allocations(total,parts):
 if parts==1:
  yield (total,); return
 for first in range(total+1):
  for tail in allocations(total-first,parts-1):yield (first,)+tail
count=0
for lengths in [(Q(0),Q(1,7),Q(6,7)),(Q(1,11),Q(3,11),Q(2,11),Q(5,11)),(Q(2),Q(3))]:
 for n in range(9):
  value=sum((math.prod(d**k/Q(math.factorial(k)) for d,k in zip(lengths,ks)) for ks in allocations(n,len(lengths))),Q(0))
  assert value==sum(lengths)**n/Q(math.factorial(n));count+=1
results['unequal_simplex_exact_cases']=count
# Arbitrary noncommuting matrices test redistribution signs independently of locality.
def herm():
 a=rng.normal(size=(7,7))+1j*rng.normal(size=(7,7));return a+a.conj().T
def comm(a,b):return a@b-b@a
energies=[herm() for _ in range(4)]
jumps=[rng.normal(size=(7,7))+1j*rng.normal(size=(7,7)) for _ in range(4)]
def diss(b,o):
 l=jumps[b];g=l.conj().T@l;return l.conj().T@o@l-(g@o+o@g)/2
h=sum(energies);res=[];wrong=[]
for a in range(4):
 direct=1j*comm(h,energies[a])+sum(diss(b,energies[a]) for b in range(4))
 p=diss(a,h)
 transfer=[1j*comm(energies[b],energies[a])+diss(b,energies[a])-diss(a,energies[b]) for b in range(4)]
 res.append(float(np.linalg.norm(direct-p-sum(transfer))))
 wrong.append(float(np.linalg.norm(direct-p+sum(transfer))))
 assert res[-1]<1e-10 and wrong[-1]>1
results['energy_balance_residuals']=res;results['wrong_transfer_sign_rejected']=wrong
# General weighted finite-band operators, coherent non-diagonal density and truncation.
N=43;weights=np.arange(1,N+1,dtype=float);v=rng.normal(size=N)+1j*rng.normal(size=N);v/=weights**3;v/=np.linalg.norm(v)
rho=np.outer(v,v.conj());a=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));a[np.abs(np.subtract.outer(np.arange(N),np.arange(N)))>4]=0
p=a+a.conj().T
c=float(np.linalg.norm(p/weights[None,:]**2,2));m4=float(np.sum(weights**4*np.abs(v)**2))
tails=[]
for r in [2,5,9,17,32]:
 cut=p.copy();cut[r:,:]=0;cut[:,r:]=0
 observed=float(abs(np.trace((p-cut)@rho)));bound=2*c*m4/r**2
 assert observed<=bound+1e-12;tails.append([r,observed,bound])
for s in [1,2,4]:
 o=a.copy();o[np.abs(np.subtract.outer(np.arange(N),np.arange(N)))>s]=0
 for u in [1,2,4]:
  norm=float(np.linalg.norm(weights[:,None]**u*o/weights[None,:]**u,2));bound=(2*s+1)*(1+s)**u*np.linalg.norm(o,2)
  assert norm<=bound
results['weighted_coherent_tails']=tails
# Inverse-star construction: contract outgoing hop from its final occupied B word.
words=list(itertools.product((-1,0,1),repeat=6));index={w:i for i,w in enumerate(words)}
phase=np.exp(1j*rng.uniform(-math.pi,math.pi,size=6));vectors=rng.normal(size=(2,len(words)))+1j*rng.normal(size=(2,len(words)))
f=np.zeros(len(words),dtype=complex)
for wi,w in enumerate(words):
 for d,q in enumerate(w):
  if not q:continue
  pre=list(w);pre[d]=0
  f[wi]+=phase[d]**(-q)*vectors[(q+1)//2,index[tuple(pre)]]
expected=sum(2*(6-sum(x!=0 for x in w))*abs(f[i])**2 for i,w in enumerate(words))
resolved=0.;coherent=0.
for b in range(6):
 outputs=[]
 for sigma in (-1,1):
  z=np.zeros((2,len(words)),dtype=complex)
  for wi,w in enumerate(words):
   if w[b]!=-sigma:continue
   pre=list(w);pre[b]=0
   z[(sigma+1)//2,wi]=phase[b]**sigma*f[index[tuple(pre)]]
  resolved+=float(np.vdot(z,z).real);outputs.append(z)
 coherent+=float(np.vdot(sum(outputs),sum(outputs)).real)
assert abs(resolved-expected)<1e-8 and abs(coherent-resolved)<1e-8
assert abs(resolved-expected/2)>100
results['inverse_star_phase_norms']={'resolved':resolved,'coherent':coherent,'weighted_F':expected,'factor_two_mutant_rejected':True}
results['scope']='Finite independent discriminators, not proof of infinite-volume theorem or initial 855 coefficients.'
results['cpu_seconds']=time.process_time()-t0;results['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
results['python']=sys.version;results['numpy']=np.__version__
print(json.dumps(results,indent=2))
