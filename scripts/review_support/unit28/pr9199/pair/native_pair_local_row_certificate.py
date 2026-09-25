"""Exact unwrapped row sums; supplements the frozen personal torus control."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json
import time

from native_pair_controls import local_delta_row


def neighbors(v):
    out = []
    for axis in range(3):
        for step in (-1, 1):
            w = list(v)
            w[axis] += step
            out.append(tuple(w))
    return out


def overlapping_pairs_near(b):
    return {tuple(sorted((a, c))) for a in neighbors(b)
            for d in neighbors(a) for c in neighbors(d) if c != a}


def row(displacement):
    from collections import Counter
    origin = (1, 0, 0)
    x = (origin, tuple(a+b for a, b in zip(origin, displacement)))
    pairs = sorted(overlapping_pairs_near(x[0]) | overlapping_pairs_near(x[1]))
    records, near = [], defaultdict(set)
    for index, (a, c) in enumerate(pairs):
        assignments = Counter(tuple(sorted((u, v))) for u in neighbors(a)
                              for v in neighbors(c) if u != v)
        records.append((a, c, assignments, 2*sum(m*m for m in assignments.values())))
        for b in set(neighbors(a)) | set(neighbors(c)):
            near[b].add(index)
    values = local_delta_row(x, records, near)
    return {'displacement': displacement, 'active_pairs': len(pairs),
            'common_active_pairs': len(overlapping_pairs_near(x[0]) & overlapping_pairs_near(x[1])),
            'diagonal': values[tuple(sorted(x))], 'row_sum': sum(values.values()),
            'nonzero_targets': len(values),
            'maximum_active_vertex_distance_from_nearer_input': max(
                min(sum(abs(v[k]-b[k]) for k in range(3)) for b in x)
                for a, c in pairs for v in neighbors(a)+neighbors(c))}


def main():
    start = time.perf_counter()
    ds = [d for d in product(range(-4, 5), repeat=3)
          if 0 < sum(map(abs, d)) <= 4 and sum(d) % 2 == 0]
    rows = [row(d) for d in ds]
    groups = defaultdict(list)
    for r in rows:
        groups[tuple(sorted(map(abs, r['displacement'])))].append(r)
    grouped = []
    for key, values in sorted(groups.items()):
        sums = {v['row_sum'] for v in values}
        assert len(sums) == 1
        grouped.append({'absolute_coordinate_type': key, 'displacements': len(values),
                        'exact_row_sum': sums.pop(), 'example': values[0]})
    far = [row(d) for d in [(0, 0, 6), (2, 2, 2), (4, 2, 0), (12, 0, 0)]]
    assert all(r['common_active_pairs'] == 0 for r in far)
    assert len({r['row_sum'] for r in far}) == 1
    assert all(r['maximum_active_vertex_distance_from_nearer_input'] <= 4 for r in rows+far)
    sums = [r['row_sum'] for r in rows+far]
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'helper_sha256': hashlib.sha256(Path('native_pair_controls.py').read_bytes()).hexdigest(),
              'scope': 'Personal exact unwrapped occupancy row sums, before independent check. Fixed-L spectral asymptotic and physical birth support require the separate proof.',
              'near_rows': rows, 'cubic_symmetry_groups': grouped, 'far_controls': far,
              'min_delta_Q_row_sum': min(sums), 'max_delta_Q_row_sum': max(sums),
              'proposed_all_L_at_least_10_g2_tau_gap_interval': [-max(sums)/4, -min(sums)/4],
              'elapsed_seconds': time.perf_counter()-start}
    p = Path('LOCAL_ROW_CERTIFICATE.json')
    p.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['cubic_symmetry_groups','far_controls',
          'min_delta_Q_row_sum','max_delta_Q_row_sum','proposed_all_L_at_least_10_g2_tau_gap_interval','elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
