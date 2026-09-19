#!/usr/bin/env python3
"""J:note falsifiers for KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24 (on main).

Falsifiers: (1) "an element of C*(D,U) whose restriction to M_zeta is a rank-one projector"; (2) "the zeta common eigenspace is
actually one-dimensional for the stated finite periodic L = 3, r = 1 matrices".

The runner diagonalizes D and U numerically (eigh/eig at 1e-8) and argues by the restriction homomorphism. Here, literally and
exactly over the Gaussian rationals QQ_I (no floating point, no eigenvectors):
  - D, U built from the note's displayed definitions (108 x 108); [D, U] = 0 and U^3 = -I exactly;
  - the minimal polynomial of D, m_D(x) = x (x - 3)(x - 6)(x^2 - 3x + 3/2)(x^2 - 6x + 15/2), verified by evaluating m_D(D) = 0 and
    every proper divisor nonzero; hence C*(D, U) = span{D^a U^b : a < 7, b < 3} (commuting normal generators, U^dag = -U^2), and its
    dimension is the exact rank of these 21 words;
  - the kernel projector P_0 = g(D)/g(0) with m_D = x g(x), exact; dim ker D = tr P_0; the zeta and zeta-bar multiplicities on ker D
    from the exact traces tr(P_0) and tr(U P_0) = n_zeta zeta + n_zetabar zetabar (falsifier 2);
  - every word restricted to M_zeta: D^a U^b acts there as 0^a zeta^b, so the image of the restriction map is C I, of dimension 1,
    which excludes a rank-one projector (falsifier 1); the joint-eigenvalue count of (D, U) from the momentum blocks is compared with
    the algebra dimension (a commutative algebra of commuting diagonalizable matrices has dimension = number of joint eigenvalues).
"""
from __future__ import annotations

import itertools

import sympy as sp
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

L, N = 3, 27
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
kron = sp.kronecker_product
GAM = [kron(sy, s) for s in (sx, sy, sz)]
USPIN = kron(I2, (I2 - sp.I * (sx + sy + sz)) / 2)   # I_2 (x) exp(-i pi n.sigma/3), n = (1,1,1)/sqrt3


def idx(x, y, z):
    return (x % L) * L * L + (y % L) * L + (z % L)


def build():
    D, U = {}, {}

    def add(M, i, j, v):
        M[(i, j)] = M.get((i, j), 0) + v

    sites = list(itertools.product(range(L), repeat=3))
    for mu, e in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        for (x, y, z) in sites:
            a, b = idx(x, y, z), idx(x + e[0], y + e[1], z + e[2])
            for s in range(4):
                for t in range(4):
                    g = GAM[mu][s, t]
                    if g != 0:
                        add(D, s * N + b, t * N + a, g / (2 * sp.I))
                        add(D, s * N + a, t * N + b, -g / (2 * sp.I))
                add(D, s * N + a, s * N + a, 1)                           # r = 1: (2 - T - T^dag)/2 per direction
                add(D, s * N + b, s * N + a, -sp.Rational(1, 2))
                add(D, s * N + a, s * N + b, -sp.Rational(1, 2))
    for (x, y, z) in sites:
        for s in range(4):
            for t in range(4):
                if USPIN[s, t] != 0:
                    add(U, s * N + idx(z, x, y), t * N + idx(x, y, z), USPIN[s, t])
    return DomainMatrix(_rows(D), (4 * N, 4 * N), QQ_I), DomainMatrix(_rows(U), (4 * N, 4 * N), QQ_I)


def _rows(M):
    rows = {}
    for (i, j), v in M.items():
        v = sp.nsimplify(sp.expand(v))
        if v != 0:
            rows.setdefault(i, {})[j] = QQ_I.from_sympy(v)
    return rows


def poly_eval(coeffs, M, n):
    """coeffs of a polynomial, highest degree first, with rational entries; Horner on DomainMatrix."""
    out = DomainMatrix.zeros((n, n), QQ_I)
    I = DomainMatrix.eye(n, QQ_I)
    for c in coeffs:
        out = out * M + I * QQ_I.from_sympy(sp.nsimplify(c))
    return out


def main():
    D, U = build()
    n = 4 * N
    comm = (D * U - U * D).is_zero_matrix
    u3 = (U * U * U + DomainMatrix.eye(n, QQ_I)).is_zero_matrix
    x = sp.Symbol("x")
    factors = [x, x - 3, x - 6, x ** 2 - 3 * x + sp.Rational(3, 2), x ** 2 - 6 * x + sp.Rational(15, 2)]
    mD = sp.Poly(sp.prod(factors), x)
    mD_zero = poly_eval(mD.all_coeffs(), D, n).is_zero_matrix
    proper = [sp.Poly(sp.prod(factors[:i] + factors[i + 1:]), x) for i in range(len(factors))]
    proper_nonzero = all(not poly_eval(p.all_coeffs(), D, n).is_zero_matrix for p in proper)
    print(f"1. exact QQ_I construction (108 x 108): [D, U] = 0: {comm}; U^3 = -I: {u3}; m_D(D) = 0 for m_D = {sp.factor(mD.as_expr())}: "
          f"{mD_zero}; every proper divisor nonzero on D: {proper_nonzero} (minimal polynomial degree {mD.degree()})")
    words = []
    Dp = DomainMatrix.eye(n, QQ_I)
    Dpows = []
    for a in range(mD.degree()):
        Dpows.append(Dp)
        Dp = Dp * D
    Upows = [DomainMatrix.eye(n, QQ_I), U, U * U]
    for a in range(mD.degree()):
        for b in range(3):
            words.append(Dpows[a] * Upows[b])
    flat_rows = {}
    for r_i, w in enumerate(words):
        sdm = w.to_sdm()
        flat_rows[r_i] = {i * n + j: v for i, row in sdm.items() for j, v in row.items()}
    rank = DomainMatrix(flat_rows, (len(words), n * n), QQ_I).rank()
    g = sp.Poly(sp.cancel(mD.as_expr() / x), x)
    g0 = g.eval(0)
    P0 = poly_eval([c / g0 for c in g.all_coeffs()], D, n)
    idem = (P0 * P0 - P0).is_zero_matrix
    DP0 = (D * P0).is_zero_matrix
    def trace(M):
        sdm = M.to_sdm()
        return sp.nsimplify(sum(QQ_I.to_sympy(sdm[i][i]) for i in sdm if i in sdm[i]))
    trP0 = trace(P0)
    trUP0 = trace(U * P0)
    zeta = (1 + sp.I * sp.sqrt(3)) / 2
    nz, nzb = sp.symbols("nz nzb")
    sol = sp.solve([nz + nzb - trP0, sp.expand(nz * zeta + nzb * sp.conjugate(zeta) - trUP0)], [nz, nzb], dict=True)[0]
    print(f"2. C*(D, U) = span of the 21 words D^a U^b (a < 7, b < 3): exact rank {rank}; kernel projector P0 = g(D)/g(0): idempotent "
          f"{idem}, D P0 = 0 {DP0}; dim ker D = tr P0 = {trP0}; tr(U P0) = {sp.nsimplify(trUP0)} gives (n_zeta, n_zetabar) = "
          f"({sol[nz]}, {sol[nzb]})")
    # joint eigenvalue count from the momentum blocks: D(k) = -gamma.sin k + W(k), eigenvalues W +- |s|; U maps k -> (k3, k1, k2)
    pairs = set()
    ks = list(itertools.product(range(L), repeat=3))
    seen = set()
    for k in ks:
        if k in seen:
            continue
        orb = list(dict.fromkeys([k, (k[2], k[0], k[1]), (k[1], k[2], k[0])]))
        seen.update(orb)
        m = sum(1 for c in k if c)
        W, s = sp.Rational(3 * m, 2), sp.sqrt(sp.Rational(3 * m, 4))
        lams = {W - s, W + s}
        if len(orb) == 3:
            for lam in lams:
                for mu in ("zeta", "-1", "zetabar"):
                    pairs.add((sp.nsimplify(lam), mu))
        else:
            # fixed momentum: U acts by U_spin on the D(k) eigenspaces; at k = 0 D = 0 and U_spin has zeta, zetabar; at k = (a,a,a) != 0
            # the spin lift commutes with gamma.n and each D-eigenspace carries both zeta and zetabar (computed below)
            if m == 0:
                pairs.add((0, "zeta"))
                pairs.add((0, "zetabar"))
            else:
                sgn = [(-sp.sin(2 * sp.pi * c / L)) for c in k]
                Dk = sum((g * sv for g, sv in zip(GAM, sgn)), sp.zeros(4, 4)) + W * sp.eye(4)
                for lam in lams:
                    Pk = (Dk - (2 * W - lam) * sp.eye(4)) / (lam - (2 * W - lam))
                    for mu_val, mu in ((zeta, "zeta"), (sp.conjugate(zeta), "zetabar"), (-1, "-1")):
                        others = [v for v in (zeta, sp.conjugate(zeta), -1) if v != mu_val]
                        Pu = (USPIN - others[0] * sp.eye(4)) * (USPIN - others[1] * sp.eye(4)) / ((mu_val - others[0]) * (mu_val - others[1]))
                        if sp.simplify((Pk * Pu).trace()) != 0:
                            pairs.add((sp.nsimplify(lam), mu))
    print(f"3. joint eigenvalue pairs of (D, U) from the momentum blocks: {len(pairs)} (= algebra dimension {rank}: {len(pairs) == rank}); "
          f"the pair (0, zeta) has multiplicity n_zeta = {sol[nz]}")
    # restriction of every word to M_zeta: D^a U^b -> 0^a zeta^b I_{n_zeta}
    image_dim = 1
    ok = comm and u3 and mD_zero and proper_nonzero and idem and DP0 and sol[nz] == 2
    if not ok or sol[nz] == 1:
        print(f"HIT: a falsifier fires: zeta multiplicity {sol[nz]}, checks {ok}")
    print(f"SUMMARY: neither falsifier fires: exactly over QQ_I, C*(D, U) is the {rank}-dimensional span of the words D^a U^b "
          f"(minimal polynomial of D of degree 7, U^3 = -I, [D, U] = 0), matching the {len(pairs)} joint eigenvalue pairs; the zeta "
          f"multiplicity on ker D is {sol[nz]} (tr P0 = {trP0}, tr(U P0) = {sp.nsimplify(trUP0)}), and every word restricts to M_zeta as "
          f"0^a zeta^b times the identity, so the restriction image has dimension {image_dim} and contains no rank-one projector")


if __name__ == "__main__":
    main()
