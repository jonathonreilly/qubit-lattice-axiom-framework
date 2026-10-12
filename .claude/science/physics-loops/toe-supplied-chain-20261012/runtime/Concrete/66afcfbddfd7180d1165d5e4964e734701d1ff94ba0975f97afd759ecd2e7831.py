#!/usr/bin/env python3
"""Numerical diagnostics of the proven actual one-particle characteristic flow.

The proof supplies inequalities for all patches; this runner illustrates two
fixtures and compares a vector ODE with independent high-precision inversion
of the quadrature coordinate. It is not an interval-arithmetic certificate.
"""
import argparse,json,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import mpmath as mp

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True)
 ap.add_argument('--mutation',choices=['none','wrong_velocity','drop_half_density','reverse_clock'],default='none');a=ap.parse_args()
 rows=[];fixtures=[]
 def check(name,test): rows.append({'name':name,'ok':bool(test)})
 for J,g,k0,kappa,rho in [(1.,1.05,.03,.09,.5),(1.,2.,.025,.2,.10)]:
  c=np.sqrt(4*J*g);m=2*(g-J)
  E=lambda k:np.sqrt(m*m+4*c*c*np.sin(k/2)**2)
  Ep=lambda k:c*c*np.sin(k)/E(k)
  v=lambda k:E(k)/c
  def rhs(t,k):
   if a.mutation=='wrong_velocity':return np.ones_like(k)
   return (-1 if a.mutation=='reverse_clock' else 1)*v(k)
  nodes,weights=np.polynomial.legendre.leggauss(160);k=k0*nodes;w=k0*weights
  packet=(1-(k/k0)**2)**2;norm=np.sqrt(np.sum(w*packet**2));packet/=norm
  sol=solve_ivp(rhs,(0,rho),k,method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
  check('ODE succeeds '+str((J,g)),sol.success)
  f=sol.y[:,-1];Hz=E(f);Qz=c*np.sin(f)
  htarget=E(k)*np.cosh(rho)+c*np.sin(k)*np.sinh(rho)
  qtarget=c*np.sin(k)*np.cosh(rho)+E(k)*np.sinh(rho)
  herr=np.sqrt(np.sum(w*packet**2*(Hz-htarget)**2));qerr=np.sqrt(np.sum(w*packet**2*(Qz-qtarget)**2))
  Rmax=E(kappa)*(1-np.cos(kappa));hb=Rmax*(np.cosh(rho)-1);qb=Rmax*np.sinh(rho)
  patch_bound=k0*np.cosh(rho)+np.sqrt(k0*k0+(m/c)**2)*np.sinh(rho)
  check('proven support condition '+str((J,g)),patch_bound<kappa)
  check('numerical characteristic stays in patch '+str((J,g)),np.max(np.abs(sol.sol(np.linspace(0,rho,20))))<=kappa)
  check('integrated energy bound '+str((J,g)),herr<=hb+2e-12)
  check('integrated current bound '+str((J,g)),qerr<=qb+2e-12)
  # The Jacobian is E(F)/E(k). Wavefunctions are half-densities.
  jac=E(k)/E(f); amp=jac**(0 if a.mutation=='drop_half_density' else .5)
  check('actual boost half-density unitarity '+str((J,g)),np.max(np.abs(amp**2-jac))<1e-13)
  # Independent inversion: integral_k^F c/E = rho. No ODE helper reused.
  mp.mp.dps=45;jm=mp.mpf(str(J));gm=mp.mpf(str(g));cm=mp.sqrt(4*jm*gm);mm=2*(gm-jm)
  em=lambda u:mp.sqrt(mm*mm+16*jm*gm*mp.sin(u/2)**2)
  implicit=[]
  for initial in [-k0,0.,k0]:
   km=mp.mpf(str(initial));rm=mp.mpf(str(rho))
   ff=mp.findroot(lambda zz:mp.quad(lambda uu:cm/em(uu),[km,zz])-rm,(km,km+rm*em(km)/cm))
   direct=solve_ivp(rhs,(0,rho),[initial],method='DOP853',rtol=2e-13,atol=2e-14).y[0,-1]
   delta=abs(float(ff)-direct);implicit.append({'k_initial':initial,'quadrature_inverse':str(ff),'ODE_value':float(direct),'absolute_difference':delta})
   check('ODE/implicit independent route '+str((J,g,initial)),delta<2e-11)
  # Pointwise infinitesimal derivatives of the actual transported multipliers.
  eps=1e-6
  fp=solve_ivp(rhs,(0,eps),k,method='DOP853',rtol=2e-13,atol=2e-14).y[:,-1]
  fm=solve_ivp(rhs,(0,-eps),k,method='DOP853',rtol=2e-13,atol=2e-14).y[:,-1]
  hder=(E(fp)-E(fm))/(2*eps);qder=c*(np.sin(fp)-np.sin(fm))/(2*eps)
  hder_error=float(np.max(np.abs(hder-c*np.sin(k))));qder_error=float(np.max(np.abs(qder-E(k)*np.cos(k))))
  check('actual flow derivative energy '+str((J,g)),hder_error<3e-9)
  check('actual flow derivative current '+str((J,g)),qder_error<3e-9)
  fixtures.append({'J':J,'g':g,'m':m,'c':c,'initial_patch':k0,'control_patch':kappa,'rapidity':rho,
   'support_upper_bound':patch_bound,'observed_support_max':float(np.max(np.abs(f))),
   'energy_packet_error':float(herr),'energy_bound':float(hb),'current_packet_error':float(qerr),'current_bound':float(qb),
   'residual_operator_patch_bound':float(Rmax),'max_flow_energy_derivative_error':hder_error,'max_flow_current_derivative_error':qder_error,
   'independent_quadrature':implicit})
 out={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__,'mutation':a.mutation,
  'method':'DOP853 rtol 2e-13 atol 2e-14; 160-point Gauss-Legendre packet quadrature; 45-decimal implicit mpmath quadrature','numeric_proof':False,'checks':rows,'fixtures':fixtures}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'checks':len(rows),'failed':[r['name'] for r in rows if not r['ok']],'fixtures':fixtures},indent=2))
 raise SystemExit(0 if all(r['ok'] for r in rows) else 1)
if __name__=='__main__': main()
