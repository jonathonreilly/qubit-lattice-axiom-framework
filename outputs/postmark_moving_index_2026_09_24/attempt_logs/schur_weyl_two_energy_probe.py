#!/usr/bin/env python3
"""Author-only finite checks for the exact two-energy anchor Schur reduction.

This is a representation check, not a global propagation or readout estimate.
The full operator is H_S = C N_S, so its eigenphase at t=1/4 is exp(-i H_S/4).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


def symbolic_four_site_pencil():
    a, b, z = sp.symbols("A B z", positive=True)
    root = sp.sqrt(a * b)
    k = sp.Matrix(
        [
            [a + b - z, -root, 0, 0],
            [-root, 2 * a - z, -a, 0],
            [0, -a, a + b - z, -b],
            [0, 0, -b, 2 * b - z],
        ]
    )
    p0 = sp.Integer(1)
    p1 = a + b - z
    p2 = (2 * a - z) * p1 - a * b
    p3 = (a + b - z) * p2 - a**2 * p1
    det_recurrence = sp.expand((2 * b - z) * p3 - b**2 * p2)
    det_matrix = sp.factor(k.det())
    inv14 = sp.factor(k.inv()[0, 3])
    schur_product = sp.factor((-a) * inv14 * (-root))
    schur_offdiagonal = sp.factor(-schur_product)
    return {
        "determinant_recurrence_matches_matrix": sp.simplify(det_recurrence - k.det()) == 0,
        "corner_resolvent": str(inv14),
        "schur_offdiagonal": str(schur_offdiagonal),
        "target_schur_offdiagonal": "-A**3*B**2/det(K)",
        "determinant_factor": str(det_matrix),
        "exact_identity": sp.simplify(schur_offdiagonal + a**3 * b**2 / det_recurrence) == 0,
    }


def full_hamiltonian(spin: int):
    c = spin * (spin + 1)
    ell = (0, 1, 0, 1, 1)
    rho = (0, 0, 0, 1, 0)
    pi = (-1, 0, 0, 0, 1)
    sites = list(range(-5 * spin, 5 * spin - 3))
    hmat = np.zeros((len(sites), len(sites)), dtype=np.float64)
    for i, n in enumerate(sites):
        h, s = divmod(n, 5)
        hmat[i, i] = (c - (h + ell[s]) * (h + ell[s] + 1)) + (
            c - (h + pi[s]) * (h + pi[s] + 1)
        )
        if i + 1 < len(sites):
            left = c - (h + ell[s]) * (h + ell[s] + 1)
            right = c - (h + rho[s]) * (h + rho[s] + 1)
            if left < 0 or right < 0:
                raise ArithmeticError(("negative link radicand", spin, n, left, right))
            hmat[i, i + 1] = hmat[i + 1, i] = -np.sqrt(left * right)
    return sites, hmat


def check_energy_pair_reduction(spin: int):
    sites, hmat = full_hamiltonian(spin)
    anchor_ids = [i for i, n in enumerate(sites) if n % 5 == 0]
    interior_ids = [i for i, n in enumerate(sites) if n % 5 != 0]
    haa = hmat[np.ix_(anchor_ids, anchor_ids)]
    hai = hmat[np.ix_(anchor_ids, interior_ids)]
    hia = hai.T
    hii = hmat[np.ix_(interior_ids, interior_ids)]
    # Negative spectral parameters avoid every pole because H_S is positive.
    lam, mu = -0.37, -0.83
    rlam = np.linalg.inv(lam * np.eye(len(interior_ids)) - hii)
    rmu = np.linalg.inv(mu * np.eye(len(interior_ids)) - hii)
    rng = np.random.default_rng(1000 + spin)
    x = rng.normal(size=len(anchor_ids)) + 1j * rng.normal(size=len(anchor_ids))
    y = rng.normal(size=len(anchor_ids)) + 1j * rng.normal(size=len(anchor_ids))
    phi_lam = np.concatenate((x, rlam @ hia @ x))
    phi_mu = np.concatenate((y, rmu @ hia @ y))
    perm = anchor_ids + interior_ids
    vdiag = np.exp((2j * np.pi / 3) * np.asarray(sites))
    vperm = vdiag[perm]
    va, vi = vperm[: len(anchor_ids)], vperm[len(anchor_ids) :]
    direct = np.vdot(phi_lam, vperm * phi_mu)
    qv = np.diag(va) + hai @ rlam @ np.diag(vi) @ rmu @ hia
    reduced = np.vdot(x, qv @ y)
    # For V=I this is the exact negative divided difference of the Schur pencil.
    def schur(e):
        re = np.linalg.inv(e * np.eye(len(interior_ids)) - hii)
        return haa - e * np.eye(len(anchor_ids)) + hai @ re @ hia

    metric = np.eye(len(anchor_ids)) + hai @ rlam @ rmu @ hia
    divided_difference = -(schur(lam) - schur(mu)) / (lam - mu)
    cell_ids = np.asarray([sites[i] // 5 for i in interior_ids])
    cross_cell = np.abs(hii[cell_ids[:, None] != cell_ids[None, :]])
    offblock_max = float(cross_cell.max()) if cross_cell.size else 0.0
    return {
        "spin": spin,
        "full_dimension": len(sites),
        "anchor_dimension": len(anchor_ids),
        "interior_dimension": len(interior_ids),
        "weighted_two_energy_overlap_abs_error": float(abs(direct - reduced)),
        "identity_weight_is_schur_negative_divided_difference_error": float(
            np.linalg.norm(metric - divided_difference)
        ),
        "interior_partition_cross_cell_link_max": offblock_max,
        "interpretation": "exact finite block-elimination identity sampled in floating arithmetic; no phase-sum bound",
    }


def main():
    out = {
        "status": "author-only representation probe",
        "operator": "H_S=C*N_S; target fast phase is exp(-i*H_S/4)",
        "symbolic_four_site": symbolic_four_site_pencil(),
        "energy_pair_checks": [check_energy_pair_reduction(s) for s in (1, 2, 3, 5)],
        "exact_reduced_observable": (
            "Q_V(lambda,mu)=V_A+H_AI*(lambda-H_II)^(-1)*V_I*(mu-H_II)^(-1)*H_IA; "
            "<Phi_lambda,V Phi_mu>=x_lambda^* Q_V x_mu"
        ),
        "scope": (
            "The identity reduces exact weighted eigenvector overlaps to anchor coordinates. "
            "It does not control the O(S^2)-time phase cancellation, central/Bragg resonance sum, "
            "or the fixed-time prepared-state readout."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
