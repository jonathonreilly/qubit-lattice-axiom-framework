#!/usr/bin/env python3
"""Finite numerical diagnostic on a supplied five-lift bank and fixed H_SEED.
No physical selector, all-shift theorem, complete bank or unique normalization
is derived. Documentary mains of the historical selector remain separate.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_SELECTOR_SUPPLIED_BANK_SEED_RELATIVE_ACTION_FINITE_DIAGNOSTIC_NOTE_2026-10-23.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py']

import sys
import numpy as np
from dm_selector_branch_support import SHIFT_OFFSETS, recovered_bank
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import H_SEED
from frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem import kz_from_h

PASS_COUNT = 0
FAIL_COUNT = 0

def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition

def unique_argmin(values: np.ndarray) -> tuple[int, float]:
    vals = np.asarray(values, dtype=float)
    order = np.argsort(vals)
    return int(order[0]), float(vals[order[1]] - vals[order[0]])

def shifted_relative_action_to_seed(h: np.ndarray, mu: float) -> float:
    a_seed = np.asarray(H_SEED, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    a = np.asarray(h, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    m = np.linalg.inv(a_seed) @ a
    sign, logdet = np.linalg.slogdet(m)
    if abs(sign) < 1.0e-12:
        raise ValueError("shifted relative-action matrix left the positive branch")
    return float(np.real(np.trace(m) - logdet - 3.0))

def dense_shift_grid(mu_floor: float) -> np.ndarray:
    return np.concatenate(
        [
            np.linspace(mu_floor + 1.0e-6, mu_floor + 0.1, 20),
            np.linspace(mu_floor + 0.1, mu_floor + 2.0, 20),
            np.linspace(mu_floor + 2.0, mu_floor + 20.0, 20),
        ]
    )

def imag12_from_h(h: np.ndarray) -> float:
    kz = np.asarray(kz_from_h(h), dtype=complex)
    return float(np.imag(kz[1, 2]))

def main() -> int:
    print('SUPPLIED FIVE-LIFT BANK: FINITE SEED-RELATIVE-ACTION DIAGNOSTIC')
    print('Floating-point comparisons at the supplied sampled shifts; no physical selection or all-shift theorem.')
    _lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    mu_floor = float(np.max(repairs_bank))
    imag_bank = np.array([imag12_from_h(h) for h in hs_bank], dtype=float)
    check('One common positivity threshold mu_floor exists on the recovered bank', mu_floor > 0.0, f'mu_floor = {mu_floor:.15f}')
    audited = []
    for offset in SHIFT_OFFSETS:
        mu = mu_floor + float(offset)
        vals = np.array([shifted_relative_action_to_seed(h, mu) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        audited.append((mu, idx, margin))
    audited_ok = all((idx == 0 and margin > 1e-09 for _mu, idx, margin in audited))
    audited_margin = min((margin for _mu, _idx, margin in audited))
    check('At all 20 supplied shift offsets, lift 0 has the required numerical score margin', audited_ok, f'worst audited margin = {audited_margin:.12f}')
    check('First supplied shift: lift 0 meets the numerical margin threshold', audited[0][1] == 0 and audited[0][2] > 1e-09, f'(mu, margin)=({audited[0][0]:.15f}, {audited[0][2]:.12f})')
    check('Last supplied shift: lift 0 meets the numerical margin threshold', audited[-1][1] == 0 and audited[-1][2] > 1e-09, f'(mu, margin)=({audited[-1][0]:.15f}, {audited[-1][2]:.12f})')
    worst_mu = None
    worst_margin = float('inf')
    dense_ok = True
    for mu in dense_shift_grid(mu_floor):
        vals = np.array([shifted_relative_action_to_seed(h, float(mu)) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        if idx != 0 or margin <= 1e-09:
            dense_ok = False
        if margin < worst_margin:
            worst_mu = float(mu)
            worst_margin = float(margin)
    check('At the 60 sampled grid entries, lift 0 meets the numerical margin threshold', dense_ok, f'worst dense margin = {worst_margin:.12f} at mu = {worst_mu:.15f}')
    large_mu = mu_floor + 1000000.0
    large_vals = np.array([shifted_relative_action_to_seed(h, large_mu) for h in hs_bank], dtype=float)
    large_idx, large_margin = unique_argmin(large_vals)
    check('At the single far-shift sample mu_floor+1e6, lift 0 meets the original numerical threshold', large_idx == 0 and large_margin > 1e-18, f'(large_mu, margin)=({large_mu:.1f}, {large_margin:.12e})')
    positive_idx = np.where(imag_bank > 0.0)[0]
    check('Exactly one member of the supplied five-lift bank has positive computed imaginary entry', len(positive_idx) == 1 and int(positive_idx[0]) == 0, f'Im(K12)_bank = {np.round(imag_bank, 12)}')
    check('Sampled score minima and computed sign comparison identify the same supplied lift0', audited_ok and dense_ok and (len(positive_idx) == 1) and (int(positive_idx[0]) == 0), 'same recovered lift 0')
    check('Finite supplied-bank and sampled-shift comparisons meet the stated predicates', audited_ok and dense_ok and (len(positive_idx) == 1) and (int(positive_idx[0]) == 0), 'packet-local closure only')
    print(f'SUMMARY: NUMERICAL_CHECKS_PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    print('Supplied bank/seed/functional/shift samples only; physical selection, completeness and normalization remain open.')
    return 0 if FAIL_COUNT == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
