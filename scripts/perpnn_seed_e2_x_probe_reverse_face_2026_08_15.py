#!/usr/bin/env python3
"""Perp-step incoming-lock formation ticks on B_3(0) with seed lock +e_2.

Host is the closed taxicab ball of radius 3. Lock letters are six-neighbor
steps. From a recorded site the next step must be orthogonal to the lock
letter; the newly formed site records that incoming step. Seed lock at the
origin is +e_2. Probes stay on the x family. Reverse and face comparisons
are displayed, not adopted.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERPNN_SEED_E2_X_PROBE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERPNN_SEED_E2_X_PROBE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Perp-step incoming-lock formation-tick reverse and face at k=1 on "
    "B_3(0) with seed lock +e_2 and x-probes are reported. Displayed, not "
    "adopted."
)

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
STEPS: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
PROBE_A: Point = (1, 0, 0)
PROBE_B: Point = (1, 1, 1)
PROBE_C: Point = (2, 0, 0)
PROBE_D: Point = (1, 1, 0)
HOST_RADIUS = 3
SEED_LOCK: Point = E2
MAX_TICK = 12

FORBIDDEN_NOTE = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "hop-cost",
    "B_57",
    "k20",
    "new axiom",
)
FORBIDDEN_SCRIPT = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "hop-cost",
    "B_57",
    "k20",
    "networkx",
    "heapq",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def taxicab(point: Point) -> int:
    return abs(point[0]) + abs(point[1]) + abs(point[2])


def in_host(point: Point) -> bool:
    return taxicab(point) <= HOST_RADIUS


def host_sites() -> frozenset[Point]:
    sites: set[Point] = set()
    for x in range(-HOST_RADIUS, HOST_RADIUS + 1):
        for y in range(-HOST_RADIUS, HOST_RADIUS + 1):
            rest = HOST_RADIUS - abs(x) - abs(y)
            for z in range(-rest, rest + 1):
                sites.add((x, y, z))
    return frozenset(sites)


def allowed_step(lock: Point, step: Point) -> bool:
    return step in STEPS and dot(step, lock) == 0


def form_history(
    seed_lock: Point = SEED_LOCK,
) -> tuple[dict[Point, int], dict[Point, frozenset[Point]]]:
    """First-arrival perp-step formation. Lock sets may be non-unique."""
    times: dict[Point, int] = {ORIGIN: 0}
    locks: dict[Point, frozenset[Point]] = {ORIGIN: frozenset({seed_lock})}
    formed_at: dict[int, list[Point]] = {0: [ORIGIN]}
    for tick in range(0, MAX_TICK + 1):
        parents = formed_at.get(tick)
        if not parents:
            break
        incoming: dict[Point, set[Point]] = defaultdict(set)
        for parent in parents:
            for lock in locks[parent]:
                for step in STEPS:
                    if not allowed_step(lock, step):
                        continue
                    child = add(parent, step)
                    if not in_host(child) or child in times:
                        continue
                    incoming[child].add(step)
        for child, letters in incoming.items():
            times[child] = tick + 1
            locks[child] = frozenset(letters)
            formed_at.setdefault(tick + 1, []).append(child)
    return times, locks


def tick1_mask(times: dict[Point, int]) -> tuple[int, ...]:
    return tuple(1 if times.get(step) == 1 else 0 for step in STEPS)


def reverse_status(times: dict[Point, int]) -> str:
    if PROBE_A not in times or PROBE_B not in times:
        return "undefined"
    left = 3 * times[PROBE_A] ** 2
    right = times[PROBE_B] ** 2
    return "holds" if left > right else "fails"


def face_status(times: dict[Point, int]) -> str:
    if PROBE_C not in times or PROBE_D not in times:
        return "undefined"
    left = times[PROBE_C] ** 2
    right = 2 * times[PROBE_D] ** 2
    return "holds" if left > right else "fails"


def rotate_e1_to_e2(point: Point) -> Point:
    """Proper cubic map sending e_1 to e_2, used only as a relabel control."""
    x, y, z = point
    return (-y, x, z)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
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
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    script_text = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    times, locks = form_history()
    mask = tick1_mask(times)
    reverse = reverse_status(times)
    face = face_status(times)
    t_a = times.get(PROBE_A)
    t_b = times.get(PROBE_B)
    t_c = times.get(PROBE_C)
    t_d = times.get(PROBE_D)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"claim_scope: {CLAIM_SCOPE}")
    print(f"seed_lock: +e_2={SEED_LOCK}")
    print(f"tick1_6_mask_order_+e1_-e1_+e2_-e2_+e3_-e3: {mask}")
    print(f"t(A)={t_a} t(B)={t_b} t(C)={t_c} t(D)={t_d}")
    print(f"reverse: 3 t(A)^2 > t(B)^2 is {reverse}")
    print(f"face: t(C)^2 > 2 t(D)^2 is {face}")
    print("displayed_not_adopted: true")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and current axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/PERPNN_SEED_E2_X_PROBE_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        AUDIT_INPUT_PATHS,
    )
    checks.check(
        "audit-timeout-declared",
        "timeout is the standard 120 second bound",
        AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "host-is-taxicab-ball-radius-3",
        "B_3(0) is the closed taxicab ball of radius 3",
        HOST_RADIUS == 3
        and in_host(ORIGIN)
        and in_host(PROBE_B)
        and in_host((3, 0, 0))
        and not in_host((4, 0, 0))
        and not in_host((2, 2, 0))
        and len(host_sites()) == 63,
    )
    checks.check(
        "seed-origin-tick-0-plus-e2",
        "origin is recorded at tick 0 with lock letter +e_2",
        times[ORIGIN] == 0 and locks[ORIGIN] == frozenset({E2}),
        (times[ORIGIN], locks[ORIGIN]),
    )
    checks.check(
        "perp-step-rule",
        "a six-neighbor step is allowed only when it is orthogonal to the lock letter",
        allowed_step(E2, E1)
        and allowed_step(E2, E3)
        and not allowed_step(E2, E2)
        and not allowed_step(E2, (0, -1, 0))
        and allowed_step(E1, E2)
        and not allowed_step(E1, E1),
    )
    checks.check(
        "tick1-6-mask",
        "tick-1 six-mask of the origin is (1,1,0,0,1,1) in ±e_1, ±e_2, ±e_3 order",
        mask == (1, 1, 0, 0, 1, 1)
        and times.get(E1) == 1
        and times.get((-1, 0, 0)) == 1
        and times.get(E3) == 1
        and times.get((0, 0, -1)) == 1
        and times.get(E2) != 1,
        mask,
    )
    checks.check(
        "probe-times",
        "x-probes form at t(A)=1, t(B)=3, t(C)=4, t(D)=2",
        t_a == 1 and t_b == 3 and t_c == 4 and t_d == 2,
        (t_a, t_b, t_c, t_d),
    )
    checks.check(
        "uniqueness-not-required",
        "first-arrival times are reported; incoming lock sets need not be unique",
        locks[PROBE_A] == frozenset({E1})
        and locks[PROBE_D] == frozenset({E2})
        and len(locks[PROBE_B]) > 1
        and len(locks[PROBE_C]) > 1,
        {PROBE_B: locks[PROBE_B], PROBE_C: locks[PROBE_C]},
    )
    checks.check(
        "reverse-at-k1",
        "reverse 3 t(A)^2 > t(B)^2 fails at k=1",
        reverse == "fails"
        and t_a is not None
        and t_b is not None
        and not (3 * t_a**2 > t_b**2),
        (reverse, t_a, t_b),
    )
    checks.check(
        "face-at-k1",
        "face t(C)^2 > 2 t(D)^2 holds at k=1",
        face == "holds"
        and t_c is not None
        and t_d is not None
        and t_c**2 > 2 * t_d**2,
        (face, t_c, t_d),
    )
    checks.check(
        "seed-orthogonal-to-x-probes",
        "seed lock +e_2 is orthogonal to the x-axis of the probes",
        dot(SEED_LOCK, E1) == 0
        and PROBE_A[1:] == (0, 0)
        and PROBE_C[1:] == (0, 0)
        and PROBE_A[0] == 1
        and PROBE_C[0] == 2,
    )
    rotated = tuple(rotate_e1_to_e2(point) for point in (PROBE_A, PROBE_B, PROBE_C, PROBE_D))
    checks.check(
        "not-cubic-relabel-of-axis-seed",
        "holding x-probes fixed while seeding +e_2 is not a cubic relabel of an +e_1 seed",
        rotated != (PROBE_A, PROBE_B, PROBE_C, PROBE_D)
        and rotate_e1_to_e2(E1) == E2
        and rotated[0] == E2,
        rotated,
    )
    checks.check(
        "formed-sites-stay-in-host",
        "every formed site lies in B_3(0) and formation never leaves the host",
        all(in_host(site) for site in times)
        and set(times) <= host_sites(),
        len(times),
    )
    checks.check(
        "note-claim-scope",
        "front matter reports the displayed k=1 reverse and face scope",
        CLAIM_SCOPE in normalize(note.split("claim_scope:", 1)[1])
        if "claim_scope:" in note
        else False,
    )
    required_note = (
        "Displayed, not adopted",
        "Do not attach L1",
        "Do not write into Admissibility",
        "Uniqueness not required",
        "t(A)=1",
        "t(B)=3",
        "t(C)=4",
        "t(D)=2",
        "tick-1 6-mask",
        "(1,1,0,0,1,1)",
        "reverse fails",
        "face holds",
        "seed lock +e_2",
        "B_3(0)",
        "actual_current_surface_status: bounded-support",
        "hypothetical_axiom_status: \"no edit\"",
        "FAIL / DO NOT SHIP",
        "authors no audit verdict",
    )
    checks.check(
        "note-theorems-and-boundary",
        "the note records Theorems 1-3, the derived ticks, and the adoption boundary",
        all(phrase in normalized_note for phrase in required_note)
        and all(f"### N{index}" in note for index in range(1, 9))
        and "## Theorem 1" in note
        and "## Theorem 2" in note
        and "## Theorem 3" in note,
        [phrase for phrase in required_note if phrase not in normalized_note],
    )
    checks.check(
        "source-lattice-and-record-sentences",
        "the current axiom memo still supplies cubic nearest-neighbor sites and record locking",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom,
    )
    checks.check(
        "no-admissibility-edit",
        "the note does not write the displayed inequalities into Admissibility",
        "Do not write into Admissibility" in note
        and "new axiom" not in note.lower()
        and "hypothetical_axiom_status: \"no edit\"" in note,
    )
    note_forbidden = [phrase for phrase in FORBIDDEN_NOTE if phrase in note]
    start = script_text.find("FORBIDDEN_NOTE = (")
    end = script_text.find("def normalize")
    script_body = script_text[:start] + script_text[end:]
    script_forbidden = [phrase for phrase in FORBIDDEN_SCRIPT if phrase in script_body]
    checks.check(
        "forbidden-phrase-hygiene",
        "note and runner omit the excluded rhetoric and excluded algorithms",
        note_forbidden == [] and script_forbidden == [],
        (note_forbidden, script_forbidden),
    )
    unit_step_ok = True
    for child, tick in times.items():
        if child == ORIGIN:
            continue
        found = False
        for step in STEPS:
            parent = add(child, (-step[0], -step[1], -step[2]))
            if parent in times and times[parent] + 1 == tick:
                if any(allowed_step(lock, step) for lock in locks[parent]):
                    found = True
                    break
        unit_step_ok = unit_step_ok and found
    checks.check(
        "first-arrival-unit-tick",
        "every non-origin formed site arrives at t(p)+1 from an allowed parent",
        unit_step_ok and times[ORIGIN] == 0,
    )

    print(
        "per_element: checked — each host site and each six-neighbor step is "
        "enumerated exactly"
    )
    print(
        "per_site: checked — origin seed lock and the four x-probes are evaluated "
        "as named sites"
    )
    print("per_mode: checked and not executed — no spectral mode is used")
    print(
        "per_block: checked — tick-1 mask, reverse comparison, and face "
        "comparison are evaluated on B_3(0)"
    )
    print(
        "lattice_wide: checked and not executed — no Admissibility rewrite, "
        "no L1 attachment, and no host beyond B_3(0)"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
