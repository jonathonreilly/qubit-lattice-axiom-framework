#!/usr/bin/env python3
"""J:confirm:J-attack-PR8178 - independent test of the finder's executed-number HIT on block 34 (PR #8178): "(12, 32) stated 1.18 vs
lag-25 1.165; linear 0.960..1.014 vs 0.97-1.01".

Different machinery from the finder (who parsed the control output and compared 3-decimal values with the claim_scope's 2-decimal
numbers at lag 25 only):
  * the claim_scope's numbers, the note's own table (lags 25, 100, 1000) and the body's calibration sentence are parsed from the note
    itself, and the control output (every lag) from the PR branch, all at the PR head;
  * every comparison is made at the claim's own precision (two decimals, both ROUND_HALF_UP and ROUND_HALF_EVEN of the printed
    three-decimal values), and each D_1 number is tested under the note's own definition ("D_1 := E|m_{t+l} - m_t|^2/(2l) at lags l
    short against tau_L", no lag named in the claim_scope): which executed lags reproduce it, and whether it lies inside the executed
    short-lag range;
  * the calibration statement is tested against the exact sampling law of the estimator on the linear model: the plane average of the
    linear field is exactly a two-component Gaussian random walk with per-level variance sigma^2/L^2 (the torus mean of the transfer
    step is the identity), so the control's ratio estimator R = MSD(l)/(2 l sigma^2/L^2) has mean 1 and, for n overlapping windows of
    l samples per seed, Var R = sum_{|d| < l} (n - |d|)(l - |d|)^2 / (n^2 l^2) per seed (exact rational, from the control's T, every,
    transient rule and seed count); checked by a direct Monte Carlo of the zero-mode walk.
Prints "HIT: confirmed - ..." for each part of the finder's conclusion that this test reproduces, and says which parts it does not.
"""
import re
import subprocess
import sys
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block34-sphere-formation-law-torus-memory-time-zero-mode-rate-and-stationary-modes-20260917"
HEAD = "e6ffae5b460b9ec0fd0d99c99f9784232bd225bd"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_"
        "NONLINEAR_LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def r2(x, mode):
    return Decimal(x).quantize(Decimal("0.01"), rounding=mode)


def exact_var(n, l):
    return sum(Fraction((n - abs(d)) * (l - abs(d)) ** 2) for d in range(-(l - 1), l)) / (n * n * l * l)


def main():
    note = show(NOTE)
    ctrl = show(SPECS + "supervisor_control_block34_torus_msd.out.txt")
    ctrl_py = show(SPECS + "supervisor_control_block34_torus_msd.py")
    # ---- the note: claim_scope numbers, table, calibration sentence
    scope = next(l for l in note.splitlines() if l.startswith("claim_scope:"))
    m = re.search(r"times ([0-9.]+), ([0-9.]+), ([0-9.]+), ([0-9.]+) at beta = 6, 12, 24, 48 \(L = 16; ([0-9.]+) and ([0-9.]+) at L = 32 "
                  r"for beta = 6, 12\)", scope)
    stated = dict(zip([(6, 16), (12, 16), (24, 16), (48, 16), (6, 32), (12, 32)], map(Decimal, m.groups())))
    lin_lo, lin_hi = map(Decimal, re.search(r"linear model returning ([0-9.]+)-([0-9.]+) under the same estimator", scope).groups())
    table = {}
    for line in note.splitlines():
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) == 8 and cells[0].isdigit() and cells[1].isdigit():
            table[(int(cells[0]), int(cells[1]))] = ([Decimal(x) for x in cells[5].split(", ")], [Decimal(x) for x in cells[6].split(", ")])
    three_pct = "within three percent at every coupling and lag" in note
    # ---- the control: parameters and every lag
    every = int(re.search(r"every = (\d+)", ctrl_py).group(1))
    assert "skip = max(5, (T // every) // 5)" in ctrl_py and "lags = [1, 2, 4, 8, 16, 40]" in ctrl_py
    runs, key = {}, None
    for line in ctrl.splitlines():
        h = re.match(r"beta=([0-9.]+) L=(\d+) T=(\d+) seeds=(\d+)", line)
        if h:
            key = (int(Decimal(h.group(1))), int(h.group(2)))
            runs[key] = {"T": int(h.group(3)), "seeds": int(h.group(4)), "lags": {}}
            continue
        g = re.search(r"lag +(\d+): nonlinear MSD \S+ -> D_1 = \S+ \(ratio to sigma\^2/L\^2: ([0-9.]+) \+- ([0-9.]+)\); linear model MSD \S+ "
                      r"\(ratio ([0-9.]+) \+- ([0-9.]+)\)", line)
        if g and key:
            runs[key]["lags"][int(g.group(1))] = tuple(Decimal(g.group(i)) for i in range(2, 6))
    print(f"[inputs] note and control at {HEAD[:10]}: claim_scope D_1 {dict((k, str(v)) for k, v in stated.items())}, linear range "
          f"{lin_lo}-{lin_hi}; table rows {sorted(table)}; body sentence 'within three percent at every coupling and lag': {three_pct}; "
          f"control runs {sorted(runs)} with lags {sorted(next(iter(runs.values()))['lags'])}, every = {every}")
    hits, not_repro = [], []
    # ---- part 1: the D_1 numbers under the note's definition
    for k, s in stated.items():
        lags = runs[k]["lags"]
        match_up = [lag for lag, v in lags.items() if r2(v[0], ROUND_HALF_UP) == s]
        match_even = [lag for lag, v in lags.items() if r2(v[0], ROUND_HALF_EVEN) == s]
        vals = [v[0] for v in lags.values()]
        mean3 = sum(lags[l][0] for l in (25, 50, 100)) / 3
        inside = min(vals) <= s <= max(vals)
        tab = table[k][0][0]
        print(f"[D_1 {k}] stated {s}; executed ratios by lag {', '.join(f'{lag}: {v[0]}+-{v[1]}' for lag, v in sorted(lags.items()))}; lags "
              f"rounding to the stated value: half-up {match_up}, half-even {match_even}; inside the executed range [{min(vals)}, {max(vals)}]: "
              f"{inside}; mean of lags 25/50/100 = {mean3:.4f} (-> {r2(mean3, ROUND_HALF_UP)}); the note's table at lag 25: {tab}")
        if k == (12, 32):
            d12 = (s, lags[25][0], tab, match_up, inside, mean3)
    s, v25, tab, match_up, inside, mean3 = d12
    if 25 not in match_up and inside and match_up:
        not_repro.append(f"(12, 32) D_1 = {s}: the claim_scope names no lag and the note defines D_1 at any lag short against tau_L = 37917; "
                         f"{s} is reproduced by the lag-{match_up} control value and lies inside the executed short-lag range; it is not the "
                         f"lag-25 value {v25} (the note's own lag-25 column says {tab}, and the other five claim_scope numbers are that column), "
                         f"an internal inconsistency of 0.01 rather than a number the control contradicts")
    elif not inside:
        hits.append(f"(12, 32) D_1 = {s} lies outside every executed lag value")
    # ---- part 2: the linear-model calibration range
    lin = [(v[2], k, lag) for k, r in runs.items() for lag, v in r["lags"].items()]
    lo, hi = min(lin), max(lin)
    outside_lo = [(str(v), k, lag, str(r2(v, ROUND_HALF_UP)), str(r2(v, ROUND_HALF_EVEN))) for v, k, lag in lin
                  if r2(v, ROUND_HALF_UP) < lin_lo and r2(v, ROUND_HALF_EVEN) < lin_lo]
    border_lo = [(str(v), k, lag, str(r2(v, ROUND_HALF_UP)), str(r2(v, ROUND_HALF_EVEN))) for v, k, lag in lin
                 if (r2(v, ROUND_HALF_UP) < lin_lo) != (r2(v, ROUND_HALF_EVEN) < lin_lo)]
    outside_hi = [(str(v), k, lag) for v, k, lag in lin if r2(v, ROUND_HALF_UP) > lin_hi and r2(v, ROUND_HALF_EVEN) > lin_hi]
    beyond3 = [(str(v), k, lag) for v, k, lag in lin if abs(v - 1) > Decimal("0.03")]
    tab_lin = sorted({x for row in table.values() for x in row[1]})
    print(f"[linear] {len(lin)} executed calibration ratios, min {lo[0]} at {lo[1]} lag {lo[2]}, max {hi[0]} at {hi[1]} lag {hi[2]}; below the "
          f"stated {lin_lo} at two decimals under both roundings (value, run, lag, half-up, half-even): {outside_lo}; below under one rounding "
          f"only: {border_lo}; above the stated {lin_hi} at two decimals: "
          f"{outside_hi}; more than three percent from 1: {beyond3}; the note's own table's linear entries {[str(x) for x in tab_lin]}")
    if outside_lo:
        hits.append(f"the claim_scope's linear-model range {lin_lo}-{lin_hi} disagrees with the control output: "
                    + "; ".join(f"{v} at (beta, L) = {k}, lag {lag}" for v, k, lag, _, _ in outside_lo)
                    + f" rounds below {lin_lo} under both roundings (the note's own table lists {min(tab_lin)})"
                    + (f"; the body's 'within three percent at every coupling and lag' fails at "
                       + "; ".join(f"{v} at {k}, lag {lag}" for v, k, lag in beyond3) if three_pct and beyond3 else ""))
    if not outside_hi:
        not_repro.append(f"the upper end: the largest executed ratio {hi[0]} rounds to {r2(hi[0], ROUND_HALF_UP)} = the stated {lin_hi}; "
                         f"the finder compared three decimals with the claim's two")
    # ---- part 3: the exact sampling law of the calibration estimator
    rows = []
    zmax = (0.0, None)
    for k, r in sorted(runs.items()):
        K = r["T"] // every
        skip = max(5, K // 5)
        for lag, v in sorted(r["lags"].items()):
            l = lag // every
            n = K - skip - l
            sd = float(exact_var(n, l) / r["seeds"]) ** 0.5
            z = (float(v[2]) - 1) / sd
            if abs(z) > abs(zmax[0]):
                zmax = (z, (k, lag))
            if lag in (25, 1000):
                rows.append(f"{k} lag {lag}: exact sd {sd:.4f} (control's +- {v[3]}), linear ratio {v[2]} (z = {z:+.2f})")
    # Monte Carlo of the zero-mode walk at (12, 32): 4 seeds, T = 160000, every 25
    rng = np.random.default_rng(8178)
    K, S = 160000 // every, runs[(12, 32)]["seeds"]
    skip = max(5, K // 5)
    est = {1: [], 40: []}
    for _ in range(10):
        X = np.cumsum(rng.standard_normal((100, S, K, 2)), axis=2)
        for l in est:
            d = X[:, :, skip + l:] - X[:, :, skip:-l]
            est[l].append(((d ** 2).sum(-1).mean(-1) / (2 * l)).mean(-1))
    mc = {l: np.concatenate(v) for l, v in est.items()}
    ex = {l: float(exact_var(K - skip - l, l) / S) ** 0.5 for l in (1, 40)}
    p_out = float(np.mean((mc[40] < 0.965) | (mc[40] >= 1.015)))
    print("[estimator] exact standard deviation of the calibration ratio (mean exactly 1): " + "; ".join(rows)
          + f"; largest |z| over all {len(lin)} entries {zmax[0]:+.2f} at {zmax[1]}; Monte Carlo of the zero-mode walk at (12, 32), 1000 "
          f"replicas of the 4-seed estimator: lag 25 mean {mc[1].mean():.4f} sd {mc[1].std():.4f} (exact {ex[1]:.4f}), lag 1000 mean "
          f"{mc[40].mean():.4f} sd {mc[40].std():.4f} (exact {ex[40]:.4f}); probability that the lag-1000 ratio at (12, 32) falls outside "
          f"the stated two-decimal range [0.965, 1.015): {p_out:.2f}")
    assert abs(mc[1].std() / ex[1] - 1) < 0.1 and abs(mc[40].std() / ex[40] - 1) < 0.1 and abs(mc[40].mean() - 1) < 0.01
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed in part' if hits else 'not reproduced'} - the linear-model calibration range: "
          f"{'reproduced' if hits else 'not reproduced'} ({lo[0]} at {lo[1]} lag {lo[2]} rounds to {r2(lo[0], ROUND_HALF_UP)} < {lin_lo}; the "
          f"calibration ratio at lag 1000 has exact sd up to {max(ex.values()):.3f}, so the stated range is the sample's, not the "
          f"estimator's); not reproduced: " + " | ".join(not_repro))
    return 0


if __name__ == "__main__":
    sys.exit(main())
