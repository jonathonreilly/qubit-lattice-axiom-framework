import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_slow_host import host
import numpy as np
from scipy.linalg import solve_banded
from scipy.optimize import root
from scipy.special import ai_zeros
alpha=abs(ai_zeros(1)[0][0])
def run(p,lam,factor=1):
 c=np.cos(p/2);f=lam**2/8;eps=(f/c)**(1/3);N=int(np.ceil(factor*(18+4*np.log(1/lam))/eps));diag=f*(np.arange(N)+3)
 sigma=c*c*host(-2*c)[0,0];a=sigma/(c+sigma);pred=(2+a)/8
 def equation(x):
  E=-2*c+alpha*c**(1/3)*f**(2/3)+lam**2*complex(*x)
  ab=np.zeros((3,N-1),complex);ab[1]=E-diag[1:];ab[0,1:]=c;ab[2,:-1]=c
  v=np.zeros(N-1);v[0]=1
  g=solve_banded((1,1),ab,v,check_finite=False)[0]
  F=E-diag[0]-c*c*(host(E)[0,0]+g)
  return [F.real,F.imag]
 sol=root(equation,[pred.real,pred.imag],tol=1e-10);res=np.linalg.norm(equation(sol.x));assert res<1e-8
 v=complex(*sol.x)
 return dict(p=p,lam=lam,N=N,gamma=c,coefficient=[v.real,v.imag],predicted=[pred.real,pred.imag],error=abs(v-pred),residual=res,width_coefficient=-2*v.imag,predicted_width=-a.imag/4)

def residue(row):
 p=row['p'];lam=row['lam'];c=np.cos(p/2);f=lam**2/8;N=row['N'];E=-2*c+alpha*c**(1/3)*f**(2/3)+lam**2*complex(*row['coefficient'])
 diag=f*(np.arange(N)+3);ab=np.zeros((3,N-1),complex);ab[1]=E-diag[1:];ab[0,1:]=c;ab[2,:-1]=c;v=np.zeros(N-1);v[0]=1;tail=solve_banded((1,1),ab,v,check_finite=False)
 G=host(E);step=1e-5;der=(host(E+step)[0,0]-host(E-step)[0,0])/(2*step)
 P11=1/(1-c*c*der+c*c*(tail@tail))
 amp=np.array([1,2])@G[:,0]/np.sqrt(2)
 R=lam**4*np.cos(p)**2*amp**2*P11/lam**6
 G0=host(-2*c);sigma=c*c*G0[0,0];amp0=np.array([1,2])@G0[:,0]/np.sqrt(2)
 pred=c*np.cos(p)**2*amp0**2/(8*(c+sigma)**2)
 return dict(p=p,lam=lam,coefficient=[R.real,R.imag],predicted=[pred.real,pred.imag],error=abs(R-pred))
