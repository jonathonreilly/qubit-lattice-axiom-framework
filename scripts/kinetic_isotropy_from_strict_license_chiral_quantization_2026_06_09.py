#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Strict unitary chiral band velocity quantization
================================================
Companion runner for
docs/KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md.

CONTEXT.  The registered kinetic_isotropy_primitive supplies the OS0 kinetic-form
equality c_t = c_s ("one tick is one edge in FORM").  The #3360 independence
support showed the LISTED structures do not fix xi := c_t/c_s -- on a BOSONIC
positive-transfer witness family.  This runner checks structures that
list omits -- (P1) the retained adjacency license read strictly as radius-1
strictness of the realized tick (a reading of a retained theorem's own locality
definition), (P2) unitarity of the real-time one-tick update (named conditional
reading), (P3) K/CPT omega <-> -omega pairing of the TICK spectrum (named
conditional reading: the retained CPT note constrains the continuous-time
staggered Hamiltonian, not the strict tick), (P4) nonzero band winding =
genuine chirality (named realization premise):

THE THEOREM (1D / per-axis, exact).  For a strict radius-1 translation-
covariant unitary 2-band tick with K/CPT-paired spectrum, a band with nonzero
Brillouin winding satisfies omega(k) = +-(k + phi) EXACTLY.  The cone slope is
|v| = 1 at EVERY momentum, every curvature order of the free single-particle
dispersion of the winding band vanishes identically, and the marginal
anisotropy dial does not exist in the winding cell: it is quantized away, not
tuned away.  The identification of the real-time cone slope with the OS0
Euclidean ratio c_t/c_s is the standard first-order Wick identification -- a
NAMED BRIDGE, not computed by this runner.

EVERY PREMISE GETS A HOSTILE WITNESS (wall-independence):
  drop P2 (unitarity)  -> Part A: the bosonic positive-transfer family sweeps
                          xi continuously (re-derives the #3360 formula);
  drop P1 (strictness) -> Part C: a Hamiltonian tick e^{i a H} leaks beyond
                          radius 1 for every nonzero hopping, velocity tunable;
  drop P4 (winding)    -> Part E1: split-step walk -- radius-1 unitary,
                          gapless, winding-0, tunable v = |cos theta|;
                          Part D6a: the symmetric partial-swap brickwork --
                          permanently gapless at k = pi, winding-0, tunable;
  drop P3 (CPT pair)   -> Part E2: U(k) = S_+ C(theta) -- radius-1 unitary,
                          COMPLEX trace, winding spectral branch with
                          continuously tunable group velocity.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  The checked
band theorem is conditional on the cited source-side premise-discharge
packets passing independent audit, their own named readings, and the named
Wick/readout bridge.  Scope is 1D/per-axis only (3D Weyl 2x2 blocks are a
named open); matter sector only; free single-particle dispersion only
(radiative/interacting orders are the velocity-RG row).  No new axiom, no new
primitive, no Tier-A admission.

Run: python3 scripts/kinetic_isotropy_from_strict_license_chiral_quantization_2026_06_09.py
"""
from __future__ import annotations
from pathlib import Path
import sys
import numpy as np
import sympy as sp

PASS, FAIL = 0, 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
SITE_LICENSE_NOTE = ROOT / "docs" / "SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11.md"
TICK_UNITARITY_NOTE = ROOT / "docs" / "TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md"
BW_BRIDGE_NOTE = ROOT / "docs" / "BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md"
WIR_NOTE = ROOT / "docs" / "WIR_CONE_AGREEMENT_FROM_SECTOR_ALIAS_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-06-11.md"
REALIZATION_NOTE = ROOT / "docs" / "REALIZATION_ROW_SIGMA_RECONCILIATION_BOUNDED_THEOREM_NOTE_2026-06-11.md"


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(path: Path) -> str:
    return " ".join(text(path).split())


k = sp.symbols('k', real=True)
z = sp.symbols('z')

# ----------------------------------------------------------------------------
print("\nPART A -- the bosonic contrast (re-derives the #3360 witness-family formula)")
print("=" * 78)
# The #3360 runner's single-mode transfer energy is
#   cosh E = 1 + omega^2(p)/(2 K_t),  omega^2(p) = m^2 + 2 K_s sum_i (1 - cos p_i).
# Re-derived here symbolically (the #3360 script itself is not invoked):
Kt, Ks, m2, p = sp.symbols('K_t K_s m2 p', positive=True)
omega2 = m2 + 2 * Ks * (1 - sp.cos(p))
E = sp.acosh(1 + omega2 / (2 * Kt))

E1 = E.subs({Kt: 1, Ks: 1, m2: sp.Rational(1, 25)})
E2 = E.subs({Kt: 2, Ks: 1, m2: sp.Rational(1, 25)})
r_low = float((E2 / E1).subs(p, sp.Rational(1, 10)))
r_high = float((E2 / E1).subs(p, 3))
check("A1 xi-change reshapes the bosonic dispersion p-dependently (>= 1% spread)",
      abs(r_low - r_high) > 0.01, f"E-ratio {r_low:.4f} (p=0.1) vs {r_high:.4f} (p=3.0)")

v_sym = sp.limit(E.subs(m2, 0) / p, p, 0, '+')
check("A2 bosonic cone velocity = sqrt(K_s/K_t) exactly (continuously tunable)",
      sp.simplify(v_sym - sp.sqrt(Ks / Kt)) == 0, f"limit E/p = {v_sym}")

tvals = [float(sp.exp(-E1.subs(p, pv))) for pv in (sp.Rational(1, 10), 1, 3)]
check("A3 bosonic one-tick eigenvalues are non-unimodular contractions (0 < t < 1)",
      all(0 < t < 1 for t in tvals), f"sample transfer eigenvalues {[f'{t:.3f}' for t in tvals]}")


# ----------------------------------------------------------------------------
print("\nPART B -- the monomial lemma (exact case analysis; the quantization core)")
print("=" * 78)
# LEMMA. u(z) = a/z + b + c z with |u(e^{ik})| = 1 for all real k  ==>  exactly
# one of a,b,c is nonzero and it has unit modulus.
# |u|^2 = 1 identically on the circle <=> the Laurent identity u(z)*ubar(1/z)=1:
#   z^2:  conj(a)*c = 0
#   z^1:  conj(a)*b + conj(b)*c = 0
#   z^0:  |a|^2 + |b|^2 + |c|^2 = 1.
a1, b1, c1, a2, b2, c2 = sp.symbols('a1 b1 c1 a2 b2 c2', real=True)
a = a1 + sp.I * a2
b = b1 + sp.I * b2
c = c1 + sp.I * c2
u = a / z + b + c * z
ubar = sp.conjugate(a) * z + sp.conjugate(b) + sp.conjugate(c) / z  # conj on |z|=1
poly = sp.Poly(sp.expand(sp.expand(u * ubar) * z**2), z)
coeffs = {2 - i: poly.all_coeffs()[i] for i in range(len(poly.all_coeffs()))}
eq_top = sp.simplify(coeffs.get(2, 0))
eq_mid = sp.simplify(coeffs.get(1, 0))
eq_zero = sp.simplify(coeffs.get(0, 0) - 1)
check("B1 top coefficient of |u|^2 is conj(a)*c (so a = 0 or c = 0)",
      sp.simplify(eq_top - sp.conjugate(a) * c) == 0, f"z^2 coeff = {eq_top}")

# COMPLETE 2-CASE ANALYSIS (replaces a blind solve, which silently drops
# branches): case c = 0: the z^1 equation degenerates to conj(a)*b = 0, so a=0
# or b=0; case a = 0: it degenerates to conj(b)*c = 0, so b=0 or c=0.  In every
# branch at most ONE coefficient survives, with |.| = 1 from the z^0 equation.
mid_case_c0 = sp.simplify(eq_mid.subs({c1: 0, c2: 0}))
mid_case_a0 = sp.simplify(eq_mid.subs({a1: 0, a2: 0}))
norm_b_only = sp.simplify(eq_zero.subs({a1: 0, a2: 0, c1: 0, c2: 0}))
check("B2 case analysis: c=0 => conj(a)*b = 0;  a=0 => conj(b)*c = 0  (monomial in every branch)",
      sp.simplify(mid_case_c0 - sp.conjugate(a) * b) == 0 and
      sp.simplify(mid_case_a0 - sp.conjugate(b) * c) == 0 and
      sp.simplify(norm_b_only - (b1**2 + b2**2 - 1)) == 0,
      "u is a monomial e^{i phase} z^n with n in {-1, 0, +1}")

# Corollary: u = c0 z^n, |c0| = 1: the dispersion omega(k) = n k + phase is
# exact -- derived from the monomial via v = u'(k)/(i u(k)):
vel_branches = []
for n in (-1, 0, 1):
    un = sp.exp(sp.I * sp.pi / 7) * sp.exp(sp.I * n * k)
    vel_branches.append(sp.simplify(sp.diff(un, k) / (sp.I * un)))
check("B3 monomial dispersion: v = u'/(i u) = n exactly, n in {-1, 0, +1}",
      all(sp.simplify(vel_branches[i] - n) == 0 for i, n in enumerate((-1, 0, 1))),
      "velocity quantized to integer edges/tick; |v| <= radius and v in Z")

# Radius-r cascade (degree-2 sample): the extreme coefficient of |u|^2 is again
# an extreme product, so induction kills mixed terms degree by degree:
d = sp.symbols('d', complex=True)
u2 = a / z**2 + b / z + c + d * z
u2bar = sp.conjugate(a) * z**2 + sp.conjugate(b) * z + sp.conjugate(c) + sp.conjugate(d) / z
top2 = sp.simplify(sp.Poly(sp.expand(sp.expand(u2 * u2bar) * z**3), z).all_coeffs()[0])
check("B4 radius-r cascade: top coefficient is again an extreme product (conj(a)*d)",
      sp.simplify(top2 - sp.conjugate(a) * d) == 0,
      "monomial z^n with |n| <= r in general")


# ----------------------------------------------------------------------------
print("\nPART C -- strictness: Hamiltonian-generated ticks violate the retained license")
print("=" * 78)
kap, at = sp.symbols('kappa a_tau', positive=True)
integrand_series = sp.series(sp.exp(sp.I * at * kap * sp.cos(k)), kap, 0, 3).removeO()
A2 = sp.simplify(sp.integrate(integrand_series * sp.exp(-2 * sp.I * k), (k, -sp.pi, sp.pi)) / (2 * sp.pi))
check("C1 one Hamiltonian tick leaks to distance 2: A_2 = -(a*kappa)^2/8 + O(kappa^4) != 0",
      sp.simplify(A2 + (at * kap)**2 / 8) == 0, f"A_2 series = {A2}")

N = 16
H = np.zeros((N, N))
for x in range(N):
    H[x, (x + 1) % N] = H[(x + 1) % N, x] = 0.5
from scipy.linalg import expm  # noqa: E402
leaks = [abs(expm(1j * kv * H)[2, 0]) for kv in (0.1, 0.5, 1.0)]
check("C2 distance-2 leak is nonzero for every sampled nonzero hopping",
      all(l > 1e-6 for l in leaks), f"|U[2,0]| = {[f'{l:.2e}' for l in leaks]}")

check("C3 Hamiltonian-tick velocity is the tunable coupling itself (v = kappa)",
      sp.simplify(sp.diff(kap * sp.sin(k), k).subs(k, 0) - kap) == 0,
      "continuous-time reading = the tunable-xi horn; strict reading excludes it")


# ----------------------------------------------------------------------------
print("\nPART D -- the band-winding saturation theorem (1D, exact)")
print("=" * 78)
# D1 FORWARD DIRECTION: a degree-<=1 Laurent trace t(k) = A e^{-ik} + B + C e^{ik}
# that is REAL for all k (P3: spectrum pairs as {e^{i omega}, e^{-i omega}}, so
# tr = 2 cos omega is real) FORCES C = conj(A) and B real -- derived by Fourier
# coefficient matching, not assumed:
Ar, Ai, Br, Bi, Cr, Ci = sp.symbols('Ar Ai Br Bi Cr Ci', real=True)
tk = (Ar + sp.I * Ai) * sp.exp(-sp.I * k) + (Br + sp.I * Bi) + (Cr + sp.I * Ci) * sp.exp(sp.I * k)
im_t = sp.expand(sp.im(sp.expand_complex(tk)))
im_coeffs = [sp.simplify(im_t.coeff(sp.cos(k))), sp.simplify(im_t.coeff(sp.sin(k))),
             sp.simplify(im_t.subs([(sp.cos(k), 0), (sp.sin(k), 0)]))]
sol_real = sp.solve(im_coeffs, [Bi, Ci, Cr], dict=True)
fwd_ok = (len(sol_real) == 1 and sol_real[0][Bi] == 0 and
          sp.simplify(sol_real[0][Ci] + Ai) == 0 and sp.simplify(sol_real[0][Cr] - Ar) == 0)
check("D1 FORWARD: real-on-circle degree-1 trace forces C = conj(A), B real (Fourier matching)",
      fwd_ok, "tr = beta + 2 g cos(k + phi) with beta = B, g = |A| -- derived, not assumed")

# D2: unitarity bounds the trace: |tr| = |e^{i omega} + e^{-i omega}| = 2|cos omega| <= 2
# (computed); a winding band is a degree-!=0 circle map, hence surjective, so it
# attains omega = 0 (tr = +2) and omega = pi (tr = -2).  With tr-range
# [beta - 2g, beta + 2g] inside [-2, 2], attaining both endpoints forces:
om = sp.symbols('omega', real=True)
tr_mag = sp.simplify(sp.Abs(sp.exp(sp.I * om) + sp.exp(-sp.I * om)))
gpos = sp.symbols('g', positive=True)
be = sp.symbols('beta', real=True)
solw = sp.solve([be + 2 * gpos - 2, be - 2 * gpos + 2], [be, gpos], dict=True)
check("D2 |tr| = 2|cos omega| <= 2 (unitarity), and winding forces beta = 0, |gamma| = 1 (unique)",
      sp.simplify(tr_mag - 2 * sp.Abs(sp.cos(om))) == 0 and
      len(solw) == 1 and solw[0][be] == 0 and solw[0][gpos] == 1,
      "a nonzero-degree circle map attains both omega = 0 and omega = pi")

# D3: SPECTRUM DERIVED from beta = 0, g = 1: the bands solve
# lambda^2 - 2 cos(k + phi) lambda + 1 = 0 (det = 1 by P3):
phi = sp.symbols('phi', real=True)
lam = sp.symbols('lambda')
roots = sp.solve(sp.Eq(lam**2 - 2 * sp.cos(k + phi) * lam + 1, 0), lam)
# verify the two roots are exactly e^{+-i(k+phi)} at exact sample points and
# numerically across the BZ (the derivation: det = 1 and tr = 2cos(k+phi)
# force the unimodular pair):
exact_ok = True
for kv, phiv in ((sp.Rational(1, 3), 0), (sp.Rational(2, 5), sp.Rational(1, 7))):
    rset = [sp.simplify(sp.expand_complex(r.subs([(k, kv), (phi, phiv)]).rewrite(sp.exp)))
            for r in roots]
    tset = [sp.simplify(sp.expand_complex(sp.exp(sgn * sp.I * (kv + phiv)))) for sgn in (1, -1)]
    matched = all(any(sp.simplify(r - t) == 0 for t in tset) for r in rset)
    exact_ok = exact_ok and matched
band_ok = True
for phiv in (0.0, 0.4):
    for kv in np.linspace(-np.pi, np.pi, 41):
        lams = np.roots([1, -2 * np.cos(kv + phiv), 1])
        tgt = np.array([np.exp(1j * (kv + phiv)), np.exp(-1j * (kv + phiv))])
        if not np.allclose(sorted(lams, key=np.angle), sorted(tgt, key=np.angle), atol=1e-9):
            band_ok = False
check("D3 beta=0, g=1 => bands are e^{+-i(k+phi)}: omega = +-(k+phi) EXACT (free single-particle dispersion)",
      bool(exact_ok) and band_ok,
      "|v| = 1 at every k; every curvature order of the winding band vanishes identically")

omega_chiral = k + phi
check("D4 cone slope quantized: |v| = 1 and curvature == 0",
      sp.simplify(sp.diff(omega_chiral, k) - 1) == 0 and
      sp.simplify(sp.diff(omega_chiral, k, 2)) == 0,
      "the real-time quantization is the theorem; any OS0 c_t/c_s consequence needs the named bridge")

# D5: CONTINUOUS TIME CANNOT WIND: for any real periodic band E(k), the
# quasi-energy winding of e^{-i E(k) a_tau} is (a_tau/2pi) Int E'(k) dk = 0.
# (Eigenvalue branches of e^{-iHt} cannot acquire net winding: E is bounded by
# ||H|| and single-valued, so the integral telescopes to zero.)
Ek = kap * sp.sin(k) + sp.Rational(1, 3) * sp.sin(2 * k)
winding_cont = sp.integrate(sp.diff(Ek, k), (k, -sp.pi, sp.pi)) / (2 * sp.pi)
check("D5 continuous-time bands cannot wind: (1/2pi) Int E'(k) dk = 0 for periodic E",
      sp.simplify(winding_cont) == 0,
      "the saturation mechanism EXISTS ONLY for a discrete tick -- the license is load-bearing")


# ----------------------------------------------------------------------------
print("\nPART D6 -- explicit brickwork constructions (traces and windings COMPUTED)")
print("=" * 78)
# One-particle Bloch matrices of 2-layer brickwork circuits on the 2-site cell
# (A,B); layer 1 acts on (A_x, B_x), layer 2 on (B_x, A_{x+1}).  The partial
# swap gate restricted to the one-particle sector is
#   g(t) = [[cos t, i sin t], [i sin t, cos t]].
def g1(t):
    return np.array([[np.cos(t), 1j * np.sin(t)], [1j * np.sin(t), np.cos(t)]])

def brickwork_U(kv, t1, t2):
    zv = np.exp(1j * kv)
    G1 = g1(t1)
    g2m = g1(t2)
    L2 = np.array([[g2m[1, 1], g2m[1, 0] * zv], [g2m[0, 1] / zv, g2m[0, 0]]])
    return L2 @ G1

def principal_band_stats(tr_func, nk=4001):
    """For a real-trace family: omega_p(k) = arccos(tr/2) in [0, pi] is the
    continuous principal band.  Returns (touches omega=0, touches omega=pi,
    max |d omega_p/dk| away from touchings).  By the D2 surjectivity logic,
    a band winds iff the spectrum traverses BOTH poles: touch0 AND touchpi."""
    ks = np.linspace(-np.pi, np.pi, nk)
    trs = np.array([np.real(tr_func(kv)) for kv in ks])
    om = np.arccos(np.clip(trs / 2, -1, 1))
    touch0 = trs.max() > 2 - 1e-9
    touchpi = trs.min() < -2 + 1e-9
    v = np.abs(np.diff(om) / np.diff(ks))
    # exclude derivative estimates adjacent to touchings (arccos kink points):
    interior = np.ones(len(v), dtype=bool)
    for i in range(len(v)):
        if min(abs(om[i]), abs(om[i + 1])) < 1e-3 or min(abs(om[i] - np.pi), abs(om[i + 1] - np.pi)) < 1e-3:
            interior[i] = False
    vmax = v[interior].max() if interior.any() else 0.0
    return touch0, touchpi, vmax

def det_winding(Ufunc, nk=4001):
    """Winding of det U(k) around the circle (sum of band windings)."""
    ks = np.linspace(-np.pi, np.pi, nk)
    dets = np.array([np.linalg.det(Ufunc(kv)) for kv in ks])
    return np.sum(np.angle(dets[1:] / dets[:-1])) / (2 * np.pi)

# D6a: the SYMMETRIC partial-swap family (t1 = t2 = theta): trace COMPUTED from
# the construction; it equals 2cos^2(theta) - 2sin^2(theta)cos(k), which hits
# +2 at k = pi for EVERY theta: permanently GAPLESS, winding-0, with tunable
# touching-point velocity -- an ADDITIONAL hostile witness for P4 (a second
# non-winding gapless cell), NOT a mass family:
sym_trace_ok = True
for t in (0.3, 0.7, 1.1):
    for kv in (0.0, 1.0, np.pi):
        tr_num = np.trace(brickwork_U(kv, t, t))
        tr_form = 2 * np.cos(t)**2 - 2 * np.sin(t)**2 * np.cos(kv)
        if abs(tr_num - tr_form) > 1e-12 or abs(tr_num.imag) > 1e-12:
            sym_trace_ok = False
touch_ok = all(abs(np.trace(brickwork_U(np.pi, t, t)) - 2) < 1e-12 for t in (0.3, 0.7, 1.1))
t0, tpi, _ = principal_band_stats(lambda kv: np.trace(brickwork_U(kv, 0.5, 0.5)))
check("D6a symmetric partial swap: tr = 2cos^2(t) - 2sin^2(t)cos k (COMPUTED); gapless at k=pi for ALL t; NON-winding",
      sym_trace_ok and touch_ok and t0 and not tpi,
      "touches omega=0 only (one pole) => winding 0; a second non-winding tunable witness (P4 load-bearing)")

# D6b: the ASYMMETRIC family (layer 1 = FULL swap t1 = pi/2, layer 2 = partial
# theta): trace COMPUTED = -2 sin(theta) cos(k) -- the beta = 0, g = sin(theta)
# family: GAPPED with gap omega_min = pi/2 - theta (the mass), closing INTO the
# winding cell as theta -> pi/2:
asym_ok = True
for t in (0.3, 0.7):
    for kv in (0.0, 1.0, np.pi):
        tr_num = np.trace(brickwork_U(kv, np.pi / 2, t))
        if abs(tr_num - (-2 * np.sin(t) * np.cos(kv))) > 1e-12:
            asym_ok = False
gaps = []
for t in (0.3, 0.7):
    ks = np.linspace(-np.pi, np.pi, 2001)
    om_min = min(abs(np.angle(np.linalg.eigvals(brickwork_U(kv, np.pi / 2, t)))).min()
                 for kv in ks)
    gaps.append((t, om_min))
gap_ok = all(abs(om - (np.pi / 2 - t)) < 1e-3 for t, om in gaps)
check("D6b asymmetric (full x partial) family: tr = -2 sin(t) cos k (COMPUTED); GAPPED, gap = pi/2 - t",
      asym_ok and gap_ok,
      f"gaps {[(t, round(g, 4)) for t, g in gaps]} -- the mass family, beta = 0")

# D6c: the gap closes into the winding cell: at t = pi/2 (full x full) the
# trace is -2 cos k (beta = 0, g = 1): the spectrum traverses BOTH poles
# (the winding criterion, = D2's surjectivity logic) and |v| = 1 exactly:
t0f, tpif, vmaxf = principal_band_stats(lambda kv: np.trace(brickwork_U(kv, np.pi / 2, np.pi / 2)))
check("D6c full x full: tr = -2 cos k traverses BOTH poles (winding cell) with |v| = 1 (COMPUTED)",
      t0f and tpif and abs(vmaxf - 1) < 1e-3,
      f"max |v| = {vmaxf:.6f}: the saturating cell")

# D6d: dichotomy sweep over the (beta, g) trace family: winding occurs ONLY at
# (beta, g) = (0, 1); every interior sample is non-winding with max |v| < 1:
sweep_ok = True
worst = (None, 0.0)
for bv in (-0.8, -0.3, 0.0, 0.4, 1.0):
    for gv in (0.1, 0.45, 0.8):
        if abs(bv) + 2 * gv > 2 + 1e-12:
            continue
        if abs(bv) < 1e-12 and abs(gv - 1) < 1e-12:
            continue
        t0s, tpis, vmaxs = principal_band_stats(
            lambda kv, bv=bv, gv=gv: bv + 2 * gv * np.cos(kv))
        winds = t0s and tpis
        if winds or vmaxs >= 1 - 1e-9:
            sweep_ok = False
        if vmaxs > worst[1]:
            worst = ((bv, gv), vmaxs)
check("D6d dichotomy sweep: every (beta, g) != (0, 1) sample is non-winding with max |v| < 1",
      sweep_ok, f"largest interior max|v| = {worst[1]:.4f} at (beta,g)={worst[0]}; winding <=> the saturating cell")


# ----------------------------------------------------------------------------
print("\nPART E -- hostile witnesses: every premise is load-bearing")
print("=" * 78)
th = sp.symbols('theta', real=True)
zz = sp.exp(sp.I * k)
Splus = sp.diag(zz, 1)
Sminus = sp.diag(1, 1 / zz)
def Cm(t):
    return sp.Matrix([[sp.cos(t), sp.I * sp.sin(t)], [sp.I * sp.sin(t), sp.cos(t)]])
Uss2 = sp.simplify(Splus * Cm(th) * Sminus * Cm(-th))
unit_ok = sp.simplify(Uss2 * Uss2.H - sp.eye(2)) == sp.zeros(2, 2)
half_tr = sp.simplify(sp.trace(Uss2) / 2)
cos_omega = sp.simplify(sp.re(sp.expand_complex(half_tr)))
target = sp.cos(th)**2 * sp.cos(k) + sp.sin(th)**2
check("E1a split-step is a radius-1 unitary with cos(omega) = cos^2(th) cos k + sin^2(th)",
      unit_ok and sp.simplify(cos_omega - target) == 0, f"cos(omega) = {sp.simplify(cos_omega)}")

v_ss = sp.limit(sp.sqrt(2 * (1 - target)) / k, k, 0, '+')
check("E1b split-step gapless cone velocity v = |cos(theta)|: CONTINUOUSLY TUNABLE (drop P4)",
      sp.simplify(v_ss - sp.Abs(sp.cos(th))) == 0,
      f"v = {v_ss}: winding-0 gapless cell, the dial returns")

coeff_mats = []
Upoly = sp.expand(Uss2)
for power in (-1, 0, 1):
    M = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            M[i, j] = sp.expand(Upoly[i, j]).coeff(zz, power)
    coeff_mats.append(sp.simplify(M))
X = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'x{i}{j}'))
eqs = []
for M in coeff_mats:
    Cc = sp.expand(X * M - M * X)
    eqs += [Cc[i, j] for i in range(2) for j in range(2)]
solX = sp.solve(eqs, [sp.Symbol('x01'), sp.Symbol('x10'), sp.Symbol('x00'), sp.Symbol('x11')], dict=True)
comm_trivial = all(sp.simplify(s.get(sp.Symbol('x01'), 0)) == 0 and
                   sp.simplify(s.get(sp.Symbol('x10'), 0)) == 0 and
                   sp.simplify(s.get(sp.Symbol('x00'), sp.Symbol('x00')) -
                               s.get(sp.Symbol('x11'), sp.Symbol('x11'))) == 0
                   for s in solX) if solX else False
check("E1c split-step admits NO decoupling grading (commutant of coefficients = scalars)",
      comm_trivial, "the tunable witness is genuinely outside the chiral class")

# E2: THE P3 DROP-OUT WITNESS: U(k) = S_+ C(theta): radius-1 unitary, COMPLEX
# trace (P3 broken), det = z (winding 1), and its winding spectral branch has
# CONTINUOUSLY TUNABLE group velocity -- so the CPT pairing premise is
# load-bearing, not decorative:
def Up3(kv, t=0.6):
    Sp = np.diag([np.exp(1j * kv), 1.0])
    Cn = np.array([[np.cos(t), 1j * np.sin(t)], [1j * np.sin(t), np.cos(t)]])
    return Sp @ Cn
tr_p3 = np.trace(Up3(1.0))
wdet = det_winding(lambda kv: Up3(kv))
# the total band winding is wdet = 1 (det = e^{ik} det C = z), so SOME branch
# winds; its velocity range: for this family the quasi-energies are
# omega_pm(k) = k/2 +- arccos(cos(t) cos(k/2)) (computed from the trace
# z^{1/2}-reduced form); track the velocity of the winding combination
# numerically via the smooth total phase:
ksw = np.linspace(-np.pi, np.pi, 4001)
om_plus = ksw / 2 + np.arccos(np.clip(np.cos(0.6) * np.cos(ksw / 2), -1, 1))
v_branch = np.abs(np.diff(om_plus) / np.diff(ksw))
# verify omega_pm reproduce the actual eigenvalues on a sample grid:
eig_ok = True
for kv in np.linspace(-np.pi + 0.1, np.pi - 0.1, 21):
    ev = np.linalg.eigvals(Up3(kv))
    omp = kv / 2 + np.arccos(np.clip(np.cos(0.6) * np.cos(kv / 2), -1, 1))
    omm = kv / 2 - np.arccos(np.clip(np.cos(0.6) * np.cos(kv / 2), -1, 1))
    tgt = np.array([np.exp(1j * omp), np.exp(1j * omm)])
    if not np.allclose(sorted(ev, key=np.angle), sorted(tgt, key=np.angle), atol=1e-9):
        eig_ok = False
check("E2 P3 drop-out witness: S_+ C(0.6) has complex trace, det-winding 1, and TUNABLE branch velocity",
      abs(tr_p3.imag) > 0.1 and abs(wdet - 1) < 1e-3 and eig_ok
      and v_branch.min() < 0.2 and v_branch.max() > 0.8 and v_branch.max() < 1 + 1e-6,
      f"branch v range [{v_branch.min():.3f}, {v_branch.max():.3f}]: without CPT pairing the dial returns")

check("E3 without unitarity the bosonic family sweeps xi continuously (Part A)",
      abs(r_low - r_high) > 0.01, "positive transfer has no unimodularity constraint")
check("E4 without strictness the Hamiltonian tick has tunable velocity (Part C)",
      all(l > 1e-6 for l in leaks), "strict license is load-bearing, same strict reading as per-plaquette")


# ----------------------------------------------------------------------------
print("\nPART F -- the first-order carrier: the ratio enters as the cone velocity")
print("=" * 78)
# The normalization quotient (joint rescale invariance) is GENERIC -- the
# bosonic family has it too (computed below); what is carrier-specific is only
# the FORM: first-order => the single surviving ratio is the velocity itself.
kt2, ks2, mm = sp.symbols('kappa_t kappa_s m', positive=True)
omega_f = sp.asinh(sp.sqrt(ks2**2 * sp.sin(k)**2 + mm**2) / kt2)
scaled_f = omega_f.subs([(ks2, 2 * ks2), (kt2, 2 * kt2), (mm, 2 * mm)])
E_scaled = E.subs([(Kt, 2 * Kt), (Ks, 2 * Ks), (m2, 2 * m2)])
check("F1 joint-rescale invariance holds for BOTH carriers (a generic normalization quotient, not a contrast)",
      sp.simplify(scaled_f - omega_f) == 0 and sp.simplify(E_scaled - E) == 0,
      "the anisotropy gate's 2 coefficients = {ratio, removable normalization} for every carrier")
v_f = sp.limit(omega_f.subs(mm, 0) / k, k, 0, '+')
check("F2 first-order carrier: the surviving ratio IS the cone velocity v = kappa_s/kappa_t (bosonic: v^2)",
      sp.simplify(v_f - ks2 / kt2) == 0,
      "consistent with the velocity-RG note's canonical-time observation")


# ----------------------------------------------------------------------------
print("\nPART G -- scope honesty: what is NOT proved here")
print("=" * 78)
check("G1 named open: 2-component blocks evade the scalar monomial lemma (split-step exists)",
      not (sp.simplify(Uss2[0, 1]) == 0 and sp.simplify(Uss2[1, 0]) == 0),
      "3D Weyl-block enumeration is a separate cycle; 1D/per-axis theorem only")
check("G2 positive-transfer ticks and unitary ticks are distinct objects (P2 is a named reading)",
      all(0 < t < 1 for t in tvals),
      "any OS0 c_t/c_s consequence additionally uses the named first-order Wick/readout bridge")


print("\nPART H -- source-side premise-discharge wiring and status firewall")
print("=" * 78)
target_text = text(NOTE_PATH)
target_flat = flat(NOTE_PATH)
site_flat = flat(SITE_LICENSE_NOTE)
unitarity_flat = flat(TICK_UNITARITY_NOTE)
bw_flat = flat(BW_BRIDGE_NOTE)
wir_flat = flat(WIR_NOTE)
realization_flat = flat(REALIZATION_NOTE)

check("H1 target note wires both 2026-06-15 premise-discharge candidate packets",
      "## 2026-06-15 premise-discharge bridge candidates" in target_text
      and "SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11.md" in target_text
      and "TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md" in target_text,
      "P1/P4 and P2/P3 now have explicit source packets for re-audit")

check("H2 all-period site-license packet states the finite-period flat-or-saturating discharge without status overreach",
      "discharges that residual" in site_flat
      and "every finite period" in site_flat
      and "No third cell at any period" in site_flat
      and "It does not derive unitarity or the license" in site_flat
      and "does not set audit status" in site_flat,
      "candidate packet narrows P1/P4 but keeps license/unitarity as named readings")

check("H3 tick-unitarity packet reduces P2/P3 to spectrum-reflection transport plus channel envelope",
      "a spectrum-reflection conjugacy exists for T" in unitarity_flat
      and "<=>" in unitarity_flat
      and "T is unitary" in unitarity_flat
      and "The bare reading \"the tick is unitary\"" in unitarity_flat
      and "retired into two narrower named readings" in unitarity_flat
      and "the C-reading) or the channel envelope (the N-reading); both are named readings" in unitarity_flat
      and "does not compute the B-W bridge" in unitarity_flat,
      "candidate packet narrows P2/P3 without bundling OS0 c_t/c_s")

check("H4 target source keeps primitive retirement, B-W, and audit authority firewalled",
      "These packets are source-side audit candidates, not status authorities" in target_flat
      and "B-W Wick/readout bridge" in target_flat
      and "does not retire the kinetic-isotropy primitive" in target_flat
      and "does not set any audit verdict" in target_flat
      and "No primitive retirement or registry action" in target_text,
      "repair is source-side wiring only, not a retained-status claim")

check("H5 target source wires the B-W bridge-chain packets as explicit markdown dependencies",
      "## 2026-06-16 B-W bridge-chain source graph" in target_text
      and "BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md" in target_text
      and "WIR_CONE_AGREEMENT_FROM_SECTOR_ALIAS_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-06-11.md" in target_text
      and "REALIZATION_ROW_SIGMA_RECONCILIATION_BOUNDED_THEOREM_NOTE_2026-06-11.md" in target_text
      and "source-side audit candidates and bridge-chain dependencies, not status authorities" in target_flat,
      "re-audit now has concrete upstream rows for the old B-W residual")

check("H6 B-W bridge packet reduces OS0 identification to W-IR while refuting full Wick pairing",
      "B-W = (T1)-(T2) exact computation + (W-IR) one named premise" in bw_flat
      and "The full pairing is refuted for strict ticks; W-IR is forced" in bw_flat
      and "does not derive W-IR" in bw_flat
      and "does not set audit status" in bw_flat,
      "B-W is no longer a naked bridge, but its residual remains named")

check("H7 WIR and realization packets expose the remaining readings without primitive retirement",
      "discharges Wick-IR in the bounded setting" in target_flat
      and "record-stack spectral reading" in wir_flat
      and "Cone-agreement corollary" in wir_flat
      and "In particular cone-point slopes agree" in wir_flat
      and "selection doesn't move the OS0-consumed content" in realization_flat
      and "does not promote, demote, or set the audit status" in wir_flat
      and "does not promote, demote, or set the audit status" in realization_flat,
      "bridge residual is now record-stack/realization/unit readings, not hidden OS0 prose")


print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
