import sys, numpy as np
sys.path.insert(0,'.')
from driver import Sim
import qmc
for L,V,T in [(2,0.5,3.0),(4,0.5,6.0),(6,0.9,8.0)]:
    s=Sim(L,V,T,seed=4,cap=200)
    for i in range(200): s.do_sweep()
    rng=np.random.default_rng(1); maxd=0; nt=0
    for trial in range(3000):
        p=rng.integers(s.lat.np); t=rng.random()*T
        ta=max(qmc.prev_evt(s.kt,s.kc,s.lat.nbh,s.lat.nnb,p,t,0,T),0.0); tb=min(qmc.next_evt(s.kt,s.kc,s.lat.nbh,s.lat.nnb,p,t,0,T),T)
        a,b=sorted(ta+(tb-ta)*rng.random(2))
        d1=qmc.delta_toggle(s.s0,s.kt,s.kc,*s.args,p,a,b,s.buf); d2=qmc.delta_toggle_fast(s.s0,s.kt,s.kc,*s.args,p,a,b,s.buf)
        maxd=max(maxd,abs(d1-d2)); nt+=(abs(d1)>1e-12)
    print(L,V,T,'kinks',s.nkinks(),'max |delta_fast - delta_ref| over',nt,'nonzero-delta intervals:',maxd)
