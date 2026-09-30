"""Kill-check T53: two-angle problem on the chamber boundary q = sqrt(8/3) - d, WIDE domain (attack searched only m in [0.55,0.85], d in [0.88,0.98]).
Lists all roots for (s12^2,s13^2)=(0.307,0.0218) and NuFIT-6.1 rectangle corners; reports s23^2, dCP per root, sigma=(2,1,0), gamma=+1/2."""
import numpy as np, math
from scipy.optimize import fsolve
from chart import obs, SQ
rng=np.random.default_rng(11)
def broots(s12t,s13t,perm=(2,1,0),gamma=0.5,n=4000,R=60):
    def f(x):
        o=obs(x[0],x[1],SQ-x[1],gamma,perm)
        return [o['s12']-s12t,o['s13']-s13t]
    F=[]
    for _ in range(n):
        x0=[rng.uniform(-R,R),rng.uniform(-R,R)] if rng.random()<0.5 else list(rng.normal(0,2,2))
        try: x,info,ier,msg=fsolve(f,x0,xtol=1e-13,full_output=True)
        except Exception: continue
        if ier==1 and max(abs(v) for v in f(x))<1e-9 and not any(np.allclose(x,r,atol=1e-5,rtol=1e-6) for r in F): F.append(x)
    return F
for tg in [(0.307,0.0218),(0.2893,0.0207),(0.3295,0.0242),(0.2893,0.0242),(0.3295,0.0207)]:
    F=broots(*tg)
    print('target (s12^2,s13^2)=',tg,' #boundary roots (m,d) found:',len(F))
    for x in sorted(F,key=lambda r:abs(r[0])+abs(r[1])):
        o=obs(x[0],x[1],SQ-x[1])
        print('    (m,d)=(%.4f,%.4f) q=%.4f s23^2=%.4f dCP=%.2f sind=%+.4f |cosd|=%.3f'%(x[0],x[1],SQ-x[1],o['s23'],o['dcp'],o['sind'],abs(o['cosd'])))
