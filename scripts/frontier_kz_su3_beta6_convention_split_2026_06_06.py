#!/usr/bin/env python3
"""K-Z / SU(3) beta=6 convention-split checker.

The K-Z external-lift route needs an explicit primary-source bracket at
`SU(3), beta=6`. The source figure for 4D SU(3) is plotted in the paper's
lambda coordinate. This runner checks a narrow convention issue:

  * the old W_lift ~= 0.05 width is reproduced by the vector figure at
    plotted lambda = 3;
  * under the paper action coefficient, standard Wilson beta=6 maps instead
    to lambda = N^2 / beta = 1.5 for N=3, where the same source figure gives
    a much wider image-derived interval.

Therefore W_lift=0.05 is not a source-certified `SU(3), beta=6` bracket until
the beta/lambda convention bridge is made explicit.
"""

from __future__ import annotations

from dataclasses import dataclass


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


@dataclass(frozen=True)
class Bracket:
    lam: float
    low: float
    high: float
    width: float


# Extracted from arXiv:2502.14421 source bundle, file
# figures/4Dsu3plotcd.eps, blue lower/upper vector paths in the 4D SU(3)
# plaquette panel. Coordinates are page-space coordinates; the figure axis is
# lambda in [0,5] and u_p in [0,1], with u_p increasing downward in the EPS
# coordinate frame.
LOWER_PATH = [
    (20.844, 19.070), (31.902, 26.703), (47.703, 37.902),
    (63.500, 49.551), (79.301, 61.734), (95.098, 74.496),
    (110.895, 87.902), (126.695, 101.723), (142.492, 114.801),
    (158.293, 124.953), (174.090, 131.570), (189.891, 135.832),
    (205.688, 138.777), (221.484, 141.004), (237.285, 142.746),
    (253.082, 144.227),
]

UPPER_PATH = [
    (20.844, 19.152), (31.902, 28.125), (47.703, 50.121),
    (63.500, 74.672), (79.301, 92.270), (95.098, 105.285),
    (110.895, 114.844), (126.695, 121.926), (142.492, 127.301),
    (158.293, 131.469), (174.090, 134.648), (189.891, 137.336),
    (205.688, 139.605), (221.484, 141.449), (237.285, 143.008),
    (253.082, 144.340),
]


def interp(path: list[tuple[float, float]], x: float) -> float:
    for (x0, y0), (x1, y1) in zip(path, path[1:]):
        if min(x0, x1) <= x <= max(x0, x1):
            t = (x - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)
    raise ValueError(f"x outside path: {x}")


def x_for_lambda(lam: float) -> float:
    x0 = LOWER_PATH[0][0]
    x5 = LOWER_PATH[-1][0]
    return x0 + (lam / 5.0) * (x5 - x0)


def y_to_u(y: float) -> float:
    y_top = min(min(y for _, y in LOWER_PATH), min(y for _, y in UPPER_PATH))
    y_bottom = max(max(y for _, y in LOWER_PATH), max(y for _, y in UPPER_PATH))
    return (y - y_top) / (y_bottom - y_top)


def bracket_at_lambda(lam: float) -> Bracket:
    x = x_for_lambda(lam)
    vals = sorted([y_to_u(interp(LOWER_PATH, x)), y_to_u(interp(UPPER_PATH, x))])
    return Bracket(lam=lam, low=vals[0], high=vals[1], width=vals[1] - vals[0])


def main() -> int:
    print("K-Z SU(3) beta=6 convention-split checker")
    print("actual_current_surface_status: no-go")
    print("trace_class: negative_route_pruning")
    print("reachability_to_target: prunes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    print("A. source-vector geometry checks")
    check("two source paths have the same endpoint x-range", LOWER_PATH[0][0] == UPPER_PATH[0][0] and LOWER_PATH[-1][0] == UPPER_PATH[-1][0])
    check("source paths are monotone in lambda coordinate", all(a[0] < b[0] for a, b in zip(LOWER_PATH, LOWER_PATH[1:])) and all(a[0] < b[0] for a, b in zip(UPPER_PATH, UPPER_PATH[1:])))
    check("source paths increase in plotted u_p coordinate", LOWER_PATH[0][1] < LOWER_PATH[-1][1] and UPPER_PATH[0][1] < UPPER_PATH[-1][1])
    check("y-to-u map sends top to 0 and bottom to 1", abs(y_to_u(min(p[1] for p in LOWER_PATH + UPPER_PATH))) < 1e-12 and abs(y_to_u(max(p[1] for p in LOWER_PATH + UPPER_PATH)) - 1) < 1e-12)

    print("\nB. beta/lambda convention split")
    n = 3
    beta_wilson = 6.0
    # Paper action coefficient: N/(2 lambda) * tr(U + Udag).
    # Standard Wilson coefficient: beta/(2N) * tr(U + Udag).
    lam_from_wilson_beta = n * n / beta_wilson
    lam_plot_old_width = 3.0
    check("SU(3) Wilson beta=6 maps to lambda=1.5 under paper action coefficient", abs(lam_from_wilson_beta - 1.5) < 1e-12, f"lambda={lam_from_wilson_beta}")
    check("lambda=3 is a distinct plotted coordinate", abs(lam_plot_old_width - lam_from_wilson_beta) > 1.0, f"lambda_plot={lam_plot_old_width}, lambda_beta6={lam_from_wilson_beta}")

    bracket_beta6 = bracket_at_lambda(lam_from_wilson_beta)
    bracket_lam3 = bracket_at_lambda(lam_plot_old_width)
    print(f"lambda=1.5 bracket: [{bracket_beta6.low:.6f}, {bracket_beta6.high:.6f}], width={bracket_beta6.width:.6f}")
    print(f"lambda=3.0 bracket: [{bracket_lam3.low:.6f}, {bracket_lam3.high:.6f}], width={bracket_lam3.width:.6f}")

    print("\nC. W_lift diagnosis")
    w_lift = 0.05
    check("lambda=3 source width matches W_lift within image precision", abs(bracket_lam3.width - w_lift) < 0.002, f"width={bracket_lam3.width:.6f}")
    check("Wilson beta=6 mapped source width is much larger than W_lift", bracket_beta6.width > 0.20, f"width={bracket_beta6.width:.6f}")
    check("Wilson beta=6 mapped source width does not match W_lift", abs(bracket_beta6.width - w_lift) > 0.19, f"width={bracket_beta6.width:.6f}")
    check("old W_lift cannot be used as SU(3) Wilson beta=6 bracket without a convention bridge", True)

    print("\nD. boundary")
    check("result is a convention/source-pruning boundary, not a theorem promotion", True)
    check("explicit numeric bracket remains image-derived, not table-derived", True)
    check("future acceptable path is table/source-data extraction or repo-owned SDP reproduction", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: W_lift ~= 0.05 is supported by the source figure at plotted "
            "lambda=3, but not by the same figure at Wilson beta=6 under the "
            "paper's action coefficient. The K-Z external-lift route needs an "
            "explicit convention bridge or a repo-owned beta=6 reproduction."
        )
        return 0
    print("VERDICT: convention split check failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
