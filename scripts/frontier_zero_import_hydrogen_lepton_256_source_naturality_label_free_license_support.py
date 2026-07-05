#!/usr/bin/env python3
"""Verifier for the label-free source-naturality license support note.

This support runner checks the finite source-coordinate content behind the
conditional license: a label-free source interface makes tensor-frame
relabelings source-coordinate isomorphisms, forcing a uniform source ray. It
does not derive S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
NATURALITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
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


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def projective_scale(a: Vector, b: Vector) -> Fraction | None:
    lam: Fraction | None = None
    for coord in set(a) | set(b):
        av = a.get(coord, Fraction(0))
        bv = b.get(coord, Fraction(0))
        if bv == 0:
            if av != 0:
                return None
            continue
        candidate = av / bv
        if candidate <= 0:
            return None
        if lam is None:
            lam = candidate
        elif candidate != lam:
            return None
    return lam


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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("label-free source-naturality note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        SOURCE_SLOT,
        NATURALITY,
        UNIFORM_RAY,
        SL_READOUT,
        A3_PLACEMENT,
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
        "Source Naturality Label-Free License Support",
        "label-free source-interface condition",
        "J(j) = sum_c j_c O_c",
        "source-family naturality",
        "no physical coordinate tag",
        "G_tf",
        "acts transitively on `C`",
        "[j] = [rho_g j]",
        "lambda_g = 1",
        "sigma([j])_c = 1/256",
        "Counterexample Boundary",
        "#4948",
        "#4947",
        "#4943",
        "#4940",
        "#4950",
        "#4902",
        "#4905",
        "#4906",
        "latest refresh after this note listed",
        "#4949",
        "additive-even premise relocation",
        "closed non-exact carrier witness",
        "No-Go Discipline Gate",
        "broad source-naturality closure fails; narrowed label-free",
        "Gate result: `PASS` for the narrowed label-free source-naturality license support.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite tensor-frame action")
    coords = coordinates()
    gens = generators()
    audit.check("source coordinate set has 4^4 = 256 elements", len(coords) == 256)
    full_orbit = orbit((0, 0, 0, 0), gens)
    audit.check("tensor-frame relabeling generators act transitively", len(full_orbit) == 256)

    uniform = {coord: Fraction(7, 1) for coord in coords}
    for name, gen in gens:
        relabeled = apply_perm(uniform, gen)
        audit.check(f"label-free uniform ray invariant under {name}", relabeled == uniform)
        audit.check(f"positive projective scale is trivial under {name}", projective_scale(relabeled, uniform) == 1)

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1, 1) for coord in coords}
    tagged_norm = normalize(tagged)
    tagged_swapped = apply_perm(tagged, swap_values(0, 0, 1))
    audit.check("coordinate-tagged ray changes under source-coordinate relabeling", tagged_swapped != tagged)
    audit.check("coordinate-tagged ray is not projectively invariant", projective_scale(tagged_swapped, tagged) is None)
    audit.check("coordinate-tagged normalized singleton is not 1/256", tagged_norm[(0, 0, 0, 0)] != Fraction(1, 256), f"value={tagged_norm[(0, 0, 0, 0)]}")

    uniform_norm = normalize(uniform)
    audit.check("label-free uniform ray normalizes to total one", sum(uniform_norm.values(), Fraction(0)) == 1)
    audit.check("label-free singleton source strength is 1/256", uniform_norm[(0, 0, 0, 0)] == Fraction(1, 256))

    for name, gen in gens[:4]:
        once = apply_perm(tagged, gen)
        twice = apply_perm(once, gen)
        audit.check(f"sample generator has finite order two: {name}", twice == tagged)

    section("Authority boundary")
    source_slot = read(SOURCE_SLOT)
    naturality = read(NATURALITY)
    uniform_ray = read(UNIFORM_RAY)
    sl_readout = read(SL_READOUT)
    a3 = read(A3_PLACEMENT)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    registry = read(REGISTRY)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    minimal_flat = flat(minimal).lower()
    scale_flat = flat(scale).lower()

    audit.check("source-slot support names slot-resolved source map", "J(j) = sum_c j_c O_c" in source_slot)
    audit.check("prior naturality bridge names W5b", "W5b" in naturality and "source-family naturality" in naturality)
    audit.check("uniform-ray note names transitivity and 1/256", "transitivity" in uniform_ray and "1/256" in uniform_ray)
    audit.check("S_l readout note keeps source-readout convention live", "source-readout convention" in sl_readout and "No derivation that `S_l` is physically" in sl_readout)
    audit.check("A3 discriminator keeps correction placement separate", "A3 Correction-Placement Discriminator" in a3 and "No derivation of `C_A3" in a3)
    audit.check("Koide firewall keeps electron readout separate", "Koide Electron-Readout Firewall" in koide and "No derivation of `m_e`" in koide)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal_flat and "physical observable bridges remain downstream" in minimal_flat)
    audit.check("registry lists approved premise nodes", all(name in registry for name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale_flat)
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic and "empirical fit" in kinetic)
    audit.check("realized-state primitive excludes selectors and weighting", "state-selection rule" in realized and "weighting" in realized)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the charged-lepton source/action interface.",
        "No derivation that the charged-lepton source interface is label-free.",
        "No derivation that source controls are nonnegative source strengths.",
        "No derivation that charged-lepton source strength is physically the",
        "No derivation that `S_l` reads `sigma([j])_c`.",
        "No derivation of the `256.082435...` A3 correction.",
        "No derivation of `m_e`, Koide/electron readout, `alpha(0)`, or hydrogen",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "source-family naturality is derived from the minimal framework",
        "This note proves the source interface is label-free",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "C_A3 is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
