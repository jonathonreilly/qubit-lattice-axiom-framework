"""T129b - the -1/3 question, lean.  Is it the tensor structure or one direction?"""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t114b import build, S_of
L=4
verts,vid,tops,edges,emid,edir,base_len=build(L)
S0=S_of(tops,edges,base_len)
print(f"T129b  Euclidean L={L}, S(flat)={S0:.2e}   continuum ratio derived independently: -1/3",flush=True)
pols={}
e=np.zeros((4,4)); e[2,3]=e[3,2]=1.0;                     pols["e23   off-diag"]=e
e=np.zeros((4,4)); e[2,2]=1.0; e[3,3]=-1.0;               pols["e22-e33  diag"]=e
e=np.zeros((4,4)); e[2,2]=1.0; e[3,3]=1.0; e[0,0]=-2.0;   pols["diag(-2,0,1,1)"]=e
e=np.zeros((4,4)); e[0,0]=1.0; e[2,2]=-1.0;               pols["e00-e22   diag"]=e
e=np.zeros((4,4)); e[0,3]=e[3,0]=1.0;                     pols["e03   off-diag"]=e
CONF=np.eye(4)
def d2(ep,kv):
    def ell_of(s):
        ell=base_len.copy()
        for key,ei in edges.items():
            u=edir[key]
            l2=float(u@u)+s*np.cos(float(kv@emid[key]))*float(u@ep@u)
            ell[ei]=np.sqrt(max(l2,1e-14))
        return ell
    h=1e-3
    return (S_of(tops,edges,ell_of(h))-2*S0+S_of(tops,edges,ell_of(-h)))/h**2
for n in (1,2):
    kv=2*np.pi*n*np.array([0.0,1.0,0.0,0.0]); k2=float(kv@kv)
    dc=d2(CONF,kv)
    print(f"\n   k along x1, n={n}, k^2={k2:.3f}   conformal d2S={dc:.6f}  d2S/k^2={dc/k2:.6f}",flush=True)
    print(f"      {'polarisation':>16} {'d2S':>14} {'d2S/k^2':>12} {'ratio to conformal':>20} {'vs -1/3':>12}",flush=True)
    for nm,ep in pols.items():
        v=d2(ep,kv); r=v/dc
        print(f"      {nm:>16} {v:14.6f} {v/k2:12.6f} {r:20.9f} {r+1/3:12.2e}",flush=True)
print("\n   All TRANSVERSE diagonal polarisations at -1/3 = the continuum trace/traceless")
print("   structure survives on the lattice.  Only e22-e33 = it is one direction's accident.")
