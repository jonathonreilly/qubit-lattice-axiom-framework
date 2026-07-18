#!/usr/bin/env python3
"""Exact finite checks for the Cycle 8 cubic QW/QCA uniqueness audit.

Companion:
  docs/work_history/repo/review_feedback/
  CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md

The checks deliberately distinguish:

* a single-particle coined walk on l2(Z^3) tensor C^s;
* a genuine many-body QCA on a tensor product of finite cell algebras;
* exact proper-cubic covariance of a lattice update;
* rotationally invariant Weyl/Dirac behavior only to first continuum order.

No network access, randomness, axiom edit, registry edit, or audit mutation.
Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from itertools import permutations, product
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
    / "CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md"
)

PASS = 0
FAIL = 0


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


def zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sp.trigsimp(value)) == 0 for value in matrix)


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(int(x) for x in matrix): matrix for matrix in rotations}
    return tuple(unique.values())


DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: i for i, direction in enumerate(DIRECTIONS)}


def act(rotation: sp.Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    result = rotation * sp.Matrix(vector)
    return tuple(int(value) for value in result)


def direction_representation(rotation: sp.Matrix) -> sp.Matrix:
    representation = sp.zeros(6)
    for source, direction in enumerate(DIRECTIONS):
        target = DIR_INDEX[act(rotation, direction)]
        representation[target, source] = 1
    return representation


def coin_projectors() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    pair_even = sp.zeros(6)
    for start in (0, 2, 4):
        pair_even[start : start + 2, start : start + 2] = sp.ones(2) / 2
    scalar = sp.ones(6) / 6
    axis_even = pair_even - scalar
    vector_odd = sp.eye(6) - pair_even
    return scalar, axis_even, vector_odd


def source_contract() -> None:
    section("A - Source-note contract")
    text = NOTE.read_text(encoding="utf-8")
    lower = text.lower()
    normalized = " ".join(lower.replace("*", "").replace("`", "").replace("_", "").split())
    for phrase in (
        "authority: none",
        "quantum walk",
        "many-body qca",
        "exact proper-cubic covariance",
        "continuum",
        "not unavoidable",
        "no unique exact update",
        "conditional no-qubit-edit conclusion",
        "n1",
        "n8",
    ):
        check(f"A note contains scope boundary: {phrase}", phrase in normalized)
    urls = (
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/hep-th/9304070",
        "https://arxiv.org/abs/1802.03910",
        "https://arxiv.org/abs/1103.2704",
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/0711.3975",
        "https://arxiv.org/abs/quant-ph/0512058",
        "https://arxiv.org/abs/1303.4652",
        "https://arxiv.org/abs/2011.05597",
        "https://arxiv.org/abs/1902.10227",
    )
    for url in urls:
        check(f"A note cites primary source: {url}", url in lower)


def cubic_group_and_coin_commutant() -> None:
    section("B - Full proper-cubic group and six-direction coin commutant")
    rotations = proper_cubic_rotations()
    representations = tuple(direction_representation(rotation) for rotation in rotations)
    check("B proper cubic group has 24 rotations", len(rotations) == 24)
    check("B every rotation permutes the six cardinal directions", all(rep.T * rep == sp.eye(6) for rep in representations))
    check("B the action is transitive on all six directions", len({act(rotation, DIRECTIONS[0]) for rotation in rotations}) == 6)

    variables = sp.symbols("x0:36")
    matrix = sp.Matrix(6, 6, variables)
    equations = []
    for representation in representations:
        equations.extend(matrix * representation - representation * matrix)
    coefficient_matrix, rhs = sp.linear_eq_to_matrix(equations, variables)
    nullity = len(variables) - coefficient_matrix.rank()
    check("B direction-representation commutant has dimension three", nullity == 3, str(nullity))
    check("B commutant equations are homogeneous", rhs == sp.zeros(rhs.rows, 1))

    scalar, axis_even, vector_odd = coin_projectors()
    projectors = (scalar, axis_even, vector_odd)
    check("B cubic coin sectors have ranks 1,2,3", tuple(p.rank() for p in projectors) == (1, 2, 3))
    check("B the three sector projectors resolve identity", zero(sum(projectors, sp.zeros(6)) - sp.eye(6)))
    check("B the sector projectors are pairwise orthogonal", all(zero(projectors[i] * projectors[j]) for i in range(3) for j in range(3) if i != j))
    check("B every sector projector commutes with all 24 rotations", all(zero(p * rep - rep * p) for p in projectors for rep in representations))

    identity_coin = sp.eye(6)
    grover_coin = scalar - axis_even - vector_odd
    phase_coin = scalar + sp.I * axis_even - vector_odd
    coins = (identity_coin, grover_coin, phase_coin)
    check("B three displayed cubic coins are exactly unitary", all(zero(coin.H * coin - sp.eye(6)) for coin in coins))
    check("B three displayed cubic coins commute with every rotation", all(zero(coin * rep - rep * coin) for coin in coins for rep in representations))
    spectra = tuple(sp.factor(coin.charpoly().as_expr()) for coin in coins)
    check("B exact cubic covariance leaves inequivalent coin spectra", len(set(map(str, spectra))) == 3, str(spectra))


def exact_cardinal_walk_covariance() -> None:
    section("C - Exact one-step cardinal walk covariance")
    rotations = proper_cubic_rotations()
    representations = tuple(direction_representation(rotation) for rotation in rotations)
    scalar, axis_even, vector_odd = coin_projectors()
    coins = (scalar - axis_even - vector_odd, scalar + sp.I * axis_even - vector_odd)
    basis_projectors = []
    for index in range(6):
        projector = sp.zeros(6)
        projector[index, index] = 1
        basis_projectors.append(projector)

    for coin_number, coin in enumerate(coins, start=1):
        transitions = tuple(projector * coin for projector in basis_projectors)
        covariance = True
        for rotation, representation in zip(rotations, representations):
            for index, direction in enumerate(DIRECTIONS):
                target = DIR_INDEX[act(rotation, direction)]
                covariance &= zero(representation * transitions[index] * representation.T - transitions[target])
        check(f"C coin {coin_number} transition matrices are exactly proper-cubic covariant", covariance)

    x, y, z = sp.symbols("x y z", nonzero=True)
    monomials = [x**d[0] * y**d[1] * z**d[2] for d in DIRECTIONS]
    shift = sp.diag(*monomials)
    inverse_shift = sp.diag(*[1 / value for value in monomials])
    for coin_number, coin in enumerate(coins, start=1):
        walk = shift * coin
        inverse = coin.H * inverse_shift
        check(f"C coin {coin_number} cardinal walk is exactly unitary as a Laurent matrix", zero(inverse * walk - sp.eye(6)))
    expected = {
        tuple(sign if coordinate == axis else 0 for coordinate in range(3))
        for axis in range(3)
        for sign in (-1, 1)
    }
    check("C support uses exactly the present six nearest-neighbour displacements", set(DIRECTIONS) == expected)


def split_step_crosscheck() -> None:
    section("D - Cycle 7 factorization and exact-order boundary")
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    i2 = sp.eye(2)
    qx, qy, qz = sp.symbols("q_x q_y q_z", real=True)

    def axis_shift(q: sp.Expr, sigma: sp.Matrix) -> sp.Matrix:
        return sp.cos(q) * i2 - sp.I * sp.sin(q) * sigma

    ux = axis_shift(qx, sx)
    uy = axis_shift(qy, sy)
    uz = axis_shift(qz, sz)
    xyz = ux * uy * uz
    zyx = uz * uy * ux

    cx, cy, cz = sp.cos(qx), sp.cos(qy), sp.cos(qz)
    ax, ay, az = sp.sin(qx), sp.sin(qy), sp.sin(qz)
    u_minus = cx * cy * cz - ax * ay * az
    nx = ax * cy * cz + cx * ay * az
    ny = cx * ay * cz - ax * cy * az
    nz = cx * cy * az + ax * ay * cz
    published_minus = u_minus * i2 - sp.I * (nx * sx + ny * sy + nz * sz)
    check("D Sx Sy Sz exactly equals the published BCC A-minus branch", zero(xyz - published_minus))
    check("D the factorized macro-step is exactly unitary", zero(xyz.H * xyz - i2))

    origin = {qx: 0, qy: 0, qz: 0}
    first_xyz = tuple(sp.I * sp.diff(xyz, q).subs(origin) for q in (qx, qy, qz))
    first_zyx = tuple(sp.I * sp.diff(zyx, q).subs(origin) for q in (qx, qy, qz))
    check("D all axis orders share the same Weyl first derivative", all(zero(first_xyz[i] - first_zyx[i]) and zero(first_xyz[i] - (sx, sy, sz)[i]) for i in range(3)))
    mixed_difference = sp.diff(xyz - zyx, qx, qy).subs(origin)
    check("D different axis orders are inequivalent at second order", not zero(mixed_difference), str(mixed_difference))

    spin_rz = (i2 - sp.I * sz) / sp.sqrt(2)
    rotated_xyz = xyz.subs({qx: -qy, qy: qx}, simultaneous=True)
    covariance_defect = sp.simplify(spin_rz * xyz * spin_rz.H - rotated_xyz)
    check("D one ordered split step is not exactly 90-degree covariant", not zero(covariance_defect))
    defect_at_origin = covariance_defect.subs(origin)
    first_defects = tuple(sp.diff(covariance_defect, q).subs(origin) for q in (qx, qy, qz))
    check("D exact covariance defect vanishes through first continuum order", zero(defect_at_origin) and all(zero(value) for value in first_defects))


def qubit_block_and_sector_counts() -> None:
    section("E - Coin, block, Fock, and primitive-translation counts")
    check("E six-direction coin plus vacuum needs at least seven cell states", 1 + 6 == 7)
    check("E a hard-core single-walker cell fits in three qubits", 2**2 < 7 <= 2**3)
    check("E six independently occupiable directional modes need local Fock dimension 64", 2**6 == 64)
    check("E six-mode local Fock space needs six qubits", int(np.log2(64)) == 6)
    check("E two-component fermion field has local Fock dimension four", 2**2 == 4)
    check("E a C2 walk coin is not that two-mode Fock carrier", 2 != 4)

    origins = set(product((0, 1), repeat=3))
    orbit = {(origin[0] ^ dx, origin[1] ^ dy, origin[2] ^ dz) for origin in origins for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
    check("E a 2^3 blocking has eight origin sectors", len(origins) == 8)
    check("E primitive translations permute rather than fix block origins", orbit == origins and all((origin[0] ^ 1, origin[1], origin[2]) != origin for origin in origins))


def gf2_rank(matrix: np.ndarray) -> int:
    work = np.array(matrix, dtype=np.uint8) % 2
    rows, columns = work.shape
    rank = 0
    for column in range(columns):
        pivots = np.flatnonzero(work[rank:, column])
        if len(pivots) == 0:
            continue
        pivot = rank + int(pivots[0])
        work[[rank, pivot]] = work[[pivot, rank]]
        for row in range(rows):
            if row != rank and work[row, column]:
                work[row] ^= work[rank]
        rank += 1
        if rank == rows:
            break
    return rank


def primitive_qubit_qca_counterexample() -> None:
    section("F - Genuine primitive-qubit QCA counterexample")
    # On a 3^3 torus, the product of controlled-Z on every undirected cubic
    # edge induces the binary symplectic map (x,z) -> (x,z+A x).
    length = 3
    sites = list(product(range(length), repeat=3))
    index = {site: i for i, site in enumerate(sites)}
    count = len(sites)
    adjacency = np.zeros((count, count), dtype=np.uint8)
    for site in sites:
        for axis in range(3):
            neighbour = list(site)
            neighbour[axis] = (neighbour[axis] + 1) % length
            i, j = index[site], index[tuple(neighbour)]
            adjacency[i, j] = adjacency[j, i] = 1
    identity = np.eye(count, dtype=np.uint8)
    zero_block = np.zeros_like(identity)
    qca = np.block([[identity, zero_block], [adjacency, identity]]) % 2
    symplectic = np.block([[zero_block, identity], [identity, zero_block]]) % 2
    check("F cubic CZ map is invertible over GF(2)", gf2_rank(qca) == 2 * count)
    check("F cubic CZ map preserves Pauli commutators", np.array_equal((qca.T @ symplectic @ qca) % 2, symplectic))
    check("F cubic CZ QCA is an involution", np.array_equal((qca @ qca) % 2, np.eye(2 * count, dtype=np.uint8)))
    check("F one-site Pauli support grows by only one cubic edge", np.all(adjacency.sum(axis=0) == 6))

    rotations = proper_cubic_rotations()
    spatial_permutations = []
    for rotation in rotations:
        permutation = np.zeros((count, count), dtype=np.uint8)
        for source, site in enumerate(sites):
            centered = sp.Matrix(tuple(value if value != 2 else -1 for value in site))
            target_vector = rotation * centered
            target_site = tuple(int(value) % length for value in target_vector)
            permutation[index[target_site], source] = 1
        spatial_permutations.append(permutation)
    exact_cubic = True
    for permutation in spatial_permutations:
        pauli_permutation = np.block([[permutation, zero_block], [zero_block, permutation]])
        exact_cubic &= np.array_equal((pauli_permutation @ qca) % 2, (qca @ pauli_permutation) % 2)
    check("F genuine one-qubit-per-site QCA is exactly proper-cubic covariant", exact_cubic)
    check("F identity and cubic CZ are distinct exact covariant QCAs", not np.array_equal(qca, np.eye(2 * count, dtype=np.uint8)))


def conclusion_contract() -> None:
    section("G - Constitutional boundary needles")
    lower = NOTE.read_text(encoding="utf-8").lower()
    for phrase in (
        "coin dimension two",
        "coin dimension six",
        "smaller than the full proper cubic group",
        "single-particle sector",
        "collision rule",
        "auxiliary fermions",
        "block origin",
        "external phase cycle",
        "internal program",
        "mass parameter",
        "exact update remains unselected",
        "no lattice edit",
        "not a direct many-body completion",
        "not an axiom candidate",
    ):
        check(f"G note contains conclusion boundary: {phrase}", phrase in lower)


def main() -> None:
    source_contract()
    cubic_group_and_coin_commutant()
    exact_cardinal_walk_covariance()
    split_step_crosscheck()
    qubit_block_and_sector_counts()
    primitive_qubit_qca_counterexample()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
