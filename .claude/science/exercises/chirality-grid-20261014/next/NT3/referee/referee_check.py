"""Independent targeted ED checks for NT-3.

This implementation does not import the worker's ED code.  It constructs only
the symmetry blocks needed for the singlet ground state and the 6-vector pair
excitation, plus a full dominant-weight scan at L=4.  The largest matrix is
3552 x 3552 (L=6/cube ground block), so no L=7 solve is performed.
"""

from __future__ import annotations

import itertools
import math
from pathlib import Path

import numpy as np
import scipy.linalg as dense_la
import scipy.sparse as sparse
import scipy.sparse.linalg as sparse_la


NF = 4
LINES: list[str] = []


def emit(line: str = "") -> None:
    print(line, flush=True)
    LINES.append(line)


class FiniteMomenta:
    def __init__(self, labels, volume, add, neg, f, name):
        self.labels = tuple(labels)
        self.volume = volume
        self.add = add
        self.neg = neg
        self.f = dict(f)
        self.name = name
        self.M = len(self.labels)
        self.position = {k: j for j, k in enumerate(self.labels)}


def ring_problem(L: int, filter_name: str) -> FiniteMomenta:
    # Norms are independently recomputed by high-order periodic quadrature.
    grid = 2.0 * np.pi * np.arange(1 << 16) / (1 << 16)
    raw_functions = {
        "F_lo": lambda k: (1.0 - np.cos(k)) * (1.0 + 0.6 * np.cos(k)) / 2.0,
        "F_star": lambda k: (1.0 - np.cos(k)) / 2.0,
        "F_hi": lambda k: ((1.0 - np.cos(k)) / 2.0) ** 2,
    }
    if filter_name == "C1":
        f = {k: 1.0 for k in range(1, L)}
    else:
        fn = raw_functions[filter_name]
        norm = float(np.sqrt(np.mean(fn(grid) ** 2)))
        f = {k: float(fn(2.0 * np.pi * k / L) / norm) for k in range(1, L)}
    return FiniteMomenta(
        range(1, L), L, lambda a, b: (a + b) % L,
        lambda a: (-a) % L, f, f"{filter_name} L={L}",
    )


def cube_problem(filter_name: str) -> FiniteMomenta:
    # The exact continuum normalization is evaluated by a separate tensor grid.
    n = 128
    k = 2.0 * np.pi * np.arange(n) / n
    sx2 = np.sin(k / 2.0) ** 2
    cx2 = np.cos(k / 2.0) ** 2
    c = np.cos(k)
    if filter_name == "f_NN":
        # E[(1-cx-cy-cz)^2/4] = 5/8.
        norm = math.sqrt(5.0 / 8.0)

        def raw(bits):
            p = np.pi * np.array([(bits >> d) & 1 for d in range(3)])
            return (1.0 - np.cos(p).sum()) / 2.0
    else:
        total = 0.0
        for ix in range(n):
            t = (sx2[ix] * cx2[:, None] * cx2[None, :]
                 + cx2[ix] * sx2[:, None] * cx2[None, :]
                 + cx2[ix] * cx2[:, None] * sx2[None, :])
            total += float(np.sum((1.0 - t) ** 2))
        norm = math.sqrt(total / n**3)

        def raw(bits):
            p = np.pi * np.array([(bits >> d) & 1 for d in range(3)])
            s2 = np.sin(p / 2.0) ** 2
            c2 = np.cos(p / 2.0) ** 2
            return 1.0 - (s2[0] * c2[1] * c2[2]
                          + s2[1] * c2[0] * c2[2]
                          + s2[2] * c2[0] * c2[1])
    light = {1, 2, 4}
    labels = [x for x in range(8) if x not in light]
    f = {x: float(raw(x) / norm) for x in labels}
    return FiniteMomenta(labels, 8, lambda a, b: a ^ b, lambda a: a,
                         f, f"cube {filter_name}")


def add_many(problem: FiniteMomenta, labels) -> int:
    out = 0
    for label in labels:
        out = problem.add(out, label)
    return out


def subset_table(problem: FiniteMomenta):
    by_number_momentum = {}
    for number in range(problem.M + 1):
        for js in itertools.combinations(range(problem.M), number):
            momentum = add_many(problem, (problem.labels[j] for j in js))
            mask = sum(1 << j for j in js)
            by_number_momentum.setdefault((number, momentum), []).append(mask)
    return by_number_momentum


def sector_basis(problem: FiniteMomenta, differences, momentum=0) -> np.ndarray:
    subsets = subset_table(problem)
    states = []
    for shift in range(-min(differences), problem.M + 1):
        numbers = tuple(shift + d for d in differences)
        if any(n < 0 or n > problem.M for n in numbers):
            continue
        pools = []
        for flavour, number in enumerate(numbers):
            entries = []
            for (n, mom), masks in subsets.items():
                if n == number:
                    entries.extend((mask << (flavour * problem.M), mom) for mask in masks)
            pools.append(entries)
        for choices in itertools.product(*pools):
            if add_many(problem, (choice[1] for choice in choices)) == momentum:
                states.append(sum(choice[0] for choice in choices))
    return np.array(sorted(states), dtype=np.int64)


def fermion_step(state: int, orbital: int, create: bool):
    occupied = (state >> orbital) & 1
    if occupied == create:
        return None
    sign = -1.0 if ((state & ((1 << orbital) - 1)).bit_count() & 1) else 1.0
    return state ^ (1 << orbital), sign


def apply_ops(state: int, operations):
    sign = 1.0
    for orbital, create in operations:
        result = fermion_step(state, orbital, create)
        if result is None:
            return None
        state, local_sign = result
        sign *= local_sign
    return state, sign


def orbital(problem: FiniteMomenta, flavour: int, j: int) -> int:
    return flavour * problem.M + j


def hamiltonian(problem: FiniteMomenta, basis: np.ndarray) -> sparse.csr_matrix:
    index = {int(state): i for i, state in enumerate(basis)}
    rows, cols, values = [], [], []
    for source_col, raw_state in enumerate(basis):
        state = int(raw_state)
        for j0, j1, j2 in itertools.product(range(problem.M), repeat=3):
            partial = add_many(problem, (problem.labels[j0], problem.labels[j1], problem.labels[j2]))
            fourth_label = problem.neg(partial)
            j3 = problem.position.get(fourth_label)
            if j3 is None:
                continue
            operations = [(orbital(problem, 3, j3), False),
                          (orbital(problem, 2, j2), False),
                          (orbital(problem, 1, j1), False),
                          (orbital(problem, 0, j0), False)]
            result = apply_ops(state, operations)
            if result is None:
                continue
            target_state, sign = result
            target_row = index.get(target_state)
            if target_row is None:
                continue
            coefficient = -(problem.f[problem.labels[j0]]
                            * problem.f[problem.labels[j1]]
                            * problem.f[problem.labels[j2]]
                            * problem.f[problem.labels[j3]]) / problem.volume
            rows.extend((target_row, source_col))
            cols.extend((source_col, target_row))
            values.extend((coefficient * sign, coefficient * sign))
    return sparse.coo_matrix((values, (rows, cols)),
                             shape=(len(basis), len(basis))).tocsr()


def lowest(matrix, count=2):
    n = matrix.shape[0]
    if n <= 600:
        values, vectors = dense_la.eigh(matrix.toarray(), subset_by_index=(0, min(count, n) - 1))
    else:
        start = np.ones(n) / math.sqrt(n)
        values, vectors = sparse_la.eigsh(matrix, k=min(count, n - 2), which="SA",
                                          tol=2e-13, ncv=24, v0=start)
        order = np.argsort(values)
        values, vectors = values[order], vectors[:, order]
    return values, vectors


def apply_sum(problem, source_basis, source_vector, target_basis, terms):
    target_index = {int(state): i for i, state in enumerate(target_basis)}
    out = np.zeros(len(target_basis))
    for source_i, raw_state in enumerate(source_basis):
        amplitude = source_vector[source_i]
        if amplitude == 0.0:
            continue
        for coefficient, operations in terms:
            result = apply_ops(int(raw_state), operations)
            if result is None:
                continue
            target_state, sign = result
            target_i = target_index.get(target_state)
            if target_i is not None:
                out[target_i] += coefficient * sign * amplitude
    return out


def occupations(problem, basis, vector):
    weights = vector * vector
    return np.array([
        sum(float(np.dot(weights, ((basis >> orbital(problem, a, j)) & 1)))
            for a in range(NF))
        for j in range(problem.M)
    ])


def analyze_target(problem: FiniteMomenta):
    ground_basis = sector_basis(problem, (0, 0, 0, 0), 0)
    six_basis = sector_basis(problem, (1, 1, 0, 0), 0)
    e0, v0 = lowest(hamiltonian(problem, ground_basis), 2)
    e6, v6 = lowest(hamiltonian(problem, six_basis), 2)
    ground, six = v0[:, 0], v6[:, 0]

    # SU(4) raising generators sum_k c_a^dag(k)c_{a+1}(k).
    raising_norms = []
    for a in range(3):
        differences = [0, 0, 0, 0]
        differences[a] += 1
        differences[a + 1] -= 1
        target = sector_basis(problem, tuple(differences), 0)
        terms = []
        for j in range(problem.M):
            terms.append((1.0, [(orbital(problem, a + 1, j), False),
                                (orbital(problem, a, j), True)]))
        raising_norms.append(float(np.linalg.norm(
            apply_sum(problem, ground_basis, ground, target, terms))))

    # Pair structure factors and resolved pair weights at q=0.
    minus_six_basis = sector_basis(problem, (-1, -1, 0, 0), 0)
    structure = {}
    for label, filtered in (("M", False), ("S", True)):
        annihilation_terms, creation_terms = [], []
        for j, momentum in enumerate(problem.labels):
            opposite = problem.neg(momentum)
            j2 = problem.position[opposite]
            coefficient = problem.f[momentum] * problem.f[opposite] if filtered else 1.0
            annihilation_terms.append((coefficient,
                [(orbital(problem, 1, j2), False), (orbital(problem, 0, j), False)]))
            creation_terms.append((coefficient,
                [(orbital(problem, 0, j), True), (orbital(problem, 1, j2), True)]))
        p = apply_sum(problem, ground_basis, ground, minus_six_basis, annihilation_terms)
        pd = apply_sum(problem, ground_basis, ground, six_basis, creation_terms)
        structure[label] = (6.0 / problem.volume * float(p @ p),
                            6.0 / problem.volume * float(pd @ pd))

    resolved = {}
    for j, momentum in enumerate(problem.labels):
        j2 = problem.position[problem.neg(momentum)]
        term = [(1.0, [(orbital(problem, 0, j), True),
                       (orbital(problem, 1, j2), True)])]
        pair = apply_sum(problem, ground_basis, ground, six_basis, term)
        resolved[momentum] = float(np.dot(six, pair) ** 2)
    total = sum(resolved.values())
    normalized_resolved = {k: value / total for k, value in resolved.items()}

    ground_occ = occupations(problem, ground_basis, ground)
    six_occ = occupations(problem, six_basis, six)
    return {
        "E0": float(e0[0]),
        "gap6": float(e6[0] - e0[0]),
        "ground_basis_size": len(ground_basis),
        "six_basis_size": len(six_basis),
        "raising_norm": max(raising_norms),
        "structure": structure,
        "pair_weights": normalized_resolved,
        "occupation_difference": six_occ - ground_occ,
    }


def full_scan_l4(problem: FiniteMomenta):
    records = []
    for d0 in range(problem.M + 1):
        for d1 in range(d0 + 1):
            for d2 in range(d1 + 1):
                d = (d0, d1, d2, 0)
                for momentum in range(problem.volume):
                    basis = sector_basis(problem, d, momentum)
                    if len(basis) == 0:
                        continue
                    values, _ = lowest(hamiltonian(problem, basis), 2)
                    for level, energy in enumerate(values):
                        records.append((float(energy), d, momentum, level))
    records.sort()
    e0 = records[0][0]
    degeneracy = sum(abs(row[0] - e0) < 1e-9 for row in records)
    gap_row = next(row for row in records if row[0] > e0 + 1e-9)
    return e0, degeneracy, gap_row[0] - e0, gap_row[1:]


def main():
    emit("Independent NT-3 targeted ED (no imports from scripts/)")
    emit("All solves: L<=6; largest symmetry block 3552; no L=7 solve")
    emit()
    for filter_name in ("C1", "F_lo", "F_star", "F_hi"):
        for L in (4, 5, 6):
            problem = ring_problem(L, filter_name)
            result = analyze_target(problem)
            weights = result["pair_weights"]
            near = weights.get(1, 0.0) + weights.get(L - 1, 0.0)
            max_dn = float(np.max(np.abs(result["occupation_difference"])))
            sS, sdS = result["structure"]["S"]
            sM, sdM = result["structure"]["M"]
            emit(f"{filter_name} L={L}: E0/L={result['E0']/L:.8f}; "
                 f"gap6={result['gap6']:.9f}; raise={result['raising_norm']:.2e}; "
                 f"S6S={sS:.6f}/{sdS:.6f}; S6M={sM:.6f}/{sdM:.6f}; "
                 f"near_pair={near:.6f}; max|Delta n|={max_dn:.2e}; "
                 f"dims={result['ground_basis_size']}/{result['six_basis_size']}")
            if L in (5, 6):
                rounded = {k: round(v, 6) for k, v in weights.items()}
                emit(f"  pair weights: {rounded}")
        scan = full_scan_l4(ring_problem(4, filter_name))
        emit(f"{filter_name} L=4 full scan: E0={scan[0]:.9f}; D={scan[1]}; "
             f"global_gap={scan[2]:.9f}; lowest_label={scan[3]}")
        emit()

    for filter_name in ("f_NN", "f_F1"):
        problem = cube_problem(filter_name)
        result = analyze_target(problem)
        sS, sdS = result["structure"]["S"]
        sM, sdM = result["structure"]["M"]
        emit(f"cube {filter_name}: E0/8={result['E0']/8:.8f}; "
             f"gap6={result['gap6']:.9f}; raise={result['raising_norm']:.2e}; "
             f"S6S={sS:.6f}/{sdS:.6f}; S6M={sM:.6f}/{sdM:.6f}; "
             f"dims={result['ground_basis_size']}/{result['six_basis_size']}")

    Path("REFEREE_CHECK.out").write_text("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
