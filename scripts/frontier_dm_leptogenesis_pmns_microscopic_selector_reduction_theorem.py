#!/usr/bin/env python3
"""Supplied numerical witnesses and conditional right-orbit non-identifiability.
No physical selection, exact numerical closure, or sole remaining blocker is claimed.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 600

import math
import sys

import numpy as np
from scipy.optimize import brentq

from frontier_dm_leptogenesis_pmns_constructive_continuity_closure_theorem import (
    constructive_column_eta,
    path_point,
    path_triplet,
)
from frontier_dm_leptogenesis_pmns_even_response_sole_axiom_boundary import (
    CANONICAL_DELTA,
    CANONICAL_X,
    CANONICAL_Y,
    carrier_even_response,
    triplet_data,
)
from frontier_dm_leptogenesis_pmns_oriented_phase_sheet_selector_theorem import (
    witness_pair,
)
from frontier_dm_neutrino_postcanonical_right_frame_obstruction import (
    canonical_y,
    cp_tensor_from_kz,
    right_rotation,
    slot_amplitudes_from_kz,
    z3_kernel,
)
from frontier_dm_neutrino_source_surface_z3_doublet_block_full_closure_boundary import (
    active_target_from_h,
    active_affine_h,
    current_bank_signature,
    exact_package,
    q_floor,
    same_signature,
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition




def part1_the_constructive_exact_eta_one_point_already_exists() -> None:
    print("\n" + "=" * 88)
    print("PART 1: SUPPLIED NUMERICAL CLOSURE SAMPLE")
    print("=" * 88)

    lam_star = brentq(lambda lam: constructive_column_eta(lam) - 1.0, 0.0, 1.0)
    x_star, y_star, delta_star = path_point(lam_star)
    triplet = path_triplet(lam_star)
    eta_star = constructive_column_eta(lam_star)

    check(
        "The supplied interpolated sample satisfies eta = 1 within 1e-12",
        0.0 < lam_star < 1.0 and abs(eta_star - 1.0) < 1e-12,
        f"lambda_*={lam_star:.12f}",
    )
    check(
        "The supplied numerical sample has positive gamma, E1 and E2",
        triplet["gamma"] > 0.0 and triplet["E1"] > 0.0 and triplet["E2"] > 0.0,
        f"(gamma,E1,E2)=({triplet['gamma']:.12f},{triplet['E1']:.12f},{triplet['E2']:.12f})",
    )
    check(
        "The interpolated numerical sample has nonzero source norms and phase",
        np.linalg.norm(x_star) > 0.0 and np.linalg.norm(y_star) > 0.0 and abs(delta_star) > 1e-6,
        f"delta_*={delta_star:.12f}",
    )


def part2_the_odd_microscopic_selector_bit_is_already_closed() -> None:
    print("\n" + "=" * 88)
    print("PART 2: SUPPLIED ODD-SIGN PAIR")
    print("=" * 88)

    data = witness_pair()
    a13_pos = data["resp_pos"][6]
    a13_neg = data["resp_neg"][6]

    check(
        "The two supplied samples match sign(A13) to sign(sin(delta))",
        math.copysign(1.0, a13_pos) == math.copysign(1.0, math.sin(data["delta_pos"]))
        and math.copysign(1.0, a13_neg) == math.copysign(1.0, math.sin(data["delta_neg"])),
        f"(A13+,A13-)=({a13_pos:.12f},{a13_neg:.12f})",
    )
    check(
        "The supplied pair agrees in E1, E2 and the computed eta vector",
        abs(data["tri_pos"]["E1"] - data["tri_neg"]["E1"]) < 1e-12
        and abs(data["tri_pos"]["E2"] - data["tri_neg"]["E2"]) < 1e-12
        and np.linalg.norm(data["eta_pos"] - data["eta_neg"]) < 1e-12,
        f"eta={np.round(data['eta_pos'], 12)}",
    )
    check(
        "The supplied pair has opposite nonzero A13 signs",
        a13_pos > 0.0 and a13_neg < 0.0,
        "equivalently sign(sin(delta))",
    )


def part3_fixing_the_odd_bit_still_does_not_choose_the_constructive_point() -> None:
    print("\n" + "=" * 88)
    print("PART 3: FIXING THE ODD BIT STILL DOES NOT CHOOSE THE CONSTRUCTIVE POINT")
    print("=" * 88)

    _c_xbar, _c_ybar, c_gamma, c_e1, c_e2 = triplet_data(
        CANONICAL_X, CANONICAL_Y, CANONICAL_DELTA
    )
    _w_xbar, _w_ybar, w_gamma, w_e1, w_e2 = triplet_data(
        path_point(1.0)[0], path_point(1.0)[1], path_point(1.0)[2]
    )
    c_e1_car, _c_e2_car, _c_gamma_car, c_sigma_sin_2v = carrier_even_response(
        CANONICAL_X, CANONICAL_Y, CANONICAL_DELTA
    )
    w_e1_car, _w_e2_car, _w_gamma_car, w_sigma_sin_2v = carrier_even_response(
        path_point(1.0)[0], path_point(1.0)[1], path_point(1.0)[2]
    )

    check(
        "The canonical near-closing sample and the constructive witness already share the positive odd sheet",
        c_gamma > 0.0 and w_gamma > 0.0 and math.sin(CANONICAL_DELTA) > 0.0 and math.sin(path_point(1.0)[2]) > 0.0,
        f"gamma=({c_gamma:.12f},{w_gamma:.12f})",
    )
    check(
        "But they still carry opposite even-response signs",
        c_e1 < 0.0 and c_e2 < 0.0 and w_e1 > 0.0 and w_e2 > 0.0,
        f"canonical=({c_e1:.12f},{c_e2:.12f}), constructive=({w_e1:.12f},{w_e2:.12f})",
    )
    check(
        "The supplied carrier readouts also distinguish these even-response signs",
        c_e1_car < 0.0 and c_sigma_sin_2v < 0.0 and w_e1_car > 0.0 and w_sigma_sin_2v > 0.0,
        f"(delta+rho,sigma sin2v)=({c_e1_car:.12f},{c_sigma_sin_2v:.12f}) vs ({w_e1_car:.12f},{w_sigma_sin_2v:.12f})",
    )


def part4_the_atlas_source_bank_already_compresses_further_to_a_right_sensitive_2_real_target() -> None:
    print("\n" + "=" * 88)
    print("PART 4: SUPPLIED SIGNATURE AND COORDINATE SAMPLES")
    print("=" * 88)

    pkg = exact_package()
    q_common = 2.2
    h_a = active_affine_h(0.0, 0.2, q_common)
    h_b = active_affine_h(0.0, 0.9, q_common)
    h_c = active_affine_h(0.0, 0.2, 2.5)
    sig_a = current_bank_signature(h_a)
    sig_b = current_bank_signature(h_b)
    sig_c = current_bank_signature(h_c)
    tgt_a = active_target_from_h(h_a)
    tgt_b = active_target_from_h(h_b)
    tgt_c = active_target_from_h(h_c)

    check(
        "The supplied package contains the stated gamma, E1 and E2 constants",
        abs(pkg.gamma - 0.5) < 1e-12
        and abs(pkg.E1 - math.sqrt(8.0 / 3.0)) < 1e-12
        and abs(pkg.E2 - math.sqrt(8.0) / 3.0) < 1e-12,
        f"(gamma,E1,E2)=({pkg.gamma:.12f},{pkg.E1:.12f},{pkg.E2:.12f})",
    )
    check(
        "The three supplied matrices share the helper-defined signature",
        same_signature(sig_a, sig_b) and same_signature(sig_a, sig_c),
        "same (gamma,E1,E2,cp1,cp2,a_*,b_*,T_slot)",
    )
    check(
        "Those same points still have different active targets",
        tgt_a != tgt_b and tgt_a != tgt_c,
        f"targets={tgt_a}, {tgt_b}, {tgt_c}",
    )
    check(
        "The first supplied coordinate sample satisfies its declared q-floor inequality",
        q_floor(0.2) < q_common,
        "This finite inequality does not select physical coordinates.",
    )


def part5_h_only_data_cannot_supply_that_selector() -> None:
    print("\n" + "=" * 88)
    print("PART 5: SUPPLIED RIGHT-UNITARY ORBIT CONTROL")
    print("=" * 88)

    x = np.array([1.0, 0.8, 1.1], dtype=float)
    y = np.array([0.4, 0.6, 0.5], dtype=float)
    delta = 2.0 * math.pi / 3.0
    y0 = canonical_y(x, y, delta)
    y1 = y0 @ right_rotation(0.41).conj().T
    h0 = y0 @ y0.conj().T
    h1 = y1 @ y1.conj().T
    kz0 = z3_kernel(y0)
    kz1 = z3_kernel(y1)
    u0, v0 = slot_amplitudes_from_kz(kz0, 2.0 * math.pi / 3.0)
    u1, v1 = slot_amplitudes_from_kz(kz1, 2.0 * math.pi / 3.0)
    cp0 = cp_tensor_from_kz(kz0)
    cp1 = cp_tensor_from_kz(kz1)

    check(
        "The supplied right-unitary pair preserves H within 1e-12",
        np.linalg.norm(h0 - h1) < 1e-12,
        f"H error={np.linalg.norm(h0 - h1):.2e}",
    )
    check(
        "The same orbit changes the right-sensitive slot amplitudes",
        abs(u0 - u1) > 1e-6 or abs(v0 - v1) > 1e-6,
        f"(u,v)_0=({u0:.6f},{v0:.6f}), (u,v)_1=({u1:.6f},{v1:.6f})",
    )
    check(
        "The same orbit changes the heavy-basis CP tensor",
        abs(cp0[0] - cp1[0]) > 1e-6 or abs(cp0[1] - cp1[1]) > 1e-6,
        f"CP0={cp0}, CP1={cp1}",
    )
    check(
        "The supplied rotation is unitary and conjugates K as specified",
        np.linalg.norm(right_rotation(0.41).conj().T @ right_rotation(0.41)-np.eye(3)) < 1e-12
        and np.linalg.norm(y1.conj().T @ y1-right_rotation(0.41) @ (y0.conj().T @ y0) @ right_rotation(0.41).conj().T) < 1e-12,
        "Non-identifiability is conditional on admitting both supplied orbit members",
    )






def main() -> int:
    print("SUPPLIED NUMERICAL WITNESSES AND RIGHT-ORBIT CONTROL")
    print("Imported constants, transport and source families are supplied, not derived here.")
    part1_the_constructive_exact_eta_one_point_already_exists()
    part2_the_odd_microscopic_selector_bit_is_already_closed()
    part3_fixing_the_odd_bit_still_does_not_choose_the_constructive_point()
    part4_the_atlas_source_bank_already_compresses_further_to_a_right_sensitive_2_real_target()
    part5_h_only_data_cannot_supply_that_selector()
    print("The finite examples do not identify the only remaining physical obligation.")
    print("H-only non-identifiability applies only if both displayed orbit members are admitted.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
