"""R4-3 check D: locate forward-tube zeros of moment-conditioned (d'Alembertian) LRL shell kernels along p = i kappa u.
K^(i kappa u) = sum_N w_N S_N(u,kappa) is real and continuous in kappa; a sign change => a zero kappa* (IVT) =>
homogeneous solution exp(-kappa* u.x) growing toward the future at rate kappa*/a (forward-tube zero = instability;
criterion as for causal-set d'Alembertians, RL1 / Aslanbeigi-Saravani-Sorkin, prior art counted once).
Weights: the 5-shell solution for shells [-1,-2,-3,-5,-7] (empirical nu_N from r43_S_arrays.npz)."""
import numpy as np
from scipy.special import k1
exec(open("r43_moment_lv.py").read().split("t0 = time.time()")[0].split('"""', 2)[2])   # shell(), boost()
D = np.load("r43_S_arrays.npz")
Ns, S, kaps, us = list(D["Ns"]), D["S"], D["kaps"], D["us"]
taus = np.sqrt(-np.array(Ns, float))
nus = S[:, -1, :].mean(1) / (4 * np.pi * k1(kaps[-1] * taus) / (kaps[-1] * taus))
pick = [-1, -2, -3, -5, -7]; idx = [Ns.index(p) for p in pick]
A = np.array([nus * taus**-2, nus, nus * np.log(taus), nus * taus**2, nus * taus**2 * np.log(taus)])[:, idx]
w = np.linalg.solve(A, [0, 0, 0, 0, 1.0])
print("weights", np.round(w, 3))
n0max = 520
X = {N: shell(N, n0max) for N in pick}
def Kw(u, k):
    um = u * np.array([1, -1, -1, -1])
    return sum(wi * np.exp(-k * (um @ X[N])).sum() for wi, N in zip(w, pick))
for iu in range(4):
    u = us[iu]
    grid = np.geomspace(0.9, 0.12, 15)
    vals = np.array([Kw(u, k) for k in grid])
    LI = (np.pi / 4) * grid**2
    print(f"\ndirection {iu} (rapidity {np.arccosh(u[0]):.3f}):")
    print("   kappa : " + " ".join(f"{k:7.3f}" for k in grid))
    print("   K/LI  : " + " ".join(f"{v/l:7.1f}" for v, l in zip(vals, LI)))
    zs = []
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            lo, hi, flo = grid[i + 1], grid[i], vals[i + 1]
            for _ in range(30):
                mid = 0.5 * (lo + hi); fm = Kw(u, mid)
                if np.sign(fm) == np.sign(flo): lo, flo = mid, fm
                else: hi = mid
            zs.append(0.5 * (lo + hi))
    print("   zeros kappa* (lattice units): " + ", ".join(f"{z:.5f}" for z in zs))
    print("   growth e-fold time 1/kappa* (lattice times): " + ", ".join(f"{1/z:.2f}" for z in zs))
