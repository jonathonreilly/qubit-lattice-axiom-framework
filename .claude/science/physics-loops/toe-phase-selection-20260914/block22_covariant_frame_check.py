#!/usr/bin/env python3
"""Private finite checks; imports the paired block22 sparse-algebra helper.

No independent review, infinite-state frame theorem, mixing or photon claim.
"""
import itertools as it
import json
from collections import defaultdict
import numpy as np
from block22_flux_repair_check import (D, ORIGIN, boundary, clean, components,
    exterior, permutation_sign, principal_integer, repair, shift)


def group():
    gs = []
    for perm in it.permutations(range(D)):
        for signs in it.product((-1, 1), repeat=D):
            g = np.zeros((D, D), dtype=int)
            for i in range(D):
                g[perm[i], i] = signs[i]
            gs.append(g)
    assert len(gs) == 384
    assert len({tuple(g.ravel()) for g in gs}) == 384
    return gs


def transform(c, g, t=ORIGIN):
    g, t = np.asarray(g, dtype=int), np.asarray(t, dtype=int)
    target = [int(np.flatnonzero(g[:, i])[0]) for i in range(D)]
    sign = [int(g[target[i], i]) for i in range(D)]
    out = {}
    for (x, axes), value in c.items():
        y = g @ np.asarray(x) + t
        axis_word = tuple(target[i] for i in axes)
        s = permutation_sign(axis_word)
        for i in axes:
            s *= sign[i]
            if sign[i] < 0:
                y[target[i]] -= 1
        key = (tuple(int(v) for v in y), tuple(sorted(axis_word)))
        assert key not in out
        out[key] = s * value
    return clean(out)


def vertices(c):
    ans = set()
    for x, axes in c:
        for bits in it.product((0, 1), repeat=len(axes)):
            y = list(x)
            for a, bit in zip(axes, bits):
                y[a] += bit
            ans.add(tuple(y))
    return sorted(ans)


def word(c, delta, sign, n):
    ans = []
    for (x, axes), value in c.items():
        residue = sign * value % n
        if residue:
            y = tuple(x[i] + delta[i] for i in range(D))
            key = (max(map(abs, y)), y, axes)
            ans.append((key, residue))
    ans.sort()
    return ans


def compare(a, b):
    """Lex compare infinite words represented by their finite nonzero entries."""
    i = j = 0
    while i < len(a) and j < len(b):
        ka, va = a[i]; kb, vb = b[j]
        if ka < kb:
            return 1, ka[0]  # b is zero at this earlier nonzero a entry
        if kb < ka:
            return -1, kb[0]
        if va != vb:
            return (-1 if va < vb else 1), ka[0]
        i += 1; j += 1
    if i < len(a):
        return 1, a[i][0][0]
    if j < len(b):
        return -1, b[j][0][0]
    return 0, 0


def winner(b, gamma, n, gs):
    origins = vertices(gamma)
    best = record = None
    count = ties = radius = 0
    for gi, g in enumerate(gs):
        rotated = transform(b, g.T)
        for origin in origins:
            delta = tuple(int(v) for v in -g.T @ np.asarray(origin))
            for sign in (-1, 1):
                code = word(rotated, delta, sign, n)
                count += 1
                if best is None:
                    best = code; record = (origin, g, sign); ties = 1
                    continue
                order, diff_radius = compare(code, best)
                radius = max(radius, diff_radius)
                if order < 0:
                    best = code; record = (origin, g, sign); ties = 1
                elif order == 0:
                    ties += 1
    assert ties == 1, ('global minimum frame tie', ties)
    origin, g, sign = record
    pulled = transform(gamma, g.T, -g.T @ np.asarray(origin))
    pulled = {key: sign * value for key, value in pulled.items()}
    fill = repair(pulled)[0]
    cov = {key: sign * value for key, value in transform(fill, g, origin).items()}
    assert exterior(cov) == gamma
    return cov, record, {'candidates': count, 'origin_vertices': len(origins),
                         'minimum_ties': ties, 'certifying_prefix_radius_upper': radius,
                         'origin': origin, 'frame': g.tolist(), 'conjugation_sign': sign}


def fixture(n=3):
    links = {(ORIGIN, (0,)): 1, ((1, 0, 0, 0), (1,)): 1,
             ((3, 1, 2, 0), (3,)): 1, ((-2, 4, 0, 1), (0,)): -1,
             ((0, -3, 2, 4), (1,)): 1, ((2, 0, -4, 1), (2,)): -1}
    b = clean({key: principal_integer(v, n) for key, v in exterior(links).items()})
    db = exterior(b)
    assert all(v % n == 0 for v in db.values())
    q = {key: v//n for key, v in db.items()}
    parts = components(q)
    assert len(parts) == 1
    assert sum(map(abs, q.values())) == 4
    return links, b, q


def cell_edges(cell):
    return set(boundary({cell: 1}))


def line_geometry(gs):
    v = np.array((1, 4, 16, 64), dtype=int)
    assert len({tuple(g @ v) for g in gs}) == 384
    L, M = 16384, 4
    ns = list(range((L+255)//256, L//128+1))
    assert len(ns) >= L/512
    identity = np.eye(D, dtype=int)
    max_degree = 0
    min_kept = len(ns)
    tested = 0
    for g in gs:
        for delta in ((0, 0, 0, 0), (1, 0, 0, 0), (3, -2, 1, 0)):
            if np.array_equal(g, identity) and delta == ORIGIN:
                continue
            supports = []
            for n in ns:
                cell = (tuple(int(x) for x in n*v), (0, 1))
                other = next(iter(transform({cell: 1}, g, delta)))
                e1, e2 = cell_edges(cell), cell_edges(other)
                assert e1 != e2
                assert (e1-e2) or (e2-e1)
                supports.append(e1 | e2)
            owners = defaultdict(list)
            for i, support in enumerate(supports):
                for edge in support:
                    owners[edge].append(i)
            assert max(map(len, owners.values())) <= 2
            graph = [set() for _ in supports]
            for ids in owners.values():
                for i in ids:
                    graph[i].update(j for j in ids if j != i)
            degree = max(map(len, graph))
            assert degree <= 8
            remaining = set(range(len(supports)))
            kept = []
            while remaining:
                root = min(remaining)
                kept.append(root)
                remaining -= graph[root] | {root}
            assert len(kept) >= len(ns)/9
            max_degree = max(max_degree, degree)
            min_kept = min(min_kept, len(kept))
            tested += 1
    return {'signed_permutation_v_orbit': 384, 'pair_geometries': tested,
            'code_radius': L, 'component_mass_budget': M, 'comparison_sites': len(ns),
            'max_conflict_degree_seen': max_degree, 'minimum_independent_comparisons': min_kept,
            'proof_degree_bound': 8, 'proof_independent_lower': L/9216}


def run():
    gs = group()
    links, b, q = fixture()
    cov, original, result = winner(b, q, 3, gs)
    tests = []
    rotations = [np.eye(D, dtype=int),
                 np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]),
                 np.array([[0,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]]),
                 np.diag((1,1,1,-1))]
    for i, h in enumerate(rotations):
        displacement = (2, -3, 1, 4)
        sign = -1 if i % 2 else 1
        lb = {key: sign * val for key, val in transform(links, h, displacement).items()}
        bb = clean({key: principal_integer(v, 3) for key, v in exterior(lb).items()})
        qq = {key: v//3 for key, v in exterior(bb).items()}
        assert bb == {key: sign * val for key, val in transform(b, h, displacement).items()}
        assert qq == {key: sign * val for key, val in transform(q, h, displacement).items()}
        ncov, rec, info = winner(bb, qq, 3, gs)
        expected = {key: sign*val for key, val in transform(cov, h, displacement).items()}
        assert ncov == expected
        old_origin, old_g, old_s = original
        new_origin, new_g, new_s = rec
        assert new_origin == tuple(int(x) for x in h @ np.asarray(old_origin)+displacement)
        assert np.array_equal(new_g, h @ old_g)
        assert new_s == sign * old_s
        tests.append({'case': i, 'external_determinant': int(round(np.linalg.det(h))),
                      'external_charge_conjugation': sign,
                      'minimum_prefix_radius_upper': info['certifying_prefix_radius_upper']})
    print(json.dumps({'status': 'private finite author checks; independent review pending',
                      'actual_N3_fixture': result, 'covariance_cases': tests,
                      'comparison_geometry': line_geometry(gs)}, indent=2))


if __name__ == '__main__':
    run()
