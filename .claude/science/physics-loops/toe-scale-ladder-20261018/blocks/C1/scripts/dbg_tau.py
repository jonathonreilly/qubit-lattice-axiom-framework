import sys, numpy as np, time
sys.path.insert(0,'.')
from driver import Sim, config_obs, st_kmin
L=int(sys.argv[1]); T=float(sys.argv[2]); N=int(sys.argv[3]); seed=int(sys.argv[4]); pr=[float(x) for x in sys.argv[5].split(',')] if len(sys.argv)>5 else [0.3,0.6,0.9,0.5]
sim=Sim(L,0.0,T,seed=seed,cap=200); sim.pr=np.array(pr); sim.hist=float(sys.argv[6]) if len(sys.argv)>6 else 0.0
t0=time.time(); out=[]
for i in range(N):
    sim.do_sweep()
    if i==2000: sim.nm_fixed=int((sim.lat.np+sim.nkinks())*(float(sys.argv[7]) if len(sys.argv)>7 else 1.0))
    if i%4==0:
        st=sim.states(np.array([T/2]))
        PE,Pn,Nf,Ek=config_obs(sim.lat,st)
        out.append((st_kmin(PE[0],L,1), Nf[0], sim.nkinks()))
out=np.array(out); np.save(f'../data/dbg_tau_L{L}_T{T}_s{seed}_h{sim.hist}.npy', out)
s=out[:,0]-out[:,0].mean(); print('ST1 autocorr (lags in meas of 4 sweeps 1,5,25,125,500,2000):', np.round([np.mean(s[:-w]*s[w:])/np.var(s) for w in [1,5,25,125,500,2000]],3), 'mean', out[:,0].mean())
n=len(out)//20
print(L,T,seed,'time',round(time.time()-t0),'block means ST1', np.round(out[:n*20,0].reshape(20,n).mean(1),3))
print('   block means Nf/Np', np.round(out[:n*20,1].reshape(20,n).mean(1)/sim.lat.np,4))
