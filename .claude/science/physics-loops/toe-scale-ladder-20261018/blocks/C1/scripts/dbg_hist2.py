import sys, numpy as np
sys.path.insert(0,'.')
from driver import Sim
import qmc
L=int(sys.argv[1])
T=float(sys.argv[2]); sim=Sim(L,0.0,T,seed=11,cap=64)
for i in range(3000): sim.do_sweep()
print('valid before', sim.valid(), sim.nkinks())
lat=sim.lat
bad=0
for trial in range(3000):
    p=np.random.randint(lat.np)
    s0b=sim.s0.copy(); ktb=sim.kt.copy(); kcb=sim.kc.copy()
    ok=qmc.hist_update_V0(sim.s0,sim.kt,sim.kc,*sim.args,1.0,T,p,sim.h_et,sim.h_eq,sim.h_f,sim.h_al,sim.h_tmp)
    if not sim.valid():
        bad+=1
        # find offending kink
        for q in range(lat.np):
            for i in range(sim.kc[q]):
                c=qmc.circ_at(sim.s0,sim.kt,sim.kc,lat.lplaqs,lat.plinks,lat.psign,q,sim.kt[q,i])
                if abs(c)!=4: print('p',p,'bad kink on q',q,'t',sim.kt[q,i],'q==p',q==p,'q in nbh',q in lat.nbh[p,:lat.nnb[p]], 'shared links', len(set(lat.plinks[p])&set(lat.plinks[q])))
        sim.s0[:]=s0b; sim.kt[:]=ktb; sim.kc[:]=kcb
        if bad>3: break
print('bad',bad)
for trial in range(3000):
    p=np.random.randint(lat.np)
    ok=qmc.hist_update_V0(sim.s0,sim.kt,sim.kc,*sim.args,1.0,T,p,sim.h_et,sim.h_eq,sim.h_f,sim.h_al,sim.h_tmp)
    okp=qmc.path_valid(sim.s0,sim.kt,sim.kc,lat.lplaqs,lat.plinks,lat.psign,T); g=np.all(lat.div(sim.s0)==0)
    if not (okp and g):
        print('ok',ok,'path',okp,'gauss',g,'kc[p]',sim.kc[p], sim.kt[p,:sim.kc[p]]); break
