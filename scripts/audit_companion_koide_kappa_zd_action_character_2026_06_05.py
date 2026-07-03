#!/usr/bin/env python3
"""Audit companion for
`KOIDE_KAPPA_ZD_ACTION_CIRCULANT_CHARACTER_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-05`.

Missing-bridge-theorem repair for the audited_conditional row
`koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10`.

The conditional verdict on that row was:

  "T4 and the isotype labels require a specific nontrivial Z_d conjugation
   action on the circulant basis, but the packet never defines that action;
   conjugation by the explicitly defined cyclic shift would be trivial on
   Herm_circ(d)."

This runner INSTANTIATES the action explicitly and proves the character-k
decomposition (it does NOT only count pairs):

  Define omega = exp(2 pi i / d), the clock matrix
  Omega = diag(1, omega, ..., omega^{d-1}), and the Z_d action
  rho(M) = Omega^{-1} M Omega on M_d(C) (restricted to Herm_circ(d)).

  (C1) rho is a faithful, non-trivial Z_d representation on Herm_circ(d)
       (distinct from the TRIVIAL shift-conjugation C M C^{-1} = M).
  (C2) rho(C^k) = omega^k C^k -- the C^k line carries character k.
  (C3) Hermiticity ties a_{d-k} = conj(a_k); the conjugate pair {k, d-k}
       (k != d-k) combines into a 2-real-dim doublet V_k on which rho acts as
       planar rotation by 2 pi k / d (eq. (6) of the note).
  (C4) for even d, rho(C^{d/2}) = - C^{d/2}: the sign irrep; rho(I) = I: trivial.
  (C5) real-irrep multiplicities (1, floor((d-1)/2), [d even]); dimension count
       1 + 2 floor((d-1)/2) + [d even] = d = dim_R Herm_circ(d); the
       (1, (1,), 0) pattern is realized uniquely at d = 3 in {2,3,4,5,6}.

All load-bearing facts are reproven from the explicit matrices C, Omega and
the root-of-unity arithmetic; no numerical comparator is imported, and no
audit files are written. Cyclic-group character theory (Serre; Fulton-Harris)
is cited in the note as a comparator only.

Exact arithmetic is done in sympy with omega = exp(2 pi i / d) represented
symbolically (sympy applies the minimal-polynomial / nsimplify-free exact
simplification via `expand_complex` + `simplify` over the cyclotomic field).
A numpy floating cross-check is run in parallel as a guard.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import sympy as sp
    from sympy import (
        I, pi, exp, Rational, Matrix, eye, zeros, simplify, expand,
        conjugate, nsimplify, sin, cos, symbols, re as sp_re, im as sp_im,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("FAIL: numpy required for the floating cross-check")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}  ({detail})")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ---------------------------------------------------------------------------
# Exact symbolic building blocks.
# ---------------------------------------------------------------------------

def omega_sym(d):
    """Exact primitive d-th root of unity omega = exp(2 pi i / d)."""
    return exp(2 * I * pi / d)


def shift_matrix(d):
    """d x d cyclic permutation C with C[i, (i+1) mod d] = 1 (exact 0/1)."""
    C = zeros(d, d)
    for i in range(d):
        C[i, (i + 1) % d] = 1
    return C


def clock_matrix(d):
    """Omega = diag(1, omega, ..., omega^{d-1}) with exact symbolic omega."""
    w = omega_sym(d)
    return sp.diag(*[w ** j for j in range(d)])


def csimp(M):
    """Exact simplification helper for symbolic-root-of-unity matrices."""
    return sp.expand_complex(M).rewrite(exp).simplify()


def mat_zero(M):
    """True iff every entry of M simplifies to exactly 0."""
    M = sp.expand_complex(M)
    return all(simplify(e) == 0 for e in M)


def mat_eq(A, B):
    return mat_zero(A - B)


def power(M, k):
    """Integer matrix power (k >= 0)."""
    out = eye(M.shape[0])
    for _ in range(k):
        out = out * M
    return out


# ---------------------------------------------------------------------------
section("Z_d action on Herm_circ(d): explicit instantiation and character-k bridge")
# ---------------------------------------------------------------------------

DS = (3, 4, 5, 6)

for d in DS:
    print(f"\n=== d = {d} ===")
    w = omega_sym(d)
    C = shift_matrix(d)
    Omega = clock_matrix(d)
    Omega_inv = clock_matrix(d).inv()  # diag(1, omega^{-1}, ...)
    Id = eye(d)

    def rho(M):
        return Omega_inv * M * Omega

    Cpows = [power(C, k) for k in range(d)]

    # -- (Validation 1) C^d = I, C unitary, tr(C^k) = 0 for 0 < k < d. ------
    check(f"[d={d}] C^d = I", mat_eq(power(C, d), Id), detail="cyclic shift cubes/etc to I")
    check(f"[d={d}] C unitary (C^H C = I)", mat_eq(C.conjugate().T * C, Id),
          detail="permutation matrix is unitary")
    tr_ok = all(simplify(sp.trace(Cpows[k])) == 0 for k in range(1, d))
    check(f"[d={d}] tr(C^k) = 0 for 0 < k < d", tr_ok, detail="shifts are traceless")

    # -- (Validation 2) Omega unitary, Omega^d = I. ------------------------
    check(f"[d={d}] Omega unitary", mat_eq(csimp(Omega.conjugate().T * Omega), Id),
          detail="diagonal unit-modulus entries")
    check(f"[d={d}] Omega^d = I", mat_eq(csimp(power(Omega, d)), Id),
          detail="omega^{d}=1 on every diagonal entry")

    # -- (Validation 3) Shift-conjugation is TRIVIAL (the trap, eq (S)). ----
    Cinv = C.conjugate().T
    shift_trivial = all(mat_eq(C * Cpows[k] * Cinv, Cpows[k]) for k in range(d))
    check(f"[d={d}] shift-conjugation C M C^-1 = M is TRIVIAL on every C^k (eq (S))",
          shift_trivial, detail="circulants commute with C -> no character structure")

    # -- (Validation 4) rho is a non-trivial Z_d representation. -----------
    check(f"[d={d}] rho(I) = I", mat_eq(csimp(rho(Id)), Id), detail="identity preserved")
    # homomorphism on a sample pair (j=1, k=2) and generally on all (j,k):
    hom_ok = all(
        mat_eq(csimp(rho(Cpows[j] * Cpows[k]) - rho(Cpows[j]) * rho(Cpows[k])), zeros(d, d))
        for j in range(d) for k in range(d)
    )
    check(f"[d={d}] rho(MN) = rho(M)rho(N) on all C^j, C^k", hom_ok, detail="conjugation is a homomorphism")
    # rho^d = id on all basis elements:
    def rho_n(M, n):
        out = M
        for _ in range(n):
            out = rho(out)
        return out
    order_ok = all(mat_eq(csimp(rho_n(Cpows[k], d) - Cpows[k]), zeros(d, d)) for k in range(d))
    check(f"[d={d}] rho^d = id (order d)", order_ok, detail="Omega^d = I")
    # Hermiticity preserved on a generic Hermitian circulant.
    # Build H with symbolic real a0 and real/imag parts of a_k.
    herm_pres_ok = True
    for k in range(d):
        Bk = Cpows[k]
        rBk = rho(Bk)
        # rho maps C^k to a multiple of C^k, and rho(M^H) = rho(M)^H:
        if not mat_eq(csimp(rho(Bk.conjugate().T) - rBk.conjugate().T), zeros(d, d)):
            herm_pres_ok = False
    check(f"[d={d}] rho(M^H) = rho(M)^H (Hermiticity-preserving)", herm_pres_ok,
          detail="Omega unitary")
    # non-trivial: rho(C^1) != C^1.
    nontrivial = not mat_eq(csimp(rho(Cpows[1]) - Cpows[1]), zeros(d, d))
    check(f"[d={d}] rho is NOT the identity (rho(C^1) = omega C^1 != C^1)", nontrivial,
          detail="distinct from shift-conjugation")

    # -- (Validation 5) Character-k: rho(C^k) = omega^k C^k. ---------------
    char_ok = True
    for k in range(d):
        lhs = csimp(rho(Cpows[k]))
        rhs = csimp((w ** k) * Cpows[k])
        if not mat_eq(lhs - rhs, zeros(d, d)):
            char_ok = False
    check(f"[d={d}] rho(C^k) = omega^k C^k for all k (character-k line) [C2]",
          char_ok, detail="exact symbolic root-of-unity identity")

    # Action matrix in the {C^0,...,C^{d-1}} basis is diag(1, omega, ..., omega^{d-1}).
    # Verified entry-wise: the coefficient of C^k in rho(C^k) is omega^k, others 0.
    action_diag_ok = True
    for k in range(d):
        # rho(C^k) = omega^k C^k; coefficient vector in the C-power basis is e_k * omega^k.
        # Compare to expected by extracting the (0, k) entry (C^k has a 1 at (0,k)).
        coeff = rho(Cpows[k])[0, k]
        if simplify(sp.expand_complex(coeff - w ** k)) != 0:
            action_diag_ok = False
    check(f"[d={d}] action matrix in C-power basis = diag(1, omega, ..., omega^{{d-1}})",
          action_diag_ok, detail="eigenvalues are the d characters")

    # -- (Validation 6) Doublets V_k for conjugate pairs {k, d-k}, k != d-k. -
    pairs = [k for k in range(1, d) if k != (d - k) % d and k < (d - k) % d]
    for k in pairs:
        kk = (d - k) % d
        Ck = Cpows[k]
        Cdk = Cpows[kk]
        B1 = Ck + Cdk
        B2 = I * (Ck - Cdk)
        # Hermitian.
        h1 = mat_eq(csimp(B1.conjugate().T - B1), zeros(d, d))
        h2 = mat_eq(csimp(B2.conjugate().T - B2), zeros(d, d))
        check(f"[d={d}] B1^(k={k}) = C^k + C^(d-k) Hermitian", h1, detail="real symmetric")
        check(f"[d={d}] B2^(k={k}) = i(C^k - C^(d-k)) Hermitian", h2,
              detail="pure-imaginary off-diagonals")
        # rho|_V_k is rotation by t = 2 pi k / d:
        t = 2 * pi * k / d
        rB1 = csimp(rho(B1))
        rB2 = csimp(rho(B2))
        rot1 = mat_eq(csimp(rB1 - (cos(t) * B1 + sin(t) * B2)), zeros(d, d))
        rot2 = mat_eq(csimp(rB2 - (-sin(t) * B1 + cos(t) * B2)), zeros(d, d))
        check(f"[d={d}] rho|_V_(k={k}) is rotation by 2pi*{k}/{d} (eq (6)) [C3]",
              rot1 and rot2, detail="real 2-dim doublet irrep")
        # Hermitian parametrization a_k C^k + conj(a_k) C^{d-k} = p B1 + q B2,
        # with a_k = p + i q (p = Re a_k, q = Im a_k, both real). Verify symbolically.
        p, q = symbols("p q", real=True)
        a_k = p + I * q
        lhs = a_k * Ck + conjugate(a_k) * Cdk
        rhs = p * B1 + q * B2
        param_ok = mat_eq(csimp(lhs - rhs), zeros(d, d))
        check(f"[d={d}] Hermitian pair a_k C^k + conj(a_k) C^(d-k) = p B1 + q B2 (in V_k)",
              param_ok, detail="Hermiticity constraint = membership in V_k")

    # -- (Validation 7) Sign irrep at k = d/2 for even d. ------------------
    if d % 2 == 0:
        kh = d // 2
        Csign = Cpows[kh]
        sign_ok = mat_eq(csimp(rho(Csign) - (-1) * Csign), zeros(d, d))
        herm_sign = mat_eq(csimp(Csign.conjugate().T - Csign), zeros(d, d))
        real_sign = all(simplify(sp_im(e)) == 0 for e in Csign)
        check(f"[d={d}] rho(C^(d/2)) = -C^(d/2) (sign irrep, omega^(d/2) = -1) [C4]",
              sign_ok, detail="even d only")
        check(f"[d={d}] C^(d/2) Hermitian and real", herm_sign and real_sign,
              detail="real symmetric line")
    else:
        check(f"[d={d}] no sign irrep (d odd: no k with k = d-k mod d)",
              all(k != (d - k) % d for k in range(1, d)), detail="odd d")

    # -- (Validation 8) Trivial irrep at k = 0. ----------------------------
    check(f"[d={d}] rho(I) = I (trivial irrep, k=0)", mat_eq(csimp(rho(Id)), Id),
          detail="omega^0 = 1")

    # -- (Validation 9) Dimension count and explicit real basis. -----------
    n_doublets = (d - 1) // 2
    sign = 1 if d % 2 == 0 else 0
    dim_formula = 1 + 2 * n_doublets + sign
    check(f"[d={d}] 1 + 2*floor((d-1)/2) + [d even] = d", dim_formula == d,
          detail=f"{1} + 2*{n_doublets} + {sign} = {dim_formula}")

    # Build the explicit real basis of Herm_circ(d) from the irrep pieces and
    # verify it is linearly independent over R with d elements and spans.
    real_basis = [Id]  # trivial
    for k in pairs:
        kk = (d - k) % d
        real_basis.append(Cpows[k] + Cpows[kk])        # B1
        real_basis.append(I * (Cpows[k] - Cpows[kk]))  # B2
    if d % 2 == 0:
        real_basis.append(Cpows[d // 2])               # sign

    check(f"[d={d}] explicit real basis has d = {d} elements", len(real_basis) == d,
          detail="1 + 2*doublets + sign")

    # Linear independence over R: flatten each Hermitian matrix into its real
    # coordinates (real diagonal + real/imag of upper triangle) and check rank.
    def real_coords(M):
        M = sp.expand_complex(M)
        coords = []
        n = M.shape[0]
        for i in range(n):
            coords.append(simplify(sp_re(M[i, i])))
        for i in range(n):
            for j in range(i + 1, n):
                coords.append(simplify(sp_re(M[i, j])))
                coords.append(simplify(sp_im(M[i, j])))
        return coords

    coord_matrix = Matrix([real_coords(B) for B in real_basis])
    rank = coord_matrix.rank()
    check(f"[d={d}] real basis is linearly independent over R (rank = d)", rank == d,
          detail=f"rank = {rank}")

    # Span: a generic Hermitian circulant is a real combination of the basis.
    # Build H_generic = a0 I + sum over pairs (p_k B1 + q_k B2) + (s C^{d/2})
    # and confirm it is a generic Hermitian circulant (Hermitian + circulant).
    a0 = symbols("a0", real=True)
    H_generic = a0 * Id
    for idx, k in enumerate(pairs):
        kk = (d - k) % d
        pk, qk = symbols(f"p{k} q{k}", real=True)
        H_generic = H_generic + pk * (Cpows[k] + Cpows[kk]) + qk * (I * (Cpows[k] - Cpows[kk]))
    if d % 2 == 0:
        s = symbols("s", real=True)
        H_generic = H_generic + s * Cpows[d // 2]
    herm_generic = mat_eq(csimp(H_generic.conjugate().T - H_generic), zeros(d, d))
    # circulant: commutes with C.
    circ_generic = mat_eq(csimp(H_generic * C - C * H_generic), zeros(d, d))
    check(f"[d={d}] real-basis combination spans Hermitian circulants (Hermitian + circulant)",
          herm_generic and circ_generic, detail="generic element is Hermitian circulant")

    # -- numpy floating cross-check of character-k (guard against symbolic typos)
    wn = np.exp(2j * np.pi / d)
    Cn = np.zeros((d, d), dtype=complex)
    for i in range(d):
        Cn[i, (i + 1) % d] = 1.0
    On = np.diag([wn ** j for j in range(d)])
    On_inv = np.diag([wn ** (-j) for j in range(d)])
    char_num_ok = True
    for k in range(d):
        Ckn = np.linalg.matrix_power(Cn, k)
        lhs = On_inv @ Ckn @ On
        rhs = (wn ** k) * Ckn
        if not np.allclose(lhs, rhs, atol=1e-10):
            char_num_ok = False
    check(f"[d={d}] numpy cross-check: Omega^-1 C^k Omega = omega^k C^k", char_num_ok,
          detail="floating guard on the exact identity")


# ---------------------------------------------------------------------------
section("Validation 10: multiplicity table for d = 2..6 and d=3 uniqueness of (1,(1,),0)")
# ---------------------------------------------------------------------------

def multiplicity_pattern(d):
    trivial = 1
    n_doublets = (d - 1) // 2
    sign = 1 if d % 2 == 0 else 0
    return (trivial, tuple([1] * n_doublets), sign)

expected_patterns = {
    2: (1, (), 1),
    3: (1, (1,), 0),
    4: (1, (1,), 1),
    5: (1, (1, 1), 0),
    6: (1, (1, 1), 1),
}
for d in (2, 3, 4, 5, 6):
    got = multiplicity_pattern(d)
    exp_pat = expected_patterns[d]
    # dimension consistency check too.
    dim = 1 + 2 * len(got[1]) + got[2]
    check(f"Herm_circ(d={d}) multiplicity = {exp_pat}, dim = {dim} = d",
          got == exp_pat and dim == d, detail=f"got {got}")

unique_d = [d for d in (2, 3, 4, 5, 6) if multiplicity_pattern(d) == (1, (1,), 0)]
check("d = 3 is the unique d in {2,3,4,5,6} with pattern (1, (1,), 0)",
      unique_d == [3], detail=f"d's with (1,(1,),0): {unique_d}")


# ---------------------------------------------------------------------------
section("Narrow theorem summary")
# ---------------------------------------------------------------------------
print("""
  Z_d action on Herm_circ(d): rho(M) = Omega^{-1} M Omega,
  Omega = diag(1, omega, ..., omega^{d-1}), omega = exp(2 pi i / d).

  Bridge facts proven (NOT just pair-counting):
    (S)  Shift-conjugation C M C^{-1} = M is TRIVIAL on Herm_circ(d) -- the
         trap the conditional verdict flagged; the genuine action is rho.
    (C1) rho is a faithful non-trivial Z_d representation on Herm_circ(d).
    (C2) rho(C^k) = omega^k C^k -- the C^k line carries character k.
    (C3) Hermiticity (a_{d-k} = conj(a_k)) ties {k, d-k} into a 2-real-dim
         doublet V_k; rho|_V_k = rotation by 2 pi k / d.
    (C4) even d: rho(C^{d/2}) = -C^{d/2} (sign irrep); rho(I) = I (trivial).
    (C5) multiplicities (1, floor((d-1)/2), [d even]); dimension 1 + 2*doublets
         + [d even] = d; pattern (1, (1,), 0) realized uniquely at d = 3.

  Repairs missing_bridge_theorem for
  koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10.
  No PDG / fitted / lattice-MC / beta=6 / g_bare inputs; no audit files written.
""")

print(f"\n{'='*88}\n  TOTAL: {PASS} PASS / {FAIL} FAIL\n{'='*88}")
sys.exit(1 if FAIL > 0 else 0)
