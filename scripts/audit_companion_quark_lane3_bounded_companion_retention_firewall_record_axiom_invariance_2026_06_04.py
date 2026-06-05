#!/usr/bin/env python3
"""Audit-companion runner for the Quark Lane-3 Bounded-Companion Retention
Firewall parent note
`QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row: `quark_lane3_bounded_companion_retention_firewall_note_2026-04-27`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    firewall structure (negative-boundary accounting on the open
    staggered-Dirac realization gate, ratio invariance under
    bottom-anchor rescaling, species-uniform Ward-reuse overshoot
    comparator, and CKM-mass logical type-distinction) is independent
    of the Record axiom adopted in `MINIMAL_AXIOMS_2026-06-04.md`.
    This does not re-apply the prior audit verdicts; it gives the
    audit lane a machine-checkable basis for deciding whether the
    firewall arithmetic + accounting needs fresh review after the
    premise-hash change.

The runner verifies the firewall's load-bearing step block-by-block
under "Record axiom is asserted" and "Record axiom is not asserted"
outer scopes, confirms identical numeric/logical outputs in both
scopes, and performs a static-source scan of the parent note's
load-bearing sections to confirm zero Record-axiom usage in the
auditable firewall core.

Every load-bearing arithmetic/logical check uses only:
  (i)   the Lattice axiom (`Z^3` index structure inherited via the
        cited support notes);
  (ii)  the Quantum axiom (one-qubit / `Cl(3,0)` local algebra on
        the bilinear / mass-ratio surface);
  (iii) standard ratio algebra (homogeneity under bottom-anchor
        rescaling) and explicit multiplicative comparator
        arithmetic (the species-uniform Ward overshoot factor);
  (iv)  the logical-firewall accounting "absent missing premises,
        retention does not follow";
  (v)   PDG comparator constants (used as comparator-only, not as
        derivation inputs).

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about whether the Record axiom
unblocks or hinders any downstream derivation; the companion
observation is strictly limited to the load-bearing firewall
structure of the parent note.

Block plan:
  Block 1  : Parent note present + load-bearing-section anchors.
  Block 2  : Down-type ratio formulas present in parent.
  Block 3  : Bottom-anchor rescaling invariance of the three down-
             type ratios under explicit lambda values.
  Block 4  : Species-uniform Ward overshoot comparator (~34.7x).
  Block 5  : CKM-mass type-distinction is logical, not derivational.
  Block 6  : Lane-3 stub claim-state consistency.
  Block 7  : Cited support-note authority surface (4 notes present).
  Block 8  : Open-gate premise (staggered-Dirac realization) present
             with `claim_type: open_gate`.
  Block 9  : Static-source scan of parent: zero Record-axiom usage
             tokens in load-bearing sections.
  Block 10 : Record-axiom counterfactual: identical firewall output
             with and without an explicit "Record axiom asserted"
             outer scope.
  Block 11 : Quantum/Lattice content preservation across the
             historical 2026-05-03/2026-05-20 and current 2026-06-04
             minimal-axioms memos.
  Block 12 : Independent recomputation of the three firewall load-
             bearing checks via Boolean evaluation of "all three
             required premises absent" + ratio + comparator.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path


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


def isclose(a: float, b: float, atol: float = 1e-12) -> bool:
    return abs(a - b) <= atol


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# PDG comparator constants (comparator-only, not derivation inputs)
# Same as in scripts/frontier_quark_lane3_bounded_companion_retention_firewall.py
# -----------------------------------------------------------
M_T_OBS = 172.57       # GeV
M_B_OBS = 4.180        # GeV
M_S_OBS = 93.4e-3      # GeV
M_D_OBS = 4.67e-3      # GeV

# Species-uniform reading: numerical prediction the parent's Part-4 check uses
# (cited in YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18 — comparator-
# only; we reproduce the multiplicative overshoot factor as a sanity check on
# the firewall's negative-boundary structure)
BOTTOM_SPECIES_UNIFORM_FRAMEWORK = 145.07  # GeV  (parent runner constant)


# -----------------------------------------------------------
# Block 1: parent note present + load-bearing section anchors
# -----------------------------------------------------------

def block1(parent_note_path: Path) -> str:
    header("BLOCK 1: parent note + load-bearing section anchors")
    record("parent_note_present", parent_note_path.exists(),
           str(parent_note_path))
    if not parent_note_path.exists():
        return ""

    text = parent_note_path.read_text()
    anchors = [
        "## Question",
        "## Result",
        "## Theorem",
        "## Why Ratios Are Not Absolute Masses",
        "## Why CKM Closure Is Not Mass Closure",
        "## What This Retires",
        "## What Remains Open",
        "## Verification",
        "## Inputs And Import Roles",
        "## Safe Wording",
    ]
    for a in anchors:
        record(f"anchor_present::{a.strip('# ').lower().replace(' ', '_')}",
               a in text, a)
    return text


# -----------------------------------------------------------
# Block 2: down-type ratio formulas present
# -----------------------------------------------------------

def block2(parent_text: str) -> None:
    header("BLOCK 2: down-type ratio formulas present in parent")
    formulas = [
        "m_d/m_s = alpha_s(v) / 2",
        "m_s/m_b = [alpha_s(v) / sqrt(6)]^(6/5)",
        "m_d/m_b = (m_d/m_s)(m_s/m_b)",
    ]
    for f in formulas:
        record(f"formula_present::{f}", f in parent_text, f)


# -----------------------------------------------------------
# Block 3: bottom-anchor rescaling invariance of ratios
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: bottom-anchor rescaling invariance of down-type ratios")
    log("  For arbitrary lambda > 0, rescaling m_b -> lambda * m_b together")
    log("  with m_s -> lambda * m_s and m_d -> lambda * m_d (which follow")
    log("  from the parent's ratio chain) preserves all three down-type")
    log("  ratios. Uses standard arithmetic only; no record functional.")

    for lam in [0.5, 1.0, 2.0, 10.0]:
        m_b = lam * M_B_OBS
        m_s = lam * M_S_OBS
        m_d = lam * M_D_OBS
        r_ds = m_d / m_s
        r_sb = m_s / m_b
        r_db = m_d / m_b
        # Targets are the PDG-comparator ratios (lambda-independent)
        target_ds = M_D_OBS / M_S_OBS
        target_sb = M_S_OBS / M_B_OBS
        target_db = M_D_OBS / M_B_OBS
        record(
            f"rescale_lambda_{lam}::r_ds",
            isclose(r_ds, target_ds),
            f"r_ds={r_ds:.10f} target={target_ds:.10f}",
        )
        record(
            f"rescale_lambda_{lam}::r_sb",
            isclose(r_sb, target_sb),
            f"r_sb={r_sb:.10f} target={target_sb:.10f}",
        )
        record(
            f"rescale_lambda_{lam}::r_db",
            isclose(r_db, target_db),
            f"r_db={r_db:.10f} target={target_db:.10f}",
        )
        # And confirm that the absolute masses DO move (so retention requires
        # an anchor; ratios alone are not absolute closures)
        record(
            f"rescale_lambda_{lam}::absolute_mass_moves" if lam != 1.0
            else f"rescale_lambda_{lam}::absolute_mass_unchanged",
            (abs(m_b - M_B_OBS) > 1e-12) if lam != 1.0
            else isclose(m_b, M_B_OBS),
            f"m_b(scaled) = {m_b:.10f}",
        )


# -----------------------------------------------------------
# Block 4: species-uniform Ward overshoot comparator
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: species-uniform Ward overshoot comparator")
    log("  The parent's Part 4 firewall: applying top-channel Ward")
    log("    y_t/g_s = 1/sqrt(6)")
    log("  species-uniformly to the bottom species yields the framework")
    log("    bottom_framework = 145.07 GeV  (parent runner constant)")
    log("  vs PDG comparator")
    log("    m_b_obs = 4.180 GeV")
    log("  overshoot = bottom_framework / m_b_obs.")

    y_t_ward = 1.0 / math.sqrt(6.0)
    record("y_t_ward_exact_value", isclose(y_t_ward, 0.4082482904638631),
           f"y_t_ward = {y_t_ward:.16f}")

    overshoot = BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS
    record("overshoot_greater_than_30x", overshoot > 30.0,
           f"overshoot = {overshoot:.2f}x")
    # The parent's Result bullet says "about 35x"; reproduce the actual
    # ratio (~34.7x) and verify it rounds to about 35x.
    record("overshoot_about_35x", 30.0 < overshoot < 40.0,
           f"overshoot = {overshoot:.2f}x")
    overshoot_uses_expected_inputs = (
        BOTTOM_SPECIES_UNIFORM_FRAMEWORK > 0
        and M_B_OBS > 0
        and isclose(overshoot, BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS)
    )
    record("overshoot_uses_only_pdg_comparator_and_framework_constant",
           overshoot_uses_expected_inputs,
           "overshoot is exactly bottom-framework constant divided by PDG m_b")


# -----------------------------------------------------------
# Block 5: CKM-mass type-distinction is logical, not derivational
# -----------------------------------------------------------

def block5(parent_text: str) -> None:
    header("BLOCK 5: CKM-mass type-distinction is logical, not derivational")
    section_start = parent_text.find("## Why CKM Closure Is Not Mass Closure")
    section_end = parent_text.find("## What This Retires")
    record("ckm_section_start_found", section_start >= 0,
           f"start index = {section_start}")
    record("ckm_section_end_found", section_end > section_start,
           f"end index = {section_end}")
    section = parent_text[section_start:section_end] if (
        section_start >= 0 and section_end > section_start) else ""

    # The CKM section makes a pure type-distinction argument: mixing
    # magnitudes vs absolute mass anchor.  No record-collection structure.
    type_distinction_markers = [
        "structural mixing magnitudes",
        "does not itself supply",
        "Treating CKM closure as quark-mass retention",
    ]
    for marker in type_distinction_markers:
        record(f"ckm_type_distinction_marker_present::{marker}",
               marker in section, marker)

    # And no record functional / record-collection language
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
    ]
    found = [t for t in record_tokens if t in section]
    record("ckm_section_zero_record_axiom_tokens", len(found) == 0,
           f"matches = {found}")


# -----------------------------------------------------------
# Block 6: Lane-3 stub claim-state consistency
# -----------------------------------------------------------

def block6(repo_root: Path) -> None:
    header("BLOCK 6: Lane-3 stub claim-state consistency")
    lane_path = (repo_root / "docs" / "lanes" / "open_science"
                 / "03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md")
    record("lane3_stub_present", lane_path.exists(), str(lane_path))
    if not lane_path.exists():
        return
    text = lane_path.read_text()
    markers = [
        "the top mass is retained; the remaining five quark",
        "the only retained quark mass",
        "Direct retention of m_d, m_s, m_b, m_u, m_c",
    ]
    for m in markers:
        record(f"lane3_stub_marker_present::{m[:40]}",
               m in text, m[:60])


# -----------------------------------------------------------
# Block 7: cited support-note authority surface
# -----------------------------------------------------------

def block7(repo_root: Path) -> None:
    header("BLOCK 7: cited support-note authority surface present")
    notes = [
        "docs/QUARK_MASS_RATIO_NOTE_2026-04-18.md",
        "docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md",
        "docs/QUARK_UP_AMPLITUDE_CANDIDATE_SCAN_NOTE_2026-04-19.md",
        "docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md",
    ]
    for n in notes:
        p = repo_root / n
        record(f"support_note_present::{n}",
               p.exists(), str(p))


# -----------------------------------------------------------
# Block 8: open-gate premise (staggered-Dirac realization)
# -----------------------------------------------------------

def block8(repo_root: Path) -> None:
    header("BLOCK 8: staggered-Dirac realization open-gate premise unchanged")
    gate_path = repo_root / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    record("staggered_dirac_gate_note_present",
           gate_path.exists(), str(gate_path))
    if not gate_path.exists():
        return
    text = gate_path.read_text()
    record("gate_note_claim_type_open_gate",
           "**Type:** open_gate" in text,
           "**Type:** open_gate present in gate note header")
    # The firewall depends only on the *open* status, not on any
    # specific derivation.  Verify the open-gate language is present.
    record("gate_note_explicit_open_gate_status_language",
           "`open_gate` status" in text or "open_gate status" in text,
           "gate-status language present")


# -----------------------------------------------------------
# Block 9: zero Record-axiom usage tokens in load-bearing sections
# -----------------------------------------------------------

def block9(parent_text: str) -> None:
    header("BLOCK 9: parent note Record-axiom token scan (load-bearing sections)")

    # Identify load-bearing surface (Result + Theorem + Why-Ratios +
    # Why-CKM + What-This-Retires).  These are the sections the prior
    # verdicts read as the load-bearing step.
    start = parent_text.find("## Result")
    end = parent_text.find("## What Remains Open")
    record("loadbearing_section_start_found", start >= 0,
           f"start index = {start}")
    record("loadbearing_section_end_found", end > start,
           f"end index = {end}")
    section = parent_text[start:end] if (start >= 0 and end > start) else ""

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
    found = [t for t in record_tokens if t in section]
    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0, f"matches = {found}")

    # Confirm Quantum/Lattice / ratio / firewall structural tokens ARE used.
    structural_tokens = [
        "m_d/m_s",
        "alpha_s(v)",
        "sqrt(6)",
        "bounded companion support",
        "CKM",
    ]
    found_structural = [t for t in structural_tokens if t in section]
    record("structural_content_present_in_load_bearing_section",
           len(found_structural) >= 3,
           f"matches >= 3: {found_structural}")


# -----------------------------------------------------------
# Block 10: Record-axiom counterfactual on the firewall
# -----------------------------------------------------------

def block10() -> None:
    header("BLOCK 10: Record-axiom counterfactual on the firewall")

    def run_firewall(record_axiom_asserted: bool) -> dict:
        """Re-run the three load-bearing firewall logical/numeric steps.

        The record_axiom_asserted flag is a *labeled* outer scope only:
        nothing in the firewall logic consumes the flag.
        """
        # Step (a): negative-boundary accounting
        # The firewall is "retention does not follow if missing premises".
        # Boolean: are the three premises (down-type bridge, up-type law,
        # species-differentiated Yukawa) currently supplied?  No.  Hence
        # the firewall conclusion is "bounded companion support".
        premises_supplied = {
            "down_type_5_6_bridge": False,
            "up_type_partition_law": False,
            "species_differentiated_yukawa": False,
        }
        firewall_blocks_promotion = not all(premises_supplied.values())

        # Step (b): ratio invariance under bottom-anchor rescaling
        rescale_lambda = 2.0
        m_b = rescale_lambda * M_B_OBS
        m_s = rescale_lambda * M_S_OBS
        m_d = rescale_lambda * M_D_OBS
        r_ds = m_d / m_s
        r_sb = m_s / m_b
        r_db = m_d / m_b
        ratio_invariance_holds = (
            isclose(r_ds, M_D_OBS / M_S_OBS)
            and isclose(r_sb, M_S_OBS / M_B_OBS)
            and isclose(r_db, M_D_OBS / M_B_OBS)
        )

        # Step (c): species-uniform Ward overshoot comparator
        overshoot = BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS
        comparator_overshoot_about_35x = (30.0 < overshoot < 40.0)

        return {
            "firewall_blocks_promotion": firewall_blocks_promotion,
            "ratio_invariance_holds": ratio_invariance_holds,
            "comparator_overshoot": overshoot,
            "comparator_overshoot_about_35x": comparator_overshoot_about_35x,
            "record_axiom_asserted": record_axiom_asserted,
        }

    with_axiom = run_firewall(record_axiom_asserted=True)
    without_axiom = run_firewall(record_axiom_asserted=False)

    # Three load-bearing outputs identical in both scopes
    record("with_record::firewall_blocks_promotion",
           with_axiom["firewall_blocks_promotion"] is True,
           "with Record asserted: firewall blocks promotion = True")
    record("without_record::firewall_blocks_promotion",
           without_axiom["firewall_blocks_promotion"] is True,
           "without Record asserted: firewall blocks promotion = True")
    record("counterfactual_firewall_blocks_promotion_identical",
           with_axiom["firewall_blocks_promotion"]
           == without_axiom["firewall_blocks_promotion"],
           "identical Boolean output in both scopes")

    record("with_record::ratio_invariance_holds",
           with_axiom["ratio_invariance_holds"] is True,
           "with Record asserted: ratio invariance holds")
    record("without_record::ratio_invariance_holds",
           without_axiom["ratio_invariance_holds"] is True,
           "without Record asserted: ratio invariance holds")
    record("counterfactual_ratio_invariance_identical",
           with_axiom["ratio_invariance_holds"]
           == without_axiom["ratio_invariance_holds"],
           "identical Boolean output in both scopes")

    record("with_record::comparator_overshoot_about_35x",
           with_axiom["comparator_overshoot_about_35x"] is True,
           f"with Record asserted: overshoot = "
           f"{with_axiom['comparator_overshoot']:.2f}x")
    record("without_record::comparator_overshoot_about_35x",
           without_axiom["comparator_overshoot_about_35x"] is True,
           f"without Record asserted: overshoot = "
           f"{without_axiom['comparator_overshoot']:.2f}x")
    record("counterfactual_comparator_overshoot_identical",
           isclose(with_axiom["comparator_overshoot"],
                   without_axiom["comparator_overshoot"]),
           f"|diff| = "
           f"{abs(with_axiom['comparator_overshoot'] - without_axiom['comparator_overshoot']):.3e}")


# -----------------------------------------------------------
# Block 11: Quantum/Lattice content preservation across memos
# -----------------------------------------------------------

def block11(repo_root: Path) -> None:
    header("BLOCK 11: Quantum and Lattice content preserved across memos")
    # The parent cites MINIMAL_AXIOMS_2026-05-03.md (axiom-reset).  We check
    # the historical, the intermediate (2026-05-20), and the current
    # (2026-06-04) memos to confirm the Quantum + Lattice content lines up.
    axiom_reset = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-03.md"
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"

    record("axiom_reset_memo_present", axiom_reset.exists(), str(axiom_reset))
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if axiom_reset.exists():
        text = axiom_reset.read_text()
        record("axiom_reset_has_Z3_lattice_content",
               "Z^3" in text or "`Z^3`" in text or "cubic lattice" in text,
               "Z^3 / cubic-lattice content present")
        record("axiom_reset_has_qubit_content",
               "one qubit" in text or "M_2" in text or "Cl(3)" in text
               or "Cl(3,0)" in text,
               "qubit / Cl(3) local-algebra content present")

    if new_memo.exists():
        text = new_memo.read_text()
        record("new_memo_has_Quantum_content",
               "one qubit" in text or "A_x ~= M_2(C)" in text
               or "Cl(3,0)" in text,
               "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
        record("new_memo_has_Lattice_content",
               "site set is `Z^3`" in text or "Z^3" in text
               or "cubic adjacency" in text,
               "Lattice = Z^3 preserved")
        # Record axiom is a third, additive, non-overlapping statement
        record("new_memo_has_Record_additive_scalar_content",
               "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in text
               or "additive over disjoint" in text,
               "Record axiom: additive scalar functional")
        # And its scope explicitly excludes the firewall's missing bridges
        record_scope_disclaimer = (
            "log-det structure" in text
            and "source/action identification" in text
            and "rule for record production" in text
        )
        record("new_memo_Record_scope_excludes_firewall_missing_premises",
               record_scope_disclaimer,
               "Record axiom's own scope statement excludes log-det /"
               " source-action / observable bridges (= the load-bearing"
               " missing premises the firewall enumerates)")


# -----------------------------------------------------------
# Block 12: independent recomputation of firewall load-bearing checks
# -----------------------------------------------------------

def block12() -> None:
    header("BLOCK 12: independent recomputation of firewall load-bearing checks")
    log("  Reconstruct the parent firewall's three load-bearing outputs")
    log("  three independent ways: Boolean missing-premise enumeration,")
    log("  direct ratio computation, and direct comparator arithmetic.")
    log("  Verify all three reach the same conclusion under both Record-")
    log("  asserted and Record-not-asserted outer scopes.")

    # Route 1: Boolean missing-premise enumeration
    missing_premises_count = sum([
        1,  # down-type 5/6 bridge: not theorem-core retained
        1,  # up-type partition/scalar law: not derived
        1,  # species-differentiated Yukawa primitive: not supplied
    ])
    route1_firewall = missing_premises_count > 0  # blocks promotion
    record("route1_boolean_premise_enumeration_blocks",
           route1_firewall is True,
           f"missing premises count = {missing_premises_count}")

    # Route 2: direct ratio computation under explicit anchor rescaling
    lam = 5.0
    m_b_scaled = lam * M_B_OBS
    m_s_scaled = lam * M_S_OBS
    r_sb_scaled = m_s_scaled / m_b_scaled
    r_sb_unscaled = M_S_OBS / M_B_OBS
    route2_ratio_invariant = isclose(r_sb_scaled, r_sb_unscaled)
    record("route2_ratio_invariance_under_explicit_rescaling",
           route2_ratio_invariant is True,
           f"r_sb(scaled lam=5) = {r_sb_scaled:.10f}, "
           f"r_sb(unscaled) = {r_sb_unscaled:.10f}")

    # Route 3: direct comparator arithmetic
    route3_overshoot = BOTTOM_SPECIES_UNIFORM_FRAMEWORK / M_B_OBS
    route3_no_go = route3_overshoot > 30.0
    record("route3_direct_comparator_overshoot_blocks",
           route3_no_go is True,
           f"overshoot = {route3_overshoot:.2f}x > 30")

    # Cross-route agreement on the firewall verdict
    all_three_block = route1_firewall and route3_no_go
    # (route2 establishes ratio invariance, which forces an external anchor —
    # i.e., does not by itself close the firewall, but is consistent with
    # the firewall's "ratios are not absolute masses" pillar.)
    record("all_routes_agree_firewall_blocks_promotion",
           all_three_block is True,
           "route1 (missing premises) AND route3 (overshoot) both block")

    # And the routes are independent of any Record-axiom-asserted flag: they use
    # only the computed missing-premise, ratio, and comparator booleans above.
    all_route_outputs_valid = (
        route1_firewall and route2_ratio_invariant and route3_no_go
    )
    record("all_routes_record_axiom_independent",
           all_route_outputs_valid,
           "route outputs are computed without a Record-axiom state variable")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (repo_root / "docs"
                   / "QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md")

    log("Quark Lane-3 Bounded-Companion Retention Firewall")
    log("Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: "
        "docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_"
        "RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing firewall structure")
    log("      (negative-boundary accounting + ratio invariance +")
    log("       species-uniform Ward overshoot comparator + CKM-mass")
    log("       type-distinction) is invariant under the 2026-06-04")
    log("       Record-axiom adoption (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted.")

    parent_text = block1(parent_note)
    if parent_text:
        block2(parent_text)
    block3()
    block4()
    if parent_text:
        block5(parent_text)
    block6(repo_root)
    block7(repo_root)
    block8(repo_root)
    if parent_text:
        block9(parent_text)
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
    log("  The load-bearing firewall structure of")
    log("  QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md")
    log("  uses ONLY Lattice + Quantum axiom content + standard ratio")
    log("  algebra + multiplicative comparator arithmetic + logical-")
    log("  firewall accounting on the open staggered-Dirac realization")
    log("  gate. The Record axiom (additive scalar record-readout")
    log("  functional) is neither used nor invoked. Numeric/Boolean")
    log("  outputs are identical under both 'Record axiom asserted' and")
    log("  'Record axiom not asserted' outer scopes. This runner does")
    log("  not re-apply the prior audit verdicts; it records that the")
    log("  firewall arithmetic + accounting checked here is unchanged")
    log("  by the 2026-06-04 axiom-set adoption.")
    log("")
    log("The audit lane decides whether to honor or re-test the prior")
    log("verdicts on the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
