#!/usr/bin/env python3
"""Referee for kernel-normalization-puzzle a2.

Author w-jonathonsmac4f50-j7bbc (claude-opus-5). Own lattice sum and own shell census.
The Monte Carlo table is the author's; it was not re-run. The sign claim does not follow from it.
"""
import numpy as np
import mpmath as mp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def prediction():
    L, n = 48, 4
    mp.mp.dps = 30
    k = 2 * np.pi * np.arange(L) / L
    K = np.meshgrid(k, k, k, indexing="ij")
    phi = (1 + sum(np.exp(1j * x) for x in K)) / n
    u = np.abs(phi) ** 2
    mask = np.ones(u.shape, bool)
    mask[0, 0, 0] = False
    W = mp.mpf((1.0 / (1 - u[mask])).sum()) / L ** 3
    rows = {}
    for beta in (2, 6, 24):
        x = mp.mpf(n * beta)
        s2 = (mp.coth(x) - 1 / x) / x
        rows[beta] = (s2, 1 + s2 * (2 - W))
    ok = (
        abs(W - mp.mpf("1.762474")) < mp.mpf("1e-6")
        and abs(rows[2][0] - mp.mpf("0.109375")) < mp.mpf("1e-6")
        and abs(rows[6][1] - mp.mpf("1.009485")) < mp.mpf("1e-6")
        and abs(rows[2][1] - mp.mpf("1.025979")) < mp.mpf("1e-6")
        and abs(rows[24][1] - mp.mpf("1.002448")) < mp.mpf("1e-6")
    )
    report(
        "step1 prediction",
        ok,
        f"W={float(W):.6f}; R=1+sigma^2(2-W) is 1.025979, 1.009485, 1.002448 at beta=2,6,24",
    )


def shells():
    L = 48
    n = np.arange(L)
    nf = np.where(n <= L // 2, n, n - L).astype(float)
    k = 2 * np.pi * nf / L
    kk = np.stack(np.meshgrid(k, k, k, indexing="ij"), -1)
    radius = np.sqrt((kk ** 2).sum(-1))
    edges = [0, 0.3, 0.6, 1.0, 1.5, 2.2, 3.2, 6.0]
    counts = []
    for a, b in zip(edges, edges[1:]):
        counts.append(int(((radius >= a) & (radius < b) & (radius > 0)).sum()))
    report(
        "step2 mode counts",
        counts == [56, 380, 1426, 4492, 13578, 41209, 49450] and sum(counts) == L ** 3 - 1,
        "lowest shell 56 modes, top shell 49450, and the bins partition every nonzero mode",
    )


def sign_claim():
    lows = [0.9846, 1.0132, 1.0613]
    mean = sum(lows) / 3
    sd = (sum((x - mean) ** 2 for x in lows) / 2) ** 0.5
    se = sd / 3 ** 0.5
    # a3 asked for a standard error below 0.02. This sample does not clear 1.
    below = sum(1 for x in lows if x < 1)
    settled = se < 0.02 and mean - se > 1 and below == 0
    report(
        "step3 not below 1",
        settled,
        f"mean {mean:.4f}, sample s.d. {sd:.4f}, s.e. {se:.4f}; one of three seeds is {lows[0]} < 1, "
        f"and (mean-1)/s.e. = {(mean - 1) / se:.2f}, so the shell is not shown to sit above 1",
    )


def main():
    prediction()
    shells()
    sign_claim()
    if fails:
        print(
            "SUMMARY: fails at step 3 - three seeds give a standard error 0.022 on the lowest shell, "
            "one seed is 0.9846, and the mean is not resolved above 1"
        )
        return
    print("SUMMARY: confirmed")


if __name__ == "__main__":
    main()
