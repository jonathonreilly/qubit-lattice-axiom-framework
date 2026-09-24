#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Finite-time validation from the own complete local matrices.
Small-spin controls exponentiate the full 256-dimensional Lindblad generator.
Moving-spin controls use a stable exact 2x2 no-event exponential, together
with the previously verified exact number-sector energy identity.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/star_finite_time_control.py', 'scripts/star_local_matrix_control.py')
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import contextlib,importlib.util,json,math,cmath
import numpy as np
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('own_local_matrix',HERE/'star_local_matrix_control.py')
m=importlib.util.module_from_spec(spec)
with (HERE/'finite_time_symbolic_import.log').open('w') as out:
 with contextlib.redirect_stdout(out):spec.loader.exec_module(m)

DELTA=1.3;K=1.7;KAPPA=0.7

def numeric(mat,eps,ell):return np.asarray(mat.subs({m.EPS:eps,m.DELTA:DELTA,m.ELL:ell,m.KAPPA:KAPPA,m.C:1}),dtype=np.complex128)

def stable_noevent(eps,ell,t):
 omega=DELTA/eps**4;gamma=2*KAPPA/eps**2;den=1+3*eps**2
 q=ell-1j*gamma
 tr=omega*den+q
 det=3*omega*eps**2*q
 fast=(tr+cmath.sqrt(tr*tr-4*det))/2
 slow=det/fast
 matrix=np.array([[3*omega*eps**2,-math.sqrt(3)*omega*eps],[-math.sqrt(3)*omega*eps,omega+q]],complex)
 ident=np.eye(2,dtype=complex)
 prop=cmath.exp(-1j*slow*t)*(matrix-fast*ident)/(slow-fast)+cmath.exp(-1j*fast*t)*(matrix-slow*ident)/(fast-slow)
 initial=np.array([1,math.sqrt(3)*eps],complex)/math.sqrt(den)
 v=prop@initial
 p=float(np.vdot(v,v).real)
 z=v[1]-math.sqrt(3)*eps*v[0]
 e1=omega*abs(z)**2+ell*abs(v[1])**2
 return v,p,float(e1)

full=[]
for S,lam in [(1,0.0),(2,0.5),(3,1.0)]:
 eps=math.sqrt(DELTA/(K*S*(S+1)));ell=lam*K;t=0.4
 H=numeric(m.H,eps,ell);psi=numeric(m.psi,eps,ell).reshape(-1)
 rho=np.outer(psi,psi.conj());I=np.eye(m.DIM,dtype=complex)
 P3=numeric(m.Q3,eps,ell);P1=numeric(m.Q1,eps,ell)
 coef=1.5*DELTA/eps**2+2*ell
 for instrument in ('resolved','coherent'):
  channels=list(m.J.values()) if instrument=='resolved' else [m.J[b,1]+m.J[b,-1] for b in (1,2,3)]
  L=-1j*(np.kron(I,H)-np.kron(H.T,I))
  for j in channels:
   jump=math.sqrt(KAPPA)/eps*numeric(j,eps,ell);loss=jump.conj().T@jump
   L+=np.kron(jump.conj(),jump)-.5*np.kron(I,loss)-.5*np.kron(loss.T,I)
  rt=(expm(L*t)@rho.reshape(-1,order='F')).reshape((m.DIM,m.DIM),order='F')
  p3=float(np.trace(P3@rt).real);E3=float(np.trace(P3@H@rt).real)
  E1=float(np.trace(P1@H@rt).real);ET=float(np.trace(H@rt).real)
  v,p1_ref,e1_ref=stable_noevent(eps,ell,t)
  trace_error=abs(np.trace(rt)-1);hermiticity=np.linalg.norm(rt-rt.conj().T)
  energy_residual=abs(E3-coef*p3)
  assert trace_error<2e-11 and hermiticity<2e-11
  assert energy_residual<2e-9
  assert abs((1-p3)-p1_ref)<2e-11 and abs(E1-e1_ref)<2e-9
  assert abs(ET-E1-E3)<2e-9
  full.append({'S':S,'lambda':lam,'instrument':instrument,'epsilon':eps,'time':t,
   'P_N3':p3,'E_N3':E3,'energy_per_N3':E3/p3,'exact_energy_per_N3':coef,
   'E_N1':E1,'E_total':ET,'trace_error':float(trace_error),'hermiticity_error':float(hermiticity),
   'number_sector_energy_residual':energy_residual,'survival_difference_to_2x2':abs((1-p3)-p1_ref)})

moving=[]
for lam in (0.0,0.5,1.0):
 ell=lam*K
 for t in (0.2,1.0):
  limit=1.5*DELTA*(1-math.exp(-12*KAPPA*t))
  for S in (4,8,16,32,64,128,256,512):
   eps=math.sqrt(DELTA/(K*S*(S+1)))
   v,p1,e1=stable_noevent(eps,ell,t)
   p3=1-p1;energy=e1+(1.5*DELTA/eps**2+2*ell)*p3
   p_limit=math.exp(-12*KAPPA*t)
   assert 0<=p1<=1+1e-12 and e1>=0
   moving.append({'S':S,'lambda':lam,'epsilon':eps,'time':t,'P_N3':p3,
    'P_N1_error_over_epsilon2':(p1-p_limit)/eps**2,'E_N1':e1,'E_N1_over_epsilon2':e1/eps**2,
    'E_total':energy,'epsilon2_E_total':eps**2*energy,'predicted_limit':limit,
    'scaled_energy_error_over_epsilon2':(eps**2*energy-limit)/eps**2})
# These finite cases corroborate, but do not replace, the analytic uniform
# O(epsilon^3) bound on the no-event dressing mismatch.
result={'parameters':{'delta':DELTA,'K':K,'kappa':KAPPA},'full_Lindblad_controls':full,
        'moving_spin_controls':moving,'scientific_role':'numerical corroboration; analytic proof is in PRE_RECONSTRUCTION.md'}
(HERE/'FINITE_TIME_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'full_Lindblad_controls':full,'largest_spin_rows':[r for r in moving if r['S']==512]},indent=2))
