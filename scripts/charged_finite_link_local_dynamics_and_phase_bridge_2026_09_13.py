"""Author challenges of finite-link dynamics and specified phase weights.

Analytic bounds and exact matrix coefficients carry the claims; finite fixtures
challenge signs, boundary terms, factors and symmetry. No phase certification.
"""
from pathlib import Path
import hashlib,json,time,math,itertools
import numpy as np
import sympy as sy
import mpmath as mp
from scipy.linalg import expm
from scipy import sparse as sp
AUDIT_TIMEOUT_SEC=90
AUDIT_INPUT_PATHS=("docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md",)
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def close(name,a,b,tol=2e-10,**detail):
 error=float(np.max(abs(np.asarray(a)-np.asarray(b))));check(name,error<tol,error=error,**detail)
def norm(a):return float(np.linalg.norm(a,2))
def max_sparse(a):return float(max(abs(a.data),default=0))
I2=np.eye(2);sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
Sg=[np.kron(I2,s) for s in sig];TR=np.kron(sig[0],I2)
def carrier(sb=.8,cb=.6,zeta=.6,mu=.2):
 on=(2+zeta)*Sg[2]+mu*np.kron(sig[0],sb*sig[0]+cb*sig[2])
 C=[-sb*Sg[0]-cb*Sg[2],-Sg[2],-Sg[2]]
 S=[np.kron(sig[2],cb*sig[0]-sb*sig[2]),Sg[1],np.zeros((4,4))]
 return on,[(c-1j*s)/2 for c,s in zip(C,S)]
def rotor(K):
 e=np.arange(-K,K+1);u=np.diag(np.ones(2*K),-1);return e,u

def link_algebra():
 for K in [1,2,3,5]:
  e,u=rotor(K);E=np.diag(e);d=len(e);I=np.eye(d);pp=np.diag((e==K).astype(float));pm=np.diag((e==-K).astype(float))
  close('exact hard-cutoff electric commutator',E@u-u@E,u,K=K)
  close('upper endpoint unitarity defect',u.T@u,I-pp,K=K)
  close('lower endpoint unitarity defect',u@u.T,I-pm,K=K)
  cyc=u.copy();cyc[0,-1]=1
  check('cyclic unitary violates electric commutator',norm(E@cyc-cyc@E-cyc)>1,K=K)
  close('trace contradiction for finite unitary shift',np.trace(cyc.T@E@cyc),np.trace(E),K=K)
  check('positive trace shift impossible',abs(np.trace(E+I)-np.trace(E))==d,K=K)
  check('qubit encoding dimension',2**math.ceil(math.log2(d))>=d,K=K)


def annihilator(j,n=8):
 rr=[];cc=[];vv=[]
 for state in range(1<<n):
  if state>>j&1:
   rr.append(state^(1<<j));cc.append(state);vv.append((-1)**((state&((1<<j)-1)).bit_count()))
 return sp.csr_matrix((vv,(rr,cc)),shape=(1<<n,1<<n),dtype=complex)

def physical_carrier():
 on,hops=carrier();cs=[annihilator(j) for j in range(8)];ns=[c.conj().T@c for c in cs];IF=sp.eye(256,format='csr')
 hon=sp.csr_matrix((256,256),dtype=complex)
 for x in range(2):
  for i,j in itertools.product(range(4),repeat=2):hon+=on[i,j]*(cs[4*x+i].conj().T@cs[4*x+j])
 permutation=[2,3,0,1,6,7,4,5];rr=[];vv=[]
 for state in range(256):
  seq=[permutation[i] for i in range(8) if state>>i&1]
  inversion=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
  rr.append(sum(1<<j for j in seq));vv.append((-1)**inversion)
 TF=sp.csr_matrix((vv,(rr,list(range(256)))),shape=(256,256))
 close('onsite ordinary time reversal',TR@on.conj()@TR,on)
 close('Fock antiunitary squares to one',(TF@TF.T-sp.eye(256)).toarray(),np.zeros((256,256)))
 for axis,hop in enumerate(hops):
  close('hopping ordinary time reversal',TR@hop.conj()@TR,hop,axis=axis)
  singular=np.linalg.svd(hop,compute_uv=False)
  close('nuclear hopping norm',singular.sum(),2,axis=axis)
  close('hopping singular values',singular,[1,1,0,0] if axis<2 else [.5]*4,axis=axis)
  F=sp.csr_matrix((256,256),dtype=complex)
  for i,j in itertools.product(range(4),repeat=2):F+=hop[i,j]*(cs[i].conj().T@cs[4+j])
  actual=float(np.sqrt(sp.linalg.eigsh(F.conj().T@F,k=1,which='LA',return_eigenvectors=False)[0]))
  check('CAR bilinear bounded by nuclear norm',actual<=2+1e-10,actual=actual,axis=axis)
  for K in [1,2]:
   e,u=rotor(K);d=len(e);V=sp.kron(F,u,format='csr');H=sp.kron(hon,np.eye(d),format='csr')+V+V.conj().T+sp.kron(IF,np.diag(.37*e*e),format='csr')
   nx=np.array([sum((state>>j)&1 for j in range(4)) for state in range(256)])
   ny=np.array([sum((state>>j)&1 for j in range(4,8)) for state in range(256)])
   gx=np.tile(e,256)-np.repeat(nx-2,d);gy=-np.tile(e,256)-np.repeat(ny-2,d)
   co=H.tocoo()
   close('exact charged Gauss commutator x',(gx[co.row]-gx[co.col])*co.data,0,axis=axis,K=K)
   close('exact charged Gauss commutator y',(gy[co.row]-gy[co.col])*co.data,0,axis=axis,K=K)
   phys=np.flatnonzero((gx==0)&(gy==0));check('nonempty physical sector dimension',len(phys)==(68 if K==1 else 70),dimension=len(phys),K=K,axis=axis)
   TT=sp.kron(TF,np.eye(d),format='csr');check('full matter link antiunitary invariance',max_sparse(TT@H.conj()@TT.T-H)<1e-10,axis=axis,K=K)
   pp=np.zeros(H.shape[0]);pp[phys]=1;rho=sp.diags(pp/len(phys));U=sp.kron(IF,u,format='csr')
   close('open link vanishes in physical mixed state',(rho@U).diagonal().sum(),0,axis=axis,K=K)
   hp=H[phys][:,phys].toarray();gibbs=expm(-.23*hp);check('physical Gibbs state positive',np.linalg.eigvalsh(gibbs).min()>0,axis=axis,K=K)
 # Pure-gauge plaquette with distinct links and its flux-basis positivity.
 e,u=rotor(1);vals=list(itertools.product(e,repeat=4));E=np.array(vals);W=u
 for _ in range(3):W=np.kron(W,u)
 div=np.stack([E[:,0]-E[:,3],E[:,1]-E[:,0],E[:,2]-E[:,1],E[:,3]-E[:,2]],axis=1)
 for x in range(4):close('plaquette commutes with vertex Gauss',(div[:,x,None]-div[None,:,x])*W,0,vertex=x)
 Hp=np.diag(.2*(E*E).sum(axis=1))-.7*(W+W.T)
 check('pure gauge positive flux representation remains live',np.min(expm(-.1*Hp))>-1e-13)


def exponential_bounds():
 rng=np.random.default_rng(12093);K=7;e,u=rotor(K);d=len(e);env=2
 B0=np.array([[.19,.31j],[.11-.07j,-.13]],complex);J=norm(B0)
 B=np.kron(u,B0);Ef=np.repeat(e,env);P0=np.flatnonzero(abs(Ef)<=0)
 blocks=[]
 for n in e:
  v=rng.normal(size=(env,env))+1j*rng.normal(size=(env,env));blocks.append((v+v.conj().T)/3)
 for electric in [.0,.17,19.0]:
  R=np.zeros((d*env,d*env),complex)
  for j,n in enumerate(e):R[env*j:env*(j+1),env*j:env*(j+1)]=blocks[j]+electric*n*n*np.eye(env)
  H=R+B+B.conj().T
  close('raising decomposition with entangled environment',(Ef[:,None]-Ef[None,:])*B,B,electric=electric)
  for t in [.13,.7,1.4]:
   U=expm(-1j*t*H)
   for lam in [.2,.7,1.1]:
    weights=np.exp(lam*Ef);Hw=(weights[:,None]*H)/weights[None,:]
    anti=(Hw-Hw.conj().T)/(2j)
    check('weighted generator growth bound',norm(anti)<=2*J*np.sinh(lam)+1e-10,electric=electric,lambda_=lam)
    growth=norm((weights[:,None]*U)/weights[None,:]);bound=np.exp(2*J*t*np.sinh(lam))
    check('weighted evolution bound',growth<=bound+2e-8,electric=electric,time=t,lambda_=lam,actual=growth,bound=bound)
    for L in [1,3,5]:
     one=np.exp(-lam*L+2*J*t*np.sinh(lam))
     for sign in [-1,1]:
      ind=np.flatnonzero(sign*Ef>=L);value=norm(U[np.ix_(ind,P0)])
      check('one-sided low-flux leakage bound',value<=one+1e-11,electric=electric,time=t,L=L,sign=sign,actual=value,bound=one)
     ind=np.flatnonzero(abs(Ef)>=L);value=norm(U[np.ix_(ind,P0)])
     check('orthogonal two-tail bound',value<=np.sqrt(2)*one+1e-11,electric=electric,time=t,L=L)
   for cutoff in [0,1,2,4]:
    p=np.flatnonzero(abs(Ef)<=cutoff);hs=H[np.ix_(p,p)];us=expm(-1j*t*hs);embed=np.zeros_like(U[:,P0]);loc=[list(p).index(v) for v in P0];embed[p,:]=us[:,loc]
    error=norm(U[:,P0]-embed);lam=1.;bound=2*t*J*np.exp(-lam*cutoff+2*J*t*np.sinh(lam))
    check('Duhamel Hamiltonian cutoff bound',error<=bound+2e-11,electric=electric,time=t,cutoff=cutoff,actual=error,bound=bound)
 e0,u0=rotor(4);H0=.7*(u0+u0.T);t0=.0001;initial=np.flatnonzero(e0==0);full0=expm(-1j*t0*H0)[:,initial];embedded0=np.eye(9)[:,initial]
 err0=norm(full0-embedded0);bound0=2*t0*.7*np.exp(2*.7*t0*np.sinh(1))
 check('coincident outward boundaries require safe prefactor',err0<=bound0 and err0>1.4*.7*t0,actual=err0,bound=bound0)
 # Multi-link term: one shift can hit both boundaries; counting it once per
 # incident link is deliberately an upper bound, not cancellation.
 K=4;e,u=rotor(K);d=len(e);E=np.array(list(itertools.product(e,e)));U1=np.kron(u,np.eye(d));U2=np.kron(np.eye(d),u)
 Vs=[.31*U1,.23*U2,.41*U1@U2.T];H=np.diag(.29*E[:,0]**2+.57*E[:,1]**2)+sum((v+v.T for v in Vs));Js=np.array([.72,.64]);p0=np.flatnonzero(np.all(E==0,axis=1))
 for t in [.2,.6,1.1]:
  full=expm(-1j*t*H)
  for cutoff in [1,2,3]:
   p=np.flatnonzero(np.max(abs(E),axis=1)<=cutoff);us=expm(-1j*t*H[np.ix_(p,p)]);embedded=np.zeros((d*d,1),complex);embedded[p,0]=us[:,list(p).index(p0[0])]
   error=norm(full[:,p0]-embedded);bound=2*t*np.sum(Js*np.exp(-cutoff+2*Js*t*np.sinh(1)))
   check('simultaneous-boundary multi-link bound',error<=bound+1e-10,time=t,cutoff=cutoff,actual=error,bound=bound)
 # Analytic optimization and sufficient cutoff criterion.
 for J,t,dist in [(.3,.7,4),(.8,2.,5),(1.7,.1,3)]:
  lam=np.arccosh(dist/(2*J*t));closed=-dist*np.arccosh(dist/(2*J*t))+np.sqrt(dist*dist-(2*J*t)**2)
  close('optimized Chernoff exponent',-lam*dist+2*J*t*np.sinh(lam),closed)
  close('stationary optimized exponent',-dist+2*J*t*np.cosh(lam),0)
 for N,J,t,eps in [(3,.2,.7,1e-3),(120,.4,2.,1e-6),(1,.01,.1,.9)]:
  cutoff=max(0,math.ceil(2*J*t*np.sinh(1)+np.log(2*N*J*t/eps)))
  bound=2*N*J*t*np.exp(-cutoff+2*J*t*np.sinh(1))
  check('sufficient integer cutoff',bound<=eps+1e-15,N=N,cutoff=cutoff,bound=bound,epsilon=eps)


def metrics_and_locality():
 for D in [np.array([.8,1.,.37]),np.array([1.3,.61,2.]),np.ones(3)]:
  det=np.prod(D);w=det/D**2
  for i in range(3):
   j,k=[q for q in range(3) if q!=i]
   close('matched quadratic magnetic metric',w[j]*w[k],D[i]**2,axis=i)
   close('canonical electric continuum coefficient',w[i]*D[i]**2/det,1,axis=i)
   close('magnetic continuum coefficient',w[i]*det/(D[j]*D[k])**2,1,axis=i)
   close('four incident plaquette raising norm',(2*w[j]+2*w[k])/2,w[j]+w[k],axis=i)
 A=np.kron(sig[0],I2);B=np.kron(I2,sig[2]);U=np.kron(expm(-.37j*sig[2]),expm(.91j*sig[0]));AA=U@A@U.conj().T;BB=U@B@U.conj().T
 close('onsite interaction picture preserves norms',norm(AA),norm(A))
 close('onsite interaction picture preserves disjoint support commutation',AA@BB-BB@AA,0)


def phase_discriminators():
 tau=sy.symbols('tau',real=True);kernel=(1+2*sy.exp(-tau/2)*sy.cos(4*sy.pi/5)+2*sy.exp(-2*tau)*sy.cos(8*sy.pi/5))/5
 check('exact phase heat-kernel derivative',sy.simplify(sy.diff(kernel,tau).subs(tau,0)-(5-3*sy.sqrt(5))/20)==0)
 check('negative finite phase heat-kernel at small step',float(kernel.subs(tau,sy.Rational(1,50)))<-.0016)
 E,u=rotor(2);phases=2*np.pi*np.arange(5)/5;F=np.exp(1j*E[:,None]*phases[None,:])/np.sqrt(5);exact=F.conj().T@np.diag(np.exp(-.02*E*E/2))@F
 close('phase heat-kernel independent Fourier matrix',exact[0,2],float(kernel.subs(tau,sy.Rational(1,50))))
 # Exact rational matrices and trace-log power series; the asserted closed
 # coefficients below are tested against the original hopping matrices.
 ss=sy.Rational(4,5);cc=sy.Rational(3,5);mu=sy.Rational(1,5);base=sy.Rational(13,5);hop=sy.Matrix([[-1,-1],[1,1]])/2;Z=sy.zeros(4);order=5
 def mul(a,b):return [sum((a[j]*b[k-j] for j in range(k+1)),Z.copy()) for k in range(order+1)]
 total=[sy.S(0)]*6
 for eta in [-1,1]:
  A=eta*mu*ss;B=base+eta*mu*cc;on=sy.Matrix([[B,A],[A,-B]]);hs=[]
  for ph in [1,sy.I,-1]:
   h=sy.zeros(4);h[:2,:2]=on;h[2:,2:]=on;h[:2,2:]=ph*hop;h[2:,:2]=sy.conjugate(ph)*hop.T;hs.append(h)
  coeff=[sy.eye(4)]+[Z.copy() for _ in range(order)]
  for h in hs:
   powers=[sy.eye(4)]
   for k in range(1,order+1):powers.append(-h*powers[-1]/k)
   coeff=mul(powers,coeff)
  xx=[Z.copy()]+[c/2 for c in coeff[1:]];power=xx;logs=[sy.S(0)]*6
  for r in range(1,6):
   for k in range(1,6):logs[k]+=sy.Rational((-1)**(r+1),r)*sy.trace(power[k])
   if r<5:power=mul(power,xx)
  logs=[sy.simplify(v) for v in logs]
  formula=[0,0,(18*A*A+18*B*B+1)/4,sy.I*A,-(162*A**4+324*A*A*B*B-110*A*A+162*B**4-28*B*B+1)/96,-sy.I*A*(7*A*A+7*B*B-1)/4]
  for k in range(6):check('exact single-flavor determinant coefficient',sy.simplify(logs[k]-formula[k])==0,eta=eta,order=k)
  total=[a+b for a,b in zip(total,logs)]
 check('quartet cubic determinant phase cancels',sy.simplify(total[3])==0)
 check('quartet fifth-order determinant phase survives',sy.simplify(sy.im(total[5])+7*base*mu*mu*ss*cc)==0)
 check('exact rational nonzero phase witness',sy.im(total[5])==-sy.Rational(1092,3125))
 # Independent high-precision exponentials, not a Taylor reconstruction.
 mp.mp.dps=70
 def mblock(eta,phase):
  a=mp.mpf(eta)*mp.mpf(4)/25;b=mp.mpf(13)/5+mp.mpf(eta)*3/25;h=mp.matrix(4)
  for q in [0,2]:h[q,q]=b;h[q,q+1]=a;h[q+1,q]=a;h[q+1,q+1]=-b
  p=mp.exp(1j*phase)
  for i,j in itertools.product(range(2),repeat=2):
   v=mp.mpf([[-1,-1],[1,1]][i][j])/2*p;h[i,2+j]=v;h[2+j,i]=mp.conj(v)
  return h
 target=-mp.mpf(1092)/3125
 for dt in [mp.mpf('0.002'),mp.mpf('0.001')]:
  weight=mp.mpf(1)
  for eta in [-1,1]:
   prod=mp.eye(4)
   for ph in [0,mp.pi/2,mp.pi]:prod=mp.expm(-dt*mblock(eta,ph))*prod
   weight*=mp.det(mp.eye(4)+prod)
  rate=mp.im(mp.log(weight))/dt**5
  check('independent precision phase coefficient limit',abs(rate-target)<mp.mpf('.0001'),step=str(dt),coefficient=str(rate),target=str(target))
 on,hops=carrier();hs=[];reverse=[];TT=np.kron(np.eye(2),TR)
 for ph in [0,np.pi/2,np.pi]:
  h=np.kron(np.eye(2),on);h[:4,4:]=hops[1]*np.exp(1j*ph);h[4:,:4]=h[:4,4:].conj().T;hs.append(h)
  r=np.kron(np.eye(2),on);r[:4,4:]=hops[1]*np.exp(-1j*ph);r[4:,:4]=r[:4,4:].conj().T;reverse.append(r)
  close('background T maps phases to opposites',TT@h.conj()@TT,r)
 for n in [1,2,3]:
  prod=np.eye(8,dtype=complex);rp=prod.copy()
  for h,r in zip(hs[:n],reverse[:n]):prod=expm(-.4*h)@prod;rp=expm(-.4*r)@rp
  sign,la=np.linalg.slogdet(np.eye(8)+prod);rs,rl=np.linalg.slogdet(np.eye(8)+rp)
  close('time reversal pairs conjugate weights',sign.conjugate(),rs);close('paired weight modulus',la,rl)
  if n<3:check('one and two positive factors give positive weight',abs(np.angle(sign))<1e-11,n=n)
  else:check('three factors have complex weight despite T',np.angle(sign)<-.00048,n=n,phase=float(np.angle(sign)))


def main():
 start=time.monotonic();link_algebra();physical_carrier();exponential_bounds();metrics_and_locality();phase_discriminators()
 for label,msg in [
 ('per_element','exact compressed link commutator, endpoint defects and phase heat kernel checked'),
 ('per_site','finite charged two-cell Gauss sectors and time reversal checked; state selection open'),
 ('per_mode','bounded one-link flux-tail fixtures and matrix growth constants challenged; photon modes not certified'),
 ('per_block','multi-link cutoff Duhamel errors and exact time-sliced determinant coefficients checked'),
 ('lattice_wide','checked and not executed — thermodynamic charged photon phase and uniform infrared limits remain proof obligations')]:print(label+': '+msg)
 print(json.dumps(dict(status='PASS',author_check_count=len(rows),checks=rows,elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claim_limit='Finite-link algebra, stated finite-time bounds and representation-specific phase witnesses; no thermodynamic charged phase or axiom update.'),indent=2))
 print('TOTAL: PASS='+str(len(rows))+' FAIL=0')
if __name__=='__main__':main()
