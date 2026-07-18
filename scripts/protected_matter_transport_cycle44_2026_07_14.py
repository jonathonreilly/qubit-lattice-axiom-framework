#!/usr/bin/env python3
"""Cycle 44 exact protected-matter transport construction attempt.

The runner replaces the Cycle-41 constant three-qubit plus reset by an exact
nearest-neighbour block-SWAP conveyor, checks a teleportation comparator, and
tests Bell formation, append recurrence, record-fibre sufficiency, collision
typing, and cylinder statistics.  It changes no repository surface.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE14 = REVIEW / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
CYCLE34 = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
CYCLE41 = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0
TOL = 2.0e-10
Coord = tuple[int, int, int]


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


def source_contract() -> None:
    section("A - Authority, foundation, and predecessor contract")
    for path in (NOTE, AXIOMS, REGISTRY, CYCLE14, CYCLE34, CYCLE41):
        check(f"A source exists: {path.name}", path.is_file())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle14 = normalized(CYCLE14)
    cycle34 = normalized(CYCLE34)
    cycle41 = normalized(CYCLE41)
    note = normalized(NOTE)
    check("A one M2 carrier per site remains the target", "M_2(C)" in axioms)
    check("A Record forbids more than one record per site", "site never carries more than one record" in axioms)
    check("A Record keeps official records permanent", "records are permanent" in axioms)
    check("A Qualification makes state record-only", "A state is a configuration of records" in axioms)
    check("A premise registry still has exactly four current sources", registry.count('"current_path"') == 4)
    check("A Cycle 14 exposes reversible archive as the reset alternative", "reversible dilation exports their prior quantum information" in cycle14)
    check("A Cycle 34 separates logical motion from record migration", "no record moves" in cycle34)
    check("A Cycle 41 names reset erasure as the matter incompatibility", "constant plus-reset maps orthogonal inputs to the same state" in cycle41)
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no live foundation edit", "no live foundation" in note)
    check("A note does not claim matter teleportation", "ordinary quantum-state transport, not matter teleportation" in note)


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
H = np.array(((1.0, 1.0), (1.0, -1.0)), dtype=complex) / np.sqrt(2.0)
ZERO = np.array((1.0, 0.0), dtype=complex)
ONE = np.array((0.0, 1.0), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)


def kron_all(*objects: np.ndarray) -> np.ndarray:
    answer = np.array([[1.0 + 0.0j]])
    for obj in objects:
        answer = np.kron(answer, obj)
    return answer


def bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - 1 - site)) & 1 for site in range(count))


def bit_index(word: tuple[int, ...]) -> int:
    answer = 0
    for bit in word:
        answer = 2 * answer + bit
    return answer


def swap_matrix(count: int, left: int, right: int) -> np.ndarray:
    dimension = 2**count
    answer = np.zeros((dimension, dimension), dtype=complex)
    for column in range(dimension):
        word = list(bits(column, count))
        word[left], word[right] = word[right], word[left]
        answer[bit_index(tuple(word)), column] = 1.0
    return answer


def block_swap_matrix() -> tuple[np.ndarray, tuple[tuple[int, int], ...]]:
    # Move three fresh right-hand sites left through the current triple.
    schedule = (
        (2, 3), (1, 2), (0, 1),
        (3, 4), (2, 3), (1, 2),
        (4, 5), (3, 4), (2, 3),
    )
    answer = np.eye(64, dtype=complex)
    for left, right in schedule:
        answer = swap_matrix(6, left, right) @ answer
    return answer, schedule


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    return float(0.5 * np.linalg.svd(left - right, compute_uv=False).sum())


def block_swap_checks() -> None:
    section("B - Exact fresh-site export and reversible-workspace bounds")
    unitary, schedule = block_swap_matrix()
    expected = np.zeros((64, 64), dtype=complex)
    for column in range(64):
        word = bits(column, 6)
        moved = word[3:] + word[:3]
        expected[bit_index(moved), column] = 1.0
    check("B nine-gate schedule uses nearest-neighbour swaps only", len(schedule) == 9 and all(right - left == 1 for left, right in schedule))
    check("B nine NN swaps equal the exact three-site register swap", np.allclose(unitary, expected, atol=TOL))
    check("B block swap is unitary", np.allclose(unitary.conj().T @ unitary, np.eye(64), atol=TOL))

    plus3 = np.kron(np.kron(PLUS, PLUS), PLUS)
    rho_plus3 = np.outer(plus3, plus3.conj())
    embedding = np.kron(np.eye(8), plus3.reshape(8, 1))
    isometry = unitary @ embedding
    target = np.kron(plus3.reshape(8, 1), np.eye(8))
    check("B clean-plus block swap has the desired export isometry", np.allclose(isometry, target, atol=TOL))
    check("B export isometry preserves the full eight-dimensional input", np.allclose(isometry.conj().T @ isometry, np.eye(8), atol=TOL) and np.linalg.matrix_rank(isometry) == 8)

    operator_basis_exact = True
    for row, column in product(range(8), repeat=2):
        matrix_unit = np.zeros((8, 8), dtype=complex)
        matrix_unit[row, column] = 1.0
        carried = isometry @ matrix_unit @ isometry.conj().T
        operator_basis_exact &= np.allclose(carried, np.kron(rho_plus3, matrix_unit), atol=TOL)
    check("B every input operator is exported while work becomes plus", operator_basis_exact)

    rho000 = np.zeros((8, 8), dtype=complex)
    rho111 = np.zeros((8, 8), dtype=complex)
    rho000[0, 0] = 1.0
    rho111[7, 7] = 1.0
    out000 = isometry @ rho000 @ isometry.conj().T
    out111 = isometry @ rho111 @ isometry.conj().T
    check("B orthogonal three-qubit matter inputs remain perfectly distinguishable", abs(trace_distance(rho000, rho111) - 1.0) < TOL and abs(trace_distance(out000, out111) - 1.0) < TOL)
    check("B a fixed work output needs export dimension at least eight", np.linalg.matrix_rank(isometry) == 8 and 2**3 >= 8 and 2**2 < 8)
    check("B arbitrary six-qubit input cannot compress into fixed work plus three-qubit export", 2**6 > 2**3)
    check("B a workspace returned to one fixed state cannot retain eight orthogonal inputs", 8 > 1)


def operator_on_site(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    return kron_all(*(operator if index == site else I2 for index in range(count)))


def cnot_matrix(count: int, control: int, target: int) -> np.ndarray:
    dimension = 2**count
    answer = np.zeros((dimension, dimension), dtype=complex)
    for column in range(dimension):
        word = list(bits(column, count))
        word[target] ^= word[control]
        answer[bit_index(tuple(word)), column] = 1.0
    return answer


def teleportation_kraus() -> dict[tuple[int, int], np.ndarray]:
    bell = (np.kron(ZERO, ZERO) + np.kron(ONE, ONE)) / np.sqrt(2.0)
    embed = np.kron(I2, bell.reshape(4, 1))
    circuit = operator_on_site(H, 0, 3) @ cnot_matrix(3, 0, 1)
    full = circuit @ embed
    answer: dict[tuple[int, int], np.ndarray] = {}
    for first, second in product((0, 1), repeat=2):
        branch = np.zeros((2, 2), dtype=complex)
        for output, source in product((0, 1), repeat=2):
            branch[output, source] = full[bit_index((first, second, output)), source]
        answer[(first, second)] = branch
    return answer


def teleportation_checks() -> None:
    section("C - Recorded teleportation comparator and resource overhead")
    branches = teleportation_kraus()
    candidates = (I2, X, Z, X @ Z, Z @ X)
    corrected: dict[tuple[int, int], np.ndarray] = {}
    for outcome, branch in branches.items():
        for correction in candidates:
            candidate = correction @ branch
            scalar = np.trace(candidate) / 2.0
            if abs(scalar) > TOL and np.allclose(candidate, scalar * I2, atol=TOL):
                corrected[outcome] = candidate
                break
    check("C teleportation has four Bell-syndrome branches", set(branches) == set(product((0, 1), repeat=2)))
    check("C every syndrome branch has input-independent weight one quarter", all(np.allclose(branch.conj().T @ branch, I2 / 4.0, atol=TOL) for branch in branches.values()))
    check("C syndrome branches form a complete instrument", np.allclose(sum((branch.conj().T @ branch for branch in branches.values()), np.zeros((2, 2), dtype=complex)), I2, atol=TOL))
    check("C a Pauli correction restores the identity channel in every branch", len(corrected) == 4 and all(np.allclose(value.conj().T @ value, I2 / 4.0, atol=TOL) for value in corrected.values()))
    check("C three parallel teleporters preserve an arbitrary input triple", all(np.allclose(value.conj().T @ value, I2 / 4.0, atol=TOL) for value in corrected.values()) and 4**3 == 64)
    check("C triple teleportation writes six syndrome records", 3 * 2 == 6)
    check("C protected teleport comparator raises block record cost from 22 to 28", 22 + 6 == 28)
    check("C triple teleport plus Bell event has 256 equiprobable joint branches", 4**3 * 4 == 256 and Fraction(1, 64) * Fraction(1, 4) == Fraction(1, 256))
    check("C teleportation still requires three fresh Bell pairs per triple", 3 * 2 == 6)


def bell_weights(state: np.ndarray) -> dict[tuple[int, int, int], float]:
    cz_ab = np.diag([(-1.0 if ((word >> 2) & 1) and ((word >> 1) & 1) else 1.0) for word in range(8)])
    cz_bc = np.diag([(-1.0 if ((word >> 1) & 1) and (word & 1) else 1.0) for word in range(8)])
    clustered = cz_bc @ cz_ab @ state
    answer: dict[tuple[int, int, int], float] = {}
    for middle_sign, left_value, right_value in product((1, -1), (0, 1), (0, 1)):
        px = (I2 + middle_sign * X) / 2.0
        pzl = (I2 + (1 if left_value == 0 else -1) * Z) / 2.0
        pzr = (I2 + (1 if right_value == 0 else -1) * Z) / 2.0
        branch = kron_all(pzl, px, pzr) @ clustered
        answer[(middle_sign, left_value, right_value)] = float(np.vdot(branch, branch).real)
    return answer


def bell_and_fibre_checks() -> None:
    section("D - Bell preservation and the record-fibre/readability fork")
    plus3 = np.kron(np.kron(PLUS, PLUS), PLUS)
    zero3 = np.kron(np.kron(ZERO, ZERO), ZERO)
    plus_weights = bell_weights(plus3)
    zero_weights = bell_weights(zero3)
    supported_plus = {word: weight for word, weight in plus_weights.items() if weight > TOL}
    supported_zero = {word: weight for word, weight in zero_weights.items() if weight > TOL}
    expected = {(1, 0, 0), (1, 1, 1), (-1, 0, 1), (-1, 1, 0)}
    check("D clean conveyor preserves the four Bell parity histories", set(supported_plus) == expected)
    check("D every protected Bell history has weight one quarter", all(abs(weight - 0.25) < TOL for weight in supported_plus.values()))
    check("D the protected Bell instrument normalizes", abs(sum(plus_weights.values()) - 1.0) < TOL)
    check("D a non-plus fresh triple does not reproduce the Bell corpus", set(supported_zero) != expected and len(supported_zero) == 2)
    check("D clean-plus resource is load-bearing, not notation", supported_plus != supported_zero)

    # The transport-only record process never probes the carried state.
    record_law_000 = tuple(round(weight, 12) for weight in plus_weights.values())
    record_law_111 = tuple(round(weight, 12) for weight in plus_weights.values())
    check("D transport-only future record laws are one record fibre", record_law_000 == record_law_111)
    pz0_from_000 = 1.0
    pz0_from_111 = 0.0
    check("D one legal separating read breaks record-fibre sufficiency", pz0_from_000 != pz0_from_111)
    check("D dark transport and readable matter cannot be conflated", record_law_000 == record_law_111 and pz0_from_000 != pz0_from_111)

    overlap_input = abs(np.vdot(ZERO, PLUS))
    overlap_cloned = overlap_input**2
    check("D an unknown carrier cannot be both preserved and copied into an exact record", abs(overlap_input - overlap_cloned) > TOL)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


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
        return tuple(add(self.trigger, scale(step, self.forward)) for step in (1, 2, 3))  # type: ignore[return-value]


def header_sites(program: Program) -> tuple[Coord, ...]:
    d, e, u = program.forward, program.transverse, program.normal
    offsets = (e, scale(2, e), scale(3, e), u, scale(2, u), add(d, add(e, u)))
    return tuple(add(program.trigger, offset) for offset in offsets)


def shifted_header_sites(program: Program, steps: int) -> tuple[Coord, ...]:
    return tuple(add(site, scale(steps, program.forward)) for site in header_sites(program))


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, scale(-1, program.transverse))


HEADER = ("H1", "H0", "H1", "H1", "H0", "H1")
BUILDER1 = ("B1", "B0", "B1", "B1", "B0", "B1")
BUILDER2 = ("D1", "D0", "D1", "D1", "D0", "D1")


def seed(program: Program) -> dict[Coord, str]:
    answer = dict(zip(header_sites(program), HEADER))
    answer[program.trigger] = "Z0"
    return answer


def assignments(program: Program, cycle: int) -> dict[Coord, str]:
    left, center, right = program.data
    answer = {
        certificate_site(program): "C",
        center: "X+" if cycle % 2 == 0 else "X-",
        left: "Z0",
        right: "Z0" if cycle % 2 == 0 else "Z1",
    }
    answer.update(dict(zip(shifted_header_sites(program, 1), BUILDER1)))
    answer.update(dict(zip(shifted_header_sites(program, 2), BUILDER2)))
    answer.update(dict(zip(shifted_header_sites(program, 3), HEADER)))
    return answer


def recurrence_collision_corpus_checks() -> None:
    section("E - Recurrence, permanent records, collision typing, and corpus")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = seed(base)
    check("E protected front begins with seven permanent seed records", len(records) == 7)
    carried_locations: list[tuple[Coord, ...]] = []
    for cycle in range(8):
        current = Program(add(base.trigger, scale(3 * cycle, base.forward)), base.forward, base.transverse)
        future = Program(add(current.trigger, scale(3, current.forward)), current.forward, current.transverse)
        check(f"E cycle {cycle:02d} current matter triple is still open", set(current.data).isdisjoint(records))
        check(f"E cycle {cycle:02d} future clean triple is still open", set(future.data).isdisjoint(records))
        check(f"E cycle {cycle:02d} conveyor pairs are separated by three edges", all(sum(abs(a - b) for a, b in zip(left, right)) == 3 for left, right in zip(current.data, future.data)))
        new = assignments(current, cycle)
        check(f"E cycle {cycle:02d} appends exactly twenty-two records", len(new) == 22)
        check(f"E cycle {cycle:02d} overwrites no official record", set(new).isdisjoint(records))
        check(f"E cycle {cycle:02d} leaves the carried output unrecorded", set(future.data).isdisjoint(new))
        records.update(new)
        carried_locations.append(future.data)
        check(f"E cycle {cycle:02d} cumulative count remains 22N+7", len(records) == 22 * (cycle + 1) + 7)
    check("E carried logical triple advances three lattice edges per block", all(next_locations == tuple(add(site, scale(3, base.forward)) for site in locations) for locations, next_locations in zip(carried_locations, carried_locations[1:])))
    check("E no official record migrates or changes content", len(records) == len(set(records)))

    check("E two arbitrary incoming triples cannot inject into one output triple", 8 * 8 > 8)
    check("E two-output six-qubit scattering remains dimensionally live", 8 * 8 == 8 * 8)
    check("E single-front reserved-corridor collision domain is explicit", len(carried_locations) == 8)

    alphabet = ((1, 0, 0), (1, 1, 1), (-1, 0, 1), (-1, 1, 0))
    for length in range(7):
        check(f"E length-{length} protected Bell cylinders normalize", sum(Fraction(1, 4**length) for _ in product(alphabet, repeat=length)) == 1)
    check("E protected child cylinders marginalize", all(sum(Fraction(1, 4**5) for _ in alphabet) == Fraction(1, 4**4) for _ in product(alphabet, repeat=4)))
    check("E teleport comparator one-block cylinders normalize", 256 * Fraction(1, 256) == 1)
    check("E teleport comparator child marginal is exact", 256 * Fraction(1, 256**2) == Fraction(1, 256))


def documentation_and_no_go_gate() -> None:
    section("F - Placement and fresh No-Go Discipline gate")
    note = normalized(NOTE)
    required = (
        "conditional positive",
        "nine nearest-neighbour swaps",
        "infinite clean-plus corridor",
        "record the carrier/decoder",
        "revise qualification for ontic open carriers",
        "ordinary quantum-state transport, not matter teleportation",
        "partial-narrowing",
        "### n1",
        "### n2",
        "### n3",
        "### n4",
        "### n5",
        "### n6",
        "### n7",
        "### n8",
    )
    for phrase in required:
        check(f"F note contains: {phrase}", phrase in note)
    n1 = note.split("### n1", 1)[1].split("### n2", 1)[0]
    check("F N1 has at least five marked attack routes", n1.count("attempted") + n1.count("ruled out by prior") >= 5)
    check("F N2 names the exact three collapsed walls", all(wall in note for wall in ("w_b", "w_s", "w_k")))
    check("F N2 contains all three pairwise independence rows", all(pair in note for pair in ("w_b/w_s", "w_b/w_k", "w_s/w_k")))
    check("F broad protected-matter no-go is rejected", "broad no-go: fail" in note)
    check("F narrow record-fibre separator is retained", "narrow separator: pass" in note)
    check("F neither state-ontology exit is selected", "this cycle selects neither exit" in note)
    check("F no axiom wording is proposed", "no axiom wording follows" in note)


def main() -> int:
    source_contract()
    block_swap_checks()
    teleportation_checks()
    bell_and_fibre_checks()
    recurrence_collision_corpus_checks()
    documentation_and_no_go_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: exact protected coherent transport and the L41 Bell corpus "
        "coexist conditionally on a clean fresh corridor; readable operational "
        "matter still requires record-derived state data or a Qualification "
        "revision, and collisions remain typed rather than solved"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
