#!/usr/bin/env python3
"""Finite controls for supplied local quantum collisions and rapid mixing.

Standard library only; no repository reads, external data, native physical
identification, or general-theorem verification by finite sampling.
The companion note proves the all-N conditional statements.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, permutations, product
from math import cos, exp, factorial, prod, sin, sqrt
import sys

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/LOCAL_QUANTUM_COLLISIONS_AND_RAPID_MIXING_BOUNDED_THEOREM_NOTE_2026-10-09.md",
    "docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md",
]


def network():
    velocities = list(product((-1, 0, 1), repeat=3))
    classes = defaultdict(list)
    for a, b in combinations_with_replacement(range(27), 2):
        key = tuple(velocities[a][d] + velocities[b][d] for d in range(3))
        key += (sum(x*x for x in velocities[a] + velocities[b]),)
        classes[key].append((a, b))
    reactions = [tuple(sorted((a, b))) for c in classes.values() for a, b in combinations(c, 2)]
    assert len(reactions) == 288 and all(len(set(a+b)) == 4 for a, b in reactions)
    index = {v: i for i, v in enumerate(velocities)}
    rotations = []
    for p in permutations(range(3)):
        parity = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0]*signs[1]*signs[2] == 1:
                rotations.append([index[tuple(signs[d]*v[p[d]] for d in range(3))] for v in velocities])
    remaining = set(reactions)
    sizes = []
    while remaining:
        a, b = next(iter(remaining))
        orbit = {tuple(sorted((tuple(sorted(R[i] for i in a)), tuple(sorted(R[i] for i in b))))) for R in rotations}
        assert orbit <= set(reactions)
        remaining -= orbit
        sizes.append(len(orbit))
    print('D3Q27: velocities=27 pair_complexes=378 reactions=288 four_distinct_species=True')
    print(f'proper_cubic_collision_orbits={len(sizes)} orbit_sizes={sorted(sizes)}')


def exact_fiber_averages():
    cases = 0
    assignments = 0
    for N in range(2, 7):
        graphs = [tuple((a, a+1) for a in range(N-1))]
        if N == 4:
            graphs.append(((0, 1), (1, 2), (2, 3), (3, 0)))
        for edges in graphs:
            rows = defaultdict(lambda: [0, 0, 0])
            for z in product(range(4), repeat=N):
                n = tuple(z.count(a) for a in range(4))
                rows[n][0] += 1
                rows[n][1] += sum({z[a], z[b]} == {0, 1} for a, b in edges)
                rows[n][2] += sum({z[a], z[b]} == {2, 3} for a, b in edges)
                assignments += 1
            lam = Q(N-1, 2*len(edges))  # two separately marked swaps, each gamma=lam/2
            for n, (multiplicity, active_fwd, active_rev) in rows.items():
                assert multiplicity == factorial(N) // prod(factorial(k) for k in n)
                assert lam * Q(active_fwd, multiplicity) == Q(n[0]*n[1], N)
                assert lam * Q(active_rev, multiplicity) == Q(n[2]*n[3], N)
                if n[0] and n[1]:
                    m = (n[0]-1, n[1]-1, n[2]+1, n[3]+1)
                    multiplicity_m = factorial(N) // prod(factorial(k) for k in m)
                    assert multiplicity * n[0]*n[1] == multiplicity_m * m[2]*m[3]
                cases += 1
    print(f'exact_fiber_averages: N=2..6 fibers={cases} assignments={assignments}; rates_and_factorials=True')


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def adj(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def local_unitary_check():
    theta = 0.37
    # system states s,t,outside times the actual one-qubit environment
    U = [[complex(i == j) for j in range(6)] for i in range(6)]
    for s in (0, 1):
        for a in (0, 1):
            U[2*s+a][2*s+a] = cos(theta)
            U[2*(1-s)+(1-a)][2*s+a] = -1j*sin(theta)
    UU = matmul(adj(U), U)
    err = max(abs(UU[i][j] - (i == j)) for i in range(6) for j in range(6))
    for i in range(3):
        for j in range(3):
            rho = [[0j]*6 for _ in range(6)]
            rho[2*i][2*j] = 1
            out = matmul(matmul(U, rho), adj(U))
            population = [out[2*k][2*k] + out[2*k+1][2*k+1] for k in range(3)]
            expected = [0.0]*3
            if i == j:
                if i == 2:
                    expected[2] = 1
                else:
                    expected[i] = cos(theta)**2
                    expected[1-i] = sin(theta)**2
            err = max(err, max(abs(x-y) for x, y in zip(population, expected)))
    assert err < 2e-15
    print(f'local_6x6_unitary_and_all_9_matrix_units: max_residual={err:.3g}')


def local_generator(states, edges, epsilon):
    N = len(states[0])
    index = {s: i for i, s in enumerate(states)}
    gamma = (N-1)/(4*len(edges))
    rows = []
    for s in states:
        row = defaultdict(float)
        for a, b in edges:
            z = list(s)
            z[a], z[b] = z[b], z[a]
            if tuple(z) != s:
                row[index[tuple(z)]] += 1/epsilon
            pair = {s[a], s[b]}
            targets = ((2, 3), (3, 2)) if pair == {0, 1} else (((0, 1), (1, 0)) if pair == {2, 3} else ())
            for u, v in targets:
                z = list(s)
                z[a], z[b] = u, v
                row[index[tuple(z)]] += gamma
        rows.append(dict(row))
    return rows


def uniformize(rows, start, t):
    n = len(rows)
    rate = max(sum(row.values()) for row in rows)
    if rate == 0:
        return [float(i == start) for i in range(n)], 0
    exits = [sum(row.values()) for row in rows]
    weight = exp(-rate*t)
    vector = [float(i == start) for i in range(n)]
    ans = [weight*x for x in vector]
    mass = weight
    k = 0
    while True:
        k += 1
        nxt = [vector[i]*(1-exits[i]/rate) for i in range(n)]
        for i, row in enumerate(rows):
            for j, r in row.items():
                nxt[j] += vector[i]*r/rate
        vector = nxt
        weight *= rate*t/k
        mass += weight
        for i in range(n):
            ans[i] += weight*vector[i]
        # Poisson series after its mode; bounded geometric tail.
        ratio = rate*t/(k+1)
        if ratio < 1 and weight*ratio/(1-ratio) < 1e-15:
            break
        assert k < 2000
    assert abs(sum(ans)-mass) < 1e-12 and abs(mass-1) < 1e-12
    return ans, k


def averaging_limit_check():
    classes = ((2, 2, 0, 0), (1, 1, 1, 1), (0, 0, 2, 2))
    states = [s for s in product(range(4), repeat=4) if tuple(s.count(a) for a in range(4)) in classes]
    assert len(states) == 36
    edges = ((0, 1), (1, 2), (2, 3))
    start = states.index((0, 0, 1, 1))
    target = [1/6+exp(-1)/2+exp(-1.5)/3, 2/3-2*exp(-1.5)/3, 1/6-exp(-1)/2+exp(-1.5)/3]
    target_rows = [{1: 1.0}, {0: 0.25, 2: 0.25}, {1: 1.0}]
    independent, _ = uniformize(target_rows, 0, 1)
    assert max(abs(a-b) for a, b in zip(target, independent)) < 2e-15
    errors = []
    print('rapid_local_mixing: N=4 path, 36_microstates, t=1, initial=(0,0,1,1)')
    print('target_occupation_probabilities=' + ','.join(f'{p:.12f}' for p in target))
    for denominator in (1, 4, 16, 64, 128):
        eps = 1/denominator
        p, steps = uniformize(local_generator(states, edges, eps), start, 1)
        coarse = [0.0]*3
        for s, w in zip(states, p):
            coarse[classes.index(tuple(s.count(a) for a in range(4)))] += w
        tv = sum(abs(a-b) for a, b in zip(coarse, target))/2
        errors.append(tv)
        print(f'  epsilon=1/{denominator:<3} TV_error={tv:.9g} series_terms={steps}')
    assert all(b < a for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 0.002
    assert 1.5 < errors[-2]/errors[-1] < 2.5
    rows = local_generator(states, edges, 1.0)
    rates = []
    for s in ((0, 0, 1, 1), (0, 1, 0, 1)):
        rates.append(sum(r for j, r in rows[states.index(s)].items() if states[j].count(0) == 1))
    assert rates == [0.5, 1.5]
    print(f'finite_mixing_example: same_counts=(2,2,0,0) clustered_and_alternating_rates={rates} target_rate=1')


def main():
    passed = failed = 0
    for label, function in (
        ('network_and_cubic_orbits', network),
        ('exact_fiber_averages_and_stationary_weights', exact_fiber_averages),
        ('local_unitary_and_coherence_matrix_units', local_unitary_check),
        ('finite_mixing_and_averaging_example', averaging_limit_check),
    ):
        try:
            function()
        except Exception as error:
            failed += 1
            print(f'FAIL {label}: {type(error).__name__}: {error}', flush=True)
        else:
            passed += 1
            print(f'PASS {label}', flush=True)
    print('per_element: all 288 D3Q27 reversible reaction supports and 24 proper-cubic rotations are enumerated')
    print('per_site: an actual system-plus-qubit unitary and every system matrix unit test local population closure')
    print('per_mode: all four-label occupation fibers on paths N=2 through N=6 and an N=4 square use exact rational rates')
    print('per_block: a 36-state local population chain tests finite mixing, exact macro rates and rapid-mixing convergence')
    print('lattice_wide: checked and not executed — no infinite lattice, native M2 realization, streaming or uniform-N limit is simulated')
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return int(failed != 0)


if __name__ == '__main__':
    sys.exit(main())
