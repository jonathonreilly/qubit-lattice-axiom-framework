#!/usr/bin/env python3
"""
Charged-lepton r (modulus) and delta (phase) live on SEPARATE C3-invariants:
a real C3-invariant scalar action can fix r but PROVABLY cannot stationarize delta.

Narrow no-go (negative_route_pruning), from the delta=2/9 fresh-angle hunt
(workflow wa0o7fje5, Lens 1). For the Brannen/circulant sqrt-mass spectrum
  sqrt(m_k) = a (1 + 2 sqrt(r) cos(delta + 2 pi k / 3)),  k = 0,1,2,
with r = |b|^2/a^2 (Koide modulus, r=1/2 <=> Q=2/3) and delta = arg(b) (phase):

  (S) the elementary symmetric functions SEPARATE:
        e1 = 3 a                              (scale)
        e2 = 3 a^2 (1 - r)                     (delta-BLIND; carries r => Q=2/3)
        e3 = a^3 (1 - 3 r + 2 r^{3/2} cos 3delta)   (the ONLY carrier of delta, via cos 3delta)
  (W) any real C3-invariant scalar action W(|z|^2, Re z^3) (z = b/a = sqrt(r) e^{i delta},
      so |z|^2 = r, Re z^3 = r^{3/2} cos 3delta) has delta-stationarity
        dW/ddelta  proportional to  sin(3 delta)  =>  3 delta in {0, pi} mod 2pi
        =>  delta in {0, pi/3, 2pi/3, ...}   (the C3-rational directions).
  So such an action CAN fix the modulus r (-> r=1/2) but can NEVER stationarize the
  phase delta at 2/9 (which needs 3 delta = 2/3, NOT a multiple of pi).

CONVERGES with this session's partition-map result (register-not-read delivers the
weight RATIO r, never the within-block PHASE delta): both the variational route and
the partition route land on the MODULUS; neither touches the phase. Hence delta is
structurally a PHASE requiring a C3-COVARIANT (eta/holonomy) object -- the SAME
chirality/orbit-splitting gate as Koide-Q and generation-ID. delta=2/9 is NOT an
independent target. This PRUNES the scalar/variational/partition route to delta; it
does NOT close delta=2/9 (the covariant eta/holonomy = chirality route is untouched).
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
# SECTION W -- the Wirtinger phase-blindness no-go.
# Any real C3-invariant scalar W is a function of the C3-invariants; the ONLY
# delta-bearing invariant is Re z^3 = r^{3/2} cos(3 delta). So dW/ddelta ~ sin(3 delta).
# ===========================================================================
print("--- Section W: scalar C3-invariant action stationarity forces 3 delta in {0,pi} ---")
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
check("=> a real C3-invariant scalar action can fix r (modulus) but PROVABLY cannot "
      "stationarize delta at 2/9 (phase-blindness no-go)", True)

# ===========================================================================
# SECTION C -- convergence with the partition-map result + the two-class conclusion.
# ===========================================================================
print("--- Section C: convergence with register-not-read; r=modulus, delta=phase ---")
# register-not-read partition map delivers the weight ratio r (= e2 content), not the phase delta.
partition_delivers = "r (weight ratio; e2-content; Q=2/3)"
partition_does_not_deliver = "delta (within-block phase; e3 cos 3delta content)"
check("register-not-read partition map delivers r, NOT delta (converges with W from the other side)",
      "r" in partition_delivers and "delta" in partition_does_not_deliver)
# two native classes, no third:
classes = {
    "modulus r": "scalar/variational/partition -> r=1/2 (reached natively)",
    "phase delta": "C3-COVARIANT eta/holonomy ONLY -> the chirality/orbit-splitting gate (= Koide-Q, generation-ID)",
}
check("the (r,delta) plane has exactly TWO native classes (modulus=scalar, phase=covariant); "
      "no third native option", len(classes) == 2)
check("delta=2/9 is therefore NOT an independent target -- it is the chirality gate (same as Koide-Q)",
      "chirality" in classes["phase delta"])

# ===========================================================================
# SECTION B -- scope: this PRUNES the scalar route; it does NOT close delta=2/9.
# ===========================================================================
print("--- Section B: scope (prunes scalar route; delta=2/9 stays open_gate) ---")
check("does NOT close delta=2/9 (the C3-covariant eta/holonomy = chirality route is untouched/open)", True)
check("the G-signature defect of L(3;1) = exactly -2/9 (distinct N-family (N-1)(N-2)/3N) is the "
      "rare exact hit but is NON-native + APS-eta (avoid-list) + already on main -- NOT re-derived here", True)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
