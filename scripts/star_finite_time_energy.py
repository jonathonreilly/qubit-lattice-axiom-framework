#!/usr/bin/env python3
"""Root extension: exact no-event reduction plus full finite GKLS control.
The complete-matrix comparison reuses the pinned root star operator builder;
it is an internal consistency check, not independent review.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/star_finite_time_energy.py', 'scripts/exact_star_energy.py')
from pathlib import Path
import hashlib,importlib.util,json,sys
sys.dont_write_bytecode=True
import numpy as np
import sympy as s
import mpmath as mp
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'exact_star_energy.py'
expected='6430b8fbc0766ac6e78c4beba477d8356028b9fd241e7ed04945d58501eb855b'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==expected
spec=importlib.util.spec_from_file_location('sealed_root_star',SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
e,delta,kappa=m.e,m.delta,m.kappa
a=1+3*e**2
H=s.Matrix([[3*delta/e**2,-s.sqrt(3)*delta/e**3],[-s.sqrt(3)*delta/e**3,delta/e**4]])
W=s.diag(0,1);G=-s.I*H-2*kappa/e**2*W
lam=s.symbols('lam')
assert s.simplify(e**4*(G-lam*s.eye(2)).det()-(e**4*lam**2+(s.I*delta*a+2*kappa*e**2)*lam+s.I*6*kappa*delta))==0
ell=s.Matrix([1,s.sqrt(3)*e])/s.sqrt(a);high=s.Matrix([s.sqrt(3)*e,-1])/s.sqrt(a)
U=s.Matrix.hstack(ell,high);rot=s.simplify(U.T*G*U)
assert s.simplify(rot[0,0]+6*kappa/a)==0
assert s.simplify(rot[1,1]+2*kappa/(e**2*a)+s.I*delta*a/e**4)==0
assert s.simplify(rot[1,0]-2*s.sqrt(3)*kappa/(e*a))==0
assert rot[0,1]==rot[1,0]
# Whole physical N=1 loss, not just the symmetric initial vector.
Gamma=s.zeros(4)
for b in (1,2,3):
 for sign in (1,-1):
  j=m.jump(b,sign);Gamma+=j.T*j
assert Gamma==4*m.W1
# N=3 has no state with both A and one B empty, so no further mark is legal.
assert all(not(q[0]==0 and q[b]==0) for q in m.bases[3] for b in (1,2,3))
# Complete physical GKLS matrix uses the pinned 4+12 matrix builder.
rows=[]
for eps,dd,kk in [(0.5,0.7,1.3),(0.25,1.,0.4),(0.125,1.2,0.8)]:
 hh1=np.array((dd/eps**4*m.h1).subs(e,eps),dtype=float)
 hh3=np.array((dd/eps**4*m.h3).subs(e,eps),dtype=float)
 full=np.zeros((16,16));full[:4,:4]=hh1;full[4:,4:]=hh3
 eye=np.eye(16);L=-1j*(np.kron(eye,full)-np.kron(full.T,eye))
 for b in (1,2,3):
  for sig in (1,-1):
   J=np.zeros((16,16));J[4:,:4]=np.sqrt(kk)/eps*np.array(m.jump(b,sig),dtype=float)
   JJ=J.T@J
   L+=np.kron(J,J)-0.5*np.kron(eye,JJ)-0.5*np.kron(JJ.T,eye)
 psi=np.zeros(16);psi[:4]=np.array(m.psi_num.subs(e,eps),dtype=float).ravel()/np.sqrt(1+3*eps**2)
 rho=np.outer(psi,psi);vec=rho.reshape(256,order='F')
 G2=np.array(G.subs({e:eps,delta:dd,kappa:kk}),dtype=complex)
 initial=np.array([1,np.sqrt(3)*eps])/np.sqrt(1+3*eps**2)
 H2=np.array(H.subs({e:eps,delta:dd}),dtype=float)
 for t in (.01,.08,.3):
  nt=expm(G2*t)@initial;p=1-float(np.vdot(nt,nt).real)
  E_no=float(np.vdot(nt,H2@nt).real);prediction=E_no+1.5*dd/eps**2*p
  evolved=(expm(L*t)@vec).reshape((16,16),order='F')
  p_full=float(np.trace(evolved[4:,4:]).real);E_full=float(np.trace(full@evolved).real)
  err=abs(E_full-prediction);assert abs(p-p_full)<2e-9,(eps,t,p,p_full)
  assert err<2e-7*(1+abs(prediction)),(eps,t,E_full,prediction)
  assert E_no>=-1e-9
  rows.append({'epsilon':eps,'delta':dd,'kappa':kk,'time':t,'P_birth_2x2':p,'P_birth_full_GKLS':p_full,'energy_no_event':E_no,'energy_full_GKLS':E_full,'energy_prediction':prediction,'absolute_energy_error':err})
mp.mp.dps=70
limit=[]
for spin in (1,2,4,8,16,32,64):
 cc=spin*(spin+1);eps=1/mp.sqrt(cc)
 gg=mp.matrix([[-3j/eps**2,1j*mp.sqrt(3)/eps**3],[1j*mp.sqrt(3)/eps**3,-1j/eps**4-2/eps**2]])
 ll=mp.matrix([1,mp.sqrt(3)*eps])/mp.sqrt(1+3*eps**2)
 hi=mp.matrix([mp.sqrt(3)*eps,-1])/mp.sqrt(1+3*eps**2)
 t=mp.mpf('0.2');out=mp.expm(gg*t)*ll
 prob=1-sum(abs(x)**2 for x in out);bet=(hi.T*out)[0]
 en=(1+3*eps**2)/eps**4*abs(bet)**2;total=en+mp.mpf('1.5')/eps**2*prob
 limit.append({'S':spin,'C':cc,'epsilon':mp.nstr(eps,30),'P_birth':mp.nstr(prob,30),'P_birth_limit':mp.nstr(1-mp.exp(-12*t),30),'epsilon_squared_energy':mp.nstr(eps**2*total,30),'limiting_scaled_energy':mp.nstr(mp.mpf('1.5')*(1-mp.exp(-12*t)),30),'no_event_energy':mp.nstr(en,30)})
result={'status':'Root finite-time consistency control; independent extension review pending','source_sha256':expected,'exact_symbolic_checks':['complete loss Gamma=4W','characteristic polynomial','orthonormal low/high generator','no further microscopic star birth in N3'],'full_GKLS_rows':rows,'high_precision_joint_limit_rows':limit,'failures':[]}
(HERE/'STAR_FINITE_TIME_ENERGY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'full_GKLS_cases':len(rows),'max_energy_error':max(r['absolute_energy_error'] for r in rows),'last_joint_limit_row':limit[-1]},indent=2))
