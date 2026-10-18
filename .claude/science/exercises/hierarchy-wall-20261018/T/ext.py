"""Extension (not pre-registered): are the 3D near-fixed points at mu~7-9 finite-size artefacts (xi ~ L)?
3D b=2, L=64 vs 32 (n=0 final 32, n=1 final 16), compared with the L=32 vs 16 grid run.
Prints D_nn = A_big - A_small (units of sigma) on t x mu. An artefact moves to larger mu as L doubles."""
import numpy as np, time
from sim import run_size
rng = np.random.default_rng(77)
tK = [0.6, 0.7, 0.8, 0.9]; MU = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
S = 64
Z = np.load("d3_b2.npz"); tg, mg = list(Z["tK"]), list(Z["MU"])
t0 = time.time()
for n in (0, 1):
    print(f"\n== matching level n={n}: D_nn/sigma, L=64 vs 32 [and L=32 vs 16 from grid run]")
for t in tK:
    K = float(np.arctanh(t))
    rowA = {0: [], 1: []}; rowB = {0: [], 1: []}
    for mu in MU:
        rb, _, Cb = run_size(3, 64, 2, [1, 2], K, mu, S, int(1e6 * t + 1e3 * mu), rng, chunk=16)
        rs, _, Cs = run_size(3, 32, 2, [0, 1], K, mu, S, int(1e6 * t + 1e3 * mu) + 5, rng, chunk=32)
        for n in (0, 1):
            ob, os_ = rb[n + 1][:, 0], rs[n][:, 0]
            Dz = (ob.mean() - os_.mean()) / np.sqrt(ob.var(ddof=1) / S + os_.var(ddof=1) / S)
            rowA[n].append(f"{Dz:+6.1f}")
            if mu in mg:
                i, j = tg.index(t), mg.index(mu)
                Db = (Z[f"big_n{n}_m"][i, j, 0] - Z[f"small_n{n}_m"][i, j, 0]) / np.hypot(Z[f"big_n{n}_e"][i, j, 0], Z[f"small_n{n}_e"][i, j, 0])
                rowB[n].append(f"{Db:+6.1f}")
            else:
                rowB[n].append("   n/a")
    for n in (0, 1):
        print(f"n={n} t={t:.1f} mu={MU}:\n   L=64/32: {' '.join(rowA[n])}\n   L=32/16: {' '.join(rowB[n])}", flush=True)
print("elapsed", round(time.time() - t0, 1))
