#!/usr/bin/env python3
"""Exact moment/symmetrizer controls and an actual-stencil initial drift check."""
from pathlib import Path
from itertools import product
import json,hashlib,math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parent
labels=[(s.eye(3)[:,i]*z,s.zeros(3,1)) for i in range(3) for z in [1,-1]]+[(s.zeros(3,1),s.Matrix(b)) for b in product([-1,1],repeat=3)]
E=s.Matrix.hstack(*[x[0] for x in labels]);B=s.Matrix.hstack(*[x[1] for x in labels]);W=E.col_join(B)
T=s.Matrix.vstack(s.eye(13),-s.ones(1,13))
one=s.ones(14,1)

def flux(p):
 X=E*p;Y=B*p;return s.Matrix.vstack(*[(p[a]*(e.cross(Y)+X.cross(b)-2*X.cross(Y))).T for a,(e,b) in enumerate(labels)])

def moments(p):
 D=s.Matrix([sum(p[a]*E[i,a]**2 for a in range(14)) for i in range(3)]);X=E*p;Y=B*p
 Z={(i,j):sum(p[a]*B[i,a]*B[j,a] for a in range(14)) for i,j in [(0,1),(0,2),(1,2)]};w=sum(p[a]*s.prod(B[:,a]) for a in range(14))
 return D,X,Y,Z,w

def moment_controls():
 rows=[]
 for seed in range(5):
  weights=[1+(i+3*seed)**2%19 for i in range(14)];p=s.Matrix([s.Rational(a,sum(weights)) for a in weights]);D,X,Y,Z,w=moments(p);rhoB=1-sum(D);F=flux(p)
  restored=[]
  for i in range(3):
   for sign in [1,-1]:restored.append((D[i]+sign*X[i])/2)
  for b in product([-1,1],repeat=3):restored.append((rhoB+s.Matrix(b).dot(Y)+sum(b[i]*b[j]*z for (i,j),z in Z.items())+s.prod(b)*w)/8)
  assert s.Matrix(restored)==p and one.T*F==s.zeros(1,3)
  MB=s.Matrix(3,3,lambda i,j:rhoB if i==j else Z[tuple(sorted((i,j)))])
  for i in range(3):
   fD=sum((E[i,a]**2*F[a,:].T for a in range(14)),s.zeros(3,1));fX=(E*F)[i,:].T;fY=(B*F)[i,:].T
   assert fD==X[i]*s.eye(3)[:,i].cross(Y)-2*D[i]*X.cross(Y)
   assert fX==D[i]*s.eye(3)[:,i].cross(Y)-2*X[i]*X.cross(Y)
   assert fY==X.cross(MB[:,i])-2*Y[i]*X.cross(Y)
  for (i,j),z in Z.items():
   k=3-i-j;actual=sum((B[i,a]*B[j,a]*F[a,:].T for a in range(14)),s.zeros(3,1))
   assert actual==X.cross(Y[j]*s.eye(3)[:,i]+Y[i]*s.eye(3)[:,j]+w*s.eye(3)[:,k])-2*z*X.cross(Y)
  actual=sum((s.prod(B[:,a])*F[a,:].T for a in range(14)),s.zeros(3,1));assert actual==X.cross(s.Matrix([Z[1,2],Z[0,2],Z[0,1]]))-2*w*X.cross(Y)
  rows.append(dict(seed=seed,exact_probability_reconstruction=True,all_thirteen_vector_fluxes_exact=True))
 return rows

def Kmatrix(n):return s.Matrix(14,14,lambda a,b:s.Matrix(n).dot(labels[a][0].cross(labels[b][1])+labels[b][0].cross(labels[a][1])))
def jac(p,K):
 v=K*p;M=(p.T*K*p)[0];return s.diag(*[x-M for x in v])+s.diag(*p)*K-2*p*v.T

def entropy_controls():
 rows=[]
 for seed in range(4):
  w=[1+(i+seed*5)**2%17 for i in range(14)];p=s.Matrix([s.Rational(a,sum(w)) for a in w]);H=T.T*s.diag(*[1/x for x in p])*T
  pn=np.array(p,dtype=float).reshape(-1);tn=np.array(T,dtype=float)
  for n in [(1,0,0),(1,2,-3),(0,-1,2)]:
   K=Kmatrix(n);A=jac(p,K);Ar=A[:13,:]*T;assert one.T*A*T==s.zeros(1,13)
   assert H*Ar==(H*Ar).T
   eigen=np.linalg.eigvals(np.array(Ar,dtype=float));imag=float(max(abs(eigen.imag)));assert imag<1e-10
   kn=np.array(K,dtype=float);an=np.array(A,dtype=float)
   def q(z,omit=False):
    eta=np.sum(z*np.log(z));v=kn@z;M=z@v
    return np.sum(z*np.log(z)*v)-eta*M-(0 if omit else M/2)
   good=[];wrong=[]
   for j in range(13):
    direction=tn[:,j];expected=(np.log(pn)+1)@(an@direction)
    good.append(abs(q(pn+1j*1e-24*direction).imag/1e-24-expected))
    wrong.append(abs(q(pn+1j*1e-24*direction,True).imag/1e-24-expected))
   assert max(good)<2e-13 and max(wrong)>1e-4
   rows.append(dict(seed=seed,direction=n,exact_entropy_symmetry=True,max_characteristic_imaginary=imag,entropy_flux_directional_error=max(good),omitted_half_M_countercontrol=max(wrong)))
 return rows

def rest(D,Z=None,w=s.Integer(0)):
 Z=Z or {};rb=1-sum(D);p=[]
 for d in D:p.extend([d/2,d/2])
 for b in product([-1,1],repeat=3):p.append((rb+sum(b[i]*b[j]*v for (i,j),v in Z.items())+s.prod(b)*w)/8)
 assert min(p)>0;return s.Matrix(p)

def optical_controls():
 rows=[];profiles={'isotropic':rest([s.Rational(1,7)]*3),'Z23':rest([s.Rational(1,7)]*3,{(1,2):s.Rational(1,14)}),'hidden_w':rest([s.Rational(1,7)]*3,w=s.Rational(1,14))}
 for name,p in profiles.items():
  D,X,Y,Z,w=moments(p);assert X==Y==s.zeros(3,1);rb=1-sum(D);MB=s.Matrix(3,3,lambda i,j:rb if i==j else Z[tuple(sorted((i,j)))])
  for axis in range(3):
   n=s.eye(3)[:,axis];cross=s.Matrix([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
   A6=s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),-s.diag(*D)*cross),s.Matrix.hstack(MB*cross,s.zeros(3)))
   A=jac(p,Kmatrix(n));assert W*A==A6*W and A.to_DM().rank()==4
   transverse=[i for i in range(3) if i!=axis];i,j=transverse;disc=rb**2*(D[i]-D[j])**2+4*D[i]*D[j]*Z[tuple(sorted((i,j)))]**2
   expected=[s.simplify((rb*(D[i]+D[j])+sgn*s.sqrt(disc))/2) for sgn in [-1,1]]
   eig=(A6*A6).eigenvals();actual=sorted([v for v,m in eig.items() if v!=0 for _ in range(m//2)])
   assert actual==sorted(expected)
   rows.append(dict(profile=name,axis=axis,exact_squared_speeds=[str(x) for x in expected],full_color_rank=4,six_vector_moment_intertwiner_exact=True))
 return rows

def initial_drift_controls():
 en=np.array(E,dtype=float);bn=np.array(B,dtype=float);p0=np.ones(14)/14
 # A finite-amplitude transverse profile with positive probabilities everywhere.
 # X=(0,A cos,A cos/2), Y=(0,-A cos,2A cos); D remains1/7 initially.
 A=.08;direction=np.zeros(14)
 for i,sgn in product(range(3),[1,-1]):
  idx=2*i+(0 if sgn==1 else 1);direction[idx]=sgn*[0,A,A/2][i]/2
 for a,b in enumerate(list(product([-1,1],repeat=3)),start=6):direction[a]=np.dot(b,[0,-A,2*A])/8
 assert min(p0+direction)>0 and min(p0-direction)>0 and abs(sum(direction))<1e-15
 k0=1.1;deltas=[np.eye(3,dtype=int)[i]*sgn for i in range(3) for sgn in [1,-1]];rows=[]
 Kx=np.array(Kmatrix((1,0,0)),dtype=float)
 for N in [8,16,32,64,128,256,512,1024,2048,4096,8192]:
  x=np.arange(N)/N;p=p0[None,:]+np.cos(2*np.pi*x)[:,None]*direction[None,:];dp=-2*np.pi*np.sin(2*np.pi*x)[:,None]*direction[None,:]
  drift=np.zeros_like(p)
  for delta in deltas:
   step=int(delta[0]-1)
   if np.array_equal(delta,[1,0,0]):continue
   S=np.array(Kmatrix(delta),dtype=float)/2
   pu=p;pw=np.roll(p,-step,axis=0);pl=np.roll(p,step,axis=0);pr=np.roll(p,-2*step,axis=0)
   ss=(pl+pr)@S.T;mu_u=np.sum(pu*ss,axis=1);mu_w=np.sum(pw*ss,axis=1)
   J=k0/2*(pu-pw)+.25*((pu+pw)*ss-pu*mu_w[:,None]-pw*mu_u[:,None])
   assert max(abs(J.sum(axis=1)))<1e-15
   drift+=N*(np.roll(J,step,axis=0)-J)
  target=np.empty_like(p)
  for j,z in enumerate(p):
   v=Kx@z;M=z@v;JF=np.diag(v-M)+np.diag(z)@Kx-2*np.outer(z,v);target[j]=-JF@dp[j]
  error=float(np.max(abs(drift-target)));rows.append(dict(N=N,max_color_initial_Euler_drift_error=error,N_times_error=N*error))
 assert rows[-1]['max_color_initial_Euler_drift_error']<rows[-2]['max_color_initial_Euler_drift_error']<.003
 # Analytic finite-amplitude second-harmonic sources in D and Z at x=1/8.
 x=s.symbols('x',real=True);amp=s.Rational(2,25);X=s.Matrix([0,amp*s.cos(x),amp*s.cos(x)/2]);Y=s.Matrix([0,-amp*s.cos(x),2*amp*s.cos(x)])
 rho_flux=s.simplify(s.Rational(1,7)*X.cross(Y)[0]);z23_flux=s.simplify(X.cross(Y[2]*s.eye(3)[:,1]+Y[1]*s.eye(3)[:,2])[0])
 assert s.simplify(s.diff(rho_flux,x))!=0 and s.simplify(s.diff(z23_flux,x))!=0
 return dict(profile_amplitude=A,minimum_color_probability=float(min(p0-abs(direction))),rows=rows,finite_amplitude_rhoA_flux=str(rho_flux),finite_amplitude_Z23_flux=str(z23_flux),scope='Exact initial product-law expected generator current, not simulated trajectories or a finite-time hydrodynamic limit. O(1/N) is a Taylor bound; no exponent is fitted.')

def main():
 result={'sources':[]}
 for name in ['DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md','DIMER_NONLINEAR_INITIAL_DRIFT.md',Path(__file__).name,'DIMER_ROUTED_RECORD_TRANSPORT.md']:
  p=ROOT/name;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 for name,fn in [('moment_fluxes',moment_controls),('entropy_symmetrizer',entropy_controls),('optical_diagnostic',optical_controls),('actual_initial_drift',initial_drift_controls)]:result[name]=fn();print(name+' complete',flush=True)
 out=ROOT/'dimer_nonlinear_flux_checks';out.mkdir(exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print('all_four_control_groups_complete',flush=True)

if __name__=='__main__':main()
