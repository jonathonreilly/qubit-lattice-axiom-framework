import numpy as np
from t1lib import tick
p=0.05; L=128; ts=[20,50,100]
for moves,g in [(False,0.0),(True,2.0)]:
    num={t:0.0 for t in ts}; den={t:0.0 for t in ts}; var={t:0.0 for t in ts}
    for seed in range(40):
        rng=np.random.default_rng(1000+seed); occ=rng.random((L,L))<0.2; H0=(~occ).sum()
        expg=np.exp(g*np.arange(5))
        for t in range(1,101):
            occ,out,form=tick(occ,g,"spont",rng,dict(p=p),moves=moves,expg=expg)
            if t in ts:
                q=(1-p)**t; num[t]+=(~occ).sum(); den[t]+=H0*q; var[t]+=H0*q*(1-q)
    print(f"moves={moves} g={g}: "+"; ".join(f"t={t}: sum H(t)/sum E = {num[t]/den[t]:.4f} +- {np.sqrt(var[t])/den[t]:.4f}" for t in ts))
