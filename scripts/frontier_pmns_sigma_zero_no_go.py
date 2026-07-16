#!/usr/bin/env python3
"""Route-specific checks for nonzero sigma on named PMNS blocks."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from frontier_pmns_active_four_real_source_from_transport import active_native_means
from frontier_pmns_c3_nontrivial_current_boundary import nontrivial_character_current
from frontier_pmns_oriented_cycle_channel_value_law import oriented_cycle_coeffs_from_block
from frontier_pmns_oriented_cycle_reduced_channel_nonselection import active_block_with_reduced_cycle
from frontier_pmns_sole_axiom_hw1_source_transfer_boundary import sole_axiom_hw1_source_transfer_pack
from frontier_pmns_uniform_scalar_deformation_boundary import scalar_triplet_block
from pmns_lower_level_utils import I3, active_response_columns_from_sector_operator, derive_active_block_from_response_columns

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


def gram_lift(a: np.ndarray) -> np.ndarray:
    return a.conj().T @ a


def relative_action_to_seed(h: np.ndarray) -> float:
    sign, logdet = np.linalg.slogdet(h)
    if sign <= 0:
        raise ValueError("matrix left the positive branch")
    return float(np.trace(h).real - logdet - 3.0)


def sigma_from_block(block: np.ndarray) -> complex:
    coeffs = oriented_cycle_coeffs_from_block(block)
    return complex(np.mean(coeffs))


def sigma_slice_block(sigma: float, u: float, v: float, xbar: float = 1.0) -> np.ndarray:
    w = 3.0 * sigma - 2.0 * u
    return active_block_with_reduced_cycle(u, v, w, xbar=xbar)


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


def checked_route_blocks(lam_act: float = 0.31) -> dict[str, np.ndarray]:
    pack = sole_axiom_hw1_source_transfer_pack(lam_act, 0.27)
    source_block = derive_active_block_from_response_columns(pack["active_columns"], lam_act)[1]

    scalar_block = scalar_triplet_block(1.13)
    scalar_cols = active_response_columns_from_sector_operator(scalar_block, lam_act)[1]
    scalar_active = derive_active_block_from_response_columns(scalar_cols, lam_act)[1]

    return {
        "free": I3.copy(),
        "hw1_source_transfer": source_block,
        "scalar": scalar_active,
    }


def part1_sigma_is_the_algebraic_cycle_coordinate_mean() -> None:
    print("\n" + "=" * 88)
    print("PART 1: SIGMA IS THE ALGEBRAIC CYCLE-COORDINATE MEAN")
    print("=" * 88)

    block = sigma_slice_block(sigma=0.23, u=0.23, v=0.0, xbar=1.0)
    xbar, sigma_transport = active_native_means(block)
    sigma_cycle = sigma_from_block(block)
    jchi = nontrivial_character_current(block)

    check("The algebraic cycle-coordinate mean equals the supplied block's transport mean", abs(sigma_cycle - sigma_transport) < 1.0e-12, f"xbar={xbar:.6f}, sigma={sigma_cycle:.6f}")
    check("At the supplied C3-covariant point the nontrivial character functional equals sigma", abs(jchi - sigma_cycle) < 1.0e-12, f"J_chi={jchi:.6f}, sigma={sigma_cycle:.6f}")
    check(
        "The matrix identity holds on a nonzero supplied point",
        abs(sigma_cycle) > 1.0e-6 and np.linalg.norm(block - I3) > 1.0e-6,
    )


def part2_three_named_route_blocks_have_sigma_zero() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THREE NAMED ROUTE BLOCKS HAVE SIGMA = 0")
    print("=" * 88)

    blocks = checked_route_blocks()
    sigmas = {name: sigma_from_block(block) for name, block in blocks.items()}

    check("The free retained PMNS route has sigma = 0", abs(sigmas["free"]) < 1.0e-12, f"sigma={sigmas['free']:.6f}")
    check("The canonical sole-axiom hw=1 source/transfer route has sigma = 0", abs(sigmas["hw1_source_transfer"]) < 1.0e-12, f"sigma={sigmas['hw1_source_transfer']:.6f}")
    check("The retained scalar PMNS route has sigma = 0", abs(sigmas["scalar"]) < 1.0e-12, f"sigma={sigmas['scalar']:.6f}")
    check(
        "All three named route blocks have sigma = 0",
        all(abs(value) < 1.0e-12 for value in sigmas.values()),
    )


def part3_the_same_route_blocks_have_jchi_zero() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE SAME ROUTE BLOCKS HAVE J_chi = 0")
    print("=" * 88)

    blocks = checked_route_blocks()
    currents = {name: nontrivial_character_current(block) for name, block in blocks.items()}

    check("The free retained PMNS route has J_chi = 0", abs(currents["free"]) < 1.0e-12, f"J_chi={currents['free']:.6f}")
    check("The canonical sole-axiom hw=1 source/transfer route has J_chi = 0", abs(currents["hw1_source_transfer"]) < 1.0e-12, f"J_chi={currents['hw1_source_transfer']:.6f}")
    check("The retained scalar PMNS route has J_chi = 0", abs(currents["scalar"]) < 1.0e-12, f"J_chi={currents['scalar']:.6f}")
    check(
        "All three named route blocks have J_chi = 0",
        all(abs(value) < 1.0e-12 for value in currents.values()),
    )


def part4_the_displayed_positive_lift_action_favors_the_zero_seed() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE DISPLAYED POSITIVE-LIFT ACTION FAVORS THE ZERO SEED")
    print("=" * 88)

    seed = sigma_slice_block(sigma=0.0, u=0.0, v=0.0, xbar=1.0)
    candidate = sigma_slice_block(sigma=0.23, u=0.23, v=0.0, xbar=1.0)
    seed_action = relative_action_to_seed(gram_lift(seed))
    candidate_action = relative_action_to_seed(gram_lift(candidate))

    check("The displayed unconstrained effective action is minimized at the zero seed", abs(seed_action) < 1.0e-12, f"S_seed={seed_action:.12f}")
    check("A nonzero sigma candidate on the canonical positive lift has strictly larger action", candidate_action > 1.0e-6, f"S_candidate={candidate_action:.12f}")
    check(
        "The tested nonzero candidate is not selected over the zero seed",
        seed_action + 1.0e-6 < candidate_action,
    )


def main() -> int:
    print("=" * 88)
    print("PMNS SIGMA-ZERO NO-GO")
    print("=" * 88)
    print()
    print("Question:")
    print("  Do the three named route blocks and the displayed positive-lift")
    print("  action force nonzero sigma?")

    part1_sigma_is_the_algebraic_cycle_coordinate_mean()
    part2_three_named_route_blocks_have_sigma_zero()
    part3_the_same_route_blocks_have_jchi_zero()
    part4_the_displayed_positive_lift_action_favors_the_zero_seed()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Route-specific PMNS boundary:")
    print("    - sigma is the algebraic cycle-coordinate/transport mean on the")
    print("      supplied blocks")
    print("    - the three named route blocks set sigma = 0 and J_chi = 0")
    print("    - the displayed positive-lift action favors the zero seed over the")
    print("      tested nonzero candidate")
    print()
    print("  This is not an exhaustive route or selector inventory. The coordinate")
    print("  lemma itself supplies no physical carrier, Record readout, or")
    print("  value-selection bridge.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
