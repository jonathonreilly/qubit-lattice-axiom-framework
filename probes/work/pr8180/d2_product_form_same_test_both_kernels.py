#!/usr/bin/env python3
"""J:falsifier:PR8180 - block 35 (PR #8180), Theorem T3 / check D2: the product-form distinction between the two kernels,
with the SAME test applied to BOTH kernels in the SAME representation.

The note (T3, D2): "The comparator's 1/E(k) is not of the form f(k1, k2) g(k3) in any direction - d^2 log E/dk1 dk3 != 0 - so it
cannot be read as a plane Green function times a propagator; it has no causal direction (D2). The formation kernel is exactly of that
form."  claim_scope (T3): "the comparator's 1/E(k) is not of the product form (plane factor) x (propagator) in any direction (proved)".
The runner checks the comparator only (one mixed derivative at a rational point; the refuting pass at five random points).

Objects (the note's declared objects; sigma^2 = 1 and beta = 1 - both are overall scales and drop out of every test below).
  formation kernel  C(q, tau) = sum_d Cov(theta_0(t), theta_d(t + tau)) e^{-i q.d}, stationary, q != 0, for the linearized recursion
                    theta_{t+1} = P theta_t + xi (P = average over the predecessors (i,j), (i-1,j), (i,j-1)); each mode is an AR(1)
                    chain, so its space-time spectral density is  C^(q, w) = sum_tau C(q, tau) e^{-i w tau} = 1/|1 - phi(q) e^{i w}|^2,
                    phi(q) = (1 + e^{i q1} + e^{i q2})/3, u = |phi|^2.
  comparator        the Z^3 lattice Green function G(x) = int d^3k/(2 pi)^3 e^{i k.x}/E(k), E(k) = sum_i 2(1 - cos k_i), in
                    (i) the note's representation, axis e3: 1/E(k1, k2, k3), mixed form G(k_perp, s) = int dk3/2pi e^{i k3 s}/E;
                    (ii) the level representation, axis (1,1,1): level tau = x1 + x2 + x3, plane coordinates (i, j) = (x1, x2), so the
                         three lower Z^3 neighbours of a site are exactly the formation law's three predecessors;
                         G^(q, w) = 1/E(q1 + w, q2 + w, w) and G(q, tau) = sum_{i,j} G(i, j, tau - i - j) e^{-i q.(i,j)}
                                                                        = int dw/2pi e^{i w tau} G^(q, w).
Tests (each applied to both kernels).
  T-a  separability (plane) x (axis) in full momentum space - the note's own D2 test, done by exact cross-ratios instead of a
       derivative: R = F(a,c) F(b,d) / (F(a,d) F(b,c)) over every quadruple of the momentum grids with rational cosines (L = 4, 6);
       R = 1 on every quadruple iff F is a product on the grid.  Exact rationals (fractions.Fraction).
  T-b  separability (plane) x (level separation) in the mixed representation (q, tau): the same cross-ratio with tau for w.
  T-c  the propagator form "(plane factor) x (propagator)^tau": C(q, tau + 1)/C(q, tau) independent of tau >= 0.
       Machinery: every mixed representation is computed from its spectral density by FFT quadrature (periodic trapezoid rule on M
       points - exponentially accurate for these analytic periodic integrands) on the L x L grid of plane momenta, tau = 0..64; no
       closed form is used to produce the numbers.  The closed forms are then verified exactly (sympy radicals) on the L = 4, 6 grids:
         formation:            r = conj(phi),                     C(q, 0) = 1/(1 - u)
         comparator (1,1,1):   r = conj(phi)/(1 + sqrt(1-u)),     C(q, 0) = 1/(6 sqrt(1 - u))
         comparator e3:        r = lambda = (a - sqrt(a^2-4))/2,  C(k_perp, 0) = 1/sqrt(a^2 - 4),  a = 6 - 2 cos k1 - 2 cos k2
       (each is the decaying solution of the kernel's three-term recurrence in tau; the decaying solution is unique because the second
       root has modulus 1/|r| > 1, and the quadrature decays by Riemann-Lebesgue).
Falsifier.  T3/D2 holds only if at least one representation finds the formation kernel of product form and the comparator not.
HIT if no tested representation does.  INFO lines (numbers only, no test): the exact identity 1/G^ = 3 (1/C^ + 1 - u) on the grids;
the per-level phase of both propagators; C(q, -tau) against conj C(q, tau); the small-|q| decay rates 1 - |r| of both propagators.
Self-contained: numpy, sympy, fractions.  Deterministic (no randomness).
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

L_EXACT = (4, 6)
L_QUAD = 96            # divisible by 4 and 6, so the exact grids are sub-grids of the quadrature grid
M_QUAD = 1 << 17       # quadrature points per mode; aliasing of the slowest mode ~ |phi|^M ~ exp(-60)
TAU_MAX = 64
REL_FLOOR = 1e-7       # ratios C(tau+1)/C(tau) are compared only where |C(tau)| >= REL_FLOOR |C(0)| (above round-off)
TOL_CONST = 1e-6       # a propagator is "tau-independent" if max |r_tau/r_0 - 1| < TOL_CONST
TOL_SEP = 1e-6         # a cross-ratio is "1" (separable) if |R - 1| < TOL_SEP

COS = {4: {0: Fr(1), 1: Fr(0), 2: Fr(-1), 3: Fr(0)},
       6: {0: Fr(1), 1: Fr(1, 2), 2: Fr(-1, 2), 3: Fr(-1), 4: Fr(-1, 2), 5: Fr(1, 2)}}


def c(L, n):
    return COS[L][n % L]


def u_ex(L, n1, n2):
    return (3 + 2 * c(L, n1) + 2 * c(L, n2) + 2 * c(L, n1 - n2)) / 9


def E_ex(L, n1, n2, n3):
    return 6 - 2 * c(L, n1) - 2 * c(L, n2) - 2 * c(L, n3)


def Dform_ex(L, n1, n2, m):
    """|1 - phi(q) e^{i w}|^2 = 1 + u - (2/3)[cos w + cos(q1 + w) + cos(q2 + w)] at q = 2 pi (n1, n2)/L, w = 2 pi m/L."""
    return 1 + u_ex(L, n1, n2) - Fr(2, 3) * (c(L, m) + c(L, n1 + m) + c(L, n2 + m))


def census(F, plane, axis):
    """exact cross-ratio census: (#quadruples, #R != 1, first witness)."""
    vals = {(p, a): F(p, a) for p in plane for a in axis}
    tot = bad = 0
    wit = None
    for p, p2 in itertools.combinations(plane, 2):
        for a, a2 in itertools.combinations(axis, 2):
            v = (vals[p, a], vals[p2, a2], vals[p, a2], vals[p2, a])
            if any(x is None or x == 0 for x in v):
                continue
            tot += 1
            R = v[0] * v[1] / (v[2] * v[3])
            if R != 1:
                bad += 1
                if wit is None:
                    wit = (p, p2, a, a2, R)
    return tot, bad, wit


def inv(x):
    return None if x == 0 else 1 / x


# ------------------------------------------------------------------------------------------------------------------ T-a (exact)
def test_a():
    print("== T-a: separability (plane) x (axis) in full momentum space, exact cross-ratios on the rational-cosine grids")
    out = {}
    for L in L_EXACT:
        plane = [(n1, n2) for n1 in range(L) for n2 in range(L) if (n1, n2) != (0, 0)]
        axis = list(range(L))
        rows = {
            "comparator_e3": census(lambda p, a: inv(E_ex(L, p[0], p[1], a)), plane, axis),
            "comparator_111": census(lambda p, a: inv(E_ex(L, p[0] + a, p[1] + a, a)), plane, axis),
            "formation": census(lambda p, a: inv(Dform_ex(L, p[0], p[1], a)), plane, axis),
        }
        for name, (tot, bad, wit) in rows.items():
            w = "" if wit is None else f"; first: q=2pi{wit[0]}/{L}, q'=2pi{wit[1]}/{L}, w=2pi*{wit[2]}/{L}, w'=2pi*{wit[3]}/{L}, R={wit[4]}"
            print(f"[T-a] L={L} {name:15s} quadruples={tot:5d} with R != 1: {bad:5d}{w}")
            out.setdefault(name, [0, 0, None])
            out[name][0] += tot
            out[name][1] += bad
            if out[name][2] is None and wit is not None:
                out[name][2] = (L, wit)
    # the note's own point, by the same exact cross-ratio instead of the derivative: comparator at the note's axis e3
    return out


def test_a_identity():
    """INFO: 1/G^(q, w) = E(q1 + w, q2 + w, w) = 3 (|1 - phi e^{iw}|^2 + 1 - u) = 3 (1/C^(q, w) + 1 - u), exact on the grids."""
    n = bad = 0
    for L in L_EXACT:
        for n1, n2, m in itertools.product(range(L), repeat=3):
            n += 1
            if E_ex(L, n1 + m, n2 + m, m) != 3 * (Dform_ex(L, n1, n2, m) + 1 - u_ex(L, n1, n2)):
                bad += 1
    print(f"[INFO] exact identity 1/G^(q,w) = 3 (1/C^(q,w) + 1 - u(q)) (comparator along (1,1,1) vs formation, sigma^2 = beta = 1): "
          f"{n - bad}/{n} grid points (L = 4, 6), {bad} failures")
    return bad == 0


# ------------------------------------------------------------------------------------------------------------------ T-b, T-c (quadrature)
def spectra(Q1, Q2, w):
    phi_re = (1 + np.cos(Q1) + np.cos(Q2)) / 3
    phi_im = (np.sin(Q1) + np.sin(Q2)) / 3
    u = phi_re ** 2 + phi_im ** 2
    S = np.cos(w) + np.cos(Q1 + w) + np.cos(Q2 + w)
    form = 1.0 / (1 + u - (2.0 / 3.0) * S)
    cone = 1.0 / (6 - 2 * np.cos(Q1 + w) - 2 * np.cos(Q2 + w) - 2 * np.cos(w))
    e3 = 1.0 / (6 - 2 * np.cos(Q1) - 2 * np.cos(Q2) - 2 * np.cos(w))
    return {"formation": form, "comparator_111": cone, "comparator_e3": e3}


def closed_forms(q1, q2):
    phi = (1 + np.exp(1j * q1) + np.exp(1j * q2)) / 3
    u = abs(phi) ** 2
    a = 6 - 2 * np.cos(q1) - 2 * np.cos(q2)
    lam = (a - np.sqrt(a * a - 4)) / 2
    return {"formation": (np.conj(phi), 1 / (1 - u)),
            "comparator_111": (np.conj(phi) / (1 + np.sqrt(1 - u)), 1 / (6 * np.sqrt(1 - u))),     # (1 - sqrt(1-u))/u = 1/(1 + sqrt(1-u))
            "comparator_e3": (lam, 1 / np.sqrt(a * a - 4))}


def test_bc():
    L, M = L_QUAD, M_QUAD
    print(f"== T-b / T-c: mixed representation (q, tau) by FFT quadrature, L = {L} ({L * L - 1} nonzero modes), M = {M}, tau = -{TAU_MAX}..{TAU_MAX}")
    t0 = time.time()
    modes = [(n1, n2) for n1 in range(L) for n2 in range(L) if (n1, n2) != (0, 0)]
    w = 2 * np.pi * np.arange(M) / M
    names = ("formation", "comparator_111", "comparator_e3")
    Cpos = {k: np.zeros((len(modes), TAU_MAX + 2), dtype=complex) for k in names}
    Cneg = {k: np.zeros((len(modes), TAU_MAX + 1), dtype=complex) for k in names}
    chunk = 32
    for i0 in range(0, len(modes), chunk):
        sub = modes[i0:i0 + chunk]
        Q1 = (2 * np.pi / L) * np.array([m[0] for m in sub], dtype=float)[:, None]
        Q2 = (2 * np.pi / L) * np.array([m[1] for m in sub], dtype=float)[:, None]
        for k, f in spectra(Q1, Q2, w[None, :]).items():
            g = np.fft.ifft(f, axis=1)            # g[tau] = (1/M) sum_m f(w_m) e^{+i w_m tau}
            Cpos[k][i0:i0 + len(sub)] = g[:, :TAU_MAX + 2]
            Cneg[k][i0:i0 + len(sub)] = g[:, [(-t) % M for t in range(TAU_MAX + 1)]]
    print(f"[T-c] quadrature done in {time.time() - t0:.1f}s")
    res = {}
    qarr = [(2 * np.pi * n1 / L, 2 * np.pi * n2 / L) for n1, n2 in modes]
    for k in names:
        C = Cpos[k]
        dev_const = 0.0
        npairs = 0
        dev_closed_r = dev_closed_c0 = 0.0
        max_herm = 0.0
        for i, (q1, q2) in enumerate(qarr):
            c0 = C[i, 0]
            r0 = C[i, 1] / C[i, 0]
            for t in range(1, TAU_MAX + 1):
                if abs(C[i, t]) < REL_FLOOR * abs(c0) or abs(C[i, t + 1]) < REL_FLOOR * abs(c0):
                    break
                dev_const = max(dev_const, abs((C[i, t + 1] / C[i, t]) / r0 - 1))
                npairs += 1
            rc, cc = closed_forms(q1, q2)[k]
            if abs(rc) < 1e-9:      # phi(q) = 0 (q = 2pi(1,2)/3, 2pi(2,1)/3): the closed form is r = 0, compared absolutely
                dev_closed_r = max(dev_closed_r, abs(r0))
            else:
                dev_closed_r = max(dev_closed_r, abs(r0 / rc - 1))
            dev_closed_c0 = max(dev_closed_c0, abs(c0 / cc - 1))
            max_herm = max(max_herm, float(np.max(np.abs(Cneg[k][i] - np.conj(C[i, :TAU_MAX + 1])))) / abs(c0))
        res[k] = dict(dev_const=dev_const, npairs=npairs, dev_r=dev_closed_r, dev_c0=dev_closed_c0, herm=max_herm)
        print(f"[T-c] {k:15s} max_tau |(C(tau+1)/C(tau))/(C(1)/C(0)) - 1| = {dev_const:.2e} over {npairs} (q, tau) pairs; "
              f"quadrature vs closed form: max |r/r_closed - 1| = {dev_closed_r:.2e}, max |C(0)/C0_closed - 1| = {dev_closed_c0:.2e}")
    for k in names:
        print(f"[INFO] {k:15s} max_q,tau |C(q,-tau) - conj C(q,tau)|/|C(q,0)| = {res[k]['herm']:.2e}")
    # the per-level phase of the two propagators along (1,1,1)
    ph = 0.0
    nph = 0
    for i, (q1, q2) in enumerate(qarr):
        if abs(1 + np.exp(1j * q1) + np.exp(1j * q2)) / 3 < 1e-6:
            continue
        rf = Cpos["formation"][i, 1] / Cpos["formation"][i, 0]
        rc = Cpos["comparator_111"][i, 1] / Cpos["comparator_111"][i, 0]
        ph = max(ph, abs(np.angle(rc / rf)))
        nph += 1
    print(f"[INFO] per-level phase along (1,1,1): max_q |arg r_comparator - arg r_formation| = {ph:.2e} rad ({nph} modes with phi(q) != 0)")
    # T-b: separability (plane) x (level separation) - cross-ratios over all pairs of a fixed sub-grid of modes and tau pairs
    sub = [i for i, (n1, n2) in enumerate(modes) if n1 % 12 == 0 and n2 % 12 == 0]   # the L = 8 sub-grid, 63 nonzero modes
    taus = (0, 1, 2, 3)
    print(f"== T-b: separability (plane) x (tau), cross-ratios on the {len(sub)} modes of the L = 8 sub-grid, tau in {taus}")
    for k in names:
        C = Cpos[k]
        tot = bad = 0
        mx = 0.0
        for i, j in itertools.combinations(sub, 2):
            for t1, t2 in itertools.combinations(taus, 2):
                den = C[i, t2] * C[j, t1]
                if abs(den) < 1e-12 * abs(C[i, 0] * C[j, 0]):
                    continue
                R = C[i, t1] * C[j, t2] / den
                tot += 1
                if abs(R - 1) > TOL_SEP:
                    bad += 1
                mx = max(mx, abs(R - 1))
        res[k]["tb"] = (tot, bad, mx)
        print(f"[T-b] {k:15s} quadruples={tot:5d} with |R - 1| > {TOL_SEP:g}: {bad:5d} (max |R - 1| = {mx:.3f})")
    # INFO: the small-|q| decay rates of the two propagators along (1,1,1): 1 - |r| against |q|
    print("[INFO] decay per level along (1,1,1) at q = 2pi(n, 0)/96:  n, |q|, 1 - |r_formation|, 1 - |r_comparator|")
    for n in (1, 2, 4, 8, 16):
        i = modes.index((n, 0))
        rf = abs(Cpos["formation"][i, 1] / Cpos["formation"][i, 0])
        rc = abs(Cpos["comparator_111"][i, 1] / Cpos["comparator_111"][i, 0])
        print(f"[INFO]   {n:2d}  {2 * np.pi * n / L:.5f}  {1 - rf:.4e}  {1 - rc:.4e}")
    return res


# ------------------------------------------------------------------------------------------------------------------ exact closed forms
def test_c_exact():
    print("== T-c exact: the closed-form propagators solve each kernel's three-term recurrence in tau (sympy radicals, L = 4, 6 grids)")
    zeta = {4: sp.I, 6: sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2}
    n_ok = n_all = 0
    for L in L_EXACT:
        for n1, n2 in itertools.product(range(L), repeat=2):
            if (n1, n2) == (0, 0):
                continue
            z1, z2 = sp.expand(zeta[L] ** n1), sp.expand(zeta[L] ** n2)
            phi = sp.expand((1 + z1 + z2) / 3)
            phib = sp.conjugate(phi)
            u = sp.nsimplify(sp.expand(phi * phib))
            assert u == u_ex(L, n1, n2)
            s = sp.sqrt(1 - u)
            # formation, from C^ |1 - phi e^{iw}|^2 = 1:  (1 + u) C(tau) - phi C(tau+1) - conj(phi) C(tau-1) = delta_{tau,0};
            # closed form C(tau) = V conj(phi)^tau (tau >= 0), V phi^|tau| (tau < 0), V = 1/(1 - u)
            rf, V = phib, 1 / (1 - u)
            okf = sp.simplify(sp.expand((1 + u) * rf - phi * rf ** 2 - phib)) == 0 \
                and sp.simplify(V * (1 + u - phi * rf - phib * sp.conjugate(rf)) - 1) == 0 \
                and bool(sp.simplify(sp.expand(rf * sp.conjugate(rf))) < 1)
            # comparator (1,1,1), from G^ E(q1+w, q2+w, w) = 1:  6 G(tau) - 3 phi G(tau+1) - 3 conj(phi) G(tau-1) = delta_{tau,0};
            # closed form G(tau) = A r^tau (tau >= 0), A conj(r)^|tau| (tau < 0), r = conj(phi)(1 - s)/u = conj(phi)/(1 + s), A = 1/(6 s)
            r = phib / (1 + s)
            A = 1 / (6 * s)
            ok1 = sp.simplify(sp.expand(3 * phi * r ** 2 - 6 * r + 3 * phib)) == 0
            ok2 = sp.simplify(A * (6 - 3 * phi * r - 3 * phib * sp.conjugate(r)) - 1) == 0
            mod2 = sp.simplify(sp.expand(r * sp.conjugate(r)))
            ok3 = sp.simplify(mod2 - u / (1 + s) ** 2) == 0 and bool(mod2 < 1) and bool(mod2 >= 0)
            # comparator e3: a G(s) - G(s+1) - G(s-1) = delta_{s,0}
            a = 6 - 2 * c(L, n1) - 2 * c(L, n2)
            a = sp.Rational(a.numerator, a.denominator)
            lam = (a - sp.sqrt(a ** 2 - 4)) / 2
            ok4 = sp.simplify(sp.expand(lam ** 2 - a * lam + 1)) == 0
            ok5 = sp.simplify((a - 2 * lam) / sp.sqrt(a ** 2 - 4) - 1) == 0
            ok6 = bool(0 < lam < 1)
            n_all += 1
            n_ok += int(okf and ok1 and ok2 and ok3 and ok4 and ok5 and ok6)
    print(f"[T-c] exact: {n_ok}/{n_all} grid modes where all three closed forms (formation; comparator along (1,1,1) and along e3) "
          f"solve their recurrences with |r| < 1 and the tau = 0 normalization holds")
    return n_ok == n_all


def main():
    t0 = time.time()
    a = test_a()
    ident = test_a_identity()
    exact_ok = test_c_exact()
    bc = test_bc()
    # decisions
    sep_a = {k: a[k][1] == 0 for k in a}                       # separable on the grids iff no cross-ratio differs from 1
    sep_b = {k: bc[k]["tb"][1] == 0 for k in bc}
    prop_c = {k: bc[k]["dev_const"] < TOL_CONST for k in bc}
    comps = ("comparator_e3", "comparator_111")
    distinguishing = []
    if sep_a["formation"] and not any(sep_a[k] for k in comps):
        distinguishing.append("T-a")
    if sep_b["formation"] and not any(sep_b[k] for k in comps):
        distinguishing.append("T-b")
    if prop_c["formation"] and not all(prop_c[k] for k in comps):
        distinguishing.append("T-c")
    print("== decisions (product form holds?)")
    for k in ("formation",) + comps:
        print(f"[DEC] {k:15s} T-a separable: {sep_a[k]}   T-b separable: {sep_b[k]}   T-c plane factor x propagator^tau: {prop_c[k]}")
    print(f"[DEC] exact closed forms verified on all L = 4, 6 modes: {exact_ok}; exact identity 1/G^ = 3(1/C^ + 1 - u): {ident}")
    print(f"[DEC] representations in which the formation kernel has the product form and the comparator lacks it: {distinguishing or 'none'}")
    fa, ca, c1 = a["formation"], a["comparator_e3"], a["comparator_111"]
    wit = fa[2]
    if not distinguishing:
        print(f"HIT: T3/D2 - the note's own test (plane x axis separability in full momentum, exact cross-ratios) finds the formation kernel's "
              f"spectral density 1/|1 - phi e^(iw)|^2 non-product in {fa[1]}/{fa[0]} quadruples (L = {wit[0]}: R = {wit[1][4]} at "
              f"q = 2pi{wit[1][0]}/{wit[0]}, q' = 2pi{wit[1][1]}/{wit[0]}, w = 2pi*{wit[1][2]}/{wit[0]}, w' = 2pi*{wit[1][3]}/{wit[0]}), "
              f"as it finds 1/E ({ca[1]}/{ca[0]} along e3, {c1[1]}/{c1[0]} along (1,1,1))")
        print(f"HIT: T3/D2 - in the mixed (q, tau) representation the comparator's Z^3 Green function is (plane factor) x (propagator)^tau "
              f"along (1,1,1) [r = conj(phi)/(1 + sqrt(1-u)), C0 = 1/(6 sqrt(1-u))] and along e3 [r = lambda(k_perp)]: max |r_tau/r_0 - 1| = "
              f"{bc['comparator_111']['dev_const']:.1e} / {bc['comparator_e3']['dev_const']:.1e} over {L_QUAD * L_QUAD - 1} modes, tau <= {TAU_MAX} "
              f"(formation: {bc['formation']['dev_const']:.1e}); closed forms {'exact on all' if exact_ok else 'NOT verified on all'} L = 4, 6 grid modes")
    print(f"[time] {time.time() - t0:.1f}s")
    print(f"SUMMARY: T3/D2 product-form test on both kernels - T-a full-momentum separability: formation non-product {fa[1]}/{fa[0]}, "
          f"comparator {ca[1]}/{ca[0]} (e3) and {c1[1]}/{c1[0]} (1,1,1); T-b (q, tau) separability: formation {bc['formation']['tb'][1]}/"
          f"{bc['formation']['tb'][0]}, comparator {bc['comparator_111']['tb'][1]}/{bc['comparator_111']['tb'][0]} non-product; "
          f"T-c propagator form holds for both (max dev {bc['formation']['dev_const']:.1e} formation, {bc['comparator_111']['dev_const']:.1e} (1,1,1), "
          f"{bc['comparator_e3']['dev_const']:.1e} e3; L = {L_QUAD}, M = {M_QUAD}, tau <= {TAU_MAX}); distinguishing representations: "
          f"{distinguishing or 'none'}; exact identity 1/G^ = 3(1/C^ + 1 - u) on {'all' if ident else 'NOT all'} grid points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
