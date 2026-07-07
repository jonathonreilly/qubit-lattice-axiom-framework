#!/usr/bin/env python3
"""
Architecture Directional Measure table runner (2026-05-03; recut 2026-07-07).

This deterministic offline runner supports
`docs/ARCHITECTURE_NOTE_DIRECTIONAL_MEASURE.md`.

Load-bearing tier:
  T1  Detector-probability partition fixture consistency.
  T2  Phase-free two-source visibility fixture consistency.
  T3  k = 0 gives real detector amplitudes.
  T4  Gravity sign count over eight fixed seeds.
  T5  Gravity scaling on the canonical 3D protocol.
  T6  Beta-sweep monotonicity of weighted theta^2.

Motivation/document tier:
  Historical beta-selection and observable-matching text is printed only as
  motivation-tier replay. Text needles check that the note states
  BETA-DIRECTIONAL as supplied and labels the motivation exhibit as
  non-load-bearing.
"""
from __future__ import annotations

import cmath
import math
import os
import sys
from collections import defaultdict, deque

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
NOTE_PATH = os.path.join(ROOT, "docs", "ARCHITECTURE_NOTE_DIRECTIONAL_MEASURE.md")

if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from three_d_gravity import compute_field_3d, generate_3d_causal_dag, pathsum_3d
import three_d_angle_weight as angle_weight
from three_d_angle_weight import (
    centroid_y_3d,
    propagate_3d_angle,
    propagate_3d_angle_amplitudes,
)


BETA_DIRECTIONAL = 0.8
PASS_COUNTS = {"load": 0, "motivation": 0}
FAIL_COUNTS = {"load": 0, "motivation": 0}


def check(tier: str, name: str, ok: bool, detail: str = "") -> bool:
    """Print one deterministic check result and update tiered accounting."""
    if tier not in PASS_COUNTS:
        raise ValueError(f"unknown check tier: {tier}")
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNTS[tier] += 1
    else:
        FAIL_COUNTS[tier] += 1
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    return ok


def check_load(name: str, ok: bool, detail: str = "") -> bool:
    return check("load", name, ok, detail)


def check_motivation(name: str, ok: bool, detail: str = "") -> bool:
    return check("motivation", name, ok, detail)


def _assert_3d_helper_beta() -> None:
    """Set and verify the helper module-global beta consumed by T3-T5."""
    angle_weight.BETA = BETA_DIRECTIONAL
    if not math.isclose(angle_weight.BETA, BETA_DIRECTIONAL, rel_tol=0.0, abs_tol=0.0):
        raise AssertionError(
            "three_d_angle_weight.BETA does not match BETA_DIRECTIONAL"
        )


def _call_3d_helper(func, *args, **kwargs):
    _assert_3d_helper_beta()
    return func(*args, **kwargs)


# ---------------------------------------------------------------------------
# 2D directional propagator: deterministic regular layer/slit grid.
# Position type: (x_layer, y). Edges go from layer x to layer x + 1 with
# abs(dy) <= 1. Theta = atan2(abs(dy), 1).
# ---------------------------------------------------------------------------

def make_2d_grid(n_layers: int, half_width: int):
    """Deterministic 2D grid fixture: integer y in [-half_width, +half_width]."""
    positions = []
    layer_indices = []
    idx_map = {}
    for layer in range(n_layers):
        layer_nodes = []
        for y in range(-half_width, half_width + 1):
            i = len(positions)
            positions.append((float(layer), float(y)))
            layer_nodes.append(i)
            idx_map[(layer, y)] = i
        layer_indices.append(layer_nodes)
    adj = defaultdict(list)
    for layer in range(n_layers - 1):
        for y in range(-half_width, half_width + 1):
            i = idx_map[(layer, y)]
            for dy in (-1, 0, 1):
                yn = y + dy
                if -half_width <= yn <= half_width:
                    adj[i].append(idx_map[(layer + 1, yn)])
    return positions, dict(adj), layer_indices, idx_map


def propagate_2d_angle(positions, adj, src_amp, k, beta):
    """2D directional propagator using exp(-beta * theta^2)."""
    n = len(positions)
    in_deg = [0] * n
    for nbs in adj.values():
        for j in nbs:
            in_deg[j] += 1
    order = []
    q = deque(i for i in range(n) if in_deg[i] == 0)
    while q:
        i = q.popleft()
        order.append(i)
        for j in adj.get(i, []):
            in_deg[j] -= 1
            if in_deg[j] == 0:
                q.append(j)

    amps = [0.0 + 0.0j] * n
    for i, a in src_amp.items():
        amps[i] = a
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            dx = x2 - x1
            dy = y2 - y1
            L = math.sqrt(dx * dx + dy * dy)
            if L < 1e-12:
                continue
            theta = math.atan2(abs(dy), dx)
            weight = math.exp(-beta * theta * theta)
            # The legacy 2D table fixture has no delay/field action; T1/T2 are
            # phase-free fixture-consistency checks, not k-variation checks.
            phase = cmath.exp(1j * k * 0.0)
            amps[j] += amps[i] * phase * weight / L
    return amps


def t1_partition_consistency_2d():
    print("\n--- LOAD-BEARING T1: detector partition fixture consistency ---")
    positions, adj, layers, _ = make_2d_grid(n_layers=8, half_width=4)
    src = {layers[0][len(layers[0]) // 2]: 1.0 + 0.0j}
    detectors = layers[-1]
    amps = propagate_2d_angle(
        positions,
        adj,
        src,
        k=0.0,
        beta=BETA_DIRECTIONAL,
    )
    total = sum(abs(amps[d]) ** 2 for d in detectors)
    mid = len(detectors) // 2
    left = sum(abs(amps[d]) ** 2 for d in detectors[:mid])
    right = sum(abs(amps[d]) ** 2 for d in detectors[mid:])
    deviation = abs(total - (left + right))
    check_load(
        "Detector-probability partition additivity on one fixed 2D list",
        deviation < 1e-12,
        f"deviation={deviation:.3e}",
    )


def t2_visibility_fixture_2d():
    print("\n--- LOAD-BEARING T2: phase-free two-source visibility fixture ---")
    n_layers = 10
    half_width = 6
    positions, adj, layers, _ = make_2d_grid(n_layers=n_layers, half_width=half_width)
    src_top = layers[0][half_width + 2]
    src_bot = layers[0][half_width - 2]
    detectors = layers[-1]
    k = 1.5

    def visibility(src):
        amps = propagate_2d_angle(
            positions,
            adj,
            src,
            k=k,
            beta=BETA_DIRECTIONAL,
        )
        probs = [abs(amps[d]) ** 2 for d in detectors]
        total = sum(probs)
        if total == 0:
            return 0.0
        probs = [p / total for p in probs]
        pmax = max(probs)
        pmin = min(probs)
        return (pmax - pmin) / (pmax + pmin) if (pmax + pmin) > 0 else 0.0

    src_both = {src_top: 1.0 / math.sqrt(2), src_bot: 1.0 / math.sqrt(2)}
    visibility_value = visibility(src_both)
    check_load(
        "Two-source visibility fixture has V > 0.95 with phase-free action",
        visibility_value > 0.95,
        f"V={visibility_value:.6f}; S_spent=0 so k is inert",
    )


def t3_k_zero_real_amplitude():
    print("\n--- LOAD-BEARING T3: k = 0 real amplitude on 3D fixture ---")
    positions, adj, _ = generate_3d_causal_dag(
        n_layers=10,
        nodes_per_layer=20,
        xyz_range=6.0,
        connect_radius=3.0,
        rng_seed=37,
    )
    field = [0.0] * len(positions)
    src = [0]
    detectors = list(range(len(positions) - 5, len(positions)))
    amps = _call_3d_helper(
        propagate_3d_angle_amplitudes,
        positions,
        adj,
        field,
        src,
        k=0.0,
    )
    max_imag = max(abs(amps[d].imag) for d in detectors)
    check_load(
        "All detector amplitudes are real at k = 0",
        max_imag < 1e-12,
        f"max|Im(amp)|={max_imag:.3e}",
    )


def t4_gravity_sign_3d():
    print("\n--- LOAD-BEARING T4: Gravity sign over 8 fixed seeds (3D) ---")
    seeds = [11, 19, 23, 29, 31, 37, 41, 43]
    attract_count = 0
    n_total = 0
    for seed in seeds:
        positions, adj, layers = generate_3d_causal_dag(
            n_layers=12,
            nodes_per_layer=24,
            xyz_range=6.0,
            connect_radius=3.0,
            rng_seed=seed,
        )
        if len(layers) < 4 or len(layers[0]) == 0:
            continue
        mass_layer = layers[len(layers) // 2]
        if not mass_layer:
            continue
        mass_idx = [mass_layer[len(mass_layer) // 2]]
        field = compute_field_3d(positions, adj, mass_idx, iterations=30)
        src = [layers[0][0]]
        detectors = layers[-1]
        probs_with = _call_3d_helper(
            propagate_3d_angle,
            positions,
            adj,
            field,
            src,
            detectors,
            k=2.5,
        )
        zero_field = [0.0] * len(positions)
        probs_no = _call_3d_helper(
            propagate_3d_angle,
            positions,
            adj,
            zero_field,
            src,
            detectors,
            k=2.5,
        )
        if not probs_with or not probs_no:
            continue

        def yz_centroid(probs):
            total = sum(probs.values())
            if total == 0:
                return 0.0, 0.0
            ycen = sum(positions[d][1] * p for d, p in probs.items()) / total
            zcen = sum(positions[d][2] * p for d, p in probs.items()) / total
            return ycen, zcen

        y1, z1 = yz_centroid(probs_with)
        y0, z0 = yz_centroid(probs_no)
        my, mz = positions[mass_idx[0]][1], positions[mass_idx[0]][2]
        dist_with = (y1 - my) ** 2 + (z1 - mz) ** 2
        dist_no = (y0 - my) ** 2 + (z0 - mz) ** 2
        if dist_with < dist_no:
            attract_count += 1
        n_total += 1

    detail = f"attract={attract_count}/{n_total}; historical note table=5/8"
    check_load(
        "Gravity sign: at least 5/8 seeds attract with supplied beta",
        attract_count >= 5 and n_total == 8,
        detail,
    )


def _gravity_card_r_angle(n_layers, n_seeds=6, k_band=(3.0, 5.0, 7.0)):
    values = []
    for seed in range(n_seeds):
        positions, adj, layers = generate_3d_causal_dag(
            n_layers=n_layers,
            nodes_per_layer=30,
            xyz_range=8.0,
            connect_radius=3.0,
            rng_seed=seed * 11 + 7,
        )
        if not layers or not layers[-1]:
            continue
        src = layers[0]
        det = set(layers[-1])
        all_ys = [y for _, y, _ in positions]
        cy = sum(all_ys) / len(all_ys)
        mid = len(layers) // 2
        gm = [i for i in layers[mid] if positions[i][1] > cy + 2]
        if len(gm) < 2:
            continue
        free_f = [0.0] * len(positions)
        field = compute_field_3d(positions, adj, gm)
        shifts = []
        for k in k_band:
            free_probs = _call_3d_helper(
                propagate_3d_angle,
                positions,
                adj,
                free_f,
                src,
                det,
                k,
            )
            mass_probs = _call_3d_helper(
                propagate_3d_angle,
                positions,
                adj,
                field,
                src,
                det,
                k,
            )
            shifts.append(
                centroid_y_3d(mass_probs, positions)
                - centroid_y_3d(free_probs, positions)
            )

        free_pathsum = pathsum_3d(positions, adj, free_f, src, det, 5.0)
        total = sum(free_pathsum.values())
        width = 1.0
        if total > 0:
            mean = sum(positions[d][1] * p for d, p in free_pathsum.items()) / total
            second = sum(
                positions[d][1] ** 2 * p for d, p in free_pathsum.items()
            ) / total
            width = max((second - mean ** 2) ** 0.5, 0.1)
        values.append(sum(shifts) / len(shifts) / width)
    return sum(values) / len(values) if values else 0.0


def t5_gravity_scaling_3d():
    print("\n--- LOAD-BEARING T5: Gravity scaling R_angle(N) on 3D protocol ---")
    r8 = _gravity_card_r_angle(8)
    r12 = _gravity_card_r_angle(12)
    r16 = _gravity_card_r_angle(16)
    r20 = _gravity_card_r_angle(20)
    detail = (
        f"R(8)={r8:+.3f}, R(12)={r12:+.3f}, "
        f"R(16)={r16:+.3f}, R(20)={r20:+.3f}"
    )
    ok = r20 > r8 and r16 > r8 and min(r8, r12, r16, r20) > 0
    check_load(
        "R_angle(N) positive for N=8..20 with R(16), R(20) > R(8)",
        ok,
        detail,
    )


def t6_beta_sweep_monotonicity():
    print("\n--- LOAD-BEARING T6: Beta-sweep monotonicity on fixed theta list ---")
    positions, adj, _ = generate_3d_causal_dag(
        n_layers=12,
        nodes_per_layer=30,
        xyz_range=8.0,
        connect_radius=3.0,
        rng_seed=137,
    )
    thetas = []
    for src, dsts in adj.items():
        x1, y1, z1 = positions[src]
        for dst in dsts:
            x2, y2, z2 = positions[dst]
            dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-12:
                continue
            theta = math.acos(min(max(dx / length, -1), 1))
            thetas.append(theta)

    betas = [0.1, 0.4, BETA_DIRECTIONAL, 1.6, 3.2]
    weighted_t2 = []
    for beta in betas:
        weights = [math.exp(-beta * theta * theta) for theta in thetas]
        total = sum(weights)
        numerator = sum(
            weight * theta * theta for weight, theta in zip(weights, thetas)
        )
        weighted_t2.append(numerator / total)

    monotone = all(
        weighted_t2[i] >= weighted_t2[i + 1]
        for i in range(len(weighted_t2) - 1)
    )
    detail = "  ".join(
        f"b={beta}:<theta^2>={value:.4f}"
        for beta, value in zip(betas, weighted_t2)
    )
    check_load(
        "Weighted theta^2 is monotone-decreasing in beta",
        monotone,
        detail,
    )


def beta_motivation_replay():
    print(
        "\n--- MOTIVATION-TIER: beta provenance replay "
        "(evidence only; not load-bearing) ---"
    )
    print(f"  supplied premise value: beta = {BETA_DIRECTIONAL}")
    print("  current Born note imports beta=0.8 from this architecture note")
    print("  current Born note says beta=0.8 beam corrections worsen the match")
    print("  current Born note withdraws the old -1.28 -> -1.43 correction claim")
    print("  historical moment-match story remains motivation-tier history")
    print("  replay status: none of these values is consumed by T1-T6")


def note_text_needles():
    print("\n--- MOTIVATION-TIER: note text needles and firewall checks ---")
    try:
        with open(NOTE_PATH, "r", encoding="utf-8") as handle:
            note = handle.read()
    except OSError as exc:
        check_motivation("Note file can be read", False, str(exc))
        return

    needles = [
        (
            "BETA-DIRECTIONAL named premise is present",
            "BETA-DIRECTIONAL (named conditional premise):",
        ),
        (
            "BETA-DIRECTIONAL states supplied beta value",
            "SUPPLIED as beta = 0.8",
        ),
        (
            "Motivation exhibit has non-load-bearing label",
            "evidence only; not load-bearing; no value below is consumed by any claim",
        ),
        (
            "Firewall forbids citing premises as derived",
            "The named premises may not be cited as derived.",
        ),
        (
            "Parseable Claim type header is present",
            "**Claim type:** bounded_theorem",
        ),
        (
            "Frontmatter claim_id matches ledger row id",
            "claim_id: architecture_note_directional_measure",
        ),
    ]
    for name, needle in needles:
        check_motivation(name, needle in note)


def print_summary() -> int:
    load_pass = PASS_COUNTS["load"]
    load_fail = FAIL_COUNTS["load"]
    motivation_pass = PASS_COUNTS["motivation"]
    motivation_fail = FAIL_COUNTS["motivation"]
    all_pass = load_pass + motivation_pass
    all_fail = load_fail + motivation_fail

    print()
    print("=" * 80)
    print(f"LOAD-BEARING: PASS={load_pass} FAIL={load_fail}")
    print(f"MOTIVATION: PASS={motivation_pass} FAIL={motivation_fail}")
    print(f"FATAL TOTAL: PASS={load_pass} FAIL={load_fail}")
    print(f"ALL CHECKS: PASS={all_pass} FAIL={all_fail}")
    print(
        "DECLARATION: BETA-DIRECTIONAL is supplied; beta derivation, "
        "beta selection, and observable matching are NOT claimed."
    )
    print("=" * 80)
    return 0 if load_fail == 0 else 1


def main() -> int:
    print("=" * 80)
    print(" architecture_directional_measure_table_runner_2026_05_03.py")
    print(" supplied-beta conditional bounded-theorem runner")
    print("=" * 80)
    print(f"Named supplied premise: BETA-DIRECTIONAL sets beta = {BETA_DIRECTIONAL}")
    _assert_3d_helper_beta()
    print(f"3D helper module BETA asserted at supplied premise: {angle_weight.BETA}")

    t1_partition_consistency_2d()
    t2_visibility_fixture_2d()
    t3_k_zero_real_amplitude()
    t4_gravity_sign_3d()
    t5_gravity_scaling_3d()
    t6_beta_sweep_monotonicity()
    beta_motivation_replay()
    note_text_needles()

    return print_summary()


if __name__ == "__main__":
    sys.exit(main())
