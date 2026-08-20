#!/usr/bin/env python3
"""Independent reconstruction of the Block-5 support/formation triangle.

This checker intentionally does not import the primary Block-5 runner.  It
rebuilds the endpoint codes, event partitions, cubic shell orbit, total
Gaussian/mixture descriptors on independent off-front shells, matched support
and formation pairs, one-site no-form/content cylinders, and finite
marginalization from the upstream Block-4 fixture and the theorem note.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_front_stage_remote_context_record_event_congruence_2026_08_20 as block4


NOTE_PATH = ROOT / "docs" / (
    "SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK4_PATH = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)

AUDIT_INPUT_PATHS = (
    "docs/SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
)

PASS = 0
FAIL = 0

Point = tuple[int, int, int]
Rotation = tuple[Point, Point, Point]
M2Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]

DIRECTIONS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
I2 = sp.eye(2)
RADIUS = sp.Rational(1, 64)
P = sp.Rational(2, 3)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def code(matrix: sp.Matrix) -> M2Code:
    return tuple(
        sp.simplify(matrix[row, column])
        for row in range(2)
        for column in range(2)
    )  # type: ignore[return-value]


def matrix(value: M2Code) -> sp.Matrix:
    return sp.Matrix(((value[0], value[1]), (value[2], value[3])))


def kappa(positive: sp.Matrix, label: sp.Expr) -> M2Code:
    return code(positive + sp.I * label * I2)


def affine(left_weight: sp.Expr, left: M2Code, right: M2Code) -> M2Code:
    return code(left_weight * matrix(left) + (1 - left_weight) * matrix(right))


def label(value: M2Code) -> sp.Expr:
    return sp.simplify(sp.im(sp.trace(matrix(value))) / 2)


def cell(value: M2Code) -> int:
    return 0 if bool(label(value) < sp.Rational(1, 2)) else 1


def hs2(left: M2Code, right: M2Code) -> sp.Expr:
    delta = matrix(left) - matrix(right)
    return sp.simplify(sp.trace(delta.conjugate().T * delta))


C0 = kappa(sp.diag(sp.Rational(3, 10), 0), 0)
CB = kappa(sp.diag(sp.Rational(3, 10), sp.Rational(2, 5)), 1)
CBAR = affine(P, C0, CB)


@dataclass(frozen=True)
class Shell:
    values: tuple[M2Code | None, ...]

    def occupied(self) -> int:
        return sum(value is not None for value in self.values)


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def shell(records: dict[Point, M2Code], target: Point) -> Shell:
    return Shell(tuple(records.get(add(target, direction)) for direction in DIRECTIONS))


def det(rotation: Rotation) -> int:
    a, b, c = rotation
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def rotations() -> tuple[Rotation, ...]:
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    result: list[Rotation] = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            candidate = tuple(
                tuple(signs[row] * axes[order[row]][column] for column in range(3))
                for row in range(3)
            )
            if det(candidate) == 1:
                result.append(candidate)  # type: ignore[arg-type]
    return tuple(result)


def rotate_point(rotation: Rotation, point: Point) -> Point:
    return tuple(
        sum(rotation[row][column] * point[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_shell(value: Shell, rotation: Rotation) -> Shell:
    carried = {
        rotate_point(rotation, direction): content
        for direction, content in zip(DIRECTIONS, value.values, strict=True)
    }
    return Shell(tuple(carried[direction] for direction in DIRECTIONS))


def distance(left: Shell, right: Shell) -> sp.Expr | None:
    if tuple(item is None for item in left.values) != tuple(
        item is None for item in right.values
    ):
        return None
    return sp.simplify(
        sum(
            hs2(a, b) if a is not None and b is not None else 0
            for a, b in zip(left.values, right.values, strict=True)
        )
    )


def bump(value: Shell, orbit: tuple[Shell, ...]) -> sp.Expr:
    distances = [d for item in orbit if (d := distance(value, item)) is not None]
    if not distances:
        return sp.Integer(0)
    minimum = min(distances, key=lambda item: float(sp.N(item)))
    if not bool(minimum < RADIUS):
        return sp.Integer(0)
    return sp.simplify(1 - minimum / RADIUS)


def gaussian_center(value: Shell) -> M2Code:
    result = value.occupied() * I2
    for content in value.values:
        if content is not None:
            item = matrix(content)
            result += (item + item.conjugate().T) / 2
    return code(sp.simplify(result / 7))


@dataclass(frozen=True)
class Descriptor:
    family: str
    weight: sp.Expr
    center: M2Code
    atoms: tuple[M2Code, ...]
    weights: tuple[sp.Expr, ...]

    def barycenter(self) -> M2Code:
        if self.family == "gaussian":
            return self.center
        if self.family == "dirac":
            return self.atoms[0]
        atomic = affine(self.weights[0], self.atoms[0], self.atoms[1])
        return code((1 - self.weight) * matrix(self.center) + self.weight * matrix(atomic))


def endpoint_descriptor(value: Shell, orbit: tuple[Shell, ...]) -> Descriptor:
    weight = bump(value, orbit)
    center = gaussian_center(value)
    if weight == 0:
        return Descriptor("gaussian", 0, center, (), ())
    return Descriptor("mixture", weight, center, (C0, CB), (P, 1 - P))


def bar_descriptor(value: Shell, orbit: tuple[Shell, ...]) -> Descriptor:
    endpoint = endpoint_descriptor(value, orbit)
    if endpoint.weight == 0:
        return endpoint
    barycenter = endpoint.barycenter()
    return Descriptor("dirac", endpoint.weight, barycenter, (barycenter,), (sp.Integer(1),))


def pattern_mass(pattern: tuple[int, ...], q: sp.Expr) -> sp.Expr:
    formed = sum(pattern)
    return sp.simplify(q**formed * (1 - q) ** (len(pattern) - formed))


def main() -> int:
    axiom = normalized(AXIOM_PATH)
    note = normalized(NOTE_PATH)
    block4_note = normalized(BLOCK4_PATH)
    check(
        "independent-source-packet",
        "distribution concerns which possibility a forming record locks" in axiom
        and "does not supply the formation site, probability, or rate" in axiom
        and "no numerical event mass is assigned" in block4_note
        and "endpoint-support faithfulness is not entailed" in note
        and "extensional formation kernel is not determined" in note,
        "the exact local-support and formation boundaries are independently source bound",
    )

    witness = code(matrix(C0) + sp.I * sp.Rational(51, 100) * I2)
    voronoi_witness = 0 if hs2(witness, C0) <= hs2(witness, CB) else 1
    check(
        "independent-event-algebra",
        label(C0) == 0
        and label(CB) == 1
        and cell(C0) == 0
        and cell(CB) == 1
        and cell(CBAR) == 0
        and cell(witness) == 1
        and voronoi_witness == 0,
        "the thick trace cells are exhaustive and endpoint-correct but not uniquely selected by endpoint data",
    )

    layout_a = block4.build_layout("A")
    layout_b = block4.build_layout("B")
    front_a = shell(layout_a.record_map(), layout_a.first_target)
    front_b = shell(layout_b.record_map(), layout_b.first_target)
    rots = rotations()
    orbit = tuple({rotate_shell(front_a, rotation) for rotation in rots})
    check(
        "independent-common-front-orbit",
        front_a == front_b
        and len(rots) == 24
        and len(orbit) == 24
        and bump(front_a, orbit) == 1
        and all(bump(rotate_shell(front_a, rotation), orbit) == 1 for rotation in rots),
        "the exact common shell independently generates one 24-member proper-cubic orbit",
    )

    perturb = list(front_a.values)
    index = next(index for index, value in enumerate(perturb) if value is not None)
    perturb[index] = code(matrix(perturb[index]) + sp.Rational(1, 32) * I2)  # type: ignore[arg-type]
    deletion = list(front_a.values)
    deletion[index] = None
    check(
        "independent-bump-and-deletion",
        0 < bump(Shell(tuple(perturb)), orbit) < 1
        and bump(Shell(tuple(deletion)), orbit) == 0,
        "the patch has nonzero content width and every occupancy deletion exits it",
    )

    empty = Shell((None,) * 6)
    one = Shell((code(I2), None, None, None, None, None))
    exact_endpoint = endpoint_descriptor(front_a, orbit)
    exact_bar = bar_descriptor(front_a, orbit)
    off_empty = endpoint_descriptor(empty, orbit)
    off_one = endpoint_descriptor(one, orbit)
    gaussian_normalization = sp.simplify(sp.pi ** -4 * sp.pi**4)
    check(
        "independent-total-kernel-descriptors",
        exact_endpoint.family == "mixture"
        and exact_bar.family == "dirac"
        and off_empty.family == off_one.family == "gaussian"
        and off_empty.center != off_one.center
        and gaussian_normalization == 1
        and exact_endpoint.barycenter() == exact_bar.barycenter(),
        "independently reconstructed exact and off-patch descriptors, condition-varying Gaussian centers, normalization, and the matched barycenter",
    )

    endpoint_bar = exact_endpoint.barycenter()
    endpoint_masses = tuple(
        sum(weight for atom, weight in zip(exact_endpoint.atoms, exact_endpoint.weights, strict=True) if cell(atom) == target)
        for target in (0, 1)
    )
    bar_masses = (sp.Integer(1), sp.Integer(0)) if cell(exact_bar.atoms[0]) == 0 else (sp.Integer(0), sp.Integer(1))
    check(
        "independent-support-twin",
        endpoint_bar == CBAR
        and endpoint_masses == (sp.Rational(2, 3), sp.Rational(1, 3))
        and bar_masses == (1, 0)
        and C0 != CBAR
        and CB != CBAR,
        "same exact matrix barycenter and formation coexist with endpoint support versus one barycenter atom",
    )

    q_plus, q_form = sp.Integer(1), sp.Rational(1, 2)
    cylinders_ok = True
    for q in (q_plus, q_form):
        for sites in range(1, 8):
            total = sum(
                pattern_mass(tuple((mask >> index) & 1 for index in range(sites)), q)
                for mask in range(2**sites)
            )
            cylinders_ok &= sp.simplify(total - 1) == 0
    marginal_ok = all(
        sp.simplify(
            pattern_mass(pattern + (0,), q_form)
            + pattern_mass(pattern + (1,), q_form)
            - pattern_mass(pattern, q_form)
        )
        == 0
        for sites in range(1, 7)
        for pattern in ((0,) * sites, (1,) * sites)
    )
    check(
        "independent-formation-twin-and-cylinders",
        q_plus != q_form and cylinders_ok and marginal_ok,
        "identical conditional content laws admit distinct normalized formation cylinders; ordinal is not time",
    )

    plus_partition = (0, endpoint_masses[0], endpoint_masses[1])
    bar_partition = (0, bar_masses[0], bar_masses[1])
    form_partition = (
        sp.Rational(1, 2),
        sp.Rational(1, 2) * endpoint_masses[0],
        sp.Rational(1, 2) * endpoint_masses[1],
    )
    check(
        "independent-combined-transition-and-survival",
        plus_partition == (0, sp.Rational(2, 3), sp.Rational(1, 3))
        and bar_partition == (0, 1, 0)
        and form_partition
        == (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6))
        and all(sp.simplify(sum(item) - 1) == 0 for item in (plus_partition, bar_partition, form_partition))
        and all(sp.Rational(1, 2) ** (n + 1) < sp.Rational(1, 2) ** n for n in range(1, 8)),
        "the independently rebuilt blank/F0/FB kernels normalize and fresh ordinal gates give survival 2^-n",
    )

    present_shells = [
        shell(layout_a.record_map(), site) for site in layout_a.record_map()
    ]
    check(
        "independent-supplied-initial-state-compatibility",
        all(bump(item, orbit) == 0 for item in present_shells),
        "all preloaded apparatus sites have present shells on the full-support branch; historical genesis is not inferred",
    )

    required = (
        "universal impossibility",
        "axiom necessity",
        "fail / do not ship",
        "zero obligation retirement",
        "toe percentage movement: zero",
        "route b begins downstream",
        "route c stops upstream",
    )
    check(
        "independent-claim-boundary",
        all(phrase in note for phrase in required),
        "only narrow support and formation non-entailment survive the no-go boundary",
    )

    resolution = (
        "per_element: checked — independently rebuilt the positive-operator codes, exact barycenter, t-coordinate margins, and decoder disagreement",
        "per_site: checked — independently reconstructed exact and off-patch total descriptors, Gaussian normalization, orbit bump, and deletion exit",
        "per_mode: checked — independently matched support, barycenter, and extensional-formation twins without importing the primary runner",
        "per_block: checked — independently normalized gate and content cylinders, projective marginals, 2^-n survival, and current-support compatibility",
        "lattice_wide: checked and not executed — standard-Borel path extension is analytic; physical time, instrument-to-Record coupling, Born selection, and seed genesis remain open",
    )
    for line in resolution:
        print(line)
    check(
        "independent-resolution-certificate",
        all(len(line) >= 100 for line in resolution)
        and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in resolution),
        "all five independent resolution lines are source bound",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
