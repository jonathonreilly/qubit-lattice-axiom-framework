"""Finite challenges of the source-parity graph Holder construction.

Checks all four-vertex bond/parity patterns, explicit spanning-tree mixtures,
finite-group Holder inequalities, and the connected source expansion against
partition inversion with both same-species Coulomb factors and hard core.
This is author verification, not a physical scaling simulation or audit.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'scripts/forest_interpolation_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/graph_source_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from forest_interpolation_check_2026_09_15 import cochains, partitions

PAIRS = list(itertools.combinations(range(4), 2))


def spanning_tree(edges, vertices, included=None, excluded=None):
    parent = list(range(vertices))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    chosen = []
    order = ([included] if included is not None else [])+[i for i in range(len(edges)) if i != included]
    for e in order:
        if e == excluded:
            continue
        i, j = edges[e]
        a, b = root(i), root(j)
        if a != b:
            chosen.append(e)
            parent[a] = b
        if len(chosen) == vertices-1:
            return chosen
    return None


def connected_pattern(states):
    edges = [e for e, state in zip(PAIRS, states) if state]
    return spanning_tree(edges, 4) is not None


def tree_mixture(spatial, powers):
    K = sum(powers)
    source = [(i, 4) for i, k in enumerate(powers) for _ in range(k)]
    edges = spatial+source
    M = len(edges)
    beta = np.zeros(M)
    for e in range(M):
        inside = spanning_tree(edges, 5, included=e)
        outside = spanning_tree(edges, 5, excluded=e)
        assert inside is not None and outside is not None
        assert e in inside and e not in outside
        beta[inside] += 1/(2*M)
        beta[outside] += 1/(2*M)
    assert beta.min() >= 1/(2*M)-1e-13 and beta.max() <= 1-1/(2*M)+1e-13
    initial = np.zeros(M)
    initial[spanning_tree(spatial, 4)] = 1
    initial[len(spatial):] = 1/K
    delta = 1/(4*(K-1))
    alpha = (1-delta)*initial+delta*beta
    assert np.all(alpha[:len(spatial)] < 1)
    assert np.all(alpha > 0)
    assert alpha[len(spatial):].max() <= 5/(4*K)+1e-13
    assert alpha[len(spatial):].sum() <= 1.25+1e-13
    assert abs(alpha.sum()-4) < 1e-12
    exponent = 2*K-4*alpha[len(spatial):].sum()
    assert exponent >= 2*K-5-1e-12
    return edges, alpha, exponent


def graph_patterns():
    count, connected, max_edges = 0, 0, 0
    min_spatial_slack, min_exponent = 1., float('inf')
    examples = []
    for states in itertools.product(range(3), repeat=6):
        if not connected_pattern(states):
            continue
        connected += 1
        spatial, parity = [], [0]*4
        for (i, j), state in zip(PAIRS, states):
            if state == 1:  # even bond is doubled
                spatial += [(i, j)]*2
            elif state == 2:  # odd bond is one edge
                spatial += [(i, j)]
                parity[i] ^= 1
                parity[j] ^= 1
        choices = [[1, 3] if p else [0, 2, 4] for p in parity]
        for powers in itertools.product(*choices):
            if sum(powers) < 4:
                continue
            degree = [powers[i] for i in range(4)]+[sum(powers)]
            for i, j in spatial:
                degree[i] += 1
                degree[j] += 1
            assert not any(d % 2 for d in degree)
            edges, alpha, exponent = tree_mixture(spatial, powers)
            count += 1
            max_edges = max(max_edges, len(edges))
            min_spatial_slack = min(min_spatial_slack, 1-alpha[:len(spatial)].max())
            min_exponent = min(min_exponent, exponent)
            if len(examples) < 3 and sum(powers) == 4:
                examples.append((edges, alpha))
    # Removing parity can leave a spatial bridge with no source on one side.
    invalid = [(0, 1), (1, 2), (2, 3)]+[(0, 4)]*4
    assert spanning_tree(invalid, 5, excluded=2) is None
    return dict(connected_bond_state_patterns=connected,
                parity_matched_remainder_patterns=count,
                maximum_augmented_edges=max_edges,
                minimum_spatial_one_minus_alpha=min_spatial_slack,
                minimum_actual_source_power=min_exponent,
                unmarked_bridge_negative_control=True), examples


def holder_examples(examples):
    rng = np.random.default_rng(427915)
    group = 5
    points = np.array(list(itertools.product(range(group), repeat=4)))
    points = np.column_stack((points, np.zeros(len(points), dtype=int)))
    rows = []
    for edges, alpha in examples:
        kernels = [.1+.8*rng.random(group) for _ in edges]
        product = np.ones(len(points))
        log_bound = 0.
        for (i, j), a, f in zip(edges, alpha, kernels):
            product *= f[(points[:, i]-points[:, j]) % group]
            p = 1/a
            # Stable log l^p norm for possibly large p.
            logs = p*np.log(f)
            peak = max(logs)
            log_bound += (peak+np.log(np.exp(logs-peak).sum()))/p
        actual, bound = product.sum(), np.exp(log_bound)
        assert actual <= bound*(1+1e-12)
        rows.append(dict(group_order=group, graph_edges=len(edges), actual=actual, bound=bound))
    return rows


def source_identity():
    mp.mp.dps = 60
    incidence, P, Q = cochains()
    D, B = incidence[1:3]
    beta, N = mp.mpf('.5'), 3
    g, b, c = N/mp.sqrt(beta), 2*mp.pi*mp.sqrt(beta), 2*mp.pi*N
    signs = list(itertools.product([-1, 1], repeat=4))
    partitions4 = list(partitions(list(range(4))))
    graphs = [states for states in itertools.product([0, 1, 2], repeat=6) if connected_pattern(states)]
    h = np.array([.04*math.sin(.3*i)+.03*math.cos(.7*i) for i in range(len(P))])
    rows = []
    for name, labels, exclusions in [('compatible', [0, 6, 0, 18], [False, False]),
                                     ('electric_overlap', [0, 0, 0, 18], [True, False]),
                                     ('double_overlap', [0, 0, 0, 0], [True, True])]:
        L = [-g*mp.mpf(float((P@h)[labels[i]])) if i < 2
             else -1j*b*mp.mpf(float((Q@h)[labels[i]])) for i in range(4)]
        C, O, raw_pairs = [], [], []
        for i, j in PAIRS:
            if (i < 2) == (j < 2):
                J = (g*g if i < 2 else b*b)*mp.mpf(float((P if i < 2 else Q)[labels[i], labels[j]]))
                chi = exclusions[0 if i < 2 else 1]
                C.append(-mp.mpf(1) if chi else mp.cosh(J)-1)
                O.append(mp.mpf(0) if chi else -mp.sinh(J))
                raw_pairs.append(('same', J, chi))
            else:
                theta = c*mp.mpf(float(P[labels[j], labels[i]]))
                C.append(mp.cos(theta)-1)
                O.append(1j*mp.sin(theta))
                raw_pairs.append(('mixed', theta, False))
        z = mp.mpc('.7', '.2')
        direct = mp.mpc(0)
        for sigma in signs:
            original_pair = []
            for e, (i, j) in enumerate(PAIRS):
                kind, coupling, excluded = raw_pairs[e]
                original = ((1-int(excluded))*mp.exp(-coupling*sigma[i]*sigma[j])
                            if kind == 'same' else mp.exp(1j*coupling*sigma[i]*sigma[j]))
                assert abs(original-(1+C[e]+sigma[i]*sigma[j]*O[e])) < mp.mpf('1e-48')
                original_pair.append(original)
            connected = mp.mpc(0)
            for partition in partitions4:
                block = {i: k for k, part in enumerate(partition) for i in part}
                weight = mp.fprod(original_pair[e] for e, (i, j) in enumerate(PAIRS) if block[i] == block[j])
                connected += (-1)**(len(partition)-1)*math.factorial(len(partition)-1)*weight
            Y = sum(s*l for s, l in zip(sigma, L))
            direct += connected*(mp.cosh(z*Y)-1-(z*Y)**2/2)/16
        expanded = mp.mpc(0)
        for states in graphs:
            parity, amplitude = [0]*4, mp.mpc(1)
            for e, ((i, j), state) in enumerate(zip(PAIRS, states)):
                if state == 1:
                    amplitude *= C[e]
                elif state == 2:
                    amplitude *= O[e]
                    parity[i] ^= 1
                    parity[j] ^= 1
            if amplitude == 0:
                continue
            full = mp.fprod(mp.sinh(z*L[i]) if parity[i] else mp.cosh(z*L[i]) for i in range(4))
            if sum(parity) == 0:
                low = 1+z*z*sum(l*l for l in L)/2
            elif sum(parity) == 2:
                low = z*z*mp.fprod(L[i] for i in range(4) if parity[i])
            else:
                low = 0
            expanded += amplitude*(full-low)
        error = abs(expanded-direct)
        assert error < mp.mpf('1e-48')*max(1, abs(direct))
        rows.append(dict(case=name, subtracted_real=str(mp.re(direct)),
                         subtracted_imag=str(mp.im(direct)), parity_expansion_error=str(error)))
    return rows


def main():
    patterns, examples = graph_patterns()
    result = dict(status='finite_graph_source_checks_passed', patterns=patterns,
                  finite_group_holder=holder_examples(examples),
                  physical_bond_source_identities=source_identity(),
                  scope='Exhaustive four-label parity bookkeeping, finite tree mixtures and '
                        'source identities. No infinite-volume numerical limit, all-order '
                        'coefficient bound, interval arithmetic or independent review.')
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
