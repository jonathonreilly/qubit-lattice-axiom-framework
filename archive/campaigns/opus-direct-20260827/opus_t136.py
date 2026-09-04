"""T136 - WHAT IS ACTUALLY PAIRING?  (and have T134/T135 been testing the wrong thing?)

T135 refuted my own explanation.  I attributed the taste degeneracy's survival of
curvature to Lambda* = S (x) S-bar, which needs a SPIN structure -- and then the
degeneracy survived on RP^2, which is non-orientable and hence non-spin.  The
fact stands; my mechanism for it does not.

Before drawing anything from d=2, check the obvious alternative: that the 2-fold
pairing I have been measuring is nothing but HODGE DUALITY, * : Lambda^k -> Lambda^{d-k},
which commutes with the Laplacian on any Riemannian manifold and in d=2 pairs
Lambda^0 with Lambda^2.  If so, then:
   * the d=2 "taste degeneracy" is Poincare duality and nothing else, and
   * it says NOTHING about d=4, where duality gives only a factor 2 while the
     taste count is 4 -- so the other factor of 2 has a different origin and may
     well be breakable.
That would mean T134 and T135 have been testing the wrong object, and the
generations route is NOT closed by them.

Decisive and cheap: compare spec(Delta_0) with spec(Delta_2) directly.  Equal
=> the pairing is duality.  Then look at whether Delta_1's own modes are paired,
which is the part duality does not explain."""
import numpy as np, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t121 import icosphere
from opus_t134 import spectra, bumpy

P,Fc=icosphere(3)
print("T136  what is pairing?  Delta_0 vs Delta_2, and inside Delta_1")
for nm,Q in (("round sphere",P),("bumpy sphere amp=0.30",bumpy(P,0.30))):
    l0,l1,l2,area=spectra(Q,Fc)
    l0=np.sort(l0); l1=np.sort(l1); l2=np.sort(l2)
    n=min(len(l0),len(l2))
    nz0=l0[l0>1e-8]; nz2=l2[l2>1e-8]; nz1=l1[l1>1e-8]
    m=min(len(nz0),len(nz2))
    print(f"\n   {nm}:  dim Lambda^0={len(l0)}, Lambda^1={len(l1)}, Lambda^2={len(l2)}")
    print(f"      spec(Delta_0) lowest 6 nonzero: " + " ".join(f"{v:.6f}" for v in nz0[:6]))
    print(f"      spec(Delta_2) lowest 6 nonzero: " + " ".join(f"{v:.6f}" for v in nz2[:6]))
    d02=np.abs(nz0[:m]-nz2[:m])/nz0[:m]
    print(f"      -> |spec(D0)-spec(D2)|/spec: max {d02.max():.3e}  "
          f"{'IDENTICAL: the pairing is HODGE DUALITY' if d02.max()<1e-9 else 'DIFFERENT'}")
    print(f"      spec(Delta_1) lowest 8 nonzero: " + " ".join(f"{v:.6f}" for v in nz1[:8]))
    d1=np.abs(nz1[1:16:2]-nz1[0:16:2])/nz1[0:16:2]
    print(f"      -> Delta_1 internal pairing: max {d1.max():.3e}  "
          f"{'PAIRED' if d1.max()<1e-9 else 'NOT paired'}")
    # is spec(D1) = spec(D0) u spec(D2) (Hodge decomposition into exact + coexact)?
    union=np.sort(np.concatenate([nz0,nz2]))
    k=min(len(union),len(nz1))
    du=np.abs(nz1[:k]-union[:k])/union[:k]
    print(f"      -> spec(D1) vs spec(D0) u spec(D2): max {du.max():.3e}  "
          f"{'EQUAL' if du.max()<1e-9 else 'DIFFERENT -- D1 is independent'}")
print()
print("   If spec(D0) = spec(D2) exactly but spec(D1) is independent, then in d=2")
print("   the degeneracy is duality plus the exact/coexact pairing inside D1 --")
print("   BOTH of which are Hodge theory on any manifold, and NEITHER of which")
print("   is the d=4 taste structure.  d=2 would then be the wrong test entirely.")
