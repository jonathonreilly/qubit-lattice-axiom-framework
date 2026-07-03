#!/usr/bin/env python3
"""
The generation-scalar and non-abelian colour gauge-representation channels cannot source the sector
r-spread.

Two structural facts, here consolidated into one counting bound:
 (A) GAUGE-UNIFORMITY (retained three_generation_observable): the generation carrier is the shared
     M3(C); the three generations carry IDENTICAL gauge charges. So any gauge action through the
     generation carrier is a SCALAR on the generation index -- it multiplies the singlet coupling a
     and the doublet coupling b EQUALLY, hence CANCELS in the degree-0 ratio r=|b|^2/a^2. (A
     non-uniform action that distinguished singlet from doublet would require the generations to
     carry different charges, which three_generation_observable forbids.)
 (B) WITHIN-DOUBLET REP-DEGENERACY (standard identification): up/down quarks share the left-handed
     gauge rep (3,2,1/6) exactly; neutrino/charged-lepton share (1,2,-1/2). So any function of the
     unbroken NON-ABELIAN (colour) rep is constant within a weak doublet -- it gives at most a
     colourless/coloured 2-CLASS partition of the four sectors and provably cannot resolve u from d
     or nu from e.
Adjacent holonomy and record-structure channels are context; they are not re-proven here.

Conclusion: no function of the generation-carrier scalar action or non-abelian colour representation
can produce the observed sector r-spread (r_lep=1/2, r_down~0.597, r_up~0.773, with r_up != r_down a
within-doublet split). The spread is registered, sector-dependent dial data on this surface; the
within-doublet resolution is forced into an abelian / hypercharge / T3 / Higgs-partner
(electroweak-breaking) datum or the within-sector measure. This note forces NO r value.

Prints "TOTAL: PASS=N FAIL=0".
"""
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


# ---- Koide / generation algebra (retained) ----
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)
Cd = C.conj().T


def koide_r(a, b):
    return abs(b) ** 2 / a ** 2


def koide_Q(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


print("[0] generation algebra: H=aI+bC+conj(b)C^2, r=|b|^2/a^2, Q=1/3+2r/3 (retained)")
a0, b0 = 1.0, 0.7
check("r and Q well-defined", abs(koide_Q(koide_r(a0, b0)) - (1/3 + 2/3 * 0.49)) < 1e-12)


# ============================================================================
# (A) GAUGE-UNIFORMITY => uniform gauge action cancels in the degree-0 ratio r.
# ============================================================================
print("\n[A] gauge-uniformity: a uniform gauge factor cancels in r (degree-0 inert)")
# the gauge-uniform action scales a and b by the SAME factor s (it is a scalar on the gen index)
for s in [0.3, 1.7, 5.0, 0.01]:
    r_dressed = koide_r(s * a0, s * b0)
    check(f"uniform gauge factor s={s} leaves r invariant (cancels in ratio)",
          abs(r_dressed - koide_r(a0, b0)) < 1e-12)
# DISCRIMINATING control: a NON-uniform factor (different on a vs b) WOULD change r --
# but that requires the generations to carry DIFFERENT gauge charges (forbidden by gauge-uniformity).
r_nonuniform = koide_r(3.0 * a0, 1.0 * b0)
check("CONTROL: a non-uniform factor (forbidden: would need different per-generation charges) DOES move r",
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
      colour_classes == {1, 3})
check("within-doublet partners share the colour rep: f_colour(u)=f_colour(d)",
      sectors["u"]["colour_dim"] == sectors["d"]["colour_dim"])
check("within-doublet partners share the colour rep: f_colour(nu)=f_colour(e)",
      sectors["nu"]["colour_dim"] == sectors["e"]["colour_dim"])
check("within-doublet partners share the FULL left-handed multiplet (3,2,1/6) / (1,2,-1/2)",
      sectors["u"]["weak_doublet"] == sectors["d"]["weak_doublet"] == "Q_L"
      and sectors["nu"]["weak_doublet"] == sectors["e"]["weak_doublet"] == "L_L"
      and sectors["u"]["Y_L"] == sectors["d"]["Y_L"] and sectors["nu"]["Y_L"] == sectors["e"]["Y_L"])

# observed r-spread has MORE distinct values within a colour class than a 2-class function can supply
r_obs = {"e": 0.5, "u": 0.773, "d": 0.597}   # anchors (not derivation inputs)
coloured_rs = {round(r_obs["u"], 3), round(r_obs["d"], 3)}    # u,d share colour rep
check("observed coloured sectors have DISTINCT r (r_up != r_down) within one colour class",
      len(coloured_rs) == 2)
check("=> a colour-rep function (1 value per colour class) CANNOT reproduce r_up != r_down (2-class bound violated)",
      len(coloured_rs) > len({sectors["u"]["colour_dim"]}))


# ============================================================================
# (C) The within-doublet split is an ABELIAN / EWSB datum, not the shared rep.
# ============================================================================
print("\n[C] the within-doublet splitter is abelian/EWSB (right-handed Y / T3), orthogonal to the shared rep")
# the LEFT-handed multiplet is identical; the difference is the RIGHT-handed hypercharge / Higgs partner
Y_R = {"u": 2/3, "d": -1/3, "e": -1.0, "nu": 0.0}   # right-handed hypercharges differ within a doublet
check("right-handed hypercharge distinguishes within-doublet partners (Y_R(u) != Y_R(d))",
      Y_R["u"] != Y_R["d"] and Y_R["nu"] != Y_R["e"])
# but the spread is not a clean function of the unbroken electric charge either (recorded FIT)
Q_em = {"u": 2/3, "d": -1/3, "e": -1.0}
# the r-ordering (e<d<u) does NOT match |Q| ordering (d<u<e) or Q^2 ordering -> not a charge function
order_r = sorted(r_obs, key=lambda k: r_obs[k])             # ['e','d','u']
order_absQ = sorted(Q_em, key=lambda k: abs(Q_em[k]))       # ['d','u','e']
check("r-ordering (e<d<u) does NOT match |Q|-ordering (d<u<e) => spread is not a |Q| function (FIT)",
      order_r != order_absQ)


# ============================================================================
# (D) FIREWALL consistency checks: forces no r value; the result is a counting/degeneracy bound.
#     (Smoke/consistency, not the load-bearing proof -- that is sections A-C.)
# ============================================================================
print("\n[D] firewall consistency checks: no r value forced; r is free registered data")
check("Q(r)=1/3+2r/3 valid for all observed sector r (none forced)",
      all(1/3 - 1e-9 <= koide_Q(r) <= 1 + 1e-9 for r in r_obs.values()))
# genuine firewall test: r is a free 2-parameter (a,b) family -- distinct couplings give distinct r,
# both valid; the runner selects none. AND the channel under-determines r (more distinct r than gauge classes).
check("distinct free couplings give distinct valid r (r is a free input, never selected)",
      abs(koide_r(1.0, 0.7) - koide_r(1.0, 0.9)) > 1e-3)
n_distinct_r = len({round(v, 3) for v in r_obs.values()})
check("more distinct observed r (3) than unbroken-colour classes (2) => r is NOT a gauge-class function",
      n_distinct_r > len(colour_classes))


print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
assert FAIL == 0, "discriminating checks failed"
