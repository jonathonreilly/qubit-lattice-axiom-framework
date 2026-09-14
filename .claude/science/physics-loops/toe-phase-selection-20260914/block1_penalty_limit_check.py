#!/usr/bin/env python3
"""Finite challenges of the penalty limit, including intentionally wrong models.

The product test uses exp(-delta A), not the full Euclidean clock kernel.
It tests the block-contraction lemma; the kernel's derivative and remainder
are established analytically in the source notes. No phase inference.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm, eigh

from block1_projection_sector_check import box_complex, flux_basis, clock_coefficients


def opnorm(a):
    return float(np.linalg.norm(a, 2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    levels, _, F, D = box_complex((1, 1, 1))
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    mu, stiffness, kappa, total_time = 0.4, 0.3, 0.7, 1.0
    electric = np.sum(b*b, axis=1)
    penalty = np.sum(q*q, axis=1)
    neutral = np.flatnonzero(penalty == 0)
    charged = np.flatnonzero(penalty != 0)
    n = len(b)
    identity = np.eye(n)
    adjacency = sum(np.exp(-k*mu)*a.toarray() for k, a in enumerate(coeff))
    A = 2*len(levels[1])*identity + np.diag(stiffness*electric)-adjacency
    assert eigh(A, eigvals_only=True)[0] >= -1e-10
    H0 = A[np.ix_(neutral, neutral)]
    e0 = float(eigh(H0, eigvals_only=True)[0])
    off = A[np.ix_(charged, neutral)]
    v = opnorm(off)
    finite_penalties = []
    for lam in (32.0, 64.0, 128.0, 256.0, 512.0):
        energy, vectors = eigh(A+np.diag(lam*penalty), subset_by_index=(0, 0))
        psi = vectors[:, 0]
        leakage = float(np.sum(psi[charged]**2))
        lower = e0-v*v/(lam-e0)
        leakage_bound = v*v/(lam-e0)**2
        assert lower-1e-10 <= energy[0] <= e0+1e-10
        assert leakage <= leakage_bound+1e-12
        finite_penalties.append({'lambda': lam, 'energy': float(energy[0]),
                                 'neutral_energy': e0, 'energy_lower_bound': lower,
                                 'charged_weight': leakage, 'charged_weight_bound': leakage_bound})

    target = np.zeros_like(A)
    target[np.ix_(neutral, neutral)] = expm(-total_time*H0)
    Mhalf = np.diag(np.exp(-kappa*penalty/2))
    zeno = []
    for steps in (8, 16, 32, 64, 128, 256):
        delta = total_time/steps
        transfer = Mhalf @ expm(-delta*A) @ Mhalf
        value = np.linalg.matrix_power(transfer, steps)
        error = opnorm(value-target)
        a = transfer[np.ix_(neutral, neutral)]
        bblock = transfer[np.ix_(neutral, charged)]
        cblock = transfer[np.ix_(charged, charged)]
        qp = opnorm(cblock)
        B = opnorm(bblock)/delta
        C = opnorm(a-expm(-delta*H0))/delta**2
        bound = qp**steps + 2*delta*B/(1-qp) + steps*delta**2*(B*B/(1-qp)+C)
        assert qp < 1
        assert error <= bound+1e-12
        zeno.append({'steps': steps, 'delta': delta, 'operator_error': error,
                     'block_bound': bound, 'fast_block_norm': qp})
    assert zeno[-1]['operator_error'] < zeno[0]['operator_error']/10

    # Wrong projected model 1: discard the all-wrap second harmonic.
    wrong = (2*len(levels[1])*identity + np.diag(stiffness*electric)
             -coeff[0].toarray())[np.ix_(neutral, neutral)]
    missing_double = opnorm(wrong-H0)
    assert missing_double > 1
    wrong_target_distance = opnorm(expm(-total_time*wrong)-target[np.ix_(neutral, neutral)])
    assert wrong_target_distance > 1e-8
    # Wrong projected model 2: use the bulk exponent four on boundary edges.
    wrong_boundary = (2*len(levels[1])*identity + np.diag(stiffness*electric)
                      -coeff[0].toarray()-np.exp(-4*mu)*coeff[2].toarray())
    boundary_error = opnorm(wrong_boundary[np.ix_(neutral, neutral)]-H0)
    assert boundary_error > 1
    # Wrong normalization 3: standard spin raising matrices, no sqrt(2).
    # Every one-cube edge has r=2, so first and double hops scale by 2 and 4.
    wrong_spin = (2*len(levels[1])*identity + np.diag(stiffness*electric)
                  -2*coeff[0].toarray()-4*np.exp(-2*mu)*coeff[2].toarray())
    spin_error = opnorm(wrong_spin[np.ix_(neutral, neutral)]-H0)
    assert spin_error > 1
    # Wrong constraint 4: modulo-three closure permits a mixed wrap that
    # integer neutrality excludes. Record an actual source/destination pair.
    mixed = coeff[1][charged][:, neutral].tocoo()
    assert mixed.nnz > 0
    dst, src = charged[mixed.row[0]], neutral[mixed.col[0]]
    assert np.all(q[src] == 0) and np.any(q[dst] != 0)
    witness = {'source_flux': b[src].tolist(), 'destination_flux': b[dst].tolist(),
               'source_charge': q[src].tolist(), 'destination_charge': q[dst].tolist()}

    result = {'status': 'finite_author_checks_only',
              'parameters': {'mu': mu, 'electric_stiffness_3K_over_2': stiffness,
                             'kappa_per_step': kappa, 'T': total_time},
              'neutral_energy': e0, 'offblock_norm': v,
              'finite_spatial_penalties': finite_penalties,
              'zeno_product_model': 'Mhalf exp(-delta A) Mhalf, testing the block lemma',
              'zeno': zeno,
              'wrong_model_challenges': {
                  'omitted_second_harmonic_operator_error': missing_double,
                  'wrong_semigroup_limit_distance': wrong_target_distance,
                  'bulk_exponent_on_boundary_operator_error': boundary_error,
                  'unnormalized_spin_raising_operator_error': spin_error,
                  'modular_instead_of_integer_constraint_witness': witness}}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
