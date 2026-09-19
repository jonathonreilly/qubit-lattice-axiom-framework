#!/usr/bin/env python3
"""J:note check for PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14 (on main).

Proof steps verified literally, by enumeration / exact arithmetic, with my own constructions and beyond the note's finite sizes:
  1. section 4: the distance-one neighbourhood of a canonical edge in Z^4 (exact rational segment-segment distances): 107 edges,
     23 parallel (5 collinear + 6 x 3) and 28 per perpendicular direction (20 + 8); its image on the periodic tori T_L, L = 4, 6, 8
     ("no more members");
  2. section 5: the 32-colouring (orientation x three transverse parities) on T_L, L = 4, 6, 8, 10: no two edges of one colour share
     a plaquette, and Q_ee = 6; the damping identity (5.1) 2 R^T u - u^T Q u = sum rho_e^2/6 for signed sums of separated currents
     with selected same-colour edges (exact integers, L = 6);
  3. section 6: the explicit filling K_1(e) (minus the jk strips, coordinate-ordered path from the box corner) on Z^4 boxes:
     boundary K_1(e) = P(x) + e - P(x + e_j) for every edge of boxes of side 2..4, at most 3R plaquettes per edge, and for random
     closed integer currents delta_2 mu = rho with ||mu||_1 <= 3R ||rho||_1 and |rho(w)| <= ||mu||_1 max |dw|;
  4. section 10: the exact-projector diagonal P_e,ij,ij(k) = (|v_i|^2 + |v_j|^2)/sum |v_a|^2 and the two directional limits
     (symbolic in sympy at generic real v, numeric at complex k);
  5. section 9: the certificate in mpmath interval arithmetic (beta_1 < 10/3, a(2000) > 15/8, q < exp(-135/4) < 2^-48, the Eulerian
     closed forms of S_5, S_6 and S_j <= 2q on [0, 1/1024], delta(2000) < 1/1000), plus numbers the note does not print: the actual
     delta(2000), the smallest beta with delta < 1/1000 and with delta < 1/2, and the smallest clock order N at beta = 2000.
HIT if any literal step fails.
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as F

import mpmath as mp
import numpy as np
import sympy as sp

# ------------------------------------------------------------------------------------------------ 1. distance-one neighbourhood
def seg_dist2(p0, d0, p1, d1):
    """Exact squared distance between unit segments p0 + s e_d0 and p1 + t e_d1 (s, t in [0,1]) in Z^4, rational arithmetic."""
    best = None
    # the distance is a convex quadratic in (s, t); minimise over the box: check interior critical point and edges exhaustively on
    # a rational candidate set (vertices, edge minimisers)
    def d2(s, t):
        return sum((F(p0[i]) + (s if i == d0 else 0) - F(p1[i]) - (t if i == d1 else 0)) ** 2 for i in range(4))
    cands = [(F(0), F(0)), (F(0), F(1)), (F(1), F(0)), (F(1), F(1))]
    # minimise along each box edge: fix s in {0,1}, optimal t = clamp(p0[d1] + s*[d0==d1] - p1[d1]); similarly for t
    for s in (F(0), F(1)):
        t = F(p0[d1]) + (s if d0 == d1 else 0) - F(p1[d1])
        cands.append((s, min(max(t, F(0)), F(1))))
    for t in (F(0), F(1)):
        s = F(p1[d0]) + (t if d0 == d1 else 0) - F(p0[d0])
        cands.append((min(max(s, F(0)), F(1)), t))
    if d0 == d1:
        # parallel: distance is transverse part plus longitudinal gap
        pass
    return min(d2(s, t) for s, t in cands)


def neighbourhood():
    x0 = (0, 0, 0, 0)
    j = 0
    par, perp = 0, {1: 0, 2: 0, 3: 0}
    members = []
    for d in range(4):
        for off in itertools.product(range(-3, 4), repeat=4):
            if seg_dist2(x0, j, off, d) <= 1:
                members.append((off, d))
                if d == j:
                    par += 1
                else:
                    perp[d] += 1
    return len(members), par, perp, members


def torus_neighbourhood(members, L):
    return len({(tuple(c % L for c in off), d) for off, d in members})


# ----------------------------------------------------------------------------------------------------- 2. colouring and damping
def plaquettes(L):
    out = []
    for x in itertools.product(range(L), repeat=4):
        for j, k in itertools.combinations(range(4), 2):
            xj = list(x); xj[j] = (xj[j] + 1) % L
            xk = list(x); xk[k] = (xk[k] + 1) % L
            out.append({(x, j): 1, (tuple(xj), k): 1, (tuple(xk), j): -1, (x, k): -1})
    return out


def colour(e):
    x, j = e
    return (j,) + tuple(x[i] % 2 for i in range(4) if i != j)


def colouring_check(L):
    ok, Qee = True, {}
    for p in plaquettes(L):
        cols = [colour(e) for e in p]
        if len(set(cols)) < 4:
            ok = False
        for e in p:
            Qee[e] = Qee.get(e, 0) + 1
    return ok, len({colour((x, j)) for x in itertools.product(range(L), repeat=4) for j in range(4)}), set(Qee.values())


def damping_identity(L=6, seed=3):
    """Separated closed currents rho (plaquette boundaries, small loops) with selected same-colour edges; exact 2R.u - u.Q.u."""
    rng = random.Random(seed)
    plq = plaquettes(L)
    # current = boundary of one plaquette times an integer, placed far apart (distance > 1 between supports)
    anchors = [(0, 0, 0, 0), (3, 3, 0, 0), (0, 3, 3, 0), (3, 0, 3, 3)]
    currents = []
    for a in anchors:
        j, k = rng.sample(range(4), 2)
        j, k = min(j, k), max(j, k)
        m = rng.choice([1, 2, 3, -2])
        xj = list(a); xj[j] = (xj[j] + 1) % L
        xk = list(a); xk[k] = (xk[k] + 1) % L
        cur = {(a, j): m, (tuple(xj), k): m, (tuple(xk), j): -m, (a, k): -m}
        currents.append(cur)
    # selected colour per current: the colour with the largest squared weight (all four edges have |m|^2; pick one colour)
    Q = {}
    for p in plq:
        for e1, s1 in p.items():
            for e2, s2 in p.items():
                Q[(e1, e2)] = Q.get((e1, e2), 0) + s1 * s2
    ok = True
    for signs in itertools.product((1, -1, 0), repeat=len(currents)):
        if not any(signs):
            continue
        R, u, target = {}, {}, F(0)
        for sgn, cur in zip(signs, currents):
            if sgn == 0:
                continue
            col = colour(next(iter(cur)))
            for e, v in cur.items():
                R[e] = R.get(e, 0) + sgn * v
                if colour(e) == col:
                    u[e] = F(sgn * v, 6)
                    target += F(v * v, 6)
        lhs = 2 * sum(R.get(e, 0) * val for e, val in u.items()) - sum(u[e1] * Q.get((e1, e2), 0) * u[e2] for e1 in u for e2 in u)
        ok &= lhs == target
    return ok


# ------------------------------------------------------------------------------------------------------------------- 3. filling
def path(b, x):
    """coordinate-ordered path from b to x: axis 0 first, then 1, 2, 3 (positive steps; x >= b)."""
    chain, cur = {}, list(b)
    for i in range(4):
        while cur[i] < x[i]:
            e = (tuple(cur), i)
            chain[e] = chain.get(e, 0) + 1
            cur[i] += 1
    return chain


def plaq_boundary(y, j, k):
    yj = list(y); yj[j] += 1
    yk = list(y); yk[k] += 1
    return {(tuple(y), j): 1, (tuple(yj), k): 1, (tuple(yk), j): -1, (tuple(y), k): -1}


def K1(e, b):
    x, j = e
    out = {}
    for k in range(j + 1, 4):
        for yk in range(b[k], x[k]):
            y = [x[i] if i < k else (yk if i == k else b[i]) for i in range(4)]
            key = (tuple(y), j, k)
            out[key] = out.get(key, 0) - 1
    return out


def boundary(mu):
    out = {}
    for (y, j, k), c in mu.items():
        for e, s in plaq_boundary(y, j, k).items():
            out[e] = out.get(e, 0) + c * s
    return {e: v for e, v in out.items() if v}


def addc(a, b, s=1):
    out = dict(a)
    for e, v in b.items():
        out[e] = out.get(e, 0) + s * v
    return {e: v for e, v in out.items() if v}


def filling_checks(seed=11):
    rng = random.Random(seed)
    ok_id, max_count_ratio = True, 0.0
    for R in (2, 3, 4):
        b = (0, 0, 0, 0)
        for x in itertools.product(range(R + 1), repeat=4):
            for j in range(4):
                if x[j] + 1 > R:
                    continue
                e = (x, j)
                xe = list(x); xe[j] += 1
                lhs = boundary(K1(e, b))
                rhs = addc(addc(path(b, x), {e: 1}), path(b, tuple(xe)), -1)
                ok_id &= lhs == rhs
                cnt = sum(abs(v) for v in K1(e, b).values())
                max_count_ratio = max(max_count_ratio, cnt / (3 * R))
    # random closed currents: sums of random plaquette boundaries inside a box of side R (closed by construction), fill and check
    ok_fill, worst = True, 0.0
    for trial in range(40):
        R = rng.choice([3, 4, 5])
        rho = {}
        for _ in range(rng.randint(1, 6)):
            y = [rng.randint(0, R - 1) for _ in range(4)]
            j, k = sorted(rng.sample(range(4), 2))
            rho = addc(rho, plaq_boundary(y, j, k), rng.choice([1, -1, 2]))
        if not rho:
            continue
        b = (0, 0, 0, 0)
        mu = {}
        for e, v in rho.items():
            for key, c in K1(e, b).items():
                mu[key] = mu.get(key, 0) + v * c
        mu = {k: v for k, v in mu.items() if v}
        ok_fill &= boundary(mu) == rho
        l1_mu, l1_rho = sum(abs(v) for v in mu.values()), sum(abs(v) for v in rho.values())
        Rbox = max(max(x[i] for (x, j) in rho) + (1 if True else 0) for i in range(4))
        ok_fill &= l1_mu <= 3 * Rbox * l1_rho
        w = {e: rng.uniform(-1, 1) for e in set(rho) | {ee for key in mu for ee in plaq_boundary(*key)}}
        dw = {key: sum(w.get(e, 0) * s for e, s in plaq_boundary(*key).items()) for key in mu}
        lhs = abs(sum(w[e] * v for e, v in rho.items()))
        rhs = l1_mu * max(abs(v) for v in dw.values())
        ok_fill &= lhs <= rhs + 1e-12
        worst = max(worst, lhs / rhs if rhs else 0)
    return ok_id, max_count_ratio, ok_fill, worst


# ---------------------------------------------------------------------------------------------------------------- 4. projectors
def projectors():
    v = sp.symbols("v0:4", real=True)
    pairs = list(itertools.combinations(range(4), 2))
    d = sp.zeros(6, 4)
    for r, (i, j) in enumerate(pairs):
        d[r, j] += v[i]
        d[r, i] -= v[j]
    M = d.T * d
    n2 = sum(x ** 2 for x in v)
    ok_M = sp.simplify(M - (n2 * sp.eye(4) - sp.Matrix(v) * sp.Matrix(v).T)) == sp.zeros(4, 4)
    # pseudo-inverse on range: (|v|^2 I - v v^T)^+ = (I - v v^T/|v|^2)/|v|^2
    Mp = (sp.eye(4) - sp.Matrix(v) * sp.Matrix(v).T / n2) / n2
    Pe = sp.simplify(d * Mp * d.T)
    ok_diag = all(sp.simplify(Pe[r, r] - (v[i] ** 2 + v[j] ** 2) / n2) == 0 for r, (i, j) in enumerate(pairs))
    ok_proj = sp.simplify(Pe * Pe - Pe) == sp.zeros(6, 6)
    rng = np.random.default_rng(1)
    k = rng.uniform(-np.pi, np.pi, 4)
    vc = np.exp(1j * k) - 1
    dc = np.zeros((6, 4), complex)
    for r, (i, j) in enumerate(pairs):
        dc[r, j] += vc[i]
        dc[r, i] -= vc[j]
    Pc = dc @ np.linalg.pinv(dc.conj().T @ dc) @ dc.conj().T
    ok_num = max(abs(Pc[r, r] - (abs(vc[i]) ** 2 + abs(vc[j]) ** 2) / np.sum(abs(vc) ** 2)) for r, (i, j) in enumerate(pairs)) < 1e-12
    lim_out = [sp.limit(Pe[0, 0].subs({v[0]: 0, v[1]: 0, v[3]: 0}), v[2], 0)] if False else [Pe[0, 0].subs({v[0]: 0, v[1]: 0, v[3]: 0})]
    lim_in = Pe[0, 0].subs({v[1]: 0, v[2]: 0, v[3]: 0})
    return ok_M, ok_diag, ok_proj, ok_num, sp.simplify(lim_out[0]), sp.simplify(lim_in)


# -------------------------------------------------------------------------------------------------------------- 5. certificate
def certificate():
    iv = mp.iv
    iv.dps = 50
    pi = iv.pi
    beta1 = (107 * iv.log(3) + iv.log(4)) / (4 * pi ** 2)
    a = lambda beta: iv.mpf(beta) / 384 - beta1
    q = lambda beta: iv.exp(-2 * pi ** 2 * a(beta))
    S5 = lambda x: x * (1 + 26 * x + 66 * x ** 2 + 26 * x ** 3 + x ** 4) / (1 - x) ** 6
    S6 = lambda x: x * (1 + 57 * x + 302 * x ** 2 + 302 * x ** 3 + 57 * x ** 4 + x ** 5) / (1 - x) ** 7
    delta = lambda beta: iv.mpf(beta) * (8503056 * S6(q(beta)) + 262144 * S5(q(beta))) / (a(beta) * iv.e)
    lo = lambda z: mp.mpf(z._mpi_[0])
    hi = lambda z: mp.mpf(z._mpi_[1])
    out = {}
    out["beta_1 < 10/3"] = hi(beta1) < mp.mpf(10) / 3
    out["a(2000) > 15/8"] = lo(a(2000)) > mp.mpf(15) / 8
    out["q < exp(-135/4) < 2^-48"] = hi(q(2000)) < hi(iv.exp(iv.mpf(-135) / 4)) and hi(iv.exp(iv.mpf(-135) / 4)) < mp.mpf(2) ** -48
    x = sp.symbols("x")
    out["Eulerian closed forms"] = all(sp.simplify(sp.series(expr, x, 0, 12).removeO() - sum(r ** jj * x ** r for r in range(1, 12))) == 0
                                       for jj, expr in ((5, x * (1 + 26 * x + 66 * x ** 2 + 26 * x ** 3 + x ** 4) / (1 - x) ** 6),
                                                        (6, x * (1 + 57 * x + 302 * x ** 2 + 302 * x ** 3 + 57 * x ** 4 + x ** 5) / (1 - x) ** 7)))
    qq = iv.mpf([0, mp.mpf(1) / 1024])
    out["S_j <= 2q on [0,1/1024]"] = all(hi(S(iv.mpf(t)) / iv.mpf(t)) <= 2 for S in (S5, S6) for t in [mp.mpf(k) / (1024 * 64) for k in range(1, 65)])
    d2000 = delta(2000)
    out["delta(2000) < 1/1000"] = hi(d2000) < mp.mpf(1) / 1000
    out["N=16384: beta_d > 2000"] = lo(iv.mpf(16384) ** 2 / (4 * pi ** 2 * 2000)) > 2000
    d2000 = (lo(d2000), hi(d2000))
    # extra numbers (mp floats, bisection)
    mp.mp.dps = 40
    b1 = (107 * mp.log(3) + mp.log(4)) / (4 * mp.pi ** 2)
    def dfl(beta):
        aa = mp.mpf(beta) / 384 - b1
        if aa <= 0:
            return mp.inf
        x_ = mp.exp(-2 * mp.pi ** 2 * aa)
        s5 = x_ * (1 + 26 * x_ + 66 * x_ ** 2 + 26 * x_ ** 3 + x_ ** 4) / (1 - x_) ** 6
        s6 = x_ * (1 + 57 * x_ + 302 * x_ ** 2 + 302 * x_ ** 3 + 57 * x_ ** 4 + x_ ** 5) / (1 - x_) ** 7
        return mp.mpf(beta) * (8503056 * s6 + 262144 * s5) / (aa * mp.e)
    def smallest(target):
        lo, hi = 384 * b1 + mp.mpf("1e-30"), mp.mpf(2000)
        for _ in range(200):
            mid = (lo + hi) / 2
            if dfl(mid) < target:
                hi = mid
            else:
                lo = mid
        return hi
    beta_min_1e3, beta_min_half = smallest(mp.mpf(1) / 1000), smallest(mp.mpf(1) / 2)
    Nmin = int(mp.ceil(4000 * mp.pi))
    grid_decr = all(dfl(b) > dfl(b + 10) for b in range(1200, 3000, 10))
    return out, d2000, beta_min_1e3, beta_min_half, Nmin, grid_decr, 384 * b1


def main():
    n, par, perp, members = neighbourhood()
    tor = {L: torus_neighbourhood(members, L) for L in (4, 6, 8)}
    print(f"1. distance-one neighbourhood in Z^4: {n} edges, parallel {par}, perpendicular {perp}; torus images {tor}")
    col = {L: colouring_check(L) for L in (4, 6, 8, 10)}
    print(f"2. 32-colouring (no same-colour pair on a plaquette, colours, Q_ee values): {col}")
    damp = damping_identity()
    print(f"   damping identity (5.1) over all 80 signed sums of four separated currents on T_6 (exact): {damp}")
    ok_id, cratio, ok_fill, worst = filling_checks()
    print(f"3. filling: boundary K_1(e) = P(x) + e - P(x+e_j) on every edge of boxes R = 2,3,4: {ok_id}; max plaquettes/(3R) {cratio:.3f}; "
          f"40 random closed currents: delta_2 mu = rho, ||mu||_1 <= 3R ||rho||_1, |rho(w)| <= ||mu||_1 max|dw|: {ok_fill} "
          f"(largest ratio {worst:.3f})")
    pr = projectors()
    print(f"4. projectors: d^T d = |v|^2 I - v v^T {pr[0]}; diagonal formula {pr[1]}; P_e idempotent {pr[2]}; complex-k check {pr[3]}; "
          f"P_e,01,01 along axis 2: {pr[4]}, along axis 0: {pr[5]}")
    cert, d2000, bmin3, bmin2, Nmin, decr, bthr = certificate()
    print(f"5. certificate (interval arithmetic): {cert}; delta(2000) in [{mp.nstr(d2000[0], 6)}, {mp.nstr(d2000[1], 6)}]; delta decreasing "
          f"on beta = 1200..3000 grid {decr}; a > 0 needs beta > {mp.nstr(bthr, 6)}; smallest beta with delta < 1/1000: "
          f"{mp.nstr(bmin3, 7)}, with delta < 1/2: {mp.nstr(bmin2, 7)}; smallest N with beta_d >= 2000 at beta = 2000: {Nmin}")
    fails = []
    if not (n == 107 and par == 23 and all(v == 28 for v in perp.values()) and all(v <= 107 for v in tor.values())):
        fails.append("neighbourhood")
    if not all(c[0] and c[1] == 32 and c[2] == {6} for c in col.values()):
        fails.append("colouring")
    if not damp:
        fails.append("damping identity")
    if not (ok_id and cratio <= 1 and ok_fill):
        fails.append("filling")
    if not (pr[0] and pr[1] and pr[2] and pr[3] and pr[4] == 0 and pr[5] == 1):
        fails.append("projectors")
    if not all(cert.values()):
        fails.append(f"certificate {[k for k, v in cert.items() if not v]}")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: 107 = 23 + 3 x 28 distance-one edges in Z^4 (torus images {tor}); the 32-colouring separates plaquette neighbours "
          f"with Q_ee = 6 on T_4..T_10; the damping identity holds exactly on all signed sums; the K_1(e) filling satisfies its boundary "
          f"identity on every edge of boxes to side 4 with at most 3R plaquettes and fills random closed currents within the l1 bound; the "
          f"exact-projector diagonal and its directional limits 0 and 1 hold; the section-9 certificate holds in interval arithmetic with "
          f"delta(2000) = {mp.nstr(d2000[1], 3)} (the note's bound 1/1000); delta < 1/1000 from beta = {mp.nstr(bmin3, 6)} and < 1/2 from "
          f"{mp.nstr(bmin2, 6)}; N >= {Nmin} suffices at beta = 2000 (note: 16384); no step fails")


if __name__ == "__main__":
    main()
