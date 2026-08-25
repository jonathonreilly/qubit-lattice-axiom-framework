#!/usr/bin/env python3
"""Directed 2-step cyclic-frame transport along +e1 at t+1.

Host: Euclidean B_3(0). Process: two-axis opposite seed, perp-step incoming
lock. Reverse and face bits are displayed, not adopted.
"""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_PLUS_E1_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
NEIGHBOR_STEPS: tuple[Vec, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
SEED_LOCKS: dict[Vec, Vec] = {
    (0, 0, 0): E1,
    (0, 1, 0): (-1, 0, 0),
    (0, 0, 1): E2,
    (0, 1, 1): (0, -1, 0),
}
REVERSE_PROBES: tuple[Vec, ...] = ((0, 0, 0), (0, 1, 0))
FACE_PROBES: tuple[Vec, ...] = ((0, 0, 1), (0, 1, 1))
ALL_PROBES: tuple[Vec, ...] = REVERSE_PROBES + FACE_PROBES
CLAIM_SCOPE = (
    "Directed 2-step cyclic-frame transport along +e1 at t+1 on the "
    "two-axis opposite seed, and reverse/face from that, are reported. "
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
        self._grow_until(1)

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


def edge_status(
    history: History, src: Vec, step: Vec, tau: int
) -> tuple[str, Mat | None]:
    dst = add(src, step)
    if not in_ball(src) or not in_ball(dst):
        return "fail", None
    if not history.formed_at(src, tau) or not history.formed_at(dst, tau):
        return "fail", None
    frame_src = history.frame(src, tau)
    frame_dst = history.frame(dst, tau)
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


def two_step_status(history: History, start: Vec, tau: int) -> str:
    mid = add(start, E1)
    end = add(start, (2, 0, 0))
    for site in (start, mid, end):
        if not in_ball(site):
            return "fail"
    first, _ = edge_status(history, start, E1, tau)
    second, _ = edge_status(history, mid, E1, tau)
    if first == "hold" and second == "hold":
        return "hold"
    return "fail"


def pair_status(bits: tuple[str, str]) -> str:
    if any(bit == "undefined" for bit in bits):
        return "undefined"
    if bits[0] == "hold" and bits[1] == "hold":
        return "hold"
    return "fail"


def fmt_vec(vec: Vec) -> str:
    return f"({vec[0]},{vec[1]},{vec[2]})"


def fmt_mat(matrix: Mat) -> str:
    return "[" + "; ".join("(" + ",".join(str(x) for x in row) + ")" for row in matrix) + "]"


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = RUNNER_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    history = History()

    print("Directed 2-step cyclic-frame transport along +e1 at t+1")
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
            "docs/TWO_AXIS_OPPOSITE_DIRECTED_TWO_STEP_PLUS_E1_CYCLIC_FRAME_TRANSPORT_TPLUS1_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    checks.check("euclidean-ball-cardinality", len(ball) == 123 and in_ball((3, 0, 0)) and not in_ball((4, 0, 0)) and not in_ball((2, 2, 2)))
    checks.check("seed-tick-zero", all(history.tick[site] == 0 for site in SEED_LOCKS))
    checks.check(
        "seed-incoming-locks",
        all(history.incoming[site] == frozenset({lock}) for site, lock in SEED_LOCKS.items()),
    )
    checks.check(
        "perp-step-blocks-parallel",
        E1 not in allowed_steps(E1) and E1 in allowed_steps(E2) and E1 in allowed_steps(E3),
    )

    tau = 1
    formed_tick1 = sorted(site for site, tick in history.tick.items() if tick <= 1)
    checks.check("tick1-record-count", len(formed_tick1) == 14, detail=str(len(formed_tick1)))

    identity = columns_to_matrix(E1, E2, E3)
    checks.check(
        "signed-permutation-identity",
        is_signed_permutation(identity)
        and transport_matrix(identity, identity) == identity
        and det3(identity) == 1,
    )

    named_edges: list[tuple[Vec, Vec]] = []
    two_step_bits: dict[Vec, str] = {}
    for probe in ALL_PROBES:
        mid = add(probe, E1)
        end = add(probe, (2, 0, 0))
        named_edges.append((probe, mid))
        named_edges.append((mid, end))
        two_step_bits[probe] = two_step_status(history, probe, tau)
        print(
            f"probe {fmt_vec(probe)} t={history.tick.get(probe, -1)} "
            f"tau={tau} two_step={two_step_bits[probe]}"
        )
        frame = history.frame(probe, tau)
        if frame is None:
            print(f"  F=fail Orient=fail")
        else:
            print(
                f"  m={fmt_vec(frame[0])} o_next={fmt_vec(frame[1])} "
                f"o_prev={fmt_vec(frame[2])} Orient={frame[3]} F={fmt_mat(frame[4])}"
            )

    edge_rows: list[str] = []
    for src, dst in named_edges:
        status, matrix = edge_status(history, src, sub(dst, src), tau)
        formed_src = history.formed_at(src, tau)
        formed_dst = history.formed_at(dst, tau)
        split_src = history.split_holds(src, tau) if formed_src else False
        split_dst = history.split_holds(dst, tau) if formed_dst else False
        p_text = fmt_mat(matrix) if matrix is not None else "fail"
        line = (
            f"{fmt_vec(src)}->{fmt_vec(dst)} formed=({int(formed_src)},{int(formed_dst)}) "
            f"split=({int(split_src)},{int(split_dst)}) P={p_text} edge={status}"
        )
        edge_rows.append(line)
        print(f"  edge {line}")
        checks.check(
            f"named-edge-{fmt_vec(src)}-{fmt_vec(dst)}",
            status == "fail" and matrix is None,
        )

    reverse_bits = tuple(two_step_bits[probe] for probe in REVERSE_PROBES)
    face_bits = tuple(two_step_bits[probe] for probe in FACE_PROBES)
    reverse = pair_status(reverse_bits)
    face = pair_status(face_bits)
    print(f"reverse={reverse} bits={reverse_bits}")
    print(f"face={face} bits={face_bits}")

    checks.check("theorem1-origin-frame", history.frame((0, 0, 0), tau) is not None)
    origin_frame = history.frame((0, 0, 0), tau)
    yseed_frame = history.frame((0, 1, 0), tau)
    zseed_frame = history.frame((0, 0, 1), tau)
    yzseed_frame = history.frame((0, 1, 1), tau)
    checks.check(
        "theorem1-seed-frames",
        origin_frame is not None
        and yseed_frame is not None
        and zseed_frame is not None
        and yzseed_frame is not None
        and origin_frame[0:4] == (E1, (0, -1, 0), (0, 0, -1), 1)
        and yseed_frame[0:4] == ((-1, 0, 0), E2, (0, 0, -1), 1)
        and zseed_frame[0:4] == (E2, E3, (-1, 0, 0), -1)
        and yzseed_frame[0:4] == ((0, -1, 0), E3, (-1, 0, 0), 1),
    )
    checks.check(
        "theorem1-mid-unformed-or-split-fail",
        not history.formed_at((1, 0, 0), tau)
        and not history.formed_at((1, 1, 0), tau)
        and history.formed_at((1, 0, 1), tau)
        and history.formed_at((1, 1, 1), tau)
        and not history.split_holds((1, 0, 1), tau)
        and not history.split_holds((1, 1, 1), tau),
    )
    checks.check(
        "theorem1-end-unformed-at-tau",
        not history.formed_at((2, 0, 0), tau)
        and not history.formed_at((2, 1, 0), tau)
        and not history.formed_at((2, 0, 1), tau)
        and not history.formed_at((2, 1, 1), tau),
    )
    checks.check(
        "theorem1-two-step-bits-fail",
        all(two_step_bits[probe] == "fail" for probe in ALL_PROBES),
    )
    checks.check("theorem2-reverse-fail", reverse == "fail" and reverse != "undefined")
    checks.check("theorem3-face-fail", face == "fail" and face != "undefined")

    both_signs = history.frame((0, 0, 1), tau)
    assert both_signs is not None
    mutated_prev = E1
    mutated = columns_to_matrix(both_signs[0], both_signs[1], mutated_prev)
    checks.check(
        "mutation-lex-largest-uses-minus",
        both_signs[2] == (-1, 0, 0)
        and det3(mutated) == 1
        and both_signs[3] == -1
        and det3(mutated) != both_signs[3],
    )
    checks.check(
        "outside-ball-is-fail",
        not in_ball((4, 0, 0)) and two_step_status(history, (3, 0, 0), tau) == "fail",
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
        "Orient((0,1,0))=+1",
        "Orient((0,0,1))=-1",
        "Orient((0,1,1))=+1",
        "authors no audit verdict",
        "Euclidean B_3(0)={n:n·n<=9}",
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
    checks.check(
        "note-computed-bits",
        all(phrase in note for phrase in required_note),
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
