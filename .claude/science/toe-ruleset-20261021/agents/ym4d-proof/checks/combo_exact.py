#!/usr/bin/env python3
"""Registered exact checks of COMBO's finite cumulant identities.

Raw moments are computed first; the full partition formula, independently
of each proposed closed form, then computes cumulants. No numeric sampling.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
from pathlib import Path
import hashlib
import json
import os
import resource

assert os.environ.get('COMBO_GUARDED') == '1', 'Run through combo_run.py'

NAMES = ['mu1', 'mu2', 'mu3', 'mu4'] + [
    f'C{i+1}{j+1}' for i, j in combinations(range(4), 2)]
ZERO_MONOMIAL = (0,) * len(NAMES)


def const(q):
    return {ZERO_MONOMIAL: Q(q)} if q else {}


def var(index):
    powers = list(ZERO_MONOMIAL)
    powers[index] = 1
    return {tuple(powers): Q(1)}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            out[powers] = out.get(powers, Q(0)) + coefficient
    return {p: c for p, c in out.items() if c}


def scale(polynomial, coefficient):
    return {p: c * coefficient for p, c in polynomial.items()
            if c * coefficient}


def mul(*polynomials):
    out = const(1)
    for polynomial in polynomials:
        new = {}
        for p, c in out.items():
            for q, d in polynomial.items():
                powers = tuple(a + b for a, b in zip(p, q))
                new[powers] = new.get(powers, Q(0)) + c * d
        out = {p: c for p, c in new.items() if c}
    return out


def square(polynomial):
    return mul(polynomial, polynomial)


MU = [var(i) for i in range(4)]
COV = {pair: var(4 + i) for i, pair in
       enumerate(combinations(range(4), 2))}


def gaussian_moment(mask, means):
    """Partition a Gaussian moment into the first singleton or paired leg."""
    if not mask:
        return const(1)
    i = next(i for i in range(4) if mask & (1 << i))
    rest = mask ^ (1 << i)
    terms = [mul(means[i], gaussian_moment(rest, means))]
    for j in range(i + 1, 4):
        if rest & (1 << j):
            terms.append(mul(COV[i, j], gaussian_moment(rest ^ (1 << j), means)))
    return add(*terms)


def partitions(items):
    """Unordered set partitions; separate from Gaussian pairing recursion."""
    if not items:
        yield []
        return
    first, *rest = items
    for partition in partitions(rest):
        yield [[first]] + partition
        for index in range(len(partition)):
            yield partition[:index] + [[first] + partition[index]] + partition[index+1:]


def cumulant(moments, mask):
    result = {}
    items = [i for i in range(4) if mask & (1 << i)]
    for partition in partitions(items):
        coefficient = (-1) ** (len(partition) - 1) * factorial(len(partition) - 1)
        factors = [moments[sum(1 << i for i in block)] for block in partition]
        result = add(result, scale(mul(*factors), coefficient))
    return result


def describe(polynomial):
    return [{'coefficient': str(c),
             'monomial': '*'.join(f'{name}^{power}' for name, power in zip(NAMES, p)
                                  if power) or '1'}
            for p, c in sorted(polynomial.items())]


records = []


def compare(name, obtained, expected, control=False):
    difference = add(obtained, scale(expected, -1))
    passed = bool(difference) if control else not difference
    records.append(dict(id=name, control=control, passed=passed,
                        obtained=describe(obtained), expected=describe(expected),
                        difference=describe(difference)))


general = {mask: gaussian_moment(mask, MU) for mask in range(16)}
centred = {mask: gaussian_moment(mask, [{}] * 4) for mask in range(16)}
compare('gaussian_arbitrary_means_K4', cumulant(general, 15), {})

pairings = [mul(COV[0, 1], COV[2, 3]),
            mul(COV[0, 2], COV[1, 3]),
            mul(COV[0, 3], COV[1, 2])]
pair_sum = add(*pairings)
amplitude = {mask: scale(moment, Q(1 + 2 ** mask.bit_count(), 2))
             for mask, moment in centred.items()}
compare('amplitude_covariance', cumulant(amplitude, 3), scale(COV[0, 1], Q(5, 2)))
compare('amplitude_K4', cumulant(amplitude, 15), scale(pair_sum, Q(9, 4)))

shifted = {mask: scale(add(gaussian_moment(mask, [const(1)] * 4),
                          gaussian_moment(mask, [const(-1)] * 4)), Q(1, 2))
           for mask in range(16)}
compare('random_shift_covariance', cumulant(shifted, 3), add(COV[0, 1], const(1)))
compare('random_shift_K4', cumulant(shifted, 15), const(-2))

product = {mask: square(moment) for mask, moment in centred.items()}
product_K4 = scale(add(*(mul(pairings[i], pairings[j])
                         for i, j in combinations(range(3), 2))), 2)
compare('independent_product_covariance', cumulant(product, 3), square(COV[0, 1]))
compare('independent_product_K3', cumulant(product, 7), {})
compare('independent_product_K4', cumulant(product, 15), product_K4)


def affine_moments(moments, a, b):
    transformed = {}
    for mask in range(16):
        terms = []
        subset = mask
        while True:
            terms.append(scale(moments[subset],
                               a ** subset.bit_count() * b ** (mask.bit_count() - subset.bit_count())))
            if subset == 0:
                break
            subset = (subset - 1) & mask
        transformed[mask] = add(*terms)
    return transformed


for index, (a, b) in enumerate([(Q(-3, 2), Q(7, 3)), (Q(2, 3), Q(-5, 2))], 1):
    transformed = affine_moments(product, a, b)
    base_B = cumulant(product, 6)
    new_B = cumulant(transformed, 6)
    new_K4 = cumulant(transformed, 15)
    compare(f'affine_{index}_covariance', new_B, scale(base_B, a ** 2))
    compare(f'affine_{index}_K4', new_K4, scale(product_K4, a ** 4))
    compare(f'affine_{index}_ratio_cross_product',
            mul(new_K4, square(base_B)), mul(product_K4, square(new_B)))

compare('control_missing_gaussian_subtraction',
        add(centred[15], scale(pairings[0], -1), scale(pairings[1], -1)),
        cumulant(centred, 15), control=True)
compare('control_wrong_amplitude_coefficient', scale(pair_sum, Q(17, 2)),
        cumulant(amplitude, 15), control=True)
compare('control_missing_product_factor_two', scale(product_K4, Q(1, 2)),
        cumulant(product, 15), control=True)
compare('control_omitted_mean_variance', COV[0, 1],
        cumulant(shifted, 3), control=True)

here = Path(__file__).resolve().parent
result = dict(passed=all(r['passed'] for r in records), records=records,
              scientific_scope='Formal finite kernel/moment identities only; no YM estimate or AF numerical test.',
              criteria_sha256=hashlib.sha256((here / 'combo_criteria.md').read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['passed'] else 1)
