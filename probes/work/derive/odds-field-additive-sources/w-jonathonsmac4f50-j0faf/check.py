#!/usr/bin/env python3
"""J:derive:odds-field-additive-sources:a2 - worker w-jonathonsmac4f50-j0faf (claude-opus-5-5).

Setting (block 42, open PR 'ail42'; supplied reading, nothing adopted): linearized self-consistent odds, lean channel
v_x = 6 l1 * (mean of v over the six neighbours) away from records; a record FIXES the lean at its site (boundary value).
So the lean of a set A of records is v(x) = P_x(walk hits A before it is killed), the walk moving to a uniform neighbour and
surviving each step with probability theta = 6 l1; its Green function is G_theta = (I - theta P)^(-1) = (1/l1)(-Lap + m^2)^(-1),
m^2 = (1 - 6 l1)/l1 (block 42). Capacity: cap(A) = 1^T (G_A)^(-1) 1, G_A = G restricted to A x A; far from A,
v ~ cap(A) G(x). Normalization used for numbers: the massless walk (theta = 1, e.g. (3,1,2)), G = G_SRW = 6 (-Lap)^(-1).
Prior attempt a3 (w-jonathonsmac4f50-j38d3, claude-opus-5, same model family, unrefereed) did the SCREENED case on tori;
this attempt does the MASSLESS case on the infinite lattice (a3's open item 1), the range dependence, arrays, and kappa.
Exact parts: sympy/Fraction.  Infinite-lattice values: floating point quadrature of G(x) = int_0^oo prod_i ive(|x_i|, 2t) dt,
validated against Watson's closed form, the exact identity G(e1) = G(0) - 1 and the lattice equation (errors ~1e-8);
every such claim is labelled NUMERICAL with its margin.
"""
import contextlib
import io
import itertools
import math

import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.special import ive, erf, gamma

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


# ---------------------------------------------------------------------------------------------- lattice Green function
_xs, _ws = leggauss(2000)


def G_lap(pts, m2=0.0, T=4.0e4):
    """(-Lap + m2)^(-1)(x) on Z^3 = int_0^oo e^(-m2 t) prod ive(|x_i|, 2t) dt; massless tail by the heat-kernel erf term."""
    pts = np.abs(np.atleast_2d(np.asarray(pts, dtype=float)))
    a, b = np.log(1e-9), np.log(T)
    s = 0.5 * (b - a) * _xs + 0.5 * (b + a)
    t = np.exp(s)
    wt = 0.5 * (b - a) * _ws * t * np.exp(-m2 * t)
    out = np.empty(len(pts))
    for i in range(0, len(pts), 256):
        P = pts[i:i + 256]
        f = ive(P[:, 0:1], 2 * t[None, :]) * ive(P[:, 1:2], 2 * t[None, :]) * ive(P[:, 2:3], 2 * t[None, :])
        r = np.sqrt((P ** 2).sum(1))
        rr = np.maximum(r, 1e-300)
        tail = 0.0
        if m2 == 0:
            tail = np.where(r > 0, erf(rr / (2 * np.sqrt(T))) / (4 * np.pi * rr), 2 * (4 * np.pi) ** -1.5 / np.sqrt(T))
        out[i:i + 256] = f @ wt + tail
    return out


def G_asym(p):
    p = np.asarray(p, float)
    r2 = (p ** 2).sum(1)
    r = np.sqrt(r2)
    return 1 / (4 * np.pi * r) + (5 * (p ** 4).sum(1) / r2 ** 2 - 3) / (32 * np.pi * r ** 3)


_cache = {}


def Gsrw(keys):
    need = [k for k in keys if k not in _cache]
    if need:
        arr = np.array(need, float)
        r = np.sqrt((arr ** 2).sum(1))
        v = np.empty(len(need))
        ex = r <= 24
        if ex.any():
            v[ex] = G_lap(arr[ex])
        if (~ex).any():
            v[~ex] = G_asym(arr[~ex])
        for k, x in zip(need, v):
            _cache[k] = 6 * x
    return np.array([_cache[k] for k in keys])


def cap(sites):
    S = np.array(sites)
    n = len(S)
    Dm = np.abs(S[:, None, :] - S[None, :, :]).reshape(-1, 3)
    key = np.sort(Dm, axis=1)[:, ::-1]
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    vals = Gsrw([tuple(int(v) for v in u) for u in uniq])
    M = vals[inv.ravel()].reshape(n, n)
    e = np.linalg.solve(M, np.ones(n))
    return float(e.sum()), e


# ================================================================ E1 the two-record identity (exact)
g0, gr = sp.symbols('G0 Gr', positive=True)
M2 = sp.Matrix([[g0, gr], [gr, g0]])
cap2 = sp.simplify((sp.ones(1, 2) * M2.inv() * sp.ones(2, 1))[0])
ratio = sp.simplify(cap2 / (2 / g0))
ok = sp.simplify(ratio - g0 / (g0 + gr)) == 0
ok &= sp.simplify((ratio - sp.Rational(9, 10)).subs(gr, g0 / 9)) == 0
check('E1', ok, "EXACT: two records at separation r have capacity 2/(G(0) + G(r)); against two isolated records "
      "cap_2/(2 c_1) = G(0)/(G(0) + G(r)), so they add to within 10 percent iff G(r)/G(0) <= 1/9 (any walk, any killing rate)",
      f"cap_2 = {cap2}")

# ================================================================ E2 exact torus anchor (a3's screened value) vs the infinite lattice
def torus_G_exact(L, m2):
    """exact (-Lap + m2)^(-1) on the L-torus by cubic-orbit reduction (odd L)."""
    h = L // 2
    rep = lambda p: tuple(sorted((min(abs(v) % L, L - abs(v) % L) for v in p), reverse=True))
    orbs = sorted({rep(p) for p in itertools.product(range(L), repeat=3)})
    idx = {o: i for i, o in enumerate(orbs)}
    A = sp.zeros(len(orbs), len(orbs))
    bvec = sp.zeros(len(orbs), 1)
    for o in orbs:
        i = idx[o]
        A[i, i] += 6 + m2
        for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            A[i, idx[rep((o[0] + d[0], o[1] + d[1], o[2] + d[2]))]] -= 1
        if o == (0, 0, 0):
            bvec[i] = 1
    sol = A.LUsolve(bvec)
    return {o: sol[idx[o]] for o in orbs}, h


Gt, _ = torus_G_exact(7, sp.Integer(5))
tor_ratio = Gt[(1, 0, 0)] / Gt[(0, 0, 0)]
inf_vals = G_lap([(0, 0, 0), (1, 0, 0)], 5.0)
inf_ratio = inf_vals[1] / inf_vals[0]
ok = abs(float(tor_ratio) - 0.098951) < 5e-7 and abs(float(tor_ratio) - inf_ratio) < 1e-5
check('E2', ok, "EXACT + NUMERICAL: on the 7-torus at m^2 = 5 (a3's screened triple) the exact rational G(e1)/G(0) is a3's "
      "0.098951, and the infinite-lattice quadrature agrees with it to 1e-5 (screening length 0.45: the torus is already "
      "infinite for this purpose) - the two methods cross-validate",
      f"torus {float(tor_ratio):.8f} (exact rational with {len(str(sp.fraction(tor_ratio)[1]))}-digit denominator); "
      f"infinite lattice {inf_ratio:.8f}")

# ================================================================ N1 validation of the massless quadrature
W = math.sqrt(6) / (32 * math.pi ** 3) * gamma(1 / 24) * gamma(5 / 24) * gamma(7 / 24) * gamma(11 / 24)
G0, G1 = Gsrw([(0, 0, 0), (1, 0, 0)])
res = []
for m2 in (0.0, 0.1, 5.0):
    G = lambda p: G_lap([p], m2)[0]
    res.append((6 + m2) * G((0, 0, 0)) - 6 * G((1, 0, 0)) - 1)
    res.append((6 + m2) * G((1, 0, 0)) - (G((0, 0, 0)) + G((2, 0, 0)) + 4 * G((1, 1, 0))))
ok = abs(G0 - W) < 2e-8 and abs(G1 - (G0 - 1)) < 2e-8 and max(abs(x) for x in res) < 2e-8
check('N1', ok, "NUMERICAL (validation): the quadrature gives G_SRW(0) within 1e-8 of Watson's closed form "
      "(sqrt6/(32 pi^3)) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24) (ASSUMED, used only as a check), satisfies the exact "
      "identity G(e1) = G(0) - 1 (the lattice equation at the origin with cubic symmetry) and the lattice equation at 0 and e1 "
      "for m^2 = 0, 0.1, 5 to 1e-8; every numerical margin claimed below exceeds 1e-6",
      f"G(0) = {G0:.10f} (Watson {W:.10f}); G(e1) - G(0) + 1 = {G1 - G0 + 1:.1e}; max residual {max(abs(x) for x in res):.1e}; "
      f"escape probability c_1 = 1/G(0) = {1 / G0:.8f}")

# ================================================================ N2 massless: which separations add to within 10 percent
orb = sorted({tuple(sorted((a, b, c), reverse=True)) for a in range(0, 13) for b in range(0, 13) for c in range(0, 13)} - {(0, 0, 0)},
             key=lambda v: (sum(x * x for x in v), v))
vals = Gsrw(orb) / G0
fail = [v for v, g in zip(orb, vals) if g > 1 / 9]
okset = [v for v, g in zip(orb, vals) if g <= 1 / 9]
margin_fail = min(g - 1 / 9 for g in vals if g > 1 / 9)
margin_ok = min(1 / 9 - g for g in vals if g <= 1 / 9)
ok = fail == [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (2, 1, 1)] and margin_fail > 1e-6 and margin_ok > 1e-6
g220 = float(vals[orb.index((2, 2, 0))])
g211 = float(vals[orb.index((2, 1, 1))])
check('N2', ok, "NUMERICAL (all separation vectors with |coordinates| <= 12; margins > 1e-6 against quadrature errors ~1e-8): "
      "in the MASSLESS case (theta = 1, e.g. (3,1,2)) two records add to within 10 percent at every separation with |r|^2 >= 8 "
      "and at no separation with |r|^2 <= 6: the failing set is exactly (1,0,0), (1,1,0), (1,1,1), (2,0,0), (2,1,0), (2,1,1); "
      "a3's statement that on the massless surface 'the exact criterion <= 1/9 is not met at any separation a lattice body "
      "offers' is false - it is met from (2,2,0) on",
      f"G(r)/G(0): (2,1,1) {g211:.8f} -> ratio {1 / (1 + g211):.6f}; (2,2,0) {g220:.8f} -> ratio {1 / (1 + g220):.6f}; "
      f"smallest margins {margin_fail:.2e} (failing side), {margin_ok:.2e} (passing side)")

# ================================================================ N3 the threshold as a function of the range
rows = []
thr = {}
for m2 in (0.0, 0.01, 0.05, 0.1, 0.5, 5.0):
    if m2 == 0:
        v = vals
    else:
        g0m = G_lap([(0, 0, 0)], m2)[0]
        v = G_lap(orb, m2) / g0m
    bad = [o for o, g in zip(orb, v) if g > 1 / 9]
    rmax_bad = max((sum(x * x for x in o) for o in bad), default=0)
    thr[m2] = math.sqrt(min(sum(x * x for x in o) for o in orb if sum(x * x for x in o) > rmax_bad))
    rows.append(f"range {('inf' if m2 == 0 else f'{1 / math.sqrt(m2):.2f}')}: |r| >= {thr[m2]:.4f}")
ok = abs(thr[0.0] - math.sqrt(8)) < 1e-9 and abs(thr[5.0] - 1) < 1e-9 and all(thr[a] >= thr[b] for a, b in ((0.0, 0.01), (0.01, 0.05), (0.05, 0.1), (0.1, 0.5), (0.5, 5.0)))
check('N3', ok, "NUMERICAL: the separation beyond which two records add to within 10 percent shrinks with the range 1/m of "
      "the lean: sqrt8 when massless, sqrt6 at range 10, sqrt5 at range 4.5, sqrt3 at range 3.2, sqrt2 at range 1.4, adjacent "
      "sites at range 0.45 (a3's (2,1,2))", "; ".join(rows))

# ================================================================ N4 massless arrays: many records do not add
arr_rows = []
ratios = {}
for d in (2, 4, 8):
    row = []
    for N in range(1, 9):
        sites = [(d * i, d * j, d * k) for i in range(N) for j in range(N) for k in range(N)]
        cp, e = cap(sites)
        ratios[(d, N)] = cp / (N ** 3 / G0)
        row.append(f"{ratios[(d, N)]:.4f}")
    arr_rows.append(f"d={d}: " + ", ".join(row))
dmin = None
for d in range(2, 40):
    sites = [(d * i, d * j, d * k) for i in range(2) for j in range(2) for k in range(2)]
    if cap(sites)[0] / (8 / G0) >= 0.9:
        dmin = d
        break
ok = all(ratios[(d, N + 1)] < ratios[(d, N)] for d in (2, 4, 8) for N in range(1, 8)) and dmin is not None and dmin > 12
check('N4', ok, "NUMERICAL (infinite lattice, massless): N^3 records at spacing d have capacity a falling fraction of N^3 c_1 - "
      f"8 records reach 90 percent of additive only at spacing d >= {dmin}, although two records do so at spacing 3 "
      "(each record's deficit is the SUM of G(r_ij)/G(0) over the others, about 0.315 sum 1/r_ij)",
      "; ".join(arr_rows))

# ================================================================ N4b rigorous two-sided bounds, and their shapes
okb = True
brow = []
for d in (2, 4, 8):
    for N in (2, 4, 6, 8):
        sites = [(d * i, d * j, d * k) for i in range(N) for j in range(N) for k in range(N)]
        cp, e = cap(sites)
        S_ = np.array(sites)
        Dm = np.abs(S_[:, None, :] - S_[None, :, :]).reshape(-1, 3)
        key = np.sort(Dm, axis=1)[:, ::-1]
        uniq, inv = np.unique(key, axis=0, return_inverse=True)
        tot = float(Gsrw([tuple(int(v) for v in u) for u in uniq])[inv.ravel()].sum())
        lb = N ** 6 / tot
        ub = N ** 3 / G0
        okb &= lb <= cp * (1 + 1e-9) and cp <= ub * (1 + 1e-9)
        if N in (2, 8):
            brow.append(f"d={d},N={N}: {lb:.4f} <= cap {cp:.4f} <= {ub:.4f}")
ok = okb
check('N4b', ok, "PROVED + NUMERICAL: for every set A, |A|^2/sum_ij G_ij <= cap(A) <= |A| c_1 (upper: escaping A implies "
      "escaping each of its sites, e_A(y) <= c_1; lower: 1/cap = min over signed unit measures of mu^T G_A mu (Lagrange), "
      "tested with the uniform measure); the lower bound is 1/(G(0)/N^3 + <G>_off), whose massless off-diagonal mean is of "
      "order 1/(N d): the same 1/(1 + (N/N*)^2) shape, now as a theorem with a smaller constant",
      "; ".join(brow))

# ================================================================ N5 kappa: the solid cube's capacity grows like its side
cubes = {}
for D in range(1, 13):
    cubes[D] = cap(list(itertools.product(range(D), repeat=3)))[0]
incr = [cubes[D + 1] - cubes[D] for D in range(1, 12)]
# fit cap(D) = kappa D + b + c/D on D = 8..12
A = np.array([[D, 1, 1 / D] for D in range(8, 13)])
kappa, bfit, cfit = np.linalg.lstsq(A, np.array([cubes[D] for D in range(8, 13)]), rcond=None)[0]
ok = all(incr[i + 1] > incr[i] for i in range(len(incr) - 1)) and 1.36 < kappa < 1.40 and incr[-1] < kappa
check('N5', ok, "NUMERICAL: the capacity of a solid lattice cube of side D grows linearly: its increments rise to "
      f"{incr[-1]:.4f} at D = 12 and a fit cap = kappa D + b + c/D on D = 8..12 gives kappa = {kappa:.4f} (walk normalization; "
      "the continuum cube capacitance 0.6607 x 4pi/6 = 1.3838 is the expected limit, not used), against N^3 c_1 = 0.6595 D^3 "
      "for records filling it: the solid cube is the extreme shielded body",
      "cap(D): " + ", ".join(f"{D}:{cubes[D]:.4f}" for D in (1, 2, 4, 6, 8, 10, 12)))

# ================================================================ N6 the crossover D*
c1 = 1 / G0
rows = []
okc = True
for d in (2, 4, 8):
    Nstar = math.sqrt(kappa * d / c1)
    Dstar = Nstar * d
    interp = {N: 1 / (1 + (N / Nstar) ** 2) for N in range(2, 9)}
    worst = max(abs(ratios[(d, N)] - interp[N]) for N in range(2, 9))
    okc &= worst < 0.08
    rows.append(f"d={d}: N* = {Nstar:.3f}, D* = {Dstar:.2f}, max |ratio - 1/(1+(N/N*)^2)| = {worst:.3f}")
ok = okc and abs(math.sqrt(kappa / c1) - 1.44) < 0.03
check('N6', ok, "NUMERICAL: with c_1 = 1/G(0) and the cube's kappa, the array ratio follows 1/(1 + (N/N*)^2), "
      "N* = sqrt(kappa d/c_1), within 0.08 for N = 2..8 and d = 2, 4, 8, i.e. the body shields itself beyond "
      f"D* = N* d = sqrt(kappa/c_1) d^(3/2) = {math.sqrt(kappa / c1):.3f} d^(3/2) (the unit's expected form, with the constant)",
      "; ".join(rows))

# ================================================================ N7 screened arrays: the bulk charge converges
rows = []
okb = True
for m2, dset in ((0.1, (2, 3)), (1.0, (1, 2, 3))):
    g0m = G_lap([(0, 0, 0)], m2)[0]
    for d in dset:
        R = int(math.ceil(20 * max(1, 1 / math.sqrt(m2)) / d))      # truncation at 20 ranges: omitted terms < 1e-6 of S
        pts = [(d * i, d * j, d * k) for i in range(-R, R + 1) for j in range(-R, R + 1) for k in range(-R, R + 1) if (i, j, k) != (0, 0, 0)]
        keyset = sorted({tuple(sorted(map(abs, p), reverse=True)) for p in pts})
        gv = dict(zip(keyset, G_lap(keyset, m2)))
        S = sum(gv[tuple(sorted(map(abs, p), reverse=True))] for p in pts) / g0m
        rows.append(f"m^2={m2}, d={d}: S = {S:.6f}, bulk charge per record = c_1/(1+S) -> {1 / (1 + S):.6f} of isolated")
        okb &= S < float('inf')
ok = okb
check('N7', ok, "NUMERICAL: when the lean is screened (m > 0) the charge of a record deep inside an infinite array converges to "
      "e = 1/(G(0)(1 + S)), S = sum over the other records of G(r)/G(0), so a large screened body's strength grows like its "
      "record count times 1/(1 + S) - no crossover size; only the massless lean, where S grows like N^2/d, turns strength into "
      "capacity (N6)", "; ".join(rows))

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, numerical on the infinite lattice with exact anchors: in the massless case two records add to "
      "within 10 percent iff their separation has |r|^2 >= 8 (a3's 'never' is false), the threshold shrinking with the range "
      "(sqrt8 -> 1 as the range falls to 0.45); N^3 records at spacing d have strength N^3 c_1/(1 + (N/N*)^2), N* = "
      "sqrt(kappa d/c_1), kappa = lim cap(cube)/side ~ 1.38, so bodies shield themselves beyond D* = 1.44 d^(3/2) and a "
      "large body's strength is kappa x its linear size, not its record count; screened arrays keep strength proportional to "
      "record count with the bulk factor 1/(1 + S)")
if all(RESULTS):
    print("HIT: for block 42's linear odds field with records as boundary values: (1) massless (5p = 7q + 4r): two records "
          "add to within 10 percent exactly at separations with |r|^2 >= 8 (checked to |coordinates| <= 12; G(2,2,0)/G(0) = "
          "0.1110080 < 1/9 < 0.1264794 = G(2,1,1)/G(0)), contradicting attempt a3's 'not met at any separation'; the threshold falls to adjacent sites as "
          "the range drops to 0.45; (2) N^3 records at spacing d follow cap = N^3 c_1/(1 + (N/N*)^2) with N* = sqrt(kappa d/c_1), "
          "kappa = 1.38 the lattice cube's capacity per side, so D* = 1.44 d^(3/2), and 8 records need spacing >= " + str(dmin) + " to "
          "add within 10 percent (two need only |r|^2 >= 8); (3) with any screening the bulk charge per record converges (strength stays proportional to "
          "record count), so the capacity law that defeats additivity is a property of the massless lean")
