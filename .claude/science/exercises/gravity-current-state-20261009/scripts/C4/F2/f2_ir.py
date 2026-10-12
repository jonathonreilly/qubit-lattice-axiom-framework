"""F2: IR extrapolation of the continuous-time Z^3 QED speeds (same formulas as f2_qed_speeds.py),
slab-wise over k_x so that L up to ~480 fits in memory. Gives dc_f, dc_gamma (per naive and per staggered)
and Delta_QED = (dc_f - dc_gamma_stag)*16pi^2/e^2 as m, lam -> 0.
Usage: python f2_ir.py
"""
import numpy as np, time

def slabs(L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    KY, KZ = np.meshgrid(k, k, indexing="ij")
    return k, KY, KZ

def fermion(L, m, lam, h=1e-4):
    k, KY, KZ = slabs(L)
    a0 = A2 = Ip = Im = 0.0
    syz2 = np.sin(KY) ** 2 + np.sin(KZ) ** 2
    cyz = np.cos(KY / 2) ** 2 + np.cos(KZ / 2) ** 2
    khyz = 4 * (np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    for kx in k:
        w = np.sqrt(4 * np.sin(kx / 2) ** 2 + khyz + lam ** 2)
        E = np.sqrt(np.sin(kx) ** 2 + syz2 + m ** 2)
        C0 = np.cos(kx / 2) ** 2 + cyz
        a0 += np.sum(-(1 - C0) / (2 * w * (E + w) ** 2))
        A2 += np.sum(1 / (2 * w))
        for sgn in (+1, -1):
            px = sgn * h
            Eq = np.sqrt(np.sin(px - kx) ** 2 + syz2 + m ** 2)
            C = 1 + np.cos(px - kx / 2) ** 2 + cyz
            F = np.sum(np.sin(px - kx) * (2 * np.cos(px - kx / 2) ** 2 - C) / (2 * Eq * w * (Eq + w)))
            if sgn > 0: Ip += F
            else: Im += F
    N = L ** 3
    a0 /= N; A2 /= N
    a1 = -0.5 * A2 - (Ip - Im) / N / (2 * h)
    return a0, a1, A2

def photon(L, m, kxs=(0.02, 0.04)):
    k, QY, QZ = slabs(L)
    sy, sz = np.sin(QY), np.sin(QZ)
    aE = tad = 0.0
    bub = np.zeros(len(kxs))
    for qx in k:
        sx = np.sin(qx)
        E2 = sx ** 2 + sy ** 2 + sz ** 2 + m ** 2
        E = np.sqrt(E2)
        aE += 0.5 * np.sum(np.cos(qx) ** 2 * (E2 - sx ** 2) / E ** 5)
        tad += 2 * np.sum(sy ** 2 / E)
        for i, kx in enumerate(kxs):
            sxp = np.sin(qx + kx)
            Ep = np.sqrt(sxp ** 2 + sy ** 2 + sz ** 2 + m ** 2)
            Y = sx * sxp - sy ** 2 + sz ** 2 + m ** 2
            bub[i] += -4 * np.sum(np.cos(QY) ** 2 * (E * Ep + Y) / (2 * E * Ep * (E + Ep)))
    N = L ** 3
    aE /= N; tad /= N; bub /= N
    vals = [(bub[i] + tad) / (4 * np.sin(kx / 2) ** 2) for i, kx in enumerate(kxs)]
    aB = (4 * vals[0] - vals[1]) / 3
    return aE, aB

if __name__ == "__main__":
    u = 16 * np.pi ** 2
    t0 = time.time()
    print("== photon, per naive fermion (8 Dirac doublers): dc_gamma*16pi^2 = (aB-aE)/2*16pi^2")
    for m in (0.1, 0.07, 0.05, 0.035):
        for L in (int(np.ceil(16 / m / 8) * 8), int(np.ceil(24 / m / 8) * 8)):
            aE, aB = photon(L, m)
            print(f"m={m:6.3f} L={L:4d}  dc_gamma(naive)*16pi^2 = {u*(aB-aE)/2:+.5f}   per Dirac {u*(aB-aE)/16:+.5f}", flush=True)
    print("\n== fermion (Feynman gauge): dc_f*16pi^2 = (a1-a0)*16pi^2")
    for (m, lam) in [(0.1, 0.2), (0.07, 0.14), (0.05, 0.1), (0.035, 0.07), (0.05, 0.05), (0.035, 0.035)]:
        for L in (int(np.ceil(10 / min(m, lam) / 8) * 8), int(np.ceil(15 / min(m, lam) / 8) * 8)):
            a0, a1, A2 = fermion(L, m, lam)
            print(f"m={m:6.3f} lam={lam:6.3f} L={L:4d}  a0={u*a0:+.4f} a1={u*a1:+.4f} (tadpole {-u*A2/2:+.4f})  dc_f*16pi^2 = {u*(a1-a0):+.5f}", flush=True)
    print(f"elapsed {time.time()-t0:.1f}s")
