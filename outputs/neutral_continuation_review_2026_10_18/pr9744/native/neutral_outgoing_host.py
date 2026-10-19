import numpy as np,json
from scipy.integrate import quad
from scipy.special import ai_zeros
from scipy.optimize import root

def integrate(fun):return quad(lambda u:fun(u).real,0,1,epsabs=2e-11,limit=100)[0]+1j*quad(lambda u:fun(u).imag,0,1,epsabs=2e-11,limit=100)[0]
def G(E):
 E=complex(E);x0=np.arccos((-4-E)/4)
 def a(u):
  x=x0*(1-u*u);c=np.cos(x);z=E+4*c
  return -1j*2*x0*u*(2*c+E/4)**2/np.sqrt(16-z*z)
 def b(u):
  x=x0+(np.pi-x0)*u*u;c=np.cos(x);z=E+4*c
  return -2*(np.pi-x0)*u*(2*c+E/4)**2/np.sqrt(z*z-16)
 return (integrate(a)+integrate(b))/np.pi-E/16
