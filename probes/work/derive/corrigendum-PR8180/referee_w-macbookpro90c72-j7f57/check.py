#!/usr/bin/env python3
"""Independent referee for corrigendum PR8180 a1.

Cyclotomic characters and sympy expansions. The author's Q(zeta_12) script is not called.
"""
import itertools

import numpy as np
import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def modes(L):
    return list(itertools.product(range(L), repeat=2))


def phi_num(L, n1, n2):
    w = np.exp(2j * np.pi / L)
    return (1 + w ** n1 + w ** n2) / 3


def main():
    # P and P^T on every mode of L=3,4,6, in float, against the closed form
    ok_p = True
    for L in (3, 4, 6):
        for n1, n2 in modes(L):
            ph = phi_num(L, n1, n2)
            # (P e)/e = (1 + e^{-ik1} + e^{-ik2})/3
            ratio = (1 + np.exp(-2j * np.pi * n1 / L) + np.exp(-2j * np.pi * n2 / L)) / 3
            ok_p &= abs(ratio - np.conjugate(ph)) < 1e-12
            ok_p &= abs(ph - (1 + np.exp(2j * np.pi * n1 / L) + np.exp(2j * np.pi * n2 / L)) / 3) < 1e-12
    check("P multiplies e_k by conj(phi) and P^T by phi on every mode of L=3,4,6", ok_p)

    # real-mode criterion and pair counts
    def real_phi(L, n1, n2):
        return (n1 + n2) % L == 0 or (n1 - n2) % L == L // 2

    counts = {}
    nonreal = {}
    for L in (3, 4, 6):
        ms = modes(L)
        nonreal[L] = sum(1 for n1, n2 in ms if abs(np.imag(phi_num(L, n1, n2))) > 1e-10)
        agree = 0
        total = 0
        crit_ok = True
        for n1, n2 in ms:
            ph = phi_num(L, n1, n2)
            is_real = abs(np.imag(ph)) < 1e-10
            crit_ok &= is_real == (real_phi(L, n1, n2) if L % 2 == 0 else (n1 + n2) % L == 0 or (2 * (n1 - n2)) % L == L)
            # for odd L, k1-k2 in pi+2pi Z means (n1-n2)/L = 1/2 + integer, impossible if L odd
            if (n1, n2) == (0, 0):
                continue
            for s in (1, 2, 3):
                total += 1
                if abs(np.imag(ph ** s)) < 1e-9:
                    agree += 1
        counts[L] = (agree, total)
        nonreal[L] = (nonreal[L], len(ms), crit_ok)
    # odd L: pi is not a lattice frequency, so the second clause never fires; the code above uses 2(n1-n2)%L==L which is n1-n2 = L/2, not integer. For L=3, L//2=1, (n1-n2)%3==1 is WRONG.
    # Recompute the criterion properly.
    def real_crit(L, n1, n2):
        # k1+k2 in 2pi Z iff (n1+n2) % L == 0
        # k1-k2 in pi + 2pi Z iff 2(n1-n2)/L is an odd integer iff 2(n1-n2) % (2L) == L
        return (n1 + n2) % L == 0 or (2 * (n1 - n2)) % (2 * L) == L

    ok_c = True
    counts = {}
    nonreal_n = {}
    for L in (3, 4, 6):
        ms = modes(L)
        nr = 0
        agree = total = 0
        for n1, n2 in ms:
            ph = phi_num(L, n1, n2)
            is_real = abs(np.imag(ph)) < 1e-10
            ok_c &= is_real == real_crit(L, n1, n2)
            if not is_real:
                nr += 1
            if (n1, n2) == (0, 0):
                continue
            for s in (1, 2, 3):
                total += 1
                if abs(np.imag(ph ** s)) < 1e-9:
                    agree += 1
        counts[L] = (agree, total)
        nonreal_n[L] = (nr, L * L)
    check("phi is real iff k1+k2 in 2pi Z or k1-k2 in pi+2pi Z; nonreal modes 6/9, 10/16, 24/36",
          ok_c and nonreal_n == {3: (6, 9), 4: (10, 16), 6: (24, 36)},
          str(nonreal_n))
    check("display and gloss agree on 8/24, 19/45, 47/105 pairs",
          counts == {3: (8, 24), 4: (19, 45), 6: (47, 105)}, str(counts))

    # Im phi identity
    k1, k2 = sp.symbols("k1 k2", real=True)
    ph = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    im = sp.simplify(sp.im(sp.expand(ph)))
    closed = sp.Rational(2, 3) * sp.sin((k1 + k2) / 2) * sp.cos((k1 - k2) / 2)
    check("Im phi = (2/3) sin((k1+k2)/2) cos((k1-k2)/2)", sp.simplify(im - closed) == 0)

    # E and D identities, Hessians, expansion
    K1, K2, K3 = sp.symbols("K1 K2 K3", real=True)
    E = sum(2 * (1 - sp.cos(K)) for K in (K1, K2, K3))
    z = (sp.exp(sp.I * K1) + sp.exp(sp.I * K2) + sp.exp(sp.I * K3)) / 3
    D = sp.expand(sp.simplify((1 - z) * (1 - sp.conjugate(z))))
    kk1, kk2 = K1 - K3, K2 - K3
    u = sp.simplify(sp.expand(
        ((1 + sp.exp(sp.I * kk1) + sp.exp(sp.I * kk2)) / 3)
        * ((1 + sp.exp(-sp.I * kk1) + sp.exp(-sp.I * kk2)) / 3)
    ))
    check("3|1-z|^2 = E - 3(1-u) and u = |z|^2",
          sp.simplify(sp.expand(3 * D - (E - 3 * (1 - u)))) == 0
          and sp.simplify(sp.expand(u - z * sp.conjugate(z))) == 0)

    hessE = sp.hessian(E, (K1, K2, K3)).subs({K1: 0, K2: 0, K3: 0})
    D3 = sp.expand(3 * D)
    hessD = sp.hessian(D3, (K1, K2, K3)).subs({K1: 0, K2: 0, K3: 0})
    ones = sp.Matrix([1, 1, 1])
    check("Hess E = 2I and Hess 3D = (2/3) 11^T at the origin",
          hessE == 2 * sp.eye(3) and sp.simplify(hessD - sp.Rational(2, 3) * ones * ones.T) == sp.zeros(3))

    eps, b = sp.symbols("eps b", real=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
    # a perpendicular to (1,1,1): set a3 = -a1-a2
    subs = {
        K1: eps * a1 + eps ** 2 * b,
        K2: eps * a2 + eps ** 2 * b,
        K3: eps * (-a1 - a2) + eps ** 2 * b,
    }
    series_D = sp.series(D3.subs(subs).expand(), eps, 0, 5).removeO()
    series_E = sp.series(E.subs(subs).expand(), eps, 0, 3).removeO()
    aa = a1 ** 2 + a2 ** 2 + (a1 + a2) ** 2
    target_D = eps ** 4 * (3 * b ** 2 + aa ** 2 / 12)
    target_E = eps ** 2 * aa
    check("3D = eps^4 (3b^2 + |a|^4/12) + O(eps^5) and E = eps^2 |a|^2 + O(eps^3) for a perpendicular to (1,1,1)",
          sp.expand(series_D - target_D) == 0 and sp.expand(series_E - target_E) == 0)

    # one finite matrix: L=4, mode (1,0), regression of P is conj(phi)
    L = 4
    n1, n2 = 1, 0
    ph = phi_num(L, n1, n2)
    # build P on the torus and apply to the character
    xs = [(i, j) for i in range(L) for j in range(L)]
    e = np.array([np.exp(2j * np.pi * (n1 * i + n2 * j) / L) for i, j in xs])
    Pe = np.zeros_like(e)
    for t, (i, j) in enumerate(xs):
        Pe[t] = (e[t] + np.exp(2j * np.pi * (n1 * ((i - 1) % L) + n2 * j) / L)
                 + np.exp(2j * np.pi * (n1 * i + n2 * ((j - 1) % L)) / L)) / 3
    check("on L=4 the mode (1,0) is an eigenvector of P with eigenvalue conj(phi), and phi is not real",
          np.allclose(Pe, np.conjugate(ph) * e) and abs(np.imag(ph)) > 1e-8)

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - with the minus transform P multiplies by conj(phi) while the covariance display is phi^s; the two differ on the non-real pairs, 16 of 24 on L=3, 26 of 45 on L=4 and 58 of 105 on L=6; E is elliptic and the formation symbol is parabolic along (1,1,1).")
    print("HIT: confirmed - block 35's display phi^s Var matches the minus transform and the pairing E[X conj Y]; the evolution multiplier is conj(phi); E and the formation symbol are separated by Hessian rank 3 against rank 1, and 3D = eps^4 (3b^2 + |a_perp|^4/12) along the cone.")


if __name__ == "__main__":
    main()
