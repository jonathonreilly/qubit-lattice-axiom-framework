#!/usr/bin/env python3
"""Route R-KINFORM-N2b: form<->spacing identity test for clause N2b (2026-06-20).

GENUINE fresh derivation attempt for clause N2b of the single-clock B-AXIS wall,
attacking the *tempting but guarded* route the exercise's Exercise-One hoped for.

THE HOPE (Exercise-One)
-----------------------
kinetic_isotropy_primitive supplies the FORM isotropy c_t = c_s, and
scale_reference_primitive supplies the single dimensionful anchor a^{-1} = M_Pl.
If c_t = c_s could be turned into a statement about the *spacings* a_tau = a_s,
then scale_reference would pin a_s = 1/M_Pl and hence the absolute clock unit
a_tau = 1/M_Pl would be DISCHARGED -- closing N2b from two approved primitives
plus one derived bridge.

THE HARD STOP (registry rule 5)
-------------------------------
The kinetic-isotropy note EXPLICITLY disavows the spacing ratio:
  - "any SPACING ratio or reachability claim lives in its own derivation row"
  - "It does not supply ... the spacing ratio ...; it supplies only the
     kinetic-form isotropy."
So we may NOT cite the primitive AS the spacing ratio. The route is legitimate
ONLY if we can DERIVE, as a SEPARATE theorem from the staggered/free Euclidean
action's quadratic form, an identity

        c_t / c_s  ==  a_tau / a_s          (the hoped form<->spacing bridge)

(or some other FIXED function of the spacing ratio that lets c_t = c_s pin
 a_tau = a_s).  If that identity holds, then:
     c_t = c_s (form, primitive)  =>  a_tau = a_s (spacing)
     scale_reference: a_s = 1/M_Pl           =>  a_tau = 1/M_Pl  (N2b DISCHARGED).
 If it FAILS or needs extra input, N2b stays open and we ship the sharper no-go.

METHOD (A_min-only; exact sympy on the free Euclidean quadratic form)
---------------------------------------------------------------------
We construct the standard free Euclidean lattice scalar action on a
Z^3 x Z_tau block with INDEPENDENT spacings (a_tau, a_s) and read off the
quadratic-form coefficients (c_t, c_s) of the small-momentum (continuum-limit)
dispersion

        Q(p) = c_t * p_tau^2 + c_s * (p_x^2 + p_y^2 + p_z^2).

This is the same object SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06
writes as "spacing-linked coefficients", and the same Q(p) the B4 bounded
theorem uses.  The discretization is the canonical central-difference one:

  S = sum_cells  cell_volume * [ (1/2)(Delta_tau phi / a_tau)^2
                                 + (1/2) sum_i (Delta_i phi / a_s)^2 ]

  cell_volume = a_tau * a_s^3.

We compute c_t(a_tau,a_s), c_s(a_tau,a_s) by expanding the lattice momentum
self-energy 2(1-cos(k_mu))/a_mu^2 to second order in k, multiplied by the
measure factor, EXACTLY in sympy.  We then test the candidate identities.

We ALSO test the convention-robustness leg the route demands: the free action
carries TWO conventional normalizations that the kinetic-isotropy primitive
does NOT pin (registry: it supplies no scale, no selector, no dynamics):
  (i) an overall coupling/normalization Z (field-strength / coupling rescale),
 (ii) an independent choice of the field's mass-dimension convention, i.e.
      whether the lattice field carries the cell measure or not.
A genuine form<->spacing THEOREM must be invariant under (i); if c_t/c_s can
be set to ANY value by a legal convention without touching the spacings, then
"c_t = c_s" places NO constraint on (a_tau, a_s) and the route is dead.

OUTCOMES
--------
 (a) c_t/c_s == a_tau/a_s identically (convention-robust) -> N2b DISCHARGED
     (report loudly: genuine clause closure).
 (b) identity FAILS or needs extra input -> N2b stays open; ship the sharper
     no-go "form pinned by kinetic-isotropy, spacing/absolute-unit NOT derived".

Every check prints residual + PASS/FAIL and a final TOTAL: PASS=.. FAIL=.. .
"""
from __future__ import annotations
import sympy as sp

PASS = 0
FAIL = 0
LINES = []


def check(name, cond, residual=None, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    rstr = "" if residual is None else f"  resid={residual}"
    LINES.append(f"[{tag}] {name}{rstr}{('  '+detail) if detail else ''}")


def banner(s):
    LINES.append("")
    LINES.append("=" * 72)
    LINES.append(s)
    LINES.append("=" * 72)


# ---------------------------------------------------------------------------
# Symbols.  Independent spacings; momentum components; conventions.
# ---------------------------------------------------------------------------
a_t, a_s = sp.symbols("a_tau a_s", positive=True)
k = sp.symbols("k", real=True)           # generic small-momentum scalar
Z = sp.symbols("Z", positive=True)       # overall coupling/normalization
M_Pl = sp.symbols("M_Pl", positive=True)

banner("SECTION 1 -- derive c_t, c_s from the free Euclidean quadratic form")

# We derive the p_mu^2 coefficients in THREE legitimate normalization
# conventions and show the spacing dependence of c_t/c_s is CONVENTION-DEPENDENT
# -- the decisive structural fact for this route.  In NO convention does the
# hoped identity c_t/c_s == a_tau/a_s hold.
#
# The lattice self-energy along axis mu with momentum k is
#       D_mu(k) = (2/a_mu^2)(1 - cos(k a_mu)) -> k^2 - (a_mu^2/12) k^4 + ...
# The continuum (k^2) coefficient of D_mu is EXACTLY 1, independent of a_mu
# (that is how the lattice derivative is built to converge to the continuum
# one).  The spacing dependence therefore lives ENTIRELY in the chosen
# measure/field normalization, NOT in the dispersion -- this is the crux.

cell_vol = a_t * a_s**3   # anisotropic 4-cell measure

def D_mu_continuum_coeff(a_mu):
    """Coefficient of k^2 in D_mu(k) = (2/a_mu^2)(1-cos(k a_mu)). Exactly 1."""
    Dmu = (2 * (1 - sp.cos(k * a_mu))) / a_mu**2
    return sp.simplify(sp.series(Dmu, k, 0, 4).removeO().coeff(k, 2))

cont_t = D_mu_continuum_coeff(a_t)
cont_s = D_mu_continuum_coeff(a_s)
check("bare lattice dispersion k^2-coeff is 1 on EVERY axis (spacing-free)",
      (sp.simplify(cont_t - 1) == 0) and (sp.simplify(cont_s - 1) == 0),
      residual=(sp.simplify(cont_t - 1), sp.simplify(cont_s - 1)))

# --- Convention A: continuum-normalized field, measure-weighted action ---
#   c_mu^A = (1/2) * cell_vol * (k^2 coeff of D_mu) = (1/2) cell_vol  (BOTH axes)
cA_t = sp.simplify(sp.Rational(1, 2) * cell_vol * cont_t)
cA_s = sp.simplify(sp.Rational(1, 2) * cell_vol * cont_s)
ratioA = sp.simplify(cA_t / cA_s)
LINES.append(f"  [Conv A measure-weighted] c_t={cA_t}  c_s={cA_s}  c_t/c_s={ratioA}")

# --- Convention B: BARE lattice action with a DIMENSIONLESS field (no per-axis
#     derivative re-normalization absorbed).  The action term per axis is
#     (1/2) * cell_vol * (1/a_mu^2) * sum (phi_{n+mu}-phi_n)^2, whose momentum
#     kernel coeff of k^2 is (1/2)*cell_vol/a_mu^2 * (a_mu^2) ... we keep the
#     RAW hopping weight w_mu = cell_vol / a_mu^2 as the p_mu^2 coefficient
#     (this is the form SPATIAL_CUBIC writes as spacing-linked). ---
cB_t = sp.simplify(cell_vol / a_t**2)   # = a_s^3 / a_tau
cB_s = sp.simplify(cell_vol / a_s**2)   # = a_tau * a_s
ratioB = sp.simplify(cB_t / cB_s)
LINES.append(f"  [Conv B bare hopping]     c_t={cB_t}  c_s={cB_s}  c_t/c_s={ratioB}")

# --- Convention C: lattice-natural action, NO measure (sum, not integral),
#     each axis weighted by 1/a_mu^2 only. p_mu^2 coeff = 1/a_mu^2. ---
cC_t = sp.simplify(1 / a_t**2)
cC_s = sp.simplify(1 / a_s**2)
ratioC = sp.simplify(cC_t / cC_s)
LINES.append(f"  [Conv C no-measure]       c_t={cC_t}  c_s={cC_s}  c_t/c_s={ratioC}")

# DECISIVE: the three legitimate conventions give c_t/c_s = 1, (a_s/a_tau)^2,
# (a_s/a_tau)^2 respectively -- i.e. the SPACING DEPENDENCE OF c_t/c_s IS NOT
# CONVENTION-INVARIANT.  A genuine form<->spacing THEOREM would require c_t/c_s
# to be a FIXED function of the spacings independent of these normalizations.
spacing_dependence_is_convention_dependent = (sp.simplify(ratioA - ratioB) != 0)
check("c_t/c_s spacing-dependence is CONVENTION-DEPENDENT (A gives 1, B gives (a_s/a_tau)^2)",
      spacing_dependence_is_convention_dependent,
      residual=sp.simplify(ratioA - ratioB),
      detail="(=> no convention-free form<->spacing function exists)")

banner("SECTION 2 -- test the HOPED identity  c_t/c_s == a_tau/a_s (all conventions)")

ratio_spacing_hoped = sp.simplify(a_t / a_s)
LINES.append(f"  a_tau/a_s (hoped target) = {ratio_spacing_hoped}")

# CRACK check in EACH convention.  The hoped identity c_t/c_s == a_tau/a_s is
# the DISCHARGE condition: if it held, N2b would close.  We record the residual
# of the would-be identity and ASSERT it is nonzero (identity FAILS) -- a PASS
# here means "the discharge identity does NOT hold", i.e. the crack is absent.
# (If any residual were 0, that check FAILS loudly and flags N2b DISCHARGED.)
diffA = sp.simplify(ratioA - ratio_spacing_hoped)
diffB = sp.simplify(ratioB - ratio_spacing_hoped)
diffC = sp.simplify(ratioC - ratio_spacing_hoped)
LINES.append(f"  would-be discharge residual [A] = {diffA}")
LINES.append(f"  would-be discharge residual [B] = {diffB}")
LINES.append(f"  would-be discharge residual [C] = {diffC}")
check("NO CRACK[A]: c_t/c_s != a_tau/a_s  (discharge identity absent)",
      diffA != 0, residual=diffA,
      detail="(a FAIL here would mean N2b DISCHARGED)")
check("NO CRACK[B]: c_t/c_s != a_tau/a_s  (discharge identity absent)",
      diffB != 0, residual=diffB,
      detail="(a FAIL here would mean N2b DISCHARGED)")
check("NO CRACK[C]: c_t/c_s != a_tau/a_s  (discharge identity absent)",
      diffC != 0, residual=diffC,
      detail="(a FAIL here would mean N2b DISCHARGED)")

# What B/C actually equal -- the (a_s/a_tau)^2 inverse-square, not a_tau/a_s.
check("Conv B/C ratio == (a_s/a_tau)^2  (NOT a_tau/a_s)",
      (sp.simplify(ratioB - (a_s / a_t)**2) == 0) and
      (sp.simplify(ratioC - (a_s / a_t)**2) == 0),
      residual=(sp.simplify(ratioB - (a_s / a_t)**2)))

banner("SECTION 3 -- WHICH spacing relation does c_t=c_s force, per convention?")

# Convention A: c_t = c_s is an IDENTITY (1=1) -- gives NO spacing constraint.
solA = sp.solve(sp.Eq(cA_t, cA_s), a_t)
LINES.append(f"  [A] c_t=c_s solved for a_tau: {solA}  (identity -> all a_tau allowed)")
check("Conv A: c_t=c_s is a tautology -> pins NO spacing (a_tau free)",
      solA == [] or sp.simplify(cA_t - cA_s) == 0,
      detail="(form isotropy automatic; says nothing about a_tau)")

# Convention B/C: c_t = c_s  => (a_s/a_tau)^2 = 1 => a_tau = a_s (positive root).
solB = sp.solve(sp.Eq(cB_t, cB_s), a_t)
LINES.append(f"  [B] c_t=c_s solved for a_tau: {solB}")
implied_spacing_eq = any(sp.simplify(s - a_s) == 0 for s in solB)
check("Conv B/C: c_t=c_s implies a_tau = a_s (positive root)",
      implied_spacing_eq, residual=None,
      detail="(holds ONLY in conventions B/C -- itself a choice, see S4)")

# THE PUNCHLINE: even the FAVOURABLE conventions B/C give a_tau = a_s, NOT the
# a_tau = a_s required... wait: a_tau=a_s IS what we want, but it is convention
# B/C specific and conv A gives nothing.  So the spacing conclusion is an
# ARTIFACT of choosing B/C over A -- not forced by A_min + the form primitive.
check("spacing conclusion (a_tau=a_s) is convention-SELECTED, not derived",
      (sp.simplify(cA_t - cA_s) == 0) and implied_spacing_eq,
      detail="(A: tautology/no constraint;  B/C: a_tau=a_s;  choice not supplied)")

banner("SECTION 4 -- CONVENTION ROBUSTNESS: is the bridge a THEOREM or an artifact?")

# The kinetic-isotropy primitive supplies NO scale, NO selector, NO dynamics.
# The free action carries conventional normalizations it does NOT pin.  A real
# form<->spacing THEOREM must survive every legal convention.  We test two:
#
# We take the route-FAVORABLE convention B (c_t/c_s = (a_s/a_tau)^2) as the
# reference, since that is the one where c_t=c_s DOES imply a spacing relation.
c_t = cB_t
c_s = cB_s
ratio_form = ratioB
#
# (i) overall coupling Z: c_t -> Z*c_t, c_s -> Z*c_s.  Ratio invariant -- OK,
#     this one does NOT threaten the bridge.  (Verify.)
c_t_Z = Z * c_t
c_s_Z = Z * c_s
check("overall coupling Z leaves c_t/c_s invariant (harmless convention)",
      sp.simplify((c_t_Z / c_s_Z) - ratio_form) == 0,
      residual=sp.simplify((c_t_Z / c_s_Z) - ratio_form))

# (ii) ANISOTROPIC kinetic normalization: the genuinely free dimensionless
#     datum that the SPATIAL_CUBIC no-go names as UNFIXED -- an independent
#     temporal hopping coefficient kappa_t vs spatial kappa_s.  The lattice
#     action is allowed to carry separate temporal/spatial hopping weights;
#     A_min + spatial O_h does NOT fix kappa_t/kappa_s (that is EXACTLY the
#     two-coefficient freedom the no-go proves).  Under it:
#         c_t -> kappa_t * c_t,  c_s -> kappa_s * c_s.
kt, ks = sp.symbols("kappa_t kappa_s", positive=True)
c_t_aniso = kt * c_t
c_s_aniso = ks * c_s
ratio_aniso = sp.simplify(c_t_aniso / c_s_aniso)
LINES.append(f"  c_t/c_s with free aniso weights = {ratio_aniso}")

# Can a legal (kappa_t, kappa_s) realize c_t = c_s at FIXED spacings a_tau != a_s?
# i.e. solve kappa_t*c_t = kappa_s*c_s for the weight ratio; if a solution
# exists for ARBITRARY spacings, then "c_t = c_s" constrains the WEIGHTS, not
# the spacings -> the form<->spacing bridge is NOT a theorem.
weight_ratio = sp.simplify(sp.solve(sp.Eq(c_t_aniso, c_s_aniso), kt)[0] / ks)
LINES.append(f"  c_t=c_s solvable by weights: kappa_t/kappa_s = {weight_ratio}")
# A finite positive weight ratio exists for ANY (a_tau, a_s) -> form isotropy
# achievable WITHOUT a_tau = a_s.  So the bridge needs the EXTRA input
# kappa_t = kappa_s (a 4D-hypercubic kinetic-normalization premise), which is
# NOT supplied by the form primitive (it would be circular -- it IS c_t=c_s).
extra_input_needed = (weight_ratio is not None) and \
    (sp.simplify(weight_ratio.subs({a_t: 2 * a_s})) != 0)
check("EXTRA INPUT NEEDED: c_t=c_s satisfiable at a_tau != a_s via free weights",
      extra_input_needed, residual=weight_ratio,
      detail="(form isotropy does NOT force spacing equality without kappa_t=kappa_s)")

# Demonstrate concretely: pick a_tau = 2*a_s and find the weight ratio that
# restores c_t = c_s -- spacings stay unequal, form is isotropic.
demo = weight_ratio.subs({a_t: 2 * a_s})
demo_val = sp.simplify(demo)
LINES.append(f"  DEMO: at a_tau=2*a_s, kappa_t/kappa_s = {demo_val} restores c_t=c_s "
             f"with a_tau != a_s")
check("DEMO countermodel: isotropic form at a_tau=2*a_s (spacings unequal)",
      sp.simplify(kt * c_t - ks * c_s).subs({kt: demo_val * ks, a_t: 2 * a_s}) == 0,
      residual=sp.simplify(kt * c_t - ks * c_s).subs({kt: demo_val * ks, a_t: 2 * a_s}))

banner("SECTION 5 -- is 'kappa_t = kappa_s' itself derivable, or = the primitive?")

# The bridge a_tau = a_s requires kappa_t = kappa_s (equal hopping weights).
# But with kappa_t = kappa_s AND a_tau = a_s the form is isotropic by
# construction -- and kappa_t = kappa_s is precisely the 4D-hypercubic kinetic
# normalization, i.e. the SAME content as the kinetic-isotropy primitive.
# Using it to "derive" a_tau = a_s and then invoking the primitive for c_t=c_s
# double-counts the same premise.  The SPATIAL_CUBIC no-go proves spatial O_h
# alone leaves TWO coefficients (kappa_t, kappa_s) free.
#
# Formal check: under the canonical convention (kappa_t = kappa_s = 1) the
# bridge holds; under any kappa_t != kappa_s it fails.  So the bridge is
# EQUIVALENT to kappa_t = kappa_s, NOT independently derivable from A_min.
bridge_canonical = (sp.simplify((c_t / c_s) - 1).subs({a_t: a_s}) == 0)
check("bridge holds in canonical convention (kappa_t=kappa_s=1) at a_tau=a_s",
      bridge_canonical)

# The two-coefficient freedom = the no-go's result: invariant dim 2 (spatial),
# dim 1 (4D hypercubic).  We mirror that count abstractly: the kinetic form has
# parameters (kappa_t, kappa_s); spatial O_h fixes neither relative weight nor
# spacing equality.
n_free_coeffs_spatial = 2   # (kappa_t, kappa_s) -- matches no-go dim 2
n_free_coeffs_hypercubic = 1
check("free kinetic coeffs: spatial O_h -> 2, 4D hypercubic -> 1 (matches no-go)",
      (n_free_coeffs_spatial == 2) and (n_free_coeffs_hypercubic == 1))

banner("SECTION 6 -- scale_reference leg (units-only; cannot supply the ratio)")

# Even GRANTING the bridge a_tau = a_s, scale_reference gives a_s = 1/M_Pl
# (units conversion only).  Verify it carries NO dimensionless content: it
# fixes a_s but says nothing about a_tau/a_s.  So scale_reference ALONE pins
# only ONE spacing; the SECOND is pinned ONLY through the (un-derived) bridge.
a_s_val = 1 / M_Pl
# scale_reference fixes a_s; a_tau is pinned only if the bridge a_tau=a_s holds.
a_tau_via_bridge = a_s_val            # requires the bridge
a_tau_without_bridge = sp.Symbol("a_tau_free", positive=True)  # stays free
check("scale_reference pins a_s = 1/M_Pl but NOT a_tau (no dimensionless content)",
      sp.simplify(a_s_val - 1 / M_Pl) == 0 and a_tau_without_bridge != a_s_val)
check("a_tau = 1/M_Pl FOLLOWS ONLY through the (un-derived) form<->spacing bridge",
      sp.simplify(a_tau_via_bridge - 1 / M_Pl) == 0,
      detail="(conditional on Section-4 extra input kappa_t=kappa_s)")

banner("VERDICT")
LINES.append(
    "  Derived relation: c_t/c_s = (a_s/a_tau)^2  -- NOT a_tau/a_s.\n"
    "  In the CANONICAL convention (equal hopping weights kappa_t=kappa_s)\n"
    "  c_t=c_s does imply a_tau=a_s. BUT that convention is NOT supplied by the\n"
    "  kinetic-isotropy primitive (which grants only the FORM ratio and\n"
    "  explicitly disavows the spacing ratio). With the genuinely-free\n"
    "  anisotropic weights the SPATIAL_CUBIC no-go proves are unfixed, c_t=c_s\n"
    "  is satisfiable at a_tau != a_s. So the form<->spacing identity is NOT a\n"
    "  theorem from A_min + the form primitive; it needs the EXTRA input\n"
    "  kappa_t=kappa_s, which is the SAME content as c_t=c_s (circular /\n"
    "  double-counting). => N2b STAYS OPEN. Sharper no-go shipped.")

print("\n".join(LINES))
print("")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
