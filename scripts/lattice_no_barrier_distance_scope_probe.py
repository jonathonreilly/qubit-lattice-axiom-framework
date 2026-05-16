#!/usr/bin/env python3
"""Scope-probe for the no-barrier lattice distance-law harness.

This runner sharpens the bounded scope of
`docs/LATTICE_DISTANCE_LAW_NOTE.md` by checking two derivable
companion properties of the same ordered 2D no-barrier harness used
in `scripts/lattice_no_barrier_distance.py`:

1. STRENGTH-SCALING (derivable):
   The per-edge action `Δact = dl - ret` with `dl = L(1+lf)` and
   `ret = √(dl² - L²)` expands non-analytically at `lf = 0+`:
     `Δact(lf) ≈ L · (lf - √(2·lf))`
   so `∂Δact/∂lf ≈ -L/√(2·lf)` diverges and the leading
   centroid-shift response is in `√(strength)`, NOT in `strength` itself.
   We verify this prediction numerically at fixed `b = 13`.

2. N-DEPENDENCE OF THE TAIL EXPONENT (scope-sharpening):
   The fitted far-field exponent `|δ| ~ b^α` on the `b >= 7` window
   is NOT universal across lattice sizes. We compute it on
   `N ∈ {30, 40, 60, 80}` at matched `b`-grids. The N=40 result
   `α ≈ -1.05` cited in the source note holds only on that specific
   harness; the exponent drifts to `≈ -0.8` on larger lattices because
   the lever arm to the detector and the beam spread re-scale with N.

Together these two checks freeze the precise bounded scope of the
source note:
- the strength-scaling is the framework-derivable companion law that
  the harness has to satisfy, and the runner confirms it
- the N-dependence of the b-exponent rules out promotion to a
  universal asymptotic theorem and makes the bounded-on-N=40 scope
  explicit

This runner does NOT change the source note's headline numbers
(those remain pinned to `scripts/lattice_no_barrier_distance.py`).
It only adds the two scope-defining cross-checks the source note's
bounded claim depends on.
"""

from __future__ import annotations

import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.lattice_mirror_distance import compute_field_at_b, generate_lattice_mirror, propagate


K = 5.0
SEED = 42
THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0


def check(name, condition, detail="", bucket="THEOREM"):
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def centroid_y(amps, positions, det_list):
    total = 0.0
    weighted = 0.0
    for d in det_list:
        p = abs(amps[d]) ** 2
        total += p
        weighted += p * positions[d][1]
    return weighted / total if total > 1e-30 else math.nan


def fit_power_law(points):
    usable = [(b, v) for b, v in points if b > 0 and v > 0 and not math.isnan(v)]
    if len(usable) < 3:
        return None
    xs = [math.log(b) for b, _ in usable]
    ys = [math.log(v) for _, v in usable]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    syy = sum((y - my) ** 2 for y in ys)
    if sxx <= 1e-12 or syy <= 1e-12:
        return None
    alpha = sxy / sxx
    coeff = math.exp(my - alpha * mx)
    r2 = (sxy * sxy) / (sxx * syy)
    return coeff, alpha, r2


def harness_run(n_layers, half_width, b_values, strength=0.1, k=K):
    positions, adj, _, node_map = generate_lattice_mirror(n_layers, half_width, SEED)
    layers = sorted({round(p[0]) for p in positions})
    src = [node_map[(layers[0], 0)]]
    det_list = [
        node_map[(layers[-1], y)]
        for y in range(-half_width, half_width + 1)
        if (layers[-1], y) in node_map
    ]
    grav_layer = layers[2 * len(layers) // 3]
    field_zero = [0.0] * len(positions)
    blocked = set()
    rows = []
    for b in b_values:
        if b > half_width:
            continue
        field_m, _ = compute_field_at_b(
            positions, node_map, grav_layer, b, n_mass=1, strength=strength
        )
        am = propagate(positions, adj, field_m, src, k, blocked)
        af = propagate(positions, adj, field_zero, src, k, blocked)
        delta = centroid_y(am, positions, det_list) - centroid_y(af, positions, det_list)
        rows.append((b, delta))
    return rows


def main():
    print("=" * 78)
    print("LATTICE DISTANCE-LAW SCOPE PROBE")
    print("  framework-derivable strength-scaling + N-dependence of tail exponent")
    print("=" * 78)
    print()

    # --- Part 1: strength-scaling at fixed b=13, N=40 ---
    print("Part 1: STRENGTH-SCALING at fixed b=13, N=40, half_width=20")
    print("  predicted: |delta| proportional to sqrt(strength)")
    print("  (from Delta_act ~= -L * sqrt(2 * lf) non-analytic at lf=0)")
    print()
    print(f"  {'strength':>10s}  {'|delta|':>10s}  {'|delta|/sqrt(s)':>16s}")
    print("  " + "-" * 42)
    strengths = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
    points = []
    for s in strengths:
        rows = harness_run(40, 20, [13], strength=s)
        d = abs(rows[0][1])
        ratio = d / math.sqrt(s)
        points.append((s, d))
        print(f"  {s:10.3f}  {d:10.4f}  {ratio:16.4f}")
    print()
    xs = [math.log(s) for s, _ in points]
    ys = [math.log(d) for _, d in points]
    mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    syy = sum((y - my) ** 2 for y in ys)
    alpha_s = sxy / sxx
    r2_s = sxy * sxy / (sxx * syy)
    print(f"  fitted: |delta| ~= {math.exp(my - alpha_s*mx):.4f} * strength^({alpha_s:.3f})")
    print(f"  R^2 = {r2_s:.4f}")
    print(f"  prediction: exponent = 0.500 (sqrt-scaling)")
    print(f"  match: |observed - 0.5| = {abs(alpha_s - 0.5):.3f}")
    check(
        "Strength-scaling exponent matches sqrt(strength) within bounded runner tolerance",
        abs(alpha_s - 0.5) <= 0.075 and r2_s >= 0.99,
        detail=f"observed={alpha_s:.3f}, target=0.500, R^2={r2_s:.4f}, tolerance=0.075",
    )
    print()

    # --- Part 2: N-dependence of tail exponent ---
    print("Part 2: N-DEPENDENCE OF TAIL EXPONENT at fixed strength=0.1")
    print("  source-note harness is N=40; check exponent on N in {30, 40, 60, 80}")
    print("  predicted: exponent is NOT universal across N (rules out asymptotic theorem)")
    print()
    print(f"  {'N':>4s}  {'half_w':>7s}  {'tail (b>=7) coeff':>18s}  {'alpha':>8s}  {'R^2':>6s}")
    print("  " + "-" * 56)
    n_alphas = []
    for n in [30, 40, 60, 80]:
        hw = max(20, n // 3 + 5)
        rows = harness_run(n, hw, [3, 5, 7, 10, 13, 16, 19])
        tail = [(b, abs(d)) for b, d in rows if b >= 7]
        fit = fit_power_law(tail)
        if fit:
            c, a, r2 = fit
            n_alphas.append((n, a))
            print(f"  {n:4d}  {hw:7d}  {c:18.4f}  {a:+8.3f}  {r2:6.4f}")
            if n == 40:
                check(
                    "N=40 row reproduces the source note far-field fit",
                    abs(c - 23.5071) <= 0.01 and abs(a + 1.052) <= 0.005 and r2 >= 0.98,
                    detail=f"coeff={c:.4f}, alpha={a:.3f}, R^2={r2:.4f}",
                    bucket="SUPPORT",
                )
    print()
    if len(n_alphas) >= 2:
        amin = min(a for _, a in n_alphas)
        amax = max(a for _, a in n_alphas)
        print(f"  exponent range across N: [{amin:.3f}, {amax:.3f}]")
        print(f"  range width: {amax - amin:.3f}")
        if amax - amin > 0.1:
            print(f"  verdict: NOT universal across N (range exceeds 0.1)")
            print(f"  bounded scope confirmed: source note's alpha = -1.05 is N=40 specific")
        else:
            print(f"  exponent universal across N within 0.1; bounded scope possibly extendable")
        check(
            "b-tail exponent is N-dependent across the probed ordered-lattice sizes",
            amax - amin > 0.1,
            detail=f"alpha range=[{amin:.3f}, {amax:.3f}], width={amax - amin:.3f}",
        )
    else:
        check(
            "b-tail exponent is N-dependent across the probed ordered-lattice sizes",
            False,
            detail=f"only {len(n_alphas)} fitted N rows were available",
        )

    print()
    print(f"THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
