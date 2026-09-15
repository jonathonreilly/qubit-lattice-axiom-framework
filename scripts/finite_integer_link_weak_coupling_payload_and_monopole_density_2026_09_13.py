"""Author challenges for finite-link weak-coupling payload and defect bounds.

The positive-flow and chain arguments are analytic. Finite algebra checks
challenge them; no thermodynamic photon or charged spectrum is computed.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import hashlib,json,time,math
import numpy as np
import sympy as sy
from scipy import sparse as sp
from scipy.integrate import quad
AUDIT_TIMEOUT_SEC=90
AUDIT_INPUT_PATHS=("docs/FINITE_INTEGER_LINK_WEAK_COUPLING_PAYLOAD_AND_MONOPOLE_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-13.md",)
MONOPOLE_CUBE_FACTOR=4/3
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def close(name,a,b,tol=2e-10,**detail):
 error=float(np.max(abs(np.asarray(a)-np.asarray(b))));check(name,error<tol,error=error,**detail)
def sparsemax(a):return float(max(abs(a.data),default=0))
def cube():
 verts=list(product(range(2),repeat=3));edges=[]
 for x in verts:
  for i in range(3):
   if x[i]==0:
    y=list(x);y[i]=1;edges.append((x,tuple(y)))
 ei={e:j for j,e in enumerate(edges)};D=np.zeros((8,12),int)
 for j,(x,y) in enumerate(edges):D[verts.index(x),j]=1;D[verts.index(y),j]=-1
 B=np.zeros((12,6),int);faces=[]
 for normal in range(3):
  ij=[i for i in range(3) if i!=normal]
  for side in [0,1]:
   x=[0,0,0];x[normal]=side;i,j=ij;v0=tuple(x);xx=x.copy();xx[i]=1;v1=tuple(xx);xx[j]=1;v2=tuple(xx);xx[i]=0;v3=tuple(xx)
   sign=(1 if side else -1)*(1 if normal!=1 else -1);face=len(faces);faces.append((normal,side))
   for a,b in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
    if (a,b) in ei:B[ei[(a,b)],face]=sign
    else:B[ei[(b,a)],face]=-sign
 return D,B

def periodic(L):
 cells=list(product(range(L),repeat=3));edges=[(x,i) for x in cells for i in range(3)];faces=[(x,i,j) for x in cells for i,j in [(0,1),(0,2),(1,2)]]
 ci={x:n for n,x in enumerate(cells)};ei={x:n for n,x in enumerate(edges)};pi={x:n for n,x in enumerate(faces)}
 def move(x,i):y=list(x);y[i]=(y[i]+1)%L;return tuple(y)
 D=np.zeros((L**3,3*L**3),int);B=np.zeros((3*L**3,3*L**3),int);C=np.zeros((L**3,3*L**3),int)
 for n,(x,i) in enumerate(edges):D[ci[x],n]=1;D[ci[move(x,i)],n]=-1
 for n,(x,i,j) in enumerate(faces):
  for edge,sign in [((x,i),1),((move(x,i),j),1),((move(x,j),i),-1),((x,j),-1)]:B[ei[edge],n]=sign
 for n,x in enumerate(cells):
  for face,sign in [((move(x,0),1,2),1),((x,1,2),-1),((move(x,1),0,2),-1),((x,0,2),1),((move(x,2),0,1),1),((x,0,1),-1)]:C[n,pi[face]]=sign
 return D,B,C

def incidence_and_monopoles():
 rng=np.random.default_rng(13093)
 for L in [3,4]:
  D,B,C=periodic(L)
  close('periodic boundary of plaquette has zero divergence',D@B,0,L=L)
  close('periodic cube Bianchi identity',C@B.T,0,L=L)
  close('four plaquettes per link',np.sum(abs(B),axis=1),4,L=L)
  close('four links per plaquette',np.sum(abs(B),axis=0),4,L=L)
  close('two cubes per plaquette',np.sum(abs(C),axis=0),2,L=L)
  close('six plaquettes per cube',np.sum(abs(C),axis=1),6,L=L)
  for trial in range(8):
   angles=rng.uniform(-np.pi,np.pi,3*L**3);raw=B.T@angles;principal=(raw+np.pi)%(2*np.pi)-np.pi;charge=C@principal/(2*np.pi);q=np.rint(charge)
   close('integer cube charge from principal wrapping',charge,q,L=L,trial=trial)
   close('total monopole neutrality on torus',q.sum(),0,L=L,trial=trial)
   deficit=1-np.cos(principal);cube_energy=abs(C)@deficit
   check('pointwise cube monopole-energy inequality',np.all(cube_energy>=MONOPOLE_CUBE_FACTOR*q*q-1e-11),L=L,trial=trial,min_slack=float(np.min(cube_energy-MONOPOLE_CUBE_FACTOR*q*q)))
   check('each plaquette counted twice in global bound',float(np.sum(q*q))<=1.5*np.sum(deficit)+1e-10,L=L,trial=trial)
   check('monopole indicator below square charge',np.all((q!=0)<=q*q),L=L,trial=trial)
 D,B=cube();check('cube curl rank five',sy.Matrix(B).rank()==5);close('closed oriented cube relation',B.sum(axis=1),0)
 target=sy.Matrix([-sy.Rational(5,3)]+[sy.Rational(1,3)]*5);theta=sy.linsolve((sy.Matrix(B).T,target));sol=next(iter(theta));parameters=set().union(*(x.free_symbols for x in sol));sol=sy.Matrix([x.subs({p:0 for p in parameters}) for x in sol]);check('exact interior charge-one angle witness',sy.Matrix(B).T*sol==target)
 wrapped=(np.array(target,float).ravel()*np.pi+np.pi)%(2*np.pi)-np.pi
 close('charge-one witness has all outward principal faces pi/3',wrapped,np.pi/3)
 close('charge-one open region exists',wrapped.sum()/(2*np.pi),1)
 q2faces=np.array([np.pi-.01]*3+[np.pi/3+.01]*3);q2=q2faces.sum()/(2*np.pi);energy=np.sum(1-np.cos(q2faces))
 close('interior charge-two face fixture',q2,2)
 check('charge-two fixture challenges cube energy factor',energy>=MONOPOLE_CUBE_FACTOR*q2*q2 and energy<8,energy=float(energy),q=float(q2))


def chain_spectrum():
 for S in [0,1,2,4]:
  d=2*S+1;u=sp.diags(np.ones(d-1),-1,shape=(d,d),format='csr');W=sp.kron(sp.kron(u,u.T),sp.kron(u,u.T),format='csr');A=(W+W.T)/2
  expected=np.cos(np.pi/(2*S+2))
  maximum=0. if S==0 else float(sp.linalg.eigsh(A,k=1,which='LA',return_eigenvectors=False)[0])
  close('compressed plaquette maximum chain eigenvalue',maximum,expected,S=S)
  for n in range(1,2*S+2):
   adj=(np.diag(np.ones(n-1),1)+np.diag(np.ones(n-1),-1))/2
   close('all finite chain eigenvalues',np.linalg.eigvalsh(adj),np.sort(np.cos(np.arange(1,n+1)*np.pi/(n+1))),S=S,n=n)
  e=np.arange(-S,S+1);weights=np.cos(np.pi*e/(2*S+2));weights/=np.linalg.norm(weights);maxchain=sp.diags(np.ones(d-1),-1,shape=(d,d)).toarray();value=weights@((maxchain+maxchain.T)/2)@weights
  close('maximal neutral plaquette-flow chain saturates bound',value,expected,S=S)
  check('explicit spectral deficit lower estimate',1-expected>=1/(2*(S+1)**2)-1e-12,S=S)


def positive_trial():
 D,B=cube()
 for M in [0,1,2]:
  kappa=np.pi/(2*M+2);amplitudes=defaultdict(float)
  for n in product(range(-M,M+1),repeat=6):amplitudes[tuple(B@np.array(n))]+=float(np.prod(np.cos(kappa*np.array(n))))
  norm=sum(a*a for a in amplitudes.values());check('positive-flow state nonzero',norm>0,M=M)
  flux=np.array(list(amplitudes));close('every supported flow obeys Gauss',flux@D.T,0,M=M)
  check('volume-local flux support bound',np.max(abs(flux))<=2*M,M=M) # cube has two incident faces per edge
  if M:
   check('redundancy changes product norm',abs(norm-(M+1)**6)>1,M=M,norm=norm,product_norm=(M+1)**6)
  for p in range(6):
   b=B[:,p];numerator=0.;slack=math.inf
   for e,a in amplitudes.items():
    plus=amplitudes.get(tuple(np.array(e)+b),0);minus=amplitudes.get(tuple(np.array(e)-b),0);numerator+=a*minus;slack=min(slack,plus+minus-2*np.cos(kappa)*a)
   check('positive push-forward recurrence despite redundant cycles',slack>-1e-10,M=M,plaquette=p,minimum_slack=float(slack))
   value=numerator/norm;check('plaquette trial expectation lower bound',value>=np.cos(kappa)-1e-12,M=M,plaquette=p,actual=value,bound=float(np.cos(kappa)))
  if M==1:
   close('exact redundant-cube norm certificate',norm,2561/32)
   close('exact redundant-cube plaquette certificate',value,1345*np.sqrt(2)/2561)
 # Independent exact rational-radical push-forward at M=1.
 aexact=defaultdict(lambda:sy.S(0))
 for n in product([-1,0,1],repeat=6):aexact[tuple(B@np.array(n))]+= (sy.sqrt(2)/2)**sum(v!=0 for v in n)
 exact_norm=sy.simplify(sum(a*a for a in aexact.values()));check('rational-radical norm independent of float accumulation',exact_norm==sy.Rational(2561,32))
 numerator=sy.simplify(sum(a*aexact.get(tuple(np.array(e)-B[:,0]),sy.S(0)) for e,a in aexact.items()))
 check('exact algebraic plaquette overlap',sy.simplify(numerator/exact_norm-1345*sy.sqrt(2)/2561)==0)
 for M in [0,1,2,5]:
  kappa=np.pi/(2*M+2)
  def f(n):return np.cos(kappa*n) if abs(n)<=M else 0.
  for n in range(-M-2,M+3):
   residual=f(n-1)+f(n+1)-2*np.cos(kappa)*f(n)
   check('auxiliary cosine recurrence has only positive outer residual',residual>=-1e-12 and (abs(residual)<1e-12 or abs(n)==M+1),M=M,n=n)


def annihilator(j):
 rr=[];cc=[];vv=[]
 for state in range(256):
  if state>>j&1:rr.append(state^(1<<j));cc.append(state);vv.append((-1)**((state&((1<<j)-1)).bit_count()))
 return sp.csr_matrix((vv,(rr,cc)),shape=(256,256),dtype=complex)

def charged_norm():
 sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)];I=np.eye(2);S=[np.kron(I,s) for s in sig];sb=.8;cb=.6;mu=.2;zeta=.6
 on=(2+zeta)*S[2]+mu*np.kron(sig[0],sb*sig[0]+cb*sig[2]);C=[-sb*S[0]-cb*S[2],-S[2],-S[2]];Ss=[np.kron(sig[2],cb*sig[0]-sb*sig[2]),S[1],np.zeros((4,4))];hops=[(c-1j*s)/2 for c,s in zip(C,Ss)]
 check('onsite product filling is two negative orbitals',np.count_nonzero(np.linalg.eigvalsh(on)<0)==2)
 cs=[annihilator(j) for j in range(8)];Nx=np.array([(s&15).bit_count() for s in range(256)])
 for axis,T in enumerate(hops):
  q=np.linalg.svd(T,compute_uv=False).sum();close('actual carrier bond nuclear norm',q,2,axis=axis)
  F=sp.csr_matrix((256,256),dtype=complex)
  for i,j in product(range(4),repeat=2):F+=T[i,j]*(cs[i].conj().T@cs[4+j])
  close('Hermitian CAR bond norm equals nuclear norm',np.linalg.eigvalsh((F+F.conj().T).toarray())[-1],q,axis=axis)
  d=7;u=sp.diags(np.ones(d-1),-1,shape=(d,d),format='lil');u[0,d-1]=1;u=u.tocsr();V=sp.csr_matrix((256*d,256*d),dtype=complex)
  for n in range(5):V+=sp.kron(sp.diags((Nx==n).astype(float)),u**n,format='csr')
  actual=V@sp.kron(F,sp.eye(d),format='csr')@V.conj().T
  check('controlled unitary shift proves bond comparison',sparsemax(actual-sp.kron(F,u,format='csr'))<1e-12,axis=axis)
  # This cyclic unitary is solely a finite test of the norm identity; the
  # physical hard cutoff below has no wrap-around link.
  for cutoff in [0,1,2]:
   d=2*cutoff+1;u=sp.diags(np.ones(d-1),-1,shape=(d,d),format='csr');A=sp.kron(F,u,format='csr');H=A+A.conj().T
   val=0. if cutoff==0 else float(sp.linalg.eigsh(H,k=1,which='LA',return_eigenvectors=False)[0])
   check('hard-cutoff Hermitian bond norm bounded by full rotor',val<=q+1e-10,axis=axis,cutoff=cutoff,actual=val)


def q2_fourier(m,n):
 if m==0 and n==0:return .25
 if n==0:return ((-1.)**m-1)/(2*np.pi*np.pi*m*m)
 def v(k):return 0. if k==0 else (1-(-1.)**k)/k
 return (-1.)**n*(v(m)-v(m-n))/(2*np.pi*np.pi*n)
def q_fourier(m,n):
 if m==0 and n==0:return 0j
 if n==0:return -1j*(-1.)**m/(2*np.pi*m)
 return -1j*(-1.)**n*((m==0)-(m==n))/(2*np.pi*n)

def compressed_povm():
 # Two-angle closed-face section (x,y,-x-y,0,0,0), not a full cubic simulation.
 for m,n in product(range(-2,3),repeat=2):
  def inner(x):return x if n==0 else (np.exp(1j*n*np.pi)-np.exp(1j*n*(np.pi-x)))/(1j*n)
  re=quad(lambda x:float(np.real(np.exp(1j*m*x)*inner(x))),0,np.pi,epsabs=1e-12)[0]
  im=quad(lambda x:float(np.imag(np.exp(1j*m*x)*inner(x))),0,np.pi,epsabs=1e-12)[0]
  close('exact monopole-square Fourier coefficient versus integration',q2_fourier(m,n),re/(2*np.pi*np.pi),m=m,n=n)
  close('exact signed monopole Fourier coefficient versus integration',q_fourier(m,n),1j*im/(2*np.pi*np.pi),m=m,n=n)
 for cutoff in [0,1,2]:
  states=list(product(range(-cutoff,cutoff+1),repeat=2));d=len(states);M=np.empty((d,d),complex);Q=M.copy();H=np.zeros((d,d),complex)
  for i,a in enumerate(states):
   for j,b in enumerate(states):
    m,n=b[0]-a[0],b[1]-a[1];M[i,j]=q2_fourier(m,n);Q[i,j]=q_fourier(m,n)
    H[i,j]=3*(m==0 and n==0)-.5*((m,n) in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)])
  mineig=float(np.linalg.eigvalsh(M).min());check('finite angle monopole effect positive definite in section',mineig>0,cutoff=cutoff,minimum_eigenvalue=mineig)
  check('compression preserves monopole-energy inequality',np.linalg.eigvalsh(H-MONOPOLE_CUBE_FACTOR*M).min()>-1e-12,cutoff=cutoff)
  gap=M-Q@Q;check('compressing square exceeds square of compression',np.linalg.eigvalsh(gap).min()>-1e-12 and np.trace(gap).real>1e-4,cutoff=cutoff)
  close('mean-square POVM trace normalization',np.trace(M),d/4,cutoff=cutoff)
 for cutoff in [0,1,3]:
  d=2*cutoff+1;ns=np.arange(-cutoff,cutoff+1);angles=2*np.pi*np.arange(d)/d;frame=np.exp(-1j*ns[:,None]*angles[None,:])
  close('finite phase POVM integrates to identity',frame@frame.conj().T/d,np.eye(d),cutoff=cutoff)


def scaling_and_scope():
 for g,w,r in [(1.,np.ones(3),1.),(.3,np.array([.3,1.2,2.]),.8),(.03,np.ones(3),1.),(.001,np.array([.4,.9,1.7]),2.)]:
  M=math.ceil(1/g);S=4*M;ws=w.sum();wm=w.min();kap=np.pi/(2*M+2);B=ws*(8*g*g*M*M+(1-np.cos(kap))/(g*g))+6*r;coarse=ws*(32+np.pi*np.pi/8)+6*r
  check('uniform positive-flow ground-state constant',B<=coarse+1e-10,g=g,M=M,constant=B,coarse=coarse)
  floor=ws*(1-np.cos(np.pi/(2*S+2)));upper=g*g*B
  check('necessary and sufficient deficit windows compatible',floor<=upper,g=g,cutoff=S,lower=floor,upper=upper)
  check('encoding payload logarithmic at chosen cutoff',math.ceil(math.log2(2*S+1))<=math.ceil(math.log2(1/g))+5,g=g,S=S)
  close('monopole density coefficient follows plaquette counting',1.5*upper/wm,3*g*g*B/(2*wm),g=g)
 # Exact density alone permits long-distance two-point order.
 b=np.array([[0,1],[0,0]],complex);n=b.conj().T@b;N=np.kron(n,np.eye(2))+np.kron(np.eye(2),n)
 for density in [.2,.01,.00001]:
  state=np.array([np.sqrt(1-density),np.sqrt(density)]);rho=np.zeros((4,4),complex)
  for phase in [0,np.pi/2,np.pi,3*np.pi/2]:
   v=state*np.array([1,np.exp(1j*phase)]);v=np.kron(v,v);rho+=np.outer(v,v.conj())/4
  close('phase-averaged counterexample preserves number symmetry',N@rho-rho@N,0)
  close('arbitrarily small local density',np.trace(rho@np.kron(n,np.eye(2))),density)
  close('small density retains separated-site order',np.trace(rho@np.kron(b.conj().T,b)),density*(1-density))
 for beta in [.01,.4,3.]:
  energies=np.array([0.,.2,.7,1.3,2.1]);p=np.exp(-beta*energies);p/=p.sum();entropy=-sum(p*np.log(p));energy=p@energies
  check('thermal energy excess bounded by entropy dimension',energy<=math.log(len(energies))/beta, beta=beta)
  close('Gibbs energy-free-energy-entropy identity',energy+np.log(np.sum(np.exp(-beta*energies)))/beta,entropy/beta)


def main():
 start=time.monotonic();incidence_and_monopoles();chain_spectrum();positive_trial();charged_norm();compressed_povm();scaling_and_scope()
 for label,msg in [
 ('per_element','exact finite shift-chain spectral ceiling and phase-POVM normalization checked'),
 ('per_site','onsite neutral filling and the sharper charged-bond CAR norm checked'),
 ('per_mode','finite chain eigenmodes and local Fourier-compressed defect operators checked; photon spectrum unproved'),
 ('per_block','redundant cube-flow trial, exact overlap, monopole energy and square-compression distinction checked'),
 ('lattice_wide','finite periodic incidence and counting checked; uniform-volume bounds are analytic, thermodynamic phase not executed')]:print(label+': '+msg)
 print(json.dumps(dict(status='PASS',author_check_count=len(rows),checks=rows,elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claim_limit='Ground-state plaquette deficit and specified monopole-POVM bounds in the supplied hard integer-link family; no photon phase, charged spectrum or axiom update.'),indent=2))
 print('TOTAL: PASS='+str(len(rows))+' FAIL=0')
if __name__=='__main__':main()
