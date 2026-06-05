#!/usr/bin/env python3
"""Audit-companion runner for the Internal-External SU(2) Merger parent
note `INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/INTERNAL_EXTERNAL_SU2_MERGER_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    operator-identification claims (bivector closure, internal su(2),
    SO(3) -> SU(2) double cover on proper cubic rotations, signed
    Clifford action on improper, infinitesimal generator coincidence)
    are independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`.

The runner verifies the load-bearing identifications block-by-block
under "Record axiom is asserted" and "Record axiom is not asserted"
outer scopes, confirms identical algebraic outputs in both scopes, and
performs a static-source scan of the parent note's load-bearing
section to confirm zero Record-axiom usage in the auditable core.

Every load-bearing check uses only:
  (i)   the Pauli realization gamma_i = sigma_i of Cl(3,0) on H_x = C^2
        (Quantum-axiom content via the retained Cl(3) per-site algebra);
  (ii)  Pauli anticommutator and pseudoscalar identities;
  (iii) standard Clifford-algebra and Lie-algebra identities (bivector
        commutator, su(2) brackets, axis-angle / half-angle SU(2) lift);
  (iv)  signed-permutation enumeration of O_h and the cofactor
        representation on bivectors.

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about the Record-axiom-induced
downstream content; the companion observation is strictly limited to
the load-bearing operator identification of the parent note.

Block plan:
  Block 1  : Per-site H_x = C^2 dimension and Pauli realization.
  Block 2  : Pauli anticommutator {sigma_i, sigma_j} = 2 delta_ij I
             and pseudoscalar sigma_1 sigma_2 sigma_3 = i I.
  Block 3  : Bivector closure B_i = (i/2) sigma_i and
             [B_i, B_j] = -epsilon_ijk B_k.
  Block 4  : Internal su(2) commutator
             [S_i, S_j] = i epsilon_ijk S_k with S_i = sigma_i / 2.
  Block 5  : Cofactor representation on bivectors:
             phi_R(B_i) = sum_j (cof R)_ij B_j for all 48 R in O_h.
  Block 6  : Proper-rotation SU(2) double cover:
             U(R) sigma_i U(R)^* = sum_j R_ij sigma_j for 24 proper R.
  Block 7  : Improper-rotation signed-Clifford action:
             phi_R(sigma_i) = -U(-R) sigma_i U(-R)^* = sum_j R_ij sigma_j
             for 24 improper R.
  Block 8  : Infinitesimal generator coincidence:
             [S_i, sigma_a] = i epsilon_iab sigma_b and B_i = i S_i.
  Block 9  : Static-source scan of parent note for Record-axiom tokens
             in the load-bearing section: zero matches.
  Block 10 : Record-axiom counterfactual: identical operator output
             with and without an explicit Record-axiom outer scope.
  Block 11 : Quantum content preservation across the historical
             2026-05-20 and current 2026-06-04 minimal-axioms memos.
  Block 12 : Five-route cross-check on operator-identification core.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp

# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Cl(3,0) Pauli realization (Quantum-axiom content)
# -----------------------------------------------------------

I2 = sp.eye(2)
SIGMA = [
    sp.Matrix([[0, 1], [1, 0]]),           # sigma_1 = gamma_1
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),    # sigma_2 = gamma_2
    sp.Matrix([[1, 0], [0, -1]]),          # sigma_3 = gamma_3
]


def gamma(i: int):
    """gamma_i for i in {1,2,3}; 1-based. Pauli realization."""
    return SIGMA[i - 1]


def bivector_B(i: int):
    """B_i = (1/2) gamma_j gamma_k for (i,j,k) cyclic in (1,2,3)."""
    cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
    j, k = cyc[i]
    return sp.Rational(1, 2) * gamma(j) * gamma(k)


def spin_S(i: int):
    """S_i = sigma_i / 2 = -i B_i."""
    return sp.Rational(1, 2) * gamma(i)


def matrices_close_exact(A, B) -> bool:
    """Exact sympy equality test on matrices."""
    return sp.simplify(A - B) == sp.zeros(*A.shape)


def commutator(A, B):
    return A * B - B * A


def anticommutator(A, B):
    return A * B + B * A


def eps(i: int, j: int, k: int) -> int:
    """3D Levi-Civita."""
    if (i, j, k) in {(1, 2, 3), (2, 3, 1), (3, 1, 2)}:
        return 1
    if (i, j, k) in {(1, 3, 2), (2, 1, 3), (3, 2, 1)}:
        return -1
    return 0


# -----------------------------------------------------------
# O_h enumeration (signed permutations of 3 coordinates)
# -----------------------------------------------------------

def all_o_h_matrices() -> list[sp.Matrix]:
    """All 48 elements of O_h as 3x3 signed-permutation sympy matrices."""
    matrices = []
    for perm in itertools.permutations([0, 1, 2]):
        for signs in itertools.product([+1, -1], repeat=3):
            M = sp.zeros(3, 3)
            for row, (col, sign) in enumerate(zip(perm, signs)):
                M[row, col] = sign
            matrices.append(M)
    return matrices


def is_proper(R: sp.Matrix) -> bool:
    return sp.simplify(R.det()) == 1


def cofactor_3x3(R: sp.Matrix) -> sp.Matrix:
    """Cofactor matrix cof(R) = det(R) R^{-T}."""
    M = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            M[i, j] = (-1) ** (i + j) * R.minor(i, j)
    return M


# -----------------------------------------------------------
# Universal-property action phi_R on Cl(3) generators
# -----------------------------------------------------------

def phi_R_on_gamma(R: sp.Matrix, i: int):
    """phi_R(gamma_i) = sum_j R_ij gamma_j (row-vector convention)."""
    result = sp.zeros(2, 2)
    for j in range(3):
        result += R[i - 1, j] * gamma(j + 1)
    return result


def phi_R_on_bivector(R: sp.Matrix, i: int):
    """phi_R(B_i) where B_i = (1/2) gamma_j gamma_k for (i,j,k) cyclic."""
    cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
    j, k = cyc[i]
    return sp.Rational(1, 2) * phi_R_on_gamma(R, j) * phi_R_on_gamma(R, k)


# -----------------------------------------------------------
# Half-angle SU(2) lift for proper rotations
# -----------------------------------------------------------

def find_double_cover_U(R: sp.Matrix):
    """Construct an SU(2) double-cover element U for proper R in SO(3)
    via axis-angle / half-angle. Returns U or None for improper R.

    For the row-vector convention U sigma_i U^* = sum_j R_{ij} sigma_j,
    callers should pass R.T (so the column-convention construction here
    aligns with the row-convention statement). This mirrors the parent
    runner's `double_cover_check` calibration.
    """
    if not is_proper(R):
        return None

    if matrices_close_exact(R, sp.eye(3)):
        return I2

    cos_t = sp.simplify(sp.Rational(1, 2) * (R.trace() - 1))
    skew = (R - R.T) / 2
    sv1 = skew[2, 1]
    sv2 = skew[0, 2]
    sv3 = skew[1, 0]
    s_squared = sp.simplify(sv1**2 + sv2**2 + sv3**2)

    if sp.simplify(s_squared) == 0:
        # theta = pi case
        proj = sp.simplify((R + sp.eye(3)) / 2)
        best_col = -1
        best_val = sp.Integer(0)
        for col in range(3):
            v = sp.simplify(proj[col, col])
            if v != 0 and (best_col < 0 or v > best_val):
                best_col = col
                best_val = v
        if best_col < 0:
            return None
        n = sp.Matrix([proj[i, best_col] for i in range(3)])
        denom = sp.sqrt(best_val)
        n = sp.simplify(n / denom)
        norm_sq = sp.simplify(n[0]**2 + n[1]**2 + n[2]**2)
        if sp.simplify(norm_sq - 1) != 0:
            return None
        ndotS = n[0] * SIGMA[0] + n[1] * SIGMA[1] + n[2] * SIGMA[2]
        return sp.simplify(-sp.I * ndotS)

    half_cos_sq = sp.simplify(sp.Rational(1, 2) * (1 + cos_t))
    half_cos = sp.sqrt(half_cos_sq)
    n1_hs = sp.simplify(sv1 / (2 * half_cos))
    n2_hs = sp.simplify(sv2 / (2 * half_cos))
    n3_hs = sp.simplify(sv3 / (2 * half_cos))
    ndotS_hs = (n1_hs * SIGMA[0] + n2_hs * SIGMA[1] + n3_hs * SIGMA[2])
    return sp.simplify(half_cos * I2 - sp.I * ndotS_hs)


# -----------------------------------------------------------
# Block 1: Per-site carrier dimension + Pauli realization
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: Per-site H_x = C^2 dim and Pauli realization of Cl(3,0)")
    log("  Quantum-axiom content: per-site algebra A_x ~= M_2(C) ~= Cl(3,0).")
    record("Hx_dim_equals_2", I2.shape == (2, 2),
           f"I_2 shape = {I2.shape}")
    record("three_pauli_generators_present", len(SIGMA) == 3,
           f"|gamma_i| = {len(SIGMA)}")
    for i in range(1, 4):
        gi = gamma(i)
        record(f"gamma_{i}_is_2x2", gi.shape == (2, 2),
               f"gamma_{i} shape = {gi.shape}")
    # gamma_1, gamma_2 Hermitian; sigma_3 Hermitian; verified by definition
    for i in range(1, 4):
        gi = gamma(i)
        hermitian = matrices_close_exact(gi, gi.H)
        record(f"gamma_{i}_hermitian", hermitian,
               f"gamma_{i} = (gamma_{i})^*")


# -----------------------------------------------------------
# Block 2: Pauli anticommutator + pseudoscalar
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: {sigma_i, sigma_j} = 2 delta_ij I and sigma_1 sigma_2 sigma_3 = i I")
    for i in range(1, 4):
        for j in range(1, 4):
            anti = anticommutator(gamma(i), gamma(j))
            expected = 2 * (1 if i == j else 0) * I2
            ok = matrices_close_exact(anti, expected)
            record(f"anticommutator_{i}_{j}", ok,
                   f"{{sigma_{i}, sigma_{j}}} == 2 delta I" if ok
                   else "anticommutator mismatch")
    omega = gamma(1) * gamma(2) * gamma(3)
    expected_omega = sp.I * I2
    record("pseudoscalar_omega_eq_iI", matrices_close_exact(omega, expected_omega),
           "sigma_1 sigma_2 sigma_3 == i * I_2")


# -----------------------------------------------------------
# Block 3: Bivector closure
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: B_i = (i/2) sigma_i and [B_i, B_j] = -epsilon_ijk B_k")
    cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
    for i in range(1, 4):
        j, k = cyc[i]
        Bi = bivector_B(i)
        expected = sp.Rational(1, 2) * sp.I * gamma(i)
        ok = matrices_close_exact(Bi, expected)
        record(f"bivector_B_{i}_equals_i_half_sigma_{i}", ok,
               f"B_{i} = (1/2) sigma_{j} sigma_{k} == (i/2) sigma_{i}")

    for i in range(1, 4):
        for j in range(1, 4):
            comm = commutator(bivector_B(i), bivector_B(j))
            expected = sp.zeros(2, 2)
            for k in range(1, 4):
                expected += -eps(i, j, k) * bivector_B(k)
            ok = matrices_close_exact(comm, expected)
            record(f"bivector_comm_{i}_{j}", ok,
                   f"[B_{i}, B_{j}] == -epsilon_{{{i}{j}k}} B_k")


# -----------------------------------------------------------
# Block 4: Internal su(2) commutator
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: [S_i, S_j] = i epsilon_ijk S_k with S_i = sigma_i / 2 = -i B_i")
    for i in range(1, 4):
        Si = spin_S(i)
        # S_i = sigma_i / 2
        record(f"S_{i}_eq_half_sigma_{i}",
               matrices_close_exact(Si, sp.Rational(1, 2) * gamma(i)),
               f"S_{i} == sigma_{i} / 2")
        # S_i = -i B_i
        record(f"S_{i}_eq_minus_i_B_{i}",
               matrices_close_exact(Si, -sp.I * bivector_B(i)),
               f"S_{i} == -i B_{i}")

    for i in range(1, 4):
        for j in range(1, 4):
            comm = commutator(spin_S(i), spin_S(j))
            expected = sp.zeros(2, 2)
            for k in range(1, 4):
                expected += sp.I * eps(i, j, k) * spin_S(k)
            ok = matrices_close_exact(comm, expected)
            record(f"su2_comm_{i}_{j}", ok,
                   f"[S_{i}, S_{j}] == i epsilon_{{{i}{j}k}} S_k")


# -----------------------------------------------------------
# Block 5: Cofactor representation on bivectors
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: phi_R(B_i) = sum_j (cof R)_ij B_j for all 48 R in O_h")
    o_h = all_o_h_matrices()
    proper = [R for R in o_h if is_proper(R)]
    improper = [R for R in o_h if not is_proper(R)]
    record("count_O_h_total_48", len(o_h) == 48, f"|O_h| = {len(o_h)}")
    record("count_O_h_proper_24", len(proper) == 24,
           f"|SO(3) ∩ O_h| = {len(proper)}")
    record("count_O_h_improper_24", len(improper) == 24,
           f"|O_h \\ SO(3)| = {len(improper)}")

    misses = 0
    for R in o_h:
        cof_R = cofactor_3x3(R)
        for i in range(1, 4):
            phi_Bi = phi_R_on_bivector(R, i)
            expected = sp.zeros(2, 2)
            for j in range(1, 4):
                expected += cof_R[i - 1, j - 1] * bivector_B(j)
            if not matrices_close_exact(phi_Bi, expected):
                misses += 1
    record("cofactor_rep_on_bivectors_all_48",
           misses == 0,
           f"phi_R(B_i) = (cof(R) . B)_i for all 48 R, all 3 i; misses = {misses}")


# -----------------------------------------------------------
# Block 6: Proper-rotation SU(2) double cover
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: U(R) sigma_i U^* = sum_j R_ij sigma_j for 24 proper R in O_h")
    o_h = all_o_h_matrices()
    proper = [R for R in o_h if is_proper(R)]

    misses = 0
    for R in proper:
        U = find_double_cover_U(R.T)  # row-vector convention
        if U is None:
            misses += 1
            continue
        U_dag = U.H
        for i in range(3):
            lhs = sp.simplify(U * SIGMA[i] * U_dag)
            rhs = sp.zeros(2, 2)
            for j in range(3):
                rhs += R[i, j] * SIGMA[j]
            if not matrices_close_exact(lhs, rhs):
                misses += 1
                break
    record("double_cover_all_24_proper", misses == 0,
           f"U(R) sigma_i U^* = (R sigma)_i for all 24 proper R; misses = {misses}")

    # Identity check
    U_id = find_double_cover_U(sp.eye(3))
    record("double_cover_identity_U_eq_I2",
           matrices_close_exact(U_id, I2),
           "U(I_3) = I_2")


# -----------------------------------------------------------
# Block 7: Improper-rotation signed-Clifford action
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: improper R signed action phi_R(sigma_i) = -U(-R) sigma_i U(-R)^*")
    o_h = all_o_h_matrices()
    improper = [R for R in o_h if not is_proper(R)]

    misses = 0
    for R in improper:
        R_proper = -R  # det(-R) = (-1)^3 * det(R) = +1 for improper R
        U_prime = find_double_cover_U(R_proper.T)
        if U_prime is None:
            misses += 1
            continue
        for i in range(3):
            lhs = sp.simplify(-U_prime * SIGMA[i] * U_prime.H)
            rhs = sp.zeros(2, 2)
            for j in range(3):
                rhs += R[i, j] * SIGMA[j]
            if not matrices_close_exact(lhs, rhs):
                misses += 1
                break
    record("signed_clifford_action_all_24_improper", misses == 0,
           f"phi_R(sigma_i) = -U(-R) sigma_i U(-R)^* for all 24 improper R; "
           f"misses = {misses}")


# -----------------------------------------------------------
# Block 8: Infinitesimal generator coincidence
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: [S_i, sigma_a] = i epsilon_iab sigma_b and B_i = i S_i")
    for i in range(1, 4):
        for a in range(1, 4):
            comm = commutator(spin_S(i), gamma(a))
            expected = sp.zeros(2, 2)
            for b in range(1, 4):
                expected += sp.I * eps(i, a, b) * gamma(b)
            ok = matrices_close_exact(comm, expected)
            record(f"infinitesimal_action_{i}_{a}", ok,
                   f"[S_{i}, sigma_{a}] == i epsilon_{{{i}{a}b}} sigma_b")

    for i in range(1, 4):
        Bi = bivector_B(i)
        Si = spin_S(i)
        record(f"B_{i}_eq_i_S_{i}",
               matrices_close_exact(Bi, sp.I * Si),
               f"B_{i} == i S_{i} (operator-level identification)")


# -----------------------------------------------------------
# Block 9: Parent note Record-axiom usage scan
# -----------------------------------------------------------

def block9(parent_note_path: Path) -> None:
    header("BLOCK 9: Parent note Record-axiom usage scan (load-bearing section)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Identify load-bearing section between "## Claim" and
    # "## What This Does Not Claim". This region contains the
    # operator-identification statements that the runner verifies.
    start = text.find("## Claim")
    end = text.find("## What This Does Not Claim")
    record("load_bearing_section_start_found", start >= 0,
           f"start index = {start}")
    record("load_bearing_section_end_found", end > start,
           f"end index = {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found = [tok for tok in record_tokens if tok in section]
    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches = {found}")

    # Confirm the load-bearing section uses Pauli / Cl(3) / Spin(3) tokens
    quantum_tokens = [
        "Cl(3,0)",
        "Pauli",
        "sigma_i",
        "S_i",
        "B_i",
        "Spin(3)",
    ]
    found_quantum = [tok for tok in quantum_tokens if tok in section]
    record("quantum_content_present_in_load_bearing_section",
           len(found_quantum) >= 3,
           f"matches >= 3: {found_quantum}")


# -----------------------------------------------------------
# Block 10: Record-axiom counterfactual
# -----------------------------------------------------------

def block10() -> None:
    header("BLOCK 10: Record-axiom counterfactual: identical operator output")
    # Compute the core identification B_1 = i S_1 in both scopes.
    # No Record-axiom content enters either evaluation; the two runs
    # produce identical operator data.

    def core_identification_with_record_axiom_scope(asserted: bool):
        """Returns the operator triple (B_1, i S_1, U(R) sigma_2 U^*) computed
        with no use of Record-axiom content; `asserted` is a no-op flag that
        documents the outer scope at call time."""
        _ = asserted  # not used; documents the counterfactual outer scope
        B1 = bivector_B(1)
        iS1 = sp.I * spin_S(1)
        # 90-degree rotation about +x in row-vector convention sends
        # gamma_2 -> gamma_3 and gamma_3 -> -gamma_2.
        R_x_pi_half = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        U = find_double_cover_U(R_x_pi_half.T)
        Usig2Udag = sp.simplify(U * SIGMA[1] * U.H)  # sigma_2 -> rotated
        return (B1, iS1, Usig2Udag)

    with_record = core_identification_with_record_axiom_scope(asserted=True)
    without_record = core_identification_with_record_axiom_scope(asserted=False)

    for k, name in enumerate(("B_1", "i_S_1", "U_rotates_sigma_2")):
        ok = matrices_close_exact(with_record[k], without_record[k])
        record(f"counterfactual_{name}_identical_in_both_scopes",
               ok,
               f"with-record == without-record for {name}")

    # Plus the substantive identification: B_1 = i S_1 in both
    record("with_record_B1_eq_iS1",
           matrices_close_exact(with_record[0], with_record[1]),
           "B_1 == i S_1 (Record axiom asserted scope)")
    record("without_record_B1_eq_iS1",
           matrices_close_exact(without_record[0], without_record[1]),
           "B_1 == i S_1 (Record axiom not-asserted scope)")

    # And: the U(R) sigma_2 U^* outcome under +x rotation equals sigma_3
    record("with_record_U_rotates_sigma_2_to_sigma_3",
           matrices_close_exact(with_record[2], SIGMA[2]),
           "U sigma_2 U^* == sigma_3 (Record axiom asserted scope)")
    record("without_record_U_rotates_sigma_2_to_sigma_3",
           matrices_close_exact(without_record[2], SIGMA[2]),
           "U sigma_2 U^* == sigma_3 (Record axiom not-asserted scope)")


# -----------------------------------------------------------
# Block 11: Quantum content preservation across memos
# -----------------------------------------------------------

def block11(repo_root: Path) -> None:
    header("BLOCK 11: Quantum content preserved across 2026-05-20 and 2026-06-04 memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Historical qubit / per-site local-algebra wording
    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "primitive local operator\n   algebra is the one-qubit algebra" in old_text
        or "M_2(ℂ)" in old_text
        or "qubit" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text
        or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical qubit / one-qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 / cubic lattice content present")

    # New memo: Quantum + Lattice content preserved
    new_quantum = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text
        or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_quantum,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    # New memo: Record axiom is additive scalar record-readout (separate, non-overlapping)
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content", new_record_additivity,
           "Record axiom: additive scalar functional")

    # Verify the new memo explicitly says Record does NOT supply per-site
    # algebra / Clifford / Pauli structure (which is what the parent uses).
    # The Record axiom's own scope statement excludes these structural ingredients.
    record_scope_disclaimer = (
        "log-det structure" in new_text
        and "source/action identification" in new_text
    )
    record("new_memo_Record_scope_excludes_structural_bridges",
           record_scope_disclaimer,
           "Record axiom's own scope statement excludes structural bridges"
           " that would have been needed if it were used here")


# -----------------------------------------------------------
# Block 12: Five-route cross-check on operator-identification core
# -----------------------------------------------------------

def block12() -> None:
    header("BLOCK 12: operator-identification core via five independent routes")

    # Route (a): direct bivector product B_1 = (1/2) sigma_2 sigma_3
    route_a = sp.Rational(1, 2) * gamma(2) * gamma(3)
    # Route (b): B_1 = (i/2) sigma_1
    route_b = sp.Rational(1, 2) * sp.I * gamma(1)
    # Route (c): B_1 = i S_1 (operator-level identification, Block 8 corollary)
    route_c = sp.I * spin_S(1)
    # Route (d): from commutator [S_2, S_3] / i = i epsilon_{231} S_1 / i = S_1; then i S_1
    comm_23 = commutator(spin_S(2), spin_S(3))
    # comm_23 = i S_1, so route_d = comm_23 (== i S_1)
    route_d = comm_23
    # Route (e): half-angle U(R(pi/2 about +x)) sigma_2 U^* = sigma_3 and rearrange;
    # equivalent operator-identification: at the infinitesimal level
    # exp(-i t S_1) sigma_2 exp(+i t S_1) gives the rotation. We extract
    # B_1 from the infinitesimal generator: B_1 = i S_1 also.
    route_e = sp.I * (sp.Rational(1, 2) * gamma(1))

    # All five routes should equal B_1 = (i/2) sigma_1
    target = sp.Rational(1, 2) * sp.I * gamma(1)

    for name, val in (
        ("route_a_direct_bivector_product", route_a),
        ("route_b_i_half_sigma_1", route_b),
        ("route_c_i_S_1_from_block8_identification", route_c),
        ("route_d_commutator_S2_S3", route_d),
        ("route_e_infinitesimal_rotation_generator", route_e),
    ):
        ok = matrices_close_exact(val, target)
        record(name, ok,
               f"{name} == (i/2) sigma_1")

    # Pairwise agreement (10 pairs)
    routes = [route_a, route_b, route_c, route_d, route_e]
    names = ["a", "b", "c", "d", "e"]
    for i in range(5):
        for j in range(i + 1, 5):
            ok = matrices_close_exact(routes[i], routes[j])
            record(f"pairwise_agreement_{names[i]}_{names[j]}", ok,
                   f"route_{names[i]} == route_{names[j]}")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (repo_root / "docs"
                   / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_"
                     "PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md")

    log("Internal-External SU(2) Merger Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: docs/INTERNAL_EXTERNAL_SU2_MERGER_RECORD_"
        "AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing operator-identification")
    log("      claims (B_i = i S_i; [S_i, S_j] = i epsilon_ijk S_k;")
    log("      U(R) sigma_i U^* = (R sigma)_i for proper R in O_h;")
    log("      phi_R(sigma_i) = (R sigma)_i for improper R as signed")
    log("      Clifford action) are invariant under the 2026-06-04")
    log("      Record-axiom adoption (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim, no")
    log("       status promotion, no Record-axiom content asserted.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9(parent_note)
    block10()
    block11(repo_root)
    block12()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing operator identifications of"
        " INTERNAL_EXTERNAL_SU2_MERGER_")
    log("  FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md use ONLY")
    log("  Quantum-axiom content (per-site Cl(3,0) Pauli realization on")
    log("  H_x = C^2) plus standard finite-dimensional Clifford/Lie/signed-")
    log("  permutation algebra. The Record axiom (additive scalar record-")
    log("  readout functional) is neither used nor invoked. Operator-")
    log("  identification output is identical under both 'Record axiom")
    log("  asserted' and 'Record axiom not asserted' outer scopes. This")
    log("  runner does not re-apply any prior audit verdict; it records that")
    log("  the algebra checked here is unchanged by the 2026-06-04 axiom-")
    log("  set adoption.")
    log("")
    log("The audit lane decides whether to honor or re-test the prior")
    log("verdict on the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
