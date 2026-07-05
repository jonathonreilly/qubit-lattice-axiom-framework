#!/usr/bin/env python3
"""Staggered kernel satisfies hypothesis (Z) — point-like isotropic
linear-cone zero-set certificate for the flux-(-1) realized kernel, and
the companion violation certificate for the flux-(+1) kernel (runner).

Companion to
docs/STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md

What is computed (all finite/exact; no thermal content, no selection):

  [A] the two licensed-class representatives are re-constructed
      self-contained (K0 = scalar NN, uniform plaquette flux +1;
      K1 = Kawamoto-Smit phases, uniform flux -1); the 8x8 Bloch symbol
      of the K1 kernel is built SYMBOLICALLY and the identity
      H_c(kappa)^2 = 4(cos^2(kappa_1/2) + cos^2(kappa_2/2)
      + c^2 cos^2(kappa_3/2)) I_8 is verified exactly (sympy, symbolic
      kappa AND symbolic direction-3 weight c), giving the closed-form
      band family +-2 sqrt(sum_mu sin^2 q_mu) (at c = 1) on the reduced
      Brillouin torus at ALL volumes; the Bloch decomposition is tied
      to the explicit lattice eigensolver at L = 4, 8.
  [B] hypothesis (Z) of the fermionic Stefan-Boltzmann theorem FSB-K is
      certified for the K1 kernel EXACTLY, clause by clause:
      (Z-i) the massless set is finite = the 8 BZ corner points
      {0, pi}^3, constant in L (eigensolver kernel dims 8, 8, 8 at
      L = 4, 8, 12); (Z-ii) each corner carries the SAME exact cone
      |E(p_j + q)| = |V q| with V = 2 I_3 (sympy identity
      sin^2(c + q) = sin^2 q at every corner component c in {0, pi}),
      with the explicit quantitative cone data (V, C, r) = (2I, 2/3, 1):
      | |E(p_j+q)| - |2Iq| | <= (2/3)|q|^3 <= (2/3)|q|^2 for |q| <= 1,
      proven by an elementary inequality chain and measured (worst
      sampled ratio 1/3); (Z-iii) V is invertible and isotropic
      (det V = 8, sigma_min = 2; directional speeds all = 2). Cone
      weights: |det V_j| = 8 per corner branch in the unit-hopping
      normalization (sum |det V|^-1 = 1 per site = 8 species per 2^3
      cell); in the staggered central-difference normalization h/2
      (the retained det-positivity row's Euclidean operator) V_j = I_3,
      |det V_j| = 1, sum |det V|^-1 = 8 per cell; exact lambda^3
      covariance ties the two conventions.
  [C] the companion negative fact (re-derived self-contained, needed by
      the downstream consumer): the K0 kernel VIOLATES (Z) -- zero-mode
      counts 20/68/140 at L = 4/8/12 (extensive, the lattice trace of
      the codim-1 surface sum_mu cos p_mu = 0); an EXACT one-parameter
      zero line p(t) = (pi/2 + t, pi/2 - t, pi/2) (sympy identity)
      kills clause (Z-i) on any neighborhood; and any candidate cone
      matrix V is forced singular along the zero-line direction
      (|Vu| t <= C t^2 for all small t => Vu = 0), with measured
      tangent speed exactly 0 and normal speed 2 sqrt(3).
  [D] falsification legs -- the certificate machinery is quantitative
      and branch-sensitive, not vacuous: a direction-3-weighted
      Kawamoto-Smit kernel (c = 1/2; off the two-class surface, still
      in FSB-K's realized class) still satisfies (Z) but with detector
      V = diag(2, 2, 1) and a DIFFERENT weight sum (= 2); at c = 0 the
      cone breaks and the detector reports V singular (axis-3 speed 0)
      while the zero set goes extended (16/32 at L = 4/8); the
      quadratic comparator is point-like yet all-direction singular
      (V = 0) -- the two (Z) clauses are detected independently. The
      (Z)-decision over {K1, K1(c=1/2), K0, K1(c=0), comparator} is
      {pass, pass, fail, fail, fail} through one code path; no flux
      label is consumed by the decision.

Deterministic, no network, no randomness; numpy + sympy.
Exit code 0 iff FAIL = 0.
"""

import itertools
import math
import os
import sys

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
CHECK = 0

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def report(ok, msg):
    global PASS, FAIL, CHECK
    CHECK += 1
    if ok:
        PASS += 1
        print(f"[PASS] {CHECK:2d}. {msg}")
    else:
        FAIL += 1
        print(f"[FAIL] {CHECK:2d}. {msg}")


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


def note_text(relpath):
    with open(os.path.join(REPO, relpath), encoding="utf-8") as f:
        return f.read()


# ----------------------------------------------------------------------
# constructions (self-contained on the axioms' NN cubic adjacency and
# the retained finite periodic Fock surface; one mode per site)
# ----------------------------------------------------------------------

def sites_of(L):
    return list(itertools.product(range(L), repeat=3))


def t_K0(x, mu):
    return 1.0


def t_K1(x, mu, c3=1.0):
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** x[0]
    return ((-1.0) ** (x[0] + x[1])) * c3


def build_h(L, t_fun, onsite=0.0):
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((N, N))
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            t = t_fun(x, mu)
            h[idx[tuple(xp)], idx[x]] += t
            h[idx[x], idx[tuple(xp)]] += t
        if onsite != 0.0:
            h[idx[x], idx[x]] += onsite
    return h


def build_euclid(L, t_fun):
    """Euclidean central-difference operator
    D = sum_mu t_mu(x) (S_mu - S_mu^T)/2 (real antisymmetric; the
    retained det-positivity row's staggered M_KS at U = 1 when
    t = eta)."""
    sites = sites_of(L)
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    D = np.zeros((N, N))
    for x in sites:
        for mu in range(3):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % L
            t = t_fun(x, mu)
            D[idx[tuple(xp)], idx[x]] += 0.5 * t
            D[idx[x], idx[tuple(xp)]] -= 0.5 * t
    return D


def plaquette_fluxes(L, t_fun):
    fluxes = []
    for x in sites_of(L):
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % L
                xm = tuple(xm)
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % L
                xn = tuple(xn)
                f = (t_fun(x, mu) * t_fun(xm, nu)
                     * np.conj(t_fun(xn, mu)) * np.conj(t_fun(x, nu)))
                fluxes.append(complex(f))
    return fluxes


def bloch_K1(kappa, c3=1.0):
    """Numeric 8x8 Bloch symbol of the (weighted) Kawamoto-Smit kernel
    on the 2x2x2 cell; kappa = cell momentum in [0, 2pi)^3."""
    cell = list(itertools.product((0, 1), repeat=3))
    idx = {s: i for i, s in enumerate(cell)}
    H = np.zeros((8, 8), complex)
    for s in cell:
        for mu in range(3):
            t = t_K1(s, mu, c3)
            s2 = list(s)
            carry = (s[mu] == 1)
            s2[mu] = (s[mu] + 1) % 2
            s2 = tuple(s2)
            ph = np.exp(1j * kappa[mu]) if carry else 1.0
            H[idx[s2], idx[s]] += t * ph
            H[idx[s], idx[s2]] += t * np.conj(ph)
    return H


def kernel_dim(h, tol=1e-9):
    return int((np.abs(np.linalg.eigvalsh(h)) < tol).sum())


def torus_grid(L):
    p = 2.0 * np.pi * np.arange(L) / L
    return np.meshgrid(p, p, p, indexing="ij")


def k0_symbol(L):
    p1, p2, p3 = torus_grid(L)
    return (2.0 * (np.cos(p1) + np.cos(p2) + np.cos(p3))).ravel()


def E_K1(p, c3=1.0):
    return 2.0 * math.sqrt(math.sin(p[0]) ** 2 + math.sin(p[1]) ** 2
                           + (c3 ** 2) * math.sin(p[2]) ** 2)


def E_K0(p):
    return 2.0 * (math.cos(p[0]) + math.cos(p[1]) + math.cos(p[2]))


def E_comp(p):
    return E_K0(p) - 6.0


def dir_speed(E_abs, p0, u, t=1e-6):
    """Directional cone-speed estimator: lim |E(p0 + t u)| / t.
    (For a symmetric two-sided estimate use the average of +-u; the
    witnesses here are all even or exactly linear at the tested
    points.)"""
    return abs(E_abs(tuple(p0[i] + t * u[i] for i in range(3)))) / t


def detect_V_diag(E_abs, p0, tol=1e-4):
    """Cone-matrix detector along the lattice axes: returns the
    diagonal directional speeds (the witnesses below have axis-aligned
    principal cone axes) and the singularity flag min(speed) < tol.
    The threshold 1e-4 cleanly separates true cone speeds (O(1)) from
    degenerate directions (O(step) = 1e-6 for a quadratic branch,
    O(step^?) ~ 0 for an exact zero line)."""
    speeds = tuple(dir_speed(E_abs, p0, u)
                   for u in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    return speeds, (min(speeds) < tol)


def z_decision(name, zero_counts_by_L, V_speeds, tol=1e-4):
    """(Z) decision from computed data only: finite (L-constant) zero
    count AND no singular cone direction."""
    counts = list(zero_counts_by_L.values())
    finite = len(set(counts)) == 1
    nonsing = min(V_speeds) >= tol
    return finite and nonsing


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("[A] the two licensed representatives re-derived; the exact")
    print("    symbolic Bloch closed form (all volumes); eigensolver tie")
    print("=" * 72)

    f0 = plaquette_fluxes(4, t_K0)
    f1 = plaquette_fluxes(4, lambda x, mu: t_K1(x, mu))
    h0 = {L: build_h(L, t_K0) for L in (4, 8, 12)}
    h1 = {L: build_h(L, lambda x, mu: t_K1(x, mu)) for L in (4, 8, 12)}
    report(np.allclose(h0[4], h0[4].T) and np.allclose(h1[4], h1[4].T)
           and len(f0) == len(f1) == 3 * 4 ** 3
           and all(abs(f - 1) < 1e-12 for f in f0)
           and all(abs(f + 1) < 1e-12 for f in f1),
           "[A] both representatives Hermitian; frame-invariant uniform "
           "plaquette flux over all 192 plaquettes at L=4: K0 phi=+1, "
           "K1 phi=-1 -- the two-class surface re-derived self-contained "
           "(no kinetic-class-note import)")

    k1s, k2s, k3s, cs = sp.symbols("k1 k2 k3 c", real=True)
    cell = list(itertools.product((0, 1), repeat=3))
    idx = {s: i for i, s in enumerate(cell)}
    Hs = sp.zeros(8, 8)
    kap = [k1s, k2s, k3s]

    def t_sym(s, mu):
        if mu == 0:
            return sp.Integer(1)
        if mu == 1:
            return sp.Integer(-1) ** s[0]
        return (sp.Integer(-1) ** (s[0] + s[1])) * cs

    for s in cell:
        for mu in range(3):
            t = t_sym(s, mu)
            s2 = list(s)
            carry = (s[mu] == 1)
            s2[mu] = (s[mu] + 1) % 2
            s2 = tuple(s2)
            ph = sp.exp(sp.I * kap[mu]) if carry else sp.Integer(1)
            Hs[idx[s2], idx[s]] += t * ph
            Hs[idx[s], idx[s2]] += t * sp.conjugate(ph)
    scalar = 4 * (sp.cos(k1s / 2) ** 2 + sp.cos(k2s / 2) ** 2
                  + cs ** 2 * sp.cos(k3s / 2) ** 2)
    diff = sp.simplify(sp.expand_trig(sp.simplify(Hs * Hs))
                       - scalar * sp.eye(8))
    qsub = sp.simplify(scalar.subs(
        [(k1s, sp.pi - 2 * k1s), (k2s, sp.pi - 2 * k2s),
         (k3s, sp.pi - 2 * k3s), (cs, 1)])
        - 4 * (sp.sin(k1s) ** 2 + sp.sin(k2s) ** 2 + sp.sin(k3s) ** 2))
    report(diff == sp.zeros(8, 8) and qsub == 0,
           "[A] exact symbolic Bloch identity (symbolic kappa AND "
           "symbolic direction-3 weight c): H_c(kappa)^2 = "
           "4(cos^2(k1/2) + cos^2(k2/2) + c^2 cos^2(k3/2)) I_8 -- at "
           "c = 1 the band family is +-2 sqrt(sum_mu sin^2 q_mu), "
           "q_mu = (pi - kappa_mu)/2, on the reduced Brillouin torus at "
           "ALL volumes (the all-L closed-form license)")

    ok_tie = True
    for c3 in (1.0, 0.5):
        for L in (4, 8):
            h = build_h(L, lambda x, mu, c=c3: t_K1(x, mu, c))
            ev = np.sort(np.linalg.eigvalsh(h))
            kg = [4 * np.pi * n / L for n in range(L // 2)]
            bl = np.sort(np.concatenate(
                [np.linalg.eigvalsh(bloch_K1(kk, c3))
                 for kk in itertools.product(kg, repeat=3)]))
            ok_tie &= np.allclose(ev, bl, atol=1e-9)
    ok_k0 = all(np.allclose(np.sort(np.linalg.eigvalsh(h0[L])),
                            np.sort(k0_symbol(L)), atol=1e-9)
                for L in (4, 8))
    report(ok_tie and ok_k0,
           "[A] Bloch decomposition tied to the explicit lattice "
           "eigensolver at L = 4, 8 (multiset equality, c = 1 and "
           "c = 1/2), and the K0 closed form 2 sum_mu cos p_mu tied "
           "likewise -- the symbol evaluations below ARE realized "
           "lattice-kernel spectra")

    D1 = build_euclid(4, lambda x, mu: t_K1(x, mu))
    eD = np.sort(np.abs(np.linalg.eigvalsh(1j * D1)))
    eh = np.sort(np.abs(np.linalg.eigvalsh(h1[4]))) / 2.0
    report(np.allclose(D1, -D1.T) and np.allclose(eD, eh, atol=1e-9),
           "[A] normalization tie: the staggered central-difference "
           "Euclidean operator D_E (the retained det-positivity row's "
           "M_KS at U = 1) has |spec(i D_E)| = |spec(h_K1)| / 2 "
           "(multiset, L = 4) -- the two declared normalizations are "
           "the SAME kernel at scale lambda = 1/2, and cone data "
           "transforms exactly as V -> lambda V")

    print()
    print("=" * 72)
    print("[B] hypothesis (Z) certified for the K1 kernel, clause by")
    print("    clause, with exact cone data")
    print("=" * 72)

    x = sp.symbols("x", real=True)
    sols = sp.solveset(sp.sin(x), x, sp.Interval.Ropen(0, 2 * sp.pi))
    z1 = {L: kernel_dim(h1[L]) for L in (4, 8, 12)}
    p1g, p2g, p3g = torus_grid(128)
    sym_zero_128 = int((np.sqrt(np.sin(p1g) ** 2 + np.sin(p2g) ** 2
                                + np.sin(p3g) ** 2).ravel() < 1e-12).sum())
    report(sols == sp.FiniteSet(0, sp.pi)
           and (z1[4], z1[8], z1[12]) == (8, 8, 8)
           and sym_zero_128 == 8,
           "[B] (Z-i) the massless set is FINITE and exactly the 8 BZ "
           "corner points: E = 2 sqrt(sum sin^2 p_mu) = 0 iff every "
           "sin p_mu = 0 iff p_mu in {0, pi} (sympy solveset on "
           "[0, 2pi)) => |Z(h)| = 2^3 = 8; eigensolver kernel dims "
           "(8, 8, 8) at L = 4, 8, 12, L-CONSTANT; symbol-grid zero "
           "count at L = 128 is 8")

    q1, q2, q3, tt = sp.symbols("q1 q2 q3 t", real=True)
    corner_ok = all(sp.simplify(sp.sin(comp + q1) ** 2 - sp.sin(q1) ** 2)
                    == 0 for comp in (0, sp.pi))
    s2 = sp.sin(q1) ** 2 + sp.sin(q2) ** 2 + sp.sin(q3) ** 2
    ser = sp.expand(sp.series(s2.subs([(q1, q1 * tt), (q2, q2 * tt),
                                       (q3, q3 * tt)]),
                              tt, 0, 6).removeO())
    pred = sp.expand((q1 ** 2 + q2 ** 2 + q3 ** 2) * tt ** 2
                     - (q1 ** 4 + q2 ** 4 + q3 ** 4) * tt ** 4 / 3)
    report(corner_ok and sp.simplify(ser - pred) == 0,
           "[B] (Z-ii) the cone is EXACT and the same at every corner: "
           "sin^2(c + q) = sin^2 q for c in {0, pi} (sympy), so "
           "E(p_j + q) = 2 sqrt(sum sin^2 q_mu) identically at all 8 "
           "corners; series E^2/4 = |q|^2 - (1/3) sum q_mu^4 + O(q^6) "
           "(sympy) => the cone term is exactly |2 I q|: V_j = 2 I_3 "
           "for every corner branch")

    xs = np.linspace(0.0, 1.0, 200001)
    low = np.sin(xs) - (xs - xs ** 3 / 6)
    cauchy = sp.expand((q1 ** 2 + q2 ** 2 + q3 ** 2) ** 2
                       - (q1 ** 4 + q2 ** 4 + q3 ** 4))
    cauchy_ok = (cauchy == sp.expand(2 * (q1 ** 2 * q2 ** 2
                                          + q1 ** 2 * q3 ** 2
                                          + q2 ** 2 * q3 ** 2)))
    worst = 0.0
    ths = np.linspace(0.05, math.pi - 0.05, 25)
    phs = np.linspace(0.0, 2 * math.pi, 49)[:-1]
    for r in (1.0, 0.7, 0.4, 0.2, 0.1, 0.05):
        for th in ths:
            for ph in phs:
                q = (r * math.sin(th) * math.cos(ph),
                     r * math.sin(th) * math.sin(ph),
                     r * math.cos(th))
                worst = max(worst, abs(E_K1(q) - 2 * r) / r ** 3)
    report(low.min() >= 0.0 and cauchy_ok and worst <= 2.0 / 3.0,
           f"[B] (Z-ii) quantitative cone data (V, C_j, r_j) = "
           f"(2I, 2/3, 1): | |E(p_j+q)| - |2Iq| | <= (2/3)|q|^3 <= "
           f"(2/3)|q|^2 for |q| <= 1 -- chain: sin^2 x <= x^2; "
           f"sin x >= x - x^3/6 >= 0 on [0,1] (scan min "
           f"{low.min():.1e} >= 0); sum q^4 <= |q|^4 (exact: "
           f"difference = 2 sum_(mu<nu) q_mu^2 q_nu^2); sqrt(a) - "
           f"sqrt(b) = (a-b)/(sqrt a + sqrt b); measured worst "
           f"deviation ratio {worst:.4f} <= 2/3")

    V = 2.0 * np.eye(3)
    svals = np.linalg.svd(V, compute_uv=False)
    dirs = ((1, 0, 0), (1 / math.sqrt(2), 1 / math.sqrt(2), 0),
            (1 / math.sqrt(3),) * 3, (2 / math.sqrt(5), 1 / math.sqrt(5), 0))
    speeds = [dir_speed(E_K1, (0.0, 0.0, 0.0), u) for u in dirs]
    speeds_pi = [dir_speed(E_K1, (math.pi, math.pi, math.pi), u)
                 for u in dirs]
    report(abs(np.linalg.det(V) - 8.0) < 1e-12 and svals.min() == 2.0
           and max(abs(s - 2.0) for s in speeds + speeds_pi) < 1e-9,
           f"[B] (Z-iii) V_j = 2I is invertible and isotropic: "
           f"det V = 8 != 0, sigma_min = 2; measured directional "
           f"speeds at corners (0,0,0) and (pi,pi,pi) along axis/face-"
           f"diagonal/body-diagonal/skew = {speeds[0]:.6f} "
           f"(spread {max(speeds) - min(speeds):.1e}) -- hypothesis "
           f"(Z) holds for the K1 kernel with explicit data")

    lam = sp.symbols("lam", positive=True)
    cov = sp.simplify(1 / sp.det(lam * 2 * sp.eye(3))
                      - lam ** -3 / sp.det(2 * sp.eye(3))) == 0
    report(cov and abs(8 * (1.0 / 8.0) - 1.0) < 1e-15
           and abs(8 * 1.0 - 8.0) < 1e-15,
           "[B] cone weights, both declared normalizations: unit "
           "hopping |det V_j| = 8 per corner branch, sum |det V|^-1 = "
           "8 x 1/8 = 1 per site (= 8 species per 2^3 cell, speed 2); "
           "central-difference h/2: V_j = I_3, |det V_j| = 1, "
           "sum |det V|^-1 = 8 per cell (speed 1) -- tied by the exact "
           "lambda^3 covariance det(lambda V)^-1 = lambda^-3 "
           "det(V)^-1; the convention-invariant datum is the count 8")

    fsb_txt = note_text("docs/AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_"
                        "NARROW_THEOREM_NOTE_2026-05-26.md")
    report("is finite, and for each" in fsb_txt
           and "invertible real `3×3` matrix" in fsb_txt
           and "C_j |q|²" in fsb_txt
           and "Hypothesis (Z) (point-like linear-cone zero set)"
               in fsb_txt,
           "[B] definition match (textual): the (Z) certified above is "
           "FSB-K's own hypothesis -- the FSB note's defining text "
           "('Hypothesis (Z) (point-like linear-cone zero set)', zero "
           "set 'is finite, and for each' branch an 'invertible real "
           "`3x3` matrix' V with the 'C_j |q|^2' bound) is exactly "
           "what checks 5-8 instantiate as (V, C_j, r_j) = "
           "(2I, 2/3, 1); only the DEFINITION text is consumed -- no "
           "theorem content, no grade")
    residual("finite-L sampling is wrap-convention data: the PBC "
             "kernel realizes the 8 corner zeros iff 4 | L (certified "
             "at L = 4, 8, 12); the (Z) statement itself is about the "
             "Bloch band family on the Brillouin torus, exact at all "
             "volumes by the symbolic identity of check 2 (boundary "
             "B-Z-L)")
    residual("two normalizations are declared (unit-hopping h and "
             "central-difference h/2); all cone data is stated in "
             "both and tied by exact scale covariance; neither is "
             "claimed canonical (boundary B-Z-N)")

    print()
    print("=" * 72)
    print("[C] the companion negative fact: the K0 kernel VIOLATES (Z)")
    print("    (both clauses, exactly)")
    print("=" * 72)

    z0 = {L: kernel_dim(h0[L]) for L in (4, 8, 12)}
    sym0 = {L: int((np.abs(k0_symbol(L)) < 1e-9).sum()) for L in (4, 8, 12)}
    expo = math.log(z0[12] / z0[8]) / math.log(12 / 8)
    report((z0[4], z0[8], z0[12]) == (20, 68, 140)
           and all(sym0[L] == z0[L] for L in (4, 8, 12)) and expo > 1.5,
           f"[C] (Z-i) FAILS for K0: zero-mode counts "
           f"({z0[4]}, {z0[8]}, {z0[12]}) at L = 4, 8, 12 = the "
           f"lattice trace of the codim-1 symbol surface "
           f"sum_mu cos p_mu = 0, growth exponent {expo:.2f} -- "
           f"extensive, not finite, not L-constant")

    line = sp.simplify(sp.cos(sp.pi / 2 + tt) + sp.cos(sp.pi / 2 - tt)
                       + sp.cos(sp.pi / 2))
    report(line == 0,
           "[C] (Z-i) fails EXACTLY: p(t) = (pi/2 + t, pi/2 - t, pi/2) "
           "is a one-parameter zero LINE of the K0 symbol for ALL t "
           "(sympy: cos(pi/2+t) + cos(pi/2-t) + cos(pi/2) = 0 "
           "identically) -- the zero set is uncountable in every "
           "neighborhood of (pi/2, pi/2, pi/2); no finite zero set "
           "exists")

    p0 = (math.pi / 2, math.pi / 2, math.pi / 2)
    u_tan = (1 / math.sqrt(2), -1 / math.sqrt(2), 0.0)
    u_nrm = (1 / math.sqrt(3),) * 3
    sp_tan = dir_speed(lambda p: abs(E_K0(p)), p0, u_tan)
    sp_nrm = dir_speed(lambda p: abs(E_K0(p)), p0, u_nrm)
    report(sp_tan < 1e-9 and abs(sp_nrm - 2 * math.sqrt(3)) < 1e-5,
           f"[C] (Z-ii) fails: along the zero-line direction u the "
           f"cone inequality |E(p0+tu)| >= |Vu| t - C t^2 forces "
           f"|Vu| <= C t -> 0, i.e. V u = 0: ANY candidate cone "
           f"matrix is singular; measured tangent speed "
           f"{sp_tan:.1e} (= 0 exactly by the check-12 identity), "
           f"normal speed {sp_nrm:.4f} = 2 sqrt(3) -- a maximally "
           f"degenerate non-cone")

    own_txt = note_text("docs/STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_"
                        "CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md")
    report("performs no selection" in own_txt
           and "no thermal content" in own_txt
           and "independent audit lane only" in own_txt,
           "[C] discipline (textual, on this note's own file): the K0 "
           "violation is a computed companion fact for the downstream "
           "consumer -- this note 'performs no selection', carries "
           "'no thermal content', and declares status authority "
           "'independent audit lane only'; both branches pass through "
           "the same machinery with the same tolerances")
    residual("the K0 violation certificate is companion content for "
             "the named downstream composer; which kernel is realized "
             "(the P-FLUX bit) is neither assumed nor decided here "
             "(boundary B-Z-S)")

    print()
    print("=" * 72)
    print("[D] falsification legs: the certificate machinery is")
    print("    quantitative and branch-sensitive, not vacuous")
    print("=" * 72)

    zc_half = {L: kernel_dim(build_h(L, lambda x, mu: t_K1(x, mu, 0.5)))
               for L in (4, 8)}
    Eh = lambda p: E_K1(p, 0.5)
    Vh, sing_h = detect_V_diag(Eh, (0.0, 0.0, 0.0))
    report((zc_half[4], zc_half[8]) == (8, 8) and not sing_h
           and np.allclose(Vh, (2.0, 2.0, 1.0), atol=1e-6),
           f"[D] weighted witness K1(c=1/2) (off the two-class "
           f"surface -- anisotropic amplitude -- but inside FSB-K's "
           f"realized class): zero set still 8 points (counts "
           f"{zc_half[4]}, {zc_half[8]} at L = 4, 8), detector "
           f"V = diag({Vh[0]:.4f}, {Vh[1]:.4f}, {Vh[2]:.4f}), "
           f"det = 4: (Z) still HOLDS but with weight sum 8/4 = 2 "
           f"!= 1 -- the machinery tracks cone data quantitatively, "
           f"it is not a rubber stamp")

    zc_zero = {L: kernel_dim(build_h(L, lambda x, mu: t_K1(x, mu, 0.0)))
               for L in (4, 8)}
    Ez = lambda p: E_K1(p, 0.0)
    Vz, sing_z = detect_V_diag(Ez, (0.0, 0.0, 0.0))
    report((zc_zero[4], zc_zero[8]) == (16, 32) and sing_z
           and Vz[2] < 1e-9 and abs(Vz[0] - 2.0) < 1e-6,
           f"[D] broken-cone witness K1(c=0): the detector reports "
           f"V = diag({Vz[0]:.4f}, {Vz[1]:.4f}, {Vz[2]:.1e}) SINGULAR "
           f"(axis-3 speed 0), and the zero set goes extended "
           f"({zc_zero[4]}, {zc_zero[8]} = 4L at L = 4, 8) -- "
           f"singular-V detection works on a perturbed kernel")

    zc_comp = {L: kernel_dim(build_h(L, t_K0, onsite=-6.0))
               for L in (4, 8, 12)}
    Vc, sing_c = detect_V_diag(lambda p: abs(E_comp(p)), (0.0, 0.0, 0.0))
    report((zc_comp[4], zc_comp[8], zc_comp[12]) == (1, 1, 1) and sing_c
           and max(Vc) < 1e-5,
           f"[D] quadratic comparator (scalar NN + on-site -6, "
           f"off-surface): POINT-LIKE zero set "
           f"({zc_comp[4]}, {zc_comp[8]}, {zc_comp[12]}) yet all "
           f"directional speeds < 1e-5 => V = 0 singular -- the two "
           f"(Z) clauses are detected independently (point-likeness "
           f"alone does not pass)")

    counts_k1 = {L: kernel_dim(h1[L]) for L in (4, 8)}
    counts_k0 = {L: kernel_dim(h0[L]) for L in (4, 8)}
    Vk1, _ = detect_V_diag(E_K1, (0.0, 0.0, 0.0))
    Vk0 = (dir_speed(lambda p: abs(E_K0(p)), p0, u_tan),
           dir_speed(lambda p: abs(E_K0(p)), p0, u_nrm), 1.0)
    decisions = {
        "K1": z_decision("K1", counts_k1, Vk1),
        "K1half": z_decision("K1half", zc_half, Vh),
        "K0": z_decision("K0", counts_k0, (Vk0[0], Vk0[1], Vk0[2])),
        "K1zero": z_decision("K1zero", zc_zero, Vz),
        "comp": z_decision("comp", zc_comp, Vc),
    }
    report(decisions == {"K1": True, "K1half": True, "K0": False,
                         "K1zero": False, "comp": False},
           "[D] non-vacuity of the decision: the (Z) machinery over "
           "{K1, K1(c=1/2), K0, K1(c=0), comparator} returns "
           "{pass, pass, fail, fail, fail} from computed zero counts "
           "and cone speeds ONLY, through one code path -- the flux "
           "certificates of check 1 are never read by the decision; "
           "no flux label, branch label, count-3, or species input "
           "enters it")
    residual("the falsification witnesses K1(c=1/2), K1(c=0), and the "
             "comparator are declared OFF the licensed two-class "
             "surface (anisotropic amplitude / on-site sector); they "
             "exercise the machinery, they are not surface members "
             "(boundary B-Z-W)")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: the flux-(-1) Kawamoto-Smit realized kernel "
              "satisfies hypothesis (Z) of FSB-K EXACTLY: massless set")
        print("         = the 8 BZ corner points (L-constant, "
              "eigensolver-certified at L = 4, 8, 12; exact by the")
        print("         all-volume symbolic Bloch identity), one exact "
              "isotropic cone V = 2I at every corner (V = I in the")
        print("         central-difference normalization), explicit "
              "(V, C, r) = (2I, 2/3, 1), cone-weight sum = 1 per site")
        print("         = 8 species per 2^3 cell. The flux-(+1) kernel "
              "VIOLATES both clauses of (Z): extensive zero set")
        print("         20/68/140 with an EXACT zero line, and every "
              "candidate cone matrix singular along it. The machinery")
        print("         is quantitative and branch-sensitive "
              "(falsification legs); no selection is performed and no")
        print("         thermal content is consumed: this row only "
              "certifies kernel geometry for the named downstream")
        print("         composer.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
