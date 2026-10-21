"""Explicit projected coefficient model, not the full native Hamiltonian."""
import json
import numpy as np
from numba import njit
from scipy.optimize import root
from scipy.special import ai_zeros
from neutral_slow_host import host
from neutral_outgoing_host import G

@njit
def fast_arm(z,f,N):
 g=0j
 for n in range(N,0,-1):g=1/(z-f*(n+1)-4*g)
 return g

def run(lam):
 fs=lam**2/8;ff=lam**3/16;N=int(16*fs**(-1/3));Nf=int(10/ff)
 a=host(-2)[0,0];a=a/(1+a)
 pred=-2+fs**(2/3)*abs(ai_zeros(1)[0][0])+fs*(2+a)
 def inverse_arm(e):
  g=0j
  for n in range(N,1,-1):g=1/(e-fs*(n+2)-g)
  return e-3*fs-g
 def boundary(e,coupled):
  h=host(e)
  if not coupled:return h[0,0]
  z=lam*(e-4);g=fast_arm(z,ff,Nf);H=G(z);R=H/(1-4*g*H)
  M=np.array([[(z*z*R-z)/4,2*z*g*R],[2*z*g*R,4*g/(1-4*g*H)]])
  return np.linalg.solve(np.eye(2)-h@(lam*M),h)[0,0]
 def solve(initial,coupled):
  def d(e):return inverse_arm(e)-boundary(e,coupled)
  sol=root(lambda v:[d(complex(*v)).real,d(complex(*v)).imag],[initial.real,initial.imag],tol=1e-10)
  e=complex(*sol.x)
  return e,abs(d(e)),bool(sol.success)
 ep,rp,sp=solve(pred,False);ec,rc,sc=solve(ep,True)
 return dict(lam=lam,partial=[ep.real,ep.imag],coupled=[ec.real,ec.imag],residual=max(rp,rc),success=sp and sc,physical_shift_over_lambda5_log=abs(ec-ep)*np.log(1/lam)/lam**3,partial_width_over_lambda4=-2*ep.imag/lam**2,coupled_width_over_lambda4=-2*ec.imag/lam**2)

if __name__=='__main__':
 out=dict(rows=[run(lam) for lam in [.2,.1,.05,.025,.02]],scope='Explicit projected fast/slow coefficient model; native higher coefficients absent')
 print(json.dumps(out,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
