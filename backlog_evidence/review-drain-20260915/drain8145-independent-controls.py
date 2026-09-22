"""Independent synthetic controls; imports no submitted runner or scientific file.
Finite floating controls supplement, and do not prove, the reviewed analytic limits.
"""
import numpy as np
import itertools as it, math, json, hashlib, pathlib
checks=[]
def ck(name,v):
 assert bool(v),name
 checks.append(name)
# Construct cellular coboundaries independently from ternary cell words:
# 0/1 fixed coordinate, 2 oriented open interval.
cells={p:[x for x in it.product(range(3),repeat=4) if x.count(2)==p] for p in range(4)}
D=[]
for p in range(3):
 index={x:i for i,x in enumerate(cells[p])};a=np.zeros((len(cells[p+1]),len(cells[p])))
 for i,x in enumerate(cells[p+1]):
  for k,axis in enumerate(j for j,v in enumerate(x) if v==2):
   for endpoint in (0,1):
    y=list(x);y[axis]=endpoint;a[i,index[tuple(y)]]=(-1)**k*(2*endpoint-1)
 D.append(a)
ck('cube_d_squared',np.max(abs(D[1]@D[0]))==0 and np.max(abs(D[2]@D[1]))==0)
P=D[1]@np.linalg.pinv(D[1]);ck('electric_rank17',abs(np.trace(P)-17)<1e-11)
ck('all24_diagonals17over24',np.max(abs(np.diag(P)-17/24))<1e-11)
ck('signed_phase51over8',abs(9*P[0,0]-51/8)<1e-11 and math.cos(2*math.pi*9*P[0,0])<-.7)
# Scalar Poisson with a symmetric shifted mixture and a nontrivial coset.
for precision in (.8,2.7,6.):
 z=np.arange(-35,36);bs=np.array([0.,.21,-.21]);weights=np.array([.6,.2,.2]);chi=np.cos(2*np.pi*z[:,None]*bs)@weights
 base=np.exp(-precision*z*z/2)*chi;normal=base.sum()
 k=np.arange(-35,36)[:,None];res=k-bs;dual=weights*np.exp(-2*np.pi*np.pi*res**2/precision);dual/=dual.sum()
 for h in (-.7,.3,1.2):
  mgf=(base*np.exp(h*z)).sum()/normal
  rhs=np.exp(h*h/(2*precision))*np.sum(dual*np.cos(2*np.pi*h*res/precision))
  ck('poisson_mgf',abs(mgf-rhs)<1e-12);ck('centered_domination',mgf<=np.exp(h*h/(2*precision))+1e-12)
 for shift in (.13,.5):
  x=z+shift;num=np.sum(np.exp(-precision*x*x/2)*(np.cos(2*np.pi*x[:,None]*bs)@weights))
  ck('coset_k_not_residual',abs(num/normal-np.sum(dual*np.cos(2*np.pi*k*shift)))<1e-12)
# Supplied finite positive Fourier kernels distinct from authors' Villain fixtures.
# Square configurations; Fourier construction first, projected kernels separately
# obtained from vertex-group character sums.
records=[]
for N,w in [(2,np.array([3.,1.])),(3,np.array([4.,1.,1.]))]:
 states=np.array(list(it.product(range(N),repeat=4)));M=len(states)
 B=np.array([[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1]])
 F=np.exp(2j*np.pi*(states@states.T)/N)/math.sqrt(M)
 c=np.fft.fft(w).real/N;cp=np.prod(c[states],axis=1)
 C=(F*cp)@F.conj().T
 V=w[states.sum(1)%N];T=np.sqrt(V)[:,None]*C*np.sqrt(V)[None,:]
 eigen,Q=np.linalg.eigh(T);omega=Q[:,-1];omega*=np.conj(omega.sum())/abs(omega.sum());tau=T/eigen[-1]
 ck('positive_ground_state',omega.real.min()>0 and abs(np.linalg.norm(omega)-1)<1e-12)
 j=np.array([1,0,0,0]);loop=np.ones(4,dtype=int)
 def phase(x):return np.exp(2j*np.pi*(states@x)/N)
 def K(x):return math.prod(max(c/c[(np.arange(N)+q)%N]) for q in x)
 for x in [j,j-loop,2*j,np.zeros(4,dtype=int)]:
  psi=phase(x)*omega;inv=np.vdot(psi,np.linalg.solve(tau,psi)).real
  ck('inverse_local_ratio',inv<=K(x)+1e-10)
 # Charge projection is exact Fourier-sector selection, checked against gauge sum.
 profiles=(states@B)%N
 for x in [j,j-loop,np.array([1,0,1,0]),N*j]:
  rho=x@B;selected=np.all(profiles==rho%N,axis=1)
  Cr=(F[:,selected]*cp[selected])@F[:,selected].conj().T
  group=np.zeros_like(C)
  for eta in states:
   moved=(states+B@eta)%N;indices=np.ravel_multi_index(moved.T,(N,)*4)
   group+=C[indices,:]*np.exp(-2j*np.pi*(rho@eta)/N)/M
  ck('gauge_projector_vs_Fourier',np.max(abs(Cr-group))<1e-11)
  neutral=np.all(profiles==0,axis=1);C0=(F[:,neutral]*cp[neutral])@F[:,neutral].conj().T
  support=np.flatnonzero(rho%N);independent=max(sum(bits) for bits in it.product((0,1),repeat=len(support)) if all((u-v)%4 not in(1,3) for u,v in it.combinations([v for v,b in zip(support,bits) if b],2)))
  r=1-(min(w)/max(w))**2
  ck('pointwise_charge_floor',np.max(abs(Cr)-r**independent*C0.real)<1e-11)
  block=np.sqrt(V)[:,None]*Cr*np.sqrt(V)[None,:]
  ck('spectral_charge_floor',np.linalg.eigvalsh(block)[-1]<=r**independent*eigen[-1]+1e-10)
 # New words and endpoint strips; chronological updates use no submitted code.
 for insertions,times in [([j,loop,-loop],[2,1]),([loop,j],[3]),([2*j,-j],[1]),([j,-j],[2])]:
  total=sum(insertions);psi=phase(insertions[0])*omega;R=1.;elapsed=0;past=insertions[0].copy()
  for x,t in zip(insertions[1:],times):
   R*=K(total-past)**t;elapsed+=t
   psi=phase(x)*(np.linalg.matrix_power(tau,t)@psi);past+=x
  inv=np.vdot(psi,np.linalg.solve(tau,psi)).real
  ck('history_inverse',inv<=K(insertions[-1])+1e-9)
  ref=phase(total)*omega
  for n in (0,2,5):
   value=np.vdot(psi,np.linalg.matrix_power(tau,n)@psi).real
   base=np.vdot(ref,np.linalg.matrix_power(tau,n+2*elapsed)@ref).real
   ck('endpoint_two_caps_and_time',base/R**2-1e-10<=value<=base*R**2+1e-10)
 records.append({'N':N,'dimension':M,'kernel':w.tolist(),'min_transfer_eigenvalue':float(eigen[0])})
# Independently integrate the temporal resolvent on a dense one-dimensional grid.
theta=(np.arange(32768)+.5)*2*np.pi/32768
for lam in (.13,1.7,8.):
 for T in (1,3,8):
  geometric=sum(np.exp(1j*k*theta) for k in range(T))
  direct=np.mean(abs(geometric)**2/(lam+2-2*np.cos(theta)))
  root=math.sqrt(lam*(lam+4));r=(lam+2-root)/2
  formula=T/lam-2*(1-r**T)/(lam*root)
  ck('temporal_resolvent_integral',abs(direct-formula)<1e-10)
print(json.dumps({'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'checks':len(checks),'failed':0,'families':sorted(set(checks)),'transfer_fixtures':records,'scope':'finite independent synthetic algebra controls; no primary runs and no infinite-volume numerical proof'},indent=2))
