"""Extension 2 (not pre-registered): does the 3D D_nn = 0 crossover move with L? (n=0 matching, b=2)
A genuine fixed line stays put; a finite-size crossover (xi ~ L) moves to larger mu as L grows."""
import numpy as np, time
from sim import run_size
rng = np.random.default_rng(78)
S = 192
MU = np.arange(5.0, 13.0, 1.0)
Z = np.load("d3_b2.npz"); tg, mg = list(np.round(Z["tK"], 2)), list(Z["MU"])
def crossing(mu, D):
    for k in range(len(D) - 1):
        if D[k] < 0 <= D[k + 1]:
            return mu[k] + (mu[k + 1] - mu[k]) * (-D[k]) / (D[k + 1] - D[k])
    return np.nan
t0 = time.time()
for t in (0.6, 0.9):
    K = float(np.arctanh(t)); i = tg.index(t)
    D16 = np.array([(Z["big_n0_m"][i, j, 0] - Z["small_n0_m"][i, j, 0]) for j in range(len(mg))])
    E16 = np.array([np.hypot(Z["big_n0_e"][i, j, 0], Z["small_n0_e"][i, j, 0]) for j in range(len(mg))])
    print(f"t={t}: L=32/16 D_nn(mu={mg[8:]}) = {np.round(D16[8:], 4).tolist()} (sigma ~{E16[8:].mean():.4f}); crossing mu = {crossing(np.array(mg), D16):.2f}", flush=True)
    for L, ch in ((64, 8), (96, 4)):
        Ds, Es = [], []
        for mu in MU:
            rb, _, _ = run_size(3, L, 2, [1], K, mu, S, int(1e6 * t + 1e3 * mu + L), rng, chunk=ch)
            rs, _, _ = run_size(3, L // 2, 2, [0], K, mu, S, int(1e6 * t + 1e3 * mu + L) + 5, rng, chunk=2 * ch)
            ob, os_ = rb[1][:, 0], rs[0][:, 0]
            Ds.append(ob.mean() - os_.mean()); Es.append(np.sqrt(ob.var(ddof=1) / S + os_.var(ddof=1) / S))
        Ds, Es = np.array(Ds), np.array(Es)
        print(f"t={t}: L={L}/{L//2} D_nn(mu={MU.tolist()}) = {np.round(Ds, 4).tolist()} (sigma ~{Es.mean():.4f}); "
              f"crossing mu = {crossing(MU, Ds):.2f}; elapsed {time.time()-t0:.0f}s", flush=True)
