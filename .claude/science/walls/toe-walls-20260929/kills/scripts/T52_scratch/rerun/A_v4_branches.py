"""Test A: the three involutions of the native Klein group V4 = <S, P23> on the hw=1 triplet.
Random Hermitian M in the commutant of each involution R (unitary symmetry), optionally with the mu-tau reflection
P23 M* P23 = M. Columns are ordered by decreasing electron content (shared sigma_hier premise)."""
import numpy as np, math, sys
from common import *
rng = np.random.default_rng(20260929)

def rand_commutant(R):
    """general Hermitian M with [M,R]=0: project a random Hermitian onto the commutant."""
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); A = (A + A.conj().T) / 2
    P_plus = (I3 + R) / 2; P_minus = (I3 - R) / 2
    return P_plus @ A @ P_plus + P_minus @ A @ P_minus

def reflect(M):   # impose P23 M* P23 = M
    return (M + P23 @ M.conj() @ P23) / 2

def run(name, R, refl, N=20000, tag=""):
    out = []
    for _ in range(N):
        M = rand_commutant(R)
        if refl:
            M = reflect(M)
            # reflect() preserves the commutant because P23 commutes with R (checked below)
        w, V = np.linalg.eigh(M)
        if np.min(np.diff(w)) < 1e-6:      # skip near-degenerate samples (mixing undefined)
            continue
        w, V = order_by_electron_content(w, V)
        out.append(observables(V) )
    return np.array(out)

assert np.allclose(P23 @ S, S @ P23)
def report(name, arr, box=BOX61):
    s12, s13, s23, sd, cd = arr.T
    inb = np.array([inbox((a, b, c), box) for a, b, c in zip(s12, s13, s23)])
    print(f"{name:44s} n={len(arr):6d}  s13^2 range [{s13.min():.4f},{s13.max():.4f}]  s12^2 range [{s12.min():.4f},{s12.max():.4f}]"
          f"  s23^2 range [{s23.min():.4f},{s23.max():.4f}]  in NuFIT-6.1 3sigma box: {inb.sum()}")
    return inb

print("Involution commutants (unitary) and mu-tau-reflected versions, electron = corner 1\n")
res = {}
for nm, R in (("S (TM2: fixes W)", S), ("S.P23 (TM1: fixes xi)", SP), ("P23 (fixes eta)", P23)):
    for refl in (False, True):
        arr = run(nm, R, refl)
        res[(nm, refl)] = arr
        inb = report(f"{nm} {'+ mu-tau reflection' if refl else ''}", arr)

# focused checks with the s13^2 window of the data
print("\n--- exact structure checks in the data window s13^2 in [0.0207, 0.0242] ---")
for nm, R in (("S (TM2)", S), ("S.P23 (TM1)", SP)):
    arr = res[(nm if nm.startswith("S (") else "S.P23 (TM1: fixes xi)", True)] if False else None
arrT2 = res[("S (TM2: fixes W)", True)]
arrT1 = res[("S.P23 (TM1: fixes xi)", True)]
for nm, arr in (("TM2 + reflection", arrT2), ("TM1 + reflection", arrT1)):
    m = (arr[:, 1] > 0.0207) & (arr[:, 1] < 0.0242)
    a = arr[m]
    if len(a) == 0:
        print(nm, "no samples in window"); continue
    s12, s13, s23, sd, cd = a.T
    print(f"{nm}: n={len(a)}  s12^2 in [{s12.min():.5f},{s12.max():.5f}]  s23^2 in [{s23.min():.10f},{s23.max():.10f}]  |sin d| in [{abs(sd).min():.10f},{abs(sd).max():.10f}]  |cos d| max {abs(cd).max():.2e}")
    pred = (1 - 3 * s13) / (3 * (1 - s13)) if "TM1" in nm else 1 / (3 * (1 - s13))
    print(f"    algebra formula {'(1-3s13)/(3c13)' if 'TM1' in nm else '1/(3c13)'} vs operator: max |diff| = {np.max(np.abs(pred - s12)):.2e}")

# TM1 without reflection: free phase psi -> correlation s23^2 vs delta
print("\n--- TM1 (S.P23 commutant) WITHOUT the mu-tau reflection: s23^2, delta correlation at s13^2 = 0.02245 ---")
arr = res[("S.P23 (TM1: fixes xi)", False)]
m = np.abs(arr[:, 1] - 0.02245) < 0.0004
a = arr[m]
s12, s13, s23, sd, cd = a.T
delta = np.degrees(np.arctan2(sd, cd)) % 360
print(f"n={len(a)}, s12^2 range [{s12.min():.4f},{s12.max():.4f}] s23^2 range [{s23.min():.3f},{s23.max():.3f}]")
for lo, hi in ((0.44, 0.50), (0.46, 0.48), (0.50, 0.56), (0.53, 0.56)):
    mm = (s23 > lo) & (s23 < hi)
    if mm.sum():
        print(f"  s23^2 in [{lo},{hi}]: n={mm.sum()}  delta range [{delta[mm].min():.0f},{delta[mm].max():.0f}] deg  (sin d range [{sd[mm].min():.3f},{sd[mm].max():.3f}])")
# sign/branches: report delta at s23^2=0.470
mm = np.abs(s23 - 0.470) < 0.004
print("  at s23^2 = 0.470 +- 0.004: deltas (deg, mod 360) =", np.unique(np.round(delta[mm] / 10) * 10))
np.save("A_tm1_norefl.npy", arr)
