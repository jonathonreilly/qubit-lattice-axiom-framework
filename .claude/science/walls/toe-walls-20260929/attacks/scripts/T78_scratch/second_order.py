"""Second-order coefficient of the RK-perturbation: E2 = -eps^2 * Int_0^inf C_c(t) dt, C_c = connected autocovariance
of N_f in the RK Markov dynamics (rate K=1 per flippable plaquette; one sweep = 3L^3 attempts = unit time).
Reports per-site Var(N_f)/Vol, tau_int, and R2/Vol = Var/Vol * tau_int  and the tail exponent estimate."""
import numpy as np, sys, json, time
from ice_flux_mc import run_replicas
res={}
for L,nsamp,burn in ((4,60000,500),(6,40000,500),(8,30000,500),(12,12000,800),(16,6000,1200)):
    nrep=10
    t=time.time()
    out,_=run_replicas(L,np.zeros(nrep,dtype=np.int64),nrep,burn,nsamp,1,777)
    x=out-out.mean(axis=1,keepdims=True)
    n=nsamp; f=np.fft.rfft(x,n=2*n,axis=1)
    ac=np.fft.irfft(f*np.conj(f),axis=1)[:,:n]
    ac=ac/np.arange(n,0,-1)[None,:]           # unbiased autocovariance per lag
    C=ac.mean(axis=0)
    var=C[0]; vol=L**3
    lagmax=min(80,n//10)
    rho=C[:lagmax+1]/var
    tau=0.5+rho[1:].sum()
    # per-replica tau for error
    taus=[0.5+ (ac[r,1:lagmax+1]/ac[r,0]).sum() for r in range(nrep)]
    # tail: fit rho(t) ~ A t^-alpha for t in 8..40 using replica-mean, noisy: report the values
    res[L]={"var_per_vol":float(var/vol),"tau_int":float(tau),"tau_err":float(np.std(taus,ddof=1)/np.sqrt(nrep)),
            "R2_per_vol":float(var/vol*tau),"rho":[float(v) for v in rho[[1,2,4,8,16,32] if lagmax>=32 else [1,2,4,8]]],"secs":time.time()-t}
    print(L,res[L],flush=True)
json.dump(res,open("second_order.json","w"),indent=1)
