#!/usr/bin/env python3
"""J:note falsifier for KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24 (on main).

Falsifier implemented: "a retained non-scalar boundary mark on the rank-two zero-mode character multiplicity space" M_zeta.
The note's scalar premise is bridged by KOIDE_RETAINED_WILSON_APS_SCALAR_ACTION_ON_RANK_TWO_MULTIPLICITY_BRIDGE_NARROW_THEOREM_NOTE_
2026-05-16: every element of A = C*(D, U) (polynomials in D, U, U^dag, P_lambda(D)) restricts to a scalar on M_zeta, for the L = 3
periodic Wilson construction of the sibling runner (D = sum_mu gamma_mu (x) (T_mu - T_mu^dag)/(2i) + r (x)_mu (2 - T_mu - T_mu^dag)/2,
gamma_mu = sigma_y (x) sigma_mu, U = U_spin (x) P_site, the body-diagonal 120-degree rotation), at r = 1 and r = 1.425.

Disjoint machinery, exact arithmetic (the runners use numpy eigh / eig at tolerance 1e-8):
  1. position space over the Gaussian rationals QQ_I (sparse DomainMatrix): D, U built from their definitions; [D, U] = 0 exactly,
     rank D exactly (so dim ker D), the constant spinor fields in ker D, and the literal restriction of the generators of A to M_zeta
     (computed with sqrt(3) exactly on the 108-dim vectors); the candidates built from the same construction that commute with D and U:
     the Clifford volume element Gamma = -i gamma_1 gamma_2 gamma_3 (x) 1, the body-diagonal translation T_x T_y T_z, and the symmetric
     hopping sum_mu (T_mu + T_mu^dag); their restrictions to M_zeta. L = 3 at r = 1, 57/40, 1/3; L = 2, 4 as cross-checks.
  2. momentum space (beyond the note's size): L = 2..6, r = 1 and 57/40 (and L = 3, r = 1/3): exact zero-mode test W^2 = |s|^2 per
     momentum (minimal polynomials), dim ker D, rank of M_zeta from the R-orbits of the momenta, and the spectra of Gamma, T_x T_y T_z
     and the hopping sum on M_zeta.
HIT only for the note's own premise at its own sizes (L = 3, r in {1, 57/40}): [D,U] != 0, dim ker D != 4, rank M_zeta != 2, or a
generator of A non-scalar on M_zeta. Operators outside A are reported as numbers (the sibling and bridge notes record Gamma).
"""
from __future__ import annotations

import itertools

import sympy as sp
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

X = sp.Symbol("X")
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I2, I4 = sp.eye(2), sp.eye(4)
kron = sp.kronecker_product
GAM = [kron(sy, s) for s in (sx, sy, sz)]
VOL = sp.expand(-sp.I * GAM[0] * GAM[1] * GAM[2])
USIG = (I2 - sp.I * (sx + sy + sz)) / 2
USPIN = kron(I2, USIG)
ZETA = (1 + sp.I * sp.sqrt(3)) / 2
ZBAR = (1 - sp.I * sp.sqrt(3)) / 2
PZETA = sp.simplify((USPIN - ZBAR * I4) / (ZETA - ZBAR))


def exact_zero(e):
    e = sp.expand(e)
    return e == 0 or sp.minimal_polynomial(e, X) == X


# ---------------------------------------------------------------- position space over QQ_I
def site_ops(L):
    idx = lambda x, y, z: (x % L) * L * L + (y % L) * L + (z % L)
    sites = list(itertools.product(range(L), repeat=3))
    unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def acc(d, i, j, v):
        d[(i, j)] = d.get((i, j), 0) + v

    K, T, W, S = [], [], {}, {}
    for e in unit:
        k, t = {}, {}
        for (x, y, z) in sites:
            a, b = idx(x, y, z), idx(x + e[0], y + e[1], z + e[2])
            acc(t, b, a, 1)
            acc(k, b, a, 1 / (2 * sp.I))
            acc(k, a, b, -1 / (2 * sp.I))
            acc(W, a, a, 1)
            acc(W, b, a, -sp.Rational(1, 2))
            acc(W, a, b, -sp.Rational(1, 2))
            acc(S, b, a, 1)
            acc(S, a, b, 1)
        K.append(k)
        T.append(t)
    P = {(idx(z, x, y), idx(x, y, z)): 1 for (x, y, z) in sites}
    TD = {(idx(x + 1, y + 1, z + 1), idx(x, y, z)): 1 for (x, y, z) in sites}
    return len(sites), K, W, P, TD, S


def skron(A, B, N):
    out = {}
    for a in range(A.rows):
        for b in range(A.cols):
            if A[a, b] != 0:
                for (i, j), v in B.items():
                    out[(a * N + i, b * N + j)] = out.get((a * N + i, b * N + j), 0) + A[a, b] * v
    return out


def dm(d, n):
    rows = {}
    for (i, j), v in d.items():
        v = sp.nsimplify(sp.expand(v))
        if v != 0:
            rows.setdefault(i, {})[j] = QQ_I.from_sympy(v)
    return DomainMatrix(rows, (n, n), QQ_I)


def addd(*ds):
    out = {}
    for d in ds:
        for k, v in d.items():
            out[k] = out.get(k, 0) + v
    return out


def position_space(L, r):
    N, K, W, P, TD, S = site_ops(L)
    n = 4 * N
    Dd = addd(*[skron(g, k, N) for g, k in zip(GAM, K)], {k: r * v for k, v in skron(I4, W, N).items()})
    D, U = dm(Dd, n), dm(skron(USPIN, P, N), n)
    G, Td, Sh = dm(skron(VOL, {(i, i): 1 for i in range(N)}, N), n), dm(skron(I4, TD, N), n), dm(skron(I4, S, N), n)
    comm = lambda A, B: (A * B - B * A).is_zero_matrix
    checks = {"[D,U]": comm(D, U), "[Gamma,D]": comm(G, D), "[Gamma,U]": comm(G, U), "[TxTyTz,D]": comm(Td, D), "[TxTyTz,U]": comm(Td, U),
              "[hop,D]": comm(Sh, D), "[hop,U]": comm(Sh, U), "U^3=-1": (U * U * U + DomainMatrix.eye(n, QQ_I)).is_zero_matrix}
    rank = D.rank()
    return N, n, D, U, checks, rank


def restrict_L3(r, full=True):
    """literal restriction at L = 3 of the A generators and the three candidates to M_zeta = (zeta-space of U_spin) (x) constants."""
    N, n, D, U, checks, rank = position_space(3, r)
    if not full:
        return checks, rank, n, None, None, None, None
    Dm, Um = D.to_Matrix(), U.to_Matrix()
    consts = [sp.Matrix([1 if k // N == a else 0 for k in range(n)]) for a in range(4)]
    consts_in_kernel = all((Dm * c).is_zero_matrix for c in consts)
    chis = (USPIN - ZETA * I4).nullspace()
    basis = []
    for chi in chis:
        v = sp.Matrix([chi[k // N] for k in range(n)])
        basis.append(v)
    Bm = sp.Matrix.hstack(*basis)
    gram = sp.simplify(Bm.H * Bm)
    pinv = gram.inv() * Bm.H
    restrict = lambda A: sp.simplify(pinv * (A * Bm))
    invariant = lambda A: sp.simplify(A * Bm - Bm * restrict(A)).is_zero_matrix
    N_, K, W, P, TD, S = site_ops(3)
    G = sp.Matrix(dm(skron(VOL, {(i, i): 1 for i in range(N)}, N), n).to_Matrix())
    Td = sp.Matrix(dm(skron(I4, TD, N), n).to_Matrix())
    Sh = sp.Matrix(dm(skron(I4, S, N), n).to_Matrix())
    gens = {"D (so P_0(D) -> 1, P_lambda(D) -> 0 for lambda != 0)": (Dm, sp.Integer(0)), "U": (Um, ZETA), "U^dag": (Um.H, ZBAR)}
    res = {}
    for name, (A, want) in gens.items():
        R2 = restrict(A)
        val = sp.simplify(sp.expand_complex(sp.radsimp(R2[0, 0])))
        res[name] = (invariant(A), R2, val, exact_zero(R2[0, 1]) and exact_zero(R2[1, 0]) and exact_zero(R2[0, 0] - want)
                     and exact_zero(R2[1, 1] - want))
    cand = {}
    for name, A in (("Gamma", G), ("TxTyTz", Td), ("hop", Sh)):
        R2 = restrict(A)
        cand[name] = (invariant(A), R2, sorted(R2.eigenvals().items(), key=lambda t: sp.default_sort_key(t[0])))
    return checks, rank, n, consts_in_kernel, len(chis), res, cand


# ---------------------------------------------------------------- momentum space
def momentum_table(L, r):
    ks = list(itertools.product(range(L), repeat=3))
    cache = {}
    info = {}
    for k in ks:
        key = tuple(sorted(min(c, L - c) for c in k))
        if key not in cache:
            p = [2 * sp.pi * c / L for c in key]
            Wv = r * sum(1 - sp.cos(q) for q in p)
            s2 = sum(sp.sin(q) ** 2 for q in p)
            cache[key] = (Wv, s2, exact_zero(Wv ** 2 - s2), exact_zero(Wv))
        info[k] = cache[key]
    zero = [k for k in ks if info[k][2]]
    dim_ker = sum(4 if info[k][3] else 2 for k in zero)
    Rmap = lambda k: (k[2], k[0], k[1])
    seen, orbits = set(), []
    for k in zero:
        if k in seen:
            continue
        orb = [k, Rmap(k), Rmap(Rmap(k))]
        orb = list(dict.fromkeys(orb))
        seen.update(orb)
        orbits.append(orb)
    mz = 0
    gam_plus = 0
    td_vals, hop_vals = [], []
    for orb in orbits:
        k = orb[0]
        p = [2 * sp.pi * c / L for c in k]
        s = [-sp.sin(q) for q in p]
        Wv = info[k][0]
        if info[k][3]:
            Pi = I4
        else:
            Pi = (I4 - sum((g * si for g, si in zip(GAM, s)), sp.zeros(4, 4)) / Wv) / 2
        assert (sp.simplify((sum((g * si for g, si in zip(GAM, s)), sp.zeros(4, 4)) + Wv * I4) * Pi)).is_zero_matrix
        if len(orb) == 3:
            proj = Pi
        else:
            proj = Pi * PZETA
        m = sp.nsimplify(sp.simplify(proj.trace()))
        gp = sp.nsimplify(sp.simplify((m + (VOL * proj).trace()) / 2))
        mz += m
        gam_plus += gp
        hop = sum(2 * sp.cos(q) for q in p)
        if m:
            td_vals.append(sum(k) % L)
            hop_vals.append(hop)
    reps = []
    for v in hop_vals:
        if not any(exact_zero(v - w) for w in reps):
            reps.append(v)
    return dim_ker, int(mz), len(orbits), int(gam_plus), len(set(td_vals)), len(reps)


def main():
    fails = []
    print("1. position space over QQ_I (exact), L = 3 (the note's construction):")
    l3 = {}
    for r in (sp.Integer(1), sp.Rational(57, 40), sp.Rational(1, 3)):
        checks, rank, n, consts_in_kernel, nchi, res, cand = restrict_L3(r, full=(r != sp.Rational(1, 3)))
        l3[r] = (checks, rank, n, nchi, res, cand)
        print(f"   r = {r}: commutators/identities {checks}; rank D = {rank} of {n} -> dim ker D = {n - rank}; constant spinor fields in ker D: "
              f"{consts_in_kernel}; dim zeta-space of U_spin = {nchi}")
        if r in (1, sp.Rational(57, 40)):
            for name, (inv, R2, val, scal) in res.items():
                print(f"      A generator {name}: preserves M_zeta {inv}; restriction = ({val}) I_2 exactly: {scal}")
                if not (inv and scal):
                    fails.append(f"L=3 r={r} {name}")
            for name, (inv, R2, ev) in cand.items():
                print(f"      outside A, commutes with D and U: {name}: preserves M_zeta {inv}; restriction {R2.tolist()}; eigenvalues {ev}")
            if not (all(checks.values()) and n - rank == 4 and nchi == 2):
                fails.append(f"L=3 r={r} premise")
    for L, r in ((2, sp.Integer(1)), (4, sp.Integer(1)), (4, sp.Rational(57, 40))):
        N, n, D, U, checks, rank = position_space(L, r)
        print(f"   cross-check L = {L}, r = {r}: commutators/identities all hold {all(checks.values())}; dim ker D = {n - rank} (of {n})")
        l3[(L, r)] = n - rank
    print("2. momentum space, exact per momentum (beyond the note's size): L, r -> dim ker D, rank M_zeta, R-orbits, "
          "Gamma=+1 multiplicity on M_zeta, distinct TxTyTz values, distinct hopping values")
    table = {}
    for L in (2, 3, 4, 5, 6):
        for r in (sp.Integer(1), sp.Rational(57, 40)) + ((sp.Rational(1, 3),) if L == 3 else ()):
            table[(L, r)] = momentum_table(L, r)
            dk, mz, no, gp, dtd, dh = table[(L, r)]
            print(f"   L={L} r={r}: dim ker D {dk}; rank M_zeta {mz}; orbits {no}; Gamma=+1 on M_zeta {gp} of {mz}; TxTyTz distinct {dtd}; "
                  f"hopping distinct {dh}")
    agree = all(table[(L, r)][0] == l3[(L, r)] for (L, r) in ((2, 1), (4, 1), (4, sp.Rational(57, 40)))) and all(
        table[(3, r)][0] == l3[r][2] - l3[r][1] for r in (sp.Integer(1), sp.Rational(57, 40), sp.Rational(1, 3)))
    print(f"   momentum-space dim ker D equals the position-space exact rank count at every cross-checked (L, r): {agree}")
    if not agree:
        fails.append("position/momentum disagreement")

    rank2 = sorted(f"L={L},r={r}" for (L, r), v in table.items() if v[1] == 2)
    not2 = sorted(f"L={L},r={r}: {v[1]}" for (L, r), v in table.items() if v[1] != 2)
    g = l3[sp.Integer(1)][5]["Gamma"][2]
    if fails:
        print(f"HIT: the note's premise fails at its own size: {fails}")
        print("SUMMARY: falsifier fired; see the HIT line")
    else:
        print(f"SUMMARY: the falsifier does not fire for A = C*(D,U): at L = 3, r = 1 and 57/40, exactly [D,U] = 0, dim ker D = 4 (constant "
              f"spinors), rank M_zeta = 2 and D, U, U^dag restrict to 0, zeta, zeta_bar times I_2 (so every P_lambda(D) to 0 or 1); outside A, the construction's "
              f"Clifford volume element Gamma commutes with D and U exactly and restricts to M_zeta with eigenvalues {g} (the sibling/bridge "
              f"notes' counter-route), while TxTyTz and the hopping sum restrict to scalars; beyond the note's size the rank-two premise holds at "
              f"{', '.join(rank2)} and fails at {'; '.join(not2)} (accidental Wilson zero modes), where TxTyTz and the hopping sum also split "
              f"M_zeta")


if __name__ == "__main__":
    main()
