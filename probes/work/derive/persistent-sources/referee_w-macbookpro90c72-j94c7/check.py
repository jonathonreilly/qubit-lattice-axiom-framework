#!/usr/bin/env python3
"""Referee for persistent-sources a4.

Author w-jonathonsmac4f50-jd96c (claude-opus-5). Own reduction of the published grid
and one live rerun. The other 29 simulator runs were not repeated.
"""
import os
import subprocess
import sys
import mpmath as mp
import sympy as sp

fails = []
mp.mp.dps = 25
DATA = {
    (1, "0.125"): {1: 0.9501, 2: 0.8993, 3: 0.9631},
    (1, "0.5"): {1: 0.9638, 2: 0.9135, 3: 0.9571},
    (2, "0.125"): {1: 0.9779, 2: 0.9666, 3: 0.9766},
    (2, "0.5"): {1: 0.9789, 2: 0.9647, 3: 0.9732},
    (3, "0.125"): {1: 0.9855, 2: 0.9782, 3: 0.9845},
    (3, "0.5"): {1: 0.9862, 2: 0.9774, 3: 0.9829},
    (6, "0.125"): {1: 0.9927, 2: 0.9892, 3: 0.9922},
    (6, "0.5"): {1: 0.9930, 2: 0.9890, 3: 0.9917},
    (12, "0.125"): {1: 0.9962, 2: 0.9945, 3: 0.9960},
    (12, "0.5"): {1: 0.9963, 2: 0.9945, 3: 0.9958},
}
BETAS = (1, 2, 3, 6, 12)


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def identity():
    x = sp.symbols("x", positive=True)
    exact = (sp.coth(x) - 1 / x) / x
    claim = 1 / x - 1 / x ** 2 + 2 * sp.exp(-2 * x) / (x * (1 - sp.exp(-2 * x)))
    report(
        "sigma identity",
        sp.simplify((exact - claim).rewrite(sp.exp)) == 0,
        "A(x)/x = 1/x - 1/x^2 + 2 e^{-2x}/(x(1-e^{-2x}))",
    )


def grid():
    def sig2(b):
        x = 7 * mp.mpf(b)
        return (mp.coth(x) - 1 / x) / x

    gaps = []
    for b in BETAS:
        if b < 2:
            continue
        for s in (1, 2, 3):
            gaps.append(abs(DATA[(b, "0.125")][s] - DATA[(b, "0.5")][s]))
    cs = {}
    for s in (1, 2, 3):
        row = []
        for b in BETAS:
            ratio = (DATA[(b, "0.125")][s] + DATA[(b, "0.5")][s]) / 2
            row.append((1 - mp.mpf(ratio)) / sig2(b))
        cs[s] = row
    flat = max(max(cs[s][2:]) - min(cs[s][2:]) for s in (1, 2, 3))
    across = max(
        max(cs[s][i] for s in (1, 2, 3)) - min(cs[s][i] for s in (1, 2, 3)) for i in range(2, 5)
    )
    plateau = {s: sum(cs[s][2:]) / 3 for s in (1, 2, 3)}
    mean = sum(plateau.values()) / 3
    pred_ok = True
    for b, quoted in ((3, "0.04535"), (6, "0.02324"), (12, "0.01176")):
        pred_ok &= abs(sig2(b) - mp.mpf(quoted)) < mp.mpf("0.00002")
    report(
        "grid arithmetic",
        max(gaps) < 0.004 and flat < mp.mpf("0.025") and across > 3 * flat and pred_ok and abs(mean - mp.mpf("0.39")) < mp.mpf("0.03"),
        f"h-split at beta>=2 is at most {max(gaps):.4f}; within-seed spread {float(flat):.3f}; across-seed {float(across):.3f}; mean plateau {float(mean):.3f}",
    )


def rerun():
    lib = os.path.join(os.getcwd(), "probes", "lib")
    if not os.path.isfile(os.path.join(lib, "formation_response.py")):
        report("live point", False, "formation_response.py is not in this checkout")
        return
    proc = subprocess.run(
        [sys.executable, "formation_response.py", "3s", "6", "32", "2000", "800", "0.125", "1"],
        capture_output=True,
        text=True,
        cwd=lib,
    )
    got = None
    for line in proc.stdout.splitlines():
        for tok in line.split():
            if tok.startswith("mean_ratio_r1to4="):
                got = float(tok.split("=")[1])
    report(
        "live point",
        got is not None and abs(got - 0.9927) < 1e-4,
        f"beta=6, h=0.125, seed 1 gives {got}",
    )


def main():
    identity()
    grid()
    rerun()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the deviation scales as sigma^2 = A(7 beta)/(7 beta), not with the source strength. "
        "On the published grid the two field strengths differ by at most 0.0034 for beta>=2, "
        "and within a seed the coefficient is flat from beta=3 to 12 while the seeds disagree. "
        "The mean plateau is about 0.39. One cell, beta=6 and h=0.125 and seed 1, reruns to 0.9927."
    )
    print(
        "SUMMARY: confirmed the sigma identity, the arithmetic of the thirty published ratios, and one live rerun. "
        "The other twenty-nine simulator runs were not repeated, so the seed interval is that grid's. "
        "The prose bound 0.0006 is smaller than the table."
    )


if __name__ == "__main__":
    main()
