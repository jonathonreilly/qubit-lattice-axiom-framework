#!/usr/bin/env python3
"""Additional independent coefficient, locality, counting and interpolation controls."""
import itertools as it, math,json,sys,datetime
import numpy as np
from scipy import linalg,integrate,special
rng=np.random.default_rng(47291);checks=[];mutations=[]
def check(n,condition,**e):checks.append(dict(name=n,passed=bool(condition),**e))
def mut(n,c,**e):mutations.append(dict(name=n,rejected=bool(c),**e))
def basis(N):
 b=[]
 for i in range(N):
  for j in range(i+1,N):
   A=np.zeros((N,N),complex);A[i,j]=1/np.sqrt(2);A[j,i]=-1/np.sqrt(2);b.append(A)
   A=np.zeros((N,N),complex);A[i,j]=1j/np.sqrt(2);A[j,i]=1j/np.sqrt(2);b.append(A)
 for k in range(1,N):
  A=np.diag([1j/np.sqrt(k*(k+1))]*k+[-1j*k/np.sqrt(k*(k+1))]+[0j]*(N-k-1));b.append(A)
 return np.array(b)
u=2.3
for N in (2,3,4):
 b=basis(N);D=len(b);G=np.einsum('aij,bij->ab',b.conj(),b).real
 A=np.einsum('ka,aij->kij',rng.normal(size=(4,D))*.15,b)
 F=A[0]+A[1]-A[2]-A[3];pred=u/N*np.vdot(F,F).real
 def wil(s):
  U=linalg.expm(s*A[0])@linalg.expm(s*A[1])@linalg.expm(-s*A[2])@linalg.expm(-s*A[3]);return u*(1-np.trace(U).real/N)
 hs=[(wil(s)+wil(-s))/s**2 for s in (2e-3,1e-3,5e-4)]
 check('actual_Wilson_Hessian_SU'+str(N),abs(hs[-1]-pred)<3e-5,steps=hs,expected=pred)
 sig=math.sqrt(N/u);scaled=(wil(5e-4*sig)+wil(-5e-4*sig))/(5e-4)**2
 check('Wilson_rescaling_SU'+str(N),abs(scaled-np.vdot(F,F).real)<3e-5)
 mut('omit_Wilson_1_over_N_SU'+str(N),abs(hs[-1]-N*pred)>3e-5)
 # Different path from eigenvalue Jacobian: construct the real adjoint representation.
 X=np.einsum('a,aij->ij',rng.normal(size=D),b);X/=np.linalg.norm(X)
 ad=np.array([[np.vdot(B,X@C-C@X).real for C in b] for B in b])
 check('HS_basis_and_adjoint_Casimir_SU'+str(N),np.max(np.abs(G-np.eye(D)))<2e-11 and abs(np.trace(ad@ad)+2*N)<2e-11,trace_ad_squared=float(np.trace(ad@ad)))
 # Mixed colour kernel is fixed by Ad-invariance, Casimir checked in full colour basis.
 check('adjoint_skew_SU'+str(N),np.max(np.abs(ad+ad.T))<2e-11)

for t in (.1,.7,1.61,5.,20.):
 vals=[integrate.quad(lambda a,p=p:2/np.pi*np.sin(a)**2*np.cos(a)**p*np.exp(t*(np.cos(a)-1)),0,np.pi,epsabs=1e-11,epsrel=1e-11)[0] for p in (0,1,2)]
 c=vals[1]/vals[0];var=vals[2]/vals[0]-c*c
 bessel=special.ive(2,t)/special.ive(1,t)
 check('Haar_tilt_mean_'+str(t),0<c<1 and var>0 and abs(c-bessel)<2e-11,c=c,variance=var,bessel=bessel)

# Endpoint-pair multiplicity is enumerated on T=2,3,4, preserving oriented coarse labels.
for T in (2,3,4):
 blocks=list(it.product(range(T),repeat=4));pairs=[]
 for X in blocks:
  for mu in range(4):
   Y=list(X);Y[mu]=(Y[mu]+1)%T;pairs.append({X,tuple(Y)})
 # Any plaquette fully contained in one/two endpoint blocks contains a vertex block X.
 # Enumerate vertex block sets for every fine plaquette at L=3.
 L=3;n=L*T;maxcount=0
 for x in it.product(range(n),repeat=4):
  for mu in range(4):
   for nu in range(mu+1,4):
    vs=[]
    for s,t in it.product([0,1],repeat=2):
     y=list(x);y[mu]=(y[mu]+s)%n;y[nu]=(y[nu]+t)%n;vs.append(tuple(a//L for a in y))
    vs=set(vs)
    # Local incident-pair enumeration avoids scanning every global pair.
    X=next(iter(vs));eligible=[]
    for a in range(4):
     for shift in (0,-1):
      Z=list(X);Z[a]=(Z[a]+shift)%T;Y=Z.copy();Y[a]=(Y[a]+1)%T
      if vs <= {tuple(Z),tuple(Y)}:eligible.append((tuple(Z),a))
    maxcount=max(maxcount,len(eligible))
 check('plaquette_endpoint_pair_charge_T'+str(T),maxcount<=8,max_oriented_labels=maxcount)
 mut('omit_eightfold_pair_multiplicity_T'+str(T),maxcount>1)

# Exact scalar integral giving both square-root prefactors; summability identity.
for a in (.3,1.,7.):
 val=integrate.quad(lambda x:2/(a+x*x)/np.pi,0,np.inf,epsabs=1e-11,epsrel=1e-11)[0]
 check('square_root_integral_a'+str(a),abs(val-1/np.sqrt(a))<2e-11)
r=.47;one=1+2*sum(np.exp(-r*k) for k in range(1,100))
check('four_dimensional_counting_sum',abs(one**4-(1/np.tanh(r/2))**4)<2e-11)
mut('omit_four_dimensional_density',abs(one**4-one**3)>1e-2)

out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),checks=checks,mutations=mutations,passed=sum(x['passed'] for x in checks),total=len(checks),mutations_rejected=sum(x['rejected'] for x in mutations),mutations_total=len(mutations),limits='Finite independent diagnostics; no author checker imported or read, no uniform proof inferred.')
print(json.dumps(out,indent=2));sys.exit(0 if out['passed']==out['total'] and out['mutations_rejected']==out['mutations_total'] else 1)
