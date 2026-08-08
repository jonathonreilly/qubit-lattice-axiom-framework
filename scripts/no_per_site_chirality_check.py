"""No gamma5 chirality operator in the supplied Cl(3) Pauli M_2(C) rep.

Given the supplied representation rho : Cl(3) -> M_2(C) with gamma_i -> sigma_i,
the Cl(3) volume element

    ω := γ_1 γ_2 γ_3

acts in Pauli rep as σ_1 σ_2 σ_3 = i I_2. Therefore:

    (1) ω is *central* in Cl(3) (commutes with all γ_i)
    (2) ω = i·I_2 is a scalar (proportional to identity)
    (3) NO element of Cl(3) anticommutes with all three generators γ_i
    (4) Therefore there is NO chirality operator γ_5 satisfying
        γ_5² = +I_2 and {γ_5, γ_i} = 0 for all i, inside this supplied M_2(C)
        Pauli carrier.

This is the per-site instance of the standard "no chirality in odd D"
fact (Lawson-Michelsohn): for Cl(p,q) with n = p+q odd, the volume element
is central, hence chirality requires extending the algebra (e.g. by
introducing a temporal direction, n+1 even). This runner does not identify the
larger spacetime or gauge chirality mechanism; it only checks the
single-site one-qubit-operator-algebra no-go.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md"
OLD_DEP = "AXIOM_FIRST_" + "CL3_PER_SITE_UNIQUENESS"


def note_firewall() -> bool:
    text = NOTE.read_text()
    lowered = text.lower()
    checks = {
        "cites minimal axioms Axiom 1": "minimal_axioms_2026-05-20" in lowered
        or "MINIMAL_AXIOMS_2026-05-20.md" in text,
        "cites retained Pauli irrep uniqueness": "cl3_pauli_irrep_uniqueness" in lowered,
        "states single-site matrix no-go": ("single-site" in lowered and "matrix no-go" in lowered)
        or "direct matrix" in lowered
        or "direct finite-dimensional" in lowered,
        "keeps larger chirality out of scope": "larger chirality mechanisms remain separate" in lowered
        or "larger spacetime clifford" in lowered,
        "no old uniqueness node in YAML": OLD_DEP not in text,
        "classified as no_go": "claim_type_author_hint: no_go" in text,
    }
    for label, ok in checks.items():
        print(f"  {label}: {'PASS' if ok else 'FAIL'}")
    return all(checks.values())


def main() -> None:
    print("=" * 72)
    print("NO γ_5 CHIRALITY INSIDE ONE-SITE M_2(C) PAULI ALGEBRA")
    print("=" * 72)
    print()

    print("-" * 72)
    print("SOURCE FIREWALL: one-site M_2(C) no-go, no imported odd-D theorem")
    print("-" * 72)
    t0_ok = note_firewall()
    print(f"  STATUS: {'PASS' if t0_ok else 'FAIL'}")
    print()

    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    sigmas = [s1, s2, s3]

    # Volume element ω = γ_1 γ_2 γ_3 = σ_1 σ_2 σ_3
    omega = s1 @ s2 @ s3
    print(f"  ω = σ_1 σ_2 σ_3 =")
    print(f"  {omega.tolist()}")
    print()

    # ----- Test 1: ω = i·I_2 -----
    print("-" * 72)
    print("TEST 1: ω = i·I_2 (scalar in Pauli rep)")
    print("-" * 72)
    target = 1j * I2
    dev = np.linalg.norm(omega - target)
    print(f"  ||ω - i·I_2|| = {dev:.3e}")
    t1_ok = dev < 1e-12
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: ω commutes with every σ_i (centrality) -----
    print("-" * 72)
    print("TEST 2: [ω, σ_i] = 0 for all i (ω is central in Cl(3))")
    print("-" * 72)
    max_comm = 0.0
    for i in range(3):
        comm = omega @ sigmas[i] - sigmas[i] @ omega
        d = np.linalg.norm(comm)
        max_comm = max(max_comm, d)
        print(f"  ||[ω, σ_{i+1}]|| = {d:.3e}")
    t2_ok = max_comm < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: ω² = -I_2 (since (i·I)² = -I) -----
    print("-" * 72)
    print("TEST 3: ω² = -I_2 (consistent with central scalar i·I)")
    print("-" * 72)
    omega_sq = omega @ omega
    target_sq = -I2
    dev_sq = np.linalg.norm(omega_sq - target_sq)
    print(f"  ||ω² - (-I_2)|| = {dev_sq:.3e}")
    t3_ok = dev_sq < 1e-12
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: NO 2x2 matrix anticommutes with all three σ_i -----
    print("-" * 72)
    print("TEST 4: No nonzero M ∈ M_2(C) anticommutes with all three σ_i")
    print("        (sweep through Pauli basis: only zero satisfies all three)")
    print("-" * 72)
    # Any M ∈ M_2(C) = a·I + b·σ_1 + c·σ_2 + d·σ_3 (Pauli basis spans M_2(C))
    # {M, σ_i} = 0 forces M to anticommute with σ_i.
    # Since {σ_i, σ_j} = 2 δ_ij I, only the scalar coefficient a contributes
    # to {M, σ_i} = 2a σ_i + (b·{σ_1,σ_i} + ...) = 2a σ_i + 2 b_i I.
    # For this to vanish for all i, need a = 0 and b = c = d = 0, i.e. M = 0.
    # Numerical sweep: try M = a I + b σ_1 + c σ_2 + d σ_3 over a basis,
    # check that requiring {M, σ_i} = 0 for all i forces M = 0.
    pauli_basis = [I2, s1, s2, s3]
    # Build the linear system: for each generator σ_i, {M, σ_i} = 0 is a
    # linear constraint on the Pauli coefficients (a, b, c, d).
    # Stack constraints: 3 generators × 4 matrix entries (real+imag) = 24 eqns
    # in 8 real unknowns (4 complex coefs).
    # Easier: compute {basis_k, σ_i} symbolically.
    constraints = []
    for i in range(3):
        for k in range(4):
            anti = pauli_basis[k] @ sigmas[i] + sigmas[i] @ pauli_basis[k]
            constraints.append(anti.flatten())
    # Stack into a 12x4 matrix where row (i, k) gives {basis_k, σ_i} as a vector
    # We want to find c = (a, b, c, d) such that Σ_k c_k · {basis_k, σ_i} = 0
    # for all i. So the constraint matrix has rows = anti_(i,k)_flat·c_k
    # Build full constraint matrix: (3·4) rows × 4 columns
    # M_ki = {basis_k, σ_i} as 2x2 matrix flattened to 4-vector
    # Constraint: Σ_k c_k · M_ki = 0 for each i ⇒ 3·4 = 12 equations.
    A = np.zeros((12, 4), dtype=complex)
    for i in range(3):
        for k in range(4):
            anti_ki = pauli_basis[k] @ sigmas[i] + sigmas[i] @ pauli_basis[k]
            A[i * 4:(i + 1) * 4, k] = anti_ki.flatten()
    # Find null space of A
    u, s, vh = np.linalg.svd(A)
    nullity = sum(1 for sv in s if sv < 1e-10)
    print(f"  rank of constraint matrix = {4 - nullity} (out of 4 unknowns)")
    print(f"  null space dim = {nullity} (only zero solution if dim = 0)")
    t4_ok = nullity == 0
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: No M satisfying both M² = +I_2 and {M, σ_i} = 0 -----
    print("-" * 72)
    print("TEST 5: No γ_5 candidate exists — no M satisfies (γ_5² = +I_2)")
    print("        AND {γ_5, σ_i} = 0 for all i, inside one M_2(C) site.")
    print("-" * 72)
    # By Test 4, the only M satisfying {M, σ_i} = 0 for all i is M = 0.
    # M = 0 doesn't satisfy M² = +I_2. Hence no γ_5 candidate exists.
    print("  Test 4 proved: only zero anticommutes with all three σ_i.")
    print("  Zero matrix doesn't satisfy γ_5² = +I_2 (since 0² = 0 ≠ I).")
    print("  Therefore no γ_5 exists inside the one-site M_2(C) Pauli algebra.")
    t5_ok = t4_ok  # follows directly from Test 4
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Test 6: dim of even subalgebra = dim of odd subalgebra = 2 -----
    print("-" * 72)
    print("TEST 6: Cl(3) has 4-dim even subalgebra (span{I, σ_1σ_2, σ_2σ_3, σ_3σ_1})")
    print("        and 4-dim odd subalgebra (span{σ_1, σ_2, σ_3, σ_1σ_2σ_3 = iI})")
    print("        BUT in Pauli rep both subalgebras already span M_2(C) = 4-dim,")
    print("        so even and odd subalgebras COINCIDE on Pauli (no Z_2 grading)")
    print("-" * 72)
    # In Pauli rep:
    # Even subalgebra basis: I, σ_1σ_2 = iσ_3, σ_2σ_3 = iσ_1, σ_3σ_1 = iσ_2
    #                       → {I, iσ_1, iσ_2, iσ_3} ↔ {I, σ_1, σ_2, σ_3} as C-span
    # Odd subalgebra basis: σ_1, σ_2, σ_3, σ_1σ_2σ_3 = iI
    #                       → {σ_1, σ_2, σ_3, iI} ↔ {I, σ_1, σ_2, σ_3} as C-span
    # Both span all of M_2(C); the Z_2 grading is invisible at the C-algebra level.
    # This means there's no internal "chirality projector" P_± = (1 ± γ_5)/2.
    even_basis = [I2, 1j * s3, 1j * s1, 1j * s2]  # σ_1σ_2 = iσ_3 etc.
    odd_basis = [s1, s2, s3, 1j * I2]
    even_matrix = np.column_stack([m.flatten() for m in even_basis])
    odd_matrix = np.column_stack([m.flatten() for m in odd_basis])
    rank_even = np.linalg.matrix_rank(even_matrix, tol=1e-10)
    rank_odd = np.linalg.matrix_rank(odd_matrix, tol=1e-10)
    print(f"  rank of even subalgebra in M_2(C) = {rank_even} (full = 4)")
    print(f"  rank of odd subalgebra in M_2(C)  = {rank_odd} (full = 4)")
    t6_ok = rank_even == 4 and rank_odd == 4
    print(f"  STATUS: {'PASS' if t6_ok else 'FAIL'}")
    print()

    print("=" * 72)
    print(f"  Source firewall (one-site Axiom 1 M_2(C) no-go):        {'PASS' if t0_ok else 'FAIL'}")
    print(f"  Test 1 (ω = i·I_2):                                {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 ([ω, σ_i] = 0 — ω is central):              {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (ω² = -I_2):                                {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (no M anticommutes with all σ_i):           {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (no γ_5 candidate exists):                  {'PASS' if t5_ok else 'FAIL'}")
    print(f"  Test 6 (even/odd subalgebras coincide on Pauli):   {'PASS' if t6_ok else 'FAIL'}")
    all_ok = all([t0_ok, t1_ok, t2_ok, t3_ok, t4_ok, t5_ok, t6_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()

    # N5 execution certificate (print-only; adds no check and no verdict)
    print("==============================================================================")
    print("N5 EXECUTION CERTIFICATE")
    print("==============================================================================")
    print(
        "  per_element: the decisive object is assembled from flattened matrix "
        "entries - Test 4 stacks the twelve anticommutators {basis_k, sigma_i} into "
        "a 12x4 complex array, one flattened 2x2 per four-row slot, and takes its "
        "singular values with a 1e-10 floor to read off a null-space dimension of "
        "zero; alongside that, omega = sigma_1 sigma_2 sigma_3 is printed entry by "
        "entry and each of the five deviation norms in Tests 1 through 3 comes out "
        "a hard zero rather than an epsilon-scale residual, because the arithmetic "
        "involves only the exact entries 0, +-1 and +-i."
    )
    print(
        "  per_site: one site is the entire subject, and the runner resolves it "
        "completely - the carrier is a single copy of the one-site Qubit algebra "
        "M_2(C), the three generators are the explicit Pauli matrices on it, and "
        "the conclusion is exactly a single-site statement: within that one carrier "
        "the volume element collapses to a central scalar, only the zero matrix "
        "anticommutes with all three generators, and therefore no gamma_5 can live "
        "at a site."
    )
    print(
        "  per_mode: checked and not executed - no mode of any kind is constructed. "
        "The three sigma_i are Clifford generators, not momentum labels, there is "
        "no transform, no dispersion and no wave vector in the file, and the only "
        "sweep it performs is over a four-element operator basis, which indexes "
        "algebra directions rather than modes."
    )
    print(
        "  per_block: the Z_2 even/odd grading is examined and found to be absent, "
        "though the test that shows this is close to automatic - the even span is "
        "entered as I, i*sigma_3, i*sigma_1, i*sigma_2 and the odd span as sigma_1, "
        "sigma_2, sigma_3, i*I, and each is column-stacked and given a matrix_rank "
        "at tol 1e-10, returning 4 out of 4 both times. Since both lists are the "
        "Pauli basis up to phases, full rank was guaranteed before the call; the "
        "honest content is the structural conclusion that follows, namely that no "
        "chirality projector (1 +- gamma_5)/2 can split this carrier into blocks."
    )
    print(
        "  lattice_wide: checked and not executed - the runner is deliberately "
        "confined to a single carrier and says so, declining to identify the larger "
        "spacetime or gauge chirality mechanism, and the firewall block even "
        "enforces that boundary by requiring the note to keep larger chirality "
        "mechanisms separate. Nothing outside the one site is ever built: no second "
        "site, no coupling, no volume, no limit."
    )
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
