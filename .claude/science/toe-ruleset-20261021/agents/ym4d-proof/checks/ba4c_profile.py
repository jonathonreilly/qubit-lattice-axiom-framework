"""ba4c: post-hoc, informational only (no criterion; written after ba4 and ba4b ran, to locate ba4b's log-type growth).
Radial profiles (coarse l1 torus distance d to X_0, bins of width 1) of |grad A| for A = Coulomb potential of
(i) the k = 1 data response (T = 4, 6) and (ii) the synthetic S-bump of ba4 D3 (R = 3, T = 4, 8, 12); for each, the bin
maxima M(d) of sum over the 16 components |grad A| (per site), the bin sums, and d^5 M(d), d^4 M(d)."""
import time

import numpy as np

import ba2_lin as b2
import ba4_lrl as b4

L = b4.L
T0 = time.time()


def profile(A, R, label):
    M = A[0].shape[0]
    G = sum(np.abs(g) for g in b4.grads(A))
    d = b4.dpoint(M, R)
    tot = float(G.sum())
    rows = []
    for D in range(0, int(d.max()) + 1):
        msk = (d >= D) & (d < D + 1)
        if not msk.any():
            continue
        mxv = float(G[msk].max()); sm = float(G[msk].sum())
        rows.append(f"[{D},{D + 1}): max {mxv:.3e} (x(1+d)^5 {mxv * (1 + D) ** 5:.3e}, x(1+d)^4 {mxv * (1 + D) ** 4:.3e}), "
                    f"bin sum/total {sm / tot:.3f}")
    print(f"{label}: total sum|grad A| / L^2 = {tot / L ** 2:.4f}")
    for r in rows:
        print("   " + r)


for T in (4, 6):
    ch = b2.SChain(4, T, 1, (1.0,)); M = ch.levels[0].n
    xs, res, Bk = b4.data_response(ch)
    A = b4.coulomb(b4.arr1(xs[0], M))
    profile(A, L, f"data response k=1 T={T} (CG res {res:.1e})")
    del ch
rng = np.random.default_rng(0)
for T in (4, 8, 12):
    M = 3 * T
    Ap = b4.synthetic("S-bump", M, 3, rng)
    A = b4.coulomb(Ap)
    profile(A, 3, f"S-bump R=3 T={T}")
print(f"ba4c: time {time.time() - T0:.1f} s, peak RSS {b4.rss():.0f} MB")
