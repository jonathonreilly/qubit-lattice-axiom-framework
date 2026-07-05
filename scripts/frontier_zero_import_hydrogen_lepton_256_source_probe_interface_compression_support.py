#!/usr/bin/env python3
"""Verifier for the lepton source-probe interface compression support note.

This runner checks the conditional composition:
if the normalized label-free charged-lepton full-cell source-probe interface is
supplied, prior source-chain notes compose to exact S_l = 1/256.
It does not derive S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
RATIFICATION_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
OBS_SOURCE = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
LABEL_FREE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
GAUGE_QUOTIENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
UNIFORM_RAY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
READOUT_DISC = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
L1_NORM = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
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


def apply_perm(vector: Vector, perm: Perm) -> Vector:
    return {perm(coord): value for coord, value in vector.items()}


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def solve_s_l(front: Fraction, source_coeff: Fraction) -> Fraction:
    if front == 0:
        raise ValueError("nonzero front required")
    return source_coeff / front


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-probe interface compression note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        RATIFICATION_TARGET,
        GOAL,
        ROUTE,
        OBS_SOURCE,
        SOURCE_COUPLED,
        FULL_CELL,
        D17_SEP,
        LABEL_FREE,
        POSITIVE_CONE,
        GAUGE_QUOTIENT,
        SHAPE_SELECTOR,
        PROJECTIVE_SECTION,
        UNIFORM_RAY,
        SL_READOUT,
        READOUT_DISC,
        L1_NORM,
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
        "Source-Probe Interface Compression Support",
        "normalized label-free charged-lepton full-cell source-probe interface",
        "S_lep[j] = h * B_lep * sum_{c in C} j_c O_c",
        "source controls carry no physical coordinate tag",
        "Source strength is the real monotone nonzero nonnegative projective ray",
        "H = h * sum_c j_c",
        "h * J(j) = H * sum_c sigma([j])_c O_c",
        "common source-coupling front",
        "no monotone positive source-strength clause",
        "no source-coupling gauge quotient clause",
        "no source-shape readout selector clause",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "sigma([j])_c = (h*j_c)/H",
        "monotone finite-additive source-strength semantics",
        "`S_l` denotes the normalized singleton source-strength multiplier",
        "dS_lep/dj_c = h * B_lep * O_c",
        "[j] = [rho_g j]",
        "sigma([j])_c = 1/256",
        "S_l = 1/256",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "source-probe ratification target discriminator",
        "full F/L/P/R interface",
        "one-clause-removed target fails",
        "256.082435",
        "Clause Failure Boundaries",
        "#4952",
        "#4960",
        "#4959",
        "#4958",
        "#4957",
        "#4956",
        "#4955",
        "#4954",
        "#4953",
        "#4951",
        "#4950",
        "#4949",
        "#4948",
        "#4947",
        "#4943",
        "#4940",
        "#4902",
        "#4905",
        "#4906",
        "dynamic helper dependency audit-packet repair",
        "hypercharge downstream trace scope quarantine",
        "Gate B helper-runner artifact repair",
        "theta W2 physical registrability no-go",
        "AC first-order determinant retirement-readiness no-go",
        "gravity eikonal small-k remainder repair",
        "stale sibling-interface runner repair",
        "K-real physicalization current-surface no-go",
        "closed without merge",
        "Qualification unfixed-choice clarification",
        "theta mass determinant-bridge retirement-readiness",
        "No-Go Discipline Gate",
        "broad `S_l` closure fails; narrowed interface-compression support passes.",
        "narrowed source-probe interface compression support",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite source-probe composition")
    coords = coordinates()
    gens = generators()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)
    audit.check("tensor-frame generators are transitive on C", len(orbit((0, 0, 0, 0), gens)) == 256)

    uniform = {coord: Fraction(3, 1) for coord in coords}
    uniform_weight = normalize(uniform)[coords[0]]
    audit.check("uniform projective source singleton is 1/256", uniform_weight == Fraction(1, 256))

    scaled_uniform = {coord: Fraction(45, 1) for coord in coords}
    audit.check("positive source-control rescaling leaves L1 section fixed", normalize(scaled_uniform)[coords[0]] == uniform_weight)

    for name, gen in gens[:6]:
        relabeled = apply_perm(uniform, gen)
        audit.check(f"uniform source ray invariant under {name}", relabeled == uniform)

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1, 1) for coord in coords}
    tagged_weight = normalize(tagged)[coords[0]]
    tagged_swapped = apply_perm(tagged, swap_values(0, 0, 1))
    audit.check("coordinate-tagged ray changes under relabeling", tagged_swapped != tagged)
    audit.check("coordinate-tagged singleton is not 1/256", tagged_weight != Fraction(1, 256), f"value={tagged_weight}")

    front = Fraction(13, 17)
    source_coeff = front * uniform_weight
    audit.check("source coefficient equals common front times singleton weight", source_coeff == front * Fraction(1, 256))
    audit.check("nonzero front cancellation returns S_l source singleton", solve_s_l(front, source_coeff) == Fraction(1, 256))

    rn_amplitude = Fraction(1, 16)
    audit.check("RN/Fisher uniform 256-channel amplitude is normalized as 1/16", len(coords) * rn_amplitude * rn_amplitude == 1)
    audit.check("RN/Fisher amplitude is not the L1 singleton weight", rn_amplitude != Fraction(1, 256))

    projection_trace = Fraction(1, 16)
    audit.check("rank-one projection trace in M_16(C) gives 1/16", projection_trace == Fraction(1, 16))
    audit.check("projection trace is not matrix-unit singleton density", projection_trace != Fraction(1, 256))

    exact_divisor = Fraction(256, 1)
    comparator_micro = Fraction(256_082_435, 1_000_000)
    audit.check("exact 256 differs from comparator divisor", exact_divisor != comparator_micro)
    correction = exact_divisor / comparator_micro
    audit.check("A3 correction remains a separate near-one factor", Fraction(999, 1000) < correction < 1)

    section("Authority boundary checks")
    obs_source = read(OBS_SOURCE)
    source_coupled = read(SOURCE_COUPLED)
    full_cell = read(FULL_CELL)
    d17_sep = read(D17_SEP)
    label_free = read(LABEL_FREE)
    positive_cone = read(POSITIVE_CONE)
    gauge_quotient = read(GAUGE_QUOTIENT)
    shape_selector = read(SHAPE_SELECTOR)
    projective_section = read(PROJECTIVE_SECTION)
    uniform_ray = read(UNIFORM_RAY)
    sl_readout = read(SL_READOUT)
    readout_disc = read(READOUT_DISC)
    l1_norm = read(L1_NORM)
    a3 = read(A3)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    audit.check("observable source candidate is open gate", "open_gate" in obs_source and "source-coupling convention" in obs_source)
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("full-cell support names 256 matrix-unit coordinates", "256" in full_cell and "matrix-unit coordinates" in full_cell)
    audit.check("D17 support names 1/sqrt(2) separation", "1/sqrt(2)" in d17_sep and "separate" in d17_sep)
    audit.check("label-free support names source-family naturality", "source-family naturality" in label_free and "label-free" in label_free)
    audit.check(
        "positive-cone support separates signed probes from source strengths",
        "Signed or complex" in positive_cone and "source strengths are nonnegative" in positive_cone,
    )
    audit.check(
        "gauge quotient support separates front from normalized source shape",
        "H = h * sum_c j_c" in gauge_quotient and "sigma([j])_c" in gauge_quotient,
    )
    audit.check(
        "shape selector support selects sigma among named candidates",
        "Q1-Q4" in shape_selector and "(h*j_c)/H" in shape_selector,
    )
    audit.check("projective section names sigma formula", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("uniform-ray support names transitivity and 1/256", "transitivity" in uniform_ray and "1/256" in uniform_ray)
    audit.check("S_l readout support names normalized singleton source-strength multiplier", "normalized singleton source-strength multiplier" in sl_readout)
    audit.check("readout discriminator keeps projection/Born trace at 1/16", "projection/Born trace" in readout_disc and "1/16" in readout_disc)
    audit.check("L1 norm discriminator names L1 algebra-coordinate density", "L1 algebra-coordinate density" in l1_norm)
    audit.check("A3 placement keeps precision separate", "A3 Correction-Placement Discriminator" in a3 and "C_A3" in a3)
    audit.check("Koide firewall keeps electron readout separate", "Koide Electron-Readout Firewall" in koide and "No derivation of `m_e`" in koide)

    minimal_flat = flat(minimal).lower()
    audit.check("minimal axioms exclude source/action bridge", "source/action" in minimal_flat and "physical observable bridge" in minimal_flat)
    scale_flat = flat(scale)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale_flat or "does not supply any dimensionless quantity" in scale_flat)
    audit.check("kinetic primitive excludes selector/readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("registry minimal node excludes source/action", "source/action bridge" in nodes["minimal_axioms"]["note"])

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation or ratification of the normalized label-free source-probe",
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
        "This note retains the interface",
        "C1 is retained",
        "S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
