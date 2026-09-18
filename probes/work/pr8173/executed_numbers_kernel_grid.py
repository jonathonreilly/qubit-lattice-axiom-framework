#!/usr/bin/env python3
"""J:attack:PR8173 - block 29, attack pattern (c) EXECUTED NUMBERS.

Claim_scope names the transverse-kernel normalization c(beta, k) = beta E(k) S_perp(k)
measured on 16^3, 24^3, 32^3 at beta = 0.8, 1, 1.5, 2, 3, lying at 0.86-0.98 for
n >= 2. This script does not reuse the provenance ITEMS loop. It:

  * parses the kernel and refuter controls as Decimal columns
  * recomputes (m^2/3)^2 from printed m
  * recomputes G_L(r) from the note's Fourier formula (N^{-1} sum_{k!=0} e^{ik.r}/E(k)
    with E(k) = 2 sum_j (1-cos k_j)) and T(r)*beta/G_L(r) against the refuter line
  * checks every named (L, beta) pair and every n >= 2 token against 0.86-0.98

HIT if a named executed range, count or grid point disagrees with the control.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path

import numpy as np
from numpy.fft import ifftn

getcontext().prec = 40

ROOT = Path(__file__).resolve().parents[3]
HEAD = "e5b3aa31686d88d8a2fe0aad5e938acac0e39404"
BRANCH = (
    "physics-loop/admissibility-induced-law-block29-transverse-kernel-normalization-"
    "measured-sum-rule-spin-wave-20260916"
)
NOTE = (
    "docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_"
    "MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_"
    "BOUNDED_THEOREM_NOTE_2026-09-16.md"
)
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
KER = SPECS + "supervisor_control_block29_kernel.out.txt"
REF = SPECS + "supervisor_control_block29_refuter.out.txt"

NAMED_L = (16, 24, 32)
NAMED_BETA = (Decimal("0.8"), Decimal("1"), Decimal("1.5"), Decimal("2"), Decimal("3"))
STATED_LO, STATED_HI = Decimal("0.86"), Decimal("0.98")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr.strip()[:400]}")
    return r.stdout


def parse_kernel(text: str) -> list[dict]:
    rows = []
    L = None
    cur = None
    for line in text.splitlines():
        m = re.match(r"===== kernel_L(\d+) =====", line)
        if m:
            L = int(m.group(1))
            continue
        m = re.match(
            r"\s+beta=([0-9.]+): m = ([0-9.]+), m\^2 = ([0-9.]+), \(m\^2/3\)\^2 = ([0-9.]+)",
            line,
        )
        if m and L is not None:
            cur = {
                "L": L,
                "beta": Decimal(m.group(1)),
                "m": Decimal(m.group(2)),
                "m2": Decimal(m.group(3)),
                "lb": Decimal(m.group(4)),
                "c": [],
                "T": [],
            }
            rows.append(cur)
            continue
        m = re.search(r"n  beta E\(k\) S_perp\(k\):\s*(.+)$", line)
        if m and cur is not None:
            cur["c"] = [Decimal(t) for t in m.group(1).split()]
            continue
        m = re.search(r"T\(r\) r=0\.\.8:\s*(.+)$", line)
        if m and cur is not None:
            cur["T"] = [Decimal(t) for t in m.group(1).split()]
    return rows


def green_e1(L: int, nmax: int = 6) -> list[Decimal]:
    kx = 2 * np.pi * np.arange(L) / L
    kx, ky, kz = np.meshgrid(kx, kx, kx, indexing="ij")
    E = 2 * ((1 - np.cos(kx)) + (1 - np.cos(ky)) + (1 - np.cos(kz)))
    inv = np.zeros_like(E)
    inv[E > 1e-15] = 1.0 / E[E > 1e-15]
    g = ifftn(inv).real
    return [Decimal(str(float(g[r, 0, 0]))) for r in range(min(nmax, L))]


def main() -> None:
    note = show(NOTE)
    ker = show(KER)
    ref = show(REF)
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r"lies at ([0-9.]+)-([0-9.]+) for the modes n >= 2", fm)
    if not m:
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; claim_scope range sentence not found")
        return
    scope_lo, scope_hi = Decimal(m.group(1)), Decimal(m.group(2))
    print(f"claim_scope n>=2 range: {scope_lo}-{scope_hi}")
    print(f"named grid: L={list(NAMED_L)} beta={list(map(str, NAMED_BETA))} ({len(NAMED_L)*len(NAMED_BETA)} pairs)")

    rows = parse_kernel(ker)
    executed = {(r["L"], r["beta"]) for r in rows}
    print(f"kernel control (L,beta) pairs: {sorted((L, str(b)) for L, b in executed)}")

    hits: list[str] = []

    named = {(L, b) for L in NAMED_L for b in NAMED_BETA}
    missing = sorted(named - executed, key=lambda t: (t[0], t[1]))
    extra = sorted(executed - named, key=lambda t: (t[0], t[1]))
    print(f"named pairs missing from control: {[(L, str(b)) for L, b in missing]}")
    if extra:
        print(f"control pairs not in named grid: {[(L, str(b)) for L, b in extra]}")
    if missing:
        hits.append(
            f"claim_scope names {len(named)} (L,beta) pairs, control ran {len(executed)}; "
            f"missing {[(L, str(b)) for L, b in missing]}"
        )

    n2_all: list[tuple] = []
    for r in rows:
        m2 = r["m"] * r["m"]
        lb = (m2 / 3) ** 2
        print(
            f"L={r['L']} beta={r['beta']}: m={r['m']} printed (m^2/3)^2={r['lb']} "
            f"recomputed {lb:.6f} |c|={len(r['c'])}"
        )
        if abs(lb - r["lb"]) > Decimal("0.00015"):
            hits.append(f"(m^2/3)^2 L={r['L']} beta={r['beta']} printed {r['lb']} vs m^2 {lb:.6f}")
        for n, c in enumerate(r["c"], start=1):
            if n >= 2:
                n2_all.append((r["L"], r["beta"], n, c))

    if n2_all:
        lo = min(n2_all, key=lambda t: t[3])
        hi = max(n2_all, key=lambda t: t[3])
        print(f"n>=2 min {lo[3]} at L={lo[0]} beta={lo[1]} n={lo[2]}")
        print(f"n>=2 max {hi[3]} at L={hi[0]} beta={hi[1]} n={hi[2]}")
        outside = [t for t in n2_all if t[3] < scope_lo or t[3] > scope_hi]
        print(f"n>=2 outside claim_scope [{scope_lo},{scope_hi}]: {len(outside)} of {len(n2_all)}")
        for t in sorted(outside, key=lambda x: x[3], reverse=True)[:8]:
            print(f"  outside: L={t[0]} beta={t[1]} n={t[2]} c={t[3]}")
        if outside:
            hits.append(
                f"n>=2 c spans {lo[3]}-{hi[3]} against claim_scope {scope_lo}-{scope_hi} "
                f"({len(outside)} of {len(n2_all)} leave the interval)"
            )

    g16 = green_e1(16, 6)
    print("recomputed G_16(r e1) r=0..5:", [f"{x:.4f}" for x in g16])
    gm = re.search(r"G_L\(r\) along e_1 \(L=16\):\s*([0-9. ]+)", ref)
    if gm:
        printed_g = [Decimal(t) for t in gm.group(1).split()]
        print("refuter G_16:", printed_g)
        for i, (a, b) in enumerate(zip(g16, printed_g)):
            if abs(a - b) > Decimal("0.00015"):
                hits.append(f"G_L(r={i}) recomputed {a:.4f} vs refuter {b}")

    # refuter real-space c from T(r)*beta/G_L
    for bm in re.finditer(
        r"beta=([0-9.]+):.*c from T\(r\)/\(G_L\(r\)/beta\), r=1\.\.4:\s*([0-9. ]+)",
        ref,
    ):
        beta = Decimal(bm.group(1))
        stated = [Decimal(t) for t in bm.group(2).split()]
        tm = re.search(rf"beta={re.escape(bm.group(1))}:.*T\(r\) r=0\.\.5:\s*([0-9.\- ]+)", ref)
        if not tm:
            continue
        T = [Decimal(t) for t in tm.group(1).split()]
        recomputed = [T[r] * beta / g16[r] for r in range(1, 5)]
        print(f"refuter real-space c beta={beta}: stated {stated} recomputed {[f'{x:.3f}' for x in recomputed]} (rounded-token INFO)")

    mm = re.search(r"single-site proposal chain at `?beta = 1.5`? gives `?c = ([0-9., ]+)", note)
    if mm:
        print("note Metropolis c n=1..6:", mm.group(1))
    rm = re.search(r"Metropolis single-site chain[\s\S]*?\n\s*([0-9. ]+)", ref)
    if rm:
        mc = [Decimal(t) for t in rm.group(1).split()]
        print("refuter Metropolis c:", mc)
        n2m = [c for i, c in enumerate(mc, start=1) if i >= 2]
        bad = [c for c in n2m if c < scope_lo or c > scope_hi]
        if bad:
            hits.append(
                f"Metropolis n>=2 tokens {[str(c) for c in n2m]} leave claim_scope {scope_lo}-{scope_hi}"
            )

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; every named range and grid point matches the controls")


if __name__ == "__main__":
    main()
