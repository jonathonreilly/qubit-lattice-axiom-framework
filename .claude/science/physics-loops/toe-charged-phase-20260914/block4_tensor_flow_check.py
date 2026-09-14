#!/usr/bin/env python3
"""Private exact angular and coupled-tensor-flow tests."""
import itertools,json,math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp,quad
from block4_velocity_check import sigma

def kn(h):
 I=np.eye(4)
 return np.einsum('mr,ns->mnrs',I,h)+np.einsum('ns,mr->mnrs',I,h)-np.einsum('ms,nr->mnrs',I,h)-np.einsum('nr,ms->mnrs',I,h)
def ricci(K):return np.einsum('mnms->ns',K)
def epsilon4():
 e=np.zeros((4,)*4)
 for p in itertools.permutations(range(4)):
  e[p]=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
 return e

def check_angular_tensor():
 points=[]
 for j in range(4):
  for sign in [-1,1]:
   p=[F(0)]*4;p[j]=F(sign);points.append(p)
 points += [[F(s,2) for s in row] for row in itertools.product([-1,1],repeat=4)]
 for i,j in itertools.product(range(4),repeat=2):
  assert sum(p[i]*p[j] for p in points)/24==F(int(i==j),4)
 for i,j,k,l in itertools.product(range(4),repeat=4):
  target=F(int(i==j)*int(k==l)+int(i==k)*int(j==l)+int(i==l)*int(j==k),24)
  assert sum(p[i]*p[j]*p[k]*p[l] for p in points)/24==target
 P=np.asarray(points,dtype=float)
 g=np.array([np.kron(sigma[0],s) for s in sigma]+[np.kron(sigma[1],np.eye(2))])
 tr4=np.empty((4,)*4)
 for b,n,a,s in itertools.product(range(4),repeat=4):
  val=np.trace(g[b]@g[n]@g[a]@g[s])/4
  target=int(b==n)*int(a==s)-int(b==a)*int(n==s)+int(b==s)*int(n==a)
  assert val==target;tr4[b,n,a,s]=val.real
 rng=np.random.default_rng(9140453);pairs=list(itertools.combinations(range(4),2));rows=[]
 for case in range(5):
  coeff=rng.integers(-5,6,(6,6));coeff=coeff+coeff.T
  K=np.zeros((4,)*4)
  for i,(a,b) in enumerate(pairs):
   for j,(c,d) in enumerate(pairs):
    K[a,b,c,d]=K[b,a,d,c]=coeff[i,j]
    K[b,a,c,d]=K[a,b,d,c]=-coeff[i,j]
  axion=np.einsum('mnrs,mnrs',K,epsilon4())/24
  K-=axion*epsilon4()
  R=ricci(K);scalar=np.trace(R);h=(R-scalar*np.eye(4)/4)/2
  J=(kn(np.eye(4))/2)
  C=K-kn(h)-scalar*J/12
  assert np.max(abs(ricci(C)))<1e-13
  for label,T in [('general',K),('metric',kn(h)),('Weyl',C)]:
   M=2*np.einsum('mnrs,tm,tr->tns',T,P,P)
   assert np.max(abs(np.einsum('tij,tj->ti',M,P)))<1e-12
   # Direct four-gamma trace and angular derivative, not the Ricci formula.
   raw=np.einsum('bnas,tns->tba',tr4,M)-2*np.einsum('ta,td,bnds,tns->tba',P,P,tr4,M)
   averaged=raw.mean(axis=0);Rc=ricci(T)
   target=4*Rc/3-np.eye(4)*np.trace(Rc)/3
   err=float(np.max(abs(averaged-target)));assert err<1e-12
   if label=='Weyl':assert np.max(abs(averaged))<1e-12
   if label=='metric':assert np.max(abs(averaged-8*h/3))<1e-12
   rows.append({'case':case,'tensor':label,'direct_gamma_vs_Ricci_error':err})
 return {'exact_cubature_points':24,'exact_second_moments':16,'exact_fourth_moments':256,'Clifford_trace_checks':256,'tensor_checks':rows}

def star(q,n):
 q=np.asarray(q);n=np.asarray(n);s=len(q);L=np.zeros((s+1,s+1))
 for a in range(s):
  L[a,a]=2*q[a]**2;L[a,-1]=-2*q[a]**2
  L[-1,a]=-n[a]*q[a]**2;L[-1,-1]+=n[a]*q[a]**2
 return L,np.r_[n/2,1.]

def check_flow():
 out=[]
 for q,n in [(np.ones(4),np.full(4,.5)),(np.array([1.,2.,.3]),np.array([1.,.5,2.]))]:
  L,w=star(q,n);W=float(np.dot(n,q*q));root=np.diag(np.sqrt(w));A=root@L@np.linalg.inv(root)
  assert np.max(abs(A-A.T))<1e-14
  eig=np.linalg.eigvalsh(A);assert abs(eig[0])<1e-13 and eig[1]>0
  y0=np.arange(len(q)+1,dtype=float)/13-.1;k0=.02
  times=np.array([0.,1.,10.,100.,1000.])
  sol=solve_ivp(lambda t,y:-k0/(1+W*k0*t)*(L@y),(0.,1000.),y0,rtol=2e-11,atol=2e-12,t_eval=times)
  errors=[]
  for t,y in zip(times,sol.y.T):
   exact=expm(-L*math.log1p(W*k0*t)/W)@y0
   errors.append(float(np.max(abs(exact-y))));assert errors[-1]<2e-10
   assert abs(w@y-w@y0)<1e-12
   assert abs(y@(np.diag(w)@L)@y-np.sum(n*q*q*(y[:-1]-y[-1])**2))<1e-12
  if len(q)==4:assert np.max(abs(eig-np.array([0,2,2,2,4])))<1e-13
  out.append({'q':q.tolist(),'Dirac_multiplicities':n.tolist(),'eigenvalues':eig.tolist(),'logarithmic_exponents':(eig/W).tolist(),'ODE_vs_matrix_power_max_error':max(errors)})
 # Decaying lattice forcing changes the matching constant, not the asymptotic power.
 W=2.;lam=4.;k0=.02;p=1.;source=.1;y0=.2
 def forcing(t):return source*k0/(1+W*k0*t)*np.exp(-p*t)
 integral=quad(lambda t:(1+W*k0*t)**(lam/W)*forcing(t),0,np.inf,epsabs=1e-12)[0]
 exact_integral=source*k0*(1+W*k0)
 assert abs(integral-exact_integral)<1e-12
 out.append({'decaying_source_matching_increment':integral,'closed_form_increment':exact_integral,'asymptotic_mode_coefficient':y0+integral})
 return out

def main():
 result={'angular_tensor':check_angular_tensor(),'metric_flow':check_flow(),'scope':'linearized parity-even marginal kinetic sector and its truncated one-loop flow; no all-orders phase, native carrier selection or finite-scale experimental match'}
 Path(__file__).with_name('BLOCK4_TENSOR_FLOW_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));print('PASS: exact angular moments, direct Clifford tensor response, weighted graph spectrum and forced flow')
if __name__=='__main__':main()
