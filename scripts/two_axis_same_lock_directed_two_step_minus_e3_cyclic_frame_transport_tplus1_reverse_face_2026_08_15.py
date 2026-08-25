#!/usr/bin/env python3
"""Directed 2-step cyclic-frame transport along -e3 at t+1.

Host: Euclidean B_3(0). Process: two-axis same-lock seed, perp-step incoming
lock. Directed 2-step as nm2frm2sz. Reverse and face bits are displayed,
not adopted.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_SAME_LOCK_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
RUNNER_PATH = Path(__file__).resolve()

Vec = tuple[int, int, int]
Mat = tuple[Vec, Vec, Vec]
UNDEFINED = "UNDEFINED"

E1: Vec = (1, 0, 0)
E2: Vec = (0, 1, 0)
E3: Vec = (0, 0, 1)
NEG_E1: Vec = (-1, 0, 0)
NEG_E2: Vec = (0, -1, 0)
NEG_E3: Vec = (0, 0, -1)
STEP: Vec = NEG_E3
NN: tuple[Vec, ...] = (E1, NEG_E1, E2, NEG_E2, E3, NEG_E3)
AXES: tuple[Vec, ...] = (E1, E2, E3)
SAME_LOCK_SEEDS: tuple[tuple[Vec, Vec], ...] = (
    ((0, 0, 0), E1),
    ((0, 1, 0), E1),
    ((0, 0, 1), E2),
    ((0, 1, 1), E2),
)
OPPOSITE_SEEDS: tuple[tuple[Vec, Vec], ...] = (
    ((0, 0, 0), E1),
    ((0, 1, 0), NEG_E1),
    ((0, 0, 1), E2),
    ((0, 1, 1), NEG_E2),
)
PROBES = {
    "A": (0, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
    "D": (0, 1, 1),
}
REVERSE_PROBES: tuple[Vec, ...] = (PROBES["A"], PROBES["B"])
FACE_PROBES: tuple[Vec, ...] = (PROBES["C"], PROBES["D"])
CLAIM_SCOPE = (
    "Directed 2-step cyclic-frame transport along −e3 at t+1 on the "
    "two-axis same-lock seed, and reverse/face from that, are reported. "
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


def perpendicular(lock: Vec, step: Vec) -> bool:
    return dot(lock, step) == 0


def axis_of_letter(vec: Vec) -> Vec:
    hits = [i for i, coord in enumerate(vec) if coord != 0]
    if len(hits) != 1 or abs(vec[hits[0]]) != 1:
        raise ValueError("lock is not a signed axis vector")
    coords = [0, 0, 0]
    coords[hits[0]] = 1
    return (coords[0], coords[1], coords[2])


def cyclic_units(incoming: Vec) -> tuple[Vec, Vec]:
    index = {E1: 0, E2: 1, E3: 2}[axis_of_letter(incoming)]
    return AXES[(index + 1) % 3], AXES[(index - 1) % 3]


def lex_largest_on_axis(options: frozenset[Vec], axis: Vec) -> Vec:
    signed = frozenset({axis, neg(axis)}) & options
    if not signed:
        raise ValueError("empty leftover-axis set")
    return max(signed, key=lambda vec: next(coord for coord in vec if coord != 0) < 0)


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


def integer_det_columns(col0: Vec, col1: Vec, col2: Vec) -> int:
    return (
        col0[0] * (col1[1] * col2[2] - col1[2] * col2[1])
        - col0[1] * (col1[0] * col2[2] - col1[2] * col2[0])
        + col0[2] * (col1[0] * col2[1] - col1[1] * col2[0])
    )


def transpose_columns(frame: Mat) -> Mat:
    return tuple(tuple(frame[column][row] for column in range(3)) for row in range(3))  # type: ignore[return-value]


def mul_columns(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(sum(left[k][i] * right[j][k] for k in range(3)) for i in range(3))
        for j in range(3)
    )  # type: ignore[return-value]


def sending_matrix(source: Mat, target: Mat) -> Mat:
    """Integer matrix P with F(r) = F(q) P."""
    return mul_columns(transpose_columns(source), target)


def is_signed_permutation(value: Mat) -> bool:
    for column in value:
        if any(entry not in (-1, 0, 1) for entry in column):
            return False
        if sum(abs(entry) for entry in column) != 1:
            return False
    rows = tuple(tuple(value[j][i] for j in range(3)) for i in range(3))
    return all(sum(abs(entry) for entry in row) == 1 for row in rows)


def matrix_display(value: Mat | str) -> str:
    if value in (UNDEFINED, "fail"):
        return str(value)
    if not isinstance(value, tuple) or len(value) != 3:
        raise TypeError(f"sending is not three columns or fail: {value!r}")
    rows = tuple(tuple(value[j][i] for j in range(3)) for i in range(3))
    return "[" + "; ".join(" ".join(str(entry) for entry in row) for row in rows) + "]"


def lockset_display(value: frozenset[Vec] | str) -> str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    return "{" + ",".join(fmt_vec(item) for item in sorted(value)) + "}"


def fmt_vec(vec: Vec) -> str:
    return f"({vec[0]},{vec[1]},{vec[2]})"


def form(
    seeds: tuple[tuple[Vec, Vec], ...] = SAME_LOCK_SEEDS,
) -> tuple[dict[Vec, int], dict[Vec, set[Vec]], dict[Vec, Vec]]:
    """Earliest formation ticks and incoming locks on B_3(0)."""
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
) -> frozenset[Vec] | str:
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
) -> frozenset[Vec] | str:
    if site not in ticks or ticks[site] > tau:
        return UNDEFINED
    outgoing: set[Vec] = set()
    for step in NN:
        neighbor = add(site, step)
        if not in_ball(neighbor):
            continue
        incoming = incoming_set(neighbor, tau, ticks, locks, seed_map)
        if incoming == UNDEFINED:
            continue
        if not isinstance(incoming, frozenset):
            raise TypeError(f"incoming is not a lock set: {incoming!r}")
        if step in incoming:
            outgoing.add(step)
    return frozenset(outgoing)


def site_sides(
    site: Vec,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> tuple[frozenset[Vec] | str, frozenset[Vec] | str]:
    if site not in ticks:
        return UNDEFINED, UNDEFINED
    tau = ticks[site] + 1
    return (
        incoming_set(site, tau, ticks, locks, seed_map),
        outgoing_set(site, tau, ticks, locks, seed_map),
    )


def axis_set(value: frozenset[Vec] | str) -> frozenset[Vec] | str:
    if value == UNDEFINED:
        return UNDEFINED
    if not isinstance(value, frozenset):
        raise TypeError(f"lock set is not a lock set: {value!r}")
    return frozenset(axis_of_letter(lock) for lock in value)


def axis_cover(incoming: frozenset[Vec] | str, outgoing: frozenset[Vec] | str) -> str:
    if incoming == UNDEFINED or outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or not isinstance(outgoing, frozenset):
        return UNDEFINED
    axes_m = axis_set(incoming)
    axes_o = axis_set(outgoing)
    if not isinstance(axes_m, frozenset) or not isinstance(axes_o, frozenset):
        return UNDEFINED
    if axes_m & axes_o:
        return "fail"
    if axes_m | axes_o != frozenset(AXES):
        return "fail"
    return "hold"


def axis_split(incoming: frozenset[Vec] | str, outgoing: frozenset[Vec] | str) -> str:
    cover = axis_cover(incoming, outgoing)
    if cover == UNDEFINED:
        return UNDEFINED
    if cover != "hold":
        return "fail"
    if not isinstance(incoming, frozenset):
        return "fail"
    if len(axis_set(incoming)) != 1 or len(incoming) != 1:
        return "fail"
    return "hold"


def unique_signed_m(incoming: frozenset[Vec] | str) -> Vec | str:
    if incoming == UNDEFINED:
        return UNDEFINED
    if not isinstance(incoming, frozenset) or len(incoming) != 1:
        return "fail"
    return next(iter(incoming))


def cyclic_signed_outgoing(
    incoming: frozenset[Vec] | str,
    outgoing: frozenset[Vec] | str,
) -> tuple[Vec, Vec] | str:
    signed_m = unique_signed_m(incoming)
    if signed_m == UNDEFINED:
        return UNDEFINED
    if signed_m == "fail" or not isinstance(signed_m, tuple):
        return "fail"
    if outgoing == UNDEFINED:
        return UNDEFINED
    if not isinstance(outgoing, frozenset):
        return "fail"
    e_next, e_prev = cyclic_units(signed_m)
    o_next_set = frozenset({e_next, neg(e_next)}) & outgoing
    o_prev_set = frozenset({e_prev, neg(e_prev)}) & outgoing
    if not o_next_set or not o_prev_set:
        return "fail"
    return lex_largest_on_axis(o_next_set, e_next), lex_largest_on_axis(o_prev_set, e_prev)


def frame_orient(incoming: frozenset[Vec] | str, outgoing: frozenset[Vec] | str) -> int | str:
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    plane = cyclic_signed_outgoing(incoming, outgoing)
    if signed_m == UNDEFINED or plane == UNDEFINED:
        return UNDEFINED
    if not isinstance(signed_m, tuple) or not isinstance(plane, tuple):
        return "fail"
    det = integer_det_columns(signed_m, plane[0], plane[1])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return "fail"


def frame_triple(incoming: frozenset[Vec] | str, outgoing: frozenset[Vec] | str) -> Mat | str:
    split = axis_split(incoming, outgoing)
    if split == UNDEFINED:
        return UNDEFINED
    if split != "hold":
        return "fail"
    signed_m = unique_signed_m(incoming)
    plane = cyclic_signed_outgoing(incoming, outgoing)
    if signed_m == UNDEFINED or plane == UNDEFINED:
        return UNDEFINED
    if not isinstance(signed_m, tuple) or not isinstance(plane, tuple):
        return "fail"
    return signed_m, plane[0], plane[1]


def sending_holds(source: Mat | str, target: Mat | str, orient_q: int | str, orient_r: int | str) -> str:
    if source == UNDEFINED or target == UNDEFINED:
        return UNDEFINED
    if source == "fail" or target == "fail":
        return "fail"
    if not isinstance(source, tuple) or not isinstance(target, tuple):
        return "fail"
    if orient_q not in (1, -1) or orient_r not in (1, -1):
        return "fail"
    sending = sending_matrix(source, target)
    det = integer_det_columns(sending[0], sending[1], sending[2])
    if is_signed_permutation(sending) and det == orient_q * orient_r:
        return "hold"
    return "fail"


def directed_edge_hold(
    source: Vec,
    step: Vec,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> str:
    target = add(source, step)
    if not in_ball(source) or not in_ball(target):
        return "fail"
    if source not in ticks or target not in ticks:
        return "fail"
    source_in, source_out = site_sides(source, ticks, locks, seed_map)
    target_in, target_out = site_sides(target, ticks, locks, seed_map)
    source_split = axis_split(source_in, source_out)
    target_split = axis_split(target_in, target_out)
    source_orient = frame_orient(source_in, source_out)
    target_orient = frame_orient(target_in, target_out)
    if (
        source_split != "hold"
        or target_split != "hold"
        or source_orient not in (1, -1)
        or target_orient not in (1, -1)
    ):
        return "fail"
    source_frame = frame_triple(source_in, source_out)
    target_frame = frame_triple(target_in, target_out)
    sending = sending_holds(source_frame, target_frame, source_orient, target_orient)
    if sending == UNDEFINED:
        return "fail"
    return sending


def directed_edge_sending(
    source: Vec,
    step: Vec,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> Mat | str:
    if directed_edge_hold(source, step, ticks, locks, seed_map) != "hold":
        return "fail"
    source_in, source_out = site_sides(source, ticks, locks, seed_map)
    target = add(source, step)
    target_in, target_out = site_sides(target, ticks, locks, seed_map)
    source_frame = frame_triple(source_in, source_out)
    target_frame = frame_triple(target_in, target_out)
    if not isinstance(source_frame, tuple) or not isinstance(target_frame, tuple):
        return "fail"
    return sending_matrix(source_frame, target_frame)


def two_step_hold(
    site: Vec,
    step: Vec,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> str:
    mid = add(site, step)
    end = add(mid, step)
    if not in_ball(site) or not in_ball(mid) or not in_ball(end):
        return "fail"
    first = directed_edge_hold(site, step, ticks, locks, seed_map)
    second = directed_edge_hold(mid, step, ticks, locks, seed_map)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def one_step_hold(
    site: Vec,
    step: Vec,
    ticks: dict[Vec, int],
    locks: dict[Vec, set[Vec]],
    seed_map: dict[Vec, Vec],
) -> str:
    end = add(site, step)
    if not in_ball(site) or not in_ball(end):
        return "fail"
    return directed_edge_hold(site, step, ticks, locks, seed_map)


def pair_bit(left: str, right: str) -> str:
    if left == UNDEFINED or right == UNDEFINED:
        return UNDEFINED
    if left == "hold" and right == "hold":
        return "hold"
    return "fail"


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = RUNNER_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("Directed 2-step cyclic-frame transport along -e3 at t+1")
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
            "docs/TWO_AXIS_SAME_LOCK_DIRECTED_TWO_STEP_MINUS_E3_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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

    ticks, locks, seed_map = form(SAME_LOCK_SEEDS)
    opp_ticks, opp_locks, opp_seeds = form(OPPOSITE_SEEDS)
    checks.check("seed-tick-zero", all(ticks[site] == 0 for site, _lock in SAME_LOCK_SEEDS))
    checks.check(
        "same-lock-pairs",
        seed_map[(0, 0, 0)] == seed_map[(0, 1, 0)] == E1
        and seed_map[(0, 0, 1)] == seed_map[(0, 1, 1)] == E2
        and SAME_LOCK_SEEDS != OPPOSITE_SEEDS,
    )
    checks.check(
        "perp-step-blocks-parallel",
        not perpendicular(E1, E1) and perpendicular(E1, E2) and perpendicular(E1, E3),
    )

    identity_frame = (E1, NEG_E2, NEG_E3)
    identity_target = (NEG_E3, NEG_E1, NEG_E2)
    identity_sending = sending_matrix(identity_frame, identity_target)
    checks.check(
        "sending-identity",
        sending_matrix(identity_frame, identity_frame) == (E1, E2, E3)
        and is_signed_permutation((E1, E2, E3))
        and sending_holds(identity_frame, identity_target, 1, -1) == "hold"
        and integer_det_columns(*identity_sending) == -1
        and mul_columns(identity_frame, identity_sending) == identity_target,
    )

    two_step: dict[str, str] = {}
    first_edge: dict[str, str] = {}
    second_edge: dict[str, str] = {}
    first_p: dict[str, Mat | str] = {}
    second_p: dict[str, Mat | str] = {}
    frames: dict[str, Mat | str] = {}
    orient: dict[str, int | str] = {}
    split: dict[str, str] = {}
    one_step: dict[str, str] = {}
    for name, site in PROBES.items():
        mid = add(site, STEP)
        end = add(mid, STEP)
        incoming, outgoing = site_sides(site, ticks, locks, seed_map)
        split[name] = axis_split(incoming, outgoing)
        frames[name] = frame_triple(incoming, outgoing)
        orient[name] = frame_orient(incoming, outgoing)
        first_edge[name] = directed_edge_hold(site, STEP, ticks, locks, seed_map)
        second_edge[name] = directed_edge_hold(mid, STEP, ticks, locks, seed_map)
        first_p[name] = directed_edge_sending(site, STEP, ticks, locks, seed_map)
        second_p[name] = directed_edge_sending(mid, STEP, ticks, locks, seed_map)
        two_step[name] = two_step_hold(site, STEP, ticks, locks, seed_map)
        one_step[name] = one_step_hold(site, STEP, ticks, locks, seed_map)
        print(
            f"{name} {fmt_vec(site)} t={ticks[site]} "
            f"M={lockset_display(incoming)} O={lockset_display(outgoing)} "
            f"split={split[name]} F={frames[name]} Orient={orient[name]} "
            f"edge1={first_edge[name]} P1={matrix_display(first_p[name])} "
            f"edge2={second_edge[name]} P2={matrix_display(second_p[name])} "
            f"two-step={two_step[name]}"
        )
        print(f"  chain {fmt_vec(site)} -> {fmt_vec(mid)} -> {fmt_vec(end)}")

    reverse = pair_bit(two_step["A"], two_step["B"])
    face = pair_bit(two_step["C"], two_step["D"])
    one_reverse = pair_bit(one_step["A"], one_step["B"])
    one_face = pair_bit(one_step["C"], one_step["D"])
    opp_two = {
        name: two_step_hold(site, STEP, opp_ticks, opp_locks, opp_seeds)
        for name, site in PROBES.items()
    }
    opp_reverse = pair_bit(opp_two["A"], opp_two["B"])
    opp_face = pair_bit(opp_two["C"], opp_two["D"])
    plus_e3 = {
        name: two_step_hold(site, E3, ticks, locks, seed_map) for name, site in PROBES.items()
    }
    print(f"reverse={reverse} bits=({two_step['A']},{two_step['B']})")
    print(f"face={face} bits=({two_step['C']},{two_step['D']})")

    dest_a_in, dest_a_out = site_sides((0, 0, -1), ticks, locks, seed_map)
    dest_b_in, dest_b_out = site_sides((0, 1, -1), ticks, locks, seed_map)
    end_a_in, end_a_out = site_sides((0, 0, -2), ticks, locks, seed_map)
    end_b_in, end_b_out = site_sides((0, 1, -2), ticks, locks, seed_map)

    checks.check(
        "theorem1-seed-frames",
        frames["A"] == (E1, NEG_E2, NEG_E3)
        and orient["A"] == 1
        and frames["B"] == (E1, E2, NEG_E3)
        and orient["B"] == -1
        and frames["C"] == "fail"
        and orient["C"] == "fail"
        and split["C"] == "fail"
        and frames["D"] == (E2, E3, NEG_E1)
        and orient["D"] == -1
        and ticks[PROBES["A"]] == ticks[PROBES["B"]] == ticks[PROBES["C"]] == ticks[PROBES["D"]] == 0,
    )
    checks.check(
        "theorem1-zseed-split-fail-not-undefined",
        split["C"] == "fail"
        and split["C"] != UNDEFINED
        and incoming_set(PROBES["C"], 1, ticks, locks, seed_map) == frozenset({E2})
        and E2 in (outgoing_set(PROBES["C"], 1, ticks, locks, seed_map) or frozenset())
        and two_step["C"] == "fail"
        and two_step["C"] != UNDEFINED,
    )
    checks.check(
        "theorem1-dest-and-second-hop",
        frame_triple(dest_a_in, dest_a_out) == (NEG_E3, NEG_E1, NEG_E2)
        and frame_orient(dest_a_in, dest_a_out) == -1
        and frame_triple(dest_b_in, dest_b_out) == (NEG_E3, NEG_E1, E2)
        and frame_orient(dest_b_in, dest_b_out) == 1
        and ticks[(0, 0, -1)] == 1
        and ticks[(0, 1, -1)] == 1
        and ticks[(0, 0, -2)] == 4
        and ticks[(0, 1, -2)] == 4
        and axis_split(end_a_in, end_a_out) == "fail"
        and axis_split(end_b_in, end_b_out) == "fail"
        and axis_split(end_a_in, end_a_out) != UNDEFINED,
    )
    expected_p_a = ((0, 0, 1), (-1, 0, 0), (0, 1, 0))
    expected_p_d_first = ((0, 0, -1), (1, 0, 0), (0, -1, 0))
    checks.check(
        "theorem1-named-edges-and-two-step",
        first_edge["A"] == "hold"
        and second_edge["A"] == "fail"
        and two_step["A"] == "fail"
        and first_edge["B"] == "hold"
        and second_edge["B"] == "fail"
        and two_step["B"] == "fail"
        and first_edge["C"] == "fail"
        and two_step["C"] == "fail"
        and first_edge["D"] == "hold"
        and second_edge["D"] == "hold"
        and two_step["D"] == "hold"
        and first_p["A"] == expected_p_a
        and first_p["B"] == expected_p_a
        and first_p["C"] == "fail"
        and first_p["D"] == expected_p_d_first
        and second_p["D"] == expected_p_a
        and integer_det_columns(*expected_p_a) == -1
        and integer_det_columns(*expected_p_d_first) == 1
        and matrix_display(expected_p_a) == "[0 -1 0; 0 0 1; 1 0 0]"
        and matrix_display(expected_p_d_first) == "[0 1 0; 0 0 -1; -1 0 0]",
    )
    checks.check(
        "theorem1-chains-in-ball",
        all(
            in_ball(PROBES[name])
            and in_ball(add(PROBES[name], STEP))
            and in_ball(add(add(PROBES[name], STEP), STEP))
            for name in ("A", "B", "C", "D")
        ),
    )
    checks.check(
        "theorem2-reverse-fail",
        reverse == "fail" and reverse != UNDEFINED and two_step["A"] == "fail" and two_step["B"] == "fail",
    )
    checks.check(
        "theorem3-face-fail",
        face == "fail" and face != UNDEFINED and two_step["C"] == "fail" and two_step["D"] == "hold",
    )
    checks.check(
        "not-leftover-of-one-step",
        one_reverse == "hold"
        and one_face == "fail"
        and reverse == "fail"
        and one_step["A"] == "hold"
        and two_step["A"] == "fail",
    )
    checks.check(
        "not-leftover-of-opposite-two-step",
        opp_reverse == "fail"
        and opp_face == "hold"
        and face == "fail"
        and opp_two["C"] == "hold"
        and two_step["C"] == "fail",
    )
    checks.check(
        "not-leftover-of-plus-e3",
        plus_e3["A"] == "fail"
        and plus_e3["B"] == "hold"
        and plus_e3["C"] == "fail"
        and plus_e3["D"] == "fail"
        and two_step["B"] == "fail"
        and two_step["D"] == "hold",
    )
    checks.check(
        "outside-ball-is-fail",
        not in_ball((0, 0, -4))
        and not in_ball((0, 1, 3))
        and two_step_hold((0, 0, -3), STEP, ticks, locks, seed_map) == "fail"
        and two_step_hold((0, 0, -3), STEP, ticks, locks, seed_map) != UNDEFINED
        and two_step_hold(PROBES["D"], E3, ticks, locks, seed_map) == "fail"
        and two_step_hold(PROBES["D"], E3, ticks, locks, seed_map) != UNDEFINED,
    )

    required_note = (
        CLAIM_SCOPE,
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write into Admissibility",
        "hypothetical_axiom_status: no edit",
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "reverse: fail",
        "face: fail",
        "Orient((0,0,0))=+1",
        "Orient((0,1,0))=-1",
        "Orient((0,0,1)) fail",
        "Orient((0,1,1))=-1",
        "authors no audit verdict",
        "Euclidean B_3(0)={n:n·n<=9}",
        "two-step(A) = fail",
        "two-step(B) = fail",
        "two-step(C) = fail",
        "two-step(D) = hold",
        "P=[0 -1 0; 0 0 1; 1 0 0]",
        "P=[0 1 0; 0 0 -1; -1 0 0]",
        "not leftover of the 1-step",
        "not leftover of the opposite-lock directed 2-step",
        "no global T",
        "two disjoint same-lock pairs",
        "Uniqueness of P is not required",
        "A vertex outside B_3(0) is fail, not UNDEFINED",
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
        detail=str(missing) if missing else "",
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
