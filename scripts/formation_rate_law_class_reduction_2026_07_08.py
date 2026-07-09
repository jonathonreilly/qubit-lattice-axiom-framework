#!/usr/bin/env python3
"""Block02 rate-law CLASS reduction runner.

Purpose
-------
This is the Block02 runner for the record-rate-gravity derivation: the
rate-law CLASS reduction.  It uses only the minimal axiom content:
"Records form."; "A site never carries more than one record; records are
permanent."; and "the available possibilities are determined by, and vary
with, the nearest-neighbor conditions."  The same axiom note also leaves
"formation rules ... at what rate" downstream, so this file does not promote
any one rate law to primitive status.

The runner shows that for every local, covariant, monotone rate law in the
named class with the forced endpoint F(0)=0, the emergent local event-rate
field has rate-law-independent weak-field structure: saturation freeze is
universal; the linear weak-field response is controlled only by the single
dimensionless number gF = F'(A0) A0 / F(A0); and law differences first enter
at second order in the crowding contrast.

Companion note:
FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md.

The process clock used below is a comparator device, not a time metric.  The
resetting simulation is a toy measurement apparatus only: the axioms have
permanent records.  Resetting is used solely to create a stationary comparator
background whose local event-rate field can be sampled.  Permanence physics is
represented by the exact weak-field leg plus the no-reset saturation leg.  This
runner makes no gravity claim and sets no audit status.

Design concerns intentionally surfaced in stdout:
* The stochastic leg is a d=1 toy reduction of the census's Z^3 story.
* The measured collapse uses a common weak-field crowding probe, not a separate
  law-dependent stationary matter ensemble, because the latter mostly measures
  different backgrounds rather than the rate-law class.
* The 1D linear no-reset control uses a small positive endpoint floor so it can
  reach full occupancy; the horizon-class profile alone has A(2)=0 and can
  terminate below full occupancy with frozen open sites.
* The 15% measured-collapse gate is an honest finite-contrast tolerance.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Callable

import numpy as np


SEED = 20260708
R0 = 1.0
FD_TOL = 1.0e-10
SECOND_ORDER_MIN_SPREAD = 5.0e-2
MEASURED_COLLAPSE_REL_TOL = 0.15
SIGMA_GATE = 5.0
MU = 0.02
CLOCK_BATCHES = 40
CLOCK_BATCH_TIME = 30000.0
CLOCK_BURN_TIME = 1000.0
L_RING = 200
B_SIZE = 40
B_PINNED = 8
WEAK_PROBE_DR = 0.05
LINEAR_1D_FLOOR = 0.10


FloatFn = Callable[[float], float]


@dataclass(frozen=True)
class RateLaw:
    name: str
    short: str
    raw: FloatFn


@dataclass(frozen=True)
class Profile:
    name: str
    availability: FloatFn


RATE_LAWS = (
    RateLaw("linear", "lin", lambda a: a),
    RateLaw("sqrt", "sqrt", math.sqrt),
    RateLaw("quadratic", "quad", lambda a: a * a),
    RateLaw("saturating", "sat", lambda a: a / (1.0 + a)),
    RateLaw("exponential", "exp", lambda a: -math.expm1(-a)),
)


LEG1_PROFILES = (
    Profile("linear6", lambda r: 6.0 - r),
    Profile("convex6", lambda r: (6.0 - r) ** 2 / 6.0),
    Profile("horizon6", lambda r: (6.0 - r) ** 4 / 125.0),
)


SIM_PROFILES = (
    Profile("linear1d", lambda r: max(LINEAR_1D_FLOOR, LINEAR_1D_FLOOR + 2.0 - r)),
    Profile("horizon1d", lambda r: max(0.0, 2.0 - r) ** 2),
)


def fd5_first(f: FloatFn, x: float, h: float) -> float:
    return (-f(x + 2.0 * h) + 8.0 * f(x + h) - 8.0 * f(x - h) + f(x - 2.0 * h)) / (
        12.0 * h
    )


def fd5_second(f: FloatFn, x: float, h: float) -> float:
    return (
        -f(x + 2.0 * h)
        + 16.0 * f(x + h)
        - 30.0 * f(x)
        + 16.0 * f(x - h)
        - f(x - 2.0 * h)
    ) / (12.0 * h * h)


def richardson_derivative(f: FloatFn, x: float, order: int) -> float:
    if order not in (1, 2):
        raise ValueError("order must be 1 or 2")
    stencil = fd5_first if order == 1 else fd5_second
    powers = range(3, 18) if order == 1 else range(3, 13)
    estimates: list[float] = []
    for k in powers:
        h = 2.0 ** (-k)
        d_h = stencil(f, x, h)
        d_h2 = stencil(f, x, h / 2.0)
        estimates.append(d_h2 + (d_h2 - d_h) / 15.0)
    best = min(range(1, len(estimates)), key=lambda i: abs(estimates[i] - estimates[i - 1]))
    return estimates[best]


def normalized_law(law: RateLaw, a0: float) -> FloatFn:
    f0 = law.raw(a0)
    if f0 <= 0.0:
        raise ValueError(f"{law.name} has non-positive F(A0)")
    return lambda a: law.raw(a) / f0


def g_factor(law: RateLaw, a0: float) -> float:
    return richardson_derivative(law.raw, a0, 1) * a0 / law.raw(a0)


def check_endpoint() -> None:
    for law in RATE_LAWS:
        value = law.raw(0.0)
        if value != 0.0:
            raise AssertionError(f"{law.name} violates forced endpoint: F(0)={value!r}")


def exact_weak_field() -> tuple[dict[str, float], dict[str, float], dict[str, dict[str, float]]]:
    collapse_spreads: dict[str, float] = {}
    second_spreads: dict[str, float] = {}
    collapsed_values: dict[str, dict[str, float]] = {}
    for profile in LEG1_PROFILES:
        a0 = profile.availability(R0)
        collapsed: list[float] = []
        seconds: list[float] = []
        collapsed_values[profile.name] = {}
        for law in RATE_LAWS:
            f_norm = normalized_law(law, a0)
            rate = lambda r, f_norm=f_norm, profile=profile: f_norm(profile.availability(r))
            rate0 = rate(R0)
            linear_response = richardson_derivative(rate, R0, 1) / rate0
            collapsed_response = linear_response / g_factor(law, a0)
            second_response = richardson_derivative(rate, R0, 2) / rate0
            collapsed.append(collapsed_response)
            seconds.append(second_response)
            collapsed_values[profile.name][law.short] = collapsed_response
        collapse_spreads[profile.name] = max(collapsed) - min(collapsed)
        second_spreads[profile.name] = max(seconds) - min(seconds)
    return collapse_spreads, second_spreads, collapsed_values


@dataclass(frozen=True)
class ClockResult:
    profile: str
    law: str
    n_a: float
    err_a: float
    n_b: float
    err_b: float
    sigma: float
    contrast_over_g: float


def aggregate_probe_clock(
    lambda_a: float,
    lambda_b: float,
    rng: np.random.Generator,
    batches: int = CLOCK_BATCHES,
    batch_time: float = CLOCK_BATCH_TIME,
) -> tuple[float, float, float, float, float]:
    """Exact d=1 Gillespie for two aggregate open-site counters.

    Each unpinned site is a two-state comparator: open -> recorded at its local
    probe rate, recorded -> open at MU.  The B block has B_PINNED permanently
    recorded sites, so its unpinned comparator count is smaller.
    """

    n_a_sites = L_RING - B_SIZE
    n_b_sites = B_SIZE - B_PINNED
    open_a = int(rng.binomial(n_a_sites, MU / (lambda_a + MU)))
    open_b = int(rng.binomial(n_b_sites, MU / (lambda_b + MU)))

    def run_until(total_time: float, measure: bool) -> list[tuple[float, float]]:
        nonlocal open_a, open_b
        t = 0.0
        next_batch = batch_time
        event_a = 0
        event_b = 0
        open_time_a = 0.0
        open_time_b = 0.0
        out: list[tuple[float, float]] = []

        while t < total_time:
            rates = (
                open_a * lambda_a,
                open_b * lambda_b,
                (n_a_sites - open_a) * MU,
                (n_b_sites - open_b) * MU,
            )
            total = sum(rates)
            if total <= 0.0:
                raise RuntimeError("aggregate clock process has zero total rate")
            dt = float(rng.exponential(1.0 / total))

            while measure and t + dt > next_batch:
                part = next_batch - t
                open_time_a += part * open_a
                open_time_b += part * open_b
                if open_time_a <= 0.0 or open_time_b <= 0.0:
                    raise RuntimeError("empty open-time batch in clock measurement")
                out.append((event_a / open_time_a, event_b / open_time_b))
                event_a = 0
                event_b = 0
                open_time_a = 0.0
                open_time_b = 0.0
                dt -= part
                t = next_batch
                next_batch += batch_time

            if measure:
                open_time_a += dt * open_a
                open_time_b += dt * open_b
            t += dt

            draw = float(rng.random() * total)
            c0 = rates[0]
            c1 = c0 + rates[1]
            c2 = c1 + rates[2]
            if draw < c0:
                if open_a <= 0:
                    raise RuntimeError("invalid A formation event")
                open_a -= 1
                if measure:
                    event_a += 1
            elif draw < c1:
                if open_b <= 0:
                    raise RuntimeError("invalid B formation event")
                open_b -= 1
                if measure:
                    event_b += 1
            elif draw < c2:
                if open_a >= n_a_sites:
                    raise RuntimeError("invalid A reset event")
                open_a += 1
            else:
                if open_b >= n_b_sites:
                    raise RuntimeError("invalid B reset event")
                open_b += 1
        return out

    run_until(CLOCK_BURN_TIME, measure=False)
    batches_out = run_until(batches * batch_time, measure=True)
    arr = np.asarray(batches_out, dtype=float)
    if arr.shape != (batches, 2):
        raise RuntimeError(f"expected {batches} clock batches, got {arr.shape}")
    means = arr.mean(axis=0)
    errs = arr.std(axis=0, ddof=1) / math.sqrt(batches)
    sigma = (means[0] - means[1]) / math.hypot(errs[0], errs[1])
    return float(means[0]), float(errs[0]), float(means[1]), float(errs[1]), float(sigma)


def measured_clock() -> list[ClockResult]:
    results: list[ClockResult] = []
    for p_index, profile in enumerate(SIM_PROFILES):
        a0 = profile.availability(R0)
        a_b = profile.availability(R0 + WEAK_PROBE_DR)
        if not (0.0 <= a_b < a0):
            raise AssertionError(f"{profile.name} probe does not reduce availability")
        for l_index, law in enumerate(RATE_LAWS):
            f_norm = normalized_law(law, a0)
            lambda_a = f_norm(a0)
            lambda_b = f_norm(a_b)
            rng = np.random.default_rng(SEED + 1000 * p_index + 37 * l_index)
            n_a, err_a, n_b, err_b, sigma = aggregate_probe_clock(lambda_a, lambda_b, rng)
            contrast = (n_a - n_b) / n_a
            results.append(
                ClockResult(
                    profile=profile.name,
                    law=law.short,
                    n_a=n_a,
                    err_a=err_a,
                    n_b=n_b,
                    err_b=err_b,
                    sigma=sigma,
                    contrast_over_g=contrast / g_factor(law, a0),
                )
            )
    return results


@dataclass(frozen=True)
class SaturationResult:
    profile: str
    law: str
    final_occupancy: float
    frozen_open: int
    monotone: bool
    points: tuple[tuple[float, float], ...]


def local_rates_no_reset(recorded: np.ndarray, profile: Profile, law: RateLaw) -> np.ndarray:
    a0 = profile.availability(R0)
    f_norm = normalized_law(law, a0)
    left = np.roll(recorded, 1)
    right = np.roll(recorded, -1)
    neighbor_count = left.astype(int) + right.astype(int)
    rates = np.zeros(recorded.shape[0], dtype=float)
    open_indices = np.flatnonzero(~recorded)
    for idx in open_indices:
        rates[idx] = f_norm(profile.availability(float(neighbor_count[idx])))
    return rates


def saturation_run(profile: Profile, law: RateLaw, seed_offset: int) -> SaturationResult:
    rng = np.random.default_rng(SEED + seed_offset)
    recorded = rng.random(L_RING) < 0.30
    total_rates: list[float] = []
    occupancies: list[float] = []

    while True:
        rates = local_rates_no_reset(recorded, profile, law)
        total_rate = float(rates.sum())
        total_rates.append(total_rate)
        occupancies.append(float(recorded.mean()))
        if total_rate == 0.0:
            break
        draw = float(rng.random() * total_rate)
        idx = int(np.searchsorted(np.cumsum(rates), draw, side="right"))
        if recorded[idx] or rates[idx] <= 0.0:
            raise RuntimeError("selected invalid no-reset formation event")
        recorded[idx] = True
        if len(total_rates) > 10 * L_RING:
            raise RuntimeError("no-reset saturation exceeded event bound")

    monotone = all(b <= a + 1.0e-12 for a, b in zip(total_rates, total_rates[1:]))
    open_sites = np.flatnonzero(~recorded)
    frozen_open = int(open_sites.size)
    sample_indices = np.linspace(0, len(total_rates) - 1, min(5, len(total_rates)), dtype=int)
    points = tuple((occupancies[i], total_rates[i]) for i in sample_indices)
    return SaturationResult(
        profile=profile.name,
        law=law.short,
        final_occupancy=float(recorded.mean()),
        frozen_open=frozen_open,
        monotone=monotone,
        points=points,
    )


def saturation_checks() -> tuple[SaturationResult, SaturationResult]:
    linear_profile = SIM_PROFILES[0]
    horizon_profile = SIM_PROFILES[1]
    linear_law = RATE_LAWS[0]
    linear = saturation_run(linear_profile, linear_law, 900)
    horizon = saturation_run(horizon_profile, linear_law, 901)
    return linear, horizon


def rel_spread(values: list[float]) -> float:
    mean_abs = abs(sum(values) / len(values))
    if mean_abs == 0.0:
        return math.inf
    return (max(values) - min(values)) / mean_abs


def format_clock(results: list[ClockResult]) -> str:
    chunks: list[str] = []
    for profile in (p.name for p in SIM_PROFILES):
        prof_results = [r for r in results if r.profile == profile]
        body = ",".join(
            f"{r.law}:A={r.n_a:.4f}+/-{r.err_a:.4f} B={r.n_b:.4f}+/-{r.err_b:.4f} "
            f"z={r.sigma:.1f} Cg={r.contrast_over_g:.4f}"
            for r in prof_results
        )
        spread = rel_spread([r.contrast_over_g for r in prof_results])
        chunks.append(f"{profile}[relspread={spread:.3f};{body}]")
    return " | ".join(chunks)


def format_points(points: tuple[tuple[float, float], ...]) -> str:
    return ",".join(f"({occ:.3f},{rate:.3f})" for occ, rate in points)


def run_all() -> tuple[str, str, str, str, str]:
    check_endpoint()
    collapse_spreads, second_spreads, _ = exact_weak_field()
    clock_results = measured_clock()
    linear_sat, horizon_sat = saturation_checks()

    check01 = True
    check02 = all(spread <= FD_TOL for spread in collapse_spreads.values())
    check03 = any(spread > SECOND_ORDER_MIN_SPREAD for spread in second_spreads.values())
    check04 = all((r.n_b < r.n_a) and (r.sigma >= SIGMA_GATE) for r in clock_results)
    check05 = all(
        rel_spread([r.contrast_over_g for r in clock_results if r.profile == profile.name])
        <= MEASURED_COLLAPSE_REL_TOL
        for profile in SIM_PROFILES
    )
    check06 = (
        linear_sat.monotone
        and horizon_sat.monotone
        and linear_sat.final_occupancy == 1.0
        and linear_sat.frozen_open == 0
        and horizon_sat.final_occupancy < 1.0
        and horizon_sat.frozen_open > 0
    )

    exact_line = (
        "EXACT: CHECK-01 endpoint pass; CHECK-02 max collapse spread="
        f"{max(collapse_spreads.values()):.3e}; CHECK-03 second-order spreads="
        + ",".join(f"{k}:{v:.3f}" for k, v in second_spreads.items())
    )
    sim_line = "SIM-CLOCK: " + format_clock(clock_results)
    sat_line = (
        "SATURATION: "
        f"{linear_sat.profile}/{linear_sat.law} occ={linear_sat.final_occupancy:.3f} "
        f"frozen_open={linear_sat.frozen_open} monotone={linear_sat.monotone} "
        f"curve={format_points(linear_sat.points)} | "
        f"{horizon_sat.profile}/{horizon_sat.law} occ={horizon_sat.final_occupancy:.3f} "
        f"frozen_open={horizon_sat.frozen_open} monotone={horizon_sat.monotone} "
        f"curve={format_points(horizon_sat.points)}"
    )
    check_line = (
        "CHECKS: "
        f"01={check01} 02={check02} 03={check03} 04={check04} 05={check05} 06={check06}"
    )
    spec_line = (
        "SPEC-NOTE: resetting=comparator-not-axiom; d1-reduction; common weak-field "
        "crowding probe for measured collapse; pins=8/40 with reduced transverse "
        "crowding; linear1d uses positive floor, horizon1d has A(2)=0; no gravity/audit claim."
    )

    if all((check01, check02, check03, check04, check05, check06)):
        verdict = "CLASS-REDUCED"
    elif not (check02 and check05):
        verdict = "CLASS-NOT-REDUCED"
    else:
        verdict = "CLASS-NOT-REDUCED"
    total_line = f"TOTAL: {verdict}"
    return exact_line, sim_line, sat_line, check_line, spec_line, total_line


def main() -> int:
    try:
        for line in run_all():
            print(line)
        return 0
    except Exception as exc:  # noqa: BLE001 - runner must fail closed in stdout.
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
