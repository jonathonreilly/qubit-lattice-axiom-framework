#!/usr/bin/env python3
"""J:confirm:J-attack-PR8173 - independent test of the finder's executed-number HIT on block 29 (PR #8173): the claim_scope's
"c(beta, k) = beta E(k) S_perp(k) ... measured on 16^3, 24^3, 32^3 at beta = 0.8, 1, 1.5, 2, 3 ... lies at 0.86-0.98 for the modes
n >= 2", against (1) the kernel control's values, (2) the named grid, (3) the refuter's single-site (Metropolis) chain.

Different machinery from the finder (who compared three-decimal control values with the claim's two-decimal bounds):
  * the claim_scope, the body's own range sentence and the note's table are parsed from the note, the controls from the PR branch,
    all at the PR head; every comparison is made at the claim's precision (two decimals, ROUND_HALF_UP and ROUND_HALF_EVEN);
  * an independent measurement of c(beta, k): my own heat-bath chain for the law prod e^{beta s.s'} (von Mises-Fisher conditionals
    drawn around e_3 and carried to the neighbour-sum direction by a Householder reflection, not the controls' orthonormal frame),
    eight independent replicas per point from an aligned start, and the structure factor from the one-dimensional transform of
    the plane sums (sum_x s_perp(x) e^{-ik.x} = sum_{x_1} e^{-ik x_1} P(x_1) for k along e_1) instead of a three-dimensional FFT; error
    bars from the replica spread; points (L, beta) = (16, 3), (16, 1.5) (where the control's values exceed 0.98) and (12, 3) (another
    size); my magnetization is checked against the control's before any c is read.
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
BRANCH = "physics-loop/admissibility-induced-law-block29-transverse-kernel-normalization-measured-sum-rule-spin-wave-20260916"
HEAD = "e5b3aa31686d88d8a2fe0aad5e938acac0e39404"
NOTE = ("docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_"
        "TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_BOUNDED_THEOREM_NOTE_2026-09-16.md")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def r2(x, mode):
    return Decimal(x).quantize(Decimal("0.01"), rounding=mode)


def vmf_householder(V, rng):
    kap = np.linalg.norm(V, axis=-1)
    u = V / np.maximum(kap, 1e-300)[..., None]
    U = rng.random(kap.shape)
    w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1)
    ph = 2 * np.pi * rng.random(kap.shape)
    rr = np.sqrt(np.clip(1 - w * w, 0, 1))
    s0 = np.stack([rr * np.cos(ph), rr * np.sin(ph), w], axis=-1)          # vMF around e_3
    v = -u.copy()
    v[..., 2] += 1                                                         # v = e_3 - u; H = I - 2 v v^T/|v|^2 maps e_3 to u
    vv = (v * v).sum(-1)
    safe = vv > 1e-24
    coef = np.where(safe, 2 * (s0 * v).sum(-1) / np.where(safe, vv, 1), 0.0)
    return s0 - coef[..., None] * v


def measure(L, beta, R, sweeps, therm, seed):
    rng = np.random.default_rng(seed)
    par = np.indices((L, L, L)).sum(0) % 2
    s = np.zeros((R, L, L, L, 3))
    s[..., 2] = 1
    ns = np.arange(1, L // 2 + 1)
    ph = np.exp(-2j * np.pi * np.outer(ns, np.arange(L)) / L)               # (modes, x_1)
    Sk = np.zeros((R, len(ns)))
    mabs = np.zeros(R)
    cnt = 0
    for sw in range(sweeps):
        for p in (0, 1):
            V = sum(np.roll(s, sh, ax) for ax in (1, 2, 3) for sh in (1, -1))
            s = np.where((par == p)[None, ..., None], vmf_householder(beta * V, rng), s)
        if sw >= therm:
            M = s.mean(axis=(1, 2, 3))
            m = np.linalg.norm(M, axis=-1)
            u = M / m[:, None]
            sp = s - np.einsum("rxyzc,rc->rxyz", s, u)[..., None] * u[:, None, None, None, :]
            P = sp.sum(axis=(2, 3))                                            # plane sums, (R, L, 3)
            F = np.einsum("nx,rxc->rnc", ph, P)
            Sk += (np.abs(F) ** 2).sum(-1) / L ** 3 / 2
            mabs += m
            cnt += 1
    Sk /= cnt
    mabs /= cnt
    E = 2 * (1 - np.cos(2 * np.pi * ns / L))
    c = beta * E[None, :] * Sk                                                # (R, modes)
    return c.mean(0), c.std(0, ddof=1) / np.sqrt(R), mabs.mean(), mabs.std(ddof=1) / np.sqrt(R)


def main():
    t0 = time.time()
    note = show(NOTE)
    ker = show(SPECS + "supervisor_control_block29_kernel.out.txt")
    ref = show(SPECS + "supervisor_control_block29_refuter.out.txt")
    scope = next(l for l in note.splitlines() if l.startswith("claim_scope:"))
    lo_s, hi_s = map(Decimal, re.search(r"lies at ([0-9.]+)-([0-9.]+) for the modes n >= 2", scope).groups())
    grid_txt = re.search(r"measured on ([0-9^, ]+) at beta = ([0-9., ]+) for k along an axis", scope)
    sizes = [int(x.split("^")[0]) for x in grid_txt.group(1).split(", ")]
    betas = [Decimal(x) for x in grid_txt.group(2).strip(", ").split(", ")]
    body = re.search(r"For the modes `n ≥ 2` the normalization lies between `([0-9.]+)` and `([0-9.]+)` at every lattice size and coupling",
                     note)
    lo_b, hi_b = map(Decimal, body.groups())
    up_front = re.search(r"comes out between\s+`([0-9.]+)` and `([0-9.]+)` for every mode but the longest", note)
    # the kernel control
    runs, L = {}, None
    for line in ker.splitlines():
        h = re.match(r"===== kernel_L(\d+) =====", line)
        if h:
            L = int(h.group(1))
            continue
        b = re.match(r"\s+beta=([0-9.]+): m = ([0-9.]+),", line)
        if b:
            key = (L, Decimal(b.group(1)).normalize())
            runs[key] = {"m": Decimal(b.group(2))}
            continue
        c = re.search(r"n  beta E\(k\) S_perp\(k\):\s*(.+)$", line)
        if c:
            runs[key]["c"] = [Decimal(x) for x in c.group(1).split()]
    table = {}
    for line in note.splitlines():
        cells = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0].isdigit() and re.fullmatch(r"[0-9.]+", cells[1]):
            table[(int(cells[0]), Decimal(cells[1]).normalize())] = [Decimal(x) for x in cells[4].split()]
    print(f"[inputs] at {HEAD[:10]}: claim_scope range {lo_s}-{hi_s} on sizes {sizes} x couplings {[str(b) for b in betas]}; body sentence "
          f"(i): {lo_b}-{hi_b}; result-up-front: {up_front.group(1)}-{up_front.group(2)}; kernel control pairs {sorted((k[0], str(k[1])) for k in runs)}; "
          f"table pairs {len(table)}")
    hits, not_repro = [], []
    # ---- part 1: the n >= 2 range at the claim's precision
    n2 = [(v, k, n) for k, r in runs.items() for n, v in enumerate(r["c"], start=1) if n >= 2]
    above = [(str(v), k, n, str(r2(v, ROUND_HALF_UP)), str(r2(v, ROUND_HALF_EVEN))) for v, k, n in n2
             if r2(v, ROUND_HALF_UP) > hi_s and r2(v, ROUND_HALF_EVEN) > hi_s]
    below = [(str(v), k, n) for v, k, n in n2 if r2(v, ROUND_HALF_UP) < lo_s and r2(v, ROUND_HALF_EVEN) < lo_s]
    tab_n2 = [x for k, row in table.items() for x in row[1:]]
    in_body = all(lo_b <= r2(v, ROUND_HALF_UP) <= hi_b for v, _, _ in n2)
    tab_same = all([r2(v, ROUND_HALF_UP) for v in runs[k]["c"]] == table[k] for k in runs)
    print(f"[range] {len(n2)} control values with n >= 2, min {min(n2)[0]}, max {max(n2)[0]}; above the claim_scope's {hi_s} at two decimals "
          f"under both roundings (value, (L, beta), n, half-up, half-even): {[(a, (k[0], str(k[1])), n, u, e) for a, k, n, u, e in above]}; "
          f"below {lo_s}: {below}; all inside the body's {lo_b}-{hi_b}: {in_body}; the note's table equals the control rounded half-up: "
          f"{tab_same}, its n >= 2 entries span {min(tab_n2)}-{max(tab_n2)}")
    if above or below:
        hits.append(f"the claim_scope's n >= 2 range {lo_s}-{hi_s} disagrees with the kernel control: {len(above)} values round above {hi_s} "
                    f"(max {max(n2)[0]} at (L, beta) = ({max(n2)[1][0]}, {max(n2)[1][1]}), n = {max(n2)[2]}), while the note's own body "
                    f"states {lo_b}-{hi_b} and its table prints entries up to {max(tab_n2)}")
    # ---- part 2: the named grid
    product = {(Lx, b.normalize()) for Lx in sizes for b in betas}
    missing = sorted(product - set(runs))
    print(f"[grid] the claim_scope's sizes x couplings = {len(product)} pairs; executed {len(runs)}; not executed: "
          f"{[(Lx, str(b)) for Lx, b in missing]}; the note's table lists exactly the executed pairs: {set(table) == set(runs)}")
    if missing:
        hits.append(f"read as the product of its three sizes and five couplings, the claim_scope's grid names {len(product)} (L, beta) pairs of "
                    f"which {len(missing)} were not executed: {[(Lx, str(b)) for Lx, b in missing]} (the note's table lists the {len(runs)} run)")
    # ---- part 3: my own chain
    mine = {}
    for (Lx, beta, seed) in [(16, 3.0, 81731), (16, 1.5, 81732), (12, 3.0, 81733)]:
        c, e, m, me = measure(Lx, beta, R=8, sweeps=2500, therm=800, seed=seed)
        mine[(Lx, beta)] = (c, e, m, me)
        ck = runs.get((Lx, Decimal(str(beta)).normalize()))
        mline = f"m = {m:.4f} +- {me:.4f}" + (f" (control {ck['m']})" if ck else "")
        print(f"[chain L={Lx} beta={beta}] {mline}; c(n) n=1..{min(8, Lx // 2)}: "
              + " ".join(f"{c[i]:.3f}+-{e[i]:.3f}" for i in range(min(8, Lx // 2))) + f"  ({time.time() - t0:.0f}s)")
        if ck:
            assert abs(m - float(ck["m"])) < 0.01 + 3 * me, (m, ck["m"])
    c16, e16 = mine[(16, 3.0)][0][1:8], mine[(16, 3.0)][1][1:8]
    over = [(n + 2, round(float(c16[n]), 3)) for n in range(7) if c16[n] - 2 * e16[n] > 0.985]
    c12 = mine[(12, 3.0)][0][1:6]
    c15, e15 = mine[(16, 1.5)][0], mine[(16, 1.5)][1]
    met_txt = re.search(r"n = 1\.\.6\n\s*([0-9. ]+)", ref).group(1).strip()
    print(f"[independent] at (16, 3): mean over n = 2..8 of c = {c16.mean():.3f}; modes whose c exceeds 0.985 by more than two standard "
          f"errors: {over}; values rounding above 0.98: {sum(1 for x in c16 if round(float(x), 2) > 0.98)} of 7; at (12, 3): n = 2..6 "
          f"{' '.join(f'{x:.3f}' for x in c12)}; at (16, 1.5): c(2) = {c15[1]:.3f} +- {e15[1]:.3f}, n = 2..6 range {c15[1:6].min():.3f}-"
          f"{c15[1:6].max():.3f}; the refuter's single-site chain at (16, 1.5): {met_txt}")
    met = [Decimal(x) for x in met_txt.split()]
    met_z = (float(met[1]) - c15[1]) / e15[1]
    not_repro.append(f"the single-site chain's values ({', '.join(map(str, met[1:]))} for n = 2..6) are not the claim_scope's measurement (the "
                     f"heat-bath control on the three sizes); my independent chain at (16, 1.5) gives c(2) = {c15[1]:.3f} +- {e15[1]:.3f}, so its "
                     f"n = 2 value {met[1]} is {met_z:.0f} of my standard errors away: a noisy check, not evidence against the range")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed in part' if hits else 'not reproduced'} - {len(hits)} of the finder's 3 parts reproduced: the n >= 2 range "
          f"({len(above)} control values round above {hi_s}, up to {max(n2)[0]}; the body says {lo_b}-{hi_b}; my own chain at (16, 3) averages "
          f"{c16.mean():.3f} over n = 2..8 with {sum(1 for x in c16 if round(float(x), 2) > 0.98)} of 7 modes rounding above 0.98) and the "
          f"grid under the product reading ({len(missing)} of {len(product)} pairs not run); not reproduced: " + " | ".join(not_repro))
    return 0


if __name__ == "__main__":
    sys.exit(main())
