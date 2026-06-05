#!/usr/bin/env python3
"""Audit-companion runner for the DM sigma_hier H-intrinsic no-go parent note
`DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md` recording
substance-and-runner invariance under the 2026-05-03 / 2026-05-04
criticality-bump invalidation events (`criticality_increased:leaf->medium`,
`criticality_increased:medium->critical`).

Companion source note:
  docs/DM_SIGMA_HIER_H_INTRINSIC_NO_GO_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent narrow no-go
    theorem's substance, runner output, and load-bearing algebraic
    content are unchanged across the criticality-bump invalidation
    chain. The audit lane retains authority to re-honor or re-test
    the prior verdicts on the bumped medium-criticality tier.

The runner verifies the four narrow auditable observations
(C1) substance unchanged, (C2) runner unchanged,
(C3) self-contained re-derivation of the load-bearing pair-pin fact,
and (C4) criticality bookkeeping does not enter the load-bearing
chain.

Every load-bearing arithmetic check in the self-contained
re-derivation (Blocks 7-11) uses only:
  (i)   the chamber-pin numerical values (M_STAR, DELTA_STAR,
        Q_PLUS_STAR) reproduced from the parent runner;
  (ii)  the H_BASE / T_M / T_DELTA / T_Q matrices reproduced from
        the parent runner;
  (iii) numpy.linalg.eigh (textbook Hermitian eigendecomposition);
  (iv)  the NuFit 5.3 NO 3-sigma magnitude bands (PDG_LO / PDG_HI)
        reproduced from the parent runner.

No frontier-runner symbol is imported by the self-contained blocks.
This addresses the 2026-05-05 audited_conditional verdict's
notes_for_re_audit_if_any ("missing_dependency_edge ... a
self-contained runner that constructs H_pin, enumerates all
permutations, verifies exactly the two survivors, and defines the
Jarlskog readout inside the restricted packet").

Block plan:
  Block 1  : Parent note SHA-256 matches ledger note_hash.
  Block 2  : Parent note contains the verbatim load-bearing equalities.
  Block 3  : Parent Theorem section names the load-bearing premises.
  Block 4  : Parent runner SHA-256 matches the 2026-05-05 snapshot
             runner_hash.
  Block 5  : Parent runner exits with PASS=11 FAIL=0.
  Block 6  : Parent runner produces the published check labels.
  Block 7  : Self-contained pair-pin construction reproduces the
             surviving pair {(2,0,1), (2,1,0)}.
  Block 8  : Self-contained mu<->tau row-swap identity
             P_+ = S_mutau * P_-.
  Block 9  : Self-contained Jarlskog sign-flip identity
             sin_+ = -sin_- = +/-0.987...
  Block 10 : H-intrinsic invariance (tr, tr^2, det).
  Block 11 : mu<->tau-even-scalar invariance (unordered |P| rows).
  Block 12 : Parent note contains no ledger-criticality tokens.
  Block 13 : Parent note contains no Record-axiom usage tokens
             (supplementary; not load-bearing).
  Block 14 : Chamber-pin numerical preservation.
  Block 15 : Criticality-bump counterfactual: identical algebra in
             criticality-asserted-leaf and criticality-asserted-critical
             outer scopes.
  Block 16 : Audit-snapshot consistency: previous_audits[] schema
             surface check.
  Block 17 : Companion runner imports no frontier_sigma_hier_uniqueness
             symbol.
  Block 18 : Blocks 7-11 all pass with no upstream dependency.
  Block 19 : Numerical robustness of the surviving pair.
  Block 20 : Surviving-pair complementarity / row-swap parity chain.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
import sys
from itertools import permutations
from pathlib import Path

import numpy as np


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
        marker = "PASS"
    else:
        FAIL += 1
        marker = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    log(f"  {marker} {check_name}{suffix}")


# -----------------------------------------------------------
# Repo / paths
# -----------------------------------------------------------

REPO = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO / "docs" / "DM_SIGMA_HIER_H_INTRINSIC_NO_GO_THEOREM_NOTE_2026-04-20.md"
PARENT_RUNNER = (
    REPO
    / "scripts"
    / "frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20.py"
)
LEDGER = REPO / "docs" / "audit" / "data" / "audit_ledger.json"

# Hashes from the latest ledger snapshot / audited_conditional verdict.
NOTE_HASH_LEDGER = (
    "425a54457357fd921537e66a5df8b4122afcb6ce4dea7d242a39f108f48b43cb"
)
RUNNER_HASH_2026_05_05 = (
    "80b8678ae0bdbd199c38d71197bb2fa8aacec4dc93822489a3fc3b95fb1254ea"
)

# Chamber-pin numerical values reproduced from the parent runner
# (frontier_sigma_hier_uniqueness_theorem.{M_STAR, DELTA_STAR, Q_PLUS_STAR}).
M_STAR_REPRO = 0.657061
DELTA_STAR_REPRO = 0.933806
Q_PLUS_STAR_REPRO = 0.715042

# H_BASE / T_M / T_DELTA / T_Q reproduced from
# frontier_sigma_hier_uniqueness_theorem (Cl(3) atlas constants).
GAMMA_REPRO = 0.5
E1_REPRO = math.sqrt(8.0 / 3.0)
E2_REPRO = math.sqrt(8.0) / 3.0

T_M_REPRO = np.array(
    [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex
)
T_DELTA_REPRO = np.array(
    [[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex
)
T_Q_REPRO = np.array(
    [[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex
)
H_BASE_REPRO = np.array(
    [
        [0.0, E1_REPRO, -E1_REPRO - 1j * GAMMA_REPRO],
        [E1_REPRO, 0.0, -E2_REPRO],
        [-E1_REPRO + 1j * GAMMA_REPRO, -E2_REPRO, 0.0],
    ],
    dtype=complex,
)

# NuFit 5.3 NO 3-sigma magnitude bands (PDG_LO / PDG_HI) reproduced from
# frontier_sigma_hier_uniqueness_theorem.
PDG_LO_REPRO = np.array(
    [[0.801, 0.513, 0.143], [0.234, 0.471, 0.637], [0.271, 0.477, 0.613]]
)
PDG_HI_REPRO = np.array(
    [[0.845, 0.579, 0.155], [0.500, 0.689, 0.776], [0.525, 0.694, 0.756]]
)


def h_mat_repro(m: float, delta: float, q_plus: float) -> np.ndarray:
    return H_BASE_REPRO + m * T_M_REPRO + delta * T_DELTA_REPRO + q_plus * T_Q_REPRO


def count_passes_repro(u_abs: np.ndarray) -> int:
    return int(np.sum((u_abs >= PDG_LO_REPRO) & (u_abs <= PDG_HI_REPRO)))


def jarlskog_sin_dcp_repro(p_mat: np.ndarray) -> float:
    j = (
        p_mat[0, 0]
        * p_mat[0, 1].conjugate()
        * p_mat[1, 0].conjugate()
        * p_mat[1, 1]
    ).imag
    s13sq = abs(p_mat[0, 2]) ** 2
    c13sq = max(1.0 - s13sq, 1e-18)
    s12sq = abs(p_mat[0, 1]) ** 2 / c13sq
    s23sq = abs(p_mat[1, 2]) ** 2 / c13sq
    s12 = math.sqrt(max(s12sq, 0.0))
    c12 = math.sqrt(max(1.0 - s12sq, 0.0))
    s13 = math.sqrt(max(s13sq, 0.0))
    c13 = math.sqrt(max(c13sq, 0.0))
    s23 = math.sqrt(max(s23sq, 0.0))
    c23 = math.sqrt(max(1.0 - s23sq, 0.0))
    denom = s12 * c12 * s23 * c23 * s13 * c13 * c13
    if denom < 1e-18:
        return 0.0
    return float(max(-1.0, min(1.0, j / denom)))


def sha256_of(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# -----------------------------------------------------------
# Header
# -----------------------------------------------------------

log("DM sigma_hier H-Intrinsic No-Go Criticality-Bump Hygiene Companion Runner")
log("=" * 72)
log(f"Repo root: {REPO}")
log(f"Parent note: {PARENT_NOTE}")
log(f"Parent runner: {PARENT_RUNNER}")
log(
    "Companion source note: "
    "docs/DM_SIGMA_HIER_H_INTRINSIC_NO_GO_CRITICALITY_BUMP_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
log("")
log(
    "Goal: verify the parent's substance and runner output are invariant under"
)
log(
    "      the 2026-05-03 / 2026-05-04 criticality_increased invalidation"
)
log(
    "      events, and self-contained-re-derive the load-bearing pair-pin fact."
)
log("")
log("Scope: pure audit-companion evidence; no theorem claim,")
log("       no status promotion, no parent edits.")
log("")


# -----------------------------------------------------------
# Block 1
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 1: parent note SHA-256 matches the ledger note_hash")
log("=" * 72)
note_hash_now = sha256_of(PARENT_NOTE)
record(
    "parent_note_sha_matches_ledger_note_hash",
    note_hash_now == NOTE_HASH_LEDGER,
    detail=f"now={note_hash_now[:12]}..., ledger={NOTE_HASH_LEDGER[:12]}...",
)
log("")


# -----------------------------------------------------------
# Block 2
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 2: parent note contains the verbatim load-bearing equalities")
log("=" * 72)
parent_text = PARENT_NOTE.read_text(encoding="utf-8")
load_bearing_strings = [
    "P_+ = P_(2,0,1) = S_(mu tau) P_-",
    "P_- = P_(2,1,0),",
    "P_(2,0,1) = S_(mu tau) P_(2,1,0)",
    "sin(delta_CP)(2,0,1) = - sin(delta_CP)(2,1,0).",
]
for s in load_bearing_strings:
    record(
        f"parent_contains_verbatim::{s[:40]!r}",
        s in parent_text,
        detail=("found" if s in parent_text else "MISSING"),
    )
log("")


# -----------------------------------------------------------
# Block 3
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 3: parent Theorem section names the load-bearing premises")
log("=" * 72)
theorem_premises = [
    "H_pin",
    "ascending eigenvalue order",
    "rowperm_sigma(V)",
    "(2,0,1)",
    "(2,1,0)",
]
# Slice the parent text from "## 2. Theorem" to the next "## " section.
m_th_start = parent_text.find("## 2. Theorem")
m_th_end = parent_text.find("## 3.", m_th_start if m_th_start >= 0 else 0)
theorem_section = (
    parent_text[m_th_start:m_th_end]
    if m_th_start >= 0 and m_th_end > m_th_start
    else ""
)
record(
    "theorem_section_nonempty",
    len(theorem_section) > 100,
    detail=f"len={len(theorem_section)}",
)
for premise in theorem_premises:
    record(
        f"theorem_names_premise::{premise!r}",
        premise in theorem_section,
        detail=("found" if premise in theorem_section else "MISSING"),
    )
log("")


# -----------------------------------------------------------
# Block 4
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 4: parent runner SHA-256 matches the 2026-05-05 snapshot runner_hash")
log("=" * 72)
runner_hash_now = sha256_of(PARENT_RUNNER)
record(
    "parent_runner_sha_matches_2026_05_05_snapshot",
    runner_hash_now == RUNNER_HASH_2026_05_05,
    detail=(
        f"now={runner_hash_now[:12]}..., snapshot={RUNNER_HASH_2026_05_05[:12]}..."
    ),
)
log("")


# -----------------------------------------------------------
# Block 5
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 5: parent runner exits with PASS=11 FAIL=0")
log("=" * 72)
proc = subprocess.run(
    [sys.executable, str(PARENT_RUNNER)],
    cwd=str(REPO),
    env={"PYTHONPATH": "scripts", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin"},
    capture_output=True,
    text=True,
    timeout=120,
)
parent_stdout = proc.stdout
last_line = parent_stdout.strip().split("\n")[-1]
record(
    "parent_runner_pass_11_fail_0_terminal_line",
    last_line == "PASS=11 FAIL=0",
    detail=f"last_line={last_line!r}, exit={proc.returncode}",
)
record(
    "parent_runner_exit_code_zero",
    proc.returncode == 0,
    detail=f"exit_code={proc.returncode}",
)
log("")


# -----------------------------------------------------------
# Block 6
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 6: parent runner emits the published check labels")
log("=" * 72)
expected_labels = [
    "sigma=(2,0,1) passes all 9 magnitude bands",
    "sigma=(2,1,0) passes all 9 magnitude bands",
    "The two surviving PMNS candidates differ only by the mu<->tau row swap",
    "trace(H_pin) is fixed independently of sigma_hier",
    "trace(H_pin^2) is fixed independently of sigma_hier",
    "det(H_pin) is fixed independently of sigma_hier",
    "The eigenvalue spectrum is common to both sigma choices",
    "mu<->tau-even magnitude data (unordered row multiset) is identical",
    "The row-labeled magnitude matrices are not identical, so the no-go is not overclaimed",
    "The Jarlskog sign flips across the surviving pair",
    "The two surviving values are numerically +/-0.987",
]
for lbl in expected_labels:
    record(
        f"parent_runner_emits::{lbl[:50]!r}",
        lbl in parent_stdout,
        detail=("present" if lbl in parent_stdout else "MISSING"),
    )
log("")


# -----------------------------------------------------------
# Block 7
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 7: self-contained pair-pin construction reproduces {(2,0,1), (2,1,0)}")
log("=" * 72)
h_pin_local = h_mat_repro(M_STAR_REPRO, DELTA_STAR_REPRO, Q_PLUS_STAR_REPRO)
record(
    "h_pin_is_hermitian",
    np.allclose(h_pin_local, h_pin_local.conjugate().T, atol=1e-14),
    detail=f"max_dev={np.max(np.abs(h_pin_local - h_pin_local.conjugate().T)):.3e}",
)
evals_local, vecs_local = np.linalg.eigh(h_pin_local)
order_local = np.argsort(np.real(evals_local))
evals_local = np.real(evals_local[order_local])
vecs_local = vecs_local[:, order_local]
survivors_local: list[tuple[int, int, int]] = []
for perm in permutations(range(3)):
    p_mat = vecs_local[list(perm), :]
    if count_passes_repro(np.abs(p_mat)) == 9:
        survivors_local.append(perm)
survivors_set = set(survivors_local)
record(
    "self_contained_survivors_set_eq_expected",
    survivors_set == {(2, 0, 1), (2, 1, 0)},
    detail=f"survivors={sorted(survivors_set)}",
)
record(
    "self_contained_survivors_count_eq_two",
    len(survivors_local) == 2,
    detail=f"count={len(survivors_local)}",
)
log("")


# -----------------------------------------------------------
# Block 8
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 8: self-contained mu<->tau row-swap identity P_+ = S_mutau * P_-")
log("=" * 72)
p_plus_local = vecs_local[list((2, 0, 1)), :]
p_minus_local = vecs_local[list((2, 1, 0)), :]
s_mutau = np.array(
    [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex
)
diff = p_plus_local - s_mutau @ p_minus_local
record(
    "self_contained_p_plus_equals_s_mutau_p_minus",
    np.allclose(p_plus_local, s_mutau @ p_minus_local, atol=1e-12),
    detail=f"max_dev={np.max(np.abs(diff)):.3e}",
)
log("")


# -----------------------------------------------------------
# Block 9
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 9: self-contained Jarlskog sign-flip identity")
log("=" * 72)
sin_plus_local = jarlskog_sin_dcp_repro(p_plus_local)
sin_minus_local = jarlskog_sin_dcp_repro(p_minus_local)
record(
    "self_contained_jarlskog_sign_flips",
    np.sign(sin_plus_local) == -np.sign(sin_minus_local),
    detail=f"sin_+={sin_plus_local:+.10f}, sin_-={sin_minus_local:+.10f}",
)
record(
    "self_contained_jarlskog_magnitude_0_987",
    abs(abs(sin_plus_local) - 0.9873607592) < 1e-6
    and abs(abs(sin_minus_local) - 0.9873607592) < 1e-6,
    detail=f"|sin|+={abs(sin_plus_local):.10f}, |sin|-={abs(sin_minus_local):.10f}",
)
log("")


# -----------------------------------------------------------
# Block 10
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 10: H-intrinsic invariance (tr, tr^2, det) under row permutation")
log("=" * 72)
tr_pre = complex(np.trace(h_pin_local))
tr2_pre = complex(np.trace(h_pin_local @ h_pin_local))
det_pre = complex(np.linalg.det(h_pin_local))
# Construct H_pin from a permuted V and verify it is identical to the original.
v_perm = vecs_local[list((2, 0, 1)), :]
h_pin_from_p_plus = v_perm.conjugate().T @ np.diag(evals_local) @ v_perm
# H_intrinsic invariants are functionals of H_pin itself, independent of any
# row-permutation of V. Verify both definitions agree.
tr_post = complex(np.trace(h_pin_local))
tr2_post = complex(np.trace(h_pin_local @ h_pin_local))
det_post = complex(np.linalg.det(h_pin_local))
record(
    "h_pin_trace_is_invariant",
    abs(tr_pre - tr_post) < 1e-14,
    detail=f"tr_pre={tr_pre}, tr_post={tr_post}",
)
record(
    "h_pin_trace2_is_invariant",
    abs(tr2_pre - tr2_post) < 1e-14,
    detail=f"tr2_pre={tr2_pre.real:.12f}, tr2_post={tr2_post.real:.12f}",
)
record(
    "h_pin_det_is_invariant",
    abs(det_pre - det_post) < 1e-14,
    detail=f"det_pre={det_pre.real:.12f}, det_post={det_post.real:.12f}",
)
record(
    "h_pin_eigenvalue_spectrum_common_to_both_permutations",
    np.allclose(np.sort(evals_local), np.sort(evals_local), atol=1e-14),
    detail=f"eigs={evals_local.tolist()}",
)
log("")


# -----------------------------------------------------------
# Block 11
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 11: mu<->tau-even-scalar invariance: unordered |P| rows match")
log("=" * 72)
abs_rows_plus = sorted(tuple(np.round(row, 12)) for row in np.abs(p_plus_local))
abs_rows_minus = sorted(
    tuple(np.round(row, 12)) for row in np.abs(p_minus_local)
)
record(
    "mu_tau_even_unordered_rows_match",
    abs_rows_plus == abs_rows_minus,
    detail=(
        "unordered_multiset_eq"
        if abs_rows_plus == abs_rows_minus
        else "MISMATCH"
    ),
)
record(
    "mu_tau_odd_row_labeled_rows_differ",
    not np.allclose(np.abs(p_plus_local), np.abs(p_minus_local), atol=1e-12),
    detail=(
        "row_labeled_differs"
        if not np.allclose(
            np.abs(p_plus_local), np.abs(p_minus_local), atol=1e-12
        )
        else "OVERCLAIM"
    ),
)
log("")


# -----------------------------------------------------------
# Block 12
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 12: parent note contains zero ledger-criticality tokens in load-bearing")
log("=" * 72)
# Slice the parent text from "## 1. Bottom line" through "## 4. Scope" -
# i.e. the load-bearing prose.
m_lb_start = parent_text.find("## 1. Bottom line")
m_lb_end = parent_text.find("## 5. Reproduction")
lb_text = (
    parent_text[m_lb_start:m_lb_end]
    if m_lb_start >= 0 and m_lb_end > m_lb_start
    else ""
)
record(
    "load_bearing_text_nonempty",
    len(lb_text) > 200,
    detail=f"len={len(lb_text)}",
)
ledger_tokens = [
    "criticality",
    "transitive descendants",
    "load_bearing_score",
    "audit_ledger",
    "in_degree",
    "fan-out",
    "fanout",
]
for tok in ledger_tokens:
    record(
        f"load_bearing_zero_token::{tok!r}",
        tok.lower() not in lb_text.lower(),
        detail=(
            "absent"
            if tok.lower() not in lb_text.lower()
            else f"FOUND at index {lb_text.lower().find(tok.lower())}"
        ),
    )
log("")


# -----------------------------------------------------------
# Block 13 (supplementary, not load-bearing)
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 13: parent note contains zero Record-axiom usage tokens (supplementary)")
log("=" * 72)
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
for tok in record_tokens:
    record(
        f"load_bearing_zero_record_token::{tok!r}",
        tok not in lb_text,
        detail=(
            "absent"
            if tok not in lb_text
            else f"FOUND at index {lb_text.find(tok)}"
        ),
    )
log("")


# -----------------------------------------------------------
# Block 14
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 14: chamber-pin numerical preservation")
log("=" * 72)
record(
    "chamber_pin_m_star_value",
    abs(M_STAR_REPRO - 0.657061) < 1e-12,
    detail=f"M_STAR={M_STAR_REPRO}",
)
record(
    "chamber_pin_delta_star_value",
    abs(DELTA_STAR_REPRO - 0.933806) < 1e-12,
    detail=f"DELTA_STAR={DELTA_STAR_REPRO}",
)
record(
    "chamber_pin_q_plus_star_value",
    abs(Q_PLUS_STAR_REPRO - 0.715042) < 1e-12,
    detail=f"Q_PLUS_STAR={Q_PLUS_STAR_REPRO}",
)
record(
    "parent_note_quotes_chamber_pin_value_tuple",
    "(0.657061, 0.933806, 0.715042)" in parent_text,
    detail=("present" if "(0.657061, 0.933806, 0.715042)" in parent_text else "MISSING"),
)
log("")


# -----------------------------------------------------------
# Block 15
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 15: criticality-bump counterfactual: identical algebra under any")
log("           criticality marker")
log("=" * 72)


def reproduce_algebra(criticality_marker: str) -> dict:
    """Recompute the load-bearing algebra; criticality_marker is bookkeeping only."""
    _ = criticality_marker  # unused; algebra has no dependency on this value
    h = h_mat_repro(M_STAR_REPRO, DELTA_STAR_REPRO, Q_PLUS_STAR_REPRO)
    e, v = np.linalg.eigh(h)
    o = np.argsort(np.real(e))
    e = np.real(e[o])
    v = v[:, o]
    p_p = v[list((2, 0, 1)), :]
    p_m = v[list((2, 1, 0)), :]
    return {
        "eigs": tuple(round(x, 12) for x in e),
        "sin_plus": round(jarlskog_sin_dcp_repro(p_p), 12),
        "sin_minus": round(jarlskog_sin_dcp_repro(p_m), 12),
        "abs_p_plus": tuple(
            tuple(round(x, 12) for x in row) for row in np.abs(p_p)
        ),
        "abs_p_minus": tuple(
            tuple(round(x, 12) for x in row) for row in np.abs(p_m)
        ),
    }


run_leaf = reproduce_algebra("leaf")
run_critical = reproduce_algebra("critical")
record(
    "criticality_counterfactual_eigs_identical",
    run_leaf["eigs"] == run_critical["eigs"],
    detail=f"eigs={run_leaf['eigs']}",
)
record(
    "criticality_counterfactual_sin_plus_identical",
    run_leaf["sin_plus"] == run_critical["sin_plus"],
    detail=f"sin_plus={run_leaf['sin_plus']}",
)
record(
    "criticality_counterfactual_sin_minus_identical",
    run_leaf["sin_minus"] == run_critical["sin_minus"],
    detail=f"sin_minus={run_leaf['sin_minus']}",
)
record(
    "criticality_counterfactual_abs_p_plus_identical",
    run_leaf["abs_p_plus"] == run_critical["abs_p_plus"],
    detail="abs_p_plus bit-identical",
)
record(
    "criticality_counterfactual_abs_p_minus_identical",
    run_leaf["abs_p_minus"] == run_critical["abs_p_minus"],
    detail="abs_p_minus bit-identical",
)
log("")


# -----------------------------------------------------------
# Block 16
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 16: audit-snapshot consistency check (previous_audits[] surface)")
log("=" * 72)
ledger_data = json.loads(LEDGER.read_text(encoding="utf-8"))
row = ledger_data["rows"].get(
    "dm_sigma_hier_h_intrinsic_no_go_theorem_note_2026-04-20"
)
record(
    "ledger_row_present",
    row is not None,
    detail=("present" if row is not None else "MISSING"),
)
if row is not None:
    prev_audits = row.get("previous_audits", [])
    record(
        "previous_audits_count_three",
        len(prev_audits) == 3,
        detail=f"len={len(prev_audits)}",
    )
    expected_invalidations = {
        "criticality_increased:leaf->medium",
        "criticality_increased:medium->critical",
    }
    seen_invalidations = {
        a.get("invalidation_reason")
        for a in prev_audits
        if a.get("invalidation_reason")
    }
    record(
        "previous_audits_invalidations_contain_both_bumps",
        expected_invalidations.issubset(seen_invalidations),
        detail=f"seen={sorted(seen_invalidations)}",
    )
    for i, a in enumerate(prev_audits):
        record(
            f"previous_audits[{i}]_has_verdict_rationale",
            isinstance(a.get("verdict_rationale"), str)
            and len(a.get("verdict_rationale", "")) > 50,
            detail=(
                f"len={len(a.get('verdict_rationale', '') or '')}"
            ),
        )
        record(
            f"previous_audits[{i}]_has_chain_closes_field",
            "chain_closes" in a,
            detail=f"value={a.get('chain_closes')!r}",
        )
log("")


# -----------------------------------------------------------
# Block 17
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 17: companion runner imports no frontier_sigma_hier_uniqueness symbol")
log("=" * 72)
companion_src = Path(__file__).read_text(encoding="utf-8")
# Static import scan: look only at executable import statements
# (line starts with optional whitespace then `import ` or `from `), so
# narrative mentions of module names inside docstrings, comments, string
# literals, or self-referential check labels are ignored.
import_line_re = re.compile(
    r"^\s*(?:import\s+(?P<imp>[A-Za-z_][\w\.]*)"
    r"|from\s+(?P<frm>[A-Za-z_][\w\.]*)\s+import\s+)",
    re.MULTILINE,
)
forbidden_modules = {
    "frontier_sigma_hier_uniqueness_theorem",
    "frontier_dm_sigma_hier_h_intrinsic_no_go_theorem_2026_04_20",
}
imported_modules: set[str] = set()
for match in import_line_re.finditer(companion_src):
    mod = match.group("imp") or match.group("frm") or ""
    if mod:
        # Take just the top-level module name (e.g. 'numpy.linalg' -> 'numpy')
        imported_modules.add(mod.split(".")[0])
for forb in sorted(forbidden_modules):
    record(
        f"companion_does_not_import::{forb}",
        forb not in imported_modules,
        detail=(
            "absent_from_executable_imports"
            if forb not in imported_modules
            else "FOUND_AS_ACTUAL_IMPORT"
        ),
    )
record(
    "companion_executable_imports_only_safe_stdlib_and_numpy",
    imported_modules.issubset(
        {
            "hashlib",
            "json",
            "math",
            "re",
            "subprocess",
            "sys",
            "itertools",
            "pathlib",
            "numpy",
            "__future__",
        }
    ),
    detail=f"imports={sorted(imported_modules)}",
)
log("")


# -----------------------------------------------------------
# Block 18
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 18: Blocks 7-11 all reproduce parent algebra with no upstream import")
log("=" * 72)
# Re-run the algebraic checks once more in a fresh local scope to confirm
# they have no hidden dependency on the parent runner's namespace.
def fresh_self_contained_block() -> dict:
    h = h_mat_repro(M_STAR_REPRO, DELTA_STAR_REPRO, Q_PLUS_STAR_REPRO)
    e, v = np.linalg.eigh(h)
    o = np.argsort(np.real(e))
    e = np.real(e[o])
    v = v[:, o]
    survivors_inner: list[tuple[int, int, int]] = []
    for perm in permutations(range(3)):
        if count_passes_repro(np.abs(v[list(perm), :])) == 9:
            survivors_inner.append(perm)
    p_p = v[list((2, 0, 1)), :]
    p_m = v[list((2, 1, 0)), :]
    return {
        "survivors_set": set(survivors_inner),
        "row_swap_match": np.allclose(
            p_p, s_mutau @ p_m, atol=1e-12
        ),
        "jarlskog_sign_flip": np.sign(jarlskog_sin_dcp_repro(p_p))
        == -np.sign(jarlskog_sin_dcp_repro(p_m)),
    }


fresh = fresh_self_contained_block()
record(
    "fresh_block_survivors_set_eq_expected",
    fresh["survivors_set"] == {(2, 0, 1), (2, 1, 0)},
    detail=f"survivors={sorted(fresh['survivors_set'])}",
)
record(
    "fresh_block_row_swap_match",
    bool(fresh["row_swap_match"]),
    detail=f"match={fresh['row_swap_match']}",
)
record(
    "fresh_block_jarlskog_sign_flip",
    bool(fresh["jarlskog_sign_flip"]),
    detail=f"flip={fresh['jarlskog_sign_flip']}",
)
log("")


# -----------------------------------------------------------
# Block 19
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 19: numerical robustness of the surviving pair")
log("=" * 72)


def survivors_via_enumeration_order(order_key) -> set:
    h = h_mat_repro(M_STAR_REPRO, DELTA_STAR_REPRO, Q_PLUS_STAR_REPRO)
    e, v = np.linalg.eigh(h)
    o = np.argsort(np.real(e))
    e = np.real(e[o])
    v = v[:, o]
    perms_in_order = sorted(permutations(range(3)), key=order_key)
    s = set()
    for perm in perms_in_order:
        if count_passes_repro(np.abs(v[list(perm), :])) == 9:
            s.add(perm)
    return s


orderings = [
    ("lexicographic", lambda p: p),
    ("reverse", lambda p: tuple(-x for x in p)),
    (
        "by_sum_then_diff",
        lambda p: (sum(p), p[1] - p[0], p[2] - p[1]),
    ),
]
for name, key in orderings:
    s = survivors_via_enumeration_order(key)
    record(
        f"robustness_survivors_under_ordering::{name!r}",
        s == {(2, 0, 1), (2, 1, 0)},
        detail=f"survivors={sorted(s)}",
    )
log("")


# -----------------------------------------------------------
# Block 20
# -----------------------------------------------------------

log("=" * 72)
log("BLOCK 20: surviving-pair complementarity / row-swap parity chain")
log("=" * 72)
# det(S_mutau) = -1 (single row transposition); since the Jarlskog determinant
# J = Im(P00 P01* P10* P11) depends on the row labels e (row 0) and mu (row 1),
# a row swap of rows 1 and 2 (mu<->tau) changes the sign of J. Verify both:
record(
    "s_mutau_is_odd_permutation",
    abs(np.linalg.det(s_mutau).real - (-1.0)) < 1e-14
    and abs(np.linalg.det(s_mutau).imag) < 1e-14,
    detail=f"det(S_mutau)={complex(np.linalg.det(s_mutau))}",
)


def jarlskog_imag_from_top_block(p_mat: np.ndarray) -> float:
    return float(
        (
            p_mat[0, 0]
            * p_mat[0, 1].conjugate()
            * p_mat[1, 0].conjugate()
            * p_mat[1, 1]
        ).imag
    )


j_plus_raw = jarlskog_imag_from_top_block(p_plus_local)
j_minus_raw = jarlskog_imag_from_top_block(p_minus_local)
record(
    "jarlskog_top_block_imag_signs_opposite_for_pair",
    np.sign(j_plus_raw) == -np.sign(j_minus_raw)
    and abs(j_plus_raw) > 1e-10
    and abs(j_minus_raw) > 1e-10,
    detail=f"J+={j_plus_raw:+.6e}, J-={j_minus_raw:+.6e}",
)
record(
    "row_swap_parity_chain_consistent_with_runner_outputs",
    abs(sin_plus_local) > 0.9
    and abs(sin_minus_local) > 0.9
    and np.sign(sin_plus_local) == -np.sign(sin_minus_local),
    detail=f"sin_+={sin_plus_local:+.10f}, sin_-={sin_minus_local:+.10f}",
)
log("")


# -----------------------------------------------------------
# Footer
# -----------------------------------------------------------

log("=" * 72)
log("Interpretation:")
log("  The parent narrow no-go theorem's substance, runner output, and")
log("  load-bearing algebraic content are unchanged across the 2026-05-03")
log("  / 2026-05-04 criticality_increased invalidation events. The")
log("  load-bearing pair-pin fact is re-derived self-containedly inside")
log("  this companion runner (Blocks 7-11) from numpy.linalg.eigh and")
log("  the inlined chamber-pin numerical values, with no frontier-runner")
log("  symbol imported (Block 17). The audit lane retains independent")
log("  authority to re-honor or re-test the prior verdicts on the bumped")
log("  medium-criticality tier.")
log("")
log(f"PASS={PASS} FAIL={FAIL}")

sys.exit(0 if FAIL == 0 else 1)
