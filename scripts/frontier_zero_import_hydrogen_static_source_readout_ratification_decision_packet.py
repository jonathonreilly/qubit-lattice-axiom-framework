#!/usr/bin/env python3
"""Verifier for the static-source readout ratification packet and no-go.

This runner checks that the readout handoff is explicit, that current support
surfaces are not over-spent as retained readout, and that downstream hydrogen
claims remain blocked.
"""

from __future__ import annotations

from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
THREE_GATE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md"
NR_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NR_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
NR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md"
RYDBERG = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
I1_BRIDGE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
I1_HYGIENE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
I1_NATIVE = ROOT / "docs" / "I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md"
I1_QUADRATIC = ROOT / "docs" / "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md"
GREEN_KERNEL = ROOT / "docs" / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md"
RP_NOTE = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
KUBO_NOTE = ROOT / "docs" / "LINEAR_RESPONSE_TRUE_KUBO_NOTE.md"
I1_RUNNER = ROOT / "scripts" / "static_source_readout_i1_accepted_premise_runner.py"
I1_NATIVE_RUNNER = ROOT / "scripts" / "i1_static_readout_is_native_field_integration_2026_06_06.py"
I1_QUADRATIC_RUNNER = ROOT / "scripts" / "i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


READOUT_INPUTS = {
    "STATIC_SOURCE_READOUT_TEXT_LOCK",
    "NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF",
    "SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF",
    "LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF",
    "UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF",
    "NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

THREE_GATE_INPUTS = {
    "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
    "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
    "HARTREE_SCALE_MAPPING_RATIFIED",
}

NR_COULOMB_INPUTS = {
    "STATIC_SOURCE_NR_COULOMB_TEXT_LOCK",
    "SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED",
    "COULOMB_KERNEL_ASYMPTOTIC_RATIFIED",
    "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
    "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
    "HARTREE_SCALE_MAPPING_RATIFIED",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_readout(inputs: set[str]) -> bool:
    return READOUT_INPUTS <= inputs


def closes_three_gate(inputs: set[str]) -> bool:
    return THREE_GATE_INPUTS <= inputs


def closes_nr_coulomb(inputs: set[str]) -> bool:
    return NR_COULOMB_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        CURRENT,
        GOAL,
        THREE_GATE,
        NR_PACKET,
        NR_ASSEMBLY,
        NR_CURRENT,
        RYDBERG,
        I1_BRIDGE,
        I1_HYGIENE,
        I1_NATIVE,
        I1_QUADRATIC,
        GREEN_KERNEL,
        RP_NOTE,
        KUBO_NOTE,
        I1_RUNNER,
        I1_NATIVE_RUNNER,
        I1_QUADRATIC_RUNNER,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    current = read(CURRENT)
    note_flat = flat(note)
    current_flat = flat(current)

    section("Required decision and no-go content")
    required_note_phrases = [
        "Static-Source Readout Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "STATIC_SOURCE_READOUT_TEXT_LOCK",
        "NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF",
        "SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF",
        "LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF",
        "UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF",
        "NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eight contract inputs",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
        "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md",
        "I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md",
        "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
        "LINEAR_RESPONSE_TRUE_KUBO_NOTE.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5006` static-source I1 hygiene companion | open, clean",
        "Primitive Registry Check",
        "static_source_readout_primitive",
        "energy_readout_primitive",
        "unit_electromagnetic_source_primitive",
        "Distance To Hydrogen",
        "Explicit Non-Claims",
    ]
    for phrase in required_note_phrases:
        audit.check(f"decision phrase present: {phrase}", flat(phrase) in note_flat)

    required_current_phrases = [
        "Static-Source Readout Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "the current retained, primitive, and open-PR surfaces do not supply",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "STATIC_SOURCE_READOUT_TEXT_LOCK",
        "NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF",
        "SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF",
        "LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF",
        "UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF",
        "NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM",
        "No-Go Discipline Gate",
        "OPEN POSITIVE ROUTE",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_current_phrases:
        audit.check(f"current-surface phrase present: {phrase}", flat(phrase) in current_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in current)

    section("Decision predicate checks")
    full_readout = set(READOUT_INPUTS)
    audit.check("full readout contract accepts readout handoff", closes_readout(full_readout))
    for missing in sorted(READOUT_INPUTS):
        reduced = set(READOUT_INPUTS)
        reduced.remove(missing)
        audit.check(f"readout handoff fails without {missing}", not closes_readout(reduced))
    accepted_readout_subsets = [subset for subset in all_subsets(READOUT_INPUTS) if closes_readout(subset)]
    audit.check("only full readout subset closes handoff", accepted_readout_subsets == [full_readout])
    audit.check(
        "readout handoff alone does not close three-gate target",
        not closes_three_gate({"STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED"}),
    )
    audit.check(
        "readout plus one-body without Hartree does not close three-gate target",
        not closes_three_gate({"STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED", "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED"}),
    )
    audit.check("full three-gate model predicate closes", closes_three_gate(set(THREE_GATE_INPUTS)))
    audit.check(
        "readout handoff alone does not close parent NR Coulomb",
        not closes_nr_coulomb({"STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED"}),
    )

    section("Finite readout arithmetic checks")
    for c_value in [1.0, 4.0 / 3.0]:
        for g_bare in [0.5, 1.0, 2.0]:
            alpha = g_bare * g_bare / (4.0 * math.pi)
            r = 7.0
            direct = -c_value * g_bare * g_bare / (4.0 * math.pi * r)
            via_alpha = -c_value * alpha / r
            audit.check(f"I1 alpha substitution C={c_value} g={g_bare}", abs(direct - via_alpha) < 1e-15)
    for g in [0.6, 1.0, 1.4]:
        g_kernel = 0.03125
        source_product = 1.0
        cross = -g * g * source_product * g_kernel
        audit.check(f"complete-square cross term scales as -g^2 G for g={g}", cross < 0 and abs(cross / (-g_kernel) - g * g) < 1e-15)
    audit.check("unit source coefficient differs from SU3 fundamental Casimir", abs(1.0 - (4.0 / 3.0)) > 0.1)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    three_gate = read(THREE_GATE)
    nr_packet = read(NR_PACKET)
    nr_assembly = read(NR_ASSEMBLY)
    nr_current = read(NR_CURRENT)
    rydberg = read(RYDBERG)
    i1_bridge = read(I1_BRIDGE)
    i1_hygiene = read(I1_HYGIENE)
    i1_native = read(I1_NATIVE)
    i1_quadratic = read(I1_QUADRATIC)
    green_kernel = read(GREEN_KERNEL)
    rp_note = read(RP_NOTE)
    kubo_note = read(KUBO_NOTE)
    i1_runner = read(I1_RUNNER)
    i1_native_runner = read(I1_NATIVE_RUNNER)
    i1_quadratic_runner = read(I1_QUADRATIC_RUNNER)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()

    for container_name, container in [
        ("goal packet", goal),
        ("three-gate target bundle", three_gate),
        ("NR Coulomb parent packet", nr_packet),
        ("NR Coulomb assembly", nr_assembly),
        ("NR Coulomb current no-go", nr_current),
        ("static-source Rydberg discriminator", rydberg),
    ]:
        audit.check(f"{container_name} references readout decision packet", NOTE.name in container)
        audit.check(f"{container_name} references readout current no-go", CURRENT.name in container)

    audit.check("I1 bridge registers accepted premise", "accepted-premise packet entry" in i1_bridge and "not derived in this bridge" in i1_bridge)
    audit.check("I1 bridge states what it does not close", "What this bridge does **not** close" in i1_bridge)
    audit.check("I1 hygiene keeps no status promotion", "does not promote status" in i1_hygiene and "substance-vs-grade separation" in i1_hygiene)
    audit.check("I1 native relocation keeps residuals explicit", "RELOCATES, does not eliminate" in i1_native and "general energy-readout bridge remains open" in i1_native)
    audit.check("I1 native names source-coupling residual", "source-coupling normalization" in i1_native)
    audit.check("I1 quadratic bridge is supplied-action scoped", "source-normalized leading quadratic action" in i1_quadratic and "does not derive the physical source-coupling normalization" in i1_quadratic)
    audit.check("I1 runner is accepted-premise scoped", "accepted-premise" in i1_runner)
    audit.check("I1 native runner preserves residuals", "residual after relocation" in i1_native_runner and "source-coupling normalization" in i1_native_runner)
    i1_quadratic_runner_flat = flat(i1_quadratic_runner)
    audit.check(
        "I1 quadratic runner preserves supplied-action boundary",
        "supplied source-normalized leading quadratic action" in i1_quadratic_runner_flat
        and "does not derive the physical" in i1_quadratic_runner_flat,
    )
    audit.check("green kernel names framework-local coefficient", "framework-local large-separation normalization" in green_kernel and "1 / (4 pi |r|)" in green_kernel)
    audit.check("RP note exists for transfer-matrix context", "transfer" in rp_note.lower() and "positivity" in rp_note.lower())
    audit.check("Kubo note exists for linear-response context", "linear response" in kubo_note.lower())

    nodes = registry["nodes"]
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal and "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes readout/coupling content", "zero dimensionless content" in scale and "readout bridge" in scale)
    audit.check("kinetic primitive excludes dynamics/couplings", "dynamics" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes values and state-selection", "state-selection rule" in realized and "or value is supplied" in realized)
    for absent in [
        "static_source_readout_primitive",
        "source_action_primitive",
        "energy_readout_primitive",
        "source_normalization_primitive",
        "unit_electromagnetic_source_primitive",
        "static_source_nr_coulomb_primitive",
        "static_source_rydberg_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered readout shortcut: {absent}", absent not in registry_text)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation or ratification of `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.",
        "No derivation or ratification of `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.",
        "No derivation or ratification of `HARTREE_SCALE_MAPPING_RATIFIED`.",
        "No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.",
        "No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.",
        "No derivation of `m_e`.",
        "No derivation of `alpha(0)`.",
        "No static-source Rydberg retained claim.",
        "No retained hydrogen calculation.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"decision explicit non-claim present: {phrase}", phrase in note)
        audit.check(f"current explicit non-claim present: {phrase}", phrase in current)

    forbidden_overclaims = [
        "This packet ratifies static-source readout",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED is supplied",
        "This note ratifies static-source readout",
        "static-source readout is retained",
        "This packet derives `m_e`",
        "This packet derives `alpha(0)`",
        "This packet claims hydrogen is retained",
        "observed Rydberg is used as proof",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent from decision: {phrase}", phrase not in note)
        audit.check(f"forbidden overclaim absent from current no-go: {phrase}", phrase not in current)

    audit.summary()


if __name__ == "__main__":
    main()
