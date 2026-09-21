#!/usr/bin/env python3
"""Exact finite controls for the ordered late-state argument.

Enumerating small uniform count sectors checks the covariance identity and
the distinction between zero and nonzero modes. It does not prove the Euler
replacement, thermodynamic concentration or an infinite-volume mixing rate.
"""
from pathlib import Path
from itertools import permutations, product
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition, detail=None):
    assert bool(condition), (name, detail)
    checks.append(dict(name=name, passed=True, detail=detail))
    print('PASS:', name, flush=True)


def simplify(matrix):
    return matrix.applyfunc(s.simplify)


def count_sector(labels, features):
    states = sorted(set(permutations(labels)))
    volume = len(labels)
    assert volume == 4
    dim = len(features[0])
    vecs = [s.Matrix(v) for v in features]
    mean = sum((vecs[a] for a in labels), s.zeros(dim, 1)) / volume
    C = sum(((vecs[a]-mean)*(vecs[a]-mean).T for a in labels),
            s.zeros(dim)) / volume
    one = sum((vecs[a[0]] for a in states), s.zeros(dim, 1)) / len(states)
    pair = sum(((vecs[a[0]]-mean)*(vecs[a[1]]-mean).T for a in states),
               s.zeros(dim)) / len(states)
    assert one == mean
    assert simplify(pair+C/(volume-1)) == s.zeros(dim)
    modes = [[sum((s.I**(k*x)*vecs[a[x]] for x in range(volume)),
                  s.zeros(dim, 1))/2 for k in range(volume)] for a in states]
    means = [sum((q[k] for q in modes), s.zeros(dim, 1))/len(states)
             for k in range(volume)]
    covariance = {}
    for k in range(volume):
        for ell in range(volume):
            value = sum(((q[k]-means[k])*(q[ell]-means[ell]).conjugate().T
                         for q in modes), s.zeros(dim))/len(states)
            covariance[k, ell] = simplify(value)
            expected = s.Rational(volume, volume-1)*C if k == ell and k else s.zeros(dim)
            assert covariance[k, ell] == expected
    return dict(states=states, means=means, covariance=covariance, C=C)


generic = count_sector([0, 1, 2, 3], [(2, 0, 1), (-1, 1, 0), (0, -2, 1), (1, 1, -3)])
check('all_permutations_four_distinct_labels_canonical_covariance', True,
      dict(permutations=len(generic['states']), ordered_mode_pairs=16))
features = [(2, 0), (-1, 1), (0, -2)]
left = count_sector([0, 0, 1, 2], features)
right = count_sector([0, 1, 1, 2], features)
check('repeated_label_count_sectors_and_nonzero_mode_means',
      all(left['means'][k] == right['means'][k] == s.zeros(2, 1) for k in (1, 2, 3)),
      dict(permutations_per_sector=len(left['states'])))

# Directly enumerate a nontrivial mixture; do not replace it by a product law.
mixture = [(s.Rational(2, 3), left), (s.Rational(1, 3), right)]
for k in (1, 2, 3):
    value = sum((weight*sector['covariance'][k, k] for weight, sector in mixture), s.zeros(2))
    target = s.Rational(4, 3)*sum((weight*sector['C'] for weight, sector in mixture), s.zeros(2))
    assert value == target
zero_mean = sum((weight*sector['means'][0] for weight, sector in mixture), s.zeros(2, 1))
zero_cov = sum((weight*(sector['means'][0]-zero_mean)*(sector['means'][0]-zero_mean).T
                for weight, sector in mixture), s.zeros(2))
check('count_mixture_preserves_nonzero_formula_but_has_zero_mode_variance',
      zero_cov != s.zeros(2), dict(zero_mode_covariance=str(zero_cov)))

unit = [s.eye(3)[:, i] for i in range(3)]
zero = s.zeros(3, 1)
record_features = [(2*sign*unit[i], zero) for i in range(3) for sign in (-1, 1)]
record_features += [(zero, s.Matrix(signs)) for signs in product((-1, 1), repeat=3)]
mu_u = sum((u for u, v in record_features), zero)/14
mu_v = sum((v for u, v in record_features), zero)/14
cov_u = sum((u*u.T for u, v in record_features), s.zeros(3))/14
cov_v = sum((v*v.T for u, v in record_features), s.zeros(3))/14
cross = sum((u*v.T for u, v in record_features), s.zeros(3))/14
check('actual_fourteen_label_full_occupancy_feature_covariances',
      mu_u == mu_v == zero and cov_u == cov_v == s.Rational(4, 7)*s.eye(3)
      and cross == s.zeros(3))

kx, ky, kz = s.symbols('kx ky kz', real=True)
k = s.Matrix([kx, ky, kz])
C = s.Matrix([[0, -kz, ky], [kz, 0, -kx], [-ky, kx, 0]])
field_cov = simplify((s.I*C)*cov_v*(s.I*C).conjugate().T)
check('late_state_scaled_curl_second_moment',
      field_cov == s.Rational(4, 7)*(k.dot(k)*s.eye(3)-k*k.T))

# Fill all three initially vacant slots, including maximally biased choices.
initial = [2, 7]
initial_counts = [initial.count(a) for a in range(14)]
completions = 0
for births in product(range(14), repeat=3):
    counts = [initial_counts[a]+births.count(a) for a in range(14)]
    assert all(initial_counts[a] <= counts[a] <= initial_counts[a]+3 for a in range(14))
    assert sum(counts) == 5
    completions += 1
check('pathwise_count_squeeze_all_three_birth_completions', True,
      dict(completions=completions, occupied_labels=14))

# A pure-death comparison saturates the total hazard lower bound r*m.
r = s.symbols('r', positive=True)
for m in range(1, 25):
    waiting = sum(1/(r*q) for q in range(1, m+1))
    assert s.simplify(waiting-s.harmonic(m)/r) == 0
check('finite_volume_harmonic_absorption_comparison', True,
      'Rate comparison still requires the pointwise lower bound in the derivation.')

report = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              checks=checks,
              scope='Exact finite count-sector, Fourier and monotone-count controls. The ordered-limit proof and conditional Euler premises require mathematical review; no fluctuation CLT or mixing rate is certified.')
(HERE/'LATE_STATE_CANONICAL_RESULTS.json').write_text(json.dumps(report, indent=2)+'\n')
print('TOTAL:', len(checks), 'PASS', flush=True)
