#!/usr/bin/env python3
"""Self-contained checks of supplied lattice one-loop logarithms and metric-flow limits.

The analytic proof is in the paired note. Finite checks are falsifiers, not a
nonperturbative phase theorem or independent scientific review.
"""
AUDIT_INPUT_PATHS = (
    "docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

import itertools
import json
import math
import traceback
from fractions import Fraction as F
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 90
I=np.eye(2,dtype=complex)
sigma=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)


def mat(a):return np.einsum('...j,jab->...ab',a,sigma)


def symbol(k,v=1.,zeta=.4):
 k=np.asarray(k);s=np.sqrt(1-zeta*zeta)
 a=np.stack([np.sin(k[...,0]),np.sin(k[...,1]),(2+zeta-np.cos(k).sum(axis=-1))/s],axis=-1)*v
 return mat(a)


def vertex(k,j,v=1.,zeta=.4):
 k=np.asarray(k);a=np.zeros(k.shape,dtype=float);s=np.sqrt(1-zeta*zeta)
 if j<2:a[...,j]=np.cos(k[...,j])
 a[...,2]=np.sin(k[...,j])/s
 return v*mat(a)


def vertex_derivative(k,j,v=1.,zeta=.4):
 k=np.asarray(k);a=np.zeros(k.shape,dtype=float);s=np.sqrt(1-zeta*zeta)
 if j<2:a[...,j]=-np.sin(k[...,j])
 a[...,2]=np.cos(k[...,j])/s
 return v*mat(a)


def check_tensor_and_Ward():
 rng=np.random.default_rng(9140441);gm=wm=0.
 for _ in range(40):
  c=float(rng.uniform(.3,2.5));xi=float(rng.uniform(.1,3));omega=float(rng.normal());q=rng.uniform(-np.pi,np.pi,3)
  h=2*np.sin(q/2);Q=omega*omega+c*c*(h@h);k=np.r_[omega,h]
  B=np.zeros((4,4));B[0,0]=h@h;B[0,1:]=B[1:,0]=-omega*h
  B[1:,1:]=omega*omega*np.eye(3)+c*c*((h@h)*np.eye(3)-np.outer(h,h))
  gf=np.r_[omega,c*c*h];M=B+np.outer(gf,gf)/(c*c*xi)
  D=np.diag([c*c,1,1,1])/Q+(xi-1)*c*c*np.outer(k,k)/Q**2
  err=float(np.max(abs(M@D-np.eye(4))));gm=max(gm,err);assert err<2e-13
  assert np.linalg.eigvalsh(M).min()>0
  p=rng.uniform(-np.pi,np.pi,3);v=float(rng.uniform(.3,2));z=float(rng.uniform(.1,.8))
  diff=symbol(p+q/2,v,z)-symbol(p-q/2,v,z)
  w=sum(h[j]*vertex(p,j,v,z) for j in range(3));err=float(np.max(abs(diff-w)));wm=max(wm,err);assert err<1e-13
  # Temporal part of the same identity, D=i omega+h, W_0=i I.
  assert np.max(abs((1j*omega*I+diff)-(1j*omega*I+w)))<1e-13
 return {'cases':40,'true_inverse_max_error':gm,'Peierls_Ward_max_error':wm}


def check_residues():
 out=[]
 for c,v in [(1,.3),(1,.7),(1,1),(1,1.7),(1,3),(1.7,.8)]:
  i3=quad(lambda x:(1-x)/(x*v*v+(1-x)*c*c)**1.5,0,1,epsabs=1e-12)[0]
  i5=quad(lambda x:(1-x)/(x*v*v+(1-x)*c*c)**2.5,0,1,epsabs=1e-12)[0]
  assert abs(i3-2/(c*(c+v)**2))<1e-11
  assert abs(i5-2*(2*c+v)/(3*c**3*v*(c+v)**2))<1e-10
  ft=quad(lambda t:(v*v-t*t)/((t*t+v*v)**2*(t*t+c*c)),-np.inf,np.inf,epsabs=1e-12)[0]
  fs=quad(lambda t:(t*t+v*v/3)/((t*t+v*v)**2*(t*t+c*c)),-np.inf,np.inf,epsabs=1e-12)[0]
  at=(3*v*v-c*c)*i3/(8*np.pi**2);ass=(c*c+v*v)*c*c*i5/(8*np.pi**2)
  assert abs(at-(3*v*v-c*c)*ft/(4*np.pi**3))<1e-12
  assert abs(ass-(c*c+v*v)*fs/(4*np.pi**3))<1e-12
  target=(c-v)*(4*v*v+3*v*c+c*c)/(6*np.pi**2*c*(v+c)**2)
  assert abs(v*(ass-at)-target)<1e-12
  out.append({'c':c,'v':v,'A_t_over_e2':at,'A_s_over_e2':ass,'dv_dell_over_e2':target})
 return out


def shell_samples(nt=64,nu=12,nphi=24):
 x,wx=leggauss(nt);u,wu=leggauss(nu);phi=2*np.pi*np.arange(nphi)/nphi
 theta_t=np.pi*x/2;t=np.tan(theta_t);wt=wx*np.pi/2/np.cos(theta_t)**2
 vectors=np.stack([np.sqrt(1-u[:,None]**2)*np.cos(phi),np.sqrt(1-u[:,None]**2)*np.sin(phi),np.broadcast_to(u[:,None],(nu,nphi))],axis=-1).reshape(-1,3)
 wangle=np.repeat(wu,nphi)*2*np.pi/nphi
 directions=np.broadcast_to(vectors,(nt,len(vectors),3)).reshape(-1,3)
 times=np.repeat(t,len(vectors));weight=np.repeat(wt,len(vectors))*np.tile(wangle,nt)/(2*np.pi)**4
 return directions,times,weight


def local_lattice_shell(rho,v=1.,c=1.,zeta=.4,sign=1,quad_data=None):
 direction,t,weight=shell_samples() if quad_data is None else quad_data
 q=rho*direction;omega=rho*t;node=np.array([0.,0.,sign*np.arccos(zeta)])
 internal=node-q;mid=node-q/2
 H=symbol(internal,v,zeta);E2=np.real(np.einsum('nab,nba->n',H,H))/2
 S=(-1j*omega[:,None,None]*I+H)/(omega*omega+E2)[:,None,None]
 qhat=2*np.sin(q/2);Q=omega*omega+c*c*np.sum(qhat*qhat,axis=1)
 V=[vertex(mid,j,v,zeta) for j in range(3)]
 St=-1j*(S@S)
 corr=c*c*St-sum(a@St@a for a in V)
 coef_t=np.einsum('n,nab->ab',weight*rho**4/Q,corr)
 at=(np.trace(coef_t)/(2j)).real
 asp=[];off=[]
 for j in range(3):
  Sj=-S@vertex(internal,j,v,zeta)@S
  Vj=vertex_derivative(mid,j,v,zeta)
  corr=c*c*Sj-sum(a@Sj@a for a in V)-Vj@S@V[j]-V[j]@S@Vj
  coef=np.einsum('n,nab->ab',weight*rho**4/Q,corr)
  components=np.array([np.trace(s@coef).real/(2*v) for s in sigma]);components[2]*=sign
  asp.append(float(components[j]));components[j]=0;off.append(float(np.linalg.norm(components)))
 i3=2/(c*(c+v)**2);i5=2*(2*c+v)/(3*c**3*v*(c+v)**2)
 target_t=(3*v*v-c*c)*i3/(8*np.pi**2);target_s=(c*c+v*v)*c*c*i5/(8*np.pi**2)
 return {'rho':rho,'v':v,'c':c,'node_sign':sign,'time':float(at),'space':asp,'target_time':target_t,'target_space':target_s,'max_error':float(max(abs(at-target_t),max(abs(a-target_s) for a in asp))),'off_axis':off}


def polarization_shell(rho,v=1.,zeta=.4,sign=1,quad_data=None):
 direction,t,weight=shell_samples() if quad_data is None else quad_data
 k=rho*direction;omega=rho*t;node=np.array([0.,0.,sign*np.arccos(zeta)])
 H=symbol(node+k,v,zeta);E2=np.einsum('nab,nba->n',H,H).real/2
 S=(-1j*omega[:,None,None]*I+H)/(omega*omega+E2)[:,None,None]
 vertices=[np.broadcast_to(1j*I,S.shape)]+[vertex(node+k,j,v,zeta) for j in range(3)]
 def coefficient(mu,nu,axis):
  W=vertices[axis]
  Sa=-S@W@S
  curvature=0 if axis==0 else vertex_derivative(node+k,axis-1,v,zeta)
  Saa=2*S@W@S@W@S
  if axis!=0:Saa-=S@curvature@S
  U=vertices[mu];V=vertices[nu]
  a=U@Saa@V@S/8+U@S@V@Saa/8-U@Sa@V@Sa/4
  out=np.dot(weight*rho**4,np.trace(a,axis1=1,axis2=2))
  return float(out.real),float(out.imag)
 # One two-component Weyl cone, before summing the actual four cones.
 values={'E_via_Pi11_p0':coefficient(1,1,0),'E_via_Pi00_p1':coefficient(0,0,1),
         'B_via_Pi22_p1':coefficient(2,2,1),'B_via_Pi11_p3':coefficient(1,1,3),
         'longitudinal_time':coefficient(0,0,0),'longitudinal_space':coefficient(1,1,1)}
 target_e=1/(12*np.pi**2*v);target_b=v/(12*np.pi**2)
 errors=[abs(values[x][0]-y) for x,y in [('E_via_Pi11_p0',target_e),('E_via_Pi00_p1',target_e),('B_via_Pi22_p1',target_b),('B_via_Pi11_p3',target_b),('longitudinal_time',0),('longitudinal_space',0)]]
 return {'rho':rho,'v':v,'node_sign':sign,'per_Weyl_cone':values,'target_E':target_e,'target_B':target_b,'maximum_residue_error':max(errors),'maximum_imaginary':max(abs(y[1]) for y in values.values())}


def check_full_lattice_Ward():
 rows=[]
 for N in [3,5,7]:
  k=2*np.pi*(np.array(list(itertools.product(range(N),repeat=3)))+np.array([.17,.29,.41]))/N-np.pi
  v=.8;zeta=.4
  for mode in [[1,0,0],[1,-1,1]]:
   q=2*np.pi*np.asarray(mode)/N;qhat=2*np.sin(q/2)
   H=symbol(k,v,zeta);Hplus=symbol(k+q,v,zeta)
   W=[np.broadcast_to(1j*I,H.shape)]+[vertex(k+q/2,j,v,zeta) for j in range(3)]
   for omega in [0.,.317,1.4,4.]:
    S=np.linalg.inv(1j*omega*I+H);Sp=np.linalg.inv(1j*omega*I+Hplus)
    bubble=np.array([[np.trace(U@Sp@V@S,axis1=1,axis2=2).mean() for V in W] for U in W])
    contact=np.zeros((4,4),dtype=complex)
    for j in range(3):contact[j+1,j+1]=-np.trace(S@vertex_derivative(k,j,v,zeta),axis1=1,axis2=2).mean()
    total=bubble+contact
    residue=np.r_[0,qhat]@total;error=float(np.max(abs(residue)))
    scale=max(1.,float(np.linalg.norm(total)));assert error<2e-12*scale
    omitted=float(np.max(abs(np.r_[0,qhat]@bubble)))
    rows.append({'N':N,'mode':mode,'omega':omega,'full_Ward_error':error,'without_contact_error':omitted})
 assert max(r['without_contact_error'] for r in rows)>.01
 # Nonzero temporal transfer requires an actual continuous-frequency integral.
 for N in [3,5]:
  spatial=2*np.pi*(np.array(list(itertools.product(range(N),repeat=3)))+np.array([.17,.29,.41]))/N-np.pi
  xx,ww=np.polynomial.legendre.leggauss(128);angle=np.pi*xx/2
  om=np.tan(angle);weights=ww/(4*np.cos(angle)**2)
  k=np.tile(spatial,(len(om),1));omega=np.repeat(om,len(spatial))
  weight=np.repeat(weights,len(spatial))/len(spatial)
  q=2*np.pi*np.array([1,0,-1])/N;q0=.41
  H=symbol(k,.8,.4);Hp=symbol(k+q,.8,.4)
  S=np.linalg.inv(1j*omega[:,None,None]*I+H);Sp=np.linalg.inv(1j*(omega+q0)[:,None,None]*I+Hp)
  W=[np.broadcast_to(1j*I,H.shape)]+[vertex(k+q/2,j,.8,.4) for j in range(3)]
  bubble=np.array([[np.dot(weight,np.trace(U@Sp@V@S,axis1=1,axis2=2)) for V in W] for U in W])
  contact=np.zeros((4,4),dtype=complex)
  for j in range(3):contact[j+1,j+1]=-np.dot(weight,np.trace(S@vertex_derivative(k,j,.8,.4),axis1=1,axis2=2))
  total=bubble+contact;qh=np.r_[q0,2*np.sin(q/2)]
  error=float(np.max(abs(qh@total)));assert error<2e-10
  rows.append({'N':N,'mode':[1,0,-1],'external_frequency':q0,'frequency_quadrature_nodes':128,'full_Ward_error':error,'without_contact_error':float(np.max(abs(qh@bubble)))})
 return rows


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


def threshold(z):return 6*quad(lambda x:(x*(1-x))**2*z/(1+x*(1-x)*z),0,1,epsabs=2e-13)[0]


def check_threshold():
 rows=[]
 for z in [1e-8,1e-4,.1,1,10,1e3,1e6]:
  f=threshold(z);assert 0<f<1 and f<=z/5*(1+1e-12)
  loss=quad(lambda x:x*(1-x)*np.log1p(x*(1-x)*z),0,1,epsabs=2e-13)[0]
  assert 0<loss<=z/30*(1+1e-12)
  eps=1e-4
  slope=(quad(lambda x:x*(1-x)*np.log1p(x*(1-x)*z*np.exp(eps)),0,1)[0]-quad(lambda x:x*(1-x)*np.log1p(x*(1-x)*z*np.exp(-eps)),0,1)[0])/(2*eps)
  assert abs(6*slope-f)<1e-8
  rows.append({'z':z,'threshold_factor':f,'screening_loss_integral':loss})
 assert all(a['threshold_factor']<b['threshold_factor'] for a,b in zip(rows,rows[1:]))
 A=quad(lambda s:threshold(np.exp(-2*s)),0,30,epsabs=1e-11)[0]
 B=3*quad(lambda x:x*(1-x)*np.log1p(x*(1-x)),0,1,epsabs=1e-13)[0]
 assert abs(A-B)<1e-11 and 0<A<.1
 assert abs(threshold(1e-8)/1e-8-.2)<1e-8
 return {'massive_momentum_subtraction':rows,'remaining_IR_flow_integral':A,'independent_integrated_formula':B,'proved_upper_bound':.1}


def check_nonlinear():
 rows=[]
 N=2.
 for v0,c0,e0 in [(.3,1.,.4),(1.7,1.,.4),(1.,1.,.4),(.8,1.7,.4)]:
  def full(t,y):
   v,c,e=y
   return [e*e*(c-v)*(4*v*v+3*v*c+c*c)/(6*np.pi**2*c*(v+c)**2),N*e*e*(v*v-c*c)/(12*np.pi**2*v*c),-N*e**3/(12*np.pi**2*v)]
  def reduced(t,y):
   r,g,lc=y
   H=2*(4*r*r+3*r+1)/(r+1)**2+N*(r+1)
   return [-g*(r-1)*H/(12*np.pi**2),-N*g*g*(r+1/r)/(12*np.pi**2),N*g*(r*r-1)/(12*np.pi**2*r)]
  tt=np.r_[0,np.geomspace(.1,1e5,45)]
  a=solve_ivp(full,(0,tt[-1]),[v0,c0,e0],t_eval=tt,rtol=2e-10,atol=2e-12)
  b=solve_ivp(reduced,(0,tt[-1]),[v0/c0,e0*e0/c0,np.log(c0)],t_eval=tt,rtol=2e-10,atol=2e-12)
  converted=np.vstack([b.y[0]*np.exp(b.y[2]),np.exp(b.y[2]),np.sqrt(b.y[1]*np.exp(b.y[2]))])
  err=float(np.max(abs(converted-a.y)));assert err<2e-9
  ratio=a.y[0]/a.y[1];difference=abs(ratio-1)
  assert np.max(np.diff(difference))<1e-12
  assert a.y[:2].min()>=min(v0,c0)-1e-12 and a.y[:2].max()<=max(v0,c0)+1e-12
  # Independent quadrature invariant c(r), from dividing the two beta functions.
  r0=v0/c0;r=float(ratio[-1])
  fun=lambda x:-N*(x+1)/(x*(2*(4*x*x+3*x+1)/(x+1)**2+N*(x+1)))
  predicted=c0*np.exp(quad(fun,r0,r,epsabs=1e-12)[0])
  assert abs(predicted-a.y[1,-1])<1e-9
  rows.append({'initial_v_c_e':[v0,c0,e0],'ell':float(tt[-1]),'final_v_c_e':a.y[:,-1].tolist(),'full_vs_reduced_error':err,'independent_c_of_r_error':float(abs(predicted-a.y[1,-1]))})
 return rows


def longitudinal_shell(rho,v,c,sign,qd):
 direction,t,weight=qd;q=rho*direction;omega=rho*t;node=np.array([0.,0.,sign*np.arccos(.4)])
 H=symbol(node-q,v,.4);S=np.linalg.inv(1j*omega[:,None,None]*I+H)
 qhat=2*np.sin(q/2);Q=omega*omega+c*c*np.sum(qhat*qhat,axis=1)
 # Internal frequency is +omega, so exchanged photon frequency is -omega.
 X=-1j*omega[:,None,None]*I+sum(qhat[:,j,None,None]*vertex(node-q/2,j,v,.4) for j in range(3))
 assert np.max(abs(X+1j*omega[:,None,None]*I+H))<1e-13
 data=[];maximum=0.
 for a in range(4):
  d0=1j*I if a==0 else vertex(node,a-1,v,.4)
  di=np.broadcast_to(1j*I,S.shape) if a==0 else vertex(node-q,a-1,v,.4)
  Xp=d0-di;Sp=-S@di@S
  # Per unit (xi-1)e^2, with the minus sign of the inverse-propagator rainbow.
  direct=-(Xp@S@X+X@Sp@X+X@S@Xp)
  reduced=2*d0-di
  err=float(np.max(abs(direct-reduced)));maximum=max(maximum,err);assert err<3e-12
  correction=np.einsum('n,nab->ab',weight*rho**4*c*c/Q**2,direct)
  projection=(np.trace(correction)/(2j)).real if a==0 else (np.trace(sigma[a-1]@correction)/(2*v)).real*(sign if a==3 else 1)
  data.append(float(projection))
 target=1/(8*np.pi**2*c)
 return {'rho':rho,'v':v,'c':c,'node_sign':sign,'time_and_spatial_shifts_per_xi_minus_one_e2':data,'target_common_shift':target,'direct_vs_Ward_kernel_error':maximum,'max_residue_error':max(abs(x-target) for x in data),'largest_speed_shift':max(abs(v*(x-data[0])) for x in data[1:])}


def check_carrier_and_gauge():
    nodes=[]
    for zeta in [.2,.4,.7]:
        for v in [.7,1.,1.7]:
            # The only allowed x/y sine-zero corner has cos(kz)=zeta.
            required=[2+zeta-sx-sy for sx,sy in itertools.product([1,-1],repeat=2)]
            assert sum(abs(z)<=1 for z in required)==1
            for sign in [-1,1]:
                k=np.array([0.,0.,sign*np.arccos(zeta)])
                assert np.max(abs(symbol(k,v,zeta)))<1e-14
                J=np.array([[np.trace(s@vertex(k,j,v,zeta)).real/2 for j in range(3)] for s in sigma])
                assert np.max(abs(J.T@J-v*v*np.eye(3)))<1e-13
                assert np.sign(np.linalg.det(J))==sign
                nodes.append({'zeta':zeta,'v':v,'chirality':sign})
    for b in [.4,1.1]:
        z=.4;k0=np.arccos(z)
        locations=[(b,0.,k0),(b,0.,-k0),(-b,0.,-k0),(-b,0.,k0)]
        assert len(set(locations))==4
        charges=np.array([1,1,-1,-1]);chirality=np.array([1,-1,1,-1])
        assert np.dot(charges**3,chirality)==np.dot(charges,chirality)==0
    result={'cone_checks':nodes,'four_Weyl_Dirac_weight':2,'gauge_and_vertex':check_tensor_and_Ward(),'full_lattice_Ward':check_full_lattice_Ward()}
    print(json.dumps(result,sort_keys=True))


def check_lattice_residue_matching():
    qd=shell_samples();fermion=[];photon=[];longitudinal=[]
    for v,c,sign in [(.7,1.,1),(1.,1.,1),(1.7,1.,-1)]:
        for rho in [.16,.08,.04,.02,.01]:
            fermion.append(local_lattice_shell(rho,v,c,sign=sign,quad_data=qd))
            photon.append(polarization_shell(rho,v,sign=sign,quad_data=qd))
        fr=fermion[-5:];pr=photon[-5:]
        assert fr[-1]['max_error']<fr[0]['max_error']/20
        assert fr[-1]['max_error']<2e-5
        assert pr[-1]['maximum_residue_error']<pr[0]['maximum_residue_error']/20
        assert pr[-1]['maximum_residue_error']<2e-5
    for v,c,sign in [(.7,1.,1),(1.7,.8,-1)]:
        for rho in [.16,.08,.04,.02,.01]:
            longitudinal.append(longitudinal_shell(rho,v,c,sign,qd))
        lr=longitudinal[-5:]
        assert lr[-1]['max_residue_error']<lr[0]['max_residue_error']/20
        assert lr[-1]['largest_speed_shift']<2e-6
    print(json.dumps({'independent_parameter_and_frequency_residues':check_residues(),'fermion_shells':fermion,'per_Weyl_photon_shells':photon,'longitudinal_shells':longitudinal},sort_keys=True))


def check_tensor_and_metric_flow():
    print(json.dumps({'angular_tensor':check_angular_tensor(),'weighted_metric_flow':check_flow()},sort_keys=True))


def check_threshold_and_flow_limits():
    print(json.dumps({'massive_threshold':check_threshold(),'nonlinear_isotropic_flow':check_nonlinear()},sort_keys=True))


def main():
    failed=0
    families=[check_carrier_and_gauge,check_lattice_residue_matching,check_tensor_and_metric_flow,check_threshold_and_flow_limits]
    for check in families:
        try:
            check()
            print('PASS: '+check.__name__,flush=True)
        except Exception:
            failed+=1
            traceback.print_exc()
            print('FAIL: '+check.__name__,flush=True)
    print('per_element: exact midpoint vertices, Clifford traces and 24-point spherical moments challenge the algebraic normalization')
    print('per_site: the explicit nearest-neighbor symbol has four separated Weyl cones, with no imported taste or Dirac multiplicity')
    print('per_mode: full photon Ward cancellations and direct longitudinal matrix derivatives test the actual tensor and source vertices')
    print('per_block: independent frequency integrals, lattice shells, tensor contractions and coupled-flow solutions challenge distinct proof steps')
    print('lattice_wide: analytic integrable remainders establish one-loop logarithmic matching; no all-orders phase or physical pole is inferred')
    print(f'TOTAL: PASS={len(families)-failed} FAIL={failed}')
    return int(failed>0)

if __name__=='__main__':
    raise SystemExit(main())
