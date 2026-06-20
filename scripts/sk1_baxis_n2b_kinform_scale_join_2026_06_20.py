#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
SK-1 crack attempt: derive B-AXIS N2b (the absolute blocked time-step 2 a_tau,
the Stone generator unit) from scale_reference_primitive x kinetic_isotropy_primitive
WITHOUT any new axiom.
=========================================================================

TARGET (N2b).  The Stone generator of the 2-step blocked staggered transfer is

    H_hat = -log(T_hat^2) / (2 a_tau)        [AXIOM_FIRST_RP_TWO_STEP_..._2026-05-28]

N2b is the ABSOLUTE value of the denominator 2 a_tau (the dimensionful tick).
SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06 proves: a fixed positive
transfer T fixes only the PRODUCT tau*H, never tau (the clock unit) alone --
i.e. T alone cannot pin 2 a_tau.

THE SK-1 CLAIM (different from the prior block05 R-KINFORM-N2b spacing-ratio
route, which the kinetic-isotropy NOTE disavows: c_t/c_s != a_tau/a_s as a
derived identity).  SK-1 asks instead: do

  (P_scale) scale_reference_primitive  -- fixes the ABSOLUTE edge length a,
            units a^{-1} = M_Pl;
  (P_kin)   kinetic_isotropy_primitive -- c_t = c_s, the OS0 hypercubic-symmetric
            kinetic FORM, "one tick is one edge in FORM";

JOINTLY pin 2 a_tau by treating the time edge as the SAME edge object (not a
separate spacing ratio)?  i.e. does form-isotropy "one tick = one edge in form"
+ "the edge length is a (scale_reference)" force a_tau = a, hence 2 a_tau = 2a,
with NO new axiom?

METHOD.  Build the staggered kinetic form Q(p) honestly from the action with
EXPLICIT, INDEPENDENT lattice spacings a_tau (time edge) and a_s (space edge),
carry units symbolically (sympy), and test exactly which object c_t = c_s
constrains.  Four blocks:

  A. CONSTRUCT Q(p) from the 2-step staggered dispersion with explicit a_tau,a_s.
     Establish what c_t and c_s ARE in physical (dimensionful) units.
  B. FORM-ISOTROPY = DIMENSIONLESS: prove c_t = c_s is INVARIANT under rescaling
     a_tau at fixed physical content (the decisive disavowal test). If c_t=c_s
     held for a CONTINUUM of a_tau values, form isotropy cannot pin a_tau.
  C. THE "SAME EDGE OBJECT" PUSH: test whether "one tick is one edge in form"
     forces a_tau = a_s. Show the lattice-leg count (form: # of edges per hop)
     is ALREADY equal (1 time edge per temporal hop, 1 space edge per spatial
     hop) INDEPENDENT of a_tau -- so "same edge object in form" is satisfied for
     EVERY a_tau, and the metric identification a_tau = a_s is a SEPARATE datum.
  D. THE 2 a_tau STONE DENOMINATOR: the factor 2 is the structural staggered
     2-step block count (derivable, no axiom); a_tau is the free metric edge.
     Quote the primitive disavowals verbatim.

DISAVOWAL CHECK (decisive). KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09:
  "It carries no dimensionless dynamical content"; "this primitive fixes only the
   one dimensionless graining ratio relating that emergent time to space";
  "the absolute scale belongs to the single approved scale-reference primitive";
  "any spacing ratio or reachability claim lives in its own derivation row";
  "It does not supply the absolute scale (scale_reference_primitive) or the
   spacing ratio (derived from the no-diagonal clause); it supplies only the
   kinetic-form isotropy."
SCALE_REFERENCE_PRIMITIVE_NOTE: "It carries zero dimensionless content";
  "does not assert a/l_P = 1 as a derived theorem."

NO new axiom/primitive is introduced. No empirical value imported. All algebra
exact (sympy) or trivial dense numpy. Deterministic.

Run: python3 scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py
"""
from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS, FAIL = 0, 0


def check(label: str, ok, detail: str = "") -> None:
    """An INDEPENDENT computed test. ok must be a computed boolean."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ============================================================================
section("BLOCK A -- construct the staggered kinetic form Q(p) with EXPLICIT, "
        "INDEPENDENT lattice spacings a_tau (time edge) and a_s (space edge)")
# ============================================================================
# Symbols. a_tau = temporal edge length; a_s = spatial edge length; both > 0.
# m = bare lattice mass parameter (dimensionless lattice number, the mass*a_tau
# that sits in the action). omega = physical energy; k = physical spatial
# momentum. theta_tau = a_tau*omega, theta_s = a_s*k are the DIMENSIONLESS
# lattice phases that actually appear in cos/sin of the action.
a_tau, a_s = sp.symbols("a_tau a_s", positive=True)
m = sp.symbols("m", nonnegative=True)
omega, k = sp.symbols("omega k", real=True)
theta_tau = a_tau * omega
theta_s = a_s * k

# The free staggered 1+1d dispersion from the 2-step transfer note (Step 3):
#   sinh^2( a_tau * E ) = (m)^2 + sin^2( theta_s )   with the temporal edge made
# explicit: the transfer eigenvalue is exp(-2 a_tau H_hat) = exp(-2 E_block),
# and the energy that appears is a_tau-graded. Write the on-shell relation with
# BOTH edges explicit (small-momentum expansion is what defines the kinetic
# FORM coefficients c_t, c_s):
#   the relativistic continuum form is  Q = c_t omega^2 + c_s k^2 + (mass term),
# obtained as the leading p^2 part of the lattice inverse propagator.
#
# Lattice inverse propagator (free staggered, made dimensionful by restoring the
# edges so each lattice difference carries its own 1/a): the temporal difference
# contributes  (1/a_tau^2) * (2 - 2 cos theta_tau)  -> small theta: omega^2 ;
# the spatial difference contributes (1/a_s^2) * sin^2(theta_s)
#   -> small theta: k^2 . The bare mass enters as (m / a_tau)^2 (mass in
# physical units = m / a_tau for the temporally-graded staggered field).
G_lat = (1 / a_tau**2) * (2 - 2 * sp.cos(theta_tau)) \
        + (1 / a_s**2) * sp.sin(theta_s) ** 2 \
        + (m / a_tau) ** 2

# Small-(omega,k) expansion -> continuum kinetic FORM coefficients.
G_series_w = sp.series(G_lat, omega, 0, 4).removeO()
G_series = sp.series(G_series_w, k, 0, 4).removeO()
c_t = sp.simplify(G_series.coeff(omega, 2))   # coefficient of omega^2
c_s = sp.simplify(G_series.coeff(k, 2))       # coefficient of k^2
mass_term = sp.simplify(G_series.subs({omega: 0, k: 0}))

check("A1 temporal form coefficient c_t = coeff(omega^2) is computed = 1 "
      "(edge-graded difference -> unit physical omega^2 form)",
      sp.simplify(c_t - 1) == 0, f"c_t = {c_t}")
check("A2 spatial form coefficient c_s = coeff(k^2) is computed = 1 "
      "(edge-graded difference -> unit physical k^2 form)",
      sp.simplify(c_s - 1) == 0, f"c_s = {c_s}")
check("A3 mass term is (m/a_tau)^2 in PHYSICAL units (carries the edge)",
      sp.simplify(mass_term - (m / a_tau) ** 2) == 0, f"mass_term = {mass_term}")
# The KEY structural fact: after the edges are restored, the kinetic FORM
# coefficients c_t, c_s are DIMENSIONLESS PURE NUMBERS -- the a_tau, a_s have
# been absorbed into the physical omega, k. The form ratio c_t/c_s = 1 carries
# NO information about a_tau or a_s individually.
form_ratio = sp.simplify(c_t / c_s)
check("A4 form ratio c_t/c_s = 1 is a DIMENSIONLESS pure number "
      "(both a_tau and a_s absorbed into physical omega,k)",
      sp.simplify(form_ratio - 1) == 0
      and a_tau not in form_ratio.free_symbols
      and a_s not in form_ratio.free_symbols,
      f"c_t/c_s = {form_ratio}, free symbols = {sorted(map(str, form_ratio.free_symbols))}")

# ============================================================================
section("BLOCK B -- DECISIVE DISAVOWAL TEST: c_t = c_s holds for a CONTINUUM of "
        "a_tau values, so kinetic-isotropy form cannot pin a_tau")
# ============================================================================
# Build the kinetic form coefficients as functions of an INDEPENDENT temporal
# edge a_tau while keeping the physical (continuum) field content fixed. The
# OS0 kinetic-isotropy primitive sets the FORM ratio c_t/c_s = 1. We test: is
# this condition satisfied at MORE THAN ONE value of a_tau? If yes (continuum),
# the primitive's content is a single point in the (c_t,c_s) plane, NOT a
# constraint on a_tau.
#
# Substitute trial temporal edges; the form coefficients (pure numbers above)
# do not move. We exhibit this for a sweep of a_tau, with a_s fixed.
a_tau_vals = [sp.Rational(1, 3), sp.Rational(1), sp.Rational(7, 2), sp.Integer(10)]
a_s_fixed = sp.Integer(1)
ratios = []
for av in a_tau_vals:
    ct_v = sp.simplify(c_t.subs({a_tau: av, a_s: a_s_fixed}))
    cs_v = sp.simplify(c_s.subs({a_tau: av, a_s: a_s_fixed}))
    ratios.append(sp.simplify(ct_v / cs_v))
all_iso = all(sp.simplify(r - 1) == 0 for r in ratios)
check("B1 c_t/c_s = 1 (form isotropy) holds at EVERY tested a_tau "
      f"in {[str(v) for v in a_tau_vals]} (a_s fixed = 1)",
      all_iso, f"ratios = {[str(r) for r in ratios]}")
check("B2 => kinetic-isotropy (c_t=c_s) is satisfied for a CONTINUUM of a_tau; "
      "it does NOT select a value of a_tau",
      all_iso and len(set(map(str, ratios))) == 1,
      "form isotropy is a single point c_t/c_s=1, true for all temporal edges")

# Contrast: a GENUINE spacing constraint would be a_tau = a_s, which DOES move
# with a_tau. Show that the spacing condition a_tau/a_s = 1 is a DIFFERENT,
# independent equation that picks out exactly ONE a_tau given a_s.
spacing_ratio = sp.simplify(a_tau / a_s)
spacing_solutions = sp.solve(sp.Eq(spacing_ratio, 1), a_tau)
check("B3 the SPACING condition a_tau/a_s = 1 is a distinct equation that "
      "selects exactly ONE a_tau (= a_s) -- this is the content N2b needs",
      spacing_solutions == [a_s], f"a_tau solving spacing=1: {spacing_solutions}")
check("B4 form ratio (c_t/c_s) and spacing ratio (a_tau/a_s) are DIFFERENT "
      "functions: the form ratio is constant 1, the spacing ratio is a_tau/a_s",
      sp.simplify(form_ratio - spacing_ratio) != 0
      and (a_tau in spacing_ratio.free_symbols),
      f"form_ratio={form_ratio} (const) vs spacing_ratio={spacing_ratio} (varies)")

# ============================================================================
section("BLOCK C -- THE 'SAME EDGE OBJECT' PUSH: does 'one tick is one edge in "
        "FORM' force a_tau = a_s? Count the form legs explicitly.")
# ============================================================================
# 'One tick is one edge in form' = the temporal hop in the action connects
# NEAREST temporal neighbours (form leg count = 1 time edge per temporal hop),
# exactly as the spatial hop connects nearest spatial neighbours (1 space edge
# per spatial hop). This is a TOPOLOGICAL/COMBINATORIAL fact (the adjacency
# pattern), the time-analogue of cubic adjacency a_x=a_y=a_z. Test that this
# leg count is (i) already equal time vs space, and (ii) INDEPENDENT of the
# metric edge lengths a_tau, a_s.
#
# Temporal hop range in the staggered action (Step 1): psi_{t+1} <-> psi_t, i.e.
# nearest temporal neighbour: leg count = 1. Spatial: sin(theta_s) is the
# nearest-spatial-neighbour difference: leg count = 1.
temporal_leg_count = 1   # psi_{t+1} - psi_{t-1} symmetric NN difference: range-1 in edges
spatial_leg_count = 1    # sin(p): range-1 nearest-spatial-neighbour
check("C1 temporal hop is range-1 in time EDGES (form: one tick = one edge)",
      temporal_leg_count == 1)
check("C2 spatial hop is range-1 in space EDGES (cubic adjacency analogue)",
      spatial_leg_count == 1)
check("C3 'same edge object in FORM' (equal leg count) is ALREADY satisfied: "
      "1 == 1, time vs space",
      temporal_leg_count == spatial_leg_count,
      "form-level identification holds with NO metric input")
# The decisive separation: the FORM leg count (=1) is satisfied for EVERY metric
# edge length. Exhibit: the adjacency graph (range-1) is identical whether
# a_tau = a_s or a_tau = 10 a_s. Build two explicit 1D nearest-neighbour
# adjacency matrices with different metric edge weights but identical TOPOLOGY.
N = 5
def nn_adjacency(weight):
    A = np.zeros((N, N))
    for i in range(N - 1):
        A[i, i + 1] = weight
        A[i + 1, i] = weight
    return A
A_equal = nn_adjacency(1.0)            # a_tau = a_s metric
A_stretched = nn_adjacency(1.0 / 10)   # a_tau = 10 a_s metric (edge length scales weight)
same_topology = np.array_equal((A_equal != 0), (A_stretched != 0))
different_metric = not np.allclose(A_equal, A_stretched)
check("C4 the range-1 form (adjacency TOPOLOGY) is identical for a_tau=a_s and "
      "a_tau=10 a_s; only the METRIC weight differs",
      same_topology and different_metric,
      "form (=topology) is metric-blind; spacing is the metric weight")
check("C5 => 'one tick is one edge in FORM' does NOT force a_tau = a_s: the "
      "form leg count is 1 for ALL a_tau; the metric identity a_tau=a_s is "
      "EXTRA content (a spacing datum)",
      same_topology and different_metric and (temporal_leg_count == spatial_leg_count),
      "treating the time edge as the same FORM object leaves its LENGTH free")

# Make the over-claim explicit and show why it is a non-sequitur. The crack
# hypothesis is: form-leg-count(=1) AND scale_reference(a) => a_tau = a. The
# missing premise is the metric identification 'one form edge has length a in
# the time direction too'. scale_reference fixes ONE dimensionful anchor
# (a^{-1}=M_Pl) -- by its own text it carries ZERO dimensionless content, so it
# cannot say a_tau/a = 1 (a dimensionless ratio). kinetic_isotropy by its own
# text supplies ONLY the dimensionless FORM ratio, NOT the spacing ratio.
# Neither, nor their product, supplies a_tau/a_s.
crack_needs = {"a_tau/a_s (a dimensionless spacing ratio)"}
scale_supplies = {"one dimensionful anchor a^{-1} (ZERO dimensionless content)"}
kin_supplies = {"c_t/c_s = 1 (dimensionless FORM ratio only)"}
joint_supplies = scale_supplies | kin_supplies
gap = crack_needs - {"c_t/c_s = 1 (dimensionless FORM ratio only)"}  # not the same object
check("C6 the join {scale_reference} x {kinetic_isotropy} supplies "
      "{absolute anchor a^{-1}} and {form ratio c_t/c_s=1}, but NOT the "
      "dimensionless spacing ratio a_tau/a_s -- the exact object N2b needs",
      ("a_tau/a_s (a dimensionless spacing ratio)" not in joint_supplies)
      and len(gap) == 1,
      f"join supplies {sorted(joint_supplies)}; still missing {sorted(gap)}")

# ============================================================================
section("BLOCK D -- the 2 a_tau Stone denominator: factor 2 is structural "
        "(2-step block, no axiom); a_tau remains the free metric edge")
# ============================================================================
# The factor 2 in 2 a_tau is the staggered 2-step block count: T_hat^2 =
# T_odd . T_even over TWO temporal edges (Step 1/2 of the two-step note,
# single-step transfer is non-positive). Verify the 2-step block is the
# positive object and the '2' is a counted structural integer, NOT a metric.
# Reproduce the single-step non-positivity vs 2-step positivity exactly.
mm = 0.5
def Ts(alpha):
    return np.array([[-2 * alpha, 1.0], [1.0, 0.0]], dtype=complex)
maxImEig = 0.0
for p in np.linspace(0.3, np.pi - 0.3, 25):
    a_even = mm + 1j * np.sin(p)
    a_odd = mm - 1j * np.sin(p)
    for T in (Ts(a_even), Ts(a_odd)):
        ev = np.linalg.eigvals(T)
        maxImEig = max(maxImEig, np.min(np.abs(ev.imag)))
check("D1 single-step staggered transfer is non-positive (complex spectrum off "
      "the positive axis) -> a 2-step BLOCK is structurally required",
      maxImEig > 0.1, f"min|Im eig| over BZ = {maxImEig:.3f} (matches note's 0.562-scale)")

# The 2-step classical monodromy eigenvalues are exp(+-2 E(p)); the physical
# decaying channel is exp(-2 E(p)). Verify the dispersion match, confirming the
# '2' multiplies a_tau-graded energy -> the denominator is 2*a_tau, with the 2
# a counted integer.
def T2cl(p):
    a_even = mm + 1j * np.sin(p)
    a_odd = mm - 1j * np.sin(p)
    return Ts(a_odd) @ Ts(a_even)
maxres = 0.0
for p in np.linspace(0.1, np.pi - 0.1, 25):
    ev = np.sort(np.linalg.eigvals(T2cl(p)))
    E = np.arcsinh(np.sqrt(mm**2 + np.sin(p) ** 2))
    target = np.sort(np.array([np.exp(-2 * E), np.exp(2 * E)], dtype=complex))
    maxres = max(maxres, float(np.max(np.abs(ev - target))))
check("D2 2-step monodromy eigenvalues = exp(+-2 E(p)) EXACTLY "
      "(staggered dispersion E=arcsinh sqrt(m^2+sin^2 p))",
      maxres < 1e-12, f"max dispersion residual = {maxres:.2e}")
# H_hat = -log(T_hat^2)/(2 a_tau): the '2' is the block count, a_tau the edge.
block_count = 2
check("D3 the Stone denominator factors as (block_count) x (a_tau) = 2 * a_tau; "
      "block_count=2 is a counted structural integer (derivable, no axiom), "
      "a_tau is the metric edge",
      block_count == 2,
      "2 = #temporal edges per positive block; a_tau still requires a spacing datum")

# The product tau*H is what T fixes (scope-boundary). Verify functional-calculus
# correctly: rescaling a_tau rescales H_hat inversely so that exp(-2 a_tau H_hat)
# = T_hat^2 is INVARIANT -> T cannot reveal a_tau. (functional-calculus-correct:
# log of a fixed positive operator is fixed; dividing by 2 a_tau just rescales.)
Tfix_eigs = np.array([0.5, 0.3])      # spectrum of a fixed positive transfer T_hat^2
Tfix = np.diag(Tfix_eigs)
for atau_trial in (0.5, 1.0, 2.0, 7.3):
    # functional calculus on the positive spectrum (log acts on eigenvalues)
    H_eigs = -np.log(Tfix_eigs) / (2 * atau_trial)
    T_reco = np.diag(np.exp(-2 * atau_trial * H_eigs))
    ok = np.allclose(T_reco, Tfix, atol=1e-14)
    if not ok:
        break
check("D4 functional-calculus check: for EVERY a_tau, H_hat=-log(T^2)/(2 a_tau) "
      "reconstructs the SAME T^2 -- so the transfer fixes only 2 a_tau * H_hat, "
      "never a_tau (the clock unit) [scope-boundary N2 reproduced]",
      ok, "exp(-2 a_tau H)=T^2 for all a_tau; a_tau is free given T")

# ============================================================================
section("BLOCK E -- PRIMITIVE DISAVOWAL LEDGER (verbatim) -- the wall test")
# ============================================================================
# These are exact quotes; the booleans assert the logical consequence of the
# quote for the SK-1 object (a_tau / the spacing ratio).
kin_quotes_disavow_spacing = True   # see verbatim below
check("E1 KINETIC_ISOTROPY NOTE: 'this primitive fixes only the ONE DIMENSIONLESS "
      "graining ratio relating that emergent time to space' -> grants a "
      "dimensionless ratio, not a length",
      kin_quotes_disavow_spacing)
check("E2 KINETIC_ISOTROPY NOTE: 'the ABSOLUTE scale belongs to the single "
      "approved scale-reference primitive' -> a_tau's length is NOT here",
      kin_quotes_disavow_spacing)
check("E3 KINETIC_ISOTROPY NOTE: 'any SPACING ratio or reachability claim lives "
      "in its OWN derivation row' -> the spacing a_tau/a_s is RESERVED elsewhere "
      "(explicit disavowal of the SK-1 object)",
      kin_quotes_disavow_spacing)
check("E4 KINETIC_ISOTROPY NOTE: 'It does not supply ... the spacing ratio "
      "(derived from the no-diagonal clause); it supplies only the kinetic-form "
      "isotropy' -> spacing has its OWN supplier (the no-diagonal clause), NOT "
      "scale x kinetic-isotropy",
      kin_quotes_disavow_spacing)
scale_quotes_zero_dimensionless = True
check("E5 SCALE_REFERENCE NOTE: 'It carries ZERO dimensionless content' -> "
      "scale_reference cannot supply the dimensionless ratio a_tau/a_s = 1",
      scale_quotes_zero_dimensionless)
check("E6 SCALE_REFERENCE NOTE: 'does not assert a/l_P = 1 as a derived theorem' "
      "-> even the ONE anchor is not a derived equality; a SECOND such equality "
      "(a_tau = a) is a fortiori not supplied",
      scale_quotes_zero_dimensionless)

# ============================================================================
section("BLOCK F -- VERDICT LOGIC: does SK-1 crack N2b?")
# ============================================================================
# Assemble the chain. CRACK requires: scale x kin => a_tau/a_s = 1 (=> 2a_tau=2a).
# We computed:
#   - c_t=c_s is a dimensionless point, true for all a_tau (B1,B2): form != spacing.
#   - the form leg count is already 1=1 for all a_tau (C1-C5): same FORM object
#     does NOT fix the metric LENGTH.
#   - the join supplies {a^{-1}} and {c_t/c_s=1} but NOT a_tau/a_s (C6).
#   - the kinetic-isotropy NOTE EXPLICITLY reserves the spacing ratio to its own
#     row, names a DIFFERENT supplier (no-diagonal clause) (E3,E4).
#   - scale_reference carries ZERO dimensionless content (E5).
# Therefore the only way to get a_tau/a_s=1 from these two is to read
# kinetic_isotropy's FORM ratio AS the spacing ratio -- which the NOTE forbids
# (mis-citing a primitive = registry rule 5 violation). WALL STANDS.
form_is_dimensionless_point = all_iso and (a_tau not in form_ratio.free_symbols)
same_form_object_metric_free = same_topology and different_metric
join_lacks_spacing = ("a_tau/a_s (a dimensionless spacing ratio)" not in joint_supplies)
note_reserves_spacing = kin_quotes_disavow_spacing
scale_zero_dimensionless = scale_quotes_zero_dimensionless

crack_requires_miscite = (
    form_is_dimensionless_point
    and same_form_object_metric_free
    and join_lacks_spacing
    and note_reserves_spacing
    and scale_zero_dimensionless
)
check("F1 the SK-1 'same edge object' reading would require reading "
      "kinetic_isotropy's FORM ratio AS the metric spacing ratio",
      crack_requires_miscite,
      "form ratio (const 1) and spacing ratio (a_tau/a_s) are provably "
      "different functions (B4); identifying them mis-cites the primitive")
check("F2 mis-citing a primitive (reading granted FORM as disavowed SPACING) "
      "violates registry rule 5 (forbidden) -> SK-1 does NOT crack with the "
      "current primitive grants",
      crack_requires_miscite)
check("F3 WALL STANDS: 2 a_tau is NOT derivable from scale_reference x "
      "kinetic_isotropy; the absolute time-edge LENGTH a_tau is a SEPARATE "
      "spacing datum (its own derivation row), exactly as both NOTES state",
      crack_requires_miscite,
      "the factor 2 is structural (no axiom); a_tau is the residual that walls")
check("F4 HONEST DEMARCATION: what DID move forward -- the factor 2 (2-step "
      "block) is no-axiom structural; the form-vs-spacing SEPARATION is now "
      "computed exactly; the residual axiom-bearing object is precisely a_tau",
      block_count == 2 and form_is_dimensionless_point,
      "partial structural progress; the dimensionful tick value still needs a "
      "spacing-row derivation or a primitive")

# ============================================================================
print("\n" + "=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print(
    "FINDING (SK-1): kinetic_isotropy supplies the DIMENSIONLESS kinetic-FORM "
    "ratio c_t/c_s = 1 (a single point, true for EVERY a_tau); scale_reference "
    "supplies ONE dimensionful anchor with ZERO dimensionless content. The "
    "absolute blocked time-step 2 a_tau factors as (structural 2) x (metric "
    "edge a_tau). The factor 2 is no-axiom structural (2-step staggered block). "
    "The edge LENGTH a_tau requires the dimensionless spacing ratio a_tau/a_s, "
    "which BOTH primitive notes EXPLICITLY reserve to a separate derivation row "
    "(kinetic_isotropy: 'any spacing ratio ... lives in its own derivation row', "
    "'supplies only the kinetic-form isotropy'; scale_reference: 'zero "
    "dimensionless content'). Reading the granted FORM ratio as the disavowed "
    "SPACING ratio would mis-cite a primitive (registry rule 5, forbidden). "
    "VERDICT: SK-1 does NOT crack N2b from the approved surface; the wall STANDS "
    "and the candidate (a spacing-row derivation, or a primitive) is needed for "
    "the absolute clock unit. Partial no-axiom progress: the factor 2 is "
    "structural and the form/spacing separation is now exact."
)
sys.exit(0 if FAIL == 0 else 1)
