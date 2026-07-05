#!/usr/bin/env python3
"""Verifier for the lepton source-shape readout selector discriminator.

This runner checks that, among current named source-chain candidates, only
sigma([j])_c satisfies the quotient source-shape criteria Q1-Q4. It does not
derive S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
GAUGE_QUOTIENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
READOUT_DISC = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
L1_NORM = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


Coord = tuple[int, int, int, int]
Vector = dict[Coord, Fraction]


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


def total_strength(vector: Vector) -> Fraction:
    if any(value < 0 for value in vector.values()):
        raise ValueError("nonnegative source-strength controls required")
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return total


def sigma(vector: Vector) -> Vector:
    total = total_strength(vector)
    return {coord: value / total for coord, value in vector.items()}


def source_front(h: Fraction, vector: Vector) -> Fraction:
    if h <= 0:
        raise ValueError("positive front required")
    return h * total_strength(vector)


def rescale_pair(h: Fraction, vector: Vector, lam: Fraction) -> tuple[Fraction, Vector]:
    if lam <= 0:
        raise ValueError("positive rescaling required")
    return h / lam, {coord: lam * value for coord, value in vector.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-shape selector note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        GAUGE_QUOTIENT,
        SL_READOUT,
        PROJECTIVE_SECTION,
        POSITIVE_CONE,
        READOUT_DISC,
        L1_NORM,
        SOURCE_MEASURE,
        COMPRESSION,
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
        "Source-Shape Readout Selector Discriminator",
        "H = h * sum_c j_c",
        "h * J(j) = H * sum_c sigma([j])_c O_c",
        "source-shape criteria",
        "Q1 gauge invariance",
        "Q2 front independence",
        "Q3 normalized shape",
        "Q4 uniform-ray value",
        "(h*j_c)/H",
        "equals `sigma([j])_c`",
        "raw coupling/front",
        "raw source-control amplitude",
        "invariant coefficient, but still front-bearing",
        "global front, not singleton shape",
        "RN/Fisher amplitude `1/16`",
        "projection/Born trace `1/16`",
        "among current named candidates",
        "source-probe interface ratification",
        "#4960",
        "#4959",
        "#4958",
        "#4957",
        "#4956",
        "#4955",
        "#4954",
        "#4953",
        "#4952",
        "#4951",
        "#4950",
        "#4943",
        "#4940",
        "#4902",
        "#4905",
        "#4906",
        "dynamic helper dependency audit-packet repair",
        "hypercharge downstream trace scope quarantine",
        "theta W2 physical registrability no-go",
        "Gate B helper-runner artifact repair",
        "closed without merge",
        "merged into `main` at 2026-07-04T16:10:45Z",
        "No-Go Discipline Gate",
        "broad `S_l` closure fails; narrowed source-shape readout selector",
        "Gate result:** `PASS` for the narrowed source-shape readout selector",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Candidate selector arithmetic")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)

    vector: Vector = {
        coord: Fraction(2, 1) if index < 128 else Fraction(1, 1)
        for index, coord in enumerate(coords)
    }
    h = Fraction(5, 1)
    lam = Fraction(7, 1)
    h_scaled, vector_scaled = rescale_pair(h, vector, lam)
    H = source_front(h, vector)
    H_scaled = source_front(h_scaled, vector_scaled)
    shape = sigma(vector)
    shape_scaled = sigma(vector_scaled)
    coord0 = coords[0]

    audit.check("test vector total is 384", total_strength(vector) == 384)
    audit.check("overall front H is 1920", H == 1920)
    audit.check("rescaled H is invariant", H_scaled == H)
    audit.check("raw h is not gauge invariant", h_scaled != h)
    audit.check("raw j_c is not gauge invariant", vector_scaled[coord0] != vector[coord0])
    audit.check("h*j_c is gauge invariant", h_scaled * vector_scaled[coord0] == h * vector[coord0])
    audit.check("sigma coordinate is gauge invariant", shape_scaled[coord0] == shape[coord0])
    audit.check("(h*j_c)/H equals sigma coordinate", (h * vector[coord0]) / H == shape[coord0])
    audit.check("sigma coordinates sum to one", sum(shape.values(), Fraction(0)) == 1)
    audit.check("h*j_c coordinates do not sum to one", sum((h * value for value in vector.values()), Fraction(0)) != 1)
    audit.check("H is global front, not singleton coordinate", H != shape[coord0])
    audit.check("nonuniform sigma coordinate is 1/192", shape[coord0] == Fraction(1, 192))
    audit.check("nonuniform sigma coordinate is not 1/256", shape[coord0] != Fraction(1, 256))

    uniform: Vector = {coord: Fraction(3, 1) for coord in coords}
    uniform_shape = sigma(uniform)
    uniform_H = source_front(h, uniform)
    audit.check("uniform shape singleton is 1/256", uniform_shape[coords[0]] == Fraction(1, 256))
    audit.check("uniform H is front-bearing", uniform_H == h * 3 * 256)
    audit.check("(h*u_c)/H gives uniform 1/256", (h * uniform[coords[0]]) / uniform_H == Fraction(1, 256))

    rn_amplitude = Fraction(1, 16)
    projection_trace = Fraction(1, 16)
    audit.check("RN/Fisher amplitude has L2 normalization over 256 channels", len(coords) * rn_amplitude * rn_amplitude == 1)
    audit.check("RN/Fisher amplitude fails L1 singleton shape", len(coords) * rn_amplitude != 1)
    audit.check("projection/Born trace is 1/16", projection_trace == Fraction(1, 16))
    audit.check("projection/Born trace is not 1/256", projection_trace != Fraction(1, 256))

    signed: Vector = {coord: Fraction(1, 1) for coord in coords}
    signed[coord0] = Fraction(-1, 1)
    try:
        sigma(signed)
        signed_rejected = False
    except ValueError:
        signed_rejected = True
    audit.check("signed source vector rejected for source-shape selector", signed_rejected)

    zero: Vector = {coord: Fraction(0, 1) for coord in coords}
    try:
        sigma(zero)
        zero_rejected = False
    except ValueError:
        zero_rejected = True
    audit.check("zero vector rejected for projective source shape", zero_rejected)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    gauge = read(GAUGE_QUOTIENT)
    sl_readout = read(SL_READOUT)
    projective = read(PROJECTIVE_SECTION)
    positive_cone = read(POSITIVE_CONE)
    readout_disc = read(READOUT_DISC)
    l1_norm = read(L1_NORM)
    source_measure = read(SOURCE_MEASURE)
    compression = read(COMPRESSION)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    audit.check("goal packet references selector note", NOTE.name in goal)
    audit.check("route triage references selector note", NOTE.name in route)
    audit.check("gauge quotient names H and sigma", "H = h * sum_c j_c" in gauge and "sigma([j])_c" in gauge)
    audit.check("S_l bridge names readout convention", "source-readout convention" in sl_readout and "S_l = sigma([j])_c" in sl_readout)
    audit.check("projective section names sigma formula", "sigma([j])_c = j_c / sum_d j_d" in projective)
    audit.check("positive-cone separates signed probes from strengths", "Signed or complex" in positive_cone and "source strengths are nonnegative" in positive_cone)
    audit.check("readout discriminator names projection/Born trace", "projection/Born trace" in readout_disc and "1/16" in readout_disc)
    audit.check("L1 norm discriminator names 1/256 class", "L1 algebra-coordinate density" in l1_norm and "1/256" in l1_norm)
    audit.check("source-measure theorem names Fisher source unit", "Fisher" in source_measure and "source unit" in source_measure)
    audit.check("compression note still requires interface ratification", "normalized label-free charged-lepton full-cell source-probe interface" in compression)
    audit.check("Koide firewall keeps electron readout separate", "Koide Electron-Readout Firewall" in koide and "No derivation of `m_e`" in koide)

    minimal_flat = flat(minimal).lower()
    audit.check("minimal axioms exclude source/action bridge", "source/action" in minimal_flat and "physical-observable identification" in minimal_flat)
    scale_flat = flat(scale)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale_flat or "does not supply any dimensionless quantity" in scale_flat)
    audit.check("kinetic primitive excludes selector/readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    for node_name in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    audit.check("registry minimal node excludes source/action", "source/action bridge" in nodes["minimal_axioms"]["note"])

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is the full-cell source",
        "No derivation that charged-lepton source strength is physically a nonzero",
        "No derivation that `S_l` is physically the normalized source-shape singleton.",
        "No derivation that `S_l = sigma([j])_c` is retained.",
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
        "S_l is now retained as `sigma([j])_c`",
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
