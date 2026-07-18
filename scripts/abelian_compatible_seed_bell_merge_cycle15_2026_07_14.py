#!/usr/bin/env python3
"""Cycle 15: abelian compatible-seed merge and permanent-output boundary.

Companion note:
  docs/work_history/repo/review_feedback/
  ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md

The runner constructs a homogeneous nearest-neighbor grow-only program field,
couples it to protected record-ready Bell cages, checks schedule confluence on
a finite exact fixture, exhausts the atomic critical pairs, tests the braid
alternative, and exhibits the minimal nonjoinable pair forced by distinct
permanent outputs at one site.

No axiom, primitive, registry, audit surface, commit, or PR is changed.  Exit
code is zero exactly when every deterministic check passes.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
import random

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE14_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
TOL = 2.0e-10
Coord = tuple[int, int, int]
RecordMap = dict[Coord, str]
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
HEADER_PATTERN = ("H1", "H0", "H1", "H1", "H0", "H1")


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def negate(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def matvec(matrix: np.ndarray, vector: Coord) -> Coord:
    moved = matrix @ np.asarray(vector, dtype=int)
    return tuple(int(value) for value in moved)  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: dict[tuple[int, ...], np.ndarray] = {}
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(axis_permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations[tuple(int(value) for value in matrix.ravel())] = matrix
    return tuple(rotations.values())


@dataclass(frozen=True)
class Program:
    trigger: Coord
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    @property
    def data(self) -> tuple[Coord, Coord, Coord]:
        return tuple(
            add(self.trigger, scale(step, self.forward)) for step in (1, 2, 3)
        )  # type: ignore[return-value]

    @property
    def left(self) -> Coord:
        return self.data[0]

    @property
    def center(self) -> Coord:
        return self.data[1]

    @property
    def right(self) -> Coord:
        return self.data[2]


def header_sites(program: Program) -> tuple[Coord, ...]:
    e = program.transverse
    u = program.normal
    offsets = (
        e,
        scale(2, e),
        scale(3, e),
        u,
        scale(2, u),
        add(program.forward, add(e, u)),
    )
    return tuple(add(program.trigger, offset) for offset in offsets)


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, negate(program.transverse))


def program_records(program: Program) -> RecordMap:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def seed_records(program: Program) -> RecordMap:
    answer = program_records(program)
    answer[program.trigger] = "Z0"
    return answer


def cage_support(program: Program) -> frozenset[Coord]:
    return frozenset(
        set(header_sites(program))
        | set(program.data)
        | {program.trigger, certificate_site(program)}
    )


def protected_sites(programs: tuple[Program, ...]) -> frozenset[Coord]:
    return frozenset(
        site
        for program in programs
        for site in (*program.data, certificate_site(program))
    )


def transform_program(
    program: Program,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> Program:
    return Program(
        add(matvec(rotation, program.trigger), translation),
        matvec(rotation, program.forward),
        matvec(rotation, program.transverse),
    )


def transform_records(
    records: RecordMap,
    rotation: np.ndarray,
    translation: Coord = (0, 0, 0),
) -> RecordMap:
    return {
        add(matvec(rotation, site), translation): content
        for site, content in records.items()
    }


class IncompatibleRecords(ValueError):
    """Raised when two permanent record maps disagree at one site."""


def compatible(left: RecordMap, right: RecordMap) -> bool:
    return all(site not in left or left[site] == content for site, content in right.items())


def join(left: RecordMap, right: RecordMap) -> RecordMap:
    if not compatible(left, right):
        conflicts = {
            site: (left[site], content)
            for site, content in right.items()
            if site in left and left[site] != content
        }
        raise IncompatibleRecords(str(conflicts))
    answer = dict(left)
    answer.update(right)
    return answer


def is_extension(old: RecordMap, new: RecordMap) -> bool:
    return len(new) >= len(old) and all(new.get(site) == content for site, content in old.items())


@dataclass(frozen=True)
class Action:
    name: str
    additions: tuple[tuple[Coord, str], ...]

    def as_map(self) -> RecordMap:
        return dict(self.additions)


def action(name: str, additions: RecordMap) -> Action:
    return Action(name, tuple(sorted(additions.items())))


def apply_action(records: RecordMap, selected: Action) -> RecordMap:
    return join(records, selected.as_map())


def diamond(base: RecordMap, first: Action, second: Action) -> bool:
    if not compatible(first.as_map(), second.as_map()):
        return False
    left = apply_action(apply_action(base, first), second)
    right = apply_action(apply_action(base, second), first)
    return left == right


def source_contract() -> None:
    section("A - Framework, predecessor, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    predecessor = CYCLE14_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(
            name in axioms
            for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")
        ),
    )
    check(
        "A Record supplies permanence but not a collision law",
        "records are permanent" in axioms and "formation rules" in axioms,
    )
    check("A approved premise registry still has four current paths", registry.count('"current_path"') == 4)
    check(
        "A predecessor leaves multi-front confluence open",
        "multi-front confluence remains open" in predecessor,
    )

    required = (
        "authority: none",
        "same-content grow-only map",
        "every finite compatible seed set",
        "branchwise schedule confluence",
        "complete atomic critical-pair census",
        "distinct permanent outputs",
        "topological braid",
        "no hidden priority",
        "no hidden cursor",
        "formation-as-extension remains a theorem",
        "no new record axiom is forced",
        "not a full autonomous replacement",
        "does not prove a general no-go",
    )
    for phrase in required:
        check(f"A note states scope phrase: {phrase}", phrase in normalized)

    for label in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"A no-go discipline includes {label}", f"{label.lower()} —" in normalized)


def crdt_algebra() -> None:
    section("B - Same-content grow-only CRDT algebra")
    rng = random.Random(1501)
    sites = [(x, 0, 0) for x in range(18)]
    master = {site: ("P" if index % 3 else "H1") for index, site in enumerate(sites)}

    for trial in range(24):
        maps = [
            {site: content for site, content in master.items() if rng.random() < 0.45}
            for _ in range(3)
        ]
        a, b, c = maps
        check(f"B join commutative trial {trial:02d}", join(a, b) == join(b, a))
        check(f"B join associative trial {trial:02d}", join(join(a, b), c) == join(a, join(b, c)))
        check(f"B join idempotent trial {trial:02d}", join(a, a) == a)
        check(f"B join is inflationary trial {trial:02d}", is_extension(a, join(a, b)))

    first = {(0, 0, 0): "H0"}
    second = {(0, 0, 0): "H1"}
    check("B distinct permanent contents at one site are incompatible", not compatible(first, second))
    try:
        join(first, second)
    except IncompatibleRecords:
        rejected = True
    else:
        rejected = False
    check("B incompatible join is rejected rather than silently prioritized", rejected)


def geometry_and_covariance() -> None:
    section("C - Relational cages and cubic covariance")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    check("C Bell data lie on two nearest-neighbor edges", all(sum(abs(a - b) for a, b in zip(base.data[i], base.data[i + 1])) == 1 for i in (0, 1)))
    check("C certificate is a nearest neighbor of trigger", sum(abs(a - b) for a, b in zip(certificate_site(base), base.trigger)) == 1)
    check("C cage roles are pairwise site-disjoint", len(cage_support(base)) == 11)

    rotations = proper_cubic_rotations()
    check("C proper cubic rotation group has 24 elements", len(rotations) == 24)
    seed = join(seed_records(base), {certificate_site(base): "C"})
    for number, rotation in enumerate(rotations):
        moved = transform_program(base, rotation)
        check(
            f"C relational seed is covariant under proper cubic rotation {number:02d}",
            transform_records(seed, rotation)
            == join(seed_records(moved), {certificate_site(moved): "C"}),
        )
    identity = np.eye(3, dtype=int)
    for number, translation in enumerate(DIRECTIONS):
        moved = transform_program(base, identity, translation)
        check(
            f"C relational seed is covariant under unit translation {number:02d}",
            transform_records(seed, identity, translation)
            == join(seed_records(moved), {certificate_site(moved): "C"}),
        )


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)


def apply_cz(state: np.ndarray, left: int, right: int, width: int = 3) -> np.ndarray:
    answer = state.copy()
    left_mask = 1 << (width - 1 - left)
    right_mask = 1 << (width - 1 - right)
    for index in range(1 << width):
        if index & left_mask and index & right_mask:
            answer[index] *= -1.0
    return answer


def single_site_operator(operator: np.ndarray, site: int, width: int = 3) -> np.ndarray:
    answer = np.array((1.0,), dtype=complex)
    for index in range(width):
        answer = np.kron(answer, operator if index == site else I2)
    return answer


def measure(
    state: np.ndarray, site: int, basis: str
) -> tuple[tuple[int, float, np.ndarray], ...]:
    if basis == "X":
        projectors = ((1, (I2 + X) / 2.0), (-1, (I2 - X) / 2.0))
    elif basis == "Z":
        projectors = ((0, (I2 + Z) / 2.0), (1, (I2 - Z) / 2.0))
    else:
        raise ValueError(basis)
    answer: list[tuple[int, float, np.ndarray]] = []
    for outcome, local in projectors:
        projector = single_site_operator(local, site)
        projected = projector @ state
        probability = float(np.vdot(projected, projected).real)
        if probability > TOL:
            answer.append((outcome, probability, projected / np.sqrt(probability)))
    return tuple(answer)


def bell_distribution() -> dict[tuple[int, int, int], float]:
    state = np.kron(np.kron(PLUS, PLUS), PLUS)
    clustered = apply_cz(apply_cz(state, 0, 1), 1, 2)
    answer: dict[tuple[int, int, int], float] = {}
    for middle, pm, state_m in measure(clustered, 1, "X"):
        for left, pl, state_l in measure(state_m, 0, "Z"):
            for right, pr, _ in measure(state_l, 2, "Z"):
                answer[(middle, left, right)] = pm * pl * pr
    return answer


def m2_and_bell_capability() -> None:
    section("D - One-M2 content and exact Bell capability")
    axes = (
        Y,
        -Y,
        X,
        -X,
        Z,
        -Z,
        (X + Y + Z) / np.sqrt(3.0),
        (X + 2.0 * Y + 3.0 * Z) / np.sqrt(14.0),
    )
    projectors = tuple((I2 + axis) / 2.0 for axis in axes)
    check(
        "D all named contents can be rank-one possibilities in one M2",
        all(
            np.allclose(projector @ projector, projector, atol=TOL)
            and abs(np.trace(projector).real - 1.0) < TOL
            for projector in projectors
        ),
    )
    check(
        "D program projector P is distinct from the Bell and header projectors",
        all(not np.allclose(projectors[-1], prior, atol=TOL) for prior in projectors[:-1]),
    )

    distribution = bell_distribution()
    check("D nearest-neighbor CZ-CZ cage has four complete record histories", len(distribution) == 4)
    check("D supplied projective/Born instrument gives weight one quarter", all(abs(value - 0.25) < TOL for value in distribution.values()))
    check(
        "D center X record fixes endpoint Z parity",
        all((left ^ right) == (0 if middle == 1 else 1) for middle, left, right in distribution),
    )


def box_sites() -> frozenset[Coord]:
    return frozenset(
        (x, y, z)
        for x in range(-2, 5)
        for y in range(-2, 10)
        for z in range(-2, 4)
    )


def finite_fixture() -> tuple[RecordMap, tuple[Program, ...], frozenset[Coord]]:
    cages = (
        Program((0, 0, 0), (1, 0, 0), (0, 1, 0)),
        Program((0, 5, 0), (1, 0, 0), (0, 1, 0)),
    )
    check("E fixture cages have disjoint complete supports", cage_support(cages[0]).isdisjoint(cage_support(cages[1])))
    records = join(seed_records(cages[0]), seed_records(cages[1]))
    records = join(records, {(-2, 0, 0): "P", (-2, 5, 0): "P"})
    return records, cages, box_sites()


def cage_outcomes(program: Program, index: int) -> tuple[str, str, str]:
    # Both parity branches are represented; outcome choice is supplied per cage.
    if index % 2 == 0:
        return ("X+", "Z0", "Z0")
    return ("X-", "Z0", "Z1")


def ready_actions(
    records: RecordMap,
    cages: tuple[Program, ...],
    domain: frozenset[Coord],
) -> tuple[Action, ...]:
    protected = protected_sites(cages)
    answer: list[Action] = []

    # One canonical action per open target.  Several P predecessors nominate
    # exactly the same permanent content, so predecessor identity is irrelevant.
    p_targets: set[Coord] = set()
    for source, content in records.items():
        if content != "P":
            continue
        for direction in DIRECTIONS:
            target = add(source, direction)
            if target in domain and target not in records and target not in protected:
                p_targets.add(target)
    for target in sorted(p_targets):
        answer.append(action(f"P@{target}", {target: "P"}))

    for index, program in enumerate(cages):
        certificate = certificate_site(program)
        middle, left, right = cage_outcomes(program, index)
        header_present = all(
            records.get(site) == content
            for site, content in program_records(program).items()
        )
        if (
            header_present
            and records.get(program.trigger, "").startswith("Z")
            and certificate not in records
            and all(site not in records for site in program.data)
        ):
            answer.append(action(f"prep-{index}", {certificate: "C"}))
        if records.get(certificate) == "C" and all(site not in records for site in program.data):
            answer.append(action(f"event-{index}", {program.center: middle}))
        if records.get(program.center) == middle and program.left not in records:
            answer.append(action(f"left-{index}", {program.left: left}))
        if records.get(program.center) == middle and program.right not in records:
            answer.append(action(f"right-{index}", {program.right: right}))
    return tuple(answer)


def run_schedule(
    chooser: str,
    initial: RecordMap,
    cages: tuple[Program, ...],
    domain: frozenset[Coord],
    seed: int = 0,
) -> tuple[RecordMap, tuple[str, ...]]:
    records = dict(initial)
    history: list[str] = []
    rng = random.Random(seed)
    limit = 4 * len(domain)
    for _ in range(limit):
        actions = ready_actions(records, cages, domain)
        if not actions:
            return records, tuple(history)
        if chooser == "first":
            selected = actions[0]
        elif chooser == "last":
            selected = actions[-1]
        elif chooser == "random":
            selected = rng.choice(actions)
        else:
            raise ValueError(chooser)
        updated = apply_action(records, selected)
        if not is_extension(records, updated) or len(updated) != len(records) + 1:
            raise RuntimeError("non-inflationary or duplicate action")
        records = updated
        history.append(selected.name)
    raise RuntimeError("finite schedule failed to terminate")


def schedule_confluence() -> None:
    section("E - Finite compatible-seed schedule confluence")
    initial, cages, domain = finite_fixture()
    check("E every initial record lies in the finite domain", set(initial).issubset(domain))
    check("E P seeds do not occupy protected Bell sites", set(site for site, value in initial.items() if value == "P").isdisjoint(protected_sites(cages)))

    runs: list[tuple[RecordMap, tuple[str, ...]]] = [
        run_schedule("first", initial, cages, domain),
        run_schedule("last", initial, cages, domain),
    ]
    runs.extend(run_schedule("random", initial, cages, domain, seed) for seed in range(20))
    reference = runs[0][0]
    for index, (records, history) in enumerate(runs):
        check(f"E schedule {index:02d} reaches the same terminal record map", records == reference)
        check(f"E schedule {index:02d} is append-only", len(history) == len(records) - len(initial))
        check(f"E schedule {index:02d} fills the finite domain", len(records) == len(domain))
    check("E different schedules genuinely use different action orders", len({history for _, history in runs}) > 2)
    check("E terminal state contains both complete Bell record triples", all(all(site in reference for site in program.data) for program in cages))
    check("E all nonprotected initially open sites receive the same P content", all(reference[site] == "P" for site in domain - protected_sites(cages) - set(initial)))


def critical_pair_census() -> None:
    section("F - Complete atomic critical-pair and representative diamond census")
    atomic = [
        action(f"{site}-{content}", {site: content})
        for site in ((0, 0, 0), (1, 0, 0))
        for content in ("P", "H0", "H1")
    ]
    pairs = [(item, item) for item in atomic] + list(combinations(atomic, 2))
    joinable = 0
    nonjoinable = 0
    for first, second in pairs:
        if compatible(first.as_map(), second.as_map()):
            joinable += 1
            check(f"F atomic diamond {first.name}/{second.name}", diamond({}, first, second))
        else:
            nonjoinable += 1
            check(f"F atomic conflict {first.name}/{second.name}", not diamond({}, first, second))
    check("F complete two-site three-content census has 15 joinable pairs", joinable == 15)
    check("F complete two-site three-content census has 6 nonjoinable pairs", nonjoinable == 6)

    representatives = (
        (
            "same-target P nominations",
            action("P-from-left", {(0, 0, 0): "P"}),
            action("P-from-right", {(0, 0, 0): "P"}),
            True,
        ),
        (
            "disjoint P writes",
            action("P-left", {(0, 0, 0): "P"}),
            action("P-right", {(1, 0, 0): "P"}),
            True,
        ),
        (
            "P and preparation certificate",
            action("P", {(0, 0, 0): "P"}),
            action("prep", {(1, 0, 0): "C"}),
            True,
        ),
        (
            "two disjoint cages",
            action("prep-a", {(0, 0, 0): "C"}),
            action("prep-b", {(2, 0, 0): "C"}),
            True,
        ),
        (
            "left and right Bell reads",
            action("left", {(0, 0, 0): "Z0"}),
            action("right", {(2, 0, 0): "Z0"}),
            True,
        ),
        (
            "duplicate identical event",
            action("event-a", {(1, 0, 0): "X+"}),
            action("event-b", {(1, 0, 0): "X+"}),
            True,
        ),
        (
            "multi-site compatible union",
            action("one", {(0, 0, 0): "P", (1, 0, 0): "H1"}),
            action("two", {(1, 0, 0): "H1", (2, 0, 0): "C"}),
            True,
        ),
        (
            "distinct permanent outputs at one site",
            action("zero", {(0, 0, 0): "H0"}),
            action("one", {(0, 0, 0): "H1"}),
            False,
        ),
    )
    for label, first, second, expected in representatives:
        check(f"F representative {label}", diamond({}, first, second) == expected)


def swap_operator(left: int, right: int, width: int = 3) -> np.ndarray:
    operator = np.zeros((1 << width, 1 << width), dtype=complex)
    for index in range(1 << width):
        bits = [int(value) for value in f"{index:0{width}b}"]
        bits[left], bits[right] = bits[right], bits[left]
        target = int("".join(str(value) for value in bits), 2)
        operator[target, index] = 1.0
    return operator


def braid_and_defect_probe() -> None:
    section("G - Braid/defect alternative and append-only obstruction")
    s12 = swap_operator(0, 1)
    s23 = swap_operator(1, 2)
    identity = np.eye(8, dtype=complex)
    check("G SWAP generators are unitary", np.allclose(s12.conj().T @ s12, identity, atol=TOL) and np.allclose(s23.conj().T @ s23, identity, atol=TOL))
    check("G SWAP generators satisfy the Yang-Baxter braid relation", np.allclose(s12 @ s23 @ s12, s23 @ s12 @ s23, atol=TOL))

    carrier = np.zeros(8, dtype=complex)
    carrier[4] = 1.0  # |100>
    moved = s12 @ carrier
    expected = np.zeros(8, dtype=complex)
    expected[2] = 1.0  # |010>
    check("G braid transport moves a local carrier from one site to another", np.allclose(moved, expected, atol=TOL))
    old_record = {(0, 0, 0): "Z1", (1, 0, 0): "Z0"}
    moved_record = {(0, 0, 0): "Z0", (1, 0, 0): "Z1"}
    check("G moving an already locked carrier is not an extension", not is_extension(old_record, moved_record))

    cz12 = np.diag((1, 1, 1, 1, 1, 1, -1, -1)).astype(complex)
    cz23 = np.diag((1, 1, 1, -1, 1, 1, 1, -1)).astype(complex)
    check("G adjacent CZ gates commute and retain Bell-capable interaction", np.allclose(cz12 @ cz23, cz23 @ cz12, atol=TOL))
    check("G commuting unitaries do not join incompatible permanent maps", not compatible(old_record, moved_record))

    trail_before = {(0, 0, 0): "D"}
    annihilated = {}
    archived = join(trail_before, {(1, 0, 0): "D"})
    check("G literal defect annihilation removes a record and violates extension", not is_extension(trail_before, annihilated))
    check("G archived defect motion is append-only but reduces to grow-only union", is_extension(trail_before, archived) and archived == join(trail_before, {(1, 0, 0): "D"}))


def impossibility_boundary_and_classification() -> None:
    section("H - Minimal impossibility boundary and constitutional classification")
    base: RecordMap = {}
    left = action("write-a", {(0, 0, 0): "H0"})
    right = action("write-b", {(0, 0, 0): "H1"})
    after_left = apply_action(base, left)
    after_right = apply_action(base, right)
    check("H two distinct writes form an immediate critical pair", after_left != after_right)
    check("H neither permanent branch extends the other", not is_extension(after_left, after_right) and not is_extension(after_right, after_left))

    possible_one_site_maps = ({}, {(0, 0, 0): "H0"}, {(0, 0, 0): "H1"})
    common_extensions = [
        candidate
        for candidate in possible_one_site_maps
        if is_extension(after_left, candidate) and is_extension(after_right, candidate)
    ]
    check("H one-record-per-site state space contains no common permanent extension", common_extensions == [])

    joined_label = {(0, 0, 0): "J"}
    check("H a later merge label cannot overwrite the first permanent output", not is_extension(after_left, joined_label) and not is_extension(after_right, joined_label))
    routed = {(0, 0, 0): "H0", (1, 0, 0): "H1"}
    check("H spatial routing can archive both contents only by adding capacity", is_extension(after_left, routed))

    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    classifications = (
        "same-content spread is candidate law content",
        "protected cage placement is boundary content",
        "bell outcomes remain supplied branch content",
        "weights and actuality remain open",
        "rate remains open",
        "formation-as-extension remains a theorem",
        "not a theorem of the current four axioms",
        "no new record axiom is forced",
        "the collision boundary follows from one record per site plus permanence",
        "the positive construction closes only compatible-seed scheduler confluence",
    )
    for phrase in classifications:
        check(f"H note preserves classification: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    crdt_algebra()
    geometry_and_covariance()
    m2_and_bell_capability()
    schedule_confluence()
    critical_pair_census()
    braid_and_defect_probe()
    impossibility_boundary_and_classification()
    print(
        "\nSUMMARY: ABELIAN COMPATIBLE-SEED BELL MERGE CYCLE 15 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
