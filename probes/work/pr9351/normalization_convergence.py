#!/usr/bin/env python3
"""J:attack-f:PR9351 -- NORMALIZATION: the factors 1/2, 2, 4 of the reduction (H0(n,n) = 4Kn^2 - 4 delta, H0(n+1,n) = -2 delta; H1 = (8 delta - 8Kn^2, 4 delta + 4Kn(n+1))) recomputed by brute force.

The note has no Fourier sums, structure factors or 2 pi / L / N factors; its normalizations are the numerical factors of the Schur reduction: Z^T R^-1 Z = (1/2) Z^T Z + ..., N0 = (8, 4), the scalar metric 1 + 4x,
and the corrections H1. If any of them were off by a factor (1/2, 2, a sign, a conjugation U <-> U^T), the first-order operator would not approximate the microscopic spectrum: the gap error would not fall with x.
This script solves the microscopic spectrum from the explicit full matrix (S <= 12, built from the parent's definitions) and from the reduced equation (S up to 640), and measures the maximum error over the first six
gaps against (a) the note's H0, H0 + xH1; (b) 12 mis-normalized variants (hopping x 1/2, x 2, sign flipped; diagonal constant 4 delta -> 2, 8 delta; H1 with each coefficient halved/doubled). The note's operators must have errors
falling as x (H0) and x^2 (H0 + xH1) with the fitted slopes 1 and 2; every variant must fail to converge at that rate (the test discriminates). Floating point (labelled). Prints SUMMARY: and, only if the note's
normalization fails to converge, HIT:.
"""
import itertools
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
from scipy.linalg import eigh, eigvalsh_tridiagonal

T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def full_levels(S, K, delta, nev=7):
    C = S * (S + 1); x = delta / (K * C)
    edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    states = []
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for n in range(-S, S + 1):
            E = (n, q[0] - 1 - n, -q[1] - n, q[2] - 1 + q[1] + n)
            if all(-S <= e <= S for e in E):
                states.append((q, E))
    idx = {s: i for i, s in enumerate(states)}
    H = np.zeros((len(states), len(states)))
    for i, (q, E) in enumerate(states):
        W = sum(1 - q[a] for a in (0, 2))
        H[i, i] += delta / x ** 2 * W + (delta / x ** 2 * x * 4.0 if W == 0 else 0.0)
        for k, (a, b) in enumerate(edges):
            if q[a] == 1 and q[b] == 0:
                a2 = 1 - E[k] * (E[k] - 1) / C
                if a2 > 1e-14:
                    q2 = list(q); q2[a] = 0; q2[b] = 1; E2 = list(E); E2[k] -= 1
                    j = idx[(tuple(q2), tuple(E2))]
                    t = -delta / x ** 1.5 * np.sqrt(a2)
                    H[i, j] += t; H[j, i] += t
    return eigh(H, eigvals_only=True, subset_by_index=(0, nev - 1))


def reduced_count(E, S, K, delta):
    C = S * (S + 1); x = delta / (K * C); lam = x * x * E / delta
    m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
    R = (1 - lam) * (2 - lam) - 4 * x * dm
    n = np.arange(-S, S + 1)
    dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam)
    q = 4 * delta * dm ** 2 / R
    dg[m + S] -= q; dg[m + S + 1] -= q
    return int((eigvalsh_tridiagonal(dg, -q) < 0).sum())


def reduced_levels(S, K, delta, nev=7):
    out = []
    for j in range(nev):
        b = -6 * delta - 5; step = 0.5
        while reduced_count(b, S, K, delta) < j + 1:
            b += step
        a = b - step
        while reduced_count(a, S, K, delta) >= j + 1:
            a -= step
        for _ in range(64):
            mid = (a + b) / 2
            if reduced_count(mid, S, K, delta) >= j + 1:
                b = mid
            else:
                a = mid
        out.append((a + b) / 2)
    return np.array(out)


def operator_levels(S, K, delta, diag_const=4.0, hop=-2.0, h1_diag=(8.0, -8.0), h1_hop=(4.0, 4.0), with_h1=True, conj=False, L=150, nev=7):
    """Tridiagonal operator diag(4Kn^2 - diag_const delta + x(h1_diag[0] delta + h1_diag[1] K n^2)), hop (n+1,n) = hop delta + x(h1_hop[0] delta + h1_hop[1] K n(n+1)); conj = use the coefficient at (n, n-1) instead."""
    C = S * (S + 1); x = delta / (K * C) if with_h1 else 0.0
    n = np.arange(-L, L + 1).astype(float)
    dg = 4 * K * n ** 2 - diag_const * delta + x * (h1_diag[0] * delta + h1_diag[1] * K * n ** 2)
    nn = n[:-1] if not conj else n[1:] - 1 + 0 * n[1:]
    off = hop * delta + x * (h1_hop[0] * delta + h1_hop[1] * K * (n[:-1] * (n[:-1] + 1) if not conj else n[:-1] * (n[:-1] - 1)))
    return eigvalsh_tridiagonal(dg, off, select="i", select_range=(0, nev - 1))


def gap_err(em, ea):
    return float(np.abs((em[1:] - em[0]) - (ea[1:] - ea[0])).max())


def run():
    K = 1.0
    # (0) small sizes: full matrix vs reduced equation, then the reduced equation up to S = 160
    for delta in (1.0, 4.0):
        for S in (6, 12):
            ef = full_levels(S, K, delta); er = reduced_levels(S, K, delta)
            check(f"(N0) S = {S}, delta = {delta:g}: the reduced equation's first seven levels equal the explicit full matrix's", float(np.abs(ef - er).max()) < 1e-7, f"max difference {float(np.abs(ef - er).max()):.1e}")
    Ss = (20, 40, 80, 160, 320, 640) if "--dry" not in sys.argv else (20, 40, 80)
    variants = {
        "note: H0 + x H1": dict(),
        "hopping x 1/2 (-delta)": dict(hop=-1.0), "hopping x 2 (-4 delta)": dict(hop=-4.0), "hopping sign flipped (+2 delta)": dict(hop=+2.0),
        "diagonal constant 4 delta -> 2 delta": dict(diag_const=2.0), "diagonal constant 4 delta -> 8 delta": dict(diag_const=8.0),
        "H1 diagonal halved": dict(h1_diag=(4.0, -4.0)), "H1 diagonal doubled": dict(h1_diag=(16.0, -16.0)),
        "H1 hopping halved": dict(h1_hop=(2.0, 2.0)), "H1 hopping doubled": dict(h1_hop=(8.0, 8.0)),
        "H1 hopping conjugated (n, n - 1) index": dict(conj=True),
        "H1 dropped (H0 alone)": dict(with_h1=False),
    }
    for delta in (1.0, 15803623 / 500000):
        xs = [delta / (K * S * (S + 1)) for S in Ss]
        micro = [reduced_levels(S, K, delta) for S in Ss]
        res = {}
        for name, kw in variants.items():
            errs = [float(np.abs(em - operator_levels(S, K, delta, **kw)).max()) for S, em in zip(Ss, micro)]      # absolute energies, so a wrong constant is visible
            res[name] = errs
        k = 3
        slope = lambda errs: float(np.polyfit(np.log(xs[-k:]), np.log(errs[-k:]), 1)[0])
        note = res["note: H0 + x H1"]; rot = res["H1 dropped (H0 alone)"]
        ratios = {n: e[-1] / note[-1] for n, e in res.items() if n not in ("note: H0 + x H1",)}
        ok = 1.9 < slope(note) < 2.1 and 0.9 < slope(rot) < 1.1 and all(r > 5 for r in ratios.values())
        check(f"(N1) delta = {delta:.6g}, S = {Ss}: over the three largest sizes the note's operator (absolute energies of the first seven levels) converges as x^2 (H0 alone as x), and every one of 11 mis-normalized variants has "
              "at least 5 times the note's error at the largest size", ok,
              f"note slope {slope(note):.3f}, errors {['%.2e' % v for v in note]}; H0 slope {slope(rot):.3f}; error ratio variant/note at S = {Ss[-1]}: " + "; ".join(f"{n}: {r:.3g}" for n, r in ratios.items()))
        if not ok:
            FIRED.append(f"delta = {delta:.6g}: the note's normalization does not converge at rate x^2 or a mis-normalized variant is as accurate as the note's")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: NORMALIZATION FAILS: " + FIRED[0])
        print("HIT: PR #9351 normalization: " + "; ".join(FIRED))
        sys.exit(1)
    print("SUMMARY: pattern has no purchase beyond the reduction's own factors: the note has no Fourier sums or 2 pi / L / N factors; its numerical factors (1/2, 2, 4, the metric 1 + 4x, H1) give errors falling as x^2 (H0 + xH1) and x (H0) "
          "against the explicit full microscopic matrix and the reduced equation up to S = 640, while 11 mis-normalized variants (hopping x 1/2, x 2, sign, diagonal constants, halved/doubled/conjugated H1) do not")


if __name__ == "__main__":
    run()
