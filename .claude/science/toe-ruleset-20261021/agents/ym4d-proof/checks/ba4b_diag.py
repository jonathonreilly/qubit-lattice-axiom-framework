"""ba4b: post-hoc diagnostic (criteria: checks/ba4b_criteria.md, written before this file). k = 1, T = 2..6."""
import sys
import time

import numpy as np

import ba2_lin as b2
import ba4_lrl as b4

L = b4.L
T0 = time.time()
QXR = {2: 0.0372, 3: 0.1777, 4: 0.2542, 5: 0.3254}  # ba4_out_D2.txt, XR-designed (4 digits as printed)
B = {}
for T in (2, 3, 4, 5, 6):
    tt = time.time()
    ch = b2.SChain(4, T, 1, (1.0,)); lf = ch.levels[0]; M = lf.n; Q = ch.Q[0]
    xs, res, Bk = b4.data_response(ch)
    Aarr = b4.coulomb(b4.arr1(xs[0], M), keep_mean=True)
    z = b4.flux_cg(Aarr, T)
    diff = b4.vec1(Aarr) - Q.T @ z
    B[T] = float(np.sum(np.abs(diff))) / L ** 2
    W = sum(float(np.sum(np.abs(g))) for g in b4.grads(Aarr)) / L ** 2
    X = b4.arr1(xs[0], M); F = b4.dform(X); A0 = b4.coulomb(X)
    qa = b4.Q_a(F, A0, L, 0.5)
    print(f"T={T}: B(T) {B[T]:.5f}, W(T) {W:.5f}, Q_a(m'=0.5) {qa:.3f}; CG res {res:.1e} "
          f"({time.time() - tt:.0f} s, RSS {b4.rss():.0f} MB)", flush=True)
    del ch
d3 = B[3] - B[2]; d6 = B[6] - B[5]
ratio = (6 * d6) / (3 * d3) if d3 != 0 else float('nan')
ok = (d6 <= 0) or (ratio <= 0.65)
print(f"discriminator: 3*D3 {3 * d3:.5f}, 6*D6 {6 * d6:.5f}, ratio {ratio:.3f} -> {'PASS' if ok else 'FAIL'}")
print("Q_XR <= B(T): " + ", ".join(f"T={T} {QXR[T]:.4f} <= {B[T]:.4f} {'ok' if QXR[T] <= B[T] else 'VIOLATED'}"
                                     for T in (2, 3, 4, 5)))
print(f"ba4b: time {time.time() - T0:.1f} s, peak RSS {b4.rss():.0f} MB")
