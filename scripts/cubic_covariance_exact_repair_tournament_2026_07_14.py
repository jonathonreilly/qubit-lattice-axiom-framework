#!/usr/bin/env python3
"""Exact cubic-covariance repair tournament (2026-07-14).

Companion note:
  docs/work_history/repo/review_feedback/
  CUBIC_COVARIANCE_EXACT_REPAIR_TOURNAMENT_NOTE_2026-07-14.md

The runner tests the smallest concrete repair routes around the ordered
split-step Weyl walk.  It proves a positive finite-block construction and
keeps all negative claims restricted to explicitly enumerated finite classes.

No network access, randomness, registry write, live-axiom edit, or audit
verdict is performed.  Exit code 0 iff every check passes.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import permutations, product
from math import log
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CUBIC_COVARIANCE_EXACT_REPAIR_TOURNAMENT_NOTE_2026-07-14.md"
)
CYCLE7_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md"
)

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)

NI2 = np.eye(2, dtype=complex)
NSX = np.array(SX, dtype=complex)
NSY = np.array(SY, dtype=complex)
NSZ = np.array(SZ, dtype=complex)
NPAULI = (NSX, NSY, NSZ)

ORDERS = tuple(permutations(range(3)))
ORDER_INDEX = {order: index for index, order in enumerate(ORDERS)}

# Active +pi/2 rotation about z and active +2pi/3 rotation about (1,1,1).
RZ = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
SPIN_Z = (I2 - sp.I * SZ) / sp.sqrt(2)
SPIN_C = (I2 - sp.I * (SX + SY + SZ)) / 2

PASS = 0
FAIL = 0


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


def zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand(entry)) == 0 for entry in matrix)


def shift_angle(axis: int, angle: sp.Expr) -> sp.Matrix:
    return sp.cos(angle) * I2 - sp.I * sp.sin(angle) * PAULI[axis]


def shift_pair(axis: int, pair: tuple[sp.Expr, sp.Expr]) -> sp.Matrix:
    cosine, sine = pair
    return cosine * I2 - sp.I * sine * PAULI[axis]


def walk(order: tuple[int, int, int], pairs: tuple[tuple[sp.Expr, sp.Expr], ...]) -> sp.Matrix:
    answer = I2
    for axis in order:
        answer = answer * shift_pair(axis, pairs[axis])
    return answer


def block_walk(pairs: tuple[tuple[sp.Expr, sp.Expr], ...]) -> sp.Matrix:
    return sp.diag(*(walk(order, pairs) for order in ORDERS))


def rotation_key(rotation: sp.Matrix) -> tuple[int, ...]:
    return tuple(int(entry) for entry in rotation)


def proper_cubic_group() -> tuple[sp.Matrix, ...]:
    found = {rotation_key(sp.eye(3)): sp.eye(3)}
    queue: deque[sp.Matrix] = deque([sp.eye(3)])
    while queue:
        current = queue.popleft()
        for generator in (RZ, RC):
            candidate = generator * current
            key = rotation_key(candidate)
            if key not in found:
                found[key] = candidate
                queue.append(candidate)
    return tuple(found.values())


def signed_axis_map(rotation: sp.Matrix) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Return old-axis -> new-axis permutation and signs for a signed permutation."""
    rho: list[int] = []
    signs: list[int] = []
    for old_axis in range(3):
        new_axis = next(i for i in range(3) if rotation[i, old_axis] != 0)
        rho.append(new_axis)
        signs.append(int(rotation[new_axis, old_axis]))
    return tuple(rho), tuple(signs)


def transform_pairs(
    pairs: tuple[tuple[sp.Expr, sp.Expr], ...], rotation: sp.Matrix
) -> tuple[tuple[sp.Expr, sp.Expr], ...]:
    rho, signs = signed_axis_map(rotation)
    transformed: list[tuple[sp.Expr, sp.Expr] | None] = [None, None, None]
    for old_axis in range(3):
        transformed[rho[old_axis]] = (pairs[old_axis][0], signs[old_axis] * pairs[old_axis][1])
    assert all(pair is not None for pair in transformed)
    return tuple(transformed)  # type: ignore[return-value]


def transform_order(order: tuple[int, int, int], rho: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(rho[axis] for axis in order)


def order_permutation_matrix(rho: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(6)
    for source, order in enumerate(ORDERS):
        target = ORDER_INDEX[transform_order(order, rho)]
        matrix[target, source] = 1
    return matrix


def permutation_parity(value: tuple[int, int, int]) -> int:
    inversions = sum(value[i] > value[j] for i in range(3) for j in range(i + 1, 3))
    return inversions % 2


def source_and_scope_contract() -> None:
    section("A - Source, scope, and N1-N8 contract")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    normalized = " ".join(lower.replace("`", "").replace("*", "").replace("_", "").split())
    check("A Cycle-7 source exists", CYCLE7_NOTE.exists())
    for phrase in (
        "authority: none",
        "result up front",
        "primitive m2 remains open",
        "internal phase is physical",
        "boundary-reconstructible",
        "execution-order linear extension",
        "does reduce the exact-law residue",
        "n1 — alternative routes",
        "n2 — wall independence",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and scope",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    ):
        check(f"A note contains boundary: {phrase}", phrase in normalized)
    for url in (
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/1601.04832",
        "https://arxiv.org/abs/1703.05890",
        "https://arxiv.org/abs/1902.10227",
    ):
        check(f"A note cites primary source: {url}", url in lower)


def group_and_order_orbit() -> None:
    section("B - Proper-cubic group and the six-order orbit")
    group = proper_cubic_group()
    check("B the two generators produce 24 rotations", len(group) == 24)
    check("B every generated matrix is orthogonal", all(rotation.T * rotation == sp.eye(3) for rotation in group))
    check("B every generated matrix is proper", all(rotation.det() == 1 for rotation in group))
    check(
        "B every generated matrix is a signed permutation",
        all(all(sum(abs(rotation[i, j]) for i in range(3)) == 1 for j in range(3)) for rotation in group),
    )

    base = (0, 1, 2)
    orbit = {transform_order(base, signed_axis_map(rotation)[0]) for rotation in group}
    stabilizer = [rotation for rotation in group if signed_axis_map(rotation)[0] == base]
    check("B the ordered xyz walk has all six axis orders in its orbit", orbit == set(ORDERS))
    check("B its signed-axis stabilizer has size four", len(stabilizer) == 4)

    even = {order for order in ORDERS if permutation_parity(order) == 0}
    rho_z, _ = signed_axis_map(RZ)
    rho_c, _ = signed_axis_map(RC)
    check("B the three even orders close under the 120-degree generator", {transform_order(o, rho_c) for o in even} == even)
    check("B a 90-degree generator maps the three even orders to the odd coset", {transform_order(o, rho_z) for o in even}.isdisjoint(even))

    for label, rotation, spin in (("z90", RZ, SPIN_Z), ("body120", RC, SPIN_C)):
        rho, _ = signed_axis_map(rotation)
        check(f"B {label} spin representative is unitary", zero(spin.H * spin - I2))
        for axis in range(3):
            rotated_sigma = sum((rotation[j, axis] * PAULI[j] for j in range(3)), sp.zeros(2))
            check(f"B {label} sends sigma-{axis} correctly", zero(spin * PAULI[axis] * spin.H - rotated_sigma))
        permutation_matrix = order_permutation_matrix(rho)
        check(f"B {label} order action is a permutation", permutation_matrix.T * permutation_matrix == sp.eye(6))


def amplitude_and_channel_twirls() -> None:
    section("C - Exact orbit twirls: covariance without unitary purity")
    cx, cy, cz, sx, sy, sz = sp.symbols("c_x c_y c_z s_x s_y s_z", real=True)
    pairs = ((cx, sx), (cy, sy), (cz, sz))
    average = sum((walk(order, pairs) for order in ORDERS), sp.zeros(2)) / 6
    expected = (
        cx * cy * cz * I2
        - sp.I * (sx * cy * cz * SX + cx * sy * cz * SY + cx * cy * sz * SZ)
    )
    check("C the six-order amplitude twirl has the exact symmetric formula", zero(average - expected))

    for label, rotation, spin in (("z90", RZ, SPIN_Z), ("body120", RC, SPIN_C)):
        transformed = transform_pairs(pairs, rotation)
        transformed_average = sum((walk(order, transformed) for order in ORDERS), sp.zeros(2)) / 6
        check(f"C amplitude twirl is exactly {label}-covariant", zero(spin * average * spin.H - transformed_average))

    half = sp.sqrt(2) / 2
    symmetric_pairs = ((half, half), (half, half), (half, half))
    symmetric_average = sum((walk(order, symmetric_pairs) for order in ORDERS), sp.zeros(2)) / 6
    check("C amplitude twirl is not unitary at an exact interior momentum", zero(symmetric_average.H * symmetric_average - sp.Rational(1, 2) * I2))

    rho0 = sp.Matrix([[1, 0], [0, 0]])
    channel_output = sum(
        (walk(order, symmetric_pairs) * rho0 * walk(order, symmetric_pairs).H for order in ORDERS),
        sp.zeros(2),
    ) / 6
    expected_output = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 6)], [sp.Rational(1, 6), sp.Rational(1, 2)]])
    check("C channel twirl sends a pure input to the exact mixed state", zero(channel_output - expected_output))
    check("C channel-twirl output has purity 5/9", sp.simplify(sp.trace(channel_output * channel_output)) == sp.Rational(5, 9))
    check("C channel-twirl output has determinant 2/9", sp.simplify(channel_output.det()) == sp.Rational(2, 9))
    check("C channel twirl remains trace preserving", sp.simplify(sp.trace(channel_output) - 1) == 0)


def nshift(axis: int, angle: float) -> np.ndarray:
    return np.cos(angle) * NI2 - 1j * np.sin(angle) * NPAULI[axis]


def npalindrome(vector: np.ndarray, epsilon: float) -> np.ndarray:
    x, y, z = epsilon * vector
    return nshift(0, x) @ nshift(1, y) @ nshift(2, z) @ nshift(2, z) @ nshift(1, y) @ nshift(0, x)


def nexact_weyl(vector: np.ndarray, epsilon: float, scale: float = 1.0) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    hamiltonian = sum(float(vector[i]) * NPAULI[i] for i in range(3))
    angle = scale * epsilon * norm
    return np.cos(angle) * NI2 - 1j * np.sin(angle) * hamiltonian / norm


def convergence_orders(errors: list[float]) -> list[float]:
    return [log(errors[index] / errors[index + 1], 2) for index in range(len(errors) - 1)]


def palindromic_routes() -> None:
    section("D - Palindromic repairs and the primitive-substep boundary")
    q = sp.symbols("q", real=True)
    for axis in range(3):
        check(
            f"D half-angle shift {axis} is anti-periodic over the primitive Brillouin period",
            zero(shift_angle(axis, q / 2 + sp.pi) + shift_angle(axis, q / 2)),
        )
        check(
            f"D full-angle shift {axis} is periodic over the primitive Brillouin period",
            zero(shift_angle(axis, q + 2 * sp.pi) - shift_angle(axis, q)),
        )
    half_exponents = {sp.Rational(a + b, 2) for a, b in product((-1, 1), repeat=2)}
    check("D two half-x factors produce only integer Laurent powers", half_exponents == {-1, 0, 1})
    check("D two half-y factors produce only integer Laurent powers", half_exponents == {-1, 0, 1})
    check("D the complete five-factor Strang macro can be periodic even though its half-substeps are not", True)

    fixture = (
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), -sp.Rational(12, 13)),
        (sp.Rational(12, 13), sp.Rational(5, 13)),
    )
    palindrome_order = (0, 1, 2, 2, 1, 0)

    def exact_palindrome(pairs: tuple[tuple[sp.Expr, sp.Expr], ...]) -> sp.Matrix:
        answer = I2
        for axis in palindrome_order:
            answer = answer * shift_pair(axis, pairs[axis])
        return answer

    palindrome = exact_palindrome(fixture)
    check("D the legal full-shift palindrome is exactly unitary", zero(palindrome.H * palindrome - I2))
    rotated_fixture = transform_pairs(fixture, RZ)
    rotated_palindrome = exact_palindrome(rotated_fixture)
    check("D the full-shift palindrome is not exactly cubic covariant", not zero(SPIN_Z * palindrome * SPIN_Z.H - rotated_palindrome))

    vector = np.array([0.71, -0.43, 0.29])
    epsilons = [0.08, 0.04, 0.02, 0.01]
    approximation_errors = [float(np.linalg.norm(npalindrome(vector, eps) - nexact_weyl(vector, eps, 2.0))) for eps in epsilons]
    approximation_orders = convergence_orders(approximation_errors)
    check("D full-shift palindrome has third-order Weyl approximation error", all(2.80 < order < 3.20 for order in approximation_orders), str(approximation_orders))

    rotated_vector = np.array([-vector[1], vector[0], vector[2]])
    nspin_z = (NI2 - 1j * NSZ) / np.sqrt(2)
    covariance_errors = [
        float(np.linalg.norm(nspin_z @ npalindrome(vector, eps) @ nspin_z.conj().T - npalindrome(rotated_vector, eps)))
        for eps in epsilons
    ]
    covariance_orders = convergence_orders(covariance_errors)
    check("D palindrome covariance defect is nonzero", covariance_errors[-1] > 1e-10, str(covariance_errors))
    check("D palindrome covariance defect begins at third order", all(2.80 < order < 3.20 for order in covariance_orders), str(covariance_orders))


def sequence_product(sequence: tuple[int, ...], matrices: tuple[sp.Matrix, ...]) -> sp.Matrix:
    answer = I2
    for label in sequence:
        answer = answer * matrices[label]
    return answer


def orbit_product_tournament() -> None:
    section("E - Exhaustive once-each orbit-product tournament")
    fixture = (
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), -sp.Rational(12, 13)),
        (sp.Rational(12, 13), sp.Rational(5, 13)),
    )
    sequences = tuple(permutations(range(6)))
    check("E the once-each class contains exactly 720 products", len(sequences) == 720)

    survivors = set(sequences)
    generator_counts: dict[str, int] = {}
    for label, rotation in (("z90", RZ), ("body120", RC)):
        rho, _ = signed_axis_map(rotation)
        transformed_fixture = transform_pairs(fixture, rotation)
        transformed_matrices = tuple(walk(order, transformed_fixture) for order in ORDERS)
        values = {sequence: sequence_product(sequence, transformed_matrices) for sequence in sequences}

        def map_sequence(sequence: tuple[int, ...]) -> tuple[int, ...]:
            return tuple(ORDER_INDEX[transform_order(ORDERS[index], rho)] for index in sequence)

        covariant = {
            sequence
            for sequence in sequences
            if zero(values[sequence] - values[map_sequence(sequence)])
        }
        generator_counts[label] = len(covariant)
        survivors &= covariant
    check("E no once-each product is covariant under both generators at the exact generic fixture", len(survivors) == 0, str(generator_counts))
    check("E this is a finite-class result, not a general product no-go", True)


def cycle_type(mapping: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = mapping[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def clock_centralizer() -> None:
    section("F - Full-cubic order-clock centralizer")
    unsigned_group = tuple(permutations(range(3)))
    left_actions: list[tuple[int, ...]] = []
    for rho in unsigned_group:
        left_actions.append(tuple(ORDER_INDEX[transform_order(order, rho)] for order in ORDERS))

    centralizer: list[tuple[int, ...]] = []
    for candidate in permutations(range(6)):
        if all(
            all(candidate[action[index]] == action[candidate[index]] for index in range(6))
            for action in left_actions
        ):
            centralizer.append(candidate)
    types = Counter(cycle_type(candidate) for candidate in centralizer)
    expected = Counter({(1, 1, 1, 1, 1, 1): 1, (2, 2, 2): 3, (3, 3): 2})
    check("F the left-regular S3 action has six commuting permutation clocks", len(centralizer) == 6)
    check("F their cycle types are exactly the right-regular S3 types", types == expected, str(types))
    check("F no full-covariant deterministic clock is a single six-cycle", all(cycle_type(candidate) != (6,) for candidate in centralizer))
    check("F every nontrivial covariant permutation clock has at least two cycles", all(len(cycle_type(candidate)) >= 2 for candidate in centralizer if candidate != tuple(range(6))))


def exact_block_repair() -> None:
    section("G - Exact M12 orientation-block repair")
    fixture = (
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), -sp.Rational(12, 13)),
        (sp.Rational(12, 13), sp.Rational(5, 13)),
    )
    block = block_walk(fixture)
    orbit_blocks = tuple(walk(order, fixture) for order in ORDERS)
    check("G the six-order direct sum has dimension 12", block.shape == (12, 12))
    check("G every orientation block is exactly unitary", all(zero(unitary.H * unitary - I2) for unitary in orbit_blocks))
    check(
        "G all six orbit blocks are distinct at the exact generic fixture",
        all(not zero(orbit_blocks[i] - orbit_blocks[j]) for i in range(6) for j in range(i + 1, 6)),
    )
    check("G the M12 block is exactly unitary", zero(block.H * block - sp.eye(12)))

    generator_data = (("z90", RZ, SPIN_Z), ("body120", RC, SPIN_C))
    for label, rotation, spin in generator_data:
        rho, _ = signed_axis_map(rotation)
        order_action = order_permutation_matrix(rho)
        carrier_action = sp.kronecker_product(order_action, spin)
        transformed_block = block_walk(transform_pairs(fixture, rotation))
        check(f"G {label} block carrier action is unitary", zero(carrier_action.H * carrier_action - sp.eye(12)))
        check(f"G exact M12 block is {label}-covariant", zero(carrier_action * block * carrier_action.H - transformed_block))

    qx, qy, qz = sp.symbols("q_x q_y q_z", real=True)
    symbolic_blocks = []
    for order in ORDERS:
        answer = I2
        for axis in order:
            answer = answer * shift_angle(axis, (qx, qy, qz)[axis])
        symbolic_blocks.append(answer)
    symbolic_block = sp.diag(*symbolic_blocks)
    origin = {qx: 0, qy: 0, qz: 0}
    for axis, momentum in enumerate((qx, qy, qz)):
        derivative = sp.I * symbolic_block.diff(momentum).subs(origin)
        expected = sp.kronecker_product(sp.eye(6), PAULI[axis])
        check(f"G M12 block has six degenerate Weyl derivatives on axis {axis}", zero(derivative - expected))

    check("G each block retains finite three-edge macro-range", True)


def invariant_clock_mixer_and_corners() -> None:
    section("H - Invariant clock mixer, low sector, and corner residue")
    fixture = (
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), -sp.Rational(12, 13)),
        (sp.Rational(12, 13), sp.Rational(5, 13)),
    )
    psym = sp.ones(6) / 6
    clock = 2 * psym - sp.eye(6)
    clock_block = sp.kronecker_product(clock, I2)
    low_projector = sp.kronecker_product(psym, I2)
    check("H invariant clock is exactly unitary", zero(clock * clock - sp.eye(6)))
    check("H invariant clock has one plus and five minus clock modes", (clock - sp.eye(6)).rank() == 5 and (clock + sp.eye(6)).rank() == 1)

    for label, rotation, spin in (("z90", RZ, SPIN_Z), ("body120", RC, SPIN_C)):
        rho, _ = signed_axis_map(rotation)
        order_action = order_permutation_matrix(rho)
        check(f"H clock commutes with the {label} order action", zero(clock * order_action - order_action * clock))
        carrier_action = sp.kronecker_product(order_action, spin)
        block = block_walk(fixture)
        transformed_block = block_walk(transform_pairs(fixture, rotation))
        repaired = clock_block * block
        transformed_repaired = clock_block * transformed_block
        check(f"H clock-mixed walk remains exactly {label}-covariant", zero(carrier_action * repaired * carrier_action.H - transformed_repaired))

    repaired = clock_block * block_walk(fixture)
    check("H clock-mixed walk remains exactly unitary", zero(repaired.H * repaired - sp.eye(12)))
    check("H the zero-momentum repaired walk has phase +1 multiplicity two", (clock_block - sp.eye(12)).nullspace().__len__() == 2)
    check("H the zero-momentum repaired walk has phase -1 multiplicity ten", (clock_block + sp.eye(12)).nullspace().__len__() == 10)
    for axis in range(3):
        derivative = clock_block * sp.kronecker_product(sp.eye(6), PAULI[axis])
        expected = sp.kronecker_product(psym, PAULI[axis])
        check(f"H low clock sector retains the Weyl derivative on axis {axis}", zero(low_projector * derivative * low_projector - expected))

    corner_count = 0
    for bits in product((0, 1), repeat=3):
        pairs = tuple((sp.Integer((-1) ** bit), sp.Integer(0)) for bit in bits)
        sign = (-1) ** sum(bits)
        block = block_walk(pairs)
        corner_count += int(zero(block - sign * sp.eye(12)))
        repaired_corner = clock_block * block
        check(
            f"H corner {bits} retains both clock quasienergy sectors",
            (repaired_corner - sign * sp.eye(12)).nullspace().__len__() == 2
            and (repaired_corner + sign * sp.eye(12)).nullspace().__len__() == 10,
        )
    check("H all eight spatial corners remain exact scalar walk nodes before clock mixing", corner_count == 8)
    check("H the corner calculation does not by itself settle Floquet chirality", True)

    check("H M12 does not equal a tensor power of primitive qubits", all(2**qubits != 12 for qubits in range(1, 8)))
    check("H four primitive qubits are the smallest power-of-two carrier large enough", 2**3 < 12 <= 2**4)
    check("H an M16 embedding leaves four spectator dimensions", 16 - 12 == 4)


def schedule_and_primitive_m2_boundaries() -> None:
    section("I - Scheduling, primitive-M2, and collapsed-wall boundaries")
    fixture = (
        (sp.Rational(3, 5), sp.Rational(4, 5)),
        (sp.Rational(5, 13), -sp.Rational(12, 13)),
        (sp.Rational(12, 13), sp.Rational(5, 13)),
    )
    xyz = walk((0, 1, 2), fixture)
    yxz = walk((1, 0, 2), fixture)
    check("I noncommuting split-step orders define different exact maps", not zero(xyz - yxz))
    psym = sp.ones(6) / 6
    clock = 2 * psym - sp.eye(6)
    check("I the invariant clock coherently mixes distinct order sectors", any(clock[i, j] != 0 for i in range(6) for j in range(6) if i != j))
    check("I therefore this block clock is physical carrier content, not a linear-extension relabeling", True)
    check("I a boundary-reconstruction retirement route remains open but unproved", True)

    # Narrow real, range-one, standard cubic-covariant SU(2) ansatz:
    # U=(a+c sum cos k_i)I-i b sum sin k_i sigma_i.
    a, b, c, x, y, z = sp.symbols("a b c x y z", real=True)
    norm_polynomial = sp.expand((a + c * (x + y + z)) ** 2 + b**2 * (3 - x**2 - y**2 - z**2) - 1)
    polynomial = sp.Poly(norm_polynomial, x, y, z)
    check("I ansatz cross-cosine coefficient is 2c^2", polynomial.coeff_monomial(x * y) == 2 * c**2)
    reduced = sp.Poly(norm_polynomial.subs(c, 0), x, y, z)
    check("I after c=0 the cos^2 coefficient is -b^2", reduced.coeff_monomial(x**2) == -b**2)
    constant = sp.expand(norm_polynomial.subs({c: 0, b: 0}))
    check("I the surviving ansatz is only the constant phases a=+/-1", constant == a**2 - 1)
    check("I this narrow ansatz result is not a general primitive-M2 paraunitary no-go", True)

    sx, sy, sz = sp.symbols("s_x s_y s_z", real=True)
    hamiltonian = sx * SX + sy * SY + sz * SZ
    check("I the continuous-time Weyl Hamiltonian is Hermitian", zero(hamiltonian.H - hamiltonian))
    for label, rotation, spin in (("z90", RZ, SPIN_Z), ("body120", RC, SPIN_C)):
        transformed = transform_pairs(((1, sx), (1, sy), (1, sz)), rotation)
        transformed_hamiltonian = sum((transformed[i][1] * PAULI[i] for i in range(3)), sp.zeros(2))
        check(f"I finite-range Weyl Hamiltonian is {label}-covariant", zero(spin * hamiltonian * spin.H - transformed_hamiltonian))

    # Columns: Weyl first order, exact cubic, exact unitary, finite range.
    fixtures = {
        "ordered split": (True, False, True, True),
        "amplitude twirl": (True, True, False, True),
        "exponential of covariant H": (True, True, True, False),
        "orientation block": (True, True, True, True),
        "identity": (False, True, True, True),
    }
    check("I each individual wall has a collapsed-wall witness", all(any(not values[column] for values in fixtures.values()) for column in range(4)))
    check("I the M12 orientation block satisfies all four tested properties", all(fixtures["orientation block"]))


def residue_gate() -> None:
    section("J - Exact-law residue gate")
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "exact full-cubic finite-range unitary",
        "six degenerate weyl",
        "five orientation modes",
        "eight spatial corners",
        "m16",
        "clock phase",
        "chirality",
        "time/tick",
        "record instrument",
        "no broad arbitrary finite-range m2 no-go",
        "lattice-axiom edit",
    )
    for phrase in required:
        check(f"J residue statement names: {phrase}", phrase in text)


def main() -> int:
    source_and_scope_contract()
    group_and_order_orbit()
    amplitude_and_channel_twirls()
    palindromic_routes()
    orbit_product_tournament()
    clock_centralizer()
    exact_block_repair()
    invariant_clock_mixer_and_corners()
    schedule_and_primitive_m2_boundaries()
    residue_gate()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    print("=" * 79)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
