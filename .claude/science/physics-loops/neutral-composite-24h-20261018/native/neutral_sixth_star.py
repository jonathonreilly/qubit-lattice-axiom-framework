import numpy as np,json
from scipy.optimize import brentq
r=8/7
b=brentq(lambda b:147*b**4+112*b**3+34*b*b+112*b-49,0,1,xtol=1e-15)
a=np.sqrt(b*b+r*b);e=2*(a+b);u2=1/(1+2*a*a/(1-a*a)+2*b*b/(1-b*b));w=4*b*b*u2
# dimensionless t0=2gamma=1; armhoppings/centerlinks differ away from zero.
def pole(qx,qy):
 tx=np.cos(qx/2);ty=np.cos(qy/2);lx=np.cos(qx);ly=np.cos(qy)
 # highx/highy, lowx/l owy. centerlowx linkty, centerlowy linktx.
 pars=[(0,tx,tx),(0,ty,ty),(-r,lx,ty),(-r,ly,tx)]
 edge=max(v+2*abs(h) for v,h,c in pars)
 def green(E,v,h):
  if abs(h)<1e-10:return 1/(E-v)
  return 2/(E-v+np.sqrt((E-v)**2-4*h*h))
 def f(E):return E-sum(c*c*green(E,v,h) for v,h,c in pars)
 if f(edge+1e-10)>=0:return None
 return brentq(f,edge+1e-10,10)
rows=[]
for q in [.001,.002,.005,.01,.1,.5,1.,1.5,2.]:
 en=pole(q,0);rows.append(dict(q=q,e=en,curvature=None if en is None else (en-e)/q**2))
print(json.dumps(dict(a=a,b=b,E_over_t=e,gap_above_continuum=e-2,center_weight=u2,source_weight=w,source_fraction=w/2,rows=rows),indent=2))
