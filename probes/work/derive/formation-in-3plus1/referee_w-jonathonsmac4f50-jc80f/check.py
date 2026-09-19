#!/usr/bin/env python3
"""Referee check for J:derive:formation-in-3plus1:a5 (author w-macbookpro90c72-jd7c3, grok-4.6); referee w-jonathonsmac4f50-jc80f.

Independent code (sympy exact). Backward stencil phi(k) = (1 + e^{ik1} + e^{ik2} + e^{ik3})/4; covariance symbol C = 1/(1 - |phi|^2);
causal static response R = 1/(1 - phi); symmetric 7-stencil phi_s = (1 + 2 sum cos k_j)/7.

V1  the DAG property on Z^4 (predecessor sets; no x is a predecessor of its own predecessor), by enumeration on a box.
V2  at k = (pi/2, 0, 0): phi, |phi|^2, C, R, R/C (attempt: (3+i)/4, 5/8, 8/3, 2(1+i), (3/4)(1+i)); the cosine identity for |phi|^2.
V3  'R is a real multiple of C iff phi is real': on all 6^3 modes k in (2 pi/6) Z^3 (exact in Q(sqrt 3, i)), Im(R/C) = 0 exactly where
    Im phi = 0.
V4  the symmetric contrast at the same mode (attempt: 5/7, 7/2, 49/24, 12/7 = 1 + phi_s).
V5  drift: grad phi at 0 = i(1,1,1)/4; grad(1 - |phi|^2) at 0 = 0.
V6  the IR statement 'causal response O(1/|k|)': along k = t(1,1,1)/sqrt3, |R| ~ 4/(sqrt3 t); along k = t(1,-1,0)/sqrt2 (sum k = 0),
    1 - phi = t^2/8 + O(t^3), so |R| ~ 8/t^2 and R/C -> 2 (real) -- the order is direction-dependent.
"""
from __future__ import annotations

import itertools

import sympy as sp


def phi(k):
    return (1 + sum(sp.exp(sp.I * kj) for kj in k)) / 4


def v1():
    box = list(itertools.product(range(3), repeat=4))
    pred = {x: [tuple(x[i] - (1 if i == j else 0) for i in range(4)) for j in range(4)] for x in box}
    two_cycle = any(x in pred.get(y, []) for x in box for y in pred[x])
    level_drop = all(sum(y) == sum(x) - 1 for x in box for y in pred[x])
    return (not two_cycle) and level_drop


def v2():
    k = (sp.pi / 2, 0, 0)
    ph = sp.nsimplify(sp.expand_complex(phi(k)))
    u = sp.nsimplify(sp.simplify(sp.expand_complex(ph * sp.conjugate(ph))))
    C = 1 / (1 - u)
    R = sp.nsimplify(sp.simplify(sp.expand_complex(1 / (1 - ph))))
    ratio = sp.nsimplify(sp.simplify(sp.expand_complex(R / C)))
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    P = phi((k1, k2, k3))
    ident = sp.simplify(sp.expand_trig(sp.expand_complex(P * sp.conjugate(P)) - (2 + sp.cos(k1) + sp.cos(k2) + sp.cos(k3)
                                                                                    + sp.cos(k1 - k2) + sp.cos(k1 - k3) + sp.cos(k2 - k3)) / 8)) == 0
    return ph, u, C, R, ratio, ident


def v3():
    bad = 0
    n = 0
    for m in itertools.product(range(6), repeat=3):
        k = tuple(2 * sp.pi * mi / 6 for mi in m)
        ph = sp.nsimplify(sp.expand_complex(phi(k)))
        if sp.simplify(ph - 1) == 0:
            continue
        u = sp.simplify(sp.expand_complex(ph * sp.conjugate(ph)))
        if sp.simplify(u - 1) == 0:
            continue
        n += 1
        ratio = sp.simplify(sp.expand_complex((1 - u) / (1 - ph)))
        im_ratio_zero = sp.simplify(sp.im(ratio)) == 0
        im_phi_zero = sp.simplify(sp.im(ph)) == 0
        bad += im_ratio_zero != im_phi_zero
    return n, bad


def v4():
    k = (sp.pi / 2, 0, 0)
    ps = sp.nsimplify((1 + 2 * sum(sp.cos(kj) for kj in k)) / 7)
    Rs = 1 / (1 - ps)
    Cs = 1 / (1 - ps ** 2)
    return ps, Rs, Cs, sp.simplify(Rs / Cs), sp.simplify(Rs / Cs - (1 + ps)) == 0


def v5():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    P = phi((k1, k2, k3))
    g = [sp.simplify(sp.diff(P, v).subs({k1: 0, k2: 0, k3: 0})) for v in (k1, k2, k3)]
    U = sp.expand_complex(P * sp.conjugate(P))
    gu = [sp.simplify(sp.diff(1 - U, v).subs({k1: 0, k2: 0, k3: 0})) for v in (k1, k2, k3)]
    return g, gu


def v6():
    t = sp.Symbol("t", positive=True)
    k_diag = tuple(t / sp.sqrt(3) for _ in range(3))
    k_plane = (t / sp.sqrt(2), -t / sp.sqrt(2), 0)
    one_minus_diag = sp.series(sp.expand_complex(1 - phi(k_diag)), t, 0, 3).removeO()
    one_minus_plane = sp.series(sp.expand_complex(1 - phi(k_plane)), t, 0, 3).removeO()
    P = phi(k_plane)
    u_plane = sp.series(sp.expand_complex(1 - P * sp.conjugate(P)), t, 0, 3).removeO()
    ratio_limit = sp.limit(sp.simplify(u_plane / one_minus_plane), t, 0)
    return sp.simplify(one_minus_diag), sp.simplify(one_minus_plane), sp.simplify(u_plane), ratio_limit


def main():
    dag = v1()
    print(f"V1 backward 4-predecessor relation on a 3^4 box: no 2-cycles and every edge lowers the level by 1: {dag}")
    ph, u, C, R, ratio, ident = v2()
    print(f"V2 k=(pi/2,0,0): phi = {ph}; |phi|^2 = {u}; C = {C}; R = {R}; R/C = {ratio}; cosine identity for |phi|^2: {ident}")
    n, bad = v3()
    print(f"V3 'R/C real iff phi real' on {n} modes of (2 pi/6)Z^3 (zero mode and |phi| = 1 excluded): mismatches {bad}")
    ps, Rs, Cs, rs, ok4 = v4()
    print(f"V4 symmetric 7-stencil at (pi/2,0,0): phi_s = {ps}, R_s = {Rs}, C_s = {Cs}, R_s/C_s = {rs} = 1 + phi_s: {ok4}")
    g, gu = v5()
    print(f"V5 grad phi(0) = {g}; grad(1 - |phi|^2)(0) = {gu}")
    od, op, up, lim = v6()
    print(f"V6 along (1,1,1)/sqrt3: 1 - phi = {od} + O(t^3) (so |R| ~ 1/t); along (1,-1,0)/sqrt2: 1 - phi = {op} + O(t^3), 1 - |phi|^2 = {up}, "
          f"R/C -> {lim} (so |R| ~ 8/t^2 there)")
    ok = (dag and ph == sp.Rational(3, 4) + sp.I / 4 and u == sp.Rational(5, 8) and C == sp.Rational(8, 3) and sp.simplify(R - 2 - 2 * sp.I) == 0
          and sp.simplify(ratio - sp.Rational(3, 4) * (1 + sp.I)) == 0 and ident and bad == 0 and ps == sp.Rational(5, 7)
          and rs == sp.Rational(12, 7) and ok4 and g == [sp.I / 4] * 3 and gu == [0, 0, 0])
    if ok:
        print("HIT: confirmed - the backward 4-predecessor stencil is a DAG; at k = (pi/2,0,0) phi = (3+i)/4, |phi|^2 = 5/8, C = 8/3, "
              f"R = 2(1+i), R/C = (3/4)(1+i); on all {n} modes of (2 pi/6)Z^3 R/C is real exactly where phi is real; the symmetric 7-stencil gives "
              "5/7, 7/2, 49/24, 12/7 = 1 + phi_s; drift grad phi(0) = i(1,1,1)/4 with grad(1 - |phi|^2)(0) = 0; all exact")
        print(f"SUMMARY: confirmed - the task-(d) partial survives; correction: 'the causal response is O(1/|k|)' holds off the plane k1+k2+k3 = 0 "
              f"only: on that plane 1 - phi = t^2/8 + O(t^3), so |R| ~ 8/|k|^2 and R/C -> {lim} (real) at small k; sphere LRO and S(k) bounds "
              "are not claimed, as the attempt says")
    else:
        print("SUMMARY: fails at step 2 - an exact value does not re-derive (see the lines above)")


if __name__ == "__main__":
    main()
