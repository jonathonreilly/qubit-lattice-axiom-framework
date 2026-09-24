"""Finite count combinatorics only; no simulation of cubic matter/field dynamics."""
from itertools import combinations
import json
import math
import time

import numpy as np


def overlap_square(h, b):
    """Integrate the square of |[0,h] intersect (t-b,t)| piecewise."""
    nodes, weights = np.polynomial.legendre.leggauss(3)
    cuts = sorted(set([0.0, h, b, h + b]))
    integral = 0.0
    for left, right in zip(cuts, cuts[1:]):
        for x, w in zip(nodes, weights):
            t = (left + right) / 2 + (right - left) * x / 2
            length = max(0.0, min(h, t) - max(0.0, t - b))
            integral += (right - left) * w * length * length / 2
    return integral


def poisson_moment_controls():
    rows = []
    for h, b in [(0.4, 0.3), (0.2, 0.7), (0.5, 0.5), (1.0, 0.02)]:
        exact = min(h, b) ** 2 * max(h, b) - min(h, b) ** 3 / 3
        quadrature = overlap_square(h, b)
        assert abs(exact - quadrature) < 1e-14
        assert exact <= h * b * b + 1e-14
        for rj, rl in [(0.02, 0.03), (2.0, 3.0), (20.0, 30.0)]:
            mu = rj * rl * h * b
            second = mu * mu + mu + rj * rl * rl * h * b * b + rj * rj * rl * exact
            upper = mu * mu + mu * (1 + (rj + rl) * b)
            assert second <= upper + 1e-10
            variance = second - mu * mu
            assert variance >= mu - 1e-12
            rows.append(dict(h=h, b=b, r_j=rj, r_l=rl, mean=mu,
                             overlap_square_exact=exact,
                             overlap_square_quadrature=quadrature,
                             second_moment=second, proposed_second_bound=upper,
                             variance=variance,
                             bernoulli_variance_formula=mu * (1 - mu)))
    assert any(r['bernoulli_variance_formula'] < 0 for r in rows)
    return rows


def bin_pair_bounds(times, labels, bins, interval, lag):
    """Closed bin hulls give conservative bounds; word order resolves zero lag."""
    left, right = interval
    step = 1.0 / bins
    lower = actual = upper = 0
    for first, second in combinations(range(len(times)), 2):
        if labels[first] != 'j' or labels[second] != 'l':
            continue
        s, t = times[first], times[second]
        actual += int(left <= s <= right and 0 < t - s <= lag)
        i = min(math.floor(s / step), bins - 1)
        k = min(math.floor(t / step), bins - 1)
        slo, shi = i * step, (i + 1) * step
        tlo, thi = k * step, (k + 1) * step
        # Given the stored order, actual lag is positive even within a bin.
        lag_max = thi - slo
        lag_min = max(0.0, tlo - shi)
        forced = slo >= left and shi <= right and lag_max <= lag
        permitted = shi >= left and slo <= right and lag_min <= lag
        lower += int(forced)
        upper += int(permitted)
    return lower, actual, upper


def register_window_controls():
    labels = ['other', 'j', 'other', 'l', 'j', 'l']
    points = [0.03, 0.11, 0.20, 0.29, 0.38, 0.50, 0.60, 0.71, 0.83, 0.97]
    interval, lag = (0.2, 0.6), 0.3
    cap = len(labels) * (len(labels) - 1) // 2
    rows = []
    for bins in [4, 8, 16, 32]:
        checked = ambiguity = exact = square_gap = max_count = 0
        example = None
        for length in range(len(labels) + 1):
            for times in combinations(points, length):
                lower, count, upper = bin_pair_bounds(times, labels[:length], bins,
                                                     interval, lag)
                assert 0 <= lower <= count <= upper <= cap
                assert upper * upper - lower * lower <= 2 * cap * (upper - lower)
                checked += 1
                ambiguity += upper - lower
                square_gap += upper * upper - lower * lower
                exact += int(lower == upper)
                max_count = max(max_count, count)
                if count > 1 and example is None:
                    example = dict(times=times, labels=labels[:length],
                                   lower=lower, actual=count, upper=upper)
        assert max_count > 1
        rows.append(dict(bins=bins, mesh=1 / bins, histories_checked=checked,
                         aggregate_bracket_gap=ambiguity,
                         aggregate_square_bracket_gap=square_gap,
                         exact_brackets=exact, maximum_actual_count=max_count,
                         multiple_count_example=example))
    # These nested partitions must improve the information on every history.
    monotone_checks = 0
    for length in range(len(labels) + 1):
        for times in combinations(points, length):
            bounds = [bin_pair_bounds(times, labels[:length], bins, interval, lag)
                      for bins in [4, 8, 16, 32]]
            assert all(a[0] <= b[0] and b[2] <= a[2]
                       for a, b in zip(bounds, bounds[1:]))
            monotone_checks += 1
    return dict(rows=rows, nested_partition_histories=monotone_checks,
                event_cap=len(labels), universal_pair_cap=cap,
                interval=interval, lag=lag)


def main():
    start = time.perf_counter()
    payload = dict(
        scope='Exact Poisson proposal moments and finite-history bin inequalities only. '
              'No original cubic dynamics, LR proof, microscopic rate, physical detector, '
              'or empirical data comparison is numerically established.',
        poisson_proposal_rows=poisson_moment_controls(),
        finite_history_register=register_window_controls(),
        elapsed_seconds=time.perf_counter() - start,
        checks_passed=['piecewise_overlap_integral', 'proposal_second_moment_bound',
                       'non_bernoulli_count_example', 'count_window_brackets',
                       'square_bracket_bound', 'nested_partition_monotonicity'])
    print(json.dumps(payload, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
