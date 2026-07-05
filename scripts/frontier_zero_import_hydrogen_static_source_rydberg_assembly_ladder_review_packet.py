#!/usr/bin/env python3
"""Verifier for the static-source Rydberg assembly ladder review packet.

This runner checks that the final static-source dependency compression is
explicit and remains a review-support surface. It does not ratify m_e,
alpha(0), the static-source NR Coulomb limit, static-source Rydberg, or full
hydrogen spectroscopy.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
STATIC_NR_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
PHYSICAL_ELECTRON_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
PHYSICAL_ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ALPHA0_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
ALPHA0_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA0_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
STATIC_NR_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
STATIC_NR_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md"
RYDBERG_FIREWALL = ROOT / "docs" / "ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
ATOMIC_PROBE = ROOT / "docs" / "ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md"
HYDROGEN_REPAIR = ROOT / "docs" / "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md"
ATOMIC_COMPANION = ROOT / "scripts" / "frontier_atomic_hydrogen_lattice_companion.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
DERIVED_INDEX = ROOT / "docs" / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md"

M_E_EV_COMPARATOR = 510_998.95
ALPHA0_INV_COMPARATOR = 137.035999084
ALPHA_MZ_INV_REPO = 127.67
RYDBERG_EV_COMPARATOR = 13.605693122994

STATIC_SOURCE_INPUTS = {
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


def closes_static_source(inputs: set[str]) -> bool:
    return STATIC_SOURCE_INPUTS <= inputs


def closes_full_precision(inputs: set[str]) -> bool:
    return closes_static_source(inputs) and FULL_PRECISION_EXTRA_REQUIRED <= inputs


def rydberg_ev(m_e_ev: float, alpha: float) -> float:
    return 0.5 * m_e_ev * alpha * alpha


def energy_ev(n: int, m_e_ev: float, alpha: float) -> float:
    return -rydberg_ev(m_e_ev, alpha) / (n * n)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        STATIC_TARGET,
        STATIC_NR_ASSEMBLY,
        PHYSICAL_ELECTRON_ASSEMBLY,
        PHYSICAL_ELECTRON_PACKET,
        PHYSICAL_ELECTRON_NO_GO,
        ALPHA0_ASSEMBLY,
        ALPHA0_PACKET,
        ALPHA0_NO_GO,
        STATIC_NR_PACKET,
        STATIC_NR_NO_GO,
        RYDBERG_FIREWALL,
        ATOMIC_PROBE,
        HYDROGEN_REPAIR,
        ATOMIC_COMPANION,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
        DERIVED_INDEX,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required packet content")
    required_phrases = [
        "Static-Source Rydberg Assembly Ladder Review Packet",
        "support / review-compression packet",
        "this packet does not ratify static-source",
        "does not claim hydrogen is retained",
        "reviewable surface",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ATOMIC_OPERATOR_HARNESS_VERIFIED",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those six final predicate inputs",
        "FULL_PRECISION_HYDROGEN",
        "RETAINED_PROTON_MASS",
        "RETAINED_REDUCED_MASS_BRIDGE",
        "RETAINED_FINE_STRUCTURE_QED_CORRECTIONS",
        "RETAINED_LAMB_SHIFT_CORRECTIONS",
        "RETAINED_HYPERFINE_AND_SPIN_STRUCTURE",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "review-compresses the direct static-source NR Coulomb ladder",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md",
        "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md",
        "frontier_atomic_hydrogen_lattice_companion.py",
        "ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md",
        "R_inf = (1/2) m_e alpha(0)^2",
        "E_n = -R_inf / n^2",
        "m_e = 510998.95 eV",
        "alpha(0)^-1 = 137.035999084",
        "R_inf = 13.605693122994 eV",
        "alpha_EM(M_Z)^-1 = 127.67",
        "about a 15 percent overshoot",
        "clean/green status is not a prerequisite",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall anomaly inflow spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5011` eta twisted walk family runner | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "static_source_rydberg_primitive",
        "static_source_nr_coulomb_primitive",
        "retained_static_source_nr_coulomb_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
        "hydrogen_spectrum_primitive",
        "proton_mass_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "review distance, not retained physics distance",
        "No-Go Discipline Gate",
        "OPEN POSITIVE ROUTE",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_static = set(STATIC_SOURCE_INPUTS)
    audit.check("full static-source predicate accepts retained handoff", closes_static_source(full_static))
    for missing in sorted(STATIC_SOURCE_INPUTS):
        reduced = set(STATIC_SOURCE_INPUTS)
        reduced.remove(missing)
        audit.check(f"static-source handoff fails without {missing}", not closes_static_source(reduced))
    accepted_subsets = [subset for subset in all_subsets(STATIC_SOURCE_INPUTS) if closes_static_source(subset)]
    audit.check("only full static-source subset closes handoff", accepted_subsets == [full_static])

    for row in sorted(STATIC_SOURCE_INPUTS):
        audit.check(f"{row} alone does not close static-source Rydberg", not closes_static_source({row}))

    key_pairs = [
        {"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB"},
        {"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT", "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT"},
        {"RETAINED_ALPHA0_LOW_ENERGY_COULOMB", "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT"},
        {
            "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
            "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
            "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        },
    ]
    for inputs in key_pairs:
        audit.check(f"{sorted(inputs)} does not close static-source Rydberg", not closes_static_source(inputs))

    full_precision = set(STATIC_SOURCE_INPUTS | FULL_PRECISION_EXTRA_REQUIRED)
    audit.check("static-source predicate alone does not close full precision", not closes_full_precision(full_static))
    audit.check("full precision predicate closes stronger target", closes_full_precision(full_precision))

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

    section("Authority and downstream wiring checks")
    goal = read(GOAL)
    static_target = read(STATIC_TARGET)
    static_nr_assembly = read(STATIC_NR_ASSEMBLY)
    physical_electron_assembly = read(PHYSICAL_ELECTRON_ASSEMBLY)
    alpha0_assembly = read(ALPHA0_ASSEMBLY)
    static_nr_packet = read(STATIC_NR_PACKET)
    static_nr_no_go = read(STATIC_NR_NO_GO)
    atomic_companion = read(ATOMIC_COMPANION)
    derived_index = read(DERIVED_INDEX)

    new_packet_name = "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
    audit.check("goal packet references static-source Rydberg assembly", new_packet_name in goal)
    audit.check("static-source discriminator references assembly", new_packet_name in static_target)
    audit.check("static-source NR assembly exists as SR.3 support", "Static-Source NR Coulomb Assembly Ladder Review Packet" in static_nr_assembly)
    audit.check("static-source NR assembly remains support-only", "does not supply `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`" in flat(static_nr_assembly))
    audit.check("physical electron assembly lists static-source assembly as downstream", new_packet_name in physical_electron_assembly)
    audit.check("alpha0 assembly lists static-source assembly as downstream", new_packet_name in alpha0_assembly)
    audit.check(
        "physical electron assembly remains support-only",
        "does not supply `PHYSICAL_ELECTRON_READOUT_RETAINED`" in flat(physical_electron_assembly)
        and "does not supply" in physical_electron_assembly,
    )
    audit.check(
        "alpha0 assembly remains support-only",
        "does not supply `ALPHA0_TRANSPORT_RETAINED`" in alpha0_assembly
        and "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in alpha0_assembly,
    )
    audit.check(
        "static NR packet gives conditional consequence only",
        "This packet supplies only the static-source NR Coulomb side of that predicate" in static_nr_packet,
    )
    audit.check(
        "static NR current surface keeps retained limit unsupplied",
        "do not supply `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`" in static_nr_no_go,
    )
    audit.check("atomic companion keeps shape harness in view", "1/n" in atomic_companion and "Rydberg" in atomic_companion)
    audit.check("derived index contains alpha_EM(M_Z) retained surface", "alpha_EM(M_Z)" in derived_index)
    audit.check(
        "derived index does not list alpha(0) as retained derived value",
        "alpha(0)" not in derived_index and "ALPHA0" not in derived_index,
    )

    section("Primitive registry boundary")
    primitive_registry = read(REGISTRY)
    for primitive in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive registry names {primitive}", primitive in primitive_registry)
    for absent in [
        "static_source_rydberg_primitive",
        "static_source_nr_coulomb_primitive",
        "retained_static_source_nr_coulomb_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
        "qed_loop_kernel_primitive",
        "hydrogen_spectrum_primitive",
        "proton_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_registry)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation or ratification of `STATIC_SOURCE_RYDBERG_RETAINED`.",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation or ratification of `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`.",
        "No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.",
        "No derivation of the atomic `1/n^2` harness as an eV-scale theorem.",
        "No derivation of proton mass, reduced-mass bridge, fine structure, Lamb",
        "No use of observed Rydberg, observed hydrogen lines, observed `m_e`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet derives `m_e`",
        "This packet derives `alpha(0)`",
        "static-source Rydberg is retained",
        "This packet claims hydrogen is retained",
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
