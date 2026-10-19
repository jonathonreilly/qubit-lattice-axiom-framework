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

def denominator(E,f,N):
 g=0j
 for n in range(N,1,-1):g=1/(E-f*(n+1)-4*g)
 return E-2*f-4*G(E)-4*g

G0=G(-4);s=4*G0;a=s/(2+s);z1=abs(ai_zeros(1)[0][0]);rows=[]
for lam in [.3,.2,.1,.05,.025]:
 f=lam**3/16;L=(2/f)**(1/3);N=int(14*L)
 pred=-4+2**(1/3)*f**(2/3)*z1+f*(1+a)
 def fun(v):
  d=denominator(complex(*v),f,N);return [d.real,d.imag]
 sol=root(fun,[pred.real,pred.imag],tol=1e-10);E=complex(*sol.x)
 g=0j;gp=0j
 for n in range(N,1,-1):
  gn=1/(E-f*(n+1)-4*g);gp=-gn**2*(1-4*gp);g=gn
 h=1e-5;Gprime=(G(E+h)-G(E-h))/(2*h);der=1-4*Gprime-4*gp
 res=8*lam**2*G(E)**2/der
 rows.append(dict(lam=lam,N=N,converged=bool(sol.success),residual=float(np.linalg.norm(fun(sol.x))),energy=[E.real,E.imag],width_over_lambda4=-2*lam*E.imag/lam**4,residue_over_lambda5=[res.real/lam**5,res.imag/lam**5]))
out=dict(G0=[G0.real,G0.imag],rows=rows,scope='Frequency-dependent analytically continued host-plus-linear-string coefficient model; higher native orders not included')
print(json.dumps(out,indent=2));open('/private/tmp/neutral_bulk_resonance_dynamic.json','w').write(json.dumps(out,indent=2)+'\n')
