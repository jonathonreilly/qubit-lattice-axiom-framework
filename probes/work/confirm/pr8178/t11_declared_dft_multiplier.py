#!/usr/bin/env python3
"""J:confirm:J-attack-f-PR8178 -- independent test of block 34's T1.1 multiplier against its declared transform (PR #8178).

The note declares theta^_k = L^-1 sum_x e^{-ik.x} theta_x and P theta_x = (theta_x + theta_{x-e1} + theta_{x-e2})/3, and T1.1 states
(P theta)^_k = phi(k) theta^_k with phi(k) = (1 + e^{ik1} + e^{ik2})/3 (its proof: 'each shift multiplies theta^_k by e^{-ik.e};
the conjugate convention gives the stated phi').

Machinery (the finder compared mode lists for L = 2, 3, 4):
  1. the symbolic shift rule: sum_x e^{-ik.x} theta_{x-e} = e^{-ik.e} sum_y e^{-ik.y} theta_y for a generic periodic field
     (sympy, L = 5, symbolic k on the grid, symbolic theta values);
  2. full diagonalization on L = 4 in exact Gaussian rationals (sympy DomainMatrix over QQ_I): F P F^-1 with the DECLARED
     F_{k,x} = L^-1 e^{-ik.x}; its diagonal against the stated phi and its conjugate; the off-diagonal entries;
  3. the parts of T1 that use only |phi|^2: T1.2's identity and T1.3's mode variances from the exact covariance recursion
     Sigma_{t+1} = P Sigma_t P^T + I on L = 4, read in the declared transform.
"""
from __future__ import annotations

import itertools

import sympy as sp
from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix


def part1(L=5):
    th = sp.symbols(f"t0:{L * L}")
    ok = True
    for n1, n2 in itertools.product(range(L), repeat=2):
        w = sp.exp(-2 * sp.pi * sp.I / L)
        hat = lambda f: sum(w ** (n1 * i + n2 * j) * f(i, j) for i in range(L) for j in range(L))
        base = hat(lambda i, j: th[(i % L) * L + (j % L)])
        for di, dj in ((1, 0), (0, 1)):
            shifted = hat(lambda i, j: th[((i - di) % L) * L + ((j - dj) % L)])
            ok &= sp.simplify(sp.expand(shifted - w ** (n1 * di + n2 * dj) * base)) == 0
    return ok


I_POW = [QQ_I(1, 0), QQ_I(0, 1), QQ_I(-1, 0), QQ_I(0, -1)]  # i^m ; e^{i 2 pi m/4} = i^m


def conj(z):
    return QQ_I(z.x, -z.y)


def part2(L=4):
    N = L * L
    zero = QQ_I(0, 0)
    idx = lambda i, j: (i % L) * L + (j % L)
    rows = [[zero] * N for _ in range(N)]
    for i, j in itertools.product(range(L), repeat=2):
        for di, dj in ((0, 0), (-1, 0), (0, -1)):
            rows[idx(i, j)][idx(i + di, j + dj)] += QQ_I(QQ(1, 3), 0)
    P = DomainMatrix(rows, (N, N), QQ_I)
    modes = list(itertools.product(range(L), repeat=2))
    xs = list(itertools.product(range(L), repeat=2))
    # declared transform: F[k, x] = L^-1 e^{-ik.x} = L^-1 i^{-(n.x)}; inverse G[x, k] = L^-1 e^{+ik.x}
    F = DomainMatrix([[I_POW[(-(n[0] * x[0] + n[1] * x[1])) % 4] * QQ_I(QQ(1, L), 0) for x in xs] for n in modes], (N, N), QQ_I)
    G = DomainMatrix([[I_POW[(n[0] * x[0] + n[1] * x[1]) % 4] * QQ_I(QQ(1, L), 0) for n in modes] for x in xs], (N, N), QQ_I)
    assert (F * G).to_list() == DomainMatrix.eye(N, QQ_I).to_dense().to_list()
    Dm = (F * P * G).to_list()
    off = sum(1 for a in range(N) for b in range(N) if a != b and Dm[a][b] != zero)
    stated, conj_count, differ, witness = 0, 0, 0, None
    for m, n in enumerate(modes):
        phi = (QQ_I(1, 0) + I_POW[n[0] % 4] + I_POW[n[1] % 4]) / QQ_I(3, 0)  # (1 + e^{ik1} + e^{ik2})/3
        got = Dm[m][m]
        stated += got == phi
        conj_count += got == conj(phi)
        if phi != conj(phi):
            differ += 1
            if witness is None and got != phi:
                witness = (n, phi, got)
    return off, stated, conj_count, differ, len(modes), witness


def part3(L=4, T=6):
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    lhs = sp.simplify(sp.expand_complex(1 - phi * sp.conjugate(phi)))
    rhs = sp.Rational(4, 9) * (sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2)
    t12 = sp.simplify(sp.expand_trig(lhs - rhs)) == 0
    # mode variances from the exact covariance recursion, read in the declared transform (exact rationals, sympy)
    N = L * L
    idx = lambda i, j: (i % L) * L + (j % L)
    P = sp.zeros(N, N)
    for i, j in itertools.product(range(L), repeat=2):
        for di, dj in ((0, 0), (-1, 0), (0, -1)):
            P[idx(i, j), idx(i + di, j + dj)] += sp.Rational(1, 3)
    Sig = sp.zeros(N, N)
    ok = True
    for t in range(1, T + 1):
        Sig = P * Sig * P.T + sp.eye(N)
        for n1, n2 in itertools.product(range(L), repeat=2):
            f = sp.Matrix([sp.exp(-2 * sp.pi * sp.I * (n1 * i + n2 * j) / L) / L for i in range(L) for j in range(L)])
            var = sp.nsimplify(sp.simplify((f.H * Sig * f)[0]))
            ph = (1 + sp.exp(2 * sp.pi * sp.I * n1 / L) + sp.exp(2 * sp.pi * sp.I * n2 / L)) / 3
            u = sp.nsimplify(sp.simplify(sp.expand_complex(ph * sp.conjugate(ph))))
            want = t if u == 1 else sp.simplify((1 - u ** t) / (1 - u))
            ok &= sp.simplify(var - want) == 0
    return t12, ok


def main():
    p1 = part1()
    print(f"1. shift rule under the declared transform (L = 5, every mode, symbolic field): sum e^(-ik.x) theta_(x-e) = e^(-ik.e) theta^: {p1}")
    off, stated, conj_count, differ, nm, witness = part2()
    n, phi, got = witness
    print(f"2. L = 4, F P F^-1 with the declared F (Gaussian rationals): off-diagonal nonzeros {off}; diagonal = stated phi on "
          f"{stated}/{nm} modes, = conj(phi) on {conj_count}/{nm}; phi non-real on {differ} modes; witness n = {n}: stated "
          f"phi = {phi.x}+{phi.y}i, declared-transform multiplier = {got.x}+{got.y}i")
    t12, t13 = part3()
    print(f"3. T1.2 identity (uses |phi|^2 only): {t12}; T1.3 mode variances sigma^2 (1-u^t)/(1-u), t <= 6, all 16 modes, from the "
          f"exact covariance recursion in the declared transform: {t13}")
    if p1 and off == 0 and conj_count == nm and stated == nm - differ and differ > 0:
        print(f"HIT: confirmed - under the declared theta^_k = L^-1 sum e^(-ik.x) theta_x the three-predecessor P multiplies by "
              f"(1 + e^(-ik1) + e^(-ik2))/3 = conj(phi): exact on L = 4 ({conj_count}/{nm} modes conj(phi), {stated}/{nm} the stated "
              f"phi = exactly the {nm - differ} modes where phi is real; e.g. n = {n}: stated {phi.x}+{phi.y}i vs {got.x}+{got.y}i); "
              f"T1.1's statement holds only in the conjugate transform its proof mentions; |phi|^2 is unchanged, so T1.2 and T1.3 "
              f"stand (checked exactly)")
        print("SUMMARY: confirmed - T1.1 states phi = (1 + e^(ik1) + e^(ik2))/3 against a declared e^(-ik.x) transform; the declared "
              "multiplier is its conjugate (presentation: declare the + transform or state phi with e^(-ik)); no effect on the |phi|^2 results")
    else:
        print(f"SUMMARY: not reproduced - shift {p1}, off {off}, stated {stated}, conj {conj_count}")


if __name__ == "__main__":
    main()
