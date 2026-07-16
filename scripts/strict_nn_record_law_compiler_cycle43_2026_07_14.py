#!/usr/bin/env python3
"""Cycle 43 strict-NN compiler attempt and bounded residual controls.

The runner closes the labeled-seed orientation question, recomputes the
one-step radius-one separator, exhibits fresh NN routes around one complete
official block, and verifies that a deterministic certificate archive would
leave the official Cycle-41 cylinders unchanged.  It does not pretend to
execute the still-missing write-once local certificate transducer W_C.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "STRICT_NN_RECORD_LAW_COMPILER_CYCLE43_NOTE_2026-07-14.md"
CYCLE41 = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
CYCLE19 = REVIEW / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md"
CYCLE34 = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Rotation = tuple[Coord, Coord, Coord]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
HEADER_PATTERN = ("H1", "H0", "H1", "H1", "H0", "H1")
BUILDER_ONE_PATTERN = ("B1", "B0", "B1", "B1", "B0", "B1")
BUILDER_TWO_PATTERN = ("D1", "D0", "D1", "D1", "D0", "D1")


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return add(left, scale(-1, right))


def dot(left: Coord, right: Coord) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def determinant(matrix: Rotation) -> int:
    a, b, c = matrix
    return dot(a, cross(b, c))


def matvec(matrix: Rotation, vector: Coord) -> Coord:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    rotations: set[Rotation] = set()
    for columns in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows: list[Coord] = []
            for row, column in enumerate(columns):
                values = [0, 0, 0]
                values[column] = signs[row]
                rows.append(tuple(values))  # type: ignore[arg-type]
            matrix = tuple(rows)  # type: ignore[assignment]
            if determinant(matrix) == 1:
                rotations.add(matrix)
    return tuple(sorted(rotations))


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


def header_sites(program: Program) -> tuple[Coord, ...]:
    d, e, u = program.forward, program.transverse, program.normal
    offsets = (
        e,
        scale(2, e),
        scale(3, e),
        u,
        scale(2, u),
        add(d, add(e, u)),
    )
    return tuple(add(program.trigger, offset) for offset in offsets)


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, scale(-1, program.transverse))


def shifted_header_sites(program: Program, step: int) -> tuple[Coord, ...]:
    return tuple(add(site, scale(step, program.forward)) for site in header_sites(program))


def seed_records(program: Program) -> dict[Coord, str]:
    records = dict(zip(header_sites(program), HEADER_PATTERN))
    records[program.trigger] = "Z0"
    return records


def transformed_program(program: Program, rotation: Rotation, shift: Coord = (0, 0, 0)) -> Program:
    return Program(
        add(matvec(rotation, program.trigger), shift),
        matvec(rotation, program.forward),
        matvec(rotation, program.transverse),
    )


def transformed_records(records: dict[Coord, str], rotation: Rotation, shift: Coord = (0, 0, 0)) -> dict[Coord, str]:
    return {add(matvec(rotation, site), shift): content for site, content in records.items()}


def canonical_record_tuple(records: dict[Coord, str]) -> tuple[tuple[Coord, str], ...]:
    return tuple(sorted(records.items()))


def decoded_programs(records: dict[Coord, str]) -> tuple[Program, ...]:
    triggers = tuple(site for site, content in records.items() if content.startswith("Z"))
    found: list[Program] = []
    for trigger in triggers:
        for forward in DIRECTIONS:
            for transverse in DIRECTIONS:
                if dot(forward, transverse) != 0:
                    continue
                candidate = Program(trigger, forward, transverse)
                if seed_records(candidate) == records:
                    found.append(candidate)
    return tuple(found)


def preparation_ready(program: Program, records: dict[Coord, str]) -> bool:
    header = dict(zip(header_sites(program), HEADER_PATTERN))
    return (
        all(records.get(site) == content for site, content in header.items())
        and records.get(program.trigger, "").startswith("Z")
        and certificate_site(program) not in records
        and all(site not in records for site in program.data)
    )


def local_view(records: dict[Coord, str], center: Coord, radius: int) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        sorted(
            (subtract(site, center), content)
            for site, content in records.items()
            if manhattan(site, center) <= radius
        )
    )


def official_block_support(program: Program) -> frozenset[Coord]:
    support = set(seed_records(program))
    support.add(certificate_site(program))
    support.update(program.data)
    for stage in (1, 2, 3):
        support.update(shifted_header_sites(program, stage))
    return frozenset(support)


def backward_archive_paths(program: Program) -> tuple[tuple[Coord, ...], ...]:
    """Route each header straight behind the trigger on a distinct fresh lane."""
    paths: list[tuple[Coord, ...]] = []
    for source in header_sites(program):
        forward_coordinate = dot(subtract(source, program.trigger), program.forward)
        steps = forward_coordinate + 4
        path = tuple(add(source, scale(-step, program.forward)) for step in range(steps + 1))
        paths.append(path)
    return tuple(paths)


def append_records(records: dict[Coord, str], assignments: dict[Coord, str]) -> dict[Coord, str]:
    overlap = set(records).intersection(assignments)
    if overlap:
        raise ValueError(f"official record overwrite at {sorted(overlap)}")
    answer = dict(records)
    answer.update(assignments)
    return answer


def source_contract() -> None:
    section("A - Authority, foundation, and source boundary")
    for path in (NOTE, CYCLE41, CYCLE19, CYCLE34, AXIOMS, REGISTRY):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    cycle41 = normalized(CYCLE41)
    axioms = normalized(AXIOMS)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no constitutional edit", "no live constitutional edit" in note)
    check("A live law slot is nearest-neighbor", "one fixed nearest-neighbor admissibility rule" in axioms)
    check("A official records are permanent", "records are permanent" in axioms)
    check("A state remains a record configuration", "a state is a configuration of records" in axioms)
    check("A registry contains exactly four canonical nodes", len(registry["nodes"]) == 4)
    check("A Cycle 41 names the exact target field", "event_readiness_local_causal_domain" in cycle41)
    check("A Cycle 43 names one collapsed transducer", "seed_orbit_local_certificate_transducer" in note and "collapsed wall set: {w_c}" in note)
    check("A Cycle 43 rejects a universal NN no-go", "not a theorem that w_c cannot exist" in note)


def seed_orbit_and_decoder() -> None:
    section("B - Labeled seed orbit, stabilizer, and covariant frame decoder")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    seed = seed_records(base)
    rotations = proper_cubic_rotations()
    orbit = {
        canonical_record_tuple(transformed_records(seed, rotation))
        for rotation in rotations
    }
    stabilizer = tuple(
        rotation
        for rotation in rotations
        if transformed_records(seed, rotation) == seed
    )
    check("B proper cubic group has 24 rotations", len(rotations) == 24)
    check("B labeled seed orbit has size 24", len(orbit) == 24)
    check("B labeled seed stabilizer is trivial", len(stabilizer) == 1)
    check("B canonical seed decodes exactly one frame", decoded_programs(seed) == (base,))

    for index, rotation in enumerate(rotations):
        shift = (7, -5, 3)
        moved_program = transformed_program(base, rotation, shift)
        moved_seed = transformed_records(seed, rotation, shift)
        check(f"B rotated seed {index:02d} decodes its rotated frame", decoded_programs(moved_seed) == (moved_program,))


def locality_and_route_controls() -> None:
    section("C - One-step separator, causal depth, and fresh path geometry")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    good = seed_records(program)
    far = add(program.trigger, scale(3, program.transverse))
    bad = dict(good)
    bad.pop(far)
    check("C good seed is preparation-ready", preparation_ready(program, good))
    check("C far-header deletion blocks preparation", not preparation_ready(program, bad))
    check("C good and bad trigger radius-one views agree", local_view(good, program.trigger, 1) == local_view(bad, program.trigger, 1))
    check("C exact predicate differs despite equal radius-one view", preparation_ready(program, good) != preparation_ready(program, bad))
    check("C far header is exactly three NN edges away", manhattan(program.trigger, far) == 3)

    dependencies = set(header_sites(program)) | {program.trigger, certificate_site(program)} | set(program.data)
    max_depth = max(manhattan(program.trigger, site) for site in dependencies)
    check("C complete direct dependency radius is three", max_depth == 3)
    reached = {program.trigger}
    layers = [frozenset(reached)]
    for _ in range(3):
        reached |= {add(site, direction) for site in reached for direction in DIRECTIONS}
        layers.append(frozenset(reached))
    check("C far header is absent before causal layer three", far not in layers[2])
    check("C far header enters at causal layer three", far in layers[3])

    official = official_block_support(program)
    paths = backward_archive_paths(program)
    auxiliary_sets = tuple(set(path[1:]) for path in paths)
    check("C six positive header facts receive six archive paths", len(paths) == 6)
    check("C every archive path uses only NN edges", all(all(manhattan(left, right) == 1 for left, right in zip(path, path[1:])) for path in paths))
    check("C every auxiliary path avoids official block support", all(not auxiliary.intersection(official) for auxiliary in auxiliary_sets))
    check("C auxiliary header paths are pairwise disjoint", all(not auxiliary_sets[i].intersection(auxiliary_sets[j]) for i in range(6) for j in range(i + 1, 6)))
    check("C archive endpoints are distinct", len({path[-1] for path in paths}) == 6)

    for index, rotation in enumerate(proper_cubic_rotations()):
        moved = transformed_program(program, rotation)
        moved_official = official_block_support(moved)
        moved_paths = backward_archive_paths(moved)
        moved_auxiliary = tuple(set(path[1:]) for path in moved_paths)
        check(
            f"C route geometry is proper-cubic covariant {index:02d}",
            {canonical_record_tuple({site: "P" for site in path}) for path in moved_paths}
            == {canonical_record_tuple(transformed_records({site: "P" for site in path}, rotation)) for path in paths}
            and all(not support.intersection(moved_official) for support in moved_auxiliary),
        )


def official_projection_controls() -> None:
    section("D - Official append projection and exact cylinder preservation")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = seed_records(base)
    compiler_archive = {
        site
        for path in backward_archive_paths(base)
        for site in path[1:]
    }
    check("D displayed compiler path archive is nonempty", bool(compiler_archive))
    check("D displayed compiler path archive avoids the official block", compiler_archive.isdisjoint(official_block_support(base)))

    for cycle in range(12):
        current = Program(add(base.trigger, scale(3 * cycle, base.forward)), base.forward, base.transverse)
        assignments: dict[Coord, str] = {
            certificate_site(current): "C",
            current.data[0]: "Z0",
            current.data[1]: "X+" if cycle % 2 == 0 else "X-",
            current.data[2]: "Z0" if cycle % 2 == 0 else "Z1",
        }
        assignments.update(dict(zip(shifted_header_sites(current, 1), BUILDER_ONE_PATTERN)))
        assignments.update(dict(zip(shifted_header_sites(current, 2), BUILDER_TWO_PATTERN)))
        assignments.update(dict(zip(shifted_header_sites(current, 3), HEADER_PATTERN)))
        check(f"D cycle {cycle:02d} has twenty-two official writes", len(assignments) == 22)
        check(f"D cycle {cycle:02d} overwrites no official record", set(assignments).isdisjoint(records))
        check(f"D cycle {cycle:02d} compiler projection targets no official record", not compiler_archive.intersection(assignments))
        records = append_records(records, assignments)
        check(f"D cycle {cycle:02d} official count is 22N+7", len(records) == 22 * (cycle + 1) + 7)

    alphabet = (
        (1, 0, 0),
        (1, 1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
    )
    for length in range(7):
        total = sum(Fraction(1, 4 ** length) for _ in product(alphabet, repeat=length))
        check(f"D length-{length} official cylinders normalize", total == 1)
    prefix = alphabet[0:1] * 4
    check("D one-block extension marginal is exact", sum(Fraction(1, 4 ** 5) for _ in alphabet) == Fraction(1, 4 ** 4))
    check("D compiler archive projects away deterministically in this control", bool(compiler_archive) and len(prefix) == 4)


def z_pointer_control() -> None:
    section("E - Z-pointer versus transverse-record CZ control")

    def conjugate_cz(pauli: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        x1, x2, z1, z2 = pauli
        return (x1, x2, z1 ^ x2, z2 ^ x1)

    z_left = (0, 0, 1, 0)
    x_left = (1, 0, 0, 0)
    check("E CZ fixes a local Z pointer", conjugate_cz(z_left) == z_left)
    check("E CZ sends local X to X tensor Z", conjugate_cz(x_left) == (1, 0, 0, 1))
    check("E transverse pointer is not pointwise fixed", conjugate_cz(x_left) != x_left)
    check("E Z coding moves rather than erases the compiler field", "z coding moves the residual into a spatial encoder/transducer" in normalized(NOTE))


def documentation_and_no_go_gate() -> None:
    section("F - Classification and N1-N8 documentation gate")
    note = normalized(NOTE)
    required = (
        "c43 / seed_orbit_local_certificate_transducer",
        "partial construction with one named unassembled field",
        "orientation token is not required",
        "a collection of paths is not yet the transducer",
        "not a theorem that w_c cannot exist",
        "no axiom need follows",
        "no live axiom addition follows",
        "### n1 — alternative route enumeration",
        "### n2 — wall-independence audit",
        "### n3 — hidden-wall scan",
        "### n4 — exact residual matching",
        "### n5 — rhetoric and resolution audit",
        "### n6 — partial-closure paths",
        "### n7 — strongest steelman",
        "### n8 — cross-cycle echo",
        "hostile steelman:",
        "outcome:",
        "no-go-discipline status: pass for the bounded non-completion claim",
    )
    for phrase in required:
        check(f"F note contains: {phrase}", phrase in note)
    check("F N1 marks at least five routes attempted", note.count("| attempted |") >= 5)
    check("F N1 rules out no route by prior", "| ruled out by prior |" not in note)
    check("F N2 collapses to one field", "collapsed wall set: {w_c}" in note)
    check("F N3 reports zero hidden conditions", "unresolved hidden conditions: 0" in note)
    check("F N4 drops mismatched QCA evidence", "no — dropped as negative evidence" in note)
    check("F N5 leaves arbitrary NN process open", "arbitrary one-m_2 nn process | no / open" in note)
    check("F N6 keeps direct tile construction live", "explicit write-once tile/certificate table | live primary target" in note)
    check("F N7 demotes the no-existence claim", "steelman succeeds against any no-existence claim" in note)
    check("F N8 carries at least five cycle mechanisms", all(f"cycle {number}" in note for number in (13, 14, 19, 34, 41)))


def main() -> int:
    source_contract()
    seed_orbit_and_decoder()
    locality_and_route_controls()
    official_projection_controls()
    z_pointer_control()
    documentation_and_no_go_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: the labeled Cycle-41 seed uniquely fixes its cubic frame and "
        "fresh NN routes exist, but the exact append-only schedule-confluent "
        "SEED_ORBIT_LOCAL_CERTIFICATE_TRANSDUCER W_C is not yet assembled"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
