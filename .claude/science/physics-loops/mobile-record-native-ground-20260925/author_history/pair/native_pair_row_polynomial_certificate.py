"""Exact pair row polynomial and six cubic interaction counts, personally derived."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

from native_pair_local_row_certificate import neighbors, overlapping_pairs_near


def polynomial(z, r, sa, sc, t):
    na, nc, ni = z-sa, z-sc, r-t
    pairs = na*nc-ni
    return 2*(pairs*((sa+1)*(sc+1)-t) + sa*ni*(nc-1)
              + sc*ni*(na-1) + ni*(ni-1) - (z*z+r*r-2*r))


def synthetic_check():
    cases = []
    for z in [3, 6]:
        for r in [1, 2]:
            a = set(range(z)); c = set(range(r)) | set(range(z, 2*z-r))
            destinations = a | c | {-1, -2}
            m = Counter(tuple(sorted((u, v))) for u in a for v in c if u != v)
            for x_tuple in combinations(sorted(destinations), 2):
                x = set(x_tuple)
                enumerated = -2*sum(v*v for v in m.values())
                for d, first in m.items():
                    if x.intersection(d):
                        continue
                    y = x | set(d)
                    enumerated += 2*first*sum(m.get(returning, 0) for returning in combinations(sorted(y), 2))
                sa, sc, t = len(a & x), len(c & x), len(a & c & x)
                value = polynomial(z, r, sa, sc, t)
                assert value == enumerated, (z, r, x_tuple, value, enumerated)
                cases.append((z, r, sa, sc, t, value))
    unique = sorted(set(cases))
    return {'exhaustive_input_pairs': len(cases), 'distinct_parameter_rows': unique}


def local_interactions(d):
    b = (1, 0, 0); e = tuple(x+y for x, y in zip(b, d)); x = {b, e}
    common = overlapping_pairs_near(b) & overlapping_pairs_near(e)
    counts = Counter()
    for a, c in common:
        aa, cc = set(neighbors(a)), set(neighbors(c)); r = len(aa & cc)
        sa, sc, t = len(aa & x), len(cc & x), len(aa & cc & x)
        single = [polynomial(6, r, int(y in aa), int(y in cc), int(y in aa & cc)) for y in [b, e]]
        delta = polynomial(6, r, sa, sc, t)-sum(single)
        counts[(r, min(sa, sc), max(sa, sc), t, delta)] += 1
    shift = sum(key[-1]*n for key, n in counts.items())
    return {'displacement': d, 'common_active_pairs': len(common),
            'interaction_counts': [{'r': key[0], 's_min': key[1], 's_max': key[2],
                                    't': key[3], 'interaction_per_pair': key[4], 'pairs': n}
                                   for key, n in sorted(counts.items())],
            'interaction_row_correction': shift, 'full_row_sum': 12096+shift}


def main():
    synthetic = synthetic_check()
    singles = [dict(r=r, sa=sa, sc=sc, t=t, count=n, row_contribution=polynomial(6, r, sa, sc, t))
               for r, sa, sc, t, n in [(1,0,1,0,30),(1,1,1,1,3),(2,0,1,0,48),(2,1,1,1,12)]]
    assert sum(row['count']*row['row_contribution'] for row in singles) == 6048
    rows = [local_interactions(d) for d in [(0,0,2),(0,1,1),(0,0,4),(0,1,3),(0,2,2),(1,1,2)]]
    previous = json.loads(Path('LOCAL_ROW_CERTIFICATE.json').read_text())
    expected = {tuple(r['absolute_coordinate_type']):r['exact_row_sum'] for r in previous['cubic_symmetry_groups']}
    for row in rows:
        assert row['full_row_sum'] == expected[row['displacement']]
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'topology_helper_sha256': hashlib.sha256(Path('native_pair_local_row_certificate.py').read_bytes()).hexdigest(),
              'prior_row_certificate_sha256': hashlib.sha256(Path('LOCAL_ROW_CERTIFICATE.json').read_bytes()).hexdigest(),
              'synthetic': synthetic, 'single_occupied_B_contributions': singles,
              'two_occupied_B_interactions': rows,
              'scope': 'Exact root controls of the pair-count polynomial; not an independent reconstruction.'}
    p = Path('ROW_POLYNOMIAL_CERTIFICATE.json');p.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
