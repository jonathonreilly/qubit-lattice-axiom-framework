#!/usr/bin/env python3
"""Referee of J:derive:re-recording:a4 (author w-macbookpro90c72-j0cfe, grok-4.6); referee w-jonathonsmac4f50-jf4b6
(claude-opus-5). Independent machinery (exact integers/rationals, sympy), none of the author's code.

Six-axis menu {+-e_i} as vectors; Boltzmann rule e^{beta s.S} with e^beta = 3 is the product rule phi = (3, 1/3, 1)
(same, opposite, orthogonal); integer weights (9, 1, 3) after multiplying every factor by 3.

Q1  the pairing identity sum_x s'_x . S_x(s) = sum_x s_x . S_x(s') for all configuration pairs on C4 (six-axis)
Q2  asynchronous detailed balance mu(s) K(a | S_x) = mu(s_{x<-a}) K(s_x | S_x) for every configuration, site and value
    on C4 and on the 2x2 torus (multiplicity 2), Boltzmann e^beta = 3 and product (3, 1, 2)
Q3  synchronous detailed balance pi(s) P(s -> s') = pi(s') P(s' -> s) with pi = prod_x Z_x(s), all pairs on C4
Q4  TV(pi, mu) on C4 and on the 2x2 torus, exactly, against the author's values
Q5  step 5 on the sphere: sum_x (|S_x| - 6) and sum_bonds (s.s' - 1) for a single transverse Fourier mode on (Z/4)^3,
    exact series in the amplitude: coefficients -E + E^2/12 and -E/2, so pi's quadratic form is twice the static one
    (transverse variance 1/(2 beta E) against 1/(beta E)); the stated 'stiffness 2 beta against beta/2' is a factor 4
Q6  the C4 ratio diagnostic of step 6 (all +z against one opposite flip) at p = 2, 3, 5, 7
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}")


MENU = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def phi_factory(p, q, r):
    def phi(a, b):
        d = dot(a, b)
        return p if d == 1 else (q if d == -1 else r)
    return phi


# graphs as neighbour lists with multiplicity (a list may repeat a neighbour)
C4 = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
T22 = {}
for x in range(2):
    for y in range(2):
        i = 2 * x + y
        T22[i] = [2 * ((x + 1) % 2) + y, 2 * ((x - 1) % 2) + y, 2 * x + (y + 1) % 2, 2 * x + (y - 1) % 2]


def S_of(conf, G, x):
    return tuple(sum(conf[y][c] for y in G[x]) for c in range(3))


def mu_weight(conf, G, phi):
    # product over ordered neighbour pairs, square-rooted by counting each unordered bond once per multiplicity:
    # every bond {x, y} appears in G[x] and in G[y] the same number of times; take ordered pairs with x < y
    w = Fraction(1)
    for x in G:
        for y in G[x]:
            if x < y:
                w *= phi(conf[x], conf[y])
    return w


def cond_unnorm(a, conf, G, x, phi):
    w = Fraction(1)
    for y in G[x]:
        w *= phi(a, conf[y])
    return w


def q1():
    confs = list(itertools.product(MENU, repeat=4))
    ok = True
    for s in confs[::7]:
        for s2 in confs:
            lhs = sum(dot(s2[x], S_of(s, C4, x)) for x in C4)
            rhs = sum(dot(s[x], S_of(s2, C4, x)) for x in C4)
            if lhs != rhs:
                ok = False
                break
    check("Q1", ok, f"step 1: the pairing identity holds for {len(confs[::7]) * len(confs)} configuration pairs on C4 "
          "(six-axis vectors, one of every seven first configurations against all 1296 second ones)")


def q2():
    ok = True
    n = 0
    for G, name in ((C4, "C4"), (T22, "T2x2")):
        for (p, q, r), lab in (((Fraction(3), Fraction(1, 3), Fraction(1)), "Boltzmann e^beta=3"),
                               ((Fraction(3), Fraction(1), Fraction(2)), "(3,1,2)")):
            phi = phi_factory(p, q, r)
            for conf in itertools.product(MENU, repeat=len(G)):
                mu_s = mu_weight(conf, G, phi)
                for x in G:
                    Zx = sum(cond_unnorm(a, conf, G, x, phi) for a in MENU)
                    for a in MENU:
                        new = list(conf)
                        new[x] = a
                        mu_new = mu_weight(tuple(new), G, phi)
                        lhs = mu_s * cond_unnorm(a, conf, G, x, phi) / Zx
                        rhs = mu_new * cond_unnorm(conf[x], tuple(new), G, x, phi) / Zx
                        ok = ok and lhs == rhs
                        n += 1
    check("Q2", ok, f"step 2: asynchronous detailed balance mu(s) K(a|S_x) = mu(s_x<-a) K(s_x|S_x) at every (configuration, "
          f"site, value), {n} cases on C4 and the 2x2 torus for Boltzmann e^beta = 3 and product (3, 1, 2); the static "
          "weight counts each bond with its multiplicity")


def sync_weights(G, phi):
    confs = list(itertools.product(MENU, repeat=len(G)))
    Zs = {}
    for s in confs:
        prodZ = Fraction(1)
        for x in G:
            prodZ *= sum(cond_unnorm(a, s, G, x, phi) for a in MENU)
        Zs[s] = prodZ
    return confs, Zs


def q3():
    phi = phi_factory(Fraction(3), Fraction(1, 3), Fraction(1))
    confs, Zs = sync_weights(C4, phi)
    ok = True
    cnt = 0
    for s in confs[::5]:
        for s2 in confs[::3]:
            # pi(s) P(s -> s') = prod_x phi-product(s'_x | S_x(s)) (normalizers cancel against pi)
            lhs = Fraction(1)
            rhs = Fraction(1)
            for x in C4:
                lhs *= cond_unnorm(s2[x], s, C4, x, phi)
                rhs *= cond_unnorm(s[x], s2, C4, x, phi)
            ok = ok and lhs == rhs
            cnt += 1
    check("Q3", ok, f"step 3: pi(s) P(s -> s') = pi(s') P(s' -> s) with pi = prod_x Z_x(s) on C4, Boltzmann e^beta = 3, "
          f"{cnt} configuration pairs (every fifth against every third)")


def tv_exact(G, phi):
    confs, Zs = sync_weights(G, phi)
    mus = {s: mu_weight(s, G, phi) for s in confs}
    zp = sum(Zs.values())
    zm = sum(mus.values())
    tv = sum(abs(Zs[s] / zp - mus[s] / zm) for s in confs) / 2
    ratios = {Zs[s] / mus[s] for s in confs}
    return tv, len(ratios)


def q4():
    phi = phi_factory(Fraction(3), Fraction(1, 3), Fraction(1))
    tv_c4, nr_c4 = tv_exact(C4, phi)
    tv_t, nr_t = tv_exact(T22, phi)
    ok = tv_c4 == Fraction(39161524, 79474827) and tv_t == Fraction(122900831405716, 159789899835723) and nr_c4 == 14 and nr_t == 14
    check("Q4", ok, f"step 4: TV(pi, mu) = {tv_c4} on C4 and {tv_t} on the 2x2 torus (14 distinct ratios pi/mu on each), "
          "the author's values")


def q5():
    eps = sp.symbols("epsilon", positive=True)
    L = 4
    ok = True
    rows = []
    for kv in ((1, 0, 0), (1, 1, 0), (2, 1, 1), (1, 2, 3)):
        k = tuple(sp.pi * sp.Rational(2 * c, L) for c in kv)
        Ek = sum(2 * (1 - sp.cos(kj)) for kj in k)
        sites = list(itertools.product(range(L), repeat=3))

        def spin(x):
            th = eps * sp.cos(sum(k[j] * x[j] for j in range(3)))
            return (th, 0, sp.sqrt(1 - th ** 2))
        spins = {x: spin(x) for x in sites}
        nbr = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        sumS = 0
        sumB = 0
        for x in sites:
            S = [0, 0, 0]
            for e in nbr:
                y = tuple((x[j] + e[j]) % L for j in range(3))
                for c in range(3):
                    S[c] += spins[y][c]
            sumS += sp.sqrt(S[0] ** 2 + S[1] ** 2 + S[2] ** 2)
            for e in nbr[::2]:
                y = tuple((x[j] + e[j]) % L for j in range(3))
                sumB += sum(spins[x][c] * spins[y][c] for c in range(3))
        N = L ** 3
        norm = N * eps ** 2 / 2          # sum_x theta_x^2 for a cosine mode = sum_k |theta_k|^2 (both +-k)
        cS = sp.nsimplify(sp.simplify(sp.series(sumS - 6 * N, eps, 0, 3).removeO().coeff(eps, 2) * eps ** 2 / norm))
        cB = sp.nsimplify(sp.simplify(sp.series(sumB - 3 * N, eps, 0, 3).removeO().coeff(eps, 2) * eps ** 2 / norm))
        ok = ok and sp.simplify(cS - (-Ek + Ek ** 2 / 12)) == 0 and sp.simplify(cB + Ek / 2) == 0
        rows.append(f"k = 2pi{kv}/4: E = {sp.nsimplify(Ek)}, sum(|S|-6) coefficient {cS}, sum_bonds coefficient {cB}")
    check("Q5", ok,
          "step 5 on the sphere, exact series for a single transverse cosine mode on (Z/4)^3: sum_x(|S_x| - 6) has "
          "coefficient -E + E^2/12 and sum_bonds(s.s' - 1) has -E/2 per |theta_k|^2 (" + "; ".join(rows) + "). So "
          "-log pi = beta E |theta_k|^2 + ... and -log mu = (beta/2) E |theta_k|^2 + ...: the synchronous law's quadratic "
          "form is TWICE the static one, transverse variance 1/(2 beta E) against block 19's 1/(beta E). The attempt's "
          "'stiffness 2 beta against the static law's beta/2' states a factor 4 and does not match its own exponents "
          "(beta vs beta/2)")


def q6():
    ok = True
    rows = []
    for pv in (2, 3, 5, 7):
        p = Fraction(pv)
        phi = phi_factory(p, 1 / p, Fraction(1))
        up = (0, 0, 1)
        down = (0, 0, -1)
        aligned = (up, up, up, up)
        flip = (down, up, up, up)

        def Zprod(conf):
            w = Fraction(1)
            for x in C4:
                w *= sum(cond_unnorm(a, conf, C4, x, phi) for a in MENU)
            return w
        r_sync = Zprod(aligned) / Zprod(flip)
        r_static = mu_weight(aligned, C4, phi) / mu_weight(flip, C4, phi)
        ok = ok and r_static == p ** 4
        rows.append(f"p = {pv}: static {r_static}, synchronous {r_sync}")
    want = {2: Fraction(121, 64), 3: Fraction(3481, 729), 5: Fraction(14641, 625), 7: Fraction(187489, 2401)}
    ok = ok and all(f"synchronous {want[pv]}" in row for pv, row in zip((2, 3, 5, 7), rows))
    check("Q6", ok, "step 6: the C4 ratios of the all-+z weight to a one-site opposite flip, " + "; ".join(rows)
          + " (the author's values); a four-site ratio is not an ordering statement on Z^3, and step 6 marks the Peierls "
          "step ASSUMED, so the sentence '(b) ... The chain orders in the same sense as the static law at large beta' is "
          "not proved")


def main():
    try:
        q1()
        q2()
        q3()
        q4()
        q5()
        q6()
    except Exception as exc:
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: referee check.py crashed")
        return 1
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS:
        print("SUMMARY: referee checks failed (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 5 - its conclusion 'IR stiffness 2 beta against the static law's beta/2' (repeated in the "
          "HIT and SUMMARY lines) does not follow from its own exponents: pi ~ exp(-beta sum E|theta_k|^2) against "
          "mu ~ exp(-(beta/2) sum E|theta_k|^2) is a factor 2 (transverse variance 1/(2 beta E) against 1/(beta E)), not 4; "
          "and (b)'s 'the chain orders in the same sense as the static law' is not proved (a C4 ratio, Peierls ASSUMED). "
          "Everything else survives and was re-verified independently: the pairing identity, asynchronous detailed "
          "balance on C4 and the 2x2 torus for both rules, synchronous reversibility w.r.t. prod_x Z_x, the exact TV "
          "values 39161524/79474827 and 122900831405716/159789899835723, the spin-wave jet -E + E^2/12, the C4 ratios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
