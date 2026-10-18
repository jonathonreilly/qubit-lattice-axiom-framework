import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from scipy.special import ai_zeros
from neutral_slow_host import host
from neutral_corrected_fast_boundary import resolvent
V=np.array([[0.,0.],[-1.,0.],[-1.,-2.],[0.,0.]])
def calc(lam,x,beta):
 f=lam**2/8;N=int(24*f**(-1/3));a=host(-2)[0,0];a=a/(1+a)
 center=-2+f**(2/3)*abs(ai_zeros(1)[0][0])+f*(2+a.real)
 e=center+lam**2*(x+1j*beta);z=lam*(e-4)
 h=host(e);g=0j
 for n in range(N,0,-1):g=1/(e-f*(n+2)-g)
 hs=h+np.outer(h[:,0],h[0,:])*g/(1-g*h[0,0])
 R,_,_=resolvent(z,lam);M=V.T@R@V;b=V.T@R[:,0]
 def resp(hh):return 2*lam*R[0,0]+2*lam**2*b@np.linalg.solve(np.eye(2)-lam*hh@M,hh@b)
 full=resp(hs);base=resp(h)
 return dict(x=x,full=-full.imag/np.pi,base=-base.imag/np.pi,contrast=-(full-base).imag/np.pi,scaled_contrast=-(full-base).imag/(np.pi*lam**2))
