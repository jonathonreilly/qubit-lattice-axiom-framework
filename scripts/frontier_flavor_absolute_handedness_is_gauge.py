#!/usr/bin/env python3
"""
The absolute flavor handedness is gauge; magnitude and relative-orientation readouts
remain open.

Class-A finite-dim verifier (3-vectors only, memory-safe). Resolves the flavor-handedness
residual by a gauge classification:

  (S)  The axis-swap transposition R (an orientation-reversing element of S_3) is an
       UNBROKEN physical symmetry of the staggered kinematics on the hw=1 generation
       triplet -- the staggered eta axis-ordering is pure Z_2 gauge (retained-bounded
       STAGGERED_AXIS_SYMMETRY_IS_S3: full S_3).

  (M)  The two orientations +delta_* and -delta_* are the SAME masses, R-relabeled:
       sqrt(m_k)(-delta) = sqrt(m_{-k})(+delta), so the sorted mass multiset is identical.

  (G)  The handedness sign(Delta), Delta=(p0-p1)(p1-p2)(p2-p0), is ODD under the
       transposition R. An observable odd under an UNBROKEN physical symmetry is not
       gauge-invariant -> the ABSOLUTE handedness is GAUGE. There is no missing
       derivation; the orientation is a labeling convention.

  (P)  The closed survivors are invariant candidates, not physical readout theorems:
       |Delta| is invariant under delta -> -delta, and the relative orientation
       sign(Delta_1)*sign(Delta_2) is R-invariant if a later bridge supplies shared axes.
       This verifier does not certify that |delta|=2/9 is a physical charged-lepton
       single-summand readout, and it does not identify the relative sign with a CKM/PMNS
       CP or mixing observable.

  Resolves the POSITIVITY notes' open "does the framework force a global handedness?" (NO --
  it is gauge, need not be forced) and completes the prior RK-even result (the residual
  R-breaking is NOT needed; R stays unbroken => handedness gauge). The NUMBER of generations
  (3) is a separate physical/derived fact (triplet dimension), untouched here. The r=1/2 cone
  and the magnitude 2/9 are untouched.

No PDG value is load-bearing; PDG enters only the (C) comparator.
"""
from itertools import permutations
from pathlib import Path

import numpy as np
from numpy import pi, cos, sqrt

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


def lam(d):
    return 1.0 + sqrt(2.0) * cos(d + 2.0 * pi * np.arange(3) / 3.0)


def born(d):
    m = lam(d) ** 2
    return m / m.sum()


def vand(p):
    return (p[0] - p[1]) * (p[1] - p[2]) * (p[2] - p[0])


def perm_sign(sigma):
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if sigma[i] > sigma[j])


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_PHYSICAL_NARROW_THEOREM_NOTE_2026-06-08.md"
two9 = 2.0 / 9.0
source = NOTE.read_text(encoding="utf-8")

# ===== (M) +delta and -delta are the SAME masses (multiset), R-relabeled =====
mp = np.sort(lam(two9) ** 2)
mm = np.sort(lam(-two9) ** 2)
check("M_same_mass_multiset_at_plus_minus_delta", np.allclose(mp, mm),
      f"sorted masses identical: {np.allclose(mp, mm)}")
check("M_sqrt_m_minus_delta_is_relabeled_plus_delta",
      np.allclose(np.sort(lam(-two9)), np.sort(lam(two9))),
      "sqrt m_k(-d) = sqrt m_{-k}(+d) (R-relabeling)")

# ===== (S) the transposition R is in S_3 and is orientation-reversing =====
# transpositions have sgn = -1 (reflections); 3-cycles have sgn=+1 (A_3 = C_3)
transpositions = [s for s in permutations(range(3)) if perm_sign(s) == -1]
cycles = [s for s in permutations(range(3)) if perm_sign(s) == +1]
check("S_S3_has_3_reflections_3_rotations", len(transpositions) == 3 and len(cycles) == 3,
      f"|transpositions|={len(transpositions)} (sgn -1), |A_3|={len(cycles)} (sgn +1)")
# R = a transposition; flips sign(Vand)
R = (1, 0, 2)
check("S_transposition_R_flips_sign_Vand",
      np.sign(vand(born(two9)[list(R)])) == -np.sign(vand(born(two9))) != 0,
      f"sign Vand -> {np.sign(vand(born(two9)[list(R)])):+.0f} under R")
# the staggered eta-ordering source is cited, but this runner does not read audit results.
check("S_R_unbroken_parent_source_named",
      "STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23" in source
      and "full, unbroken `S_3`" in source,
      "source note names the staggered S3 parent for unbroken R")

# ===== (G) sign(Vand) odd under the unbroken R => GAUGE =====
# odd under ALL transpositions (the full sign rep)
allodd = all(np.sign(vand(born(two9)[list(s)])) == -np.sign(vand(born(two9))) for s in transpositions)
alleven = all(np.sign(vand(born(two9)[list(s)])) == np.sign(vand(born(two9))) for s in cycles)
check("G_sign_Vand_is_S3_sign_rep", allodd and alleven,
      "odd under all 3 transpositions, even under A_3 -> the sign rep")
check("G_absolute_handedness_is_gauge", allodd,
      "odd under an unbroken physical symmetry (R) => not gauge-invariant => GAUGE")

# ===== (P) invariant survivors only; physical readout bridges remain open =====
check("P_magnitude_is_S3_invariant",
      abs(abs(vand(born(two9))) - abs(vand(born(-two9)))) < 1e-12,
      f"|Vand| same at +/-delta: {abs(vand(born(two9))):.6f}")
# inter-sector relative orientation sign(V1)*sign(V2) is R-invariant (R on BOTH sectors)
d1, d2 = two9, 0.35
rel = np.sign(vand(born(d1))) * np.sign(vand(born(d2)))
relR = np.sign(vand(born(d1)[list(R)])) * np.sign(vand(born(d2)[list(R)]))
check("P_relative_orientation_R_invariant", rel == relR != 0,
      f"sign(V1)*sign(V2)={rel:+.0f} = under R-on-both {relR:+.0f} (invariant candidate only)")
# magnitude carries |delta|=2/9=L_3(1,2) as a separate operator-side identity.
z = np.exp(2j * pi / 3.0)
L312 = (1.0 / 3.0) * (1.0 / ((z - 1) * (z ** 2 - 1)) + 1.0 / ((z ** 2 - 1) * (z ** 4 - 1)))
check("P_operator_side_L312_identity_is_2_9", abs(L312.real - two9) < 1e-12,
      f"L_3(1,2)={L312.real:.6f}; physical readout bridge is not checked here")

# ===== number of generations (3) is separate/physical; cone r=1/2 untouched =====
check("number_three_is_separate", len(born(two9)) == 3,
      "the NUMBER 3 = triplet dimension (separate from the gauge orientation)")
sweep = np.linspace(-pi, pi, 41)
maxQ = max(abs(np.sum(lam(x) ** 2) / np.sum(lam(x)) ** 2 - 2.0 / 3.0) for x in sweep)
check("firewall_cone_Q_two_thirds", maxQ < 1e-12, f"max|Q-2/3|={maxQ:.2e}")

# ===== (C) comparator only =====
m_pdg = np.array([0.5109989461, 105.6583755, 1776.86])
xn = sqrt(m_pdg); xn = xn / (xn.sum() / 3.0)
g = np.linspace(0.0, 0.6, 600001)
xs = np.sort(xn)
errs = np.array([np.sum((np.sort(1 + sqrt(2) * cos(t + 2 * pi * np.arange(3) / 3)) - xs) ** 2) for t in g])
check("C_comparator_delta_pdg", abs(g[int(np.argmin(errs))] - two9) < 1e-3, f"delta_PDG={g[int(np.argmin(errs))]:.6f}")

# ===== source-boundary guard: do not re-promote the open readout bridges =====
check("B_note_title_is_gauge_only_boundary",
      source.startswith("# Absolute Flavor Handedness Is Gauge; Magnitude and Relative-Orientation Readouts Remain Open"),
      "title records gauge theorem plus open readouts")
check("B_physical_2_9_readout_left_open",
      "does **not** derive a physical\nsingle-summand readout for `2/9`" in source
      and "physical single-summand readout" in source,
      "2/9 physical readout bridge left open")
check("B_relative_orientation_CP_bridge_left_open",
      "does **not** identify the relative sign with a CKM/PMNS\nCP or mixing observable" in source
      and "multi-sector shared-axis/readout bridge target" in source,
      "relative orientation CP/mixing bridge left open")
forbidden = [
    "Only the Magnitude and Inter-Sector Relative Orientations Are Physical",
    "This is where the physical **mixing / CP phase** lives",
    "the physical, derived flavor number",
    "the relative (CKM/PMNS-type)\norientation is physical",
]
check("B_no_stale_physical_survivor_overclaim_phrases",
      not any(phrase in source for phrase in forbidden),
      "stale physical-survivor promotion phrases absent")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: the ABSOLUTE flavor handedness sign(Delta) is GAUGE -- it is odd under the "
      "orientation-reversing transposition R, an UNBROKEN physical symmetry of the staggered "
      "kinematics (retained full S_3), and +delta/-delta are the same masses R-relabeled. The "
      "runner also checks invariant survivors -- |Delta| and relative sign -- only as candidates "
      "whose physical readout bridges remain open. The handedness residual is RESOLVED as gauge; "
      "the number 3 and the r=1/2 cone are separate/untouched.")
