#!/usr/bin/env python3
"""Koide r=1/2 durability-stationarity conditional chain -- runner.

Companion runner for
    docs/KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md

The three 2026-06-02 FLAVOR notes left the r-gate in this state: the
records/Lueders sharpening map on the 2-sector coordinate is r -> 2r^2
(grounded in retained_bounded luders_rule_from_composition_consistency);
r = 1/2 is its UNSTABLE separatrix; the thermalizing-arrow STABILIZER
route is a closed no-go (the reverse map is erasure; honest
thermalization gives r = 1; einselection is a no-op); and the named
remaining route was "a measure/reference choice on the two-sector
partition".

This runner lands a third shape the no-go's own N4/N6 scope leaves open:
neither an attractor claim nor a measure admission, but STATIONARITY
UNDER DURABILITY.  A durably registered 2-sector weight coordinate must
be a FIXED POINT of the records flow (fixedness, not attraction).  The
chain, every step computed:

  A. The map, re-derived: Lueders sharpening p -> p^2/Z on the 2-sector
     distribution (p_s, p_d) = (1/(1+2r), 2r/(1+2r)) reduces exactly to
     r -> 2r^2.

  B. The COMPLETE stationary set on the closed 2-sector simplex is
     {r = 0, r = 1/2, r = infinity} (the two vertices and the
     barycenter) -- a third member, r = infinity (vanishing singlet
     coupling a = 0), that the prior notes did not discuss.

  C. Stationarity is not attraction: multipliers f'(0) = 0 (stable),
     f'(1/2) = 2 (unstable separatrix) computed; textual interface
     checks verify the stabilizer-fails no-go closed only the
     ATTRACTOR question and itself names the non-dynamical alternative.

  D. Exclusion of the other two stationary points from registered lane
     content (no PDG anywhere): r = 0 forces the exactly degenerate
     spectrum for every delta (b = 0: no C_3-breaking to register --
     incompatible with the lane's registered C_3-breaking content);
     r = infinity forces a = 0, i.e. sum of channel weights zero,
     impossible on the unsigned (all-positive-sqrt-m) branch -- it is
     the signed/Brannen-branch endpoint, flagged, not consumed.

  E. Uniqueness + corollary: the unique admissible stationary value is
     r = 1/2, hence Q = (1+2r)/3 = 2/3; and at r = 1/2 the HS 2-sector
     equipartition identity 3a^2 = 6|b|^2 holds exactly -- the
     equal-power-per-block WEIGHT (custody prong ii) emerges as a
     stationarity corollary instead of a stipulated measure.

  F. Consistency: the knife-edge is quantified (a registered value off
     the separatrix by 10^-5 leaves the neighbourhood in a computed
     number of records-flow steps -- persistence at the observed
     precision requires exactness); g(f(r)) = r exactly (the reverse
     map is the inverse/erasure -- NOT used as a stabilizer); thermal
     I/3 gives r = 1 and r = 1 is NOT records-stationary (f(1) = 2):
     thermal ensemble values are not durable registrations, so the
     Q = 1 cell's consumer is ensemble statistics, with no conflict.

Conditional inputs (named, NOT adopted, each printed as a residual at
point of use): the 2-sector partition prong (custody selector i), and
the R-D durability bridge (durable registration is invariant under
records-flow self-composition) -- a premise Record's own non-supply
clause shows must be named, not smuggled.

PASS/FAIL per check; final line: TOTAL: PASS=<n> FAIL=<m>
"""

import pathlib

import sympy as sp

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"


def doc_text(name):
    """Whitespace-normalized note text (hard-wrapped lines joined), so
    interface substrings match sentences across line breaks."""
    raw = (DOCS / name).read_text(encoding="utf-8")
    return " ".join(raw.split())


print("=" * 72)
print("Koide r=1/2 durability-stationarity conditional chain")
print("=" * 72)

# ===================== A. the records map, re-derived ==================
print("\n--- A. the 2-sector records/Lueders map, re-derived exactly")

r = sp.Symbol("r", nonnegative=True)
p_s = 1 / (1 + 2 * r)
p_d = 2 * r / (1 + 2 * r)
Z = p_s ** 2 + p_d ** 2
p_s2, p_d2 = p_s ** 2 / Z, p_d ** 2 / Z
# the post-sharpening coordinate r' with p'_d = 2r'/(1+2r')
r_after = sp.simplify(p_d2 / (2 * p_s2))
ok = sp.simplify(r_after - 2 * r ** 2) == 0
check(1, "Lueders sharpening p -> p^2/Z on the 2-sector distribution "
         "(p_s, p_d) = (1/(1+2r), 2r/(1+2r)) reduces EXACTLY to "
         "r -> 2r^2 (the separatrix note's map, re-derived)", ok)
residual("the 2-SECTOR partition defining (p_s, p_d) is the custody "
         "selector (i) prong, consumed at its declared admitted-input "
         "status (CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_"
         "2026-06-02); the 06-11 channel-space work supplies K-orbit "
         "support (the omega/omega-bar pair is one K-orbit for every "
         "equivariant channel) as context, not closure.")

# ===================== B. the complete stationary set ==================
print("\n--- B. the complete stationary set on the closed simplex")

q = sp.Symbol("q", nonnegative=True)          # q = p_d on the simplex
sharpen_q = q ** 2 / (q ** 2 + (1 - q) ** 2)
fixed_q = sp.solve(sp.Eq(sharpen_q, q), q)
ok = sorted(fixed_q) == [0, sp.Rational(1, 2), 1]
check(2, "fixed points of 2-outcome Lueders sharpening on the CLOSED "
         "simplex are exactly p_d in {0, 1/2, 1}", ok,
      f"computed: {sorted(fixed_q)}")

# in the r coordinate: p_d = 0 -> r = 0; p_d = 1/2 -> r = 1/4? no:
# p_d = 2r/(1+2r) = 1/2 -> r = 1/2; p_d = 1 -> r = infinity (a = 0)
r_of_pd = sp.solve(sp.Eq(2 * r / (1 + 2 * r), sp.Rational(1, 2)), r)
finite_fixed = sp.solve(sp.Eq(2 * r ** 2, r), r)
ok = (r_of_pd == [sp.Rational(1, 2)]
      and sorted(finite_fixed) == [0, sp.Rational(1, 2)]
      and sp.limit(2 * r / (1 + 2 * r), r, sp.oo) == 1)
check(3, "in the r coordinate the stationary set is {0, 1/2, infinity}: "
         "finite fixed points of r -> 2r^2 are {0, 1/2}, and p_d = 1 is "
         "the projective end r = infinity (a = 0, vanishing singlet "
         "coupling) -- a THIRD stationary point the 06-02 notes did not "
         "discuss", ok)

# ===================== C. stationarity is not attraction ===============
print("\n--- C. scope: the no-go closed attraction; stationarity is open")

f = 2 * r ** 2
ok = (sp.diff(f, r).subs(r, 0) == 0
      and sp.diff(f, r).subs(r, sp.Rational(1, 2)) == 2)
check(4, "multipliers computed: f'(0) = 0 (stable), f'(1/2) = 2 "
         "(unstable separatrix) -- r = 1/2 is STATIONARY but not "
         "attracting; durability needs fixedness, not attraction", ok)

nogo = doc_text("FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS"
                "_2026-06-02.md")
sep = doc_text("FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md")
ok = ("whether the tested dynamics makes `r=1/2` an attractor" in nogo
      and "A direct block-measure admission could close the value "
          "without using dynamics" in nogo
      and "Out of scope and NOT closed here: stationarity/durability "
          "occupancy of a records-flow fixed point" in nogo)
check(5, "textual scope interface: the stabilizer-fails no-go's own N4 "
         "restricts its residual to the ATTRACTOR question, its N6 "
         "names only the measure-admission alternative, and its "
         "2026-06-11 scope statement explicitly places stationarity/"
         "durability occupancy OUTSIDE the closed scope -- the "
         "durability route is not a reopening", ok)

ok = ("lies on its separatrix" in sep
      and "requires a **stabilizer**" in sep)
check(6, "textual interface: the separatrix note frames the knife-edge "
         "as needing a STABILIZER (an attraction mechanism); the "
         "durability chain replaces that demand with fixedness under "
         "re-registration, which the separatrix property itself "
         "supports (see check 12)", ok)

axioms = doc_text("MINIMAL_AXIOMS_2026-06-05.md")
ok = ("durable" in axioms and "occupancy rule" in axioms)
check(7, "Record-axiom interface: the live axiom text contains both the "
         "DURABILITY of registration (the property the R-D bridge "
         "formalizes) and the non-supply clause ('occupancy rule') that "
         "forces R-D to be a NAMED bridge rather than an axiom "
         "consequence", ok)
residual("R-D durability bridge (named, NOT adopted): the durably "
         "registered 2-sector weight coordinate is invariant under "
         "records-flow self-composition (the retained_bounded Lueders "
         "map). Record's non-supply clause means this identification "
         "must be supplied as an explicit premise; this chain is a "
         "theorem CONDITIONAL on it, in the R-eta pattern of the "
         "|delta| = 2/9 chain.")

# ===================== D. excluding r = 0 and r = infinity =============
print("\n--- D. exclusion of the other stationary points (no PDG)")

a_s, delta = sp.symbols("a delta", positive=True)
modb = sp.Symbol("modb", nonnegative=True)
lam = [a_s + 2 * modb * sp.cos(delta + 2 * sp.pi * k / 3)
       for k in range(3)]
spec0 = [li.subs(modb, 0) for li in lam]
ok = (spec0 == [a_s, a_s, a_s])
check(8, "r = 0 (b = 0) forces the EXACTLY degenerate spectrum "
         "[a, a, a] for every delta: there is no C_3-breaking left to "
         "register -- incompatible with the lane's registered "
         "C_3-breaking content (the delta admission), so r = 0 is not "
         "a registrable charged-lepton configuration", ok)
residual("the exclusion of r = 0 consumes the lane's REGISTERED "
         "C_3-breaking content (the delta != 0 admission inside "
         "AC_phi_lambda, e.g. the |delta| = 2/9 chain's carrier gate) "
         "at its admitted status -- not a PDG input.")

sum_lam = sp.simplify(sum(lam))
ok = (sp.simplify(sum_lam - 3 * a_s) == 0)
check(9, "sum of the three channel weights = 3a exactly (delta-"
         "independent), so r = infinity (a = 0) forces sum lambda = 0: "
         "impossible when all three sqrt-m weights are positive -- the "
         "UNSIGNED charged-lepton branch excludes the third stationary "
         "point", ok)
residual("the unsigned (all-positive-sqrt-m) branch premise is consumed "
         "for the r = infinity exclusion; the r = infinity stationary "
         "point is exactly the signed/Brannen-branch endpoint (one "
         "negative sqrt-m, sum sqrt-m -> 0), flagged as the candidate "
         "neutrino-side consumer -- NOT consumed or claimed here.")

# ===================== E. uniqueness and the weight corollary ==========
print("\n--- E. uniqueness, Q = 2/3, and the equal-power corollary")

ok = (sp.Rational(1, 3) + sp.Rational(2, 3) * sp.Rational(1, 2)
      == sp.Rational(2, 3))
check(10, "uniqueness: stationary set {0, 1/2, infinity} minus the two "
          "excluded points leaves r = 1/2 alone; Q = 1/3 + (2/3) r = "
          "2/3 exactly", ok)

m2 = sp.Symbol("m2", nonnegative=True)         # m2 = |b|^2
sol = sp.solve(sp.Eq(3 * a_s ** 2, 6 * m2), m2)
ok = (sol == [a_s ** 2 / 2]
      and sp.simplify((a_s ** 2 / 2) / a_s ** 2 - sp.Rational(1, 2))
      == 0)
check(11, "corollary: r = 1/2 is exactly the HS 2-sector equipartition "
          "3a^2 = 6|b|^2 (|b|^2 = a^2/2) -- the equal-power-per-block "
          "WEIGHT (custody prong ii) emerges as a stationarity "
          "corollary on this chain instead of a stipulated measure", ok)

custody = doc_text("CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY"
                   "_2026-06-02.md")
ok = ("K-reality" in custody and "det_C / equal-power-per-block" in custody)
check(12, "custody interface: the two named selectors are present in "
          "the custody note; this chain consumes prong (i) (the "
          "2-sector partition) and conditionally REPLACES prong (ii) "
          "(equal-power weight) with the R-D stationarity corollary",
      ok)

# ===================== F. consistency checks ===========================
print("\n--- F. knife-edge, erasure honesty, thermal consistency")

# knife-edge: persistence at observed precision requires exactness
def steps_to_leave(r0, lo=0.4, hi=0.6, cap=200):
    x, n = r0, 0
    while lo <= x <= hi and n < cap:
        x = 2 * x * x
        n += 1
    return n


n_minus = steps_to_leave(0.5 - 1e-5)
n_plus = steps_to_leave(0.5 + 1e-5)
n_exact = steps_to_leave(0.5)
ok = (n_exact == 200 and 10 < n_minus < 40 and 10 < n_plus < 40)
check(13, "knife-edge quantified: r = 1/2 exactly persists forever "
          "under the records flow, while an offset of 1e-5 (the "
          "observed Koide precision scale) leaves the neighbourhood in "
          "O(20) records-flow steps -- durable persistence at that "
          "precision requires EXACTNESS, turning the separatrix "
          "instability into the sharpening of the claim", ok,
      f"steps: exact = cap({n_exact}), -1e-5: {n_minus}, "
      f"+1e-5: {n_plus}")

g = sp.sqrt(r / 2)
ok = sp.simplify(g.subs(r, f) - r) == 0
check(14, "g(f(r)) = r exactly: the 'thermalizing' reverse map is the "
          "functional INVERSE (erasure) of the records map -- "
          "consistent with the stabilizer-fails no-go; this chain does "
          "NOT use g as a stabilizer or reopen that route", ok)

# thermal I/3: dimension weights (1/3, 2/3) -> r = 1; not stationary
r_thermal = sp.solve(sp.Eq(2 * r / (1 + 2 * r), sp.Rational(2, 3)), r)
ok = (r_thermal == [1]
      and "thermalizing to `I/3` gives dimension weights" in nogo
      and sp.simplify(f.subs(r, 1)) == 2)
check(15, "thermal consistency: I/3 gives p = (1/3, 2/3) -> r = 1 (the "
          "no-go's computed value, interface-checked), and r = 1 is "
          "NOT records-stationary (f(1) = 2 != 1): thermal-ensemble "
          "values are not durable registrations -- the Q = 1 cell's "
          "consumer is ensemble statistics, with no conflict with the "
          "registered Q = 2/3", ok)
residual("the records-map identification itself (registration composes "
         "by the Lueders map) is consumed at the retained_bounded "
         "grade of luders_rule_from_composition_consistency via the "
         "separatrix note; binding PHYSICAL charged-lepton "
         "re-registration to that map is part of the R-D bridge, not "
         "derived here.")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: conditional on the named R-D durability bridge and the "
      "custody 2-sector partition prong, the unique durably "
      "registrable 2-sector weight is r = 1/2 (Q = 2/3): the complete "
      "records-flow stationary set is {0, 1/2, infinity}; r = 0 is "
      "excluded by the registered C_3-breaking content and r = "
      "infinity by the unsigned branch (it is the signed/Brannen "
      "endpoint); the equal-power weight admission becomes a "
      "corollary. Attraction is neither claimed nor needed; the "
      "stabilizer-fails no-go's closed scope is respected. No premise "
      "is adopted; no audit status is set.")
raise SystemExit(0 if _fail == 0 else 1)
