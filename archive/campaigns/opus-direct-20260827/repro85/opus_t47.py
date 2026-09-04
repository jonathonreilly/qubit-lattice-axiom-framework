"""T47 - (V2) THE HEAT-KERNEL CURVATURE TERM: read the curvature integral out of
the spectrum, by a route completely independent of the l(l+1) test.
For a closed surface,
      Tr exp(-t Lap_0)  =  Area/(4 pi t)  +  (1/4pi) int (R/6) dA  +  O(t)
and with R = 2K plus Gauss-Bonnet int K dA = 2 pi chi, the constant term is
      chi / 6      ->  1/3 = 0.33333 for the sphere,  0 for the torus.
Only the 0-form Laplacian is needed, so this is cheap; the full Dirac operator
was overkill and was making the run enormous.
Only modes below the mesh cutoff are trustworthy, so the signature to look for is
a PLATEAU in t, not the t -> 0 limit (small t weights exactly the modes the mesh
gets wrong)."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def lap0(V,F,tn=None):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,tn)
    if np.any(s1<=1e-12): raise ValueError("degenerate")
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    return np.clip(np.linalg.eigvalsh(A0.T@A0),0,None), float(np.sum(s0)), nv-ne+nf
print("T47  heat-kernel constant term = chi/6")
print()
cases=[]
for k in (3,4):
    V,F=icosphere(k); e,a,chi=lap0(V,F); cases.append((f"sphere sub={k}",e,a,chi,2))
for n in (12,16):
    V,F,tn=flat_torus(n); e,a,chi=lap0(V,F,tn); cases.append((f"torus n={n}",e,a,chi,0))
for nm,e,a,chi,cx in cases:
    print(f"  {nm}: modes={len(e)}  discrete area={a:.5f}  V-E+F={chi}  chi/6 = {cx/6:.5f}")
print()
print(f"   {'t':>7}" + "".join(f"{nm:>18}" for nm,_,_,_,_ in cases))
for t in (0.005,0.01,0.02,0.04,0.08,0.15,0.3,0.6,1.2):
    row=f"   {t:7.3f}"
    for nm,e,a,chi,cx in cases:
        row+=f"{float(np.sum(np.exp(-t*e)))-a/(4*np.pi*t):18.5f}"
    print(row, flush=True)
print()
print("   want: sphere -> 0.33333 (chi/6 with chi=2),  torus -> 0.00000")
print("   the sphere columns should sit on 1/3 over a window of t and drift only")
print("   where the mesh cutoff bites (small t) or the O(t) term bites (large t).")
