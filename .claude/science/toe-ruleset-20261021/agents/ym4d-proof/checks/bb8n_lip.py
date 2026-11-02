"""bb8n: Theorem N2-loc (b), (c) (BFT_B §24.2) in the d = 2 SU(2) model of bb7n (lane B session 8).

Criteria: checks/bb8n_criteria.md (written before this script). The framed DD8 chain is bb7n_chain.py's code, executed unchanged
up to its first test (definitions only). Covariant curvature difference: dF = F_j(p) - Ad_tau F_j(p'), tau = the chain's
transport from p's first corner along axis 0 then axis 1 to p''s first corner.
"""
import os
import time

import numpy as np

T0 = time.time()
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bb7n_chain.py")).read()
exec(_src.split("\nout = []\n")[0])          # qmul, qinv, qexp, qlog, NA, LIN, refine, hol, chain, sh, TK, ...
rng8 = np.random.default_rng(8282)
OFFS = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 0), (3, 3), (9, 0), (9, 4), (27, 0), (27, 27)]


def Ad(t, v):
    pv = np.concatenate([np.zeros(v.shape[:-1] + (1,)), v], axis=-1)
    return qmul(qmul(t, pv), qinv(t))[..., 1:]


def transport(Z, a, b):
    """tau(x, y) = Z0(x,y)...Z0(x+a-1,y) Z1(x+a,y)...Z1(x+a,y+b-1) (periodic arrays)."""
    tau = NA.one(Z.shape[:2])
    for i in range(a):
        tau = qmul(tau, sh(Z[:, :, 0], i, 0))
    for i in range(b):
        tau = qmul(tau, sh(Z[:, :, 1], a, i))
    return tau


def curvF(Z, m):
    return qlog(hol(Z, NA)) * 9.0 ** m


def scaled_field(b, target):
    f = lambda s: curv_profile(qexp(b * s), NA).max()
    slope = f(1e-5) / 1e-5
    lo, hi = 0.3 * target / slope, 3.0 * target / slope
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return b * 0.5 * (lo + hi)


def measure(V, fk, gauged=None):
    levs = chain(V, NA, 3)
    lip, ctrl, fields = {}, {}, {}
    for m in (1, 2, 3):
        Z = levs[m]
        F = curvF(Z, m)
        best = 0.0
        bctrl = 0.0
        for (a, bb) in OFFS:
            if max(a, bb) > 3 ** m:
                continue
            dist = max(a, bb) / 3.0 ** m
            tau = transport(Z, a, bb)
            Fp = sh(F, a, bb)
            dF = np.linalg.norm(F - Ad(tau, Fp), axis=-1)
            fields[(m, a, bb)] = dF
            best = max(best, dF.max() / (dist * fk))
            bctrl = max(bctrl, np.linalg.norm(F - Fp, axis=-1).max() / (dist * fk))
        lip[m] = best
        ctrl[m] = bctrl
    dmax = {}
    for m in (1, 2, 3):
        Zc, Zf = levs[m - 1], levs[m]
        rho = 3.0 ** (-(m - 1))
        worst = 0.0
        for a in range(2):
            e = (1, 0) if a == 0 else (0, 1)
            row = NA.one(Zf.shape[:2])
            for i in range(3):
                row = qmul(row, sh(Zf[:, :, a], i * e[0], i * e[1]))
            row = row[0::3, 0::3]
            d = qlog(qmul(qinv(row), Zc[:, :, a]))
            worst = max(worst, np.linalg.norm(d, axis=-1).max())
        dmax[m] = worst / (rho ** 4 * fk ** 2)
    return lip, ctrl, fields, dmax


out = []
b = rng8.standard_normal((TK, TK, 2, 3))
res = {}
for target in (0.10, 0.05):
    bs = scaled_field(b, target)
    V = qexp(bs)
    fk = curv_profile(V, NA).max()
    res[target] = (fk,) + measure(V, fk)
fk, lip, ctrl0, fields, dmax = res[0.10]
out.append(f"setup: top side {TK}, depth 3, f_k = {fk:.6f} (and {res[0.05][0]:.6f}); offsets {OFFS} with |delta|_inf <= 3^m")
La = lip[3] <= 1.25 * max(lip[1], lip[2])
out.append(f"L-a covariant Lipschitz ratio Lip_m/f_k (m = 1, 2, 3) = {lip[1]:.4f}, {lip[2]:.4f}, {lip[3]:.4f}: "
           f"{'PASS' if La else 'FAIL'}")
# L-b, C: Haar-random level-k gauge
h = rng8.standard_normal((TK, TK, 4))
h /= np.linalg.norm(h, axis=-1, keepdims=True)
V = qexp(scaled_field(b, 0.10))
Vh = np.stack([qmul(qmul(h, V[:, :, a]), qinv(sh(h, *((1, 0) if a == 0 else (0, 1))))) for a in range(2)], axis=2)
lip_h, ctrl_h, fields_h, dmax_h = measure(Vh, fk)
lb = max(np.abs(fields[key] - fields_h[key]).max() for key in fields)
Lb = lb <= 1e-10
out.append(f"L-b gauge invariance of |F_j(p) - Ad_tau F_j(p')| under a Haar-random level-k gauge: max diff {lb:.1e}: "
           f"{'PASS' if Lb else 'FAIL'}")
D10, D05 = res[0.10][4], res[0.05][4]
rat = [D05[m] / D10[m] for m in (1, 2, 3)]
Lc = D10[3] <= 2 * max(D10[1], D10[2]) and all(0.5 <= r <= 2 for r in rat)
out.append(f"L-c row defects |d_j|/(rho_(j+1)^4 f_k^2) (m = 1, 2, 3) at f_k = 0.10: {D10[1]:.4f}, {D10[2]:.4f}, {D10[3]:.4f}; "
           f"at 0.05: {D05[1]:.4f}, {D05[2]:.4f}, {D05[3]:.4f}; ratios {rat[0]:.3f}, {rat[1]:.3f}, {rat[2]:.3f}: "
           f"{'PASS' if Lc else 'FAIL'}")
cmax = max(ctrl_h.values())
Cc = cmax >= 5 * max(lip.values())
out.append(f"C control: non-covariant ratio in the Haar gauge (m = 1, 2, 3) = {ctrl_h[1]:.2f}, {ctrl_h[2]:.2f}, {ctrl_h[3]:.2f} "
           f"(ungauged: {ctrl0[1]:.3f}, {ctrl0[2]:.3f}, {ctrl0[3]:.3f}); >= 5 x max Lip: {'PASS' if Cc else 'FAIL'}")
out.append(f"informational: Lip at f_k = 0.05: {res[0.05][1][1]:.4f}, {res[0.05][1][2]:.4f}, {res[0.05][1][3]:.4f}")
allp = La and Lb and Lc and Cc
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (L-a, L-b, L-c, C)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
