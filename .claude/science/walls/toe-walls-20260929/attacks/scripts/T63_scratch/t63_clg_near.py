import sys; sys.dont_write_bytecode=True; sys.path.insert(0,".")
import numpy as np, math, time
from t63_clg import evolve, init
from t63_spectra import shell_S, fits
L=int(sys.argv[1]); nseeds=int(sys.argv[2]); T=int(sys.argv[3]); nmax=4
for rho in [float(x) for x in sys.argv[4:]]:
    t0=time.time(); acc=[]; times=[]
    for sd in range(nseeds):
        rng=np.random.default_rng(sd+int(rho*10000)); occ=init(L,rho,rng); t=evolve(occ,L,T,7000+sd); times.append(t)
        if t>=0: acc.append(shell_S(occ,nmax))
    if len(acc)>=3:
        A=np.array(acc); S=A.mean(0); sem=A.std(0,ddof=1)/math.sqrt(len(A))
        a,ae,cp,ca,c2=fits(L,S,np.maximum(sem,1e-9),nmax)
        print("L=%d rho=%.3f absorbed %d/%d mean t_abs=%.0f S=%s alpha_eff=%+.2f+-%.2f chi2pow=%.1f chi2an=%.1f [%.0fs]"%(L,rho,len(acc),nseeds,np.mean([t for t in times if t>=0]),np.round(S,4).tolist(),a,ae,cp,ca,time.time()-t0),flush=True)
    else:
        print("L=%d rho=%.3f absorbed %d/%d within %d sweeps [%.0fs]"%(L,rho,len(acc),nseeds,T,time.time()-t0),flush=True)
