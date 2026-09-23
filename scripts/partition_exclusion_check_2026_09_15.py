"""Finite author check of random-connectivity exclusion interpolation.

This is a different interpolation from the earlier pair-affine one. The
three-component BKAR test uses its own analytically differentiated weight.
It does not certify a spatial tree bound or full activity-one convergence.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'scripts/forest_interpolation_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/partition_exclusion_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from forest_interpolation_check_2026_09_15 import cochains, partitions


PAIRS = list(itertools.combinations(range(3), 2))
SIGNS = np.array(list(itertools.product([-1., 1.], repeat=3)))
SP = np.array([SIGNS[:, i]*SIGNS[:, j] for i, j in PAIRS])


def connected_partition(bits):
    labels = list(range(3))
    for present, (i, j) in zip(bits, PAIRS):
        if present:
            old, new = labels[j], labels[i]
            labels = [new if x == old else x for x in labels]
    return labels


def exclusion(s, chi, derivatives=(), wrong_contact=False):
    if wrong_contact and any(not chi[e] for e in derivatives):
        return np.zeros(len(s))
    out = np.zeros(len(s))
    for bits in itertools.product([0, 1], repeat=3):
        labels = connected_partition(bits)
        if any(chi[e] and labels[i] == labels[j] for e, (i, j) in enumerate(PAIRS)):
            continue
        weight = np.ones(len(s))
        for e, bit in enumerate(bits):
            weight *= (1. if bit else -1.) if e in derivatives else (s[:, e] if bit else 1-s[:, e])
        out += weight
    return out


def subsets(items):
    for bits in itertools.product([0, 1], repeat=len(items)):
        yield tuple(i for bit, i in zip(bits, items) if bit)


def weight(s, chi, coupling, source, self_factor, derivatives=(), wrong_contact=False):
    gaussian = np.exp(-(s@np.diag(coupling))@SP)
    gaussian = gaussian*np.exp(SIGNS@source)[None, :]*self_factor
    differentiated = np.zeros_like(gaussian, dtype=complex)
    for h_derivatives in subsets(derivatives):
        term = np.broadcast_to(exclusion(s, chi, h_derivatives, wrong_contact)[:, None], gaussian.shape).copy()
        for e in derivatives:
            if e not in h_derivatives:
                term *= -coupling[e]*SP[e]
        differentiated += term
    return (gaussian*differentiated).mean(axis=1)


def connected_direct(chi, coupling, source, self_factor):
    total = 0j
    for partition in partitions(list(range(3))):
        labels = {i: k for k, block in enumerate(partition) for i in block}
        s = np.array([[float(labels[i] == labels[j]) for i, j in PAIRS]])
        total += (-1)**(len(partition)-1)*math.factorial(len(partition)-1)*weight(s, chi, coupling, source, self_factor)[0]
    return total


def forest_integral(chi, coupling, source, self_factor, order, wrong_contact=False):
    nodes, weights = leggauss(order)
    nodes, weights = (nodes+1)/2, weights/2
    grid = np.array(list(itertools.product(nodes, repeat=2)))
    quadrature = np.prod(np.array(list(itertools.product(weights, repeat=2))), axis=1)*grid[:, 0]
    total = 0j
    for tree in itertools.combinations(range(3), 2):
        missing = next(e for e in range(3) if e not in tree)
        for first, second in [tree, tree[::-1]]:
            s = np.zeros((len(grid), 3))
            s[:, first] = grid[:, 0]
            s[:, second] = grid[:, 0]*grid[:, 1]
            s[:, missing] = s[:, second]
            total += quadrature@weight(s, chi, coupling, source, self_factor, tree, wrong_contact)
    return total


def main():
    chi = np.array([0, 1, 0])  # only vertices 0 and 2 incompatible
    s = np.array([[.2, .4, .7], [.8, .1, .3]])
    expected = (1-s[:, 1])*(1-s[:, 0]*s[:, 2])
    assert np.max(abs(exclusion(s, chi)-expected)) < 2e-15
    expected_derivative = -(1-s[:, 1])*s[:, 2]
    assert np.max(abs(exclusion(s, chi, (0,))-expected_derivative)) < 2e-15
    assert np.max(abs(exclusion(s, chi)-(1-s[:, 1]))) > .08
    # Exhaust all three-vertex incompatibility graphs and all derivatives.
    rng = np.random.default_rng(51083)
    maximum_variation_ratio = 0.
    for mask in itertools.product([0, 1], repeat=3):
        ch = np.array(mask)
        points = rng.uniform(0, 1, size=(31, 3))
        values = exclusion(points, ch)
        assert values.min() >= -1e-14 and values.max() <= 1+1e-14
        for derivatives in subsets(tuple(range(3))):
            value = exclusion(points, ch, derivatives)
            ratio = np.max(abs(value))/2**len(derivatives)
            maximum_variation_ratio = max(maximum_variation_ratio, ratio)
            assert ratio <= 1+1e-14

    incidence, p, q = cochains()
    c0, d, b, c3 = incidence
    supports = []
    for row in d:
        edges = np.flatnonzero(row)
        supports.append(set(np.flatnonzero(np.any(c0[edges] != 0, axis=0))))
    # Locate the stated incompatibility pattern on the actual cochain fixture.
    triple = None
    for i, j, k in itertools.permutations(range(len(p)), 3):
        actual = [bool(supports[a]&supports[b]) for a, b in [(i, j), (i, k), (j, k)]]
        if actual == list(chi.astype(bool)):
            triple = [i, j, k]
            break
    assert triple is not None
    x = 18.
    kernel = p-d@d.T/32
    gram = x*kernel[np.ix_(triple, triple)]
    assert np.linalg.eigvalsh(gram)[0] > -1e-12
    coupling = np.array([gram[i, j] for i, j in PAIRS])
    local = x*np.sum(d[triple]**2)/64
    self_factor = np.exp(-local-.5*np.trace(gram))
    h = .011*np.cos(np.arange(len(p))*.71+.2)
    source = -np.sqrt(x)*(p@h)[triple]*(.4+.3j)
    reference = connected_direct(chi, coupling, source, self_factor)
    checks = []
    for order in [12, 20, 28]:
        value = forest_integral(chi, coupling, source, self_factor, order)
        error = abs(value-reference)
        checks.append(dict(order=order, absolute_error=float(error),
                           relative_error=float(error/max(abs(reference), 1e-300))))
    assert checks[-1]['absolute_error'] < 1e-12+1e-10*abs(reference)
    wrong = forest_integral(chi, coupling, source, self_factor, 28, True)
    wrong_error = abs(wrong-reference)
    assert wrong_error > max(1e-12, .01*abs(reference))
    result = dict(status='finite_author_checks_passed', independent_review=False,
                  new_interpolation_value=exclusion(s, chi).tolist(),
                  old_affine_value=(1-s[:, 1]).tolist(),
                  derivative_at_compatible_pair=exclusion(s, chi, (0,)).tolist(),
                  maximum_derivative_variation_ratio=float(maximum_variation_ratio),
                  cochain_face_triple=triple, incompatibility=chi.tolist(),
                  gram_eigenvalues=np.linalg.eigvalsh(gram).tolist(),
                  connected_reference=dict(real=float(reference.real), imag=float(reference.imag)),
                  quadrature=checks,
                  wrong_local_contact_routing_error=float(wrong_error),
                  limitations=['three-component identity fixture only',
                               'shared float cochain inputs',
                               'no spatial routing or full convergence theorem'])
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
