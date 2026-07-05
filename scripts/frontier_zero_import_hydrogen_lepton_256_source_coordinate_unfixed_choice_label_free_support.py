#!/usr/bin/env python3
"""Verifier for source-coordinate unfixed-choice label-free support.

This runner checks the conditional finite implication:
if a law may not depend on an unfixed source-coordinate choice absent
admission, then coordinate-tagged nonuniform source laws are not zero-import
law-level selectors. It does not derive S_l, m_e, alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
SOURCE_PROBE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
LABEL_FREE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
A3 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]
Vector = dict[Coord, Fraction]
Perm = Callable[[Coord], Coord]


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


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def swap_values(slot: int, a: int, b: int) -> Perm:
    def perm(coord: Coord) -> Coord:
        values = list(coord)
        if values[slot] == a:
            values[slot] = b
        elif values[slot] == b:
            values[slot] = a
        return tuple(values)  # type: ignore[return-value]

    return perm


def swap_slots(slot_a: int, slot_b: int) -> Perm:
    def perm(coord: Coord) -> Coord:
        values = list(coord)
        values[slot_a], values[slot_b] = values[slot_b], values[slot_a]
        return tuple(values)  # type: ignore[return-value]

    return perm


def generators() -> list[tuple[str, Perm]]:
    gens: list[tuple[str, Perm]] = []
    for slot in range(4):
        for a, b in [(0, 1), (1, 2), (2, 3)]:
            gens.append((f"slot{slot} swap {a}{b}", swap_values(slot, a, b)))
    for a, b in [(0, 1), (1, 2), (2, 3)]:
        gens.append((f"slot swap {a}{b}", swap_slots(a, b)))
    return gens


def apply_perm(vector: Vector, perm: Perm) -> Vector:
    return {perm(coord): value for coord, value in vector.items()}


def orbit(start: Coord, gens: list[tuple[str, Perm]]) -> set[Coord]:
    seen = {start}
    queue: deque[Coord] = deque([start])
    while queue:
        current = queue.popleft()
        for _, gen in gens:
            nxt = gen(current)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def invariant_under(vector: Vector, gens: list[tuple[str, Perm]]) -> bool:
    return all(apply_perm(vector, gen) == vector for _, gen in gens)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-coordinate unfixed-choice note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        SOURCE_PROBE,
        LABEL_FREE,
        UNIFORM_RAY,
        SL_READOUT,
        A3,
        KOIDE,
        MINIMAL,
        REGISTRY,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Source-Coordinate Unfixed-Choice Label-Free Support",
        "law may not depend on a choice not fixed by the supplied structure",
        "unless that choice is admitted",
        "source controls carry no physical coordinate tag",
        "coordinate-tagged nonuniform rays",
        "law-level charged-lepton source-strength rule",
        "tensor-frame source structure",
        "w_c = w_d",
        "sigma([j])_c = 1/256",
        "first source coordinate has value 0",
        "#4952",
        "#4956",
        "#4955",
        "#4953",
        "#4954",
        "#4951",
        "#4950",
        "#4949",
        "#4948",
        "#4947",
        "#4943",
        "#4902",
        "#4905",
        "#4906",
        "closed without merge",
        "AC first-order determinant retirement-readiness no-go",
        "gravity eikonal small-k remainder repair",
        "K-real physicalization current-surface no-go",
        "stale sibling-interface runner repair",
        "No-Go Discipline Gate",
        "broad source-probe closure fails; narrowed unfixed-choice",
        "narrowed source-coordinate unfixed-choice label-free support",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite tensor-frame law test")
    coords = coordinates()
    gens = generators()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)
    full_orbit = orbit((0, 0, 0, 0), gens)
    audit.check("tensor-frame generators are transitive", len(full_orbit) == 256)

    uniform = {coord: Fraction(1, 1) for coord in coords}
    audit.check("uniform law is invariant under all tensor-frame generators", invariant_under(uniform, gens))
    uniform_norm = normalize(uniform)
    audit.check("uniform law normalizes to singleton 1/256", uniform_norm[(0, 0, 0, 0)] == Fraction(1, 256))

    orbit_constant = {coord: Fraction(9, 1) for coord in full_orbit}
    audit.check("any one-orbit invariant law is constant", invariant_under(orbit_constant, gens))
    audit.check("one-orbit invariant law has one distinct value", len(set(orbit_constant.values())) == 1)

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1, 1) for coord in coords}
    audit.check("coordinate-tagged law is nonuniform", len(set(tagged.values())) > 1)
    audit.check("coordinate-tagged law is not tensor-frame invariant", not invariant_under(tagged, gens))
    tagged_swapped = apply_perm(tagged, swap_values(0, 0, 1))
    audit.check("source-coordinate relabeling moves the first-coordinate tag", tagged_swapped != tagged)
    tagged_norm = normalize(tagged)
    audit.check("coordinate-tagged singleton is not 1/256", tagged_norm[(0, 0, 0, 0)] != Fraction(1, 256), f"value={tagged_norm[(0, 0, 0, 0)]}")

    admitted_tag = {coord for coord in coords if coord[0] == 0}
    tagged_by_admission = {coord: Fraction(4 if coord in admitted_tag else 1, 1) for coord in coords}
    audit.check("admitted tag can define a nonuniform law if supplied", len(set(tagged_by_admission.values())) == 2)
    audit.check("admitted tag route remains nonuniform", normalize(tagged_by_admission)[(0, 0, 0, 0)] != Fraction(1, 256))

    section("Authority boundary checks")
    source_probe = read(SOURCE_PROBE)
    label_free = read(LABEL_FREE)
    uniform_ray = read(UNIFORM_RAY)
    sl_readout = read(SL_READOUT)
    a3 = read(A3)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)

    audit.check("source-probe note names compressed C1 interface", "normalized label-free charged-lepton full-cell source-probe interface" in source_probe)
    audit.check("label-free note names coordinate tag counterexample", "first source coordinate has value 0" in label_free)
    audit.check("uniform-ray note names transitivity", "transitivity" in uniform_ray and "1/256" in uniform_ray)
    audit.check("S_l readout note keeps S_l convention separate", "source-readout convention" in sl_readout)
    audit.check("A3 discriminator keeps precision separate", "A3 Correction-Placement Discriminator" in a3 and "C_A3" in a3)
    audit.check("Koide firewall keeps electron separate", "Koide Electron-Readout Firewall" in koide and "No derivation of `m_e`" in koide)
    minimal_flat = flat(minimal).lower()
    audit.check("minimal axioms name no privileged sites", "no site is privileged" in minimal_flat)
    audit.check("minimal axioms name no privileged possibilities", "no possibility is privileged" in minimal_flat)
    audit.check("minimal axioms keep source/action downstream", "source/action" in minimal_flat and "physical observable bridge" in minimal_flat)
    nodes = registry["nodes"]
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("scale primitive excludes dimensionless selectors", "selector" in scale and "zero dimensionless" in flat(scale))
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selector and weighting", "state-selection rule" in realized and "weighting" in realized)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation or ratification of the full source-probe interface.",
        "No claim that `#4952` is merged or locally retained in this worktree.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation of the `256.082435...` precision correction.",
        "No derivation of the Koide/electron branch or physical `m_e`.",
        "No derivation of `alpha(0)` or hydrogen spectroscopy.",
        "No new axiom, primitive, or admitted import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "the source-probe interface is retained",
        "#4952 is merged",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
