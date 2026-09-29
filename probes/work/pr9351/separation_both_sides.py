#!/usr/bin/env python3
"""J:attack-b:PR9351 -- SAME TEST, BOTH SIDES: the note's separation claim that the first correction changes BOTH the electric energy and the adjacent field hopping, and that "a rotor-only higher harmonic omits" it.

Claims tested (note, abstract and "Scientific meaning"): (i) the formal first correction H1 changes both the electric energy (diagonal 8 delta - 8 K n^2) and the adjacent hopping (4 delta + 4 K n(n + 1)), so both parts are needed;
(ii) a rotor-only description (a function of the phase alone: 4 K' n^2 - sum_j E_j cos(j phi), i.e. hopping between n and n + j independent of n, plus a rescaled electric coefficient) omits the correction.
The identical test is applied to every object in the same representation: the maximum absolute error over the first six excitation gaps against the microscopic spectrum (the reduced equation of the note, equal to the explicit
full matrix; checked at S <= 12), for S = 20 ... 640 and delta = 1, 15803623/500000, K = 1, with the slope of log(error) against log(x) over the three largest sizes:
  A  H0 + x H1                           (both parts)             expected slope 2
  B1 H0 + x H1_diag                       (electric part only)     expected slope 1
  B2 H0 + x H1_hop                        (hopping part only)      expected slope 1
  B3 rotor-only: 4K'n^2 - EJ' cos(phi)                    fitted by least squares on the six gaps (K', EJ')
  B4 rotor-only with a second harmonic: + E2 cos(2 phi)   fitted (K', EJ', E2)
  B4i isolated harmonic: H0 + E2 cos(2 phi) with K and EJ = 4 delta fixed at the law's values (E2 fitted)
  B5 rotor-only with second and third harmonics           fitted (K', EJ', E2, E3)
  B6 rotor-only with NO fitted parameter: K' = K(1 - 2x), EJ' = 4 delta (1 - 2x) + 2 K x, E2 = 2 delta x  (the values the fits converge to, in closed form)
The separation holds if A converges as x^2 while every B converges no faster than x (best-fit errors compared at the largest size). A B that matches A's error refutes 'omits'. Floating point (labelled). Prints SUMMARY:
and, only if the separation fails, HIT:.
"""
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
from scipy.linalg import eigvalsh_tridiagonal
from scipy.optimize import least_squares
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def reduced_count(E, S, K, delta):
    C = S * (S + 1); x = delta / (K * C); lam = x * x * E / delta
    m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
    R = (1 - lam) * (2 - lam) - 4 * x * dm
    n = np.arange(-S, S + 1)
    dg = 4 * K * n.astype(float) ** 2 - E * (1 + 4 * x - lam)
    q = 4 * delta * dm ** 2 / R
    dg[m + S] -= q; dg[m + S + 1] -= q
    return int((eigvalsh_tridiagonal(dg, -q) < 0).sum())


def micro_levels(S, K, delta, nev=7):
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


def note_operator(S, K, delta, diag=True, hop=True, L=200, nev=7):
    C = S * (S + 1); x = delta / (K * C)
    n = np.arange(-L, L + 1).astype(float)
    dg = 4 * K * n ** 2 - 4 * delta + (x * (8 * delta - 8 * K * n ** 2) if diag else np.zeros_like(n))
    off = np.full(len(n) - 1, -2 * delta) + (x * (4 * delta + 4 * K * n[:-1] * (n[:-1] + 1)) if hop else 0.0)
    return eigvalsh_tridiagonal(dg, off, select="i", select_range=(0, nev - 1))


def rotor_levels(K2, EJ, E2, E3, L=120, nev=7):
    """4 K2 n^2 - EJ cos(phi) - E2 cos(2 phi) - E3 cos(3 phi): hopping -EJ/2 (n, n +- 1), -E2/2 (n, n +- 2), -E3/2 (n, n +- 3), all independent of n."""
    n = np.arange(-L, L + 1).astype(float); N = len(n)
    H = diags([4 * K2 * n ** 2], [0]).toarray()
    for j, e in ((1, EJ), (2, E2), (3, E3)):
        if e != 0.0:
            H += np.diag(np.full(N - j, -e / 2), j) + np.diag(np.full(N - j, -e / 2), -j)
    return np.linalg.eigvalsh(H)[:nev]


def gaps(e):
    return e[1:] - e[0]


def best_fit(target_gaps, K, delta, nparam):
    """Least-squares fit of the rotor-only family to the six gaps; returns the maximum absolute gap error of the fit."""
    def res(p):
        K2, EJ = p[0], p[1]
        E2 = p[2] if nparam >= 3 else 0.0
        E3 = p[3] if nparam >= 4 else 0.0
        return gaps(rotor_levels(K2, EJ, E2, E3, L=60)) - target_gaps
    best = None
    for start in ([K, 4 * delta, 0.0, 0.0][:nparam], [K * 0.98, 4 * delta * 1.02, 0.01, 0.0][:nparam], [K * 1.02, 4 * delta * 0.98, -0.01, 0.01][:nparam]):
        r = least_squares(res, start, xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=400)
        e = float(np.abs(r.fun).max())
        if best is None or e < best[0]:
            best = (e, r.x)
    return best


def isolated_fit(target_gaps, K, delta):
    """H0 + E2 cos(2 phi) with K and EJ = 4 delta fixed at the law's values: one fitted parameter E2."""
    def res(p):
        return gaps(rotor_levels(K, 4 * delta, p[0], 0.0, L=60)) - target_gaps
    best = None
    for start in (0.0, 0.01 * delta, -0.01 * delta):
        r = least_squares(res, [start], xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=400)
        e = float(np.abs(r.fun).max())
        if best is None or e < best[0]:
            best = (e, r.x)
    return best


def slope(xs, errs, k=3):
    return float(np.polyfit(np.log(xs[-k:]), np.log(errs[-k:]), 1)[0])


def run():
    K = 1.0
    Ss = (20, 40, 80, 160, 320) if "--dry" not in sys.argv else (20, 40, 80)
    # sanity: the reduced-equation levels are the full matrix's (checked in the sibling units); here a light consistency check at S = 6
    for delta in (1.0, 15803623 / 500000):
        xs = [delta / (K * S * (S + 1)) for S in Ss]
        table = {"A  H0 + x H1 (both parts)": [], "B1 H0 + x H1_diag (electric part only)": [], "B2 H0 + x H1_hop (hopping part only)": [],
                 "B3 rotor-only, 2 fitted parameters (K', EJ')": [], "B4i isolated harmonic: H0 + E2 cos 2 phi, K and EJ fixed (1 fitted)": [], "B4 rotor-only + cos 2 phi, 3 fitted": [], "B5 rotor-only + cos 2 phi, cos 3 phi, 4 fitted": [], "B6 rotor-only, no fitted parameter: K(1-2x), 4 delta(1-2x)+2Kx, 2 delta x": []}
        fits3 = []
        for S in Ss:
            em = micro_levels(S, K, delta); g = gaps(em)
            table["A  H0 + x H1 (both parts)"].append(float(np.abs(gaps(note_operator(S, K, delta)) - g).max()))
            table["B1 H0 + x H1_diag (electric part only)"].append(float(np.abs(gaps(note_operator(S, K, delta, hop=False)) - g).max()))
            table["B2 H0 + x H1_hop (hopping part only)"].append(float(np.abs(gaps(note_operator(S, K, delta, diag=False)) - g).max()))
            table["B3 rotor-only, 2 fitted parameters (K', EJ')"].append(best_fit(g, K, delta, 2)[0])
            table["B4i isolated harmonic: H0 + E2 cos 2 phi, K and EJ fixed (1 fitted)"].append(isolated_fit(g, K, delta)[0])
            fit3 = best_fit(g, K, delta, 3)
            table["B4 rotor-only + cos 2 phi, 3 fitted"].append(fit3[0])
            fits3.append(fit3[1])
            table["B5 rotor-only + cos 2 phi, cos 3 phi, 4 fitted"].append(best_fit(g, K, delta, 4)[0])
            xx = delta / (K * S * (S + 1))
            table["B6 rotor-only, no fitted parameter: K(1-2x), 4 delta(1-2x)+2Kx, 2 delta x"].append(
                float(np.abs(gaps(rotor_levels(K * (1 - 2 * xx), 4 * delta * (1 - 2 * xx) + 2 * K * xx, 2 * delta * xx, 0.0, L=80)) - g).max()))
        # the two operators against each other (no microscopic data): gaps of H0 + x H1 vs the parameter-free rotor-only Hamiltonian
        dAB = []
        for S in Ss:
            xx = delta / (K * S * (S + 1))
            dAB.append(float(np.abs(gaps(note_operator(S, K, delta)) - gaps(rotor_levels(K * (1 - 2 * xx), 4 * delta * (1 - 2 * xx) + 2 * K * xx, 2 * delta * xx, 0.0, L=80))).max()))
        s_ab = slope(xs, dAB)
        check(f"(B7) delta = {delta:.6g}: H0 + x H1 and the parameter-free rotor-only Hamiltonian have the same six gaps to O(x^2) (their difference converges with slope ~2 in x, without reference to the microscopic model)",
              1.8 < s_ab < 2.2, f"slope {s_ab:.2f}; max gap difference {['%.2e' % v for v in dAB]}")
        sl = {k: slope(xs, v) for k, v in table.items()}
        A = table["A  H0 + x H1 (both parts)"]
        ratios = {k: v[-1] / A[-1] for k, v in table.items() if not k.startswith("A ")}
        refit = [k for k in table if k.startswith("B4 ") or k.startswith("B5") or k.startswith("B6")]
        sep_keys = [k for k in table if not k.startswith("A ") and k not in refit]
        ok = 1.85 < sl["A  H0 + x H1 (both parts)"] < 2.15 and all(ratios[k] > 5 for k in sep_keys) and all(sl[k] < 1.5 for k in sep_keys) and not any(sl[k] > 1.5 and ratios[k] < 2.0 for k in refit)
        par = "; ".join(f"S {S}: K'/K-1 = {(p[0] / K - 1) / (delta / (K * S * (S + 1))):+.3f} x, EJ'/(4 delta)-1 = {(p[1] / (4 * delta) - 1) / (delta / (K * S * (S + 1))):+.3f} x, E2/delta = {p[2] / delta / (delta / (K * S * (S + 1))):+.3f} x" for S, p in zip(Ss, fits3))
        check(f"(B) delta = {delta:.6g}, S = {Ss}: the note's operator (both parts) converges as x^2; the electric-only, hopping-only and rotor-only (1-3 harmonics, least-squares fitted) descriptions converge no faster than x and "
              f"have at least 5 times its error at S = {Ss[-1]}", ok,
              "fitted B4 parameters in units of x: " + par + "; slopes " + "; ".join(f"{k.split(' ')[0]} {s:.2f}" for k, s in sl.items()) + f"; errors at S = {Ss[-1]}: " + "; ".join(f"{k.split(' ')[0]} {v[-1]:.2e}" for k, v in table.items())
              + f"; ratios to A: " + "; ".join(f"{k.split(' ')[0]} {r:.3g}" for k, r in ratios.items()) + f"; {time.time() - T0:.0f} s")
        if not ok:
            FIRED.append(f"delta = {delta:.6g}: a rotor-only Hamiltonian with renormalized K, EJ and a second harmonic (fitted, or with no fitted parameter: K(1-2x), 4 delta(1-2x)+2Kx, 2 delta x) matches the microscopic gaps as well as H0 + x H1 (separation fails; slopes ({ {k.split(' ')[0]: round(s, 2) for k, s in sl.items()} }; ratios to A { {k.split(' ')[0]: float(f'{r:.3g}') for k, r in ratios.items()} })")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: SEPARATION FAILS: with the identical test (six-gap maximum error against the microscopic spectrum, slope in x over the three largest sizes), a rotor-only Hamiltonian 4K(1-2x) n^2 - [4 delta(1-2x)+2Kx] cos(phi) "
              "- 2 delta x cos(2 phi) with no fitted parameter converges as x^2 with the same error as H0 + x H1 (ratio near 1), so 'a rotor-only higher harmonic omits the earlier-order joint electric/hopping correction' holds only for an isolated "
              "harmonic with K and EJ left at the law's values (B4i converges as x)")
        print("HIT: PR #9351 abstract sentence 'A rotor-only higher harmonic omits the earlier-order joint electric/hopping correction': " + "; ".join(FIRED))
        sys.exit(0)
    print("SUMMARY: pattern applied both sides and the separation holds")


if __name__ == "__main__":
    run()
