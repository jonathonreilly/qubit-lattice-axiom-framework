#!/usr/bin/env python3
"""Private direct longitudinal tensor versus exact lattice-Ward reduction."""
import json
from pathlib import Path
import numpy as np
from block4_velocity_check import I,sigma,symbol,vertex,shell_samples

def one(rho,v,c,sign,qd):
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
def main():
 qd=shell_samples();rows=[]
 for v,c,sign in [(.7,1.,1),(1.7,.8,-1)]:
  for rho in [.16,.08,.04,.02,.01]:
   r=one(rho,v,c,sign,qd);rows.append(r);print(json.dumps(r),flush=True)
  g=rows[-5:];assert g[-1]['max_residue_error']<g[0]['max_residue_error']/20
  assert g[-1]['largest_speed_shift']<2e-6
 result={'longitudinal_lattice_Ward_reduction':rows,'scope':'exact longitudinal kernel reduction at a bare cone and the common leading wavefunction shift; finite lattice terms need not be gauge independent as off-shell coefficient ratios'}
 Path(__file__).with_name('BLOCK4_LONGITUDINAL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS: direct longitudinal tensor reduction and gauge-independent speed logarithm')
if __name__=='__main__':main()
