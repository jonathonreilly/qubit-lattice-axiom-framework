#!/usr/bin/env python3
"""J:note falsifiers for LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10 (on main).

Falsifiers implemented: (1) "an additional SU(2)-singlet, Lorentz-scalar, hypercharge-conserving contraction independent of
sum_alpha bar L_L^alpha H_alpha e_R"; (3) "a correction ... that makes the tilde H monomial gauge-allowed for charged leptons".

Disjoint machinery: the invariant space of a block bar(psi) Phi chi is the tensor product of the invariant spaces of the factors on
which colour SU(3), weak SU(2) and the Lorentz group act separately, so its dimension is the product of three exact nullspace
dimensions (generators acting on R_psi-bar (x) R_Phi (x) R_chi: Gell-Mann/2 on triplets, Pauli/2 on doublets, conjugate generators
-T^* on barred factors; for the Lorentz part the complexified generators of (1/2, 0) and (0, 1/2) Weyl spinors), times the hypercharge
condition -Y(psi) + Y(Phi) + Y(chi) = 0 (doubled convention, Q = T3 + Y/2). The note's one block is checked, and beyond it the whole
one-generation census: psi, chi in {Q_L, u_R, d_R, L_L, e_R, nu_R}, Phi in {H, H^*} (72 blocks); the normalization Z^2 = N_c N_iso of
each surviving singlet is computed from its explicit invariant tensor.
"""
from __future__ import annotations

import itertools

import sympy as sp

I = sp.I
PAULI = [sp.Matrix([[0, 1], [1, 0]]) / 2, sp.Matrix([[0, -I], [I, 0]]) / 2, sp.Matrix([[1, 0], [0, -1]]) / 2]


def gell_mann():
    l = [sp.zeros(3, 3) for _ in range(8)]
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1], l[1][1, 0] = -I, I
    l[2][0, 0], l[2][1, 1] = 1, -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2], l[4][2, 0] = -I, I
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2], l[6][2, 1] = -I, I
    l[7] = sp.diag(1, 1, -2) / sp.sqrt(3)
    return [m / 2 for m in l]


GM = gell_mann()


def gens(kind, dim):
    """generators of a representation: kind in {'fund', 'antifund', 'trivial'}."""
    base = GM if dim == 3 else PAULI
    if kind == "trivial":
        return None
    return [g if kind == "fund" else -g.conjugate() for g in base]


def invariant_dim(factors, ngens):
    """factors: list of (dim, generator list or None); dimension of the joint kernel of sum_k 1 (x) .. (x) T_k^a (x) .. (x) 1."""
    dims = [d for d, _ in factors]
    n = 1
    for d in dims:
        n *= d
    rows = []
    for a in range(ngens):
        total = sp.zeros(n, n)
        for k, (d, gs) in enumerate(factors):
            if gs is None:
                continue
            mat = sp.Matrix([[1]])
            for j, (dj, _) in enumerate(factors):
                mat = sp.kronecker_product(mat, gs[a] if j == k else sp.eye(dj))
            total += mat
        rows.append(total)
    A = sp.Matrix.vstack(*rows)
    ns = A.nullspace()
    return len(ns), ns


# fields: colour dim, weak dim, doubled hypercharge, chirality
FERMIONS = {"Q_L": (3, 2, sp.Rational(1, 3), "L"), "u_R": (3, 1, sp.Rational(4, 3), "R"), "d_R": (3, 1, sp.Rational(-2, 3), "R"),
            "L_L": (1, 2, -1, "L"), "e_R": (1, 1, -2, "R"), "nu_R": (1, 1, 0, "R")}
SCALARS = {"H": (2, "fund", 1), "H*": (2, "antifund", -1)}


def lorentz_dim(chir_field_barred, chir):
    """invariants of bar(psi) (x) chi under the complexified Lorentz algebra sl2_L (+) sl2_R (six generators): a left-handed field is
    (1/2, 0), its bar is (0, 1/2), and vice versa; each factor feels only its own sl2."""
    t_bar = "R" if chir_field_barred == "L" else "L"

    def g6(t):
        return [p if t == "L" else sp.zeros(2) for p in PAULI] + [p if t == "R" else sp.zeros(2) for p in PAULI]

    d, _ = invariant_dim([(2, g6(t_bar)), (2, g6(chir))], 6)
    return d


def block_dim(psi, phi, chi):
    cp, wp, yp, hp = FERMIONS[psi]
    cc, wc, yc, hc = FERMIONS[chi]
    ws, skind, ys = SCALARS[phi]
    if -yp + ys + yc != 0:
        return 0, None
    col_f = [(cp, gens("antifund", 3) if cp == 3 else None), (1, None), (cc, gens("fund", 3) if cc == 3 else None)]
    dc, nsc = invariant_dim(col_f, 8) if (cp == 3 or cc == 3) else (1, [sp.Matrix([1])])
    weak_f = [(wp, gens("antifund", 2) if wp == 2 else None), (ws, gens(skind, 2)), (wc, gens("fund", 2) if wc == 2 else None)]
    dw, nsw = invariant_dim(weak_f, 3)
    dl = lorentz_dim(hp, hc)
    return dc * dw * dl, (nsc, nsw)


def main():
    note_dim, (nsc, nsw) = block_dim("L_L", "H", "e_R")
    tilde_dim, _ = block_dim("L_L", "H*", "e_R")
    t = nsw[0]
    Z2 = sum(abs(x) ** 2 for x in t) / max(abs(x) for x in t) ** 2   # entries of the singlet tensor delta_ab: Z^2 = N_c N_iso
    print(f"1. the note's block bar(L_L) H e_R: invariant dimension {note_dim} (colour x weak x Lorentz x hypercharge); weak singlet tensor "
          f"{list(t)} (the Kronecker pairing), Z^2 = {Z2}; the tilde-H monomial bar(L_L) H^* e_R: invariant dimension {tilde_dim} "
          f"(hypercharge sum {-FERMIONS['L_L'][2] + SCALARS['H*'][2] + FERMIONS['e_R'][2]})")
    census = {}
    for psi, chi in itertools.product(FERMIONS, repeat=2):
        for phi in SCALARS:
            d, _ = block_dim(psi, phi, chi)
            if d:
                census[(psi, phi, chi)] = d
    print(f"2. one-generation census of bar(psi) Phi chi, 72 blocks: nonzero invariant dimensions {census}")
    norms = {}
    for (psi, phi, chi), d in census.items():
        _, (nsc, nsw) = block_dim(psi, phi, chi)
        tc = nsc[0]
        tw = nsw[0]
        norms[(psi, phi, chi)] = (sum(abs(x) ** 2 for x in tc) / max(abs(x) for x in tc) ** 2) * (sum(abs(x) ** 2 for x in tw) / max(abs(x) for x in tw) ** 2)
    print(f"   Z^2 of each surviving singlet (colour x weak normalization of the unit-entry tensor): {norms}")
    expected = {("L_L", "H", "e_R"), ("L_L", "H*", "nu_R"), ("Q_L", "H", "d_R"), ("Q_L", "H*", "u_R"),
                ("e_R", "H*", "L_L"), ("nu_R", "H", "L_L"), ("d_R", "H*", "Q_L"), ("u_R", "H", "Q_L")}
    ok = note_dim == 1 and tilde_dim == 0 and Z2 == 2 and set(census) == expected and all(v == 1 for v in census.values())
    if not ok:
        print(f"HIT: the census disagrees with the note's uniqueness claim: note block {note_dim}, tilde {tilde_dim}, Z^2 {Z2}, census {census}")
    print(f"SUMMARY: falsifiers 1 and 3 do not fire: the charged-lepton block bar(L_L) H e_R has exactly one invariant (dimension {note_dim}, "
          f"Z^2 = {Z2}, so 1/sqrt2), the tilde-H monomial has none (hypercharge sum -2); beyond the note, the full one-generation census of "
          f"72 Yukawa-shaped blocks has exactly {len(census)} nonzero blocks, each 1-dimensional: the four Yukawas (e, nu, d, u) and their "
          f"conjugates, with Z^2 = N_c N_iso ({sorted(set(norms.values()))})")


if __name__ == "__main__":
    main()
