"""Runner for the AC_phi_lambda retirement-basis re-match and claim-surface
audit (2026-07-06).

Post-landing verification, all mechanical:

  M1  registry state: live Tier-A count 0; AC + theta preserved under
      retired_derivation_targets; owner-governed registry carries exactly the
      one AC node with exactly the two adopted atom ids, the recorded
      no-value boundary, and the audited retirement surface; theta is NOT an
      owner-governed premise.
  M2  basis grades: every row of the audited decomposition basis reads
      retained-grade in the live ledger.
  M3  atom-match witnesses: the adoption note's Candidate 1/2 texts name the
      audited survivors; the basis notes carry the matching survivor and
      declared-premise language; the species note carries the
      nothing-further-survives sentence.
  M4  boundary witnesses: comparator labeling (exactness residual open, never
      thresholded) and the custody structure/value split are present.
  M5  claim-surface sweep: every existing direct dependent of the retired
      gate row that mentions the values (r = 1/2 / 2/9) also carries
      admission/conditionality vocabulary (note-level lexical guard).
  M6  cross-admission separation: theta retired by retained derivation,
      absent from owner-governed ids; its source row remains retained-grade.

No check passes by literal stipulation. Expected: PASS=N FAIL=0.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
OWNER_GOV = ROOT / "docs" / "audit" / "data" / "owner_governed_premise_nodes.json"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
GRAPH = ROOT / "docs" / "audit" / "data" / "citation_graph.json"
ADOPTION = DOCS / "TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md"

GATE_ID = "staggered_dirac_realization_gate_note_2026-05-03"
THETA_ID = "strong_cp_theta_zero_note"

BASIS_ROWS = [
    GATE_ID,
    "acphilambda_occupancy_selection_realized_state_reduction_note_2026-06-11",
    "koide_orbit_occupancy_independence_and_premise_candidate_note_2026-06-09",
    "acphilambda_r_eta_value_face_registered_angle_functional_exactness_relocation_note_2026-07-05",
    "acphilambda_r_eta_readout_identification_narrowing_bounded_theorem_note_2026-06-11",
    "acphilambda_r_eta_w2_registrability_context_bridge_note_2026-06-18",
    "acphilambda_species_bridge_realized_state_decomposition_note_2026-06-11",
    "acphilambda_hw_complement_reading_registration_equivalence_bounded_theorem_note_2026-06-12",
    "koide_delta_eta_density_readout_chain_bounded_theorem_note_2026-06-09",
    "charged_lepton_koide_value_full_chain_of_custody_2026-06-02",
    "record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06",
    "staggered_dirac_substep4_labeling_no_go_note_2026-05-17",
    "staggered_dirac_gate_ac_phi_lambda_labeling_convention_accepted_premise_bridge_bounded_note_2026-05-26",
    "staggered_dirac_substep4_amin_joint_c3_automorphism_selector_invariance_bridge_narrow_theorem_note_2026-07-05",
    "staggered_dirac_common_hw1_bz_corner_carrier_identification_bridge_narrow_theorem_note_2026-07-05",
    "koide_aps_eta_topological_robustness_bounded_theorem_note_2026-07-02",
]

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}

PASS = 0
FAIL = 0


def check(name: str, ok, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("=== AC_phi_lambda retirement-basis re-match + claim-surface audit ===\n")

    # ------------------------------------------------------------------ M1
    print("[M1] registry state\n")
    tier_a = json.loads(TIER_A.read_text(encoding="utf-8"))
    check("live Tier-A count is 0", tier_a.get("genuine_admitted_input_count") == 0)
    check("canonical_ids empty and derivation_targets empty",
          tier_a.get("canonical_ids") == [] and tier_a.get("derivation_targets") == {})
    retired = tier_a.get("retired_derivation_targets", {})
    check("AC and theta preserved under retired_derivation_targets",
          GATE_ID in retired and THETA_ID in retired)

    gov = json.loads(OWNER_GOV.read_text(encoding="utf-8"))
    check("owner-governed registry carries exactly one canonical id (the AC gate id)",
          gov.get("canonical_ids") == [GATE_ID])
    node = gov.get("nodes", {}).get(GATE_ID, {})
    check("the adopted residual candidates are exactly the two AC atoms",
          node.get("adopted_residual_candidates")
          == ["ac_orbit_occupancy_statistical_grain_premise",
              "ac_reta_hclass_hunit_readout_premise"])
    check("the recorded boundary carries the no-value sentence verbatim",
          "It supplies no value of r, delta, charged-lepton mass, mixing angle,"
          in flat(node.get("boundary", "")))
    check("the retirement surface records the audited gate landing",
          "audited_clean / retained_bounded" in node.get("retirement_surface", ""))
    check("theta is NOT an owner-governed premise (registry-level separation)",
          THETA_ID not in gov.get("canonical_ids", []))

    # ------------------------------------------------------------------ M2
    print("\n[M2] audited basis grades (live ledger)\n")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger["rows"] if isinstance(ledger, dict) and "rows" in ledger else ledger
    row_list = rows if isinstance(rows, list) else list(rows.values())
    eff = {r.get("claim_id"): r.get("effective_status", "?") for r in row_list}
    note_path = {r.get("claim_id"): r.get("note_path") for r in row_list}
    bad = [(b, eff.get(b, "MISSING")) for b in BASIS_ROWS
           if eff.get(b, "MISSING") not in RETAINED_GRADE]
    check(f"all {len(BASIS_ROWS)} basis rows are retained-grade",
          not bad, detail=str(bad) if bad else "")

    # ------------------------------------------------------------------ M3
    print("\n[M3] atom-match witnesses\n")
    adoption = flat(ADOPTION.read_text(encoding="utf-8"))
    check("Candidate 1 adopts the AC(i) measure-side grain (verbatim witness)",
          "the matter-action occupancy grain needed to discharge the surviving AC(i) measure-side realization binary"
          in adoption)
    check("Candidate 2 adopts the h-class/h-unit identity-read license (verbatim witness)",
          "the fixed-locus density class h, identity-read in h-units" in adoption)
    occupancy = flat((DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md").read_text(encoding="utf-8"))
    check("occupancy note carries the measure/realization-binary survivor language",
          "realization" in occupancy and "binary" in occupancy)
    delta_chain = flat((DOCS / "KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md").read_text(encoding="utf-8"))
    check("delta-eta chain declares the R-eta premise as supplied, not derived",
          "supplied, not derived" in delta_chain)
    value_face = flat((DOCS / "ACPHILAMBDA_R_ETA_VALUE_FACE_REGISTERED_ANGLE_FUNCTIONAL_EXACTNESS_RELOCATION_NOTE_2026-07-05.md").read_text(encoding="utf-8"))
    check("value-face note carries the registered-angle functional claim",
          "functional" in value_face and "registered" in value_face)
    species = flat((DOCS / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md").read_text(encoding="utf-8"))
    check("species note: nothing further survives in sub-admission (iii) (verbatim witness)",
          "No admitted content beyond named, already-tracked items survives in sub-admission (iii)"
          in species)

    # ------------------------------------------------------------------ M4
    print("\n[M4] boundary witnesses\n")
    check("value-face note labels the PDG comparison a comparator (exactness residual open)",
          "comparator" in value_face)
    custody = flat((DOCS / "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md").read_text(encoding="utf-8"))
    check("custody capstone carries the structure/value split (value modulo the named input)",
          "modulo" in custody and "structure derived" in custody.lower())

    # ------------------------------------------------------------------ M5
    print("\n[M5] claim-surface sweep over the retired gate row's dependents\n")
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    edges = graph.get("edges", graph)
    dependents = set()
    if isinstance(edges, list):
        for e in edges:
            src = e.get("from") or e.get("source")
            dst = e.get("to") or e.get("target")
            if dst == GATE_ID:
                dependents.add(src)
    else:
        for src, dsts in edges.items():
            if GATE_ID in dsts:
                dependents.add(src)
    check("dependent set is substantial (>= 50 direct dependents)",
          len(dependents) >= 50, detail=f"{len(dependents)} dependents")

    value_pat = re.compile(r"r\s*=\s*1/2|2/9")
    markers = ["ac_phi_lambda", "ac_φλ", "admitted", "modulo", "conditional",
               "premise", "adopted", "registered", "tier-a", "tier_a"]
    checked = 0
    missing_path = 0
    flagged: list[str] = []
    for dep in sorted(dependents):
        p = note_path.get(dep)
        fp = (ROOT / p) if p else None
        if fp is None or not fp.exists():
            missing_path += 1
            continue
        text = flat(fp.read_text(encoding="utf-8", errors="replace")).lower()
        checked += 1
        if value_pat.search(text) and not any(m in text for m in markers):
            flagged.append(dep)
    check("every checked dependent mentioning the values also carries "
          "admission/conditionality vocabulary (zero flagged)",
          not flagged,
          detail=f"checked={checked}, no-path={missing_path}, flagged={flagged}")
    check("sweep coverage: at least 45 dependent notes read from disk",
          checked >= 45, detail=f"checked={checked}")

    # ------------------------------------------------------------------ M6
    print("\n[M6] cross-admission separation (theta)\n")
    check("theta source row remains retained-grade in the live ledger",
          eff.get(THETA_ID) in RETAINED_GRADE, detail=str(eff.get(THETA_ID)))
    check("adoption note records the theta disposition (approval context only; "
          "retained-derivation retirement untouched)",
          "approval context only" in adoption
          and "does not resurrect theta as an owner-governed premise" in adoption)

    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
