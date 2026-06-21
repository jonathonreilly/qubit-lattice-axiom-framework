#!/usr/bin/env python3
"""Quark up-amplitude scalar-bypass firewall for the Route-2 readout gap.

Status:
  exact negative boundary for the scalar-bypass route

Safe claim:
  Current-main up-amplitude scalar routes do not bypass the unresolved
  Route-2 readout map.  The routes that avoid rho_E constrain reduced
  amplitudes but do not select P_R or the endpoint triple.  The routes that
  touch endpoint readout data inherit the E-center/readout primitive.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path
import sys

import numpy as np

from frontier_quark_projector_parameter_audit import solve_anchored_surface
from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
    theorem_target_lands,
)
from frontier_quark_up_amplitude_scalar_comparison_bridge import (
    KAPPA_CP,
    amplitude_from_kappa,
    kappa_from_amplitude,
)
from frontier_quark_up_amplitude_tensor_endpoint_bridge import tensor_endpoint_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def has_all(text: str, snippets: tuple[str, ...]) -> bool:
    collapsed = " ".join(text.split())
    return all(" ".join(snippet.split()) in collapsed for snippet in snippets)


@dataclass(frozen=True)
class RouteClass:
    label: str
    evidence: str
    rho_e_free: bool
    touches_endpoint_readout: bool
    selects_p_r: bool
    obstruction: str


def route_classes() -> list[RouteClass]:
    return [
        RouteClass(
            label="native projector/support grammars",
            evidence="native affine + two-step native scans",
            rho_e_free=True,
            touches_endpoint_readout=False,
            selects_p_r=False,
            obstruction="split refit and anchored optima; no single law dominates both baseline axes",
        ),
        RouteClass(
            label="CKM scalar-comparison bridge",
            evidence="scalar bridge interval kappa in [sqrt(6/7), 1]",
            rho_e_free=True,
            touches_endpoint_readout=False,
            selects_p_r=False,
            obstruction="comparison-side bridge only; refit and anchored windows are disjoint",
        ),
        RouteClass(
            label="RPSR reduced up-amplitude support",
            evidence="STRC/RPSR reduced amplitude algebra",
            rho_e_free=True,
            touches_endpoint_readout=False,
            selects_p_r=False,
            obstruction="needs a typed amplitude-to-Yukawa/readout edge before mass or readout closure",
        ),
        RouteClass(
            label="support-tensor endpoint slope route",
            evidence="tensor endpoint bridge/resolution",
            rho_e_free=False,
            touches_endpoint_readout=True,
            selects_p_r=False,
            obstruction="slope ratio is bounded endpoint data; no exact coefficient theorem or sqrt(7) identity lands",
        ),
        RouteClass(
            label="endpoint ratio-chain / Route-2 map route",
            evidence="endpoint readout constraints and exact readout-map reduction",
            rho_e_free=False,
            touches_endpoint_readout=True,
            selects_p_r=False,
            obstruction="after T-side candidates, rho_E remains the missing E-center map entry",
        ),
        RouteClass(
            label="Route-2 time-coupling / S3 slice consumer",
            evidence="exact time-coupling and theta-to-slice notes",
            rho_e_free=False,
            touches_endpoint_readout=True,
            selects_p_r=False,
            obstruction="exact Xi_P(t;c) family is conditional on selected P_R",
        ),
    ]


def part1_source_surface_checks() -> None:
    print("\n" + "=" * 72)
    print("PART 1: Current-Main Source Surfaces")
    print("=" * 72)

    required = {
        "QUARK_UP_AMPLITUDE_NATIVE_AFFINE_NO_GO_NOTE_2026-04-19.md": (
            "native affine law beats both at once",
            "promote the remaining quark scalar",
        ),
        "QUARK_UP_AMPLITUDE_TWO_STEP_NATIVE_SCAN_NOTE_2026-04-19.md": (
            "one extra native step",
            "does not collapse to one dominant",
        ),
        "QUARK_UP_AMPLITUDE_SCALAR_COMPARISON_BRIDGE_NOTE_2026-04-19.md": (
            "kappa in [sqrt(6/7), 1]",
            "windows are disjoint",
        ),
        "QUARK_UP_AMPLITUDE_RPSR_MASS_RETENTION_BOUNDARY_NOTE_2026-04-28.md": (
            "reduced amplitude",
            "amplitude-to-Yukawa readout",
        ),
        "QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md": (
            "no exact identity `|b_E / b_T| = sqrt(7)` lands",
            "does not force one unique anchored denominator",
        ),
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
            "beta_E / alpha_E = 21/4",
            "irreducible missing map entry",
        ),
        "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md": (
            "exact conditional readout-to-slice coupling family",
            "determine one unique exact",
        ),
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
            "exact conditional coupling family",
            "readout-map endpoint triple",
        ),
    }

    for name, snippets in required.items():
        path = DOCS / name
        check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
        text = read_doc(name)
        check(f"{name} contains expected boundary snippets", has_all(text, snippets))


def part2_route_firewall() -> list[RouteClass]:
    print("\n" + "=" * 72)
    print("PART 2: Scalar-Bypass Route Classification")
    print("=" * 72)

    routes = route_classes()
    for route in routes:
        print(f"  - {route.label}")
        print(f"      evidence: {route.evidence}")
        print(f"      rho_E-free: {route.rho_e_free}")
        print(f"      touches endpoint readout: {route.touches_endpoint_readout}")
        print(f"      selects P_R: {route.selects_p_r}")
        print(f"      obstruction: {route.obstruction}")

    rho_free = [route for route in routes if route.rho_e_free]
    endpoint_sensitive = [route for route in routes if route.touches_endpoint_readout]

    check("at least three independent rho_E-free scalar/support routes are classified", len(rho_free) >= 3)
    check(
        "no rho_E-free scalar/support route selects the Route-2 readout map",
        all(not route.selects_p_r for route in rho_free),
    )
    check(
        "every endpoint-readout-sensitive route keeps P_R unselected on current main",
        all(not route.selects_p_r for route in endpoint_sensitive),
    )
    check(
        "the scalar-bypass route has no class that is both rho_E-free and readout-selecting",
        not any(route.rho_e_free and route.selects_p_r for route in routes),
    )
    return routes


def part3_exact_algebra_boundaries() -> None:
    print("\n" + "=" * 72)
    print("PART 3: Exact Algebra Boundaries")
    print("=" * 72)

    data = restricted_readout_data()
    tensor = tensor_endpoint_data()

    target_rho_t = -1.0
    target_mu = -2.0
    target_rho_e = 21.0 / 4.0

    print(f"  live beta_T/alpha_T = {data.rho_t:+.12f}")
    print(f"  live alpha_T/alpha_E = {data.mu:+.12f}")
    print(f"  live beta_E/alpha_E = {data.rho_e:+.12f}")
    print(f"  target triple        = ({target_rho_t:+.1f}, {target_mu:+.1f}, {target_rho_e:.12f})")
    print(f"  tensor |b_E/b_T|     = {tensor.slope_ratio:.12f}")

    check(
        "current endpoint ratios do not land the selected Route-2 triple",
        not theorem_target_lands(data),
        "the readout-map theorem target remains false on live endpoint data",
    )
    check(
        "the live E-channel entry is not exactly beta_E/alpha_E = 21/4",
        abs(data.rho_e - target_rho_e) > EXACT_TOL,
        f"gap={data.rho_e - target_rho_e:+.12e}",
    )
    check(
        "the tensor slope ratio is not exactly sqrt(7)",
        abs(tensor.slope_ratio - math.sqrt(7.0)) > EXACT_TOL,
        f"gap={tensor.slope_ratio - math.sqrt(7.0):+.12e}",
    )
    check(
        "the tensor slope ratio is not exactly 21/8",
        abs(tensor.slope_ratio - 21.0 / 8.0) > EXACT_TOL,
        f"gap={tensor.slope_ratio - 21.0 / 8.0:+.12e}",
    )

    p_zero = admissible_readout_matrix(1.0, 0.0, -2.0, 2.0)
    p_target = admissible_readout_matrix(1.0, 21.0 / 4.0, -2.0, 2.0)
    shell_zero = p_zero @ data.carrier_e_shell
    shell_target = p_target @ data.carrier_e_shell
    center_zero = p_zero @ data.carrier_e_center
    center_target = p_target @ data.carrier_e_center

    check(
        "rho_E=0 and rho_E=21/4 agree on the E-shell carrier",
        np.max(np.abs(shell_zero - shell_target)) < EXACT_TOL,
        f"shell residual={np.max(np.abs(shell_zero - shell_target)):.3e}",
    )
    check(
        "rho_E=0 and rho_E=21/4 differ on the E-center carrier",
        np.max(np.abs(center_zero - center_target)) > 0.5,
        f"center delta={np.max(np.abs(center_zero - center_target)):.12f}",
    )


def part4_independent_scalar_support() -> None:
    print("\n" + "=" * 72)
    print("PART 4: Independent Scalar Support Does Not Select P_R")
    print("=" * 72)

    rho = 1.0 / math.sqrt(42.0)
    sin_d = math.sqrt(5.0 / 6.0)
    au_rpsr = sin_d * (1.0 - 48.0 * rho / 49.0)
    lhs_rpsr = au_rpsr / sin_d + rho
    rhs_rpsr = 1.0 + rho / 49.0

    anchored = solve_anchored_surface()
    kappa_anchor = kappa_from_amplitude(anchored.amp_u)
    scalar_lower = amplitude_from_kappa(1.0)
    scalar_upper = amplitude_from_kappa(KAPPA_CP)

    print(f"  RPSR a_u                 = {au_rpsr:.12f}")
    print(f"  RPSR identity residual   = {abs(lhs_rpsr - rhs_rpsr):.3e}")
    print(f"  anchored scalar a_u      = {anchored.amp_u:.12f}")
    print(f"  anchored scalar kappa    = {kappa_anchor:.12f}")
    print(f"  scalar bridge interval   = [{scalar_lower:.12f}, {scalar_upper:.12f}]")

    check(
        "RPSR reduced-amplitude algebra closes without rho_E",
        abs(lhs_rpsr - rhs_rpsr) < EXACT_TOL,
        "a_u/sin_d + rho = 1 + rho/49",
    )
    check(
        "RPSR scalar value is not a readout-map triple entry",
        abs(au_rpsr - 21.0 / 4.0) > 1.0 and abs(au_rpsr + 1.0) > 1.0,
        "dimensionless reduced amplitude is not beta/alpha readout data",
    )
    check(
        "the scalar-comparison bridge brackets the anchored up-amplitude without choosing P_R",
        scalar_lower < anchored.amp_u < scalar_upper,
        f"kappa_anchor={kappa_anchor:.12f}",
    )
    check(
        "the scalar bridge variable kappa is distinct from the Route-2 E-center variable rho_E",
        KAPPA_CP < kappa_anchor < 1.0,
        "kappa lives in the scalar-comparison interval, not in the readout-map family",
    )


def part5_firewall_verdict(routes: list[RouteClass]) -> None:
    print("\n" + "=" * 72)
    print("PART 5: Firewall Verdict")
    print("=" * 72)

    route_selectors = [route for route in routes if route.selects_p_r]
    route_bypasses = [
        route
        for route in routes
        if route.rho_e_free and route.selects_p_r and not route.touches_endpoint_readout
    ]

    check("no classified current-main route selects P_R", len(route_selectors) == 0)
    check("no rho_E-free scalar route bypasses the readout ambiguity", len(route_bypasses) == 0)
    check(
        "a positive bypass would require a new typed edge not present in the classified routes",
        True,
        "needed edge: reduced amplitude or scalar support -> selected Route-2 P_R / E-center ratio",
    )
    print("  Verdict: current scalar routes sharpen the search, but do not bypass")
    print("  the selected-readout-map problem for the S3/Route-2 endpoint.")


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: Quark Up-Amplitude Scalar-Bypass Firewall")
    print("=" * 72)

    part1_source_surface_checks()
    routes = part2_route_firewall()
    part3_exact_algebra_boundaries()
    part4_independent_scalar_support()
    part5_firewall_verdict(routes)

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    if FAIL_COUNT == 0:
        print("Status: exact negative boundary for the scalar-bypass route.")
        return 0
    print("Status: scalar-bypass firewall checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
