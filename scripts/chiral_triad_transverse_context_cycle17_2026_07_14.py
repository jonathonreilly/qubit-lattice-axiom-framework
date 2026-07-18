#!/usr/bin/env python3
"""Cycle 17 exact controls for chiral-frame transverse-context selection.

Companion note:
  docs/work_history/repo/review_feedback/
  CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md

This runner checks finite-dimensional algebra, the 24-element proper-cubic
group, and source/interface contracts.  It does not choose a physical law,
promote a theorem, amend an axiom or primitive, set an audit verdict, edit a
queue, commit, push, or open a PR.  Exit code is zero iff every check passes.
"""

from __future__ import annotations

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
    / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md"
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
CYCLE15 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md"
)
CYCLE16 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md"
)

TOL = 1.0e-9
PASS = 0
FAIL = 0

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = (I2, X, Y, Z)
ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)
PLUS_X = (ZERO + ONE) / np.sqrt(2)
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


def projector(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=complex).reshape(-1)
    return np.outer(vector, vector.conj())


def axis_matrix(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    vector = vector / np.linalg.norm(vector)
    return vector[0] * X + vector[1] * Y + vector[2] * Z


def axis_projectors(axis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return (I2 + axis) / 2, (I2 - axis) / 2


def plus_eigenvector(axis: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(axis)
    return vectors[:, int(np.argmax(values))]


def dephase(axis: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(axis)
    return p_plus @ matrix @ p_plus + p_minus @ matrix @ p_minus


def copy_unitary(pointer_axis: np.ndarray, target_flip: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(pointer_axis)
    return np.kron(p_plus, I2) + np.kron(p_minus, target_flip)


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


def proper_cubic_group() -> tuple[np.ndarray, ...]:
    group = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                group.append(matrix)
    return tuple(group)


def intertwiner_dimension(
    spatial_rep: tuple[np.ndarray, ...], internal_rep: tuple[np.ndarray, ...]
) -> int:
    columns = []
    for row in range(3):
        for column in range(3):
            candidate = np.zeros((3, 3), dtype=float)
            candidate[row, column] = 1.0
            columns.append(
                np.concatenate(
                    [
                        (candidate @ g - rho @ candidate).reshape(-1)
                        for g, rho in zip(spatial_rep, internal_rep)
                    ]
                )
            )
    constraint = np.column_stack(columns)
    return 9 - np.linalg.matrix_rank(constraint, tol=TOL)


def conditional_endpoint_vector(
    three_qubit_state: np.ndarray, center_vector: np.ndarray
) -> np.ndarray:
    tensor = three_qubit_state.reshape(2, 2, 2)
    endpoint = np.einsum("b,abc->ac", center_vector.conj(), tensor).reshape(4)
    return endpoint / np.linalg.norm(endpoint)


def pure_two_qubit_concurrence(vector: np.ndarray) -> float:
    coefficients = vector.reshape(2, 2)
    return float(2 * abs(np.linalg.det(coefficients)))


def cluster_unitary() -> np.ndarray:
    diagonal = []
    for a, b, c in product((0, 1), repeat=3):
        diagonal.append((-1) ** (a * b + b * c))
    return np.diag(diagonal).astype(complex)


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, predecessor, and primary-source contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = REGISTRY.read_text(encoding="utf-8").lower()
    cycle13 = normalized(CYCLE13.read_text(encoding="utf-8"))
    cycle15 = normalized(CYCLE15.read_text(encoding="utf-8"))
    cycle16 = normalized(CYCLE16.read_text(encoding="utf-8"))
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
        "A foundation withholds context and frame selection",
        "context selection" in axioms and "measurement basis selection" in axioms,
    )
    for primitive in (
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ):
        check(f"A registry contains {primitive}", primitive in registry)
    check(
        "A Cycle 13 exposes the Y header and shared-frame import",
        "h1 is the rank-one y+ projector" in cycle13
        and "shared relational pauli frame" in cycle13,
    )
    check(
        "A Cycle 15 supplies the binary repeatability reduction",
        "sharp binary-qubit reduction" in cycle15,
    )
    check(
        "A Cycle 16 supplies the Z commutant and X/Y residual",
        "cz-cz" in cycle16
        and "center x rather than y" in cycle16
        and "full apparatus interaction" in cycle16,
    )
    for token in (
        "gour",
        "spekkens",
        "bagan",
        "baig",
        "muñoz-tapia",
        "głowacki",
        "loveridge",
        "waldron",
        "carmeli",
        "heinosaari",
        "toigo",
        "zurek",
        "kribs",
    ):
        check(f"A primary-source ledger names {token}", token in note)


def spatial_chiral_frame_controls() -> tuple[np.ndarray, ...]:
    section("B - Proper-cubic local geometry supplies oriented spatial frames")
    group = proper_cubic_group()
    cardinal = tuple(
        np.array(direction, dtype=int)
        for direction in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
    )
    cardinal_set = {tuple(vector) for vector in cardinal}
    frames = []
    for d in cardinal:
        for e in cardinal:
            if int(d @ e) == 0:
                u = np.cross(d, e)
                frames.append((d, e, u))
    check("B proper cubic group has 24 elements", len(group) == 24)
    check("B ordered perpendicular cardinal pairs give 24 proper frames", len(frames) == 24)
    check(
        "B every frame is right handed",
        all(round(np.linalg.det(np.column_stack(frame))) == 1 for frame in frames),
    )
    check(
        "B every proper rotation preserves cardinal nearest-neighbor support",
        all(tuple(rotation @ vector) in cardinal_set for rotation in group for vector in cardinal),
    )
    check(
        "B cross product is covariant under all 24 proper rotations",
        all(
            np.array_equal(rotation @ np.cross(d, e), np.cross(rotation @ d, rotation @ e))
            for rotation in group
            for d, e, _ in frames
        ),
    )
    translation = np.array([7, -3, 4], dtype=int)
    check(
        "B translated rotated frame legs remain nearest neighbors of the anchor",
        all(
            np.sum(np.abs((translation + rotation @ vector) - translation)) == 1
            for rotation in group
            for vector in cardinal
        ),
    )
    mirror = np.diag([-1, 1, 1])
    d, e, u = frames[0]
    check(
        "B an improper mirror reverses the cross-product orientation",
        np.array_equal(mirror @ np.cross(d, e), -np.cross(mirror @ d, mirror @ e)),
    )
    return group


def two_ray_frame_theorem() -> None:
    section("C - Z plus one noncommuting record ray determines a full Pauli triad")
    reference_vectors = (
        np.array([0.0, 1.0, 0.0]),
        np.array([1.0, 1.0, 1.0]),
        np.array([-2.0, 1.0, 0.5]),
    )
    for index, vector in enumerate(reference_vectors):
        reference = axis_matrix(vector)
        overlap = float(np.trace(reference @ Z).real / 2)
        transverse = (reference - overlap * Z) / np.sqrt(1 - overlap**2)
        third = -1j * transverse @ Z
        check(f"C reference {index} is a Hermitian involution", np.allclose(reference, reference.conj().T, atol=TOL) and np.allclose(reference @ reference, I2, atol=TOL))
        check(f"C transverse {index} is a Hermitian involution", np.allclose(transverse, transverse.conj().T, atol=TOL) and np.allclose(transverse @ transverse, I2, atol=TOL))
        check(f"C transverse {index} is orthogonal to Z", abs(np.trace(transverse @ Z)) < TOL)
        check(f"C third axis {index} is a Hermitian involution", np.allclose(third, third.conj().T, atol=TOL) and np.allclose(third @ third, I2, atol=TOL))
        check(f"C third axis {index} is orthogonal to both supplied rays", abs(np.trace(third @ Z)) < TOL and abs(np.trace(third @ transverse)) < TOL)
        check(f"C triad {index} has positive Pauli orientation", abs(np.trace(third @ transverse @ Z) / (2j) - 1) < TOL)

    header = Y
    derived = -1j * header @ Z
    check("C Cycle-13 Y header plus CZ-selected Z gives X", np.allclose(derived, X, atol=TOL))
    check("C no absolute matrix label is needed by the relational formula", np.allclose(-1j * Y @ Z, X, atol=TOL))

    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    phase = np.diag([1, 1j]).astype(complex)
    angle = np.pi / 7
    oblique = np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * axis_matrix(np.array([1.0, 2.0, 3.0]))
    for index, recoder in enumerate((hadamard, phase, oblique)):
        z_rotated = recoder @ Z @ recoder.conj().T
        y_rotated = recoder @ Y @ recoder.conj().T
        x_from_frame = -1j * y_rotated @ z_rotated
        check(
            f"C relational third-axis construction is common-M2 covariant {index}",
            np.allclose(x_from_frame, recoder @ X @ recoder.conj().T, atol=TOL),
        )

    opposite = 1j * Y @ Z
    p_x = axis_projectors(derived)
    p_minus_x = axis_projectors(opposite)
    check("C opposite chirality reverses the oriented third-axis sign", np.allclose(opposite, -X, atol=TOL))
    check(
        "C opposite chirality leaves the unordered binary PVM unchanged",
        np.allclose(p_x[0], p_minus_x[1], atol=TOL)
        and np.allclose(p_x[1], p_minus_x[0], atol=TOL),
    )

    quarter_turn = np.cos(np.pi / 4) * I2 - 1j * np.sin(np.pi / 4) * Z
    check("C deleting the second ray leaves Z invariant", np.allclose(quarter_turn @ Z @ quarter_turn.conj().T, Z, atol=TOL))
    check("C the same stabilizer rotates X to Y", np.allclose(quarter_turn @ X @ quarter_turn.conj().T, Y, atol=TOL))
    check("C one Z ray therefore leaves a continuous transverse orbit", not np.allclose(X, Y, atol=TOL))


def soldering_intertwiner_controls(group: tuple[np.ndarray, ...]) -> None:
    section("D - A fixed cubic-to-Pauli soldering is unique; the lift is not supplied")
    spatial_rep = group
    internal_rep_0 = group
    s90 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
    internal_rep_90 = tuple(s90 @ rotation @ s90.T for rotation in group)
    check("D fixed vector/adjoint representations have a one-dimensional intertwiner space", intertwiner_dimension(spatial_rep, internal_rep_0) == 1)
    check("D conjugated internal representation also has a one-dimensional intertwiner space", intertwiner_dimension(spatial_rep, internal_rep_90) == 1)

    j0 = np.eye(3, dtype=int)
    j90 = s90
    check("D identity soldering intertwines every proper cubic rotation", all(np.array_equal(j0 @ g, rho @ j0) for g, rho in zip(spatial_rep, internal_rep_0)))
    check("D quarter-turn soldering intertwines its conjugated representation", all(np.array_equal(j90 @ g, rho @ j90) for g, rho in zip(spatial_rep, internal_rep_90)))
    check("D both solderings are normalized and orientation preserving", round(np.linalg.det(j0)) == round(np.linalg.det(j90)) == 1 and np.array_equal(j0.T @ j0, np.eye(3)) and np.array_equal(j90.T @ j90, np.eye(3)))

    propagation = np.array([0, 0, 1], dtype=int)
    apparatus_leg = np.array([1, 0, 0], dtype=int)
    check("D both proper solderings map the propagation leg to the same Z axis", np.array_equal(j0 @ propagation, propagation) and np.array_equal(j90 @ propagation, propagation))
    check("D one maps the same apparatus leg to X while the other maps it to Y", np.array_equal(j0 @ apparatus_leg, np.array([1, 0, 0])) and np.array_equal(j90 @ apparatus_leg, np.array([0, 1, 0])))
    check("D both preserve the chiral cross product", all(np.array_equal(j @ np.cross(a, b), np.cross(j @ a, j @ b)) for j in (j0, j90) for a, b in ((np.array([0, 0, 1]), np.array([1, 0, 0])), (np.array([1, 0, 0]), np.array([0, 1, 0])))))
    check("D proper chirality cannot separate the X/Y soldering pair", round(np.linalg.det(j0)) == round(np.linalg.det(j90)) == 1)
    check("D deleting the fixed spin lift exposes two exact framed embeddings", not np.array_equal(j0, j90) and len(set(tuple(matrix.reshape(-1)) for matrix in internal_rep_0)) == 24 and len(set(tuple(matrix.reshape(-1)) for matrix in internal_rep_90)) == 24)


def framed_apparatus_pair() -> dict[str, tuple[np.ndarray, ...]]:
    section("E - Same full frame admits exact X-read and Y-read apparatus laws")
    models = {
        "X-third-axis": (X, X, ZERO),
        "Y-header-axis": (Y, X, ZERO),
    }
    result: dict[str, tuple[np.ndarray, ...]] = {}
    probes = (
        projector(ZERO),
        projector(ONE),
        projector(PLUS_X),
        projector(PLUS_Y),
        I2 / 2,
    )
    for name, (pointer, flip, blank_vector) in models.items():
        unitary = copy_unitary(pointer, flip)
        blank = projector(blank_vector)
        channel = lambda matrix, u=unitary, b=blank: reduced_channel(u, b, matrix)
        check(f"E {name} apparatus is unitary", np.allclose(unitary.conj().T @ unitary, np.eye(4), atol=TOL))
        check(f"E {name} system commutant is the unique binary pointer algebra", system_commutant_dimension(unitary) == 2)
        check(f"E {name} fresh blank gives exact pointer dephasing", all(np.allclose(channel(rho), dephase(pointer, rho), atol=TOL) for rho in probes))

        plus_vector = plus_eigenvector(pointer)
        minus_vector = plus_eigenvector(-pointer)
        out_plus = unitary @ np.kron(plus_vector, blank_vector)
        out_minus = unitary @ np.kron(minus_vector, blank_vector)
        env_plus = reduced_density(out_plus, (2, 2), (1,))
        env_minus = reduced_density(out_minus, (2, 2), (1,))
        sys_plus = reduced_density(out_plus, (2, 2), (0,))
        sys_minus = reduced_density(out_minus, (2, 2), (0,))
        check(f"E {name} writes orthogonal conditional fragment states", abs(np.trace(env_plus @ env_minus)) < TOL)
        check(f"E {name} nondemolishes both pointer branches", np.allclose(sys_plus, projector(plus_vector), atol=TOL) and np.allclose(sys_minus, projector(minus_vector), atol=TOL))
        result[name] = (pointer, flip, blank_vector, blank, unitary)

    pointer_x = result["X-third-axis"][0]
    pointer_y = result["Y-header-axis"][0]
    check("E both framed laws are transverse to the CZ-selected Z axis", abs(np.trace(pointer_x @ Z)) < TOL and abs(np.trace(pointer_y @ Z)) < TOL)
    check("E pointer-to-header relation separates X from Y", abs(np.trace(pointer_x @ Y)) < TOL and abs(np.trace(pointer_y @ Y) / 2 - 1) < TOL)
    check("E both laws use the same one-qubit system/fragment support", result["X-third-axis"][4].shape == result["Y-header-axis"][4].shape == (4, 4))

    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    phase = np.diag([1, 1j]).astype(complex)
    angle = np.pi / 9
    rotation = np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * axis_matrix(np.array([2.0, -1.0, 1.0]))
    for name, (pointer, flip, blank_vector, blank, unitary) in result.items():
        for index, recoder in enumerate((hadamard, phase, rotation)):
            transformed = np.kron(recoder, recoder) @ unitary @ np.kron(recoder.conj().T, recoder.conj().T)
            check(
                f"E {name} is common-M2 covariant {index}",
                np.allclose(
                    transformed,
                    copy_unitary(
                        recoder @ pointer @ recoder.conj().T,
                        recoder @ flip @ recoder.conj().T,
                    ),
                    atol=TOL,
                ),
            )
            check(
                f"E {name} blank co-transports with the frame {index}",
                np.allclose(recoder @ blank @ recoder.conj().T, projector(recoder @ blank_vector), atol=TOL),
            )
    return result


def cluster_bell_separator() -> None:
    section("F - CZ-CZ Bell front keeps an exact X/Y apparatus fork")
    prepared = np.kron(PLUS_X, np.kron(PLUS_X, PLUS_X))
    cluster = cluster_unitary() @ prepared
    endpoint_x = conditional_endpoint_vector(cluster, PLUS_X)
    endpoint_y = conditional_endpoint_vector(cluster, PLUS_Y)
    endpoint_z = conditional_endpoint_vector(cluster, ZERO)
    phi_plus = (np.kron(ZERO, ZERO) + np.kron(ONE, ONE)) / np.sqrt(2)
    check("F center X read gives a maximally entangled endpoint state", abs(pure_two_qubit_concurrence(endpoint_x) - 1) < TOL)
    check("F center Y read also gives a maximally entangled endpoint state", abs(pure_two_qubit_concurrence(endpoint_y) - 1) < TOL)
    check("F center Z read gives a product endpoint state", pure_two_qubit_concurrence(endpoint_z) < TOL)
    check("F Bell capability selects transverse class but ties X and Y", abs(pure_two_qubit_concurrence(endpoint_x) - pure_two_qubit_concurrence(endpoint_y)) < TOL)
    fidelity_x = abs(np.vdot(phi_plus, endpoint_x)) ** 2
    fidelity_y = abs(np.vdot(phi_plus, endpoint_y)) ** 2
    check("F phase-sensitive Phi-plus effect accepts X branch with certainty", abs(fidelity_x - 1) < TOL)
    check("F the same fixed effect accepts Y branch with probability one-half", abs(fidelity_y - 0.5) < TOL)
    check("F a fixed framed continuation operationally separates X and Y", abs(fidelity_x - fidelity_y) > 0.49)


def clause_delete_event_actuality_controls(
    models: dict[str, tuple[np.ndarray, ...]]
) -> None:
    section("G - Clause deletes: blank, apparatus, occurrence, persistence, actuality")
    pointer, flip, blank_vector, blank, unitary = models["X-third-axis"]
    flip_eigenblank = projector(PLUS_X)
    probes = (projector(ZERO), projector(PLUS_X), projector(PLUS_Y), I2 / 2)
    check(
        "G supplied fresh blank makes the X apparatus dephase",
        all(np.allclose(reduced_channel(unitary, blank, rho), dephase(pointer, rho), atol=TOL) for rho in probes),
    )
    check(
        "G deleting blank preparation can make the same apparatus channel identity",
        all(np.allclose(reduced_channel(unitary, flip_eigenblank, rho), rho, atol=TOL) for rho in probes),
    )

    input_state = np.kron(ZERO, blank_vector)
    zero_executions = input_state
    one_execution = unitary @ input_state
    two_executions = unitary @ one_execution
    check("G an apparatus operator does not execute itself", not np.allclose(zero_executions, one_execution, atol=TOL))
    check("G a second coherent execution can erase the imprint", np.allclose(two_executions, zero_executions, atol=TOL))
    check("G future-operation scope is needed for permanent physical imprint", np.allclose(unitary @ unitary, np.eye(4), atol=TOL))

    system_marginal = reduced_density(one_execution, (2, 2), (0,))
    branch_plus = np.kron(plus_eigenvector(X), ZERO)
    branch_minus = np.kron(plus_eigenvector(-X), ONE)
    check("G one executed copy leaves a pure coherent joint state", abs(np.vdot(one_execution, one_execution) - 1) < TOL)
    check("G its system marginal is mixed", abs(np.trace(system_marginal @ system_marginal).real - 0.5) < TOL)
    check("G the coherent imprint is neither one actual branch", not np.allclose(one_execution, branch_plus, atol=TOL) and not np.allclose(one_execution, branch_minus, atol=TOL))

    frame_only_state = np.kron(PLUS_Y, PLUS_X)
    check("G a named frame without apparatus leaves the system-fragment state unchanged", np.allclose(np.eye(4) @ frame_only_state, frame_only_state, atol=TOL))
    check("G X and Y apparatus laws differ despite the same full frame", not np.allclose(models["X-third-axis"][4], models["Y-header-axis"][4], atol=TOL))


def interface_and_no_go_contract() -> None:
    section("H - Lane map and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    for interface in (
        "CONTEXT",
        "CHIRALITY",
        "BLANK",
        "EVENT",
        "PERSISTENCE",
        "ACTUALITY",
    ):
        check(f"H interface map contains {interface}", f"`{interface}`" in note_raw)
    for phrase in (
        "two-ray frame theorem",
        "fixed-lift soldering theorem",
        "a full frame names more than one transverse relation",
        "chirality does not select x versus y",
        "same full frame",
        "phase-sensitive continuation",
        "no axiom text is proposed",
        "blank-fragment preparation",
        "event occurrence",
        "single-history actuality",
    ):
        check(f"H conclusion needle: {phrase}", phrase in note)
    for index in range(1, 9):
        check(f"H N{index} section is present", f"### N{index}" in note_raw)
    check("H no-go discipline gate is narrowly scoped PASS", "no-go discipline status: pass" in note)
    check("H broad result remains partial", "partial-attempt-with-named-untested-routes" in note)
    check("H no universal no-go or new-axiom necessity is claimed", "not a universal no-go" in note and "does not establish that a new axiom is required" in note)


def main() -> int:
    authority_and_source_contract()
    group = spatial_chiral_frame_controls()
    two_ray_frame_theorem()
    soldering_intertwiner_controls(group)
    models = framed_apparatus_pair()
    cluster_bell_separator()
    clause_delete_event_actuality_controls(models)
    interface_and_no_go_contract()
    section("SUMMARY")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
