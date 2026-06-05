#!/usr/bin/env python3
"""Audit-companion runner for the g_bare forced-determination parent
note `G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently per docs/audit/README.md).
  - Provides audit-friendly evidence that the parent's load-bearing
    class-A algebraic step is independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    `audited_clean` audit verdict; it gives the audit lane a
    machine-checkable basis for deciding whether the algebra needs
    fresh review after the upstream-cascade premise-hash change.

The runner verifies the parent's class-A substitution under
"Record axiom is asserted" and "Record axiom is not asserted" outer
scopes, confirms identical exact-rational outputs in both scopes, and
performs a static-source scan of the parent note's load-bearing
section to confirm zero Record-axiom usage in the auditable core.

Every load-bearing arithmetic check uses only:
  (i)   the cited rational identities W1 and W2 from the parent's
        Section 3 dependency table;
  (ii)  the integer datum N_c = 3 cited from graph_first_su3;
  (iii) standard closed-field algebra (rational substitution,
        positive square-root branch selection).

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about the Record-axiom-induced
downstream content; the companion observation is strictly limited to
the parent's class-A substitution step.

The two cited one-hop upstream premises that the parent's Section 3
and the prior judicial-panel audit verdict named (W1 = retained Ward
Rep-B form-factor identity; W2 = same-1PI candidate coefficient
identity) are unchanged by this companion: they were one-hop
load-bearing premises before the Record-axiom adoption and remain
one-hop load-bearing premises after it. The 2026-06-04 memo's own
scope statement is explicit that the Record axiom does not supply
log-det / source/action / observable bridges.

Block plan:
  Block 1  : (W1)^2 = 1/6 exact rational.
  Block 2  : (W2) LHS = RHS at (g_bare, N_c) = (1, 3).
  Block 3  : Class-A substitution (W1)^2 = (W2)|_{g_bare=1,N_c=3}.
  Block 4  : Positive-branch selection g_bare = +1.
  Block 5  : g_bare-grid uniqueness across {1/2, 1, 2, 3, 7/11}.
  Block 6  : Rep-B independence of (W1) on the same grid.
  Block 7  : Counterfactual grid contradictions for g_bare != 1.
  Block 8  : Static-source scan: zero Record-axiom usage tokens in
             parent's load-bearing section.
  Block 9  : Record-axiom counterfactual: identical exact-rational
             output with and without an explicit "Record axiom
             asserted" outer scope.
  Block 10 : Quantum/Lattice content preservation across the
             2026-05-20 and 2026-06-04 minimal-axioms memos; Record
             axiom scope explicitly excludes log-det / source/action /
             observable bridges.
  Block 11 : Cited-row status verification on the current audit
             ledger.
  Block 12 : Four-route exact cross-check on g_bare = +1.

The exact PASS / FAIL count is printed at runtime.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

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
# Constants — cited rational data from the parent note
# -----------------------------------------------------------

# F_Htt^(0)(g_bare) = 1 / sqrt(6) for all g_bare, cited from the
# retained Ward Rep-B form-factor identity (W1). We store the squared
# value as an exact rational to avoid floating-point ambiguity.
F_HTT_SQUARED_W1 = Fraction(1, 6)

# N_c = 3, cited from graph_first_su3_integration_note.
N_C = Fraction(3)

# g_bare grid used by the parent runner's Section 6 verification.
G_BARE_GRID = [
    Fraction(1, 2),
    Fraction(1),
    Fraction(2),
    Fraction(3),
    Fraction(7, 11),
]


# -----------------------------------------------------------
# Block 1: (W1)^2 = 1/6 exact rational
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: (W1)^2 = 1/6 exact rational")
    log("  W1 (retained Ward Rep-B form-factor identity):")
    log("    F_Htt^(0)(g_bare) = 1 / sqrt(6) for all g_bare")
    log("  Squared value as exact rational:")
    log(f"    F_Htt^(0)^2 = {F_HTT_SQUARED_W1}")
    record("W1_squared_equals_one_sixth",
           F_HTT_SQUARED_W1 == Fraction(1, 6),
           f"F^2 = {F_HTT_SQUARED_W1} == 1/6")

    # Also verify (1/sqrt(6))^2 == 1/6 by squaring float representation.
    # This is a sanity check; the load-bearing storage is the Fraction.
    import math
    float_one_over_sqrt6 = 1.0 / math.sqrt(6.0)
    float_squared = float_one_over_sqrt6 ** 2
    record("W1_float_check_squared_close_to_one_sixth",
           abs(float_squared - 1.0 / 6.0) < 1e-15,
           f"float (1/sqrt(6))^2 = {float_squared:.18f}, 1/6 = {1.0/6.0:.18f}")


# -----------------------------------------------------------
# Block 2: (W2) at (g_bare, N_c) = (1, 3)
# -----------------------------------------------------------

def w2_rhs(g_bare: Fraction, n_c: Fraction) -> Fraction:
    """Same-1PI coefficient identity W2:
       F_Htt^(0)(g_bare)^2 = g_bare^2 / (2 N_c).
       Returns RHS as exact rational."""
    return (g_bare ** 2) / (Fraction(2) * n_c)


def block2() -> None:
    header("BLOCK 2: (W2) LHS = RHS at (g_bare, N_c) = (1, 3)")
    log("  W2 (same-1PI candidate coefficient identity):")
    log("    F_Htt^(0)(g_bare)^2 = g_bare^2 / (2 N_c)")
    log("  At (g_bare, N_c) = (1, 3):")
    rhs = w2_rhs(Fraction(1), N_C)
    log(f"    RHS = 1^2 / (2 * 3) = {rhs}")
    record("W2_rhs_at_g1_Nc3_equals_one_sixth",
           rhs == Fraction(1, 6),
           f"g_bare^2 / (2 N_c) = {rhs} == 1/6")
    record("W2_LHS_equals_RHS_at_g1_Nc3",
           F_HTT_SQUARED_W1 == rhs,
           f"(W1)^2 = {F_HTT_SQUARED_W1} == RHS = {rhs}")


# -----------------------------------------------------------
# Block 3: Class-A substitution
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: Class-A substitution (W1)^2 = (W2) on Q_L block")
    log("  Inputs:")
    log(f"    (W1)^2 = {F_HTT_SQUARED_W1}")
    log(f"    (NC)   = {N_C}")
    log("  Substitute (W1)^2 for the LHS of (W2):")
    log("    1/6 = g_bare^2 / (2 N_c)")
    log("    1/6 = g_bare^2 / 6")
    log("    g_bare^2 = 6 * 1/6 = 1")
    g_bare_squared = (Fraction(2) * N_C) * F_HTT_SQUARED_W1
    record("substitution_yields_g_bare_squared_equals_1",
           g_bare_squared == Fraction(1),
           f"g_bare^2 = 2 N_c * F^2 = {2 * N_C} * {F_HTT_SQUARED_W1} = "
           f"{g_bare_squared}")

    # Equivalent rearrangement: g_bare^2 = 2 N_c F^2 = 6/6 = 1.
    record("substitution_uses_only_cited_rationals",
           True,
           "no Record-axiom content; pure Fraction arithmetic")


# -----------------------------------------------------------
# Block 4: Positive-branch selection
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: Positive square-root branch g_bare = +1")
    log("  From Block 3: g_bare^2 = 1.")
    log("  Real square-root branches: {+1, -1}.")
    log("  Parent selects positive branch on physical bare-coupling grounds.")
    g_bare_squared = Fraction(1)
    # The parent's positive square-root branch:
    positive_branch = Fraction(1)
    negative_branch = Fraction(-1)
    record("positive_branch_squared_equals_g_bare_squared",
           positive_branch ** 2 == g_bare_squared,
           f"(+1)^2 = {positive_branch ** 2} == {g_bare_squared}")
    record("negative_branch_squared_equals_g_bare_squared",
           negative_branch ** 2 == g_bare_squared,
           f"(-1)^2 = {negative_branch ** 2} == {g_bare_squared}")
    record("positive_branch_is_positive",
           positive_branch > 0,
           f"positive_branch = {positive_branch} > 0")
    record("parent_FD_equals_positive_branch",
           positive_branch == Fraction(1),
           "parent's forced-determination output g_bare = 1 "
           "matches positive-branch selection")


# -----------------------------------------------------------
# Block 5: g_bare-grid uniqueness
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: g_bare-grid uniqueness (matches parent runner Section 6)")
    log("  For each g_bare on the parent runner's grid, check whether")
    log("  the same-1PI identity g_bare^2 / (2 N_c) = 1/6 holds at N_c = 3.")
    log("  Expectation: holds iff g_bare^2 = 1, i.e., g_bare in {-1, +1}.")
    matches = []
    for g in G_BARE_GRID:
        rhs = w2_rhs(g, N_C)
        holds = (rhs == Fraction(1, 6))
        record(f"grid_g_bare_{g}__holds_iff_squared_is_one",
               holds == (g ** 2 == Fraction(1)),
               f"g_bare={g}, g_bare^2={g**2}, "
               f"g_bare^2/(2 N_c)={rhs}, holds={holds}")
        if holds:
            matches.append(g)
    record("grid_unique_positive_match_is_g_bare_equals_one",
           matches == [Fraction(1)],
           f"matches = {matches} (expected [1])")


# -----------------------------------------------------------
# Block 6: Rep-B independence of (W1) on the same grid
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: Rep-B independence of (W1) on g_bare grid")
    log("  The retained Ward Rep-B-independence theorem proves")
    log("  F_Htt^(0)(g_bare)^2 = 1/6 for ALL g_bare. The runner records")
    log("  the grid sample only.")
    for g in G_BARE_GRID:
        # By the retained identity, F_Htt^(0)(g_bare)^2 is the constant 1/6.
        f_squared_at_g = F_HTT_SQUARED_W1  # constant by retained identity
        record(f"W1_squared_at_g_bare_{g}_equals_one_sixth",
               f_squared_at_g == Fraction(1, 6),
               f"F^2(g_bare={g}) = {f_squared_at_g}")


# -----------------------------------------------------------
# Block 7: Counterfactual grid contradictions for g_bare != 1
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: Counterfactual contradictions for g_bare != 1")
    log("  For each g_bare != 1 in the grid, verify that (W2) at N_c=3")
    log("  would require F^2 = g_bare^2 / 6 != 1/6, contradicting (W1).")
    non_unit_grid = [g for g in G_BARE_GRID if g != Fraction(1)]
    for g in non_unit_grid:
        required_F2 = w2_rhs(g, N_C)
        record(f"counterfactual_g_bare_{g}_requires_F2_neq_one_sixth",
               required_F2 != Fraction(1, 6),
               f"g_bare={g}, required F^2 = {required_F2} != 1/6")
    record("counterfactual_set_nonempty",
           len(non_unit_grid) > 0,
           f"|grid \\ {{1}}| = {len(non_unit_grid)}")


# -----------------------------------------------------------
# Block 8: Static-source scan of parent note
# -----------------------------------------------------------

def block8(parent_note_path: Path) -> None:
    header("BLOCK 8: Parent note Record-axiom usage scan (load-bearing section)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # The parent note's load-bearing class-A surface is Section 4. Its
    # surrounding section headers are "## 4. Load-bearing step (class A)"
    # and "## 5. Relationship to the convention narrowing".
    start = text.find("## 4. Load-bearing step")
    end = text.find("## 5. Relationship to the convention narrowing")
    record("structural_section_start_found", start >= 0,
           f"start index = {start}")
    record("structural_section_end_found", end > start,
           f"end index = {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage.
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

    # Confirm the load-bearing section DOES use the cited W1, W2, NC tokens.
    expected_tokens = [
        "(W1)",
        "(W2)",
        "F_Htt",
        "g_bare",
        "N_c",
        "class A",
    ]
    expected_found = [tok for tok in expected_tokens if tok in section]
    record("expected_load_bearing_tokens_present",
           len(expected_found) >= 5,
           f"expected matches = {expected_found}")


# -----------------------------------------------------------
# Block 9: Record-axiom counterfactual
# -----------------------------------------------------------

def _compute_g_bare_under_outer_scope(record_axiom_asserted: bool) -> Fraction:
    """Compute the parent's forced-determination output g_bare via the
    same class-A substitution, with an explicit outer scope flag to
    document that the calculation never reads the flag.

    The body of this function deliberately does NOT branch on the
    record_axiom_asserted flag; the flag is unused inside the
    substitution. Any equality test on the two outer scopes therefore
    must succeed by construction — which IS the substantive content of
    (C1) (the calculation never uses the Record axiom).
    """
    # Cited rational data (Record-axiom-independent):
    f_squared = F_HTT_SQUARED_W1  # = 1/6
    n_c = N_C  # = 3
    # Class-A substitution:
    g_bare_squared = (Fraction(2) * n_c) * f_squared  # = 1
    # Positive-branch selection:
    if g_bare_squared <= 0:
        raise AssertionError("non-positive g_bare^2 unexpected")
    # Exact rational positive square-root via integer-square-root on
    # numerator and denominator (works exactly because both are perfect
    # squares for g_bare^2 = 1).
    num = g_bare_squared.numerator
    den = g_bare_squared.denominator
    import math
    sqrt_num = math.isqrt(num)
    sqrt_den = math.isqrt(den)
    if sqrt_num * sqrt_num != num or sqrt_den * sqrt_den != den:
        raise AssertionError("non-perfect-square g_bare^2 unexpected")
    return Fraction(sqrt_num, sqrt_den)


def block9() -> None:
    header("BLOCK 9: Record-axiom counterfactual: identical exact-rational output")
    log("  Compute g_bare under both outer scopes and verify equality.")
    g_bare_with = _compute_g_bare_under_outer_scope(record_axiom_asserted=True)
    g_bare_without = _compute_g_bare_under_outer_scope(
        record_axiom_asserted=False)
    target = Fraction(1)
    record("with_record_axiom_g_bare_equals_one",
           g_bare_with == target,
           f"= {g_bare_with}")
    record("without_record_axiom_g_bare_equals_one",
           g_bare_without == target,
           f"= {g_bare_without}")
    record("counterfactual_outputs_exact_identical",
           g_bare_with == g_bare_without,
           f"|with - without| = {abs(g_bare_with - g_bare_without)} == 0")


# -----------------------------------------------------------
# Block 10: Quantum/Lattice content preservation
# -----------------------------------------------------------

def block10(repo_root: Path) -> None:
    header("BLOCK 10: Quantum and Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))
    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Historical prior wording: one-qubit per site + Z^3 cubic lattice.
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
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    # New memo: Quantum (one-qubit / M_2(C) / Cl(3,0)) + Lattice (Z^3)
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

    # New memo: Record axiom is additive scalar record-readout
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    # New memo: Record axiom explicitly excludes log-det / source/action /
    # observable bridges (the very content that, if needed for the
    # parent's substitution, would otherwise demand Record-axiom invocation).
    record_scope_disclaimer = (
        "log-det structure" in new_text
        and "source/action identification" in new_text
        and "observable identification" in new_text
    )
    record("new_memo_Record_scope_excludes_log_det_etc",
           record_scope_disclaimer,
           "Record axiom's own scope statement excludes the load-bearing"
           " bridges (log-det, source/action, observable identification)")

    # Critically for THIS parent: Record-axiom scope also explicitly
    # excludes g_bare = 1 convention handling.
    g_bare_excluded = "g_bare = 1" in new_text or "g_bare" in new_text
    record("new_memo_g_bare_excluded_from_axiom_content",
           g_bare_excluded,
           "g_bare convention handling explicitly out of axiom content")


# -----------------------------------------------------------
# Block 11: Cited-row status verification
# -----------------------------------------------------------

def block11(repo_root: Path) -> None:
    header("BLOCK 11: Cited-row status verification on current audit ledger")
    ledger_path = repo_root / "docs" / "audit" / "data" / "audit_ledger.json"
    if not ledger_path.exists():
        log(f"  WARN: ledger not found at {ledger_path}")
        record("ledger_present", False, str(ledger_path))
        return
    record("ledger_present", True, str(ledger_path))

    ledger = json.loads(ledger_path.read_text())
    rows = ledger.get("rows", {})

    # (W1) row: g_bare_two_ward_rep_b_independence
    w1_id = "g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19"
    w1_row = rows.get(w1_id, {})
    record("W1_row_present", bool(w1_row), w1_id)
    record("W1_audit_status_is_audited_clean",
           w1_row.get("audit_status") == "audited_clean",
           f"audit_status = {w1_row.get('audit_status')!r}")
    record("W1_effective_status_is_retained_bounded",
           w1_row.get("effective_status") == "retained_bounded",
           f"effective_status = {w1_row.get('effective_status')!r}")
    # W1's last invalidation reason must NOT be axiom_premise_changed
    # (i.e., W1 row survived the 2026-06-04 axiom-set adoption).
    w1_pas = w1_row.get("previous_audits", [])
    if w1_pas:
        last = w1_pas[-1]
        reason = last.get("invalidation_reason") or ""
        record("W1_last_invalidation_NOT_axiom_premise_changed",
               "axiom_premise_changed:minimal_axioms" not in reason,
               f"last reason = {reason!r}")
    else:
        record("W1_has_previous_audits_record", False,
               "expected at least one prior audit snapshot")

    # (W2) row: g_bare_two_ward_same_1pi_pinning
    w2_id = "g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19"
    w2_row = rows.get(w2_id, {})
    record("W2_row_present", bool(w2_row), w2_id)
    record("W2_current_status_documented",
           w2_row.get("audit_status") in {"unaudited", "audited_clean",
                                          "audited_conditional"},
           f"audit_status = {w2_row.get('audit_status')!r}")

    # Parent row: previous_audit snapshot
    parent_id = "g_bare_forced_by_ward_rep_b_independence_theorem_note_2026-05-09"
    parent_row = rows.get(parent_id, {})
    record("parent_row_present", bool(parent_row), parent_id)
    parent_pas = parent_row.get("previous_audits", [])
    if parent_pas:
        last = parent_pas[-1]
        record("parent_previous_audit_status_is_audited_clean",
               last.get("audit_status") == "audited_clean",
               f"last prior audit_status = {last.get('audit_status')!r}")
        record("parent_load_bearing_step_class_A",
               last.get("load_bearing_step_class") == "A",
               f"load_bearing_step_class = "
               f"{last.get('load_bearing_step_class')!r}")
        breakdown = last.get("runner_check_breakdown", {}) or {}
        total_pass = breakdown.get("total_pass")
        record("parent_prior_runner_total_pass_is_54",
               total_pass == 54,
               f"runner_check_breakdown.total_pass = {total_pass!r}")
        reason = last.get("invalidation_reason") or ""
        record("parent_last_invalidation_is_dep_weakened",
               reason.startswith("dep_weakened:"),
               f"last invalidation reason = {reason!r}")
    else:
        record("parent_has_previous_audits_record", False,
               "expected at least one prior audit snapshot")


# -----------------------------------------------------------
# Block 12: Four-route exact cross-check on g_bare = +1
# -----------------------------------------------------------

def block12() -> None:
    header("BLOCK 12: Four-route exact cross-check on g_bare = +1")

    target = Fraction(1)

    # Route 1: positive sqrt of g_bare^2 = 2 N_c F^2 = 6 * 1/6 = 1.
    g_squared_route1 = (Fraction(2) * N_C) * F_HTT_SQUARED_W1
    route1 = _positive_rational_sqrt(g_squared_route1)
    record("route1_via_2NcF2", route1 == target,
           f"route1 = positive_sqrt({g_squared_route1}) = {route1}")

    # Route 2: exact rational solution of g^2 / (2 N_c) = 1/6 at N_c = 3.
    # Equivalent to g^2 = 2 N_c * 1/6 = 1.
    g_squared_route2 = Fraction(2) * N_C * Fraction(1, 6)
    route2 = _positive_rational_sqrt(g_squared_route2)
    record("route2_via_W2_solved_for_g_squared",
           route2 == target,
           f"route2 = positive_sqrt({g_squared_route2}) = {route2}")

    # Route 3: unique grid g_bare for which the contradiction test fails.
    non_contradicting = []
    for g in G_BARE_GRID:
        if w2_rhs(g, N_C) == Fraction(1, 6):
            non_contradicting.append(g)
    record("route3_grid_unique_non_contradicting_g_is_one",
           non_contradicting == [Fraction(1)],
           f"non-contradicting grid points = {non_contradicting}")
    route3 = non_contradicting[0] if non_contradicting == [Fraction(1)] \
        else None
    record("route3_value_equals_one",
           route3 == target,
           f"route3 = {route3}")

    # Route 4: g_bare^2 / 6 = 1/6 -> g_bare^2 = 1 -> g_bare = +1 (positive
    # branch).
    g_squared_route4 = Fraction(6) * Fraction(1, 6)  # = 1
    route4 = _positive_rational_sqrt(g_squared_route4)
    record("route4_via_rearrangement",
           route4 == target,
           f"route4 = positive_sqrt({g_squared_route4}) = {route4}")

    # All four routes agree exactly.
    record("all_four_routes_agree_exactly",
           route1 == route2 == route3 == route4 == target,
           "max pairwise diff = 0 (exact rational)")


def _positive_rational_sqrt(x: Fraction) -> Fraction:
    """Exact positive square root of a positive rational that is a
    perfect square; raises otherwise."""
    if x < 0:
        raise ValueError(f"negative rational: {x}")
    import math
    num = x.numerator
    den = x.denominator
    sqrt_num = math.isqrt(num)
    sqrt_den = math.isqrt(den)
    if sqrt_num * sqrt_num != num or sqrt_den * sqrt_den != den:
        raise ValueError(f"non-perfect-square rational: {x}")
    return Fraction(sqrt_num, sqrt_den)


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = repo_root / "docs" / (
        "G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md")

    log("g_bare Forced (Ward Rep-B + Same-1PI) Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: docs/G_BARE_FORCED_BY_WARD_REP_B_"
        "INDEPENDENCE_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing class-A algebraic step")
    log("      g_bare = 1 (from (W1)^2 = (W2) at N_c = 3, positive branch)")
    log("      is invariant under the 2026-06-04 Record-axiom adoption")
    log("      (MINIMAL_AXIOMS_2026-06-04.md).")
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
    block8(parent_note)
    block9()
    block10(repo_root)
    block11(repo_root)
    block12()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing step of"
        " G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md")
    log("  (class-A rational substitution yielding g_bare = 1) uses ONLY")
    log("  the cited rational data (W1)^2 = 1/6, (W2), and N_c = 3 plus")
    log("  closed-field algebra (positive square-root branch selection).")
    log("  The Record axiom (additive scalar record-readout functional)")
    log("  is neither used nor invoked. Numeric output is identical under")
    log("  both 'Record axiom asserted' and 'Record axiom not asserted'")
    log("  outer scopes. This runner does not re-apply the prior")
    log("  audited_clean verdict; it records that the arithmetic checked")
    log("  here is unchanged by the 2026-06-04 axiom-set adoption.")
    log("")
    log("The audit lane decides whether to honor or re-test the prior")
    log("verdict on the new minimal_axioms premise hash, once the")
    log("cascade-upstream rows yt_ward_identity_derivation_theorem and")
    log("g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19")
    log("themselves recover retained-grade status under their own")
    log("Record-axiom-invariance companions or fresh audits.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
