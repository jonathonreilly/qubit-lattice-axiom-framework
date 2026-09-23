"""Finite challenges of the phase-preserving forest construction.

Builds cubical cochains numerically without the earlier projector helper.
Compares connected partition inversion with ordered-sector BKAR quadrature,
including overlapping components. This is author verification, not an
independent review, interval quadrature, or an all-order convergence test.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/forest_interpolation_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def cochains(width=(4, 1, 1, 1)):
    vertices = list(itertools.product(*(range(w+1) for w in width)))
    cells = [[(x, axes) for x in vertices
              for axes in itertools.combinations(range(4), degree)
              if all(x[a] < width[a] for a in axes)] for degree in range(5)]
    incidence = []
    for degree in range(1, 5):
        lower = {c: i for i, c in enumerate(cells[degree-1])}
        C = np.zeros((len(cells[degree]), len(cells[degree-1])))
        for row, (x, axes) in enumerate(cells[degree]):
            for k, a in enumerate(axes):
                remaining = axes[:k]+axes[k+1:]
                xp = list(x)
                xp[a] += 1
                C[row, lower[tuple(xp), remaining]] += (-1)**k
                C[row, lower[x, remaining]] -= (-1)**k
        incidence.append(C)
    for left, right in zip(incidence, incidence[1:]):
        assert np.max(np.abs(right@left)) == 0
    D, B = incidence[1:3]
    U, singular, _ = np.linalg.svd(D, full_matrices=False)
    U = U[:, singular > 1e-10]
    P = U@U.T
    Q = np.eye(len(P))-P
    assert np.linalg.norm(P@P-P) < 1e-12
    assert np.linalg.norm(B@P) < 1e-12
    assert np.linalg.norm(D.T@Q) < 1e-12
    expected = np.array([[3256681/4643045, -211582/4643045],
                         [496/3905, 63/3905]])
    assert np.max(np.abs(P[np.ix_([0, 18], [0, 6])].T-expected)) < 1e-13
    return incidence, P, Q


PAIRS = list(itertools.combinations(range(4), 2))
SIGNS = np.array(list(itertools.product([-1., 1.], repeat=4)))
SP = np.array([SIGNS[:, i]*SIGNS[:, j] for i, j in PAIRS])


def partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        yield [[first]]+[b[:] for b in p]
        for k in range(len(p)):
            yield [b+[first] if i == k else b[:] for i, b in enumerate(p)]


def tree_paths(edges):
    neighbors = [[] for _ in range(4)]
    for index, (i, j) in enumerate(edges):
        neighbors[i].append((j, index))
        neighbors[j].append((i, index))
    paths = []
    for start, finish in PAIRS:
        stack = [(start, -1, [])]
        found = None
        visited = set()
        while stack:
            node, parent, path = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node == finish:
                found = path
                break
            stack.extend((n, node, path+[e]) for n, e in neighbors[node] if n not in visited)
        if found is None:
            return None
        paths.append(found)
    return paths


TREES = [(edges, tree_paths(edges)) for edges in itertools.combinations(PAIRS, 3)]
TREES = [(edges, paths) for edges, paths in TREES if paths is not None]
assert len(TREES) == 16 and len(list(partitions(list(range(4))))) == 15


def pair_product(s, same, J, chi, theta, differentiated=()):
    """Self-weight factored out; batch s has shape (points, six pairs)."""
    out = np.ones((len(s), 16), dtype=complex)
    for p in range(6):
        v = s[:, p, None]
        if same[p]:
            z = J[p]*SP[p]
            term = np.exp(-v*z)
            if p in differentiated:
                term = term*(-chi[p]-z*(1-v*chi[p]))
            else:
                term = term*(1-v*chi[p])
        else:
            f = np.exp(1j*theta[p]*SP[p])-1
            term = np.broadcast_to(f, out.shape) if p in differentiated else 1+v*f
        out *= term
    return out.mean(axis=1)


def connected_by_partitions(same, J, chi, theta):
    value = 0j
    import math
    for partition in partitions(list(range(4))):
        labels = {v: k for k, block in enumerate(partition) for v in block}
        s = np.array([[float(labels[i] == labels[j]) for i, j in PAIRS]])
        value += (-1)**(len(partition)-1)*math.factorial(len(partition)-1)*pair_product(
            s, same, J, chi, theta)[0]
    return value


def connected_by_forest(same, J, chi, theta, order):
    points, weights = leggauss(order)
    points, weights = (points+1)/2, weights/2
    grid = np.array(list(itertools.product(points, repeat=3)))
    quadrature = np.prod(np.array(list(itertools.product(weights, repeat=3))), axis=1)
    descending = np.cumprod(grid, axis=1)
    quadrature *= grid[:, 0]**2*grid[:, 1]
    total = 0j
    for tree, paths in TREES:
        differentiated = {PAIRS.index(e) for e in tree}
        for permutation in itertools.permutations(range(3)):
            t = np.zeros_like(grid)
            t[:, permutation] = descending
            s = np.array([t[:, path].min(axis=1) for path in paths]).T
            total += quadrature@pair_product(s, same, J, chi, theta, differentiated)
    return total


def main():
    incidence, P, Q = cochains()
    C0, D, B, C3 = incidence
    c0, beta, N = 1/32, .5, 3
    xe, xm = N*N/beta, 4*np.pi*np.pi*beta
    H1, H3 = C0@C0.T+D.T@D, B@B.T+C3.T@C3
    assert max(np.linalg.eigvalsh(H1)[-1], np.linalg.eigvalsh(H3)[-1]) <= 16+1e-12
    modified = [P-c0*D@D.T, Q-c0*B.T@B]
    assert min(np.linalg.eigvalsh(k)[0] for k in modified) > -1e-12
    assert max(np.linalg.eigvalsh(k)[-1] for k in modified) <= 1+1e-12
    rng = np.random.default_rng(739204)
    results = []
    for name, es, ms in [('compatible', [0, 6], [0, 18]),
                         ('overlapping_electric', [0, 0], [0, 18]),
                         ('overlapping_both', [0, 0], [0, 0])]:
        fills = es+ms
        current = [D[p] for p in es]+[B[:, p] for p in ms]
        support = []
        for i, p in enumerate(fills):
            if i < 2:
                edges = np.flatnonzero(D[p])
                support.append(set(np.flatnonzero(np.any(C0[edges] != 0, axis=0))))
            else:
                cells = np.flatnonzero(B[:, p])
                support.append(set(np.flatnonzero(np.any(C3[:, cells] != 0, axis=1))))
        same = np.array([(i < 2) == (j < 2) for i, j in PAIRS])
        J = np.zeros(6)
        original_J = np.zeros(6)
        theta = np.zeros(6)
        chi = np.zeros(6)
        gram = np.zeros((4, 4))
        self_energy, local_reserve = 0., 0.
        for i in range(4):
            species, x = (0, xe) if i < 2 else (1, xm)
            kernel = P if i < 2 else Q
            self_energy += x*kernel[fills[i], fills[i]]/2
            local_reserve += c0*x*np.dot(current[i], current[i])/2
            for j in range(4):
                if (i < 2) == (j < 2):
                    gram[i, j] = x*modified[species][fills[i], fills[j]]
        for p, (i, j) in enumerate(PAIRS):
            if same[p]:
                x, kernel = (xe, P) if i < 2 else (xm, Q)
                J[p] = gram[i, j]
                original_J[p] = x*kernel[fills[i], fills[j]]
                chi[p] = bool(support[i] & support[j]) or bool(np.any(current[i]*current[j]))
                if not chi[p]:
                    assert abs(J[p]-original_J[p]) < 1e-12
            else:
                theta[p] = 2*np.pi*N*P[fills[j], fills[i]]
        full = pair_product(np.ones((1, 6)), same, J, chi, theta)[0]
        original = pair_product(np.ones((1, 6)), same, original_J, chi, theta)[0]
        assert abs(full-original) < 1e-11
        min_gram, max_ratio, max_contraction = float('inf'), 0., 0.
        for tree, paths in TREES:
            t = rng.random(3)
            S = np.eye(4)
            for (i, j), path in zip(PAIRS, paths):
                S[i, j] = S[j, i] = min(t[path])
            assert np.linalg.eigvalsh(S)[0] >= -1e-12
            min_gram = min(min_gram, np.linalg.eigvalsh(S*gram)[0])
            A = rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4))
            ratio = np.linalg.norm(S*A, 2)/np.linalg.norm(A, 2)
            max_contraction = max(max_contraction, ratio)
            assert ratio <= 1+1e-12
            # Check sign-wise actual modulus, not the modulus after averaging.
            for sigma in SIGNS:
                ratio = np.exp(-sigma@(S*gram)@sigma/2)
                for p, (i, j) in enumerate(PAIRS):
                    s = S[i, j]
                    if same[p]:
                        ratio *= 1-s*chi[p]
                    else:
                        ratio *= abs(1-s+s*np.exp(1j*sigma[i]*sigma[j]*theta[p]))
                max_ratio = max(max_ratio, ratio)
                assert ratio <= 1+1e-12
        assert min_gram > -1e-12
        direct = connected_by_partitions(same, J, chi, theta)
        estimates = {order: connected_by_forest(same, J, chi, theta, order) for order in (10, 16)}
        error = abs(estimates[16]-direct)
        assert error < 2e-9*max(1., abs(direct)), (name, direct, estimates, error)
        results.append(dict(case=name, chi=chi.tolist(), self_energy=self_energy,
                            local_reserve=local_reserve, normalized_connected=direct.real,
                            imaginary_residual=abs(direct.imag),
                            quadrature={str(n):dict(real=z.real, imag=z.imag,
                                                    error=abs(z-direct)) for n, z in estimates.items()},
                            minimum_interpolated_gram_eigenvalue=min_gram,
                            maximum_modulus_to_local_reserve_ratio=max_ratio,
                            maximum_tested_schur_contraction_ratio=max_contraction))
    # Actual integer filling gauge change; raw interpolated exponent fails.
    p = 0
    edge = np.flatnonzero(D[p])[0]
    delta = 2*np.pi*N*(D[:, edge]@P[:, p])
    assert abs(abs(delta)-2*np.pi*N) < 1e-12
    theta0, s = 2*np.pi*N*P[p, p], .5
    raw_change = abs(np.exp(1j*s*theta0)-np.exp(1j*s*(theta0+delta)))
    affine_change = abs((1-s+s*np.exp(1j*theta0))-(1-s+s*np.exp(1j*(theta0+delta))))
    assert raw_change > 1.99 and affine_change < 1e-12
    result = dict(status='finite_forest_checks_passed', N=N, beta=beta,
                  source='independently assembled finite incidences within author check',
                  raw_phase_interpolation_gauge_failure=raw_change,
                  affine_phase_interpolation_gauge_error=affine_change,
                  cases=results,
                  scope='Finite floating checks and two quadrature orders. No interval '
                        'certification, full gas estimate, physical scaling theorem, or independent review.')
    _OUTPUT_JSON.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: finite cochain, signed phase, partition and derivative fixtures')
    print('per_site: finite source-support configurations only')
    print('per_mode: finite matrix/operator directions; no all-order or infinite-kernel execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
