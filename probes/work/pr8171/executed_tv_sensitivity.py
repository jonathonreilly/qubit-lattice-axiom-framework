#!/usr/bin/env python3
"""J:attack:PR8171 - block 27, attack pattern (c) EXECUTED NUMBERS.

Claim_scope/body: TV sensitivity is numerically 1/4 per unit at small |V|,
control max 0.2499 over 300 pairs against 1/(2 sqrt3)=0.2887; A(3 beta) and
(sqrt3 beta)^t printed in the control. This script parses those outputs,
recomputes A, 1/(2 sqrt3) and small-|V| TV by spherical quadrature, and
checks m_t <= (sqrt3 beta)^t on the printed magnetization rows.

HIT if a stated executed number disagrees with the control or the recomputation.
"""
from __future__ import annotations

import math
import re
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path

import numpy as np

getcontext().prec = 40
ROOT = Path(__file__).resolve().parents[3]
HEAD = "15b6e402b902964ada51ffdd8e8c88fb4e472013"
BRANCH = (
    "physics-loop/admissibility-induced-law-block27-unsoldered-formation-law-weak-coupling-"
    "causal-coupling-contracts-20260916"
)
CTRL = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block27.out.txt"
)
REF = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block27_refuter.out.txt"
)
PI = Decimal("3.141592653589793238462643383279502884197")


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def A(k: Decimal) -> Decimal:
    t = (2 * k).exp()
    coth = (t + 1) / (t - 1)
    return coth - 1 / k


def tv_small(eps=Decimal("0.01")) -> float:
    """Quadrature TV(uniform, K_{eps e_3}) / eps."""
    n_th, n_ph = 80, 160
    th = np.linspace(0, np.pi, n_th + 1)
    thc = 0.5 * (th[1:] + th[:-1])
    dth = th[1] - th[0]
    dph = 2 * np.pi / n_ph
    k = float(eps)
    f0 = 1 / (4 * np.pi)
    f = (k / (4 * np.pi * math.sinh(k))) * np.exp(k * np.cos(thc))
    w = np.sin(thc) * dth * 2 * np.pi  # phi-integrated
    return float(0.5 * np.sum(np.abs(f - f0) * w) / k)


def main() -> None:
    ctrl = show(CTRL)
    ref = show(REF)
    hits = []

    bound = 1 / (2 * Decimal(3).sqrt())
    print(f"1/(2 sqrt3) = {bound:.10f} (stated 0.2887)")
    if abs(float(bound) - 0.2887) > 5e-5:
        hits.append(f"1/(2 sqrt3) {float(bound):.6f} vs stated 0.2887")

    m = re.search(r"max TV/\|V - V'\| over 300 random pairs = ([0-9.]+); bound 1/\(2 sqrt3\) = ([0-9.]+); the small-\|V\| value 1/4", ctrl)
    if not m:
        hits.append("control TV line not found")
    else:
        mx, bd = Decimal(m.group(1)), Decimal(m.group(2))
        print(f"control max {mx} bound {bd}")
        if mx > bound + Decimal("0.00005"):
            hits.append(f"control max {mx} exceeds 1/(2 sqrt3)={bound:.6f}")
        if abs(bd - Decimal("0.2887")) > Decimal("0.00005"):
            hits.append(f"control printed bound {bd} vs 0.2887")
        if mx > Decimal("0.25") + Decimal("0.001"):
            hits.append(f"control max {mx} exceeds stated small-|V| 1/4 beyond 0.001")

    small = tv_small()
    print(f"quadrature small-|V| TV/|V| = {small:.6f} (stated 1/4)")
    if abs(small - 0.25) > 5e-4:
        hits.append(f"quadrature small-V Lip {small:.6f} vs 1/4")

    rm = re.search(r"max TV/\|V - V'\| = ([0-9.]+) against the bound ([0-9.]+)", ref)
    if rm:
        rmx, rbd = Decimal(rm.group(1)), Decimal(rm.group(2))
        print(f"refuter max {rmx} bound {rbd}")
        if rmx > bound + Decimal("0.001"):
            hits.append(f"refuter max {rmx} exceeds 1/(2 sqrt3)")

    for beta in (Decimal("0.3"), Decimal("0.5")):
        a = A(3 * beta)
        cm = re.search(rf"beta={beta}: m_t = \[([^\]]+)\].*A\(3beta\) = ([0-9.]+)", ctrl)
        if not cm:
            hits.append(f"magnetization line missing for beta={beta}")
            continue
        printed_A = Decimal(cm.group(2))
        print(f"beta={beta}: A(3beta) printed {printed_A} recomputed {a:.6f}")
        if abs(printed_A - a) > Decimal("0.00015"):
            hits.append(f"A(3beta) beta={beta} printed {printed_A} vs {a:.6f}")
        if a > beta:
            hits.append(f"A(3beta)={a:.6f} > beta={beta} (T3)")
        nums = [Decimal(x.replace("np.float64(", "").replace(")", "")) for x in cm.group(1).split(",")]
        s3b = Decimal(3).sqrt() * beta
        for t, mt in enumerate(nums, start=1):
            bound_t = s3b ** t
            print(f"  t={t} m={mt} (sqrt3 beta)^t={bound_t:.4f}")
            if mt > bound_t + Decimal("0.01"):
                hits.append(f"beta={beta} t={t} m_t={mt} > (sqrt3 beta)^t={bound_t:.4f}")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; control max 0.2499, bound 0.2887, "
            "small-|V| 1/4, A(3beta) and m_t <= (sqrt3 beta)^t all match the controls and exact recomputation"
        )


if __name__ == "__main__":
    main()
