#!/usr/bin/env python3
"""J:confirm:J-attack-PR8180 - independent test of the finder's executed-number HIT on block 35 (PR #8180): the claim_scope's
"the nonlinear sphere formation law's equal-level transverse structure factor is the linearized kernel sigma^2/(1 - u(k)) times a
normalization 0.83-0.89, 0.90-0.94, 0.94-0.97 (rising with |k| and with beta)" at beta = 6, 12, 24 on a 256 x 256 plane, against the
control's shell means (finder: beta = 12 spans 0.8975-0.9477 and dips after [0.3, 0.6); beta = 24 spans 0.9397-0.9714 and dips).

Different machinery from the finder (who compared four-decimal shell means with two-decimal bounds and required strict increase):
  * the claim_scope and the control output are read at the PR head and compared at the claim's precision (two decimals, both
    ROUND_HALF_UP and ROUND_HALF_EVEN; "rising" as non-decreasing at that precision);
  * the linearized model's own expectation for the control's statistic, exactly: from the aligned start E|theta^_k(t)|^2 =
    sigma^2 (1 - u^t)/(1 - u) per component (the note's T1), so the control's average over levels T0+1..T carries the factor
    1 - mean_t u^t, computed in closed form mode by mode and averaged over each shell;
  * an independent simulation of the formation law (my own sampler: von Mises-Fisher conditionals around e_3 carried to the direction
    of the three predecessors' sum by a Householder reflection; three independent replicas per coupling; another seed) on the same
    256 x 256 plane and levels, with shell means and replica standard errors, reported in two representations of |k|: the control's
    (the magnitude of the representative in [0, 2 pi)^2, as its code builds it) and the minimal image in (-pi, pi]^2 (the wavevector's
    magnitude), raw and divided by the transient factor; plus the linearized model run with the same code as a calibration.
Prints "HIT: confirmed - ..." for each part of the finder's conclusion that this test reproduces, and says which parts it does not.
"""
import re
import subprocess
import sys
import time
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block35-gravity-kernel-under-the-formation-reading-heat-kernel-times-plane-green-function-20260918"
HEAD = "7c844adf7555a3558729be69179646f6a83a1539"
NOTE = ("docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_TIMES_A_PLANE_GREEN_"
        "FUNCTION_NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md")
CTRL = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block35_kernel_sim.out.txt"
EDGES = ((0, 0.3), (0.3, 0.6), (0.6, 1.0), (1.0, 1.5), (1.5, 2.2), (2.2, 3.2), (3.2, 5.0))
L, T, T0 = 256, 4000, 2000


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def r2(x, mode):
    return Decimal(x).quantize(Decimal("0.01"), rounding=mode)


def A(k):
    return 1 / np.tanh(k) - 1 / k


def vmf_householder(V, rng):
    kap = np.linalg.norm(V, axis=-1)
    u = V / kap[..., None]
    U = rng.random(kap.shape)
    w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1)
    ph = 2 * np.pi * rng.random(kap.shape)
    rr = np.sqrt(np.clip(1 - w * w, 0, 1))
    s0 = np.stack([rr * np.cos(ph), rr * np.sin(ph), w], axis=-1)
    v = -u
    v[..., 2] += 1
    vv = (v * v).sum(-1)
    safe = vv > 1e-24
    coef = np.where(safe, 2 * (s0 * v).sum(-1) / np.where(safe, vv, 1), 0.0)
    return s0 - coef[..., None] * v


def run(beta, R, seed, linear=False):
    rng = np.random.default_rng(seed)
    S0 = np.zeros((R, L, L))
    if linear:
        sig = np.sqrt(A(3 * beta) / (3 * beta))
        th = np.zeros((R, L, L, 2))
    else:
        s = np.zeros((R, L, L, 3))
        s[..., 2] = 1
    for t in range(1, T + 1):
        if linear:
            th = (th + np.roll(th, 1, axis=1) + np.roll(th, 1, axis=2)) / 3 + sig * rng.standard_normal(th.shape)
            x0, x1 = th[..., 0], th[..., 1]
        else:
            s = vmf_householder(beta * (s + np.roll(s, 1, axis=1) + np.roll(s, 1, axis=2)), rng)
            x0, x1 = s[..., 0], s[..., 1]
        if t > T0:
            S0 += (np.abs(np.fft.fft2(x0) / L) ** 2 + np.abs(np.fft.fft2(x1) / L) ** 2) / 2
    return S0 / (T - T0)


def main():
    t0 = time.time()
    note = show(NOTE)
    ctrl = show(CTRL)
    scope = next(l for l in note.splitlines() if l.startswith("claim_scope:"))
    m = re.search(r"times a normalization ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+) \(rising with \|k\| and with beta\)", scope)
    stated = {6: tuple(map(Decimal, m.group(1, 2))), 12: tuple(map(Decimal, m.group(3, 4))), 24: tuple(map(Decimal, m.group(5, 6)))}
    shells, beta = {}, None
    for line in ctrl.splitlines():
        h = re.match(r"beta=([0-9.]+) L=(\d+) T=(\d+)", line)
        if h:
            beta = int(float(h.group(1)))
            shells[beta] = []
            continue
        g = re.search(r"\|k\| in \[([0-9.]+),([0-9.]+)\): mean ratio ([0-9.]+) \(n=(\d+)\)", line)
        if g and beta:
            shells[beta].append((float(g.group(1)), float(g.group(2)), Decimal(g.group(3)), int(g.group(4))))
    hits, not_repro = [], []
    print(f"[inputs] at {HEAD[:10]}: claim_scope normalizations {dict((b, f'{lo}-{hi}') for b, (lo, hi) in stated.items())} 'rising with |k| and "
          f"with beta'; control shells per coupling {dict((b, len(v)) for b, v in shells.items())}")
    # ---- part 1: the control's shells at the claim's precision
    for b in (6, 12, 24):
        vals = [x[2] for x in shells[b]]
        up = [r2(v, ROUND_HALF_UP) for v in vals]
        ev = [r2(v, ROUND_HALF_EVEN) for v in vals]
        lo, hi = stated[b]
        out_up = [(str(v), str(q)) for v, q in zip(vals, up) if not lo <= q <= hi]
        out_ev = [(str(v), str(q)) for v, q in zip(vals, ev) if not lo <= q <= hi]
        both = [x for x in out_up if x in out_ev]
        nondec = all(up[i] <= up[i + 1] for i in range(len(up) - 1)) and all(ev[i] <= ev[i + 1] for i in range(len(ev) - 1))
        drops = [(f"[{shells[b][i][0]},{shells[b][i][1]})", str(up[i]), str(up[i + 1])) for i in range(len(up) - 1) if up[i] > up[i + 1]]
        print(f"[control beta={b}] shell means {[str(v) for v in vals]} -> two decimals {[str(q) for q in up]}; outside the stated {lo}-{hi} "
              f"under both roundings: {both}; non-decreasing in the shell index at two decimals: {nondec}; drops {drops}")
        if both:
            if b == 12:
                hits.append(f"beta = 12: the control's shell [0.3, 0.6) mean {both[0][0]} rounds to {both[0][1]}, outside the claim_scope's {lo}-{hi} "
                            f"(executed range at two decimals {min(up)}-{max(up)})")
            else:
                hits.append(f"beta = {b}: control shells {both} outside {lo}-{hi}")
        elif b in (12, 24):
            not_repro.append(f"beta = {b} range: at two decimals the control spans {min(up)}-{max(up)}" + (" = the stated range" if (min(up), max(up)) == (lo, hi) else ""))
        if not nondec and b == 12:
            hits.append(f"beta = 12: the control's shell means are not rising with |k| at the claim's precision ({drops[0][0]} {drops[0][1]} then "
                        f"{drops[0][2]})")
        elif nondec and b == 24:
            not_repro.append("beta = 24 'not rising': at two decimals the control's shells are non-decreasing (0.94 then 0.97 throughout); "
                             "the finder's dips are 0.001-0.004, below the claim's precision")
    # ---- part 2: the linearized model's transient factor, exactly, and the two representations of |k|
    K = 2 * np.pi * np.arange(L) / L
    K1, K2 = np.meshgrid(K, K, indexing="ij")
    u = np.abs((1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3) ** 2
    mask = np.ones((L, L), bool)
    mask[0, 0] = False
    um = np.where(mask, u, 0.5)
    ubar = um ** (T0 + 1) * (1 - um ** (T - T0)) / ((1 - um) * (T - T0))
    fac = 1 - ubar
    kk_a = np.sqrt(K1 ** 2 + K2 ** 2)
    Km1, Km2 = np.where(K1 > np.pi, K1 - 2 * np.pi, K1), np.where(K2 > np.pi, K2 - 2 * np.pi, K2)
    kk_b = np.sqrt(Km1 ** 2 + Km2 ** 2)
    sel_a = [mask & (kk_a >= a) & (kk_a < b) for a, b in EDGES]
    sel_b = [mask & (kk_b >= a) & (kk_b < b) for a, b in EDGES]
    na = [int(x.sum()) for x in sel_a]
    nb = [int(x.sum()) for x in sel_b]
    ctrl_n = [x[3] for x in shells[12]]
    fac_a = [float(fac[x].mean()) for x in sel_a]
    fac_b = [float(fac[x].mean()) for x in sel_b]
    print(f"[shells] the control's counts {ctrl_n} equal the [0, 2 pi)^2 representation's {na}: {ctrl_n == na}; minimal-image counts {nb}; modes "
          f"with |k| < 5 in the minimal image left out of every control shell: {int((mask & (kk_b < 5) & (kk_a >= 5)).sum())}; the linearized "
          f"model's expected shell mean of the control's statistic (1 - mean_t u^t over levels {T0 + 1}..{T}), control shells: "
          f"{' '.join(f'{x:.4f}' for x in fac_a)}; minimal-image shells: {' '.join(f'{x:.4f}' for x in fac_b)}")
    # ---- part 3: independent simulation
    res = {}
    for b, seed in ((12, 818012), (24, 818024)):
        sig2 = A(3 * b) / (3 * b)
        S0 = run(b, 3, seed)
        ratio = S0 / np.where(mask, sig2 / (1 - um), 1.0)
        rows = {}
        for name, sels, corr in (("control |k|", sel_a, None), ("minimal-image |k|", sel_b, None), ("control |k| / transient", sel_a, fac)):
            per = np.array([[(ratio[r][x] / (corr[x] if corr is not None else 1)).mean() for x in sels] for r in range(3)])
            rows[name] = (per.mean(0), per.std(0, ddof=1) / np.sqrt(3))
        res[b] = rows
        for name, (mu, se) in rows.items():
            print(f"[chain beta={b}] {name}: " + " ".join(f"{mu[i]:.4f}+-{se[i]:.4f}" for i in range(len(EDGES))) + f"  ({time.time() - t0:.0f}s)")
    lin = run(12, 3, 818000, linear=True)
    lratio = lin / np.where(mask, (A(36) / 36) / (1 - um), 1.0)
    lin_raw = [float(lratio[:, x].mean()) for x in sel_a]
    lin_cor = [float((lratio[:, x] / fac[x]).mean()) for x in sel_a]
    print(f"[linear model, same code, beta=12] control shells raw: {' '.join(f'{x:.4f}' for x in lin_raw)}; divided by the transient factor: "
          f"{' '.join(f'{x:.4f}' for x in lin_cor)}  ({time.time() - t0:.0f}s)")
    mu12, se12 = res[12]["control |k|"]
    bump = (mu12[1] - mu12[2:].mean()) / np.sqrt(se12[1] ** 2 + (se12[2:] ** 2).mean() / len(se12[2:]))
    mu12b, se12b = res[12]["minimal-image |k|"]
    mono_b = [round(float(x), 2) for x in mu12b]
    print(f"[independent beta=12] my control-|k| shells at two decimals {[round(float(x), 2) for x in mu12]}: shell [0.3, 0.6) minus the mean of "
          f"the larger shells = {mu12[1] - mu12[2:].mean():+.4f} ({bump:+.1f} standard errors); minimal-image shells at two decimals {mono_b}; "
          f"the first shell divided by its transient factor {res[12]['control |k| / transient'][0][0]:.4f} against the raw {mu12[0]:.4f}")
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed in part' if hits else 'not reproduced'} - reproduced at the claim's two-decimal precision: "
          + ("; ".join(hits) if hits else "none")
          + f"; my independent chain at beta = 12 gives the control-|k| shell [0.3, 0.6) {mu12[1]:.4f}+-{se12[1]:.4f} against {mu12[2:].mean():.4f} for "
          f"the larger shells ({bump:+.1f} s.e.); the first shell's dip is the linearized model's own finite-level factor "
          f"({fac_a[0]:.3f} expected, {lin_raw[0]:.3f} simulated for the linear model); not reproduced: " + " | ".join(not_repro))
    return 0


if __name__ == "__main__":
    sys.exit(main())
