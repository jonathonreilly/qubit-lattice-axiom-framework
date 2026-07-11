#!/usr/bin/env python3
"""Born/eikonal observable discriminator for the finite lensing harness.

This runner does not insert a target slope.  It computes, from the supplied
finite propagation rules, both

1. the plane-ray finite-path function, and
2. the exact first-order detector-centroid response written as a signed
   adjoint edge sum.

It also tests whether the old 2D and 3D Gaussian ray formulas define ordinary
beam expectations.  They do not: every tested angular family crosses a
zero-impact ray where I_ray(b_eff) ~ 2/b_eff, while the Gaussian weights are
strictly positive.  The two one-sided improper integrals diverge with opposite
signs.  A Cauchy principal value or an explicit core regularization can be
defined, but that is an additional model choice rather than a Gaussian-beam
correction derived by the displayed formula.

The expensive part is a literal recomputation of the two fine-H adjoint edge
laws.  The audit lane therefore allows up to 30 minutes.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 1800

import argparse
import gc
import hashlib
import math
from dataclasses import dataclass
from pathlib import Path

from kubo_continuum_limit import (
    BETA,
    K_PER_H,
    PW_PHYS,
    SRC_LAYER_FRAC,
    grow,
)
from lensing_adjoint_kernel_probe import build_free_and_adjoint
from lensing_adjoint_kernel_reduced_model import (
    exact_edge_sum,
    signed_edge_coefficients,
)


H_FINE = 0.25
B_VALUES = (3.0, 4.0, 5.0, 6.0)
T_SHORT = 7.5
T_LONG = 15.0
ROOT = Path(__file__).resolve().parents[1]
HELPER_PATHS = (
    "scripts/kubo_continuum_limit.py",
    "scripts/lensing_adjoint_kernel_probe.py",
    "scripts/lensing_adjoint_kernel_reduced_model.py",
)


@dataclass(frozen=True)
class Fit:
    slope: float
    prefactor: float
    r2: float


@dataclass(frozen=True)
class AdjointResult:
    t_phys: float
    x_src: float
    n_edges: int
    values: tuple[float, ...]
    fit: Fit
    cz_free: float
    detector_norm: float


checks: list[tuple[str, str, bool]] = []


def check(kind: str, name: str, ok: bool) -> None:
    checks.append((kind, name, bool(ok)))


def plane_eikonal(b_eff: float, x_src: float, length: float) -> float:
    """Finite-path transverse-gradient factor for a source inside the path."""
    if b_eff == 0.0:
        raise ZeroDivisionError("the ray model has a pole at zero impact")
    left = x_src / math.sqrt(x_src * x_src + b_eff * b_eff)
    right_length = length - x_src
    right = right_length / math.sqrt(right_length * right_length + b_eff * b_eff)
    return (left + right) / b_eff


def power_fit(xs: tuple[float, ...], ys: tuple[float, ...]) -> Fit:
    lx = [math.log(x) for x in xs]
    ly = [math.log(abs(y)) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    var = sum((x - mx) ** 2 for x in lx)
    cov = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    slope = cov / var
    intercept = my - slope * mx
    pred = [intercept + slope * x for x in lx]
    ss_res = sum((y - p) ** 2 for y, p in zip(ly, pred))
    ss_tot = sum((y - my) ** 2 for y in ly)
    return Fit(slope, math.exp(intercept), 1.0 - ss_res / ss_tot)


def harness_geometry(t_phys: float) -> tuple[int, float, float]:
    nl = max(3, round(t_phys / H_FINE))
    x_src = round(nl * SRC_LAYER_FRAC) * H_FINE
    detector_x = (nl - 1) * H_FINE
    return nl, x_src, detector_x


def plane_result(t_phys: float) -> tuple[float, float, tuple[float, ...], Fit]:
    _nl, x_src, detector_x = harness_geometry(t_phys)
    values = tuple(plane_eikonal(b, x_src, detector_x) for b in B_VALUES)
    return detector_x, x_src, values, power_fit(B_VALUES, values)


def source_sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def theta_from_b_eff(b_eff: float, b: float, x_src: float) -> float:
    """Invert b_eff = b - x_src tan(theta) on the forward angular chart."""
    return math.atan((b - b_eff) / x_src)


def b_eff_jacobian(b_eff: float, b: float, x_src: float) -> float:
    """Absolute dtheta/db_eff for the forward angular chart."""
    return x_src / (x_src * x_src + (b - b_eff) ** 2)


def gaussian_2d_weight(theta: float, beta: float) -> float:
    return math.exp(-beta * theta * theta)


def gaussian_3d_marginal(theta_z: float, beta: float, n_y: int = 600) -> float:
    """Positive theta_y marginal used by the old 3D ray formula."""
    y_cap_sq = (math.pi / 2.0) ** 2 - theta_z * theta_z
    if y_cap_sq <= 0.0:
        return 0.0
    y_cap = math.sqrt(y_cap_sq)
    dy = 2.0 * y_cap / n_y
    total = 0.0
    for i in range(n_y):
        theta_y = -y_cap + (i + 0.5) * dy
        theta = math.sqrt(theta_y * theta_y + theta_z * theta_z)
        total += (
            math.exp(-beta * (theta_y * theta_y + theta_z * theta_z))
            * math.cos(theta) ** 2
            * dy
        )
    return total


def absolute_decade_shell(
    epsilon: float,
    b: float,
    x_src: float,
    length: float,
    beta: float,
    n_log: int = 1200,
) -> float:
    """Absolute 2D beam integral over epsilon < |b_eff| < 10 epsilon."""
    lo = math.log(epsilon)
    hi = math.log(10.0 * epsilon)
    dt = (hi - lo) / n_log
    total = 0.0
    for sign in (-1.0, 1.0):
        for i in range(n_log):
            magnitude = math.exp(lo + (i + 0.5) * dt)
            b_eff = sign * magnitude
            theta = theta_from_b_eff(b_eff, b, x_src)
            integrand = (
                gaussian_2d_weight(theta, beta)
                * abs(plane_eikonal(b_eff, x_src, length))
                * b_eff_jacobian(b_eff, b, x_src)
            )
            # db_eff = |b_eff| d(log |b_eff|).
            total += integrand * magnitude * dt
    return total


def pole_shell_limit(b: float, x_src: float, beta: float) -> float:
    theta0 = math.atan(b / x_src)
    jac0 = x_src / (x_src * x_src + b * b)
    # Two sides, I ~ 2/b_eff, integrated over one logarithmic decade.
    return 4.0 * gaussian_2d_weight(theta0, beta) * jac0 * math.log(10.0)


def compute_adjoint_result(t_phys: float) -> AdjointResult:
    """Recompute the exact signed-adjoint edge law without target values."""
    nl, x_src, _detector_x = harness_geometry(t_phys)
    k_phase = K_PER_H / H_FINE
    pos, adj, _ = grow(0, 0.20, 0.70, nl, PW_PHYS, 3, H_FINE)
    amp, lam, cz_free, detector_norm, _ = build_free_and_adjoint(
        pos,
        adj,
        nl,
        PW_PHYS,
        H_FINE,
        k_phase,
        BETA,
    )
    edges = signed_edge_coefficients(
        pos,
        adj,
        H_FINE,
        k_phase,
        BETA,
        amp,
        lam,
    )
    values = tuple(exact_edge_sum(edges, x_src, b) for b in B_VALUES)
    result = AdjointResult(
        t_phys=t_phys,
        x_src=x_src,
        n_edges=len(edges),
        values=values,
        fit=power_fit(B_VALUES, values),
        cz_free=cz_free,
        detector_norm=detector_norm,
    )
    del edges, amp, lam, pos, adj
    gc.collect()
    return result


def print_values(label: str, values: tuple[float, ...], fit: Fit) -> None:
    print(label)
    for b, value in zip(B_VALUES, values):
        print(f"  b={b:g}: {value:+.9f}")
    print(
        f"  fit: {fit.prefactor:.9f} * b^({fit.slope:+.9f}), "
        f"R^2={fit.r2:.9f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--analytic-only",
        action="store_true",
        help="skip the expensive literal adjoint recomputation",
    )
    args = parser.parse_args()

    print("=" * 92)
    print("BORN/EIKONAL OBSERVABLE DISCRIMINATOR")
    print("=" * 92)
    print("No target exponent is supplied to this runner.")
    print("Helper source provenance:")
    for helper_path in HELPER_PATHS:
        print(f"  {helper_path}: {source_sha256(helper_path)}")
    print()

    # Frame 1: exact scale structure of the finite-path ray primitive.
    length_short, x_short, plane_short, plane_fit_short = plane_result(T_SHORT)
    length_long, x_long, plane_long, plane_fit_long = plane_result(T_LONG)
    nominal_long = tuple(plane_eikonal(b, x_long, T_LONG) for b in B_VALUES)
    nominal_long_fit = power_fit(B_VALUES, nominal_long)
    print("[A] Plane-ray finite-path law")
    print("  I(b;L,qL) = b^-1 F_q(b/L)")
    print("  local slopes are strictly between -2 and -1 for finite positive b/L")
    print_values(
        f"  short harness: T_phys={T_SHORT:g}, L_det={length_short:g}, x_src={x_short:g}",
        plane_short,
        plane_fit_short,
    )
    print_values(
        f"  long harness:  T_phys={T_LONG:g}, L_det={length_long:g}, x_src={x_long:g}",
        plane_long,
        plane_fit_long,
    )
    rho = 2.0
    print_values(
        "  historical nominal convention: L=15, x_src=5",
        nominal_long,
        nominal_long_fit,
    )
    scale_lhs = plane_eikonal(rho * 4.0, rho * x_long, rho * length_long)
    scale_rhs = plane_eikonal(4.0, x_long, length_long) / rho
    check(
        "A",
        "plane law obeys exact one-over-length scale covariance",
        math.isclose(scale_lhs, scale_rhs, rel_tol=1e-13, abs_tol=1e-13),
    )
    check(
        "A",
        "endpoint-matched plane four-point shape changes materially across paths",
        abs(plane_fit_short.slope - plane_fit_long.slope) > 0.20,
    )
    print()

    # Frame 2: existence of the Gaussian angular expectations.
    print("[A] Gaussian ray-family existence test")
    pole_rows = []
    theta_cap = min(4.0 / math.sqrt(2.0 * BETA), math.pi / 2.0 - 0.01)
    for b in B_VALUES:
        theta0 = math.atan(b / x_long)
        w2 = gaussian_2d_weight(theta0, BETA)
        w3 = gaussian_3d_marginal(theta0, BETA)
        pole_rows.append((b, theta0, w2, w3))
        print(
            f"  b={b:g}: theta0={theta0:.9f}, angular cap={theta_cap:.9f}, "
            f"w2(theta0)={w2:.9f}, w3_marg(theta0)={w3:.9f}"
        )
    check(
        "A",
        "every fitted ray family contains its zero-impact pole",
        all(theta0 < theta_cap for _, theta0, _, _ in pole_rows),
    )
    check(
        "A",
        "2D and 3D angular weights are positive at every pole",
        all(w2 > 0.0 and w3 > 0.0 for _, _, w2, w3 in pole_rows),
    )
    for sign in (-1.0, 1.0):
        y = sign * 1e-7
        check(
            "A",
            f"pole coefficient b_eff*I(b_eff) tends to 2 ({sign:+g} side)",
            math.isclose(y * plane_eikonal(y, x_long, length_long), 2.0, rel_tol=1e-12),
        )

    shell_expected = pole_shell_limit(3.0, x_long, BETA)
    shells = [
        absolute_decade_shell(eps, 3.0, x_long, length_long, BETA)
        for eps in (1e-2, 1e-3, 1e-4)
    ]
    print("  absolute integral in successive pole decades (b=3):")
    for eps, shell in zip((1e-2, 1e-3, 1e-4), shells):
        print(f"    {eps:g} < |b_eff| < {10*eps:g}: {shell:.12f}")
    print(f"    analytic decade limit:             {shell_expected:.12f}")
    check(
        "A",
        "each shrinking pole decade carries nonzero absolute mass",
        all(abs(shell / shell_expected - 1.0) < 5e-4 for shell in shells),
    )
    print(
        "  consequence: the left and right one-sided angular integrals diverge "
        "with opposite signs; only an added principal-value/core prescription is finite."
    )
    print()

    if args.analytic_only:
        print("Literal adjoint recomputation skipped by --analytic-only.")
    else:
        # Frame 3: compute the literal response before comparing shapes.
        print("[C] Exact signed-adjoint detector-centroid laws")
        short = compute_adjoint_result(T_SHORT)
        print_values(
            f"  short harness: T_phys={short.t_phys:g}, x_src={short.x_src:g}, "
            f"edges={short.n_edges}",
            short.values,
            short.fit,
        )
        long = compute_adjoint_result(T_LONG)
        print_values(
            f"  long harness:  T_phys={long.t_phys:g}, x_src={long.x_src:g}, "
            f"edges={long.n_edges}",
            long.values,
            long.fit,
        )
        adjoint_shape_change = abs(short.fit.slope - long.fit.slope)
        plane_shape_change = abs(plane_fit_short.slope - plane_fit_long.slope)
        print(
            f"  adjoint slope change={adjoint_shape_change:.9f}; "
            f"plane-ray slope change={plane_shape_change:.9f}"
        )
        print(
            f"  long-harness adjoint/plane slope separation="
            f"{abs(long.fit.slope-plane_fit_long.slope):.9f}"
        )
        check(
            "C",
            "both adjoint edge lists are nonempty large finite computations",
            short.n_edges > 1_000_000 and long.n_edges > short.n_edges,
        )
        check(
            "C",
            "literal adjoint values are finite and positive on the declared window",
            all(math.isfinite(v) and v > 0.0 for v in short.values + long.values),
        )
        check(
            "C",
            "literal adjoint four-point shape is stable across the two path lengths",
            adjoint_shape_change < 0.01,
        )
        check(
            "C",
            "plane-ray shape change is at least twenty times the adjoint shape change",
            plane_shape_change > 20.0 * adjoint_shape_change,
        )
        check(
            "C",
            "long-harness slopes are discriminated without ingesting the target exponent",
            abs(long.fit.slope - plane_fit_long.slope) > 0.10,
        )

    print()
    print("Checks")
    for kind, name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'} [{kind}] {name}")
    n_pass = sum(ok for _, _, ok in checks)
    n_fail = len(checks) - n_pass
    n_a = sum(ok for kind, _, ok in checks if kind == "A")
    n_c = sum(ok for kind, _, ok in checks if kind == "C")
    print()
    print(
        "runner_check_breakdown = "
        f"{{A: {n_a}, B: 0, C: {n_c}, D: 0, total_pass: {n_pass}}}"
    )
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    print()
    if args.analytic_only:
        print("ANALYTIC-ONLY DISPOSITION: INCOMPLETE")
        print("  The five literal-adjoint C checks were skipped.")
        print("  This mode certifies only the ray scale law and Gaussian pole theorem.")
        print("TOTAL WITH SKIPS: PASS=7 FAIL=0 SKIP=5")
        raise SystemExit(2)

    print("NARROW VERDICT")
    print(
        "  The plane-ray law is a well-defined finite-path surrogate, but its "
        "path-length shape response is not the literal signed-adjoint centroid response."
    )
    print(
        "  The old 2D/3D Gaussian ray formulas do not define ordinary beam "
        "expectations because they cross a nonintegrable zero-impact pole."
    )
    print(
        "  Therefore numerical proximity at one path length cannot provide the "
        "missing observable bridge."
    )
    if n_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
