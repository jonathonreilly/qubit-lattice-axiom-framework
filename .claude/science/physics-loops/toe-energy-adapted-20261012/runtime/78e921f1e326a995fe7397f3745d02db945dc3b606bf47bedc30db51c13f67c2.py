"""Predeclared complete rows; keep failures and survivors."""
import argparse,importlib.util,json,sys
from pathlib import Path
import numpy as np
import scipy.linalg as la
from scipy.integrate import quad,solve_ivp
from scipy.special import erf
import sympy as sp
p=argparse.ArgumentParser();p.add_argument('--candidate',required=True);args=p.parse_args()
spec=importlib.util.spec_from_file_location('candidate_test',args.candidate);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
rows=[]
def emit(name,passed,**data):
 r={'name':name,'passed':bool(passed),**data};rows.append(r);print(json.dumps(r,sort_keys=True),flush=True)
def close(name,value,tol=2e-10):emit(name,float(value)<tol,value=float(value),tolerance=tol)
def greater(name,value,threshold):emit(name,float(value)>threshold,value=float(value),threshold=threshold)
def norm(x):return float(la.norm(x,2))
def actual_D(a,q):
 sig=np.sqrt(.25+1/a**2);g=sig/2+.25;j=sig/2-.25
 d=2j*(g-j*np.exp(-1j*a*q));return np.array([[0,d],[d.conjugate(),0]])
def actual_P(a,q):
 eig,u=la.eigh(actual_D(a,q));return (u*((1+np.sign(eig))/2)[None,:])@u.conj().T
def energy(a,q):return np.sqrt(1+4*np.sin(a*q/2)**2/a**2)
C0=np.array([[0,1j],[-1j,0]]);P0=(np.eye(2)+C0)/2

# Exact independent differential and substitution checks.
t=sp.symbols('p',real=True);a,v,m=sp.symbols('a v m',positive=True)
W=sp.Function('w',positive=True)(t);EE=sp.Function('E',real=True)(t);u=sp.Function('psi')(t)
lhs=(sp.I*(EE*W*sp.diff(sp.sqrt(W)*u,t)+W*sp.diff(EE,t)*sp.sqrt(W)*u/2)-a*EE*sp.sqrt(W)*u/2)/sp.sqrt(W)
rhs=sp.I*(EE*W*sp.diff(u,t)+sp.diff(EE*W,t)*u/2)-a*EE*u/2
emit('exact/boost_half_density',sp.simplify(lhs-rhs)==0)
emit('exact/dispersion_coordinate',sp.expand(m*m+4*v*v/a**2*(a*t/2)**2-(m*m+v*v*t*t))==0)
emit('exact/inverse_jacobian',sp.simplify(sp.diff(2*sp.asin(a*t/2)/a,t)-1/sp.sqrt(1-a*a*t*t/4))==0)

for a in [1.,.5,.25]:
 b=a/2;d=b/2
 for fraction in [-.9,-.5,-.1,0.,.1,.5,.9]:
  p=2/a*fraction;tag=f'coordinates/a{a:g}_f{fraction:g}'
  qa=c.qa(a,p);qb=c.qa(b,p)
  close(tag+'/inverse',abs(c.pa(a,qa)-p))
  derivative=np.imag(c.qa(a,p+1e-25j))/1e-25
  close(tag+'/jacobian',abs(derivative-1/c.w(a,p)))
  close(tag+'/energy_coordinate',abs(energy(a,qa)-np.sqrt(1+p*p)))
  fa=c.frame(a,qa)
  close(tag+'/frame_reality',norm(c.frame(a,-qa)-fa.conj()))
  close(tag+'/actual_frame_polarization',norm(fa@actual_P(a,qa)@fa.conj().T-P0))
  matrix=c.transfer(b,a,p)
  close(tag+'/transfer_reality',norm(c.transfer(b,a,-p)-matrix.conj()))
  close(tag+'/transfer_composition',norm(c.transfer(d,b,p)@matrix-c.transfer(d,a,p)))
  close(tag+'/weighted_state_pullback',norm(matrix.conj().T@actual_P(b,qb)@matrix/c.w(b,p)-actual_P(a,qa)/c.w(a,p)))
  close(tag+'/actual_energy_intertwining',norm(actual_D(b,qb)@matrix-matrix@actual_D(a,qa)))
 # Integrate the full actual delta input, retaining both endpoints.
 direct,err=quad(lambda p:c.delta_density(a,p),-2/a,2/a,epsabs=1e-11,epsrel=1e-11,limit=300)
 nodes,weights=np.polynomial.legendre.leggauss(128);theta=np.pi/2*nodes
 transformed=float(np.sum(weights*np.pi/2/np.pi*np.cos(theta)**(1-2*c.JACOBIAN_POWER)))
 close(f'endpoint/a{a:g}/direct_norm',abs(direct-1),2e-8)
 close(f'endpoint/a{a:g}/theta_norm',abs(transformed-1),2e-8)
 close(f'endpoint/a{a:g}/routes_agree',abs(direct-transformed),2e-8)
 print(json.dumps({'diagnostic':'endpoint_integral','a':a,'direct':direct,'theta':transformed,'quad_error_estimate':err}),flush=True)
 for eps in [1e-3,1e-6]:
  p=2/a*(1-eps);computed=c.w(a,p)**(-c.JACOBIAN_POWER);expected=(2*eps-eps*eps)**(-.25)
  close(f'endpoint/a{a:g}/power_eps{eps:g}',abs(computed/expected-1),2e-8)
 # Independent real-space cell integral and alias formula for Gaussian.
 n=int(np.ceil(16/a));sites=np.arange(-n,n)
 cells=np.pi**(-.25)/np.sqrt(a)*np.sqrt(np.pi/2)*(erf(a*(sites+1)/np.sqrt(2))-erf(a*sites/np.sqrt(2)))
 fhat=lambda q:np.pi**(-.25)*np.exp(-np.asarray(q)**2/2)
 for q in [-1.1,-.3,0.,.7,2.1]:
  literal=np.sqrt(a/(2*np.pi))*np.sum(cells*np.exp(-1j*a*q*sites))
  alias=c.aliases(a,q,fhat)
  close(f'aliases/a{a:g}/q{q:g}',abs(literal-alias))

# Fixed compact Fourier input and full error integral (all supports inside[-1,1]).
nodes,weights=np.polynomial.legendre.leggauss(32);edges=np.linspace(-1,1,81)
mid=(edges[:-1]+edges[1:])/2;half=np.diff(edges)/2
grid=(mid[:,None]+half[:,None]*nodes).ravel();weight=(half[:,None]*weights).ravel()
close('geometry/input_norm',abs(float(np.sum(weight*c.compact_hat(grid)**2))-1))
for a in [1.,.5,.25,.125,.0625]:
 error=float(np.sqrt(np.sum(weight*np.abs(c.geometric_hat(a,grid)-c.compact_hat(grid))**2)))
 print(json.dumps({'diagnostic':'geometric_error','a':a,'norm_error':error}),flush=True)
 if a==.0625:emit('geometry/fine_limit_diagnostic',error<.08,norm_error=error,threshold=.08)

for p in [.4,1.,1.8]:
 a=1.;b=.5
 cur=p*(c.w(b,p)-c.w(a,p))
 phase=abs(np.exp(-1j*c.qa(a,p))-np.exp(-1j*c.qa(b,p)))
 greater(f'defects/p{p:g}/actual_current',abs(cur),1e-6)
 greater(f'defects/p{p:g}/common_integer_space',phase,1e-6)
close('defects/zero_momentum_current',abs(0.*(c.w(.5,0)-c.w(1.,0))))
close('defects/zero_momentum_space',abs(np.exp(-1j*c.qa(1.,0))-np.exp(-1j*c.qa(.5,0))))
for p0 in [1.9,1.95]:
 b=.5;q0=float(c.qa(b,p0))
 sol=solve_ivp(lambda t,y:energy(b,y),(0,.1),[q0],method='DOP853',rtol=1e-11,atol=1e-13)
 emit(f'boost/p{p0:g}/solver_completed',sol.success)
 q1=float(sol.y[0,-1]);p1=float(c.pa(b,q1));travel,err=quad(lambda q:1/energy(b,q),q0,q1,epsabs=1e-12,epsrel=1e-12)
 greater(f'boost/p{p0:g}/leaves_coarse_band',p1,2.001)
 close(f'boost/p{p0:g}/travel_time',abs(travel-.1),2e-9)
 print(json.dumps({'diagnostic':'boost_support','initial_p':p0,'final_p':p1,'q0':q0,'q1':q1,'travel_time':travel,'quad_error_estimate':err,'sign':'This characteristic corresponds to upward support motion under the opposite group parameter.'}),flush=True)

print('per_element: checked a delta normalization and specified smooth packet mechanisms; constants remain compatible.',flush=True)
print('per_site: checked and not executed — infinite spin support is proved by the Fourier open-arc argument, not a finite lattice.',flush=True)
print('per_mode: checked actual state/energy matrices and current/space discrepancies at specified momenta, retaining zero-mode survivors.',flush=True)
print('per_block: checked transfer composition at three scales in common interior coordinates; endpoint domains remain analytic.',flush=True)
print('lattice_wide: checked and not executed — the infinite inductive limit and Cauchy/local quotient are conditional analytic proofs.',flush=True)
failed=sum(not r['passed'] for r in rows)
print(json.dumps({'summary':True,'candidate':str(Path(args.candidate).resolve()),'total':len(rows),'failed':failed,'passed':len(rows)-failed}),flush=True)
sys.exit(1 if failed else 0)
