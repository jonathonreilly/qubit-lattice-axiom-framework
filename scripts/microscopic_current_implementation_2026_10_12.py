#!/usr/bin/env python3
"""Author finite-algebra controls, not an infinite-volume/domain proof.

Exact Gaussian-rational sparse Pauli algebra checks local commutators. A
separate dense Kronecker assembly checks finite matrix clocks and remainders.
No model realization, spectral gap, boost domain, or scattering is tested.
"""
from collections import defaultdict

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from fractions import Fraction as F
from functools import reduce
from math import factorial
from operator import mul
from pathlib import Path
import datetime
import hashlib
import json
import platform

import numpy as np
from scipy.linalg import expm
import scipy

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IM = (F(0), F(1))
RESULTS = []


def addc(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mulc(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def scale(a, c):
    c = c if isinstance(c, tuple) else (F(c), F(0))
    return {p: mulc(v, c) for p, v in a.items() if mulc(v, c) != ZERO}


def add(*args):
    out = {}
    for a in args:
        for p, v in a.items():
            out[p] = addc(out.get(p, ZERO), v)
            if out[p] == ZERO:
                del out[p]
    return out


def single(items, c=1):
    return {tuple(sorted(items)): (F(c), F(0))}


# Products of distinct Pauli letters: coefficient i times the cyclic sign.
CYCLE = {('X', 'Y'): 'Z', ('Y', 'Z'): 'X', ('Z', 'X'): 'Y'}


def word_product(p, q):
    out = dict(p)
    c = ONE
    for site, letter in q:
        old = out.get(site)
        if old is None:
            out[site] = letter
        elif old == letter:
            del out[site]
        elif (old, letter) in CYCLE:
            out[site] = CYCLE[(old, letter)]
            c = mulc(c, IM)
        else:
            out[site] = CYCLE[(letter, old)]
            c = mulc(c, (F(0), F(-1)))
    return tuple(sorted(out.items())), c


def product(a, b):
    out = {}
    for p, u in a.items():
        for q, v in b.items():
            w, phase = word_product(p, q)
            out[w] = addc(out.get(w, ZERO), mulc(mulc(u, v), phase))
            if out[w] == ZERO:
                del out[w]
    return out


def comm(a, b):
    return add(product(a, b), scale(product(b, a), -1))


def support(a):
    return {x for word in a for x, _ in word}


def shift(a, j):
    return {tuple((x+j, p) for x, p in word): c for word, c in a.items()}


def density(x):
    return add(single([(x-1, 'X'), (x+1, 'Z')]),
               single([(x, 'Y')], F(1, 2)),
               single([(x-1, 'Z'), (x, 'Y')], F(1, 4)))


def current(x):
    return add(*(scale(comm(density(x), density(x+r)), (F(0), F(r, 2)))
                 for r in range(-2, 3)))


def deriv(a, kind='h', centers=None):
    if not support(a):
        return {}
    radius = 3 if kind == 'p' else 1
    if centers is None:
        centers = range(min(support(a))-radius, max(support(a))+radius+1)
    out = {}
    for x in centers:
        term = current(x) if kind == 'p' else density(x)
        weight = x if kind == 'b' else 1
        out = add(out, scale(comm(term, a), (F(0), F(weight))))
    return out


def norm1(a):
    return sum(abs(z[0])+abs(z[1]) for z in a.values())


def record(name, passed, **details):
    row = {'name': name, 'passed': bool(passed), **details}
    RESULTS.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)


PAULI = {
    'I': np.eye(2, dtype=complex),
    'X': np.array([[0, 1], [1, 0]], dtype=complex),
    'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
    'Z': np.diag([1, -1]).astype(complex),
}


def dense(a, sites):
    out = np.zeros((2**len(sites), 2**len(sites)), dtype=complex)
    for word, coeff in a.items():
        factors = dict(word)
        term = np.array([[1]], dtype=complex)
        for x in sites:
            term = np.kron(term, PAULI[factors.get(x, 'I')])
        out += complex(float(coeff[0]), float(coeff[1]))*term
    return out


def opnorm(a):
    return float(np.linalg.norm(a, ord=2))


def algebra_controls():
    probes = [single([(0, p)]) for p in 'XYZ']
    probes += [single([(-1, 'X'), (0, 'Y')]),
               single([(-1, 'Z'), (1, 'X')])]
    for index, a in enumerate(probes):
        bracket = add(deriv(deriv(a, 'b'), 'h'),
                      scale(deriv(deriv(a, 'h'), 'b'), -1))
        p_action = deriv(a, 'p')
        record(f'exact_pair_sign_{index}', bracket == p_action
               and bracket != scale(p_action, -1) and bracket != scale(p_action, 2),
               current_coefficient_l1=str(norm1(p_action)),
               wrong_sign_detected=(bracket != scale(p_action, -1)),
               missing_half_detected=(bracket != scale(p_action, 2)))
        j = 2
        shifted = shift(deriv(shift(a, -j), 'b'), j)
        expected = add(deriv(a, 'b'), scale(deriv(a, 'h'), -j))
        record(f'first_moment_translation_{index}', shifted == expected
               and shifted != add(deriv(a, 'b'), scale(deriv(a, 'h'), j))
               and shift(deriv(shift(a, -j), 'p'), j) == p_action,
               opposite_sign_detected=(shifted != add(deriv(a, 'b'),
                                                       scale(deriv(a, 'h'), j))),
               current_covariant=(shift(deriv(shift(a, -j), 'p'), j) == p_action))

    a = single([(0, 'Y')])
    full = add(deriv(deriv(a, 'b'), 'h'),
               scale(deriv(deriv(a, 'h'), 'b'), -1))
    padded = add(deriv(deriv(a, 'b', range(-3, 4)), 'h', range(-3, 4)),
                 scale(deriv(deriv(a, 'h', range(-3, 4)), 'b', range(-3, 4)), -1))
    short = add(deriv(deriv(a, 'b', range(-1, 2)), 'h', range(-1, 2)),
                scale(deriv(deriv(a, 'h', range(-1, 2)), 'b', range(-1, 2)), -1))
    record('padded_pair_reduction', padded == full and short != full,
           adequate_center_radius=3, inadequate_center_radius=1,
           insufficient_padding_defect_l1=str(norm1(add(short, scale(full, -1)))))
    p0 = current(0)
    record('density_support_hermiticity', all(v[1] == 0 for v in p0.values())
           and support(p0).issubset(set(range(-3, 4))),
           support=sorted(support(p0)), terms=len(p0))


def coefficient_stabilization():
    def d(a, volume=None):
        if not support(a):
            return {}
        out = {}
        for x in range(min(support(a))-1, max(support(a))+1):
            if volume is None or {x, x+1}.issubset(volume):
                out = add(out, scale(comm(single([(x, 'X'), (x+1, 'Z')]), a), IM))
        return out
    a = single([(0, 'Z')])
    for n in range(1, 6):
        full = padded = short = a
        for _ in range(n):
            full = d(full)
            padded = d(padded, set(range(-n, n+1)))
            short = d(short, set(range(1-n, n)))
        record(f'nested_volume_padding_{n}', padded == full and short != full,
               exact_terms=len(full), padding_radius=n,
               missing_layer_defect_l1=str(norm1(add(short, scale(full, -1)))))


def support_count_controls():
    # Enumerate every allowed ordered support history, aggregating only after
    # its union is known. All bond weights are one and the per-site sum is J=2.
    for initial in [{0}, {0, 4}, {0, 1, 2}]:
        states = {frozenset(initial): 1}
        for n in range(1, 8):
            updated = defaultdict(int)
            for union, weight in states.items():
                edges = {(x, x+1) for z in union for x in (z-1, z)}
                for edge in edges:
                    updated[union.union(edge)] += weight
            states = updated
            total = sum(states.values())
            a = len(initial)
            upper = 2**n*reduce(mul, (a+k for k in range(n)), 1)
            record(f'connected_history_a{a}_n{n}', total <= upper
                   and max(map(len, states)) <= a+n,
                   exact_history_count=total, upper_history_count=upper,
                   largest_union=max(map(len, states)), union_bound=a+n)
    count2 = next(row['exact_history_count'] for row in RESULTS
                  if row['name'] == 'connected_history_a1_n2')
    record('growth_factor_mutation', count2 > 2**2,
           exact_history_count=count2, false_history_upper=2**2,
           explanation='The enumerated histories violate the mutant bound that omits support growth.')
    # Enumerate singleton and zero-interaction histories through seven steps.
    for label, terms, J in [('singleton', [{0}, {1}, {2}], 1), ('zero', [], 0)]:
        states = {frozenset({0, 1, 2}): 1}
        for _ in range(7):
            updated = defaultdict(int)
            for union, weight in states.items():
                for term in terms:
                    if union.intersection(term):
                        updated[union.union(term)] += weight
            states = updated
        record(f'{label}_history_edge', sum(states.values()) == (3*J)**7
               and all(len(union) == 3 for union in states),
               exact_history_count=sum(states.values()), initial_sites=3,
               J=J, s=1, order=7)


def matrix_controls():
    sites = list(range(-2, 3))
    centers = list(range(-1, 2))
    hs = {x: dense(density(x), sites) for x in centers}
    H = sum(hs.values())
    B = sum(x*hx for x, hx in hs.items())
    P = 1j*(H@B-B@H)
    pair = sum(0.5j*(y-x)*(hs[x]@hs[y]-hs[y]@hs[x])
               for x in centers for y in centers)
    A = dense(single([(0, 'Y')]), sites)
    residual = opnorm(P-pair)
    record('dense_pair_vs_direct_commutator', residual < 1e-12,
           residual=residual, current_norm=opnorm(P),
           wrong_sign_distance=opnorm(P+pair),
           missing_half_distance=opnorm(P-2*pair))

    beta, q = 2.0, 1.0
    negative = expm(-1j*q*P/beta)@A@expm(1j*q*P/beta)
    plus_scaled = expm(1j*(-q/beta)*pair)@A@expm(-1j*(-q/beta)*pair)
    wrong_sign = expm(1j*q*pair/beta)@A@expm(-1j*q*pair/beta)
    double_beta = expm(-1j*q*pair/beta**2)@A@expm(1j*q*pair/beta**2)
    record('negative_clock_single_beta', opnorm(negative-plus_scaled) < 1e-12
           and opnorm(negative-wrong_sign) > 1e-3
           and opnorm(negative-double_beta) > 1e-3,
           correct_residual=opnorm(negative-plus_scaled),
           reversed_clock_distance=opnorm(negative-wrong_sign),
           double_beta_distance=opnorm(negative-double_beta))

    t = 1/32
    exact = expm(1j*t*P)@A@expm(-1j*t*P)
    derivative, poly = A, np.zeros_like(A)
    for n in range(1, 7):
        poly += t**(n-1)/factorial(n-1)*derivative
        derivative = 1j*(P@derivative-derivative@P)
        error = opnorm(exact-poly)
        bound = t**n/factorial(n)*opnorm(derivative)
        record(f'finite_matrix_Taylor_remainder_{n}', error <= bound+1e-12,
               error=error, remainder_bound=bound)

    hnorm = opnorm(dense(density(0), [-1, 0, 1]))
    pnorm = opnorm(dense(current(0), list(range(-3, 4))))
    # The triangle bound is exact for this fixture's rational coefficients.
    # Floating eigenvalue calculations are observations, not certified upper
    # enclosures for ||h||. Do not turn their last bit into an analytic input.
    h_triangle = F(1)+F(1, 2)+F(1, 4)
    bound = 6*h_triangle**2
    record('current_density_norm_bound', pnorm <= bound+1e-12,
           h_norm_numeric=hnorm, p_norm_numeric=pnorm,
           h_triangle_upper=str(h_triangle), p_analytic_upper=str(bound),
           assigned_site_count=7, current_diameter_bound=6,
           J_analytic_upper=str(7*bound))


def main():
    algebra_controls()
    coefficient_stabilization()
    support_count_controls()
    matrix_controls()
    path = Path(__file__).resolve()
    result = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Author finite controls only; no analytic-domain or thermodynamic theorem is numerically certified.',
        'runner_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                     'scipy': scipy.__version__},
        'results': RESULTS,
        'total_checks': len(RESULTS),
        'failed_checks': sum(not r['passed'] for r in RESULTS),
    }
    # Canonical runner reports through stdout; frozen original JSON is preserved in the milestone packet.
    print(json.dumps({k: result[k] for k in ['total_checks', 'failed_checks', 'runner_sha256']}))
    print("TOTAL: PASS="+str(result["total_checks"]-result["failed_checks"])+" FAIL="+str(result["failed_checks"]))
    print("SCOPE: Finite controls only; no domain, thermodynamic or physical-realization certificate.")
    raise SystemExit(1 if result['failed_checks'] else 0)


if __name__ == '__main__':
    main()
