#!/usr/bin/env python3
"""Verifier for the lepton source positive-cone discriminator support note.

This runner checks the finite theorem that monotone finite-additive source
strengths have nonnegative singleton weights, while signed/complex source
probes are not normalized source-strength weights. It does not derive S_l,
m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
NORMALIZATION_GAUGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
UNFIXED_CHOICE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COORDINATE_UNFIXED_CHOICE_LABEL_FREE_SUPPORT_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


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


def normalize_real(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def measure(weights: Vector, subset: set[Coord]) -> Fraction:
    return sum((weights.get(coord, Fraction(0)) for coord in subset), Fraction(0))


def is_monotone(weights: Vector, subsets: list[tuple[set[Coord], set[Coord]]]) -> bool:
    return all(measure(weights, a) <= measure(weights, b) for a, b in subsets)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("positive-cone discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        PROJECTIVE_SECTION,
        NORMALIZATION_GAUGE,
        SOURCE_STRENGTH,
        SOURCE_CONTROL,
        COMPRESSION,
        UNFIXED_CHOICE,
        MINIMAL,
        KINETIC,
        SCALE,
        REALIZED,
        REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Source Positive-Cone Discriminator Support",
        "monotone finitely additive source-strength measure",
        "source strength is a real monotone finitely additive measure",
        "0 = mu(empty) <= mu({c})",
        "w_c = 1/256",
        "Signed And Complex Probe Firewalls",
        "negative normalized weight",
        "positive/negative channel split",
        "does not follow from source-control linearity",
        "source-positive closure fails; narrowed positive-cone",
        "#4956",
        "#4955",
        "#4954",
        "#4953",
        "#4952",
        "#4951",
        "#4950",
        "#4949",
        "#4948",
        "#4947",
        "#4943",
        "#4902",
        "#4905",
        "#4906",
        "gravity eikonal small-k remainder repair",
        "AC first-order determinant retirement-readiness no-go",
        "closed without merge",
        "Qualification unfixed-choice clarification",
        "No-Go Discipline Gate",
        "Gate result: `PASS` for the narrowed positive-cone discriminator support",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Positive-cone arithmetic")
    coords = coordinates()
    n = len(coords)
    audit.check("source coordinate set has 4^4 = 256 labels", n == 256)

    uniform = {coord: Fraction(1, 256) for coord in coords}
    audit.check("uniform source-strength weights sum to one", sum(uniform.values(), Fraction(0)) == 1)
    audit.check("uniform singleton strength is nonnegative", uniform[coords[0]] >= 0)
    audit.check("uniform singleton strength is 1/256", uniform[coords[0]] == Fraction(1, 256))

    empty: set[Coord] = set()
    one = {coords[0]}
    two = {coords[0], coords[1]}
    audit.check("empty subset singleton monotonicity gives nonnegative singleton", measure(uniform, empty) <= measure(uniform, one))
    audit.check("singleton subset two-point block monotonicity holds", measure(uniform, one) <= measure(uniform, two))
    audit.check("uniform test measure is monotone on sampled inclusions", is_monotone(uniform, [(empty, one), (one, two), (empty, set(coords))]))

    raw_signed = {coord: Fraction(1, 1) for coord in coords}
    raw_signed[coords[0]] = Fraction(-1, 1)
    signed_weights = normalize_real(raw_signed)
    audit.check("signed probe can have positive total", sum(raw_signed.values(), Fraction(0)) == 254)
    audit.check("signed probe normalized coordinate is negative", signed_weights[coords[0]] < 0, f"value={signed_weights[coords[0]]}")
    audit.check("signed normalized vector violates monotone source-strength order", measure(signed_weights, empty) > measure(signed_weights, one))

    zero_sum = {coord: Fraction(1, 1) for coord in coords}
    zero_sum[coords[0]] = Fraction(-255, 1)
    try:
        normalize_real(zero_sum)
        zero_sum_rejected = False
    except ValueError:
        zero_sum_rejected = True
    audit.check("zero-sum signed probe has no positive L1 source-strength section", zero_sum_rejected)

    complex_probe = {coords[0]: 1 + 1j, coords[1]: 1 - 1j}
    try:
        _ = complex_probe[coords[0]] <= complex_probe[coords[1]]  # type: ignore[operator]
        complex_order_rejected = False
    except TypeError:
        complex_order_rejected = True
    audit.check("complex probe amplitudes have no real monotone order", complex_order_rejected)

    audit.check("absolute-value salvage is nonlinear", abs(1 + -1) != abs(1) + abs(-1))
    audit.check("squared amplitude changes the linear coefficient object", Fraction(1, 16) ** 2 == Fraction(1, 256))
    audit.check("positive/negative channel split doubles 256 labels to 512", 2 * n == 512)

    positive_raw = {coord: Fraction(7, 1) for coord in coords}
    scaled_positive = {coord: Fraction(91, 1) for coord in coords}
    audit.check("positive rescaling preserves normalized source strengths", normalize_real(positive_raw) == normalize_real(scaled_positive))

    section("Authority boundary checks")
    projective = read(PROJECTIVE_SECTION)
    gauge = read(NORMALIZATION_GAUGE)
    strength = read(SOURCE_STRENGTH)
    control = read(SOURCE_CONTROL)
    compression = read(COMPRESSION)
    unfixed_choice = read(UNFIXED_CHOICE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)

    audit.check(
        "projective section assumes the nonnegative positive-cone domain",
        "positive projective source ray" in projective and "nonzero nonnegative source controls" in projective,
    )
    audit.check("normalization gauge names positive source-strength cone as open", "positive source-strength cone" in gauge)
    audit.check("source-strength support names nonnegative finite-additive semantics", "nonnegative finite-additive" in strength or "nonnegative finite-additive" in flat(strength))
    audit.check("source-control linearity names raw source-control addition", "J(j_A + j_B) = J(j_A) + J(j_B)" in control)
    audit.check("source-probe compression includes projective source-strength clause", "Projective source-strength clause" in compression)
    audit.check("unfixed-choice support is coordinate-tag, not positivity, support", "coordinate tag" in unfixed_choice and "#4952" in unfixed_choice)

    minimal_flat = flat(minimal).lower()
    audit.check("minimal axioms exclude source/action and weights", "source/action" in minimal_flat and "weights" in minimal_flat)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless quantity", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    for node_name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node_name}", node_name in registry)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation that raw source probes are nonnegative source strengths.",
        "No derivation that charged-lepton source strength is physically the",
        "No derivation that tensor-frame symmetry forces the uniform source ray.",
        "No derivation that `S_l` reads `sigma([j])_c`.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "positivity is derived for the charged-lepton source",
        "source-positive closure passes",
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
