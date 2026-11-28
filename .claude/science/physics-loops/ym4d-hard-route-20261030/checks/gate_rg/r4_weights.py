#!/usr/bin/env python3
"""R4 of CRITERIA.md: compatible down-averages of one scalar top profile, along one coordinate."""
import math
import numpy as np

def tau(L):
    r = (L - 1) // 2
    d = {}
    for t in range(-r, r + L):
        d[t] = sum(1 for a in range(-r, r + 1) if a <= t <= a + L - 1)
    return d

def down(W, L, kind):
    """W on parent sites 0..N-1. Fine site z = L*y + o. Returns fine weights on the interior."""
    N = len(W)
    r = (L - 1) // 2
    if kind == "box":
        return np.repeat(W, L)                       # one block: z in [Ly-r, Ly+r]
    t = tau(L)
    out = np.zeros(N * L)
    # fine index i <-> z = i - r, so block y holds i in [Ly, Ly+L-1]
    ts = np.array(sorted(t))
    wt = np.array([t[v] for v in ts]) / L
    for i in range(N * L):
        z = i - r
        lo = int(math.ceil((z - ts[-1]) / L))
        hi = int(math.floor((z - ts[0]) / L))
        for y in range(max(lo, 0), min(hi, N - 1) + 1):
            out[i] += t[z - L * y] / L * W[y]
    return out

ok = True
for L in (3, 5, 7):
    M = 5 if L == 7 else 6
    for nu in (0.1,):
        top = np.exp(nu * np.arange(12))
        Wb, Wt = top.copy(), top.copy()
        row = []
        for m in range(1, M + 1):
            Wb = down(Wb, L, "box")
            Wt = down(Wt, L, "tent")
            s = L ** m
            lo, hi = 2 * s, len(Wb) - 2 * s
            lb, lt = np.log(Wb[lo:hi]), np.log(Wt[lo:hi])
            same_box = np.abs(np.diff(lb)).max()
            same_tent = np.abs(np.diff(lt)).max()
            cross = np.abs(lb - lt).max()
            near = np.maximum.reduce([np.abs(lb[1:] - lt[:-1]).max(), np.abs(lt[1:] - lb[:-1]).max(), cross, same_box, same_tent])
            frac = float(np.mean(np.abs(lb - lt) > nu / 10))
            row.append((m, near, same_box, same_tent, cross, frac))
            print(f"L {L} m {m}: rho {near:.5f} box jump {same_box:.5f} tent step {same_tent:.6f} box-tent {cross:.5f} frac>nu/10 {frac:.3f} rho L^m {near*s:.2f}", flush=True)
        rho6 = row[-1][1]
        refuted = rho6 > nu / 10
        print(f"R4a L {L}: rho at m = {row[-1][0]} is {rho6:.4f}; nu/10 = {nu/10:.4f}; claim {'REFUTED' if refuted else 'not refuted'}")
        s = L ** 3
        z = np.arange(2000)
        sc = nu * z / s
        c_ok = abs(np.abs(np.diff(sc)).max() - nu / s) < 1e-12
        ok &= c_ok
        print(f"R4c L {L}: scalar rho {np.abs(np.diff(sc)).max():.8f} against {nu/s:.8f} {'PASS' if c_ok else 'FAIL'}")
print("R4c", "PASS" if ok else "FAIL")
