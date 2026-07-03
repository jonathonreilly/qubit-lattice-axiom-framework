#!/usr/bin/env python3
"""H=0.25 edge-kernel certificate for the lensing crossover claim.

This runner addresses the fine-H blocker for
LENSING_EXPONENT_IS_A_DIPOLE_CROSSOVER_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-06-07:
the previous mechanism runner was memory-safe at H=0.6, while the retained
deflection slope to be explained is the H=0.25 b={3,4,5,6} result.

It recomputes the H=0.25 free propagator and detector adjoint, then streams the
edge coefficients c_e without storing the full edge list. The checks certify:

  * exact-edge replay at H=0.25 matches the existing fine-H slope certificate;
  * the fine-H exact-edge slope is the observed -1.43 crossover slope;
  * the signed monopole is cancelled;
  * the large-b signed edge sum is steeper than monopole-like, while the
    non-cancelling |c| control is monopole-like.

This is a bounded edge-kernel certificate for one setup. It is not a continuum
theorem, not a standard 1/b lensing claim, and not a claim about other families.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from kubo_continuum_limit import BETA, K_PER_H, PW_PHYS, SRC_LAYER_FRAC, grow
from lensing_adjoint_kernel_probe import build_free_and_adjoint


AUDIT_TIMEOUT_SEC = 1800

ROOT = Path(__file__).resolve().parents[1]
SOURCE_CERT = ROOT / "outputs/lensing_deflection_h025_slope_fit_certificate.json"
OUT = ROOT / "outputs/lensing_h025_edge_kernel_certificate_2026_06_08.json"

H = 0.25
T_PHYS = 15.0
SEED = 0
DRIFT = 0.20
RESTORE = 0.70
SMALL_B = [3.0, 4.0, 5.0, 6.0]
LARGE_B = [30.0, 45.0, 60.0, 80.0]


def log_slope(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    lx = [math.log(x) for x in xs]
    ly = [math.log(abs(y)) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    sxx = sum((x - mx) ** 2 for x in lx)
    syy = sum((y - my) ** 2 for y in ly)
    sxy = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    slope = sxy / sxx
    intercept = my - slope * mx
    r2 = (sxy * sxy) / (sxx * syy) if syy > 0.0 else 1.0
    return slope, intercept, r2


def check(results: list[dict], name: str, ok: bool, detail: str) -> None:
    results.append({"name": name, "passed": bool(ok), "detail": detail})
    print(("PASS" if ok else "FAIL") + f" {name}: {detail}")


def stream_edge_certificate() -> dict:
    nl = max(3, round(T_PHYS / H))
    k_phase = K_PER_H / H
    x_src = round(nl * SRC_LAYER_FRAC) * H

    pos, adj, _ = grow(SEED, DRIFT, RESTORE, nl, PW_PHYS, 3, H)
    amps, lam, cz_free, free_prob, _ = build_free_and_adjoint(
        pos, adj, nl, PW_PHYS, H, k_phase, BETA
    )

    all_b = SMALL_B + LARGE_B
    exact = {b: 0.0 for b in all_b}
    abs_control = {b: 0.0 for b in LARGE_B}
    coeff_sum = 0.0
    coeff_abs_sum = 0.0
    support_num = 0.0
    mx_min = float("inf")
    mx_max = float("-inf")
    edge_count = 0
    h2 = H * H

    for i, outs in adj.items():
        ai = amps[i]
        if abs(ai) < 1e-30:
            continue
        xi, yi, zi = pos[i]
        for j in outs:
            xj, yj, zj = pos[j]
            dx = xj - xi
            dy = yj - yi
            dz = zj - zi
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-10:
                continue
            phase = k_phase * length
            phi = complex(math.cos(phase), math.sin(phase))
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            weight = math.exp(-BETA * theta * theta)
            free_edge = phi * weight * h2 / (length * length)
            coeff = 2.0 * (
                lam[j] * ai * free_edge * complex(0.0, -k_phase * length)
            ).real
            mx = 0.5 * (xi + xj)
            mz = 0.5 * (zi + zj)

            edge_count += 1
            coeff_sum += coeff
            coeff_abs = abs(coeff)
            coeff_abs_sum += coeff_abs
            support_num += coeff_abs * abs(mx - x_src)
            mx_min = min(mx_min, mx)
            mx_max = max(mx_max, mx)

            dxs = mx - x_src
            for b in all_b:
                r = math.sqrt(dxs * dxs + (mz - b) ** 2) + 0.1
                exact[b] += coeff / r
                if b in abs_control:
                    abs_control[b] += coeff_abs / r

    small_vals = [exact[b] for b in SMALL_B]
    large_vals = [exact[b] for b in LARGE_B]
    abs_vals = [abs_control[b] for b in LARGE_B]
    small_slope, small_intercept, small_r2 = log_slope(SMALL_B, small_vals)
    large_slope, large_intercept, large_r2 = log_slope(LARGE_B, large_vals)
    abs_slope, abs_intercept, abs_r2 = log_slope(LARGE_B, abs_vals)

    return {
        "setup": {
            "H": H,
            "T_phys": T_PHYS,
            "NL": nl,
            "PW": PW_PHYS,
            "seed": SEED,
            "drift": DRIFT,
            "restore": RESTORE,
            "beta": BETA,
            "k_phase": k_phase,
            "x_src": x_src,
            "cz_free": cz_free,
            "free_detector_probability": free_prob,
            "n_nodes": len(pos),
            "n_edges_streamed": edge_count,
        },
        "monopole_ratio": abs(coeff_sum) / coeff_abs_sum,
        "support": support_num / coeff_abs_sum,
        "path_span": mx_max - mx_min,
        "exact_edge": {str(b): exact[b] for b in all_b},
        "abs_control": {str(b): abs_control[b] for b in LARGE_B},
        "small_fit": {
            "b": SMALL_B,
            "values": small_vals,
            "slope": small_slope,
            "intercept": small_intercept,
            "r_squared": small_r2,
        },
        "large_fit": {
            "b": LARGE_B,
            "values": large_vals,
            "slope": large_slope,
            "intercept": large_intercept,
            "r_squared": large_r2,
        },
        "abs_control_fit": {
            "b": LARGE_B,
            "values": abs_vals,
            "slope": abs_slope,
            "intercept": abs_intercept,
            "r_squared": abs_r2,
        },
    }


def main() -> int:
    print("=" * 78)
    print("LENSING H=0.25 EDGE-KERNEL CERTIFICATE")
    print("Scope: one retained fine-H setup; exact-edge replay and mechanism checks")
    print("=" * 78)

    source = json.loads(SOURCE_CERT.read_text(encoding="utf-8"))
    source_kubo = {
        float(b): v
        for b, v in zip(
            source["fit_inputs"]["b"], source["fit_inputs"]["kubo_true"]
        )
    }
    cert = stream_edge_certificate()

    results: list[dict] = []
    setup = cert["setup"]
    check(results, "H025_setup_NL60", setup["NL"] == 60, f"NL={setup['NL']}")
    check(
        results,
        "H025_streamed_many_edges",
        setup["n_edges_streamed"] > 60_000_000,
        f"n_edges={setup['n_edges_streamed']}",
    )

    for b in SMALL_B:
        got = cert["exact_edge"][str(b)]
        ref = source_kubo[b]
        check(
            results,
            f"exact_edge_matches_fine_slope_certificate_b{b:g}",
            abs(got - ref) < 5.0e-6,
            f"exact={got:+.6f}, source={ref:+.6f}",
        )

    small = cert["small_fit"]
    large = cert["large_fit"]
    absfit = cert["abs_control_fit"]
    check(
        results,
        "small_window_replays_minus_1p43",
        abs(small["slope"] + 1.4335) < 1.0e-3 and small["r_squared"] > 0.998,
        f"slope={small['slope']:+.6f}, R2={small['r_squared']:.6f}",
    )
    check(
        results,
        "monopole_cancels_at_H025",
        cert["monopole_ratio"] < 0.01,
        f"|sum c|/sum|c|={cert['monopole_ratio']:.6f}",
    )
    check(
        results,
        "kernel_support_is_finite_and_near_source",
        3.0 < cert["support"] < 6.0 and cert["support"] < 0.4 * cert["path_span"],
        f"support={cert['support']:.3f}, path_span={cert['path_span']:.3f}",
    )
    check(
        results,
        "large_b_signed_falloff_is_steeper_than_monopole",
        large["slope"] < -1.8,
        f"slope={large['slope']:+.6f}, R2={large['r_squared']:.6f}",
    )
    check(
        results,
        "noncancelling_abs_control_is_monopole_like",
        abs(absfit["slope"] + 1.0) < 0.10,
        f"slope={absfit['slope']:+.6f}, R2={absfit['r_squared']:.6f}",
    )
    check(
        results,
        "small_window_is_crossover_not_asymptote",
        abs(small["slope"]) < abs(large["slope"]),
        f"small={small['slope']:+.6f}, large={large['slope']:+.6f}",
    )

    cert["checks"] = results
    cert["summary"] = {
        "pass": sum(1 for row in results if row["passed"]),
        "fail": sum(1 for row in results if not row["passed"]),
        "verdict": "bounded_h025_edge_kernel_certificate",
        "open_scope": [
            "not a continuum theorem",
            "not a standard 1/b lensing claim",
            "not an exact dipole-asymptotic theorem",
            "not a proof for other families or observables",
        ],
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print()
    print(
        "MECHANISM: "
        f"mono={cert['monopole_ratio']:.6f} "
        f"support={cert['support']:.3f} "
        f"small_slope={small['slope']:+.6f} "
        f"large_slope={large['slope']:+.6f} "
        f"abs_control_slope={absfit['slope']:+.6f}"
    )
    print(f"CERTIFICATE_WRITTEN: {OUT.relative_to(ROOT)}")
    print(f"TOTAL: PASS={cert['summary']['pass']} FAIL={cert['summary']['fail']}")
    return 0 if cert["summary"]["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
