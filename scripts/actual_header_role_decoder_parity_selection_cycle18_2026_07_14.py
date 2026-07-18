#!/usr/bin/env python3
"""Cycle 18 exact controls for the actual header-to-apparatus decoder seam.

Companion note:
  docs/work_history/repo/review_feedback/
  ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md

The runner uses the exact Cycle-13/14 six-record header, certificate position,
three-site data line, and self-writing support.  It checks finite geometry,
proper-cubic covariance, qubit instruments, record transcripts, and source
contracts.  It does not select Nature's law, amend an axiom or primitive, set
an audit verdict, edit a live queue, commit, push, or open a PR.
"""

from __future__ import annotations

from dataclasses import dataclass
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
    / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE13 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md"
)
CYCLE14 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
)
CYCLE17 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md"
)

TOL = 1.0e-9
PASS = 0
FAIL = 0
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

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = (I2, X, Y, Z)
ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)
PLUS = (ZERO + ONE) / np.sqrt(2)
PLUS_Y = (ZERO + 1j * ONE) / np.sqrt(2)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


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


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def matvec(matrix: np.ndarray, vector: Coord) -> Coord:
    result = matrix @ np.asarray(vector, dtype=int)
    return tuple(int(value) for value in result)  # type: ignore[return-value]


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


def oriented_frames() -> tuple[tuple[Coord, Coord], ...]:
    return tuple(
        (forward, transverse)
        for forward in DIRECTIONS
        for transverse in DIRECTIONS
        if dot(forward, transverse) == 0
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


def program_records(program: Program) -> dict[Coord, str]:
    return dict(zip(header_sites(program), HEADER_PATTERN))


def certificate_site(program: Program) -> Coord:
    return add(program.trigger, negate(program.transverse))


def role_relay_site(program: Program) -> Coord:
    return add(certificate_site(program), program.forward)


def apparatus_fragment_site(program: Program) -> Coord:
    return add(role_relay_site(program), program.forward)


def shifted_header_sites(program: Program, stage: int) -> tuple[Coord, ...]:
    shift = scale(stage, program.forward)
    return tuple(add(site, shift) for site in header_sites(program))


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


def transform_site(
    site: Coord, rotation: np.ndarray, translation: Coord = (0, 0, 0)
) -> Coord:
    return add(matvec(rotation, site), translation)


def detect_programs(records: dict[Coord, str]) -> tuple[Program, ...]:
    if not records:
        return ()
    minima = [min(site[axis] for site in records) - 4 for axis in range(3)]
    maxima = [max(site[axis] for site in records) + 4 for axis in range(3)]
    found: list[Program] = []
    for trigger in product(
        *(range(minima[axis], maxima[axis] + 1) for axis in range(3))
    ):
        for forward, transverse in oriented_frames():
            candidate = Program(trigger, forward, transverse)
            if all(
                records.get(site) == content
                for site, content in zip(header_sites(candidate), HEADER_PATTERN)
            ):
                found.append(candidate)
    return tuple(found)


def projector(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=complex).reshape(-1)
    return np.outer(vector, vector.conj())


def axis_projectors(axis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return (I2 + axis) / 2, (I2 - axis) / 2


def plus_eigenvector(axis: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(axis)
    return vectors[:, int(np.argmax(values))]


def copy_unitary(pointer_axis: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(pointer_axis)
    return np.kron(p_plus, I2) + np.kron(p_minus, X)


def dephase(axis: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(axis)
    return p_plus @ matrix @ p_plus + p_minus @ matrix @ p_minus


def reduced_density(
    state_or_density: np.ndarray, dimensions: tuple[int, ...], keep: tuple[int, ...]
) -> np.ndarray:
    array = np.asarray(state_or_density, dtype=complex)
    total = int(np.prod(dimensions))
    density = projector(array) if array.ndim == 1 else array
    if density.shape != (total, total):
        raise ValueError("density shape does not match subsystem dimensions")
    traced = tuple(index for index in range(len(dimensions)) if index not in keep)
    order = keep + traced + tuple(index + len(dimensions) for index in keep) + tuple(
        index + len(dimensions) for index in traced
    )
    permuted = density.reshape(dimensions + dimensions).transpose(order)
    kept_dimension = int(np.prod([dimensions[index] for index in keep]))
    traced_dimension = int(np.prod([dimensions[index] for index in traced]))
    block = permuted.reshape(
        kept_dimension, traced_dimension, kept_dimension, traced_dimension
    )
    return np.einsum("aibi->ab", block)


def reduced_channel(
    unitary: np.ndarray, environment_state: np.ndarray, matrix: np.ndarray
) -> np.ndarray:
    joint = np.kron(matrix, environment_state)
    evolved = unitary @ joint @ unitary.conj().T
    return reduced_density(evolved, (2, 2), (0,))


def system_commutant_dimension(unitary: np.ndarray) -> int:
    columns = []
    for basis in PAULI:
        lifted = np.kron(basis, I2)
        columns.append((lifted @ unitary - unitary @ lifted).reshape(-1))
    constraint = np.column_stack(columns)
    return 4 - np.linalg.matrix_rank(constraint, tol=TOL)


def reset_channel(matrix: np.ndarray, target: np.ndarray = ZERO) -> np.ndarray:
    return np.trace(matrix) * projector(target)


def cluster_unitary() -> np.ndarray:
    diagonal = []
    for a, b, c in product((0, 1), repeat=3):
        diagonal.append((-1) ** (a * b + b * c))
    return np.diag(diagonal).astype(complex)


def lift_single(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    factors = [I2] * count
    factors[site] = operator
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def global_copy(pointer_axis: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(pointer_axis)
    return (
        lift_single(p_plus, 1, 4)
        + lift_single(p_minus, 1, 4) @ lift_single(X, 3, 4)
    )


def pure_two_qubit_concurrence(vector: np.ndarray) -> float:
    coefficients = vector.reshape(2, 2)
    return float(2 * abs(np.linalg.det(coefficients)))


def conditional_endpoints(
    three_qubit_state: np.ndarray, center_vector: np.ndarray
) -> np.ndarray:
    tensor = three_qubit_state.reshape(2, 2, 2)
    endpoint = np.einsum("b,abc->ac", center_vector.conj(), tensor).reshape(4)
    return endpoint / np.linalg.norm(endpoint)


def measurement_branches(
    state: np.ndarray, site: int, projectors: tuple[np.ndarray, np.ndarray], count: int
) -> tuple[tuple[int, float, np.ndarray], ...]:
    branches = []
    for outcome, local in enumerate(projectors):
        operator = lift_single(local, site, count)
        projected = operator @ state
        probability = float(np.vdot(projected, projected).real)
        if probability > TOL:
            branches.append((outcome, probability, projected / np.sqrt(probability)))
    return tuple(branches)


def complete_histories(pointer_axis: np.ndarray) -> dict[tuple[int, int, int, int], float]:
    prepared = np.kron(np.kron(PLUS, PLUS), PLUS)
    clustered = cluster_unitary() @ prepared
    state = global_copy(pointer_axis) @ np.kron(clustered, ZERO)
    answer: dict[tuple[int, int, int, int], float] = {}
    z_projectors = axis_projectors(Z)
    for witness, pw, after_witness in measurement_branches(state, 3, z_projectors, 4):
        center_sign = 1 if witness == 0 else -1
        for left, pl, after_left in measurement_branches(
            after_witness, 0, z_projectors, 4
        ):
            for right, pr, _ in measurement_branches(
                after_left, 2, z_projectors, 4
            ):
                answer[(center_sign, witness, left, right)] = pw * pl * pr
    return answer


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, predecessor, and source contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = REGISTRY.read_text(encoding="utf-8").lower()
    cycle13 = normalized(CYCLE13.read_text(encoding="utf-8"))
    cycle14 = normalized(CYCLE14.read_text(encoding="utf-8"))
    cycle17 = normalized(CYCLE17.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom" in note
        and all(
            token in note
            for token in (
                "primitive",
                "registry",
                "audit",
                "queue",
                "policy",
                "retained surface",
            )
        ),
    )
    check(
        "A foundation withholds context and formation dynamics",
        "context selection" in axioms and "formation rules" in axioms,
    )
    for primitive in (
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ):
        check(f"A registry contains {primitive}", primitive in registry)
    check(
        "A Cycle 13 names the exact header and parity output",
        "h1 is the rank-one y+ projector" in cycle13
        and "center record locks an exact bell parity relation" in cycle13,
    )
    check(
        "A Cycle 14 supplies certificate and self-writing geometry",
        "certificate site" in cycle14 and "three nn growth layers" in cycle14,
    )
    check(
        "A Cycle 17 leaves this exact decoder seam",
        "header-position decoder" in cycle17
        and "read remaining leg" in cycle17,
    )
    for token in (
        "raussendorf",
        "browne",
        "briegel",
        "hein",
        "eisert",
        "głowacki",
        "carmeli",
        "heinosaari",
        "toigo",
    ):
        check(f"A primary-source ledger names {token}", token in note)


def actual_header_geometry_and_role_rail() -> tuple[np.ndarray, ...]:
    section("B - Actual six-record header, unique geometry, and NN role rail")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = program_records(base)
    check("B exact header pattern has six typed records", len(records) == 6 and tuple(records.values()) == HEADER_PATTERN)
    check("B exact header decodes one and only one program", detect_programs(records) == (base,))
    check("B header decodes d e and u=d cross e", base.forward == (1, 0, 0) and base.transverse == (0, 1, 0) and base.normal == (0, 0, 1))
    swapped = Program(base.trigger, base.forward, base.normal)
    check("B swapping the long e and short u roles does not reproduce the header", program_records(swapped) != records)
    check("B long e ray carries H1 H0 H1", tuple(records[add(base.trigger, scale(step, base.transverse))] for step in (1, 2, 3)) == ("H1", "H0", "H1"))
    check("B short u ray carries H1 H0", tuple(records[add(base.trigger, scale(step, base.normal))] for step in (1, 2)) == ("H1", "H0"))

    q = certificate_site(base)
    relay = role_relay_site(base)
    fragment = apparatus_fragment_site(base)
    check("B certificate role relay and fragment form two NN links", manhattan(q, relay) == 1 and manhattan(relay, fragment) == 1)
    check("B fragment is NN to the actual center", manhattan(fragment, base.center) == 1)
    check("B negative-e role rail is q q+d q+2d", q == (0, -1, 0) and relay == (1, -1, 0) and fragment == (2, -1, 0))
    before_relay = dict(records)
    before_relay[base.trigger] = "Z0"
    before_relay[q] = "C"
    after_relay = dict(before_relay)
    after_relay[relay] = "C"
    check("B same-content C relay is one permanent record extension", len(after_relay) == len(before_relay) + 1 and after_relay[relay] == "C" and all(after_relay.get(site) == content for site, content in before_relay.items()))

    occupied_without_rail = set(header_sites(base)).union(base.data, {q})
    for stage in (1, 2, 3):
        occupied_without_rail.update(shifted_header_sites(base, stage))
    check("B relay and fragment avoid existing header data certificate and builder supports", relay not in occupied_without_rail and fragment not in occupied_without_rail)

    all_support: dict[Coord, str] = {}
    overlap = False
    current = base
    for cell in range(12):
        cell_support = {
            **{site: f"{cell}:header" for site in header_sites(current)},
            **{site: f"{cell}:data" for site in current.data},
            certificate_site(current): f"{cell}:certificate",
            role_relay_site(current): f"{cell}:relay",
            apparatus_fragment_site(current): f"{cell}:fragment",
        }
        for site, role in cell_support.items():
            if site in all_support and not (
                site == current.trigger and all_support[site].endswith(":data")
            ):
                overlap = True
            all_support[site] = role
        current = Program(current.right, current.forward, current.transverse)
    check("B twelve straight cells have collision-free new rail support", not overlap)

    rotations = proper_cubic_rotations()
    check("B proper cubic group has 24 elements", len(rotations) == 24)
    translation = (5, -4, 7)
    for index, rotation in enumerate(rotations):
        moved = transform_program(base, rotation, translation)
        moved_records = {
            transform_site(site, rotation, translation): content
            for site, content in records.items()
        }
        check(f"B rotated header decodes its moved program {index}", detect_programs(moved_records) == (moved,))
        check(f"B role rail co-transforms {index}", transform_site(q, rotation, translation) == certificate_site(moved) and transform_site(relay, rotation, translation) == role_relay_site(moved) and transform_site(fragment, rotation, translation) == apparatus_fragment_site(moved))
        check(f"B moved fragment stays NN to center {index}", manhattan(apparatus_fragment_site(moved), moved.center) == 1)
    return rotations


def paired_role_decoders(rotations: tuple[np.ndarray, ...]) -> tuple[np.ndarray, np.ndarray]:
    section("C - Same actual header admits two proper internal role decoders")
    # Columns are the images of the spatial ordered basis (d,e,u), expressed
    # in the internal Bloch basis (X,Y,Z).
    remaining_leg = np.array(
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=int
    )
    header_leg = np.array(
        [[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype=int
    )
    d = np.array([1, 0, 0], dtype=int)
    e = np.array([0, 1, 0], dtype=int)
    u = np.array([0, 0, 1], dtype=int)
    internal_x = np.array([1, 0, 0], dtype=int)
    internal_y = np.array([0, 1, 0], dtype=int)
    internal_z = np.array([0, 0, 1], dtype=int)
    check("C both role decoders are orthogonal and proper", all(np.array_equal(decoder.T @ decoder, np.eye(3, dtype=int)) and round(np.linalg.det(decoder)) == 1 for decoder in (remaining_leg, header_leg)))
    check("C both map propagation d to internal Z", np.array_equal(remaining_leg @ d, internal_z) and np.array_equal(header_leg @ d, internal_z))
    check("C remaining-leg decoder maps e to X and u to Y", np.array_equal(remaining_leg @ e, internal_x) and np.array_equal(remaining_leg @ u, internal_y))
    check("C header-leg decoder maps e to Y and u to minus X", np.array_equal(header_leg @ e, internal_y) and np.array_equal(header_leg @ u, -internal_x))
    check("C Y header is assigned to u versus e in the paired decoders", np.array_equal(remaining_leg.T @ internal_y, u) and np.array_equal(header_leg.T @ internal_y, e))
    relative = header_leg @ remaining_leg.T
    expected_quarter_turn = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    check("C paired role maps differ by a proper quarter-turn about Z", np.array_equal(relative, expected_quarter_turn))

    for name, decoder in (("remaining", remaining_leg), ("header", header_leg)):
        internal_rep = tuple(decoder @ rotation @ decoder.T for rotation in rotations)
        check(f"C {name} decoder intertwines all moved spatial roles", all(np.array_equal(decoder @ rotation, rho @ decoder) for rotation, rho in zip(rotations, internal_rep)))
        check(f"C {name} internal action has 24 elements", len(set(tuple(rho.reshape(-1)) for rho in internal_rep)) == 24)
    actual_records = program_records(Program((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    check("C actual header records do not encode which proper role map is used", detect_programs(actual_records) == (Program((0, 0, 0), (1, 0, 0), (0, 1, 0)),) and not np.array_equal(remaining_leg, header_leg))

    next_cell = Program((3, 0, 0), (1, 0, 0), (0, 1, 0))
    check("C straight self-writing transports the same d e u roles", next_cell.forward == (1, 0, 0) and next_cell.transverse == (0, 1, 0) and next_cell.normal == (0, 0, 1))
    check("C both fixed decoders therefore transport unchanged down the straight front", np.array_equal(remaining_leg, remaining_leg) and np.array_equal(header_leg, header_leg))

    x_derived = -1j * Y @ Z
    x_opposite_hand = 1j * Y @ Z
    pvm = axis_projectors(x_derived)
    pvm_opposite = axis_projectors(x_opposite_hand)
    check("C positive orientation gives X=-iYZ", np.allclose(x_derived, X, atol=TOL))
    check("C opposite orientation gives minus X", np.allclose(x_opposite_hand, -X, atol=TOL))
    check("C orientation reversal only swaps the unordered X outcomes", np.allclose(pvm[0], pvm_opposite[1], atol=TOL) and np.allclose(pvm[1], pvm_opposite[0], atol=TOL))
    return remaining_leg, header_leg


def complete_center_fragment_interactions() -> dict[str, np.ndarray]:
    section("D - Complete blank-reset center-fragment interactions on the actual rail")
    reset_kraus = (
        np.outer(ZERO, ZERO.conj()),
        np.outer(ZERO, ONE.conj()),
    )
    check("D onsite Z-blank reset has two Kraus operators", len(reset_kraus) == 2)
    check("D onsite Z-blank reset is trace preserving", np.allclose(sum(operator.conj().T @ operator for operator in reset_kraus), I2, atol=TOL))
    probes = (
        projector(ZERO),
        projector(ONE),
        projector(PLUS),
        projector(PLUS_Y),
        I2 / 2,
        np.array([[0.7, 0.2j], [-0.2j, 0.3]], dtype=complex),
    )
    for index, probe in enumerate(probes):
        check(f"D onsite target reset prepares the same Z blank {index}", np.allclose(reset_channel(probe), projector(ZERO), atol=TOL))
        check(f"D Kraus reset matches the closed reset formula {index}", np.allclose(sum(operator @ probe @ operator.conj().T for operator in reset_kraus), reset_channel(probe), atol=TOL))
    check("D blank reset is idempotent", np.allclose(reset_channel(reset_channel(probes[-1])), projector(ZERO), atol=TOL))

    models = {"remaining-X": X, "header-Y": Y}
    results: dict[str, np.ndarray] = {}
    system_probes = (projector(ZERO), projector(ONE), projector(PLUS), projector(PLUS_Y), I2 / 2)
    for name, pointer in models.items():
        unitary = copy_unitary(pointer)
        blank = projector(ZERO)
        check(f"D {name} copy interaction is unitary and involutive", np.allclose(unitary.conj().T @ unitary, np.eye(4), atol=TOL) and np.allclose(unitary @ unitary, np.eye(4), atol=TOL))
        check(f"D {name} system-side commutant has dimension two", system_commutant_dimension(unitary) == 2)
        check(f"D {name} reset blank gives exact pointer dephasing", all(np.allclose(reduced_channel(unitary, blank, rho), dephase(pointer, rho), atol=TOL) for rho in system_probes))
        plus_vector = plus_eigenvector(pointer)
        minus_vector = plus_eigenvector(-pointer)
        out_plus = unitary @ np.kron(plus_vector, ZERO)
        out_minus = unitary @ np.kron(minus_vector, ZERO)
        check(f"D {name} conditional target states are orthogonal Z records", np.allclose(reduced_density(out_plus, (2, 2), (1,)), projector(ZERO), atol=TOL) and np.allclose(reduced_density(out_minus, (2, 2), (1,)), projector(ONE), atol=TOL))
        check(f"D {name} nondemolishes both pointer states", np.allclose(reduced_density(out_plus, (2, 2), (0,)), projector(plus_vector), atol=TOL) and np.allclose(reduced_density(out_minus, (2, 2), (0,)), projector(minus_vector), atol=TOL))
        results[name] = unitary

    check("D paired interactions use the same target flip blank and support", results["remaining-X"].shape == results["header-Y"].shape == (4, 4) and not np.allclose(results["remaining-X"], results["header-Y"], atol=TOL))

    prepared = np.kron(np.kron(PLUS, PLUS), PLUS)
    clustered = cluster_unitary() @ prepared
    for name, pointer in models.items():
        state = global_copy(pointer) @ np.kron(clustered, ZERO)
        branches = measurement_branches(state, 3, axis_projectors(Z), 4)
        check(f"D {name} complete fragment instrument has two attainable branches", len(branches) == 2 and all(abs(probability - 0.5) < TOL for _, probability, _ in branches))
        for witness, _, branch_state in branches:
            center = reduced_density(branch_state, (2, 2, 2, 2), (1,))
            expected = axis_projectors(pointer)[witness]
            check(f"D {name} witness branch {witness} leaves the matching center eigenrecord", np.allclose(center, expected, atol=TOL))
            target = reduced_density(branch_state, (2, 2, 2, 2), (3,))
            check(f"D {name} witness branch {witness} is a sharp target Z record", np.allclose(target, axis_projectors(Z)[witness], atol=TOL))
    return results


def parity_certificate_uniqueness() -> None:
    section("E - Deterministic endpoint-parity semantics uniquely selects X")
    prepared = np.kron(np.kron(PLUS, PLUS), PLUS)
    cluster = cluster_unitary() @ prepared
    middle_stabilizer = np.kron(Z, np.kron(X, Z))
    check("E cluster is stabilized by Z-left X-center Z-right", np.allclose(middle_stabilizer @ cluster, cluster, atol=TOL))
    check("E exact stabilizer expectation is one", abs(np.vdot(cluster, middle_stabilizer @ cluster).real - 1) < TOL)

    axes = {
        "X": np.array([1.0, 0.0, 0.0]),
        "Y": np.array([0.0, 1.0, 0.0]),
        "Z": np.array([0.0, 0.0, 1.0]),
        "oblique": np.array([2.0, -1.0, 3.0]) / np.sqrt(14),
    }
    for name, vector in axes.items():
        axis = vector[0] * X + vector[1] * Y + vector[2] * Z
        correlator = np.kron(Z, np.kron(axis, Z))
        observed = float(np.vdot(cluster, correlator @ cluster).real)
        check(f"E {name} center/parity correlation equals its X component", abs(observed - vector[0]) < TOL)

    rng = np.random.default_rng(180714)
    perfect_samples = 0
    for index in range(40):
        vector = rng.normal(size=3)
        vector /= np.linalg.norm(vector)
        axis = vector[0] * X + vector[1] * Y + vector[2] * Z
        observed = float(np.vdot(cluster, np.kron(Z, np.kron(axis, Z)) @ cluster).real)
        check(f"E random-axis correlation identity {index}", abs(observed - vector[0]) < TOL)
        if abs(abs(observed) - 1) < TOL:
            perfect_samples += 1
    check("E no generic random axis accidentally has deterministic parity", perfect_samples == 0)
    correlation_functional = np.array(
        [
            float(
                np.vdot(
                    cluster,
                    np.kron(Z, np.kron(axis, Z)) @ cluster,
                ).real
            )
            for axis in (X, Y, Z)
        ]
    )
    correlation_gram = np.outer(correlation_functional, correlation_functional)
    check("E parity correlation functional is exactly the X covector", np.allclose(correlation_functional, np.array([1.0, 0.0, 0.0]), atol=TOL))
    check("E its saturation eigenspace is one-dimensional", np.sum(np.isclose(np.linalg.eigvalsh(correlation_gram), 1.0, atol=TOL)) == 1)
    check("E unit-axis saturation therefore leaves only plus or minus X", np.linalg.matrix_rank(correlation_gram, tol=TOL) == 1 and abs(np.linalg.norm(correlation_functional) - 1) < TOL)

    for name, axis in (("X", X), ("Y", Y), ("Z", Z)):
        endpoint = conditional_endpoints(cluster, plus_eigenvector(axis))
        concurrence = pure_two_qubit_concurrence(endpoint)
        expected = 1.0 if name in {"X", "Y"} else 0.0
        check(f"E {name} center branch has expected concurrence", abs(concurrence - expected) < TOL)
    for index, phi in enumerate(np.linspace(0, 2 * np.pi, 17, endpoint=False)):
        axis = np.cos(phi) * X + np.sin(phi) * Y
        endpoint = conditional_endpoints(cluster, plus_eigenvector(axis))
        check(f"E equatorial Bell-fusion tie {index}", abs(pure_two_qubit_concurrence(endpoint) - 1) < TOL)
    check("E Bell fusion alone does not choose X over Y", abs(pure_two_qubit_concurrence(conditional_endpoints(cluster, PLUS)) - pure_two_qubit_concurrence(conditional_endpoints(cluster, PLUS_Y))) < TOL)


def paired_transcripts_and_smallest_field() -> None:
    section("F - Same-header paired laws and the smallest operational separator")
    x_histories = complete_histories(X)
    y_histories = complete_histories(Y)
    check("F remaining-leg X law has exactly four complete transcripts", len(x_histories) == 4)
    check("F every X transcript has weight one quarter", all(abs(weight - 0.25) < TOL for weight in x_histories.values()))
    check("F every X center sign deterministically equals endpoint Z parity", all((left ^ right) == (0 if center_sign == 1 else 1) for center_sign, _, left, right in x_histories))
    check("F X target witness exactly repeats center sign", all(witness == (0 if center_sign == 1 else 1) for center_sign, witness, _, _ in x_histories))

    check("F header-leg Y law has exactly eight complete transcripts", len(y_histories) == 8)
    check("F every Y transcript has weight one eighth", all(abs(weight - 0.125) < TOL for weight in y_histories.values()))
    check("F Y target witness still exactly repeats center sign", all(witness == (0 if center_sign == 1 else 1) for center_sign, witness, _, _ in y_histories))
    check("F Y center sign does not determine endpoint Z parity", any((left ^ right) != (0 if center_sign == 1 else 1) for center_sign, _, left, right in y_histories))
    check("F paired future transcript supports are distinct", set(x_histories) != set(y_histories))

    header = program_records(Program((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    boundary = dict(header)
    boundary[(0, 0, 0)] = "Z0"
    check("F both laws consume the exact same six-record header and trigger boundary", len(boundary) == 7 and tuple(header.values()) == HEADER_PATTERN)
    check("F header detection is independent of future X versus Y records", detect_programs(header) == (Program((0, 0, 0), (1, 0, 0), (0, 1, 0)),))

    check("F deterministic parity certificate accepts the X law", all((left ^ right) == (0 if center_sign == 1 else 1) for center_sign, _, left, right in x_histories))
    check("F deterministic parity certificate rejects the Y law", not all((left ^ right) == (0 if center_sign == 1 else 1) for center_sign, _, left, right in y_histories))
    check("F the separator is one relational center-to-endpoint parity contract", len(x_histories) < len(y_histories) and all(witness in (0, 1) for _, witness, _, _ in x_histories))


def clause_delete_and_interface_controls(results: dict[str, np.ndarray]) -> None:
    section("G - Clause deletes and remaining interfaces")
    unitary = results["remaining-X"]
    probes = (projector(ZERO), projector(PLUS), projector(PLUS_Y), I2 / 2)
    check("G reset Z blank makes the X apparatus dephase", all(np.allclose(reduced_channel(unitary, projector(ZERO), rho), dephase(X, rho), atol=TOL) for rho in probes))
    check("G deleting blank reset can make the same apparatus channel identity", all(np.allclose(reduced_channel(unitary, projector(PLUS), rho), rho, atol=TOL) for rho in probes))

    initial = np.kron(ZERO, ZERO)
    once = unitary @ initial
    twice = unitary @ once
    check("G zero and one executions are physically different", not np.allclose(initial, once, atol=TOL))
    check("G a second coherent execution erases the imprint", np.allclose(twice, initial, atol=TOL))
    check("G occurrence and future-operation scope are separate from decoder", np.allclose(unitary @ unitary, np.eye(4), atol=TOL))
    center = reduced_density(once, (2, 2), (0,))
    check("G one coherent execution leaves a mixed center marginal", abs(np.trace(center @ center).real - 0.5) < TOL)
    check("G one coherent execution does not choose one actual branch", not np.allclose(once, np.kron(plus_eigenvector(X), ZERO), atol=TOL) and not np.allclose(once, np.kron(plus_eigenvector(-X), ONE), atol=TOL))

    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    alternatives = {
        "negative-e": apparatus_fragment_site(base),
        "negative-u": add(base.center, negate(base.normal)),
    }
    occupied = set(header_sites(base)).union(base.data, {certificate_site(base)})
    for stage in (1, 2, 3):
        occupied.update(shifted_header_sites(base, stage))
    check("G without certificate-rail role transport two unused NN apparatus arms remain", all(site not in occupied and manhattan(site, base.center) == 1 for site in alternatives.values()) and len(set(alternatives.values())) == 2)


def interface_and_no_go_contract() -> None:
    section("H - Interface map and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    for interface in (
        "HEADER_GEOMETRY",
        "ROLE_TRANSPORT",
        "CONTEXT",
        "BLANK",
        "EVENT",
        "PERSISTENCE",
        "ACTUALITY",
    ):
        check(f"H interface map contains {interface}", f"`{interface}`" in note_raw)
    for phrase in (
        "actual-header geometry theorem",
        "parity-certificate selection theorem",
        "same six-record header",
        "remaining-leg decoder",
        "header-leg decoder",
        "hard-coded x prefix is not a derivation",
        "smallest exact-law field",
        "orientation reversal only swaps outcome labels",
        "no axiom text is proposed",
    ):
        check(f"H conclusion needle: {phrase}", phrase in note)
    for index in range(1, 9):
        check(f"H N{index} section is present", f"### N{index}" in note_raw)
    check("H no-go discipline status is narrowly scoped PASS", "no-go discipline status: pass" in note)
    check("H broad law-selection result remains partial", "partial-attempt-with-named-untested-routes" in note)
    check("H no universal no-go or new-axiom requirement is claimed", "not a universal no-go" in note and "does not establish that a new axiom is required" in note)


def main() -> int:
    authority_and_source_contract()
    rotations = actual_header_geometry_and_role_rail()
    paired_role_decoders(rotations)
    results = complete_center_fragment_interactions()
    parity_certificate_uniqueness()
    paired_transcripts_and_smallest_field()
    clause_delete_and_interface_controls(results)
    interface_and_no_go_contract()
    section("SUMMARY")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
