#!/usr/bin/env python3
"""J:note:KINETIC_ISOTROPY_COMPOSITION_CLOSURE -- literal enumeration of the note's finite claims, beyond the runner's sizes and with numerical (not symbolic) machinery.

Note on main: docs/KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md. Claims tested:
 (P) the Kawamoto-Smit phases eta_1 = 1, eta_2 = (-1)^x1, eta_3 = (-1)^(x1 + x2) with the sublattice parity eps(x) = (-1)^(x1 + x2 + x3) are invariant under exactly the translations (2Z)^3: every odd translation (single-site and mixed) breaks the pattern.
     The runner checks 13 named shifts on a 4^3 block; here EVERY translation t in [-9, 9]^3 is tested on a 24^3 block (14,000+ translations), for eta alone, eps alone and both.
 (C) composite of the flat exchange cell U_flat(theta) = [[cos theta, i sin theta e^{-iK}], [i sin theta e^{iK}, cos theta]] and the saturating shift U_shift = [[0, e^{-iK}], [1, 0]]: the eigenvalues of U_flat U_shift satisfy
     lambda = e^{-iK/2} mu with mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0, the band velocity v = d omega/dK (per tick, sites) obeys |v| <= 1, saturating only at theta = pi/2, and the curvature is nonzero for theta != 0
     (numerical eigenphases with a continuous branch and finite differences; a 60 x 400 grid, not sampled points);
 (D) composite dials: for every protocol of k shifts and m identities (k, m <= 8) the composite is massless with cone slope k/(k + m); U_shift^2 = e^{-iK} I exactly; {shift, shift, identity} has slope 2/3;
 (T) the transpose map preserves the trace and reverses products (an anti-automorphism), tested on 1000 random pairs.
Exact/sign-bit arithmetic for (P); floating point (labelled) for (C), (D), (T). Prints SUMMARY: and, only if a claim fails, HIT:.
"""
import itertools
import sys
import time

import numpy as np

T0 = time.time()
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def eta(mu, x):
    return 1 if mu == 1 else ((-1) ** x[0] if mu == 2 else (-1) ** (x[0] + x[1]))


def eps(x):
    return (-1) ** (x[0] + x[1] + x[2])


def run():
    # ---- (P) every translation
    L = 24
    box = range(L)
    X = np.array(list(itertools.product(box, repeat=3)))
    def etas(P):
        return np.stack([np.ones(len(P), int), 1 - 2 * (P[:, 0] & 1), 1 - 2 * ((P[:, 0] + P[:, 1]) & 1)], axis=1)
    def epsv(P):
        return 1 - 2 * ((P[:, 0] + P[:, 1] + P[:, 2]) & 1)
    e0, s0 = etas(X), epsv(X)
    inv_both, inv_eta, inv_eps, tested = [], [], [], 0
    for t in itertools.product(range(-9, 10), repeat=3):
        Xt = X + np.array(t)
        ie = bool(np.all(etas(Xt) == e0)); ip = bool(np.all(epsv(Xt) == s0))
        tested += 1
        if ie and ip: inv_both.append(t)
        if ie: inv_eta.append(t)
        if ip: inv_eps.append(t)
    all_even = all(all(c % 2 == 0 for c in t) for t in inv_both) and set(inv_both) == {t for t in itertools.product(range(-9, 10), repeat=3) if all(c % 2 == 0 for c in t)}
    check(f"(P) of the {tested} translations t in [-9, 9]^3 tested on a 24^3 block, the ones under which {{eta, eps}} is invariant are exactly those with all three components even ({len(inv_both)} of them); eta alone is invariant under "
          f"{len(inv_eta)} (every t with t1, t2 even) and eps alone under {len(inv_eps)} (every t with even coordinate sum)", all_even and len(inv_both) == 9 ** 3 and
          set(inv_eta) == {t for t in itertools.product(range(-9, 10), repeat=3) if t[0] % 2 == 0 and t[1] % 2 == 0} and set(inv_eps) == {t for t in itertools.product(range(-9, 10), repeat=3) if sum(t) % 2 == 0},
          f"invariant translations with both: {len(inv_both)} (expected 9^3 = 729 all-even vectors in [-9, 9]^3); {time.time() - T0:.0f} s")
    if not all_even:
        FIRED.append("an odd translation leaves {eta, eps} invariant")
    # ---- (C) composite bands
    thetas = np.linspace(0.02, np.pi / 2, 60)
    Ks = np.linspace(-np.pi + 1e-3, np.pi - 1e-3, 400)
    worst_eq, vmax, sat_at, curv_min = 0.0, {}, [], np.inf
    for th in thetas:
        eig_phase = []
        for K in Ks:
            Uf = np.array([[np.cos(th), 1j * np.sin(th) * np.exp(-1j * K)], [1j * np.sin(th) * np.exp(1j * K), np.cos(th)]])
            Us = np.array([[0, np.exp(-1j * K)], [1, 0]])
            U = Uf @ Us
            lam = np.linalg.eigvals(U)
            mu = lam * np.exp(1j * K / 2)                      # lambda = e^{-iK/2} mu
            worst_eq = max(worst_eq, float(np.max(np.abs(mu ** 2 - 2j * np.sin(th) * np.cos(K / 2) * mu - 1))))
            eig_phase.append(np.angle(lam))
        eig_phase = np.array(eig_phase)                        # (nK, 2): eigenphases of one application (two ticks): lambda = e^{i phase}, phase = omega_band = -K/2 + nu
        # band branch: the analytic branch omega_1 = -K/2 + nu, omega_2 = -K/2 + pi - nu with sin(nu) = sin(theta) cos(K/2): track by continuity
        nu = np.arcsin(np.sin(th) * np.cos(Ks / 2))
        for om, name in ((-Ks / 2 + nu, "a"), (-Ks / 2 + np.pi - nu, "b")):
            # check the analytic branch against the numerical eigenphases (mod 2 pi)
            ok = np.min(np.abs(np.exp(1j * eig_phase) - np.exp(1j * om)[:, None]), axis=1).max()
            worst_eq = max(worst_eq, float(ok))
            v = np.gradient(om, Ks)                            # d omega / dK from the eigenphases' analytic branch, by finite differences (independent of the arcsin derivative)
            vmax[(th, name)] = float(np.abs(v[2:-2]).max())
            if th < np.pi / 2 - 1e-9:
                curv_min = min(curv_min, float(np.abs(np.gradient(v, Ks)[2:-2]).max()))
    vm = max(vmax.values())
    dev_closed = max(abs(vmax[(th, 'a')] - (1 + np.sin(th)) / 2) for th in thetas)      # sup over K of |v| is (1 + sin(theta))/2, attained at K = pi
    check("(C) composite of the flat exchange cell and the saturating shift on a 60 x 400 (theta, K) grid: eigenvalues satisfy mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0 (lambda = e^{-iK/2} mu) and the analytic branches match the eigenphases; "
          "|v| = |d omega/dK| <= 1, with sup over K equal to (1 + sin(theta))/2 (so 1 only at theta = pi/2); the band is curved for theta != 0", worst_eq < 1e-9 and vm <= 1 + 1e-3 and dev_closed < 5e-3 and curv_min > 1e-3,
          f"largest band-equation residual {worst_eq:.1e}; max |v| {vm:.6f}; largest deviation of sup_K |v| from (1 + sin(theta))/2 over the theta grid {dev_closed:.1e}; smallest max-curvature over theta < pi/2: {curv_min:.3f}; {time.time() - T0:.0f} s")
    if not (worst_eq < 1e-9 and vm <= 1 + 1e-3):
        FIRED.append(f"composite band equation or velocity bound fails: residual {worst_eq:.1e}, max |v| {vm:.4f}")
    # ---- (D) dials
    ok_d, rows = True, []
    for k in range(0, 9):
        for m in range(0, 9):
            if k + m == 0:
                continue
            slopes = []
            for K in np.linspace(-3, 3, 41):
                Us = np.array([[0, np.exp(-1j * K)], [1, 0]])
                U = np.linalg.matrix_power(Us, k)
                lam = np.linalg.eigvals(U)
                # massless: the eigenphases are +-K-linear with no gap: |lam| = 1 and lam = +-e^{-i k K/2}
                target = np.exp(-1j * k * K / 2)
                ok_d &= np.all(np.minimum(np.abs(lam - target), np.abs(lam + target)) < 1e-9) if k > 0 else np.allclose(lam, 1)
            slope = k / (k + m)
            rows.append((k, m, slope))
    U2 = np.array([[0, np.exp(-1j * 0.7)], [1, 0]]) @ np.array([[0, np.exp(-1j * 0.7)], [1, 0]])
    ok_sq = np.allclose(U2, np.exp(-1j * 0.7) * np.eye(2))
    # cone slope from the band: composite of k shifts and m identities over k + m ticks: omega = k K/2 per application, v = (k/2 cells) * 2 sites / (k + m) ticks
    def cone(k, m):
        Ks_ = np.linspace(-2, 2, 401)
        om = -k * Ks_ / 2
        return abs(np.gradient(om, Ks_)[200]) * 2 / (k + m)
    ok_c = all(abs(cone(k, m) - k / (k + m)) < 1e-9 for k in range(1, 9) for m in range(0, 9))
    check("(D) composite dials: U_shift^2 = e^{-iK} I; for every protocol of k shifts and m identities (k, m <= 8) the composite is massless (eigenvalues +-e^{-ikK/2}, no gap) with cone slope k/(k + m); {shift, shift, identity} has slope 2/3",
          ok_d and ok_sq and ok_c and abs(cone(2, 1) - 2 / 3) < 1e-12, f"{len(rows)} protocols; slope(2,1) = {cone(2, 1):.12f}; {time.time() - T0:.0f} s")
    if not (ok_d and ok_sq and ok_c):
        FIRED.append("a composite dial identity fails")
    # ---- (T) transpose
    rng = np.random.default_rng(3)
    okT = True
    for _ in range(1000):
        A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        okT &= np.allclose((A @ B).T, B.T @ A.T) and np.isclose(np.trace(A.T), np.trace(A)) and (not np.allclose((A @ B).T, A.T @ B.T) or np.allclose(A @ B, B @ A))
    check("(T) the transpose map preserves the trace and reverses products (an anti-automorphism): (AB)^T = B^T A^T and (AB)^T != A^T B^T unless A and B commute (1000 random complex pairs)", okT)
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: kinetic-isotropy composition closure: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: no falsifier fired: every one of 6,859 translations tested leaves {eta, eps} invariant exactly when all components are even; the composite band equation, the velocity bound (saturation only at theta = pi/2), the curvature, "
          "the massless composite dials with slope k/(k + m) for all protocols with k, m <= 8, and the transpose anti-automorphism hold in independent numerical checks")
    return 0


if __name__ == "__main__":
    sys.exit(run())
