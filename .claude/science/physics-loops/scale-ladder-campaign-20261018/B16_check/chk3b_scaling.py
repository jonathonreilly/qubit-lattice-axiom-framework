"""B16 check, item 3b: order counting of the {G[e0], H(N)} defect with an O(1)-correlated test configuration.

Run 1 (chk3_obstruction.py, C3c) was pre-asymptotic: the leading term H(d_0 N) had a ~2% overlap with the
energy density, so the N-independent defect dominated up to L = 32.  Here the fields carry an envelope
(1 + 0.6 sin 2 pi x) and N = exp(0.5 cos 2 pi x), so H(d_0 N) is O(a) H(1) with an O(1) coefficient.

Measured (box units, a = 1/L):  Lead = H(N'_central),  D = {G[e0], H(1)},  R = {G[e0], H(N)} - H(N'_best).
Expectation stated BEFORE running (from the analytic counting in REPORT):
  FWD    : D/Lead ~ a^1 (slope -1), R/Lead ~ a^1
  scalar : D = 0, R/Lead ~ a^2
  STAG   : D = 0 on band-limited smooth fields (pure doubler coupling, seen in run 1); R/Lead: no prior expectation.
"""
from fractions import Fraction as Fr

import numpy as np

from chk_lat import Lat, uniform_timing
from chk1_timing import staggered
from chk1b_induced_generator import induced_generator, fwd_GA
from chk3_obstruction import sparse_gen, fmat, smear, dlapse

RES = {"pass": 0, "fail": 0}
TP = 2 * np.pi


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def env(r):
    return 1 + 0.6 * np.sin(TP * r[0])


def lapse(lat):
    a = 1.0 / lat.L
    return np.array([np.exp(0.5 * np.cos(TP * x[0] * a)) for x in lat.sites])


def em_fields(lat):
    a = 1.0 / lat.L
    def Ac(j, r):
        x, y, z = r
        return env(r) * [np.sin(TP * y) + 0.5 * np.cos(TP * z + 0.3), np.cos(TP * (x + 0.2)) * np.sin(TP * z), 0.7 * np.sin(TP * (x - y))][j]
    def Wc(q, r):
        x, y, z = r
        return env(r) * [np.cos(TP * (x + z)) + 0.4 * np.sin(TP * y), 0.8 * np.sin(TP * (y - 0.1)) * np.cos(TP * x), np.cos(TP * z + 0.7)][q]
    A = np.zeros(len(lat.links))
    for k, (x, j) in enumerate(lat.links):
        r = np.array(x, float); r[j] += 0.5
        A[k] = a * Ac(j, r * a)
    b = np.zeros(len(lat.plaqs))
    for p, (y, (i, j)) in enumerate(lat.plaqs):
        r = np.array(y, float); r[i] += 0.5; r[j] += 0.5
        b[p] = a * Wc(lat.pairs.index((i, j)), r * a)
    Fm = fmat(lat)
    return A, Fm.T @ b, Fm


def em_run(name, L):
    g2, cb = 0.9, 1.7
    lat = Lat(L)
    if name == "FWD":
        u, w = uniform_timing(lat, {j: (Fr(1), Fr(0)) for j in range(3)}, {ij: {"00": Fr(1)} for ij in lat.pairs})
        X = fwd_GA(lat)
    else:
        u, w = staggered(lat, 0)
        X = induced_generator(lat, u, w, Fr(1))
    G = sparse_gen(lat, X, {b: (1 if b[1] == 0 else 0) for b in X})
    A, E, Fm = em_fields(lat)
    F = Fm @ A

    def br(N):
        nl, mp = smear(lat, u, w, N)
        return (G.T @ E) @ (g2 * nl * E) - (G @ A) @ ((cb / g2) * (Fm.T @ (mp * F)))

    def H(N):
        nl, mp = smear(lat, u, w, N)
        return (g2 / 2) * np.sum(nl * E * E) + (cb / (2 * g2)) * np.sum(mp * F * F)
    N = lapse(lat)
    one = np.ones(len(lat.sites))
    B = br(N)
    lead = H(dlapse(lat, N, "central"))
    R = min(abs(B - H(dlapse(lat, N, k))) for k in ("backward", "forward", "central"))
    return br(one), lead, B, R


def scalar_run(L):
    c = 1.3
    lat = Lat(L)
    a = 1.0 / L
    Xs = np.array(lat.sites, float) * a
    e = 1 + 0.6 * np.sin(TP * Xs[:, 0])
    phi = e * (np.sin(TP * Xs[:, 0] + 0.3) * np.cos(TP * Xs[:, 1]) + 0.5 * np.cos(TP * (Xs[:, 2] - Xs[:, 0])))
    pi = a * e * (np.cos(TP * Xs[:, 1] - 0.2) + 0.7 * np.sin(TP * (Xs[:, 0] + Xs[:, 2])))
    idx = np.arange(len(lat.sites))
    fwd = [np.array([lat.sidx[lat.sh(x, j)] for x in lat.sites]) for j in range(3)]
    bwd = []
    for j in range(3):
        b = np.empty_like(fwd[j]); b[fwd[j]] = idx; bwd.append(b)

    def H(N):
        v = np.sum(N * pi ** 2 / 2)
        for j in range(3):
            v += np.sum((N + N[fwd[j]]) / 2 * c / 2 * (phi[fwd[j]] - phi) ** 2)
        return v

    def br(N):
        dGdpi = (phi[fwd[0]] - phi[bwd[0]]) / 2
        dGdphi = (pi[bwd[0]] - pi[fwd[0]]) / 2
        dHdpi = N * pi
        dHdphi = np.zeros_like(N)
        for j in range(3):
            wf = (N + N[fwd[j]]) / 2
            wb = (N[bwd[j]] + N) / 2
            dHdphi += c * (wb * (phi - phi[bwd[j]]) - wf * (phi[fwd[j]] - phi))
        return dGdphi @ dHdpi - dGdpi @ dHdphi
    N = lapse(lat)
    B = br(N)
    lead = H(dlapse(lat, N, "central"))
    R = min(abs(B - H(dlapse(lat, N, k))) for k in ("backward", "forward", "central"))
    return br(np.ones(len(lat.sites))), lead, B, R


def slope(Ls, v):
    return np.polyfit(np.log(Ls), np.log(np.abs(v)), 1)[0]


if __name__ == "__main__":
    Ls = [8, 12, 16, 24, 32, 40]
    out = {}
    for name in ("FWD", "STAG", "scalar"):
        rows = []
        for L in Ls:
            D, lead, B, R = scalar_run(L) if name == "scalar" else em_run(name, L)
            rows.append((L, D, lead, B, R))
            print(f"  {name:6s} L={L:3d}  Lead={lead: .4e}  B={B: .4e}  B/Lead={B / lead: .5f}  D/Lead={D / lead: .3e}  R/Lead={R / lead: .3e}", flush=True)
        out[name] = rows
    s = {}
    for name, rows in out.items():
        Lv = [r[0] for r in rows]
        sD = slope(Lv, [max(abs(r[1] / r[2]), 1e-300) for r in rows])
        sR = slope(Lv, [r[4] / r[2] for r in rows])
        s[name] = (sD, sR)
        print(f"  {name}: slope D/Lead {sD:.2f}, slope R/Lead {sR:.2f}")
    check("C3d-FWD", abs(s["FWD"][0] + 1) < 0.15 and abs(s["FWD"][1] + 1) < 0.2,
          f"forward Maxwell: uniform-shift defect D/Lead ~ L^{s['FWD'][0]:.2f}, full residual R/Lead ~ L^{s['FWD'][1]:.2f}: the defect is O(a) relative to the leading H(xi.grad N)")
    check("C3d-scalar", max(abs(r[1]) for r in out["scalar"]) < 1e-10 and abs(s["scalar"][1] + 2) < 0.2,
          f"scalar (B14 conventions): D = 0, residual R/Lead ~ L^{s['scalar'][1]:.2f}: O(a^2)")
    stag_D = max(abs(r[1]) for r in out["STAG"])
    stag_R = [r[4] / r[2] for r in out["STAG"]]
    print(f"  STAG: max|D| = {stag_D:.2e}; R/Lead = {[round(v, 4) for v in stag_R]}")
    check("C3d-STAG", stag_D < 1e-10 and min(abs(v) for v in stag_R[-3:]) > 0.05,
          "staggered: D = 0 on smooth fields, but the residual does NOT decrease with L: {G',C} fails at O(1) relative to H(xi.grad N) (doubler part of G' x staggered O(a) part of the lapse smearing)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
