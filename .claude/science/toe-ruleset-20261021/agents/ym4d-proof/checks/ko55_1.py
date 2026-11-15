#!/usr/bin/env python3
"""ko55_1 -- exact checks for KFACTOR_OFF55 (Opus 5.5 worker, claude-opus-5-5).

Criteria: checks/ko55_1_criteria.md (written and amended BEFORE this script existed).
Exact integer / Fraction arithmetic only; no floats in any verdict.  Pure python, single thread.

Implements literally the objects defined in the criteria file:
  level-j sites Z in (Z/(T L^{k-j}))^d; level-j block of Z = {L^j Z + t : t in [0,L^j)^d};
  root of the level-(j+1) block of Y, as a level-j site = L*Y + (L-1)/2 (centre);
  ev^{(j)} site map Z -> L^j Z + (L^j-1)/2;  d*v(Z) = sum_mu [v(Z-e_mu,mu) - v(Z,mu)];
  D(S) = sum_j ev^{(j)T} d*_j S_j;  hierarchical routing P^T u (axial path from the block root, coordinates 0..d-1).
"""
from fractions import Fraction
from math import comb, factorial
import itertools
import random
import sys

L = 3
RESULTS = {}


def say(*a):
    print(*a)
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------------------------------
# lattice helpers
# ----------------------------------------------------------------------------------------------------------------
def side(T, k, j):
    return T * L ** (k - j)


def all_sites(T, k, j, d):
    return list(itertools.product(range(side(T, k, j)), repeat=d))


def ev_site(Z, j):
    off = (L ** j - 1) // 2
    return tuple(L ** j * z + off for z in Z)


def add(a, mu, s, n):
    b = list(a)
    b[mu] = (b[mu] + s) % n
    return tuple(b)


def dstar(v, T, k, j, d):
    """d* of a level-j 1-form v (dict (Z,mu) -> value, missing = 0); returns dict Z -> value."""
    n = side(T, k, j)
    out = {}
    for Z in all_sites(T, k, j, d):
        s = 0
        for mu in range(d):
            s += v.get((add(Z, mu, -1, n), mu), 0) - v.get((Z, mu), 0)
        out[Z] = s
    return out


def axial_path(R, Z, d, n):
    """level-j axial path from R to Z, coordinates 0..d-1 in order, no wrap needed (same block).
    returns list of ((site, mu), sign)."""
    steps = []
    cur = list(R)
    for mu in range(d):
        while cur[mu] != Z[mu]:
            if Z[mu] > cur[mu]:
                steps.append(((tuple(cur), mu), +1))
                cur[mu] += 1
            else:
                cur[mu] -= 1
                steps.append(((tuple(cur), mu), -1))
    assert tuple(cur) == tuple(Z)
    return steps


def block_values(u, T, k, j, d):
    """V_j(Z) := sum of level-0 function u over the level-j block of every level-j site Z."""
    V = {}
    Lj = L ** j
    for Z in all_sites(T, k, j, d):
        base = tuple(Lj * z for z in Z)
        s = 0
        for t in itertools.product(range(Lj), repeat=d):
            s += u[tuple(b + tt for b, tt in zip(base, t))]
        V[Z] = s
    return V


def route(u, T, k, d, root_mode="centre", skip_level=None):
    """Hierarchical routing P^T u: returns (list of level-j currents as dicts, list of V_j dicts)."""
    currents, Vs = [], []
    for j in range(k):
        n = side(T, k, j)
        V = block_values(u, T, k, j, d)
        cur = {}
        if j != skip_level:
            for Z, val in V.items():
                if val == 0:
                    continue
                Y = tuple(z // L for z in Z)
                if root_mode == "centre":
                    R = tuple(L * y + (L - 1) // 2 for y in Y)
                else:  # corner (control)
                    R = tuple(L * y for y in Y)
                for (lk, sg) in axial_path(R, Z, d, n):
                    cur[lk] = cur.get(lk, 0) + sg * val
        currents.append(cur)
        Vs.append(V)
    return currents, Vs


def composite_div(currents, T, k, d):
    """D(S) = sum_j ev^{(j)T} d*_j S_j as a level-0 function (dict)."""
    D = {z: 0 for z in all_sites(T, k, 0, d)}
    for j, cur in enumerate(currents):
        dj = dstar(cur, T, k, j, d)
        for Z, val in dj.items():
            if val:
                z = ev_site(Z, j)
                D[z] += val
    return D


def level_k_roots(T, k, d):
    return {ev_site(X, k): X for X in all_sites(T, k, k, d)}


def a1_rhs(u, T, k, d):
    """u off level-k roots; u(r) - (cell total) at level-k roots."""
    rhs = dict(u)
    Lk = L ** k
    for r, X in level_k_roots(T, k, d).items():
        base = tuple(Lk * x for x in X)
        tot = 0
        for t in itertools.product(range(Lk), repeat=d):
            tot += u[tuple(b + tt for b, tt in zip(base, t))]
        rhs[r] = u[r] - tot
    return rhs


def multiplicity(d):
    """max over level-j links of the number of Z in one level-(j+1) block whose path from the centre uses it."""
    cnt = {}
    R = tuple((L - 1) // 2 for _ in range(d))
    for Z in itertools.product(range(L), repeat=d):
        for (lk, sg) in axial_path(R, Z, d, 10 ** 9):
            cnt[lk] = cnt.get(lk, 0) + 1
    return max(cnt.values()) if cnt else 0


CASES = [(2, 1, 1), (2, 2, 1), (2, 2, 2), (2, 3, 1), (2, 3, 2), (2, 4, 1), (4, 1, 1), (4, 2, 1)]

# ----------------------------------------------------------------------------------------------------------------
# Part A1 + controls
# ----------------------------------------------------------------------------------------------------------------
say("=== Part A1: routing identity D(P^T u) = u off level-k roots; u(r) - cell total at roots ===")
a1_ok, ctl_ok = True, True
for (d, k, T) in CASES:
    rng = random.Random(1000 * d + 100 * k + T)
    u = {z: rng.randint(-5, 5) for z in all_sites(T, k, 0, d)}
    cur, _ = route(u, T, k, d)
    D = composite_div(cur, T, k, d)
    rhs = a1_rhs(u, T, k, d)
    bad = [z for z in D if D[z] != rhs[z]]
    ok = (len(bad) == 0)
    a1_ok &= ok
    # control (i): corner routing
    curc, _ = route(u, T, k, d, root_mode="corner")
    Dc = composite_div(curc, T, k, d)
    fire_i = any(Dc[z] != rhs[z] for z in Dc)
    # control (ii): skip level 1 (only if k >= 2)
    if k >= 2:
        curs, _ = route(u, T, k, d, skip_level=1)
        Ds = composite_div(curs, T, k, d)
        fire_ii = any(Ds[z] != rhs[z] for z in Ds)
    else:
        fire_ii = None
    c_ok = fire_i and (fire_ii in (True, None))
    ctl_ok &= c_ok
    say(f"  (d,k,T)=({d},{k},{T}) sites={len(u)}: identity {'PASS' if ok else 'FAIL'} (mismatches {len(bad)}); "
        f"control(i) corner fires={fire_i}; control(ii) skip-level-1 fires={fire_ii}")
RESULTS["A1"] = a1_ok
RESULTS["A1-ctl"] = ctl_ok
say(f"A1: {'PASS' if a1_ok else 'FAIL'}   A1-ctl: {'PASS' if ctl_ok else 'FAIL'}")

# ----------------------------------------------------------------------------------------------------------------
# Part A2: vanishing below l, flux bound, sup route, multiplicity
# ----------------------------------------------------------------------------------------------------------------
say("=== Part A2: u = ev^{(l)T} d*_l w; (P^T u)_i = 0 for i<l; |V_i| <= 2d L^{(d-1)(i-l)} max|w|; "
    "max|(P^T u)_i| <= M_gamma 2d L^{(d-1)(i-l)} max|w| ===")
a2_ok = True
Mg = {}
for d in (2, 4):
    Mg[d] = multiplicity(d)
    expect = L ** (d - 1) * (L - 1) // 2
    okm = (Mg[d] == expect)
    a2_ok &= okm
    say(f"  d={d}: M_gamma = {Mg[d]} (expected L^(d-1)(L-1)/2 = {expect}) {'PASS' if okm else 'FAIL'}")
worst = Fraction(0)
for (d, k, T) in CASES:
    for l in range(k):
        rng = random.Random(7 + 31 * d + 17 * k + 5 * T + l)
        w = {}
        for Z in all_sites(T, k, l, d):
            for mu in range(d):
                w[(Z, mu)] = rng.randint(-5, 5)
        wmax = max(abs(v) for v in w.values())
        dw = dstar(w, T, k, l, d)
        u = {z: 0 for z in all_sites(T, k, 0, d)}
        for Z, val in dw.items():
            u[ev_site(Z, l)] += val
        cur, Vs = route(u, T, k, d)
        for i in range(k):
            cmax = max((abs(v) for v in cur[i].values()), default=0)
            if i < l:
                if cmax != 0:
                    a2_ok = False
                    say(f"  FAIL: nonzero routing below l: (d,k,T,l,i)=({d},{k},{T},{l},{i})")
                continue
            vb = 2 * d * L ** ((d - 1) * (i - l)) * wmax
            vmax = max(abs(v) for v in Vs[i].values())
            cb = Mg[d] * vb
            if vmax > vb or cmax > cb:
                a2_ok = False
                say(f"  FAIL: (d,k,T,l,i)=({d},{k},{T},{l},{i}) |V|max={vmax} bound {vb}; |cur|max={cmax} bound {cb}")
            if cb:
                worst = max(worst, Fraction(cmax, cb))
    say(f"  (d,k,T)=({d},{k},{T}) done")
RESULTS["A2"] = a2_ok
say(f"A2: {'PASS' if a2_ok else 'FAIL'}  (largest observed current/bound ratio = {worst} = {float(worst):.4f}; display only)")

# ----------------------------------------------------------------------------------------------------------------
# Part A3: boundary-flux identity for V_i of u = d*_0 w
# ----------------------------------------------------------------------------------------------------------------
say("=== Part A3: V_i(Z) [u = d*_0 w] = sum_mu sum_lines [w(entry) - w(exit)] for every level-i block, 1<=i<=k-1 ===")
a3_ok = True
for (d, k, T) in CASES:
    if k < 2:
        continue
    rng = random.Random(4242 + d * 10 + k * 3 + T)
    n0 = side(T, k, 0, )
    w = {}
    for z in all_sites(T, k, 0, d):
        for mu in range(d):
            w[(z, mu)] = rng.randint(-5, 5)
    u = dstar(w, T, k, 0, d)
    nbad = 0
    for i in range(1, k):
        V = block_values(u, T, k, i, d)
        Li = L ** i
        for Z, val in V.items():
            base = [Li * z for z in Z]
            s = 0
            for mu in range(d):
                others = [nu for nu in range(d) if nu != mu]
                for tt in itertools.product(range(Li), repeat=d - 1):
                    first = list(base)
                    for nu, t in zip(others, tt):
                        first[nu] = base[nu] + t
                    entry = list(first)
                    entry[mu] = (base[mu] - 1) % n0
                    last = list(first)
                    last[mu] = base[mu] + Li - 1
                    s += w[(tuple(entry), mu)] - w[(tuple(last), mu)]
            if s != val:
                nbad += 1
    ok = (nbad == 0)
    a3_ok &= ok
    say(f"  (d,k,T)=({d},{k},{T}): {'PASS' if ok else 'FAIL'} (mismatching blocks {nbad})")
RESULTS["A3"] = a3_ok
say(f"A3: {'PASS' if a3_ok else 'FAIL'}")

# ----------------------------------------------------------------------------------------------------------------
# Part A4': mechanism (amended criteria)
# ----------------------------------------------------------------------------------------------------------------
say("=== Part A4': d=2, T=1, k=1..5; w_mu(z) = tri(z_mu); u = d*_0 w; hierarchical vs single-level routing ===")
d, T = 2, 1
rho_h, rho_s = {}, {}
a4a = True
bound_a = Fraction(d * Mg[d], L - 1)
for k in range(1, 6):
    n = L ** k

    def tri(t):
        t %= n
        return min(t, n - t)
    sites0 = all_sites(T, k, 0, d)
    w = {}
    for z in sites0:
        for mu in range(d):
            w[(z, mu)] = tri(z[mu])
    smax = 0
    for z in sites0:
        for mu in range(d):
            for nu in range(d):
                smax = max(smax, abs(w[(add(z, nu, +1, n), mu)] - w[(z, mu)]))
    u = dstar(w, T, k, 0, d)
    nonzero = sum(1 for v in u.values() if v)
    cur, _ = route(u, T, k, d)
    Jh = 0
    for i in range(k):
        cmax = max((abs(v) for v in cur[i].values()), default=0)
        Jh += L ** ((d - 1) * (k - i)) * cmax
    # single-level routing to the level-k root of the (single) cell
    Rk = tuple((n - 1) // 2 for _ in range(d))
    single = {}
    for z in sites0:
        val = u[z]
        if val == 0:
            continue
        for (lk, sg) in axial_path(Rk, z, d, n):
            single[lk] = single.get(lk, 0) + sg * val
    smax_cur = max((abs(v) for v in single.values()), default=0)
    Js = L ** ((d - 1) * k) * smax_cur
    Lipc = n ** (d - 1) * n * smax
    rho_h[k] = Fraction(Jh, Lipc)
    rho_s[k] = Fraction(Js, Lipc)
    oka = rho_h[k] <= bound_a
    a4a &= oka
    say(f"  k={k} n={n}: nonzero charges={nonzero}, s_max={smax}, J_hier={Jh}, J_single={Js}, Lip_c={Lipc}; "
        f"rho_hier={rho_h[k]} (<= {bound_a}: {oka}), rho_single={rho_s[k]}  "
        f"[display: {float(rho_h[k]):.4f}, {float(rho_s[k]):.4f}]")
a4b = rho_s[5] >= 10 * rho_s[2]
RESULTS["A4'"] = a4a and a4b
say(f"A4': (a) {'PASS' if a4a else 'FAIL'}; (b) control rho_single(5) >= 10 rho_single(2): {a4b} "
    f"(ratio {rho_s[5] / rho_s[2]}) -> {'PASS' if (a4a and a4b) else 'FAIL'}")

# ----------------------------------------------------------------------------------------------------------------
# Part B: Bernoulli series constant
# ----------------------------------------------------------------------------------------------------------------
say("=== Part B: S_60 = sum_{n=1}^{60} |B_n|/n! + tail <= 59/100; |B_n|/n! <= 4/6^n (2<=n<=60) ===")
B = [Fraction(1)]
for m in range(1, 61):
    B.append(-sum(comb(m + 1, j) * B[j] for j in range(m)) / (m + 1))
assert B[1] == Fraction(-1, 2) and B[2] == Fraction(1, 6) and B[4] == Fraction(-1, 30)
S = sum(abs(B[n]) / factorial(n) for n in range(1, 61))
tail = Fraction(4, 6 ** 61) / (1 - Fraction(1, 6))
okB1 = S + tail <= Fraction(59, 100)
okB2 = all(abs(B[n]) / factorial(n) <= Fraction(4, 6 ** n) for n in range(2, 61))
RESULTS["B"] = okB1 and okB2
say(f"  S_60 = {float(S):.10f} (display), S_60 + tail <= 59/100: {okB1}; termwise bound: {okB2}")
say(f"B: {'PASS' if RESULTS['B'] else 'FAIL'}")

# ----------------------------------------------------------------------------------------------------------------
# Part C: series constants
# ----------------------------------------------------------------------------------------------------------------
say("=== Part C: sum_{m<=M} (m+1) L^-m < (L/(L-1))^2; closed form exact; sum L^-m < L/(L-1); (1316/1000)^4 < 3 ===")
x = Fraction(1, L)
okC = True
lim2 = Fraction(L, L - 1) ** 2
lim1 = Fraction(L, L - 1)
s2, s1 = Fraction(0), Fraction(0)
for M in range(0, 401):
    s2 += (M + 1) * x ** M
    s1 += x ** M
    closed = (1 - (M + 2) * x ** (M + 1) + (M + 1) * x ** (M + 2)) / (1 - x) ** 2
    if M >= 1 and not (s2 < lim2 and s2 == closed and s1 < lim1):
        okC = False
ok4 = Fraction(1316, 1000) ** 4 < 3
okC = okC and ok4 and lim2 == Fraction(9, 4)
RESULTS["C"] = okC
say(f"  (L/(L-1))^2 = {lim2}; (1316/1000)^4 = {Fraction(1316, 1000) ** 4} < 3: {ok4}")
say(f"C: {'PASS' if okC else 'FAIL'}")

overall = all(RESULTS[key] for key in ["A1", "A1-ctl", "A2", "A3", "A4'", "B", "C"])
say("=== SUMMARY ===")
for key in ["A1", "A1-ctl", "A2", "A3", "A4'", "B", "C"]:
    say(f"  {key}: {'PASS' if RESULTS[key] else 'FAIL'}")
say(f"OVERALL: {'PASS' if overall else 'FAIL'}")
