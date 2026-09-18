#!/usr/bin/env python3
"""J:confirm:J-provenance:PR8170 — independent check of 'exponents above gamma'.

Finder (opus-max-1 / claude-opus-5) logged that claim_scope's executed
'local exponents above gamma(beta)' is contradicted by the fit table, using
hardcoded gamma floats and an ITEMS regex. This script does not reuse that
loop. It:

  * pulls claim_scope, the markdown table, the fit control, and the E3 cache
    line from the PR head via git
  * parses fit-control columns with Decimal (whitespace fields, not 'beta=')
  * recomputes gamma(beta) = (3 sqrt(3)/(4 pi)) A(3 beta)/(3 beta) from
    A(kappa) = coth(kappa) - 1/kappa in Decimal
  * compares printed exp columns to that gamma and to the T5 enclosures
    parsed as fractions from the runner cache

HIT if any L>=256 printed local exponent is strictly below gamma(beta).
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[4]
HEAD = "f9e1177003afa991ec87831d2be70611068a09ab"
NOTE = (
    "docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_"
    "FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md"
)
FIT = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block26_fit.out.txt"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_"
    "local_limit_constant_finite_planes_forget_2026_09_16.txt"
)
PI = Decimal("3.14159265358979323846264338327950288419716939937510")
WINDOWS = (
    ("exp[500,5000]", 6, 500, 5000),
    ("exp[5000,T]", 7, 5000, 20000),
    ("exp[500,T]", 8, 500, 20000),
)


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def coth(x: Decimal) -> Decimal:
    t = (2 * x).exp()
    return (t + 1) / (t - 1)


def langevin_A(kappa: Decimal) -> Decimal:
    return coth(kappa) - 1 / kappa


def gamma_of(beta: Decimal) -> Decimal:
    return (3 * Decimal(3).sqrt() / (4 * PI)) * langevin_A(3 * beta) / (3 * beta)


def parse_fit(text: str) -> list[tuple]:
    """Return (beta, L, T, m500, m5000, mT, e1, e2, e3, gamma_print, tag) as Decimal/int."""
    rows = []
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 11:
            continue
        try:
            beta = Decimal(parts[0])
            L = int(parts[1])
            T = int(parts[2])
            m500, m5000, mT = Decimal(parts[3]), Decimal(parts[4]), Decimal(parts[5])
            e1, e2, e3 = Decimal(parts[6]), Decimal(parts[7]), Decimal(parts[8])
            gprint = Decimal(parts[9])
        except Exception:
            continue
        if beta not in (Decimal(3), Decimal(6), Decimal(12), Decimal(24)):
            continue
        if any(v.is_nan() for v in (e1, e2, e3, m500, m5000, mT)):
            continue
        rows.append((beta, L, T, m500, m5000, mT, e1, e2, e3, gprint, parts[10]))
    return rows


def parse_note_table(note: str) -> list[tuple]:
    rows = []
    for line in note.splitlines():
        if not re.match(r"\| *`?\d+`? *\|", line):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 11:
            continue
        try:
            beta, L = Decimal(cells[0]), int(cells[1])
            e1, e2, e3 = Decimal(cells[6]), Decimal(cells[7]), Decimal(cells[8])
            gprint = Decimal(cells[9])
            tag = cells[10]
        except Exception:
            continue
        rows.append((beta, L, e1, e2, e3, gprint, tag))
    return rows


def parse_enclosures(cache: str) -> dict[int, tuple[Fraction, Fraction]]:
    m = re.search(
        r"lies in \[(\d+), (\d+)\]/10\^(\d+) at beta = (\d+), "
        r"\[(\d+), (\d+)\]/10\^(\d+) at (\d+), "
        r"\[(\d+), (\d+)\]/10\^(\d+) at (\d+), "
        r"\[(\d+), (\d+)\]/10\^(\d+) at (\d+)",
        cache,
    )
    if not m:
        return {}
    g = m.groups()
    out = {}
    for i in range(0, 16, 4):
        lo, hi, p, b = int(g[i]), int(g[i + 1]), int(g[i + 2]), int(g[i + 3])
        den = 10 ** p
        out[b] = (Fraction(lo, den), Fraction(hi, den))
    return out


def loc_exp(m1: Decimal, t1: int, m2: Decimal, t2: int) -> Decimal:
    return (m1 / m2).ln() / (Decimal(t2) / Decimal(t1)).ln()


def main() -> None:
    note = git_show(NOTE)
    fit = git_show(FIT)
    cache = git_show(CACHE)
    fm = note.split("\n---\n", 1)[0]
    if "at local exponents above gamma(beta)" not in fm.replace("\n", " "):
        print("SUMMARY: not reproduced - claim_scope sentence 'local exponents above gamma(beta)' not found")
        return

    encl = parse_enclosures(cache)
    print(f"T5 enclosures from cache E3: { {b: (str(lo), str(hi)) for b, (lo, hi) in encl.items()} }")
    for b in (3, 6, 12, 24):
        g = gamma_of(Decimal(b))
        print(f"Langevin gamma({b}) = {g:.12f}")
        if b in encl:
            lo, hi = encl[b]
            inside = Decimal(lo.numerator) / Decimal(lo.denominator) <= g <= Decimal(hi.numerator) / Decimal(hi.denominator)
            print(f"  enclosure [{lo}, {hi}] contains computed gamma: {inside}")

    table = parse_note_table(note)
    print(f"note table rows: {len(table)}")
    fit_rows = parse_fit(fit)
    large = [r for r in fit_rows if r[1] >= 256 and r[2] == 20000]
    print(f"fit control large-L rows (L>=256, T=20000): {len(large)}")

    hits: list[str] = []
    for beta, L, T, m500, m5000, mT, e1, e2, e3, gprint, tag in large:
        g = gamma_of(beta)
        ms = {500: m500, 5000: m5000, 20000: mT}
        printed = (e1, e2, e3)
        print(f"beta={int(beta)} L={L} {tag}: printed exp {e1} {e2} {e3}; printed gamma_lin {gprint}; computed gamma {g:.12f}")
        for (lab, idx, t1, t2), pv in zip(WINDOWS, printed):
            recomp = loc_exp(ms[t1], t1, ms[t2], t2)
            below_g = pv < g
            below_encl = False
            b = int(beta)
            if b in encl:
                lo = Decimal(encl[b][0].numerator) / Decimal(encl[b][0].denominator)
                below_encl = pv < lo
            print(f"  {lab}: printed {pv} recomputed-from-4dp-m {recomp:.6f} below_gamma={below_g} below_encl_lo={below_encl}")
            if below_g or below_encl:
                hits.append(f"{tag} beta={int(beta)} L={L} {lab}={pv} < gamma={g:.8f}")

    n5 = re.search(r"H_t - (\S+) for t <= 150", cache)
    d3 = re.search(r"H_t - (\S+) for t <= 150", cache.split("PASS: D3", 1)[-1] if "PASS: D3" in cache else "")
    if n5 and "per_block" in cache:
        pb = [ln for ln in cache.splitlines() if ln.startswith("per_block:")]
        print(f"N5 per_block: {pb[0] if pb else 'missing'}; D3 constant token {d3.group(1) if d3 else '?'}")

    if hits:
        print("HIT: confirmed - " + "; ".join(hits))
        print("SUMMARY: confirmed exponent mismatch: claim_scope says local exponents above gamma(beta); " + "; ".join(hits))
    else:
        print("SUMMARY: not reproduced - every L>=256 printed local exponent is at or above computed gamma(beta)")


if __name__ == "__main__":
    main()
