"""Narrow post-source BV/Gronwall/branch checks; no author suite import/run."""
from pathlib import Path
import hashlib,json,datetime,time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad_vec
OUT=Path(__file__).resolve().parent
start=time.perf_counter();checks=[]
def ck(name,ok,**details):checks.append({'name':name,'passed':bool(ok),**details})
def cl(name,a,b,tol=5e-10):
 e=float(np.max(abs(np.asarray(a)-np.asarray(b))));ck(name,e<=tol,error=e,tolerance=tol)
t,v,eta,sg=sp.symbols('t v eta sg',real=True)
u=sp.Rational(1,10)+t/20;sig=1-u*u
W=(1-t/10)*16*t*t*(1-t)**2
C=(1-t/10)*sp.Rational(32,5)*t*t*(1-t)**2+sig*sp.Rational(1,10)*16*t*t*(1-t)**2*u
b=sig*(sg*v*eta-u)/(1-sg*v*eta*u)
j=-sp.diff(b*W,t);rr=(b+sig*u)*W
afun=sp.lambdify((t,v,eta,sg),[b,j,rr],'numpy')
wfun=sp.lambdify(t,[W,C,u,sig,t/10+t*t/40],'numpy')
def pbound(expr,which):
 p=sp.Poly(sp.expand(expr),t);terms=[(m[0],abs(c)) for m,c in p.terms()]
 return float(sum(c/(n+1) if which=='l1' else c for n,c in terms))
Wl=pbound(W,'l1');W1=pbound(sp.diff(W,t),'l1');T1=pbound(sp.diff(W,t,2),'l1');Cl=pbound(C,'l1')
beta=.15;delta=.85;acc=.05;jerk=0.
Q0=1+beta;Q1=1+2*beta*(1+beta)
B0=Q0/delta;B1=Q1*acc/delta+Q0*acc/delta**2
B2=((2+6*beta)*acc**2+Q1*jerk)/delta+(2*Q1*acc**2+Q0*jerk)/delta**2+2*Q0*acc**2/delta**3
VF=(B2*Wl+2*B1*W1+B0*T1)/delta+acc*(B1*Wl+B0*W1)/delta**2
GF=(B1*Wl+B0*W1)/delta
R0=B0+beta;R1=B1+(1+2*beta**2)*acc
RL=R0*Wl/delta
VR=(R1*Wl+R0*W1)/delta+acc*R0*Wl/delta**2
H=.1;B=16.;mu=np.sqrt(B-2)*H;U0=mu**2*((1-H)**-2-1);U1=2*H*mu**2/(1-H)**3
S=mu**2*H/(1-H);R=np.exp(S/mu);CF=2*R*(VF+(U0/mu)*(GF+VR)+(U1/mu+U0+U0*U0/mu**2)*RL)
epsilon=(R*S*Cl*np.sqrt(np.pi/(4*mu))+2*np.sqrt(R*S*(1+beta)*Wl*(CF+VF)))/(np.sqrt(2)*np.pi)
records=[]
for k in [0.,.04,.4,4.,40.]:
 omega=np.hypot(k,mu);vel=k/omega
 def ode(tt,y):return [y[1],-(k*k+mu*mu/(1-H*tt)**2)*y[0]]
 sol=solve_ivp(ode,[0,1],[1.+0j,1j*omega],method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True,max_step=min(.02,1/(12*omega)))
 ck('independent_mode_solver_'+str(k),sol.success)
 def amps(tt):
  f,fp=sol.sol(tt);ap=(f+fp/(1j*omega))*np.exp(-1j*omega*tt)/2;am=(f-fp/(1j*omega))*np.exp(1j*omega*tt)/2
  U=mu*mu*((1-H*tt)**-2-1);Up=2*H*mu*mu/(1-H*tt)**3
  e=np.exp(2j*omega*tt);M=np.array([[1,1/e],[-e,-1]],complex)*1j*U/(2*omega)
  Mp=np.array([[1,1/e],[-e,-1]],complex)*1j*Up/(2*omega)+np.array([[0,-2j*omega/e],[-2j*omega*e,0]],complex)*1j*U/(2*omega)
  av=np.array([ap,am]);avp=M@av;avpp=(Mp+M@M)@av
  return av,avp,avpp,M,Mp
 ratios=[0.,0.,0.];matrix_errors=[]
 for tt in np.linspace(0,1,121):
  av,avp,avpp,M,Mp=amps(tt);U=mu*mu*((1-H*tt)**-2-1);Up=2*H*mu*mu/(1-H*tt)**3
  ratios[0]=max(ratios[0],np.sum(abs(av))/R);ratios[1]=max(ratios[1],np.sum(abs(avp))/(R*U0/mu));ratios[2]=max(ratios[2],np.sum(abs(avpp))/(R*(U1/mu+U0+U0*U0/mu**2)))
  matrix_errors.append(abs(np.linalg.norm(M,1)-abs(U)/omega))
  ck('matrix_derivative_bound_'+str(k)+'_'+str(round(float(tt),4)),np.linalg.norm(Mp,1)<=abs(Up)/omega+abs(U)+1e-13)
 cl('matrix_l1_norm_'+str(k),max(matrix_errors),0.,1e-13)
 for jn,ra in enumerate(ratios):ck('Gronwall_coefficient_bound_'+str(k)+'_'+str(jn),ra<=1+1e-10,max_ratio=float(ra))
 for z in [-.8,.3,1.]:
  def raw(tt,kind):
   ww,cc,uu,ss,xx=map(float,wfun(tt));f,fp=sol.sol(tt);phase=np.exp(-1j*k*z*xx)
   if kind=='force':return ss*ww*(1j*k*z*f-uu*fp)*phase/omega
   if kind=='frozen_force':return ss*ww*(1j*k*z-uu*1j*omega)*np.exp(1j*omega*tt)*phase/omega
   if kind=='clock_difference':return cc*(f-np.exp(1j*omega*tt))*phase/omega
  direct,_=quad_vec(lambda tt:raw(tt,'force'),0,1,epsabs=3e-12,epsrel=3e-12)
  frozen,_=quad_vec(lambda tt:raw(tt,'frozen_force'),0,1,epsabs=3e-12,epsrel=3e-12)
  clock,_=quad_vec(lambda tt:raw(tt,'clock_difference'),0,1,epsabs=3e-12,epsrel=3e-12)
  branches=[]
  for ix,sign in enumerate([1,-1]):
   def branch_integrated(tt):
    av,avp,_,_,_=amps(tt);bb,jj,rv=map(float,afun(tt,vel,z,sign));xx=float(wfun(tt)[4]);return (av[ix]*jj-avp[ix]*rv)*np.exp(1j*sign*omega*tt-1j*k*z*xx)/omega
   def branch_direct(tt):
    av,avp,_,_,_=amps(tt);ww,cc,uu,ss,xx=map(float,wfun(tt));ff=av[ix]*np.exp(1j*sign*omega*tt);ffp=(avp[ix]+1j*sign*omega*av[ix])*np.exp(1j*sign*omega*tt);return ss*ww*(1j*k*z*ff-uu*ffp)*np.exp(-1j*k*z*xx)/omega
   val,_=quad_vec(branch_integrated,0,1,epsabs=3e-12,epsrel=3e-12);bval,_=quad_vec(branch_direct,0,1,epsabs=3e-12,epsrel=3e-12)
   cl('individual_branch_IBP_'+str(k)+'_'+str(z)+'_'+str(sign),val,bval,5e-11);branches.append(val)
  cl('full_force_branch_sum_'+str(k)+'_'+str(z),sum(branches),direct,5e-11)
  ck('clock_global_difference_bound_'+str(k)+'_'+str(z),abs(clock)<=R*S*Cl/omega**2+1e-11,observed=float(abs(clock)),bound=R*S*Cl/omega**2)
  ck('force_low_difference_bound_'+str(k)+'_'+str(z),abs(direct-frozen)<=R*S*(1+beta)*Wl/omega+1e-11,observed=float(abs(direct-frozen)),bound=R*S*(1+beta)*Wl/omega)
  ck('variable_force_BV_bound_'+str(k)+'_'+str(z),abs(direct)<=CF/omega**2+1e-11,observed=float(abs(direct)),bound=CF/omega**2)
  ck('frozen_force_BV_bound_'+str(k)+'_'+str(z),abs(frozen)<=VF/omega**2+1e-11,observed=float(abs(frozen)),bound=VF/omega**2)
  if k:ck('force_high_difference_bound_'+str(k)+'_'+str(z),abs(direct-frozen)<=(CF+VF)/k**2+1e-11,observed=float(abs(direct-frozen)),bound=(CF+VF)/k**2)
  records.append({'k':k,'z':z,'force_difference':float(abs(direct-frozen)),'clock_difference':float(abs(clock))})
source={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('AUTHOR_*')}
result={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Targeted post-source potential-coefficient/force-branch/BV comparison; author aggregate suite not imported or run','author_source_snapshots':source,'independent_prior_identity_sha256':hashlib.sha256((OUT/'INDEPENDENT_IDENTITY_v1.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'counts':{'total':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)},'constants':dict(mu=mu,S=S,R=R,U0=U0,U1=U1,VF=VF,GF=GF,VR=VR,RL=RL,CF=CF,epsilon_C1=epsilon),'records':records,'elapsed_seconds':time.perf_counter()-start,'author_suite_rerun':False,'empirical_tests':0,'limits':['Finite checks support the source comparison but do not prove uniform BV or Gronwall bounds.','The complete handwritten proof and supplier derivations were checked separately.','The final four-endpoint exact Gram has a separately assigned independent checker; this script does not claim a fresh independent exact-Gram derivation.']}
p=OUT/'AUTHOR_COMPARISON_RESULTS_v1.json'
with p.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'counts':result['counts'],'elapsed_seconds':result['elapsed_seconds'],'source_sha256':result['source_sha256'],'result_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
raise SystemExit(0 if not result['counts']['failed'] else 1)
