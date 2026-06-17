#!/usr/bin/env python3
"""Ideal lock-in detector theorem for the Diamond/NV discriminator lane.

This runner proves the detector-map part of the Diamond/NV handoff without
using a textbook identity as an unverified import.  It applies the lock-in
definition directly to delayed sinusoidal source histories, then checks the
analytic formula against numerical cycle averages.

Scope:

- ideal detector only: perfect phase reference, integer-cycle integration,
  no technical noise, no finite bandwidth, no NV transfer coefficient;
- no derivation that the repo source dynamics produce the delayed field;
- no calibrated lab-amplitude or detectability claim.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

AUDIT_TIMEOUT_SEC = 120

TOL = 1.0e-10


@dataclass(frozen=True)
class LockinResult:
    amplitude: float
    frequency_hz: float
    delay_s: float
    x_numeric: float
    y_numeric: float
    x_formula: float
    y_formula: float
    phase_rad: float

    @property
    def omega_tau(self) -> float:
        return 2.0 * math.pi * self.frequency_hz * self.delay_s

    @property
    def max_abs_error(self) -> float:
        return max(
            abs(self.x_numeric - self.x_formula),
            abs(self.y_numeric - self.y_formula),
        )


def principal_phase(theta: float) -> float:
    """Return theta in (-pi, pi]."""

    return math.atan2(math.sin(theta), math.cos(theta))


def analytic_channels(
    amplitude: float,
    frequency_hz: float,
    delay_s: float,
    *,
    reference_flip: bool = False,
) -> tuple[float, float]:
    theta = 2.0 * math.pi * frequency_hz * delay_s
    sign = -1.0 if reference_flip else 1.0
    return sign * amplitude * math.cos(theta), sign * amplitude * math.sin(theta)


def numeric_channels(
    amplitude: float,
    frequency_hz: float,
    delay_s: float,
    *,
    cycles: int = 8,
    samples_per_cycle: int = 2048,
    reference_flip: bool = False,
    static_source: bool = False,
) -> tuple[float, float]:
    omega = 2.0 * math.pi * frequency_hz
    samples = cycles * samples_per_cycle
    duration = cycles / frequency_hz
    dt = duration / samples
    x_acc = 0.0
    y_acc = 0.0
    ref_phase = math.pi if reference_flip else 0.0

    for k in range(samples):
        t = (k + 0.5) * dt
        if static_source:
            signal = amplitude
        else:
            signal = amplitude * math.cos(omega * (t - delay_s))
        x_acc += signal * math.cos(omega * t + ref_phase)
        y_acc += signal * math.sin(omega * t + ref_phase)

    # Lock-in convention: twice the cycle average gives the input amplitude for
    # an in-phase unit sinusoid.
    return 2.0 * x_acc / samples, 2.0 * y_acc / samples


def lockin_result(amplitude: float, frequency_hz: float, delay_s: float) -> LockinResult:
    x_num, y_num = numeric_channels(amplitude, frequency_hz, delay_s)
    x_formula, y_formula = analytic_channels(amplitude, frequency_hz, delay_s)
    return LockinResult(
        amplitude=amplitude,
        frequency_hz=frequency_hz,
        delay_s=delay_s,
        x_numeric=x_num,
        y_numeric=y_num,
        x_formula=x_formula,
        y_formula=y_formula,
        phase_rad=math.atan2(y_num, x_num),
    )


def fit_slope(xs: list[float], ys: list[float]) -> float:
    x_bar = sum(xs) / len(xs)
    y_bar = sum(ys) / len(ys)
    num = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    den = sum((x - x_bar) ** 2 for x in xs)
    return num / den


def widefield_phase_slope(
    frequency_hz: float,
    tau0_s: float,
    tau_per_pixel_s: float,
    pixels: list[float],
) -> tuple[float, float, list[float]]:
    phases = [
        principal_phase(2.0 * math.pi * frequency_hz * (tau0_s + tau_per_pixel_s * z))
        for z in pixels
    ]
    slope = fit_slope(pixels, phases)
    expected = 2.0 * math.pi * frequency_hz * tau_per_pixel_s
    return slope, expected, phases


def run_checks() -> tuple[bool, list[str]]:
    lines: list[str] = []
    ok = True

    cases = [
        (1.0, 100.0, 0.0),
        (1.0, 100.0, 0.1e-6),
        (1.0, 1_000.0, 0.1e-6),
        (1.0, 10_000.0, 1.0e-6),
        (0.37, 2_500.0, 0.4e-6),
    ]
    results = [lockin_result(*case) for case in cases]
    max_err = max(r.max_abs_error for r in results)
    ok &= max_err < TOL
    lines.append(f"analytic lock-in formula max_abs_error={max_err:.3e} tol={TOL:.1e}")

    # Small-delay law: Y / X = tan(omega tau), so Y / X ~ omega tau when
    # omega tau is small.
    small = lockin_result(1.0, 1_000.0, 0.1e-6)
    ratio = small.y_numeric / small.x_numeric
    tan_expected = math.tan(small.omega_tau)
    ok &= abs(ratio - tan_expected) < TOL
    ok &= abs(ratio - small.omega_tau) < 1.0e-9
    lines.append(
        "small-delay law "
        f"Y/X={ratio:.12e} tan(omega*tau)={tan_expected:.12e} "
        f"omega*tau={small.omega_tau:.12e}"
    )

    # Controls: no driven source or a static source has no AC lock-in response.
    x_off, y_off = numeric_channels(0.0, 1_000.0, 0.7e-6)
    x_static, y_static = numeric_channels(
        1.0, 1_000.0, 0.0, static_source=True
    )
    control_max = max(abs(x_off), abs(y_off), abs(x_static), abs(y_static))
    ok &= control_max < TOL
    lines.append(f"drive-off/static-source controls max_abs_channel={control_max:.3e}")

    # Pi reference flip changes the sign of both lock-in channels.
    x0, y0 = numeric_channels(1.0, 1_000.0, 0.3e-6)
    x_pi, y_pi = numeric_channels(1.0, 1_000.0, 0.3e-6, reference_flip=True)
    flip_err = max(abs(x_pi + x0), abs(y_pi + y0))
    ok &= flip_err < TOL
    lines.append(f"pi-reference flip sign_error={flip_err:.3e}")

    pixels = [-2.0, -1.0, 0.0, 1.0, 2.0]
    slope, expected_slope, phases = widefield_phase_slope(
        frequency_hz=1_000.0,
        tau0_s=0.4e-6,
        tau_per_pixel_s=0.2e-6,
        pixels=pixels,
    )
    slope_err = abs(slope - expected_slope)
    ok &= slope_err < TOL
    lines.append(
        "widefield phase slope "
        f"fit={slope:.12e} expected={expected_slope:.12e} error={slope_err:.3e}"
    )
    lines.append(
        "widefield phases "
        + ", ".join(f"z={z:+.0f}:{phi:+.6e}" for z, phi in zip(pixels, phases))
    )

    return ok, lines


def build_report() -> str:
    ok, check_lines = run_checks()
    rows = [
        lockin_result(1.0, 100.0, 0.1e-6),
        lockin_result(1.0, 1_000.0, 0.1e-6),
        lockin_result(1.0, 10_000.0, 1.0e-6),
    ]

    lines: list[str] = []
    lines.append("DIAMOND IDEAL LOCK-IN DETECTOR THEOREM")
    lines.append("ASSERTIONS: PASS" if ok else "ASSERTIONS: FAIL")
    lines.append("")
    lines.append("Scope:")
    lines.append("  ideal lock-in detector map only; no NV transfer coefficient or lab noise model")
    lines.append("  no claim that repo source dynamics already produce the delayed field")
    lines.append("")
    lines.append("Definitions:")
    lines.append("  signal_z(t) = A_z cos(omega * (t - tau_z))")
    lines.append("  X_z = 2 <signal_z(t) cos(omega t)> over integer drive cycles")
    lines.append("  Y_z = 2 <signal_z(t) sin(omega t)> over integer drive cycles")
    lines.append("")
    lines.append("Theorem:")
    lines.append("  X_z = A_z cos(omega tau_z)")
    lines.append("  Y_z = A_z sin(omega tau_z)")
    lines.append("  phi_z = atan2(Y_z, X_z) = omega tau_z mod 2*pi")
    lines.append("  if tau_z = tau_0 + kappa z and phases are unwrapped, dphi/dz = omega kappa")
    lines.append("")
    lines.append("Numerical cycle-average checks:")
    for line in check_lines:
        lines.append(f"  {line}")
    lines.append("")
    lines.append("| f (Hz) | tau (us) | omega*tau | X | Y | phi (rad) |")
    lines.append("| ---: | ---: | ---: | ---: | ---: | ---: |")
    for row in rows:
        lines.append(
            f"| {row.frequency_hz:.0f} | {row.delay_s * 1e6:.3f} | "
            f"{row.omega_tau:.6e} | {row.x_numeric:+.6e} | "
            f"{row.y_numeric:+.6e} | {row.phase_rad:+.6e} |"
        )
    lines.append("")
    lines.append("Conclusion:")
    lines.append(
        "  the ideal detector bridge from a delayed driven source to X, Y, phi,"
        " and a widefield phase slope is closed at this bounded mathematical scope"
    )
    return "\n".join(lines)


def main() -> int:
    ok, _ = run_checks()
    print(build_report())
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
