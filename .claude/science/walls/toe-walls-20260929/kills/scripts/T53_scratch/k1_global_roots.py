"""Kill-check T53: global (wide-domain) chamber-interior roots of the three-angle map, both sigma, gamma=+1/2.
Checks whether the attack's 'excluded band' / 'octant fixed by sigma' is a chart-wide fact or Basin-1-only."""
import numpy as np, math, itertools
from scipy.optimize import fsolve
from chart import obs, SQ
rng = np.random.default_rng(3)
def roots(target, perm, gamma=0.5, nstart=1500, box=((-40,40),(-40,40),(-40,40))):
    def f(x):
        o = obs(x[0],x[1],x[2],gamma,perm)
        return [o['s12']-target[0], o['s13']-target[1], o['s23']-target[2]]
    found=[]
    for _ in range(nstart):
        x0=[rng.uniform(*b) for b in box]
        # also bias towards moderate scale
        if rng.random()<0.5: x0=list(rng.normal(0,2.0,3))
        try:
            x,info,ier,msg=fsolve(f,x0,xtol=1e-13,full_output=True)
        except Exception: continue
        if ier==1 and max(abs(v) for v in f(x))<1e-9:
            if not any(np.allclose(x,r,atol=1e-5,rtol=1e-6) for r in found): found.append(x)
    return found
tg=(0.307,0.0218)
for perm in [(2,1,0),(2,0,1)]:
    for s23 in [0.545,0.455,0.500,0.470]:
        R=roots((tg[0],tg[1],s23),perm)
        print('perm',perm,'target s23^2',s23,'#roots',len(R))
        for x in sorted(R,key=lambda r:-(r[1]+r[2])):
            o=obs(*x,0.5,perm); marg=x[2]+x[1]-SQ
            if abs(x[0])<60:
                print('   (m,d,q)=(%.4f,%.4f,%.4f) margin=%+.4f dCP=%.2f sind=%+.4f s23=%.4f'%(x[0],x[1],x[2],marg,o['dcp'],o['sind'],o['s23']))
