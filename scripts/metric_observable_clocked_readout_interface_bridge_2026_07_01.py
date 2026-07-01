#!/usr/bin/env python3
"""Verifier for the metric/observable clocked readout interface bridge."""

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


def strictly_increasing(values: list[Fraction]) -> bool:
    return all(b > a for a, b in zip(values, values[1:]))


def durations(tau: list[Fraction]) -> list[Fraction]:
    return [b - a for a, b in zip(tau, tau[1:])]


def total_rate(total: Fraction, tau: list[Fraction]) -> Fraction:
    return total / (tau[-1] - tau[0])


def dot_metric(metric: list[list[Fraction]], u: list[Fraction], v: list[Fraction]) -> Fraction:
    return sum(metric[i][j] * u[i] * v[j] for i in range(len(u)) for j in range(len(v)))


def scale_metric(metric: list[list[Fraction]], omega: Fraction) -> list[list[Fraction]]:
    return [[omega * omega * entry for entry in row] for row in metric]


def convert_power(coefficient: Fraction, power_of_a_inverse: int, mpl: Fraction) -> Fraction:
    """Convert coefficient * a^{-p} using a^{-1}=M_Pl."""

    return coefficient * (mpl**power_of_a_inverse)


def source_ratio(derivatives: list[Fraction], i: int, j: int) -> Fraction:
    return derivatives[i] / derivatives[j]


def main() -> int:
    print("=== Metric/observable clocked readout interface bridge ===")

    files = [
        "docs/METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md",
        "docs/RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md",
        "docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md",
        "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md",
        "docs/OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md",
        "docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md",
        "docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md",
    ]
    for rel in files:
        check(f"{rel} exists", exists(rel))

    note = read("docs/METRIC_OBSERVABLE_CLOCKED_READOUT_INTERFACE_BRIDGE_2026-07-01.md")
    axioms = read("docs/MINIMAL_AXIOMS_2026-06-29.md")
    registry_text = read("docs/audit/data/axiom_premise_nodes.json")
    registry = json.loads(registry_text)
    scale = read("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    kinetic = read("docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md")
    realized = read("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    clock = read("docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md")
    clock_gate = read("docs/RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md")
    metric = read("docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md")
    scalar_map = read("docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md")
    source_response = read("docs/OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md")
    source_action = read("docs/SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md")
    primitive = read("docs/MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01.md")
    gap_map = read("docs/OPERATIONAL_PREMISE_GAP_MAP_2026-07-01.md")
    flat_note = flat(note)

    print("\nPART A -- source boundary")
    check("note declares independent audit authority", "independent audit lane only" in note)
    check("note declares no registry/axiom edit", "does not set an audit verdict, edit registries, register primitives, change axioms" in flat_note)
    check("axioms supply scalar record readout", "scalar readout `I` is additive" in axioms)
    check("axioms require bridges for further structure", "Further physical structure requires derivation" in flat(axioms))
    check("scale primitive says units conversion only", "units conversion" in scale and "zero dimensionless content" in flat(scale).lower())
    check("kinetic primitive does not supply dynamics", "no dimensionless dynamical content" in flat(kinetic).lower())
    check("realized primitive does not supply state selection", "state-selection rule" in flat(realized))
    check("clock interface says supplied tau gives rates", "supplied clock map tau" in clock)
    check("clock interface says counts alone do not determine rates", "does not determine a clock rate" in flat(clock))
    check("clock gate separates rate normalization", "Rate and clock remain separate" in clock_gate)
    check("metric note isolates conformal factor", "conformal factor" in metric and "clock-rate" in metric)
    check("record scalar map no-go preserves scalar selector", "does not derive the branch-to-scalar map" in scalar_map)
    check("source-response theorem cancels c", "Source-response ratio invariance" in source_response)
    check("source/action factorization preserves physical source selector", "W_physical_source" in source_action)

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
    check("minimal axioms registry note says no observable bridge", "physical observable bridge" in registry["nodes"]["minimal_axioms"]["note"])
    check("minimal axioms registry note says no normalization", "normalization" in registry["nodes"]["minimal_axioms"]["note"])
    check("scale primitive does not supply observable selector", "readout bridge" in flat(scale) and "empirical fit" in flat(scale))
    check("kinetic primitive does not supply readout bridge", "readout bridge" in kinetic)
    check("realized primitive does not supply measure", "measure" in realized and "weighting" in realized)
    check("P_metric_observable is not registered", "P_metric_observable" not in registry_text)

    print("\nPART C -- clocked record rates")
    record_values = [Fraction(2), Fraction(1), Fraction(3), Fraction(4)]
    total_i = sum(record_values, Fraction(0))
    tau_uniform = [Fraction(0), Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    tau_slow = [Fraction(0), Fraction(2), Fraction(4), Fraction(6), Fraction(8)]
    tau_accel = [Fraction(0), Fraction(1), Fraction(3), Fraction(6), Fraction(10)]
    for name, tau in [("uniform", tau_uniform), ("slow", tau_slow), ("accel", tau_accel)]:
        check(f"{name} clock is strictly increasing", strictly_increasing(tau), tau)
        check(f"{name} durations are positive", all(dt > 0 for dt in durations(tau)), durations(tau))
    check("record scalar total is 10", total_i == 10, total_i)
    check("uniform event rate is 1", total_rate(Fraction(len(record_values)), tau_uniform) == 1)
    check("slow event rate is 1/2", total_rate(Fraction(len(record_values)), tau_slow) == Fraction(1, 2))
    check("accel event rate is 2/5", total_rate(Fraction(len(record_values)), tau_accel) == Fraction(2, 5))
    check("uniform scalar rate is 5/2", total_rate(total_i, tau_uniform) == Fraction(5, 2))
    check("slow scalar rate is 5/4", total_rate(total_i, tau_slow) == Fraction(5, 4))
    check("accel scalar rate is 1", total_rate(total_i, tau_accel) == 1)
    check("same records support inequivalent rates", len({total_rate(total_i, t) for t in [tau_uniform, tau_slow, tau_accel]}) == 3)
    check("note displays clock witness", "tau_uniform" in note and "10/8" in note and "10/10" in note)

    print("\nPART D -- finite region densities")
    region_values = [Fraction(2), Fraction(0), Fraction(5), Fraction(1)]
    region_size = Fraction(len(region_values))
    region_total = sum(region_values, Fraction(0))
    density = region_total / region_size
    disjoint_a = [Fraction(2), Fraction(0)]
    disjoint_b = [Fraction(5), Fraction(1)]
    check("region total is additive", sum(disjoint_a, Fraction(0)) + sum(disjoint_b, Fraction(0)) == region_total)
    check("region density is total over site count", density == Fraction(2), density)
    check("empty scalar readout is zero by axiom note", "I(empty)=0" in axioms)
    check("density is not a selector", "rho_I(R)" in note and "not a dimensionless prediction" in note)

    print("\nPART E -- conformal metric split")
    g_hat = [
        [Fraction(-1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]
    omega = Fraction(3)
    g_scaled = scale_metric(g_hat, omega)
    null = [Fraction(1), Fraction(1), Fraction(0), Fraction(0)]
    time = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    space = [Fraction(0), Fraction(1), Fraction(0), Fraction(0)]
    check("null vector is null in conformal representative", dot_metric(g_hat, null, null) == 0)
    check("null vector remains null after scaling", dot_metric(g_scaled, null, null) == 0)
    check("timelike interval scales by omega^2", dot_metric(g_scaled, time, time) == omega * omega * dot_metric(g_hat, time, time))
    check("spacelike interval scales by omega^2", dot_metric(g_scaled, space, space) == omega * omega * dot_metric(g_hat, space, space))
    check("scaled metric is not equal to unscaled when omega != 1", g_scaled != g_hat)
    check("null cone unchanged but metric scale changed", dot_metric(g_scaled, null, null) == dot_metric(g_hat, null, null) == 0 and dot_metric(g_scaled, time, time) != dot_metric(g_hat, time, time))
    check("note displays conformal witness", "g_hat = diag(-1, 1, 1, 1)" in note and "Omega^2" in note)

    print("\nPART F -- scale reference unit conversion")
    mpl = Fraction(7)
    check("dimensionless coefficient unchanged at power 0", convert_power(Fraction(5), 0, mpl) == 5)
    check("one inverse-a power multiplies by M_Pl", convert_power(Fraction(2), 1, mpl) == 14)
    check("three inverse-a powers multiply by M_Pl^3", convert_power(Fraction(1, 2), 3, mpl) == Fraction(343, 2))
    ratio_before = Fraction(6, 3)
    ratio_after = convert_power(Fraction(6), 2, mpl) / convert_power(Fraction(3), 2, mpl)
    check("same-dimension ratios cancel scale reference", ratio_before == ratio_after)
    check("scale conversion creates no dimensionless selector", ratio_after == 2)
    check("note says scale reference is units only", "This is a unit conversion" in note)

    print("\nPART G -- source-response scalar-unit cancellation")
    w_derivatives = [Fraction(2), Fraction(5), Fraction(-3)]
    for c in [Fraction(1), Fraction(2), Fraction(-4), Fraction(3, 5)]:
        f_derivatives = [c * d for d in w_derivatives]
        check(f"source ratio 0/1 cancels c={c}", source_ratio(f_derivatives, 0, 1) == source_ratio(w_derivatives, 0, 1))
        check(f"source ratio 2/1 cancels c={c}", source_ratio(f_derivatives, 2, 1) == source_ratio(w_derivatives, 2, 1))
    positive_c = Fraction(3)
    negative_c = Fraction(-3)
    check("positive scalar preserves derivative sign", positive_c * w_derivatives[0] > 0)
    check("negative scalar flips derivative sign", negative_c * w_derivatives[0] < 0)
    check("absolute derivative changes with scalar unit", positive_c * w_derivatives[0] != w_derivatives[0])
    check("note states absolute readout still needs unit", "absolute measured readout still needs the physical scalar unit" in note)

    print("\nPART H -- note content")
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
    check("note names W_metric_observable", "W_metric_observable" in note)
    check("note names W_metric_clock", "W_metric_clock" in note)
    check("note names W_observable_readout", "W_observable_readout" in note)
    check("note says no ontology axiom update follows", "No ontology axiom update follows" in note)
    check("note preserves P_metric_observable fallback", "P_metric_observable" in note)
    check("gap map names W_metric_observable", "W_metric_observable" in gap_map)
    check("primitive recommendation names P_metric_observable", "P_metric_observable" in primitive)

    print("\nPART I -- no-go discipline N1-N8")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", f"### {item}" in note)
    routes = [
        "Clocked-record route",
        "Record-count route",
        "Conformal-class route",
        "Scale-reference route",
        "Record scalar route",
        "Source-response route",
        "New primitive route",
    ]
    for route in routes:
        check(f"N1 route present: {route}", route in note)
    check("N2 collapsed residuals are two walls", "W_metric_clock" in note and "W_observable_readout" in note)
    check("N3 classifies supplied clock map", "`supplied clock map`" in note)
    check("N4 has residual matching table", "Residual Matching" in note and "POST_RECORD_CLOCK_RATE_INTERFACE" in note)
    check("N5 narrows tested resolutions", "finite record-stream level" in note and "finite conformal-rescaling level" in note)
    check("N6 lists live closure paths", "derive the physical clock/conformal factor" in note and "derive the physical scalar observable map" in note)
    check("N7 steelman preserves action-principle objection", "true physical action principle" in note)
    check("N8 cross-cycle echo present", "counts are not a clock" in note and "conformal class is not the full metric" in note)

    print("\nPART J -- non-overclaim checks")
    forbidden = [
        "therefore the physical clock is derived",
        "therefore the conformal factor is derived",
        "therefore measured observables are derived",
        "therefore source/action is closed",
        "therefore record occurrence is closed",
        "requires a new ontology axiom",
    ]
    for phrase in forbidden:
        check(f"note avoids overclaim phrase: {phrase}", phrase not in note)
    check("note says not a terminal no-go", "not a terminal no-go" in note)
    check("note says no record occurrence closure", "record occurrence" in note and "This note does not claim" in note)
    check("note says no source direction closure", "physical source direction" in note)
    check("note says no measured imports are used", "use of PDG values" in note and "lattice-MC values" in note)
    check("note says no new primitive use", "does not register the primitive" in flat_note)
    check("note says finite algebra is exact after selectors", "once those selectors are supplied" in flat_note)

    print("\nPART K -- assembled conclusion")
    bridge_ok = (
        len({total_rate(total_i, t) for t in [tau_uniform, tau_slow, tau_accel]}) == 3
        and dot_metric(g_hat, null, null) == 0
        and dot_metric(g_scaled, null, null) == 0
        and dot_metric(g_scaled, time, time) != dot_metric(g_hat, time, time)
        and ratio_before == ratio_after
        and source_ratio([Fraction(2) * d for d in w_derivatives], 0, 1)
        == source_ratio(w_derivatives, 0, 1)
        and "W_metric_clock" in note
        and "W_observable_readout" in note
    )
    check("assembled bridge conclusion holds", bridge_ok)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
