"""Test A: the record gas (block 81/117, no contents, zeta=g^-3) is the 3D Ising model; where does it order?"""
import sys, time, itertools
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t21_common import *

# ---- A1: exact identity on random 4^3 torus configurations
L = 4
N = L ** 3
nb = neighbours(L)
eps = eps_array(L).astype(int)
rng = np.random.default_rng(7)
bonds = [(i, nb[i, 2 * j]) for i in range(N) for j in range(3)]
for g in (0.25, 0.4119, 0.05, 1.0 / 7):
    K = np.log(1.0 / g) / 4.0
    diffs = []
    for _ in range(300):
        n = rng.integers(0, 2, N)
        B = sum(n[i] * n[j] for i, j in bonds)
        lnw_gas = n.sum() * np.log(g ** -3.0) + B * np.log(g)         # zeta^N g^B, zeta=g^-3
        sigma = eps * (2 * n - 1)
        lnw_ising = K * sum(sigma[i] * sigma[j] for i, j in bonds)     # ferromagnet in sigma
        diffs.append(lnw_gas - lnw_ising)
    diffs = np.array(diffs)
    print(f"A1 g={g:.4f}: spread of ln w_gas - ln w_Ising over 300 configs = {diffs.max()-diffs.min():.2e}  (const {diffs.mean():.6f})")

# ---- A2: Binder cumulant crossing
Kc = 0.221654626
gc = np.exp(-4 * Kc)
print(f"prediction: K_c = {Kc}  ->  g_c = exp(-4 K_c) = {gc:.5f}")
# cross-check Wolff against Metropolis at one point
seed_numba(5)
Lc = 6; nbc = neighbours(Lc); Nc = Lc ** 3
gtest = 0.30; Kt = np.log(1 / gtest) / 4
sig = np.ones(Nc, dtype=np.int8)
metropolis_sweeps(sig, nbc, Kt, 2000)
acc = 0.0; nm = 6000
for _ in range(nm):
    metropolis_sweeps(sig, nbc, Kt, 3)
    acc += abs(sig.sum() / Nc)
mw = binder_run(6, gtest, 500, 20000, 1, seed=11)[0]
print(f"Wolff vs Metropolis <|M|> at L=6, g=0.30: {mw:.4f} vs {acc/nm:.4f}")

gs = [0.36, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.46]
res = {}
t0 = time.time()
for Ls in (6, 8, 10):
    for g in gs:
        m1, m2, m4 = binder_run(Ls, g, 1000, 60000, 1, seed=100 + Ls)
        res[(Ls, g)] = (m1, 1 - m4 / (3 * m2 * m2))
print(f"(A2 runtime {time.time()-t0:.0f}s)")
print("Binder U = 1 - <M^4>/(3<M^2>^2):")
print("   g   " + "  ".join(f"L={Ls:2d}" for Ls in (6, 8, 10)))
for g in gs:
    print(f"{g:.2f}  " + "  ".join(f"{res[(Ls,g)][1]:.4f}" for Ls in (6, 8, 10)))
# crossing of L=6/8 and L=8/10 by linear interpolation
def crossing(La, Lb):
    d = np.array([res[(La, g)][1] - res[(Lb, g)][1] for g in gs])
    for k in range(len(gs) - 1):
        if d[k] * d[k + 1] < 0:
            return gs[k] + (gs[k + 1] - gs[k]) * d[k] / (d[k] - d[k + 1])
    return None
print("crossing (6,8):", crossing(6, 8), " crossing (8,10):", crossing(8, 10), " (6,10):", crossing(6, 10))

# ---- A3: staggered magnetisation and defect density
print("A3: <|sigma|> = <|M|> per site, defect density p = P(sigma=-1) = (1-<|M|>)/2")
for Ls in (8, 12):
    for g in (9 / 62500, 1e-2, 0.1, 0.25, 0.35, 0.4119, 0.5, 0.6, 1.0):
        m1, m2, m4 = binder_run(Ls, g, 500, 8000, 1, seed=7)
        print(f"  L={Ls:2d} g={g:.6f}  <|M|>={m1:.4f}  p~{(1-m1)/2:.4f}")
