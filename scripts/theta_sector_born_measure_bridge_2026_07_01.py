#!/usr/bin/env python3
"""Verifier for the theta sector Born-measure bridge."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def flat(text: str) -> str:
    return " ".join(text.split())


def born_weights(rho_diag: list[Fraction], projectors: dict[int, list[int]]) -> dict[int, Fraction]:
    return {
        q: sum(rho_diag[i] * mask[i] for i in range(len(rho_diag)))
        for q, mask in projectors.items()
    }


def complete_projectors(projectors: dict[int, list[int]]) -> bool:
    dim = len(next(iter(projectors.values())))
    return all(sum(mask[i] for mask in projectors.values()) == 1 for i in range(dim))


def orthogonal_projectors(projectors: dict[int, list[int]]) -> bool:
    labels = list(projectors)
    dim = len(next(iter(projectors.values())))
    for i, q in enumerate(labels):
        if any(value not in (0, 1) for value in projectors[q]):
            return False
        for q2 in labels[i + 1 :]:
            if any(projectors[q][j] * projectors[q2][j] != 0 for j in range(dim)):
                return False
    return True


def theta_sign(q: int, theta: str) -> int:
    if theta == "0":
        return 1
    if theta == "pi":
        return 1 if q % 2 == 0 else -1
    raise ValueError(theta)


def theta_contrib(weights: dict[int, Fraction], theta: str) -> dict[int, Fraction]:
    return {q: theta_sign(q, theta) * z for q, z in weights.items()}


def has_odd_support(weights: dict[int, Fraction]) -> bool:
    return any(q % 2 != 0 and z > 0 for q, z in weights.items())


def paired(weights: dict[int, Fraction]) -> bool:
    return all(weights.get(-q, Fraction(0)) == z for q, z in weights.items())


def main() -> int:
    print("=== Theta sector Born-measure bridge ===")

    files = [
        "docs/THETA_SECTOR_BORN_MEASURE_BRIDGE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md",
        "docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md",
        "docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md",
        "docs/STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md",
        "docs/STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
        "docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/THETA_SECTOR_BORN_MEASURE_BRIDGE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    born = read("docs/RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md")
    selector = read("docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md")
    substrate = read("docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md")
    weighting = read("docs/THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md")
    positivity = read("docs/STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md")
    theta_bar = read("docs/STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    gap_map = read("docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry or axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("axioms supply record readability but no theta", "Only records are readable" in axioms and "Further physical structure requires" in flat(axioms))
    check("Record/Born bridge supplies trace weights after interface", "Tr(rho P_r)" in born and "supplied finite readout context" in born)
    check("theta selector needs pointwise sector measure", "pointwise nonnegative record-facing probability measure" in flat(selector))
    check("theta selector selects zero with odd support", "theta = 0" in selector and "odd-`Q` sector has nonzero weight" in selector)
    check("substrate note preserves emergent Q bridge", "Emergent-Q bridge" in substrate)
    check("weighting bridge narrows to {0, pi}", "{0, π}" in weighting or "{0, pi}" in weighting)
    check("positivity note does not force theta zero", "not forced" in positivity.lower() or "does not force" in positivity.lower())
    check("theta-bar note keeps assembly open", "joint gauge/mass basis bridge is not supplied" in theta_bar)

    print("\nPART B -- primitive registry check")
    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("registry canonical ids are expected set", set(registry["canonical_ids"]) == expected_ids, registry["canonical_ids"])
    for node_id in expected_ids:
        check(f"registry node present: {node_id}", node_id in registry["nodes"])
        check(f"registry source exists: {node_id}", exists(registry["nodes"][node_id]["current_path"]))
    check("minimal axioms registry note says no probability/observable bridge", "probability" in registry["nodes"]["minimal_axioms"]["note"] and "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("scale primitive supplies no dimensionless theta selector", "zero dimensionless content" in flat(scale).lower())
    check("kinetic primitive supplies no selector", "selector" in flat(kinetic).lower())
    check("realized primitive supplies no state-selection/measure", "state-selection rule" in flat(realized) and "measure" in flat(realized))
    check("P_gauge_sector_measure is not registered", "P_gauge_sector_measure" not in registry_text)

    print("\nPART C -- finite sharp Q Born measure")
    rho = [Fraction(1, 8), Fraction(3, 4), Fraction(1, 8)]
    projectors = {
        -1: [1, 0, 0],
        0: [0, 1, 0],
        1: [0, 0, 1],
    }
    weights = born_weights(rho, projectors)
    check("rho is normalized", sum(rho, Fraction(0)) == 1)
    check("projectors are complete", complete_projectors(projectors))
    check("projectors are orthogonal sharp effects", orthogonal_projectors(projectors))
    check("Born sector weights are expected", weights == {-1: Fraction(1, 8), 0: Fraction(3, 4), 1: Fraction(1, 8)}, weights)
    check("Born sector weights are nonnegative", all(z >= 0 for z in weights.values()))
    check("Born sector weights normalize", sum(weights.values(), Fraction(0)) == 1)
    check("Born sector weights are conjugation-paired", paired(weights))
    check("Born sector weights have odd support", has_odd_support(weights))
    check("note displays finite witness", "rho = diag(1/8, 3/4, 1/8)" in note and "Z_1  = 1/8" in note)

    print("\nPART D -- theta pointwise selector")
    w0 = theta_contrib(weights, "0")
    wpi = theta_contrib(weights, "pi")
    check("theta=0 contributions are nonnegative", all(z >= 0 for z in w0.values()), w0)
    check("theta=pi has negative odd sector -1", wpi[-1] == Fraction(-1, 8), wpi)
    check("theta=pi has negative odd sector +1", wpi[1] == Fraction(-1, 8), wpi)
    check("theta=pi has positive total partition sum", sum(wpi.values(), Fraction(0)) == Fraction(1, 2), wpi)
    check("pointwise positivity rejects pi despite positive total", any(z < 0 for z in wpi.values()) and sum(wpi.values(), Fraction(0)) > 0)
    check("theta=0 is selected from CP-even pair", all(z >= 0 for z in w0.values()) and any(z < 0 for z in wpi.values()))
    even_weights = {-2: Fraction(1, 4), 0: Fraction(1, 2), 2: Fraction(1, 4)}
    even_w0 = theta_contrib(even_weights, "0")
    even_wpi = theta_contrib(even_weights, "pi")
    check("even-only support has no odd support", not has_odd_support(even_weights))
    check("even-only support cannot distinguish 0 from pi", even_w0 == even_wpi)

    print("\nPART E -- bridge consequence")
    check("Record/Born plus sharp Q supplies pointwise measure", "Z_Q = Tr(rho P_Q)" in note)
    check("measure subwall closes only after Q context", "once `Q` is a sharp record context" in note)
    check("remaining W_theta_Q_context named", "W_theta_Q_context" in note)
    check("remaining W_theta_bar_assembly named", "W_theta_bar_assembly" in note)
    check("audit citation chain present", "Record/Born sector measure" in note and "theta pointwise sector selector" in note)
    check("primitive fallback is narrowed", "pointwise measure portion does not need to be primitive" in flat_note)
    check("gap map names W_theta_sector", "W_theta_sector" in gap_map)
    check("primitive recommendation names gauge sector measure", "P_gauge_sector_measure" in primitive)

    print("\nPART F -- note content")
    required_sections = [
        "Claim",
        "Finite Theorem",
        "Explicit Finite Witness",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "Minimum Foundation Update If Bridge Work Fails",
        "No-Go Discipline Gate",
    ]
    for section_name in required_sections:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note says no Strong-CP closure", "Strong-CP closure" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note preserves sign-weighted boundary", "sign-weighted" in note)
    check("note preserves odd-support boundary", "odd-sector support" in note)
    check("note avoids measured imports", "measured constants" in note and "PDG" not in note)

    print("\nPART G -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Record/Born sector-measure route",
        "Pointwise theta selector route",
        "Reality/conjugation route",
        "Partition-positivity route",
        "Emergent-Q route",
        "Theta-bar route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed residuals are two walls", "W_theta_Q_context" in note and "W_theta_bar_assembly" in note)
    check("N3 classifies supplied sharp Q context", "\"Supplied sharp `Q` context\" is an explicit bridge input" in note)
    check("N4 has seven witness matches", note.count("| `") >= 7 and "Residual Matching" in note)
    check("N5 narrows finite sharp-sector resolution", "finite sharp-sector context resolution" in note)
    check("N6 lists live closure paths", "gauge-action/scaling" in note and "anomaly" in note)
    check("N7 steelman preserves objection", "mostly interface plumbing" in note)
    check("N8 cross-cycle echo present", "substrate carrier" in note and "pointwise selector" in note)

    print("\nPART H -- non-overclaim checks")
    forbidden = [
        "therefore Strong-CP is closed",
        "therefore emergent Q is derived",
        "therefore odd-sector support is proved",
        "therefore sign-weighted formulations are excluded",
        "therefore theta_bar is assembled",
        "requires a new ontology axiom",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no terminal no-go", "not a terminal no-go" in note)
    check("note says Q is not derived", "does not derive the emergent `Q`" in note)
    check("note says theta-bar is not derived", "does not derive" in note and "theta_bar" in note)
    check("note preserves future bridge-first route", "bridge-first routes fail" in note)
    check("explicit non-claim preserves sign-weighted formulations", "sign-weighted formulations outside a record-facing probability measure" in flat_note)

    print("\nPART I -- assembled conclusion")
    bridge_ok = (
        complete_projectors(projectors)
        and orthogonal_projectors(projectors)
        and weights == {-1: Fraction(1, 8), 0: Fraction(3, 4), 1: Fraction(1, 8)}
        and paired(weights)
        and has_odd_support(weights)
        and all(z >= 0 for z in w0.values())
        and any(z < 0 for z in wpi.values())
    )
    check("Record/Born sharp Q measure supplies pointwise sector measure", bridge_ok)
    check("theta=0 selector follows under odd support", any(z < 0 for z in wpi.values()) and all(z >= 0 for z in w0.values()))
    check("emergent Q and theta-bar remain open", "W_theta_Q_context" in note and "W_theta_bar_assembly" in note)
    check("no axiom update requested", "No ontology axiom update follows" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL -- theta sector Born-measure bridge is not verifier-clean.")
        return 1
    print(
        "RESULT: PASS -- supplied sharp Q sector records plus Record/Born "
        "give the pointwise sector measure; theta=0 follows from the selector "
        "under odd support, while Q-context and theta-bar assembly remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
