#!/usr/bin/env python3
"""J:attack:PR8170 - block 26, attack pattern (c) EXECUTED NUMBERS.

Claim_scope: the nonlinear law on planes up to 512x512 at beta=3,6,12,24
loses magnetization 'at local exponents above gamma(beta)'. This script
parses supervisor_control_block26_fit.out.txt as Decimal columns, recomputes
gamma(beta)=(3 sqrt(3)/(4 pi)) A(3 beta)/(3 beta) from A=coth-1/kappa in
Decimal, and compares printed exp[t1,t2] (and log-ratio from printed m) to
that gamma. Also checks the runner N5 per_block constant against D3.

HIT if a large-L printed local exponent sits below gamma(beta), or N5 disagrees
with D3.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 50
ROOT = Path(__file__).resolve().parents[3]
HEAD = "f9e1177003afa991ec87831d2be70611068a09ab"
BRANCH = (
    "physics-loop/admissibility-induced-law-block26-unsoldered-formation-law-level-time-"
    "gain-one-spin-waves-memory-decay-20260916"
)
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


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def coth(x: Decimal) -> Decimal:
    t = (2 * x).exp()
    return (t + 1) / (t - 1)


def gamma_of(beta: Decimal) -> Decimal:
    A = coth(3 * beta) - 1 / (3 * beta)
    return (3 * Decimal(3).sqrt() / (4 * PI)) * A / (3 * beta)


def parse_fit(text: str):
    rows = []
    for line in text.splitlines():
        p = line.split()
        if len(p) < 11:
            continue
        try:
            beta, L, T = Decimal(p[0]), int(p[1]), int(p[2])
            m500, m5000, mT = Decimal(p[3]), Decimal(p[4]), Decimal(p[5])
            e1, e2, e3 = Decimal(p[6]), Decimal(p[7]), Decimal(p[8])
        except Exception:
            continue
        if beta not in (Decimal(3), Decimal(6), Decimal(12), Decimal(24)):
            continue
        if any(v.is_nan() for v in (e1, e2, e3)):
            continue
        rows.append((beta, L, T, m500, m5000, mT, e1, e2, e3, p[10]))
    return rows


def main() -> None:
    note = show(NOTE)
    fit = show(FIT)
    cache = show(CACHE)
    fm = note.split("\n---\n", 1)[0]
    if "at local exponents above gamma(beta)" not in fm.replace("\n", " "):
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; claim_scope exponent sentence not found")
        return

    hits = []
    rows = [r for r in parse_fit(fit) if r[1] >= 256 and r[2] == 20000]
    print(f"large-L fit rows: {len(rows)}")
    for beta, L, T, m500, m5000, mT, e1, e2, e3, tag in rows:
        g = gamma_of(beta)
        print(f"beta={int(beta)} L={L} {tag}: exp {e1} {e2} {e3}; gamma={g:.8f}")
        for lab, pv in (("exp[500,5000]", e1), ("exp[5000,T]", e2), ("exp[500,T]", e3)):
            if pv < g:
                hits.append(f"{tag} beta={int(beta)} L={L} {lab}={pv} < gamma={g:.8f}")

    pb = next((ln for ln in cache.splitlines() if ln.startswith("per_block:")), "")
    d3 = re.search(r"H_t - (\S+) for t <= 150", cache.split("PASS: D3", 1)[-1] if "PASS: D3" in cache else "")
    n5 = re.search(r"H_t - (\S+) for t <= 150", pb)
    print(f"N5 per_block token {n5.group(1) if n5 else '?'}; D3 token {d3.group(1) if d3 else '?'}")
    if n5 and d3 and n5.group(1) != d3.group(1):
        hits.append(f"N5 per_block prints H_t - {n5.group(1)} against D3 H_t - {d3.group(1)}")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; every large-L printed exponent is at or above Langevin gamma(beta)")


if __name__ == "__main__":
    main()
