#!/usr/bin/env python3
"""Verifier for approved primitive axiom-absorption current-surface no-go."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "APPROVED_PRIMITIVE_AXIOM_ABSORPTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_NODES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
FRONT_DOOR = DOCS / "repo" / "FRONT_DOOR_STATUS.md"
POLICY = DOCS / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC_SUPPORT = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("Approved primitive axiom-absorption current-surface no-go")
    print("=" * 88)

    paths = [
        NOTE,
        MINIMAL,
        AXIOM_NODES,
        TIER_A,
        FRONT_DOOR,
        POLICY,
        REGISTRY,
        SCALE,
        KINETIC,
        REALIZED,
        KINETIC_SUPPORT,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimal_flat = flat(texts[MINIMAL])
    front_flat = flat(texts[FRONT_DOOR])
    policy_flat = flat(texts[POLICY])
    registry_flat = flat(texts[REGISTRY])
    scale_flat = flat(texts[SCALE])
    kinetic_flat = flat(texts[KINETIC])
    realized_flat = flat(texts[REALIZED])
    kinetic_support_flat = flat(texts[KINETIC_SUPPORT])
    nodes = json.loads(texts[AXIOM_NODES])
    tier = json.loads(texts[TIER_A])

    section("A - source presence and registry state")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    expected_ids = [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    check("axiom premise registry has exactly current axiom plus three primitive ids", nodes["canonical_ids"] == expected_ids, nodes["canonical_ids"])
    for pid in expected_ids:
        check(f"registry node exists: {pid}", pid in nodes["nodes"])
    check("front door lists scale reference primitive", "`scale_reference_primitive` | approved primitive" in front_flat)
    check("front door lists kinetic isotropy primitive", "`kinetic_isotropy_primitive` | approved primitive" in front_flat)
    check("front door lists realized state primitive", "`realized_state_primitive` | approved primitive" in front_flat)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check("Tier-A canonical ids remain AC and theta", tier["canonical_ids"] == [
        "staggered_dirac_realization_gate_note_2026-05-03",
        "strong_cp_theta_zero_note",
    ], tier["canonical_ids"])
    check(
        "tier registry says approved primitives are separate from Tier-A",
        "Framework axioms and approved primitives" in registry_flat
        and "Does **not** treat approved primitives as Tier-A admissions" in registry_flat,
    )
    check("policy separates approved primitives from Tier-A", "Framework primitives are distinct from Tier-A admitted derivation targets" in policy_flat)

    section("B - note metadata and no-edit boundaries")
    check("new note declares no_go type", "**Type:** no_go" in note)
    check("new note declares no_go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    for phrase in [
        "No approved primitive is retired by the current axiom text alone.",
        "No primitive is retired.",
        "No axiom or primitive registry is edited.",
        "No Tier-A admission is retired or reclassified.",
        "No audit status or effective status is changed.",
        "approved, non-bounding primitive nodes, not Tier-A rows",
    ]:
        check(f"note preserves boundary: {phrase[:60]}", phrase in note_flat)

    section("C - scale reference is not axiom-absorbed")
    scale_not_absorbed = all(
        phrase in scale_flat
        for phrase in [
            "exactly one dimensionful reference",
            "carries zero dimensionless content",
            "A dimensionful scale cannot be derived from purely dimensionless structure",
            "does not assert `a/l_P = 1`",
        ]
    )
    minimal_keeps_scale_outside = "scale-reference primitive" in minimal_flat and "natural unit equals the Planck length" in minimal_flat
    check("scale note marks the ruler dimensionful and non-derivable from dimensionless structure", scale_not_absorbed)
    check("minimal axiom memo keeps scale/natural-unit issue outside axiom content", minimal_keeps_scale_outside)
    check("note classifies scale as no axiom overlap", "| `scale_reference_primitive` | None." in note)
    check("scale primitive remains a separate registry node", nodes["nodes"]["scale_reference_primitive"]["current_path"] == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")

    section("D - kinetic isotropy is not axiom-absorbed")
    minimal_withholds_dynamics = all(
        phrase in minimal_flat
        for phrase in [
            "Admissibility is not a dynamics axiom",
            "does not choose a Hamiltonian or transfer operator",
            "transition probabilities or weights",
            "time metric",
        ]
    )
    kinetic_declares_ratio = "c_t = c_s" in kinetic_flat and "c_t / c_s" in kinetic_flat
    kinetic_not_derived = "does **not** fix the kinetic isotropy" in kinetic_flat or "does not fix the kinetic isotropy" in kinetic_flat
    support_nonfixation = "listed current structures do not fix `xi`" in kinetic_support_flat
    check("minimal axioms withhold dynamics/time-metric content", minimal_withholds_dynamics)
    check("kinetic primitive declares c_t=c_s / c_t/c_s ratio", kinetic_declares_ratio)
    check("kinetic primitive note says baseline does not fix the ratio", kinetic_not_derived)
    check("kinetic support note preserves non-fixation boundary", support_nonfixation)
    check("note classifies kinetic as outside axiom memo", "It does not supply `c_t = c_s`." in note)
    check("kinetic primitive remains a separate registry node", nodes["nodes"]["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")

    section("E - realized-state has state-type overlap but not full absorption")
    state_type_in_axioms = "A state is a configuration of records." in minimal_flat and "A law privileges no states." in minimal_flat
    minimal_withholds_state_selection = all(
        phrase in minimal_flat
        for phrase in [
            "A law privileges no states",
            "probability rules",
            "context selection",
        ]
    )
    realized_slot = all(
        phrase in realized_flat
        for phrase in [
            "The laws do not pick the state; the world does",
            "Derivations may evaluate at the realized state, pointwise",
            "not a state-selection rule",
            "no averaging over alternatives",
            "A realized state cannot be derived from state-blind laws",
        ]
    )
    registry_realized_boundary = "the axioms select no state" in nodes["nodes"]["realized_state_primitive"]["note"]
    check("minimal axioms now define state type and no-state-privilege law boundary", state_type_in_axioms)
    check("minimal axioms still withhold state-selection/probability/boundary content", minimal_withholds_state_selection)
    check("realized primitive declares actual-history pointwise slot and no selection content", realized_slot)
    check("machine registry says realized primitive is the no-state-selection slot", registry_realized_boundary)
    check("note records realized-state as partially overlapping only", "only partially overlapping case" in note_flat)
    check("realized-state primitive remains a separate registry node", nodes["nodes"]["realized_state_primitive"]["current_path"] == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")

    section("F - aggregate conclusion and overclaim guards")
    classifications = {
        "scale_reference_primitive": "not_absorbed",
        "kinetic_isotropy_primitive": "not_absorbed",
        "realized_state_primitive": "partial_state_type_overlap_not_absorbed",
    }
    check("aggregate classification has no absorbed primitive", all(value != "absorbed" for value in classifications.values()), classifications)
    check("realized-state is the only partial-overlap classification", classifications["realized_state_primitive"].startswith("partial") and classifications["scale_reference_primitive"] == "not_absorbed" and classifications["kinetic_isotropy_primitive"] == "not_absorbed", classifications)
    banned = [
        "The primitive is retired",
        "A primitive is retired",
        "The primitive registry is edited",
        "A Tier-A admission is retired",
        "The audit status is changed",
        "The effective status is changed",
        "scale_reference_primitive is absorbed",
        "kinetic_isotropy_primitive is absorbed",
        "realized_state_primitive is absorbed",
        "approved primitive cleanup reduces the current Tier-A count",
    ]
    for phrase in banned:
        check(f"banned overclaim absent: {phrase}", phrase not in note_flat)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
