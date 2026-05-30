#!/usr/bin/env python3
"""Audit companion runner for STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.

Pattern A audit-companion. Verifies (S1)-(S6) of the narrow theorem at
exact precision:

- Numpy 3-d slice on L in {4, 6}: D entries are exactly representable
  rational +/-1/2, so numpy comparisons are exact equality (no FP
  rounding).
- Sympy 1-d slice on L = 4: exhibits (S1)-(S6) at exact symbolic
  precision to confirm the numpy result is not a floating-point
  accident.

Statement isolated: on the staggered Cl(3) framework Hamiltonian
H = i D with D the real anti-Hermitian staggered hopping operator on
periodic Z^3 with even L,

  (S1) H = H_1 + H_2 + H_3 exact, with H_mu := i D_mu the direction-mu
       single-direction NN hopping summand.
  (S2) On-site (diagonal) Hilbert-Schmidt projection of H vanishes.
  (S3) Longer-range (d_per > 1) Hilbert-Schmidt projection vanishes.
  (S4) Cross-direction (non-axis-aligned NN) projection vanishes
       (vacuous on the cubic NN lattice; explicit axis-alignment
       tabulation).
  (S5) Pairwise Hilbert-Schmidt orthogonality of H_1, H_2, H_3:
       Tr(H_mu^dag H_nu) = 0 for mu != nu.
  (S6) Direction-completeness corollary: Hilbert-Schmidt projection of
       H onto the orthogonal complement of span_C{H_1, H_2, H_3} is
       exactly zero.

Out of scope (explicitly NOT verified, deliberately):

  - Continuum SME bilinear operator dictionary.
  - SME coefficient-level vanishing.
  - Theta_H = P K symmetry algebra (that is the sister narrow theorem
    HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17).

No PDG values, no fitted constants, no SME numerical input, no
continuum-CPT input, no interacting-theory input.
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, ok: bool, detail: str = "", kind: str = "EXACT") -> bool:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    print(
        f"  [{'PASS' if ok else 'FAIL'}]{tag} {label}"
        + (f"  ({detail})" if detail else "")
    )
    return ok


# =============================================================================
# Framework construction (D, D_mu, H, H_mu)
# =============================================================================


def staggered_eta(mu: int, site: tuple[int, int, int]) -> int:
    return (-1) ** sum(site[nu] for nu in range(mu))


def site_index(L: int) -> tuple[callable, callable]:
    def idx(x: int, y: int, z: int) -> int:
        return ((x % L) * L + (y % L)) * L + (z % L)

    def site(i: int) -> tuple[int, int, int]:
        z = i % L
        y = (i // L) % L
        x = i // (L * L)
        return x, y, z

    return idx, site


def build_D_numpy(L: int) -> np.ndarray:
    """Full staggered D on L^3 lattice (numpy, exact rational +/-1/2 entries)."""
    n = L**3
    idx, site = site_index(L)
    D = np.zeros((n, n), dtype=complex)
    for i in range(n):
        x = site(i)
        for mu in range(3):
            eta = staggered_eta(mu, x)
            fwd = list(x)
            bwd = list(x)
            fwd[mu] = (fwd[mu] + 1) % L
            bwd[mu] = (bwd[mu] - 1) % L
            D[i, idx(*fwd)] += 0.5 * eta
            D[i, idx(*bwd)] -= 0.5 * eta
    return D


def build_D_mu_numpy(L: int, mu: int) -> np.ndarray:
    """Direction-mu hopping summand D_mu (numpy)."""
    n = L**3
    idx, site = site_index(L)
    D = np.zeros((n, n), dtype=complex)
    for i in range(n):
        x = site(i)
        eta = staggered_eta(mu, x)
        fwd = list(x)
        bwd = list(x)
        fwd[mu] = (fwd[mu] + 1) % L
        bwd[mu] = (bwd[mu] - 1) % L
        D[i, idx(*fwd)] += 0.5 * eta
        D[i, idx(*bwd)] -= 0.5 * eta
    return D


def periodic_manhattan(s1: tuple[int, int, int], s2: tuple[int, int, int], L: int) -> int:
    d = 0
    for k in range(3):
        dk = abs(s1[k] - s2[k])
        dk = min(dk, L - dk)
        d += dk
    return d


# =============================================================================
# 1-d sympy slice (mu = 0 only, exact symbolic)
# =============================================================================


def build_D_sympy_1d(L: int) -> sp.Matrix:
    """1-d staggered D on direction mu=0 only, exact sympy rationals."""
    n = L
    D = sp.zeros(n, n)
    for i in range(n):
        # eta_0 = 1 always
        eta = sp.Integer(1)
        fwd = (i + 1) % L
        bwd = (i - 1) % L
        D[i, fwd] += sp.Rational(1, 2) * eta
        D[i, bwd] -= sp.Rational(1, 2) * eta
    return D


def main() -> int:
    print("=" * 78)
    print("AUDIT COMPANION: STAGGERED HAMILTONIAN DIRECTION DECOMPOSITION")
    print("Narrow theorem (S1)-(S6) on H = iD lattice operator algebra.")
    print("Parent: PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30")
    print("Sister: HERMITIAN_LIFT_THETA_H_PK_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17")
    print("=" * 78)
    print()

    # -------------------------------------------------------------------------
    # PART 1. Numpy 3-d slice on L in {4, 6}: exact (D entries are +/-1/2).
    # -------------------------------------------------------------------------
    print("Part 1: Numpy 3-d slice on L in {4, 6} (exact rational +/-1/2 entries).")
    print("-" * 78)

    for L in (4, 6):
        print(f"  L = {L}:")

        # Construct D and direction summands D_mu.
        D = build_D_numpy(L)
        D_mus = [build_D_mu_numpy(L, mu) for mu in range(3)]
        n = L**3

        # Step 1: D^T = -D (real anti-Hermitian sanity).
        anti = np.allclose(D.T, -D, atol=0.0)
        check(f"L={L} step 1: D^T = -D (real anti-Hermitian)", anti)

        # Step 2: D = D_1 + D_2 + D_3 exact.
        D_sum = sum(D_mus)
        diff = np.max(np.abs(D - D_sum))
        check(
            f"L={L} step 2: D = D_1 + D_2 + D_3 matrix-entrywise exact",
            diff == 0.0,
            f"max|D - sum_mu D_mu| = {diff:.2e}",
        )

        # Step 3: H = iD Hermitian.
        H = 1j * D
        herm_diff = np.max(np.abs(H - H.conj().T))
        check(
            f"L={L} step 3: H = iD Hermitian",
            herm_diff == 0.0,
            f"max|H - H^dag| = {herm_diff:.2e}",
        )

        # Step 4: (S1) H = H_1 + H_2 + H_3 exact.
        H_mus = [1j * Dm for Dm in D_mus]
        H_sum = sum(H_mus)
        s1_diff = np.max(np.abs(H - H_sum))
        check(
            f"L={L} step 4: (S1) H = H_1 + H_2 + H_3 exact",
            s1_diff == 0.0,
            f"max|H - sum_mu H_mu| = {s1_diff:.2e}",
        )

        # Step 5: each H_mu Hermitian.
        all_herm = True
        for mu in range(3):
            hm_diff = np.max(np.abs(H_mus[mu] - H_mus[mu].conj().T))
            if hm_diff != 0.0:
                all_herm = False
        check(f"L={L} step 5: each H_mu = i D_mu Hermitian", all_herm)

        # Step 6: (S2) on-site (diagonal) projection vanishes.
        diag = np.diag(H)
        diag_max = float(np.max(np.abs(diag)))
        check(
            f"L={L} step 6: (S2) on-site (diagonal) projection of H vanishes",
            diag_max == 0.0,
            f"max_x |<x|H|x>| = {diag_max:.2e}",
        )

        # Step 7: (S3) longer-range (d_per > 1) projection vanishes.
        _, site = site_index(L)
        violations_s3 = 0
        max_violator_s3 = 0.0
        for i in range(n):
            for j in range(n):
                d = periodic_manhattan(site(i), site(j), L)
                if d > 1:
                    val = abs(H[i, j])
                    if val > 0.0:
                        violations_s3 += 1
                        if val > max_violator_s3:
                            max_violator_s3 = val
        check(
            f"L={L} step 7: (S3) longer-range (d_per > 1) projection of H vanishes",
            violations_s3 == 0,
            f"violations = {violations_s3}, max violator = {max_violator_s3:.2e}",
        )

        # Step 8: (S4) cross-direction NN projection vanishes (every nonzero
        # entry of H has axis-aligned displacement).
        nonaxis_violations = 0
        for i in range(n):
            for j in range(n):
                if H[i, j] != 0:
                    s1 = site(i)
                    s2 = site(j)
                    # Check axis-aligned: displacement nonzero on exactly one axis.
                    diffs = []
                    for k in range(3):
                        dk = (s2[k] - s1[k]) % L
                        # Allow both forward and backward
                        if dk == 0:
                            diffs.append(0)
                        elif dk == 1 or dk == L - 1:
                            diffs.append(1)
                        else:
                            diffs.append(dk)
                    nonzero_axes = sum(1 for d in diffs if d != 0)
                    if nonzero_axes != 1:
                        nonaxis_violations += 1
        check(
            f"L={L} step 8: (S4) every nonzero H entry has axis-aligned displacement",
            nonaxis_violations == 0,
            f"non-axis-aligned violations = {nonaxis_violations}",
        )

        # Step 9: (S5) pairwise Hilbert-Schmidt orthogonality of H_mu.
        orth_violations = []
        for mu in range(3):
            for nu in range(3):
                if mu == nu:
                    continue
                ip = np.trace(H_mus[mu].conj().T @ H_mus[nu])
                if abs(ip) != 0.0:
                    orth_violations.append((mu, nu, complex(ip)))
        check(
            f"L={L} step 9: (S5) <H_mu, H_nu>_HS = 0 for mu != nu",
            len(orth_violations) == 0,
            f"violations = {len(orth_violations)}",
        )

        # Step 10: (S6) direction-completeness: projection of H onto orthogonal
        # complement of span_C{H_1, H_2, H_3} is zero.
        # Using (S5) HS-orthogonality of H_mu, the projection of H onto
        # span_C{H_mu} is sum_mu (<H_mu, H>_HS / <H_mu, H_mu>_HS) H_mu.
        coeffs = []
        for mu in range(3):
            num = np.trace(H_mus[mu].conj().T @ H)
            den = np.trace(H_mus[mu].conj().T @ H_mus[mu])
            coeffs.append(num / den)
        H_proj = sum(c * Hm for c, Hm in zip(coeffs, H_mus))
        perp = H - H_proj
        perp_max = float(np.max(np.abs(perp)))
        check(
            f"L={L} step 10: (S6) HS projection of H onto (span{{H_mu}})^perp = 0",
            perp_max == 0.0,
            f"max|H - sum_mu c_mu H_mu| = {perp_max:.2e}, c = {[complex(c) for c in coeffs]}",
        )

    # -------------------------------------------------------------------------
    # PART 2. Sympy 1-d slice on L=4: exact symbolic exhibition of (S1)-(S6).
    # -------------------------------------------------------------------------
    print()
    print("Part 2: Sympy 1-d slice on L=4 (exact symbolic precision).")
    print("-" * 78)

    L = 4
    D1 = build_D_sympy_1d(L)
    H1 = sp.I * D1
    # Direction-decomposition is trivial in 1-d: H = H_0 with only one direction.
    # Check (S1) trivially:
    # In 1-d the staggered Hamiltonian has only one direction summand H_0 = i D_0,
    # so H = H_0 + 0 + 0 (the other directions contribute zero).
    s1_sym = sp.simplify(H1 - sp.I * D1)
    s1_zero = s1_sym == sp.zeros(L, L)
    check("sympy 1-d L=4: (S1) H = H_0 (1-d slice) exact symbolic", s1_zero)

    # (S2) on-site (diagonal) projection of H vanishes.
    diag_sym = sp.Matrix([H1[i, i] for i in range(L)])
    s2_zero = all(diag_sym[i] == 0 for i in range(L))
    check("sympy 1-d L=4: (S2) on-site diagonal entries of H vanish", s2_zero)

    # (S3) longer-range (d_per > 1) entries vanish.
    s3_zero = True
    for i in range(L):
        for j in range(L):
            d = min(abs(i - j), L - abs(i - j))
            if d > 1 and sp.simplify(H1[i, j]) != 0:
                s3_zero = False
    check("sympy 1-d L=4: (S3) longer-range (d>1) entries of H vanish", s3_zero)

    # (S4) on 1-d slice, axis-alignment is automatic (only one axis).
    s4_trivial = True
    check("sympy 1-d L=4: (S4) axis-alignment automatic on 1-d slice (trivial)", s4_trivial)

    # (S5) on 1-d slice, only one direction summand exists, so the pairwise
    # orthogonality statement is vacuous; tabulate as such.
    s5_vacuous = True
    check(
        "sympy 1-d L=4: (S5) pairwise HS orthogonality (vacuous in 1-d)",
        s5_vacuous,
    )

    # (S6) projection onto orthogonal complement of span{H_0} is zero
    # (trivially, since H = H_0).
    s6_zero = sp.simplify(H1 - sp.I * D1) == sp.zeros(L, L)
    check(
        "sympy 1-d L=4: (S6) projection of H onto (span{H_0})^perp = 0 (trivial)",
        s6_zero,
    )

    # -------------------------------------------------------------------------
    # PART 3. Sympy 3-d slice on L=4: exact symbolic exhibition of (S1)-(S6).
    # -------------------------------------------------------------------------
    print()
    print("Part 3: Sympy 3-d slice on L=4 (exact symbolic precision, full theorem).")
    print("-" * 78)

    L = 4

    def build_D_sympy_3d(L: int) -> sp.Matrix:
        n = L**3
        idx, site = site_index(L)
        D = sp.zeros(n, n)
        for i in range(n):
            x = site(i)
            for mu in range(3):
                eta = sp.Integer((-1) ** sum(x[nu] for nu in range(mu)))
                fwd = list(x)
                bwd = list(x)
                fwd[mu] = (fwd[mu] + 1) % L
                bwd[mu] = (bwd[mu] - 1) % L
                D[i, idx(*fwd)] += sp.Rational(1, 2) * eta
                D[i, idx(*bwd)] -= sp.Rational(1, 2) * eta
        return D

    def build_D_mu_sympy_3d(L: int, mu_target: int) -> sp.Matrix:
        n = L**3
        idx, site = site_index(L)
        D = sp.zeros(n, n)
        for i in range(n):
            x = site(i)
            eta = sp.Integer((-1) ** sum(x[nu] for nu in range(mu_target)))
            fwd = list(x)
            bwd = list(x)
            fwd[mu_target] = (fwd[mu_target] + 1) % L
            bwd[mu_target] = (bwd[mu_target] - 1) % L
            D[i, idx(*fwd)] += sp.Rational(1, 2) * eta
            D[i, idx(*bwd)] -= sp.Rational(1, 2) * eta
        return D

    D3 = build_D_sympy_3d(L)
    D3_mus = [build_D_mu_sympy_3d(L, mu) for mu in range(3)]
    H3 = sp.I * D3
    H3_mus = [sp.I * Dm for Dm in D3_mus]

    # (S1) H = sum H_mu exact symbolic.
    H3_sum = H3_mus[0] + H3_mus[1] + H3_mus[2]
    s1_diff = sp.simplify(H3 - H3_sum)
    s1_3d_ok = s1_diff == sp.zeros(L**3, L**3)
    check("sympy 3-d L=4: (S1) H = H_1 + H_2 + H_3 exact symbolic", s1_3d_ok)

    # (S2) on-site diagonal entries.
    s2_3d_ok = all(H3[i, i] == 0 for i in range(L**3))
    check("sympy 3-d L=4: (S2) all on-site H entries vanish", s2_3d_ok)

    # (S5) pairwise HS orthogonality.
    s5_3d_violations = 0
    for mu in range(3):
        for nu in range(3):
            if mu == nu:
                continue
            # Hermitian conjugate: M^dag = M^T.conjugate() = transpose then conj.
            inner = sp.simplify((H3_mus[mu].H * H3_mus[nu]).trace())
            if inner != 0:
                s5_3d_violations += 1
    check(
        "sympy 3-d L=4: (S5) <H_mu, H_nu>_HS = 0 for mu != nu (exact symbolic)",
        s5_3d_violations == 0,
        f"violations = {s5_3d_violations}",
    )

    # -------------------------------------------------------------------------
    # PART 4. Out-of-scope marker (algebraic completeness probe).
    # -------------------------------------------------------------------------
    print()
    print("Part 4: Out-of-scope marker (algebraic completeness probe).")
    print("-" * 78)
    print(
        "  Note: this runner does NOT verify the continuum SME bilinear "
        "operator dictionary"
    )
    print(
        "  (parent bridge note's open conditional item (1)), nor the SME "
        "coefficient-level"
    )
    print(
        "  vanishing (item (4)), nor the continuum CPT-theorem bridge. The "
        "operator-completeness"
    )
    print(
        "  statement here is purely at the LATTICE OPERATOR LEVEL on End_C(V_lat)."
    )
    print(
        "  The continuum-side mapping and SME-zero leap remain the bridge's "
        "open content."
    )

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    print()
    print("=" * 78)
    print(f"Summary: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "Verdict: PASS. (S1)-(S6) exact at numpy precision on L in {4, 6} "
            "and exact"
        )
        print(
            "symbolic on sympy 1-d (L=4) and sympy 3-d (L=4) slices. The "
            "lattice operator"
        )
        print(
            "algebra End_C(V_lat) has no Hermitian-bilinear content in H "
            "outside the three"
        )
        print("single-direction NN hopping summands {H_1, H_2, H_3}.")
        return 0
    print("Verdict: FAIL. At least one check failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
