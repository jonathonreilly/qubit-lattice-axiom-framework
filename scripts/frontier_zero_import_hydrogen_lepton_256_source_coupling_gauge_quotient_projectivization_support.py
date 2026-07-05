#!/usr/bin/env python3
"""Verifier for the lepton source-coupling gauge quotient support note.

This runner checks the finite quotient arithmetic separating the raw
source-coupling/control pair (h,j) into an invariant overall front H and a
normalized projective source-shape coordinate sigma([j]). It does not derive
S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
NORMALIZATION_GAUGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
POSITIVE_CONE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
SL_READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
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
        raise ValueError("nonzero positive total source strength required")
    return total


def sigma(vector: Vector) -> Vector:
    total = total_strength(vector)
    return {coord: value / total for coord, value in vector.items()}


def decompose(h: Fraction, vector: Vector) -> tuple[Fraction, Vector]:
    if h <= 0:
        raise ValueError("positive source-coupling front required")
    total = total_strength(vector)
    return h * total, sigma(vector)


def rescale_pair(h: Fraction, vector: Vector, lam: Fraction) -> tuple[Fraction, Vector]:
    if lam <= 0:
        raise ValueError("positive rescaling required")
    return h / lam, {coord: lam * value for coord, value in vector.items()}


def coefficient_map(h: Fraction, vector: Vector) -> Vector:
    return {coord: h * value for coord, value in vector.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-coupling gauge quotient note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        NORMALIZATION_GAUGE,
        PROJECTIVE_SECTION,
        POSITIVE_CONE,
        SOURCE_COUPLED,
        SOURCE_CONTROL,
        SOURCE_STRENGTH,
        COMPRESSION,
        SL_READOUT,
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
        "Source-Coupling Gauge Quotient Projectivization Support",
        "S_src[j] = h * B_lep * J(j)",
        "J(j) = sum_{c in C} j_c O_c",
        "(h, j) -> (h/lambda, lambda j)",
        "H = h * sum_c j_c",
        "sigma([j])_c = j_c / sum_d j_d",
        "h * J(j) = H * sum_c sigma([j])_c O_c",
        "source-coupling amplitude and the raw source-control magnitude",
        "overall amplitude `H`",
        "projective source-shape coordinate",
        "The raw pair `(h, j)` is not unique",
        "sigma([u])_c = a / (256a) = 1/256",
        "projective source-shape coordinate sigma([j])_c rather than the raw control",
        "source-coupling gauge quotient",
        "product coefficient readout",
        "includes the overall source-coupling front",
        "#4957",
        "#4956",
        "#4955",
        "#4958",
        "#4959",
        "#4960",
        "#4954",
        "#4953",
        "#4952",
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
        "Gate B helper-runner artifact repair",
        "theta W2 physical registrability no-go",
        "dynamic helper dependency audit-packet repair",
        "hypercharge downstream trace scope quarantine",
        "closed without merge",
        "Koide occupancy/slot/phase stack",
        "No-Go Discipline Gate",
        "broad `S_l` closure fails; narrowed source-coupling gauge",
        "Gate result:** `PASS` for the narrowed source-coupling gauge quotient",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite quotient arithmetic")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)

    nonuniform: Vector = {
        coord: Fraction(2, 1) if index < 128 else Fraction(1, 1)
        for index, coord in enumerate(coords)
    }
    h = Fraction(5, 1)
    total = total_strength(nonuniform)
    H, shape = decompose(h, nonuniform)
    audit.check("nonuniform positive vector total is 384", total == 384)
    audit.check("overall amplitude H is h times total strength", H == 1920)
    audit.check("first half normalized shape coordinate is 1/192", shape[coords[0]] == Fraction(1, 192))
    audit.check("second half normalized shape coordinate is 1/384", shape[coords[-1]] == Fraction(1, 384))
    audit.check("normalized source shape sums to one", sum(shape.values(), Fraction(0)) == 1)
    audit.check("coefficient equals H times normalized source shape", h * nonuniform[coords[0]] == H * shape[coords[0]])

    lam = Fraction(7, 1)
    h_scaled, vector_scaled = rescale_pair(h, nonuniform, lam)
    H_scaled, shape_scaled = decompose(h_scaled, vector_scaled)
    audit.check("raw coupling changes under positive rescaling", h_scaled != h)
    audit.check("raw source control changes under positive rescaling", vector_scaled[coords[0]] != nonuniform[coords[0]])
    audit.check("overall amplitude H is rescaling invariant", H_scaled == H)
    audit.check("projective source shape is rescaling invariant", shape_scaled == shape)
    audit.check("source coefficients h*j_c are rescaling invariant", coefficient_map(h_scaled, vector_scaled) == coefficient_map(h, nonuniform))
    audit.check("scaled total strength changes while H stays fixed", total_strength(vector_scaled) == lam * total and H_scaled == H)

    uniform: Vector = {coord: Fraction(3, 1) for coord in coords}
    H_uniform, uniform_shape = decompose(h, uniform)
    audit.check("uniform total strength is 3*256", total_strength(uniform) == 3 * 256)
    audit.check("uniform overall amplitude is h*3*256", H_uniform == h * 3 * 256)
    audit.check("uniform projective singleton shape is 1/256", uniform_shape[coords[0]] == Fraction(1, 256))
    audit.check("uniform shape differs from RN/Fisher amplitude 1/16", uniform_shape[coords[0]] != Fraction(1, 16))

    raw_product_first = h * nonuniform[coords[0]]
    raw_product_last = h * nonuniform[coords[-1]]
    audit.check("product coefficient is invariant but not normalized shape", raw_product_first == 10 and raw_product_first != shape[coords[0]])
    audit.check("nonuniform product coefficients carry overall front", raw_product_first != raw_product_last)

    signed: Vector = {coord: Fraction(1, 1) for coord in coords}
    signed[coords[0]] = Fraction(-1, 1)
    try:
        sigma(signed)
        signed_rejected = False
    except ValueError:
        signed_rejected = True
    audit.check("signed vector is rejected as positive source-strength shape", signed_rejected)

    zero: Vector = {coord: Fraction(0, 1) for coord in coords}
    try:
        sigma(zero)
        zero_rejected = False
    except ValueError:
        zero_rejected = True
    audit.check("zero vector is rejected as projective source-strength shape", zero_rejected)

    try:
        decompose(Fraction(0, 1), uniform)
        zero_front_rejected = False
    except ValueError:
        zero_front_rejected = True
    audit.check("zero source-coupling front rejected by quotient theorem", zero_front_rejected)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    normalization_gauge = read(NORMALIZATION_GAUGE)
    projective_section = read(PROJECTIVE_SECTION)
    positive_cone = read(POSITIVE_CONE)
    source_coupled = read(SOURCE_COUPLED)
    source_control = read(SOURCE_CONTROL)
    source_strength = read(SOURCE_STRENGTH)
    compression = read(COMPRESSION)
    sl_readout = read(SL_READOUT)
    koide = read(KOIDE)
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    audit.check("goal packet references the new quotient support", NOTE.name in goal)
    audit.check("route triage references the new quotient support", NOTE.name in route)
    audit.check("normalization gauge names the rescaling freedom", "(h, j) -> (h/lambda, lambda j)" in normalization_gauge)
    audit.check("projective section names sigma formula", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("positive-cone support separates signed probes from source strengths", "Signed or complex" in positive_cone and "source strengths are nonnegative" in positive_cone)
    audit.check("source-coupled support names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("source-control support names raw additivity", "J(j_A + j_B) = J(j_A) + J(j_B)" in source_control)
    audit.check("source-strength support names total strength section", "mu(C) = 1" in source_strength)
    audit.check("compression support still requires interface ratification", "normalized label-free charged-lepton full-cell source-probe interface" in compression)
    audit.check(
        "S_l readout bridge keeps convention explicit",
        "source-readout convention" in sl_readout and "S_l = sigma([j])_c" in sl_readout,
    )
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
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is the full-cell source",
        "No derivation that charged-lepton source strength is physically a nonzero",
        "No derivation or ratification that the quotient `H` plus `sigma([j])`",
        "No derivation that `S_l = sigma([j])_c`.",
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
        "This note retains the quotient",
        "source-coupling quotient is retained",
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
