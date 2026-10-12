"""R3-1 check 4: Bragg resonances of an in-band momentum on one realization (L7).
Dual lattice: 2*pi*L7^*; its sublattice {m0 = 0 mod 7} equals 2*pi*L7 (G = 2pi(sqrt7 j, m)).  Use the
dual shell G^2 = 4 pi^2 (j,m in the L7 shell N = 1, both time signs).
For an in-band momentum k (|k|_E = omega << 2pi) count G with |(k - G)^2| < delta, per dyadic Euclidean
shell |G|_E in [T, 2T).  Kinematics (report): timelike k -> resonant G confined to |G|_E ~ 4pi^2/(2M);
null k -> count grows ~ T/omega per dyadic shell (collinear, trans-Planckian partners k' = k - G).
Also: min over the shell of |(k-G)^2| for G != 0 (no in-band-to-in-band channel: |k-G|_E >= 2pi - omega)."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("s", "r31_lv_scaling_lib.py")
lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(lib)
n0max = 700
X = lib.shell(1, n0max)
X = [np.concatenate([x, -x]) for x in X]
# n0 = 0 points: |m|^2 = 1
extra = np.array([[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]], float)
X = [np.concatenate([X[i], extra[:, i]]) for i in range(4)]
G = [2 * np.pi * x for x in X]
GE = np.sqrt(sum(g * g for g in G)); G2 = -G[0]**2 + G[1]**2 + G[2]**2 + G[3]**2
assert np.allclose(G2, 4 * np.pi**2)
Tmax = 2 * np.pi * np.sqrt(7.0) * n0max  # complete for |G|_E <= Tmax (since |G|_E >= sqrt2*|G0|... conservative)
Tmax = 2 * np.pi * np.sqrt(14.0 * n0max**2 + 1)
print(f"dual shell G^2 = 4pi^2: {len(G[0])} vectors, complete for |G|_E <= {Tmax:.0f}")
delta = 1.0
def counts(k, label):
    kG = -k[0] * G[0] + k[1] * G[1] + k[2] * G[2] + k[3] * G[3]
    z = 4 * np.pi**2 - 2 * kG + (-k[0]**2 + k[1]**2 + k[2]**2 + k[3]**2)
    res = np.abs(z) < delta
    edges = 2 * np.pi * 2.0 ** np.arange(0, 20)
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        if hi > Tmax: break
        sel = (GE >= lo) & (GE < hi)
        out.append((int(lo), int((res & sel).sum())))
    kE = np.sqrt((k * k).sum())
    minE = np.min(np.sqrt(sum((ki - g)**2 for ki, g in zip(k, G))))
    print(f"{label}: |k|_E={kE:.3f}; resonant |(k-G)^2|<{delta} per dyadic |G|_E shell [T,2T): {out}; min |k-G|_E = {minE:.3f}")
omega = 0.1
khat = np.array([0.3, 0.5, np.sqrt(1 - 0.34)])
counts(np.array([omega, *(omega * khat)]), "null k, omega=0.1")
counts(np.array([0.05, *(0.05 * khat)]), "null k, omega=0.05")
counts(np.array([omega, 0, 0, 0]), "timelike k=(0.1,0,0,0) (rest frame M=0.1)")
counts(np.array([omega * np.cosh(1.0), *(omega * np.sinh(1.0) * khat)]), "timelike k, M=0.1, rapidity 1")
