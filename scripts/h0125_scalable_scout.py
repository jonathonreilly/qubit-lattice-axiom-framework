#!/usr/bin/env python3
"""Deterministic claim-specific replay for the h=0.125 scalable-scout row."""

from __future__ import annotations

import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lattice_3d_l2_numpy_h0125_only import (  # noqa: E402
    K,
    born_ratio,
    build_dense_family,
    centroid_z,
    free_prefix_to_barrier,
    make_field_layers,
    propagate_field,
    propagate_free_from_barrier,
)


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/H0125_SCALABLE_SCOUT_NOTE.md",
    "scripts/lattice_3d_l2_numpy_h0125_only.py",
    "scripts/numpy_replay_bootstrap.py",
)

PHYS_L = 4
PHYS_W = 3
H = 0.125
Z_MASSES = (1.5, 2.0, 3.0)
STRENGTHS = (1e-7, 2e-7, 5e-7, 1e-6, 2e-6, 5e-6)


def fit_power(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 3:
        return None
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    sxx = sum((x - mx) ** 2 for x in lx)
    if sxx <= 1e-12:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / sxx


def main() -> int:
    lat = build_dense_family(PHYS_L, PHYS_W, H)
    _prefix, barrier_in = free_prefix_to_barrier(lat)
    free_final = propagate_free_from_barrier(
        lat, barrier_in, lat["default_open"]
    )
    z_free, p_free = centroid_z(lat, free_final)
    born = born_ratio(lat, barrier_in)

    max_field = make_field_layers(lat, Z_MASSES[-1], STRENGTHS[-1])
    null_final = propagate_field(lat, max_field, lat["default_open"], 0.0)
    z_null, _ = centroid_z(lat, null_final)
    null_delta = z_null - z_free

    rows: list[tuple[float, int, float | None, float]] = []
    for z_mass in Z_MASSES:
        used_strengths: list[float] = []
        deltas: list[float] = []
        for strength in STRENGTHS:
            field = make_field_layers(lat, z_mass, strength)
            final = propagate_field(lat, field, lat["default_open"], K)
            z_final, _ = centroid_z(lat, final)
            delta = z_final - z_free
            if delta > 0.0:
                used_strengths.append(strength)
                deltas.append(delta)
        alpha = fit_power(used_strengths, deltas)
        rows.append(
            (z_mass, len(used_strengths), alpha, max(deltas, default=float("nan")))
        )

    print("=" * 88)
    print("H=0.125 SCALABLE SCOUT — CLAIM-SPECIFIC FULL-WINDOW REPLAY")
    print(
        f"phys_l={PHYS_L} phys_w={PHYS_W} h={H} nodes={lat['n']} "
        f"layers={lat['nl']} nodes_per_layer={lat['npl']}"
    )
    print(f"Born={born:.3e} k0={null_delta:+.6e} P_free={p_free:.6e}")
    for z_mass, count, alpha, delta_max in rows:
        alpha_text = "n/a" if alpha is None else f"{alpha:.6f}"
        print(
            f"z_mass={z_mass:.1f} count={count} alpha={alpha_text} "
            f"delta_max={delta_max:+.6e}"
        )

    alphas = [alpha for _z, _count, alpha, _delta in rows if alpha is not None]
    passed = (
        born < 1e-10
        and abs(null_delta) < 1e-10
        and len(rows) == 3
        and len(alphas) == 3
        and all(count == len(STRENGTHS) for _z, count, _a, _d in rows)
        and all(0.45 <= alpha <= 0.55 for alpha in alphas)
        and all(delta > 0.0 for _z, _count, _alpha, delta in rows)
    )
    print()
    print(
        f"per_element: computed dense layer-transition amplitudes for "
        f"{lat['edges']} directed edges per propagation"
    )
    print(
        f"per_site: computed all {lat['n']} sites on the "
        f"phys_l={PHYS_L}, phys_w={PHYS_W}, h={H} family"
    )
    print(
        f"per_mode: computed Born, k=0, gravity sign, and six-strength "
        f"F~M fits; alphas={','.join(f'{value:.6f}' for value in alphas)}"
    )
    print(
        f"per_block: computed full-window source blocks z_mass="
        f"{','.join(f'{value:.1f}' for value in Z_MASSES)}"
    )
    print(
        "lattice_wide: checked and not executed — the claim is a single "
        "phys_l=4, phys_w=3 finite family, not a volume/width continuum limit"
    )
    print(f"CERTIFICATE passed={passed} rows={len(rows)}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
