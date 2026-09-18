#!/usr/bin/env python3
"""J:attack:PR8155 - block 21, attack pattern (c) EXECUTED NUMBERS.

Recompute alpha=2 sqrt(3) beta, the uniqueness threshold beta=sqrt(3)/6,
coefficient ratios 6/(n(2n-1)) and 3/(2n+1), L(x)/x -> 1/3, artanh(1/6),
and antipodal TV=tanh(beta/2) against supervisor_control_block21_weak_coupling.

HIT if a stated executed number disagrees with the control or the exact value.
"""
from __future__ import annotations

import math
import re
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "c286f2fc6ad4dc94562c1e1e1aa3f85f850f8a9a"
BRANCH = (
    "physics-loop/admissibility-induced-law-block21-unsoldered-sphere-static-law-weak-coupling-"
    "uniqueness-exponential-decay-20260915"
)
CTRL = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block21_weak_coupling.out.txt"
)


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    hits = []
    ctrl = show(CTRL)

    # threshold arithmetic
    s3 = math.sqrt(3)
    bc = s3 / 6
    bc2 = 1 / (2 * s3)
    print(f"sqrt(3)/6 = {bc:.12f}; 1/(2 sqrt3) = {bc2:.12f}")
    if abs(bc - bc2) > 1e-15:
        hits.append("sqrt(3)/6 != 1/(2 sqrt3)")
    if not (bc > 0.28):
        hits.append(f"sqrt(3)/6={bc} not > 28/100")

    # alpha = 2 sqrt(3) beta = 6 beta / sqrt(3)
    for beta in (0.1, F(1, 8)):
        b = float(beta)
        a1 = 2 * s3 * b
        a2 = 6 * b / s3
        print(f"beta={beta}: alpha={a1:.6f} vs 6b/sqrt3={a2:.6f}")
        if abs(a1 - a2) > 1e-12:
            hits.append(f"alpha identity fail at beta={beta}")

    # ratios 6/(n(2n-1)) for n=2..7
    stated = [F(1), F(2, 5), F(3, 14), F(2, 15), F(1, 11), F(6, 91)]
    for n, st in zip(range(2, 8), stated):
        got = F(6, n * (2 * n - 1))
        print(f"n={n}: 6/(n(2n-1))={got} stated {st}")
        if got != st:
            hits.append(f"ratio n={n} {got} != {st}")

    # 3/(2n+1) for n=1..6
    stated2 = [F(1), F(3, 5), F(3, 7), F(1, 3), F(3, 11), F(3, 13)]
    for n, st in zip(range(1, 7), stated2):
        got = F(3, 2 * n + 1)
        print(f"n={n}: 3/(2n+1)={got} stated {st}")
        if got != st:
            hits.append(f"L/x ratio n={n} {got} != {st}")

    m = re.search(r"artanh\(1/6\) = ([0-9.]+); \(1/2\) log\(7/5\) = ([0-9.]+); 6 tanh\(b0\) = ([0-9.]+)", ctrl)
    if m:
        at, lg, six = map(float, m.groups())
        exact_at = math.atanh(1 / 6)
        exact_lg = 0.5 * math.log(7 / 5)
        print(f"artanh(1/6) control {at} exact {exact_at:.6f}; (1/2)log(7/5) {lg} exact {exact_lg:.6f}")
        if abs(at - exact_at) > 5e-6 or abs(lg - exact_lg) > 5e-6:
            hits.append("artanh(1/6) mismatch")
        if abs(six - 1.0) > 5e-6:
            hits.append(f"6 tanh(b0)={six} != 1")
        if abs(exact_at - bc) > 0.02:
            # artanh(1/6) is a different route's threshold, not sqrt(3)/6
            print(f"  artanh(1/6)={exact_at:.6f} vs sqrt(3)/6={bc:.6f} (distinct routes)")
    else:
        hits.append("artanh line missing from control")

    # antipodal TV vs tanh(beta/2)
    for beta, tv_st in ((0.1, 0.05), (0.5, 0.2449), (1.0, 0.4621)):
        th = math.tanh(beta / 2)
        print(f"beta={beta}: tanh(beta/2)={th:.4f} control TV~{tv_st}")
        if abs(th - tv_st) > 0.00015:
            hits.append(f"tanh(beta/2) {th:.4f} vs control TV {tv_st} at beta={beta}")

    # L(x)/x = 1/3 - x^2/45 + ... so the x=0 value is 1/3 exactly
    from decimal import Decimal, getcontext

    getcontext().prec = 50
    x = Decimal("1e-8")
    t = (2 * x).exp()
    coth = (t + 1) / (t - 1)
    Lx = (coth - 1 / x) / x
    print(f"L(x)/x at x=1e-8: {Lx:.10f} (stated 1/3)")
    if abs(Lx - Decimal(1) / 3) > Decimal("1e-10"):
        hits.append(f"L/x at 0 {Lx} != 1/3")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; sqrt(3)/6 threshold, alpha=2 sqrt(3) beta, "
            "coefficient ratios 6/(n(2n-1)) and 3/(2n+1), artanh(1/6), antipodal tanh(beta/2) "
            "and L/x=1/3 all match the control and exact arithmetic"
        )


if __name__ == "__main__":
    main()
