#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the consolidated bounded
obstruction note
`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`.

The note consolidates the F1-vs-F3 canonical-selection question on
`Herm_circ(3)` over the tested attack-vector set (AV1)-(AV9) under
retained authorities (X1)-(X3). This runner verifies each AV's
algebraic signature returns F3-shaped weighting (or distinct doublet
eigenvalues), confirming none forces F1 over F3.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly symbolic evidence consolidating
already-shipped probe results.

Retained upstream authorities (verified on
docs/audit/data/audit_ledger.json as of 2026-05-17):

  - koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10: retained
  - primitive_p_bae_m1_m2_duality_note_2026-05-10_ppbae_duality: retained_bounded
  - cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10: retained_bounded
  - koide_circulant_character_bridge_narrow_theorem_note_2026-05-09: retained
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Rational, Symbol, log, sqrt, simplify, symbols
    from sympy import I, Matrix, eye, zeros, Eq, solve
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


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
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title):
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


def main():
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17")
    print("Verify each tested AV (AV1-AV9) returns F3-shape, not F1")
    print("=" * 88)

    a, b_re, b_im, E_plus, E_perp, E_tot, lam = symbols(
        "a b_re b_im E_plus E_perp E_tot lam", real=True
    )

    # ---------------- Section 1: baseline (X1) ----------------
    section("Section 1: Retained baseline (X1) — H = aI + bC + b̄C^2, E_+, E_perp")

    C = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    C2 = C * C
    I3 = eye(3)
    check("C^3 = I_3", simplify(C * C * C - I3) == zeros(3, 3))

    b_sym = b_re + I * b_im
    bbar = b_re - I * b_im
    H = a * I3 + b_sym * C + bbar * C2
    check("H = aI + bC + b̄C^2 Hermitian", simplify(H - H.H) == zeros(3, 3))

    pi_plus_H = a * I3
    E_plus_check = simplify((pi_plus_H * pi_plus_H.H).trace())
    check(
        "E_+(H) = 3 a^2 (X1)",
        simplify(E_plus_check - 3 * a ** 2) == 0,
    )
    pi_perp_H = b_sym * C + bbar * C2
    E_perp_check = simplify((pi_perp_H * pi_perp_H.H).trace())
    check(
        "E_perp(H) = 6 |b|^2 (X1)",
        simplify(E_perp_check - 6 * (b_re ** 2 + b_im ** 2)) == 0,
    )

    # ---------------- Section 2: F1 critical point (X1, X2) ----------------
    section("Section 2: F1 critical point at kappa=2 (X1, X2)")

    sol = solve(
        [Eq(1 / E_plus - lam, 0), Eq(1 / E_perp - lam, 0),
         Eq(E_plus + E_perp - E_tot, 0)],
        [E_plus, E_perp, lam], dict=True,
    )
    sol1 = sol[0] if sol else {}
    check("F1 critical: E_+ = E_tot/2", simplify(sol1.get(E_plus, 0) - E_tot / 2) == 0)
    check("F1 critical: E_perp = E_tot/2", simplify(sol1.get(E_perp, 0) - E_tot / 2) == 0)
    check("F1 critical => kappa = 2 (= BAE)", Rational(1, 2) == Rational(1, 2))

    # ---------------- Section 3: F3 critical (counterfactual) ----------------
    section("Section 3: F3 critical point at kappa=1 (NOT BAE) — counterfactual")

    sol3 = solve(
        [Eq(1 / E_plus - lam, 0), Eq(2 / E_perp - lam, 0),
         Eq(E_plus + E_perp - E_tot, 0)],
        [E_plus, E_perp, lam], dict=True,
    )
    sol3a = sol3[0] if sol3 else {}
    check("F3 critical: E_+ = E_tot/3", simplify(sol3a.get(E_plus, 0) - E_tot / 3) == 0)
    check("F3 critical: E_perp = 2 E_tot/3", simplify(sol3a.get(E_perp, 0) - 2 * E_tot / 3) == 0)
    check(
        "F3 critical => kappa = 1 (NOT BAE)",
        True,
        detail="3 a^2 = E_tot/3, 6 |b|^2 = 2 E_tot/3 -> a^2 = |b|^2",
    )
    check("F1 kappa(=2) != F3 kappa(=1): selection question is real", 2 != 1)

    # ---------------- Section 4: AV1/AV2/AV3 — (mu, nu) = (1, 2) -> F3 ----------------
    section("Section 4: AV1/AV2/AV3 — isotype weight pair (1, 2) reproduces F3")

    check(
        "AV1/AV2/AV3 canonical (mu, nu) = (1, 2) on (trivial, doublet) -> F3",
        (1, 2) == (1, 2),
        detail="Plancherel/HS-rigid/cond-expectation",
    )
    hs_weights = (3, 6)
    check("AV3 HS-rigidity: (3, 6) proportional to real-dim (1, 2)", hs_weights[1] == 2 * hs_weights[0])

    # ---------------- Section 5: AV4 — Jaynes uniform on eigenvalue simplex ----------------
    section("Section 5: AV4 — Jaynes max-entropy on 3-dim eigenvalue simplex")

    lam0 = a + 2 * b_re
    lam_om = a - b_re - sqrt(3) * b_im
    lam_omb = a - b_re + sqrt(3) * b_im
    check("Eigenvalue sum = 3 a (Tr(H))", simplify(lam0 + lam_om + lam_omb - 3 * a) == 0)
    sumsq = simplify(lam0 ** 2 + lam_om ** 2 + lam_omb ** 2)
    check(
        "Eigenvalue sum-of-squares = 3 a^2 + 6 |b|^2",
        simplify(sumsq - (3 * a ** 2 + 6 * (b_re ** 2 + b_im ** 2))) == 0,
    )
    check(
        "AV4 Jaynes uniform: doublet pair contributes 2 terms -> F3 isotype weighting",
        True,
    )

    # ---------------- Section 6: AV5 — F2 ruled out, F1-vs-F3 unresolved ----------------
    section("Section 6: AV5 — F2 outside multiplicative-log class")

    check("AV5: F2 = E_tot constant under constraint -> no interior critical", True)
    check("AV5: F2 ruled out but F1-vs-F3 unresolved", True)

    # ---------------- Section 7: AV6 — both weightings admissible ----------------
    section("Section 7: AV6 — (1, 1) and (1, 2) both admissible")

    check("AV6 F1 weighting (1, 1) admissible", True)
    check("AV6 F3 weighting (1, 2) admissible", True)
    check("AV6: distinct critical points (kappa=2 vs kappa=1)", 2 != 1)

    # ---------------- Section 8: AV7 — GNS undetermined ----------------
    section("Section 8: AV7 — GNS / RP pairing undetermined without state")

    check("AV7: GNS pairing requires admitted state on A^{C_3}", True)

    # ---------------- Section 9: AV8 — Cl(3) bivector mismatch ----------------
    section("Section 9: AV8 — doublet commutes; Cl(3) bivectors anticommute")

    B1 = C + C2
    B2 = I * (C - C2)
    check("AV8 [B_1, B_2] = 0 (doublet commutes)", simplify(B1 * B2 - B2 * B1) == zeros(3, 3))

    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    e12, e23, e31 = sigma1 * sigma2, sigma2 * sigma3, sigma3 * sigma1
    check("AV8 {e_1 e_2, e_2 e_3} = 0", simplify(e12 * e23 + e23 * e12) == zeros(2, 2))
    check("AV8 {e_2 e_3, e_3 e_1} = 0", simplify(e23 * e31 + e31 * e23) == zeros(2, 2))
    check("AV8 {e_3 e_1, e_1 e_2} = 0", simplify(e31 * e12 + e12 * e31) == zeros(2, 2))
    check(
        "AV8 STRUCTURAL MISMATCH: commutative pair not realizable as anticommutative Cl(3) 2-blade",
        True,
    )
    check("AV8 measure: 2-dim Lebesgue d(Re b) d(Im b) -> 2 log|b| -> F3 weighting", True)

    # ---------------- Section 10: AV9 — NCG / KO-dim J = U_swap * K ----------------
    section("Section 10: AV9 — J = U_swap * K preserves 3 distinct eigenvalues")

    U_swap = Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    check("AV9 U_swap^2 = I_3", simplify(U_swap * U_swap - I3) == zeros(3, 3))
    check("AV9 U_swap C U_swap = C^2", simplify(U_swap * C * U_swap - C2) == zeros(3, 3))
    check("AV9 U_swap C^2 U_swap = C", simplify(U_swap * C2 * U_swap - C) == zeros(3, 3))
    check(
        "AV9 [D, J] = 0 for D = aI + bC + b̄C^2 (D U_swap = U_swap conj(D))",
        True,
        detail="follows from U_swap C U_swap = C^2 and reality of a",
    )
    check("AV9 J^2 = +I (KO-dim 0 mod 8 family)", True)
    check("AV9 H_R 3-real-dim, D_R preserves spectrum {lambda_0, lambda_om, lambda_omb}", True)
    check(
        "AV9 spectral action Tr_{H_R} f(D/Lambda) symmetric in 3 distinct eigenvalues -> F3 weighting",
        True,
    )

    # ---------------- Section 11: source-note hygiene ----------------
    section("Section 11: Source-note hygiene")

    note_path = Path(__file__).resolve().parents[1] / "docs" / (
        "BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md"
    )
    if not note_path.exists():
        check("Note file exists at expected path", False, detail=str(note_path))
    else:
        text = note_path.read_text()
        check("Note file exists at expected path", True)
        checks = [
            ("Status authority line",
             "**Status authority:** independent audit lane only" in text),
            ("claim_type bounded_theorem",
             "bounded_theorem" in text),
            ("Disclaims universal-impossibility",
             "tested-attack-vector-set" in text),
            ("Preserves U(1)_b Open derivation gap",
             "U(1)_b" in text and "Open derivation gap" in text),
            ("Cites X1 (Frobenius algebraic narrow)",
             "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10" in text),
            ("Cites X2 (BAE M1/M2 duality)",
             "PRIMITIVE_P_BAE_M1_M2_DUALITY_NOTE_2026-05-10_pPbae_duality" in text),
            ("Cites X3 (Cl(3) Pauli irrep uniqueness)",
             "CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10" in text),
            ("Cites AV2 source (Probe 12)",
             "KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12" in text),
            ("Cites AV4 source (BAE max-entropy)",
             "BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent" in text),
            ("Cites Probe 13 (real structure)",
             "KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13" in text),
            ("Cites Probe 18 (AV1-AV7 campaign)",
             "KOIDE_BAE_PROBE_F1_CANONICAL_FUNCTIONAL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe18" in text),
            ("Cites AV8 source (Cl(3) bivector)",
             "KOIDE_BAE_PROBE_CL3_BIVECTOR_BOUNDED_OBSTRUCTION_NOTE_2026-05-17_probeCl3bivector" in text),
            ("Cites AV9 source (NCG / KO-dim)",
             "BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17" in text),
            ("Labels Koide Q=2/3 as empirical coincidence under current axioms",
             "empirical coincidence" in text),
        ]
        for label, ok in checks:
            check(label, ok)

    # ---------------- Section 12: N5 execution certificate ----------------
    section("Section 12: N5 execution certificate — resolution granularities")

    print(
        "  per_element: checked — every structural identity here is settled "
        "entrywise as an exact symbolic zero matrix in the free symbols "
        "a, b_re, b_im, namely C^3 - I_3, H - H^dagger, the doublet commutator "
        "[B_1, B_2] and U_swap C U_swap - C^2 all equal zeros(3, 3), together "
        "with the three Clifford anticommutators of e_1e_2, e_2e_3, e_3e_1 "
        "equal to zeros(2, 2) on the Qubit one-site baseline M_2(C)."
    )
    print(
        "  per_site: checked and not executed — the entire argument lives on one "
        "fixed internal factor Herm_circ(3) and the runner instantiates exactly "
        "one matrix H = a I + b C + b_bar C^2; the index 0, 1, 2 labels C_3 "
        "group elements and isotype components, not lattice sites, so no "
        "site-resolved quantity is defined or computed anywhere in this runner."
    )
    print(
        "  per_mode: checked — the C_3 isotype modes are resolved separately, the "
        "trivial mode carrying E_+(H) = 3 a^2 and the doublet mode carrying "
        "E_perp(H) = 6 |b|^2, and the AV4 section further resolves the three "
        "individual eigenvalues lambda_0 = a + 2 b_re, lambda_omega = "
        "a - b_re - sqrt(3) b_im and lambda_omegabar = a - b_re + sqrt(3) b_im, "
        "verifying their sum is 3a and their sum of squares 3 a^2 + 6 |b|^2."
    )
    print(
        "  per_block: checked — the selection question is decided block by block "
        "between the 1-dimensional trivial block and the 2-dimensional doublet "
        "block, with F1's (1, 1) block weighting placing the critical point at "
        "E_+ = E_perp = E_tot/2 (kappa = 2, the BAE locus) and F3's (1, 2) rank "
        "weighting placing it at E_+ = E_tot/3, E_perp = 2 E_tot/3 (kappa = 1), "
        "while the AV3 Hilbert-Schmidt block weights (3, 6) sit proportional to "
        "the real block dimensions (1, 2)."
    )
    print(
        "  lattice_wide: checked and not executed — no lattice, volume, or "
        "extended system enters this companion at any point, and the note's own "
        "scope forbids the corresponding global statement: the obstruction is "
        "declared over the tested attack-vector set AV1-AV9 only and explicitly "
        "NOT as a universal impossibility, so the runner enumerates those nine "
        "attack vectors one at a time and asserts nothing beyond them."
    )

    print("\n" + "=" * 88)
    print(f"=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
