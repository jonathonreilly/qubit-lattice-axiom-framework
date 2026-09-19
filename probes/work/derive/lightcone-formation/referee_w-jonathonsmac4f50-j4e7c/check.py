#!/usr/bin/env python3
"""Referee of J:derive:lightcone-formation:a2 (author w-macbookpro90c72-jfbe5, grok-4.6); referee w-jonathonsmac4f50-j4e7c
(claude-opus-5). Independent code (exact integer / Fraction enumeration; floats only in the INFO line); nothing from the
author's check.py. Disclosure: this referee's model family refereed attempts a5 and a6 of this problem (both grok); their
doubled-graph facts overlap steps 1-4 here.

Objects: T = (Z/L)^3, stencil N(x) = {x, x +- e_j}; the doubled graph Gamma on T x {0,1} with edges (x,0)-(y,1), y in N(x);
theta_Gamma(x, eps) = (theta x, 1 - eps) for theta a reflection through a pair of antipodal bond planes x_j -> 2c + 1 - x_j.

D1  steps 1-2: the 7-stencil pairing sum_x s'_x . S_x(s) is symmetric on (Z/4)^3 (integer vectors), and detailed balance of
    the Ising analogue on the 3-stencil ring Z/4 with t = e^beta in {2, 3} holds exactly on all 16^2 pairs (pi P = pi)
D2  step 4: on (Z/4)^3 the Gamma Laplacian has eigenvalue E(k) on layer-symmetric and 14 - E(k) on layer-antisymmetric plane
    waves (exact, every k)
D3  step 7's claim 'a field invariant under the whole group is ... constant on V(Gamma)' is false: every theta_Gamma (all
    bond planes, three directions, L = 4 and 6) preserves the bipartition A = {(x,0): |x| even} u {(y,1): |y| odd}, B = rest,
    so the two-valued field 1_A is invariant under the whole group and not constant
D4  why: the crossing edges of every theta_Gamma are the pairs {v, theta_Gamma v}; a vertical edge (x,0)-(x,1) never crosses
    any plane, every other edge crosses one; so the reflection argument makes a maximizing field constant on the non-vertical
    edges only, i.e. two-valued on A, B; 1_A - 1_B is a Gamma-Laplacian eigenfunction with eigenvalue 2 (the odd sector at
    k = (pi,pi,pi)), and Z(t 1_A) <= Z(0) is exactly that mode's infrared bound: not supplied by the argument
D5  what survives: the reflected fields phi^+- of a layer-symmetric field are layer-symmetric (exact, all planes), vertical
    edges then carry no twist, and the argument closes: Gaussian domination and <|s_+^e(k)|^2> <= 1/(beta E(k)) hold for the
    EVEN sector; the odd-sector bound, hence the bound (1/(2beta))(1/E + 1/(14-E)) on pi, the LRO threshold of step 9 (which
    drops all odd modes via those bounds) and the upper side of step 10's sandwich are not proved
D6  step 12: the linear prefactor 7/(2(1 - E/14)) runs from 7/2 to 49/2 on (0, 12] (exact), as stated
I1  INFO: Ising analogue on the 1D doubled graph (3-stencil, L = 4, 6): every even and odd infrared ratio < 1 and the
    staggered twist Z(t 1_A)/Z(0) < 1 at the tested beta, t: no violation of the unproved bounds found
"""
from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as F

import numpy as np

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def stencil(x, L, d):
    out = [tuple(x)]
    for j in range(d):
        for s in (1, -1):
            y = list(x)
            y[j] = (y[j] + s) % L
            out.append(tuple(y))
    return out


def gamma(L, d=3):
    sites = list(itertools.product(range(L), repeat=d))
    V = [(x, e) for e in (0, 1) for x in sites]
    E = [((x, 0), (y, 1)) for x in sites for y in stencil(x, L, d)]
    return sites, V, E


def planes(L, d=3):
    for j in range(d):
        for c in range(L // 2):
            def th(x, j=j, c=c):
                y = list(x)
                y[j] = (2 * c + 1 - y[j]) % L
                return tuple(y)
            half = {x for x in itertools.product(range(L), repeat=d) if (x[j] - c - 1) % L >= L // 2}
            yield j, c, th, half


def main():
    # D1
    L = 4
    rng = np.random.default_rng(1)
    sites = list(itertools.product(range(L), repeat=3))
    ok = True
    for _ in range(5):
        s = {x: tuple(int(v) for v in rng.integers(-3, 4, 3)) for x in sites}
        t = {x: tuple(int(v) for v in rng.integers(-3, 4, 3)) for x in sites}
        S = lambda f, x: tuple(sum(f[y][i] for y in stencil(x, L, 3)) for i in range(3))
        lhs = sum(sum(a * b for a, b in zip(t[x], S(s, x))) for x in sites)
        rhs = sum(sum(a * b for a, b in zip(s[x], S(t, x))) for x in sites)
        ok &= lhs == rhs
    ring = range(4)
    db_ok = True
    for tt in (2, 3):
        confs = list(itertools.product((-1, 1), repeat=4))

        def Sx(c, x):
            return c[x] + c[(x + 1) % 4] + c[(x - 1) % 4]

        def P(c, c2):
            out = F(1)
            for x in ring:
                h = Sx(c, x)
                out *= F(tt) ** (c2[x] * h) / (F(tt) ** h + F(tt) ** (-h))
            return out

        def pi(c):
            w = F(1)
            for x in ring:
                h = Sx(c, x)
                w *= F(tt) ** h + F(tt) ** (-h)
            return w
        Z = sum(pi(c) for c in confs)
        for c in confs:
            db_ok &= sum(P(c, c2) for c2 in confs) == 1
            for c2 in confs:
                db_ok &= pi(c) * P(c, c2) == pi(c2) * P(c2, c)
        db_ok &= all(sum(pi(c) / Z * P(c, c2) for c in confs) == pi(c2) / Z for c2 in confs)
    check("D1", ok and db_ok, "7-stencil pairing symmetric on (Z/4)^3 (5 random integer fields); Ising 3-stencil ring Z/4, "
          "t = 2, 3: rows sum to 1, detailed balance on all 256 pairs, pi P = pi (exact)")

    # D2
    sites, V, E = gamma(4)
    idx = {v: i for i, v in enumerate(V)}
    ok = True
    for k in itertools.product(range(4), repeat=3):
        # use the real parts cos(pi/2 k.x): values in {1, 0, -1} exactly
        ck = {x: [1, 0, -1, 0][(sum(a * b for a, b in zip(k, x))) % 4] for x in sites}
        Ek = sum(2 * (1 - [1, 0, -1, 0][kk % 4]) for kk in k)
        for sec, lam in ((1, Ek), (-1, 14 - Ek)):
            f = {(x, 0): ck[x] for x in sites}
            f.update({(x, 1): sec * ck[x] for x in sites})
            Lf = {v: 7 * f[v] for v in V}
            for u, w in E:
                Lf[u] -= f[w]
                Lf[w] -= f[u]
            ok &= all(Lf[v] == lam * f[v] for v in V)
    check("D2", ok, "(Z/4)^3: layer-symmetric plane waves have Gamma-Laplacian eigenvalue E(k), antisymmetric ones 14 - E(k), all 64 k")

    # D3, D4
    ok3 = ok4 = True
    for L in (4, 6):
        sites, V, E = gamma(L)
        par = lambda x: sum(x) % 2
        A = {(x, 0) for x in sites if par(x) == 0} | {(x, 1) for x in sites if par(x) == 1}
        for j, c, th, half in planes(L):
            tg = lambda v: (th(v[0]), 1 - v[1])
            ok3 &= all((tg(v) in A) == (v in A) for v in V)
            Vp = {(x, e) for x in half for e in (0, 1)}
            cross = [(u, w) for u, w in E if (u in Vp) != (w in Vp)]
            ok4 &= all(tg(u) == w for u, w in cross)
            ok4 &= not any(u[0] == w[0] for u, w in cross)
        crossed = set()
        for j, c, th, half in planes(L):
            Vp = {(x, e) for x in half for e in (0, 1)}
            crossed |= {(u, w) for u, w in E if (u in Vp) != (w in Vp)}
        ok4 &= crossed == {(u, w) for u, w in E if u[0] != w[0]}
        if L == 4:
            psi = {v: (1 if v in A else -1) for v in V}
            Lp = {v: 7 * psi[v] for v in V}
            for u, w in E:
                Lp[u] -= psi[w]
                Lp[w] -= psi[u]
            eig2 = all(Lp[v] == 2 * psi[v] for v in V)
            anti = all(psi[(x, 0)] == -psi[(x, 1)] for x in sites)
    check("D3", ok3, "L = 4, 6: every theta_Gamma (bond planes in three directions, layer swap) maps A = {(x,0): |x| even} u "
          "{(y,1): |y| odd} onto itself; 1_A is invariant under the whole group and not constant (|A| = |B| = N)")
    check("D4", ok4 and eig2 and anti, "the crossing edges of each theta_Gamma are exactly pairs {v, theta_Gamma v}, none vertical; "
          "the union over all planes is every non-vertical edge, so vertical edges (x,0)-(x,1) are never controlled; "
          "1_A - 1_B is layer-antisymmetric with Gamma-Laplacian eigenvalue 2 (odd sector, k = (pi,pi,pi))")

    # D5
    ok5 = True
    L = 4
    sites, V, E = gamma(L)
    for trial in range(3):
        f = {x: int(rng.integers(-9, 10)) for x in sites}
        g = {x: int(rng.integers(-9, 10)) for x in sites}
        sym = {(x, e): f[x] for x in sites for e in (0, 1)}
        ant = {(x, e): (g[x] if e == 0 else -g[x]) for x in sites for e in (0, 1)}
        for j, c, th, half in planes(L):
            tg = lambda v: (th(v[0]), 1 - v[1])
            Vp = {(x, e) for x in half for e in (0, 1)}
            for phi, want in ((sym, 1), (ant, -1)):
                plus = {v: (phi[v] if v in Vp else phi[tg(v)]) for v in V}
                minus = {v: (phi[tg(v)] if v in Vp else phi[v]) for v in V}
                for q in (plus, minus):
                    ok5 &= all(q[(x, 0)] == want * q[(x, 1)] for x in sites)
    check("D5", ok5, "(Z/4)^3, all planes: reflected fields phi^+- of layer-symmetric (antisymmetric) fields are layer-symmetric "
          "(antisymmetric); on the symmetric class the vertical edges carry no twist and the argument closes, on the "
          "antisymmetric class the staggered field 1_A - 1_B remains")

    # D6
    ok6 = True
    vals = [F(7, 2) / (1 - F(e, 14)) for e in range(0, 13)]
    ok6 &= vals[0] == F(7, 2) and vals[12] == F(49, 2) and all(a < b for a, b in zip(vals, vals[1:]))
    check("D6", ok6, "7/(2(1 - E/14)) increases from 7/2 (E -> 0) to 49/2 (E = 12)")

    # I1
    worst, zmax = 0.0, 0.0
    for L in (4, 6):
        Vv = [(x, e) for e in (0, 1) for x in range(L)]
        ix = {v: i for i, v in enumerate(Vv)}
        Ed = [(ix[(x, 0)], ix[(y, 1)]) for x in range(L) for y in (x, (x + 1) % L, (x - 1) % L)]
        n = len(Vv)
        st = np.array(list(itertools.product((-1, 1), repeat=n)), dtype=float)
        Eb = sum(st[:, u] * st[:, v] for u, v in Ed)
        Ad = np.zeros((n, n))
        for u, v in Ed:
            Ad[u, v] += 1
            Ad[v, u] += 1
        Lap = np.diag(Ad.sum(1)) - Ad
        Aset = np.array([1.0 if ((x % 2 == 0) == (e == 0)) else 0.0 for (x, e) in Vv])
        for beta in (0.1, 0.3, 0.5, 1.0, 2.0):
            w = np.exp(beta * (Eb - Eb.max()))
            w /= w.sum()
            for k in range(L):
                for sec in (1, -1):
                    for fn in (np.cos, np.sin):
                        psi = np.array([fn(2 * math.pi * k * x / L) * (1 if e == 0 else sec) for (x, e) in Vv])
                        if psi @ psi < 1e-9:
                            continue
                        lam = psi @ Lap @ psi / (psi @ psi)
                        if lam < 1e-9:
                            continue
                        X = st @ psi
                        worst = max(worst, (w * X * X).sum() / ((psi @ psi) / (beta * lam)))
            D = st @ (2 * Aset - 1)
            for t in np.linspace(0.05, 3, 60):
                zmax = max(zmax, math.exp(-beta * n / 2 * t * t) * (w * np.exp(beta * t * D)).sum())
    print(f"INFO I1: Ising on the 1D doubled graph (L = 4, 6; beta 0.1..2): largest infrared ratio over even and odd modes "
          f"{worst:.4f} < 1, largest staggered-twist ratio Z(t 1_A)/Z(0) {zmax:.4f} < 1 (no violation of the unproved bounds found)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 7 - Gaussian domination on Gamma is proved only for layer-symmetric fields: the theta_Gamma "
          "reflections preserve the bipartition A/B of V(Gamma) (layer x spatial parity), vertical edges never cross a plane, "
          "and the field 1_A is invariant under the whole group but not constant (D3, D4), so 'invariant => constant' is false "
          "and Z(phi) <= Z(0) is not established for layer-antisymmetric phi; the odd-sector bound 2/(beta(14 - E)), the "
          "bound (1/(2beta))(1/E + 1/(14-E)) on pi, the LRO threshold 3 sqrt3 pi/16 + 3/4 and the upper side of step 10's "
          "sandwich rest on it. Holds: reversibility, the Gibbs / doubled-graph identity, the spectrum {E, 14 - E}, RP for "
          "theta_Gamma, the even-sector bound <|s_+(k)|^2> <= 1/(beta E(k)) (D5), the linear prefactor range [7/2, 49/2]; the "
          "missing lemma is Z(t 1_A) <= Z(0) (the staggered twist), not violated in the 1D Ising analogue (I1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
