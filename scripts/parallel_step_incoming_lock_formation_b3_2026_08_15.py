#!/usr/bin/env python3
"""Parallel-step incoming-lock formation on B_3(0); reverse/face display."""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/PARALLEL_STEP_INCOMING_LOCK_FORMATION_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
LOCK_ALPHABET: frozenset[Point] = frozenset(NN)
SEED_LOCK: Point = E1
RADIUS = 3
PROBE_A: Point = (1, 0, 0)
PROBE_B: Point = (1, 1, 1)
PROBE_C: Point = (2, 0, 0)
PROBE_D: Point = (1, 1, 0)
UNDEFINED = "undefined"

CLAIM_SCOPE = (
    "Parallel-step incoming-lock formation-tick reverse and face at k=1 "
    "on B_3(0) with seed lock +e_1 are reported. Displayed, not adopted."
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Point, right: Point) -> Point:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def taxicab(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def in_ball(point: Point) -> bool:
    return taxicab(point) <= RADIUS


def ball_sites() -> frozenset[Point]:
    sites: set[Point] = set()
    for x in range(-RADIUS, RADIUS + 1):
        for y in range(-RADIUS, RADIUS + 1):
            for z in range(-RADIUS, RADIUS + 1):
                point = (x, y, z)
                if in_ball(point):
                    sites.add(point)
    return frozenset(sites)


def axis_of(lock: Point) -> Point:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


def is_unit_nn(step: Point) -> bool:
    return step in LOCK_ALPHABET


def parallel_to_lock_axis(step: Point, lock: Point) -> bool:
    """Allowed iff s = ±e_i when L(p) = ±e_i."""
    if not is_unit_nn(step):
        return False
    return dot(step, axis_of(lock)) != 0


def literal_audit_input_paths(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        value = node.value
        if not isinstance(value, ast.Tuple):
            return None
        out: list[str] = []
        for element in value.elts:
            if not isinstance(element, ast.Constant) or not isinstance(element.value, str):
                return None
            out.append(element.value)
        return tuple(out)
    return None


def form_history() -> dict[Point, tuple[int, Point]]:
    """Incoming-lock parallel-step formation. First write wins; uniqueness not required."""
    formed: dict[Point, tuple[int, Point]] = {ORIGIN: (0, SEED_LOCK)}
    frontier: list[Point] = [ORIGIN]
    while frontier:
        nxt: list[Point] = []
        for parent in frontier:
            tick, lock = formed[parent]
            for step in NN:
                if not parallel_to_lock_axis(step, lock):
                    continue
                child = add(parent, step)
                if not in_ball(child) or child in formed:
                    continue
                formed[child] = (tick + 1, step)
                nxt.append(child)
        frontier = nxt
    return formed


def tick_of(history: dict[Point, tuple[int, Point]], site: Point) -> int | str:
    if site not in history:
        return UNDEFINED
    return history[site][0]


def reverse_status(t_a: int | str, t_b: int | str) -> str:
    if not isinstance(t_a, int) or not isinstance(t_b, int):
        return UNDEFINED
    return "hold" if 3 * t_a * t_a > t_b * t_b else "fail"


def face_status(t_c: int | str, t_d: int | str) -> str:
    if not isinstance(t_c, int) or not isinstance(t_d, int):
        return UNDEFINED
    return "hold" if t_c * t_c > 2 * t_d * t_d else "fail"


def tick1_six_mask(history: dict[Point, tuple[int, Point]]) -> tuple[int, ...]:
    mask: list[int] = []
    for step in NN:
        neighbor = add(ORIGIN, step)
        formed_at_one = neighbor in history and history[neighbor][0] == 1
        mask.append(int(formed_at_one))
    return tuple(mask)


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    source = Path(__file__).read_text(encoding="utf-8")
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    history = form_history()
    t_a = tick_of(history, PROBE_A)
    t_b = tick_of(history, PROBE_B)
    t_c = tick_of(history, PROBE_C)
    t_d = tick_of(history, PROBE_D)
    mask = tick1_six_mask(history)
    reverse = reverse_status(t_a, t_b)
    face = face_status(t_c, t_d)
    sites = ball_sites()

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries are source-bound; the parallel-step incoming-lock rule is a displayed construction")
    print("integrity_reads: this runner, its note, and the current axiom memo; no other scientific inputs")
    print("construction: B_3(0) host, seed origin lock +e_1, allowed 6-NN steps parallel to the current lock axis")
    print("negative_scope: reverse and face are displayed, not adopted; uniqueness is not required; Admissibility is not edited")
    print(f"theorem1_tick1_6mask: {mask} on NN order +e1,-e1,+e2,-e2,+e3,-e3")
    print(f"theorem1_ticks: t(A)={t_a} t(B)={t_b} t(C)={t_c} t(D)={t_d}")
    print(f"theorem2_reverse: {reverse}")
    print(f"theorem3_face: {face}")

    literal_paths = literal_audit_input_paths(source)
    declared_paths = (
        "docs/PARALLEL_STEP_INCOMING_LOCK_FORMATION_B3_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-inputs",
        "static literal AUDIT_INPUT_PATHS names the two declared files and both exist",
        AUDIT_INPUT_PATHS == declared_paths
        and literal_paths == declared_paths
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        residual=literal_paths,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility-boundary", "Admissibility does not supply formation site, probability, or rate", formation_boundary in normalized_axiom and formation_boundary in normalized_note)
    checks.check("source-admissibility-wording", "current local-distribution wording is pinned", admissibility_sentence in normalized_axiom)
    checks.check(
        "source-record-boundary",
        "current lock, content-only readout, and unreadable absence are pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )

    checks.check("host-ball", "B_3(0) is the NN graph ball of radius 3 and contains the four probes", ORIGIN in sites and {PROBE_A, PROBE_B, PROBE_C, PROBE_D}.issubset(sites) and (4, 0, 0) not in sites and len(sites) == 63)
    checks.check("seed", "origin is recorded at tick 0 with lock +e_1", history[ORIGIN] == (0, E1))
    checks.check("lock-alphabet", "lock letters are exactly the six unit NN steps", LOCK_ALPHABET == frozenset(NN) and all(taxicab(step) == 1 for step in NN))
    checks.check(
        "allowed-step-rule",
        "from lock ±e_i a unit NN step is allowed iff it is parallel to e_i",
        parallel_to_lock_axis(E1, E1)
        and parallel_to_lock_axis((-1, 0, 0), E1)
        and not parallel_to_lock_axis(E2, E1)
        and not parallel_to_lock_axis(E3, E1)
        and parallel_to_lock_axis((-1, 0, 0), (-1, 0, 0)),
    )
    checks.check("tick1-6mask", "tick-1 6-mask of the origin is (1,1,0,0,0,0)", mask == (1, 1, 0, 0, 0, 0), residual=mask)
    checks.check("tick-A", "t(A) is defined and equals 1", t_a == 1)
    checks.check("tick-B", "t(B) is undefined", t_b == UNDEFINED)
    checks.check("tick-C", "t(C) is defined and equals 2", t_c == 2)
    checks.check("tick-D", "t(D) is undefined", t_d == UNDEFINED)
    checks.check("incoming-lock-A", "A locks the incoming step +e_1", history[PROBE_A][1] == E1)
    checks.check("incoming-lock-C", "C locks the incoming step +e_1", history[PROBE_C][1] == E1)
    checks.check("reverse-undefined", "reverse 3 t(A)^2 > t(B)^2 is undefined", reverse == UNDEFINED)
    checks.check("face-undefined", "face t(C)^2 > 2 t(D)^2 is undefined", face == UNDEFINED)

    formed_sites = frozenset(history)
    axis_sites = frozenset((n, 0, 0) for n in range(-RADIUS, RADIUS + 1))
    checks.check("axis-support", "every formed site lies on the seed-lock axis inside B_3(0)", formed_sites == axis_sites)
    checks.check(
        "axis-ticks",
        "on-axis formation ticks equal |n| and off-axis ball sites remain unformed",
        all(history[(n, 0, 0)][0] == abs(n) for n in range(-RADIUS, RADIUS + 1))
        and PROBE_B not in history
        and PROBE_D not in history
        and all(point in history or point[1] != 0 or point[2] != 0 for point in sites),
    )
    checks.check(
        "perp-load-bearing",
        "perpendicular NN steps from the origin stay unformed, so reverse/face have no off-axis ticks",
        add(ORIGIN, E2) not in history
        and add(ORIGIN, E3) not in history
        and reverse == UNDEFINED
        and face == UNDEFINED,
    )
    checks.check(
        "no-collision",
        "this seed writes each formed site once; uniqueness is not required of the rule",
        len(history) == 2 * RADIUS + 1
        and all(history[site][1] in LOCK_ALPHABET for site in history),
    )
    checks.check(
        "ball-cutoff",
        "the would-be axial step to (4,0,0) is excluded by the B_3(0) host",
        in_ball((3, 0, 0))
        and not in_ball((4, 0, 0))
        and (3, 0, 0) in history
        and (4, 0, 0) not in history
        and history[(3, 0, 0)][0] == 3,
    )
    checks.check(
        "predicate-gating",
        "hold/fail require both ticks; a missing tick yields undefined rather than a boolean",
        reverse_status(1, 1) == "hold"
        and reverse_status(1, 2) == "fail"
        and face_status(3, 2) == "hold"
        and face_status(2, 2) == "fail"
        and reverse_status(1, UNDEFINED) == UNDEFINED
        and face_status(2, UNDEFINED) == UNDEFINED,
    )

    required = (
        CLAIM_SCOPE,
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write into Admissibility",
        "Uniqueness is not required",
        "tick-1 6-mask",
        "3 t(A)^2 > t(B)^2",
        "t(C)^2 > 2 t(D)^2",
        "undefined",
        'hypothetical_axiom_status: "no edit"',
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "parallel to the current lock",
        "B_3(0)",
        "seed lock +e_1",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "B_57",
        "k20",
        "Dijkstra",
        "hop-cost table",
        "new axiom",
        "Block 12",
        "trace_class: direct_blocker_closure",
        "For any finite collection of pairwise-disjoint records",
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "claim scope, display boundary, theorems, and forbidden-phrase hygiene hold",
        CLAIM_SCOPE in note
        and all(phrase in note for phrase in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "L1" in note
        and "attach L1" in note,
        residual=None,
    )
    checks.check(
        "claim-scope-field",
        "YAML claim_scope matches the declared display sentence",
        f'claim_scope: "{CLAIM_SCOPE}"' in note,
    )
    checks.check(
        "no-admissibility-write",
        "the displayed step rule is not entered as an Admissibility edit",
        "Do not write into Admissibility" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "parallel-step incoming-lock" in normalized_note
        and "displayed construction" in normalized_note,
    )

    print("per_element: tick-1 6-mask and the four named probes are enumerated")
    print("per_site: incoming lock is the forming NN step on B_3(0)")
    print("per_mode: checked and not executed — no spectral claim")
    print("per_block: reverse and face predicates are evaluated as hold/fail/undefined")
    print("lattice_wide: checked and not executed — no unbounded-host theorem")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
