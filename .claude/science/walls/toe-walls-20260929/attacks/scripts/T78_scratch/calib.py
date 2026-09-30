import numpy as np, time, sys
from ice_flux_mc import run_replicas
L=int(sys.argv[1]); q=int(sys.argv[2])
nrep=10
t=time.time()
out,diag=run_replicas(L,np.full(nrep,q,dtype=np.int64),nrep,200,4000,1,999)
print("time",time.time()-t)
x=out[:, :]
m=x.mean()
print("mean N_f",m,"per plaq",m/(3*L**3))
# integrated autocorr time (in sweeps, gap=1)
xc=x-x.mean(axis=1,keepdims=True)
var=(xc**2).mean()
tau=0.5
for lag in range(1,200):
    ac=(xc[:,:-lag]*xc[:,lag:]).mean()/var
    if ac<0.02: break
    tau+=ac
print("tau_int (sweeps) ~",tau,"lags",lag, "std single",np.sqrt(var))
# block a: first 500 vs last 500 mean drift after burn
print("first/last 500 means",x[:, :500].mean(),x[:, -500:].mean())
