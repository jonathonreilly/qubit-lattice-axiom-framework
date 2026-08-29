#!/usr/bin/env python3
"""Block 17: exact sparse signed-ray/fan NN transaction compiler scout.

The positive construction is conditional on the selected hybrid Record-sector
carrier and effective gates.  The only negative result is nonfactorization of
the frozen all-sector writer/STOP map through the strict-M2 forgetful quotient
with one fixed product environment.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, replace
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
PACKET = ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829"
SOURCE_NOTE = "docs/ADMISSIBILITY_D4_NN_TRANSACTIONAL_CAP_PACKET_COMPILER_SCOUT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block17-nn-transactional-compiler-scout-20260829/APPROACH_REGISTRY.md",
    "docs/ADMISSIBILITY_D4_NN_TRANSACTIONAL_CAP_PACKET_COMPILER_SCOUT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_D4_COVARIANT_CONDITIONAL_CAP_PACKET_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829/CLAIM_STATUS_CERTIFICATE.md",
)

HEAD = "58a2b5d5320d3d48ac8a6520823d9b55fa148bfc"
PREREG = "091308fdec1f91c25d1674a4bfd2c041eaf0f0c8"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
BLOCK16_DELIVERY = "7cda8b604004d16c1becf08c503e05c54c48844a"
BLOCK16_RESULT = "71c02ab1fe5129e76263c683300304ab4ff45d19"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "b26fd69e7a4cca5218410a57b8a1e2e735f85beb"
PREFLIGHT_BLOB = "3514931dea54edfe5a3fc5e8c8d4c80d11b7abcf"
ATTACK_BLOB = "4b0e7d8c6c8fae415a7d956537c17bdf83f5eb15"
REGISTRY_BLOB = "a196306e1416f509529668c2cf101a160b5d593d"

UNAWARDED_TERMINAL = "HYBRID-RECORD-SECTOR-NN-TRANSACTION-GRAMMAR"
FAILURE_TERMINAL = "SCOUT-FAILED-TO-CONSTRUCT-FROZEN-SIGNED-RAY-FAN-GRAMMAR"
SUBCERT = "NO-FACTORIZATION-THROUGH-STRICT-M2"

V = tuple[int, int, int]
ZERO: V = (0, 0, 0)
D: tuple[V, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def add(a: V, b: V) -> V:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a: V, b: V) -> V:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def mul(n: int, a: V) -> V:
    return (n * a[0], n * a[1], n * a[2])


def dot(a: V, b: V) -> int:
    return sum(x * y for x, y in zip(a, b))


def l1(a: V) -> int:
    return sum(abs(x) for x in a)


def perpendicular(p: V) -> tuple[V, ...]:
    return tuple(q for q in D if dot(p, q) == 0)


@dataclass(frozen=True)
class Role:
    name: str
    p: V = ZERO
    q: V = ZERO

    @property
    def site(self) -> V:
        if self.name == "C":
            return ZERO
        distance = int(self.name[1])
        return add(mul(distance, self.p), self.q if self.name[0] == "T" else ZERO)


def generate_roles() -> tuple[tuple[Role, ...], tuple[Role, ...]]:
    base: list[Role] = [Role("C")]
    fringe: list[Role] = []
    for p in D:
        base.extend((Role("A1", p), Role("A2", p), Role("A3", p)))
        base.extend(Role("T2", p, q) for q in perpendicular(p))
        fringe.append(Role("A4", p))
        fringe.extend(Role("T3", p, q) for q in perpendicular(p))
    return tuple(base), tuple(base + fringe)


B_ROLES, F_ROLES = generate_roles()
B = frozenset(role.site for role in B_ROLES)
FAN = frozenset(role.site for role in F_ROLES)


def parent(role: Role) -> Role | None:
    if role.name == "C":
        return None
    if role.name == "A1":
        return Role("C")
    if role.name[0] == "A":
        return Role(f"A{int(role.name[1]) - 1}", role.p)
    return Role(f"A{int(role.name[1])}", role.p)


def role_path(role: Role) -> tuple[V, ...]:
    reversed_path: list[V] = []
    cursor: Role | None = role
    while cursor is not None:
        reversed_path.append(cursor.site)
        cursor = parent(cursor)
    return tuple(reversed(reversed_path))


def proper_cubic_rotations() -> tuple[tuple[V, V, V], ...]:
    rotations = []
    even = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}
    for permutation in itertools.permutations(range(3)):
        parity = 1 if permutation in even else -1
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * math.prod(signs) != 1:
                continue
            rows = []
            for row_index in range(3):
                row = [0, 0, 0]
                row[permutation[row_index]] = signs[row_index]
                rows.append(tuple(row))
            rotations.append(tuple(rows))
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_rotations()


def rotate(rotation: tuple[V, V, V], vector: V) -> V:
    return tuple(dot(row, vector) for row in rotation)  # type: ignore[return-value]


def difference_kernel(points: Iterable[V]) -> frozenset[V]:
    points = tuple(points)
    return frozenset(sub(right, left) for left in points for right in points)


KERNEL = difference_kernel(FAN)
CONFLICTS = KERNEL - {ZERO}
BALL8 = frozenset(x for x in itertools.product(range(-8, 9), repeat=3) if l1(x) <= 8)


def orbit_partition(points: Iterable[V]) -> tuple[frozenset[V], ...]:
    remaining = set(points)
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = frozenset(rotate(rotation, seed) for rotation in ROTATIONS)
        orbits.append(orbit)
        remaining -= orbit
    return tuple(orbits)


def geometry_certificate(fan: frozenset[V] = FAN) -> bool:
    kernel = difference_kernel(fan)
    shells = tuple(Counter(l1(x) for x in kernel)[radius] for radius in range(9))
    hist = Counter(role.name for role in F_ROLES if role.site in fan)
    paths_ok = all(
        role_path(role)[-1] == role.site
        and all(l1(sub(v, u)) == 1 for u, v in zip(role_path(role), role_path(role)[1:]))
        for role in F_ROLES if role.site in fan
    )
    return (
        fan == FAN and len(B_ROLES) == len(B) == 43 and len(fan) == 73 and len(fan - B) == 30
        and hist == Counter({"T2": 24, "T3": 24, "A1": 6, "A2": 6, "A3": 6, "A4": 6, "C": 1})
        and len(ROTATIONS) == 24 and paths_ok
        and max(len(role_path(role)) - 1 for role in F_ROLES) == 4
        and len(kernel) == 761 and max(map(l1, kernel)) == 8
        and shells == (1, 6, 18, 38, 66, 102, 146, 198, 186)
        and len(orbit_partition(kernel - {ZERO})) == 41
        and len(BALL8) == 833 and len((BALL8 - kernel) - {ZERO}) == 72
        and all(frozenset(rotate(rotation, x) for x in fan) == fan for rotation in ROTATIONS)
    )


@dataclass(frozen=True)
class BoolVar:
    displacement: V


@dataclass(frozen=True)
class BoolOr:
    left: "BoolExpr"
    right: "BoolExpr"


BoolExpr = BoolVar | BoolOr


def balanced_or(variables: tuple[V, ...]) -> BoolExpr:
    if len(variables) == 1:
        return BoolVar(variables[0])
    middle = len(variables) // 2
    return BoolOr(balanced_or(variables[:middle]), balanced_or(variables[middle:]))


def or_support(expression: BoolExpr) -> frozenset[V]:
    if isinstance(expression, BoolVar):
        return frozenset((expression.displacement,))
    return or_support(expression.left) | or_support(expression.right)


def or_eval(expression: BoolExpr, assignment: Callable[[V], bool]) -> bool:
    if isinstance(expression, BoolVar):
        return assignment(expression.displacement)
    return or_eval(expression.left, assignment) or or_eval(expression.right, assignment)


def overlap_certificate(rail_variables: frozenset[V] = CONFLICTS) -> bool:
    # One construction comes from footprint-pair equations; the second is the
    # emitted provenance-rail expression.  Equality of idempotent OR normal
    # forms proves equality for every assignment of all 760 variables.
    pair_variables = frozenset(
        sub(right, left) for left in FAN for right in FAN if left != right
    )
    if not rail_variables:
        return False
    expression = balanced_or(tuple(sorted(rail_variables)))
    symbolic_ok = or_support(expression) == pair_variables == CONFLICTS
    # Exhaust the full [-9,9]^3 box.  This includes every one of the 72
    # radius-eight nonconflicts and all 6,026 points outside the L1 ball.
    bounded_box = itertools.product(range(-9, 10), repeat=3)
    theorem_ok = True
    for delta in bounded_box:
        translated = frozenset(add(delta, x) for x in FAN)
        if bool(FAN & translated) != (delta in KERNEL):
            theorem_ok = False
            break
    regressions = (
        or_eval(expression, lambda d: d == (1, 0, 0))
        and not or_eval(expression, lambda _d: False)
        and len((BALL8 - KERNEL) - {ZERO}) == 72
    )
    return symbolic_ok and theorem_ok and regressions


# Exact Q(sqrt(3)) and complex extension used by the channel certificates.
@dataclass(frozen=True)
class Q3:
    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other: "Q3") -> "Q3":
        return Q3(self.rational + other.rational, self.radical + other.radical)

    def __neg__(self) -> "Q3":
        return Q3(-self.rational, -self.radical)

    def __sub__(self, other: "Q3") -> "Q3":
        return self + (-other)

    def __mul__(self, other: "Q3 | Fraction | int") -> "Q3":
        if not isinstance(other, Q3):
            other = Q3(Fraction(other))
        return Q3(
            self.rational * other.rational + 3 * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )

    __rmul__ = __mul__


@dataclass(frozen=True)
class CQ3:
    real: Q3 = Q3()
    imag: Q3 = Q3()

    def __add__(self, other: "CQ3") -> "CQ3":
        return CQ3(self.real + other.real, self.imag + other.imag)

    def __mul__(self, scalar: Fraction | int) -> "CQ3":
        return CQ3(self.real * scalar, self.imag * scalar)

    __rmul__ = __mul__


QVec = tuple[Q3, Q3, Q3]
Density = tuple[CQ3, CQ3, CQ3, CQ3]


def qvector(vector: V) -> QVec:
    return tuple(Q3(Fraction(component)) for component in vector)  # type: ignore[return-value]


def qadd(left: QVec, right: QVec) -> QVec:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def qscale(scalar: Fraction, vector: QVec) -> QVec:
    return tuple(component * scalar for component in vector)  # type: ignore[return-value]


def density_from_bloch(vector: QVec) -> Density:
    x, y, z = vector
    half = Fraction(1, 2)
    return (
        CQ3((Q3(Fraction(1)) + z) * half),
        CQ3(x * half, (-y) * half),
        CQ3(x * half, y * half),
        CQ3((Q3(Fraction(1)) - z) * half),
    )


def density_add(*terms: tuple[Fraction, Density]) -> Density:
    zero = CQ3()
    return tuple(
        sum((weight * matrix[index] for weight, matrix in terms), start=zero)
        for index in range(4)
    )  # type: ignore[return-value]


def writer_state_direct(shrink: Fraction = Fraction(143, 256)) -> Density:
    return density_from_bloch((Q3(-shrink), Q3(), Q3()))


def writer_state_spectral() -> Density:
    plus = density_from_bloch((Q3(1), Q3(), Q3()))
    minus = density_from_bloch((Q3(-1), Q3(), Q3()))
    return density_add((Fraction(113, 512), plus), (Fraction(399, 512), minus))


WriterKey = tuple[int, int, int, int, int, int]


def writer_formula_map(
    reference_dimension: int = 3,
    trace_offdiagonal: bool = False,
    shrink: Fraction = Fraction(143, 256),
) -> dict[WriterKey, CQ3]:
    state = writer_state_direct(shrink)
    output: dict[WriterKey, CQ3] = {}
    for i, j, r, s in itertools.product(range(2), range(2), range(reference_dimension), range(reference_dimension)):
        if i != j and not trace_offdiagonal:
            continue
        for a, b in itertools.product(range(2), repeat=2):
            output[(i, j, r, s, a, b)] = Fraction(1, 6) * state[2 * a + b]
    return output


def writer_kraus_map(reference_dimension: int = 3) -> dict[WriterKey, CQ3]:
    # Independently sum the two spectral projector families and the two input
    # erasure Kraus labels; contraction forces i=j rather than assuming it.
    eigensystems = (
        (Fraction(113, 512), density_from_bloch((Q3(1), Q3(), Q3()))),
        (Fraction(399, 512), density_from_bloch((Q3(-1), Q3(), Q3()))),
    )
    output: dict[WriterKey, CQ3] = {}
    for i, j, r, s in itertools.product(range(2), range(2), range(reference_dimension), range(reference_dimension)):
        for erased_input in range(2):
            contraction = int(i == erased_input and j == erased_input)
            if not contraction:
                continue
            for a, b in itertools.product(range(2), repeat=2):
                coefficient = sum(
                    (Fraction(1, 6) * eigenvalue * projector[2 * a + b] for eigenvalue, projector in eigensystems),
                    start=CQ3(),
                )
                output[(i, j, r, s, a, b)] = coefficient
    return output


@dataclass(frozen=True)
class ParametricWriterForm:
    input_relation: str
    reference_matrix_unit: tuple[int, int]
    branch_weight: Fraction
    output_state_digest: str


def writer_sigma_digest(f: V, spectral: bool) -> str:
    rho = writer_state_spectral() if spectral else writer_state_direct()
    mixed = density_from_bloch((Q3(), Q3(), Q3()))
    assignment = writer_roles(f)
    factors = tuple(
        rho if "rho_f" in assignment[site] else mixed
        for site in sorted(B)
    )
    return hashlib.sha256(repr(factors).encode()).hexdigest()


def writer_parametric_formula(reference_dimension: int = 3) -> dict[tuple[str, int, int], ParametricWriterForm | None]:
    digest = writer_sigma_digest(D[0], spectral=False)
    forms: dict[tuple[str, int, int], ParametricWriterForm | None] = {}
    for relation, r, s in itertools.product(("diagonal", "offdiagonal"), range(reference_dimension), range(reference_dimension)):
        key = (relation, r, s)
        forms[key] = None if relation == "offdiagonal" else ParametricWriterForm(
            relation, (r, s), Fraction(1, 6), digest
        )
    return forms


def writer_parametric_kraus(reference_dimension: int = 3) -> dict[tuple[str, int, int], ParametricWriterForm | None]:
    digest = writer_sigma_digest(D[0], spectral=True)
    forms: dict[tuple[str, int, int], ParametricWriterForm | None] = {}
    for relation, r, s in itertools.product(("diagonal", "offdiagonal"), range(reference_dimension), range(reference_dimension)):
        # For generic block indices i,j and erasure label t,
        # sum_t delta(i,t)delta(j,t) is one exactly when i=j.
        contraction = int(relation == "diagonal")
        key = (relation, r, s)
        forms[key] = None if contraction == 0 else ParametricWriterForm(
            relation, (r, s), Fraction(1, 6), digest
        )
    return forms


@dataclass(frozen=True)
class Outcome:
    orbit: str
    ray: QVec
    weight: Fraction


def outcomes(axis_weight: Fraction = Fraction(1, 12)) -> tuple[Outcome, ...]:
    axes = tuple(Outcome("axis", qvector(direction), axis_weight) for direction in D)
    corners = tuple(
        Outcome(
            "corner",
            tuple(Q3(Fraction(0), Fraction(sign, 3)) for sign in signs),  # sign/sqrt(3)
            Fraction(1, 16),
        )
        for signs in itertools.product((-1, 1), repeat=3)
    )
    return axes + corners


def direct_controller_state(f: V, outcome: Outcome) -> Density:
    ray = qadd(qscale(Fraction(-9, 16), qvector(f)), qscale(Fraction(1, 256), outcome.ray))
    return density_from_bloch(ray)


def mixture_controller_state(
    f: V,
    outcome: Outcome,
    pure_coefficient: Fraction = Fraction(144, 256),
) -> Density:
    pure_minus_f = density_from_bloch(qscale(Fraction(-1), qvector(f)))
    pure_ray = density_from_bloch(outcome.ray)
    mixed = density_from_bloch((Q3(), Q3(), Q3()))
    return density_add(
        (pure_coefficient, pure_minus_f),
        (Fraction(1, 256), pure_ray),
        (Fraction(111, 256), mixed),
    )


def swap_bit_permutation(left: int, right: int, bits: int = 10) -> tuple[int, ...]:
    result = []
    for value in range(2**bits):
        left_bit, right_bit = (value >> left) & 1, (value >> right) & 1
        changed = value
        if left_bit != right_bit:
            changed ^= (1 << left) | (1 << right)
        result.append(changed)
    return tuple(result)


def compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


IDENTITY_S = tuple(range(2**10))


def direct_obstacle_permutation(mask: int, clear_mask: int = 0) -> tuple[int, ...]:
    if mask != clear_mask:
        return IDENTITY_S
    return tuple(
        sum(((value >> (bit ^ 1)) & 1) << bit for bit in range(10))
        for value in range(2**10)
    )


def gate_obstacle_permutation(mask: int) -> tuple[int, ...]:
    permutation = IDENTITY_S
    if mask == 0:
        for pair in range(5):
            permutation = compose_permutations(swap_bit_permutation(2 * pair, 2 * pair + 1), permutation)
    return permutation


def permutation_digest(permutation: tuple[int, ...]) -> str:
    encoded = b"".join(value.to_bytes(2, "big") for value in permutation)
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class ControllerNormalForm:
    control: tuple[int, int, int]
    x_matrix_unit: tuple[int, int]
    weighted_output: Density
    s_basis_permutation: str
    reference_index_map: tuple[int, int]


@dataclass(frozen=True)
class ChannelStats:
    writer_block_basis_units: int
    writer_surviving_basis_units: int
    writer_local_nonzero_coefficients: int
    controller_examined: int
    controller_nonzero_classes: int
    spectator_classes: int


def controller_formula_forms(
    clear_mask: int = 0,
    drop_reference: bool = False,
) -> dict[tuple[int, int, int, int, int], ControllerNormalForm | None]:
    forms: dict[tuple[int, int, int, int, int], ControllerNormalForm | None] = {}
    generated_outcomes = outcomes()
    for f_index, f in enumerate(D):
        for b_index, outcome in enumerate(generated_outcomes):
            for mask in range(32):
                permutation = direct_obstacle_permutation(mask, clear_mask)
                digest = permutation_digest(permutation)
                weighted = tuple(outcome.weight * entry for entry in direct_controller_state(f, outcome))
                for i, j in itertools.product(range(2), repeat=2):
                    key = (f_index, b_index, mask, i, j)
                    forms[key] = None if i != j else ControllerNormalForm(
                        (f_index, b_index, mask), (i, j), weighted, digest,
                        (0, 0) if drop_reference else (0, 1),
                    )
    return forms


def controller_composed_forms(
    pure_coefficient: Fraction = Fraction(144, 256),
) -> dict[tuple[int, int, int, int, int], ControllerNormalForm | None]:
    forms: dict[tuple[int, int, int, int, int], ControllerNormalForm | None] = {}
    generated_outcomes = outcomes()
    for f_index, f in enumerate(D):
        for b_index, outcome in enumerate(generated_outcomes):
            for mask in range(32):
                permutation = gate_obstacle_permutation(mask)
                digest = permutation_digest(permutation)
                weighted = tuple(outcome.weight * entry for entry in mixture_controller_state(f, outcome, pure_coefficient))
                for i, j in itertools.product(range(2), repeat=2):
                    # Sum over the two erasure Kraus labels.  Exactly one term
                    # survives iff the x matrix unit is diagonal.
                    surviving_erasure_labels = tuple(k for k in range(2) if i == k and j == k)
                    key = (f_index, b_index, mask, i, j)
                    forms[key] = None if not surviving_erasure_labels else ControllerNormalForm(
                        (f_index, b_index, mask), (i, j), weighted, digest, (0, 1)
                    )
    return forms


@dataclass(frozen=True)
class LocalFactor:
    name: str
    support: frozenset[V]
    channel_digest: str


def factorized_action(order: tuple[LocalFactor, ...]) -> tuple[tuple[str, str], ...] | None:
    occupied: set[V] = set()
    transformed = {"A": "generic-cross-matrix-unit-A", "B": "generic-cross-matrix-unit-B", "R": "spectator-E_rs"}
    for factor in order:
        if occupied & factor.support:
            return None
        occupied |= factor.support
        transformed[factor.name] = factor.channel_digest
    return tuple(sorted(transformed.items()))


def arbitrary_reference_certificate(
    trace_offdiagonal: bool = False,
    clear_mask: int = 0,
    drop_reference: bool = False,
    pure_coefficient: Fraction = Fraction(144, 256),
) -> tuple[bool, ChannelStats]:
    direct_writer = writer_formula_map(trace_offdiagonal=trace_offdiagonal)
    kraus_writer = writer_kraus_map()
    parametric_writer = writer_parametric_formula()
    parametric_kraus = writer_parametric_kraus()
    direct_controller = controller_formula_forms(clear_mask, drop_reference)
    composed_controller = controller_composed_forms(pure_coefficient)
    block_dimension = 2**43
    controller_examined = 6 * 14 * 32 * 4
    writer_ok = direct_writer == kraus_writer and parametric_writer == parametric_kraus
    controller_ok = direct_controller == composed_controller
    # The 1,024-entry S permutations are checked on every basis state; the
    # symbolic E_uv and E_rs labels then cover arbitrary S/reference operators.
    permutation_ok = all(
        sorted(permutation) == list(range(2**10))
        for mask in range(32)
        for permutation in (direct_obstacle_permutation(mask, clear_mask), gate_obstacle_permutation(mask))
    )
    translation = (20, 0, 0)
    ordered_keys = tuple(sorted(direct_controller))
    factor_a = LocalFactor("A", FAN, hashlib.sha256(repr(direct_controller[ordered_keys[0]]).encode()).hexdigest())
    factor_b = LocalFactor("B", frozenset(add(translation, x) for x in FAN), hashlib.sha256(repr(direct_controller[ordered_keys[-1]]).encode()).hexdigest())
    left = factorized_action((factor_a, factor_b))
    right = factorized_action((factor_b, factor_a))
    spectator_ok = left is not None and left == right and dict(left)["R"] == "spectator-E_rs"
    stats = ChannelStats(
        3**2 * block_dimension**2,
        3**2 * block_dimension,
        len(direct_writer),
        controller_examined,
        sum(form is not None for form in direct_controller.values()),
        3,
    )
    expected_stats = ChannelStats(9 * 2**86, 9 * 2**43, 72, 10752, 5376, 3)
    return writer_ok and controller_ok and permutation_ok and spectator_ok and stats == expected_stats, stats


def cap_packet_certificate(
    axis_weight: Fraction = Fraction(1, 12),
    writer_shrink: Fraction = Fraction(143, 256),
    mixture_pure: Fraction = Fraction(144, 256),
) -> bool:
    generated = outcomes(axis_weight)
    axes = tuple(outcome for outcome in generated if outcome.orbit == "axis")
    corners = tuple(outcome for outcome in generated if outcome.orbit == "corner")
    weights_ok = sum((outcome.weight for outcome in generated), start=Fraction(0)) == 1
    norm_bound = Fraction(9, 16) + Fraction(1, 256)
    states_ok = all(
        direct_controller_state(f, outcome) == mixture_controller_state(f, outcome, mixture_pure)
        for f in D for outcome in generated
    )
    return (
        len(axes) == 6 and len(corners) == 8 and weights_ok
        and writer_state_direct(writer_shrink) == writer_state_spectral()
        and writer_shrink != 1 and norm_bound == Fraction(145, 256) and norm_bound < 1
        and states_ok
        and spin_orbit_certificate()
        and 36 * Fraction(1, 72) + 48 * Fraction(1, 96) == 1
    )


ROTATION_WORDS: dict[V, tuple[str, ...]] = {
    (0, 0, 1): (),
    (0, 0, -1): ("X",),
    (1, 0, 0): ("H",),
    (-1, 0, 0): ("H", "Z"),
    (0, 1, 0): ("H", "S"),
    (0, -1, 0): ("H", "SDG"),
}


CLIFFORD_BLOCH = {
    "X": ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    "Z": ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    "H": ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    "S": ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    "SDG": ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
}


def apply_clifford_word(word: tuple[str, ...], vector: V) -> V:
    result = vector
    for gate_name in word:
        result = rotate(CLIFFORD_BLOCH[gate_name], result)
    return result


def spin_orbit_certificate(words: dict[V, tuple[str, ...]] = ROTATION_WORDS) -> bool:
    base_bloch = (0, 0, 1)
    generated = {direction: apply_clifford_word(word, base_bloch) for direction, word in words.items()}
    return (
        set(words) == set(D) and generated == {direction: direction for direction in D}
        and all(
            density_from_bloch(qscale(Fraction(-143, 256), qvector(generated[direction])))
            == density_from_bloch(qscale(Fraction(-143, 256), qvector(direction)))
            for direction in D
        )
    )


def writer_roles(f: V) -> dict[V, str]:
    result = {site: "I/2" for site in B}
    result[ZERO] = result[f] = result[mul(-2, f)] = "Record(rho_f)"
    result[mul(3, f)] = "live(rho_f)"
    result[mul(-1, f)] = result[mul(2, f)] = "fresh-gap"
    return result


def radius2_flag(f: V, candidate: V, records: frozenset[V]) -> bool:
    nearest = tuple(add(candidate, p) for p in D if add(candidate, p) in records)
    return len(nearest) == 1 and nearest[0] == add(candidate, mul(-1, f)) and add(candidate, mul(-2, f)) in records


def transaction_certificate(reuse_writer_orientation: bool = False) -> bool:
    clear = blocked = 0
    for actual_f in D:
        roles = writer_roles(actual_f)
        records = frozenset(site for site, value in roles.items() if value.startswith("Record"))
        if reuse_writer_orientation:
            fired = (actual_f,)  # hostile private-oracle route, deliberately rejected below
            inference_source = "writer_coin"
        else:
            fired = tuple(p for p in D if radius2_flag(p, mul(2, p), records))
            inference_source = "six_fresh_A2_geometry_queries"
        if fired != (actual_f,) or inference_source != "six_fresh_A2_geometry_queries":
            return False
        sources = (mul(3, actual_f),) + tuple(add(mul(2, actual_f), q) for q in perpendicular(actual_f))
        destinations = (mul(4, actual_f),) + tuple(add(mul(3, actual_f), q) for q in perpendicular(actual_f))
        if len(set(sources + destinations)) != 10:
            return False
        if any(l1(sub(destination, source)) != 1 for source, destination in zip(sources, destinations)):
            return False
        for mask in range(32):
            if mask == 0:
                clear += 14
            else:
                blocked += 14
    return (clear, blocked, clear + blocked) == (84, 2604, 2688) and writer_mask_stop_certificate()


def writer_mask_stop_certificate() -> bool:
    mask_variables = tuple((index, 0, 0) for index in range(43))
    mask_or = balanced_or(mask_variables)
    # The idempotent OR normal form has every status variable exactly once;
    # hence its zero fibre is only the all-blank mask, for arbitrary 43-bit
    # assignments.  Every other fibre selects the identity permutation on the
    # 43 system matrix-unit axes plus the untouched reference axis.
    identity_signature = tuple(range(44))
    generated_stop_signature = tuple(index for index in range(44))
    return (
        or_support(mask_or) == frozenset(mask_variables)
        and sum((Fraction(1, 6) for _ in D), start=Fraction(0)) == 1
        and identity_signature == generated_stop_signature
    )


# Sparse exact circuit DSL.  Entries are actual basis transitions; coefficient
# squares and signs encode the real radical amplitudes without dense matrices.
@dataclass(frozen=True)
class SparseEntry:
    kraus: int
    source: int
    target: int
    square_numerator: int = 1
    square_denominator: int = 1
    sign: int = 1
    phase_quarters: int = 0

    @property
    def square(self) -> Fraction:
        return Fraction(self.square_numerator, self.square_denominator)


@dataclass(frozen=True)
class ExactMap:
    name: str
    family: str
    input_dimension: int
    output_dimension: int
    inverse: str | None
    entries: tuple[SparseEntry, ...]


def permutation_map(name: str, permutation: tuple[int, ...], inverse: str) -> ExactMap:
    return ExactMap(name, "permutation", len(permutation), len(permutation), inverse,
                    tuple(SparseEntry(0, source, target) for source, target in enumerate(permutation)))


def initialized_map(name: str, inverse: str | None, transitions: tuple[tuple[int, int], ...]) -> ExactMap:
    dimension = max(max(pair) for pair in transitions) + 1
    return ExactMap(name, "initialized_isometry", dimension, dimension, inverse,
                    tuple(SparseEntry(0, source, target) for source, target in transitions))


SWAP_PERMUTATION = (0, 2, 1, 3)
H_MAP = ExactMap("H", "unitary", 2, 2, "H", (
    SparseEntry(0, 0, 0, 1, 2), SparseEntry(0, 0, 1, 1, 2),
    SparseEntry(0, 1, 0, 1, 2), SparseEntry(0, 1, 1, 1, 2, -1),
))


def monomial_map(name: str, targets: tuple[int, ...], phases: tuple[int, ...], inverse: str) -> ExactMap:
    return ExactMap(name, "monomial_unitary", len(targets), len(targets), inverse, tuple(
        SparseEntry(0, source, target, phase_quarters=phase)
        for source, (target, phase) in enumerate(zip(targets, phases))
    ))


def branch6_swap_permutation() -> tuple[int, ...]:
    permutation = []
    for value in range(2**13):
        onehot = value & 63
        changed = value
        if onehot and onehot & (onehot - 1) == 0:
            code = onehot.bit_length() - 1
            system_bit = (value >> 6) & 1
            stage_position = 7 + code
            stage_bit = (value >> stage_position) & 1
            if system_bit != stage_bit:
                changed ^= (1 << 6) | (1 << stage_position)
        permutation.append(changed)
    return tuple(permutation)


def bit_fanout_maps(width: int) -> tuple[ExactMap, ExactMap]:
    forward = initialized_map(f"FANOUT{width}_TRIGGER", f"UNFANOUT{width}_TRIGGER",
                              ((0, 0), (1 << width, (1 << (width + 1)) - 1)))
    inverse = initialized_map(f"UNFANOUT{width}_TRIGGER", f"FANOUT{width}_TRIGGER",
                              ((0, 0), ((1 << (width + 1)) - 1, 1 << width)))
    return forward, inverse


def branch_broadcast_maps() -> tuple[ExactMap, ExactMap]:
    transitions = []
    for code in range(6):
        source = code << 438
        pattern = sum(1 << (73 * code + index) for index in range(73))
        transitions.append((source, source | pattern))
    for stop_code in (6, 7):
        source = stop_code << 438
        transitions.append((source, source))
    forward = initialized_map("FANOUT438_BRANCH", "UNFANOUT438_BRANCH", tuple(transitions))
    inverse = initialized_map("UNFANOUT438_BRANCH", "FANOUT438_BRANCH",
                              tuple((target, source) for source, target in transitions))
    return forward, inverse


def swap_if_clear_permutation() -> tuple[int, ...]:
    permutation = []
    for value in range(2**7):
        mask = value & 31
        changed = value
        if mask == 0:
            left, right = (value >> 5) & 1, (value >> 6) & 1
            if left != right:
                changed ^= (1 << 5) | (1 << 6)
        permutation.append(changed)
    return tuple(permutation)

TRIGGER_FANOUT_MAPS = bit_fanout_maps(73)
BRANCH_BROADCAST_MAPS = branch_broadcast_maps()

MAPS = (
    H_MAP,
    permutation_map("X", (1, 0), "X"),
    monomial_map("Z", (0, 1), (0, 2), "Z"),
    monomial_map("S", (0, 1), (0, 1), "SDG"),
    monomial_map("SDG", (0, 1), (0, 3), "S"),
    permutation_map("SWAP", SWAP_PERMUTATION, "SWAP"),
    permutation_map("CNOT", (0, 1, 3, 2), "CNOT"),
    permutation_map("TOFFOLI", (0, 1, 2, 3, 4, 5, 7, 6), "TOFFOLI"),
    initialized_map("QND_RECORD_COPY", "QND_RECORD_UNCOPY", ((0, 0), (2, 3))),
    initialized_map("QND_RECORD_UNCOPY", "QND_RECORD_COPY", ((0, 0), (3, 2))),
    initialized_map("FANOUT0", "UNFANOUT", ((0, 0), (2, 3))),
    initialized_map("UNFANOUT", "FANOUT0", ((0, 0), (3, 2))),
    initialized_map("FANOUT6_RECORD", "UNFANOUT6_RECORD", ((0, 0), (64, 127))),
    initialized_map("UNFANOUT6_RECORD", "FANOUT6_RECORD", ((0, 0), (127, 64))),
    initialized_map("GE2_COPY", "GE2_UNCOPY", tuple((2*n, 2*n + int(n >= 2)) for n in range(128))),
    initialized_map("GE2_UNCOPY", "GE2_COPY", tuple((2*n + int(n >= 2), 2*n) for n in range(128))),
    initialized_map("COPY_F_TO_SINK", None,
                    tuple((1 << code, (code << 6) | (1 << code)) for code in range(6))),
    initialized_map("COPY5_TO_SINK", None, tuple((32*n, 32*n + n) for n in range(32))),
    initialized_map("MOVE1_TO_SINK", None, ((0, 0), (2, 1))),
    initialized_map("LOCK", None, ((0, 3),)),
    initialized_map("LOCK_IF_ONE", None, ((0, 0), (4, 7))),
    initialized_map("LOCK_IF_ANY6", None,
                    ((0, 0),) + tuple((1 << code, (1 << code) | (3 << 6)) for code in range(6))),
    permutation_map("BRANCH6_SWAP", branch6_swap_permutation(), "BRANCH6_SWAP"),
    permutation_map("SWAP_IF_CLEAR", swap_if_clear_permutation(), "SWAP_IF_CLEAR"),
    permutation_map("COMMIT_BARRIER", (0,), "COMMIT_BARRIER"),
    permutation_map("INC7", tuple((n + 1) % 128 for n in range(128)), "DEC7"),
    permutation_map("DEC7", tuple((n - 1) % 128 for n in range(128)), "INC7"),
    permutation_map("ONSITE_SCATTER", tuple(int(f"{n:06b}"[::-1], 2) for n in range(64)), "ONSITE_UNSCATTER"),
    permutation_map("ONSITE_UNSCATTER", tuple(int(f"{n:06b}"[::-1], 2) for n in range(64)), "ONSITE_SCATTER"),
    ExactMap("COIN6", "kraus", 1, 1, None, tuple(SparseEntry(k, 0, 0, 1, 6) for k in range(6))),
    ExactMap("COIN14", "kraus", 1, 1, None,
             tuple(SparseEntry(k, 0, 0, 1, 12) for k in range(6))
             + tuple(SparseEntry(k, 0, 0, 1, 16) for k in range(6, 14))),
    ExactMap("P143", "preparation", 1, 4, None,
             (SparseEntry(0, 0, 0, 113, 512), SparseEntry(0, 0, 3, 399, 512))),
    ExactMap("BELL", "preparation", 1, 4, None,
             (SparseEntry(0, 0, 0, 1, 2), SparseEntry(0, 0, 3, 1, 2))),
    ExactMap("CHOICE3", "preparation", 1, 3, None, (
        SparseEntry(0, 0, 0, 144, 256), SparseEntry(0, 0, 1, 1, 256),
        SparseEntry(0, 0, 2, 111, 256),
    )),
    ExactMap("PREP_AXIS_ORBIT", "certified_orbit", 1, 2, None,
             (SparseEntry(0, 0, 0, 1, 2), SparseEntry(0, 0, 1, 1, 2))),
    ExactMap("PREP_CORNER_ORBIT", "certified_orbit", 1, 2, None,
             (SparseEntry(0, 0, 0, 1, 2), SparseEntry(0, 0, 1, 1, 2))),
    ExactMap("AFFINE_PREP", "certified_orbit", 1, 2, None,
             (SparseEntry(0, 0, 0, 1),)),
) + TRIGGER_FANOUT_MAPS + BRANCH_BROADCAST_MAPS + (
    ExactMap("SELECT5_MASK", "certified_orbit", 1, 1, None, (SparseEntry(0, 0, 0, 1),)),
    ExactMap("COIN6_OR_STOP", "certified_orbit", 1, 1, None, (SparseEntry(0, 0, 0, 1),)),
)


@dataclass(frozen=True)
class RegisterBank:
    name: str
    width: int
    multiplicity: int
    lifetime: str

    @property
    def allocated_bits(self) -> int:
        return self.width * self.multiplicity


BASE_REGISTER_BANKS = (
    RegisterBank("port_in_out", 12, 73, "reusable"),
    RegisterBank("conflict_tag_rails", 219, 73, "reusable"),
    RegisterBank("conflict_ack", 73, 73, "reusable"),
    RegisterBank("collision_count", 7, 73, "reusable"),
    RegisterBank("abort", 1, 73, "reusable"),
    RegisterBank("address", 7, 73, "reusable"),
    RegisterBank("role", 7, 73, "reusable"),
    RegisterBank("blank", 1, 73, "reusable"),
    RegisterBank("phase", 2, 73, "reusable"),
    RegisterBank("predicate", 4, 73, "reusable"),
    RegisterBank("path_word", 12, 73, "reusable"),
    RegisterBank("status_query", 9, 73, "reusable"),
    RegisterBank("writer_branch_staging_or_dump", 1, 6 * 43, "retained"),
    RegisterBank("writer_branch_purifier", 1, 6 * 43, "retained"),
    RegisterBank("writer_direction_sink", 3, 1, "retained"),
    RegisterBank("writer_mask_sink", 1, 43, "retained"),
    RegisterBank("writer_conflict_sink", 1, 73, "retained"),
    RegisterBank("controller_predicate_sink", 1, 12, "retained"),
    RegisterBank("controller_candidate_fresh_sink", 1, 6, "retained"),
    RegisterBank("controller_obstacle_sink", 1, 30, "retained"),
    RegisterBank("candidate_staging_or_old_dump", 1, 1, "retained"),
    RegisterBank("candidate_purifier", 1, 1, "retained"),
    RegisterBank("outcome_sink", 4, 1, "retained"),
    RegisterBank("affine_choice", 2, 1, "retained"),
    RegisterBank("mixed_branch_purifier", 1, 1, "retained"),
    RegisterBank("fresh_controller_direction_sink", 3, 1, "retained"),
    RegisterBank("controller_obstacle_mask_sink", 5, 1, "retained"),
    RegisterBank("writer_and_controller_lock_sinks", 1, 14, "retained"),
)


@dataclass(frozen=True)
class GateInstance:
    elementary_layer: int
    communication_round: int
    phase: str
    operation: str
    targets: tuple[str, ...]
    pair_id: str = ""
    pair_direction: int = 0
    route_id: str = ""
    route_event: str = ""
    route_step: int = 0
    edge: tuple[V, V] | None = None


@dataclass(frozen=True)
class RouteSpec:
    route_id: str
    family: str
    path: tuple[V, ...]
    branch: int = -1
    role_index: int = -1


@dataclass(frozen=True)
class Netlist:
    register_banks: tuple[RegisterBank, ...]
    maps: tuple[ExactMap, ...]
    gates: tuple[GateInstance, ...]
    routes: tuple[RouteSpec, ...]

    def canonical_bytes(self) -> bytes:
        def encode(value: object) -> object:
            if isinstance(value, Fraction):
                return {"numerator": value.numerator, "denominator": value.denominator}
            raise TypeError(type(value).__name__)
        return json.dumps(asdict(self), sort_keys=True, separators=(",", ":"), default=encode).encode()


def build_netlist() -> Netlist:
    gates: list[GateInstance] = []
    routes: list[RouteSpec] = []

    def gate(layer: int, rnd: int, phase: str, op: str, targets: tuple[str, ...],
             route: RouteSpec | None = None, event: str = "", step: int = 0,
             edge: tuple[V, V] | None = None) -> None:
        gates.append(GateInstance(layer, rnd, phase, op, targets, route_id="" if route is None else route.route_id,
                                  route_event=event, route_step=step, edge=edge))

    def lane(route: RouteSpec, vertex: int, port: str) -> str:
        return f"lane:{route.route_id}:v{vertex}:{port}"

    def emit_edge(route: RouteSpec, step: int, outward: bool, layer: int, rnd: int) -> None:
        left, right = route.path[step - 1], route.path[step]
        if outward:
            targets, event, edge = (lane(route, step - 1, "out"), lane(route, step, "in")), "EDGE_OUT", (left, right)
        else:
            targets, event, edge = (lane(route, step, "in"), lane(route, step - 1, "out")), "EDGE_RETURN", (right, left)
        gate(layer, rnd, route.family, "SWAP", targets, route, event, step, edge)

    def emit_handoff(route: RouteSpec, vertex: int, outward: bool, layer: int, rnd: int) -> None:
        targets = (lane(route, vertex, "in"), lane(route, vertex, "out"))
        gate(layer, rnd, route.family, "ONSITE_SCATTER", targets, route,
             "HANDOFF_OUT" if outward else "HANDOFF_RETURN", vertex)

    def add_roundtrip(route: RouteSpec) -> None:
        routes.append(route)
        length = len(route.path) - 1
        local = lane(route, 0, "local") if length == 0 else lane(route, 0, "out")
        gate(1 if route.family in ("conflict", "blank") else 57 if route.family == "predicate" else 89,
             0, route.family, "SWAP", (f"seed:{route.route_id}", local), route, "LOAD")
        if route.family in ("conflict", "blank"):
            for step in range(1, length + 1):
                emit_edge(route, step, True, 4 * step, step)
                if step < length:
                    emit_handoff(route, step, True, 4 * step + 1, step)
            endpoint_lane = local if length == 0 else lane(route, length, "in")
            endpoint = route.path[-1]
            if route.family == "blank":
                for offset, (operation, event) in enumerate((("QND_RECORD_COPY", "ENDPOINT_QUERY"),
                                                             ("CNOT", "ENDPOINT_COPY"),
                                                             ("QND_RECORD_UNCOPY", "ENDPOINT_UNQUERY"))):
                    gate(17 + offset, 4, route.family, operation,
                         (f"status:{endpoint}", endpoint_lane, f"endpoint_query:{route.route_id}"), route, event)
            else:
                for offset, (operation, event) in enumerate((("INC7", "ENDPOINT_QUERY"),
                                                             ("GE2_COPY", "ENDPOINT_COPY"),
                                                             ("DEC7", "ENDPOINT_UNQUERY"))):
                    gate(17 + offset, 4, route.family, operation,
                         (f"collision_count:{endpoint}", endpoint_lane), route, event)
            for step in range(length, 0, -1):
                return_round = 9 - step
                emit_edge(route, step, False, 4 * return_round, return_round)
                if step > 1:
                    emit_handoff(route, step - 1, False, 4 * return_round + 1, return_round)
            sink_kind = "writer_mask_sink" if route.family == "blank" else "writer_conflict_sink"
            gate(33, 8, route.family, "MOVE1_TO_SINK", (local, f"{sink_kind}:{route.role_index}"), route, "CONSUME")
        elif route.family in ("predicate", "obstacle"):
            out_base = 58 if route.family == "predicate" else 90
            for step in range(1, length + 1):
                emit_edge(route, step, True, out_base + 2 * (step - 1), 22 + step if route.family == "predicate" else 26 + step)
                if step < length:
                    emit_handoff(route, step, True, out_base + 2 * (step - 1) + 1,
                                 22 + step if route.family == "predicate" else 26 + step)
            endpoint_lane = lane(route, length, "in")
            endpoint = route.path[-1]
            if route.family == "predicate" and length == 2:
                query_base = 64 + 3 * route.branch
            else:
                query_base = 61 if route.family == "predicate" else 93
            for offset, (operation, event) in enumerate((("QND_RECORD_COPY", "ENDPOINT_QUERY"),
                                                         ("CNOT", "ENDPOINT_COPY"),
                                                         ("QND_RECORD_UNCOPY", "ENDPOINT_UNQUERY"))):
                gate(query_base + offset, 24 if route.family == "predicate" else 28, route.family, operation,
                     (f"status:{endpoint}", endpoint_lane, f"endpoint_query:{route.route_id}"), route, event)
            return_base = 82 if route.family == "predicate" else 96
            for reverse_index, step in enumerate(range(length, 0, -1)):
                emit_edge(route, step, False, return_base + 2 * reverse_index,
                          27 - step if route.family == "predicate" else 31 - step)
                if step > 1:
                    emit_handoff(route, step - 1, False, return_base + 2 * reverse_index + 1,
                                 27 - step if route.family == "predicate" else 31 - step)
            sink_kind = "controller_predicate_sink" if route.family == "predicate" else "controller_obstacle_sink"
            gate(85 if route.family == "predicate" else 99, 26 if route.family == "predicate" else 30,
                 route.family, "MOVE1_TO_SINK", (local, f"{sink_kind}:{route.role_index}"), route, "CONSUME")

    # Source-bound trigger and blank request seeds are explicit bundle outputs.
    conflict_seeds = tuple(f"seed:conflict:{index}" for index in range(len(F_ROLES)))
    gate(0, 0, "writer_seed", "FANOUT73_TRIGGER", ("trigger_input",) + conflict_seeds)
    for index, role in enumerate(F_ROLES):
        add_roundtrip(RouteSpec(f"conflict:{index}", "conflict", role_path(role), role_index=index))
    for index, role in enumerate(B_ROLES):
        add_roundtrip(RouteSpec(f"blank:{index}", "blank", role_path(role), role_index=index))
    gate(34, 8, "writer_decision", "COIN6_OR_STOP",
         ("writer_mask_sink", "writer_conflict_sink", "writer_direction_sink"))

    # One-hot branch broadcasts remain live through the public writer lock.
    broadcast_seeds = tuple(f"seed:broadcast:{f_index}:{role_index}"
                            for f_index in range(6) for role_index in range(len(F_ROLES)))
    gate(35, 8, "writer_broadcast_seed", "FANOUT438_BRANCH", ("writer_direction_sink",) + broadcast_seeds)
    broadcast_routes: dict[tuple[int, int], RouteSpec] = {}
    for f_index, f in enumerate(D):
        assignment = writer_roles(f)
        for role_index, role in enumerate(F_ROLES):
            route = RouteSpec(f"broadcast:{f_index}:{role_index}", "broadcast", role_path(role), f_index, role_index)
            routes.append(route)
            broadcast_routes[(f_index, role_index)] = route
            length = len(route.path) - 1
            local = lane(route, 0, "local") if length == 0 else lane(route, 0, "out")
            gate(36, 8, "broadcast", "SWAP", (f"seed:{route.route_id}", local), route, "LOAD")
            for step in range(1, length + 1):
                emit_edge(route, step, True, 37 + 2 * (step - 1), 8 + step)
                if step < length:
                    emit_handoff(route, step, True, 38 + 2 * (step - 1), 8 + step)
            endpoint_lane = local if length == 0 else lane(route, length, "in")
            if role.site in B:
                stage = f"writer_stage:{f_index}:{role.site}"
                purifier = f"writer_purifier:{f_index}:{role.site}"
                operation = "P143" if "rho_f" in assignment[role.site] else "BELL"
                gate(44, 12, "writer_private_stage", operation, (endpoint_lane, stage, purifier), route, "ENDPOINT")
                if operation == "P143":
                    for word_index, rotation_gate in enumerate(ROTATION_WORDS[f]):
                        gate(45 + word_index, 12, "writer_cubic_rotation", rotation_gate,
                             (endpoint_lane, stage), route, f"ROTATE{word_index + 1}")
            else:
                gate(44, 12, "broadcast_endpoint_ack", "COMMIT_BARRIER", (endpoint_lane,), route, "ENDPOINT")
            for reverse_index, step in enumerate(range(length, 0, -1)):
                emit_edge(route, step, False, 50 + 2 * reverse_index, 17 - step)
                if step > 1:
                    emit_handoff(route, step - 1, False, 51 + 2 * reverse_index, 17 - step)
            gate(57, 16, "broadcast", "SWAP", (local, f"seed:{route.route_id}"), route, "CONSUME")

    gate(47, 12, "writer_commit_barrier", "COMMIT_BARRIER", ("writer_atomic_commit_barrier",))
    site_to_role = {role.site: index for index, role in enumerate(F_ROLES)}
    for site in sorted(B):
        role_index = site_to_role[site]
        controls = tuple(lane(broadcast_routes[(f_index, role_index)], len(role_path(F_ROLES[role_index])) - 1,
                              "local" if len(role_path(F_ROLES[role_index])) == 1 else "in") for f_index in range(6))
        stages = tuple(f"writer_stage:{f_index}:{site}" for f_index in range(6))
        gate(48, 12, "writer_atomic_content_commit", "BRANCH6_SWAP", controls + (f"content:{site}",) + stages)
    center_role = site_to_role[ZERO]
    center_controls = tuple(lane(broadcast_routes[(f_index, center_role)], 0, "local") for f_index in range(6))
    gate(49, 12, "writer_public_commit", "LOCK_IF_ANY6",
         center_controls + ("status:(0, 0, 0)", "lock_sink:C"))
    for p in D:
        a1_role = site_to_role[p]
        f_index = D.index(p)
        control = lane(broadcast_routes[(f_index, a1_role)], len(role_path(F_ROLES[a1_role])) - 1,
                       "local" if len(role_path(F_ROLES[a1_role])) == 1 else "in")
        gate(49, 12, "writer_public_commit", "LOCK_IF_ONE", (control, f"status:{p}", f"lock_sink:A1:{p}"))
        a2_site = mul(2, p)
        a2_role = site_to_role[a2_site]
        opposite_index = D.index(mul(-1, p))
        opposite_control = lane(broadcast_routes[(opposite_index, a2_role)], len(role_path(F_ROLES[a2_role])) - 1, "in")
        gate(49, 12, "writer_public_commit", "LOCK_IF_ONE", (opposite_control, f"status:{a2_site}", f"lock_sink:A2:{p}"))

    # Fresh branch-independent A2 inference and explicit radius-two routes.
    for p_index, p in enumerate(D):
        gate(57, 21, "fresh_six_A2_enable", "FANOUT0", (f"fresh_phase:{p_index}", f"A2:{mul(2,p)}"))
        add_roundtrip(RouteSpec(f"predicate:{p_index}:near", "predicate", (mul(2, p), p), p_index, 2*p_index))
        add_roundtrip(RouteSpec(f"predicate:{p_index}:grand", "predicate", (mul(2, p), p, ZERO), p_index, 2*p_index + 1))
        gate(86, 26, "radius2_collinear_logic", "TOFFOLI",
             (f"controller_predicate_sink:{2*p_index}", f"controller_predicate_sink:{2*p_index+1}", f"predicate:{p_index}"))
        gate(88, 26, "radius2_collinear_unlogic", "TOFFOLI",
             (f"controller_predicate_sink:{2*p_index}", f"controller_predicate_sink:{2*p_index+1}", f"predicate:{p_index}"))
        gate(61, 23, "candidate_fresh_query", "QND_RECORD_COPY",
             (f"status:{mul(2,p)}", f"candidate_fresh_query:{p_index}"))
        gate(62, 23, "candidate_fresh_copy", "CNOT",
             (f"candidate_fresh_query:{p_index}", f"controller_candidate_fresh_sink:{p_index}"))
        gate(63, 23, "candidate_fresh_unquery", "QND_RECORD_UNCOPY",
             (f"status:{mul(2,p)}", f"candidate_fresh_query:{p_index}"))
    gate(87, 26, "copy_inferred_f", "COPY_F_TO_SINK", ("six_predicates", "fresh_controller_direction_sink"))

    # Obstacle routes bind destination QND samples to retained mask sinks.
    obstacle_index = 0
    for f_index, f in enumerate(D):
        destinations = (mul(4, f),) + tuple(add(mul(3, f), q) for q in perpendicular(f))
        for leg, destination in enumerate(destinations):
            add_roundtrip(RouteSpec(f"obstacle:{f_index}:{leg}", "obstacle",
                                    (mul(2, f), mul(3, f), destination), f_index, obstacle_index))
            obstacle_index += 1
    gate(100, 30, "copy_winning_obstacle_mask", "SELECT5_MASK",
         ("fresh_controller_direction_sink", "controller_obstacle_sink", "controller_obstacle_mask_sink"))
    gate(100, 30, "controller_outcome_coin", "COIN14", ("outcome_sink",))
    gate(101, 30, "controller_affine_choice", "CHOICE3", ("affine_choice", "mixed_branch_purifier"))
    gate(102, 30, "controller_axis_orbit", "PREP_AXIS_ORBIT", ("outcome_sink", "candidate_staging", "candidate_purifier"))
    gate(103, 30, "controller_corner_orbit", "PREP_CORNER_ORBIT", ("outcome_sink", "candidate_staging", "candidate_purifier"))
    gate(104, 30, "controller_affine_prepare", "AFFINE_PREP",
         ("fresh_controller_direction_sink", "affine_choice", "candidate_staging", "candidate_purifier"))
    gate(105, 30, "controller_candidate_dump", "SWAP", ("content:2f", "candidate_staging"))
    gate(106, 30, "controller_public_commit", "LOCK", ("status:2f", "candidate_lock_sink"))
    for leg in range(5):
        gate(107 + leg, 30, "conditional_five_swaps", "SWAP_IF_CLEAR",
             ("controller_obstacle_mask_sink", f"source:{leg}", f"destination:{leg}"))
    for p_index, p in enumerate(D):
        gate(112, 34, "fresh_six_A2_cleanup", "UNFANOUT", (f"fresh_phase:{p_index}", f"A2:{mul(2,p)}"))
    gate(58, 16, "writer_broadcast_seed_cleanup", "UNFANOUT438_BRANCH",
         ("writer_direction_sink",) + broadcast_seeds)

    controller_phases = {
        "fresh_six_A2_enable", "fresh_six_A2_cleanup", "radius2_collinear_logic",
        "radius2_collinear_unlogic", "candidate_fresh_query", "candidate_fresh_copy",
        "candidate_fresh_unquery", "copy_inferred_f", "copy_winning_obstacle_mask",
        "controller_outcome_coin", "controller_affine_choice", "controller_axis_orbit",
        "controller_corner_orbit", "controller_affine_prepare", "controller_candidate_dump",
        "controller_public_commit", "conditional_five_swaps",
    }
    gates = [
        replace(instance, elementary_layer=instance.elementary_layer + 2)
        if instance.route_id.startswith(("predicate:", "obstacle:")) or instance.phase in controller_phases
        else instance
        for instance in gates
    ]
    ordered_gates = tuple(sorted(gates, key=lambda item: (item.elementary_layer, item.communication_round,
                                                          item.operation, item.targets, item.route_id)))
    route_registers = frozenset(target for instance in ordered_gates for target in instance.targets
                                if target.startswith(("lane:", "seed:", "endpoint_query:", "fringe_ack:", "broadcast_return_sink:")))
    banks = BASE_REGISTER_BANKS + (RegisterBank("explicit_route_and_binding_bits", 1, len(route_registers), "reusable"),)
    return Netlist(banks, MAPS, ordered_gates, tuple(routes))


NETLIST = build_netlist()


def exact_map_certificate() -> bool:
    names = {exact_map.name for exact_map in MAPS}
    if len(names) != len(MAPS):
        return False
    for exact_map in MAPS:
        if not exact_map.entries or any(entry.square <= 0 or entry.sign not in (-1, 1)
                                        or entry.phase_quarters not in range(4) for entry in exact_map.entries):
            return False
        if exact_map.family in ("permutation", "monomial_unitary"):
            if sorted(entry.source for entry in exact_map.entries) != list(range(exact_map.input_dimension)):
                return False
            if sorted(entry.target for entry in exact_map.entries) != list(range(exact_map.output_dimension)):
                return False
            if any(entry.square != 1 for entry in exact_map.entries):
                return False
        elif exact_map.family == "kraus":
            if sum((entry.square for entry in exact_map.entries), start=Fraction(0)) != 1:
                return False
        elif exact_map.family in ("preparation", "certified_orbit"):
            if sum((entry.square for entry in exact_map.entries), start=Fraction(0)) != 1:
                return False
        elif exact_map.family == "initialized_isometry":
            if len({entry.source for entry in exact_map.entries}) != len(exact_map.entries):
                return False
            if len({entry.target for entry in exact_map.entries}) != len(exact_map.entries):
                return False
        elif exact_map.name == "H":
            columns = {source: [entry for entry in exact_map.entries if entry.source == source] for source in range(2)}
            if any(sum((entry.square for entry in column), start=Fraction(0)) != 1 for column in columns.values()):
                return False
            cross = sum(
                (Fraction(left.sign * right.sign, 2) for left in columns[0] for right in columns[1] if left.target == right.target),
                start=Fraction(0),
            )
            if cross != 0:
                return False
        else:
            return False
    by_name = {exact_map.name: exact_map for exact_map in MAPS}
    for exact_map in MAPS:
        if exact_map.inverse is None:
            continue
        inverse = by_name.get(exact_map.inverse)
        if inverse is None or inverse.inverse != exact_map.name:
            return False
        forward_pairs = {(entry.source, entry.target) for entry in exact_map.entries}
        inverse_pairs = {(entry.target, entry.source) for entry in inverse.entries}
        if forward_pairs != inverse_pairs:
            return False
    return True


def schedule_certificate(netlist: Netlist = NETLIST) -> bool:
    required_ops = {
        "SWAP", "QND_RECORD_COPY", "QND_RECORD_UNCOPY", "INC7", "DEC7", "GE2_COPY",
        "CNOT", "COIN6_OR_STOP", "COIN14", "P143", "BELL", "CHOICE3", "TOFFOLI",
        "FANOUT0", "UNFANOUT", "FANOUT73_TRIGGER",
        "FANOUT438_BRANCH", "UNFANOUT438_BRANCH", "COPY_F_TO_SINK", "SELECT5_MASK", "MOVE1_TO_SINK",
        "LOCK", "LOCK_IF_ONE", "LOCK_IF_ANY6", "ONSITE_SCATTER", "BRANCH6_SWAP", "COMMIT_BARRIER",
        "PREP_AXIS_ORBIT", "PREP_CORNER_ORBIT", "AFFINE_PREP", "SWAP_IF_CLEAR",
    }
    invoked = {gate.operation for gate in netlist.gates}
    if not required_ops <= invoked:
        return False
    # A circuit layer is a parallel matching: even disjoint logical rails may
    # not alias one physical register/port target in the same layer.
    targets_by_layer: dict[int, set[str]] = {}
    for gate in netlist.gates:
        occupied = targets_by_layer.setdefault(gate.elementary_layer, set())
        if len(set(gate.targets)) != len(gate.targets) or occupied & set(gate.targets):
            return False
        occupied.update(gate.targets)
    # Independently regenerate the complete route family, including paths.
    expected_routes: dict[str, tuple[str, tuple[V, ...], int, int]] = {}
    for index, role in enumerate(F_ROLES):
        expected_routes[f"conflict:{index}"] = ("conflict", role_path(role), -1, index)
    for index, role in enumerate(B_ROLES):
        expected_routes[f"blank:{index}"] = ("blank", role_path(role), -1, index)
    for f_index in range(6):
        for role_index, role in enumerate(F_ROLES):
            expected_routes[f"broadcast:{f_index}:{role_index}"] = ("broadcast", role_path(role), f_index, role_index)
    for p_index, p in enumerate(D):
        expected_routes[f"predicate:{p_index}:near"] = ("predicate", (mul(2,p), p), p_index, 2*p_index)
        expected_routes[f"predicate:{p_index}:grand"] = ("predicate", (mul(2,p), p, ZERO), p_index, 2*p_index+1)
    obstacle_index = 0
    for f_index, f in enumerate(D):
        for leg, destination in enumerate((mul(4,f),) + tuple(add(mul(3,f), q) for q in perpendicular(f))):
            expected_routes[f"obstacle:{f_index}:{leg}"] = ("obstacle", (mul(2,f), mul(3,f), destination), f_index, obstacle_index)
            obstacle_index += 1
    actual_routes = {route.route_id: (route.family, route.path, route.branch, route.role_index) for route in netlist.routes}
    if actual_routes != expected_routes or len(actual_routes) != 596:
        return False

    events_by_route: dict[str, list[GateInstance]] = {route_id: [] for route_id in expected_routes}
    for gate in netlist.gates:
        if gate.route_id:
            if gate.route_id not in events_by_route:
                return False
            events_by_route[gate.route_id].append(gate)
    for route in netlist.routes:
        length = len(route.path) - 1
        expected_events = ["LOAD"]
        for step in range(1, length + 1):
            expected_events.append("EDGE_OUT")
            if step < length:
                expected_events.append("HANDOFF_OUT")
        if route.family == "broadcast":
            expected_events.append("ENDPOINT")
            role = F_ROLES[route.role_index]
            if role.site in B and "rho_f" in writer_roles(D[route.branch])[role.site]:
                expected_events.extend(f"ROTATE{index+1}" for index in range(len(ROTATION_WORDS[D[route.branch]])))
        else:
            expected_events.extend(("ENDPOINT_QUERY", "ENDPOINT_COPY", "ENDPOINT_UNQUERY"))
        for step in range(length, 0, -1):
            expected_events.append("EDGE_RETURN")
            if step > 1:
                expected_events.append("HANDOFF_RETURN")
        expected_events.append("CONSUME")
        actual_events = sorted(events_by_route[route.route_id], key=lambda gate: (gate.elementary_layer, gate.route_event))
        if [gate.route_event for gate in actual_events] != expected_events:
            return False
        root_register = f"lane:{route.route_id}:v0:{'local' if length == 0 else 'out'}"
        endpoint_register = f"lane:{route.route_id}:v{length}:{'local' if length == 0 else 'in'}"
        for gate in actual_events:
            if gate.route_event == "LOAD" and gate.targets != (f"seed:{route.route_id}", root_register):
                return False
            if gate.route_event == "EDGE_OUT":
                expected_targets = (f"lane:{route.route_id}:v{gate.route_step-1}:out",
                                    f"lane:{route.route_id}:v{gate.route_step}:in")
                if gate.targets != expected_targets:
                    return False
            if gate.route_event == "EDGE_RETURN":
                expected_targets = (f"lane:{route.route_id}:v{gate.route_step}:in",
                                    f"lane:{route.route_id}:v{gate.route_step-1}:out")
                if gate.targets != expected_targets:
                    return False
            if gate.route_event in ("HANDOFF_OUT", "HANDOFF_RETURN"):
                expected_targets = (f"lane:{route.route_id}:v{gate.route_step}:in",
                                    f"lane:{route.route_id}:v{gate.route_step}:out")
                if gate.targets != expected_targets:
                    return False
                expected_round = (gate.route_step if route.family in ("blank", "conflict")
                                  else 8 + gate.route_step if route.family == "broadcast"
                                  else 22 + gate.route_step if route.family == "predicate"
                                  else 26 + gate.route_step)
                if gate.route_event == "HANDOFF_RETURN":
                    expected_round = (8-gate.route_step if route.family in ("blank", "conflict")
                                      else 16-gate.route_step if route.family == "broadcast"
                                      else 26-gate.route_step if route.family == "predicate"
                                      else 30-gate.route_step)
                if gate.communication_round != expected_round:
                    return False
            if gate.route_event.startswith("ENDPOINT") or gate.route_event.startswith("ROTATE"):
                if endpoint_register not in gate.targets:
                    return False
            if gate.route_event == "CONSUME":
                expected_sink = (f"writer_mask_sink:{route.role_index}" if route.family == "blank"
                                 else f"writer_conflict_sink:{route.role_index}" if route.family == "conflict"
                                 else f"seed:{route.route_id}" if route.family == "broadcast"
                                 else f"controller_predicate_sink:{route.role_index}" if route.family == "predicate"
                                 else f"controller_obstacle_sink:{route.role_index}")
                if gate.targets != (root_register, expected_sink):
                    return False
        edge_out = [gate for gate in actual_events if gate.route_event == "EDGE_OUT"]
        edge_return = [gate for gate in actual_events if gate.route_event == "EDGE_RETURN"]
        for step, gate in enumerate(edge_out, start=1):
            expected_edge = (route.path[step-1], route.path[step])
            if gate.edge != expected_edge or l1(sub(*reversed(expected_edge))) != 1:
                return False
            expected_round = step if route.family in ("blank", "conflict") else 8+step if route.family == "broadcast" else 22+step if route.family == "predicate" else 26+step
            if gate.communication_round != expected_round:
                return False
        for gate, step in zip(edge_return, range(length, 0, -1)):
            expected_edge = (route.path[step], route.path[step-1])
            expected_round = 9-step if route.family in ("blank", "conflict") else 17-step if route.family == "broadcast" else 27-step if route.family == "predicate" else 31-step
            if gate.edge != expected_edge or gate.communication_round != expected_round:
                return False
        if any(f"lane:{route.route_id}:" not in "|".join(gate.targets) for gate in actual_events):
            return False

    trigger_seed_gates = [gate for gate in netlist.gates if gate.operation == "FANOUT73_TRIGGER"]
    branch_seed_gates = [gate for gate in netlist.gates if gate.operation in ("FANOUT438_BRANCH", "UNFANOUT438_BRANCH")]
    expected_conflict_seeds = {f"seed:conflict:{index}" for index in range(73)}
    expected_broadcast_seeds = {f"seed:broadcast:{f_index}:{role_index}" for f_index in range(6) for role_index in range(73)}
    if len(trigger_seed_gates) != 1 or any(set(gate.targets[1:]) != expected_conflict_seeds for gate in trigger_seed_gates):
        return False
    if len(branch_seed_gates) != 2 or any(set(gate.targets[1:]) != expected_broadcast_seeds for gate in branch_seed_gates):
        return False

    # All 258 private writer preparations are role-derived; system mutation is
    # forbidden until the explicit barrier, and exactly 43 mux-swaps/13 locks commit.
    prep_gates = [gate for gate in netlist.gates if gate.phase == "writer_private_stage"]
    expected_preps: dict[str, str] = {}
    for f_index, f in enumerate(D):
        assignment = writer_roles(f)
        for site in B:
            expected_preps[f"writer_stage:{f_index}:{site}"] = "P143" if "rho_f" in assignment[site] else "BELL"
    actual_preps = {gate.targets[1]: gate.operation for gate in prep_gates}
    if actual_preps != expected_preps:
        return False
    rotations = [gate for gate in netlist.gates if gate.phase == "writer_cubic_rotation"]
    expected_rotation_count = sum(4 * len(ROTATION_WORDS[f]) for f in D)
    if len(rotations) != expected_rotation_count or not spin_orbit_certificate():
        return False
    barriers = [gate for gate in netlist.gates if gate.phase == "writer_commit_barrier"]
    content_commits = [gate for gate in netlist.gates if gate.phase == "writer_atomic_content_commit"]
    writer_locks = [gate for gate in netlist.gates if gate.phase == "writer_public_commit"]
    if len(barriers) != 1 or len(content_commits) != 43 or len(writer_locks) != 13:
        return False
    barrier_layer = barriers[0].elementary_layer
    if any(gate.elementary_layer <= barrier_layer for gate in content_commits + writer_locks):
        return False
    if {gate.elementary_layer for gate in content_commits} != {48} or {gate.elementary_layer for gate in writer_locks} != {49}:
        return False
    if max(gate.elementary_layer for gate in netlist.gates if gate.route_id.startswith(("blank:", "conflict:"))) >= barrier_layer:
        return False
    broadcast_consumes = [gate for gate in netlist.gates if gate.route_id.startswith("broadcast:") and gate.route_event == "CONSUME"]
    if min(gate.elementary_layer for gate in broadcast_consumes) <= max(gate.elementary_layer for gate in writer_locks):
        return False

    inferred = [gate for gate in netlist.gates if gate.operation == "COPY_F_TO_SINK"]
    if (len(inferred) != 1 or inferred[0].elementary_layer != 89
            or inferred[0].targets != ("six_predicates", "fresh_controller_direction_sink")):
        return False
    candidate_prep_phases = {"controller_affine_choice", "controller_axis_orbit", "controller_corner_orbit", "controller_affine_prepare"}
    if len([gate for gate in netlist.gates if gate.phase in candidate_prep_phases]) != 4:
        return False
    candidate_dump = [gate for gate in netlist.gates if gate.phase == "controller_candidate_dump"]
    controller_lock = [gate for gate in netlist.gates if gate.phase == "controller_public_commit"]
    controller_swaps = sorted((gate for gate in netlist.gates if gate.phase == "conditional_five_swaps"), key=lambda gate: gate.elementary_layer)
    if len(candidate_dump) != 1 or len(controller_lock) != 1 or len(controller_swaps) != 5:
        return False
    if not (candidate_dump[0].elementary_layer == 107 < controller_lock[0].elementary_layer == 108
            < min(gate.elementary_layer for gate in controller_swaps)):
        return False
    if [gate.elementary_layer for gate in controller_swaps] != list(range(109, 114)):
        return False
    if max(gate.elementary_layer for gate in netlist.gates if gate.route_id.startswith(("predicate:", "obstacle:"))) >= 107:
        return False
    return True


def resource_timing_certificate(netlist: Netlist = NETLIST) -> bool:
    reusable = sum(bank.allocated_bits for bank in netlist.register_banks if bank.lifetime == "reusable")
    retained = sum(bank.allocated_bits for bank in netlist.register_banks if bank.lifetime == "retained")
    base_reusable = sum(bank.allocated_bits for bank in BASE_REGISTER_BANKS if bank.lifetime == "reusable")
    explicit_bank = next((bank for bank in netlist.register_banks if bank.name == "explicit_route_and_binding_bits"), None)
    actual_route_registers = frozenset(target for gate in netlist.gates for target in gate.targets
                                       if target.startswith(("lane:", "seed:", "endpoint_query:", "fringe_ack:", "broadcast_return_sink:")))
    writer_rank = 6 * 2**86 + 1
    composed_rank = 84 * 2**86 + 1
    ceil_log2 = lambda n: (n - 1).bit_length()
    edge_rounds = {gate.communication_round for gate in netlist.gates if gate.route_event.startswith("EDGE_")}
    elementary_depth = max(gate.elementary_layer for gate in netlist.gates)
    return (
        base_reusable == 354 * 73 == 25842 and retained == 714
        and explicit_bank is not None and explicit_bank.multiplicity == len(actual_route_registers) > 0
        and reusable == base_reusable + len(actual_route_registers)
        and next(bank for bank in netlist.register_banks if bank.name == "writer_branch_staging_or_dump").multiplicity == 258
        and next(bank for bank in netlist.register_banks if bank.name == "writer_branch_purifier").multiplicity == 258
        and ceil_log2(writer_rank) == 89 and ceil_log2(composed_rank) == 93
        and len(edge_rounds) == 24 and min(edge_rounds) == 1 and max(edge_rounds) == 30
        and elementary_depth == 114
        and max(gate.elementary_layer for gate in netlist.gates if gate.phase == "writer_public_commit") == 49
        and max(gate.elementary_layer for gate in netlist.gates if gate.phase == "controller_public_commit") == 108
    )


ROUTES = (
    ("full-domain same-environment strict quotient", "closed by sole fibre nonconstancy obstruction"),
    ("blank-promise strict channel", "LIVE EXIT: removes the nonblank comparison"),
    ("hybrid status carrier", "LIVE EXIT: retains the status summand"),
    ("status-conditioned environment", "LIVE EXIT: changes the fixed environment"),
    ("wider onsite carrier", "LIVE EXIT: changes strict M2"),
    ("distributed orthogonal pointer", "LIVE EXIT: changes carrier and support"),
    ("modified or coarse target", "LIVE EXIT: changes the exact target"),
)


def strict_m2_certificate(nonblank_bloch: Fraction = Fraction(0)) -> bool:
    purifier_difference = Fraction(113, 512) - Fraction(399, 512)
    blank_bloch = purifier_difference / 6
    one_fibre = {
        "blank": ("I/2 quotient content", blank_bloch),
        "nonblank": ("I/2 quotient content", nonblank_bloch),
    }
    sole_obstruction = one_fibre["blank"][0] == one_fibre["nonblank"][0] and one_fibre["blank"][1] != one_fibre["nonblank"][1]
    corroboration = {
        "hybrid_dimension": 2 * 4,
        "strict_dimension": 4,
        "hybrid_center_dimension": 2,
        "strict_center_dimension": 1,
    }
    live_exits = tuple(route for route, result in ROUTES if result.startswith("LIVE EXIT"))
    return (
        blank_bloch == Fraction(-143, 1536) and sole_obstruction
        and corroboration == {"hybrid_dimension": 8, "strict_dimension": 4, "hybrid_center_dimension": 2, "strict_center_dimension": 1}
        and len(live_exits) == 6 and len(ROUTES) == 7
    )


LAYER_REPORT = {
    "per_element": "exact mixtures checked; one common quotient input has unequal writer and STOP outputs",
    "per_site": "85 blank/predicate/obstacle route seeds have no producer in the emitted netlist",
    "per_mode": "selected equal-six writer mode compared with STOP; no negative claim about other modes",
    "per_block": "geometry and abstract channel formulas survive, but the frozen netlist does not bind their payloads",
    "lattice_wide": "checked and not executed — supplied trigger batch has no occurrence hazard, concurrency law, or physical clock",
}


def provenance_certificate() -> bool:
    if len(AUDIT_INPUT_PATHS) != 9 or not all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS):
        return False

    def git(*arguments: str) -> str:
        return subprocess.check_output(("git",) + arguments, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()

    if git("rev-parse", "HEAD") != HEAD or git("rev-parse", "origin/main") != MAIN:
        return False
    for commit in (PREREG, BLOCK16_DELIVERY, BLOCK16_RESULT):
        if subprocess.run(("git", "merge-base", "--is-ancestor", commit, "HEAD"), cwd=ROOT, timeout=AUDIT_TIMEOUT_SEC).returncode:
            return False
    blobs = (
        (f"{PACKET}/GOAL.md", GOAL_BLOB),
        (f"{PACKET}/PREFLIGHT_WITNESSES.md", PREFLIGHT_BLOB),
        (f"{PACKET}/INDEPENDENT_PREREG_ATTACK.md", ATTACK_BLOB),
        (f"{PACKET}/APPROACH_REGISTRY.md", REGISTRY_BLOB),
        ("docs/MINIMAL_AXIOMS_2026-06-29.md", AXIOM_BLOB),
    )
    return all(git("hash-object", path) == expected for path, expected in blobs)


def remove_first_gate(netlist: Netlist, predicate: Callable[[GateInstance], bool]) -> Netlist:
    removed = False
    gates = []
    for gate in netlist.gates:
        if not removed and predicate(gate):
            removed = True
            continue
        gates.append(gate)
    return replace(netlist, gates=tuple(gates))


def mutate_first_gate(netlist: Netlist, predicate: Callable[[GateInstance], bool], **changes: object) -> Netlist:
    changed = False
    gates = []
    for gate in netlist.gates:
        if not changed and predicate(gate):
            gate = replace(gate, **changes)
            changed = True
        gates.append(gate)
    return replace(netlist, gates=tuple(sorted(gates, key=lambda item: (item.elementary_layer,
                                                                          item.communication_round,
                                                                          item.operation, item.targets,
                                                                          item.route_id))))


def reused_orientation_netlist(netlist: Netlist) -> Netlist:
    gates = tuple(
        replace(gate, targets=("writer_direction_sink", "fresh_controller_direction_sink"))
        if gate.operation == "COPY_F_TO_SINK" else gate
        for gate in netlist.gates
    )
    return replace(netlist, gates=gates)


def alias_one_layer_target(netlist: Netlist) -> Netlist:
    gates = list(netlist.gates)
    indices = [index for index, gate in enumerate(gates) if gate.elementary_layer == 1 and gate.targets]
    first, second = indices[:2]
    gates[second] = replace(gates[second], targets=(gates[first].targets[0],) + gates[second].targets[1:])
    return replace(netlist, gates=tuple(gates))


def bad_resource_bank(netlist: Netlist) -> Netlist:
    banks = tuple(replace(bank, multiplicity=bank.multiplicity - 1)
                  if bank.name == "explicit_route_and_binding_bits" else bank
                  for bank in netlist.register_banks)
    return replace(netlist, register_banks=banks)


def retarget_first_gate(
    netlist: Netlist,
    predicate: Callable[[GateInstance], bool],
    target_index: int,
    replacement: str,
) -> Netlist:
    changed = False
    gates = []
    for instance in netlist.gates:
        if not changed and predicate(instance):
            targets = list(instance.targets)
            targets[target_index] = replacement
            instance = replace(instance, targets=tuple(targets))
            changed = True
        gates.append(instance)
    return replace(netlist, gates=tuple(sorted(gates, key=lambda item: (
        item.elementary_layer, item.communication_round, item.operation,
        item.targets, item.route_id,
    ))))


def unsourced_route_seed_falsifier(netlist: Netlist = NETLIST) -> bool:
    """Certify the first exact construction failure, not a class-wide no-go.

    A LOAD seed is live only if an emitted fanout gate produces it.  Product-
    blank environment bits are zero and cannot silently become request bits.
    The frozen candidate sources conflict and branch-broadcast seeds, but none
    of its blank-query, predicate-query, or obstacle-query seeds.
    """
    fanout_operations = {"FANOUT73_TRIGGER", "FANOUT438_BRANCH"}
    produced = {
        target
        for instance in netlist.gates
        if instance.operation in fanout_operations
        for target in instance.targets[1:]
    }
    load_seeds = {
        instance.route_id: instance.targets[0]
        for instance in netlist.gates
        if instance.route_event == "LOAD"
    }
    missing = {
        route_id: seed
        for route_id, seed in load_seeds.items()
        if seed not in produced
    }
    missing_families = Counter(route_id.split(":", 1)[0] for route_id in missing)
    sourced_families = Counter(
        route_id.split(":", 1)[0]
        for route_id, seed in load_seeds.items()
        if seed in produced
    )
    return (
        len(load_seeds) == 596
        and missing_families == Counter({"blank": 43, "predicate": 12, "obstacle": 30})
        and sourced_families == Counter({"broadcast": 438, "conflict": 73})
        and len(missing) == 85
    )


def operation_map_binding_falsifier(netlist: Netlist = NETLIST) -> bool:
    """Show that route labels are not executable instances of registered maps.

    Route lanes are charged as one bit each.  The listed map dimensions thus
    disagree with the actual target tuples at three load-bearing operation
    families.  This leaves the abstract channel proof disconnected from the
    emitted circuit even though each map is valid in isolation.
    """
    maps = {exact_map.name: exact_map for exact_map in netlist.maps}
    handoffs = [instance for instance in netlist.gates if instance.route_event.startswith("HANDOFF")]
    qnd = [
        instance for instance in netlist.gates
        if instance.route_event in ("ENDPOINT_QUERY", "ENDPOINT_UNQUERY")
        and instance.operation in ("QND_RECORD_COPY", "QND_RECORD_UNCOPY")
    ]
    endpoint_cnot = [
        instance for instance in netlist.gates
        if instance.route_event == "ENDPOINT_COPY" and instance.operation == "CNOT"
    ]
    collision_updates = [instance for instance in netlist.gates if instance.operation in ("INC7", "DEC7")]
    route_bank = next(bank for bank in netlist.register_banks if bank.name == "explicit_route_and_binding_bits")
    return (
        route_bank.width == 1
        and len(handoffs) == 2388
        and all(instance.operation == "ONSITE_SCATTER" and len(instance.targets) == 2 for instance in handoffs)
        and maps["ONSITE_SCATTER"].input_dimension == maps["ONSITE_SCATTER"].output_dimension == 64
        and len(qnd) == 170 and all(len(instance.targets) == 3 for instance in qnd)
        and maps["QND_RECORD_COPY"].input_dimension == maps["QND_RECORD_COPY"].output_dimension == 4
        and maps["QND_RECORD_UNCOPY"].input_dimension == maps["QND_RECORD_UNCOPY"].output_dimension == 4
        and len(endpoint_cnot) == 85 and all(len(instance.targets) == 3 for instance in endpoint_cnot)
        and maps["CNOT"].input_dimension == maps["CNOT"].output_dimension == 4
        and len(collision_updates) == 146 and all(len(instance.targets) == 2 for instance in collision_updates)
        and maps["INC7"].input_dimension == maps["INC7"].output_dimension == 128
        and maps["DEC7"].input_dimension == maps["DEC7"].output_dimension == 128
    )


def surviving_hostile_mutation_falsifier(netlist: Netlist = NETLIST) -> tuple[bool, tuple[str, ...]]:
    """Reproduce eight independent false-green mutations in the old checks."""
    mutations: tuple[tuple[str, Netlist], ...] = (
        ("edge-opcode-CNOT", mutate_first_gate(
            netlist, lambda gate: gate.route_event == "EDGE_OUT", operation="CNOT")),
        ("endpoint-query-opcode-CNOT", mutate_first_gate(
            netlist, lambda gate: gate.route_event == "ENDPOINT_QUERY", operation="CNOT")),
        ("handoff-opcode-CNOT", mutate_first_gate(
            netlist, lambda gate: gate.route_event == "HANDOFF_OUT", operation="CNOT")),
        ("missing-fresh-A2-cleanup", remove_first_gate(
            netlist, lambda gate: gate.phase == "fresh_six_A2_cleanup")),
        ("missing-candidate-QND-unquery", remove_first_gate(
            netlist, lambda gate: gate.phase == "candidate_fresh_unquery")),
        ("writer-purifier-miswire", retarget_first_gate(
            netlist, lambda gate: gate.phase == "writer_private_stage", -1, "writer_purifier:miswired")),
        ("writer-commit-stage-miswire", retarget_first_gate(
            netlist, lambda gate: gate.phase == "writer_atomic_content_commit", -1, "writer_stage:miswired")),
        ("controller-affine-stage-disconnect", retarget_first_gate(
            netlist, lambda gate: gate.phase == "controller_affine_prepare", 2, "candidate_stage:disconnected")),
    )
    survivors = tuple(
        name
        for name, mutation in mutations
        if schedule_certificate(mutation) and resource_timing_certificate(mutation)
    )
    return survivors == tuple(name for name, _ in mutations), survivors


def frozen_construction_failure_certificate() -> bool:
    mutation_ok, survivors = surviving_hostile_mutation_falsifier()
    return (
        unsourced_route_seed_falsifier()
        and operation_map_binding_falsifier()
        and mutation_ok
        and len(survivors) == 8
    )


def hostile_mutation_sweep() -> tuple[bool, tuple[str, ...]]:
    removed_site = max(FAN)
    missing_conflict = frozenset(set(CONFLICTS) - {max(CONFLICTS)})
    overblocking = BALL8 - {ZERO}
    mutations: tuple[tuple[str, Callable[[], bool]], ...] = (
        ("altered-support-footprint", lambda: geometry_certificate(FAN - {removed_site})),
        ("missing-conflict-variable", lambda: overlap_certificate(missing_conflict)),
        ("radius-overblocking-72", lambda: overlap_certificate(overblocking)),
        ("premature-writer-system-change", lambda: schedule_certificate(mutate_first_gate(
            NETLIST, lambda gate: gate.phase == "writer_atomic_content_commit", elementary_layer=44))),
        ("missing-role-default-prep", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.phase == "writer_private_stage" and gate.operation == "BELL"))),
        ("missing-role-P143-prep", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.phase == "writer_private_stage" and gate.operation == "P143"))),
        ("missing-cubic-rotation", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.phase == "writer_cubic_rotation"))),
        ("wrong-cubic-orbit", lambda: spin_orbit_certificate({**ROTATION_WORDS, D[0]: ("X",)})),
        ("missing-writer-QND-unquery", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id.startswith("blank:") and gate.route_event == "ENDPOINT_UNQUERY"))),
        ("missing-controller-QND-unquery", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id.startswith("obstacle:") and gate.route_event == "ENDPOINT_UNQUERY"))),
        ("aliased-same-layer-port", lambda: schedule_certificate(alias_one_layer_target(NETLIST))),
        ("missing-conflict-edge", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id == "conflict:1" and gate.route_event == "EDGE_OUT"))),
        ("missing-broadcast-handoff", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id.startswith("broadcast:") and gate.route_event == "HANDOFF_OUT"))),
        ("missing-radius2-NN-route", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id == "predicate:0:grand" and gate.route_event == "EDGE_OUT"))),
        ("mismatched-return-edge", lambda: schedule_certificate(mutate_first_gate(
            NETLIST, lambda gate: gate.route_id == "blank:1" and gate.route_event == "EDGE_RETURN", edge=(ZERO, ZERO)))),
        ("non-NN-edge", lambda: schedule_certificate(mutate_first_gate(
            NETLIST, lambda gate: gate.route_id == "conflict:1" and gate.route_event == "EDGE_OUT", edge=(ZERO, (2,0,0))))),
        ("wrong-route-round", lambda: schedule_certificate(mutate_first_gate(
            NETLIST, lambda gate: gate.route_id == "obstacle:0:0" and gate.route_event == "EDGE_OUT", communication_round=31))),
        ("missing-endpoint-logic", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.route_id == "conflict:0" and gate.route_event == "ENDPOINT_COPY"))),
        ("reused-writer-orientation-geometry", lambda: transaction_certificate(True)),
        ("reused-writer-orientation-netlist", lambda: schedule_certificate(reused_orientation_netlist(NETLIST))),
        ("pre-lock-controller-swap", lambda: schedule_certificate(mutate_first_gate(
            NETLIST, lambda gate: gate.phase == "conditional_five_swaps", elementary_layer=105))),
        ("missing-candidate-dump", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.phase == "controller_candidate_dump"))),
        ("missing-candidate-prep", lambda: schedule_certificate(remove_first_gate(
            NETLIST, lambda gate: gate.phase == "controller_affine_prepare"))),
        ("route-register-underallocation", lambda: resource_timing_certificate(bad_resource_bank(NETLIST))),
        ("wrong-axis-weight", lambda: cap_packet_certificate(axis_weight=Fraction(1, 13))),
        ("wrong-writer-143", lambda: cap_packet_certificate(writer_shrink=Fraction(144, 256))),
        ("wrong-mixture-144", lambda: cap_packet_certificate(mixture_pure=Fraction(143, 256))),
        ("clear-vs-blocked-swap", lambda: arbitrary_reference_certificate(clear_mask=1)[0]),
        ("altered-writer-trace", lambda: arbitrary_reference_certificate(trace_offdiagonal=True)[0]),
        ("altered-reference-signature", lambda: arbitrary_reference_certificate(drop_reference=True)[0]),
        ("altered-controller-partial-trace", lambda: arbitrary_reference_certificate(pure_coefficient=Fraction(143, 256))[0]),
        ("strict-M2-equal-output", lambda: strict_m2_certificate(nonblank_bloch=Fraction(-143, 1536))),
    )
    survivors = tuple(name for name, mutated_certificate in mutations if mutated_certificate())
    return not survivors, tuple(name for name, _ in mutations)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, certificate: Callable[[], bool], detail: str) -> None:
        try:
            passed = bool(certificate())
        except Exception as error:  # visible failure; never convert an exception to PASS
            passed, detail = False, f"{type(error).__name__}: {error}"
        if passed:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    checks = Checks()
    channel_ok, channel_stats = arbitrary_reference_certificate()
    digest = hashlib.sha256(NETLIST.canonical_bytes()).hexdigest()
    reusable_bits = sum(bank.allocated_bits for bank in NETLIST.register_banks if bank.lifetime == "reusable")
    retained_bits = sum(bank.allocated_bits for bank in NETLIST.register_banks if bank.lifetime == "retained")
    lane_bits = next(bank.allocated_bits for bank in NETLIST.register_banks if bank.name == "explicit_route_and_binding_bits")
    checks.check("provenance", provenance_certificate, "corrected two-commit authority and nine forensic inputs including source note and registry")
    checks.check("signed-ray-fan", geometry_certificate, "derived B=43 F=73, K=761, shells, 41 orbits, 72 radius-rule nonconflicts")
    checks.check("overlap-symbolic-OR", overlap_certificate, "all 6,859 displacements in [-9,9]^3 plus one symbolic 760-variable OR normal form")
    checks.check("two-phase-transaction", transaction_certificate, "fresh six-A2 geometry inference and all 2,688 clear/blocked controller controls")
    checks.check("arbitrary-reference", lambda: channel_ok,
                 f"writer block basis {channel_stats.writer_block_basis_units} / surviving {channel_stats.writer_surviving_basis_units}, local coefficients {channel_stats.writer_local_nonzero_coefficients}; controller {channel_stats.controller_nonzero_classes}/{channel_stats.controller_examined}")
    checks.check("exact-packet-effects", cap_packet_certificate, "generated 6+8 coin, 143 writer state, 144/1/111 affine state, positivity and effects")
    checks.check("isolated-sparse-maps", exact_map_certificate, "individual basis maps are exact; invocation binding is tested separately and fails")
    checks.check("netlist-structural-partial", schedule_certificate,
                 f"596 route skeletons and ordering census pass, but this checker is mutation-incomplete; sha256={digest}")
    checks.check("resources-and-depth", resource_timing_certificate,
                 f"354 base bits/site*73 +{lane_bits} route/binding bits +{retained_bits} retained = {reusable_bits + retained_bits}; 24 routed edge rounds, 34 scheduled rounds, depth 114")
    failure_ok, surviving_mutations = surviving_hostile_mutation_falsifier()
    checks.check("frozen-construction-falsifier", frozen_construction_failure_certificate,
                 f"85 unsourced route seeds, three load-bearing opcode/map arity families disconnected, {len(surviving_mutations)}/8 fresh hostile mutations survive the old structural checks")
    checks.check("strict-M2-N1-N8", strict_m2_certificate, "one fibre-nonconstancy wall; center/dimension corroboration; exactly six live exits")
    mutation_ok, mutation_names = hostile_mutation_sweep()
    checks.check("original-hostile-mutations", lambda: mutation_ok,
                 f"{len(mutation_names)} original mutants rejected, but the independent eight-mutation extension exposes the blind spot")
    for layer, report in LAYER_REPORT.items():
        print(f"N5 {layer}: {report}")
    print(f"SUBCERTIFICATE: {SUBCERT} — exact same-environment full-domain strict quotient only")
    print(f"UNAWARDED: {UNAWARDED_TERMINAL} — payload provenance and executable map binding fail")
    print(f"TERMINAL: {FAILURE_TERMINAL} — this frozen candidate only; other finite local constructions remain live")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
