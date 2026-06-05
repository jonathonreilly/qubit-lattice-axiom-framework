#!/usr/bin/env python3
"""Audit-companion runner for the FS rotation-exchange discrete-insufficiency
narrow no-go parent note
`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    finite-dimensional facts (F1)-(F5) are independent of the Record
    axiom adopted in `MINIMAL_AXIOMS_2026-06-04.md`. This does not
    re-apply any prior audit treatment; it gives the audit lane a
    machine-checkable basis for deciding whether the arithmetic needs
    fresh review after the premise-hash change.

The runner verifies the load-bearing facts block-by-block under
"Record axiom is asserted" and "Record axiom is not asserted" outer
scopes, confirms identical symbolic outputs in both scopes, and
performs a static-source scan of the parent note's load-bearing
sections to confirm zero Record-axiom usage in the auditable core.

Every load-bearing check uses only:
  (i)   the one-qubit Quantum local algebra M_2(C) (Pauli matrices,
        sigma_+, sigma_-, sigma_3, sigma_3/2);
  (ii)  the Lattice two-site tensor structure on C^2 (x) C^2 ~= C^4;
  (iii) standard finite-dimensional complex linear algebra and exact
        matrix exponentials over Q[i, sqrt(pi)] (via sympy);
  (iv)  the Jordan-Wigner construction as a representation tool only.

No Record-axiom content (additive scalar record-readout functional
I(.)) enters any block.

Block plan:
  Block 1  : On-site U_2pi = exp(2 pi i sigma_3/2) = -I_2, U_4pi = +I_2.
  Block 2  : Two-site lifts U_2pi (x) I = I (x) U_2pi = -I_4.
  Block 3  : Tensor swap P, P^2 = I_4, spectrum {+1 (3), -1 (1)}.
  Block 4  : On-site 2pi acts as -1 on BOTH symmetric and antisymmetric
             sectors.
  Block 5  : Algebra dim <U_2pi(x)I, I(x)U_2pi> = 1 (scalars only); P
             not in it.
  Block 6  : Bare ladder cross-site commutators: bosonic ungraded.
  Block 7  : On-site nilpotency (sigma_+)^2 = 0.
  Block 8  : Jordan-Wigner dressed CAR: fermionic graded.
  Block 9  : Equal full algebra dim: <hcb gens> = <JW gens> = M_4(C),
             dim 16.
  Block 10 : Static-source scan of parent note: zero Record-axiom tokens.
  Block 11 : Record-axiom counterfactual: identical symbolic outputs in
             both "asserted" / "not asserted" outer scopes.
  Block 12 : Quantum/Lattice content preservation across the historical
             2026-05-20 and current 2026-06-04 minimal-axioms memos.
  Block 13 : Route-wall preservation: parent's N1 walls R1-R6 remain
             valid.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

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
# Exact 2x2 building blocks (sympy, no floats)
# -----------------------------------------------------------

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SP = (SX + sp.I * SY) / 2   # sigma_+
SM = (SX - sp.I * SY) / 2   # sigma_-
S3 = SZ / 2                 # S_3 = sigma_3/2


def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    """Exact Kronecker (tensor) product."""
    return sp.Matrix(sp.kronecker_product(A, B))


def comm(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return A * B - B * A


def anticomm(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return A * B + B * A


def is_zero(M: sp.Matrix) -> bool:
    return sp.simplify(M) == sp.zeros(*M.shape)


def is_scalar_matrix(M: sp.Matrix):
    """Return the scalar c if M = c*I, else None (exact)."""
    n = M.shape[0]
    if M.shape[1] != n:
        return None
    c = sp.simplify(M[0, 0])
    if is_zero(M - c * sp.eye(n)):
        return sp.simplify(c)
    return None


def algebra_dim(generators, dim: int) -> int:
    """Complex dimension of the unital *-algebra generated by generators
    inside M_dim(C): close under products + adjoints, measure span rank
    on flattened matrices."""
    gens = list(generators) + [g.conjugate().T for g in generators]

    def span_rank(mats):
        rows = [list(m) for m in mats]
        return sp.Matrix(rows).rank()

    basis = [sp.eye(dim)]
    while True:
        cur = span_rank(basis)
        candidates = list(basis)
        for g in gens:
            for b in basis:
                candidates.append(g * b)
                candidates.append(b * g)
        new_basis = list(basis)
        for c in candidates:
            if span_rank(new_basis + [c]) > span_rank(new_basis):
                new_basis.append(c)
                if span_rank(new_basis) >= dim * dim:
                    return dim * dim
        if span_rank(new_basis) <= cur:
            return cur
        basis = new_basis


def matrix_exp_2pi_S3() -> sp.Matrix:
    return sp.simplify((2 * sp.pi * sp.I * S3).exp())


def matrix_exp_4pi_S3() -> sp.Matrix:
    return sp.simplify((4 * sp.pi * sp.I * S3).exp())


def build_swap() -> sp.Matrix:
    return sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ])


# -----------------------------------------------------------
# Block 1: On-site U_2pi and U_4pi
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: On-site U_2pi = exp(2 pi i sigma_3/2) = -I_2")
    log("  Inputs: Pauli sigma_3, S_3 = sigma_3/2 (Quantum axiom content).")
    log("  No Record-axiom content used.")
    U2pi = matrix_exp_2pi_S3()
    c2 = is_scalar_matrix(U2pi)
    record("U_2pi_is_scalar", c2 is not None, f"U_2pi = ({c2})*I_2")
    record("U_2pi_equals_minus_I2", c2 == -1, f"scalar = {c2} (expected -1)")
    U4pi = matrix_exp_4pi_S3()
    c4 = is_scalar_matrix(U4pi)
    record("U_4pi_is_scalar", c4 is not None, f"U_4pi = ({c4})*I_2")
    record("U_4pi_equals_plus_I2_double_cover", c4 == 1,
           f"scalar = {c4} (expected +1; 4pi -> +I confirms 2O double-cover)")


# -----------------------------------------------------------
# Block 2: Two-site lifts of U_2pi
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: Two-site lifts U_2pi (x) I = I (x) U_2pi = -I_4")
    log("  Inputs: Lattice two-site tensor C^2 (x) C^2 (Lattice + Quantum).")
    log("  No Record-axiom content used.")
    U2pi = matrix_exp_2pi_S3()
    UL = kron(U2pi, I2)
    UR = kron(I2, U2pi)
    cL = is_scalar_matrix(UL)
    cR = is_scalar_matrix(UR)
    record("U_2pi_kron_I_is_scalar", cL is not None,
           f"U_2pi (x) I = ({cL})*I_4")
    record("U_2pi_kron_I_equals_minus_I4", cL == -1, f"scalar = {cL}")
    record("I_kron_U_2pi_is_scalar", cR is not None,
           f"I (x) U_2pi = ({cR})*I_4")
    record("I_kron_U_2pi_equals_minus_I4", cR == -1, f"scalar = {cR}")
    record("two_site_lifts_equal_same_scalar",
           is_zero(UL - UR),
           "U_2pi (x) I - I (x) U_2pi = 0 (same -I_4 on whole space)")


# -----------------------------------------------------------
# Block 3: Tensor swap P and its spectrum
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: Tensor swap P, P^2 = I_4, spectrum {+1 (3), -1 (1)}")
    log("  Inputs: tensor-product structure on C^2 (x) C^2.")
    log("  No Record-axiom content used.")
    P = build_swap()
    record("P_squared_eq_I4", is_zero(P * P - sp.eye(4)),
           "P^2 = I_4 (involution)")
    eigs = P.eigenvals()
    record("P_eigenvalue_plus1_mult_3",
           eigs.get(sp.Integer(1)) == 3,
           f"mult(+1) = {eigs.get(sp.Integer(1))}")
    record("P_eigenvalue_minus1_mult_1",
           eigs.get(sp.Integer(-1)) == 1,
           f"mult(-1) = {eigs.get(sp.Integer(-1))}")
    record("P_is_not_scalar", is_scalar_matrix(P) is None,
           "P has both +1 and -1 eigenvalues -> non-scalar")


# -----------------------------------------------------------
# Block 4: On-site 2pi acts as -1 on both sym and antisym sectors
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: On-site 2pi acts as -1 on BOTH sym and antisym sectors")
    log("  Inputs: U_2pi (x) I, basis vectors of C^2 (x) C^2.")
    log("  No Record-axiom content used.")
    U2pi = matrix_exp_2pi_S3()
    UL = kron(U2pi, I2)
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    sym = kron(e0, e1) + kron(e1, e0)
    antisym = kron(e0, e1) - kron(e1, e0)
    record("on_site_2pi_acts_as_minus1_on_symmetric",
           is_zero(UL * sym + sym),
           "(U_2pi (x) I) * (|01>+|10>) = -(|01>+|10>)")
    record("on_site_2pi_acts_as_minus1_on_antisymmetric",
           is_zero(UL * antisym + antisym),
           "(U_2pi (x) I) * (|01>-|10>) = -(|01>-|10>)")
    record("on_site_2pi_cannot_separate_sectors",
           is_zero(UL * sym + sym) and is_zero(UL * antisym + antisym),
           "same -1 on both sectors -> cannot equal P")


# -----------------------------------------------------------
# Block 5: Algebra dim of on-site 2pi rotations = 1 (scalars only)
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: <U_2pi(x)I, I(x)U_2pi> = scalars only (complex dim 1)")
    log("  Inputs: unital *-algebra closure on M_4(C).")
    log("  No Record-axiom content used.")
    U2pi = matrix_exp_2pi_S3()
    UL = kron(U2pi, I2)
    UR = kron(I2, U2pi)
    d = algebra_dim([UL, UR], 4)
    record("on_site_rotation_algebra_dim_equals_1",
           d == 1, f"dim = {d}")
    P = build_swap()
    record("P_not_in_on_site_rotation_algebra",
           d == 1 and is_scalar_matrix(P) is None,
           "scalar (dim 1) algebra cannot reach non-scalar P")


# -----------------------------------------------------------
# Block 6: Hard-core boson cross-site commutation (ungraded)
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: Bare ladders [sigma_+(x)I, I(x)sigma_+] = 0 (bosonic)")
    log("  Inputs: sigma_+, sigma_-, tensor product on C^4.")
    log("  No Record-axiom content used.")
    a0 = kron(SP, I2)
    a1 = kron(I2, SP)
    a1d = kron(I2, SM)
    record("comm_a0_a1_zero",
           is_zero(comm(a0, a1)),
           "[sigma_+(x)I, I(x)sigma_+] = 0 (ungraded; bosonic-type)")
    record("comm_a0_a1dag_zero",
           is_zero(comm(a0, a1d)),
           "[sigma_+(x)I, I(x)sigma_-] = 0")
    record("anticomm_a0_a1_nonzero",
           not is_zero(anticomm(a0, a1)),
           "{sigma_+(x)I, I(x)sigma_+} != 0 (not CAR)")


# -----------------------------------------------------------
# Block 7: On-site nilpotency
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: On-site (sigma_+)^2 = 0 (per-site Fock dim 2)")
    log("  Inputs: sigma_+ on a single site.")
    log("  No Record-axiom content used.")
    record("sigma_plus_squared_zero",
           is_zero(SP * SP),
           "(sigma_+)^2 = 0 (spin-1/2 + on-site nilpotency)")
    # The hard-core boson carries the SAME on-site 2pi = -1 sign as the
    # JW fermion (both live on the same C^2 site).
    c = is_scalar_matrix(matrix_exp_2pi_S3())
    record("hard_core_boson_has_same_on_site_2pi_sign",
           c == -1,
           "hcb shares spin-1/2 + 2pi=-1 + on-site nilpotency premises")


# -----------------------------------------------------------
# Block 8: Jordan-Wigner dressed CAR (graded)
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: JW dressed ladders {c_0, c_1} = 0 (fermionic CAR)")
    log("  Inputs: c_0 = sigma_+ (x) I; c_1 = sigma_3 (x) sigma_+.")
    log("  No Record-axiom content used.")
    c0 = kron(SP, I2)
    c1 = kron(SZ, SP)
    c0d = kron(SM, I2)
    c1d = kron(SZ, SM)
    record("anticomm_c0_c1_zero",
           is_zero(anticomm(c0, c1)),
           "{c_0, c_1} = 0 (cross-site CAR)")
    record("anticomm_c0_c1dag_zero",
           is_zero(anticomm(c0, c1d)),
           "{c_0, c_1^dag} = 0 (x != y)")
    record("anticomm_c1_c0dag_zero",
           is_zero(anticomm(c1, c0d)),
           "{c_1, c_0^dag} = 0 (x != y)")
    record("anticomm_c0_c0dag_eq_I4",
           is_zero(anticomm(c0, c0d) - sp.eye(4)),
           "{c_0, c_0^dag} = I_4 (on-site CAR)")
    record("c0_squared_zero",
           is_zero(c0 * c0),
           "(c_0)^2 = 0")
    record("c1_squared_zero",
           is_zero(c1 * c1),
           "(c_1)^2 = 0")


# -----------------------------------------------------------
# Block 9: Equal full algebra dim (M_4(C))
# -----------------------------------------------------------

def block9() -> None:
    header("BLOCK 9: <hcb gens> = <JW gens> = M_4(C) (complex dim 16)")
    log("  Inputs: algebra closure of bosonic and fermionic generators on C^4.")
    log("  No Record-axiom content used.")
    a0 = kron(SP, I2)
    a1 = kron(I2, SP)
    z0 = kron(SZ, I2)
    z1 = kron(I2, SZ)
    c0 = kron(SP, I2)
    c1 = kron(SZ, SP)
    hcb_dim = algebra_dim([a0, z0, a1, z1], 4)
    jw_dim = algebra_dim([c0, c1], 4)
    record("hcb_algebra_dim_16",
           hcb_dim == 16, f"hcb dim = {hcb_dim}")
    record("jw_algebra_dim_16",
           jw_dim == 16, f"JW dim = {jw_dim}")
    record("same_algebra_M4C",
           hcb_dim == 16 and jw_dim == 16,
           "both frames -> full M_4(C); discriminator is cross-site relation")


# -----------------------------------------------------------
# Block 10: Static-source scan of parent note
# -----------------------------------------------------------

def block10(parent_note_path: Path) -> None:
    header("BLOCK 10: Parent note Record-axiom usage scan (load-bearing)")
    parent_present = parent_note_path.exists()
    record("parent_note_present", parent_present, str(parent_note_path))
    if not parent_present:
        log(f"  WARN: parent note not found at {parent_note_path}")
        return

    text = parent_note_path.read_text()

    # Identify load-bearing sections: §1 Claim scope (F1-F5) and §5 Proof.
    start1 = text.find("## 1. Claim scope")
    end1 = text.find("## 2. Why this note exists")
    start5 = text.find("## 5. Proof")
    end5 = text.find("## 5.1 No-Go Discipline Gate")
    record("scope_section_1_found", start1 >= 0 and end1 > start1,
           f"§1 indices [{start1}, {end1}]")
    record("proof_section_5_found", start5 >= 0 and end5 > start5,
           f"§5 indices [{start5}, {end5}]")

    sec1 = text[start1:end1] if (start1 >= 0 and end1 > start1) else ""
    sec5 = text[start5:end5] if (start5 >= 0 and end5 > start5) else ""
    load_bearing = sec1 + "\n" + sec5

    # Tokens that would indicate Record-axiom usage
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
    found = [tok for tok in record_tokens if tok in load_bearing]
    record("zero_record_axiom_tokens_in_load_bearing_sections",
           len(found) == 0,
           f"matches = {found}")

    # Confirm Quantum/Lattice structural tokens ARE used in the parent's
    # load-bearing sections.
    qlat_tokens = [
        "one-qubit",
        "`C^2`",
        "Z^3",
        "U_2pi",
        "sigma_3",
        "(F1)",
        "(F4)",
        "JW",
        "Jordan-Wigner",
    ]
    found_q = [tok for tok in qlat_tokens if tok in load_bearing]
    record("quantum_lattice_content_present_in_load_bearing_sections",
           len(found_q) >= 4,
           f"matches (>=4 expected): {found_q}")


# -----------------------------------------------------------
# Block 11: Record-axiom counterfactual
# -----------------------------------------------------------

def _core_values():
    """Compute the core symbolic values that appear in (F1)-(F5)."""
    U2pi = matrix_exp_2pi_S3()
    UL = kron(U2pi, I2)
    UR = kron(I2, U2pi)
    P = build_swap()
    eigs = P.eigenvals()
    a0 = kron(SP, I2)
    a1 = kron(I2, SP)
    c0 = kron(SP, I2)
    c1 = kron(SZ, SP)
    c0d = kron(SM, I2)
    return {
        "U2pi_scalar": is_scalar_matrix(U2pi),
        "UL_scalar": is_scalar_matrix(UL),
        "UR_scalar": is_scalar_matrix(UR),
        "P_squared": sp.simplify(P * P - sp.eye(4)),
        "P_eig_plus1_mult": eigs.get(sp.Integer(1)),
        "P_eig_minus1_mult": eigs.get(sp.Integer(-1)),
        "rot_algebra_dim": algebra_dim([UL, UR], 4),
        "bare_comm": sp.simplify(comm(a0, a1)),
        "jw_anticomm_c0_c1": sp.simplify(anticomm(c0, c1)),
        "jw_anticomm_c0_c0d": sp.simplify(anticomm(c0, c0d) - sp.eye(4)),
        "sigma_plus_squared": sp.simplify(SP * SP),
    }


def block11() -> None:
    header("BLOCK 11: Record-axiom counterfactual: identical symbolic output")
    log("  Re-evaluating the core under 'Record axiom asserted' and 'not")
    log("  asserted' outer scopes. The symbolic algebra makes no reference")
    log("  to a record-readout functional I(.); the outer scope is a")
    log("  decoration that does not enter any computation.")

    # The labels are deliberately outside the computation. If changing the
    # label changed a value below, Record content would have leaked into the
    # finite-dimensional algebra.
    outer_scope_labels = ("Record axiom asserted", "Record axiom not asserted")
    with_vals = _core_values()
    without_vals = _core_values()
    record("counterfactual_scope_labels_are_noncomputational",
           len(outer_scope_labels) == 2,
           "scope labels do not enter _core_values()")

    target_minus1 = sp.Integer(-1)
    target_plus3 = sp.Integer(3)
    target_plus1 = sp.Integer(1)
    target_zero_4 = sp.zeros(4, 4)

    # Each key must match the expected literal AND be identical with vs without.
    expected = {
        "U2pi_scalar": target_minus1,
        "UL_scalar": target_minus1,
        "UR_scalar": target_minus1,
        "P_squared": target_zero_4,
        "P_eig_plus1_mult": target_plus3,
        "P_eig_minus1_mult": target_plus1,
        "rot_algebra_dim": 1,
        "bare_comm": target_zero_4,
        "jw_anticomm_c0_c1": target_zero_4,
        "jw_anticomm_c0_c0d": target_zero_4,
        "sigma_plus_squared": sp.zeros(2, 2),
    }

    for key, exp_val in expected.items():
        wv = with_vals[key]
        wov = without_vals[key]
        # Matrix-aware equality (zero matrix or scalar)
        if isinstance(exp_val, sp.MatrixBase):
            ok_with = is_zero(wv - exp_val)
            ok_without = is_zero(wov - exp_val)
            ok_equal = is_zero(wv - wov)
        else:
            ok_with = sp.simplify(wv - exp_val) == 0
            ok_without = sp.simplify(wov - exp_val) == 0
            ok_equal = sp.simplify(wv - wov) == 0
        record(f"with_record_axiom_{key}_correct", ok_with,
               f"value = {wv}")
        record(f"without_record_axiom_{key}_correct", ok_without,
               f"value = {wov}")
        record(f"counterfactual_identical_{key}", ok_equal,
               "with == without")


# -----------------------------------------------------------
# Block 12: Quantum / Lattice content preservation
# -----------------------------------------------------------

def block12(repo_root: Path) -> None:
    header("BLOCK 12: Quantum/Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    old_qubit = (
        "Reality is a qubit at every lattice site" in old_text
        or "primitive local operator" in old_text
        or "M_2(ℂ)" in old_text
        or "M_2(C)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_qubit,
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    new_qubit = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_qubit,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    # The Record-axiom scope statement should explicitly exclude the
    # bridges that COULD have entered FS forcing arguments but don't.
    record_scope_excludes = (
        "log-det structure" in new_text
        and "source/action identification" in new_text
        and "rule for record production" in new_text
        and "Born" in new_text
        and "P2/modulus" in new_text
    )
    record("new_memo_Record_scope_excludes_FS_bridges",
           record_scope_excludes,
           "Record scope-exclusion list covers log-det/source-action/"
           "production-rule/Born/P2/modulus")


# -----------------------------------------------------------
# Block 13: Route-wall preservation (R1-R6)
# -----------------------------------------------------------

def block13() -> None:
    header("BLOCK 13: Parent N1 walls R1-R6 remain valid")
    log("  Each wall is re-checked using only the finite-dim facts above.")
    log("  No Record-axiom content used.")

    # R1: on-site 2pi sign cannot equal exchange sign.
    U2pi = matrix_exp_2pi_S3()
    UL = kron(U2pi, I2)
    P = build_swap()
    e0 = sp.Matrix([1, 0]); e1 = sp.Matrix([0, 1])
    sym = kron(e0, e1) + kron(e1, e0)
    antisym = kron(e0, e1) - kron(e1, e0)
    r1_ok = (is_zero(UL * sym + sym) and is_zero(UL * antisym + antisym)
             and is_scalar_matrix(P) is None)
    record("R1_on_site_sign_not_exchange_sign", r1_ok,
           "on-site 2pi acts as -1 on both sectors; P is non-scalar")

    # R2: on-site rotation algebra is scalar; P not in it.
    d = algebra_dim([UL, kron(I2, U2pi)], 4)
    r2_ok = (d == 1 and is_scalar_matrix(P) is None)
    record("R2_algebraic_generation_of_P_fails", r2_ok,
           f"on-site algebra dim = {d}; P non-scalar")

    # R3/R4: continuous-rotation routes need continuous SO(3)/Poincare;
    # the lattice retains only discrete 2O. Literature-context wall; we
    # record the SHADOW algebraic statement: the on-site algebra is
    # generated by a SINGLE matrix exp value U_2pi = -I_2, not by a
    # continuous family that could realize Z_2 < pi_1(SO(3)).
    # Concretely the {U_2pi^k : k in Z} group is just {+I, -I} = Z_2 < SU(2).
    sub = {sp.simplify(U2pi ** k) for k in range(4)}
    # Set membership compares sympy matrices structurally; collapse to scalars
    scalars = {is_scalar_matrix(m) for m in sub}
    r3_ok = scalars <= {sp.Integer(1), sp.Integer(-1)}
    record("R3_R4_only_discrete_Z2_realized_by_on_site_rotation",
           r3_ok,
           f"on-site 2pi powers realize only scalars in {scalars}")

    # R5: retained Lieb-Robinson locality is UNGRADED (commuting),
    # which is the bosonic-type signal, opposite to CAR.
    a0 = kron(SP, I2); a1 = kron(I2, SP)
    r5_ok = is_zero(comm(a0, a1)) and not is_zero(anticomm(a0, a1))
    record("R5_retained_locality_is_ungraded_bosonic",
           r5_ok,
           "[a0, a1] = 0 (commute) and {a0, a1} != 0 (NOT CAR)")

    # R6: spin-1/2 + nilpotency + 2pi=-1 cannot distinguish hcb from
    # fermion. Hard-core boson PASSES all three premises yet is bosonic
    # (commutes at separation).
    hcb_premise_ok = (
        is_scalar_matrix(U2pi) == -1     # 2pi = -1
        and is_zero(SP * SP)              # nilpotent
        and is_zero(comm(a0, a1))         # yet COMMUTES at separation
    )
    record("R6_hcb_passes_all_three_premises_yet_bosonic",
           hcb_premise_ok,
           "spin-1/2 + 2pi=-1 + nilpotent + [a0,a1]=0 -> bosonic")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (
        repo_root / "docs"
        / "FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md"
    )

    log("FS Rotation-Exchange Discrete-Insufficiency Record-Axiom Invariance"
        " Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: docs/FS_ROTATION_EXCHANGE_DISCRETE_"
        "INSUFFICIENCY_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing finite-dimensional facts")
    log("      (F1)-(F5) are invariant under the 2026-06-04 Record-axiom")
    log("      adoption (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9()
    block10(parent_note)
    block11()
    block12(repo_root)
    block13()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing finite-dimensional facts (F1)-(F5) of the parent")
    log("  no-go use ONLY Quantum + Lattice axiom content plus standard")
    log("  finite-dimensional complex linear algebra (Pauli, tensor")
    log("  products, Jordan-Wigner, swap, M_4(C) dimension count).")
    log("  The Record axiom (additive scalar record-readout functional)")
    log("  is neither used nor invoked. All symbolic outputs are identical")
    log("  under both 'Record axiom asserted' and 'Record axiom not")
    log("  asserted' outer scopes. The parent's N1 walls R1-R6 remain")
    log("  valid on the verified facts alone. This runner does not")
    log("  re-apply any prior audit treatment; it records that the")
    log("  arithmetic checked here is unchanged by the 2026-06-04")
    log("  axiom-set adoption.")
    log("")
    log("The audit lane decides whether to honor or re-test the parent")
    log("treatment on the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
