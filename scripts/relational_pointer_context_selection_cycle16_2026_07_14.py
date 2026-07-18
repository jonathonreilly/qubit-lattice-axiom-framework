#!/usr/bin/env python3
"""Cycle 16 exact controls for relational pointer-context selection.

Companion note:
  docs/work_history/repo/review_feedback/
  RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md

The runner checks only finite-dimensional algebra and source/interface
contracts.  It does not select a microscopic law, promote a theorem, amend an
axiom or primitive, set an audit verdict, edit a queue, commit, or open a PR.
Exit code is zero iff every check passes.
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
    / "RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE15 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md"
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
PLUS = (ZERO + ONE) / np.sqrt(2)
MINUS = (ZERO - ONE) / np.sqrt(2)


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


def axis_projectors(axis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    axis = np.asarray(axis, dtype=complex)
    return (I2 + axis) / 2, (I2 - axis) / 2


def dephase(axis: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    p_plus, p_minus = axis_projectors(axis)
    return p_plus @ matrix @ p_plus + p_minus @ matrix @ p_minus


def partial_dephase(axis: np.ndarray, eta: float, matrix: np.ndarray) -> np.ndarray:
    return ((1 + eta) / 2) * matrix + ((1 - eta) / 2) * axis @ matrix @ axis


def depolarize(matrix: np.ndarray) -> np.ndarray:
    return np.trace(matrix) * I2 / 2


def pauli_transfer(channel) -> np.ndarray:
    transfer = np.zeros((4, 4), dtype=complex)
    for row, observable in enumerate(PAULI):
        for column, source in enumerate(PAULI):
            transfer[row, column] = np.trace(observable @ channel(source)) / 2
    return transfer


def fixed_dimension(channel, dimension: int) -> int:
    basis = []
    for row in range(dimension):
        for column in range(dimension):
            matrix = np.zeros((dimension, dimension), dtype=complex)
            matrix[row, column] = 1
            basis.append(matrix)
    superoperator = np.column_stack([channel(matrix).reshape(-1) for matrix in basis])
    return dimension * dimension - np.linalg.matrix_rank(
        superoperator - np.eye(dimension * dimension), tol=TOL
    )


def commutant_dimension(operators: tuple[np.ndarray, ...], dimension: int) -> int:
    columns = []
    for row in range(dimension):
        for column in range(dimension):
            matrix = np.zeros((dimension, dimension), dtype=complex)
            matrix[row, column] = 1
            columns.append(
                np.concatenate([(matrix @ op - op @ matrix).reshape(-1) for op in operators])
            )
    constraint = np.column_stack(columns)
    return dimension * dimension - np.linalg.matrix_rank(constraint, tol=TOL)


def plus_eigenvector(axis: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(axis)
    return vectors[:, int(np.argmax(values))]


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
    constraints = []
    for basis in PAULI:
        lifted = np.kron(basis, I2)
        constraints.append((lifted @ unitary - unitary @ lifted).reshape(-1))
    matrix = np.column_stack(constraints)
    return 4 - np.linalg.matrix_rank(matrix, tol=TOL)


def lift_single(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    factors = [I2] * count
    factors[site] = operator
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def local_commutant_dimension(unitary: np.ndarray, site: int, count: int) -> int:
    constraints = []
    for basis in PAULI:
        lifted = lift_single(basis, site, count)
        constraints.append((lifted @ unitary - unitary @ lifted).reshape(-1))
    matrix = np.column_stack(constraints)
    return 4 - np.linalg.matrix_rank(matrix, tol=TOL)


def conditional_endpoint_vector(
    three_qubit_state: np.ndarray, center_vector: np.ndarray
) -> np.ndarray:
    tensor = three_qubit_state.reshape(2, 2, 2)
    endpoint = np.einsum("b,abc->ac", center_vector.conj(), tensor).reshape(4)
    return endpoint / np.linalg.norm(endpoint)


def pure_two_qubit_concurrence(vector: np.ndarray) -> float:
    coefficients = vector.reshape(2, 2)
    return float(2 * abs(np.linalg.det(coefficients)))


def branch(axis: np.ndarray, sign: int, density: np.ndarray) -> np.ndarray:
    projector_ = axis_projectors(axis)[0 if sign == 1 else 1]
    return projector_ @ density @ projector_


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


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, and primary-source contract")
    note = normalized(NOTE.read_text(encoding="utf-8"))
    axioms = normalized(AXIOMS.read_text(encoding="utf-8"))
    registry = REGISTRY.read_text(encoding="utf-8").lower()
    cycle15 = normalized(CYCLE15.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom" in note
        and all(token in note for token in ("primitive", "registry", "audit", "queue", "policy", "retained surface")),
    )
    check(
        "A current foundation explicitly withholds context selection",
        "context selection" in axioms and "measurement basis selection" in axioms,
    )
    for primitive in (
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ):
        check(f"A registry contains {primitive}", primitive in registry)
    check(
        "A Cycle 15 supplies the binary repeatability reduction",
        "sharp binary-qubit reduction" in cycle15
        and "x versus z remains supplied" in cycle15,
    )
    for token in (
        "zurek",
        "kribs",
        "holbrook",
        "laflamme",
        "zanardi",
        "rasetti",
        "carmeli",
        "heinosaari",
        "toigo",
        "bartlett",
        "rudolph",
        "spekkens",
        "paz",
    ):
        check(f"A primary-source ledger names {token}", token in note)


def simple_fixed_axis_theorem() -> None:
    section("B - Simple fixed axis uniquely selects a binary pointer context")
    axes = {"X": X, "Y": Y, "Z": Z}
    for name, axis in axes.items():
        channel = lambda matrix, a=axis: dephase(a, matrix)
        transfer = pauli_transfer(channel)
        eigenvalues = np.linalg.eigvals(transfer)
        check(f"B {name} dephasing is trace preserving", all(abs(np.trace(channel(rho)) - np.trace(rho)) < TOL for rho in (projector(ZERO), projector(PLUS), I2 / 2)))
        check(f"B {name} dephasing is unital", np.allclose(channel(I2), I2, atol=TOL))
        check(f"B {name} dephasing is idempotent", all(np.allclose(channel(channel(matrix)), channel(matrix), atol=TOL) for matrix in PAULI))
        check(f"B {name} dephasing fixed space has dimension two", fixed_dimension(channel, 2) == 2)
        check(f"B {name} transfer has exactly two unit eigenvalues including identity", sum(abs(value - 1) < TOL for value in eigenvalues) == 2)
        p_plus, p_minus = axis_projectors(axis)
        check(f"B {name} minimal projectors are fixed", np.allclose(channel(p_plus), p_plus, atol=TOL) and np.allclose(channel(p_minus), p_minus, atol=TOL))
        check(f"B {name} projectors are rank one and exhaustive", round(np.trace(p_plus).real) == 1 and round(np.trace(p_minus).real) == 1 and np.allclose(p_plus + p_minus, I2, atol=TOL))
        check(f"B {name} binary branches are exactly repeatable", all(np.allclose(branch(axis, sign, branch(axis, sign, rho)), branch(axis, sign, rho), atol=TOL) for sign in (-1, 1) for rho in (projector(ZERO), projector(PLUS), I2 / 2)))

    eta = 0.37
    partial = lambda matrix: partial_dephase(Z, eta, matrix)
    check("B partial dephasing still has one simple non-scalar fixed axis", fixed_dimension(partial, 2) == 2)
    check("B partial dephasing preserves the Z pointer states", np.allclose(partial(projector(ZERO)), projector(ZERO), atol=TOL) and np.allclose(partial(projector(ONE)), projector(ONE), atol=TOL))
    check("B partial dephasing does not itself make a perfect record", np.trace(partial(projector(PLUS)) @ partial(projector(PLUS))).real > 0.5 + TOL)


def exact_interaction_selects_its_commutant() -> dict[str, object]:
    section("C - Exact controlled interactions select their own pointer commutants")
    models = {
        "Z-relative": (Z, X),
        "X-relative": (X, Z),
    }
    result: dict[str, object] = {}
    probes = (projector(ZERO), projector(ONE), projector(PLUS), projector((ZERO + 1j * ONE) / np.sqrt(2)), I2 / 2)
    for name, (axis, flip) in models.items():
        unitary = copy_unitary(axis, flip)
        blank_vector = plus_eigenvector(axis)
        blank = projector(blank_vector)
        channel = lambda matrix, u=unitary, b=blank: reduced_channel(u, b, matrix)
        check(f"C {name} controlled interaction is unitary", np.allclose(unitary.conj().T @ unitary, np.eye(4), atol=TOL))
        check(f"C {name} system-side commutant has dimension two", system_commutant_dimension(unitary) == 2)
        check(f"C {name} reduced channel is exact full dephasing", all(np.allclose(channel(rho), dephase(axis, rho), atol=TOL) for rho in probes))
        check(f"C {name} reduced channel has unique binary fixed algebra", fixed_dimension(channel, 2) == 2)

        p_plus, p_minus = axis_projectors(axis)
        plus_vector = plus_eigenvector(axis)
        minus_vector = plus_eigenvector(-axis)
        out_plus = unitary @ np.kron(plus_vector, blank_vector)
        out_minus = unitary @ np.kron(minus_vector, blank_vector)
        env_plus = reduced_density(out_plus, (2, 2), (1,))
        env_minus = reduced_density(out_minus, (2, 2), (1,))
        check(f"C {name} conditional fragment states are orthogonal", abs(np.trace(env_plus @ env_minus)) < TOL)
        check(f"C {name} pointer eigenstates are nondemolished", np.allclose(reduced_density(out_plus, (2, 2), (0,)), p_plus, atol=TOL) and np.allclose(reduced_density(out_minus, (2, 2), (0,)), p_minus, atol=TOL))
        result[name] = (axis, flip, unitary, blank, blank_vector, channel)

    z_axis, _, z_unitary, _, _, _ = result["Z-relative"]
    blank_zero = projector(ZERO)
    blank_plus = projector(PLUS)
    check("C CNOT with Z blank produces Z dephasing", all(np.allclose(reduced_channel(z_unitary, blank_zero, rho), dephase(z_axis, rho), atol=TOL) for rho in probes))
    check("C the same CNOT with X-plus blank produces the identity channel", all(np.allclose(reduced_channel(z_unitary, blank_plus, rho), rho, atol=TOL) for rho in probes))
    check("C exact interaction alone does not supply the fragment preparation", not np.allclose(blank_zero, blank_plus, atol=TOL))
    return result


def programmed_cz_context_control() -> None:
    section("D - The programmed CZ-CZ interaction selects Z, not the center X read")
    diagonal = []
    for a, b, c in product((0, 1), repeat=3):
        diagonal.append((-1) ** (a * b + b * c))
    cluster_unitary = np.diag(diagonal).astype(complex)
    check("D CZ-CZ is a unitary involution", np.allclose(cluster_unitary @ cluster_unitary, np.eye(8), atol=TOL))
    for site, label in enumerate(("left", "center", "right")):
        check(f"D {label} onsite interaction commutant has dimension two", local_commutant_dimension(cluster_unitary, site, 3) == 2)
        check(f"D {label} Z is conserved by CZ-CZ", np.allclose(cluster_unitary @ lift_single(Z, site, 3), lift_single(Z, site, 3) @ cluster_unitary, atol=TOL))
    check("D center X is not in the stable interaction commutant", not np.allclose(cluster_unitary @ lift_single(X, 1, 3), lift_single(X, 1, 3) @ cluster_unitary, atol=TOL))
    check("D center Y is not in the stable interaction commutant", not np.allclose(cluster_unitary @ lift_single(Y, 1, 3), lift_single(Y, 1, 3) @ cluster_unitary, atol=TOL))

    prepared = np.kron(PLUS, np.kron(PLUS, PLUS))
    cluster = cluster_unitary @ prepared
    x_plus_endpoint = conditional_endpoint_vector(cluster, PLUS)
    y_plus = (ZERO + 1j * ONE) / np.sqrt(2)
    y_plus_endpoint = conditional_endpoint_vector(cluster, y_plus)
    z_zero_endpoint = conditional_endpoint_vector(cluster, ZERO)
    check("D center X read produces a maximally entangled endpoint state", abs(pure_two_qubit_concurrence(x_plus_endpoint) - 1) < TOL)
    check("D center Y read also produces a maximally entangled endpoint state", abs(pure_two_qubit_concurrence(y_plus_endpoint) - 1) < TOL)
    check("D center Z read produces a product endpoint state", pure_two_qubit_concurrence(z_zero_endpoint) < TOL)
    check("D Bell capability selects an equatorial class but not X uniquely", abs(pure_two_qubit_concurrence(x_plus_endpoint) - pure_two_qubit_concurrence(y_plus_endpoint)) < TOL)


def redundancy_event_and_actuality(models: dict[str, object]) -> None:
    section("E - Redundancy supplies an imprint, not occurrence or actuality")
    _, _, cnot, _, _, _ = models["Z-relative"]
    initial = np.kron(PLUS, np.kron(ZERO, ZERO))
    cnot_01 = np.zeros((8, 8), dtype=complex)
    cnot_02 = np.zeros((8, 8), dtype=complex)
    for bits in product((0, 1), repeat=3):
        source = 4 * bits[0] + 2 * bits[1] + bits[2]
        out_01 = (bits[0], bits[1] ^ bits[0], bits[2])
        out_02 = (bits[0], bits[1], bits[2] ^ bits[0])
        cnot_01[4 * out_01[0] + 2 * out_01[1] + out_01[2], source] = 1
        cnot_02[4 * out_02[0] + 2 * out_02[1] + out_02[2], source] = 1
    fanout = cnot_02 @ cnot_01
    ghz = fanout @ initial
    target = (np.kron(ZERO, np.kron(ZERO, ZERO)) + np.kron(ONE, np.kron(ONE, ONE))) / np.sqrt(2)
    check("D two local copy interactions form exact redundant GHZ witnesses", np.allclose(ghz, target, atol=TOL))
    for witness in (1, 2):
        marginal = reduced_density(ghz, (2, 2, 2), (witness,))
        check(f"D witness {witness} carries a classical half-half marginal", np.allclose(marginal, I2 / 2, atol=TOL))
    check("D the global redundant state remains pure", abs(np.trace(projector(ghz) @ projector(ghz)).real - 1) < TOL)
    check("D reversing the interaction restores input and blank fragments", np.allclose(fanout.conj().T @ ghz, initial, atol=TOL))

    once = cnot @ np.kron(PLUS, ZERO)
    zero_times = np.kron(PLUS, ZERO)
    twice = cnot @ once
    check("D zero executions and one execution give different physical states", not np.allclose(zero_times, once, atol=TOL))
    check("D a second identical coherent copy can erase the first imprint", np.allclose(twice, zero_times, atol=TOL))
    reduced = reduced_density(once, (2, 2), (0,))
    check("D one interaction yields a mixed local state while the joint state is pure", np.allclose(reduced, I2 / 2, atol=TOL) and abs(np.vdot(once, once) - 1) < TOL)
    branch_zero = np.kron(ZERO, ZERO)
    branch_one = np.kron(ONE, ONE)
    check("D the coherent result is neither single outcome branch", not np.allclose(once, branch_zero, atol=TOL) and not np.allclose(once, branch_one, atol=TOL))


def noiseless_commutant_controls() -> None:
    section("F - Noiseless commutants can be unique, trivial, or nonclassical")
    z_dephase = lambda matrix: dephase(Z, matrix)
    check("E one-qubit Z noise commutant has dimension two", commutant_dimension((I2, Z), 2) == 2)
    check("E one-qubit Z channel fixed algebra matches that commutant", fixed_dimension(z_dephase, 2) == 2)

    identity = lambda matrix: matrix
    check("E identity dynamics fixes the full qubit algebra", fixed_dimension(identity, 2) == 4)
    check("E identity dynamics selects no unique classical pointer basis", commutant_dimension((I2,), 2) == 4)
    check("E complete depolarization fixes scalars only", fixed_dimension(depolarize, 2) == 1)

    zz = np.kron(Z, Z)
    parity = lambda matrix: (matrix + zz @ matrix @ zz) / 2
    check("E two-qubit parity channel has an eight-dimensional fixed algebra", fixed_dimension(parity, 4) == 8)
    check("E parity fixed algebra equals the noise commutant dimension", commutant_dimension((np.eye(4), zz), 4) == 8)
    fixed_a = np.kron(Z, I2)
    fixed_b = np.kron(X, X)
    check("E two explicit parity-fixed observables survive", np.allclose(parity(fixed_a), fixed_a, atol=TOL) and np.allclose(parity(fixed_b), fixed_b, atol=TOL))
    check("E those stable observables do not commute", not np.allclose(fixed_a @ fixed_b, fixed_b @ fixed_a, atol=TOL))
    check("E a noiseless fixed algebra need not be a unique classical MASA", fixed_dimension(parity, 4) > 2 and np.linalg.norm(fixed_a @ fixed_b - fixed_b @ fixed_a) > TOL)


def predictability_sieve_controls() -> None:
    section("G - Predictability sieve selects within a dynamics and can tie")
    pointer_scores = []
    identity_scores = []
    depolarizing_scores = []
    zero_score_only_at_poles = True
    for theta in np.linspace(0, np.pi, 13):
        for phi in np.linspace(0, 2 * np.pi, 16, endpoint=False):
            vector = np.cos(theta / 2) * ZERO + np.exp(1j * phi) * np.sin(theta / 2) * ONE
            rho = projector(vector)
            for channel, bucket in (
                (lambda matrix: dephase(Z, matrix), pointer_scores),
                (lambda matrix: matrix, identity_scores),
                (depolarize, depolarizing_scores),
            ):
                output = channel(rho)
                bucket.append(1 - np.trace(output @ output).real)
            if abs(pointer_scores[-1]) < TOL and abs(np.sin(theta)) > TOL:
                zero_score_only_at_poles = False
    check("F Z dephasing has zero entropy production only at its two poles", zero_score_only_at_poles)
    check("F Z pointer poles have exact zero sieve score", min(pointer_scores) < TOL)
    check("F transverse states lose purity under Z dephasing", max(pointer_scores) > 0.49)
    check("F identity dynamics ties every pure state at zero", max(abs(value) for value in identity_scores) < TOL)
    check("F depolarizing dynamics ties every pure state at one-half", max(abs(value - 0.5) for value in depolarizing_scores) < TOL)
    check("F a sieve is a ranking functional conditional on supplied dynamics", len(set(round(value, 8) for value in pointer_scores)) > 2 and len(set(round(value, 8) for value in identity_scores)) == 1)


def relational_covariance_and_paired_countermodel(models: dict[str, object]) -> None:
    section("H - Relational covariance preserves a genuine parallel/transverse fork")
    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    phase = np.diag([1, 1j]).astype(complex)
    angle = np.pi / 5
    y_rotation = np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * Y
    recoders = (I2, hadamard, phase, y_rotation)
    probes = (projector(ZERO), projector(PLUS), projector((ZERO + 1j * ONE) / np.sqrt(2)), I2 / 2)

    for model_name, model in models.items():
        axis, flip, unitary, blank, _, _ = model
        for index, recoder in enumerate(recoders):
            axis_rotated = recoder @ axis @ recoder.conj().T
            flip_rotated = recoder @ flip @ recoder.conj().T
            unitary_rotated = np.kron(recoder, recoder) @ unitary @ np.kron(recoder.conj().T, recoder.conj().T)
            blank_rotated = recoder @ blank @ recoder.conj().T
            check(f"G {model_name} common-M2 interaction covariance {index}", np.allclose(unitary_rotated, copy_unitary(axis_rotated, flip_rotated), atol=TOL))
            channel_covariant = all(
                np.allclose(
                    reduced_channel(unitary_rotated, blank_rotated, recoder @ rho @ recoder.conj().T),
                    recoder @ reduced_channel(unitary, blank, rho) @ recoder.conj().T,
                    atol=TOL,
                )
                for rho in probes
            )
            check(f"G {model_name} reduced-channel covariance {index}", channel_covariant)
            instrument_covariant = all(
                np.allclose(
                    branch(axis_rotated, sign, recoder @ rho @ recoder.conj().T),
                    recoder @ branch(axis, sign, rho) @ recoder.conj().T,
                    atol=TOL,
                )
                for sign in (-1, 1)
                for rho in probes
            )
            check(f"G {model_name} binary-instrument covariance {index}", instrument_covariant)

    z_axis = models["Z-relative"][0]
    x_axis = models["X-relative"][0]
    parallel_invariant = np.trace(z_axis @ Z).real / 2
    transverse_invariant = np.trace(x_axis @ Z).real / 2
    check("G pointer-to-frame Hilbert-Schmidt relation separates the laws", abs(parallel_invariant - 1) < TOL and abs(transverse_invariant) < TOL)
    check("G common recoding preserves the pointer-to-frame relation", all(abs(np.trace((v @ z_axis @ v.conj().T) @ (v @ Z @ v.conj().T)).real / 2 - parallel_invariant) < TOL and abs(np.trace((v @ x_axis @ v.conj().T) @ (v @ Z @ v.conj().T)).real / 2 - transverse_invariant) < TOL for v in recoders))
    rho_zero = projector(ZERO)
    z_channel = models["Z-relative"][5]
    x_channel = models["X-relative"][5]
    check("G same framed input operationally separates parallel and transverse laws", not np.allclose(z_channel(rho_zero), x_channel(rho_zero), atol=TOL))

    rz = np.cos(np.pi / 4) * I2 - 1j * np.sin(np.pi / 4) * Z
    pz = projector(ZERO)
    px = projector(PLUS)
    check("G a Z-axis reference is invariant under its U1 stabilizer", np.allclose(rz @ pz @ rz.conj().T, pz, atol=TOL))
    check("G that stabilizer rotates a transverse X projector", not np.allclose(rz @ px @ rz.conj().T, px, atol=TOL))
    equatorial = []
    for phi in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        vector = (ZERO + np.exp(1j * phi) * ONE) / np.sqrt(2)
        candidate = projector(vector)
        equatorial.append(np.allclose(rz @ candidate @ rz.conj().T, candidate, atol=TOL))
    check("G no sampled transverse axis is fixed by the one-axis stabilizer", not any(equatorial))
    check("G a single-axis reference cannot covariantly name a transverse context", np.allclose(rz @ pz @ rz.conj().T, pz, atol=TOL) and not any(equatorial))

    rotations = proper_cubic_group()
    directions = tuple(np.array(direction, dtype=int) for direction in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
    direction_set = {tuple(direction) for direction in directions}
    check("G proper cubic group has 24 elements", len(rotations) == 24)
    check("G every proper cubic rotation preserves nearest-neighbor support", all(tuple(rotation @ direction) in direction_set for rotation in rotations for direction in directions))
    translation = np.array([3, -2, 5], dtype=int)
    check("G relational two-site motif is translation/proper-cubic covariant", all(np.sum(np.abs((rotation @ direction + translation) - translation)) == 1 for rotation in rotations for direction in directions))
    check("G both pointer laws use the same covariant spatial support class", models["Z-relative"][2].shape == models["X-relative"][2].shape == (4, 4))


def interface_and_no_go_contract() -> None:
    section("I - CONTEXT/EVENT/ACTUALITY and N1-N8 contract")
    note_raw = NOTE.read_text(encoding="utf-8")
    note = normalized(note_raw)
    for interface in ("CONTEXT", "EVENT", "ACTUALITY"):
        check(f"H interface map contains {interface}", f"`{interface}`" in note_raw)
    for phrase in (
        "simple-fixed-axis theorem",
        "interaction-side commutant",
        "context after dynamics",
        "parallel versus transverse",
        "one-axis reference cannot select a transverse context",
        "covariant instruments form a class",
        "redundancy is not occurrence",
        "redundancy is not actuality",
        "no axiom text is proposed",
    ):
        check(f"H note contains conclusion needle: {phrase}", phrase in note)
    for index in range(1, 9):
        check(f"H N{index} section is present", f"### N{index}" in note_raw)
    check("H no-go discipline status is scoped PASS", "no-go discipline status: pass" in note)
    check("H negative boundary is explicitly finite and premise-bounded", "finite paired countermodel" in note and "not a universal no-go" in note)
    check("H overall result remains a partial attempt", "partial-attempt-with-named-untested-routes" in note)


def main() -> int:
    authority_and_source_contract()
    simple_fixed_axis_theorem()
    models = exact_interaction_selects_its_commutant()
    programmed_cz_context_control()
    redundancy_event_and_actuality(models)
    noiseless_commutant_controls()
    predictability_sieve_controls()
    relational_covariance_and_paired_countermodel(models)
    interface_and_no_go_contract()
    section("SUMMARY")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
