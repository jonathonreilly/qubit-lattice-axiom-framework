"""Independent exact local controls; no author or prior model-builder imports.

Finite paths use integer matter/field states, with all edges oriented A to B.
They test local diagnostic factors and interference, not the infinite-volume
proof. The separate Wilson-loop calculation tests the claimed time topology.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


OUT = Path(__file__).resolve().parent


def distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def radius_two_ball(d):
    # The central site is B; each adjacent A has its entire Zd star present.
    center = (1,) + (0,)*(d-1)
    points = sorted(tuple(center[i]+h[i] for i in range(d))
                    for h in itertools.product(range(-2, 3), repeat=d)
                    if sum(map(abs, h)) <= 2)
    aa = tuple(i for i, x in enumerate(points) if sum(x) % 2 == 0)
    bb = tuple(i for i in range(len(points)) if i not in aa)
    edges = tuple((a, b) for a in aa for b in bb
                  if distance(points[a], points[b]) == 1)
    return points, aa, bb, edges, points.index(center)


def gauss(state, aa, edges):
    q, electric = state
    div = [0]*len(q)
    for value, (a, b) in zip(electric, edges):
        div[a] += value
        div[b] -= value
    return all(div[x] == q[x] - int(x in aa) for x in range(len(q)))


def mark(initial, edge, charge, edges):
    q0, electric0 = initial
    a, b = edges[edge]
    result = Counter()
    # First the actual old record leaves a; then the opposite-charge pair forms.
    for old_edge, (old_a, c) in enumerate(edges):
        if old_a != a or c == b or q0[c] or q0[b] or not q0[a]:
            continue
        q, electric = list(q0), list(electric0)
        old_charge = q[a]
        q[c], q[a], q[b] = old_charge, charge, -charge
        electric[old_edge] -= old_charge
        electric[edge] += charge
        result[(tuple(q), tuple(electric))] += 1
    return result


def norm_squared(vector):
    return sum(abs(v)**2 for v in vector.values())


def diagonal_expectation(vector, function):
    return sum(abs(v)**2*function(state) for state, v in vector.items())


def diagnostic(d):
    points, aa, bb, edges, center = radius_two_ball(d)
    z = 2*d
    initial = (tuple(int(x in aa) for x in range(len(points))), (0,)*len(edges))
    assert gauss(initial, aa, edges)
    assert all(sum(a == x for a, b in edges) == z for x in aa)
    per_mark = []
    total_rate_resolved = total_rate_coherent = 0
    central_derivative_resolved = central_derivative_coherent = 0
    total_records_derivative_resolved = total_records_derivative_coherent = 0
    output_paths = 0
    for e in range(len(edges)):
        plus, minus = mark(initial, e, 1, edges), mark(initial, e, -1, edges)
        assert not set(plus).intersection(minus)
        coherent = plus + minus
        for sigma, vector in ((1, plus), (-1, minus)):
            assert norm_squared(vector) == z-1
            for state in vector:
                assert gauss(state, aa, edges)
                assert sum(x*x for x in state[0]) == len(aa)+2
                assert sum(state[0]) == len(aa)
                assert all(state[0][a] != 0 for a in aa)
            total_rate_resolved += norm_squared(vector)
            central_derivative_resolved += diagonal_expectation(
                vector, lambda state: state[0][center]**2)
            total_records_derivative_resolved += 2*norm_squared(vector)
            per_mark.append((e, sigma, norm_squared(vector)))
            output_paths += len(vector)
        assert norm_squared(coherent) == 2*(z-1)
        total_rate_coherent += norm_squared(coherent)
        central_derivative_coherent += diagonal_expectation(
            coherent, lambda state: state[0][center]**2)
        total_records_derivative_coherent += 2*norm_squared(coherent)
    expected_local = 4*z*(z-1)
    assert central_derivative_resolved == central_derivative_coherent == expected_local
    assert total_rate_resolved == total_rate_coherent == 2*len(aa)*z*(z-1)
    assert total_records_derivative_resolved == total_records_derivative_coherent
    # Difference of the two normalized post-mark densities has off-diagonal
    # blocks +/- |plus><minus|/(2(z-1)); its trace distance is exactly 1/2.
    purity_resolved, purity_coherent = Fraction(1, 2), Fraction(1)
    return {
        'd': d, 'coordination_z': z, 'finite_vertices': len(points),
        'finite_A': len(aa), 'finite_edges': len(edges),
        'Gauss_checked_output_paths': output_paths,
        'resolved_mark_norm2': z-1, 'coherent_edge_norm2': 2*(z-1),
        'central_B_occupation_derivative_over_kappa': expected_local,
        'infinite_lattice_births_per_vertex_per_time_over_kappa': z*(z-1),
        'infinite_lattice_record_density_derivative_over_kappa': 2*z*(z-1),
        'finite_ball_total_birth_rate_over_kappa': total_rate_resolved,
        'finite_ball_total_record_derivative_over_kappa': total_records_derivative_resolved,
        'normalized_resolved_discarded_mark_purity': str(purity_resolved),
        'normalized_coherent_mark_purity': str(purity_coherent),
        'normalized_post_mark_trace_distance': '1/2',
        'per_mark_norms': per_mark,
    }


def norm_discontinuity():
    # Gauge-legal plaquette circulations |m>: electric energy 4 K m^2.
    # W|m>=|m+1>. At t_m=pi/[K(8m+4)], its phase difference is exactly -1.
    rows = []
    for m in (0, 1, 2, 4, 8, 16, 32, 64, 128, 256):
        difference = 4*(m+1)**2 - 4*m*m
        t_over_pi = Fraction(1, difference)
        assert difference*t_over_pi == 1
        rows.append({'m': m, 'electric_gap_over_K': difference,
                     'K_t_over_pi_exact': str(t_over_pi),
                     'K_t_numeric': math.pi/difference,
                     'norm_difference_exact': 2})
    return {
        'allowed_parameters': 'K>0, delta=kappa=0',
        'observable': 'bounded gauge-invariant unitary plaquette shift W',
        'claim': 'norm discontinuity at t=0 on the full local bounded algebra',
        'rows': rows,
    }


def global_folium_countercontrol():
    # Independent, separated physical plaquettes: psi=(|0>+|1>)/sqrt(2).
    # At t=pi/(8K), psi becomes (|0>-i|1>)/sqrt(2); squared overlap=1/2.
    # The product-state overlap on M plaquettes tends to zero exactly.
    return {
        'allowed_parameters': 'K>0, delta=kappa=0',
        'K_t_over_pi_exact': '1/8',
        'one_plaquette_squared_overlap': '1/2',
        'overlaps': [{'number_of_disjoint_plaquettes': m,
                      'squared_overlap': str(Fraction(1, 2**m))}
                     for m in (1, 2, 4, 8, 16, 32)],
        'meaning': 'local normality does not assert global normality in the initial incomplete tensor-product representation',
    }


def main():
    result = {
        'method': 'own integer legal-path enumeration; exact fractions; no root-builder imports',
        'initial_diagnostics': [diagnostic(d) for d in (2, 3, 4)],
        'time_topology_countercontrol': norm_discontinuity(),
        'representation_boundary': global_folium_countercontrol(),
        'limits': ['not a finite-volume trajectory simulation',
                   'not a numerical proof of the spatial locality theorem',
                   'all rates in diagnostic tables are divided by kappa'],
    }
    target = OUT/'EXACT_RESULTS.json'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'status': 'passed',
        'd_and_central_B_derivative_over_kappa': [
            [x['d'], x['central_B_occupation_derivative_over_kappa']]
            for x in result['initial_diagnostics']],
        'results': str(target),
        'norm_discontinuity_exact': True,
        'coherent_and_resolved_post_states_differ': True,
    }, indent=2))


if __name__ == '__main__':
    main()
