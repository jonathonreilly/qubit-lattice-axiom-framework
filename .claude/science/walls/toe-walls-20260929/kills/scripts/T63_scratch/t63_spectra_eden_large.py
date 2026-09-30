import sys; sys.dont_write_bytecode=True; sys.path.insert(0,".")
import numpy as np, math
from t63_spectra import eden_snapshots, shell_S, fits
L=96; nseeds=8; nmax=5
fills=[0.15,0.30,0.60]
acc={f:[] for f in fills}
for sd in range(nseeds):
    sn=eden_snapshots(L,0.002,np.array(fills),8000+sd)
    for i,f in enumerate(fills): acc[f].append(shell_S(sn[i],nmax))
for f in fills:
    A=np.array(acc[f]); S=A.mean(0); sem=A.std(0,ddof=1)/math.sqrt(nseeds)
    print("L=96 Eden fill %.2f S(n=1..5)=%s sem=%s"%(f,np.round(S,2).tolist(),np.round(sem,2).tolist()))
    for nm in (3,4,5):
        a,ae,cp,ca,c2=fits(L,S[:nm],sem[:nm],nm)
        print("    fit n=1..%d: alpha_eff=%+.2f+-%.2f  chi2pow=%.1f chi2(S0+S2k^2)=%.1f (dof %d) S0=%.2f S2=%.1f"%(nm,a,ae,cp,ca,nm-2,c2[0],c2[1]))
