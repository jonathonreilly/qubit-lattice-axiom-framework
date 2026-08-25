#!/usr/bin/env python3
"""Directed 2-step cyclic-frame transport along -e3 freeze t+1 vs t+2.

Host: Euclidean B_3(0). Process: two-axis opposite seed, perp-step incoming
lock. Reverse, face, and composition bits are displayed, not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
RUNNER_PATH = Path(__file__).resolve()

Vec = tuple[int, int, int]
Mat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Incoming = frozenset[Vec] | str
Outgoing = frozenset[Vec] | str
FrameVal = tuple[Vec, Vec, Vec] | str
Sending = tuple[Vec, Vec, Vec] | str

E1: Vec = (1, 0, 0)
E2: Vec = (0, 1, 0)
E3: Vec = (0, 0, 1)
NEG_E1: Vec = (-1, 0, 0)
NEG_E2: Vec = (0, -1, 0)
NEG_E3: Vec = (0, 0, -1)
STEP: Vec = NEG_E3
NN: tuple[Vec, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
TWO_AXIS_SEEDS: tuple[tuple[Vec, Vec], ...] = (
    ((0, 0, 0), E1),
    ((0, 1, 0), NEG_E1),
    ((0, 0, 1), E2),
    ((0, 1, 1), NEG_E2),
)
REVERSE_PROBES: tuple[Vec, ...] = ((0, 0, 0), (0, 1, 0))
FACE_PROBES: tuple[Vec, ...] = ((0, 0, 1), (0, 1, 1))
ALL_PROBES: tuple[Vec, ...] = REVERSE_PROBES + FACE_PROBES
CUTS: tuple[int, ...] = (1, 2)
UNDEFINED = "UNDEFINED"
LOCK_NAME = {
    E1: "+e_1",
    NEG_E1: "−e_1",
    E2: "+e_2",
    NEG_E2: "−e_2",
    E3: "+e_3",
    NEG_E3: "−e_3",
}
CLAIM_SCOPE = (
    "Directed 2-step cyclic-frame transport along −e3 freeze t+1 vs t+2 "
    "on the two-axis opposite seed, reverse/face at each cut, and "
    "composition, are reported. Displayed, not adopted."
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


def perpendicular(lock: Vec, step: Vec) -> bool:
    return dot(lock, step) == 0


def axis_of_letter(lock: Vec) -> Vec:
    return (abs(lock[0]), abs(lock[1]), abs(lock[2]))


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


def columns_to_matrix(col0: Vec, col1: Vec, col2: Vec) -> Mat:
    return (
        (col0[0], col1[0], col2[0]),
        (col0[1], col1[1], col2[1]),
        (col0[2], col1[2], col2[2]),
    )


def mat_mul(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3))
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


def integer_det_columns(col1: Vec, col2: Vec, col3: Vec) -> int:
    return det3(columns_to_matrix(col1, col2, col3))


def is_signed_permutation_mat(matrix: Mat) -> bool:
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


def set_display(locks: frozenset[Vec]) -> str:
    if not locks:
        return "{}"
    names = ", ".join(LOCK_NAME[lock] for lock in NN if lock in locks)
    return "{" + names + "}"


def matrix_display(value: Sending) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if value == "fail" or not isinstance(value, tuple):
        return "fail"
    rows = tuple(tuple(value[j][i] for j in range(3)) for i in range(3))
    return "[" + "; ".join(" ".join(str(entry) for entry in row) for row in rows) + "]"


def fmt_vec(vec: Vec) -> str:
    return f"({vec[0]},{vec[1]},{vec[2]})"


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


def form(
    seeds: tuple[tuple[Vec, Vec], ...] = TWO_AXIS_SEEDS,
) -> tuple[dict[Vec, int], dict[Vec, set[Vec]], dict[Vec, Vec]]:
    """Earliest formation ticks and incoming locks on B_3(0). Mixed sites emit."""
    ticks: dict[Vec, int] = {site: 0 for site, _lock in seeds}
    locks: dict[Vec, set[Vec]] = {site: {lock} for site, lock in seeds}
    seed_map: dict[Vec, Vec] = {site: lock for site, lock in seeds}
    queue: deque[tuple[Vec, int]] = deque((site, 0) for site, _lock in seeds)
    while queue:
        parent, parent_tick = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_tick = parent_tick + 1
                if child not in ticks:
                    ticks[child] = next_tick
                    locks[child] = {step}
                    queue.append((child, next_tick))
                elif ticks[child] == next_tick:
                    locks[child].add(step)
    return ticks, locks, seed_map


def incoming_set(
    site: Vec,
    tau: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> Incoming:
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    if site in seed_map:
        return frozenset({seed_map[site]})
    arrivals: dict[int, set[Vec]] = {}
    for step in NN:
        parent = sub(site, step)
        if parent not in ticks or ticks[parent] > tau:
            continue
        if any(perpendicular(lock, step) for lock in locks[parent]):
            arrivals.setdefault(ticks[parent] + 1, set()).add(step)
    if not arrivals:
        return frozenset()
    earliest = min(arrivals)
    return frozenset(arrivals[earliest])


def outgoing_set(
    site: Vec,
    tau: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> Outgoing:
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    outgoing: set[Vec] = set()
    for step in NN:
        neighbor = add(site, step)
        incoming = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if incoming == UNDEFINED:
            continue
        if not isinstance(incoming, frozenset):
            raise TypeError("incoming is not a lock set")
        if step in incoming:
            outgoing.add(step)
    return frozenset(outgoing)


def split_holds(incoming: Incoming, outgoing: Outgoing) -> bool:
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return False
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return False
    axes_in = axis_set(incoming)
    axes_out = axis_set(outgoing)
    cover = axes_in.isdisjoint(axes_out) and axes_in | axes_out == frozenset({0, 1, 2})
    return cover and len(axes_in) == 1 and len(incoming) == 1


def frame_triple(incoming: Incoming, outgoing: Outgoing) -> tuple[Vec, Vec, Vec, int, Mat] | None:
    if not split_holds(incoming, outgoing):
        return None
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return None
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


def sending_matrix(src: Mat, dst: Mat) -> Mat:
    """Unique integer P with F(dst) = F(src) P."""
    return mat_mul(mat_transpose(src), dst)


def site_tau(ticks: dict[Vec, int], site: Vec, offset: int) -> int | None:
    if site not in ticks:
        return None
    return ticks[site] + offset


def site_sides(
    site: Vec,
    offset: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> tuple[Incoming, Outgoing]:
    tau = site_tau(ticks, site, offset)
    if tau is None:
        return UNDEFINED, UNDEFINED
    return (
        incoming_set(site, tau, ticks, locks, seed_map),
        outgoing_set(site, tau, ticks, locks, seed_map),
    )


def edge_status(
    src: Vec,
    step: Vec,
    offset: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> tuple[str, Sending]:
    dst = add(src, step)
    if not in_ball(src) or not in_ball(dst):
        return "fail", "fail"
    if src not in ticks or dst not in ticks:
        return "fail", "fail"
    src_in, src_out = site_sides(src, offset, ticks, locks, seed_map)
    dst_in, dst_out = site_sides(dst, offset, ticks, locks, seed_map)
    frame_src = frame_triple(src_in, src_out)
    frame_dst = frame_triple(dst_in, dst_out)
    if frame_src is None or frame_dst is None:
        return "fail", "fail"
    matrix = sending_matrix(frame_src[4], frame_dst[4])
    if not is_signed_permutation_mat(matrix):
        return "fail", "fail"
    if det3(matrix) != frame_src[3] * frame_dst[3]:
        return "fail", "fail"
    columns = (
        (matrix[0][0], matrix[1][0], matrix[2][0]),
        (matrix[0][1], matrix[1][1], matrix[2][1]),
        (matrix[0][2], matrix[1][2], matrix[2][2]),
    )
    return "hold", columns


def one_step_status(
    start: Vec,
    offset: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> str:
    end = add(start, STEP)
    if not in_ball(start) or not in_ball(end):
        return "fail"
    status, _ = edge_status(start, STEP, offset, ticks, locks, seed_map)
    return "hold" if status == "hold" else "fail"


def two_step_status(
    start: Vec,
    offset: int,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> str:
    mid = add(start, STEP)
    end = add(mid, STEP)
    for site in (start, mid, end):
        if not in_ball(site):
            return "fail"
    first, _ = edge_status(start, STEP, offset, ticks, locks, seed_map)
    second, _ = edge_status(mid, STEP, offset, ticks, locks, seed_map)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def pair_status(bits: tuple[str, str]) -> str:
    if any(bit == "undefined" for bit in bits):
        return "undefined"
    if bits[0] == "hold" and bits[1] == "hold":
        return "hold"
    return "fail"


def composition_status(
    reverse_bits_tau1: tuple[str, str],
    face_bits_tau1: tuple[str, str],
    reverse_bits_tau2: tuple[str, str],
    face_bits_tau2: tuple[str, str],
) -> str:
    if reverse_bits_tau1 == reverse_bits_tau2 and face_bits_tau1 == face_bits_tau2:
        return "hold"
    return "fail"


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = RUNNER_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    ticks, locks, seed_map = form()

    print("Directed 2-step cyclic-frame transport along -e3 freeze t+1 vs t+2")
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
            "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_TPLUS2_COMPOSITION_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    checks.check("seed-tick-zero", all(ticks[site] == 0 for site, _lock in TWO_AXIS_SEEDS))
    checks.check(
        "seed-incoming-locks",
        all(locks[site] == {lock} for site, lock in TWO_AXIS_SEEDS),
    )
    checks.check(
        "perp-step-blocks-parallel",
        not perpendicular(E1, E1) and perpendicular(E2, E1) and perpendicular(E3, E1),
    )
    checks.check(
        "mixed-emit-end-site",
        ticks[(0, 0, -2)] == 4
        and ticks[(0, 1, -2)] == 4
        and locks[(0, 0, -2)] == {E1, NEG_E1, E2}
        and locks[(0, 1, -2)] == {E1, NEG_E1, NEG_E2},
    )

    identity = columns_to_matrix(E1, E2, E3)
    checks.check(
        "signed-permutation-identity",
        is_signed_permutation_mat(identity)
        and sending_matrix(identity, identity) == identity
        and det3(identity) == 1,
    )

    expected_first_p = {
        ((0, 0, 0), (0, 0, -1)): ((0, 0, 1), (-1, 0, 0), (0, 1, 0)),
        ((0, 1, 0), (0, 1, -1)): ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 0, 1), (0, 0, 0)): ((0, 0, -1), (-1, 0, 0), (0, -1, 0)),
        ((0, 1, 1), (0, 1, 0)): ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    }
    expected_second_p = {
        ((0, 0, 1), (0, 0, -1)): ((0, 0, 1), (-1, 0, 0), (0, 1, 0)),
        ((0, 1, 1), (0, 1, -1)): ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    }
    expected_first_display = {
        ((0, 0, 0), (0, 0, -1)): "[0 -1 0; 0 0 1; 1 0 0]",
        ((0, 1, 0), (0, 1, -1)): "[0 1 0; 0 0 1; 1 0 0]",
        ((0, 0, 1), (0, 0, 0)): "[0 -1 0; 0 0 -1; -1 0 0]",
        ((0, 1, 1), (0, 1, 0)): "[0 -1 0; 0 0 -1; 1 0 0]",
    }

    two_step_by_cut: dict[int, dict[Vec, str]] = {}
    reverse_by_cut: dict[int, str] = {}
    face_by_cut: dict[int, str] = {}
    reverse_bits_by_cut: dict[int, tuple[str, str]] = {}
    face_bits_by_cut: dict[int, tuple[str, str]] = {}
    first_p_by_cut: dict[int, dict[tuple[Vec, Vec], Sending]] = {}

    for offset in CUTS:
        print(f"cut tau=t+{offset}")
        two_step_bits: dict[Vec, str] = {}
        first_p: dict[tuple[Vec, Vec], Sending] = {}
        for probe in ALL_PROBES:
            mid = add(probe, STEP)
            end = add(mid, STEP)
            two_step_bits[probe] = two_step_status(probe, offset, ticks, locks, seed_map)
            tau = site_tau(ticks, probe, offset)
            src_in, src_out = site_sides(probe, offset, ticks, locks, seed_map)
            frame = frame_triple(src_in, src_out)
            print(
                f"probe {fmt_vec(probe)} t={ticks.get(probe, -1)} "
                f"tau={tau} two_step={two_step_bits[probe]}"
            )
            if frame is None:
                print("  F=fail Orient=fail")
            else:
                print(
                    f"  m={fmt_vec(frame[0])} o_next={fmt_vec(frame[1])} "
                    f"o_prev={fmt_vec(frame[2])} Orient={frame[3]}"
                )
            for src, dst in ((probe, mid), (mid, end)):
                status, matrix = edge_status(src, STEP, offset, ticks, locks, seed_map)
                if src == probe:
                    first_p[(src, dst)] = matrix
                p_text = matrix_display(matrix)
                print(
                    f"  edge {fmt_vec(src)}->{fmt_vec(dst)} P={p_text} edge={status}"
                )
                if (src, dst) in expected_first_p:
                    checks.check(
                        f"named-first-edge-tplus{offset}-{fmt_vec(src)}-{fmt_vec(dst)}",
                        status == "hold"
                        and matrix == expected_first_p[(src, dst)]
                        and p_text == expected_first_display[(src, dst)],
                    )
                elif probe in FACE_PROBES:
                    checks.check(
                        f"named-second-edge-tplus{offset}-{fmt_vec(src)}-{fmt_vec(dst)}",
                        status == "hold" and matrix == expected_second_p[(probe, dst)],
                    )
                else:
                    checks.check(
                        f"named-second-edge-tplus{offset}-{fmt_vec(src)}-{fmt_vec(dst)}",
                        status == "fail" and matrix == "fail",
                    )
        reverse_bits = tuple(two_step_bits[probe] for probe in REVERSE_PROBES)
        face_bits = tuple(two_step_bits[probe] for probe in FACE_PROBES)
        reverse = pair_status(reverse_bits)
        face = pair_status(face_bits)
        print(f"reverse at t+{offset}={reverse} bits={reverse_bits}")
        print(f"face at t+{offset}={face} bits={face_bits}")
        two_step_by_cut[offset] = two_step_bits
        reverse_by_cut[offset] = reverse
        face_by_cut[offset] = face
        reverse_bits_by_cut[offset] = reverse_bits
        face_bits_by_cut[offset] = face_bits
        first_p_by_cut[offset] = first_p

    composition = composition_status(
        reverse_bits_by_cut[1],
        face_bits_by_cut[1],
        reverse_bits_by_cut[2],
        face_bits_by_cut[2],
    )
    print(
        f"composition={composition} reverse=({reverse_by_cut[1]},{reverse_by_cut[2]}) "
        f"face=({face_by_cut[1]},{face_by_cut[2]})"
    )

    def seed_frame(site: Vec, offset: int) -> tuple[Vec, Vec, Vec, int] | None:
        incoming, outgoing = site_sides(site, offset, ticks, locks, seed_map)
        frame = frame_triple(incoming, outgoing)
        if frame is None:
            return None
        return frame[0], frame[1], frame[2], frame[3]

    origin_tau1 = seed_frame((0, 0, 0), 1)
    yseed_tau1 = seed_frame((0, 1, 0), 1)
    zseed_tau1 = seed_frame((0, 0, 1), 1)
    yzseed_tau1 = seed_frame((0, 1, 1), 1)
    origin_tau2 = seed_frame((0, 0, 0), 2)
    yseed_tau2 = seed_frame((0, 1, 0), 2)
    zseed_tau2 = seed_frame((0, 0, 1), 2)
    yzseed_tau2 = seed_frame((0, 1, 1), 2)
    dest_a = seed_frame((0, 0, -1), 1)
    dest_b = seed_frame((0, 1, -1), 1)
    dest_a_tau2 = seed_frame((0, 0, -1), 2)
    dest_b_tau2 = seed_frame((0, 1, -1), 2)
    checks.check(
        "theorem1-seed-frames-both-cuts",
        origin_tau1 == (E1, NEG_E2, NEG_E3, 1)
        and yseed_tau1 == (NEG_E1, E2, NEG_E3, 1)
        and zseed_tau1 == (E2, E3, NEG_E1, -1)
        and yzseed_tau1 == (NEG_E2, E3, NEG_E1, 1)
        and origin_tau1 == origin_tau2
        and yseed_tau1 == yseed_tau2
        and zseed_tau1 == zseed_tau2
        and yzseed_tau1 == yzseed_tau2,
    )
    checks.check(
        "theorem1-mid-frames-both-cuts",
        dest_a == (NEG_E3, NEG_E1, NEG_E2, -1)
        and dest_b == (NEG_E3, NEG_E1, E2, 1)
        and dest_a == dest_a_tau2
        and dest_b == dest_b_tau2
        and ticks[(0, 0, -1)] == 1
        and ticks[(0, 1, -1)] == 1,
    )
    checks.check(
        "theorem1-two-step-bits-both-cuts",
        two_step_by_cut[1][(0, 0, 0)] == "fail"
        and two_step_by_cut[1][(0, 1, 0)] == "fail"
        and two_step_by_cut[1][(0, 0, 1)] == "hold"
        and two_step_by_cut[1][(0, 1, 1)] == "hold"
        and two_step_by_cut[2][(0, 0, 0)] == "fail"
        and two_step_by_cut[2][(0, 1, 0)] == "fail"
        and two_step_by_cut[2][(0, 0, 1)] == "hold"
        and two_step_by_cut[2][(0, 1, 1)] == "hold",
    )
    checks.check(
        "theorem2-reverse-fail-both-cuts",
        reverse_by_cut[1] == "fail"
        and reverse_by_cut[2] == "fail"
        and reverse_by_cut[1] != "undefined"
        and reverse_by_cut[2] != "undefined",
    )
    checks.check(
        "theorem3-face-hold-both-cuts",
        face_by_cut[1] == "hold"
        and face_by_cut[2] == "hold"
        and face_by_cut[1] != "undefined"
        and face_by_cut[2] != "undefined",
    )
    checks.check(
        "theorem3-composition-hold",
        composition == "hold"
        and reverse_bits_by_cut[1] == reverse_bits_by_cut[2]
        and face_bits_by_cut[1] == face_bits_by_cut[2]
        and reverse_bits_by_cut[1] == ("fail", "fail")
        and face_bits_by_cut[1] == ("hold", "hold"),
    )
    checks.check(
        "not-leftover-of-one-step-freeze",
        all(
            one_step_status(probe, offset, ticks, locks, seed_map) == "hold"
            for offset in CUTS
            for probe in ALL_PROBES
        )
        and reverse_by_cut[1] == "fail"
        and reverse_by_cut[2] == "fail"
        and pair_status(
            (
                one_step_status(REVERSE_PROBES[0], 1, ticks, locks, seed_map),
                one_step_status(REVERSE_PROBES[1], 1, ticks, locks, seed_map),
            )
        )
        == "hold",
    )
    checks.check(
        "not-leftover-of-prior-freeze",
        site_tau(ticks, (0, 0, 0), 1) == 1
        and site_tau(ticks, (0, 0, 0), 2) == 2
        and site_tau(ticks, (0, 0, 0), 1) != site_tau(ticks, (0, 0, 0), 2)
        and composition == "hold",
    )
    checks.check(
        "outside-ball-is-fail",
        not in_ball((0, 0, -4))
        and two_step_status((0, 0, -3), 1, ticks, locks, seed_map) == "fail"
        and two_step_status((0, 0, -3), 2, ticks, locks, seed_map) == "fail"
        and two_step_status((0, 0, -3), 1, ticks, locks, seed_map) != "undefined",
    )
    checks.check(
        "first-p-det-matches-orient-product",
        integer_det_columns(*expected_first_p[((0, 0, 0), (0, 0, -1))]) == -1
        and integer_det_columns(*expected_first_p[((0, 1, 0), (0, 1, -1))]) == 1
        and integer_det_columns(*expected_first_p[((0, 0, 1), (0, 0, 0))]) == -1
        and integer_det_columns(*expected_first_p[((0, 1, 1), (0, 1, 0))]) == 1
        and first_p_by_cut[1] == first_p_by_cut[2],
    )

    required_note = (
        CLAIM_SCOPE,
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write into Admissibility",
        "hypothetical_axiom_status: no edit",
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "reverse at τ1: fail",
        "reverse at τ2: fail",
        "face at τ1: hold",
        "face at τ2: hold",
        "composition: hold",
        "Orient((0,0,0))=+1",
        "Orient((0,1,0))=+1",
        "Orient((0,0,1))=-1",
        "Orient((0,1,1))=+1",
        "authors no audit verdict",
        "Euclidean B_3(0)={n:n·n<=9}",
        "2-step at (0,0,0) at τ1: fail",
        "2-step at (0,1,0) at τ1: fail",
        "2-step at (0,0,1) at τ1: hold",
        "2-step at (0,1,1) at τ1: hold",
        "2-step at (0,0,0) at τ2: fail",
        "2-step at (0,1,0) at τ2: fail",
        "2-step at (0,0,1) at τ2: hold",
        "2-step at (0,1,1) at τ2: hold",
        "P=[0 -1 0; 0 0 1; 1 0 0]",
        "P=[0 1 0; 0 0 1; 1 0 0]",
        "P=[0 -1 0; 0 0 -1; -1 0 0]",
        "P=[0 -1 0; 0 0 -1; 1 0 0]",
        "first t+2 of this letter",
        "not leftover remaining-bit of HOLDING 1-step freeze",
        "no global T",
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
    )
    checks.check(
        "note-claim-scope",
        f'claim_scope: "{CLAIM_SCOPE}"' in note or CLAIM_SCOPE in note,
    )
    missing = [phrase for phrase in required_note if phrase not in note]
    checks.check(
        "note-computed-bits",
        not missing,
        detail="; ".join(missing) if missing else "",
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
