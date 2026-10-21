import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_slow_host import host
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import ai_zeros
alpha=abs(ai_zeros(1)[0][0]);grid=np.linspace(.05,.35,121);values=[]
for p in grid:
 c=np.cos(p/2);G=host(-2*c);sigma=c*c*G[0,0];a=sigma/(c+sigma);u=np.array([1,2])@G[:,0]/np.sqrt(2);R=c*np.cos(p)**2*u*u/(8*(c+sigma)**2);e4=29/192+19*c/16-13*np.cos(p)/64+(2+a)/8
 values.append([R,e4])
interp=CubicSpline(grid,np.array(values),axis=0)
def run(lam,N=65536):
 p=2*np.pi*np.fft.fftfreq(N);sel=(p>.1)&(p<.3);q=p[sel];u=(q-.2)/.1;f=(1-u*u)**4;f/=np.sqrt(np.sum(f*f)/N)
 R,e4=interp(q).T;c=np.cos(q/2);phase=(((-4-2*c)+6)/lam**2+alpha*(c**(1/3)-1)/(4*lam**(2/3))+e4)
 A=np.zeros(N,complex);A[sel]=f*R*np.exp(-1j*phase);psi=np.fft.ifft(A);x=np.arange(N);x[x>N//2]-=N
 # Parseval convention sum|psi|²=mean|A|². A rapid perturbation is a
 # discrete multiplier stress test only; not a native coefficient.
 stress=A.copy();stress[sel]*=np.exp(-1j*lam*np.log(1/lam)*np.sin(q/lam**3));ps=np.fft.ifft(stress)
 diff=np.linalg.norm(ps-psi);bound=lam*np.log(1/lam)*np.linalg.norm(psi);assert diff<=bound*(1+1e-12)
 out=[]
 for k in [0,1,3,8]:
  actual=np.sum(np.exp(1j*k*lam**2*x)*abs(psi)**2)
  limit=np.sum(abs(f*R)**2*np.exp(2*e4.imag)*np.exp(1j*k*np.sin(q/2)))/N
  out.append(dict(k=k,actual=[actual.real,actual.imag],limit=[limit.real,limit.imag],error=abs(actual-limit)))
 return dict(lam=lam,N=N,tests=out,stress_difference=diff,stress_bound=bound,edge_mass=float(np.sum(abs(psi[abs(x)>N/3])**2)))
