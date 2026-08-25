#!/usr/bin/env python3
"""Distance-3 neighbor-read of L-path cyclic-frame transport -e3 then -e1 at t+1.

Host: Euclidean B_3(0). Process: two-axis opposite seed, perp-step incoming
lock. Distance-3 neighbor-read, reverse, and face bits are displayed, not adopted.
"""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_DISTANCE_THREE_NEIGHBOR_READ_LPATH_MINUS_E3_MINUS_E1_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
RUNNER_PATH = Path(__file__).resolve()

Vec = tuple[int, int, int]
Mat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

E1: Vec = (1, 0, 0)
E2: Vec = (0, 1, 0)
E3: Vec = (0, 0, 1)
NEG_E1: Vec = (-1, 0, 0)
NEG_E3: Vec = (0, 0, -1)
FIRST_STEP: Vec = NEG_E3
SECOND_STEP: Vec = NEG_E1
NEIGHBOR_STEPS: tuple[Vec, ...] = (
    E1,
    NEG_E1,
    E2,
    (0, -1, 0),
    E3,
    NEG_E3,
)
SEED_LOCKS: dict[Vec, Vec] = {
    (0, 0, 0): E1,
    (0, 1, 0): NEG_E1,
    (0, 0, 1): E2,
    (0, 1, 1): (0, -1, 0),
}
REVERSE_PROBES: tuple[Vec, ...] = ((0, 0, 0), (0, 1, 0))
FACE_PROBES: tuple[Vec, ...] = ((0, 0, 1), (0, 1, 1))
ALL_PROBES: tuple[Vec, ...] = REVERSE_PROBES + FACE_PROBES
CLAIM_SCOPE = (
    "Distance-3 neighbor-read of L-path cyclic-frame transport −e3 then −e1 at t+1 on "
    "the two-axis opposite seed, and reverse/face from that, are reported. "
    "Displayed, not adopted."
)


def add(left: Vec, right: Vec) -> Vec:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def sub(left: Vec, right: Vec) -> Vec:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def dot(left: Vec, right: Vec) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def neg(vec: Vec) -> Vec:
    return (-vec[0], -vec[1], -vec[2])


def in_ball(point: Vec) -> bool:
    return dot(point, point) <= 9


def axis_index(vec: Vec) -> int:
    hits = [i for i, coord in enumerate(vec) if coord != 0]
    if len(hits) != 1 or abs(vec[hits[0]]) != 1:
        raise ValueError("lock is not a signed axis vector")
    return hits[0]


def unit_axis(index: int) -> Vec:
    coords = [0, 0, 0]
    coords[index] = 1
    return (coords[0], coords[1], coords[2])


def axis_set(vectors: frozenset[Vec]) -> frozenset[int]:
    return frozenset(axis_index(vec) for vec in vectors)


def unique_lock(incoming: frozenset[Vec]) -> Vec | None:
    if len(incoming) != 1:
        return None
    return next(iter(incoming))


def allowed_steps(lock: Vec) -> tuple[Vec, ...]:
    axis = unit_axis(axis_index(lock))
    return tuple(step for step in NEIGHBOR_STEPS if dot(step, axis) == 0)


def columns_to_matrix(col0: Vec, col1: Vec, col2: Vec) -> Mat:
    return (
        (col0[0], col1[0], col2[0]),
        (col0[1], col1[1], col2[1]),
        (col0[2], col1[2], col2[2]),
    )


def mat_mul(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(
            sum(left[row][mid] * right[mid][col] for mid in range(3))
            for col in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def mat_transpose(matrix: Mat) -> Mat:
    return tuple(tuple(matrix[col][row] for col in range(3)) for row in range(3))  # type: ignore[return-value]


def det3(matrix: Mat) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def is_signed_permutation(matrix: Mat) -> bool:
    columns = [(matrix[0][col], matrix[1][col], matrix[2][col]) for col in range(3)]
    rows_used: list[int] = []
    for column in columns:
        hits = [i for i, coord in enumerate(column) if coord != 0]
        if len(hits) != 1 or abs(column[hits[0]]) != 1:
            return False
        rows_used.append(hits[0])
    return len(set(rows_used)) == 3 and abs(det3(matrix)) == 1


def lex_largest_signed_axis(options: frozenset[Vec]) -> Vec:
    """Order +e < -e on a single axis; the negative letter is largest."""
    if not options:
        raise ValueError("empty leftover-axis set")
    return max(options, key=lambda vec: next(coord for coord in vec if coord != 0) < 0)


def normalize(text: str) -> str:
    return " ".join(text.split())


def literal_audit_paths(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                try:
                    value = ast.literal_eval(node.value)
                except (TypeError, ValueError):
                    return None
                if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
                    return value
                return None
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


class History:
    """Perp-step incoming-lock records on Euclidean B_3(0)."""

    def __init__(self) -> None:
        self.tick: dict[Vec, int] = {}
        self.incoming: dict[Vec, frozenset[Vec]] = {}
        for site, lock in SEED_LOCKS.items():
            self.tick[site] = 0
            self.incoming[site] = frozenset({lock})
        self._grow_until(5)

    def _grow_until(self, last_tick: int) -> None:
        for parent_tick in range(last_tick):
            candidates: dict[Vec, set[Vec]] = {}
            for parent, formed_tick in self.tick.items():
                if formed_tick != parent_tick:
                    continue
                lock = unique_lock(self.incoming[parent])
                if lock is None:
                    continue
                for step in allowed_steps(lock):
                    child = add(parent, step)
                    if not in_ball(child) or child in self.tick:
                        continue
                    candidates.setdefault(child, set()).add(step)
            for child, steps in candidates.items():
                self.tick[child] = parent_tick + 1
                self.incoming[child] = frozenset(steps)

    def formed_at(self, site: Vec, tau: int) -> bool:
        return site in self.tick and self.tick[site] <= tau

    def M(self, site: Vec, tau: int) -> frozenset[Vec] | None:
        if not self.formed_at(site, tau):
            return None
        return self.incoming[site]

    def O(self, site: Vec, tau: int) -> frozenset[Vec] | None:
        if not self.formed_at(site, tau):
            return None
        outgoing: set[Vec] = set()
        for step in NEIGHBOR_STEPS:
            neighbor = add(site, step)
            incoming = self.M(neighbor, tau)
            if incoming is not None and step in incoming:
                outgoing.add(step)
        return frozenset(outgoing)

    def split_holds(self, site: Vec, tau: int) -> bool:
        incoming = self.M(site, tau)
        outgoing = self.O(site, tau)
        if incoming is None or outgoing is None:
            return False
        axes_in = axis_set(incoming)
        axes_out = axis_set(outgoing)
        cover = axes_in.isdisjoint(axes_out) and axes_in | axes_out == frozenset({0, 1, 2})
        return cover and len(axes_in) == 1 and len(incoming) == 1

    def frame(self, site: Vec, tau: int) -> tuple[Vec, Vec, Vec, int, Mat] | None:
        if not self.split_holds(site, tau):
            return None
        incoming = self.M(site, tau)
        outgoing = self.O(site, tau)
        assert incoming is not None and outgoing is not None
        m = next(iter(incoming))
        index = axis_index(m)
        e_next = unit_axis((index + 1) % 3)
        e_prev = unit_axis((index - 1) % 3)
        o_next_set = frozenset({e_next, neg(e_next)}) & outgoing
        o_prev_set = frozenset({e_prev, neg(e_prev)}) & outgoing
        if not o_next_set or not o_prev_set:
            return None
        o_next = lex_largest_signed_axis(o_next_set)
        o_prev = lex_largest_signed_axis(o_prev_set)
        matrix = columns_to_matrix(m, o_next, o_prev)
        orient = det3(matrix)
        if orient not in (1, -1):
            return None
        return m, o_next, o_prev, orient, matrix


def transport_matrix(src: Mat, dst: Mat) -> Mat:
    """Unique integer P with P F(src) = F(dst)."""
    return mat_mul(dst, mat_transpose(src))


def site_tau(history: History, site: Vec) -> int | None:
    if site not in history.tick:
        return None
    return history.tick[site] + 1


def edge_status(history: History, src: Vec, step: Vec) -> tuple[str, Mat | None]:
    dst = add(src, step)
    if not in_ball(src) or not in_ball(dst):
        return "fail", None
    tau_src = site_tau(history, src)
    tau_dst = site_tau(history, dst)
    if tau_src is None or tau_dst is None:
        return "fail", None
    if not history.formed_at(src, tau_src) or not history.formed_at(dst, tau_dst):
        return "fail", None
    frame_src = history.frame(src, tau_src)
    frame_dst = history.frame(dst, tau_dst)
    if frame_src is None or frame_dst is None:
        return "fail", None
    if frame_src[3] not in (1, -1) or frame_dst[3] not in (1, -1):
        return "fail", None
    matrix = transport_matrix(frame_src[4], frame_dst[4])
    if not is_signed_permutation(matrix):
        return "fail", None
    if det3(matrix) != frame_src[3] * frame_dst[3]:
        return "fail", None
    return "hold", matrix


def lpath_sites(start: Vec) -> tuple[Vec, Vec, Vec]:
    mid = add(start, FIRST_STEP)
    end = add(mid, SECOND_STEP)
    return start, mid, end


def lpath_status(history: History, start: Vec) -> str:
    start, mid, end = lpath_sites(start)
    for site in (start, mid, end):
        if not in_ball(site):
            return "fail"
    first, _ = edge_status(history, start, FIRST_STEP)
    second, _ = edge_status(history, mid, SECOND_STEP)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def one_step_minus_e3_status(history: History, start: Vec) -> str:
    end = add(start, FIRST_STEP)
    for site in (start, end):
        if not in_ball(site):
            return "fail"
    status, _ = edge_status(history, start, FIRST_STEP)
    if status == "hold":
        return "hold"
    return "fail"


def two_step_minus_e3_status(history: History, start: Vec) -> str:
    mid = add(start, FIRST_STEP)
    end = add(mid, FIRST_STEP)
    for site in (start, mid, end):
        if not in_ball(site):
            return "fail"
    first, _ = edge_status(history, start, FIRST_STEP)
    second, _ = edge_status(history, mid, FIRST_STEP)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def manhattan(left: Vec, right: Vec) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def formed_distance_two(history: History, site: Vec) -> tuple[Vec, ...]:
    neighbors: list[Vec] = []
    for x in range(-3, 4):
        for y in range(-3, 4):
            for z in range(-3, 4):
                neighbor = (x, y, z)
                if not in_ball(neighbor) or neighbor not in history.tick:
                    continue
                if manhattan(neighbor, site) == 2:
                    neighbors.append(neighbor)
    return tuple(neighbors)


def formed_distance_three(history: History, site: Vec) -> tuple[Vec, ...]:
    neighbors: list[Vec] = []
    for x in range(-3, 4):
        for y in range(-3, 4):
            for z in range(-3, 4):
                neighbor = (x, y, z)
                if not in_ball(neighbor) or neighbor not in history.tick:
                    continue
                if manhattan(neighbor, site) == 3:
                    neighbors.append(neighbor)
    return tuple(neighbors)


def distance_two_status(history: History, site: Vec) -> str:
    if lpath_status(history, site) != "hold":
        return "fail"
    for neighbor in formed_distance_two(history, site):
        if lpath_status(history, neighbor) == "hold":
            return "hold"
    return "fail"


def distance_three_status(history: History, site: Vec) -> str:
    if lpath_status(history, site) != "hold":
        return "fail"
    for neighbor in formed_distance_three(history, site):
        if lpath_status(history, neighbor) == "hold":
            return "hold"
    return "fail"


def distance_three_witnesses(history: History, site: Vec) -> tuple[Vec, ...]:
    return tuple(
        neighbor
        for neighbor in formed_distance_three(history, site)
        if lpath_status(history, neighbor) == "hold"
    )


def pair_status(bits: tuple[str, str]) -> str:
    if any(bit == "undefined" for bit in bits):
        return "undefined"
    if bits[0] == "hold" and bits[1] == "hold":
        return "hold"
    return "fail"


def fmt_vec(vec: Vec) -> str:
    return f"({vec[0]},{vec[1]},{vec[2]})"


def fmt_mat(matrix: Mat) -> str:
    return "[" + "; ".join(" ".join(str(x) for x in row) for row in matrix) + "]"


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = RUNNER_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    history = History()

    print("Distance-3 neighbor-read of L-path cyclic-frame transport -e3 then -e1 at t+1")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("displayed_not_adopted: true")

    literal_paths = literal_audit_paths(runner_src)
    checks.check(
        "audit-input-paths-literal",
        literal_paths == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_AXIS_OPPOSITE_DISTANCE_THREE_NEIGHBOR_READ_LPATH_MINUS_E3_MINUS_E1_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    checks.check(
        "audit-inputs-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"
    checks.check(
        "source-lattice",
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility-unedited",
        admissibility_sentence in normalized_axiom
        and admissibility_sentence in normalized_note
        and "Do not write into Admissibility" in note,
    )
    checks.check(
        "source-record-boundary",
        record_lock in normalized_axiom
        and record_absence in normalized_axiom
        and formation_boundary in normalized_axiom
        and record_lock in normalized_note,
    )

    ball = [
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if x * x + y * y + z * z <= 9
    ]
    checks.check(
        "euclidean-ball-cardinality",
        len(ball) == 123 and in_ball((3, 0, 0)) and not in_ball((4, 0, 0)) and not in_ball((2, 2, 2)),
    )
    checks.check("seed-tick-zero", all(history.tick[site] == 0 for site in SEED_LOCKS))
    checks.check(
        "seed-incoming-locks",
        all(history.incoming[site] == frozenset({lock}) for site, lock in SEED_LOCKS.items()),
    )
    checks.check(
        "perp-step-blocks-parallel",
        E1 not in allowed_steps(E1) and E1 in allowed_steps(E2) and E1 in allowed_steps(E3),
    )

    formed_tick1 = sorted(site for site, tick in history.tick.items() if tick <= 1)
    checks.check("tick1-record-count", len(formed_tick1) == 14, detail=str(len(formed_tick1)))

    identity = columns_to_matrix(E1, E2, E3)
    checks.check(
        "signed-permutation-identity",
        is_signed_permutation(identity)
        and transport_matrix(identity, identity) == identity
        and det3(identity) == 1,
    )

    lpath_bits: dict[Vec, str] = {}
    distance_three_bits: dict[Vec, str] = {}
    witnesses: dict[Vec, tuple[Vec, ...]] = {}
    expected_first_p = {
        ((0, 0, 0), (0, 0, -1)): ((0, 1, 0), (0, 0, 1), (-1, 0, 0)),
        ((0, 1, 0), (0, 1, -1)): ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
        ((0, 0, 1), (0, 0, 0)): ((0, 1, 0), (0, 0, -1), (1, 0, 0)),
        ((0, 1, 1), (0, 1, 0)): ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    }
    expected_second_p = {
        ((0, 0, -1), (-1, 0, -1)): ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 1, -1), (-1, 1, -1)): ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    }
    expected_witnesses = {
        (0, 0, 0): ((0, 1, 2), (1, -1, 1)),
        (0, 1, 0): ((0, 0, 2),),
        (0, 0, 1): (),
        (0, 1, 1): ((1, -1, 1),),
    }
    for probe in ALL_PROBES:
        start, mid, end = lpath_sites(probe)
        lpath_bits[probe] = lpath_status(history, probe)
        distance_three_bits[probe] = distance_three_status(history, probe)
        witnesses[probe] = distance_three_witnesses(history, probe)
        tau = site_tau(history, probe)
        print(
            f"probe {fmt_vec(probe)} t={history.tick.get(probe, -1)} "
            f"tau={tau} lpath={lpath_bits[probe]} "
            f"distance_three={distance_three_bits[probe]} "
            f"path={fmt_vec(start)}->{fmt_vec(mid)}->{fmt_vec(end)}"
        )
        for site in (start, mid, end):
            site_cut = site_tau(history, site)
            frame = history.frame(site, site_cut) if site_cut is not None else None
            if frame is None:
                print(f"  {fmt_vec(site)} t={history.tick.get(site, -1)} F=fail Orient=fail")
            else:
                print(
                    f"  {fmt_vec(site)} t={history.tick.get(site, -1)} "
                    f"m={fmt_vec(frame[0])} o_next={fmt_vec(frame[1])} "
                    f"o_prev={fmt_vec(frame[2])} Orient={frame[3]} F={fmt_mat(frame[4])}"
                )
        first_status, first_p = edge_status(history, start, FIRST_STEP)
        second_status, second_p = edge_status(history, mid, SECOND_STEP)
        print(
            f"  hop1 {fmt_vec(start)}->{fmt_vec(mid)} P="
            f"{fmt_mat(first_p) if first_p is not None else 'fail'} edge={first_status}"
        )
        print(
            f"  hop2 {fmt_vec(mid)}->{fmt_vec(end)} P="
            f"{fmt_mat(second_p) if second_p is not None else 'fail'} edge={second_status}"
        )
        print(
            f"  d3_count={len(formed_distance_three(history, probe))} "
            "witnesses="
            + (",".join(fmt_vec(item) for item in witnesses[probe]) if witnesses[probe] else "none")
        )
        checks.check(
            f"named-first-edge-{fmt_vec(start)}-{fmt_vec(mid)}",
            first_status == "hold" and first_p == expected_first_p[(start, mid)],
        )
        if (mid, end) in expected_second_p:
            checks.check(
                f"named-second-edge-{fmt_vec(mid)}-{fmt_vec(end)}",
                second_status == "hold" and second_p == expected_second_p[(mid, end)],
            )
        else:
            checks.check(
                f"named-second-edge-{fmt_vec(mid)}-{fmt_vec(end)}",
                second_status == "fail" and second_p is None,
            )

    reverse_bits = tuple(distance_three_bits[probe] for probe in REVERSE_PROBES)
    face_bits = tuple(distance_three_bits[probe] for probe in FACE_PROBES)
    reverse = pair_status(reverse_bits)
    face = pair_status(face_bits)
    print(f"reverse={reverse} bits={reverse_bits}")
    print(f"face={face} bits={face_bits}")

    origin_frame = history.frame((0, 0, 0), 1)
    yseed_frame = history.frame((0, 1, 0), 1)
    zseed_frame = history.frame((0, 0, 1), 1)
    yzseed_frame = history.frame((0, 1, 1), 1)
    mid_a = history.frame((0, 0, -1), 2)
    mid_b = history.frame((0, 1, -1), 2)
    end_a = history.frame((-1, 0, -1), 3)
    end_b = history.frame((-1, 1, -1), 3)
    checks.check(
        "theorem1-seed-frames",
        origin_frame is not None
        and yseed_frame is not None
        and zseed_frame is not None
        and yzseed_frame is not None
        and origin_frame[0:4] == (E1, (0, -1, 0), NEG_E3, 1)
        and yseed_frame[0:4] == (NEG_E1, E2, NEG_E3, 1)
        and zseed_frame[0:4] == (E2, E3, NEG_E1, -1)
        and yzseed_frame[0:4] == ((0, -1, 0), E3, NEG_E1, 1),
    )
    checks.check(
        "theorem1-path-frames",
        mid_a is not None
        and mid_b is not None
        and end_a is not None
        and end_b is not None
        and mid_a[0:4] == (NEG_E3, NEG_E1, (0, -1, 0), -1)
        and mid_b[0:4] == (NEG_E3, NEG_E1, E2, 1)
        and end_a[0:4] == (NEG_E1, (0, -1, 0), NEG_E3, -1)
        and end_b[0:4] == (NEG_E1, E2, NEG_E3, 1)
        and history.tick[(0, 0, -1)] == 1
        and history.tick[(0, 1, -1)] == 1
        and history.tick[(-1, 0, -1)] == 2
        and history.tick[(-1, 1, -1)] == 2
        and history.tick[(-1, 0, 0)] == 2
        and history.tick[(-1, 1, 0)] == 2,
    )
    checks.check(
        "theorem1-lpath-bits",
        lpath_bits[(0, 0, 0)] == "hold"
        and lpath_bits[(0, 1, 0)] == "hold"
        and lpath_bits[(0, 0, 1)] == "fail"
        and lpath_bits[(0, 1, 1)] == "fail"
        and all(lpath_bits[probe] != "undefined" for probe in ALL_PROBES),
    )
    checks.check(
        "theorem1-distance-three-bits",
        distance_three_bits[(0, 0, 0)] == "hold"
        and distance_three_bits[(0, 1, 0)] == "hold"
        and distance_three_bits[(0, 0, 1)] == "fail"
        and distance_three_bits[(0, 1, 1)] == "fail"
        and all(distance_three_bits[probe] != "undefined" for probe in ALL_PROBES),
    )
    checks.check(
        "theorem1-existential-witnesses",
        all(witnesses[probe] == expected_witnesses[probe] for probe in ALL_PROBES)
        and len(witnesses[(0, 0, 0)]) == 2
        and len(witnesses[(0, 1, 0)]) == 1,
    )
    checks.check("theorem2-reverse-hold", reverse == "hold" and reverse != "undefined")
    checks.check("theorem3-face-fail", face == "fail" and face != "undefined")

    isolated = (1, -1, 1)
    fail_site = (0, -1, 0)
    fail_neighbors = formed_distance_three(history, fail_site)
    checks.check(
        "lpath-fail-distance-three-fail-not-undefined",
        lpath_status(history, fail_site) == "fail"
        and distance_three_status(history, fail_site) == "fail"
        and distance_three_status(history, fail_site) != "undefined"
        and (0, 0, 2) in fail_neighbors
        and lpath_status(history, (0, 0, 2)) == "hold"
        and manhattan(fail_site, (0, 0, 2)) == 3
        and lpath_status(history, FACE_PROBES[1]) == "fail"
        and distance_three_status(history, FACE_PROBES[1]) == "fail"
        and distance_three_status(history, FACE_PROBES[1]) != "undefined"
        and (1, -1, 1) in formed_distance_three(history, FACE_PROBES[1])
        and manhattan(FACE_PROBES[1], (1, -1, 1)) == 3,
    )
    checks.check(
        "not-leftover-of-distance-two",
        lpath_status(history, isolated) == "hold"
        and distance_two_status(history, isolated) == "fail"
        and distance_three_status(history, isolated) == "hold"
        and distance_three_status(history, isolated) != "undefined"
        and distance_three_witnesses(history, isolated) == ((0, 0, 0), (0, 0, 2))
        and reverse == "hold"
        and face == "fail",
    )
    checks.check(
        "distance-three-not-six-neighbor",
        manhattan((0, 0, 0), (0, 1, 0)) == 1
        and (0, 1, 0) not in formed_distance_three(history, (0, 0, 0))
        and (0, 0, 0) not in formed_distance_three(history, (0, 1, 0))
        and manhattan((0, 0, 0), (0, 0, 2)) == 2
        and (0, 0, 2) not in formed_distance_three(history, (0, 0, 0))
        and manhattan((0, 0, 0), (0, 1, 2)) == 3
        and manhattan((0, 1, 0), (0, 0, 2)) == 3
        and witnesses[(0, 0, 0)] == ((0, 1, 2), (1, -1, 1))
        and witnesses[(0, 1, 0)] == ((0, 0, 2),),
    )

    one_reverse = pair_status(
        (
            one_step_minus_e3_status(history, REVERSE_PROBES[0]),
            one_step_minus_e3_status(history, REVERSE_PROBES[1]),
        )
    )
    one_face = pair_status(
        (
            one_step_minus_e3_status(history, FACE_PROBES[0]),
            one_step_minus_e3_status(history, FACE_PROBES[1]),
        )
    )
    two_reverse = pair_status(
        (
            two_step_minus_e3_status(history, REVERSE_PROBES[0]),
            two_step_minus_e3_status(history, REVERSE_PROBES[1]),
        )
    )
    two_face = pair_status(
        (
            two_step_minus_e3_status(history, FACE_PROBES[0]),
            two_step_minus_e3_status(history, FACE_PROBES[1]),
        )
    )
    checks.check(
        "not-leftover-of-one-step-minus-e3",
        one_reverse == "hold"
        and one_face == "hold"
        and reverse == "hold"
        and face == "fail",
    )
    checks.check(
        "not-leftover-of-two-step-minus-e3",
        two_reverse == "fail"
        and two_face == "hold"
        and reverse == "hold"
        and face == "fail",
    )

    both_signs = history.frame((0, 0, 1), 1)
    assert both_signs is not None
    mutated_prev = E1
    mutated = columns_to_matrix(both_signs[0], both_signs[1], mutated_prev)
    checks.check(
        "mutation-lex-largest-uses-minus",
        both_signs[2] == NEG_E1
        and det3(mutated) == 1
        and both_signs[3] == -1
        and det3(mutated) != both_signs[3],
    )
    checks.check(
        "outside-ball-is-fail",
        not in_ball((0, 0, -4))
        and lpath_status(history, (0, 0, -3)) == "fail"
        and distance_three_status(history, (0, 0, -3)) == "fail"
        and distance_three_status(history, (0, 0, -3)) != "undefined",
    )
    face_end_a = (-1, 0, 0)
    face_end_b = (-1, 1, 0)
    checks.check(
        "face-second-hop-split-fail",
        history.split_holds(face_end_a, 3) is False
        and history.split_holds(face_end_b, 3) is False
        and history.frame(face_end_a, 3) is None
        and history.frame(face_end_b, 3) is None,
    )

    required_note = (
        CLAIM_SCOPE,
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write into Admissibility",
        "hypothetical_axiom_status: no edit",
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "reverse: hold",
        "face: fail",
        "Orient((0,0,0))=+1",
        "Orient((0,1,0))=+1",
        "Orient((0,0,1))=-1",
        "Orient((0,1,1))=+1",
        "authors no audit verdict",
        "Euclidean B_3(0)={n:n·n<=9}",
        "L-path at (0,0,0): hold",
        "L-path at (0,1,0): hold",
        "L-path at (0,0,1): fail",
        "L-path at (0,1,1): fail",
        "distance-3 at (0,0,0): hold",
        "distance-3 at (0,1,0): hold",
        "distance-3 at (0,0,1): fail",
        "distance-3 at (0,1,1): fail",
        "P=[0 1 0; 0 0 1; -1 0 0]",
        "P=[0 -1 0; 0 0 -1; 1 0 0]",
        "P=[0 1 0; 0 0 -1; 1 0 0]",
        "P=[0 1 0; 0 0 1; 1 0 0]",
        "P=[0 0 1; 1 0 0; 0 1 0]",
        "P=[0 0 1; -1 0 0; 0 -1 0]",
        "If L-path fails at `q`, distance-3 fails, not UNDEFINED",
        "Uniqueness is not required",
        "occupied half",
        "no global T",
        "not leftover of the 1-step along",
        "not leftover of the 2-step along",
        "not leftover of the distance-2",
        "(1,-1,1)",
        "witnesses (0,1,2), (1,-1,1)",
        "witnesses (0,0,2)",
        "witnesses none",
        "witnesses (1,-1,1)",
    )
    forbidden_note = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Dijkstra",
        "Cl(3,0)",
        "S^+",
        "S⁺",
        "unique P_+",
        "occupancy n",
        "new axiom",
        "Gram",
    )
    checks.check(
        "note-claim-scope",
        f'claim_scope: "{CLAIM_SCOPE}"' in note or CLAIM_SCOPE in note,
    )
    missing = [phrase for phrase in required_note if phrase not in note]
    checks.check(
        "note-computed-bits",
        not missing,
        detail=("missing:" + ",".join(missing) if missing else ""),
    )
    checks.check(
        "note-forbidden-phrases",
        not any(phrase in note for phrase in forbidden_note)
        and "promoted" not in note.lower()
        and "toe-lphys" not in note,
    )
    other = note
    for line in (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "actual_current_surface_status: bounded-support",
    ):
        other = other.replace(line, "")
    checks.check(
        "note-no-status-overclaim",
        "audit_required_before_effective_retained: true" in note
        and "bare_retained_allowed: false" in note
        and "retained" not in other.lower(),
    )
    checks.check(
        "axiom-file-unedited-by-this-packet",
        "Lattice / Physical Locality" in axiom and "Qubit / Site Possibility" in axiom,
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
