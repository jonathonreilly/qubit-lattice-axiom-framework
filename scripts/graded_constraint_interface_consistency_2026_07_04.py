#!/usr/bin/env python3
"""Mechanical checks for the graded-constraint interface note.

Verdicts live in the prose note. This runner checks finite projection algebra,
record-conditioned availability, density-trace weights, conditioning, and
explicit rejectors.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = (
    ROOT
    / "docs"
    / "GRADED_CONSTRAINT_INTERFACE_CONSISTENCY_BOUNDED_NOTE_2026-07-04.md"
)

TOL = 1e-9
Matrix = list[list[complex]]

V1_CORE = """**graded_constraint v1 (superseded core text).** For record-conditioned
menus of admissible possibilities, a weight function `w >= 0` exists with
`w(0) = 0`, `w(identity) = 1`: normalized on each menu, additive over
exclusive alternatives, non-contextual across embedding menus, and defined
on the full projection lattice of every nearest-neighbor composite, with
every finite orthogonal resolution of the composite identity menu-eligible.
No rate, propagation rule, orientation, scale, or record-production rule is
supplied."""

V2_CORE = """**graded_constraint v2 (candidate, unregistered).** A weight function
`w >= 0` is defined on the full projection lattice of every
nearest-neighbor composite, with `w(0) = 0`, `w(identity) = 1`, additive
over all orthogonal pairs, non-contextual, and dependent on the
surrounding record configuration through the nearest-neighbor channel.
Formation statistics on a record-conditioned menu of available
possibilities are `w` conditioned on that menu: the available elements'
weights renormalized by their total. If the available total is zero the
conditional is undefined — a named boundary, not hidden. No rate,
propagation rule, orientation, scale, or record-production rule is
supplied."""

AXIOM_NEEDLES = [
    "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.",
    "Records form.",
    "When present, a record locks exactly one admissible local possibility.",
    "Only records are readable.",
    "A readout value is determined by record content alone.",
]

NOTE_NEEDLES = [
    "the v1 core as literally worded is **DEFECTIVE**",
    "landed pager's core text (v1) is superseded by v2",
    "the pager amendment travels separately",
    "availability filters outcomes, never weights",
    "zero-available-total boundary",
    "Record frequencies can read `w` in aggregate",
    "two states with identical records do not differ in `w`",
    "TOTAL: PASS=7 FAIL=0",
]


@dataclass(frozen=True)
class Result:
    name: str
    ok: bool
    detail: str


@dataclass(frozen=True)
class RecordConfig:
    name: str
    records: tuple[str, ...]


@dataclass(frozen=True)
class State:
    records: tuple[str, ...]
    rho: Matrix


def normalize(text: str) -> str:
    return " ".join(text.split())


def close(a: complex, b: complex = 0j) -> bool:
    return abs(a - b) <= TOL


def real_close(a: complex, b: float) -> bool:
    return abs(a.real - b) <= TOL and abs(a.imag) <= TOL


def zeros(rows: int, cols: int) -> Matrix:
    return [[0j for _ in range(cols)] for _ in range(rows)]


def identity(n: int) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = 1 + 0j
    return out


def diagonal(entries: list[float]) -> Matrix:
    out = zeros(len(entries), len(entries))
    for i, value in enumerate(entries):
        out[i][i] = complex(value)
    return out


def shape(a: Matrix) -> tuple[int, int]:
    return len(a), len(a[0])


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    rows, cols = shape(a)
    return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    rows, cols = shape(a)
    return [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]


def scalar_mul(c: complex, a: Matrix) -> Matrix:
    rows, cols = shape(a)
    return [[c * a[i][j] for j in range(cols)] for i in range(rows)]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    rows, inner = shape(a)
    inner_b, cols = shape(b)
    assert inner == inner_b
    out = zeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            out[i][j] = sum(a[i][k] * b[k][j] for k in range(inner))
    return out


def tensor(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    out = zeros(ar * br, ac * bc)
    for i in range(ar):
        for j in range(ac):
            for k in range(br):
                for l in range(bc):
                    out[i * br + k][j * bc + l] = a[i][j] * b[k][l]
    return out


def trace(a: Matrix) -> complex:
    rows, cols = shape(a)
    assert rows == cols
    return sum(a[i][i] for i in range(rows))


def adjoint(a: Matrix) -> Matrix:
    rows, cols = shape(a)
    return [[a[i][j].conjugate() for i in range(rows)] for j in range(cols)]


def mat_eq(a: Matrix, b: Matrix) -> bool:
    rows, cols = shape(a)
    if shape(b) != (rows, cols):
        return False
    return all(close(a[i][j], b[i][j]) for i in range(rows) for j in range(cols))


def is_projection(p: Matrix) -> bool:
    return mat_eq(p, adjoint(p)) and mat_eq(mat_mul(p, p), p)


def projector(vector: list[complex]) -> Matrix:
    n = len(vector)
    return [[vector[i] * vector[j].conjugate() for j in range(n)] for i in range(n)]


I2 = identity(2)
I4 = identity(4)
Z0 = projector([1 + 0j, 0j])
Z1 = projector([0j, 1 + 0j])
X_PLUS = projector([2**-0.5 + 0j, 2**-0.5 + 0j])
X_MINUS = projector([2**-0.5 + 0j, -(2**-0.5) + 0j])

PROJECTIONS: dict[str, Matrix] = {
    "ZA0": tensor(Z0, I2),
    "ZA1": tensor(Z1, I2),
    "XA+": tensor(X_PLUS, I2),
    "XA-": tensor(X_MINUS, I2),
    "BellPhi+": projector([2**-0.5 + 0j, 0j, 0j, 2**-0.5 + 0j]),
}
PROJECTIONS["BellPhi+^c"] = mat_sub(I4, PROJECTIONS["BellPhi+"])

LOCAL_PROJECTIONS = frozenset({"ZA0", "ZA1", "XA+", "XA-"})
ENTANGLED_PROJECTION = "BellPhi+"

RESOLUTION_NAMES = ("z_local_A", "x_local_A", "bell_phi")


def resolution_from_dimension(name: str, dim: int) -> list[str]:
    if dim != 4:
        raise ValueError("this finite model only builds the two-site composite")
    if name == "z_local_A":
        return ["ZA0", "ZA1"]
    if name == "x_local_A":
        return ["XA+", "XA-"]
    if name == "bell_phi":
        return ["BellPhi+", "BellPhi+^c"]
    raise KeyError(name)


def algebra_dimension(_config: RecordConfig) -> int:
    return len(I4)


def candidate_shapes(config: RecordConfig) -> dict[str, list[str]]:
    dim = algebra_dimension(config)
    return {name: resolution_from_dimension(name, dim) for name in RESOLUTION_NAMES}


def matrix_resolution_ok(matrices: list[Matrix], dim: int) -> bool:
    if not all(is_projection(p) for p in matrices):
        return False
    total = zeros(dim, dim)
    for p in matrices:
        total = mat_add(total, p)
    if not mat_eq(total, identity(dim)):
        return False
    for i, p in enumerate(matrices):
        for j, q in enumerate(matrices):
            if i != j and not mat_eq(mat_mul(p, q), zeros(dim, dim)):
                return False
    return True


def resolution_ok(labels: list[str]) -> bool:
    return matrix_resolution_ok([PROJECTIONS[label] for label in labels], 4)


OPEN = RecordConfig("neighbor-open", ("north:Z0", "east:Z0"))
BLOCKED = RecordConfig("neighbor-blocked", ("north:Z1", "east:Z0"))
TILTED = RecordConfig("neighbor-tilted", ("north:Z0", "east:X1"))
ZERO_TOTAL = RecordConfig("zero-total", ("north:Z2-boundary", "east:Z0"))

AVAILABILITY: dict[tuple[str, ...], set[str]] = {
    OPEN.records: {"ZA0", "ZA1", "XA+", "XA-"},
    BLOCKED.records: {"ZA0", "XA+"},
    TILTED.records: {"ZA0", "ZA1", "XA+", "XA-"},
    ZERO_TOTAL.records: {"ZA0"},
}

RHO_OPEN = diagonal([0.40, 0.10, 0.20, 0.30])
RHO_TILTED = diagonal([0.70, 0.10, 0.10, 0.10])
RHO_ZERO_TOTAL = diagonal([0.00, 0.00, 0.40, 0.60])

DENSITY_BY_RECORDS: dict[tuple[str, ...], Matrix] = {
    OPEN.records: RHO_OPEN,
    BLOCKED.records: RHO_OPEN,
    TILTED.records: RHO_TILTED,
    ZERO_TOTAL.records: RHO_ZERO_TOTAL,
}


def density_ok(rho: Matrix) -> bool:
    if not mat_eq(rho, adjoint(rho)) or not real_close(trace(rho), 1.0):
        return False
    rows, cols = shape(rho)
    return all(
        (i != j and close(rho[i][j])) or (i == j and rho[i][i].real >= -TOL)
        for i in range(rows)
        for j in range(cols)
    )


def weight(config: RecordConfig, projection_label: str) -> float:
    rho = DENSITY_BY_RECORDS[config.records]
    value = trace(mat_mul(rho, PROJECTIONS[projection_label]))
    if abs(value.imag) > TOL:
        raise AssertionError(f"non-real weight for {projection_label}: {value}")
    return value.real


def overridden_weight(config: RecordConfig, projection_label: str) -> float:
    if config == OPEN and projection_label == "ZA1":
        return weight(config, projection_label) + 0.25
    return weight(config, projection_label)


def resolution_additive(config: RecordConfig, labels: list[str], weight_fn=weight) -> bool:
    return abs(sum(weight_fn(config, label) for label in labels) - 1.0) <= TOL


def available(config: RecordConfig, projection_label: str) -> bool:
    return projection_label in AVAILABILITY[config.records]


def availability_snapshot(config: RecordConfig) -> frozenset[str]:
    return frozenset(AVAILABILITY[config.records])


def physical_menu_status(config: RecordConfig, labels: list[str]) -> bool:
    return all(available(config, label) for label in labels)


def conditioned_statistics(config: RecordConfig, labels: list[str]) -> dict[str, float] | None:
    available_labels = [label for label in labels if available(config, label)]
    total = sum(weight(config, label) for label in available_labels)
    if abs(total) <= TOL:
        return None
    return {label: weight(config, label) / total for label in available_labels}


def bad_conditioning_that_alters_availability(config: RecordConfig, labels: list[str]) -> None:
    stats = conditioned_statistics(config, labels)
    if stats is not None:
        AVAILABILITY[config.records] = {label for label, value in stats.items() if value > 0.0}


def build_state(records: tuple[str, ...], supplied_rho: Matrix | None = None) -> State:
    expected = DENSITY_BY_RECORDS[records]
    if supplied_rho is not None and not mat_eq(supplied_rho, expected):
        raise ValueError("v2 rejects extra state content: w is record-determined")
    return State(records=records, rho=expected)


def lockable_set(config: RecordConfig) -> frozenset[str]:
    return frozenset(label for label in LOCAL_PROJECTIONS if available(config, label))


def readout_value(state: State) -> tuple[str, ...]:
    return tuple(sorted(state.records))


class WeightAccessProbe:
    def __init__(self, state: State) -> None:
        self.state = state
        self.queries = 0

    def weight(self, projection_label: str) -> float:
        self.queries += 1
        config = RecordConfig("probe", self.state.records)
        return weight(config, projection_label)


def bad_readout_value(state: State, probe: WeightAccessProbe) -> tuple[str, ...]:
    return tuple(sorted(state.records + (f"w={probe.weight('ZA0'):.3f}",)))


def check_defect_exhibit() -> Result:
    labels = resolution_from_dimension("z_local_A", 4)
    weights_sum = resolution_additive(BLOCKED, labels)
    contains_unavailable = any(not available(BLOCKED, label) for label in labels)
    available_element_present = any(available(BLOCKED, label) for label in labels)
    ok = (
        resolution_ok(labels)
        and weights_sum
        and contains_unavailable
        and available_element_present
    )
    return Result(
        "Defect exhibit: v1 mixed identity resolution",
        ok,
        "orthogonal identity resolution normalizes while containing unavailable ZA1",
    )


def check_n1_v2_coexistence() -> Result:
    labels = resolution_from_dimension("z_local_A", 4)
    availability_before = availability_snapshot(BLOCKED)
    w_before = [weight(BLOCKED, label) for label in labels]
    stats = conditioned_statistics(BLOCKED, labels)
    availability_after = availability_snapshot(BLOCKED)
    w_after = [weight(BLOCKED, label) for label in labels]

    availability_changes_w_not = (
        availability_snapshot(OPEN) != availability_snapshot(BLOCKED)
        and [weight(OPEN, label) for label in labels]
        == [weight(BLOCKED, label) for label in labels]
    )
    w_changes_availability_not = (
        [weight(OPEN, label) for label in labels]
        != [weight(TILTED, label) for label in labels]
        and availability_snapshot(OPEN) == availability_snapshot(TILTED)
    )
    conditioning_excludes_unavailable = stats == {"ZA0": 1.0}
    unavailable_weight_defined = weight(BLOCKED, "ZA1") > 0.0
    lattice_constrained = resolution_additive(BLOCKED, labels)
    densities_ok = all(density_ok(rho) for rho in DENSITY_BY_RECORDS.values())
    ok = all(
        [
            densities_ok,
            stats is not None,
            availability_before == availability_after,
            w_before == w_after,
            availability_changes_w_not,
            w_changes_availability_not,
            conditioning_excludes_unavailable,
            unavailable_weight_defined,
            lattice_constrained,
        ]
    )
    return Result(
        "N1 v2: coexistence and conditioning separation",
        ok,
        "availability and w remain distinct; conditioning excludes unavailable outcomes",
    )


def check_n1_zero_boundary() -> Result:
    labels = resolution_from_dimension("z_local_A", 4)
    stats = conditioned_statistics(ZERO_TOTAL, labels)
    available_total = sum(weight(ZERO_TOTAL, label) for label in labels if available(ZERO_TOTAL, label))
    ok = stats is None and abs(available_total) <= TOL and resolution_additive(ZERO_TOTAL, labels)
    return Result(
        "N1 v2: zero-available-total boundary",
        ok,
        "conditional is undefined while full-lattice additivity remains intact",
    )


def check_n2_v2_channel() -> Result:
    open_shapes = candidate_shapes(OPEN)
    blocked_shapes = candidate_shapes(BLOCKED)
    local_resolutions_verified = matrix_resolution_ok([Z0, Z1], 2) and matrix_resolution_ok(
        [X_PLUS, X_MINUS], 2
    )
    all_resolutions_verified = all(
        resolution_ok(labels) for labels in list(open_shapes.values()) + list(blocked_shapes.values())
    )
    all_resolution_weights_additive = all(
        resolution_additive(config, labels)
        for config in (OPEN, BLOCKED, TILTED, ZERO_TOTAL)
        for labels in candidate_shapes(config).values()
    )
    shapes_same = all(
        open_shapes[name] == blocked_shapes[name] for name in RESOLUTION_NAMES
    )
    menu_status_varies = physical_menu_status(
        OPEN, open_shapes["z_local_A"]
    ) != physical_menu_status(BLOCKED, blocked_shapes["z_local_A"])
    conditioned_stats_vary = conditioned_statistics(
        OPEN, open_shapes["z_local_A"]
    ) != conditioned_statistics(BLOCKED, blocked_shapes["z_local_A"])
    support_varies = availability_snapshot(OPEN) != availability_snapshot(BLOCKED)
    ok = all(
        [
            all_resolutions_verified,
            local_resolutions_verified,
            all_resolution_weights_additive,
            shapes_same,
            support_varies,
            menu_status_varies,
            conditioned_stats_vary,
        ]
    )
    return Result(
        "N2 v2: record-independent shapes, record-dependent menus",
        ok,
        "shape function receives records but derives shapes from algebra dimension",
    )


def check_n3_v2_record_readout() -> Result:
    state = build_state(OPEN.records)
    rejected = False
    try:
        build_state(OPEN.records, supplied_rho=RHO_TILTED)
    except ValueError:
        rejected = True
    law_answer_once = tuple(
        (label, round(weight(OPEN, label), 12))
        for label in sorted(PROJECTIONS)
    )
    probe = WeightAccessProbe(state)
    readout = readout_value(state)
    ok = all(
        [
            ENTANGLED_PROJECTION not in lockable_set(OPEN),
            ENTANGLED_PROJECTION not in lockable_set(BLOCKED),
            weight(OPEN, ENTANGLED_PROJECTION) > 0.0,
            readout == tuple(sorted(OPEN.records)),
            probe.queries == 0,
            rejected,
            law_answer_once
            == tuple((label, round(weight(OPEN, label), 12)) for label in sorted(PROJECTIONS)),
        ]
    )
    return Result(
        "N3 v2: local locking and record-only readout",
        ok,
        "entangled projection not lockable; identical-record different-w state rejected",
    )


def check_rejectors() -> Result:
    labels = resolution_from_dimension("z_local_A", 4)
    additivity_caught = not resolution_additive(OPEN, labels, weight_fn=overridden_weight)

    before = availability_snapshot(OPEN)
    bad_conditioning_that_alters_availability(OPEN, labels)
    after = availability_snapshot(OPEN)
    conditioning_mutation_caught = before != after
    AVAILABILITY[OPEN.records] = set(before)

    state = build_state(OPEN.records)
    probe = WeightAccessProbe(state)
    bad_readout_value(state, probe)
    readout_w_query_caught = probe.queries > 0

    ok = additivity_caught and conditioning_mutation_caught and readout_w_query_caught
    return Result(
        "Rejectors: additivity, conditioning, readout mutations caught",
        ok,
        "same projections and states fail under three genuine mutations",
    )


def check_needles() -> Result:
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    normalized_axiom = normalize(axiom_text)
    normalized_note = normalize(note_text)
    axiom_ok = all(normalize(needle) in normalized_axiom for needle in AXIOM_NEEDLES)
    note_quotes_ok = all(needle in note_text for needle in AXIOM_NEEDLES)
    core_ok = normalize(V1_CORE) in normalized_note and normalize(V2_CORE) in normalized_note
    note_ok = all(needle in note_text for needle in NOTE_NEEDLES)
    return Result(
        "Needle: prose premises and status discipline",
        axiom_ok and note_quotes_ok and core_ok and note_ok,
        "v1/v2 text, landed sentences, boundary, aggregate-readability, measured total",
    )


def main() -> int:
    results = [
        check_defect_exhibit(),
        check_n1_v2_coexistence(),
        check_n1_zero_boundary(),
        check_n2_v2_channel(),
        check_n3_v2_record_readout(),
        check_rejectors(),
        check_needles(),
    ]

    passes = 0
    fails = 0
    for index, result in enumerate(results, start=1):
        status = "PASS" if result.ok else "FAIL"
        passes += int(result.ok)
        fails += int(not result.ok)
        print(f"CHECK {index:02d}: {status} - {result.name} :: {result.detail}")
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
