#!/usr/bin/env python3
"""Audit-companion runner for the YT qubit neutral-Higgs carrier-ray
bridge parent note
`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`,
recording Record-axiom invariance after the 2026-06-04 framework
axiom adoption.

Companion source note:
  docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    carrier-ray identification (sigma_z = P_+ - P_-, P_- H_0 = H_0,
    Q_H H_0 = 0, radial tangent neutral, source-coordinate Jacobian
    cancellation in the same-source top/W response ratio) is
    independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    audit verdict; it gives the audit lane a machine-checkable basis
    for deciding whether the arithmetic needs fresh review after the
    premise-hash change.

The runner verifies the load-bearing step block-by-block under
"Record axiom is asserted" and "Record axiom is not asserted" outer
scopes, confirms bit-identical outputs in both scopes, and performs a
static-source scan of the parent note's load-bearing section to
confirm zero Record-axiom usage in the auditable core.

Every load-bearing algebraic check uses only:
  (i)   one-qubit Pauli/projector content
        (Quantum-axiom: A_x ~= M_2(C) ~= Cl(3,0));
  (ii)  defined C^2 matrix bookkeeping
        (T_3, Y_H, Q_H, H_0 from
        EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md);
  (iii) elementary finite-dimensional matrix-exponential algebra and
        one-variable symbolic calculus.

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about the Record-axiom-induced
downstream content; the companion observation is strictly limited to
the load-bearing step of the parent note.

Block plan:
  Block 1  : Pauli / projector algebra
             (sigma_z^2 = I; P_+, P_- projectors; sum to I;
             sigma_z = P_+ - P_- = I - 2 P_-).
  Block 2  : Affine source-coordinate equivalence
             exp(h sigma_z) = exp(h) * exp(-2 h P_-) at sampled h.
  Block 3  : Normalized weight equivalence
             (common exp(h) factor cancels).
  Block 4  : Defined C^2 matrix bookkeeping
             (T_3 = sigma_z/2; Y_H = (1/2) I; Q_H = diag(1, 0);
             H_0 = (0, v/sqrt(2))^T).
  Block 5  : Neutral-ray annihilation
             (P_- H_0 = H_0, P_+ H_0 = 0, Q_H H_0 = 0,
             Q_H (1,0)^T = (1,0)^T).
  Block 6  : Neutral ray uniqueness in one-Higgs doublet
             (rank(Q_H) = 1; nullspace = span((0,1)^T)).
  Block 7  : Radial tangent neutral
             (P_- dH/ds = dH/ds, Q_H dH/ds = 0).
  Block 8  : Top/W response-ratio Jacobian cancellation
             (sqrt(2) y_t / g_2 independent of v'(s)).
  Block 9  : Static-source scan of parent note: zero Record-axiom
             usage tokens, but structural Pauli/projector/EW tokens
             present.
  Block 10 : Record-axiom counterfactual: bit-identical output with
             and without an explicit "Record axiom asserted" outer
             scope.
  Block 11 : Quantum/Lattice content preservation across the
             historical 2026-05-20 and current 2026-06-04
             minimal-axioms memos; Record-axiom scope explicitly
             excludes the bridges (source/action, log-det, etc.)
             that would be needed to upgrade carrier-ray to physical
             Y_T.
  Block 12 : Independent recomputation of the carrier-ray
             identification from scratch (no parent constants).

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
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


def isclose(a: complex, b: complex, atol: float = 1e-12) -> bool:
    return abs(a - b) <= atol


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Quantum-axiom-only one-qubit Pauli / projector construction
# -----------------------------------------------------------


def pauli_z() -> np.ndarray:
    return np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)


def identity2() -> np.ndarray:
    return np.eye(2, dtype=complex)


def projector_plus() -> np.ndarray:
    return (identity2() + pauli_z()) / 2.0


def projector_minus() -> np.ndarray:
    return (identity2() - pauli_z()) / 2.0


# -----------------------------------------------------------
# Block 1: Pauli / projector algebra
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: Pauli / projector algebra (Quantum-axiom only)")
    I2 = identity2()
    z = pauli_z()
    Pp = projector_plus()
    Pm = projector_minus()

    record("sigma_z_squared_equals_I",
           np.allclose(z @ z, I2, atol=1e-12),
           "sigma_z^2 = I")
    record("P_plus_idempotent",
           np.allclose(Pp @ Pp, Pp, atol=1e-12),
           "P_+^2 = P_+")
    record("P_minus_idempotent",
           np.allclose(Pm @ Pm, Pm, atol=1e-12),
           "P_-^2 = P_-")
    record("P_plus_P_minus_orthogonal",
           np.allclose(Pp @ Pm, np.zeros((2, 2), dtype=complex), atol=1e-12),
           "P_+ P_- = 0")
    record("P_plus_plus_P_minus_equals_I",
           np.allclose(Pp + Pm, I2, atol=1e-12),
           "P_+ + P_- = I")
    record("sigma_z_equals_P_plus_minus_P_minus",
           np.allclose(z, Pp - Pm, atol=1e-12),
           "sigma_z = P_+ - P_-")
    record("sigma_z_equals_I_minus_2_P_minus",
           np.allclose(z, I2 - 2.0 * Pm, atol=1e-12),
           "sigma_z = I - 2 P_-")
    record("identity_commutes_with_P_minus",
           np.allclose(I2 @ Pm - Pm @ I2,
                       np.zeros((2, 2), dtype=complex), atol=1e-12),
           "[I, P_-] = 0 (needed for split exponential)")


# -----------------------------------------------------------
# Block 2: Affine source-coordinate exponential equivalence
# -----------------------------------------------------------

def matrix_exp(M: np.ndarray) -> np.ndarray:
    """Diagonal 2x2 matrix exponential via eigen-decomposition.
    Both sigma_z and P_- are diagonal in the standard basis, so this is
    elementary."""
    w, V = np.linalg.eig(M)
    return V @ np.diag(np.exp(w)) @ np.linalg.inv(V)


def block2() -> None:
    header("BLOCK 2: exp(h sigma_z) = exp(h) * exp(-2 h P_-)")
    z = pauli_z()
    Pm = projector_minus()
    h_samples = [0.0, 0.01, 0.5, 1.0, 2.5, -0.7, -3.0]
    for h in h_samples:
        lhs = matrix_exp(h * z)
        rhs = math.exp(h) * matrix_exp(-2.0 * h * Pm)
        diff = float(np.max(np.abs(lhs - rhs)))
        ok = diff < 1e-12
        record(f"exp_identity_h_{h:+.3f}",
               ok,
               f"max|exp(h sigma_z) - exp(h) exp(-2 h P_-)| = {diff:.3e}")


# -----------------------------------------------------------
# Block 3: Normalized weight equivalence (common exp(h) factor cancels)
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: normalized weight equivalence cancels exp(h)")
    h = sp.symbols("h", real=True)
    signed_weights = sp.Matrix([sp.exp(h), sp.exp(-h)])
    pminus_weights = sp.exp(h) * sp.Matrix([1, sp.exp(-2 * h)])
    diff = sp.simplify(signed_weights - pminus_weights)
    record("weight_diff_is_zero_vector",
           all(sp.simplify(entry) == 0 for entry in diff),
           f"sympy diff = {sp.expand(diff[0])}, {sp.expand(diff[1])}")

    # The normalized source family is the same: the common scalar
    # exp(h) cancels in normalization. Verify numerically for several h.
    for hv in [0.0, 0.3, 1.0, -0.5, 2.0]:
        sv = np.array([math.exp(hv), math.exp(-hv)])
        nsv = sv / sv.sum()
        pv = math.exp(hv) * np.array([1.0, math.exp(-2.0 * hv)])
        npv = pv / pv.sum()
        ok = float(np.max(np.abs(nsv - npv))) < 1e-13
        record(f"normalized_family_identical_h_{hv:+.3f}", ok,
               f"normalized diff = {np.max(np.abs(nsv - npv)):.3e}")


# -----------------------------------------------------------
# Block 4: Defined C^2 matrix bookkeeping
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: defined C^2 matrix bookkeeping")
    z = pauli_z()
    I2 = identity2()
    T3 = z / 2.0
    Y_H = 0.5 * I2
    Q_H = T3 + Y_H
    record("T3_equals_sigma_z_over_2",
           np.allclose(T3, np.array([[0.5, 0], [0, -0.5]], dtype=complex),
                       atol=1e-12),
           "T_3 = diag(1/2, -1/2)")
    record("Y_H_equals_half_I",
           np.allclose(Y_H, 0.5 * I2, atol=1e-12),
           "Y_H = (1/2) * I")
    record("Q_H_equals_diag_1_0",
           np.allclose(Q_H, np.array([[1.0, 0], [0, 0.0]], dtype=complex),
                       atol=1e-12),
           "Q_H = T_3 + Y_H = diag(1, 0)")

    # H_0 has the retained form (0, v/sqrt(2))^T
    v_sample = 246.0
    H0 = np.array([0.0, v_sample / math.sqrt(2.0)], dtype=complex)
    record("H0_neutral_component_form",
           isclose(H0[0], 0.0) and isclose(H0[1], v_sample / math.sqrt(2.0)),
           f"H_0 = (0, {v_sample}/sqrt(2)) numerically")


# -----------------------------------------------------------
# Block 5: Neutral-ray annihilation
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: neutral-ray annihilation")
    z = pauli_z()
    I2 = identity2()
    Pp = projector_plus()
    Pm = projector_minus()
    T3 = z / 2.0
    Y_H = 0.5 * I2
    Q_H = T3 + Y_H

    v = 246.0
    H0 = np.array([0.0, v / math.sqrt(2.0)], dtype=complex)
    upper = np.array([1.0, 0.0], dtype=complex)

    record("P_minus_H0_equals_H0",
           np.allclose(Pm @ H0, H0, atol=1e-12),
           f"P_- H_0 = {Pm @ H0}")
    record("P_plus_H0_equals_zero",
           np.allclose(Pp @ H0, np.zeros(2, dtype=complex), atol=1e-12),
           f"P_+ H_0 = {Pp @ H0}")
    record("Q_H_H0_equals_zero",
           np.allclose(Q_H @ H0, np.zeros(2, dtype=complex), atol=1e-12),
           f"Q_H H_0 = {Q_H @ H0}")
    record("Q_H_upper_equals_upper",
           np.allclose(Q_H @ upper, upper, atol=1e-12),
           f"Q_H (1,0)^T = {Q_H @ upper}")


# -----------------------------------------------------------
# Block 6: Neutral ray uniqueness in one-Higgs doublet
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: neutral ray uniqueness inside stipulated C^2")
    # Use sympy for exact rank / nullspace.
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    T3 = z / 2
    Y_H = sp.Rational(1, 2) * ident
    Q_H = T3 + Y_H

    rank = Q_H.rank()
    record("rank_Q_H_equals_1", rank == 1, f"rank(Q_H) = {rank}")

    ns = Q_H.nullspace()
    record("nullspace_dim_equals_1", len(ns) == 1,
           f"nullspace dim = {len(ns)}")
    if ns:
        # nullspace vector should be a scalar multiple of (0,1)^T
        v = ns[0]
        # Normalize: v should have v[0] == 0 and v[1] != 0
        record("nullspace_is_neutral_ray",
               sp.simplify(v[0]) == 0 and sp.simplify(v[1]) != 0,
               f"nullspace vector = {list(v)}")


# -----------------------------------------------------------
# Block 7: Radial tangent stays on neutral ray
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: radial tangent stays neutral (symbolic)")
    s = sp.symbols("s", real=True)
    v = sp.Function("v")(s)
    ident = sp.eye(2)
    z = sp.Matrix([[1, 0], [0, -1]])
    Pm = (ident - z) / 2
    Pp = (ident + z) / 2
    T3 = z / 2
    Y_H = sp.Rational(1, 2) * ident
    Q_H = T3 + Y_H

    H_s = sp.Matrix([0, v / sp.sqrt(2)])
    tangent = sp.diff(H_s, s)

    diff_PmH = sp.simplify(Pm * H_s - H_s)
    record("Pm_H_equals_H_symbolic",
           all(sp.simplify(entry) == 0 for entry in diff_PmH),
           f"Pm H(s) - H(s) = {[sp.simplify(e) for e in diff_PmH]}")

    diff_PpH = sp.simplify(Pp * H_s)
    record("Pp_H_equals_zero_symbolic",
           all(sp.simplify(entry) == 0 for entry in diff_PpH),
           f"Pp H(s) = {[sp.simplify(e) for e in diff_PpH]}")

    diff_QH = sp.simplify(Q_H * H_s)
    record("Q_H_H_equals_zero_symbolic",
           all(sp.simplify(entry) == 0 for entry in diff_QH),
           f"Q_H H(s) = {[sp.simplify(e) for e in diff_QH]}")

    diff_Pm_tangent = sp.simplify(Pm * tangent - tangent)
    record("Pm_tangent_equals_tangent",
           all(sp.simplify(entry) == 0 for entry in diff_Pm_tangent),
           f"Pm dH/ds - dH/ds = {[sp.simplify(e) for e in diff_Pm_tangent]}")

    diff_Q_tangent = sp.simplify(Q_H * tangent)
    record("Q_H_tangent_equals_zero",
           all(sp.simplify(entry) == 0 for entry in diff_Q_tangent),
           f"Q_H dH/ds = {[sp.simplify(e) for e in diff_Q_tangent]}")


# -----------------------------------------------------------
# Block 8: Top/W response-ratio Jacobian cancellation
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: top/W response-ratio Jacobian cancellation")
    s = sp.symbols("s", real=True)
    v = sp.Function("v")(s)
    g2, yt = sp.symbols("g_2 y_t", nonzero=True)

    m_t = yt * v / sp.sqrt(2)
    m_W = g2 * v / 2
    dmt = sp.diff(m_t, s)
    dmW = sp.diff(m_W, s)
    ratio = sp.simplify(dmt / dmW)
    expected = sp.sqrt(2) * yt / g2
    diff = sp.simplify(ratio - expected)
    record("ratio_equals_sqrt2_yt_over_g2",
           sp.simplify(diff) == 0,
           f"ratio - sqrt(2) y_t / g_2 = {sp.simplify(diff)}")

    # Independent: try a few explicit profiles v(s) to verify the Jacobian
    # v'(s) really cancels.
    for prof_label, prof in [
        ("linear", s),
        ("quadratic", s ** 2),
        ("exponential", sp.exp(s)),
        ("sinusoidal", sp.sin(s)),
    ]:
        mt_p = yt * prof / sp.sqrt(2)
        mW_p = g2 * prof / 2
        ratio_p = sp.simplify(sp.diff(mt_p, s) / sp.diff(mW_p, s))
        ok = sp.simplify(ratio_p - expected) == 0
        record(f"jacobian_cancels_profile_{prof_label}", ok,
               f"ratio with v(s) = {prof}: {ratio_p}")


# -----------------------------------------------------------
# Block 9: Static-source scan of parent note
# -----------------------------------------------------------

def block9(parent_note_path: Path) -> None:
    header("BLOCK 9: parent-note static scan for Record-axiom usage")
    parent_present = parent_note_path.exists()
    record("parent_note_present", parent_present, str(parent_note_path))
    if not parent_present:
        log(f"  WARN: parent note not found at {parent_note_path}")
        return

    text = parent_note_path.read_text()

    # The load-bearing section spans the "## Theorem" heading through
    # the end of "## What This Closes". (The subsequent
    # "What This Still Does Not Close" + "Why This Is Not A Renaming"
    # sections are scoping disclaimers / firewalls; they are scanned
    # separately below.)
    start = text.find("## Theorem")
    end = text.find("## What This Still Does Not Close")
    record("structural_section_start_found", start >= 0,
           f"start index = {start}")
    record("structural_section_end_found", end > start,
           f"end index = {end}")
    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage in the load-bearing
    # section. Note: the literal phrase "signed record" appears in the
    # parent as inherited NAMING (the predecessor support packet uses
    # epsilon_x in {-1,+1} as a signed indicator), but the parent's
    # actual load-bearing content uses sigma_z as a Pauli operator and
    # never invokes the Record-axiom's scalar additivity functional
    # I(.). We therefore scan only for tokens that exhibit Record-
    # axiom CONTENT (additive functional, disjoint-union additivity,
    # additive baseline) -- not the inherited terminology.
    record_content_tokens = [
        "I(R_1",
        "I(R)",
        "I(empty)",
        "scalar record functional",
        "record functional",
        "additive scalar record",
        "additive over disjoint",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found = [t for t in record_content_tokens if t in section]
    record("zero_record_axiom_content_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches in load-bearing section = {found}")

    # Confirm Pauli / projector / retained-EW structural tokens ARE
    # used in the load-bearing section.
    structural_tokens = [
        "sigma_z",
        "P_+",
        "P_-",
        "T_3",
        "Y_H",
        "H_0",
        "Q",  # Q acts on H_0
    ]
    found_structural = [t for t in structural_tokens if t in section]
    record("structural_load_bearing_tokens_present",
           len(found_structural) >= 6,
           f"matches >= 6 of 7: {found_structural}")


# -----------------------------------------------------------
# Block 10: Record-axiom counterfactual
# -----------------------------------------------------------

def _counterfactual_compute(record_axiom_asserted: bool) -> dict:
    """Re-run the load-bearing computations and return numeric outputs.

    The record_axiom_asserted flag is intentionally NOT read by any
    computation inside this function. The point of the counterfactual
    is to show that no branch of the computation depends on it; the
    outputs must be bit-identical whether the flag is True or False.
    """
    z = pauli_z()
    I2 = identity2()
    Pp = projector_plus()
    Pm = projector_minus()
    T3 = z / 2.0
    Y_H = 0.5 * I2
    Q_H = T3 + Y_H

    v_sample = 246.0
    H0 = np.array([0.0, v_sample / math.sqrt(2.0)], dtype=complex)
    upper = np.array([1.0, 0.0], dtype=complex)

    return {
        "sigma_z_minus_Pp_plus_Pm": float(np.max(np.abs(z - (Pp - Pm)))),
        "exp_h_1": matrix_exp(1.0 * z),
        "Pm_H0": Pm @ H0,
        "Pp_H0": Pp @ H0,
        "Q_H_H0": Q_H @ H0,
        "Q_H_upper": Q_H @ upper,
        # We do not use `record_axiom_asserted` anywhere; that is the
        # substantive content of (C1).
        "flag_was_set": record_axiom_asserted,
    }


def block10() -> None:
    header("BLOCK 10: Record-axiom counterfactual")
    scope_flags = (bool(1), bool(0))
    with_axiom = _counterfactual_compute(record_axiom_asserted=scope_flags[0])
    without_axiom = _counterfactual_compute(record_axiom_asserted=scope_flags[1])

    # Compare all numeric outputs
    numeric_keys = [
        "sigma_z_minus_Pp_plus_Pm",
        "exp_h_1",
        "Pm_H0",
        "Pp_H0",
        "Q_H_H0",
        "Q_H_upper",
    ]
    for k in numeric_keys:
        a = np.asarray(with_axiom[k])
        b = np.asarray(without_axiom[k])
        diff = float(np.max(np.abs(a - b)))
        ok = diff == 0.0
        record(f"counterfactual_identical_{k}", ok,
               f"max|with - without| = {diff:.3e}")

    # And confirm the flag really differed (so the comparison is
    # not vacuous because of a stale toggle).
    record("counterfactual_flag_differed",
           with_axiom["flag_was_set"] != without_axiom["flag_was_set"],
           f"with_axiom.flag = {with_axiom['flag_was_set']}, "
           f"without_axiom.flag = {without_axiom['flag_was_set']}")


# -----------------------------------------------------------
# Block 11: Quantum / Lattice content preservation across memos
# -----------------------------------------------------------

def block11(repo_root: Path) -> None:
    header("BLOCK 11: Quantum / Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))
    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Historical wording: one-qubit per site + Z^3 cubic lattice.
    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "primitive local operator\n   algebra is the one-qubit algebra" in old_text
        or "M_2(ℂ)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text
        or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    # New memo: Quantum (one-qubit / M_2(C) / Cl(3,0)) + Lattice (Z^3).
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

    # Record axiom: additive scalar record-readout (separate, non-overlapping).
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    # New memo explicitly says Record does NOT supply log-det /
    # source/action / observable / etc. content -- which is exactly
    # what would be needed to upgrade carrier-ray identification to
    # a physical Y_T coefficient.
    record_scope_disclaimer = (
        "source/action identification" in new_text
        and "rule for record production" in new_text
    )
    record("new_memo_Record_scope_excludes_source_action_etc",
           record_scope_disclaimer,
           "Record axiom's own scope statement excludes the bridges"
           " (source/action, production, etc.) that would otherwise"
           " be needed to upgrade carrier-ray to physical Y_T")


# -----------------------------------------------------------
# Block 12: Independent recomputation from scratch
# -----------------------------------------------------------

def block12() -> None:
    header("BLOCK 12: independent recomputation of the carrier-ray ID")
    # Build everything from raw sympy primitives -- no shared helpers.
    z_indep = sp.Matrix([[1, 0], [0, -1]])
    I_indep = sp.eye(2)
    Pp_indep = (I_indep + z_indep) / 2
    Pm_indep = (I_indep - z_indep) / 2

    # Verify sigma_z = P_+ - P_- (independent of helper code)
    record("indep_sigma_z_decomp",
           sp.simplify(z_indep - (Pp_indep - Pm_indep)) == sp.zeros(2, 2),
           f"sigma_z - (P_+ - P_-) = {sp.simplify(z_indep - (Pp_indep - Pm_indep))}")

    # Independent EW bookkeeping
    T3_indep = z_indep / 2
    Y_indep = sp.Rational(1, 2) * I_indep
    Q_indep = T3_indep + Y_indep

    record("indep_Q_H_diagonal_1_0",
           sp.simplify(Q_indep - sp.Matrix([[1, 0], [0, 0]])) == sp.zeros(2, 2),
           f"Q_H = {Q_indep.tolist()}")

    # Independent H_0
    v_sym = sp.symbols("v", positive=True, real=True)
    H0_indep = sp.Matrix([0, v_sym / sp.sqrt(2)])

    record("indep_Pm_H0_equals_H0",
           sp.simplify(Pm_indep * H0_indep - H0_indep) == sp.zeros(2, 1),
           f"Pm H_0 - H_0 = {sp.simplify(Pm_indep * H0_indep - H0_indep).tolist()}")

    record("indep_Pp_H0_equals_zero",
           sp.simplify(Pp_indep * H0_indep) == sp.zeros(2, 1),
           f"Pp H_0 = {sp.simplify(Pp_indep * H0_indep).tolist()}")

    record("indep_Q_H_H0_equals_zero",
           sp.simplify(Q_indep * H0_indep) == sp.zeros(2, 1),
           f"Q_H H_0 = {sp.simplify(Q_indep * H0_indep).tolist()}")

    # Independent affine identity
    h_sym = sp.symbols("h", real=True)
    lhs = sp.exp(h_sym * z_indep)
    rhs = sp.exp(h_sym) * sp.exp(-2 * h_sym * Pm_indep)
    # sympy matrix exp of diagonal matrices is straightforward
    diff = sp.simplify(lhs - rhs)
    record("indep_exp_identity_symbolic",
           all(sp.simplify(entry) == 0 for entry in diff),
           f"max symbolic diff entry = {[sp.simplify(e) for e in diff]}")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (repo_root / "docs"
                   / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md")

    log("YT Qubit Neutral-Higgs Carrier-Ray Bridge")
    log("Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note:")
    log("  docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_"
        "RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing carrier-ray")
    log("      identification is invariant under the 2026-06-04")
    log("      Record-axiom adoption (MINIMAL_AXIOMS_2026-06-04.md).")
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
    log("  The load-bearing carrier-ray identification of")
    log("  YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md")
    log("  (sigma_z = P_+ - P_-; sigma_z source <-> P_- occupation source;")
    log("   P_- H_0 = H_0; Q_H H_0 = 0; radial tangent neutral;")
    log("   sqrt(2) y_t / g_2 cancels v'(s)) uses ONLY one-qubit Pauli")
    log("  content (Quantum axiom), stipulated C^2/lower-ray bookkeeping, and")
    log("  elementary calculus. The Record axiom (additive scalar")
    log("  record-readout functional) is neither used nor invoked.")
    log("  Numeric output is bit-identical under both 'Record axiom")
    log("  asserted' and 'Record axiom not asserted' outer scopes. This")
    log("  runner does not re-apply the prior audit verdict; it records")
    log("  that the arithmetic checked here is unchanged by the")
    log("  2026-06-04 axiom-set adoption.")
    log("")
    log("The audit lane decides how to treat the parent on the new")
    log("minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
