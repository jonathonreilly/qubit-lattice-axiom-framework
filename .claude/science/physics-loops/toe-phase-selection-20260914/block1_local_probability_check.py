#!/usr/bin/env python3
"""Checks of the local-probability proof, not a phase or thermodynamic fit."""
from __future__ import annotations

import argparse
from itertools import combinations, product
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, expm

from block1_projection_sector_check import box_complex, flux_basis, clock_coefficients


def log_lower(C, h, r, tau):
    # k = exp(2h tau)*(1-exp(-3h tau))/3, evaluated stably.
    log_k = 2*h*tau+np.log(-np.expm1(-3*h*tau))-np.log(3)
    return float(-2*C*tau+2*r*log_k)


def optimum(C, h, r):
    if C <= 2*r*h:
        return 1/max(C, h)
    return float(np.log1p(3*r*h/(C-2*r*h))/(3*h))


def abstract_chain_check():
    # Four qutrits, state-dependent rates on three-site neighborhoods.
    # The R={0} split has a nontrivial far Hamiltonian that need not commute
    # with H_near. The near terms are positive individually.
    digits = np.asarray(list(product(range(3), repeat=4)), dtype=np.int64)
    index = {tuple(row): i for i, row in enumerate(digits)}
    n, h, t = len(digits), 0.17, 0.9
    terms = []
    for site in range(4):
        support = set(range(max(0, site-1), min(4, site+2)))
        adjacency = np.zeros((n, n))
        for i, row in enumerate(digits):
            for target in range(3):
                if target == row[site]:
                    continue
                new = row.copy()
                new[site] = target
                j = index[tuple(new)]
                # Symmetric in the old/new central values, depends only on
                # the declared local neighborhood, and lies in [h,t].
                context = sum((a+1)*int(row[a]) for a in support if a != site)
                code = (context + int(row[site])+target + 2*int(row[site])*target) % 7
                adjacency[j, i] = h+(t-h)*code/6
        assert np.max(np.abs(adjacency-adjacency.T)) == 0
        term = 2*t*np.eye(n)-adjacency
        assert eigh(term, eigvals_only=True)[0] >= -1e-12
        terms.append((support, term))
    for site in range(3):
        v = 0.37*(digits[:, site]-digits[:, site+1])**2
        terms.append(({site, site+1}, np.diag(v)))
    near = sum(term for support, term in terms if 0 in support)
    far = sum(term for support, term in terms if 0 not in support)
    H = near+far
    C = float(np.max(np.diag(near)))
    e, vec = eigh(H, subset_by_index=(0, 0))
    omega = vec[:, 0]
    if np.sum(omega) < 0:
        omega = -omega
    assert np.min(omega) > 0
    B = np.zeros((n, n))
    for i, row in enumerate(digits):
        for step in (-1, 1):
            new = row.copy()
            new[0] = (new[0]+step) % 3
            B[index[tuple(new)], i] = 1
    G = -far-C*np.eye(n)+h*B
    assert np.min(-H-G) >= -1e-12
    assert np.linalg.norm(near@far-far@near) > 1e-3
    probabilities = np.sum(omega.reshape(3, -1)**2, axis=1)
    rows = []
    for tau in (0.02, 0.1, 0.4):
        semigroup_margin = float(np.min(expm(-tau*H)-expm(tau*G)))
        assert semigroup_margin >= -1e-12
        bound = np.exp(log_lower(C, h, 1, tau))
        assert np.min(probabilities) >= bound
        jensen_left = np.linalg.norm(expm(-tau*far)@omega)
        jensen_right = np.exp(-tau*(omega@far@omega))
        assert jensen_left >= jensen_right-1e-12
        rows.append({'tau': tau, 'lower_probability': float(bound),
                     'minimum_actual_probability': float(np.min(probabilities)),
                     'entrywise_semigroup_margin': semigroup_margin})
    return {'dimension': n, 'h': h, 'C': C,
            'noncommuting_near_far_norm': float(np.linalg.norm(near@far-far@near)),
            'cases': rows}


def cube_assignment_and_counts():
    levels, _, F, D = box_complex((1, 1, 1))
    witness = None
    for l1, l2 in combinations(range(F.shape[1]), 2):
        for s1, s2 in product((-1, 1), repeat=2):
            a = np.zeros(F.shape[1], dtype=np.int64)
            a[l1], a[l2] = s1, s2
            b = (F@a+1) % 3-1
            q = D@b//3
            if np.any(q):
                witness = {'nonzero_edge_indexes': [l1, l2],
                           'nonzero_oriented_edges': [levels[1][l1], levels[1][l2]],
                           'edge_values': [s1, s2], 'all_edge_values': a.tolist(),
                           'face_flux': b.tolist(), 'cube_charge': q.tolist()}
                break
        if witness:
            break
    assert witness is not None
    levels, _, F, D = box_complex((5, 5, 5))
    c = levels[3].index(((0, 1, 2), (2, 2, 2)))
    faces = set(np.flatnonzero(D[c]))
    R = set(np.flatnonzero(np.any(F[list(faces)] != 0, axis=0)))
    assert len(R) == 12
    face_supports = [set(np.flatnonzero(row)) for row in F]
    cube_supports = []
    for row in D:
        cube_supports.append(set().union(*(face_supports[p] for p in np.flatnonzero(row))))
    electric_supports = []
    for l in range(F.shape[1]):
        electric_supports.append(set().union(*(face_supports[p]
                                               for p in np.flatnonzero(F[:, l]))))
    counts = {'electric': sum(bool(s & R) for s in electric_supports),
              'faces': sum(bool(s & R) for s in face_supports),
              'cubes': sum(bool(s & R) for s in cube_supports)}
    assert counts['electric'] <= 13*12
    assert counts['faces'] <= 4*12
    assert counts['cubes'] <= 4*12
    return {'two_edge_charge_assignment': witness, 'bulk_cube_region_size': len(R),
            'bulk_near_term_counts': counts}


def physical_cube_probability_check():
    levels, _, F, D = box_complex((1, 1, 1))
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    electric = np.sum(b*b, axis=1)
    charge2 = np.sum(q*q, axis=1)
    orbit_size = 3**(len(levels[0])-1)
    rows = []
    for mu, K, lam in ((0., 0., 0.), (0.4, 0.2, 2.), (1., 0.5, 5.)):
        adjacency = sum(np.exp(-k*mu)*a.toarray() for k, a in enumerate(coeff))
        H = 2*len(levels[1])*np.eye(len(b))-adjacency+np.diag(1.5*K*electric+lam*charge2)
        e, vec = eigh(H, subset_by_index=(0, 0))
        omega = vec[:, 0]
        if np.sum(omega) < 0:
            omega = -omega
        assert np.min(omega) > 0
        # Each physical flux vector is the normalized sum of 3^(V-1)
        # coordinate configurations in its original gauge orbit.
        minimum_coordinate_probability = float(np.min(omega**2)/orbit_size)
        h = np.exp(-4*mu)
        C = 2*len(levels[1])+1.5*K*len(levels[2])+4*lam*len(levels[3])
        tau = optimum(C, h, len(levels[1]))
        log_bound = log_lower(C, h, len(levels[1]), tau)
        assert np.log(minimum_coordinate_probability) >= log_bound
        rows.append({'mu': mu, 'K': K, 'lambda': lam, 'h': h, 'C': C,
                     'tau': tau, 'log_lower_bound': log_bound,
                     'minimum_coordinate_probability': minimum_coordinate_probability,
                     'charge_defect_probability': float(np.sum(omega[charge2 != 0]**2))})
    return {'gauge_orbit_size': orbit_size, 'cases': rows}


def dropped_positive_near_counterexample():
    # Entrywise hopping positivity remains, but H_near is not positive.
    # Retaining the final conclusion after deleting that hypothesis fails.
    B = np.ones((3, 3))-np.eye(3)
    H = np.diag([-100., 0., 0.])-B
    e, vec = eigh(H, subset_by_index=(0, 0))
    prob = vec[:, 0]**2
    claimed = np.exp(log_lower(C=0., h=1., r=1, tau=1.))
    assert claimed > 1 and np.min(prob) < claimed
    return {'H': H.tolist(), 'lowest_near_eigenvalue': float(e[0]),
            'false_bound_if_positive_near_is_dropped': float(claimed),
            'minimum_actual_probability': float(np.min(prob))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'status': 'author_finite_checks_not_a_phase_claim',
              'abstract_noncommuting_chain': abstract_chain_check(),
              'cube_geometry': cube_assignment_and_counts(),
              'physical_cube': physical_cube_probability_check(),
              'necessary_hypothesis_counterexample': dropped_positive_near_counterexample()}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
