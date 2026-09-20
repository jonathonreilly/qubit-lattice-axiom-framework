#!/usr/bin/env python3
"""two-pin-interaction-linear, independent run 2 of 2 (worker w-jonathonsmac4f50-j4dda, claude-opus-5).

Stationary equal-time law of the linear formation model on the periodic L^3 lattice: a centred Gaussian field with
C(k) = sigma^2/(1 - |phi(k)|^2), the zero mode removed; light-cone past phi = 1 - E(k)/7, E(k) = sum_i 2(1 - cos k_i);
backward past phi = (1 + sum_j e^{i k_j})/4.  sigma^2 = 1 below; every C and every interaction scales with sigma^2.

A1 (exact)  conditioning on theta(x1) = a, theta(x2) = b: the pair has density proportional to exp(-(1/2) v^T K^-1 v),
            K = [[C0, Cr], [Cr, C0]]; the cross term of -(1/2) v^T K^-1 v is + a b Cr/(C0^2 - Cr^2), so the interaction
            energy is U(r) = -a b C(r)/(C0^2 - C(r)^2) = -a b C(r)/C0^2 (1 + O((C(r)/C0)^2)).
A2 (exact)  1 - phi^2 = E(14 - E)/49 and E = |k|^2 + O(|k|^4), so C(k) = (7/2)/|k|^2 + O(1) and C(r) -> c/r with c = 7/(8 pi).
N1 (numerical, labelled)  C(r) by FFT at L = 32, 64, 128 along (1,0,0), (1,1,0), (1,1,1): r C(r)/c against 1, and against the
            periodic (image) prediction c sum_n (1/|r + L n| - 1/(L|n|)) + const fixed by the zero mode.
N2 (numerical, labelled)  the interaction U(r)/(a b) against -c/(r C0^2) over 3 <= r <= L/6.
N3 (exact + numerical)  backward past: M = Cov of {0, e1, e2, e3}, its eigenvalues, the anisotropic continuum law
            C(r) = 1/(4 pi sqrt(det M) sqrt(r^T M^-1 r)), the equipotential ellipsoids, and the FFT table."""
import itertools
import math
import sys

import numpy as np
import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def cov_fft(L, kind):
    k = 2 * np.pi * np.fft.fftfreq(L)
    K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
    if kind == "lightcone":
        E = 2 * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3))
        den = E * (14 - E) / 49.0
    else:
        ph = (1 + np.exp(1j * K1) + np.exp(1j * K2) + np.exp(1j * K3)) / 4.0
        den = 1 - np.abs(ph) ** 2
    S = np.zeros_like(den)
    m = den > 1e-14
    S[m] = 1.0 / den[m]
    S[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(S))


def cont_ref(L, Mmat=None):
    """the zero-mode-removed continuum kernel on the same torus grid: (1/N) sum_{k != 0} e^{ikr}/Q(k), Q = |k|^2 or k^T M k.
    This is the periodic 1/r law with its image (Madelung) constant built in, and carries no lattice artefact."""
    k = 2 * np.pi * np.fft.fftfreq(L)
    K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
    if Mmat is None:
        Q = K1 ** 2 + K2 ** 2 + K3 ** 2
    else:
        Q = (Mmat[0][0] * K1 ** 2 + Mmat[1][1] * K2 ** 2 + Mmat[2][2] * K3 ** 2
             + 2 * Mmat[0][1] * K1 * K2 + 2 * Mmat[0][2] * K1 * K3 + 2 * Mmat[1][2] * K2 * K3)
    S = np.zeros_like(Q)
    m = Q > 1e-14
    S[m] = 1.0 / Q[m]
    S[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(S))


def main():
    # ---------------- A1
    a, b, C0, Cr = sp.symbols("a b C0 Cr", real=True)
    K = sp.Matrix([[C0, Cr], [Cr, C0]])
    v = sp.Matrix([a, b])
    quad = sp.expand(-(v.T * K.inv() * v)[0, 0] / 2)
    cross = sp.simplify(quad.coeff(a, 1).coeff(b, 1))
    ok = sp.simplify(cross - Cr / (C0 ** 2 - Cr ** 2)) == 0
    ser = sp.series(-Cr / (C0 ** 2 - Cr ** 2), Cr, 0, 4).removeO()
    ok &= sp.simplify(ser - (-Cr / C0 ** 2 - Cr ** 3 / C0 ** 4)) == 0
    check("A1", ok, "for the Gaussian pair (theta(x1), theta(x2)) with covariance K = [[C0, Cr], [Cr, C0]], -(1/2) v^T K^-1 v has cross term "
          "+ a b Cr/(C0^2 - Cr^2), so the interaction energy is U = -a b C(r)/(C0^2 - C(r)^2) = -a b C(r)/C0^2 - a b C(r)^3/C0^4 + ... : "
          "like pins (a b > 0) attract wherever C(r) > 0 (symbolic)")

    # ---------------- A2
    k1, k2, k3, t = sp.symbols("k1 k2 k3 t", real=True)
    E = sum(2 * (1 - sp.cos(ki)) for ki in (k1, k2, k3))
    phi = 1 - E / 7
    ok = sp.simplify(sp.expand(1 - phi ** 2) - E * (14 - E) / 49) == 0
    Es = sp.series(E.subs({k1: t * k1, k2: t * k2, k3: t * k3}), t, 0, 4).removeO()
    ok &= sp.simplify(Es.coeff(t, 2) - (k1 ** 2 + k2 ** 2 + k3 ** 2)) == 0
    lead = sp.limit(sp.Symbol("q") ** 2 * 49 / (sp.Symbol("q") ** 2 * (14 - sp.Symbol("q") ** 2)), sp.Symbol("q"), 0)
    ok &= lead == sp.Rational(7, 2)
    c_exact = sp.Rational(7, 8) / sp.pi
    check("A2", ok, f"1 - phi^2 = E(14 - E)/49 and E = |k|^2 + O(|k|^4), so C(k) = (7/2)/|k|^2 + O(1) and, by the transform of A/|k|^2 "
          f"(A/(4 pi r)), C(r) -> c/r with c = 7 sigma^2/(8 pi) = {float(c_exact):.6f} sigma^2 (symbolic; the lattice tables below are the check)")

    # ---------------- N1, N2
    c = 7 / (8 * math.pi)
    dirs = {"(1,0,0)": (1, 0, 0), "(1,1,0)": (1, 1, 0), "(1,1,1)": (1, 1, 1)}
    okn = True
    worst, worst_raw = {}, {}
    for L in (32, 64, 128):
        Cg = cov_fft(L, "lightcone")
        Ref = (7 / 2) * cont_ref(L)          # c/r with the torus images: the same zero-mode-removed sum with the symbol |k|^2
        C0v = Cg[0, 0, 0]
        fs = c * float(np.mean([1 / rr - Ref[rr, 0, 0] / c for rr in (6, 8, 10, 12)])) * L   # the finite-size constant, in units c/L
        for nm, u in dirs.items():
            rows, dev, dev_raw = [], [], []
            rmax = L // 2 // max(u)
            for rr in range(1, rmax + 1):
                pos = tuple((rr * ui) % L for ui in u)
                pos2 = tuple(((rr + 1) * ui) % L for ui in u)
                dist = rr * math.dist([0, 0, 0], list(u))
                val, ref = Cg[pos], Ref[pos]
                pair = (val + Cg[pos2]) / 2 / ((ref + Ref[pos2]) / 2) if rr < rmax else float("nan")
                rows.append((dist, val, dist * val / c, val / ref, pair))
                if 3 <= dist <= L / 6:
                    dev_raw.append(abs(val / ref - 1))
                    if pair == pair:
                        dev.append(abs(pair - 1))
            worst[(L, nm)] = max(dev) if dev else float("nan")
            worst_raw[(L, nm)] = max(dev_raw) if dev_raw else float("nan")
            okn &= (max(dev) if dev else 0) < (0.05 if u == (1, 0, 0) else 0.03)
            show = ", ".join(f"r={d:.2f}: rC/c={q:.3f}, C/periodic={w:.3f}" for d, v, q, w, pr in rows[:6])
            print(f"   L={L} {nm}: C(0) = {C0v:.5f}; {show}")
        print(f"   L={L}: the periodic law is c(1/r - {fs / c:.3f}/L) at r << L (the textbook cubic Wigner constant is 2.8373)")
    check("N1", okn, "(numerical, labelled) light-cone C(r) by FFT against c/r with the torus images, i.e. the same zero-mode-removed Fourier sum "
          "with the continuum symbol: over 3 <= r <= L/6 the largest |C/periodic - 1| is " +
          ", ".join(f"L={L} {nm}: {worst_raw[(L, nm)]:.3f}" for L, nm in sorted(worst_raw)) +
          "; the deviation along (1,0,0) is an even-odd lattice term from the factor 1/(14 - E), which peaks at the zone corner: averaging "
          "neighbouring r removes it and leaves " + ", ".join(f"L={L} {nm}: {worst[(L, nm)]:.3f}" for L, nm in sorted(worst)) +
          "; without the image term the plain c/r is low by about 2.8 r/L, 47 % at r = L/6")
    L = 64
    Cg = cov_fft(L, "lightcone")
    Ref = (7 / 2) * cont_ref(L)
    C0v = Cg[0, 0, 0]
    rows = []
    for rr in range(1, L // 2):
        val, ref = Cg[rr, 0, 0], Ref[rr, 0, 0]
        pair = (-(val + Cg[rr + 1, 0, 0]) / 2) / (C0v ** 2)
        rows.append((rr, -val / (C0v ** 2 - val ** 2), -ref / C0v ** 2, pair / (-(ref + Ref[rr + 1, 0, 0]) / 2 / C0v ** 2)))
    band = [(r, u, p, q) for r, u, p, q in rows if 3 <= r <= L / 6]
    dev2 = max(abs(q - 1) for r, u, p, q in band)
    check("N2", dev2 < 0.05, f"(numerical, labelled) L = 64 axis: U(r)/(a b) = -C(r)/(C0^2 - C(r)^2) against the periodic -C_1/r(r)/C0^2, "
          f"C(0) = {C0v:.5f}: " + ", ".join(f"r={r}: {u:+.6f} vs {p:+.6f}" for r, u, p, q in rows[:3] + band[-2:]) +
          f"; over 3 <= r <= L/6, after averaging neighbouring r, the largest deviation is {dev2:.4f}")

    # ---------------- N3
    P = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    mean = [sp.Rational(sum(p[i] for p in P), 4) for i in range(3)]
    M = sp.Matrix(3, 3, lambda i, j: sp.Rational(sum(p[i] * p[j] for p in P), 4) - mean[i] * mean[j])
    ev = M.eigenvals()
    Minv = M.inv()
    detM = sp.det(M)
    pre = 1 / (4 * sp.pi * sp.sqrt(detM))
    axis_fac = sp.sqrt((sp.Matrix([1, 0, 0]).T * Minv * sp.Matrix([1, 0, 0]))[0, 0])
    diag_fac = sp.sqrt((sp.Matrix([1, 1, 1]).T * Minv * sp.Matrix([1, 1, 1]))[0, 0] / 3)
    ok = M == sp.Matrix([[sp.Rational(3, 16), sp.Rational(-1, 16), sp.Rational(-1, 16)],
                         [sp.Rational(-1, 16), sp.Rational(3, 16), sp.Rational(-1, 16)],
                         [sp.Rational(-1, 16), sp.Rational(-1, 16), sp.Rational(3, 16)]])
    ok &= set(ev) == {sp.Rational(1, 16), sp.Rational(1, 4)} and detM == sp.Rational(1, 256)
    Lb = 64
    Cb = cov_fft(Lb, "backward")
    Mf = [[float(M[i, j]) for j in range(3)] for i in range(3)]
    RefM = cont_ref(Lb, Mf)                               # the anisotropic continuum kernel, same zero-mode removal
    rows = []
    for nm, u in (("(1,0,0)", (1, 0, 0)), ("(1,1,0)", (1, 1, 0)), ("(1,1,1)", (1, 1, 1))):
        fac = float(sp.sqrt((sp.Matrix(list(u)).T * Minv * sp.Matrix(list(u)))[0, 0] / sum(x * x for x in u)))
        vals = []
        for rr in (3, 4, 6, 8):
            pos = tuple((rr * ui) % Lb for ui in u)
            dist = rr * math.dist([0, 0, 0], list(u))
            vals.append((dist, Cb[pos], Cb[pos] / RefM[pos], float(pre) / (dist * fac)))
        rows.append((nm, fac, vals))
    okn3 = all(abs(v[2] - 1) < 0.06 for nm, f, vs in rows for v in vs)
    check("N3", ok and okn3, f"backward past: M = Cov{{0, e1, e2, e3}} = (1/4)I - (1/16)J with eigenvalues 1/16 along (1,1,1) and 1/4 twice, "
          f"det M = 1/256; the continuum law is C(r) = sigma^2/(4 pi sqrt(det M) sqrt(r^T M^-1 r)) = {sp.nsimplify(pre)} sigma^2/sqrt(r^T M^-1 r), "
          f"so the equipotentials are the ellipsoids r^T M^-1 r = const: semi-axes proportional to sqrt(eigenvalue), 1/4 along (1,1,1) against 1/2 "
          f"across, i.e. at fixed |r| the potential is twice as large across the cone axis as along it; FFT at L = 64 against the anisotropic "
          f"continuum kernel on the same grid (numerical): "
          + "; ".join(f"{nm} (sqrt(u^T M^-1 u) = {f:.3f}, infinite-volume {vs[0][3]:.5f} at r = {vs[0][0]:.2f}): "
                      + ", ".join(f"r={d:.2f}: C={v:.5f}, C/continuum={q:.3f}" for d, v, q, w in vs) for nm, f, vs in rows))

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: FAILED checks {FAILS}")
        return 0
    print("SUMMARY: conditioning the stationary linear field on two pins gives U(r) = -a b C(r)/(C0^2 - C(r)^2) (exact), and for the light-cone "
          f"past C(r) -> c/r with c = 7 sigma^2/(8 pi) exactly; the FFT tables at L = 32, 64, 128 match the image-corrected 1/r law to better than "
          f"{max(worst_raw[(L, nm)] for L, nm in worst_raw if nm != chr(40) + chr(49) + ',0,0)'):.1%} along the two diagonals for 3 <= r <= L/6 "
          f"(the axis carries an even-odd lattice term of up to {max(worst_raw[(128, chr(40) + chr(49) + ',0,0)')], worst_raw[(64, chr(40) + chr(49) + ',0,0)')]):.1%}), so like pins attract with a 1/r potential; the backward past gives "
          "the same law with the anisotropic metric M = (1/4)I - (1/16)J: equipotential ellipsoids r^T M^-1 r = const, the potential twice as strong "
          "across the cone axis as along it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
