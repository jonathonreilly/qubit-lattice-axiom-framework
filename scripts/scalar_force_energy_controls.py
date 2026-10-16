"""Conditional conformal force and physical energy normalization controls."""
from pathlib import Path
import json,hashlib,time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
AUDIT_TIMEOUT_SEC=120

def mode_energy_bound(alpha, energies):
 return np.sqrt(2*(alpha@alpha)*sum(energies))

def run_checks():
 checks=[];trajectories=[];norms=[];frames=[]
 def check(label,ok):
  assert bool(ok),label
  checks.append(label)
 v=sp.Matrix(sp.symbols('v1:4',real=True));g=sp.Matrix(sp.symbols('g1:4',real=True))
 A=sp.symbols('A',positive=True);lt=sp.symbols('lt',real=True)
 r=(v.T*v)[0];Lag=-A*sp.sqrt(1-r)
 momentum=sp.Matrix([sp.diff(Lag,x) for x in v]);H=momentum.jacobian(v)
 acceleration=-(1-r)*(g+v*lt)
 residual=H*acceleration+momentum*(lt+(v.T*g)[0])+A*sp.sqrt(1-r)*g
 for i,entry in enumerate(residual):
  check(f'Euler_Lagrange_component_{i}',sp.simplify(entry)==0)
 # Momentum and coordinate-acceleration ODEs use independently evolved variables.
 wave=np.array([.6,-.4,.7])
 for eps,omega in [(.03,.8),(.25,1.1),(.2,0.)]:
  def ell(t,x):return eps*np.sin(omega*t+.3)*np.cos(wave@x)
  def grad(t,x):return -eps*np.sin(omega*t+.3)*np.sin(wave@x)*wave
  def partial(t,x):return eps*omega*np.cos(omega*t+.3)*np.cos(wave@x)
  x0=np.array([.2,-.3,.4]);v0=np.array([.2,.1,-.12]);a0=np.exp(ell(0,x0))
  p0=a0*v0/np.sqrt(1-v0@v0)
  def rhs_momentum(t,y):
   x,p=y[:3],y[3:];aa=np.exp(ell(t,x));den=np.sqrt(aa*aa+p@p);vv=p/den
   return np.r_[vv,-aa*aa/den*grad(t,x)]
  def rhs_velocity(t,y):
   x,vv=y[:3],y[3:]
   return np.r_[vv,-(1-vv@vv)*(grad(t,x)+vv*partial(t,x))]
  ts=np.linspace(0,4,101)
  solp=solve_ivp(rhs_momentum,[0,4],np.r_[x0,p0],rtol=3e-12,atol=3e-13,t_eval=ts)
  solv=solve_ivp(rhs_velocity,[0,4],np.r_[x0,v0],rtol=3e-12,atol=3e-13,t_eval=ts)
  check(f'ODE_success_{eps}_{omega}',solp.success and solv.success)
  recovered=np.array([solp.y[3:,i]/np.sqrt(np.exp(2*ell(t,solp.y[:3,i]))+solp.y[3:,i]@solp.y[3:,i]) for i,t in enumerate(ts)]).T
  err=max(np.max(abs(solp.y[:3]-solv.y[:3])),np.max(abs(recovered-solv.y[3:])))
  check(f'canonical_momentum_vs_acceleration_{eps}_{omega}',err<5e-10)
  omitted=(1-v0@v0)*v0*partial(0,x0)
  if omega:check(f'partial_time_force_material_{eps}_{omega}',np.linalg.norm(omitted)>1e-3)
  trajectories.append(dict(epsilon=eps,frequency=omega,max_trajectory_or_velocity_error=float(err),
                           initial_omitted_partial_time_term=omitted.tolist()))
 # Coefficient derivative budgets on a genuinely turning/accelerating path.
 T=1.2;u=.18;aa=.04;ox=1.7;bb=.025;rho=.43
 V=np.sqrt(u*u+(aa*ox)**2+(bb*T)**2);A2=np.sqrt((aa*ox*ox)**2+bb*bb);J3=abs(aa*ox**3)
 N1=abs(rho);N2=rho*rho
 Pb=np.array([1.,2*V*A2+N1,2*(A2*A2+V*J3)+4*V*A2*N1+N2])
 Rb=np.array([V,2*V*V*A2+N1*V+A2,2*V*(A2*A2+V*J3)+4*V*A2*(N1*V+A2)+N2*V+2*N1*A2+J3])
 actualP=[];actualR=[]
 for t in np.linspace(-T,T,101):
  vv=np.array([u,aa*ox*np.cos(ox*t),bb*t])
  ac=np.array([0.,-aa*ox**2*np.sin(ox*t),bb])
  jj=np.array([0.,-aa*ox**3*np.cos(ox*t),0.])
  n=np.array([np.cos(rho*t),np.sin(rho*t),0.]);nd=rho*np.array([-np.sin(rho*t),np.cos(rho*t),0.]);ndd=-rho*rho*n
  L=1-vv@vv;Lp=-2*(vv@ac);Lpp=-2*(ac@ac+vv@jj)
  b0=n@vv;b1=nd@vv+n@ac;b2=ndd@vv+2*nd@ac+n@jj
  actualP.append([np.linalg.norm(L*n),np.linalg.norm(Lp*n+L*nd),np.linalg.norm(Lpp*n+2*Lp*nd+L*ndd)])
  actualR.append(np.abs([L*b0,Lp*b0+L*b1,Lpp*b0+2*Lp*b1+L*b2]))
 for i in range(3):
  check(f'P_derivative_budget_{i}',max(x[i] for x in actualP)<=Pb[i]+1e-14)
  check(f'R_derivative_budget_{i}',max(x[i] for x in actualR)<=Rb[i]+1e-14)
 # Candidate coupling ceiling is exact algebra, conditional on its supplied action.
 kk=sp.symbols('k',real=True);ak=(1-kk)*(1+3*kk)/4
 check('candidate_coupling_ceiling_identity',sp.expand(sp.Rational(1,3)-ak-(1-3*kk)**2/12)==0)
 # Independent numerical angular integration for the first-jet reference-path norm.
 for speed in [0.,.2,.65,.9,.99]:
  par=quad(lambda z:(z-speed)**2/(1-speed*z)**3,-1,1,epsabs=1e-11)[0]*(1-speed*speed)**2/(2*np.pi)
  perp=quad(lambda z:(1-z*z)/(1-speed*z)**3,-1,1,epsabs=1e-11)[0]*(1-speed*speed)**2/(4*np.pi)
  # Stationary coefficients in the general envelope have C0=1+speed and C1=C2=0.
  coarse=2/(3*np.pi**2)*(4*(1+speed)/(1-speed)**2)**1.5*np.sqrt(1+speed)
  check(f'forcejet_exact_norm_inside_envelope_{speed}',max(par,perp)<=coarse)
  if speed:
   lr=np.log((1+speed)/(1-speed))
   exact_par=(1-speed*speed)**2*(lr-2*speed)/(2*np.pi*speed**3)
   exact_perp=(1-speed*speed)*(2*speed-(1-speed*speed)*lr)/(4*np.pi*speed**3)
   check(f'forcejet_parallel_angular_antiderivative_{speed}',abs(par-exact_par)<2e-13)
   check(f'forcejet_perpendicular_angular_antiderivative_{speed}',abs(perp-exact_perp)<2e-13)
  if speed==0:check('forcejet_rest_limit',max(abs(par-1/(3*np.pi)),abs(perp-1/(3*np.pi)))<1e-14)
  norms.append(dict(speed=speed,parallel_norm_squared=par,perpendicular_norm_squared=perp,coarse_norm_squared=coarse))
 # Frame scaling using a directly integrated dipolar Gaussian energy formula.
 for Ab,Q,alpha,ell,mu,amp in [(.4,3.,.2,.7,.8,.3),(2.3,.7,.4,1.1,.2,.1),(1.,2.,.1,.8,0.,.5)]:
  eE=amp*amp*np.pi**1.5*ell*(5/8+mu*mu*ell*ell/4)
  ellJ=Ab*ell;muJ=mu/Ab
  eJ=amp*amp*np.pi**1.5*ellJ*(5/8+muJ*muJ*ellJ*ellJ/4)
  QJ=Q/(Ab*Ab);physE=2*Q*eE;physJ=2*QJ*eJ
  cbE=1/(3*np.pi);cbJ=1/(3*np.pi*Ab**3)
  boundE=abs(alpha)*np.sqrt(physE/Q*cbE);boundJ=abs(alpha)*np.sqrt(physJ/QJ*cbJ)
  Gbare=Ab*Ab/(8*np.pi*Q)
  fromG=np.sqrt(8*np.pi*Gbare*alpha*alpha*physJ*cbJ)
  check(f'Gaussian_energy_frame_scaling_{Ab}',abs(eJ-Ab*eE)<1e-14)
  check(f'physical_energy_frame_scaling_{Ab}',abs(physJ-physE/Ab)<1e-14)
  check(f'acceleration_frame_scaling_{Ab}',abs(boundJ-boundE/Ab)<1e-14)
  check(f'Q_to_G_normalization_{Ab}',abs(boundJ-fromG)<1e-14)
  frames.append(dict(Ab=Ab,Q=Q,energy_E=eE,energy_J=eJ,physical_energy_E=physE,physical_energy_J=physJ,bound_E=boundE,bound_J=boundJ))
 # Joint finite-mode budget and an attained aligned example. No independent full
 # energy allocation to every mode. The mathematical inequality is analytic.
 rng=np.random.default_rng(143)
 for j in range(12):
  alpha=rng.normal(size=3);energies=rng.uniform(.01,2.,size=3);values=np.sqrt(2*energies)*rng.uniform(-1,1,size=3)
  bound=mode_energy_bound(alpha,energies)
  check(f'joint_mode_energy_{j}',abs(alpha@values)<=bound)
 alpha=np.array([.2,-.3,.1]);etot=.8;energy=etot*alpha*alpha/(alpha@alpha)
 vals=np.sign(alpha)*np.sqrt(2*energy)
 check('joint_mode_budget_attainment',abs(alpha@vals-mode_energy_bound(alpha,energy))<1e-14)
 result=dict(checks_passed=len(checks),checks=checks,momentum_ODE_controls=trajectories,
             coefficient_budgets=dict(P=Pb.tolist(),R=Rb.tolist(),P_observed_max=np.max(actualP,axis=0).tolist(),R_observed_max=np.max(actualR,axis=0).tolist()),
             constant_velocity_force_norms=norms,frame_controls=frames,
             scope='Conditional point-particle action, prescribed-path linear force functional, joint energy and constant-frame conversion. All controls synthetic; no empirical fit or physical energy calibration.')
 return result
