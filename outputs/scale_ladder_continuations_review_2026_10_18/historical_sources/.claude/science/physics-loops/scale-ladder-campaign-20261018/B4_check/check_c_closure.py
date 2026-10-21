#!/usr/bin/env python3
"""B4 independent check (b,c): curvature-member kinetic eps3 and the lattice lapse-bracket closure.

Re-implementation (own code, not importing B4 scripts).  Instead of testing 4 hand-picked kinetic
points, solve for the WHOLE set of cubic inverse-kinetic forms
    dH/dP_jj = a P_jj + b sum_i P_ii ,   dH/dP_ij = f P_ij  (i<j, P_ij conjugate to h_ij counted once)
for which {C[N], C[M]} (term linear in P, flat strain) lies in the span of ALL lattice relabellings,
exactly over QQ, for several torus sides, lapse pairs and face timings.  Lagrangian anisotropy:
M3 = 1/(2f), 2M1 - M2 = 1/a  ->  eps3 = M3/(2M1-M2) - 1 = a/(2f) - 1.
Also: float SVD gap of [D | bracket] for the B4 script's four kinetic points.
"""
import random
import sys
from itertools import product

import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

PAIRS = ((0, 1), (0, 2), (1, 2))


def unit(j):
    return tuple(int(k == j) for k in range(3))


def build(n):
    sites = list(product(range(n), repeat=3))
    sidx = {x: i for i, x in enumerate(sites)}

    def sh(x, v, s=1):
        return tuple((x[k] + s * v[k]) % n for k in range(3))
    comps = [("d", x, j) for x in sites for j in range(3)] + [("f", y, p) for y in sites for p in PAIRS]
    cidx = {c: i for i, c in enumerate(comps)}
    # relabelling D: xi (3 n^3) -> delta h
    D = [[0] * (3 * len(sites)) for _ in comps]
    for x in sites:
        for j in range(3):
            col = 3 * sidx[x] + j
            # delta h_jj(z) = 2(xi_j(z) - xi_j(z - e_j))
            D[cidx[("d", x, j)]][col] += 2
            D[cidx[("d", sh(x, unit(j)), j)]][col] -= 2
            # delta h_ij(y) = xi_j(y+e_i) - xi_j(y) + xi_i(y+e_j) - xi_i(y)
            for (p, q) in PAIRS:
                if j == q:
                    D[cidx[("f", sh(x, unit(p), -1), (p, q))]][col] += 1
                    D[cidx[("f", x, (p, q))]][col] -= 1
                if j == p:
                    D[cidx[("f", sh(x, unit(q), -1), (p, q))]][col] += 1
                    D[cidx[("f", x, (p, q))]][col] -= 1
    return sites, sidx, sh, comps, cidx, D


def r1_grad(N, sites, sh, comps, cidx, s_face=2):
    """dR1[N]/dh  for  R1 = p^2 tr h - p.h.p  (diag on sites, off-diag on faces)."""
    r = [sp.Rational(0)] * len(comps)
    for x in sites:
        lap = [N[sh(x, unit(i))] - 2 * N[x] + N[sh(x, unit(i), -1)] for i in range(3)]
        for j in range(3):
            r[cidx[("d", x, j)]] = -sum(lap[i] for i in range(3) if i != j)
    for y in sites:
        for (i, j) in PAIRS:
            mixed = N[y] - N[sh(y, unit(i))] - N[sh(y, unit(j))] + N[sh(sh(y, unit(i)), unit(j))]
            r[cidx[("f", y, (i, j))]] = s_face * mixed
    return r


def timing(M, y, i, j, sh, kind):
    c = [y, sh(y, unit(i)), sh(y, unit(j)), sh(sh(y, unit(i)), unit(j))]
    if kind == "mean4":
        return sum(M[z] for z in c) / 4
    if kind == "opp_a":
        return (M[c[0]] + M[c[3]]) / 2
    if kind == "opp_b":
        return (M[c[1]] + M[c[2]]) / 2
    if kind == "corner":
        return M[c[0]]
    raise ValueError(kind)


def bracket_parts(N, M, sites, sh, comps, cidx, kind):
    """bracket coefficient vector on P = a*Ba + b*Bb + f*Bf ; returns (Ba, Bb, Bf)."""
    rN = r1_grad(N, sites, sh, comps, cidx)
    rM = r1_grad(M, sites, sh, comps, cidx)
    Ba = [sp.Rational(0)] * len(comps)
    Bb = [sp.Rational(0)] * len(comps)
    Bf = [sp.Rational(0)] * len(comps)
    for x in sites:
        trN = sum(rN[cidx[("d", x, j)]] for j in range(3))
        trM = sum(rM[cidx[("d", x, j)]] for j in range(3))
        for j in range(3):
            I = cidx[("d", x, j)]
            # d/dP_jj of sum_x M_x H_x  times dR1[N]/dh_jj, minus (N<->M)
            Ba[I] = M[x] * rN[I] - N[x] * rM[I]
            Bb[I] = M[x] * trN - N[x] * trM
    for y in sites:
        for (i, j) in PAIRS:
            I = cidx[("f", y, (i, j))]
            Bf[I] = timing(M, y, i, j, sh, kind) * rN[I] - timing(N, y, i, j, sh, kind) * rM[I]
    return Ba, Bb, Bf


def dm(rows):
    return DomainMatrix([[QQ(int(v.p), int(v.q)) if isinstance(v, sp.Rational) else QQ(v) for v in r]
                         for r in rows], (len(rows), len(rows[0])), QQ)


def closure_space(n, N, M, kind, cache={}):
    if n not in cache:
        cache[n] = build(n)
    sites, sidx, sh, comps, cidx, D = cache[n]
    Ba, Bb, Bf = bracket_parts(N, M, sites, sh, comps, cidx, kind)
    Dm = dm(D)
    # left null space Y of D (rows y with y D = 0)
    Y = Dm.transpose().nullspace()               # rows
    W = Y * dm([list(t) for t in zip(Ba, Bb, Bf)])   # (#Y x 3)
    sol = W.nullspace()
    return Dm.rank(), sol.to_Matrix(), (Ba, Bb, Bf), D


def main():
    random.seed(11)
    # gauge sanity: R1 functional annihilates relabellings
    sites, sidx, sh, comps, cidx, D = build(3)
    N = {x: sp.Rational(random.randint(-3, 3)) for x in sites}
    r = sp.Matrix(r1_grad(N, sites, sh, comps, cidx))
    print("R1 relabelling invariance on 3^3 (D^T r1[N] == 0):", (sp.Matrix(D).T * r).is_zero_matrix)

    print("\n== closure solution space for (a, b, f); expected 1-dim ray (2,-1,1) = DeWitt, eps3 = 0 ==")
    for n in (3, 4, 5):
        sites = list(product(range(n), repeat=3))
        e0 = (0, 0, 0)
        lapses = {
            "delta(0), delta(e1)": ({x: sp.Rational(int(x == e0)) for x in sites},
                                    {x: sp.Rational(int(x == (1, 0, 0))) for x in sites}),
            "delta(0), delta(e1+e2)": ({x: sp.Rational(int(x == e0)) for x in sites},
                                       {x: sp.Rational(int(x == (1, 1, 0))) for x in sites}),
            "random ints": ({x: sp.Rational(random.randint(-5, 5)) for x in sites},
                            {x: sp.Rational(random.randint(-5, 5)) for x in sites}),
            "smooth-ish": ({x: sp.Rational(x[0] * (n - x[0]) + 2 * x[1]) for x in sites},
                           {x: sp.Rational(x[2] * x[2] + x[0]) for x in sites}),
        }
        kinds = ("mean4", "opp_a", "opp_b", "corner") if n == 3 else ("mean4", "corner")
        for kind in kinds:
            for lname, (Nl, Ml) in lapses.items():
                if n == 5 and lname != "random ints":
                    continue
                rk, sol, _, _ = closure_space(n, Nl, Ml, kind)
                rays = [tuple(sol.row(i)) for i in range(sol.rows)]
                print(f"   n={n} timing={kind:6s} lapses={lname:24s}: rank D = {rk}; closing (a,b,f) space dim "
                      f"{sol.rows}: {rays}")
                sys.stdout.flush()

    print("\n== float SVD gap at the B4 script's four kinetic points (n=3, random lapses, mean4) ==")
    sites, sidx, sh, comps, cidx, D = build(3)
    Nl = {x: sp.Rational(random.randint(-5, 5)) for x in sites}
    Ml = {x: sp.Rational(random.randint(-5, 5)) for x in sites}
    Ba, Bb, Bf = bracket_parts(Nl, Ml, sites, sh, comps, cidx, "mean4")
    Df = np.array(D, float)
    sD = np.linalg.svd(Df, compute_uv=False)
    Ba, Bb, Bf = (np.array([float(v) for v in B]) for B in (Ba, Bb, Bf))
    al = 3 / 7
    for label, ad, af, c in (("alpha_d=alpha_f, c=1/2", al, al, 0.5), ("alpha_d=1.1 alpha_f, c=1/2", 1.1 * al, al, 0.5),
                             ("alpha_d=0.8 alpha_f, c=1/2", 0.8 * al, al, 0.5), ("alpha_d=alpha_f, c=1/3", al, al, 1 / 3),
                             ("alpha_d=(1+1e-6) alpha_f", (1 + 1e-6) * al, al, 0.5)):
        a, b, f = 1 / (2 * ad), -c / (2 * ad), 1 / (4 * af)
        br = a * Ba + b * Bb + f * Bf
        s = np.linalg.svd(np.column_stack([Df, br / np.linalg.norm(br) * sD[0]]), compute_uv=False)
        resid = np.linalg.norm(br - Df @ np.linalg.lstsq(Df, br, rcond=None)[0]) / np.linalg.norm(br)
        print(f"   {label:30s}: true eps3 = alpha_f/alpha_d - 1 = {af / ad - 1:+.6f}; sigma_78..80/sigma_1 = "
              f"{s[77] / s[0]:.2e}, {s[78] / s[0]:.2e}, {s[79] / s[0]:.2e}; relative residual outside range(D) {resid:.2e}")

    print("\n== (b) eps3 of alpha tr hdot^2 + beta (tr hdot)^2 ==")
    al_, be_ = sp.symbols("alpha beta")
    print("   M1 = alpha+beta, M2 = 2 beta, M3 = 2 alpha -> eps3 =", sp.simplify(2 * al_ / (2 * (al_ + be_) - 2 * be_) - 1))


if __name__ == "__main__":
    main()
