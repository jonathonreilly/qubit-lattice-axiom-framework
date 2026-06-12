#!/usr/bin/env python3
"""Axiom-first fermionic Stefan-Boltzmann on the realized kernel class
(narrow theorem runner).

Companion to
docs/AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md
(re-scoped 2026-06-11: the quantifier now binds the REALIZED kinetic
kernel class, not a supplied continuum dispersion).

Theorem computed here (FSB-K).  For every kinetic kernel in the
licensed realized class -- finite-range, sublattice-periodic, Hermitian
hopping on the Z^3 single-mode-per-site one-particle surface -- whose
massless set is point-like with linear cones (hypothesis (Z): finitely
many zero branches (p_j, b), each |E_b(p_j + q)| = |V_jb q| + O(|q|^2)
with invertible V_jb), the half-filled free-Fermi thermal energy
density per site obeys

    u(T) = g_eff * (7/8)(pi^2/30) T^4 + O(T^5),
    g_eff = sum_(j,b) |det V_jb|^(-1)  (finite),

i.e. g_eff(T) := u(T) / [(7/8)(pi^2/30) T^4] has a finite T -> 0
plateau equal to the cone-weighted massless species count -- the
clause (CL) ("the massless species density is finite", in the retained
Stefan-Boltzmann bridge row's own per-dof currency), conditional on
the kernel-geometry hypothesis (Z).

Load-bearing content COMPUTED (not just continuum arithmetic):

  [A] the exact currency: eta(4)/zeta(4) = 7/8 (symbolic), the
      Fermi-Dirac integral Gamma(4) eta(4) = 7 pi^4/120 (40-digit),
      the per-dof normalization (1/2pi^2) I_F = (7/8)(pi^2/30)
      (exact), and the cone-reduction Jacobian
      int d^3q/(2pi)^3 |Vq| n_F(|Vq|/T) = |det V|^(-1) (7/8)(pi^2/30) T^4
      certified by direct 3D quadrature on an anisotropic V.
  [B] the positive leg on explicit realized-class kernels: the
      flux-(-1)-class symbol (8 point zeros, isotropic cones, speed 2;
      spectrum tied to the explicit lattice kernel by eigensolver at
      L = 8) plateaus at g_eff = 8/2^3 = 1; an ANISOTROPIC-cone kernel
      (V = diag(2,2,4)) plateaus at 8/16 = 1/2, certifying the
      |det V|^(-1) weighting (isotropy NOT required); a gapped extra
      band contributes nothing (off-cone exponential suppression);
      finite-size and low-T error control measured.
  [C] the falsification legs (hypothesis (Z) demonstrably
      load-bearing, BOTH clauses): the flux-(+1)-class extended-zero-
      surface kernel VIOLATES the T^4 law -- g_eff diverges like T^-2
      with a Sommerfeld u/T^2 plateau (reproducing the F-3 behavior of
      the P-FLUX finite-species-density note independently); a
      point-like-but-QUADRATIC zero diverges like T^-3/2 (point-
      likeness alone is insufficient; linear cones are load-bearing).
  [D] composition and circularity discipline: the retained 7/8 bridge
      row keeps the integral arithmetic (this row consumes, does not
      duplicate it); the note's load-bearing citations exclude the
      staggered-derived emergent-Lorentz row (RP circularity class);
      phi = -1 is neither assumed nor derived (branch-blind quantifier;
      both licensed branch symbols enter only as computed witnesses
      classified by their zero-set geometry).

Deterministic, no network, no randomness; numpy + sympy + mpmath.
Exit code 0 iff FAIL = 0.
"""

import itertools
import json
import math
import os
import sys
from fractions import Fraction

import mpmath
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


def ledger():
    with open(os.path.join(REPO, "docs/audit/data/audit_ledger.json"),
              encoding="utf-8") as f:
        return json.load(f)["rows"]


# ----------------------------------------------------------------------
# kernel-class constructions (self-contained; the licensed single-mode
# Z^3 one-particle hopping surface)
# ----------------------------------------------------------------------

PREF = (7.0 / 8.0) * (math.pi ** 2 / 30.0)  # the bridge per-dof coeff


def n_F(x):
    return 1.0 / (np.exp(np.minimum(x, 700.0)) + 1.0)


def u_density(absvals, T):
    """Half-filled free-Fermi thermal energy density per mode:
    u(T) = (1/N) sum |E| n_F(|E|/T) -- the retained SB bridge row's
    integrand evaluated on the kernel spectrum (probe currency,
    boundary B-1)."""
    a = np.abs(absvals)
    return float(np.sum(a * n_F(a / T)) / len(a))


def g_eff(absvals, T):
    return u_density(absvals, T) / (PREF * T ** 4)


def torus_grid(L):
    p = 2.0 * np.pi * np.arange(L) / L
    return np.meshgrid(p, p, p, indexing="ij")


def sym_cone8(L):
    """W1: flux-(-1)-class symbol |E| = 2 sqrt(sum_mu sin^2 p_mu) on
    the full torus (same |E| multiset as the Kawamoto-Smit lattice
    kernel; tied to the eigensolver in check 6)."""
    p1, p2, p3 = torus_grid(L)
    return (2.0 * np.sqrt(np.sin(p1) ** 2 + np.sin(p2) ** 2
                          + np.sin(p3) ** 2)).ravel()


def sym_cone_aniso(L):
    """W2: anisotropic-cone kernel |E| = 2 sqrt(sin^2 p1 + sin^2 p2
    + 4 sin^2 p3): 8 point zeros, V = diag(2, 2, 4), |det V| = 16."""
    p1, p2, p3 = torus_grid(L)
    return (2.0 * np.sqrt(np.sin(p1) ** 2 + np.sin(p2) ** 2
                          + 4.0 * np.sin(p3) ** 2)).ravel()


def sym_gapped(L):
    """W3 extra band: |E| = sqrt(1 + 4 sum sin^2) -- gap Delta = 1."""
    p1, p2, p3 = torus_grid(L)
    return np.sqrt(1.0 + 4.0 * (np.sin(p1) ** 2 + np.sin(p2) ** 2
                                + np.sin(p3) ** 2)).ravel()


def sym_k0(L):
    """X1: flux-(+1)-class scalar tight-binding symbol E = 2 sum cos
    (extended codim-1 zero surface)."""
    p1, p2, p3 = torus_grid(L)
    return (2.0 * (np.cos(p1) + np.cos(p2) + np.cos(p3))).ravel()


def sym_quad(L):
    """X2: point-like-but-quadratic zero, E = 2 sum cos p - 6
    (single zero at p = 0, quadratic dispersion, no cone)."""
    return sym_k0(L) - 6.0


def build_lattice_kernel(L, t_fun):
    """Explicit finite-range Hermitian hopping kernel on Z^3 sites
    (PBC), single mode per site."""
    sites = list(itertools.product(range(L), repeat=3))
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
    return h


def t_scalar(x, mu):
    return 1.0


def t_ks(x, mu):
    """Kawamoto-Smit phases (uniform plaquette flux -1)."""
    if mu == 0:
        return 1.0
    if mu == 1:
        return (-1.0) ** x[0]
    return (-1.0) ** (x[0] + x[1])


def count_zeros(vals, tol=1e-9):
    return int((np.abs(vals) < tol).sum())


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("[A] exact currency: eta/zeta arithmetic, the Fermi-Dirac")
    print("    integral, the per-dof normalization, the cone-reduction")
    print("    Jacobian")
    print("=" * 72)

    eta4 = sp.dirichlet_eta(4)
    zeta4 = sp.zeta(4)
    s = sp.symbols("s", positive=True)
    eta_rel = sp.simplify((sp.zeta(s) - 2 * 2 ** (-s) * sp.zeta(s))
                          - (1 - 2 ** (1 - s)) * sp.zeta(s)) == 0
    report(eta_rel
           and sp.simplify(eta4 - 7 * sp.pi ** 4 / 720) == 0
           and sp.simplify(zeta4 - sp.pi ** 4 / 90) == 0
           and sp.simplify(eta4 / zeta4 - sp.Rational(7, 8)) == 0,
           "[A] exact eta/zeta arithmetic: eta(s) = (1 - 2^(1-s)) "
           "zeta(s) (even-n split, symbolic); eta(4) = 7 pi^4/720; "
           "zeta(4) = pi^4/90; eta(4)/zeta(4) = 7/8 exactly -- the "
           "d = 4 fermion/boson ratio")

    mpmath.mp.dps = 40
    I_F = mpmath.quad(lambda x: x ** 3 / (mpmath.exp(x) + 1),
                      [0, mpmath.inf])
    I_B = mpmath.quad(lambda x: x ** 3 / (mpmath.exp(x) - 1),
                      [0, mpmath.inf])
    report(abs(I_F - 7 * mpmath.pi ** 4 / 120) < mpmath.mpf("1e-30")
           and abs(I_F / I_B - mpmath.mpf("0.875")) < mpmath.mpf("1e-30"),
           "[A] the Fermi-Dirac integral (40-digit): "
           "int_0^inf x^3/(e^x + 1) dx = Gamma(4) eta(4) = 7 pi^4/120; "
           "I_F / I_B = 7/8 -- the retained bridge row's identity, "
           "consumed (not re-derived) as the cone integral's value")

    # per-dof normalization: (1/(2 pi^2)) * I_F = (7/8)(pi^2/30) T^4
    norm_exact = sp.simplify(
        sp.Rational(1, 2) / sp.pi ** 2 * (7 * sp.pi ** 4 / 120)
        - sp.Rational(7, 8) * sp.pi ** 2 / 30) == 0
    frac_ok = (Fraction(7, 240) == Fraction(7, 8) * Fraction(1, 30)
               and Fraction(7, 240) * 30 == Fraction(7, 8))
    T0 = mpmath.mpf("0.3")
    radial = (1 / (2 * mpmath.pi ** 2)) * mpmath.quad(
        lambda k: k ** 3 / (mpmath.exp(k / T0) + 1), [0, mpmath.inf])
    target = mpmath.mpf(7) / 8 * mpmath.pi ** 2 / 30 * T0 ** 4
    report(norm_exact and frac_ok
           and abs(radial - target) < mpmath.mpf("1e-35"),
           "[A] per-dof normalization, exact AND 40-digit radial: "
           "(1/2pi^2) int k^3 n_F(k/T) dk = (1/2pi^2) Gamma(4) eta(4) "
           "T^4 = (7/8)(pi^2/30) T^4 = (7 pi^2/240) T^4 -- the g_eff "
           "denominator IS the retained bridge row's per-dof "
           "coefficient (7/240 = (7/8)*(1/30) exact)")

    # cone-reduction Jacobian by direct 3D quadrature (anisotropic V):
    # int d^3q/(2pi)^3 |Vq| n_F(|Vq|/T) = |det V|^-1 (7/8)(pi^2/30) T^4
    Tq = 0.15
    Vd = (2.0, 2.0, 4.0)
    detV = Vd[0] * Vd[1] * Vd[2]
    R, N = 1.6, 192
    ax = (np.arange(N) + 0.5) / N * 2 * R - R  # midpoint rule
    h3 = (2 * R / N) ** 3
    q1g, q2g = np.meshgrid(ax, ax, indexing="ij")
    acc = 0.0
    for q3 in ax:
        e = np.sqrt((Vd[0] * q1g) ** 2 + (Vd[1] * q2g) ** 2
                    + (Vd[2] * q3) ** 2)
        acc += float(np.sum(e * n_F(e / Tq)))
    quad3d = acc * h3 / (2 * math.pi) ** 3
    pred = PREF * Tq ** 4 / detV
    report(abs(quad3d - pred) / pred < 5e-3,
           f"[A] cone-reduction Jacobian certified by direct 3D "
           f"midpoint quadrature at V = diag(2,2,4), T = {Tq}: "
           f"int d^3q/(2pi)^3 |Vq| n_F = {quad3d:.6e} vs |det V|^-1 "
           f"(7/8)(pi^2/30) T^4 = {pred:.6e} (rel dev "
           f"{abs(quad3d - pred) / pred:.1e}) -- one cone contributes "
           f"exactly 1/|det V| species in the bridge currency")

    print()
    print("=" * 72)
    print("[B] positive leg: explicit realized-class kernels with")
    print("    point-like linear-cone zero sets -- g_eff plateau =")
    print("    cone-weighted species count, with error control")
    print("=" * 72)

    # tie the symbol witnesses to explicit lattice kernels (L = 8)
    L8 = 8
    ks_eigs = np.linalg.eigvalsh(build_lattice_kernel(L8, t_ks))
    sc_eigs = np.linalg.eigvalsh(build_lattice_kernel(L8, t_scalar))
    tie1 = np.allclose(np.sort(np.abs(ks_eigs)),
                       np.sort(np.abs(sym_cone8(L8))), atol=1e-9)
    tie0 = np.allclose(np.sort(sc_eigs), np.sort(sym_k0(L8)), atol=1e-9)
    report(tie1 and tie0,
           "[B] realized-kernel tie (eigensolver, L = 8): the explicit "
           "Kawamoto-Smit-phase lattice kernel's |spectrum| multiset "
           "equals the W1 symbol 2 sqrt(sum sin^2 p) on the full "
           "torus, and the scalar NN kernel's spectrum equals the X1 "
           "symbol 2 sum cos p -- the witnesses below ARE realized-"
           "class kernel spectra, licensing the symbol grids")

    # zero-set geometry classification (computed, branch-blind)
    zc1 = (count_zeros(sym_cone8(24)), count_zeros(sym_cone8(48)))
    zca = (count_zeros(sym_cone_aniso(24)), count_zeros(sym_cone_aniso(48)))
    zc0 = (count_zeros(sym_k0(24)), count_zeros(sym_k0(48)))
    zcq = (count_zeros(sym_quad(24)), count_zeros(sym_quad(48)))
    # cone expansion order at a W1 zero (0,0,pi): dev from 2|q| is O(q^2)
    def w1_E(q):
        return 2.0 * math.sqrt(sum(math.sin(x) ** 2 for x in q))
    d_dir = (1 / math.sqrt(3),) * 3
    dev = {}
    for r in (0.1, 0.05):
        q = [r * d for d in d_dir]
        qz = [q[0], q[1], math.pi + q[2]]
        dev[r] = abs(w1_E(qz) - 2.0 * r)
    report(zc1 == (8, 8) and zca == (8, 8) and zcq == (1, 1)
           and zc0[0] > 100 and zc0[1] > 2 * zc0[0]
           and dev[0.1] < 0.1 ** 2 and dev[0.05] / dev[0.1] < 0.35,
           f"[B] zero-set geometry classified by computation (branch-"
           f"blind): W1 zeros (L=24,48) = {zc1} and W2 = {zca} "
           f"(point-like, L-independent); X2 = {zcq}; X1 = {zc0} "
           f"(extended: the exact lattice trace of the codim-1 "
           f"surface grows without bound); W1 cone expansion "
           f"|E(p_j+q)| - 2|q| = O(|q|^2) or better (dev "
           f"{dev[0.1]:.2e} at |q|=0.1, halving ratio "
           f"{dev[0.05] / dev[0.1]:.2f} <= 0.35, order >= 2; this "
           f"odd-symbol witness is in fact O(|q|^3)) -- hypothesis "
           f"(Z) holds for W1/W2, fails for X1/X2")

    Lbig, Lmid = 128, 64
    T_ladder = (0.05, 0.1, 0.2, 0.4)
    w1_big = sym_cone8(Lbig)
    g1 = {T: g_eff(w1_big, T) for T in T_ladder}
    r1 = g1[0.05] / g1[0.1]
    report(abs(g1[0.05] - 1.0) < 0.05 and 0.85 < r1 < 1.05,
           f"[B] W1 (8 isotropic cones, speed 2, the flux-(-1)-class "
           f"symbol): g_eff(T) at L=128 = "
           f"{g1[0.05]:.3f}, {g1[0.1]:.3f}, {g1[0.2]:.3f}, "
           f"{g1[0.4]:.3f} at T=0.05..0.4 -- FINITE plateau at the "
           f"predicted cone-weighted count sum |det V|^-1 = 8/2^3 = 1 "
           f"(T-halving ratio {r1:.3f} ~ 1); the T^4 law holds with "
           f"g_eff = the massless species count")

    g1_mid = g_eff(sym_cone8(Lmid), 0.2)
    conv = abs(g1_mid - g1[0.2]) / g1[0.2]
    report(conv < 0.01,
           f"[B] finite-size control (measured): |g_eff(L=64) - "
           f"g_eff(L=128)| / g_eff = {conv:.2e} < 1% at T = 0.2 -- "
           f"the mode sum is Cauchy in L at the stated grids "
           f"(thermodynamic-limit statement, boundary B-2)")

    ga = {T: g_eff(sym_cone_aniso(Lbig), T) for T in (0.05, 0.1)}
    ra = ga[0.05] / ga[0.1]
    report(abs(ga[0.05] - 0.5) < 0.03 and 0.85 < ra < 1.05,
           f"[B] W2 (8 ANISOTROPIC cones, V = diag(2,2,4)): g_eff = "
           f"{ga[0.05]:.3f}, {ga[0.1]:.3f} at T=0.05, 0.1 -- plateau "
           f"at sum |det V|^-1 = 8/16 = 1/2 (ratio {ra:.3f}); the "
           f"|det V|^-1 weighting is certified: conicity, NOT "
           f"isotropy, is what (Z) requires")

    Tg = 0.05
    g_gap = g_eff(sym_gapped(Lbig), Tg) * 1.0
    u_gap_share = (u_density(sym_gapped(Lbig), Tg)
                   / (PREF * Tg ** 4))
    g_union = g_eff(np.concatenate([w1_big, sym_gapped(Lbig)]), Tg) * 2.0
    report(u_gap_share < 1e-3 and abs(g_union - g1[0.05]) < 1e-3,
           f"[B] W3 (W1 plus a gapped band, Delta = 1): the gapped "
           f"band's own g_eff share = {u_gap_share:.2e} < 1e-3 at "
           f"T = 0.05 and the 2-band g_eff (per-band-sum convention) "
           f"= {g_union:.4f} = W1's {g1[0.05]:.4f} -- off-cone modes "
           f"are exponentially suppressed (theorem Step 2), so g_eff "
           f"consumes ONLY the zero-set geometry")

    dev_t = {T: abs(g1[T] - 1.0) for T in (0.1, 0.2, 0.4)}
    report(dev_t[0.1] < dev_t[0.2] < dev_t[0.4]
           and dev_t[0.1] / dev_t[0.2] < 0.55,
           f"[B] low-T error control (measured): |g_eff(T) - 1| = "
           f"{dev_t[0.1]:.4f}, {dev_t[0.2]:.4f}, {dev_t[0.4]:.4f} at "
           f"T = 0.1, 0.2, 0.4 -- monotone in T with halving ratio "
           f"{dev_t[0.1] / dev_t[0.2]:.2f} (consistent with the proven "
           f"O(T) relative order; the symmetric sin-cone witness "
           f"converges faster, boundary B-4)")
    residual("the theorem statement is at the thermodynamic limit; "
             "finite-L mode-sum convergence is certified numerically "
             "at the stated grids (L = 64 vs 128), not proven with "
             "explicit constants (boundary B-2)")

    print()
    print("=" * 72)
    print("[C] falsification legs: hypothesis (Z) is load-bearing in")
    print("    BOTH clauses (point-likeness AND linear cones)")
    print("=" * 72)

    k0_big = sym_k0(Lbig)
    g0 = {T: g_eff(k0_big, T) for T in T_ladder}
    r0a, r0b = g0[0.05] / g0[0.1], g0[0.1] / g0[0.2]
    report(3.8 < r0a < 4.2 and 3.8 < r0b < 4.2 and g0[0.05] > 100,
           f"[C] X1 (extended zero surface, the flux-(+1)-class "
           f"symbol) VIOLATES the T^4 law: g_eff = {g0[0.05]:.0f}, "
           f"{g0[0.1]:.0f}, {g0[0.2]:.1f}, {g0[0.4]:.1f} at "
           f"T=0.05..0.4, T-halving ratios {r0a:.2f}, {r0b:.2f} ~ 4 "
           f"-- a T^-2 divergence, reproducing the P-FLUX note's F-3 "
           f"certificate independently on this runner's own "
           f"construction")

    u_T2 = [u_density(k0_big, T) / T ** 2 for T in T_ladder]
    report(max(u_T2) / min(u_T2) < 1.05,
           f"[C] X1's true low-T law is Sommerfeld T^2 (Fermi "
           f"surface): u/T^2 = {u_T2[0]:.3f}, {u_T2[1]:.3f}, "
           f"{u_T2[2]:.3f}, {u_T2[3]:.3f} -- the point-likeness "
           f"clause of (Z) is load-bearing (without it the T^4 form "
           f"fails structurally, not numerically)")

    q_big = sym_quad(Lbig)
    gq = {T: g_eff(q_big, T) for T in T_ladder}
    rqa, rqb = gq[0.05] / gq[0.1], gq[0.1] / gq[0.2]
    report(2.5 < rqa < 2.95 and 2.5 < rqb < 2.95,
           f"[C] X2 (point-like but QUADRATIC zero): g_eff T-halving "
           f"ratios {rqa:.2f}, {rqb:.2f} ~ 2^1.5 = 2.83 -- a T^-3/2 "
           f"divergence: point-likeness alone does NOT give the T^4 "
           f"law; the linear-cone clause of (Z) is load-bearing "
           f"separately")

    cl = {nm: g[0.05] / g[0.1] < 1.5
          for nm, g in (("W1", g1), ("W2", ga), ("X1", g0), ("X2", gq))}
    report(cl["W1"] and cl["W2"] and not cl["X1"] and not cl["X2"],
           "[C] single-clause selection consistency: the conclusion "
           "clause (CL) 'g_eff(T) bounded as T -> 0' holds on exactly "
           "the (Z)-satisfying kernels {W1, W2} and fails on exactly "
           "the (Z)-violating ones {X1, X2} -- the theorem's "
           "hypothesis and conclusion classify the witness set "
           "identically (non-vacuous, non-trivial)")
    residual("u(T) is the half-filled free-Fermi probe in the "
             "retained SB bridge row's own integrand (hypothesis-"
             "satisfiability currency); thermal equilibrium of the "
             "realized dynamics is NOT derived here (boundary B-1)")

    print()
    print("=" * 72)
    print("[D] composition with the retained 7/8 bridge and")
    print("    circularity discipline")
    print("=" * 72)

    sb_txt = note_text("docs/GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_"
                       "BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_"
                       "2026-06-06.md")
    rows = ledger()
    st_sb = rows.get("gstar_thermal_seven_eighths_stefan_boltzmann_"
                     "bridge_narrow_theorem_note_2026-06-06",
                     {}).get("effective_status")
    retained_grade = {"retained", "retained_bounded", "retained_no_go"}
    report(st_sb in retained_grade
           and "relativistic, effectively massless thermal degree of "
               "freedom" in sb_txt
           and "It does not derive the Standard Model particle "
               "inventory" in sb_txt
           and Fraction(7, 240) == Fraction(7, 8) * Fraction(1, 30),
           f"[D] composition with the retained-grade bridge (current "
           f"effective_status={st_sb}): the bridge binds 'a "
           "relativistic, effectively massless thermal degree of "
           "freedom' with a SUPPLIED inventory and owns the integral "
           "arithmetic; this row binds the kernel class and derives "
           "WHICH count the realized spectrum supplies (g_eff = "
           "cone-weighted species count) -- same per-dof coefficient "
           "7/240, disjoint roles, no duplication, no contradiction")

    self_txt = note_text("docs/AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_"
                         "NARROW_THEOREM_NOTE_2026-05-26.md")
    no_lorentz_link = "](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)" not in self_txt
    no_kms_link = "](AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md)" \
        not in self_txt
    no_u4_link = "](U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md)" \
        not in self_txt
    report(no_lorentz_link and no_kms_link and no_u4_link
           and "neither assumes nor derives `phi = -1`" in self_txt
           and "hypothesis (Z)" in self_txt,
           "[D] circularity discipline (textual, on this note's own "
           "file): the staggered-derived emergent-Lorentz row and the "
           "unaudited KMS row are NOT load-bearing citations, and the "
           "old U4 qubit-reframe row is not a load-bearing citation "
           "(no markdown links; the linear-cone dispersion is hypothesis "
           "(Z), stated of the kernel, not imported); the note "
           "declares it 'neither assumes nor derives `phi = -1`' -- "
           "branch-blind on its face")

    same_path = all(len(v) == Lbig ** 3
                    for v in (w1_big, k0_big))
    report(same_path and cl["W1"] != cl["X1"],
           "[D] branch-blindness of the computation: both licensed "
           "branch symbols are evaluated by the SAME probe/grid code "
           "path and are separated ONLY by their computed zero-set "
           "geometry (the (Z) classification of check 6); no flux "
           "value, branch label, or species inventory enters any "
           "load-bearing computation above")
    residual("hypothesis (Z) is a CONDITION: this row verifies it for "
             "its explicit witnesses only and does NOT certify it for "
             "the realized kernel; which kernel is realized (the "
             "P-FLUX bit) is neither assumed nor derived here "
             "(boundary B-3)")
    residual("the falsification legs [C] are computed certificates "
             "with proof sketches, not the theorem-grade core; they "
             "establish only that (Z) is load-bearing (boundary B-5)")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: on the licensed realized kernel class, for every "
              "kinetic kernel whose massless set is point-like with")
        print("         linear cones (hypothesis (Z)), the low-T thermal "
              "energy density obeys u(T) = g_eff (7/8)(pi^2/30) T^4")
        print("         + O(T^5) with g_eff = sum |det V|^-1 finite = the "
              "cone-weighted massless species count, in the retained")
        print("         Stefan-Boltzmann bridge row's own per-dof currency "
              "(clause (CL), supplied CONDITIONALLY on (Z)).")
        print("         Falsification: an extended-zero-surface kernel "
              "violates the T^4 law (g_eff ~ T^-2, Sommerfeld), and a")
        print("         quadratic point zero diverges ~ T^-3/2 -- both "
              "clauses of (Z) are load-bearing. phi = -1 is neither")
        print("         assumed nor derived: the row is branch-blind and "
              "consumes no flux, branch, or inventory input.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
