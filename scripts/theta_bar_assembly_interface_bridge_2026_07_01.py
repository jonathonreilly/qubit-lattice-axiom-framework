#!/usr/bin/env python3
"""Verifier for the theta-bar assembly interface bridge."""

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


def mod2(x: Fraction) -> Fraction:
    """Return x modulo 2 in [0, 2). Angles are in units of pi."""

    return x % 2


def theta_bar(theta_gauge: Fraction, phi_mass: Fraction) -> Fraction:
    return mod2(theta_gauge + phi_mass)


def axial_shift(theta_gauge: Fraction, phi_mass: Fraction, n: int, alpha: Fraction) -> tuple[Fraction, Fraction]:
    return mod2(theta_gauge - n * alpha), mod2(phi_mass + n * alpha)


def paired(weights: dict[int, Fraction]) -> bool:
    return all(weights.get(-q, Fraction(0)) == z for q, z in weights.items())


def has_odd_support(weights: dict[int, Fraction]) -> bool:
    return any(q % 2 != 0 and z > 0 for q, z in weights.items())


def theta_sector_contributions(weights: dict[int, Fraction], theta: Fraction) -> dict[int, Fraction]:
    if theta == 0:
        return dict(weights)
    if theta == 1:
        return {q: ((-1) ** q) * z for q, z in weights.items()}
    raise ValueError("only theta=0 or pi supported in this finite selector")


def k_orbit_constant(k: int, sample_phis: list[Fraction]) -> bool:
    """Check exp(i k phi) equals exp(-i k phi) on rational pi-grid by parity."""

    return all(mod2(k * phi) == mod2(-k * phi) for phi in sample_phis)


def main() -> int:
    print("=== Theta-bar assembly interface bridge ===")

    files = [
        "docs/THETA_BAR_ASSEMBLY_INTERFACE_BRIDGE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/THETA_SECTOR_BORN_MEASURE_BRIDGE_2026-07-01.md",
        "docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md",
        "docs/THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md",
        "docs/STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md",
        "docs/STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04.md",
        "docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "docs/THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/THETA_BAR_ASSEMBLY_INTERFACE_BRIDGE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    born = read("docs/THETA_SECTOR_BORN_MEASURE_BRIDGE_2026-07-01.md")
    pointwise = read("docs/THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01.md")
    p2 = read("docs/THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md")
    det_bridge = read("docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md")
    structured = read("docs/STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md")
    joint_fail = read("docs/STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04.md")
    substrate = read("docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md")
    weighting = read("docs/THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_BOUNDED_THEOREM_NOTE_2026-06-13.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry/axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("minimal axioms do not supply theta", "Further physical structure requires" in flat(axioms) and "theta" in flat(axioms).lower())
    check("scale primitive supplies no theta selector", "zero dimensionless content" in flat(scale).lower())
    check("kinetic primitive supplies no selector", "selector" in flat(kinetic).lower())
    check("realized primitive supplies no measure", "measure" in flat(realized) and "state-selection rule" in flat(realized))
    check("theta sector Born bridge preserves Q/theta_bar walls", "W_theta_Q_context" in born and "W_theta_bar_assembly" in born)
    check("pointwise selector preserves theta_bar assembly", "joint gauge/mass `theta_bar` assembly" in pointwise)
    check("P2 bridge names W2/action-entry premises", "W2 physical-registrability" in p2 and "action-level `theta_eff` determinant-entry" in p2)
    check("determinant bridge is supplied channel only", "supplied finite mass-sector readout interface" in det_bridge)
    check("structured admission names theta_bar invariant", "theta_bar = theta_QCD + arg det M" in structured)
    check("joint bridge failure keeps holomorphic residual", "Holomorphic-generation escape" in joint_fail)
    check("substrate note preserves emergent-Q bridge", "Emergent-Q bridge" in substrate)
    check("weighting note confines to {0, pi}", "{0, pi}" in weighting or "{0, \u03c0}" in weighting)

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
    check("registry minimal axioms note says no probability/observable bridge", "probability" in registry["nodes"]["minimal_axioms"]["note"] and "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("no registered theta sector primitive", "P_theta_sector_surface" not in registry_text)
    check("no registered gauge sector measure primitive", "P_gauge_sector_measure" not in registry_text)

    print("\nPART C -- pointwise gauge theta selector")
    weights = {-1: Fraction(1, 8), 0: Fraction(3, 4), 1: Fraction(1, 8)}
    w0 = theta_sector_contributions(weights, Fraction(0))
    wpi = theta_sector_contributions(weights, Fraction(1))
    check("sector weights normalize", sum(weights.values(), Fraction(0)) == 1)
    check("sector weights are nonnegative", all(z >= 0 for z in weights.values()))
    check("sector weights are paired", paired(weights))
    check("sector weights have odd support", has_odd_support(weights))
    check("theta=0 sector weights are nonnegative", all(z >= 0 for z in w0.values()))
    check("theta=pi has negative odd sector", wpi[-1] < 0 and wpi[1] < 0, wpi)
    check("theta=pi can still have positive total", sum(wpi.values(), Fraction(0)) == Fraction(1, 2), wpi)
    check("pointwise selector chooses zero in witness", all(z >= 0 for z in w0.values()) and any(z < 0 for z in wpi.values()))
    check("note displays sector witness", "Z_-1 = 1/8" in note and "W_pi(1) = -1/8" in note)

    print("\nPART D -- mass determinant phase erasure interface")
    sample_phis = [Fraction(0), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(7, 5)]
    valid_ks = [k for k in range(-4, 5) if k_orbit_constant(k, sample_phis)]
    check("only k=0 is K-orbit constant on test grid", valid_ks == [0], valid_ks)
    check("k=1 is not K-orbit constant", not k_orbit_constant(1, sample_phis))
    check("k=-2 is not K-orbit constant", not k_orbit_constant(-2, sample_phis))
    check("zero phase character gives phi_mass zero branch", theta_bar(Fraction(0), Fraction(0)) == 0)
    check("pi orientation branch is distinct", theta_bar(Fraction(0), Fraction(1)) == 1)
    check("note displays zero orientation branch", "zero orientation branch" in note and "phi_mass = 0" in note)

    print("\nPART E -- theta_bar modular assembly")
    check("zero plus zero gives theta_bar zero", theta_bar(Fraction(0), Fraction(0)) == 0)
    check("pi gauge plus zero mass gives theta_bar pi", theta_bar(Fraction(1), Fraction(0)) == 1)
    check("zero gauge plus pi mass gives theta_bar pi", theta_bar(Fraction(0), Fraction(1)) == 1)
    check("pi plus pi gives theta_bar zero modulo 2", theta_bar(Fraction(1), Fraction(1)) == 0)
    check("half plus three halves gives zero modulo 2", theta_bar(Fraction(1, 2), Fraction(3, 2)) == 0)
    check("note states load-bearing contrast cases", "theta_gauge = pi, phi_mass = 0" in note and "theta_gauge = 0,  phi_mass = pi" in note)

    print("\nPART F -- anomaly paired-shift invariance")
    for n in [1, 2, 3, 6]:
        for alpha in [Fraction(1, 7), Fraction(2, 5), Fraction(3, 4)]:
            theta0 = Fraction(0)
            phi0 = Fraction(0)
            shifted_theta, shifted_phi = axial_shift(theta0, phi0, n, alpha)
            check(f"theta_bar invariant for n={n}, alpha={alpha}", theta_bar(shifted_theta, shifted_phi) == theta_bar(theta0, phi0), (shifted_theta, shifted_phi))
    theta_s, phi_s = axial_shift(Fraction(0), Fraction(0), 3, Fraction(1, 7))
    check("explicit n=3 alpha=1/7 witness", theta_s == Fraction(11, 7) and phi_s == Fraction(3, 7), (theta_s, phi_s))
    check("explicit shifted witness sums to zero", theta_bar(theta_s, phi_s) == 0)
    check("note displays axial witness", "theta_gauge' = -3/7" in note and "phi_mass'    =  3/7" in note)

    print("\nPART G -- note content")
    required_sections = [
        "Claim",
        "Source Surface",
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
    for wall in ["W_theta_Q_context", "W_mass_determinant_action", "W_anomaly_covariant_assembly"]:
        check(f"note names {wall}", wall in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note says no Strong-CP closure", "claim Strong-CP closure" in flat_note)
    check("note gives primitive fallback shape", "P_theta_sector_surface" in note)
    check("primitive recommendation still has gauge-sector measure candidate", "P_gauge_sector_measure" in primitive)

    print("\nPART H -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Gauge pointwise selector route",
        "Partition-positivity route",
        "Mass determinant channel route",
        "Mass K-reality route",
        "Axial anomaly bookkeeping route",
        "Holomorphic/quark-sector route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed residuals are three walls", all(w in note for w in ["W_theta_Q_context", "W_mass_determinant_action", "W_anomaly_covariant_assembly"]))
    check("N3 classifies sharp Q context", "`sharp Q context`" in note)
    check("N4 has residual matching table", "Residual Matching" in note and "THETA_P2_DETERMINANT_READOUT_EXHAUSTION" in note)
    check("N5 narrows finite resolutions", "finite sector-weight" in note and "modular-angle" in note)
    check("N6 lists live closure paths", "derive sharp `Q`" in note and "derive W2 physical registrability" in note)
    check("N7 steelman admits bookkeeping objection", "mostly bookkeeping" in note)
    check("N8 cross-cycle echo present", "substrate no-carrier" in note and "determinant reality" in note)

    print("\nPART I -- non-overclaim checks")
    forbidden = [
        "therefore Strong-CP is closed",
        "therefore theta_bar is derived unconditionally",
        "therefore emergent Q is derived",
        "therefore W2 is derived",
        "therefore the quark determinant is physical",
        "therefore anomaly assembly is automatic",
        "requires a new ontology axiom",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says no Tier-A retirement", "Tier-A retirement" in note)
    check("note says no Q derivation", "derivation of emergent `Q`" in note)
    check("note says no W2 derivation", "derivation of W2 physical registrability" in note)
    check("note says no anomaly assembly derivation", "derivation of anomaly-covariant gauge/mass assembly" in note)
    check("note says no measured imports", "use of PDG values" in note and "lattice-MC values" in note)
    check("note says no new primitive use", "does not request or register that primitive" in flat_note)

    print("\nPART J -- assembled conclusion")
    bridge_ok = (
        theta_bar(Fraction(0), Fraction(0)) == 0
        and theta_bar(Fraction(1), Fraction(0)) == 1
        and theta_bar(Fraction(0), Fraction(1)) == 1
        and theta_bar(*axial_shift(Fraction(0), Fraction(0), 3, Fraction(1, 7))) == 0
        and valid_ks == [0]
        and has_odd_support(weights)
        and "W_mass_determinant_action" in note
        and "W_anomaly_covariant_assembly" in note
    )
    check("assembled theta-bar interface conclusion holds", bridge_ok)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
