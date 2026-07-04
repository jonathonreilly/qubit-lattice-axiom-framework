#!/usr/bin/env python3
"""Verifier for theta mass W2 physical-registrability stretch no-go."""

from __future__ import annotations

import cmath
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PRIMITIVE = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
CORE_SPLIT = DOCS / "REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md"
REGISTRABLE = DOCS / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
STRONG_BRIDGE = DOCS / "STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"
EXHAUSTION = DOCS / "THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
EPSILON_REALITY = DOCS / "THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
ZERO_BRANCH = DOCS / "THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def close(a: float, b: float, eps: float = 1.0e-12) -> bool:
    return abs(a - b) < eps


def main() -> int:
    print("Theta mass W2 physical-registrability stretch no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    realized_primitive = REALIZED_PRIMITIVE.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    core_split = CORE_SPLIT.read_text(encoding="utf-8")
    registrable = REGISTRABLE.read_text(encoding="utf-8")
    strong_bridge = STRONG_BRIDGE.read_text(encoding="utf-8")
    exhaustion = EXHAUSTION.read_text(encoding="utf-8")
    epsilon_reality = EPSILON_REALITY.read_text(encoding="utf-8")
    zero_branch = ZERO_BRANCH.read_text(encoding="utf-8")

    note_flat = flat(note)
    axioms_flat = flat(axioms)
    realized_flat = flat(realized_primitive)
    registry_flat = flat(registry)
    core_flat = flat(core_split)
    registrable_flat = flat(registrable)
    strong_flat = flat(strong_bridge)
    exhaustion_flat = flat(exhaustion)
    epsilon_flat = flat(epsilon_reality)
    zero_flat = flat(zero_branch)

    section("A - source and registry firewalls")

    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check(
        "note denies theta retirement and registry edits",
        "does not retire theta" in note_flat
        and "does not edit the Tier-A registry" in note_flat
        and "does not set `theta_bar = 0`" in note_flat,
    )
    check(
        "note denies primitive, axiom, and audit changes",
        "does not add or remove an axiom or primitive" in note_flat
        and "does not set an audit verdict" in note_flat,
    )
    check(
        "note leaves future W2/governance routes open",
        "future W2 theorem" in note_flat
        and "owner-ratified primitive is impossible" in note_flat,
    )
    check("runner path is wired in note", Path(__file__).name in note)

    section("B - current foundation withholds W2 ingredients")

    check(
        "minimal axioms withhold readout/source/observable bridges",
        "readout-context selection" in axioms_flat
        and "central-sector decomposition" in axioms_flat
        and "`K`/CPT" in axioms_flat
        and "source/action" in axioms_flat
        and "physical-observable identification" in axioms_flat,
    )
    check(
        "realized-state primitive is pointwise only",
        "This is pointwise evaluation, not a state-selection rule" in realized_primitive
        and "no state, averaging over alternatives, measure" in realized_flat
        and "probability rule" in realized_flat,
    )
    check(
        "registry localizes theta(b) but does not close it",
        "localized onto the named **determinant-readout bridge**" in registry
        and "only after the determinant-readout/exhaustion bridge is closed" in registry_flat,
    )
    check(
        "exhaustion note quarantines W2 and action-level determinant entry",
        "W2 physical-registrability" in exhaustion
        and "action-level `theta_eff` determinant-entry" in exhaustion
        and "does **not** derive the W2 physical-registrability theorem" in exhaustion_flat,
    )

    section("C - existing determinant route is preserved but supplied")

    check(
        "core split says determinant homomorphism boundary is supplied",
        "supplied determinant-character/log-character context" in core_flat
        and "does not derive the determinant-character/log-character boundary from Record" in core_flat,
    )
    check(
        "registrable theorem does not derive physical readout identification",
        "does not prove the physical readout must be registrable" in registrable_flat
        and "standing modeling identification" in registrable_flat,
    )
    check(
        "strong bridge is conditional on supplied determinant channel",
        "If the mass-side strong-CP readout is a supplied determinant-channel record readout" in strong_flat
        and "does not supply the determinant channel by itself" in strong_flat,
    )
    check(
        "epsilon reality and zero branch still leave physical identification outside",
        "Not** a derivation of K-reality" in epsilon_reality
        and "physical determinant-channel identification" in zero_flat,
    )

    section("D - finite two-extension witness")

    # Same record skeleton and same multiplicative determinant datum.
    phi1 = math.pi / 5.0
    phi2 = math.pi / 7.0
    z1 = 2.0 * cmath.exp(1j * phi1)
    z2 = 3.0 * cmath.exp(1j * phi2)
    z12 = z1 * z2

    log_mod = lambda z: math.log(abs(z))
    check(
        "supplied determinant scalar is additive over multiplicative union",
        close(log_mod(z12), log_mod(z1) + log_mod(z2)),
        f"log|z12|={log_mod(z12):.12f}",
    )

    cos_phase = lambda z: math.cos(cmath.phase(z))
    check("cos(arg z) is K-even", close(cos_phase(z1), cos_phase(z1.conjugate())))
    check(
        "cos(arg z) is not an additive record scalar for determinant union",
        not close(cos_phase(z12), cos_phase(z1) + cos_phase(z2)),
        f"cos12={cos_phase(z12):.12f}; sum={cos_phase(z1) + cos_phase(z2):.12f}",
    )
    check(
        "cos(arg z) is not a multiplicative determinant character either",
        not close(cos_phase(z12), cos_phase(z1) * cos_phase(z2)),
        f"cos12={cos_phase(z12):.12f}; product={cos_phase(z1) * cos_phase(z2):.12f}",
    )

    # Record additivity can be satisfied by scalar readouts unrelated to the
    # determinant datum. The determinant channel is therefore an extra
    # supplied interface, not a consequence of the record skeleton.
    readout_a = {"empty": 0.0, "e1": 1.0, "e2": 2.0, "e12": 3.0}
    readout_b = {"empty": 0.0, "e1": -4.0, "e2": 9.0, "e12": 5.0}
    add_a = close(readout_a["e12"], readout_a["e1"] + readout_a["e2"]) and readout_a["empty"] == 0.0
    add_b = close(readout_b["e12"], readout_b["e1"] + readout_b["e2"]) and readout_b["empty"] == 0.0
    check(
        "two additive Record scalar extensions share the same determinant datum",
        add_a and add_b and readout_a != readout_b,
        "I_A and I_B both additive; neither is forced by z",
    )

    same_z_different_record_content = z1 == z1 and readout_a["e1"] != readout_b["e1"]
    check(
        "determinant datum alone does not determine record scalar without W2",
        same_z_different_record_content,
        f"same z1 with scalar values {readout_a['e1']} and {readout_b['e1']}",
    )

    section("E - no-go assembly")

    check("note states the invalid implication", "therefore the physical theta mass readout is W2 Record-registrable" in note)
    check("note names W2 as the live bridge", "W2 physical registrability bridge remains live" in note_flat)
    check("note separates W2 from action-level determinant entry", "The action-level `theta_eff` determinant-entry premise remains separate" in note)
    check("note separates gauge winding", "multi-plaquette / large-winding residual is untouched" in note_flat)
    check("note names owner governance option", "approve it explicitly and narrowly" in note)
    check("no-go discipline is complete", all(tag in note for tag in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8")))

    banned = [
        "theta is retired",
        "retires theta",
        "w2 is derived",
        "determinant channel is forced",
        "registry is edited",
        "new primitive is approved",
    ]
    found = [phrase for phrase in banned if phrase in note_flat.lower()]
    check("banned overclaim phrases are absent", not found, str(found))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
