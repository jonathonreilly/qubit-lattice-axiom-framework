#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen static-source Rydberg closure target.

This is a support runner. It checks the final-lane closure predicate and the
bookkeeping arithmetic for the static-source Rydberg target. It does not
derive m_e, alpha(0), or full hydrogen spectroscopy.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
DERIVED_INDEX = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"

M_E_EV_COMPARATOR = 510_998.95
ALPHA0_INV_COMPARATOR = 137.035999084
ALPHA_MZ_INV_REPO = 127.67
RYDBERG_EV_COMPARATOR = 13.605693122994

STATIC_SOURCE_REQUIRED = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
}

FULL_PRECISION_EXTRA_REQUIRED = {
    "RETAINED_PROTON_MASS",
    "RETAINED_REDUCED_MASS_BRIDGE",
    "RETAINED_FINE_STRUCTURE_QED_CORRECTIONS",
    "RETAINED_LAMB_SHIFT_CORRECTIONS",
    "RETAINED_HYPERFINE_AND_SPIN_STRUCTURE",
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
        print(f"\nSUMMARY failures={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def rydberg_ev(m_e_ev: float, alpha: float) -> float:
    return 0.5 * m_e_ev * alpha * alpha


def energy_ev(n: int, m_e_ev: float, alpha: float) -> float:
    return -rydberg_ev(m_e_ev, alpha) / (n * n)


def closes_static_source_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_REQUIRED <= inputs


def closes_full_precision_hydrogen(inputs: set[str]) -> bool:
    return closes_static_source_rydberg(inputs) and FULL_PRECISION_EXTRA_REQUIRED <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("static-source Rydberg discriminator exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md",
        "docs/HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md",
        "docs/ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md",
        "scripts/frontier_atomic_hydrogen_lattice_companion.py",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "E_n = -m_e alpha(0)^2 / (2 n^2)",
        "static-source one-body target",
        "full precision hydrogen",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ATOMIC_OPERATOR_HARNESS_VERIFIED",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "AUDIT_ACCEPTANCE",
        "FULL_PRECISION_HYDROGEN",
        "RETAINED_PROTON_MASS",
        "RETAINED_REDUCED_MASS_BRIDGE",
        "RETAINED_FINE_STRUCTURE_QED_CORRECTIONS",
        "RETAINED_LAMB_SHIFT_CORRECTIONS",
        "RETAINED_HYPERFINE_AND_SPIN_STRUCTURE",
        "R_inf = (1/2) m_e alpha(0)^2",
        "alpha_EM(M_Z)^-1 = 127.67",
        "about a 15 percent overshoot",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "STATIC_SOURCE_NR_COULOMB_TEXT_LOCK",
        "SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED",
        "COULOMB_KERNEL_ASYMPTOTIC_RATIFIED",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` as an unsupplied upstream input",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "review compression only",
        "static-source NR Coulomb handoff",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "unsupplied upstream input",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "the Lane 2 `alpha(0)` handoff",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB` as an unsupplied upstream input",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "review compression only",
        "Open PR Alignment",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "six direct final predicate inputs",
        "#5033",
        "#5030",
        "#5021",
        "#5018",
        "#5017",
        "#5016",
        "#5015",
        "#5014",
        "#5012",
        "#5011",
        "#5007",
        "#4991",
        "open, clean",
        "open draft, dirty",
        "Lane 6 closes m_e",
        "Lane 2 closes alpha(0)",
        "retained static-source NR Coulomb limit",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed static-source Rydberg closure",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Closure predicate checks")
    empty_inputs: set[str] = set()
    only_shape = {"ATOMIC_OPERATOR_HARNESS_VERIFIED"}
    with_me = only_shape | {"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}
    with_alpha = only_shape | {"RETAINED_ALPHA0_LOW_ENERGY_COULOMB"}
    almost = STATIC_SOURCE_REQUIRED - {"AUDIT_ACCEPTANCE"}
    full_static = set(STATIC_SOURCE_REQUIRED)
    full_precision = set(STATIC_SOURCE_REQUIRED | FULL_PRECISION_EXTRA_REQUIRED)

    audit.check("empty inputs do not close static-source Rydberg", not closes_static_source_rydberg(empty_inputs))
    audit.check("shape harness alone does not close static-source Rydberg", not closes_static_source_rydberg(only_shape))
    audit.check("m_e without alpha(0) does not close static-source Rydberg", not closes_static_source_rydberg(with_me))
    audit.check("alpha(0) without m_e does not close static-source Rydberg", not closes_static_source_rydberg(with_alpha))
    audit.check("all but audit acceptance does not close static-source Rydberg", not closes_static_source_rydberg(almost))
    audit.check("full static-source predicate closes static-source Rydberg", closes_static_source_rydberg(full_static))
    audit.check("static-source predicate alone does not close full precision hydrogen", not closes_full_precision_hydrogen(full_static))
    audit.check("full precision predicate closes stronger target", closes_full_precision_hydrogen(full_precision))

    section("Comparator arithmetic")
    alpha0 = 1.0 / ALPHA0_INV_COMPARATOR
    alpha_mz = 1.0 / ALPHA_MZ_INV_REPO
    ryd_alpha0 = rydberg_ev(M_E_EV_COMPARATOR, alpha0)
    ryd_alpha_mz = rydberg_ev(M_E_EV_COMPARATOR, alpha_mz)
    shift = ryd_alpha_mz / ryd_alpha0 - 1.0
    print(f"Rydberg from comparator m_e and alpha(0): {ryd_alpha0:.12f} eV")
    print(f"Rydberg from comparator m_e and alpha(M_Z): {ryd_alpha_mz:.12f} eV")
    print(f"relative high-energy-alpha overshoot: {100.0 * shift:.3f}%")
    audit.check(
        "alpha(0) comparator reproduces Rydberg comparator",
        abs(ryd_alpha0 - RYDBERG_EV_COMPARATOR) / RYDBERG_EV_COMPARATOR < 1e-11,
        f"ryd={ryd_alpha0:.12f}",
    )
    audit.check(
        "direct alpha(M_Z) substitution overshoots by about 15 percent",
        0.14 < shift < 0.16,
        f"shift={100.0 * shift:.3f}%",
    )
    audit.check(
        "alpha(M_Z) and alpha(0) are distinct inputs",
        abs(alpha_mz - alpha0) / alpha0 > 0.07,
        f"relative alpha gap={(alpha_mz / alpha0 - 1.0):.3%}",
    )

    expected_levels = {
        1: -13.605693122994,
        2: -3.4014232807485,
        3: -1.5117436803326665,
        4: -0.850355820187125,
        5: -0.54422772491976,
    }
    for n, expected in expected_levels.items():
        got = energy_ev(n, M_E_EV_COMPARATOR, alpha0)
        audit.check(
            f"Bohr/Rydberg level n={n} matches comparator table",
            abs(got - expected) < 5e-11,
            f"E={got:.12f} eV",
        )
        audit.check(
            f"n^2 E_n is constant for n={n}",
            abs((n * n * got) + ryd_alpha0) < 5e-13,
        )

    section("Primitive and derived-index boundary")
    primitive_registry = read(PRIMITIVE_REGISTRY)
    derived_index = read(DERIVED_INDEX)
    for primitive in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive registry names {primitive}", primitive in primitive_registry)
    for absent in [
        "electron_mass_primitive",
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
        "hydrogen_spectrum_primitive",
        "proton_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_registry)
    audit.check("derived index contains alpha_EM(M_Z) retained surface", "alpha_EM(M_Z)" in derived_index)
    audit.check(
        "derived index does not list alpha(0) as retained derived value",
        "alpha(0)" not in derived_index and "ALPHA0" not in derived_index,
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `m_e`.",
        "No derivation of `alpha(0)`.",
        "No derivation of the physical-unit nonrelativistic Coulomb limit.",
        "No retained static-source hydrogen claim.",
        "No full precision hydrogen spectroscopy.",
        "No proton mass, reduced-mass, fine-structure, Lamb-shift, hyperfine, helium,",
        "No use of observed Rydberg, observed `m_e`, or observed `alpha(0)` as proof",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `m_e`",
        "This note derives `alpha(0)`",
        "hydrogen is retained",
        "full precision hydrogen is retained",
        "observed Rydberg is used as proof",
        "proton mass is retained",
        "Lamb shift is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
