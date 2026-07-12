#!/usr/bin/env python3
"""Source-step-free certificate for a finite cubic-star tensor response.

This runner replaces the former class-E definition/existence check.  It
computes the directional derivative of the declared finite tensor stencil,
checks the unique max-absolute branch, and replays the endpoint and midpoint
values as high-precision Dirichlet sine sums.  The result is a bounded
numerical non-affinity witness, not a certified exact nonzero theorem.

Claim boundary: the fixed SIZE=15, R=4, cubic ``mode="nearest"`` interpolation,
three-probe, coordinate-step h=1/25 algorithm only.  No continuum, physical
tensor-primitive, GR, or exact affine-law claim is made.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
from scipy.ndimage import map_coordinates

import quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12 as stepfree
import quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12 as exactsum


GRID_X = tuple(Fraction(k, 10) for k in range(11))
ACTIVE_ID = (0, 0, 0)
CHECKS: list[tuple[str, bool, str, str]] = []
HELPER_HASHES = {
    "quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py":
        "87c70736f62c2e845d8b750e1341fddb16f0be5a64427bb408178c5d7a39f64e",
    "quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py":
        "58fca749d3f95c02f7775f45d889bcc0e0ebe04636a88b0aaeb59617cdd3ff36",
}


def check(name: str, condition: bool, detail: str, status: str) -> None:
    CHECKS.append((name, bool(condition), detail, status))
    print(f"[{status}] {'PASS' if condition else 'FAIL'}: {name}")
    print(f"    {detail}")


def adapted_vectors() -> dict[str, np.ndarray]:
    e0 = np.zeros(7)
    e0[0] = 1.0
    px, mx, py, my, pz, mz = [np.eye(7)[i] for i in range(1, 7)]
    s_unit = (px + mx + py + my + pz + mz) / 6.0
    e1 = (px + mx - py - my) / 2.0
    e2 = (px + mx + py + my - 2.0 * pz - 2.0 * mz) / math.sqrt(12.0)
    ex = (math.sqrt(3.0) * e1 + e2) / 2.0
    eperp = (-e1 + math.sqrt(3.0) * e2) / 2.0
    tx = (px - mx) / math.sqrt(2.0)
    ty = (py - my) / math.sqrt(2.0)
    tz = (pz - mz) / math.sqrt(2.0)
    return {
        "e0": e0,
        "s_unit": s_unit,
        "ex": ex,
        "eperp": eperp,
        "tx": tx,
        "ty": ty,
        "tz": tz,
    }


def rotation_x_quarter_turn() -> np.ndarray:
    """Proper cubic rotation (x,y,z) -> (x,-z,y) on the star support."""
    coords = (
        (0, 0, 0),
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    index = {coord: idx for idx, coord in enumerate(coords)}
    rot = np.zeros((7, 7))
    for src, (x, y, z) in enumerate(coords):
        rot[index[(x, -z, y)], src] = 1.0
    return rot


def canonical_q(x: Fraction, vec: dict[str, np.ndarray]) -> np.ndarray:
    xf = float(x)
    return xf * vec["e0"] + (1.0 - xf) * vec["s_unit"]


@dataclass(frozen=True)
class TangentRow:
    x: Fraction
    direction: str
    gamma: float
    active_value: float
    margin: float


def tangent_row(
    x: Fraction,
    q: np.ndarray,
    direction_name: str,
    direction: np.ndarray,
    anchor: float,
) -> TangentRow:
    rows = stepfree.tf_rows_pair(stepfree.phi_from_q(q), stepfree.dphi_from_v(direction))
    active = rows[0]
    margin, _ = stepfree.margin_to_next(rows)
    beta = math.copysign(1.0, active.value) * active.derivative
    return TangentRow(x, direction_name, beta / anchor, active.value, margin)


def average_mode_weights(
    left: list[list[list[mp.mpf]]],
    right: list[list[list[mp.mpf]]],
) -> list[list[list[mp.mpf]]]:
    return [
        [
            [(left[i][j][k] + right[i][j][k]) / 2 for k in range(exactsum.N)]
            for j in range(exactsum.N)
        ]
        for i in range(exactsum.N)
    ]


def add_midpoint(evaluator: exactsum.ExactActiveBranchEvaluator) -> None:
    evaluator.mode_weights["a1_mid"] = average_mode_weights(
        evaluator.mode_weights["e0"], evaluator.mode_weights["s_unit"]
    )


def total_shell_coefficients() -> dict[tuple[int, int, int], Fraction]:
    """Linear functional for total charge of H P_{r>4} phi."""
    coeffs: dict[tuple[int, int, int], Fraction] = {}
    for i in range(1, 14):
        for j in range(1, 14):
            for k in range(1, 14):
                for site, value in exactsum.sigma_coeff((i, j, k)).items():
                    coeffs[site] = coeffs.get(site, Fraction(0)) + value
    return {site: value for site, value in coeffs.items() if value}


def exact_rows(
    evaluator: exactsum.ExactActiveBranchEvaluator,
) -> dict[tuple[str, str], exactsum.BranchRow]:
    rows = (
        evaluator.active_row("shell", "s_unit", "E_x", "ex"),
        evaluator.active_row("shell", "s_unit", "T1x", "t1x"),
        evaluator.active_row("midpoint", "a1_mid", "E_x", "ex"),
        evaluator.active_row("midpoint", "a1_mid", "T1x", "t1x"),
        evaluator.active_row("center", "e0", "E_x", "ex"),
        evaluator.active_row("center", "e0", "T1x", "t1x"),
    )
    return {(row.label, row.direction): row for row in rows}


def interpolate_center_spike_samples(dphi: np.ndarray, order: int) -> float:
    maximum = 0.0
    for xyz in exactsum.interpolation_points(exactsum.PROBE0):
        coords = np.array(
            [[7.0 + float(xyz[0])], [7.0 + float(xyz[1])], [7.0 + float(xyz[2])]],
            dtype=float,
        )
        value = float(
            map_coordinates(
                dphi, coords, order=order, mode="nearest", prefilter=True
            )[0]
        )
        maximum = max(maximum, abs(value))
    return maximum


def main() -> int:
    print("Finite cubic-star tensor response: source-step-free certificate")
    print("=" * 78)
    print("Claim surface: SIZE=15, interior=13^3, R=4, h=1/25,")
    print('cubic map_coordinates(order=3, mode="nearest", prefilter=True),')
    print("three fixed probes; Route 2 is the legacy program label.")
    print(
        f"versions: numpy={np.__version__}, scipy={scipy.__version__}, "
        f"mpmath={mp.__version__}"
    )

    scripts_dir = Path(__file__).resolve().parent
    actual_hashes = {
        name: hashlib.sha256((scripts_dir / name).read_bytes()).hexdigest()
        for name in HELPER_HASHES
    }
    check(
        "the two implementation-helper sources match the reviewed fingerprints",
        actual_hashes == HELPER_HASHES,
        "; ".join(f"{name}={digest}" for name, digest in actual_hashes.items()),
        "REPRODUCIBILITY",
    )

    vec = adapted_vectors()
    e0 = vec["e0"]
    s_unit = vec["s_unit"]
    d_source = e0 - s_unit

    gram_vectors = np.column_stack(
        [e0, math.sqrt(6.0) * s_unit, vec["ex"], vec["eperp"], vec["tx"], vec["ty"], vec["tz"]]
    )
    gram_err = float(np.max(np.abs(gram_vectors.T @ gram_vectors - np.eye(7))))
    check(
        "the declared adapted support basis is orthonormal",
        gram_err < 1.0e-14,
        f"max Gram residual={gram_err:.3e}",
        "EXACT-ALGEBRA",
    )

    dphi = stepfree.phi_from_q(d_source)
    expected = np.zeros_like(dphi)
    expected[7, 7, 7] = 1.0 / 6.0
    green_identity_err = float(np.max(np.abs(dphi - expected)))
    check(
        "the cubic-scalar endpoint difference is a center Kronecker spike",
        green_identity_err < 1.0e-13,
        "G(e0-s_unit)=delta_center/6, " f"max residual={green_identity_err:.3e}",
        "EXACT-ALGEBRA",
    )
    print("  Therefore q_delta=s_unit+6 delta(e0-s_unit) and")
    print("  phi_delta=phi_shell+delta*delta_center, 0 <= delta <= 1/6.")

    rot = rotation_x_quarter_turn()
    bright = np.column_stack([vec["ex"], vec["tx"]])
    dark = np.column_stack([vec["eperp"], vec["ty"], vec["tz"]])
    bright_fixed_err = float(np.max(np.abs(rot @ bright - bright)))
    dark_fixed_rank = int(np.linalg.matrix_rank(dark.T @ rot @ dark - np.eye(3), tol=1.0e-12))
    check(
        "the +x-probe stabilizer fixes exactly the E_x and T1x tangent directions",
        bright_fixed_err < 1.0e-14 and dark_fixed_rank == 3,
        f"bright fixed residual={bright_fixed_err:.3e}; rank(R_x90-I) on dark block={dark_fixed_rank}",
        "EXACT-ALGEBRA",
    )

    eval60 = exactsum.ExactActiveBranchEvaluator(60)
    add_midpoint(eval60)
    eval90 = exactsum.ExactActiveBranchEvaluator(90)
    add_midpoint(eval90)
    anchor_coeffs = exactsum.anchor_coefficients()
    total_coeffs = total_shell_coefficients()
    anchor_shell = eval90.lattice_functional("s_unit", anchor_coeffs)
    anchor_mid = eval90.lattice_functional("a1_mid", anchor_coeffs)
    anchor_center = eval90.lattice_functional("e0", anchor_coeffs)
    total_shell = eval90.lattice_functional("s_unit", total_coeffs)
    total_mid = eval90.lattice_functional("a1_mid", total_coeffs)
    total_center = eval90.lattice_functional("e0", total_coeffs)
    anchor_drift = max(abs(anchor_shell - anchor_mid), abs(anchor_shell - anchor_center))
    total_drift = max(abs(total_shell - 1), abs(total_mid - 1), abs(total_center - 1))
    check(
        "the reduced R=4 shell normalization is computed, nonzero, and constant on the cubic-scalar segment",
        anchor_drift < mp.mpf("1e-55") and total_drift < mp.mpf("1e-55") and anchor_shell > 0,
        "A=" + mp.nstr(anchor_shell, 36) + "; max anchor drift=" + mp.nstr(anchor_drift, 8)
        + "; max total-shell-Q drift=" + mp.nstr(total_drift, 8),
        "FINITE-COMPUTE",
    )

    anchor_float = float(anchor_shell)
    bright_rows: dict[tuple[Fraction, str], TangentRow] = {}
    min_margin = float("inf")
    active_ok = True
    for x in GRID_X:
        q = canonical_q(x, vec)
        for name, direction in (("E_x", vec["ex"]), ("T1x", vec["tx"])):
            row = tangent_row(x, q, name, direction, anchor_float)
            bright_rows[(x, name)] = row
            min_margin = min(min_margin, row.margin)
            active_ok = active_ok and row.active_value < 0.0
            rows = stepfree.tf_rows_pair(stepfree.phi_from_q(q), stepfree.dphi_from_v(direction))
            active_ok = active_ok and rows[0].entry_id == ACTIVE_ID
    check(
        "probe0:xx is the unique negative active branch on the declared 11-point cubic-scalar grid",
        active_ok and min_margin > 1.0e-5,
        f"minimum max-branch gap={min_margin:.12e}",
        "FINITE-COMPUTE",
    )

    max_dark = 0.0
    for x in (Fraction(0), Fraction(1, 2), Fraction(1)):
        q = canonical_q(x, vec)
        for name in ("eperp", "ty", "tz"):
            row = tangent_row(x, q, name, vec[name], anchor_float)
            max_dark = max(max_dark, abs(row.gamma))
    min_bright = min(abs(row.gamma) for row in bright_rows.values())
    check(
        "stabilizer-dark tangent responses vanish while both bright responses are nonzero",
        max_dark < 1.0e-14 and min_bright > 1.0e-5,
        f"max |dark gamma|={max_dark:.3e}; min |bright gamma|={min_bright:.3e}",
        "FINITE-COMPUTE",
    )

    exact60 = exact_rows(eval60)
    exact90 = exact_rows(eval90)
    labels = (("shell", "E_x"), ("shell", "T1x"), ("midpoint", "E_x"),
              ("midpoint", "T1x"), ("center", "E_x"), ("center", "T1x"))
    gamma90 = {key: exact90[key].beta / anchor_shell for key in labels}
    precision_drift = max(abs(exact90[key].beta - exact60[key].beta) for key in labels)
    double_drift = max(
        abs(mp.mpf(repr(bright_rows[(x, direction)].gamma)) - gamma90[(label, direction)])
        for x, label in ((Fraction(0), "shell"), (Fraction(1, 2), "midpoint"), (Fraction(1), "center"))
        for direction in ("E_x", "T1x")
    )
    check(
        "60-dps and 90-dps finite-operator endpoint/midpoint replays agree",
        precision_drift < mp.mpf("1e-50") and double_drift < mp.mpf("2e-12"),
        "precision drift=" + mp.nstr(precision_drift, 8) + "; sparse-double drift=" + mp.nstr(double_drift, 8),
        "FINITE-COMPUTE",
    )

    print("\nSource-step-free normalized endpoint values (12 displayed decimals)")
    print(f"  Theta_R^(0)(e0)        = ({float(gamma90[('center', 'E_x')]):+.12e}, "
          f"{float(gamma90[('center', 'T1x')]):+.12e})")
    print(f"  Theta_R^(0)(s_unit)    = ({float(gamma90[('shell', 'E_x')]):+.12e}, "
          f"{float(gamma90[('shell', 'T1x')]):+.12e})")
    print(f"  Theta_R^(0)(midpoint)  = ({float(gamma90[('midpoint', 'E_x')]):+.12e}, "
          f"{float(gamma90[('midpoint', 'T1x')]):+.12e})")

    defect_e = gamma90[("midpoint", "E_x")] - (
        gamma90[("shell", "E_x")] + gamma90[("center", "E_x")]
    ) / 2
    defect_t = gamma90[("midpoint", "T1x")] - (
        gamma90[("shell", "T1x")] + gamma90[("center", "T1x")]
    ) / 2
    check(
        "the declared numerical replay is inconsistent with affinity at the stated tolerance",
        defect_e > mp.mpf("4e-9") and defect_t > mp.mpf("1e-8"),
        "midpoint defects: R_E=" + mp.nstr(defect_e, 30) + ", R_T=" + mp.nstr(defect_t, 30),
        "BOUNDED-OBSTRUCTION",
    )

    max_grid_residual = {"E_x": 0.0, "T1x": 0.0}
    for direction in ("E_x", "T1x"):
        shell = bright_rows[(Fraction(0), direction)].gamma
        center = bright_rows[(Fraction(1), direction)].gamma
        for x in GRID_X:
            prediction = shell + float(x) * (center - shell)
            max_grid_residual[direction] = max(
                max_grid_residual[direction], abs(bright_rows[(x, direction)].gamma - prediction)
            )
    check(
        "the endpoint secant is a bounded approximation on the declared cubic-scalar grid",
        max_grid_residual["E_x"] < 5.0e-9 and max_grid_residual["T1x"] < 1.1e-8,
        f"max residuals: E={max_grid_residual['E_x']:.12e}, T={max_grid_residual['T1x']:.12e}",
        "BOUNDED-COMPUTE",
    )

    linear_tail = interpolate_center_spike_samples(dphi, order=1)
    cubic_tail = interpolate_center_spike_samples(dphi, order=3)
    check(
        "the cubic prefilter supplies the observed scalar-segment variation at the shell stencil in this replay",
        linear_tail < 1.0e-14 and cubic_tail > 1.0e-5,
        f"max interpolated |G(e0-s_unit)|: order1={linear_tail:.3e}, order3={cubic_tail:.3e}",
        "BOUNDED-OBSTRUCTION",
    )

    print("\nClaim firewall")
    print("  - finite fixed-stencil derivative and grid bound: certified")
    print("  - exact affine support identity: numerically disfavored, not exactly certified")
    print("  - interpolation-independent or continuum coefficient: not claimed")
    print("  - physical tensor primitive / GR bridge: not claimed")
    passed = sum(ok for _, ok, _, _ in CHECKS)
    failed = len(CHECKS) - passed
    print("=" * 78)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
