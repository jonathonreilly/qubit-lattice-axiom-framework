"""T19 - the same P(s) test at large L, where BOTH windows are open at once:
lattice artifact ~ 1/s (needs large s) and derivative expansion ~ s k^2 (needs
small s k^2).  At L=64, nk=1: k^2 = 0.00964, so s can run to 40 with s k^2 < 0.39.
Saves the spectra so the analysis can be redone without recomputing."""
import numpy as np, sys, time; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]); AMP=float(sys.argv[2]); NKW=int(sys.argv[3])
POLS={'gauge':[1,0,0,0],'TT':[0,1,-1,0],'conf':[1,1,1,1],'tran':[0,1,0,0]}
out={}
for tag,al in [('flat',[0,0,0,0])]+list(POLS.items()):
    t0=time.time()
    S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,al); g=geometry(S,L)
    _,lam=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
    out[tag+'_lam']=np.sort(lam).astype(np.float64)
    out[tag+'_VR']=np.array([g['Vol'],g['Reg']])
    print(f"  {tag}: {time.time()-t0:.0f}s  Vol={g['Vol']:.6f} S_Regge={g['Reg']:.6e}",flush=True)
np.savez_compressed(f"spec_L{L}_a{AMP}_nk{NKW}.npz",**out)
print("saved")
