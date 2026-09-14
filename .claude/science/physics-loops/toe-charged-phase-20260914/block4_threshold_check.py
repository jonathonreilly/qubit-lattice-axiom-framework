#!/usr/bin/env python3
"""Private finite threshold and exact nonlinear truncated-flow checks."""
import json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad,solve_ivp

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

def main():
 r={'threshold':check_threshold(),'nonlinear_isotropic_truncated_ODE':check_nonlinear(),'scope':'supplied massive Dirac polarization and truncated one-loop massless ODE; neither demonstrates a gap in the normal lattice carrier or a full interacting phase'}
 Path(__file__).with_name('BLOCK4_THRESHOLD_CHECK.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));print('PASS: threshold decoupling and independent nonlinear flow reconstructions')
if __name__=='__main__':main()
