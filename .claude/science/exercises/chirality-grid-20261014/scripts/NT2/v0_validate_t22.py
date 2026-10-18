"""V0: validate the T22 closed form against (i) the independent arc/tau builder and (ii) brute-force Monte Carlo
over the site gauge angles, on random pairs (admissible and also generic)."""
import numpy as np, time, resource
from t22lib import *
delta = 0.6; rng = np.random.default_rng(7)
# admissible-with-margin configurations, random holonomies, random gauge
P = sample_plaq(40, delta - 0.05, rng)
L = build_links(P[:, 0], P[:, 1], P[:, 2], rng.uniform(-np.pi, np.pi, 40), rng.uniform(-np.pi, np.pi, 40), rng=rng)
I = invariants(L)
print("max |p11 + p00+p10+p01| (should be 0 mod 2pi):", np.abs(wrap(I['p00'] + I['p10'] + I['p01'] + I['p11'])).max())
print("max |plaquette|:", max(np.abs(I[k]).max() for k in ('p00', 'p10', 'p01', 'p11')))
# pairs with small holonomy differences so that K != 0 often
L2 = L.copy()
Kc = kernel_matrix_closed(L, delta); Ki = kernel_matrix_indep(L, delta)
print("closed vs indep: max |diff| =", np.abs(Kc - Ki).max(), " max K =", Kc.max(), " nonzero frac", (Kc > 0).mean())
# make a pool with near-equal holonomies to have dense nonzero entries
Lb = build_links(P[:, 0], P[:, 1], P[:, 2], rng.uniform(-0.4, 0.4, 40), rng.uniform(-0.4, 0.4, 40), rng=rng)
Kc = kernel_matrix_closed(Lb, delta); Ki = kernel_matrix_indep(Lb, delta)
print("near-matched pool: closed vs indep max |diff| =", np.abs(Kc - Ki).max(), " max K =", Kc.max(), " nonzero frac", (Kc > 0).mean())
# Monte Carlo for a few pairs (whole reduction incl. gauge structure)
t = time.time()
for (i, j) in [(0, 1), (2, 3), (4, 5), (0, 0), (6, 9), (10, 11), (12, 20)]:
    p, s = kernel_mc(Lb[i], Lb[j], delta, 4_000_000, rng)
    print(f"pair {i},{j}: closed {Kc[i,j]:.6e}  indep {Ki[i,j]:.6e}  MC {p:.6e} +- {s:.1e}  (z = {(p-Kc[i,j])/max(s,1e-30):+.2f})")
# generic (non-admissible) pairs too: formula should still hold for 4 delta < pi
Lg = wrap(rng.uniform(-np.pi, np.pi, (6, 8)) * 0.35)
for (i, j) in [(0, 1), (2, 3), (4, 5)]:
    kc = float(kernel_closed_inv({k: v[i] for k, v in invariants(Lg).items()}, {k: v[j] for k, v in invariants(Lg).items()}, delta))
    p, s = kernel_mc(Lg[i], Lg[j], delta, 4_000_000, rng)
    print(f"generic pair {i},{j}: closed {kc:.6e} indep {kernel_indep(Lg[i], Lg[j], delta):.6e} MC {p:.6e} +- {s:.1e}")
print("time", round(time.time() - t, 1), "s; peak RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20)
