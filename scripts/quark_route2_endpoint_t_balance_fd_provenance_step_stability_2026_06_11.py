"""Endpoint t_balance: finite-difference provenance + step-stability of the near-miss.

Establishes, on the live Route-2 support-tensor surface:

(P1) PROVENANCE: the current live endpoint readout ratios
     (|b_E/b_T|, |a_T/a_E|, |b_T/a_T|) are central-difference values of the
     eta-floor chain at the module step EPS = 0.005, reproduced here by
     re-running the live chain at that step.

(P2) STEP-STABILITY: the t_balance near-miss |b_T/a_T| - 1 ~ 3.1e-5 is NOT
     explained by the tested O(eps^2) finite-difference truncation model: over the stable
     window eps in [5e-4, 2e-3] the value stays inside a narrow band around
     1.00003, and Richardson extrapolation for the leading O(eps^2) term
     stays inside a slightly wider stated band.  The raw stable-window band
     excludes 1 by more than six times the observed jitter.

(P3) NOISE FLOOR: at and below eps ~ 2e-4 the central differences hit the chain's
     internal noise floor (values wander at the 1e-4 scale), which bounds the
     honest precision of any FD-based statement; the exact slope requires the
     named symbolic route (Hellmann-Feynman derivative of the eta floor),
     which this runner does not perform.

No status assertions; the parent gate is untouched.
"""
from __future__ import annotations

import math
import sys

import numpy as np

sys.path.insert(0, "scripts")

import frontier_same_source_metric_ansatz_scan as same  # noqa: E402
import frontier_tensor_support_center_excess_law as center  # noqa: E402

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"{tag}: {name}")
    if detail:
        print(f"    {detail}")


CURRENT_LIVE = {
    "slope_ratio": 2.621601678209,
    "shell_ratio": 2.005382749600,
    "t_balance": 1.000030814262,
}

# The stable-window band measured for t_balance including Richardson values.
BAND_LO = 1.0000259
BAND_HI = 1.0000319


def build_probe_vectors() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    basis = same.build_adapted_basis()
    e0 = basis[:, 0]
    s_unit = basis[:, 1] / math.sqrt(6.0)
    e1 = basis[:, 2]
    e2 = basis[:, 3]
    t1x = basis[:, 4]
    ex = (math.sqrt(3.0) * e1 + e2) / 2.0
    return e0, s_unit, ex, t1x


E0, S_UNIT, EX, T1X = build_probe_vectors()


def gamma_pair_at_step(q: np.ndarray, eps: float) -> tuple[float, float]:
    f = center.eta_floor
    beta_e = (f(q + eps * EX) - f(q - eps * EX)) / (2.0 * eps)
    beta_t = (f(q + eps * T1X) - f(q - eps * T1X)) / (2.0 * eps)
    red = center.shell.reduced_data(center.phi_from_q(q))
    anchor = float(red["anchor_per_Q"]) * float(np.sum(q))
    return beta_e / anchor, beta_t / anchor


def endpoint_ratios_at_step(eps: float) -> tuple[float, float, float]:
    gamma_e_center, gamma_t_center = gamma_pair_at_step(E0, eps)
    gamma_e_shell, gamma_t_shell = gamma_pair_at_step(S_UNIT, eps)
    delta_center = center.support_delta(E0)
    delta_shell = center.support_delta(S_UNIT)
    gap = delta_center - delta_shell
    slope_e = (gamma_e_center - gamma_e_shell) / gap
    intercept_e = gamma_e_shell - slope_e * delta_shell
    slope_t = (gamma_t_center - gamma_t_shell) / gap
    intercept_t = gamma_t_shell - slope_t * delta_shell
    return (
        abs(slope_e / slope_t),
        abs(intercept_t / intercept_e),
        abs(slope_t / intercept_t),
    )


def part1_provenance() -> None:
    print("\nPart 1: finite-difference provenance of the current live ratios")
    print("-" * 72)
    r = endpoint_ratios_at_step(0.005)
    names = ("slope_ratio", "shell_ratio", "t_balance")
    for value, name in zip(r, names):
        target = CURRENT_LIVE[name]
        check(
            f"current live {name} = {target:.12f} reproduced at module step EPS=0.005",
            abs(value - target) < 5e-12,
            f"recomputed {value:.12f}; |diff| = {abs(value - target):.2e}",
        )


def part2_step_stability() -> None:
    print("\nPart 2: step-stability of the t_balance near-miss (stable window)")
    print("-" * 72)
    window = [2e-3, 1e-3, 5e-4]
    values = {}
    print("  eps        |b_E/b_T|        |a_T/a_E|        |b_T/a_T|")
    for eps in window:
        r = endpoint_ratios_at_step(eps)
        values[eps] = r
        print(f"  {eps:7.1e}  {r[0]:.12f}  {r[1]:.12f}  {r[2]:.12f}")
    tb = [values[e][2] for e in window]
    check(
        "t_balance stays inside the narrow band over the stable window",
        all(BAND_LO <= v <= BAND_HI for v in tb),
        f"band [{BAND_LO}, {BAND_HI}]; observed [{min(tb):.9f}, {max(tb):.9f}]",
    )
    # Richardson: (4 f(eps/2) - f(eps)) / 3 cancels the leading O(eps^2)
    # term in the smooth-error model.
    print("  Richardson extrapolants (leading O(eps^2) cancellation model):")
    rich_values = []
    for eps in [2e-3, 1e-3]:
        fine = values.get(eps / 2.0) or endpoint_ratios_at_step(eps / 2.0)
        coarse = values[eps]
        rich = (4.0 * fine[2] - coarse[2]) / 3.0
        rich_values.append(rich)
        print(f"    from eps={eps:.0e}: t_balance -> {rich:.12f}")
    check(
        "Richardson extrapolants stay inside the same band",
        all(BAND_LO <= v <= BAND_HI for v in rich_values),
        f"extrapolants {['%.9f' % v for v in rich_values]}",
    )
    spread = max(tb) - min(tb)
    gap_to_one = min(tb) - 1.0
    check(
        "the band excludes t_balance = 1 by more than six times the observed spread",
        gap_to_one > 6.0 * spread,
        f"min(t_balance) - 1 = {gap_to_one:.2e}; window spread = {spread:.2e}",
    )


def part3_noise_floor() -> None:
    print("\nPart 3: small-step noise floor (bounds the honest FD precision)")
    print("-" * 72)
    noisy_steps = (2e-4, 1e-4, 5e-5)
    noisy = [endpoint_ratios_at_step(eps)[2] for eps in noisy_steps]
    for eps, v in zip(noisy_steps, noisy):
        print(f"  eps={eps:7.1e}: t_balance = {v:.12f}")
    drift = max(abs(v - 1.0000308) for v in noisy)
    check(
        "at/below eps ~ 2e-4 the chain leaves the stable band (internal noise floor)",
        any(not (BAND_LO <= v <= BAND_HI) for v in noisy),
        f"max |drift from 1.0000308| = {drift:.2e}; the exact slope needs the "
        "symbolic (Hellmann-Feynman) route, not smaller FD steps",
    )


def main() -> int:
    print("Endpoint t_balance: FD provenance + step stability")
    print("=" * 72)
    part1_provenance()
    part2_step_stability()
    part3_noise_floor()
    print(f"\nTOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
