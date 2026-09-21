#!/usr/bin/env python3
"""Author controls for the moving-geometry color-wave extension.

Finite evidence for actual record motion and the conditional energy estimate;
the all-volume argument remains the separately supplied proof.
"""
from pathlib import Path
from collections import Counter
import datetime, hashlib, itertools, json
import numpy as np
from scipy.linalg import expm
import dimer_routed_transport_check as base

HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def geometric_controls():
    rows = []
    for N in (8, 10, 12):
        for kind in ('winding', 'columnar', 'irregular'):
            partner, accepted = base.matching(
                N, 8*N**3 if kind == 'irregular' else 0, 77200+N,
                winding=kind == 'winding')
            xyz, index, nb, black, white, d, q, inv = base.routing(N, partner)
            K = len(black)
            black_index = np.full(N**3, -1, dtype=int)
            black_index[black] = np.arange(K)
            ids = np.empty(N**3, dtype=int)
            ids[black] = 2*np.arange(K)
            ids[white] = 2*np.arange(K)+1
            channels = Counter(tuple(sorted((u, int(v))))
                               for z in q for u, v in enumerate(z) if u != v)
            square_edges = Counter()
            replayed = 0
            max_fourier_ratio = 0.0
            for a in range(N**3):
                for i, j in itertools.combinations(range(3), 2):
                    b, dd = int(nb[2*i, a]), int(nb[2*j, a])
                    c = int(nb[2*j, b])
                    vertices = np.array([a, b, c, dd])
                    horizontal = partner[a] == b and partner[dd] == c
                    vertical = partner[a] == dd and partner[b] == c
                    if not (horizontal or vertical):
                        continue
                    diagonal = vertices[(xyz[vertices].sum(axis=1) % 2) == 0]
                    pair_edge = tuple(sorted(map(int, black_index[diagonal])))
                    square_edges[pair_edge] += 1
                    assert channels[pair_edge] >= 1
                    projections = []
                    target = {a: dd, dd: a, b: c, c: b} if horizontal else {
                        a: b, b: a, dd: c, c: dd}
                    for sense in (-1, 1):
                        new_ids = np.roll(ids[vertices], sense)
                        location = {int(key): int(site)
                                    for key, site in zip(new_ids, vertices)}
                        assert set(location) == set(map(int, ids[vertices]))
                        assert all(location[int(key)^1] == target[int(site)]
                                   for key, site in zip(new_ids, vertices))
                        for old, new in zip(vertices, np.roll(vertices, -sense)):
                            # The roll assignment moves the old item to +sense.
                            assert new in nb[:, old]
                        new_by_site = dict(zip(map(int, vertices), map(int, new_ids)))
                        projections.append(tuple(new_by_site[int(v)]//2 for v in diagonal))
                        replayed += 1
                    old_colors = tuple(map(int, ids[diagonal]//2))
                    assert set(projections) == {old_colors, old_colors[::-1]}
                    # Four signed positively oriented links of the geometric
                    # B field. A sign change of occupation reverses orientation.
                    edges = [(a, b, i), (dd, c, i), (a, dd, j), (b, c, j)]
                    delta = []
                    divergence = Counter()
                    for start, end, axis in edges:
                        occupation_change = int(target[start] == end)-int(partner[start] == end)
                        value = (1-2*int(xyz[start].sum()%2))*occupation_change
                        delta.append((start, axis, value))
                        divergence[start] += value
                        divergence[end] -= value
                    assert all(v == 0 for v in divergence.values())
                    assert all(sum(v for _, ax, v in delta if ax == axis) == 0
                               for axis in range(3))
                    for integer_mode in ((1, 0, 0), (0, 1, 0), (1, 1, 1)):
                        Q = 2*np.pi*np.array(integer_mode)
                        increment = np.zeros(3, dtype=complex)
                        for start, axis, value in delta:
                            midpoint = xyz[start] + np.eye(3)[axis]/2
                            increment[axis] += value*np.exp(-1j*Q@midpoint/N)/np.sqrt(N**3)
                        # Each component is a difference over a unit transverse
                        # displacement; sum of two squared components <= |Q|^2.
                        ratio = float(np.vdot(increment, increment).real*N**5/(Q@Q))
                        max_fourier_ratio = max(max_fourier_ratio, ratio)
                        assert ratio <= 1+2e-12
                        symbol = 2j*np.sin(Q/(2*N))
                        assert abs(symbol@increment) < 2e-14
            assert max(square_edges.values(), default=0) <= 1
            if kind != 'winding':
                assert replayed > 0
            else:
                assert replayed == 0
            # D_K=(nu/2) sum square E Delta^2, while
            # D_S=(k0/4) sum directed-channel E Delta^2.
            # Comparing these nonnegative coefficients proves the finite
            # all-function form inequality, without sampling test functions.
            assert all(count <= channels[edge] for edge, count in square_edges.items())
            rows.append(dict(N=N, kind=kind, pairs=K,
                             accepted_geometry_flips=accepted,
                             flippable_squares=sum(square_edges.values()),
                             immutable_rotation_replays=replayed,
                             maximum_scaled_geometric_increment=max_fourier_ratio,
                             exact_color_projections_and_form_coefficients=True))
    return dict(rows=rows)


def switched_energy_controls():
    rng = np.random.default_rng(19062026)
    rows = []
    for trial in range(40):
        k = 4+trial%3
        intervals = 1+trial%8
        p = np.ones(k)/k
        m = np.zeros(k)
        n = np.zeros(k)
        bound = 0.0
        witnesses = []
        for interval in range(intervals):
            # Every directed cycle is balanced; symmetric complete exchanges
            # give a common uniform law and a strictly positive sector gap.
            Q = np.zeros((k, k))
            for i in range(k):
                for j in range(i+1, k):
                    rate = float(rng.integers(1, 6))/10
                    Q[i, j] += rate
                    Q[j, i] += rate
            order = rng.permutation(k)
            for i, j in zip(order, np.roll(order, -1)):
                Q[i, j] += .7
            np.fill_diagonal(Q, -Q.sum(axis=1))
            assert np.max(abs(Q.sum(axis=0))) < 2e-14
            f = rng.integers(-7, 8, size=k).astype(float)
            f -= f.mean()
            duration = float(rng.integers(1, 15))/10
            S = (Q+Q.T)/2
            hminus = float(f@np.linalg.solve(-S+np.ones((k, k))/k, f)/k)
            bound += 2*duration*hminus
            F = np.diag(f)
            operator = np.block([[Q.T, np.zeros((k, k)), np.zeros((k, k))],
                                 [F, Q.T, np.zeros((k, k))],
                                 [np.zeros((k, k)), 2*F, Q.T]])
            result = expm(duration*operator)@np.r_[p, m, n]
            p, m, n = np.split(result, 3)
            assert np.max(abs(p-1/k)) < 3e-13
            assert abs(m.sum()) < 3e-12
            if interval+1 < intervals:
                # Arbitrary prescribed boundary permutations preserve pi;
                # carried additive moments must move with the color state.
                permutation = rng.permutation(k)
                p, m, n = p[permutation], m[permutation], n[permutation]
            witnesses.append(dict(duration=duration, hminus=hminus))
        second_moment = float(n.sum())
        assert second_moment >= -1e-11
        assert second_moment <= bound+1e-10
        rows.append(dict(states=k, intervals=intervals,
                         integral_second_moment=second_moment,
                         energy_upper_bound=bound,
                         ratio=second_moment/bound if bound else 0,
                         interval_witnesses=witnesses))
    return dict(rows=rows, numerical_matrix_exponential_control=True,
                maximum_ratio=max(row['ratio'] for row in rows))


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE/'dimer_routed_moving_geometry_checks')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = dict(status='pass', completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  sources={name: sha(HERE/name) for name in (
                      'DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md',
                      'DIMER_ROUTED_RECORD_TRANSPORT.md',
                      'DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md',
                      'dimer_routed_moving_geometry_check.py',
                      'dimer_routed_transport_check.py')})
    for name, check in [('geometry_and_dirichlet', geometric_controls),
                        ('switched_energy', switched_energy_controls)]:
        result[name] = check()
        (args.output/(name+'.json')).write_text(json.dumps(result[name], indent=2)+'\n')
        print(name, 'PASS', flush=True)
    (args.output/'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
