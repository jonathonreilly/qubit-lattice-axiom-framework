#!/usr/bin/env python3
"""Verifier for the theta G1 kinetic-isotropy 4D scaffold support split."""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G1_KINETIC_ISOTROPY_4D_SCAFFOLD_EXACT_SUPPORT_SPLIT_NOTE_2026-07-04.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
BLOCK37 = DOCS / "THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
BLOCK38 = DOCS / "THETA_G1_DEFECT_SUPPRESSION_SUPPLIED_PENALTY_EXACT_SUPPORT_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


SOURCE_ROWS = {
    "minimal": "minimal_axioms",
    "kinetic": "kinetic_isotropy_primitive",
    "block37": "theta_g1_4d_carrier_supply_current_surface_no_go_note_2026-07-04",
    "block38": "theta_g1_defect_suppression_supplied_penalty_exact_support_note_2026-07-04",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
}


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 96)
    print(title)
    print("=" * 96)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row(claim_id: str) -> dict:
    row = json.loads(read(LEDGER))["rows"].get(claim_id)
    if row is None:
        raise AssertionError(f"missing ledger row {claim_id}")
    return row


def cell_orientation_count(dim: int, degree: int) -> int:
    if degree > dim:
        return 0
    return len(list(itertools.combinations(range(dim), degree)))


def complementary_plane_pairs(dim: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    planes = list(itertools.combinations(range(dim), 2))
    pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for a, b in itertools.combinations(planes, 2):
        if len(set(a) | set(b)) == 4:
            pairs.append((a, b))
    return pairs


def cup_2_2_local_nonzero(plane_a: tuple[int, int], plane_b: tuple[int, int], target: tuple[int, int, int, int]) -> int:
    """Local oriented cubical cup sign for ordered complementary planes."""
    if set(plane_a) & set(plane_b):
        return 0
    if set(plane_a) | set(plane_b) != set(target):
        return 0
    order = list(plane_a + plane_b)
    inversions = 0
    target_pos = {axis: idx for idx, axis in enumerate(target)}
    mapped = [target_pos[a] for a in order]
    for i, j in itertools.combinations(range(len(mapped)), 2):
        if mapped[i] > mapped[j]:
            inversions += 1
    return -1 if inversions % 2 else 1


def main() -> int:
    print("theta G1 kinetic-isotropy 4D scaffold exact-support verifier")

    paths = [NOTE, KINETIC, MINIMAL, PREMISES, TIER_A, LEDGER, REGISTRY, BLOCK37, BLOCK38]
    texts = {path: read(path) for path in paths}
    flats = {path: flat(text) for path, text in texts.items()}
    note = texts[NOTE]
    note_flat = flats[NOTE]

    section("A. source presence, metadata, and firewall")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    check("note has Type bounded_theorem", "**Type:** bounded_theorem" in note)
    check("note has Claim type bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note declares exact-support scaffold status", "exact-support source-side split for the local 4D regulator scaffold only" in note_flat)
    check("runner path is wired", Path(__file__).name in note)
    for phrase in [
        "This note does not retire theta",
        "does not set `theta_bar = 0`",
        "does not edit any Tier-A registry",
        "does not claim that the current framework derives the physical 4D gauge carrier",
    ]:
        check(f"scope boundary present: {phrase[:60]}", phrase in note_flat)
    for banned in [
        "theta is retired",
        "theta_bar = 0 is derived",
        "the physical 4D gauge carrier is derived",
        "compact topology is supplied",
        "branch cochains are supplied",
        "sector/readout registration is supplied",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note_flat)

    section("B. premise and Tier-A registry state")
    premises = json.loads(read(PREMISES))
    check("kinetic primitive is approved premise node", "kinetic_isotropy_primitive" in premises["canonical_ids"])
    check("kinetic current path is expected note", premises["nodes"]["kinetic_isotropy_primitive"]["current_path"] == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger_row(claim_id)
        check(f"{label} ledger row resolves", row.get("claim_id") == claim_id)
    tier = json.loads(read(TIER_A))
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition unchanged",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )

    section("C. source-boundary checks")
    for phrase in [
        "Euclidean regulator block `Z^3 x Z_tau`",
        "hypercubic-symmetric",
        "c_t = c_s",
        "not a fourth spatial dimension",
        "does not supply any dimensionless dynamical quantity",
    ]:
        check(f"kinetic primitive phrase present: {phrase[:58]}", phrase in flats[KINETIC])
    for phrase in [
        "source/action and physical-observable identification",
        "readout-context selection",
        "do not close, import, or rename the framework's downstream open",
    ]:
        check(f"minimal axiom withholding present: {phrase[:58]}", phrase in flats[MINIMAL])
    for phrase in [
        "does not supply the 4D cubical/gauge carrier",
        "Theta's gauge-side winding account therefore remains live",
    ]:
        check(f"Block37 no-go preserved: {phrase[:58]}", phrase in flats[BLOCK37])
    for phrase in [
        "No physical 4D carrier is supplied",
        "No current-surface defect penalty",
    ]:
        check(f"Block38 boundary preserved: {phrase[:58]}", phrase in flats[BLOCK38])

    section("D. finite local cell arithmetic")
    check("3D has three edge directions", cell_orientation_count(3, 1) == 3)
    check("3D has three plaquette orientations", cell_orientation_count(3, 2) == 3)
    check("3D has no 4-cell orientation", cell_orientation_count(3, 4) == 0)
    check("4D scaffold has four edge directions", cell_orientation_count(4, 1) == 4)
    check("4D scaffold has six plaquette orientations", cell_orientation_count(4, 2) == 6)
    check("4D scaffold has four 3-cell orientations", cell_orientation_count(4, 3) == 4)
    check("4D scaffold has one 4-cell orientation", cell_orientation_count(4, 4) == 1)
    pairs3 = complementary_plane_pairs(3)
    pairs4 = complementary_plane_pairs(4)
    check("3D has no complementary plane pairs spanning four directions", len(pairs3) == 0, pairs3)
    check("4D has three complementary plane pairs", len(pairs4) == 3, pairs4)
    target = (0, 1, 2, 3)
    expected_pairs = {((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))}
    check("4D complementary pairs match intersection-form pairs", set(pairs4) == expected_pairs, pairs4)
    signs = {pair: cup_2_2_local_nonzero(pair[0], pair[1], target) for pair in pairs4}
    check("all complementary 2-cup-2 signs are nonzero", all(abs(s) == 1 for s in signs.values()), signs)
    check("non-complementary spatial pair has zero 4D cup target", cup_2_2_local_nonzero((0, 1), (0, 2), target) == 0)
    check("note records local scaffold support", "local 4D regulator scaffold" in note)
    check("note records 3D C4 absence", "C^4=0" in note)

    section("E. open-content boundary")
    for phrase in [
        "compact `T^4` topology or boundary conditions",
        "gauge links, branch 2-cochains, or integer shift variables",
        "non-exact `H^2` sectors",
        "the closedness law `dn=0`",
        "physical record/readout registration",
        "the `F cup F` phase coefficient",
    ]:
        check(f"open content explicitly withheld: {phrase[:58]}", phrase in note)
    for phrase in [
        "Theta is not retired",
        "No physical 4D carrier theorem is supplied",
        "No G1 closedness or defect-suppression theorem is supplied",
        "No G3 phase source",
    ]:
        check(f"non-claim present: {phrase[:58]}", phrase in note)
    for phrase in [
        "Gauge branch carrier theorem on the scaffold",
        "Compact/topological sector theorem",
        "G1 closedness or defect suppression",
    ]:
        check(f"remaining route present: {phrase}", phrase in note)

    total = PASS + FAIL
    print("\n" + "=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL} CHECKS={total}")
    print("=" * 96)
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
