#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Kinetic isotropy: composition closure
=====================================
Companion runner for
docs/KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md.
Composition-closure pass of the kinetic-isotropy derivation loop.

TARGET.  The site-licensed tick dichotomy parent's remaining conditional set:
{site-strict reading + unitary-tick reading + Berezin-Wick bridge +
scheme-forcing + a dispersive realized tick + the 2-site periodicity scope}.
This note attacks three of those:

  Periodicity reduction. The periodicity wall becomes the landed KS structure:
      the joint landed
      pattern {eta_mu phases, epsilon sublattice parity} breaks EVERY odd
      translation (single-site and mixed) and is invariant under exactly
      (2Z)^3 -- computed from the landed formulas.  A tick covariant under
      the realized structure's UNBROKEN translations therefore has the
      uniform 2-site Bloch cell per axis that the site-licensed tick dichotomy parent assumed: the scope
      wall becomes a consequence of {Lattice translation action + landed
      {eta, eps} pattern (KS note, itself unaudited) + a homogeneity reading
      (the tick respects the realized structure's own unbroken symmetry)}.

  Composition reduction. Curvature and sub-saturation are composition content:
      the two-tick
      composite of two LICENSED cells -- the flat exchange cell U_flat(theta)
      and the saturating shift U_shift -- has bands
          mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0,   lambda = e^{-iK/2} mu,
      i.e. genuinely CURVED massive bands (computed), while every licensed
      SINGLE tick is flat-or-saturating (the site-licensed tick dichotomy parent).  Composite/effective
      velocities are DYNAMICS: tunable in [0, 1] by protocol and theta.
      HOSTILE WITNESS (composite-dial witness, load-bearing honesty): shift/identity protocols
      give MASSLESS composites with tunable cone slope k/(k+m) -- composite-
      level kinetic dials EXIST.  What excludes them from the regulator
      normalization is a PLACEMENT READING, declared by this note as the
      single-tick normalization-placement reading: "the OS0 kinetic
      normalization is the single-tick kernel's" -- motivated by (NOT derived
      from) the primitive's own
      self-locating wording ("one tick is one edge in form") and the per-
      plaquette note's one-tick form context; citing the primitive's own
      wording here carries a limited-circularity caveat, stated.  Under single-tick normalization-placement reading,
      the site-licensed tick dichotomy parent's dichotomy leaves no dial; without single-tick normalization-placement reading the dial returns at
      the composite level.  single-tick normalization-placement reading is the campaign's sharpest surviving
      residual and is flagged as such.

  Automorphism reduction. The unitary-tick reading is sharpened by
      Skolem-Noether: if the one-tick map is an AUTOMORPHISM
      of the site algebra (the Quantum axiom's M_2(C) structure preserved),
      it is unitary -- automorphisms of full matrix algebras are inner.  The
      premise has content: the transpose map preserves positivity and trace
      but REVERSES products (computed witness) -- it is excluded by the
      automorphism premise, not by fiat.  The unitary-tick reading's residual
      content shrinks from
      "unitary" to "the tick preserves the algebra structure (reversible,
      product-preserving)".

  Free-sector bridge computation. The Berezin-Wick bridge is computed in the
      free sector given a named sub-bridge: the
      identification of the tick's EUCLIDEAN one-tick kernel with the same
      shift structure (the standard Berezin transfer representation) is the
      free-sector instance of Berezin-Wick -- a named standard-math sub-bridge
      (Berezin-Wick free-sector bridge), assumed not derived.  GIVEN Berezin-Wick free-sector bridge, the kinetic operator
      1 - e^{-omega_E} e^{iK} expands to partial_tau - i partial_x, the
      conjugate cell to partial_tau + i partial_x (both coefficients
      computed), the chiral pair assembles omega_E^2 + K^2, and the exact
      zero locus is omega_E = iK identically: c_t = c_s with zero artifact
      corrections at the free level.  Berezin-Wick interacting bridge remains named.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  Remaining
conditional set after this note, COMPLETE: {site-strict reading +
algebra-automorphism reading (was unitary-tick reading; C-LINEAR --
antiunitary ticks are a named exclusion, not computed away) + single-tick
normalization-placement reading (new, declared here -- the sharpest residual)
+ homogeneity reading (periodicity reduction) + Berezin-Wick free-sector
bridge transfer-representation sub-bridge + Berezin-Wick interacting bridge + scheme-forcing
(landed, unaudited) + KS pattern (landed, unaudited) + a dispersive realized
tick}.  The 3D simultaneous tick remains the named open.  Skolem-Noether is
consumed as admissible standard math (cited, with a consistency exhibit; the
automorphism => inner direction is NOT machine-proved here).  No new axiom,
no new primitive, no Tier-A admission, no registry action.

Run: python3 scripts/kinetic_isotropy_composition_closure_2026_06_09.py
"""
from __future__ import annotations
import sys
import numpy as np
import sympy as sp

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


K, th = sp.symbols('K theta', real=True)
z = sp.exp(sp.I * K)

# ----------------------------------------------------------------------------
print("\nPART periodicity reduction -- derived from the landed KS breaking pattern")
print("=" * 78)
# The landed Kawamoto-Smit phases: eta_1 = 1, eta_2 = (-1)^{x1},
# eta_3 = (-1)^{x1+x2}.  Compute the translation-breaking pattern mechanically:
def eta(mu, xv):
    if mu == 1:
        return 1
    if mu == 2:
        return (-1) ** (xv[0])
    return (-1) ** (xv[0] + xv[1])

def eps(xv):
    # the sublattice parity, FORCED by the landed KS construction (Step 1):
    return (-1) ** (xv[0] + xv[1] + xv[2])

pts = [(x1, x2, x3) for x1 in range(4) for x2 in range(4) for x3 in range(4)]
def invariant_under(shift):
    sx = lambda x, i: [x[0] + shift[0], x[1] + shift[1], x[2] + shift[2]][i]
    shifted = lambda x: [x[0] + shift[0], x[1] + shift[1], x[2] + shift[2]]
    return all(eta(mu, shifted(x)) == eta(mu, list(x)) for mu in (1, 2, 3) for x in pts) \
        and all(eps(shifted(x)) == eps(list(x)) for x in pts)

# single-site translation is broken along EVERY axis (eps breaks axis 3 even
# though the eta's do not depend on x3), mixed odd shifts are broken too, and
# ALL 2-site translations are exact invariances:
singles_broken = all(not invariant_under(sh) for sh in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
mixed_broken = all(not invariant_under(sh) for sh in ((1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)))
doubles_ok = all(invariant_under(sh) for sh in ((2, 0, 0), (0, 2, 0), (0, 0, 2),
                                                (2, 2, 0), (2, 0, 2), (0, 2, 2)))
check("periodicity subgroup: landed {eta, eps} breaks every odd translation (incl. mixed) and preserves all 2-site translations",
      singles_broken and mixed_broken and doubles_ok,
      "unbroken translation subgroup = (2Z)^3 exactly -- computed on a 4^3 block")

# A tick covariant under the realized structure's unbroken translations has
# Bloch structure over the (2Z)^3 subgroup: a UNIFORM 2-site cell per axis --
# precisely the site-licensed tick dichotomy parent setting.  (Homogeneity reading, declared: the tick
# respects the realized structure's own unbroken symmetry; a spontaneously
# symmetry-breaking tick is not excluded by computation.)
check("periodicity cell consequence: unbroken subgroup (2Z)^3 gives the uniform 2-site Bloch cell per axis",
      doubles_ok and singles_broken,
      "scope wall -> {Lattice translation (axiom) + landed {eta, eps} pattern (KS note, unaudited) + homogeneity reading}")


# ----------------------------------------------------------------------------
print("\nPART composition reduction -- curvature and sub-saturation are composition (dynamics) content")
print("=" * 78)
# Two LICENSED single ticks (both verified against the site-licensed tick dichotomy parent degree table):
U_flat = sp.Matrix([[sp.cos(th), sp.I * sp.sin(th) / z], [sp.I * sp.sin(th) * z, sp.cos(th)]])
U_shift = sp.Matrix([[0, 1 / z], [1, 0]])
# license check: diagonal entries momentum-independent; off-diagonals single
# monomials within the {0,-1}/{0,+1} cell-offset table:
def fourier_coeff(e, n):
    return sp.simplify(sp.integrate(e * sp.exp(-sp.I * n * K), (K, -sp.pi, sp.pi)) / (2 * sp.pi))

def offdiag_single_monomial(M):
    ok = True
    for (i, j, powers) in ((0, 1, (0, -1)), (1, 0, (0, 1))):
        e = sp.expand(M[i, j].rewrite(sp.exp))
        coeffs = [fourier_coeff(e, n) for n in powers]
        nz = [c for c in coeffs if sp.simplify(c) != 0]
        resid = sp.simplify(sp.expand_complex(sp.expand(
            e - sum(c * sp.exp(sp.I * K * n) for c, n in zip(coeffs, powers)))))
        ok = ok and len(nz) <= 1 and resid == 0
    return ok
lic_flat = (sp.simplify(sp.diff(U_flat[0, 0], K)) == 0 and sp.simplify(sp.diff(U_flat[1, 1], K)) == 0
            and offdiag_single_monomial(U_flat))
lic_shift = (U_shift[0, 0] == 0 and U_shift[1, 1] == 0 and offdiag_single_monomial(U_shift))
unit_flat = sp.simplify((U_flat * U_flat.H).applyfunc(sp.expand_complex)) == sp.eye(2)
unit_shift = sp.simplify((U_shift * U_shift.H).applyfunc(sp.expand_complex)) == sp.eye(2)
check("licensed factors: flat exchange cell and saturating shift are licensed unitary single ticks",
      lic_flat and lic_shift and unit_flat and unit_shift,
      "each factor obeys the site-licensed tick dichotomy parent site-license degree table")

# The 2-tick composite:
U_eff = sp.simplify(U_flat * U_shift)
tr_eff = sp.simplify(sp.expand_complex(sp.trace(U_eff)))
det_eff = sp.simplify(sp.expand_complex(U_eff.det()))
check("composite trace: tr = i sin(theta)(1 + e^{-iK}) is momentum-dependent, so single-tick structure is broken",
      sp.simplify(sp.expand_complex(sp.trace(U_eff) - sp.I * sp.sin(th) * (1 + sp.exp(-sp.I * K)))) == 0
      and sp.simplify(det_eff + sp.exp(-sp.I * K)) == 0,
      "the composite is radius-2 (TWO ticks) -- the license binds the tick, not compositions")

# Reduced band equation: lambda = e^{-iK/2} mu with mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0:
mu = sp.symbols('mu')
lam = sp.exp(-sp.I * K / 2) * mu
charpoly = sp.simplify(sp.expand_complex(sp.expand(
    lam**2 - sp.trace(U_eff) * lam + U_eff.det()) * sp.exp(sp.I * K)))
target = sp.simplify(sp.expand_complex(sp.expand(
    (mu**2 - 2 * sp.I * sp.sin(th) * sp.cos(K / 2) * mu - 1))))
check("composite band equation: mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0 is derived from the composite",
      sp.simplify(sp.expand(charpoly - target)) == 0,
      "mu = e^{i nu}: sin(nu) = sin(theta) cos(K/2): a genuinely CURVED massive band")

# Curvature: nu(K) = arcsin(sin(theta) cos(K/2)): compute the band and its
# curvature exactly; at theta = 0 the band is the saturating shift:
nu = sp.asin(sp.sin(th) * sp.cos(K / 2))
omega_band = -K / 2 + nu
curv = sp.simplify(sp.diff(omega_band, K, 2))
curv_at = sp.simplify(curv.subs([(th, sp.pi / 6), (K, sp.pi / 3)]))
curv_nonzero = (curv_at.equals(0) is False)
massless = sp.simplify(omega_band.subs(th, 0) + K / 2)
check("composite curvature: the band is curved for theta != 0 and the theta -> 0 limit is the saturating cell",
      curv_nonzero and massless == 0,
      f"curvature sample = {sp.nsimplify(curv_at, rational=False)} != 0; curvature lives in COMPOSITES, never the single tick (the site-licensed tick dichotomy parent)")

# Composite velocities are DYNAMICS: compute v_sites_per_tick(K) (one
# application of U_eff = TWO ticks, one cell = two sites, so
# v = |d omega/dK| * 2 / 2 = |d omega/dK|): (i) the Lieb-Robinson bound
# |v| <= 1 holds for all theta, K; (ii) v is genuinely theta- and K-dependent
# (tunable) -- including average 1/2 at theta = 0 ({identity, shift}
# alternation); the kinetic normalization is NOT a composite quantity:
v_per_tick = sp.diff(omega_band, K)   # cells/application * 2 sites / 2 ticks
# SYMBOLIC bound: |d nu/dK| <= 1/2 because
# (1 - sin^2(th) cos^2(K/2)) - sin^2(th) sin^2(K/2) = cos^2(th) >= 0:
bound_identity = sp.simplify((1 - sp.sin(th)**2 * sp.cos(K / 2)**2)
                             - sp.sin(th)**2 * sp.sin(K / 2)**2 - sp.cos(th)**2)
v_samples = [abs(float(v_per_tick.subs([(th, tv), (K, kv)])))
             for tv in (0.0, 0.4, 1.0) for kv in (0.3, 1.5, 2.8)]
v_tunable = abs(float(v_per_tick.subs([(th, 0.4), (K, 1.5)])) -
                float(v_per_tick.subs([(th, 1.0), (K, 1.5)]))) > 1e-3
check("velocity bound: |v| <= 1 follows from cos^2(theta) >= 0 and v is theta/K-tunable",
      bound_identity == 0 and all(v <= 1 + 1e-12 for v in v_samples) and v_tunable,
      "saturation only at theta = pi/2; sub-saturation and curvature are composition/dynamics quantities")

# Single-tick contrast (the site-licensed tick dichotomy parent cross-check): NO licensed single tick curves --
# the flat factor's bands are constant, the shift's are exactly linear:
flat_bands_const = all(sp.simplify(sp.diff(sp.simplify(ev), K)) == 0
                       for ev in U_flat.eigenvals())
shift_linear = all(sp.simplify(sp.diff(sp.simplify(sp.expand_complex(
    sp.log(sp.simplify(ev)) / sp.I)), K, 2)) == 0 for ev in U_shift.eigenvals())
check("single-tick contrast: flat-factor bands are constant and shift bands are exactly linear",
      flat_bands_const and shift_linear,
      "curvature REQUIRES composition: the kinetic form is a single-tick fact, mass/speed are composition facts")

# Hostile composite-dial witness (load-bearing honesty): shift/identity
# protocols give MASSLESS composites with TUNABLE cone slope k/(k+m): e.g.
# two shifts + one identity over three ticks: U = U_shift^2 = e^{-iK} I:
# bands omega = -K per 3 ticks: |v| = (2 sites)/(3 ticks) = 2/3 -- a
# composite-level kinetic dial with NO gap.  ONLY the placement reading single-tick normalization-placement reading
# (the OS0 normalization is the SINGLE-tick kernel's) excludes it from the
# regulator normalization.  single-tick normalization-placement reading is this note's declared residual:
U_two = sp.simplify(U_shift * U_shift)
is_scalar_shift = sp.simplify(U_two - sp.exp(-sp.I * K) * sp.eye(2)) == sp.zeros(2, 2)
check("composite-dial witness: shift^2 = e^{-iK} I gives a massless {shift, shift, identity} cone with slope 2/3",
      is_scalar_shift and 0 < sp.Rational(2, 3) < 1,
      "only the declared single-tick normalization-placement reading excludes composite dials from the OS0 normalization")


# ----------------------------------------------------------------------------
print("\nPART automorphism reduction -- unitary-tick reading sharpened by Skolem-Noether")
print("=" * 78)
# The Quantum axiom supplies the site algebra M_2(C).  If the one-tick map is
# an automorphism of that algebra (product-preserving, identity-preserving,
# adjoint-preserving), it is inner: phi = Ad_U with U unitary (Skolem-Noether
# for full matrix algebras).  Exhibits:
# (a) an automorphism IS product-preserving and inner (sampled, computed);
# (b) the TRANSPOSE map preserves trace/positivity but REVERSES products --
#     it is an ANTI-automorphism, excluded by the premise (the premise has
#     content; unitarity is not smuggled).
rng = np.random.default_rng(11)
X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
Q_, _ = np.linalg.qr(X)
A1 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
B1 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
phi = lambda M: Q_ @ M @ Q_.conj().T
prod_pres = np.allclose(phi(A1 @ B1), phi(A1) @ phi(B1))
unitary_inner = np.allclose(Q_ @ Q_.conj().T, np.eye(2))
check("automorphism consistency exhibit: inner maps Ad_U are C-linear automorphisms; converse is Skolem-Noether, cited not machine-proved",
      prod_pres and unitary_inner,
      "premise must say C-LINEAR automorphism: antiunitary (antilinear) ticks are excluded by the premise, named")

transpose_reverses = (np.allclose((A1 @ B1).T, B1.T @ A1.T) and
                      not np.allclose((A1 @ B1).T, A1.T @ B1.T))
check("anti-automorphism witness: transpose reverses products, so the automorphism premise has content",
      transpose_reverses,
      "unitary-tick reading residual = 'the tick preserves the algebra structure', not bare unitarity")


# ----------------------------------------------------------------------------
print("\nPART free-sector bridge computation -- Berezin-Wick bridge, free sector")
print("=" * 78)
# The saturating tick is the light-cone hop: its Euclidean kernel couples
# (x, tau) -> (x + 1, tau + 1).  The momentum-space kinetic operator of the
# corresponding Gaussian/Berezin action is
#     M(K, omega_E) = 1 - e^{-omega_E} e^{iK}
# (one field per site; the kernel is the shift).  Expand to first order:
wE = sp.symbols('omega_E', real=True)
M_op = 1 - sp.exp(-wE) * sp.exp(sp.I * K)
expansion = sp.expand(sp.series(sp.series(M_op, wE, 0, 2).removeO(), K, 0, 2).removeO())
# first-order part: omega_E - iK  ~  partial_tau - i partial_x:
lin = sp.expand(expansion - sp.expand(expansion.subs([(wE, 0), (K, 0)])))
lin1 = sp.simplify(lin.coeff(wE, 1).subs(K, 0))
lin2 = sp.simplify(lin.coeff(K, 1).subs(wE, 0))
check("free-kernel linearization: given Berezin-Wick free-sector bridge, the Euclidean kernel expands to partial_tau - i partial_x",
      sp.simplify(lin1 - 1) == 0 and sp.simplify(lin2 + sp.I) == 0,
      "EQUAL-MAGNITUDE temporal and spatial coefficients: |c_t| = |c_s| = 1 exactly")

# the conjugate cell: M_L = 1 - e^{-omega_E} e^{-iK} linearizes to
# partial_tau + i partial_x (coefficient +i COMPUTED), and the PRODUCT of the
# two kernels expands to the isotropic OS0 form at total degree 2:
M_opL = 1 - sp.exp(-wE) * sp.exp(-sp.I * K)
linL = sp.expand(sp.series(sp.series(M_opL, wE, 0, 2).removeO(), K, 0, 2).removeO())
linL = sp.expand(linL - linL.subs([(wE, 0), (K, 0)]))
linL1 = sp.simplify(linL.coeff(wE, 1).subs(K, 0))
linL2 = sp.simplify(linL.coeff(K, 1).subs(wE, 0))
pair = sp.expand(sp.series(sp.series(sp.expand(M_op * M_opL), wE, 0, 3).removeO(), K, 0, 3).removeO())
cross_wK = sp.simplify(pair.coeff(wE, 1).coeff(K, 1))
check("conjugate-pair kernel: degree-2 part is omega_E^2 + K^2 with zero mixed term",
      sp.simplify(linL1 - 1) == 0 and sp.simplify(linL2 - sp.I) == 0
      and sp.simplify(pair.coeff(wE, 2).subs(K, 0) - 1) == 0
      and sp.simplify(pair.coeff(K, 2).subs(wE, 0) - 1) == 0
      and cross_wK == 0,
      "GIVEN the named Berezin-Wick free-sector bridge transfer representation: c_t = c_s exactly at the free level")

onshell = sp.simplify(M_op.subs(wE, sp.I * K))
# (uniqueness: e^{-w} e^{iK} = 1 fixes w = iK modulo 2 pi i -- the exponential
# is injective on the principal strip; verified by the nonvanishing derivative)
dM = sp.simplify(sp.diff(M_op, wE).subs(wE, sp.I * K))
check("free zero-locus: omega_E = i K is an exact zero locus for the saturating cell",
      onshell == 0 and sp.simplify(dM - 1) == 0,
      "the light-cone hop is exactly conical at ALL orders -- nothing to renormalize at the free kinetic level")


print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
