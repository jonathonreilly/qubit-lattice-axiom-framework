"""Independent adversarial checks for the G0c referee report.

This file deliberately does not reuse Stab.reduce for the group-law test.
It extracts the diagonal stabilizer constraints by independent GF(2) row
reduction, describes the entire computational-basis support of the code as an
affine space, and tests each quadratic composition phase on that full affine
space (not on random points from one gauge orbit).
"""

from itertools import combinations

import numpy as np
import networkx as nx

from ckcore import (
    ROTS,
    Omega,
    Stab,
    Torus,
    build,
    build_stabilizer,
    mmul,
    pcomm,
    pmul,
)
from turns import depth_of_cz, make_turn, perm_config, qval


def gf2_kernel(vectors):
    """Return a basis of dependencies among integer bit-vectors."""
    pivots = {}
    deps = []
    for i, value in enumerate(vectors):
        row = value
        combo = 1 << i
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (row, combo)
                break
            prow, pcombo = pivots[pivot]
            row ^= prow
            combo ^= pcombo
        if not row:
            deps.append(combo)
    return deps


def diagonal_constraints(stabilizers):
    """Obtain all independent Z-only stabilizers (z, rhs) from generators."""
    constraints = []
    for combo in gf2_kernel([p[0] for p in stabilizers]):
        product = (0, 0, 0)
        for i, generator in enumerate(stabilizers):
            if combo >> i & 1:
                product = pmul(product, generator)
        x, z, phase = product
        assert x == 0 and phase in (0, 2)
        constraints.append((z, phase // 2))
    return constraints


def affine_solutions(equations, nbits):
    """Return one solution and a basis of the homogeneous solution space."""
    rows = [[z, rhs] for z, rhs in equations]
    pivot_rows = {}
    for z, rhs in rows:
        while z:
            pivot = z.bit_length() - 1
            if pivot not in pivot_rows:
                pivot_rows[pivot] = [z, rhs]
                break
            pz, prhs = pivot_rows[pivot]
            z ^= pz
            rhs ^= prhs
        assert z or rhs == 0, "inconsistent diagonal stabilizer sector"

    particular = 0
    for pivot in sorted(pivot_rows):
        z, rhs = pivot_rows[pivot]
        # Rows are upper-triangular with their highest bit as pivot, so all
        # lower variables have already been assigned in this ascending pass.
        value = rhs ^ ((z & particular).bit_count() & 1)
        if value:
            particular |= 1 << pivot

    free = [b for b in range(nbits) if b not in pivot_rows]
    null_basis = []
    for bit in free:
        vector = 1 << bit
        for pivot in sorted(pivot_rows):
            z, _ = pivot_rows[pivot]
            if (z & vector).bit_count() & 1:
                vector |= 1 << pivot
        null_basis.append(vector)

    def valid(y):
        return all(((z & y).bit_count() & 1) == rhs for z, rhs in equations)

    assert valid(particular)
    assert all(all(((z & v).bit_count() & 1) == 0 for z, _ in equations)
               for v in null_basis)
    return particular, null_basis


def composition_phase(g, h, gh, y):
    hy = perm_config(h.fmap, y)
    ghy = perm_config(g.fmap, hy)
    return qval(h, hy) ^ qval(g, ghy) ^ qval(gh, ghy)


def quadratic_constant_on_affine(func, origin, basis):
    """Exactly test a degree-at-most-two GF(2) function on an affine space."""
    f0 = func(origin)
    singles = [func(origin ^ v) for v in basis]
    if any(value != f0 for value in singles):
        return False, f0, "linear"
    for i, j in combinations(range(len(basis)), 2):
        second = func(origin ^ basis[i] ^ basis[j]) ^ singles[i] ^ singles[j] ^ f0
        if second:
            return False, f0, "quadratic"
    return True, f0, None


def check_group_law(L, center, out_order=(0, 1, 2), in_order=(0, 1, 2)):
    T = Torus(L, out_order, in_order)
    data = build(T)
    stab, _, _ = build_stabilizer(T, data)
    omega = Omega(T, data)
    turns = [make_turn(T, data, stab, omega, M, center) for M in ROTS]
    origin, support_basis = affine_solutions(diagonal_constraints(stab.gens), T.nq)
    index = {tuple(map(tuple, M.tolist())): i for i, M in enumerate(ROTS)}

    failures = []
    signs = {}
    for i, g in enumerate(turns):
        for j, h in enumerate(turns):
            k = index[tuple(map(tuple, (ROTS[i] @ ROTS[j]).tolist()))]
            gh = turns[k]
            ok, sign, defect = quadratic_constant_on_affine(
                lambda y: composition_phase(g, h, gh, y), origin, support_basis
            )
            signs[sign] = signs.get(sign, 0) + 1
            if not ok or sign:
                failures.append((i, j, k, sign, defect))
    print(
        f"L={L} frame={out_order}/{in_order} center={center}: exact full-support group law; "
        f"diagonal constraints={len(diagonal_constraints(stab.gens))}, "
        f"support affine dimension={len(support_basis)}, failures={len(failures)}, signs={signs}"
    )
    if failures:
        print("  first failures:", failures[:10])

    # Independently validate that the reported greedy layers really are a
    # bounded-depth schedule: their edge count and maximum degree are useful
    # diagnostics, while depth_of_cz itself supplies the explicit coloring.
    stats = []
    for tr in turns:
        degree = max(a.bit_count() for a in tr.A)
        depth, edges = depth_of_cz(tr)
        stats.append((depth, degree, edges))
    print(
        f"  CZ schedule: max greedy depth={max(s[0] for s in stats)}, "
        f"max graph degree={max(s[1] for s in stats)}, max edges={max(s[2] for s in stats)}"
    )


def pauli_dense(nqubits, pauli):
    x, z, phase = pauli
    one = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.diag([1, -1]).astype(complex)
    out = np.array([[1]], dtype=complex)
    for bit in range(nqubits):
        local = np.linalg.matrix_power(X, x >> bit & 1) @ np.linalg.matrix_power(Z, z >> bit & 1)
        out = np.kron(out, local if local.shape == (2, 2) else one)
    return (1j ** phase) * out


def majorana_dense(nmodes, mono):
    mask, phase = mono
    one = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.diag([1, -1]).astype(complex)
    generators = []
    for mode in range(nmodes):
        for endpoint in (X, Y):
            factors = [Z] * mode + [endpoint] + [one] * (nmodes - mode - 1)
            matrix = factors[0]
            for factor in factors[1:]:
                matrix = np.kron(matrix, factor)
            generators.append(matrix)
    out = (1j ** phase) * np.eye(2 ** nmodes, dtype=complex)
    for bit, generator in enumerate(generators):
        if mask >> bit & 1:
            out = out @ generator
    return out


def check_multiplication_conventions():
    pauli_bad = 0
    paulis = [(x, z, p) for x in range(4) for z in range(4) for p in range(4)]
    for left in paulis:
        for right in paulis:
            got = pauli_dense(2, pmul(left, right))
            want = pauli_dense(2, left) @ pauli_dense(2, right)
            pauli_bad += not np.allclose(got, want)

    majorana_bad = 0
    monos = [(m, p) for m in range(16) for p in range(4)]
    for left in monos:
        for right in monos:
            got = majorana_dense(2, mmul(left, right))
            want = majorana_dense(2, left) @ majorana_dense(2, right)
            majorana_bad += not np.allclose(got, want)
    print(f"dense convention checks: pmul failures={pauli_bad}, mmul failures={majorana_bad}")


def check_stabilizer_reduction():
    # Six graph-state generators are independent, Hermitian, and commuting.
    nqubits = 6
    adjacency = [0] * nqubits
    for a, b in ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3)):
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    generators = [(1 << q, adjacency[q], 0) for q in range(nqubits)]
    assert all(pcomm(a, b) == 0 for a, b in combinations(generators, 2))
    stab = Stab(nqubits)
    for generator in generators:
        assert stab.add(generator) == "new"

    group = []
    for combo in range(1 << len(generators)):
        product = (0, 0, 0)
        for i, generator in enumerate(generators):
            if combo >> i & 1:
                product = pmul(product, generator)
        group.append(product)

    bad_member = sum(stab.reduce(element) != (0, 0, 0) for element in group)
    bad_negative = sum(stab.reduce((x, z, (p + 2) % 4)) != (0, 0, 2) for x, z, p in group)
    bad_coset = 0
    for x in range(1 << nqubits):
        for z in range(1 << nqubits):
            probe = (x, z, 0)
            if all(pcomm(probe, generator) == 0 for generator in generators):
                normal = stab.reduce(probe)
                for element in group:
                    bad_coset += stab.reduce(pmul(probe, element)) != normal
    print(
        f"Stab.reduce exhaustive graph-code check: member failures={bad_member}, "
        f"negative-phase failures={bad_negative}, centralizer-coset failures={bad_coset}"
    )


def check_omega():
    T = Torus(3)
    data = build(T)
    omega = Omega(T, data)
    q = 0
    left, right = T.ends(q)
    fermion_generators = [T.S_mono(q), T.P_mono(left), T.P_mono(right)]
    boson_generators = [T.U_pauli(q), T.W_pauli(left), T.W_pauli(right)]
    span = {}
    for combo in range(8):
        fermion = (0, 0)
        boson = (0, 0, 0)
        for i in range(3):
            if combo >> i & 1:
                fermion = mmul(fermion, fermion_generators[i])
                boson = pmul(boson, boson_generators[i])
        span[fermion[0]] = (fermion[1], boson)

    local_bits = [2 * left, 2 * left + 1, 2 * right, 2 * right + 1]
    failures = 0
    cases = 0
    for subset in range(16):
        if subset.bit_count() & 1:
            continue
        mask = sum(1 << local_bits[i] for i in range(4) if subset >> i & 1)
        for phase in range(4):
            base_phase, boson = span[mask]
            expected = (boson[0], boson[1], (boson[2] + phase - base_phase) % 4)
            failures += omega((mask, phase)) != expected
            cases += 1
    print(f"Omega exhaustive adjacent-pair check: failures={failures}/{cases}")


def cup1_pair(T, f, g):
    total = 0
    for cube in range(T.N):
        outward, inward = T.faces_of_cube(cube)
        for face_class, order in ((outward, T.out_order), (inward, T.in_order)):
            sequence = [face_class[axis] for axis in order]
            if f in sequence and g in sequence and sequence.index(f) < sequence.index(g):
                total ^= 1
    return total


def check_ck30_phase(out_order=(0, 1, 2), in_order=(0, 1, 2)):
    T = Torus(3, out_order, in_order)
    data = build(T)
    stab, _, _ = build_stabilizer(T, data)
    plus = minus = other = 0
    for vertex in range(T.N):
        coordinate = T.ccoord(vertex)
        for direction in range(3):
            a, b = [axis for axis in range(3) if axis != direction]

            def shift(da, db):
                out = list(coordinate)
                out[a] -= da
                out[b] -= db
                return tuple(out)

            corner = shift(1, 1)
            corner_a = list(corner)
            corner_a[a] += 1
            corner_b = list(corner)
            corner_b[b] += 1
            faces = [
                T.qf(corner, a),
                T.qf(corner, b),
                T.qf(tuple(corner_a), b),
                T.qf(tuple(corner_b), a),
            ]
            xpart = sum(1 << face for face in faces)
            zpart = 0
            for candidate in range(T.nq):
                if sum(cup1_pair(T, face, candidate) for face in faces) & 1:
                    zpart |= 1 << candidate
            plus_ok = stab.contains((xpart, zpart, 0))[0]
            minus_ok = stab.contains((xpart, zpart, 2))[0]
            plus += plus_ok
            minus += minus_ok
            other += not (plus_ok or minus_ok)
    print(
        f"CK Eq.(30) sign check on L=3 frame={out_order}/{in_order}: "
        f"+G in S {plus}/81, -G in S {minus}/81, neither={other}"
    )


def check_depth_coloring(L, out_order, in_order):
    """Produce and validate a better explicit CZ edge coloring than first-fit."""
    T = Torus(L, out_order, in_order)
    data = build(T)
    stab, _, _ = build_stabilizer(T, data)
    omega = Omega(T, data)
    for center in ("cube", "vertex"):
        depths = []
        for matrix in ROTS:
            turn = make_turn(T, data, stab, omega, matrix, center)
            graph = nx.Graph()
            for a, partners in enumerate(turn.A):
                rest = partners
                while rest:
                    low = rest & -rest
                    b = low.bit_length() - 1
                    rest ^= low
                    if a < b:
                        graph.add_edge(a, b)
            if not graph.edges:
                depths.append(0)
                continue
            coloring = nx.coloring.greedy_color(
                nx.line_graph(graph), strategy="saturation_largest_first"
            )
            color_by_edge = {frozenset(edge): color for edge, color in coloring.items()}
            for vertex in graph:
                incident = [color_by_edge[frozenset(edge)] for edge in graph.edges(vertex)]
                assert len(incident) == len(set(incident))
            depths.append(max(coloring.values()) + 1)
        print(
            f"L={L} frame={out_order}/{in_order} center={center}: "
            f"validated DSATUR CZ depths={sorted(set(depths))}, max={max(depths)}"
        )


def check_spin_structures():
    """Action of the 24 signed permutation matrices on H^1(T^3,Z2)."""
    fixed_by_all = []
    orbit_data = []
    for spin in range(8):
        bits = [(spin >> i) & 1 for i in range(3)]
        orbit = set()
        stabilizer = 0
        for M in ROTS:
            image = tuple(sum((int(M[i, j]) & 1) * bits[j] for j in range(3)) & 1
                          for i in range(3))
            orbit.add(image)
            stabilizer += image == tuple(bits)
        if stabilizer == 24:
            fixed_by_all.append(tuple(bits))
        orbit_data.append((tuple(bits), len(orbit), stabilizer))
    print("spin structures (bits 0=P, 1=A by convention):")
    for item in orbit_data:
        print(" ", item)
    print("fixed by all 24 proper cubic turns:", fixed_by_all)


if __name__ == "__main__":
    check_multiplication_conventions()
    check_stabilizer_reduction()
    check_omega()
    check_ck30_phase()
    check_ck30_phase((2, 1, 0), (0, 1, 2))
    for size in (3, 4):
        for rotation_center in ("cube", "vertex"):
            check_group_law(size, rotation_center)
    # Fig. 5/A10 has opposite orders for the positive- and negative-axis
    # face triples (up to a common axis relabeling); this representative is
    # out=(U,F,R) and in=(L,B,D).
    for size in (3, 4):
        for rotation_center in ("cube", "vertex"):
            check_group_law(size, rotation_center, (2, 1, 0), (0, 1, 2))
    check_depth_coloring(4, (2, 1, 0), (0, 1, 2))
    check_spin_structures()
