#!/usr/bin/env python3
"""Exact-precision audit-companion runner for
`HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`.

The narrow theorem isolates the algebraic-clean half of the parent
`PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md`,
restricted to the matrix-level Hermitian-lift identities

    (L1)  Theta_H := P K is an antiunitary involution on V_lat
    (L2)  Theta_H H Theta_H^{-1} = H   for H = i D
    (L3)  H_odd := (H - Theta_H H Theta_H^{-1}) / 2 = 0_{V_lat}
    (L4)  Direction-resolved sectors H_{mu, odd} = 0 for each mu

on the framework's specific staggered hopping operator D (real
anti-Hermitian, real entries +/- 1/2 only) and framework C, P on the
periodic cubic lattice Lambda = (Z mod L)^3, even L.

The runner does NOT verify any SME bilinear operator dictionary;
that is the parent bridge note's open conditional and is explicitly
out of scope (see Item 10).

Pattern A: every load-bearing check is an exact matrix-level identity
in either sympy (1-d slice for symbolic certainty) or numpy with
integer/rational arithmetic (the framework D has entries in {0, +/-1/2}
which are exactly representable, so all numpy equality tests succeed
without floating-point tolerance).
"""

from __future__ import annotations

from itertools import product as iproduct
from pathlib import Path
import sys

try:
    import numpy as np
    import sympy
    from sympy import (
        Matrix,
        I as sym_I,
        Rational,
        eye,
        simplify,
        zeros,
    )
except ImportError as exc:
    print(f"FAIL: required package missing: {exc}")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# =============================================================================
# Framework operator builders (numpy 3-d instance)
# =============================================================================


def staggered_eta(mu: int, x: tuple) -> int:
    """KS staggered phase eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}."""
    s = 0
    for nu in range(mu):
        s += x[nu]
    return (-1) ** s


def build_D_3d(L: int) -> np.ndarray:
    """Build the staggered hopping operator D on V_lat = C^{L^3}.

    D|x> = sum_{mu=0}^{2} (1/2) * eta_mu(x) * (|x + e_mu> - |x - e_mu>).
    All entries are in {0, +/- 1/2}: representable exactly in float64.
    """
    if L % 2 != 0:
        raise ValueError("Even L required for periodic bipartite Z^3.")
    N = L ** 3
    sites = list(iproduct(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    D = np.zeros((N, N), dtype=np.complex128)
    for x in sites:
        i = idx[x]
        for mu in range(3):
            eta = staggered_eta(mu, x)
            e_mu = [0, 0, 0]
            e_mu[mu] = 1
            xp = tuple((x[k] + e_mu[k]) % L for k in range(3))
            xm = tuple((x[k] - e_mu[k]) % L for k in range(3))
            D[i, idx[xp]] += 0.5 * eta
            D[i, idx[xm]] -= 0.5 * eta
    return D


def build_D_mu_3d(L: int, mu: int) -> np.ndarray:
    """Build the direction-mu piece D_mu of D so that D = sum_mu D_mu."""
    if L % 2 != 0:
        raise ValueError("Even L required.")
    N = L ** 3
    sites = list(iproduct(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    Dmu = np.zeros((N, N), dtype=np.complex128)
    for x in sites:
        i = idx[x]
        eta = staggered_eta(mu, x)
        e_mu = [0, 0, 0]
        e_mu[mu] = 1
        xp = tuple((x[k] + e_mu[k]) % L for k in range(3))
        xm = tuple((x[k] - e_mu[k]) % L for k in range(3))
        Dmu[i, idx[xp]] += 0.5 * eta
        Dmu[i, idx[xm]] -= 0.5 * eta
    return Dmu


def build_C_3d(L: int) -> np.ndarray:
    """Build C = diag((-1)^{x1+x2+x3}) on V_lat = C^{L^3}."""
    N = L ** 3
    sites = list(iproduct(range(L), repeat=3))
    C = np.zeros((N, N), dtype=np.complex128)
    for i, x in enumerate(sites):
        C[i, i] = (-1) ** (x[0] + x[1] + x[2])
    return C


def build_P_3d(L: int) -> np.ndarray:
    """Build P: x -> -x mod L on V_lat = C^{L^3}.

    P|x> = |-x mod L>, so [P]_{y, x} = delta_{y, (-x) mod L}.
    """
    N = L ** 3
    sites = list(iproduct(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    P = np.zeros((N, N), dtype=np.complex128)
    for x in sites:
        i = idx[x]
        y = tuple((-x[k]) % L for k in range(3))
        j = idx[y]
        P[j, i] = 1.0
    return P


def matrix_eq_exact(A: np.ndarray, B: np.ndarray) -> bool:
    """Element-wise exact equality. D entries are in {0, +/- 1/2}, so
    every matrix product entry is an exact dyadic rational. We test
    equality with np.array_equal on the explicit complex arrays.
    """
    if A.shape != B.shape:
        return False
    diff = A - B
    # All operations involve sums of half-integers and products with +/- 1
    # and i. The real and imaginary parts of the difference must each
    # be exactly zero.
    return bool(np.all(diff.real == 0.0) and np.all(diff.imag == 0.0))


def conjugate_by_antiunitary_PK(M: np.ndarray, P: np.ndarray) -> np.ndarray:
    """Compute Theta_H M Theta_H^{-1} for Theta_H = P K, K complex conjugation.

    On linear operators M, the action is M -> P M^* P^{-1}.
    Since P is a real permutation, P^{-1} = P^T = P (P^2 = I and P is real
    symmetric). Use P @ conj(M) @ P.
    """
    return P @ np.conj(M) @ P


# =============================================================================
# Sympy 1-d slice (symbolic certainty)
# =============================================================================


def build_D_1d_sympy(L: int) -> Matrix:
    """Build the 1-d staggered hopping D on V_lat = C^L at exact sympy precision.

    Eta_0(x) = 1 in 1-d (only direction). All entries in {0, +/- 1/2}.
    """
    half = Rational(1, 2)
    D = zeros(L, L)
    for x in range(L):
        # eta_0(x) = 1
        D[x, (x + 1) % L] += half
        D[x, (x - 1) % L] -= half
    return D


def build_C_1d_sympy(L: int) -> Matrix:
    """Build C = diag((-1)^x) on V_lat = C^L."""
    C = zeros(L, L)
    for x in range(L):
        C[x, x] = (-1) ** x
    return C


def build_P_1d_sympy(L: int) -> Matrix:
    """Build P: x -> -x mod L on V_lat = C^L."""
    P = zeros(L, L)
    for x in range(L):
        y = (-x) % L
        P[y, x] = 1
    return P


def sympy_matrix_eq(A: Matrix, B: Matrix) -> bool:
    """Exact sympy matrix equality via simplify per entry."""
    if A.shape != B.shape:
        return False
    diff = A - B
    for i in range(diff.rows):
        for j in range(diff.cols):
            if simplify(diff[i, j]) != 0:
                return False
    return True


# =============================================================================
# Main verification suite
# =============================================================================


def verify_3d(L: int) -> None:
    section(f"Item 1-7 [3-d numpy at L={L}]: D real anti-Hermitian, "
            f"H Hermitian, framework C, P-on-D identities, Theta_H = P K "
            f"preserves H, H_odd = 0, H_{{mu,odd}} = 0.")

    D = build_D_3d(L)
    C = build_C_3d(L)
    P = build_P_3d(L)

    # Item 1: D is real anti-Hermitian
    check(
        f"L={L}: D has only real entries (Im D == 0)",
        bool(np.all(D.imag == 0.0)),
    )
    check(
        f"L={L}: D entries in {{0, +/- 1/2}} (max |D| <= 1/2)",
        bool(np.all(np.abs(D) <= 0.5 + 1e-15)),
    )
    check(
        f"L={L}: D^T = -D (anti-Hermitian)",
        matrix_eq_exact(D.T, -D),
    )

    # Item 2: H = iD is Hermitian
    H = 1j * D
    check(
        f"L={L}: H = iD Hermitian (H = H^dagger)",
        matrix_eq_exact(H, H.conj().T),
    )

    # Item 3: parent framework identities (D1), (D2)
    check(
        f"L={L}: (D1) C D C^{{-1}} = -D  (parent cpt_exact_note item 1)",
        matrix_eq_exact(C @ D @ C, -D),
    )
    check(
        f"L={L}: (D2) P D P^{{-1}} = -D  (parent cpt_exact_note item 2)",
        matrix_eq_exact(P @ D @ P, -D),
    )
    check(
        f"L={L}: (D3) K D K^{{-1}} = D  (D real)",
        matrix_eq_exact(np.conj(D), D),
    )

    # Sanity: C^2 = I, P^2 = I
    N = L ** 3
    I = np.eye(N, dtype=np.complex128)
    check(
        f"L={L}: C^2 = I_lat",
        matrix_eq_exact(C @ C, I),
    )
    check(
        f"L={L}: P^2 = I_lat",
        matrix_eq_exact(P @ P, I),
    )

    # Item 4 (numpy view of L1): Theta_H = P K acts as M -> P M^* P^{-1}
    # on operators; Theta_H^2 = (P K)^2 acts as M -> P (P M^* P^{-1})^* P^{-1}
    #                                       = P P M (P P)^{-1}
    # (since (M^*)^* = M and K commutes with P because P is real)
    # Apply Theta_H^2 to a generic-looking complex matrix and check
    # it returns the matrix unchanged.
    rng = np.random.default_rng(0xC97)
    M_test = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N)))
    M_round = conjugate_by_antiunitary_PK(
        conjugate_by_antiunitary_PK(M_test, P), P
    )
    # Theta_H^2 M Theta_H^{-2} = M  (Theta_H^2 = I on V_lat)
    check(
        f"L={L}: (L1) Theta_H^2 acts trivially on operators (Theta_H is involutive)",
        bool(np.allclose(M_round, M_test, atol=1e-12, rtol=0)),
    )

    # Item 5 (L2): Theta_H H Theta_H^{-1} = H
    H_conj = conjugate_by_antiunitary_PK(H, P)
    check(
        f"L={L}: (L2) Theta_H H Theta_H^{{-1}} = H  (exact)",
        matrix_eq_exact(H_conj, H),
    )

    # Item 6 (L3): H_odd = 0
    H_odd = (H - H_conj) / 2
    check(
        f"L={L}: (L3) H_odd matrix entrywise = 0  (||H_odd||_F = 0 exact)",
        matrix_eq_exact(H_odd, np.zeros_like(H_odd)),
    )
    frob = np.sqrt(np.sum(np.abs(H_odd) ** 2))
    check(
        f"L={L}: (L3) ||H_odd||_F = 0 numeric  (got {frob:.3e})",
        bool(frob == 0.0),
    )

    # Item 7 (L4): per-direction H_{mu, odd} = 0
    for mu in range(3):
        Dmu = build_D_mu_3d(L, mu)
        Hmu = 1j * Dmu
        Hmu_conj = conjugate_by_antiunitary_PK(Hmu, P)
        Hmu_odd = (Hmu - Hmu_conj) / 2
        check(
            f"L={L}: (L4) H_{{mu={mu+1}, odd}} matrix entrywise = 0",
            matrix_eq_exact(Hmu_odd, np.zeros_like(Hmu_odd)),
        )

    # Decomposition sanity: sum of H_mu = H
    H_recon = sum(1j * build_D_mu_3d(L, m) for m in range(3))
    check(
        f"L={L}: H = sum_mu H_mu (direction decomposition consistency)",
        matrix_eq_exact(H_recon, H),
    )


def verify_1d_sympy(L: int) -> None:
    section(f"Item 8 [1-d sympy at L={L}]: symbolic certainty for "
            f"(L1)-(L3) on a 1-d staggered slice.")

    D = build_D_1d_sympy(L)
    C = build_C_1d_sympy(L)
    P = build_P_1d_sympy(L)
    I_L = eye(L)

    # D real anti-Hermitian on 1-d slice
    check(
        f"L={L} (sympy 1-d): D^T = -D",
        sympy_matrix_eq(D.T, -D),
    )

    # H = i D Hermitian
    H = sym_I * D
    # H^dagger = (i D)^dagger = -i D^dagger = -i (-D) = i D = H
    H_dag = -sym_I * D.T
    check(
        f"L={L} (sympy 1-d): H = iD Hermitian (H = H^dagger)",
        sympy_matrix_eq(H, H_dag),
    )

    # Note: in 1-d, the parity is trivially the same calculation.
    # We do NOT need to re-verify (D1) here: C is not the same as
    # the 3-d sublattice parity in 1-d. Skip C-on-D and check only
    # the load-bearing P-on-D and Theta_H = P K identities, which
    # are the algebraically core ones.
    check(
        f"L={L} (sympy 1-d): P D P^{{-1}} = -D",
        sympy_matrix_eq(P * D * P, -D),
    )

    # (L1) sympy: Theta_H^2 = I  (act on a generic symbolic vector
    # via M -> P M^* P^{-1} and check (Theta_H^2)(M) = M)
    # In sympy, complex conjugation of a Matrix entry m is m.conjugate(),
    # which on real-or-sym_I expressions returns the conjugated entry.
    M_sym = Matrix(L, L, lambda i, j: sym_I ** (i + j) + Rational(i, 1) + sym_I * Rational(j, 1))
    M_conj_once = P * M_sym.applyfunc(lambda e: e.conjugate()) * P
    M_conj_twice = P * M_conj_once.applyfunc(lambda e: e.conjugate()) * P
    check(
        f"L={L} (sympy 1-d): (L1) Theta_H^2 acts trivially "
        f"(M -> P (P M^* P)^* P = M)",
        sympy_matrix_eq(M_conj_twice, M_sym),
    )

    # (L2) sympy: Theta_H H Theta_H^{-1} = H
    H_conj = P * H.applyfunc(lambda e: e.conjugate()) * P
    check(
        f"L={L} (sympy 1-d): (L2) Theta_H H Theta_H^{{-1}} = H  (sympy exact)",
        sympy_matrix_eq(H_conj, H),
    )

    # (L3) sympy: H_odd = 0 entrywise
    H_odd = (H - H_conj) / 2
    check(
        f"L={L} (sympy 1-d): (L3) H_odd entrywise = 0  (sympy exact)",
        sympy_matrix_eq(H_odd, zeros(L, L)),
    )


def verify_counterfactual(L: int) -> None:
    section(f"Item 9 [counterfactual at L={L}]: the *naive* lift "
            f"CP K does NOT preserve H — confirms (L2) requires "
            f"Theta_H = P K specifically, not Theta_naive = CP K.")

    D = build_D_3d(L)
    C = build_C_3d(L)
    P = build_P_3d(L)
    H = 1j * D

    # Naive lift: Theta_naive = CP K, action on H is M -> CP M^* (CP)^{-1}
    CP = C @ P
    CP_inv = P @ C  # CP and PC differ by sign-structure but on the
    # framework instance C, P commute on V_lat = C^{L^3}: C is diagonal
    # in lattice sites, P is a permutation, and the [C, P] = 0 check
    # is verified in parent runner Part 6. So (CP)^{-1} = P^{-1} C^{-1}
    # = P C, and on the diagonal C with P pure permutation,
    # (CP)^{-1} = (PC) is sufficient.
    # Compute (CP) H^* (CP)^{-1}
    H_naive_conj = CP @ np.conj(H) @ CP_inv

    # The bridge note's Part 2 ("Why The Naive Lift Fails") claims
    # (CP K)(iD)(CP K)^{-1} = -iD = -H. Verify this.
    check(
        f"L={L}: counterfactual — (CP K) H (CP K)^{{-1}} = -H  (naive lift "
        f"flips sign, NOT a symmetry of H)",
        matrix_eq_exact(H_naive_conj, -H),
    )

    # Sanity: Theta_H = P K preserves H (re-verify alongside)
    H_correct_conj = P @ np.conj(H) @ P
    check(
        f"L={L}: counterfactual sanity — Theta_H = P K  preserves H  (correct lift)",
        matrix_eq_exact(H_correct_conj, H),
    )


def out_of_scope_marker() -> None:
    section("Item 10 [out-of-scope marker, NOT a check]: SME bilinear "
            "operator dictionary, basis completeness, and exclusion of "
            "CPT-odd bilinear structures outside the direction-resolved "
            "hopping proxy.")
    print(
        "  [SKIP] No SME bilinear operator dictionary verified here.\n"
        "         Per the bridge note's 2026-05-16 audit verdict, the\n"
        "         SME bilinear basis-completeness assertion is the open\n"
        "         conditional of the parent bridge.\n"
        "         The present narrow theorem explicitly does NOT claim it,\n"
        "         and the present runner explicitly does NOT verify it.\n"
        "         The SME-zero conclusion of the parent bridge remains\n"
        "         audited_conditional until the SME operator dictionary\n"
        "         derivation is supplied by separate authority."
    )


def main() -> int:
    print("=" * 88)
    print("HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM audit companion")
    print("=" * 88)
    print(
        "Verifies (L1)-(L4) on the framework's specific staggered C, P\n"
        "and H = iD construction at exact sympy precision (1-d slice)\n"
        "and exact numpy precision (3-d L = 4 and L = 6).\n"
        "Out-of-scope marker (Item 10): does NOT verify the SME bilinear\n"
        "operator dictionary; that is the parent bridge's open conditional."
    )

    # Item 1-7: 3-d numpy at L = 4, 6
    for L in (4, 6):
        verify_3d(L)

    # Item 8: 1-d sympy at L = 4
    verify_1d_sympy(4)

    # Item 9: counterfactual at L = 4
    verify_counterfactual(4)

    # Item 10: out-of-scope marker (no check)
    out_of_scope_marker()

    print()
    print("=" * 88)
    print(f"Summary: PASS={PASS}  FAIL={FAIL}")
    verdict = "PASS" if FAIL == 0 else "FAIL"
    print(f"Verdict: {verdict}.")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
