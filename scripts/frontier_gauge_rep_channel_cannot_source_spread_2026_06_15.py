#!/usr/bin/env python3
"""
Conditional counting test for common-scalar and non-abelian colour channels.

Two structural facts, here consolidated into one counting bound:
 (A) COMMON-SCALAR LEMMA: if a supplied nonzero real scalar multiplies both
     a and b on a!=0, it cancels in r=|b|^2/a^2. Generation uniformity alone
     does not derive that common-scalar premise.
 (B) WITHIN-DOUBLET REP-DEGENERACY (standard identification): up/down quarks share the left-handed
     gauge rep (3,2,1/6) exactly; neutrino/charged-lepton share (1,2,-1/2). So any function of the
     unbroken NON-ABELIAN (colour) rep is constant within a weak doublet -- it gives at most a
     colourless/coloured 2-CLASS partition of the four sectors and provably cannot resolve u from d
     or nu from e.
Adjacent holonomy and record-structure channels are context; they are not re-proven here.

The SM representation table, observed r anchors, and sector readout are
explicitly conditional. This runner separates those checks from the exact
common-scalar algebra and forces no r value.

Prints "TOTAL: PASS=N FAIL=0".
"""
import numpy as np

ALGEBRA_PASS = 0
ALGEBRA_FAIL = 0
CONDITIONAL_PASS = 0
CONDITIONAL_FAIL = 0


def check(name, cond, *, kind="algebra"):
    global ALGEBRA_PASS, ALGEBRA_FAIL, CONDITIONAL_PASS, CONDITIONAL_FAIL
    if kind not in {"algebra", "conditional"}:
        raise ValueError(f"unknown check kind: {kind}")
    prefix = kind.upper()
    if cond:
        if kind == "algebra":
            ALGEBRA_PASS += 1
        else:
            CONDITIONAL_PASS += 1
        print(f"  {prefix} PASS  {name}")
    else:
        if kind == "algebra":
            ALGEBRA_FAIL += 1
        else:
            CONDITIONAL_FAIL += 1
        print(f"  {prefix} FAIL  {name}")


# ---- Supplied abstract Koide / generation algebra ----
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)
Cd = C.conj().T


def koide_r(a, b):
    return abs(b) ** 2 / a ** 2


def koide_Q(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


print("[0] supplied algebra: H=aI+bC+conj(b)C^2, a!=0, r=|b|^2/a^2")
a0, b0 = 1.0, 0.7
check("r and Q well-defined", abs(koide_Q(koide_r(a0, b0)) - (1/3 + 2/3 * 0.49)) < 1e-12)


# ============================================================================
# (A) COMMON-SCALAR HOMOGENEITY: a supplied common scalar cancels in r.
# ============================================================================
print("\n[A] common-scalar homogeneity: a supplied common scalar cancels in r")
# Conditional lemma premise: a supplied nonzero real scalar rescales both coefficients.
for s in [0.3, 1.7, 5.0, 0.01]:
    r_dressed = koide_r(s * a0, s * b0)
    check(f"common scalar s={s} leaves r invariant (cancels in ratio)",
          abs(r_dressed - koide_r(a0, b0)) < 1e-12)
# Discriminating control: different factors on a and b move r. Such dressing
# is not forbidden by generation uniformity.
r_nonuniform = koide_r(3.0 * a0, 1.0 * b0)
check("CONTROL: distinct onsite/hopping factors move r",
      abs(r_nonuniform - koide_r(a0, b0)) > 0.1)


# ============================================================================
# (B) WITHIN-DOUBLET REP-DEGENERACY => a colour-rep function gives <= 2 classes.
#     (Under the standard identification of the sectors with their SM gauge reps.)
# ============================================================================
print("\n[B] within-doublet rep-degeneracy: colour-rep functions give <= 2 classes (cannot split the spread)")
# (SU(3)_c , SU(2)_L , U(1)_Y) of the left-handed fields; the mass pairs L with R.
sectors = {
    "e":   {"colour_dim": 1, "weak_doublet": "L_L", "Y_L": -0.5},   # (1,2,-1/2)
    "nu":  {"colour_dim": 1, "weak_doublet": "L_L", "Y_L": -0.5},   # same left-handed multiplet as e
    "u":   {"colour_dim": 3, "weak_doublet": "Q_L", "Y_L": 1/6},    # (3,2,1/6)
    "d":   {"colour_dim": 3, "weak_doublet": "Q_L", "Y_L": 1/6},    # same left-handed multiplet as u
}
# any function of the unbroken NON-ABELIAN (colour) rep is constant on colour_dim
colour_classes = {s["colour_dim"] for s in sectors.values()}
check("colour rep gives exactly 2 classes over {e,nu,u,d} (colourless dim1 | coloured dim3)",
      colour_classes == {1, 3}, kind="conditional")
check("within-doublet partners share the colour rep: f_colour(u)=f_colour(d)",
      sectors["u"]["colour_dim"] == sectors["d"]["colour_dim"], kind="conditional")
check("within-doublet partners share the colour rep: f_colour(nu)=f_colour(e)",
      sectors["nu"]["colour_dim"] == sectors["e"]["colour_dim"], kind="conditional")
check("within-doublet partners share the FULL left-handed multiplet (3,2,1/6) / (1,2,-1/2)",
      sectors["u"]["weak_doublet"] == sectors["d"]["weak_doublet"] == "Q_L"
      and sectors["nu"]["weak_doublet"] == sectors["e"]["weak_doublet"] == "L_L"
      and sectors["u"]["Y_L"] == sectors["d"]["Y_L"] and sectors["nu"]["Y_L"] == sectors["e"]["Y_L"],
      kind="conditional")

# observed r-spread has MORE distinct values within a colour class than a 2-class function can supply
r_obs = {"e": 0.5, "u": 0.773, "d": 0.597}   # anchors (not derivation inputs)
coloured_rs = {round(r_obs["u"], 3), round(r_obs["d"], 3)}    # u,d share colour rep
check("observed coloured sectors have DISTINCT r (r_up != r_down) within one colour class",
      len(coloured_rs) == 2, kind="conditional")
check("=> a colour-rep function (1 value per colour class) CANNOT reproduce r_up != r_down (2-class bound violated)",
      len(coloured_rs) > len({sectors["u"]["colour_dim"]}), kind="conditional")


# ============================================================================
# (C) One named open comparator is ABELIAN / EWSB data; this is not exclusive.
# ============================================================================
print("\n[C] named open comparator: abelian/EWSB data (right-handed Y / T3); other routes untested")
# The left-handed quark multiplet is identical, while its supplied standard
# right-handed partners have different hypercharges.  No nu_R is assumed:
# the minimal SM has none, and a Dirac/sterile-neutrino comparator would be an
# additional premise.
Y_R = {"u": 2/3, "d": -1/3, "e": -1.0}
check("right-handed hypercharge distinguishes the quark partners (Y_R(u) != Y_R(d))",
      Y_R["u"] != Y_R["d"], kind="conditional")
# but the spread is not a clean function of the unbroken electric charge either (recorded FIT)
Q_em = {"u": 2/3, "d": -1/3, "e": -1.0}
# the r-ordering (e<d<u) does NOT match |Q| ordering (d<u<e) or Q^2 ordering -> not a charge function
order_r = sorted(r_obs, key=lambda k: r_obs[k])             # ['e','d','u']
order_absQ = sorted(Q_em, key=lambda k: abs(Q_em[k]))       # ['d','u','e']
check("r-ordering (e<d<u) does NOT match |Q|-ordering (d<u<e) => no monotone |Q| law (FIT)",
      order_r != order_absQ, kind="conditional")


# ============================================================================
# (D) FIREWALL consistency checks: forces no r value; the result is a counting/degeneracy bound.
#     (Smoke/consistency, not the load-bearing proof -- that is sections A-C.)
# ============================================================================
print("\n[D] firewall consistency checks: no r value forced; r is free registered data")
check("Q(r)=1/3+2r/3 valid for all observed sector r (none forced)",
      all(1/3 - 1e-9 <= koide_Q(r) <= 1 + 1e-9 for r in r_obs.values()),
      kind="conditional")
# genuine firewall test: r is a free 2-parameter (a,b) family -- distinct couplings give distinct r,
# both valid; the runner selects none. AND the channel under-determines r (more distinct r than gauge classes).
check("distinct free couplings give distinct valid r (r is a free input, never selected)",
      abs(koide_r(1.0, 0.7) - koide_r(1.0, 0.9)) > 1e-3)
n_distinct_r = len({round(v, 3) for v in r_obs.values()})
check("more distinct observed r (3) than unbroken-colour classes (2) => r is NOT a gauge-class function",
      n_distinct_r > len(colour_classes), kind="conditional")


total_pass = ALGEBRA_PASS + CONDITIONAL_PASS
total_fail = ALGEBRA_FAIL + CONDITIONAL_FAIL
print(
    f"\nSCORECARD ALGEBRA_PASS={ALGEBRA_PASS} ALGEBRA_FAIL={ALGEBRA_FAIL} "
    f"CONDITIONAL_PASS={CONDITIONAL_PASS} CONDITIONAL_FAIL={CONDITIONAL_FAIL}"
)
print(f"TOTAL: PASS={total_pass} FAIL={total_fail}")
if total_fail:
    raise SystemExit(1)
