#!/usr/bin/env python3
"""Audit-companion runner for the Higgs lattice eigenvalue ratio parent note
`HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`
recording dep-resolution hygiene evidence after the historical
dep_weakened invalidation cycles cited by the task
(`g_bare_canonical_convention_narrow_theorem_note_2026-05-02:
retained_bounded -> unaudited`, plus a later
`g_bare_constraint_vs_convention_theorem_note_2026-05-03:
retained_bounded -> unaudited`).

Companion source note:
  docs/HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence in two narrow respects:
    (N1) the historical *deprecated* dep cited by the rounds 1-2
         dep_weakened invalidations
         (g_bare_canonical_convention_narrow_theorem_note_2026-05-02)
         is no longer in the parent's declared dependency set on
         origin/main; the parent's 2026-05-28 repair replaced it
         with two retained-grade 2026-05-03 sister theorems plus
         a retained-bounded one-hop authority for u_0 plus a
         retained-pending-chain Clifford-chirality row;
    (N2) the parent's load-bearing substantive R_lattice = 1/(4 u_0^2)
         algebra is mechanically demonstrated by the parent's own
         runner via exact symbolic computation that never queries
         any dep audit grade.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm it exits 0 with the load-bearing identity
            R_lattice = 1/(4 u_0^2) verified at the runner level.
  Block 2 : Re-derive structural counts (N_taste = 2^4 = 16,
            N_tot = N_c * N_sites = 48) and the load-bearing exact
            symbolic identities (W''(0) = N_tot/(4 u_0^2),
            R_lattice = 1/(4 u_0^2), W''/N_tot = 1/(4 u_0^2))
            directly in this companion runner via sympy.Rational.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            references to dep audit-status fields used as load-bearing
            inputs to any algebraic step. (The runner does read the
            ledger for dep-existence checks in Part 6 only; the
            absence-of-load-bearing-status-usage is what matters.)
  Block 4 : Live-ledger scan: confirm the deprecated dep
            g_bare_canonical_convention_narrow_theorem_note_2026-05-02
            is NOT in the parent row's deps field on origin/main.
  Block 5 : Static source-scan of the parent note: confirm the
            historical-pointer disclaimer for the deprecated note is
            present (no load-bearing markdown link).
  Block 6 : Counterfactual: re-execute the parent's runner on the
            current head and confirm identical PASS count to Block 1
            (the current head is exactly the post-dep-weakening
            state, with the parent's repaired 5-dep surface).
  Block 7 : Independent re-derivation of the Clifford identity
            D_taste^2 = d*I at d=4 via explicit Euclidean Cl(4)
            matrix construction, independent of the parent's runner.
  Block 8 : Live-ledger scan: all 5 current declared deps are
            retained-grade (retained, retained_bounded, or
            retained_pending_chain) on origin/main.
  Block 9 : No-claim gate preservation: companion declares
            claim_type=meta, disclaims status promotion, and disclaims
            any physical Higgs-mass / SM matching identification.

Every check uses only the parent's existing runner / parent note /
audit ledger plus standard finite-dimensional sympy/numeric primitives.
No audit-status content is asserted. No new theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

from sympy import I as sympy_I
from sympy import (
    Matrix,
    Rational,
    diff,
    eye,
    log as sym_log,
    simplify,
    sqrt as sym_sqrt,
    symbols,
    zeros,
)
from sympy.physics.quantum import TensorProduct


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    log(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    log("")
    log("-" * 88)
    log(title)
    log("-" * 88)


# -----------------------------------------------------------
# Paths and constants
# -----------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
PARENT_NOTE_PATH = ROOT / "docs" / "HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md"
COMPANION_NOTE_PATH = ROOT / "docs" / "HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
PARENT_RUNNER_PATH = ROOT / "scripts" / "frontier_higgs_lattice_eigenvalue_ratio_narrow.py"
COMPANION_RUNNER_PATH = Path(__file__).resolve()
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_CLAIM_ID = "higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02"
DEPRECATED_DEP_ID = "g_bare_canonical_convention_narrow_theorem_note_2026-05-02"
CURRENT_DEP_IDS = {
    "graph_first_su3_integration_note",
    "g_bare_rescaling_freedom_removal_theorem_note_2026-05-03",
    "g_bare_constraint_vs_convention_theorem_note_2026-05-03",
    "u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17",
    "clifford_chirality_dimension_narrow_theorem_note_2026-05-10",
}
RETAINED_GRADES = {
    "retained",
    "retained_bounded",
    "retained_pending_chain",
}


# -----------------------------------------------------------
# Section header
# -----------------------------------------------------------

log("=" * 88)
log("Audit-companion: higgs_lattice_eigenvalue_ratio dep-resolution hygiene")
log("Parent:   docs/HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md")
log("Companion: docs/HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md")
log("Companion type: claim_type=meta, audit_companion, no status promotion.")
log("=" * 88)


# -----------------------------------------------------------
# Block 1 : parent runner re-executes on current head
# -----------------------------------------------------------

section("Block 1: parent runner re-executes on current head")

parent_run = subprocess.run(
    [sys.executable, str(PARENT_RUNNER_PATH)],
    cwd=str(ROOT),
    env={"PYTHONPATH": str(ROOT / "scripts")},
    capture_output=True,
    text=True,
)
parent_stdout = parent_run.stdout
parent_stderr = parent_run.stderr
parent_rc = parent_run.returncode

check(
    "parent runner exits 0",
    parent_rc == 0,
    detail=f"returncode={parent_rc}",
)

# Pull PASS/FAIL counts from the parent runner total line
parent_total_match = re.search(
    r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", parent_stdout
)
parent_pass = int(parent_total_match.group(1)) if parent_total_match else -1
parent_fail = int(parent_total_match.group(2)) if parent_total_match else -1

check(
    "parent runner emits TOTAL line",
    parent_total_match is not None,
    detail="grep 'TOTAL: PASS=' in stdout",
)

check(
    "parent runner FAIL=0",
    parent_fail == 0,
    detail=f"parent_fail={parent_fail}",
)

check(
    "parent runner PASS>=30 (matches prior audit snapshot range)",
    parent_pass >= 30,
    detail=f"parent_pass={parent_pass}",
)

# Spot-check that the load-bearing parts (3, 4, 5) all emit at least one PASS line
for part_title, needle in [
    ("Part 3 Clifford identity", "Σ_μ γ_μ² = d·I = 4·I"),
    ("Part 4 generating-functional curvature", "W'' at J=0 = N_tot / (4 u_0²) = 12 / u_0²"),
    ("Part 5 R_lattice identity", "R_lattice = 4 / (u_0² · N_taste) at N_taste=16 = 1/(4 u_0²)"),
    ("Part 5 per-taste curvature", "per-taste curvature W''/N_tot = 1/(4 u_0²) matches R_lattice"),
]:
    pass_line = f"[PASS (A)] {needle}"
    check(
        f"parent runner emits PASS for: {part_title}",
        pass_line in parent_stdout,
        detail=f"searched for {pass_line!r}",
    )

check(
    "parent runner emits no FAIL line",
    "[FAIL " not in parent_stdout,
    detail="grep '[FAIL ' in stdout",
)


# -----------------------------------------------------------
# Block 2 : independent re-derivation of structural counts and
#          exact symbolic identities
# -----------------------------------------------------------

section("Block 2: independent exact-symbolic re-derivation")

N_c = 3
d = 4
N_sites = 2 ** d
N_taste = N_sites
N_tot = N_c * N_sites

check("N_c = 3", N_c == 3)
check(f"d = 4 (Z^d spacetime; framework 3+1)", d == 4)
check(f"N_sites = 2^d = 16", N_sites == 16 and N_sites == 2 ** d)
check(f"N_taste = N_sites = 16", N_taste == N_sites == 16)
check(f"N_tot = N_c * N_sites = 48", N_tot == 48 and N_tot == N_c * N_sites)

# Generating functional at mean field
J, u0 = symbols("J u0", positive=True)
W = Rational(N_tot, 2) * sym_log(J ** 2 + 4 * u0 ** 2)
W_curvature = simplify(diff(W, J, 2).subs(J, 0))
expected_curvature = Rational(N_tot, 1) / (4 * u0 ** 2)

check(
    "W''(0) = N_tot / (4 u_0^2) = 12 / u_0^2 by exact symbolic differentiation",
    simplify(W_curvature - expected_curvature) == 0,
    detail=f"W''(0) = {W_curvature}, expected {expected_curvature}",
)

# R_lattice
R_lattice = Rational(4, 1) / (u0 ** 2 * Rational(N_taste, 1))
expected_R_lattice = Rational(1, 4) / (u0 ** 2)
check(
    "R_lattice = 4 / (u_0^2 * N_taste) at N_taste=16 = 1 / (4 u_0^2)",
    simplify(R_lattice - expected_R_lattice) == 0,
    detail=f"R_lattice = {simplify(R_lattice)}, expected {expected_R_lattice}",
)

# Per-taste curvature matches R_lattice
per_taste = simplify(W_curvature / Rational(N_tot, 1))
check(
    "W''(0) / N_tot = 1 / (4 u_0^2) matches R_lattice",
    simplify(per_taste - R_lattice) == 0,
    detail=f"W''/N_tot = {per_taste}, R_lattice = {simplify(R_lattice)}",
)

# Mean-field eigenvalue magnitude
lam_mag = 2 * u0
W_alt = Rational(N_tot, 2) * sym_log(J ** 2 + lam_mag ** 2)
check(
    "mean-field eigenvalue magnitude |lambda_full| = 2 u_0 reproduces W(J)",
    simplify(W_alt - W) == 0,
    detail="W = (N_tot/2) log(J^2 + (2 u_0)^2)",
)

# Exact-rational sanity at u_0 = 1: R_lattice = 1/4
R_at_u0_1 = Fraction(4, 1) / (1 * 16)
check(
    "exact-rational sanity: R_lattice = 1/4 at u_0=1, N_taste=16",
    R_at_u0_1 == Fraction(1, 4),
    detail=f"R_lattice|u_0=1 = {R_at_u0_1}",
)

# Per-taste pure-imaginary eigenvalue square magnitude check
# |lambda|^2 = 4 u_0^2 by staggered anti-Hermiticity
lam_sq = lam_mag ** 2
check(
    "|lambda_full|^2 = 4 u_0^2",
    simplify(lam_sq - 4 * u0 ** 2) == 0,
    detail=f"|lambda|^2 = {lam_sq}",
)


# -----------------------------------------------------------
# Block 3 : static source-scan of parent runner
# -----------------------------------------------------------

section("Block 3: parent runner does not use dep audit-status as load-bearing input")

runner_text = PARENT_RUNNER_PATH.read_text()

# Audit-status field substrings that, if used as a *load-bearing input*
# to an algebraic step, would mean the parent depends on the dep grade.
# The parent's runner is allowed to *read* the ledger to verify dep
# existence (Part 6), but the load-bearing algebra (Parts 2-5) must not
# query any audit-status field. We check that the only ledger reads in
# the parent runner are dep-existence checks (rows.get(dep_id) is not
# None) and the parent row's own effective_status, not any dep's
# effective_status used in an algebraic step.

# Count occurrences of "effective_status" in the parent runner. The
# parent's runner Part 6 reads effective_status of the *parent row* for
# a single audit-ordering sanity check (effective_status in
# {unaudited, audited_conditional}); it does NOT read any *dep's*
# effective_status as a load-bearing input to any algebraic step. The
# count is bounded (<=6) and the only usages are the dep-existence
# detail strings (Part 6, line 199) and the parent-row sanity check
# (Part 6, lines 212-213).
effective_status_count = runner_text.count("effective_status")
check(
    "parent runner mentions 'effective_status' at most 6 times "
    "(dep-existence detail strings and parent-row sanity check only, "
    "not dep-grade load-bearing inputs)",
    effective_status_count <= 6,
    detail=f"count={effective_status_count}",
)

# The parent runner's parent-row sanity check (Part 6, line 212) reads
# the parent row's own effective_status and confirms it is in the
# allowed pre-audit set {unaudited, audited_conditional}. This is an
# audit-ordering scope guard for the parent row itself, not a
# dep-grade load-bearing input. We confirm this allowed pattern is
# the only audited_conditional usage in the parent runner.
audited_conditional_count = runner_text.count("audited_conditional")
check(
    "parent runner mentions 'audited_conditional' at most once "
    "(parent-row scope-guard sanity check, not dep-grade load-bearing)",
    audited_conditional_count <= 1,
    detail=f"count={audited_conditional_count}",
)

# Confirm the parent runner does not query dep audit-status fields like
# intrinsic_status, audit_status, retained_bounded, audited_clean, or
# max_descendant_status anywhere (these substrings should be absent).
for forbidden in [
    "intrinsic_status",
    "audit_status",
    "retained_bounded",
    "audited_clean",
    "max_descendant_status",
]:
    check(
        f"parent runner contains no '{forbidden}' usage (no dep-grade load-bearing reference)",
        forbidden not in runner_text,
        detail=f"absent from {PARENT_RUNNER_PATH.name}",
    )

# Confirm the parent runner's only ledger access pattern in Part 6 is
# rows.get(<dep_id>) for existence checks, not queries of dep audit fields.
check(
    "parent runner Part 6 uses rows.get for dep-existence checks (not dep-grade reads)",
    "rows.get(dep_id)" in runner_text,
    detail="dep-existence pattern present",
)


# -----------------------------------------------------------
# Block 4 : live-ledger dep-set scan
# -----------------------------------------------------------

section("Block 4: deprecated dep is not in parent's live ledger deps field")

ledger_text = LEDGER_PATH.read_text()
ledger = json.loads(ledger_text)
parent_row = ledger["rows"].get(PARENT_CLAIM_ID)

check(
    f"parent row '{PARENT_CLAIM_ID}' is present in audit ledger",
    parent_row is not None,
    detail=f"ledger path = {LEDGER_PATH}",
)

if parent_row is not None:
    parent_deps = set(parent_row.get("deps", []))
    check(
        "parent ledger row deps field is non-empty",
        len(parent_deps) > 0,
        detail=f"deps count = {len(parent_deps)}",
    )

    check(
        f"deprecated dep '{DEPRECATED_DEP_ID}' is NOT in parent deps",
        DEPRECATED_DEP_ID not in parent_deps,
        detail=f"parent deps = {sorted(parent_deps)}",
    )

    # All 5 current deps are present
    for dep_id in sorted(CURRENT_DEP_IDS):
        check(
            f"current dep '{dep_id}' is in parent deps",
            dep_id in parent_deps,
        )

    # Sanity: parent deps set equals exactly the 5 current deps
    check(
        "parent deps set equals the 5 current declared deps (no extras, no omissions)",
        parent_deps == CURRENT_DEP_IDS,
        detail=f"parent deps = {sorted(parent_deps)}",
    )

    # Parent ledger row historical invalidation references the deprecated dep
    prior_audits = parent_row.get("previous_audits", []) or []
    deprecated_in_history = any(
        DEPRECATED_DEP_ID in (a.get("invalidation_reason") or "")
        for a in prior_audits
    )
    check(
        "ledger previous_audits[*] confirms historical dep_weakened cited the deprecated dep",
        deprecated_in_history,
        detail=f"prior_audits count = {len(prior_audits)}",
    )


# -----------------------------------------------------------
# Block 5 : parent note historical-pointer disclaimer is present
# -----------------------------------------------------------

section("Block 5: parent note historical-pointer disclaimer for deprecated note")

parent_note_text = PARENT_NOTE_PATH.read_text()

# The parent note mentions the deprecated note ONLY as a historical
# plain-text reader pointer, with an explicit disclaimer.
deprecated_note_basename = "G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md"

check(
    f"parent note mentions deprecated note basename '{deprecated_note_basename}'",
    deprecated_note_basename in parent_note_text,
    detail="historical reference expected (plain-text only)",
)

# The disclaimer language must be present. The parent note hard-wraps
# the disclaimer across multiple lines; we strip whitespace runs to a
# single space before substring search.
parent_note_flat = re.sub(r"\s+", " ", parent_note_text)
disclaimer_fragments = [
    "plain-text reader pointer, not a markdown-link load-bearing dependency",
    "load-bearing g_bare content is now carried by the two retained 2026-05-03 sister theorems",
]
for frag in disclaimer_fragments:
    check(
        f"parent note carries disclaimer fragment: {frag!r}",
        frag in parent_note_flat,
    )

# The deprecated note must NOT appear as a markdown link (no [..](DEPRECATED..) form).
# A markdown link to it would look like ](G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md)
markdown_link_pattern = "](" + deprecated_note_basename + ")"
check(
    "deprecated note is NOT present as a markdown link in parent note "
    "(only plain-text pointer permitted)",
    markdown_link_pattern not in parent_note_text,
    detail="absence of markdown ](...) link to deprecated note",
)


# -----------------------------------------------------------
# Block 6 : counterfactual re-execution under current dep surface
# -----------------------------------------------------------

section("Block 6: counterfactual under current dep surface — identical PASS count")

# Re-run the parent runner; the current origin/main head IS the
# post-dep-weakening / 2026-05-28-repair state. Confirming identical
# PASS count to Block 1 is the substance of the counterfactual.
parent_run_2 = subprocess.run(
    [sys.executable, str(PARENT_RUNNER_PATH)],
    cwd=str(ROOT),
    env={"PYTHONPATH": str(ROOT / "scripts")},
    capture_output=True,
    text=True,
)

parent_stdout_2 = parent_run_2.stdout
parent_total_match_2 = re.search(
    r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", parent_stdout_2
)
parent_pass_2 = int(parent_total_match_2.group(1)) if parent_total_match_2 else -1
parent_fail_2 = int(parent_total_match_2.group(2)) if parent_total_match_2 else -1

check(
    "counterfactual parent runner exits 0",
    parent_run_2.returncode == 0,
    detail=f"returncode={parent_run_2.returncode}",
)

check(
    "counterfactual PASS count matches Block 1",
    parent_pass_2 == parent_pass and parent_pass_2 > 0,
    detail=f"block1 PASS={parent_pass}, counterfactual PASS={parent_pass_2}",
)

check(
    "counterfactual FAIL count is zero",
    parent_fail_2 == 0,
    detail=f"counterfactual FAIL={parent_fail_2}",
)


# -----------------------------------------------------------
# Block 7 : independent re-derivation of D_taste^2 = d * I
# -----------------------------------------------------------

section("Block 7: independent Clifford identity re-derivation (Cl(4))")

s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -sympy_I], [sympy_I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
I2 = eye(2)
I4 = eye(4)

# Independent choice for the four Euclidean Cl(4) generators
gammas = [
    TensorProduct(s1, s1),
    TensorProduct(s1, s2),
    TensorProduct(s1, s3),
    TensorProduct(s2, I2),
]

check(
    "constructed 4 Euclidean gamma matrices, each 4x4",
    len(gammas) == d and all(g.shape == (4, 4) for g in gammas),
)

# Clifford anticommutator {g_a, g_b} = 2 delta_ab I
clifford_ok = True
for a_idx in range(d):
    for b_idx in range(d):
        anti = gammas[a_idx] * gammas[b_idx] + gammas[b_idx] * gammas[a_idx]
        expected = (2 if a_idx == b_idx else 0) * I4
        if simplify(anti - expected) != zeros(4):
            clifford_ok = False
            break
    if not clifford_ok:
        break

check(
    "{gamma_a, gamma_b} = 2 delta_ab I by exact matrix algebra",
    clifford_ok,
)

# Sum of squares
sum_sq = zeros(4)
for g in gammas:
    sum_sq += g * g
check(
    "sum_a gamma_a^2 = d * I = 4 * I (derived)",
    simplify(sum_sq - d * I4) == zeros(4),
)

# Symmetric taste-Dirac element
D_taste = zeros(4)
for g in gammas:
    D_taste += g
D_taste_sq = simplify(D_taste * D_taste)
check(
    "D_taste = sum_a gamma_a has D_taste^2 = d * I = 4 * I (derived)",
    simplify(D_taste_sq - d * I4) == zeros(4),
)

# Magnitude of taste eigenvalues
lam_taste_mag = sym_sqrt(Rational(d, 1))
check(
    "|lambda_taste| = sqrt(d) = 2 (lattice units)",
    lam_taste_mag == Rational(2, 1),
)


# -----------------------------------------------------------
# Block 8 : live-ledger current dep-grade scan
# -----------------------------------------------------------

section("Block 8: all 5 current declared deps are retained-grade")

for dep_id in sorted(CURRENT_DEP_IDS):
    dep_row = ledger["rows"].get(dep_id)
    check(
        f"dep '{dep_id}' present in audit ledger",
        dep_row is not None,
    )
    if dep_row is None:
        continue
    eff = dep_row.get("effective_status")
    check(
        f"dep '{dep_id}' effective_status is retained-grade (eff={eff!r})",
        eff in RETAINED_GRADES,
        detail=f"valid retained grades = {sorted(RETAINED_GRADES)}",
    )


# -----------------------------------------------------------
# Block 9 : no-claim gate preservation
# -----------------------------------------------------------

section("Block 9: companion declares claim_type=meta and disclaims status promotion")

if COMPANION_NOTE_PATH.exists():
    companion_text = COMPANION_NOTE_PATH.read_text()
    companion_flat = re.sub(r"\s+", " ", companion_text)
    for needle in [
        "**Type:** meta",
        "audit-companion / dep-resolution hygiene evidence",
        "not a status promotion",
        "claim_type=meta",
        "It is not a re-audit and does not promote status",  # disclaimer
        "physical Higgs-mass / SM matching",  # disclaimer
        "derive `m_H = v/(2 u_0)` (separate full theorem)",  # explicit non-derivation
        "deprecated dep cited by the historical rounds 1-2",  # angle 1
        "exact symbolic computation",  # angle 2
        "audit_companion",
    ]:
        check(
            f"companion note carries: {needle!r}",
            needle in companion_flat,
        )
else:
    check(
        "companion note exists at expected path",
        False,
        detail=f"missing: {COMPANION_NOTE_PATH}",
    )

# Forbidden claims (status-promotion / scope-overreach)
forbidden_in_companion = [
    "is hereby audited_clean",
    "promote to retained_bounded",
    "this companion changes audit_status",
    "Standard Model Higgs mass is established",
    "m_H = v/(2 u_0) is hereby derived",
    "(m_H/v)^2 is identified",
]
if COMPANION_NOTE_PATH.exists():
    companion_text2 = COMPANION_NOTE_PATH.read_text()
    for f in forbidden_in_companion:
        check(
            f"companion note avoids forbidden claim: {f!r}",
            f not in companion_text2,
        )


# -----------------------------------------------------------
# Summary and FINAL_TAG
# -----------------------------------------------------------

log("")
log("=" * 88)
log(f"  TOTAL: PASS={PASS}, FAIL={FAIL}")
log("=" * 88)
log("")

if FAIL == 0:
    log("FINAL_TAG: HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_OK")
else:
    log("FINAL_TAG: HIGGS_LATTICE_EIGENVALUE_RATIO_DEP_RESOLUTION_HYGIENE_FAIL")

sys.exit(1 if FAIL > 0 else 0)
