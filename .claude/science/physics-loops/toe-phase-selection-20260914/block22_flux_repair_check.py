#!/usr/bin/env python3
"""Author falsifiers for the fixed-clock localization/repair derivation.

Finite arithmetic and controlled finite sums only. No infinite-volume
probability, phase theorem or independent review is certified by execution.
"""
import itertools as it
import json
import math
from collections import defaultdict, deque
import numpy as np
import mpmath as mp

D = 4
ORIGIN = (0,) * D


def shift(x, axis, amount=1):
    y = list(x)
    y[axis] += amount
    return tuple(y)


def clean(c):
    return {k: int(v) for k, v in c.items() if v}


def exterior(c):
    """Sparse primal exterior derivative, all canonical positively oriented cells."""
    out = defaultdict(int)
    for (x, axes), value in c.items():
        for a in range(D):
            if a in axes:
                continue
            full = tuple(sorted(axes + (a,)))
            sign = (-1) ** full.index(a)
            out[(shift(x, a, -1), full)] += sign * value
            out[(x, full)] -= sign * value
    return clean(out)


def boundary(c):
    out = defaultdict(int)
    for (x, axes), value in c.items():
        for i, a in enumerate(axes):
            reduced = axes[:i] + axes[i+1:]
            sign = (-1) ** i
            out[(shift(x, a), reduced)] += sign * value
            out[(x, reduced)] -= sign * value
    return clean(out)


def permutation_sign(axes):
    return (-1) ** sum(axes[i] > axes[j] for i in range(len(axes))
                      for j in range(i+1, len(axes)))


def star(c):
    out = {}
    for (x, axes), value in c.items():
        comp = tuple(i for i in range(D) if i not in axes)
        z = list(x)
        for i in comp:
            z[i] -= 1
        out[(tuple(z), comp)] = permutation_sign(axes + comp) * value
    return clean(out)


def inverse_star(c):
    out = {}
    for (z, axes), value in c.items():
        comp = tuple(i for i in range(D) if i not in axes)
        x = list(z)
        for i in axes:
            x[i] += 1
        out[(tuple(x), comp)] = permutation_sign(comp + axes) * value
    return clean(out)


def cycle_fill(j):
    assert not boundary(j)
    assert j
    vertices = [x for (x, _), v in j.items() if v]
    vertices += [shift(x, axes[0]) for (x, axes), v in j.items() if v]
    anchor = tuple(min(x[i] for x in vertices) for i in range(D))
    work = dict(j)
    surf = defaultdict(int)
    for i in range(D):
        projected = defaultdict(int)
        strips = defaultdict(int)
        for (x, axes), value in work.items():
            k = axes[0]
            assert k >= i
            if k == i:
                continue
            for r in range(anchor[i], x[i]):
                y = list(x)
                y[i] = r
                strips[(tuple(y), (i, k))] += value
            z = list(x)
            z[i] = anchor[i]
            projected[(tuple(z), axes)] += value
        projected, strips = clean(projected), clean(strips)
        residual = defaultdict(int, work)
        for key, value in projected.items():
            residual[key] -= value
        assert boundary(strips) == clean(residual), (i, 'strip identity')
        assert not boundary(projected)
        for key, value in strips.items():
            surf[key] += value
        work = projected
    assert not work
    surf = clean(surf)
    assert boundary(surf) == j
    return surf


def q_neighbors(cell):
    x, axes = cell
    comp = next(a for a in range(D) if a not in axes)
    # Both possible4-cell cofaces; then all of their3-faces.
    result = set()
    for z in (x, shift(x, comp, -1)):
        for a in range(D):
            others = tuple(i for i in range(D) if i != a)
            result.add((z, others))
            result.add((shift(z, a), others))
    result.discard(cell)
    return result


def components(q):
    remaining = set(q)
    parts = []
    while remaining:
        root = min(remaining)
        remaining.remove(root)
        queue, part = deque([root]), {root: q[root]}
        while queue:
            cell = queue.popleft()
            for neighbor in sorted(q_neighbors(cell) & remaining):
                remaining.remove(neighbor)
                part[neighbor] = q[neighbor]
                queue.append(neighbor)
        assert not exterior(part)
        parts.append(part)
    return parts


def repair(q):
    total = defaultdict(int)
    metadata = []
    for part in components(q):
        j = star(part)
        assert not boundary(j)
        surf = cycle_fill(j)
        n = {key: -value for key, value in inverse_star(surf).items()}
        assert exterior(n) == part
        mass = sum(abs(v) for v in part.values())
        assert sum(abs(v) for v in n.values()) <= 16 * mass * mass
        assert max(map(abs, n.values()), default=0) <= 4 * mass
        root = min(part)[0]
        assert all(max(abs(x[i] - root[i]) for i in range(D)) <= 6 * mass
                   for x, _ in n)
        for key, value in n.items():
            total[key] += value
        metadata.append({'mass': mass, 'charge_cells': len(part),
                         'fill_cells': len(n), 'fill_l1': sum(map(abs, n.values()))})
    total = clean(total)
    assert exterior(total) == q
    return total, metadata


def translated(c, delta):
    return {(tuple(x[i] + delta[i] for i in range(D)), axes): v
            for (x, axes), v in c.items()}


def principal_integer(n, order):
    # [-N/2,N/2), including the explicit even-N tie convention.
    return int((n + order // 2) % order - order // 2)


def finite_physical_checks():
    rng = np.random.default_rng(20260915)
    rows = []
    all_axes = list(it.combinations(range(D), 2))
    for seed in range(24):
        c = defaultdict(int)
        for _ in range(18):
            x = tuple(int(v) for v in rng.integers(-2, 3, size=D))
            c[(x, all_axes[int(rng.integers(len(all_axes)))])] += int(rng.integers(-3, 4))
        c = clean(c)
        q = exterior(c)
        assert not exterior(q)
        n, stats = repair(q)
        assert repair({key: -v for key, v in q.items()})[0] == {key: -v for key, v in n.items()}
        delta = (2, -3, 1, 4)
        assert repair(translated(q, delta))[0] == translated(n, delta)
        assert inverse_star(star(c)) == c
        # Sign convention is challenged independently by the differential identity.
        assert boundary(star(c)) == {key: -v for key, v in star(exterior(c)).items()}
        rows.append({'fixture': seed, 'components': len(stats),
                     'total_charge_mass': sum(abs(v) for v in q.values()),
                     'fill_l1': sum(map(abs, n.values()))})
    physical = []
    for order in (2, 3, 4, 5, 7):
        for trial in range(6):
            links = {}
            for x in it.product(range(2), repeat=D):
                for a in range(D):
                    v = int(rng.integers(order))
                    if v:
                        links[(x, (a,))] = v
            curl = exterior(links)
            b = clean({key: principal_integer(v, order) for key, v in curl.items()})
            db = exterior(b)
            assert all(v % order == 0 for v in db.values())
            q = {key: v // order for key, v in db.items()}
            n, stats = repair(q)
            lift = defaultdict(int, b)
            for key, v in n.items():
                lift[key] -= order * v
            lift = clean(lift)
            assert not exterior(lift)
            assert all((lift.get(key, 0) - b.get(key, 0)) % order == 0
                       for key in set(lift) | set(b))
            # Integer Wilson surfaces, including an explicitly added cube boundary.
            for _ in range(8):
                x = tuple(int(v) for v in rng.integers(-1, 3, size=D))
                axes = tuple(sorted(int(v) for v in rng.choice(D, size=3, replace=False)))
                bd = boundary({(x, axes): 1})
                assert sum(lift.get(key, 0) * v for key, v in bd.items()) == 0
                assert sum(b.get(key, 0) * v for key, v in bd.items()) % order == 0
            physical.append({'N': order, 'trial': trial, 'charge_mass': sum(map(abs, q.values())),
                             'components': len(stats), 'lift_nonzero': len(lift)})
    return {'integer_fill_fixtures': rows, 'actual_clock_flux_fixtures': physical}


def geometry_checks():
    p = (ORIGIN, (0, 1))
    comp = (2, 3)
    cofaces = []
    for bits in it.product((0, -1), repeat=2):
        z = list(ORIGIN)
        for a, bit in zip(comp, bits):
            z[a] += bit
        cofaces.append(tuple(z))
    neighbors = set()
    for z in cofaces:
        for axes in it.combinations(range(D), 2):
            omitted = [i for i in range(D) if i not in axes]
            for bits in it.product((0, 1), repeat=2):
                x = list(z)
                for a, bit in zip(omitted, bits):
                    x[a] += bit
                neighbors.add((tuple(x), axes))
    neighbors.discard(p)
    assert len(neighbors) <= 92
    assert len(q_neighbors((ORIGIN, (0, 1, 2)))) == 14
    incident_cubes = set()
    for a in comp:
        incident_cubes.add((ORIGIN, tuple(sorted((0, 1, a)))))
        incident_cubes.add((shift(ORIGIN, a, -1), tuple(sorted((0, 1, a)))))
    assert len(incident_cubes) == 4
    assert len(cofaces) == 4
    return {'bad_plaquette_graph_actual_degree': len(neighbors),
            'used_degree_bound': 92, 'charge_graph_degree': 14,
            'plaquette_incident_3cells': 4, 'plaquette_incident_4cells': 4}


def cube_complex(d):
    cells = []
    for degree in range(d+1):
        layer = []
        for axes in it.combinations(range(d), degree):
            for x in it.product(*[(0,) if a in axes else (0, 1) for a in range(d)]):
                layer.append((x, axes))
        cells.append(layer)
    incidence = []
    for degree in range(d):
        index = {cell: i for i, cell in enumerate(cells[degree])}
        m = np.zeros((len(cells[degree+1]), len(cells[degree])), dtype=int)
        for row, (x, axes) in enumerate(cells[degree+1]):
            for i, a in enumerate(axes):
                other = axes[:i] + axes[i+1:]
                xp = list(x); xp[a] += 1
                m[row, index[(tuple(xp), other)]] += (-1) ** i
                m[row, index[(x, other)]] -= (-1) ** i
        incidence.append(m)
    return cells, incidence


def small_clock_bound_checks():
    cells, ds = cube_complex(3)
    # A tree is selected by its independent vertex incidence rows; curl columns
    # not in that tree are the exact five gauge-fixed clock coordinates.
    d0, d1 = ds[:2]
    tree = []
    rank = 0
    for e in range(len(cells[1])):
        candidate = d0[tree + [e], :].astype(float)
        new_rank = np.linalg.matrix_rank(candidate)
        if new_rank > rank:
            tree.append(e); rank = new_rank
    cols = [e for e in range(len(cells[1])) if e not in tree]
    assert len(tree) == 7 and len(cols) == 5
    mat = d1[:, cols]
    mp.mp.dps = 60
    rows = []
    for order, beta0 in ((3, 2), (3, 5), (4, 2), (5, 2), (3, 20)):
        beta = mp.mpf(beta0)
        vals = []
        images = range(-8, 9)
        for residue in range(order):
            u = 2 * mp.pi * principal_integer(residue, order) / order
            w = sum(mp.exp(-beta*(u-2*mp.pi*k)**2/2) for k in images)
            w2 = sum(mp.exp(-beta*(u-2*mp.pi*k)**2/2) for k in range(-11, 12))
            assert abs(w-w2) < mp.mpf('1e-55')
            vals.append(w)
        prob_sums = [mp.mpf(0) for _ in range(64)]
        norm = mp.mpf(0)
        charge_prob = mp.mpf(0)
        for ell in it.product(range(order), repeat=5):
            residues = (mat @ np.asarray(ell, dtype=int)) % order
            bs = [principal_integer(int(r), order) for r in residues]
            weight = math.prod(vals[int(r)] for r in residues)
            norm += weight
            mask = sum((1 << i) for i, b in enumerate(bs) if 6 * abs(b) >= order)
            # eta=pi/3 means2pi|b|/N>=pi/3, including exact equality.
            subset = mask
            while True:
                prob_sums[subset] += weight
                if subset == 0:
                    break
                subset = (subset-1) & mask
            q = int(ds[2][0] @ np.asarray(bs, dtype=int))
            assert q % order == 0
            if q:
                charge_prob += weight
        max_ratio = mp.mpf(0)
        for mask in range(1, 64):
            size = mask.bit_count()
            probability = prob_sums[mask] / norm
            upper = 2**size * mp.exp(-beta * mp.pi**2 * size / 18)
            assert probability <= upper * (1 + mp.mpf('1e-45'))
            max_ratio = max(max_ratio, probability/upper)
        physical_charge = charge_prob/norm
        charge_upper = 12 * mp.exp(-beta*mp.pi**2/18)
        assert physical_charge <= charge_upper
        rows.append({'N': order, 'beta': beta0, 'states': order**5,
                     'all_nonempty_bad_subsets': 63, 'max_probability_to_bound': str(max_ratio),
                     'physical_magnetic_charge_probability': str(physical_charge)})
    return rows


def large_rectangle_control():
    # Generic closed integer charge, to challenge deterministic finite range.
    # It is not asserted to be an actual principal-flux charge configuration.
    radius = 7
    surface = {((0, 0, x, y), (2, 3)): 1
               for x in range(-radius, radius) for y in range(-radius, radius)}
    j = boundary(surface)
    q = inverse_star(j)
    assert not exterior(q)
    n, stats = repair(q)
    center = ((0, 0, 1, 1), (0, 1))
    # Shift due to inverse duality is explicit in this coordinate choice.
    interior_keys = [key for key in n if max(abs(a) for a in key[0]) <= 2]
    assert interior_keys
    key = min(interior_keys)
    assert n[key]
    local_q = {cell: v for cell, v in q.items()
               if max(abs(cell[0][i]-key[0][i]) for i in range(D)) <= 3}
    assert not local_q
    assert repair(local_q)[0].get(key, 0) == 0
    return {'radius': radius, 'charge_mass': sum(map(abs, q.values())),
            'fill_l1': sum(map(abs, n.values())), 'interior_cell': key,
            'full_fill_value': n[key], 'radius3_visible_charge_cells': 0,
            'scope': 'generic closed-charge representative; no physical principal-lift claim'}


def analytic_bound_controls():
    for m in range(1, 31):
        for k in range(1, 31):
            assert 2 * max(m, k)**2 >= k * (m+k)
    beta = 20
    r = 2 * 92**2 * math.exp(-beta*math.pi**2/18)
    assert 0 < r < 0.5
    nd = math.ceil(40*math.pi)
    beta_dual = nd**2/(4*math.pi**2*beta)
    assert beta_dual >= 20
    return {'beta': beta, 'physical_bad_cluster_ratio': r,
            'charge_mass_decay_rate': -math.log(r)/12,
            'fixed_N_example': nd, 'beta_dual': beta_dual,
            'auxiliary_mass_threshold': 16*math.log(392)/math.pi**2,
            'physical_bad_threshold': 18*math.log(2*92**2)/math.pi**2}


def run():
    result = {'status': 'finite author checks; proof and independent review remain separate',
              'geometry': geometry_checks(), 'bounds': analytic_bound_controls(),
              'algebra': finite_physical_checks(),
              'small_actual_clock_probabilities': small_clock_bound_checks(),
              'non_finite_range_control': large_rectangle_control()}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
