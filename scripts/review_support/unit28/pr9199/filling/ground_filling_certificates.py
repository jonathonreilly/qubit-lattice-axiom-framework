"""Exact root occupancy certificates; no diagonalization or physical-vacuum selection."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import time


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def local_certificate(r):
    common = set(range(r))
    aa = common | set(range(r, 6))
    cc = common | set(range(6, 12-r))
    union = aa | cc
    kernel = Counter(tuple(sorted((a, c))) for a in aa for c in cc if a != c)
    v = sum(k*k for k in kernel.values())
    shared = sum(a*b for x, a in kernel.items() for y, b in kernel.items()
                 if x != y and len(set(x) & set(y)) == 1)
    disjoint = sum(a*b for x, a in kernel.items() for y, b in kernel.items()
                   if not set(x) & set(y))
    patterns = defaultdict(list)
    direct_by_count = Counter()
    for mask in range(1 << len(union)):
        occupied = {i for i in union if mask & (1 << i)}
        # Direct intermediate-set Gram row sum, with all old-record returns.
        direct = 0
        for outward, weight in kernel.items():
            if occupied & set(outward):
                continue
            intermediate = occupied | set(outward)
            direct += weight * sum(k for inward, k in kernel.items()
                                   if set(inward) <= intermediate)
        sa, sc, t = len(occupied & aa), len(occupied & cc), len(occupied & common)
        na, nc, ni = 6-sa, 6-sc, r-t
        formula = (na*nc-ni)*((sa+1)*(sc+1)-t) + sa*ni*(nc-1) + sc*ni*(na-1) + ni*(ni-1)
        assert formula == direct
        ell, holes = len(occupied), len(union)-len(occupied)
        add_bound = 40 if r == 1 else 44
        vacancy_bound = Fraction(28) if r == 1 else Fraction(104, 3)
        assert direct <= v + add_bound*ell
        assert direct <= vacancy_bound*holes
        patterns[t, sa, sc].append(direct)
        direct_by_count[ell] += direct
    rows = []
    for (t, sa, sc), values in sorted(patterns.items()):
        assert min(values) == max(values)
        ell, holes = sa+sc-t, 12-r-(sa+sc-t)
        multiplicity = comb(r, t)*comb(6-r, sa-t)*comb(6-r, sc-t)
        assert multiplicity == len(values)
        rows.append({'t': t, 'sa': sa, 'sc': sc, 'occupied': ell, 'vacant': holes,
                     'row': values[0], 'multiplicity': multiplicity,
                     'increment_per_occupied': str(Fraction(values[0]-v, ell)) if ell else None,
                     'row_per_vacant': str(Fraction(values[0], holes)) if holes else None})
    n = 12
    average_rows = []
    for m in range(n+1):
        direct_sum = sum(total*choose(n-len(union), m-ell) for ell, total in direct_by_count.items())
        formula_sum = v*choose(n-2, m)+shared*choose(n-3, m-1)+disjoint*choose(n-4, m-2)
        assert direct_sum == formula_sum
        average_rows.append({'global_B_sites': n, 'occupied': m,
                             'uniform_Rayleigh': str(Fraction(direct_sum, comb(n, m)))})
    return {'overlap': r, 'union_sites': len(union), 'complete_subsets_checked': 1 << len(union),
            'local_counts': {'v': v, 'a': shared, 'd': disjoint},
            'pattern_rows': rows, 'all_m_average_rows': average_rows,
            'maximum_increment_per_occupied': str(max(Fraction(r['increment_per_occupied']) for r in rows if r['increment_per_occupied'] is not None)),
            'maximum_row_per_vacant': str(max(Fraction(r['row_per_vacant']) for r in rows if r['row_per_vacant'] is not None))}


def torus_certificate(side):
    vertices = list(product(range(side), repeat=3))
    aa = [v for v in vertices if sum(v) % 2 == 0]
    bb = [v for v in vertices if sum(v) % 2 == 1]
    def near(v):
        return {tuple((x+(s if axis == j else 0)) % side for j, x in enumerate(v))
                for axis in range(3) for s in [-1, 1]}
    pairs = {tuple(sorted(pair)) for b in bb for pair in combinations(near(b), 2)}
    kind = Counter()
    incident = {b: Counter() for b in bb}
    for a, c in pairs:
        na, nc = near(a), near(c)
        r = len(na & nc)
        assert r in [1, 2]
        kind[r] += 1
        for b in na | nc:
            incident[b][r] += 1
    n = len(bb)
    assert kind == {1: 3*n, 2: 6*n}
    assert all(count == {1: 33, 2: 60} for count in incident.values())
    m = n//2
    assert m % 2 == 0
    v, a, d = 321*n, 3666*n, 6624*n
    selected = sorted({0, 2, 2*(n//8), m, 2*(3*n//8), n-2, n})
    rows = []
    for count in selected:
        value = Fraction(v*choose(n-2, count)+a*choose(n-3, count-1)+d*choose(n-4, count-2), choose(n, count))
        assert value <= min(321*n+3960*count, 3004*(n-count))
        rows.append({'occupied_B': count, 'minus_charges': count//2,
                     'Rayleigh_per_n': str(value/n),
                     'two_row_upper_bounds_per_n': [str(Fraction(321*n+3960*count, n)), str(Fraction(3004*(n-count), n))]})
        if count == m:
            half = value/n
    expected = Fraction(1905, 2)+Fraction(378, n-1)+Fraction(414*(2*n-3), (n-1)*(n-3))
    assert half == expected > Fraction(1905, 2)
    return {'side': side, 'B_sites': n, 'overlapping_pair_counts': dict(kind),
            'every_B_union_incidence': {'overlap_1': 33, 'overlap_2': 60},
            'all_B_sites_checked': len(incident), 'selected_occupancies': rows,
            'half_filling_Rayleigh_per_n': str(half),
            'half_filling_excess_above_1905_over_2': str(half-Fraction(1905, 2))}


if __name__ == '__main__':
    tick = time.perf_counter()
    local = [local_certificate(r) for r in [1, 2]]
    assert [r['maximum_increment_per_occupied'] for r in local] == ['40', '44']
    assert [r['maximum_row_per_vacant'] for r in local] == ['28', '104/3']
    add_coefficient = 33*40+60*44
    vacancy_coefficient = 33*28+60*Fraction(104, 3)
    lower = (Fraction(1905, 2)-321)/add_coefficient
    upper = 1-Fraction(1905, 2)/vacancy_coefficient
    assert add_coefficient == 3960 and vacancy_coefficient == 3004
    assert lower == Fraction(421, 2640) and upper == Fraction(4103, 6008)
    result = {'scope': __doc__, 'local_certificates': local,
              'torus_certificates': [torus_certificate(side) for side in [6, 8, 10, 12]],
              'necessary_lowest_energy_sector_filling': {'strict_lower': str(lower), 'strict_upper': str(upper),
                                                        'lower_decimal': float(lower), 'upper_decimal': float(upper)},
              'all_assertions_passed': True,
              'limits': 'Finite-pattern proof and finite controls, no full many-body diagonalization or physical vacuum selection; fixed graph before g tends to zero.',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.perf_counter()-tick}
    print(json.dumps(result, indent=2, allow_nan=False))
