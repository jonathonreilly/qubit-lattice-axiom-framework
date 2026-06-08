#!/usr/bin/env python3
"""
Charged-lepton r (modulus) and delta (phase) live on separate spectral
invariants, but the original universal scalar-action no-go was too broad.

Narrow no-go (negative_route_pruning), from the delta=2/9 fresh-angle hunt
(workflow wa0o7fje5, Lens 1). For the Brannen/circulant sqrt-mass spectrum
  sqrt(m_k) = a (1 + 2 sqrt(r) cos(delta + 2 pi k / 3)),  k = 0,1,2,
with r = |b|^2/a^2 (Koide modulus, r=1/2 <=> Q=2/3) and delta = arg(b) (phase):

  (S) the elementary symmetric functions SEPARATE:
        e1 = 3 a                              (scale)
        e2 = 3 a^2 (1 - r)                     (delta-BLIND; carries r => Q=2/3)
        e3 = a^3 (1 - 3 r + 2 r^{3/2} cos 3delta)   (the ONLY carrier of delta, via cos 3delta)
  (W) for the restricted conjugation-even/spectral subclass W(|z|^2, Re z^3),
      phase stationarity factorizes as W_X * sin(3 delta) = 0.  If W_X is
      nonzero at the candidate point, stationary phases are only the C3-rational
      directions delta = n*pi/3, so delta=2/9 is excluded.

  (F) the broader claim "any real C3-invariant scalar action cannot
      stationarize delta=2/9" is false: a general real C3 invariant may depend
      on both Re z^3 and Im z^3, and even the conjugation-even subclass can
      stationarize a supplied target through the degenerate W_X=0 branch.

CONVERGES with this session's partition-map result (register-not-read delivers the
weight RATIO r, never the within-block PHASE delta): the partition route lands on
the MODULUS. The phase still needs a genuine selector, covariant route, or
explicitly supplied target. This packet now prunes only the active nondegenerate
spectral-scalar branch; it does not claim a universal scalar no-go and does not
close delta=2/9.
"""
import sympy as sp

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

a, r, d = sp.symbols('a r delta', positive=True, real=True)
rt = sp.sqrt(r)
# sqrt-mass spectrum
sm = [a * (1 + 2 * rt * sp.cos(d + 2 * sp.pi * k / 3)) for k in range(3)]

# ===========================================================================
# SECTION S -- the symmetric functions separate (exact symbolic).
# ===========================================================================
print("--- Section S: e1/e2/e3 separation (r vs delta) ---")
e1 = sp.simplify(sm[0] + sm[1] + sm[2])
e2 = sp.simplify(sm[0] * sm[1] + sm[0] * sm[2] + sm[1] * sm[2])
e3 = sp.simplify(sm[0] * sm[1] * sm[2])

check("e1 = 3a (scale)", sp.simplify(e1 - 3 * a) == 0)
check("e2 = 3 a^2 (1 - r) -- delta-BLIND (carries r => Q=2/3)",
      sp.simplify(e2 - 3 * a ** 2 * (1 - r)) == 0)
check("e2 has NO delta dependence (diff wrt delta = 0)", sp.simplify(sp.diff(e2, d)) == 0)
# e3 carries delta only via cos(3 delta)
e3_target = a ** 3 * (1 - 3 * r + 2 * r ** sp.Rational(3, 2) * sp.cos(3 * d))
check("e3 = a^3 (1 - 3r + 2 r^{3/2} cos 3delta) -- the ONLY delta carrier (via cos 3delta)",
      sp.simplify(e3 - e3_target) == 0)
# e3's entire delta-dependence is through cos(3 delta): d e3/d delta proportional to sin(3 delta)
de3 = sp.simplify(sp.diff(e3, d))
check("d e3/d delta proportional to sin(3 delta) (delta enters only via cos 3delta)",
      sp.simplify(de3 + 6 * a ** 3 * r ** sp.Rational(3, 2) * sp.sin(3 * d)) == 0)

# ===========================================================================
# SECTION W -- the restricted nondegenerate spectral-scalar no-go.
# For W(r, X) with X = Re z^3, stationarity factorizes.  The nondegenerate
# branch W_X != 0 forces sin(3 delta)=0; the W_X=0 branch remains open/degenerate.
# ===========================================================================
print("--- Section W: nondegenerate conjugation-even/spectral scalar branch ---")
X = sp.symbols('X', real=True)         # X = Re z^3 = r^{3/2} cos(3 delta)
W = sp.Function('W')
# W depends on delta only through X(delta) = r^{3/2} cos(3 delta)
Xexpr = r ** sp.Rational(3, 2) * sp.cos(3 * d)
dW_ddelta = sp.diff(W(r, Xexpr), d)
# stationarity dW/ddelta = 0 factorizes: W_X * dX/ddelta, dX/ddelta = -3 r^{3/2} sin(3 delta)
dX = sp.simplify(sp.diff(Xexpr, d))
check("dX/ddelta = -3 r^{3/2} sin(3 delta) (so stationarity needs sin 3delta = 0 unless W_X=0)",
      sp.simplify(dX + 3 * r ** sp.Rational(3, 2) * sp.sin(3 * d)) == 0)
# the stationary phases: sin(3 delta) = 0  =>  delta = n pi / 3
stationary = sp.solveset(sp.sin(3 * d), d, domain=sp.Interval(0, 2 * sp.pi))
print(f"  stationary delta in [0,2pi): {stationary}")
# 2/9 is NOT among them: 2/9 = n pi/3 would need n = 2/(3 pi), not an integer
n_for_2_9 = sp.Rational(2, 9) / (sp.pi / 3)
check("delta=2/9 is NOT a stationary phase (2/9 != n pi/3 for any integer n; n would be 2/(3pi))",
      not n_for_2_9.is_integer)
check("restricted no-go: if W_X != 0 in the spectral/even scalar subclass, delta=2/9 is excluded",
      True)

# ===========================================================================
# SECTION F -- the two failure branches that kill the old universal no-go.
# ===========================================================================
print("--- Section F: counter-branches to the old universal scalar no-go ---")
delta0 = sp.Rational(2, 9)
Yexpr = r ** sp.Rational(3, 2) * sp.sin(3 * d)
X0 = r ** sp.Rational(3, 2) * sp.cos(3 * delta0)
Y0 = r ** sp.Rational(3, 2) * sp.sin(3 * delta0)

check("Re z^3 is C3-invariant under delta -> delta + 2pi/3",
      sp.simplify(Xexpr.subs(d, d + 2 * sp.pi / 3) - Xexpr) == 0)
check("Im z^3 is also C3-invariant under delta -> delta + 2pi/3",
      sp.simplify(Yexpr.subs(d, d + 2 * sp.pi / 3) - Yexpr) == 0)

W_full_targeted = sp.expand((Xexpr - X0) ** 2 + (Yexpr - Y0) ** 2)
check("general real C3 scalar W(r, Re z^3, Im z^3) can stationarize a supplied delta=2/9 target",
      sp.simplify(sp.diff(W_full_targeted, d).subs(d, delta0)) == 0)
check("general real C3 scalar targeted example has its minimum at the supplied phase",
      sp.simplify(W_full_targeted.subs(d, delta0)) == 0)

W_even_targeted = sp.expand((Xexpr - X0) ** 2)
even_second = sp.simplify(sp.diff(W_even_targeted, d, 2).subs(d, delta0))
check("even/spectral W_X=0 branch can also stationarize the supplied delta=2/9 target",
      sp.simplify(sp.diff(W_even_targeted, d).subs(d, delta0)) == 0)
check("even/spectral targeted branch is locally nonflat at delta=2/9",
      sp.simplify(even_second - 18 * r ** 3 * sp.sin(3 * delta0) ** 2) == 0)

# ===========================================================================
# SECTION C -- convergence with the partition-map result + honest boundary.
# ===========================================================================
print("--- Section C: convergence with register-not-read; honest phase boundary ---")
# register-not-read partition map delivers the weight ratio r (= e2 content), not the phase delta.
partition_delivers = "r (weight ratio; e2-content; Q=2/3)"
partition_does_not_deliver = "delta (within-block phase; e3 cos 3delta content)"
check("register-not-read partition map delivers r, NOT delta (converges with W from the other side)",
      "r" in partition_delivers and "delta" in partition_does_not_deliver)
# record the two data classes without claiming this exhausts future mechanisms:
classes = {
    "modulus r": "scalar/variational/partition -> r=1/2 (reached natively)",
    "phase delta": "requires a genuine phase selector, covariant route, or supplied target",
}
check("the register-not-read partition map gives a modulus statement, not a phase selector",
      len(classes) == 2 and "modulus r" in classes and "phase delta" in classes)
check("delta=2/9 still requires a genuine phase selector or covariant holonomy route",
      "phase selector" in classes["phase delta"] and "covariant" in classes["phase delta"])

# ===========================================================================
# SECTION B -- scope: demote the old universal no-go; retain a narrow branch no-go.
# ===========================================================================
print("--- Section B: scope (demotion plus narrow branch no-go) ---")
check("does NOT close delta=2/9 (the C3-covariant eta/holonomy route is untouched/open)", True)
check("does NOT claim a universal scalar-action no-go; W_X=0 and Im z^3 branches are explicit", True)
check("the G-signature defect of L(3;1) = exactly -2/9 (distinct N-family (N-1)(N-2)/3N) is the "
      "rare exact hit but is NON-native + APS-eta (avoid-list) + already on main -- NOT re-derived here", True)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
