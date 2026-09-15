#!/usr/bin/env python3
"""Finite author falsifiers for the large-beta fixed-clock score control.

This private runner imports the block22 sparse-cell helper. It checks exact
geometry, finite laws and controlled sums; it does not certify the proposed
infinite-volume dependence estimate, CLT, or an independent review.
"""
import itertools as it
import json
import math
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp
import block22_flux_repair_check as h


def plaquette_neighbors(cell):
    x, axes = cell
    neighbors = set()
    for a in range(4):
        if a in axes:
            continue
        full = tuple(sorted(axes + (a,)))
        for z in (x, h.shift(x, a, -1)):
            neighbors.update(h.boundary({(z, full): 1}))
    neighbors.discard(cell)
    return neighbors


def variance_patch():
    links = {(h.ORIGIN, (0,)): 1, (h.shift(h.ORIGIN, 0), (1,)): 1}
    curl = h.exterior(links)
    principal = h.clean({cell: h.principal_integer(v, 3)
                         for cell, v in curl.items()})
    patch = set()
    for cell in curl:
        patch.update(h.boundary({cell: 1}))
    interactions = set()
    for cell in patch:
        interactions.update(h.exterior({cell: 1}))
    assert len(patch) == 30
    assert len(curl) == 11
    assert len(interactions) == 106 <= 6 * len(patch)
    assert all(set(h.boundary({cell: 1})) <= patch for cell in curl)
    assert set(links) <= patch
    assert len([v for v in curl.values() if abs(v) > 1]) == 1
    assert curl[(h.ORIGIN, (0, 1))] == 2
    assert principal[(h.ORIGIN, (0, 1))] == -1
    curl_sums = [sum(v for (x, axes), v in curl.items() if axes == pair)
                 for pair in it.combinations(range(4), 2)]
    principal_sums = [sum(v for (x, axes), v in principal.items() if axes == pair)
                      for pair in it.combinations(range(4), 2)]
    assert curl_sums == [0] * 6
    assert principal_sums == [-3, 0, 0, 0, 0, 0]
    q = h.exterior(principal)
    assert len(q) == 4 and sum(abs(v // 3) for v in q.values()) == 4
    assert not h.exterior(q)

    bounds = [(min(x[i] for x, axes in interactions),
               max(x[i] for x, axes in interactions)) for i in range(4)]
    assert all(hi - lo <= 3 for lo, hi in bounds)
    # These bounding intervals prove disjointness for EVERY nonzero 8Z4
    # translation; the explicit nearest translations challenge the predicate.
    for delta0 in it.product((-1, 0, 1), repeat=4):
        if not any(delta0):
            continue
        delta = tuple(8 * v for v in delta0)
        moved = {(tuple(x[i] + delta[i] for i in range(4)), axes)
                 for x, axes in interactions}
        assert interactions.isdisjoint(moved)
    assert len(plaquette_neighbors((h.ORIGIN, (0, 1)))) == 20
    assert all(max(abs(x[i]) for i in range(4)) <= 1
               for x, axes in plaquette_neighbors((h.ORIGIN, (0, 1))))
    return {'patch_links': len(patch), 'changed_plaquettes': len(curl),
            'interaction_plaquettes': len(interactions),
            'interaction_base_bounds': bounds, 'spacing': 8,
            'checked_nearest_patch_translations': 80,
            'all_translations_argument': 'each base interval has width at most 3 < 8',
            'curl_plane_sums': curl_sums, 'principal_plane_sums': principal_sums,
            'magnetic_charge_mass': 4, 'plaquette_graph_degree': 20}


def exact_finite_polymer_law():
    cells, ds = h.cube_complex(3)
    d0, d1, d2 = ds
    # Independent columns are chosen only to enumerate the finite gauge-fixed
    # law; the statement about infinite-volume conditioning uses original links.
    tree = []
    for e in range(len(cells[1])):
        candidate = tree + [e]
        if sp.Matrix(d0[candidate, :]).rank() > len(tree):
            tree.append(e)
    remaining = [e for e in range(len(cells[1])) if e not in tree]
    assert len(tree) == 7 and len(remaining) == 5
    weights = (Fraction(1), Fraction(1, 7), Fraction(1, 7))
    original = {}
    for ell in it.product(range(3), repeat=5):
        b = tuple(int(v) for v in (d1[:, remaining] @ np.array(ell)) % 3)
        assert b not in original
        original[b] = math.prod(weights[v] for v in b)
    closed = {}
    polymers = {}
    for b in it.product(range(3), repeat=6):
        if int(d2[0] @ np.array(b)) % 3:
            continue
        weight = math.prod(weights[v] for v in b)
        closed[b] = weight
        if any(b):
            # All six faces share this cube: any nonempty support is one
            # connected polymer and all distinct polymers are incompatible.
            polymers[b] = weight
    assert original == closed
    assert len(original) == 243 and len(polymers) == 242
    partition = sum(closed.values(), Fraction(0))
    assert partition == 1 + sum(polymers.values(), Fraction(0))
    empty_prob = 1 / partition
    for b, activity in polymers.items():
        probability = closed[b] / partition
        assert empty_prob * activity == probability * 1
    return {'clock_order': 3, 'closed_fields': len(closed),
            'tree_fixed_link_fields': len(original), 'nonempty_polymers': len(polymers),
            'weights': ['1', '1/7', '1/7'], 'partition_exact': str(partition),
            'detailed_balance_edges': len(polymers),
            'scope': 'exact positive-weight law algebra on one free 3-cube'}


def free_boundary_control():
    cells, ds = h.cube_complex(4)
    ell = np.zeros(len(cells[1]), dtype=int)
    ell[cells[1].index((h.ORIGIN, (0,)))] = 1
    b0 = ds[1] @ ell
    assert not np.any(ds[2] @ b0)
    b = {(x, axes): int(v) for (x, axes), v in zip(cells[2], b0) if v}
    assert len(b) == 3
    outside_charge = h.exterior(b)
    assert outside_charge
    assert any(v % 3 for v in outside_charge.values())
    assert not (set(outside_charge) & set(cells[3]))
    return {'finite_4cube_nonzero_plaquettes': len(b),
            'finite_domain_closure': True,
            'zero_extension_closure': False,
            'outside_nonzero_3cells': len(outside_charge),
            'reason': 'universal proposals need separate finite and infinite validity filters'}


def analytic_constants_and_score():
    mp.mp.dps = 90
    rows = []
    for beta0 in (1, 2, 5, 20, 30):
        beta = mp.mpf(beta0)
        u = 2 * mp.pi / 3

        def images(cutoff):
            vals = []
            deriv = []
            for r in (0, 1, -1):
                angle = u * r
                terms = [mp.exp(-beta * (angle - 2 * mp.pi * k)**2 / 2)
                         for k in range(-cutoff, cutoff + 1)]
                vals.append(sum(terms))
                deriv.append(sum(-beta * (angle - 2 * mp.pi * k) * value
                                 for k, value in zip(range(-cutoff, cutoff + 1), terms)))
            return vals, deriv

        vals, deriv = images(8)
        vals2, deriv2 = images(11)
        assert all(abs(x-y) < mp.mpf('1e-85')
                   for x, y in zip(vals + deriv, vals2 + deriv2))
        alpha = (vals[1] + vals[2]) / vals[0]
        alpha_upper = 4 * mp.exp(-2 * mp.pi**2 * beta / 9) / (1-mp.exp(-2*mp.pi**2*beta))
        assert 0 < alpha <= alpha_upper
        y = -deriv[1] / (mp.sqrt(beta) * vals[1])
        assert y > 0
        assert abs(y + (-deriv[2] / (mp.sqrt(beta) * vals[2]))) < mp.mpf('1e-85')
        ratio = sum((3*n-1)*mp.exp(-2*mp.pi**2*beta*(n*n-mp.mpf(2)*n/3))
                    for n in range(1, 15))
        r = mp.exp(-2*mp.pi**2*beta/3)
        ratio_upper = r*(2+r)/(1-r)**2
        assert ratio <= ratio_upper < 1
        record = {'beta': beta0, 'alpha': str(alpha), 'alpha_upper': str(alpha_upper),
                  'positive_score_y': str(y), 'opposite_derivative_ratio_bound': str(ratio_upper)}
        if beta0 >= 20:
            assert alpha_upper < 8 * mp.exp(-40)
            assert 1600 * mp.e * alpha_upper < 1
            x = 400 * alpha * mp.e
            T = alpha * mp.e / (1-x)**2
            c = 21 * T
            assert 0 < x < mp.mpf('0.25') and 0 < c < 1
            partial = sum(k * (400**(k-1)) * (alpha * mp.e)**k for k in range(1, 10))
            assert abs(partial/T - 1) < mp.mpf('1e-70')
            repair_ratio = 2 * 92**2 * mp.exp(-beta*mp.pi**2/18)
            assert repair_ratio < 1
            record.update({'weighted_series_T': str(T), 'ancestor_contraction_c': str(c),
                           'repair_cluster_ratio': str(repair_ratio)})
        rows.append(record)
    # Closed two-forms cannot have a nonzero continuous zero-momentum
    # covariance range if closure holds along every momentum direction.
    pairs = list(it.combinations(range(4), 2))
    triples = list(it.combinations(range(4), 3))
    wedges = []
    for a in range(4):
        matrix = sp.zeros(4, 6)
        for j, pair in enumerate(pairs):
            if a in pair:
                continue
            triple = tuple(sorted((a,) + pair))
            matrix[triples.index(triple), j] = h.permutation_sign((a,) + pair)
        wedges.append(matrix)
    all_wedges = sp.Matrix.vstack(*wedges)
    assert all_wedges.rank() == 6
    assert not all_wedges.nullspace()
    assert any(w * sp.eye(6) != sp.zeros(4, 6) for w in wedges)
    return {'villain_sum_checks': rows, 'all_direction_wedge_stack_rank': 6,
            'warning': 'finite arithmetic does not certify the dependence proof or CLT'}


def run():
    result = {'status': 'finite author checks only; infinite proofs and independent review separate',
              'positive_variance_geometry': variance_patch(),
              'finite_polymer_law': exact_finite_polymer_law(),
              'free_boundary_countercontrol': free_boundary_control(),
              'analytic_constants': analytic_constants_and_score()}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
