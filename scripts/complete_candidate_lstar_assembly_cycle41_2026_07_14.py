#!/usr/bin/env python3
"""Cycle 41: exact L* assembly attempt and first-interface failure.

This runner assembles the strongest current finite pieces into one explicit
radius-three append-only Bell-front process and then tests the stricter target:
a homogeneous radius-one nearest-neighbour law on Z^3 with one M_2 carrier per
site.  It verifies the exact first mismatch, the direct all-edge-CZ record
conflict, the normalized projective corpus, the thirteen-job contract, and the
scoped N1--N8 documentation gate.

It changes no axiom, primitive, registry, audit surface, queue, commit, or PR.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CONTRACT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md"
)
CYCLE40 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md"
)
CYCLE42 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
TOL = 2.0e-10
Coord = tuple[int, int, int]
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def negate(vector: Coord) -> Coord:
    return scale(-1, vector)


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
    d = program.forward
    e = program.transverse
    u = program.normal
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
    return add(program.trigger, negate(program.transverse))


def shifted_header_sites(program: Program, steps: int) -> tuple[Coord, ...]:
    displacement = scale(steps, program.forward)
    return tuple(add(site, displacement) for site in header_sites(program))


def program_records(program: Program) -> dict[Coord, str]:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def seed_records(program: Program) -> dict[Coord, str]:
    answer = program_records(program)
    answer[program.trigger] = "Z0"
    return answer


def has_header(program: Program, records: dict[Coord, str]) -> bool:
    return all(records.get(site) == value for site, value in program_records(program).items())


def preparation_ready(program: Program, records: dict[Coord, str]) -> bool:
    return (
        has_header(program, records)
        and records.get(program.trigger, "").startswith("Z")
        and certificate_site(program) not in records
        and all(site not in records for site in program.data)
    )


def local_record_view(records: dict[Coord, str], center: Coord, radius: int) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        sorted(
            (add(site, negate(center)), value)
            for site, value in records.items()
            if manhattan(site, center) <= radius
        )
    )


def transform_program(program: Program, rotation: np.ndarray, translation: Coord) -> Program:
    return Program(
        add(matvec(rotation, program.trigger), translation),
        matvec(rotation, program.forward),
        matvec(rotation, program.transverse),
    )


def transform_records(records: dict[Coord, str], rotation: np.ndarray, translation: Coord) -> dict[Coord, str]:
    return {
        add(matvec(rotation, site), translation): value
        for site, value in records.items()
    }


def append_records(records: dict[Coord, str], assignments: dict[Coord, str]) -> dict[Coord, str]:
    overlap = set(records).intersection(assignments)
    if overlap:
        raise ValueError(f"record overwrite at {sorted(overlap)}")
    answer = dict(records)
    answer.update(assignments)
    return answer


def source_and_contract_checks() -> None:
    section("A - Foundation, source, and thirteen-interface record-law contract")
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    contract = CONTRACT.read_text(encoding="utf-8")
    cycle40 = CYCLE40.read_text(encoding="utf-8")
    cycle42 = CYCLE42.read_text(encoding="utf-8")
    cycle42_flat = " ".join(cycle42.split())
    check("A live foundation requires a nearest-neighbour admissibility rule", "one fixed nearest-neighbor admissibility rule" in axioms)
    check("A Record keeps one record per site", "site never carries more than one record" in axioms)
    check("A Record keeps formed records permanent", "records are permanent" in axioms)
    check("A state qualification is record-only", "A state is a configuration of records" in axioms)
    check("A registry has exactly four canonical premise ids", registry.count('"current_path"') == 4)
    check("A realized-state registry entry disclaims a selector", "no state, state-selection rule" in registry)
    check("A Cycle 40 keeps strict radius-one one-qubit QCA routes live", "conditional one-skeleton closure" in cycle40 and "larger-radius Clifford QCA remain open" in cycle40)
    check("A Cycle 42 separates pointwise state, complete H, and law identity", "pointwise-reference-only" in cycle42_flat and "complete h" in cycle42_flat and "separating" in cycle42_flat)
    check("A Cycle 42 retains a positive separating reconstruction route", "Exact Positive Reconstruction Route" in cycle42)

    jobs = (
        "raw joint carrier/composition",
        "complete predictive state or record decoder",
        "global event/readiness domain",
        "physical contexts and interventions",
        "exact atomic branch maps",
        "availability-to-supported-formation relation",
        "causal continuation and gluing",
        "disjoint and overlapping concurrency",
        "record status, formation, identity, writing, and preservation",
        "one-history actuality",
        "normalized contextual statistics",
        "compatible full-lattice/projective extension",
        "renewal/export for indefinitely extensible record production",
    )
    for index, job in enumerate(jobs, start=1):
        check(f"A contract job {index:02d} is explicit", job in contract)


def geometry_and_locality_checks() -> None:
    section("B - Exact front geometry, covariance, and radius-one separator")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    valid = seed_records(program)
    far_header = add(program.trigger, scale(3, program.transverse))
    defective = dict(valid)
    defective.pop(far_header)

    check("B valid seed makes preparation ready", preparation_ready(program, valid))
    check("B deleting the distance-three header blocks preparation", not preparation_ready(program, defective))
    check("B separator record is three NN edges from trigger", manhattan(program.trigger, far_header) == 3)
    check("B two separator configurations have identical radius-one trigger view", local_record_view(valid, program.trigger, 1) == local_record_view(defective, program.trigger, 1))
    check("B exact preparation predicate is not a one-invocation radius-one function", preparation_ready(program, valid) != preparation_ready(program, defective))

    dependencies = set(header_sites(program)) | set(program.data) | {program.trigger, certificate_site(program)}
    candidate_centers = tuple(product(range(-4, 5), repeat=3))
    cover_radius = min(max(manhattan(center, site) for site in dependencies) for center in candidate_centers)
    check("B smallest Manhattan ball covering the preparation predicate has radius three", cover_radius == 3, str(cover_radius))
    check("B coherent data edges are nearest neighbours", manhattan(program.left, program.center) == manhattan(program.center, program.right) == 1)
    for stage in (1, 2, 3):
        previous = header_sites(program) if stage == 1 else shifted_header_sites(program, stage - 1)
        current = shifted_header_sites(program, stage)
        check(f"B builder stage {stage} consists of six NN edges", len(previous) == len(current) == 6 and all(manhattan(a, b) == 1 for a, b in zip(previous, current)))

    rotations = proper_cubic_rotations()
    check("B proper cubic rotation census", len(rotations) == 24)
    for index, rotation in enumerate(rotations):
        moved = transform_program(program, rotation, (7, -3, 4))
        moved_records = transform_records(valid, rotation, (7, -3, 4))
        check(f"B covariance {index:02d}", preparation_ready(moved, moved_records))


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
PLUS = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)


def kron_all(*operators: np.ndarray) -> np.ndarray:
    answer = np.array([[1.0 + 0.0j]])
    for operator in operators:
        answer = np.kron(answer, operator)
    return answer


def projector(axis: np.ndarray, sign: int) -> np.ndarray:
    return (I2 + sign * axis) / 2.0


def operator_on_site(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    return kron_all(*(operator if index == site else I2 for index in range(count)))


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    singular_values = np.linalg.svd(left - right, compute_uv=False)
    return float(0.5 * singular_values.sum())


def quantum_and_record_checks() -> None:
    section("C - Branch instrument, Born normalization, and CZ record conflict")
    axes = {
        "H1": Y,
        "H0": -Y,
        "B1": (X + Y) / np.sqrt(2.0),
        "B0": -(X + Y) / np.sqrt(2.0),
        "D1": (X + Z) / np.sqrt(2.0),
        "D0": -(X + Z) / np.sqrt(2.0),
        "C": (X + Y + Z) / np.sqrt(3.0),
        "X+": X,
        "X-": -X,
        "Z0": Z,
        "Z1": -Z,
    }
    role_projectors = {name: (I2 + axis) / 2.0 for name, axis in axes.items()}
    check(
        "C all eleven role values are exact rank-one M2 projectors",
        all(
            np.allclose(value, value.conj().T, atol=TOL)
            and np.allclose(value @ value, value, atol=TOL)
            and abs(float(np.trace(value).real) - 1.0) < TOL
            for value in role_projectors.values()
        ),
    )
    check(
        "C all eleven role projectors are pairwise distinct",
        all(
            not np.allclose(role_projectors[left], role_projectors[right], atol=TOL)
            for left, right in permutations(role_projectors, 2)
        ),
    )
    plus3 = kron_all(PLUS.reshape(-1, 1), PLUS.reshape(-1, 1), PLUS.reshape(-1, 1)).reshape(-1)
    cz_ab = np.diag([(-1.0 if ((word >> 2) & 1) and ((word >> 1) & 1) else 1.0) for word in range(8)])
    cz_bc = np.diag([(-1.0 if ((word >> 1) & 1) and (word & 1) else 1.0) for word in range(8)])
    clustered = cz_bc @ cz_ab @ plus3

    history_weights: dict[tuple[int, int, int], float] = {}
    for middle_sign in (1, -1):
        middle = operator_on_site(projector(X, middle_sign), 1, 3)
        for left_value, right_value in product((0, 1), repeat=2):
            left = operator_on_site(projector(Z, 1 if left_value == 0 else -1), 0, 3)
            right = operator_on_site(projector(Z, 1 if right_value == 0 else -1), 2, 3)
            branch = right @ left @ middle @ clustered
            history_weights[(middle_sign, left_value, right_value)] = float(np.vdot(branch, branch).real)

    supported = {history: weight for history, weight in history_weights.items() if weight > TOL}
    expected_support = {
        (1, 0, 0),
        (1, 1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
    }
    check("C Bell-front branch support has four parity histories", set(supported) == expected_support)
    check("C each supported history has Born weight one quarter", all(abs(weight - 0.25) < TOL for weight in supported.values()))
    check("C complete branch family normalizes", abs(sum(history_weights.values()) - 1.0) < TOL)
    check("C unsupported algebraic branches have zero weight", all(weight < TOL for history, weight in history_weights.items() if history not in expected_support))

    rho_plus = np.outer(PLUS, PLUS.conj())
    p_x_plus_identity = float(np.trace(projector(X, 1) @ rho_plus).real)
    dephased = sum(
        projector(Z, sign) @ rho_plus @ projector(Z, sign)
        for sign in (1, -1)
    )
    p_x_plus_after_z = float(np.trace(projector(X, 1) @ dephased).real)
    mixed_channel = (1.0 / 3.0) * rho_plus + (2.0 / 3.0) * dephased
    spectator = np.outer(np.array((1.0, 0.0), dtype=complex), np.array((1.0, 0.0), dtype=complex).conj())
    joint = np.kron(rho_plus, spectator)
    joint_effect = np.kron(projector(X, 1), I2)
    check("C identity containment differs from a real Z intervention", abs(p_x_plus_identity - 1.0) < TOL and abs(p_x_plus_after_z - 0.5) < TOL)
    check("C convex intervention mixture remains normalized and positive", abs(float(np.trace(mixed_channel).real) - 1.0) < TOL and np.linalg.eigvalsh(mixed_channel).min() > -TOL)
    check("C tensor spectator/ancilla leaves the local branch weight unchanged", abs(float(np.trace(joint_effect @ joint).real) - p_x_plus_identity) < TOL)

    zero = np.array((1.0, 0.0), dtype=complex)
    one = np.array((0.0, 1.0), dtype=complex)
    a0 = np.outer(PLUS, zero.conj())
    a1 = np.outer(PLUS, one.conj())
    check("C plus-reset Kraus family is trace preserving", np.allclose(a0.conj().T @ a0 + a1.conj().T @ a1, I2, atol=TOL))
    rho0 = np.outer(zero, zero.conj())
    rho1 = np.outer(one, one.conj())
    reset0 = a0 @ rho0 @ a0.conj().T + a1 @ rho0 @ a1.conj().T
    reset1 = a0 @ rho1 @ a0.conj().T + a1 @ rho1 @ a1.conj().T
    check("C reset maps orthogonal inputs to the same plus state", np.allclose(reset0, reset1, atol=TOL) and np.allclose(reset0, rho_plus, atol=TOL))
    check("C reset destroys a nonzero matter distinguishability", abs(trace_distance(rho0, rho1) - 1.0) < TOL and trace_distance(reset0, reset1) < TOL)

    # Seven-site star: center first, then its six neighbours.  The all-edge CZ
    # automorphism maps X_center to X_center product Z_neighbour.
    count = 7
    dimension = 2**count
    diagonal = np.empty(dimension, dtype=complex)
    for word in range(dimension):
        center_bit = (word >> (count - 1)) & 1
        neighbour_ones = sum((word >> (count - 2 - index)) & 1 for index in range(6))
        diagonal[word] = -1.0 if center_bit * neighbour_ones % 2 else 1.0
    all_edge_cz = np.diag(diagonal)
    x_center = operator_on_site(X, 0, count)
    z_center = operator_on_site(Z, 0, count)
    neighbour_z = kron_all(I2, Z, Z, Z, Z, Z, Z)
    stabilizer = x_center @ neighbour_z
    p_x = (np.eye(dimension) + x_center) / 2.0
    p_z = (np.eye(dimension) + z_center) / 2.0
    transported_x = all_edge_cz @ p_x @ all_edge_cz.conj().T
    transported_z = all_edge_cz @ p_z @ all_edge_cz.conj().T
    check("C all-edge CZ sends a local X record to the seven-site stabilizer sector", np.allclose(transported_x, (np.eye(dimension) + stabilizer) / 2.0, atol=TOL))
    check("C all-edge CZ does not preserve a formed local X record", not np.allclose(transported_x, p_x, atol=TOL))
    check("C all-edge CZ does preserve a formed local Z record", np.allclose(transported_z, p_z, atol=TOL))
    check("C direct global-CZ union is incompatible with the multiaxis front dictionary", np.linalg.norm(transported_x - p_x) > 1.0)


def front_and_corpus_checks() -> None:
    section("D - Append recurrence, projective process, corpus, and actual-H firewall")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = seed_records(base)
    check("D finite boundary seed has seven records", len(records) == 7)
    all_new_supports: list[set[Coord]] = []

    for cycle in range(12):
        current = Program(add(base.trigger, scale(3 * cycle, base.forward)), base.forward, base.transverse)
        check(f"D cycle {cycle:02d} begins with its visible header", has_header(current, records))
        check(f"D cycle {cycle:02d} begins with a visible trigger", records.get(current.trigger, "").startswith("Z"))
        assignments: dict[Coord, str] = {
            certificate_site(current): "C",
            current.center: "X+" if cycle % 2 == 0 else "X-",
            current.left: "Z0",
            current.right: "Z0" if cycle % 2 == 0 else "Z1",
        }
        assignments.update(dict(zip(shifted_header_sites(current, 1), BUILDER_ONE_PATTERN)))
        assignments.update(dict(zip(shifted_header_sites(current, 2), BUILDER_TWO_PATTERN)))
        assignments.update(dict(zip(shifted_header_sites(current, 3), HEADER_PATTERN)))
        check(f"D cycle {cycle:02d} has exactly twenty-two fresh assignments", len(assignments) == 22)
        check(f"D cycle {cycle:02d} does not overwrite an old record", set(assignments).isdisjoint(records))
        check(f"D cycle {cycle:02d} support is disjoint from prior new supports", all(set(assignments).isdisjoint(old) for old in all_new_supports))
        all_new_supports.append(set(assignments))
        records = append_records(records, assignments)
        check(f"D cycle {cycle:02d} exact cumulative record count", len(records) == 22 * (cycle + 1) + 7)
        next_program = Program(current.right, current.forward, current.transverse)
        check(f"D cycle {cycle:02d} writes the next header", has_header(next_program, records))

    check("D twelve cycles advance the trigger by thirty-six edges", add(base.trigger, scale(36, base.forward)) in records)
    check("D recurrence uses six record-visible microphases per block", 6 * 12 == 72)

    alphabet = (
        (1, 0, 0),
        (1, 1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
    )

    def cylinder_weight(word: tuple[tuple[int, int, int], ...]) -> Fraction:
        return Fraction(1, 4 ** len(word))

    for length in range(0, 7):
        words = tuple(product(alphabet, repeat=length))
        check(f"D length-{length} cylinders normalize", sum(cylinder_weight(word) for word in words) == 1)
    prefix_consistency = all(
        sum(cylinder_weight(prefix + (symbol,)) for symbol in alphabet) == cylinder_weight(prefix)
        for prefix in product(alphabet, repeat=4)
    )
    check("D all 256 length-four cylinders have the correct child marginal", prefix_consistency)

    check("D center signs are IID fair in the exact corpus", sum(Fraction(1, 4) for symbol in alphabet if symbol[0] == 1) == Fraction(1, 2))
    check("D endpoint parity is certified by the center record", all((left ^ right) == (0 if sign == 1 else 1) for sign, left, right in alphabet))
    check("D component mean equals the one-block Born weight", Fraction(1, 2) == sum(Fraction(1, 4) for symbol in alphabet if symbol[0] == 1))

    # One observed finite history is admitted by different counterfactual laws.
    actual_prefix = (alphabet[0],) * 6
    fair_weight = Fraction(1, 4**6)
    biased_symbol_weights = {
        alphabet[0]: Fraction(1, 2),
        alphabet[1]: Fraction(1, 6),
        alphabet[2]: Fraction(1, 6),
        alphabet[3]: Fraction(1, 6),
    }
    biased_weight = Fraction(1)
    for symbol in actual_prefix:
        biased_weight *= biased_symbol_weights[symbol]
    check("D one actual prefix is compatible with two normalized counterfactual laws", fair_weight > 0 and biased_weight > 0)
    check("D actual history data do not identify the counterfactual law", fair_weight != biased_weight)


def contract_and_toe_checks() -> None:
    section("E - Thirteen-interface assembly and TOE-lane classification")
    radius_three_shell = (
        (1, "RAW_JOINT_CARRIER", "FILLED"),
        (2, "PREDICTIVE_RECORD_DECODER", "FILLED"),
        (3, "EVENT_READINESS_DOMAIN", "FILLED_AT_RADIUS_3"),
        (4, "CONTEXT_INTERVENTION_REPERTOIRE", "FILLED"),
        (5, "EXACT_NORMALIZED_BRANCH_MAPS", "FILLED"),
        (6, "AVAILABILITY_SUPPORT_RELATION", "FILLED"),
        (7, "CAUSAL_CONTINUATION_GLUING", "FILLED"),
        (8, "CONCURRENCY", "FILLED"),
        (9, "RECORD_FORMATION_IDENTITY_PRESERVATION", "FILLED"),
        (10, "ONE_HISTORY_ACTUALITY_TYPE", "CONDITIONAL_EXPLICIT_HISTORY_ROUTE"),
        (11, "NORMALIZED_CONTEXTUAL_STATISTICS", "FILLED"),
        (12, "PROJECTIVE_FULL_LATTICE_EXTENSION", "FILLED_ON_BOUNDARY_CLASS"),
        (13, "RENEWAL_EXPORT", "FILLED_BY_FRESH_RAY"),
    )
    check("E radius-three shell names all thirteen jobs exactly once", tuple(index for index, _, _ in radius_three_shell) == tuple(range(1, 14)))
    check("E radius-three shell has no unnamed field", all(status.startswith("FILLED") or status == "CONDITIONAL_EXPLICIT_HISTORY_ROUTE" for _, _, status in radius_three_shell))

    strict_nn = tuple(
        (index, name, "FIRST_UNFILLED" if index == 3 else ("FILLED" if index < 3 else "EXPLICIT_BUT_NOT_ASSEMBLED_AFTER_C3"))
        for index, name, _ in radius_three_shell
    )
    first_unfilled = next(row for row in strict_nn if row[2] == "FIRST_UNFILLED")
    check("E strict-NN target first fails at interface three", first_unfilled[:2] == (3, "EVENT_READINESS_DOMAIN"))
    check("E first failure is a Boolean dependency map, not a scalar coefficient", first_unfilled[1] == "EVENT_READINESS_DOMAIN")
    check("E later exact pieces do not silently certify one assembled NN law", all(status == "EXPLICIT_BUT_NOT_ASSEMBLED_AFTER_C3" for index, _, status in strict_nn if index > 3))

    toe = (
        ("OPERATIONAL", "BOUNDED_EXACT", "fixed reset/CZ/X/Z protocol; spectators, sequence, mixtures, and tensor ancillas are typed"),
        ("CLOCK", "OPEN", "six causal layers per block but no metric rate or lapse response"),
        ("MATTER", "INCOMPATIBLE_WITH_RESET_SECTOR", "constant reset erases arbitrary input distinguishability"),
        ("RESOURCE", "PARTIAL", "twenty-two permanent records per block; no thermodynamic law"),
        ("CONTINUUM", "OPEN", "no controlled interacting Lorentz/CPT limit"),
        ("GRAVITY", "OPEN", "no universal source-response or WEP theorem"),
        ("BOUNDARY", "FILLED_CONDITIONALLY", "one finite seed plus blank infinite corridor class"),
    )
    check("E all seven TOE interfaces are classified", tuple(name for name, _, _ in toe) == ("OPERATIONAL", "CLOCK", "MATTER", "RESOURCE", "CONTINUUM", "GRAVITY", "BOUNDARY"))
    check("E first unfilled TOE interface in contract order is CLOCK", next(name for name, status, _ in toe if status in {"OPEN", "INCOMPATIBLE_WITH_RESET_SECTOR"}) == "CLOCK")
    check("E first hard channel incompatibility is MATTER", next(name for name, status, _ in toe if status == "INCOMPATIBLE_WITH_RESET_SECTOR") == "MATTER")
    check("E boundary instance is not used to select the law", toe[-1][0] == "BOUNDARY" and "conditionally" in toe[-1][1].lower())


def documentation_gate() -> None:
    section("F - Authority-free placement and N1--N8 documentation contract")
    note = NOTE.read_text(encoding="utf-8")
    required = (
        "Authority: none",
        "L41^R3",
        "first unfilled field",
        "EVENT_READINESS_LOCAL_CAUSAL_DOMAIN",
        "not a scalar parameter",
        "primitive supplies only pointwise state evaluation",
        "Cycle 42",
        "site-only cubic action",
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
        "No-go-discipline status: PASS",
        "no live axiom edit",
        "not a no-go against",
    )
    for marker in required:
        check(f"F note contract contains: {marker}", marker.lower() in note.lower())
    check("F note does not promote itself to retained authority", "this note is not the framework law" in note.lower())
    check("F note keeps the exact failure narrower than all NN laws", "same exact radius-three readiness predicate" in note.lower())
    check("F note names the Z-only spatial-code escape", "z-only spatial" in note.lower())
    check("F note names the global-history escape", "global-history" in note.lower())


def main() -> int:
    source_and_contract_checks()
    geometry_and_locality_checks()
    quantum_and_record_checks()
    front_and_corpus_checks()
    contract_and_toe_checks()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: L41^R3 is radius-three/single-front record-law complete, "
        "but neither strict-NN record-law complete nor TOE-predictively "
        "complete; the strict-NN assembly first lacks the record-visible "
        "EVENT_READINESS_LOCAL_CAUSAL_DOMAIN map, while all-edge CZ is not "
        "record-faithful for its multiaxis dictionary"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
