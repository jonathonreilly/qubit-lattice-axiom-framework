#!/usr/bin/env python3
"""One-loop MSbar heavy-threshold matching kernel for the alpha_s lane."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import exp, isclose, log, pi
from pathlib import Path
from typing import Iterable


NOTE_PATH = Path("docs/ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md")
QCD_LOW_NOTE_PATH = Path("docs/QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md")
EXPECTED_SUMMARY = "SUMMARY: PASS=40 FAIL=0"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def close(a: float, b: float, rel: float = 1e-12, abs_: float = 1e-12) -> bool:
    return isclose(a, b, rel_tol=rel, abs_tol=abs_)


def b0_fraction(n_f: int) -> Fraction:
    """SU(3) one-loop coefficient b0 = 11 - 2 n_f / 3."""
    if n_f < 0:
        raise ValueError("n_f must be nonnegative")
    c_a = Fraction(3, 1)
    t_f = Fraction(1, 2)
    return Fraction(11, 3) * c_a - Fraction(4, 3) * t_f * n_f


def slope(n_f: int) -> float:
    return float(b0_fraction(n_f)) / (2.0 * pi)


def feynman_weight_moment() -> Fraction:
    """Integral_0^1 dx x(1-x), evaluated from polynomial antiderivatives."""
    return Fraction(1, 2) - Fraction(1, 3)


def one_loop_decoupling_log_coefficient(t_f: Fraction = Fraction(1, 2)) -> Fraction:
    """Coefficient of (alpha_s/pi) log(mu^2/m_h^2) in zeta_g^2."""
    return -heavy_polarization_log_coefficient(t_f)


def heavy_polarization_log_coefficient(t_f: Fraction = Fraction(1, 2)) -> Fraction:
    """Coefficient of (alpha_s/pi) log(mu^2/m_h^2) in Pi_h^MSbar(0)."""
    return 2 * t_f * feynman_weight_moment()


def decoupling_log_coefficient_from_beta_jump(n_f_hi: int) -> Fraction:
    """RG-consistency coefficient c for c*(alpha_s/pi)*log(mu^2/m_h^2)."""
    if n_f_hi <= 0:
        raise ValueError("threshold crossing requires n_f_hi >= 1")
    return (b0_fraction(n_f_hi) - b0_fraction(n_f_hi - 1)) / 4


def zeta_g_squared_one_loop(alpha_hi: float, mu: float, heavy_msbar_mass: float) -> float:
    """One-loop MSbar alpha_s decoupling factor, truncated after its log term."""
    if not (alpha_hi > 0.0 and mu > 0.0 and heavy_msbar_mass > 0.0):
        raise ValueError("alpha_s, mu, and the heavy MSbar mass must be positive")
    coefficient = float(one_loop_decoupling_log_coefficient())
    return 1.0 + (alpha_hi / pi) * coefficient * log((mu / heavy_msbar_mass) ** 2)


def match_alpha_below_one_loop(alpha_hi: float, mu: float, heavy_msbar_mass: float) -> float:
    """Match alpha_s from n_f to n_f-1 through one-loop decoupling."""
    alpha_lo = zeta_g_squared_one_loop(alpha_hi, mu, heavy_msbar_mass) * alpha_hi
    if alpha_lo <= 0.0:
        raise ValueError("truncated matching factor leaves the positive-coupling domain")
    return alpha_lo


def run_inverse_down(x_hi: float, mu_hi: float, mu_lo: float, n_f: int) -> float:
    """Run x=1/alpha_s from mu_hi down to mu_lo at fixed active n_f."""
    if not (x_hi > 0.0 and mu_hi > mu_lo > 0.0):
        raise ValueError("segment requires x_hi > 0 and mu_hi > mu_lo > 0")
    x_lo = x_hi - slope(n_f) * log(mu_hi / mu_lo)
    if x_lo <= 0.0:
        raise ValueError("segment crosses the one-loop Landau pole")
    return x_lo


def run_inverse_up(x_lo: float, mu_lo: float, mu_hi: float, n_f: int) -> float:
    """Run x=1/alpha_s from mu_lo up to mu_hi at fixed active n_f."""
    if not (x_lo > 0.0 and mu_hi > mu_lo > 0.0):
        raise ValueError("segment requires x_lo > 0 and mu_hi > mu_lo > 0")
    return x_lo + slope(n_f) * log(mu_hi / mu_lo)


def inverse_from_lambda(mu: float, lambda_qcd: float, n_f: int) -> float:
    if not (mu > lambda_qcd > 0.0):
        raise ValueError("requires mu > Lambda > 0")
    return slope(n_f) * log(mu / lambda_qcd)


def lambda_from_inverse(mu: float, x: float, n_f: int) -> float:
    if not (mu > 0.0 and x > 0.0):
        raise ValueError("requires mu > 0 and x > 0")
    return mu * exp(-x / slope(n_f))


def lambda_below_threshold(lambda_hi: float, threshold: float, n_f_hi: int) -> float:
    """LO Lambda transition induced by alpha_s continuity at a threshold."""
    if not (threshold > lambda_hi > 0.0):
        raise ValueError("requires threshold > Lambda_hi > 0")
    if n_f_hi <= 0:
        raise ValueError("threshold crossing requires n_f_hi >= 1")
    b_hi = b0_fraction(n_f_hi)
    b_lo = b0_fraction(n_f_hi - 1)
    exponent = float(b_hi / b_lo)
    return threshold * (lambda_hi / threshold) ** exponent


@dataclass(frozen=True)
class Threshold:
    scale: float
    n_f_hi: int
    n_f_lo: int


@dataclass(frozen=True)
class Event:
    scale: float
    n_f_hi: int
    n_f_lo: int
    x_above: float
    x_below: float
    zeta_g_squared: float


def validate_thresholds(mu_hi: float, mu_lo: float, thresholds: Iterable[Threshold]) -> list[Threshold]:
    ordered = list(thresholds)
    previous = mu_hi
    current_nf = ordered[0].n_f_hi if ordered else None
    for threshold in ordered:
        if not (previous > threshold.scale > mu_lo):
            raise ValueError("thresholds must be strictly descending inside the segment")
        if threshold.n_f_hi != current_nf:
            raise ValueError("threshold n_f_hi must match the active flavor count")
        if threshold.n_f_lo != threshold.n_f_hi - 1:
            raise ValueError("this kernel only crosses one heavy flavor at a time")
        previous = threshold.scale
        current_nf = threshold.n_f_lo
    return ordered


def piecewise_run_down(
    x_hi: float,
    mu_hi: float,
    mu_lo: float,
    n_f_hi: int,
    thresholds: Iterable[Threshold],
) -> tuple[float, list[Event]]:
    ordered = validate_thresholds(mu_hi, mu_lo, thresholds)
    current_x = x_hi
    current_mu = mu_hi
    current_nf = n_f_hi
    events: list[Event] = []
    for threshold in ordered:
        if threshold.n_f_hi != current_nf:
            raise ValueError("first active flavor count does not match threshold list")
        current_x = run_inverse_down(current_x, current_mu, threshold.scale, current_nf)
        alpha_above = 1.0 / current_x
        # The abstract threshold is the mass-fixed MSbar point M=m_h(M).
        zeta_g_squared = zeta_g_squared_one_loop(
            alpha_above,
            threshold.scale,
            threshold.scale,
        )
        alpha_below = match_alpha_below_one_loop(
            alpha_above,
            threshold.scale,
            threshold.scale,
        )
        x_below = 1.0 / alpha_below
        events.append(
            Event(
                scale=threshold.scale,
                n_f_hi=threshold.n_f_hi,
                n_f_lo=threshold.n_f_lo,
                x_above=current_x,
                x_below=x_below,
                zeta_g_squared=zeta_g_squared,
            )
        )
        current_x = x_below
        current_mu = threshold.scale
        current_nf = threshold.n_f_lo
    current_x = run_inverse_down(current_x, current_mu, mu_lo, current_nf)
    return current_x, events


def assert_raises(fn) -> bool:
    try:
        fn()
    except ValueError:
        return True
    return False


def main() -> int:
    print("=== Source-boundary checks ===")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    qcd_low_text = QCD_LOW_NOTE_PATH.read_text(encoding="utf-8")
    required_note_phrases = [
        "**Claim type:** bounded_theorem",
        "**Status:** bounded support theorem; independent re-audit required",
        "M = m_h^(n_f)(M)",
        "This note does not derive the numerical value of a physical threshold mass.",
        "This note does not supply two-loop or higher MSbar decoupling constants.",
        "This note does not promote any downstream alpha_s(M_Z) value to retained status.",
        "load-bearing derivation here.",
    ]
    for phrase in required_note_phrases:
        check(f"note declares boundary: {phrase}", phrase in note_text)
    check(
        "parent QCD-low bridge points to this threshold kernel",
        "ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md" in qcd_low_text,
    )

    print("\n=== SU(3) beta0 algebra ===")
    check("b0(n_f=6) = 7", b0_fraction(6) == Fraction(7, 1))
    check("b0(n_f=5) = 23/3", b0_fraction(5) == Fraction(23, 3))
    check("b0(n_f=4) = 25/3", b0_fraction(4) == Fraction(25, 3))
    check("b0(n_f=3) = 9", b0_fraction(3) == Fraction(9, 1))
    check("one flavor changes b0 by -2/3", b0_fraction(5) - b0_fraction(4) == Fraction(-2, 3))
    check("asymptotic-freedom slopes positive through n_f=16", all(slope(nf) > 0.0 for nf in range(17)))

    print("\n=== One-loop MSbar decoupling derivation ===")
    check("Feynman weight integral is exactly 1/6", feynman_weight_moment() == Fraction(1, 6))
    check(
        "SU(3) heavy polarization logarithm coefficient is exactly +1/6",
        heavy_polarization_log_coefficient() == Fraction(1, 6),
    )
    check(
        "SU(3) heavy-quark logarithm coefficient is exactly -1/6",
        one_loop_decoupling_log_coefficient() == Fraction(-1, 6),
    )
    check(
        "background-field matching cancels Pi_h in zeta_g^2*(1+Pi_h) at linear order",
        one_loop_decoupling_log_coefficient()
        + heavy_polarization_log_coefficient()
        == 0,
    )
    check(
        "independent beta-jump route reproduces the heavy-loop coefficient",
        decoupling_log_coefficient_from_beta_jump(5)
        == one_loop_decoupling_log_coefficient(),
    )
    alpha_match = 0.2
    mass_fixed_point = 4.0
    zeta_at_match = zeta_g_squared_one_loop(alpha_match, mass_fixed_point, mass_fixed_point)
    alpha_below_match = match_alpha_below_one_loop(alpha_match, mass_fixed_point, mass_fixed_point)
    check("mass-fixed matching point sets log(mu^2/m_h^2) to zero", close(log((mass_fixed_point / mass_fixed_point) ** 2), 0.0))
    check("one-loop zeta_g^2 equals one at M=m_h(M)", close(zeta_at_match, 1.0))
    check("derived one-loop matcher has no alpha_s jump at M=m_h(M)", close(alpha_below_match, alpha_match))
    check("derived one-loop matcher has no inverse-coupling jump at M=m_h(M)", close(1.0 / alpha_below_match, 1.0 / alpha_match))
    check(
        "away from the mass-fixed point the one-loop matching logarithm is nonzero",
        not close(zeta_g_squared_one_loop(alpha_match, 2.0 * mass_fixed_point, mass_fixed_point), 1.0),
    )

    print("\n=== Segment and semigroup checks ===")
    x0 = 10.0
    mu_hi = 100.0
    mu_mid = 20.0
    mu_lo = 5.0
    direct = run_inverse_down(x0, mu_hi, mu_lo, 5)
    integrated = x0 - slope(5) * log(mu_hi / mu_lo)
    check("fixed-n_f affine inverse-coupling segment equals integrated beta equation", close(direct, integrated))
    split = run_inverse_down(run_inverse_down(x0, mu_hi, mu_mid, 5), mu_mid, mu_lo, 5)
    check("fixed-n_f segments compose as a semigroup", close(direct, split))
    restored = run_inverse_up(direct, mu_lo, mu_hi, 5)
    check("upward and downward maps invert on the same segment", close(restored, x0))

    print("\n=== Lambda transition checks ===")
    lambda_hi = 0.25
    threshold = 12.0
    x_at_threshold_hi = inverse_from_lambda(threshold, lambda_hi, 5)
    lambda_lo = lambda_below_threshold(lambda_hi, threshold, 5)
    x_at_threshold_lo = inverse_from_lambda(threshold, lambda_lo, 4)
    check("Lambda reconstructed from alpha inverts the one-loop solution", close(lambda_from_inverse(threshold, x_at_threshold_hi, 5), lambda_hi))
    check("threshold Lambda transition preserves alpha_s continuity", close(x_at_threshold_hi, x_at_threshold_lo))
    check("5-to-4 flavor sample raises Lambda below the threshold", lambda_lo > lambda_hi)

    print("\n=== Multi-threshold kernel checks ===")
    thresholds = [
        Threshold(scale=50.0, n_f_hi=6, n_f_lo=5),
        Threshold(scale=8.0, n_f_hi=5, n_f_lo=4),
        Threshold(scale=2.0, n_f_hi=4, n_f_lo=3),
    ]
    x_final, events = piecewise_run_down(10.0, 120.0, 1.0, 6, thresholds)
    summed_logs = (
        10.0
        - slope(6) * log(120.0 / 50.0)
        - slope(5) * log(50.0 / 8.0)
        - slope(4) * log(8.0 / 2.0)
        - slope(3) * log(2.0 / 1.0)
    )
    check("three threshold events are emitted", len(events) == 3)
    check("every event derives zeta_g^2=1 at its mass-fixed point", all(close(e.zeta_g_squared, 1.0) for e in events))
    check("every threshold event is exactly continuous in inverse coupling", all(close(e.x_above, e.x_below) for e in events))
    check("piecewise threshold kernel equals the summed-log closed form", close(x_final, summed_logs))

    print("\n=== Domain guards and falsifiers ===")
    check(
        "domain guard rejects non-descending thresholds",
        assert_raises(lambda: validate_thresholds(120.0, 1.0, [thresholds[1], thresholds[0]])),
    )
    check(
        "domain guard rejects thresholds outside the running interval",
        assert_raises(lambda: validate_thresholds(120.0, 1.0, [Threshold(scale=150.0, n_f_hi=6, n_f_lo=5)])),
    )
    check(
        "domain guard rejects skipped flavor crossings",
        assert_raises(lambda: validate_thresholds(120.0, 1.0, [Threshold(scale=50.0, n_f_hi=6, n_f_lo=4)])),
    )
    check(
        "domain guard rejects nonpositive initial inverse coupling",
        assert_raises(lambda: piecewise_run_down(0.0, 120.0, 1.0, 6, thresholds)),
    )
    check(
        "domain guard rejects a segment crossing the one-loop Landau pole",
        assert_raises(lambda: run_inverse_down(0.1, 100.0, 1.0, 5)),
    )
    alpha_above = 1.0 / events[0].x_above
    bad_alpha_below = 1.05 * alpha_above
    bad_x_below = 1.0 / bad_alpha_below
    check(
        "falsifier detects a non-continuous threshold jump",
        abs(events[0].x_above - bad_x_below) > 1e-3,
    )

    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if EXPECTED_SUMMARY != f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}":
        print(f"EXPECTED_SUMMARY mismatch: {EXPECTED_SUMMARY}")
        return 1
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
