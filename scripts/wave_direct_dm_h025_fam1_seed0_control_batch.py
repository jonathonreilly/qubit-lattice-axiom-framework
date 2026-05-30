#!/usr/bin/env python3
"""Self-contained audit runner for the Fam1 seed-0 H=0.25 control note.

The generic wave helpers are large enough to be truncated in the restricted
audit packet.  This row-specific runner keeps the load-bearing growth, wave,
`prop_beam`, and `cz` implementations in the primary source so the auditor sees
the complete computation without helper truncation.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 1800

import gc
import math
import random
from statistics import mean

T_PHYS_LAYERS = 15.0
IZ_START_PHYS = 3.0
IZ_END_PHYS = 0.0
PW_PHYS = 6.0
SRC_LAYER_FRAC = 1.0 / 3.0
K_PER_H = 2.5
BETA = 0.8

FAMILY_LABEL = "Fam1"
DRIFT = 0.20
RESTORE = 0.70
SEED = 0
H_VAL = 0.25
STRENGTHS = (0.0, 0.002, 0.004, 0.008)


def grow(seed: int, drift: float, restore: float, nl: int, pw: float, max_d_phys: float, h: float):
    rng = random.Random(seed)
    hw = int(pw / h)
    md = max(1, round(max_d_phys / h))
    pos = [(0.0, 0.0, 0.0)]
    adj: dict[int, list[int]] = {}
    nmap = {(0, 0, 0): 0}
    for layer in range(1, nl):
        x = layer * h
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y, z = iy * h, iz * h
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, drift * h)
                    z = pz + rng.gauss(0, drift * h)
                    y = y * (1 - restore) + (iy * h) * restore
                    z = z * (1 - restore) + (iz * h) * restore
                idx = len(pos)
                pos.append((x, y, z))
                nmap[(layer, iy, iz)] = idx
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                si = nmap.get((layer - 1, iy, iz))
                if si is None:
                    continue
                for dy in range(-md, md + 1):
                    for dz in range(-md, md + 1):
                        di = nmap.get((layer, iy + dy, iz + dz))
                        if di is not None:
                            adj.setdefault(si, []).append(di)
    return pos, adj, nmap


def laplacian_yz(f: list[list[float]], nw: int):
    lap = [[0.0] * nw for _ in range(nw)]
    for iy in range(1, nw - 1):
        for iz in range(1, nw - 1):
            lap[iy][iz] = (
                f[iy - 1][iz] + f[iy + 1][iz] + f[iy][iz - 1] + f[iy][iz + 1]
                - 4.0 * f[iy][iz]
            )
    return lap


def solve_wave(nl: int, pw: float, h: float, strength: float, iz_of_t, src_layer: int):
    hw = int(pw / h)
    nw = 2 * hw + 1
    f_prev = [[0.0] * nw for _ in range(nw)]
    f_curr = [[0.0] * nw for _ in range(nw)]
    history = [
        [[0.0] * nw for _ in range(nw)],
        [[0.0] * nw for _ in range(nw)],
    ]
    h2 = h * h
    for t in range(2, nl):
        if t >= src_layer:
            iz_now = iz_of_t(t)
            sy = nw // 2
            sz = nw // 2 + iz_now
        else:
            sy = sz = -1
        lap = laplacian_yz(f_curr, nw)
        f_next = [[0.0] * nw for _ in range(nw)]
        for iy in range(nw):
            for iz in range(nw):
                src = strength if (iy == sy and iz == sz) else 0.0
                f_next[iy][iz] = 2.0 * f_curr[iy][iz] - f_prev[iy][iz] + h2 * (lap[iy][iz] + src)
        f_prev = f_curr
        f_curr = f_next
        history.append([row[:] for row in f_curr])
    return history


def field_at(history, nl: int, pw: float, h: float, layer: int, iy: int, iz: int) -> float:
    hw = int(pw / h)
    nw = 2 * hw + 1
    sy = iy + nw // 2
    sz = iz + nw // 2
    if 0 <= layer < nl and 0 <= sy < nw and 0 <= sz < nw:
        return history[layer][sy][sz]
    return 0.0


def prop_beam(pos, adj, nmap, history, k_phase: float, nl: int, pw: float, h: float):
    n = len(pos)
    hw = int(pw / h)
    field = [0.0] * n
    if history is not None:
        for layer in range(nl):
            for iy in range(-hw, hw + 1):
                for iz in range(-hw, hw + 1):
                    idx = nmap.get((layer, iy, iz))
                    if idx is not None:
                        field[idx] = field_at(history, nl, pw, h, layer, iy, iz)
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    h2 = h * h
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            length = math.sqrt(dx * dx + dy * dy + dz * dz)
            if length < 1e-10:
                continue
            f = 0.5 * (field[i] + field[j])
            phase = k_phase * length * (1.0 - f)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            weight = math.exp(-BETA * theta * theta)
            amps[j] += amps[i] * complex(math.cos(phase), math.sin(phase)) * weight * h2 / (length * length)
    return amps


def cz(amps, pos, nl: int, pw: float, h: float) -> float:
    hw = int(pw / h)
    npl = (2 * hw + 1) ** 2
    ds = len(pos) - npl
    weights = [abs(amps[i]) ** 2 for i in range(ds, len(pos))]
    zs = [pos[i][2] for i in range(ds, len(pos))]
    total = sum(weights)
    if total <= 0:
        return 0.0
    return sum(w * z for w, z in zip(weights, zs)) / total


def _shared_move_trace(iz_start: int, iz_end: int, move_steps: int):
    if move_steps <= 1:
        return [iz_end]
    return [iz_start + int(round((iz_end - iz_start) * (u / (move_steps - 1)))) for u in range(move_steps)]


def make_early_move(iz_start: int, iz_end: int, src_layer: int, nl: int):
    active = nl - src_layer
    move_steps = max(2, active // 2)
    trace = _shared_move_trace(iz_start, iz_end, move_steps)
    hold_steps = active - move_steps

    def iz_of_t(t: int) -> int:
        if t < src_layer:
            return iz_start
        u = t - src_layer
        if u < move_steps:
            return trace[u]
        if hold_steps > 0:
            return iz_end
        return trace[-1]

    return iz_of_t


def make_late_move(iz_start: int, iz_end: int, src_layer: int, nl: int):
    active = nl - src_layer
    move_steps = max(2, active // 2)
    wait_steps = active - move_steps
    trace = _shared_move_trace(iz_start, iz_end, move_steps)

    def iz_of_t(t: int) -> int:
        if t < src_layer:
            return iz_start
        u = t - src_layer
        if u < wait_steps:
            return iz_start
        v = u - wait_steps
        if v < move_steps:
            return trace[v]
        return trace[-1]

    return iz_of_t


def measure_dm(h_val: float, strength: float):
    nl = round(T_PHYS_LAYERS / h_val)
    pw = round(PW_PHYS / h_val) * h_val
    k_phase = K_PER_H / h_val
    src_layer = round(SRC_LAYER_FRAC * nl)
    iz_start = round(IZ_START_PHYS / h_val)
    iz_end = round(IZ_END_PHYS / h_val)

    pos, adj, nmap = grow(SEED, DRIFT, RESTORE, nl, pw, 3, h_val)
    free = prop_beam(pos, adj, nmap, None, k_phase, nl, pw, h_val)
    z_free = cz(free, pos, nl, pw, h_val)

    early = make_early_move(iz_start, iz_end, src_layer, nl)
    late = make_late_move(iz_start, iz_end, src_layer, nl)
    h_early = solve_wave(nl, pw, h_val, strength, early, src_layer)
    h_late = solve_wave(nl, pw, h_val, strength, late, src_layer)

    d_early = cz(prop_beam(pos, adj, nmap, h_early, k_phase, nl, pw, h_val), pos, nl, pw, h_val) - z_free
    d_late = cz(prop_beam(pos, adj, nmap, h_late, k_phase, nl, pw, h_val), pos, nl, pw, h_val) - z_free
    delta_hist = d_early - d_late
    r_hist = delta_hist / max(abs(d_early), abs(d_late), 1e-12)
    return {
        "NL": nl,
        "PW": pw,
        "src_layer": src_layer,
        "iz_start_real": iz_start * h_val,
        "iz_end_real": iz_end * h_val,
        "strength": strength,
        "d_early": d_early,
        "d_late": d_late,
        "delta_hist": delta_hist,
        "r_hist": r_hist,
    }


def main() -> int:
    rows = []
    print("=" * 108)
    print("WAVE DIRECT-DM H=0.25 CONTROL BATCH")
    print("=" * 108)
    print(f"family={FAMILY_LABEL} drift={DRIFT:.2f} restore={RESTORE:.2f} seed={SEED} H={H_VAL:.3f}")
    print("Exact null plus weak-field ladder on one predeclared fine-H pair")
    print()

    for strength in STRENGTHS:
        r = measure_dm(H_VAL, strength)
        rows.append(r)
        print(f"[strength={strength:.6f}]")
        print(f"  NL={r['NL']}  PW={r['PW']:.3f}  src_layer={r['src_layer']}")
        print(f"  start_z_real={r['iz_start_real']:.3f}  end_z_real={r['iz_end_real']:.3f}")
        print(f"  dM(early)    = {r['d_early']:+.6f}")
        print(f"  dM(late)     = {r['d_late']:+.6f}")
        print(f"  delta_hist   = {r['delta_hist']:+.6f}")
        print(f"  R_hist       = {r['r_hist']:+.2%}")
        if abs(strength) <= 1e-12:
            print("  null         = exact S=0 control")
        else:
            print(f"  delta_hist/s = {r['delta_hist'] / strength:+.6f}")
        print()
        gc.collect()

    null_max = max(abs(r["delta_hist"]) for r in rows if abs(r["strength"]) <= 1e-12)
    scaled = [r["delta_hist"] / r["strength"] for r in rows if r["strength"] > 0]
    spread = (max(abs(v) for v in scaled) - min(abs(v) for v in scaled)) / max(mean(abs(v) for v in scaled), 1e-12)

    print("=" * 108)
    print("SUMMARY")
    print("=" * 108)
    print(f"null max |delta_hist| = {null_max:.3e}")
    print(
        "delta_hist sign pattern = "
        f"{' '.join('-' if r['delta_hist'] < 0 else '+' if r['delta_hist'] > 0 else '0' for r in rows if r['strength'] > 0)}"
    )
    print(f"|delta_hist/s| spread   = {spread:+.2%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
