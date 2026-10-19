import numpy as np,json
from functools import lru_cache
from scipy.integrate import quad

def lattice(E,dx,dy,tx=1.,ty=1.):
 E=complex(E);x0=np.arccos((-2*ty-E)/(2*tx))
 def fun(u,inside):
  x=x0*(1-u*u) if inside else x0+(np.pi-x0)*u*u
  jac=2*(x0 if inside else np.pi-x0)*u;z=E+2*tx*np.cos(x)
  den=1j*np.sqrt(4*ty*ty-z*z) if inside else -np.sqrt(z*z-4*ty*ty)
  r=(-z+den)/(2*ty)
  return jac*np.cos(dx*x)*r**abs(dy)/den
 out=0j
 for inside in [True,False]:
  out+=quad(lambda u:fun(u,inside).real,0,1,epsabs=2e-11)[0]+1j*quad(lambda u:fun(u,inside).imag,0,1,epsabs=2e-11)[0]
 return out/np.pi

def host(E,tx=1.,ty=1.):
 holes=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
 A=[(2,0),(-2,0),(0,2),(0,-2)];D=[(1,1),(1,-1),(-1,1),(-1,-1)]
 sites=holes+A+D
 @lru_cache(None)
 def g(dx,dy):return lattice(E,abs(dx),abs(dy),tx,ty)
 M=np.array([[g(x-u,y-v) for u,v in sites] for x,y in sites]);S=M[5:,5:]-M[5:,:5]@np.linalg.solve(M[:5,:5],M[:5,5:])
 va=np.r_[np.ones(4)/2,np.zeros(4)];vd=np.r_[np.zeros(4),np.ones(4)/2]
 return np.array([[va@S@va,va@S@vd],[vd@S@va,vd@S@vd]])
G=host(-2);a=G[0,0]/(1+G[0,0]);rows=[]
for q in [.04,.02,.01]:
 g=host(-2,tx=np.cos(q/2))[0,0];aq=g/(1+g);coef=(aq-a)/q**2;rows.append(dict(q=q,a_quadratic=[coef.real,coef.imag],physical_curvature_over_lambda4=coef.real/8))
print(rows)
open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2)+'\n')
