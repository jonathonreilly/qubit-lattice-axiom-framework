#!/usr/bin/env python3
"""J:confirm:J-attack-PR8170 - independent test of the finder's executed-number HIT on block 26 (PR #8170): the claim_scope's "the
nonlinear law ... loses the magnetization of its initial plane with no plateau, at local exponents above gamma(beta)" (body: "at or above
gamma(beta) at every beta") against the executed exponents 0.0055 (beta = 24, [500, 5000]) and 0.0076, 0.0103 (beta = 12, the refuter's
independent sampler), and the runner's N5 per_block line "H_t - 3" against its D3 check "H_t - 6/25".

Different machinery from the finder (who read the fit table's printed exponents and computed gamma in Decimal):
  * gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta) at 50 digits, against the note's exact enclosures;
  * every exponent recomputed from the raw m(t) series printed by the controls (the sphere simulation's and the refuter's output files),
    by the fit's least-squares slope at 50 digits and by the two-point slope, at the printed precision;
  * the harmonic bound recomputed from exact rationals: P_k = 9^{-k} sum_{a+b+c=k} (k!/(a!b!c!))^2 (two independent level walks meet),
    min over t <= 150 of sum_{k=1..t} P_k - (3 sqrt3/(4 pi)) H_t;
  * an independent chain of the law (von Mises-Fisher conditionals carried by a Householder reflection; four replicas; 256 x 256 planes;
    5000 levels; other seeds) for exp[500, 5000] at beta = 24 and 12, from the norm |m| and from the projection m_z, with replica errors.
Prints "HIT: confirmed - ..." for each part of the finder's conclusion this test reproduces, and says which parts it does not.
Usage: python3 exponents_vs_gamma_independent.py [--quick]   (--quick: tiny chain, for testing only)
"""
import re
import subprocess
import sys
import time
from fractions import Fraction
from math import factorial
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block26-unsoldered-formation-law-level-time-gain-one-spin-waves-memory-decay-20260916"
HEAD = "f9e1177003afa991ec87831d2be70611068a09ab"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_"
        "THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md")
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.txt"
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
mp.mp.dps = 50


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def gamma(beta):
    k = 3 * mp.mpf(beta)
    return 3 * mp.sqrt(3) / (4 * mp.pi) * (mp.coth(k) - 1 / k) / k


def ls_slope(ts, ms, a, b):
    pts = [(mp.log(t), mp.log(m)) for t, m in zip(ts, ms) if a <= t <= b]
    n = len(pts)
    sx = mp.fsum(x for x, _ in pts)
    sy = mp.fsum(y for _, y in pts)
    sxx = mp.fsum(x * x for x, _ in pts)
    sxy = mp.fsum(x * y for x, y in pts)
    return -(n * sxy - sx * sy) / (n * sxx - sx * sx)


def series(text, header_regex):
    out, on = [], False
    for line in text.splitlines():
        if line.startswith("====="):
            on = re.search(header_regex, line) is not None
            continue
        if on:
            g = re.match(r"\s*t=\s*(\d+)\s+\|m\|=([0-9.]+)(?:\s+m_z=(-?[0-9.]+))?", line)
            if g:
                out.append((int(g.group(1)), mp.mpf(g.group(3) if g.group(3) else g.group(2))))
    return out


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


def chain(beta, L, R, T, every, seed):
    rng = np.random.default_rng(seed)
    s = np.zeros((R, L, L, 3))
    s[..., 2] = 1
    ts, mn, mz = [], [], []
    for t in range(1, T + 1):
        s = vmf_householder(beta * (s + np.roll(s, 1, axis=1) + np.roll(s, 1, axis=2)), rng)
        if t % every == 0:
            M = s.mean(axis=(1, 2))
            ts.append(t)
            mn.append(np.linalg.norm(M, axis=-1))
            mz.append(M[:, 2])
    return ts, np.array(mn), np.array(mz)


def main():
    quick = "--quick" in sys.argv
    t0 = time.time()
    note = show(NOTE)
    cache = show(CACHE)
    sim = show(SPECS + "supervisor_control_block26_sphere_sim.out.txt")
    ref = show(SPECS + "supervisor_control_block26_refuter.out.txt")
    scope = next(l for l in note.splitlines() if l.startswith("claim_scope:"))
    claim = "at local exponents above gamma(beta) that approach it as beta grows" in scope
    body = "The local exponent is at or above `γ(β)` at every `β`" in note
    rows = []
    for line in note.splitlines():
        c = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(c) == 11 and c[0].isdigit():
            rows.append((int(c[0]), int(c[1]), [mp.mpf(c[6]), mp.mpf(c[7]), mp.mpf(c[8])], c[10]))
    encl = {3: (408, 10 ** 4), 6: (216, 10 ** 4), 12: (1116, 10 ** 5), 24: (566, 10 ** 5)}
    g = {b: gamma(b) for b in encl}
    encl_ok = all(mp.mpf(lo) / d <= g[b] <= mp.mpf(lo + 1) / d for b, (lo, d) in encl.items())
    print(f"[inputs] at {HEAD[:10]}: claim_scope 'at local exponents above gamma(beta)': {claim}; body 'at or above gamma(beta) at every beta': "
          f"{body}; table rows {len(rows)}; gamma at 50 digits: " + ", ".join(f"{b}: {mp.nstr(g[b], 8)}" for b in sorted(g))
          + f" (inside the note's enclosures: {encl_ok})")
    # ---- recompute every exponent from the raw series
    srcs = {("control", 24): series(sim, r"sim_b24_L512"), ("control", 12): series(sim, r"sim_b12_L512"), ("control", 3): series(sim, r"sim_b3_L512"),
            ("control", 6): series(sim, r"sim_b6_L512"), ("refuter", 12): series(ref, r"mode sphere beta=12 L=512")}
    below = []
    lines = []
    for (run, b), ser in srcs.items():
        ts = [t for t, _ in ser]
        ms = [m for _, m in ser]
        T = ts[-1]
        fits = [ls_slope(ts, ms, 500, 5000), ls_slope(ts, ms, 5000, T), ls_slope(ts, ms, 500, T)]
        idx = {t: m for t, m in ser}
        two = [mp.log(idx[500] / idx[5000]) / mp.log(10), mp.log(idx[5000] / idx[T]) / mp.log(mp.mpf(T) / 5000), mp.log(idx[500] / idx[T]) / mp.log(mp.mpf(T) / 500)]
        tab = next((r[2] for r in rows if r[0] == b and r[1] == 512 and (("refuter" in r[3]) == (run == "refuter"))), None)
        match = tab is not None and all(abs(mp.nint(f * 10 ** 4) / 10 ** 4 - x) < mp.mpf(10) ** -6 for f, x in zip(fits, tab))
        for lab, f, tw in zip(("[500,5000]", "[5000,T]", "[500,T]"), fits, two):
            if f < g[b]:
                below.append((run, b, lab, f, tw))
        lines.append(f"{run} beta={b}: least-squares {', '.join(mp.nstr(f, 4) for f in fits)} (table {', '.join(mp.nstr(x, 4) for x in tab) if tab else '-'}, "
                     f"reproduced: {match}); two-point {', '.join(mp.nstr(x, 4) for x in two)}; gamma {mp.nstr(g[b], 5)}")
    print("[exponents] " + " | ".join(lines))
    print(f"[below gamma] least-squares exponents below gamma(beta): "
          + "; ".join(f"{r} beta={b} {lab} {mp.nstr(f, 4)} (two-point {mp.nstr(tw, 4)}) vs {mp.nstr(g[b], 5)}" for r, b, lab, f, tw in below))
    # ---- the harmonic bound, exactly
    c0 = 3 * mp.sqrt(3) / (4 * mp.pi)
    Pk = []
    for k in range(0, 151):
        s = sum((factorial(k) // (factorial(a) * factorial(b) * factorial(k - a - b))) ** 2 for a in range(k + 1) for b in range(k + 1 - a))
        Pk.append(Fraction(s, 9 ** k))
    S, H, worst, tw = Fraction(0), Fraction(0), None, 0
    for t in range(1, 151):
        S += Pk[t]
        H += Fraction(1, t)
        d = mp.mpf(S.numerator) / S.denominator - c0 * (mp.mpf(H.numerator) / H.denominator)
        if worst is None or d < worst:
            worst, tw = d, t
    pb = re.search(r"per_block: executed — sum_\{k<=t\} P_k >= \(3 sqrt3/\(4 pi\)\) H_t - (\S+) for t <= 150", cache)
    d3 = re.search(r"PASS: D3 .*?H_t - (\S+) for t <= 150 exactly", cache)
    print(f"[harmonic] P_1 = {Pk[1]}, P_2 = {Pk[2]}; min over t <= 150 of sum_(k=1..t) P_k - (3 sqrt3/(4 pi)) H_t = {mp.nstr(worst, 8)} at t = {tw} "
          f"(>= -6/25: {worst >= -mp.mpf(6) / 25}); the runner's per_block line prints the constant {pb.group(1) if pb else '?'}, its D3 check "
          f"{d3.group(1) if d3 else '?'}, the note's T3 1/4")
    # ---- independent chain
    L, R, T, every = (32, 2, 600, 100) if quick else (256, 4, 5000, 500)
    chain_rows = {}
    for b, seed in ((24, 81702), (12, 81701)):
        ts, mn, mz = chain(b, L, R, T, every, seed)
        a0 = 500 if not quick else 100
        eN = [ls_slope(ts, [mp.mpf(x) for x in mn[:, r]], a0, T) for r in range(R)]
        eZ = [ls_slope(ts, [mp.mpf(x) for x in mz[:, r]], a0, T) for r in range(R)]
        mN, sN = mp.fsum(eN) / R, mp.sqrt(mp.fsum((x - mp.fsum(eN) / R) ** 2 for x in eN) / (R - 1) / R)
        mZ, sZ = mp.fsum(eZ) / R, mp.sqrt(mp.fsum((x - mp.fsum(eZ) / R) ** 2 for x in eZ) / (R - 1) / R)
        chain_rows[b] = (mN, sN, mZ, sZ, eN)
        print(f"[chain beta={b}] {L}x{L}, {R} replicas, {T} levels: exp[{a0},{T}] from |m| {mp.nstr(mN, 4)} +- {mp.nstr(sN, 2)} (replicas "
              f"{', '.join(mp.nstr(x, 4) for x in eN)}), from m_z {mp.nstr(mZ, 4)} +- {mp.nstr(sZ, 2)}; gamma {mp.nstr(g[b], 5)}; |m|({T}) "
              f"{np.mean(mn[-1]):.4f}  ({time.time() - t0:.0f}s)")
    hits, not_repro = [], []
    if claim and below:
        hits.append("the claim_scope's 'at local exponents above gamma(beta)' (body: 'at or above gamma(beta) at every beta') is contradicted by "
                    + "; ".join(f"the {r}'s beta = {b} exponent over {lab}, {mp.nstr(f, 4)} < gamma = {mp.nstr(g[b], 5)}" for r, b, lab, f, tw in below)
                    + " (recomputed from the printed m(t) series; gamma at 50 digits)")
    if pb and d3 and pb.group(1) != d3.group(1):
        hits.append(f"the runner's N5 per_block line states the harmonic bound with the constant {pb.group(1)}, its D3 check executes {d3.group(1)} and "
                    f"the note's T3 states 1/4 (exact minimum of sum P_k - c0 H_t over t <= 150: {mp.nstr(worst, 6)}); the resolution line misprints "
                    f"the executed constant (a weaker, still true statement)")
    mN24, sN24 = chain_rows[24][0], chain_rows[24][1]
    not_repro.append(f"whether the law's exponent over [500, 5000] at beta = 24 lies below gamma: my chain gives {mp.nstr(mN24, 4)} +- {mp.nstr(sN24, 2)} "
                     f"from |m| against gamma {mp.nstr(g[24], 5)} (the control's single 512^2 run gave 0.0055)")
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed' if hits else 'not reproduced'} - {len(hits)} of the finder's parts reproduced with exact gamma and exponents "
          f"recomputed from the raw series: {len(below)} executed exponents below gamma(beta); the per_block constant {pb.group(1) if pb else '?'} vs "
          f"D3's {d3.group(1) if d3 else '?'}; context: " + " | ".join(not_repro)
          + f"; beta = 12 chain {mp.nstr(chain_rows[12][0], 4)} +- {mp.nstr(chain_rows[12][1], 2)} vs gamma {mp.nstr(g[12], 5)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
