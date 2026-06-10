#!/usr/bin/env python3
"""Class-A runner: electroweak dependency-composition over the EWSB source-proposal DAG.

Re-verifies, with exact rational arithmetic, the three electroweak source proposals on
origin/main and the composition that ties them together:

  parent : EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02   (Q = T3 + Y/2)
  child A: EM_COUPLING_FROM_EWSB_NOTE_2026-05-02        (e = g sin th = g' cos th)
  child B: W_Z_MASS_RATIO_FROM_EWSB_NOTE_2026-05-02     (MW^2/MZ^2 = cos^2 th, rho = 1)

Dependency edges (quoted in the paired note): child A and child B each consume the
parent's Q = T3 + Y/2 pattern; both children are governed by the SAME electroweak mixing
angle th_W (tan th_W = g'/g) inherited through the EWSB pattern.

NEW composed content (in no single child note): eliminating the shared th_W between the
two children yields the cross-child relation  e^2/g^2 + MW^2/MZ^2 = 1  (equivalently
MW^2/MZ^2 = 1 - e^2/g^2). This is the load-bearing payload of the dependency structure:
the two children are NOT independent results -- they are two faces of one mixing angle.

Authors NO audit status for any note; this runner re-checks the cited identities only.
No PDG/fitted value is consumed as an input; all checks are exact rational tautologies
over arbitrary rational gauge-coupling instantiations. Absolute scales (v, g, g', and the
scale-dependent value of th_W) are external observables and are not asserted here.
"""
from fractions import Fraction as F

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")


# ----------------------------------------------------------------------------
# NODE (parent): Q = T3 + Y/2 from the Higgs Y_H = +1 VEV alignment.
# Convention: weak hypercharge Y with Q = T3 + Y/2 (the parent note's convention).
# ----------------------------------------------------------------------------
# (T3, Y) for the standard chiral SM content + the two Higgs doublet components.
SM_CONTENT = {
    "u_L": (F(1, 2), F(1, 3), F(2, 3)),
    "d_L": (F(-1, 2), F(1, 3), F(-1, 3)),
    "nu_L": (F(1, 2), F(-1), F(0)),
    "e_L": (F(-1, 2), F(-1), F(-1)),
    "u_R": (F(0), F(4, 3), F(2, 3)),
    "d_R": (F(0), F(-2, 3), F(-1, 3)),
    "e_R": (F(0), F(-2), F(-1)),
    "nu_R": (F(0), F(0), F(0)),
    "H+": (F(1, 2), F(1), F(1)),
    "H0": (F(-1, 2), F(1), F(0)),
}
for name, (t3, y, q_expected) in SM_CONTENT.items():
    check(f"node parent: Q=T3+Y/2 for {name}", t3 + y / 2 == q_expected)

# Unbroken-photon / broken-generator structure on the neutral VEV <H> ~ (0, 1).
# On the lower (neutral) doublet component: T3 = -1/2, Y_H = +1.
t3_neutral, y_higgs = F(-1, 2), F(1)
alpha = F(1, 2)  # the coefficient solving (T3 + alpha*Y)<H> = 0
check("node parent: photon (T3 + 1/2 Y) annihilates neutral VEV",
      t3_neutral + alpha * y_higgs == 0)
# The three would-be-broken combinations act nonzero on the VEV:
#  T1, T2 (off-diagonal, move the neutral component) and the orthogonal (T3 - Y/2).
check("node parent: orthogonal Z-direction (T3 - 1/2 Y) acts nonzero on neutral VEV",
      t3_neutral - alpha * y_higgs != 0)

# ----------------------------------------------------------------------------
# NODES (children) + EDGES + COMPOSITION, over arbitrary rational gauge couplings.
# Parameterize by (g^2, g'^2); define the SHARED mixing angle via the EWSB pattern:
#   sin^2 th = g'^2/(g^2+g'^2),  cos^2 th = g^2/(g^2+g'^2).
# ----------------------------------------------------------------------------
COUPLINGS = [
    (F(1), F(1)),
    (F(4), F(3)),
    (F(100), F(1)),       # extreme ratio
    (F(7, 11), F(13, 17)),  # non-trivial rationals
    (F(3), F(5)),         # GUT-flavoured sin^2 = 5/8? -> checked below symbolically
    (F(1), F(0)),         # g' -> 0 limit (no mixing)
]
for g2, gp2 in COUPLINGS:
    denom = g2 + gp2
    s2 = gp2 / denom          # sin^2 th_W
    c2 = g2 / denom           # cos^2 th_W
    # child A: e = g sin = g' cos  <=>  e^2 = g^2 sin^2 = g'^2 cos^2
    e2 = g2 * s2
    check(f"node child A: e^2 = g^2 sin^2 = g'^2 cos^2  (g2={g2},gp2={gp2})",
          e2 == gp2 * c2)
    # child A internal: 1/e^2 = 1/g^2 + 1/g'^2  (skip the g'=0 singular case)
    if e2 != 0 and gp2 != 0:
        check(f"node child A: 1/e^2 = 1/g^2 + 1/g'^2  (g2={g2},gp2={gp2})",
              1 / e2 == 1 / g2 + 1 / gp2)
    # child B: MW^2/MZ^2 = g^2/(g^2+g'^2) = cos^2 th_W ; rho = 1
    mw2_over_mz2 = g2 / denom
    check(f"node child B: MW^2/MZ^2 = cos^2 th_W  (g2={g2},gp2={gp2})",
          mw2_over_mz2 == c2)
    if c2 != 0:
        check(f"node child B: rho = (MW^2/MZ^2)/cos^2 = 1  (g2={g2},gp2={gp2})",
              mw2_over_mz2 / c2 == 1)
    # EDGE consistency: both children built on the SAME th_W (Pythagorean closure)
    check(f"edge: sin^2 + cos^2 = 1 (shared th_W)  (g2={g2},gp2={gp2})", s2 + c2 == 1)
    # COMPOSITION (NEW): e^2/g^2 + MW^2/MZ^2 = 1  (cross-child, requires both + parent)
    check(f"COMPOSITION: e^2/g^2 + MW^2/MZ^2 = 1  (g2={g2},gp2={gp2})",
          e2 / g2 + mw2_over_mz2 == 1)
    # sibling form
    check(f"COMPOSITION sibling: MW^2/MZ^2 = 1 - e^2/g^2  (g2={g2},gp2={gp2})",
          mw2_over_mz2 == 1 - e2 / g2)

# ----------------------------------------------------------------------------
# Cross-node consistency the child notes themselves record (symbolic, no PDG input):
# at a hypothetical sin^2 th = 3/8, the mass ratio cos^2 th = 5/8 and e^2/g^2 = 3/8 close.
# ----------------------------------------------------------------------------
s2_demo = F(3, 8)
c2_demo = 1 - s2_demo
check("cross-node demo: sin^2=3/8 -> cos^2 (=MW^2/MZ^2) = 5/8", c2_demo == F(5, 8))
check("cross-node demo: e^2/g^2 + MW^2/MZ^2 = 1 at sin^2=3/8", s2_demo + c2_demo == 1)

# ----------------------------------------------------------------------------
# Negative control: a SPURIOUS independent mass ratio (not = cos^2) breaks the
# composition -- confirms the relation is non-vacuous (the edge carries content).
# ----------------------------------------------------------------------------
g2, gp2 = F(4), F(3)
s2 = gp2 / (g2 + gp2)
e2 = g2 * s2
spurious = F(1, 2)  # an MW^2/MZ^2 NOT equal to cos^2 th_W
check("negative control: spurious MW^2/MZ^2 breaks the composition",
      e2 / g2 + spurious != 1)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
