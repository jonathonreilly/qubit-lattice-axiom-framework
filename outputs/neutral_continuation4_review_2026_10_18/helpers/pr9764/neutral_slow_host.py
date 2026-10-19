import numpy as np,json
from functools import lru_cache
from scipy.integrate import quad

def lattice(E,dx,dy):
 E=complex(E);x0=np.arccos((-2-E)/2)
 def fun(u,inside):
  x=x0*(1-u*u) if inside else x0+(np.pi-x0)*u*u
  jac=2*(x0 if inside else np.pi-x0)*u;z=E+2*np.cos(x)
  den=1j*np.sqrt(4-z*z) if inside else -np.sqrt(z*z-4)
  r=(-z+den)/2
  return jac*np.cos(dx*x)*r**abs(dy)/den
 out=0j
 for inside in [True,False]:
  out+=quad(lambda u:fun(u,inside).real,0,1,epsabs=2e-11)[0]+1j*quad(lambda u:fun(u,inside).imag,0,1,epsabs=2e-11)[0]
 return out/np.pi

def host(E):
 holes=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
 A=[(2,0),(-2,0),(0,2),(0,-2)];D=[(1,1),(1,-1),(-1,1),(-1,-1)]
 sites=holes+A+D
 @lru_cache(None)
 def g(dx,dy):return lattice(E,abs(dx),abs(dy))
 M=np.array([[g(x-u,y-v) for u,v in sites] for x,y in sites]);S=M[5:,5:]-M[5:,:5]@np.linalg.solve(M[:5,:5],M[:5,5:])
 va=np.r_[np.ones(4)/2,np.zeros(4)];vd=np.r_[np.zeros(4),np.ones(4)/2]
 return np.array([[va@S@va,va@S@vd],[vd@S@va,vd@S@vd]])
if __name__=='__main__':
 G=host(-2);a=G[0,0]/(1+G[0,0]);source=np.array([1,2])/np.sqrt(2)
 # arm hopping-1, sigma=GAA, boundary a=Sigma/(1+Sigma), f=lambda²/8.
 print(G,a,'width coefficient',-a.imag/4)
 out=dict(host=[[ [v.real,v.imag] for v in row] for row in G],a=[a.real,a.imag],width_coefficient=-a.imag/4,scope='Partial K2 slow-host model; further fast-channel/source and native control pending')
 open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
