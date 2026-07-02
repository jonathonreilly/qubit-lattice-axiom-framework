#!/usr/bin/env python3
"""Complex action: local kernel damping vs detector-escape threshold.

The complex action S = L(1-f) + i*gamma*L*f has TWO distinct effects:

  1. LOCAL KERNEL DAMPING: every traversed link with averaged field f_ij > 0
     and gamma > 0 has modulus multiplier exp(-k*gamma*L*f_ij) < 1.  This
     is a per-link statement, not a theorem that the detector escape ratio is
     below one for every positive gamma.

  2. DETECTOR OBSERVABLES: on the archived finite setup, the total detector
     escape ratio is below one for the tested nonzero fields at gamma=0.5, but
     remains above one for several nonzero fields at gamma=0.1 and gamma=0.2.

  3. GRAVITY-SPECIFIC CENTROID CROSSOVER: the tested 1/r field changes the
     centroid sign from TOWARD at gamma=0 to AWAY by gamma=0.2; the uniform
     controls do not show that TOWARD -> AWAY crossover.

This runner is a boundary repair for the archived failed row.  It verifies the
separation above and explicitly guards against the historical overclaim that
local damping alone implies detector escape < 1 for every gamma > 0.
"""

from __future__ import annotations

# Heavy compute runner. The current cache completes in about 127 seconds on
# this machine, just above the default 120 second audit timeout.
AUDIT_TIMEOUT_SEC = 600

import math
import random
from pathlib import Path

BETA = 0.8
K = 5.0
MAX_D_PHYS = 3
H = 0.5
NL = 30
PW = 8
MASS_Z = 3.0
DRIFT = 0.2
RESTORE = 0.7
SEEDS = [0, 1]
GAMMAS = [0.0, 0.1, 0.2, 0.5]
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "archive_unlanded"
    / "kernel-gravity-conflation-2026-04-30"
    / "KERNEL_VS_GRAVITY_NOTE.md"
)


def grow(seed):
    rng = random.Random(seed)
    hw = int(PW / H)
    md = max(1, round(MAX_D_PHYS / H))
    pos = []
    adj = {}
    nmap = {}
    pos.append((0.0, 0.0, 0.0))
    nmap[(0, 0, 0)] = 0
    for layer in range(1, NL):
        x = layer * H
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y, z = iy * H, iz * H
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, DRIFT * H)
                    z = pz + rng.gauss(0, DRIFT * H)
                    y = y * (1 - RESTORE) + (iy * H) * RESTORE
                    z = z * (1 - RESTORE) + (iz * H) * RESTORE
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


def make_gravity_field(pos, nmap, s, z_src):
    n = len(pos)
    gl = NL // 3
    iz_s = round(z_src / H)
    mi = nmap.get((gl, 0, iz_s))
    if mi is None:
        return [0.0] * n
    mx, my, mz = pos[mi]
    return [s / (math.sqrt((pos[i][0] - mx) ** 2 + (pos[i][1] - my) ** 2 +
                            (pos[i][2] - mz) ** 2) + 0.1)
            for i in range(n)]


def make_uniform_field(pos, f_val):
    return [f_val] * len(pos)


def prop_cx(pos, adj, field, k, gamma):
    n = len(pos)
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    h2 = H * H
    for i in order:
        if abs(amps[i]) < 1e-30:
            continue
        for j in adj.get(i, []):
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            s_real = L * (1.0 - lf)
            s_imag = gamma * L * lf
            phase = k * s_real
            decay = -k * s_imag
            if decay < -50:
                amp_f = 0.0
            elif decay > 50:
                amp_f = math.exp(50)
            else:
                amp_f = math.exp(decay)
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            amps[j] += amps[i] * complex(math.cos(phase), math.sin(phase)) * amp_f * w * h2 / (L * L)
    return amps


def main():
    pass_count = 0
    fail_count = 0

    def check(name, ok, detail=""):
        nonlocal pass_count, fail_count
        if ok:
            pass_count += 1
            tag = "PASS"
        else:
            fail_count += 1
            tag = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{tag}: {name}{suffix}")

    hw = int(PW / H)
    npl = (2 * hw + 1) ** 2

    def cz(amps, pos):
        ds = len(pos) - npl
        t = sum(abs(amps[i]) ** 2 for i in range(ds, len(amps)))
        if t <= 0:
            return 0.0
        return sum(abs(amps[i]) ** 2 * pos[i][2] for i in range(ds, len(amps))) / t

    def dp(amps, pos):
        ds = len(pos) - npl
        return sum(abs(amps[i]) ** 2 for i in range(ds, len(amps)))

    print("=" * 75)
    print("COMPLEX ACTION: LOCAL KERNEL DAMPING vs DETECTOR ESCAPE")
    print(f"drift={DRIFT}, restore={RESTORE}")
    print("=" * 75)

    field_configs = [
        ("ZERO", lambda pos, nmap: [0.0] * len(pos)),
        ("UNIFORM (f=0.005)", lambda pos, nmap: make_uniform_field(pos, 0.005)),
        ("UNIFORM (f=0.01)", lambda pos, nmap: make_uniform_field(pos, 0.01)),
        ("GRAVITY (s=0.004)", lambda pos, nmap: make_gravity_field(pos, nmap, 0.004, MASS_Z)),
    ]

    seed_packets = []
    for seed in SEEDS:
        pos, adj, nmap = grow(seed)
        free_ref = prop_cx(pos, adj, [0.0] * len(pos), K, 0.0)
        seed_packets.append(
            {
                "seed": seed,
                "pos": pos,
                "adj": adj,
                "nmap": nmap,
                "z_free": cz(free_ref, pos),
                "p_free": dp(free_ref, pos),
            }
        )

    results = {}

    for label, field_fn in field_configs:
        print(f"\nFIELD: {label}")
        print(f"  {'gamma':>6s} {'toward':>6s}/{len(SEEDS)} {'avg_defl':>12s} {'avg_esc':>10s}")
        print("  " + "-" * 42)

        for gamma in GAMMAS:
            towrd = 0
            defls = []
            escs = []
            for packet in seed_packets:
                pos = packet["pos"]
                adj = packet["adj"]
                nmap = packet["nmap"]
                field = field_fn(pos, nmap)

                amps = prop_cx(pos, adj, field, K, gamma)
                delta = cz(amps, pos) - packet["z_free"]
                esc = dp(amps, pos) / packet["p_free"] if packet["p_free"] > 0 else 0
                if delta > 0:
                    towrd += 1
                defls.append(delta)
                escs.append(esc)

            avg_d = sum(defls) / len(defls)
            avg_e = sum(escs) / len(escs)
            results[(label, gamma)] = {
                "toward": towrd,
                "avg_defl": avg_d,
                "avg_esc": avg_e,
                "defls": defls,
                "escs": escs,
            }
            dr = "T" if avg_d > 0 else "A"
            print(f"  {gamma:6.1f} {towrd:6d}/{len(SEEDS)} {avg_d:+12.4e}{dr} {avg_e:10.4f}")

    print()
    print("SEPARATION OF EFFECTS")
    print()
    print("  LOCAL KERNEL DAMPING:")
    print("    exp(-k*gamma*L*f_ij) < 1 for each link with f_ij > 0 and gamma > 0")
    print("    this is local link attenuation, not a detector-escape theorem")
    print()
    print("  DETECTOR ESCAPE (tested finite setup):")
    print("    gamma=0.5 suppresses total detector escape for the tested nonzero fields")
    print("    gamma=0.1 and gamma=0.2 do not uniformly suppress total detector escape")
    print()
    print("  GRAVITY-SPECIFIC (deflection TOWARD -> AWAY):")
    print("    tested 1/r field flips TOWARD at gamma=0 to AWAY by gamma=0.2")
    print("    uniform controls do not show that crossover")
    print("    mechanism: 1/r gradient couples to beam centroid")

    print()
    print("BOUNDARY CHECKS")
    sample_factor = math.exp(-K * 0.1 * 1.0 * 0.005)
    check(
        "local attenuation factor is below one for f>0 and gamma>0",
        0.0 < sample_factor < 1.0,
        f"exp(-5*0.1*1*0.005)={sample_factor:.12f}",
    )

    zero_ok = all(
        abs(results[("ZERO", gamma)]["avg_esc"] - 1.0) < 1e-12
        and abs(results[("ZERO", gamma)]["avg_defl"]) < 1e-12
        for gamma in GAMMAS
    )
    check("zero field leaves detector escape and centroid unchanged", zero_ok)

    nonzero_labels = ["UNIFORM (f=0.005)", "UNIFORM (f=0.01)", "GRAVITY (s=0.004)"]
    gamma_half_ok = all(results[(label, 0.5)]["avg_esc"] < 1.0 for label in nonzero_labels)
    check(
        "gamma=0.5 suppresses detector escape for all tested nonzero fields",
        gamma_half_ok,
        ", ".join(f"{label}: {results[(label, 0.5)]['avg_esc']:.4f}" for label in nonzero_labels),
    )

    small_gamma_above_one = [
        ("UNIFORM (f=0.005)", 0.1),
        ("UNIFORM (f=0.005)", 0.2),
        ("UNIFORM (f=0.01)", 0.1),
        ("UNIFORM (f=0.01)", 0.2),
        ("GRAVITY (s=0.004)", 0.1),
        ("GRAVITY (s=0.004)", 0.2),
    ]
    small_gamma_guard_ok = all(results[key]["avg_esc"] > 1.0 for key in small_gamma_above_one)
    check(
        "small-gamma detector-escape overclaim is explicitly blocked",
        small_gamma_guard_ok,
        ", ".join(f"{label}@{gamma}: {results[(label, gamma)]['avg_esc']:.4f}" for label, gamma in small_gamma_above_one),
    )

    gravity_crossover_ok = (
        results[("GRAVITY (s=0.004)", 0.0)]["toward"] == len(SEEDS)
        and results[("GRAVITY (s=0.004)", 0.0)]["avg_defl"] > 0.0
        and results[("GRAVITY (s=0.004)", 0.2)]["toward"] == 0
        and results[("GRAVITY (s=0.004)", 0.2)]["avg_defl"] < 0.0
        and results[("GRAVITY (s=0.004)", 0.5)]["toward"] == 0
        and results[("GRAVITY (s=0.004)", 0.5)]["avg_defl"] < 0.0
    )
    check("tested gravity field has TOWARD -> AWAY centroid crossover by gamma=0.2", gravity_crossover_ok)

    uniform_no_crossover_ok = all(
        results[(label, 0.0)]["avg_defl"] < 0.0 and results[(label, 0.2)]["avg_defl"] < 0.0
        for label in ["UNIFORM (f=0.005)", "UNIFORM (f=0.01)"]
    )
    check("uniform controls do not carry the gravity centroid crossover", uniform_no_crossover_ok)

    note = NOTE_PATH.read_text(encoding="utf-8")
    note_ok = (
        "Boundary clarification" in note
        and "local per-link attenuation" in note
        and "does not imply total detector-escape suppression" in note
        and "gamma = 0.5" in note
        and "TOWARD -> AWAY" in note
    )
    check("archived note states the narrowed boundary", note_ok)

    print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    if fail_count:
        print("VERDICT: FAIL")
        return 1
    print("VERDICT: THRESHOLDED DETECTOR-ESCAPE BOUNDARY VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
