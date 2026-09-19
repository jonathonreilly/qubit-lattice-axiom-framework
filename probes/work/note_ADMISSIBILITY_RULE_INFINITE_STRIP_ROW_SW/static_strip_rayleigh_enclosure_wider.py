#!/usr/bin/env python3
"""J:note falsifier for ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.

Falsifiers implemented: "the enclosure of s_inf ... containing p/(p + q + 4r)" and the displayed enclosures themselves (Theorem F4,
F5), re-derived with machinery disjoint from the runner and carried beyond the note's widths (the note executes W = 2, 3).

The runner encloses s_inf through the characteristic polynomial of the orbit quotient Q, Sturm isolation of the Perron root and exact
arithmetic in Q(lambda_1). Here, instead, a variational certificate:
  - T(rho, rho') = V(rho, rho') A(rho') is self-adjoint for the weighted inner product <u, v>_A = sum_rho A(rho) u(rho) v(rho) (V is
    symmetric), so the orbit quotient Q is self-adjoint for the weights omega_O = |O| A_O and all its eigenvalues are real; the static
    centre-row law w ~ A rho_1^2 makes s_inf = <y, Pibar y>_omega / <y, y>_omega for the Perron vector y, with Pibar the orbit-averaged
    indicator of the pair [rho_0 = rho_1] (diagonal, entries in [0, 1]);
  - an approximate Perron vector x (float power iteration, rounded to integers) gives, in exact integer/rational arithmetic, the
    Rayleigh quotient theta <= lambda_1, the residual eps = ||Q x - theta x|| / ||x||, the trace bound |lambda_i| <= mu =
    sqrt(tr Q^2 - theta^2) for every i >= 2, hence the gap delta >= theta - mu, the angle bound sin(x, y) <= eps / delta
    (Davis-Kahan for one vector), and |<x, Pibar x> - <y, Pibar y>| <= 2 s + s^2 with s = eps / delta: a rigorous enclosure of s_inf.
Widths W = 2, 3 are compared with the note's printed enclosures; W = 4 and W = 5 (1296 and 7776 row states) are beyond the note, with
both horizontal pair classes at W = 4, 5 (edge pair (0,1) and the central pair). Triples (3, 1, 2) and (5, 2, 4).
HIT if an enclosure at W = 2 or 3 misses the note's printed value or contains the formation value p/(p + q + 4r).
"""
from __future__ import annotations

import itertools
from fractions import Fraction
from math import isqrt

import numpy as np

AXIS = [0, 0, 1, 1, 2, 2]
SIGN = [1, -1, 1, -1, 1, -1]


def phi_matrix(p, q, r):
    M = np.zeros((6, 6), dtype=np.int64)
    for a in range(6):
        for b in range(6):
            M[a, b] = p if a == b else (q if AXIS[a] == AXIS[b] else r)
    return M


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            Mx = np.zeros((3, 3), int)
            for a in range(3):
                Mx[perm[a], a] = signs[a]
            if round(np.linalg.det(Mx)) != 1:
                continue
            m = []
            for d in range(6):
                a, s = AXIS[d], SIGN[d]
                na, ns = perm[a], s * signs[a]
                m.append(2 * na + (0 if ns == 1 else 1))
            out.append(m)
    return out


def sqrt_up(fr: Fraction, scale=10 ** 60) -> Fraction:
    n = fr.numerator * scale * scale // fr.denominator + 1
    return Fraction(isqrt(n) + 1, scale)


def analyse(W, trip, pairs):
    p, q, r = trip
    phi = phi_matrix(p, q, r)
    rows = np.array(list(itertools.product(range(6), repeat=W)), dtype=np.int64)
    n = len(rows)
    code = lambda arr: sum(int(arr[j]) * 6 ** (W - 1 - j) for j in range(W))
    A = np.ones(n, dtype=np.int64)
    for j in range(W - 1):
        A *= phi[rows[:, j], rows[:, j + 1]]
    rots = rotations()
    assert len(rots) == 24
    rep = np.full(n, -1)
    orbit_of = {}
    orbits = []
    for i in range(n):
        if rep[i] >= 0:
            continue
        members = set()
        for m in rots:
            img = [m[x] for x in rows[i]]
            for g in (img, img[::-1]):
                members.add(code(g))
        oid = len(orbits)
        orbits.append(sorted(members))
        for c in members:
            rep[c] = oid
    k = len(orbits)
    size = np.array([len(o) for o in orbits], dtype=object)
    A_O = [int(A[o[0]]) for o in orbits]
    assert all(int(A[c]) == A_O[i] for i, o in enumerate(orbits) for c in o)
    Q = np.zeros((k, k), dtype=object)
    for i, o in enumerate(orbits):
        rho = rows[o[0]]
        Vcol = np.ones(n, dtype=np.int64)
        for j in range(W):
            Vcol *= phi[rho[j], rows[:, j]]
        contrib = Vcol * A
        sums = np.zeros(k, dtype=object)
        np.add.at(sums, rep, contrib.astype(object))
        Q[i] = sums
    # symmetry check of the weighted form: omega_O Q[O, O'] = omega_O' Q[O', O]
    omega = [int(size[i]) * A_O[i] for i in range(k)]
    selfadj = all(omega[i] * Q[i, j] == omega[j] * Q[j, i] for i in range(k) for j in range(k))
    Qf = np.array(Q, dtype=float)
    x = np.ones(k)
    for _ in range(3000):
        y = Qf @ x
        x = y / np.linalg.norm(y)
    xi = [int(round(v * 2 ** 52)) for v in x / x.max()]
    Qx = [sum(Q[i, j] * xi[j] for j in range(k)) for i in range(k)]
    nx = sum(omega[i] * xi[i] * xi[i] for i in range(k))
    theta = Fraction(sum(omega[i] * xi[i] * Qx[i] for i in range(k)), nx)
    res2 = sum(omega[i] * (theta.denominator * Qx[i] - theta.numerator * xi[i]) ** 2 for i in range(k))
    eps2 = Fraction(res2, theta.denominator ** 2 * nx)
    trQ2 = sum(Q[i, j] * Q[j, i] for i in range(k) for j in range(k))
    mu = sqrt_up(Fraction(trQ2) - theta * theta)
    delta = theta - mu
    assert delta > 0
    s = sqrt_up(eps2) / delta
    width = 2 * s + s * s
    out = {}
    for name, (a, b) in pairs.items():
        Pbar = []
        for o in orbits:
            Pbar.append(Fraction(sum(1 for c in o if rows[c][a] == rows[c][b]), len(o)))
        sx = Fraction(sum(omega[i] * xi[i] * xi[i] * Pbar[i] for i in range(k)), nx)
        out[name] = (sx - width, sx + width)
    return {"rows": n, "orbits": k, "selfadjoint": selfadj, "theta": theta, "mu_over_theta": float(mu / theta), "sin_bound": s,
            "enclosures": out}


def dec(fr: Fraction, digits: int, up: bool) -> str:
    scaled = fr * 10 ** digits
    v = scaled.numerator // scaled.denominator + (1 if up and scaled.denominator != 1 else 0)
    s = str(v).rjust(digits + 1, "0")
    return s[:-digits] + "." + s[-digits:]


def main():
    note = {(2, (3, 1, 2)): (Fraction("0.255943088901618766"), Fraction("0.255943088901618767")),
            (2, (5, 2, 4)): (Fraction("0.219874176124090031"), Fraction("0.219874176124090032")),
            (3, (3, 1, 2)): (Fraction("0.2561109872857786908612"), Fraction("0.2561109872857786908613")),
            (3, (5, 2, 4)): (Fraction("0.2199151616870197815075"), Fraction("0.2199151616870197815076"))}
    fails = []
    results = {}
    for W in (2, 3, 4, 5):
        pairs = {"(0,1)": (0, 1)}
        if W >= 4:
            pairs["central"] = ((W - 1) // 2, (W - 1) // 2 + 1)
        for trip in ((3, 1, 2), (5, 2, 4)):
            res = analyse(W, trip, pairs)
            formation = Fraction(trip[0], trip[0] + trip[1] + 4 * trip[2])
            results[(W, trip)] = res
            encl = res["enclosures"]
            txt = "; ".join(f"pair {nm}: s_inf in [{dec(lo, 20, False)}, {dec(hi, 20, True)}], contains formation value {formation}: "
                            f"{lo <= formation <= hi}" for nm, (lo, hi) in encl.items())
            extra = ""
            if (W, trip) in note:
                lo, hi = encl["(0,1)"]
                nlo, nhi = note[(W, trip)]
                ok = lo <= nhi and nlo <= hi
                extra = f"; meets the note's printed interval [{float(nlo):.18f}.., {float(nhi):.18f}..]: {ok}"
                if not ok or lo <= formation <= hi:
                    fails.append((W, trip))
            print(f"W = {W}, (p,q,r) = {trip}: {res['rows']} row states, {res['orbits']} orbits, weighted self-adjointness "
                  f"{res['selfadjoint']}, theta = {float(res['theta']):.12g}, second-eigenvalue bound mu/theta <= {res['mu_over_theta']:.4f}, "
                  f"angle bound {float(res['sin_bound']):.2e}; {txt}{extra}")
    if fails:
        print(f"HIT: the static enclosure disagrees with the note or contains the formation value at {fails}")
    sep = all(not (lo <= Fraction(t[0], t[0] + t[1] + 4 * t[2]) <= hi) for (W, t), res in results.items() for lo, hi in res["enclosures"].values())
    s01 = {k: float(sum(v["enclosures"]["(0,1)"]) / 2) for k, v in results.items()}
    print(f"SUMMARY: a variational certificate (weighted self-adjointness, Rayleigh quotient, trace bound on the second eigenvalue, "
          f"Davis-Kahan angle) encloses the static centre-row pair-parallel probability with angle bounds below 1e-12; at W = 2, 3 the "
          f"enclosures contain the note's printed values and exclude 1/4 and 5/23 ({not fails}); beyond the note, at W = 4 and 5 every "
          f"enclosure (edge and central pairs) also excludes the formation value ({sep}); edge-pair midpoints by width: "
          + ", ".join(f"W={W} {t}: {s01[(W, t)]:.10f}" for (W, t) in sorted(s01)))


if __name__ == "__main__":
    main()
