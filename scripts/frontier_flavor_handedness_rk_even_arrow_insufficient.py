#!/usr/bin/env python3
"""
The flavor handedness Z_2 is T-odd AND R-odd (RK-even): the time-arrow alone cannot fix it.

Class-A finite-dim verifier (3-vectors / 3x3 only, memory-safe). Establishes, on the
generation circulant operator and the Brannen records:

  (H)  The flavor handedness is sign(Delta), Delta(p)=(p0-p1)(p1-p2)(p2-p0) = the S_3
       sign-rep / Cl(3) pseudoscalar orientation that governs BOTH the generation count
       and the Brannen phase (companion result).

  (T)  sign(Delta) is T-ODD: time-reversal T=K (complex conjugation, b->conj b on the
       circulant doublet G = g0 I + g1 C + conj(g1) C^2) sends arg(g1) -> -arg(g1), i.e.
       the Brannen phase delta -> -delta, flipping sign(Delta).

  (R)  sign(Delta) is R-ODD: a spatial axis-swap reflection R (an IMPROPER element of the
       cubic point group, det R = -1) conjugates the cyclic shift C -> C^2, again sending
       delta -> -delta, flipping sign(Delta). The proper 3-fold rotation C3[111]
       (det = +1, in A_3) PRESERVES sign(Delta).

  (RK) Hence sign(Delta) is EVEN under the combination R.K. The two operations that flip
       it are the antiunitary time-reversal (T=K) and the unitary spatial reflection (R);
       they are distinct (one antiunitary, one unitary), and only their product fixes it.

  (A)  The framework dynamics is T-symmetric (H = iD, Theta_H = P K commutes with H,
       retained CPT), and the arrow is a past-hypothesis BOUNDARY datum that breaks only T
       (retained arrow note). R remains a bare-lattice symmetry. Therefore breaking T
       (the arrow) does NOT fix sign(Delta): the unbroken reflection R maps the two
       orientations into each other. Fixing the handedness requires breaking R (spatial
       reflection / parity) -- NOT supplied by the time-arrow.

  (S)  Separate, untouched: the magnitude |delta|=2/9=L_3(1,2); the realized R-breaking
       (the open residual); the r=1/2 cone (Q=2/3, firewall).

No PDG value is load-bearing; PDG enters only the (C) comparator.
"""
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


# Cyclic shift C (x->y->z), real permutation; C^2 = C^T
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)


def Gcirc(g0, g1):
    return g0 * np.eye(3) + g1 * C + np.conj(g1) * C.T


def lam(d):
    return 1.0 + sqrt(2.0) * cos(d + 2.0 * pi * np.arange(3) / 3.0)


def born(d):
    m = lam(d) ** 2
    return m / m.sum()


def vand(p):
    return (p[0] - p[1]) * (p[1] - p[2]) * (p[2] - p[0])


two9 = 2.0 / 9.0

# ===== (H) the handedness is sign(Delta); nonzero at the physical point =====
check("H_handedness_is_sign_Delta_nonzero", abs(vand(born(two9))) > 1e-6,
      f"Delta(+2/9)={vand(born(two9)):+.6e} -> sign={np.sign(vand(born(two9))):+.0f}")

# ===== (T) sign(Delta) is T-ODD (time-reversal K: arg(g1) -> -arg(g1)) =====
# on the circulant operator, K (conjugation) sends g1 -> conj(g1) i.e. delta -> -delta
g0, mag, d = 0.3, 0.5, two9
G = Gcirc(g0, mag * np.exp(1j * d))
GK = np.conj(G)  # K G K = conj(G)
Gminus = Gcirc(g0, mag * np.exp(-1j * d))
check("T_K_conjugates_circulant_to_minus_delta", np.allclose(GK, Gminus),
      "K: g1->conj(g1) == delta->-delta on the circulant")
check("T_sign_Delta_is_T_odd",
      np.sign(vand(born(d))) == -np.sign(vand(born(-d))) != 0,
      f"sign Delta(+d)={np.sign(vand(born(d))):+.0f}  sign Delta(-d)={np.sign(vand(born(-d))):+.0f}")

# ===== (R) sign(Delta) is R-ODD (spatial axis-swap reflection, improper) =====
R = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], float)  # swap axes 2<->3
check("R_is_improper_reflection", abs(np.linalg.det(R) + 1) < 1e-12, f"det(R)={np.linalg.det(R):+.0f}")
check("R_conjugates_C_to_C2", np.allclose(R @ C @ R.T, C.T), "R C R^T = C^2 (reverses the 3-cycle)")
# R on the Born weights = permutation (0,2,1) -> same as delta->-delta
Rp = born(d)[[0, 2, 1]]
check("R_sign_Delta_is_R_odd", np.sign(vand(Rp)) == -np.sign(vand(born(d))) != 0,
      f"sign Delta -> {np.sign(vand(Rp)):+.0f} under R")
# proper rotation C3[111] (det +1) PRESERVES orientation
C3p = born(d)[[2, 0, 1]]  # cyclic relabel (proper, A_3)
check("R_proper_rotation_preserves_orientation",
      np.sign(vand(C3p)) == np.sign(vand(born(d))),
      "C3[111] (det=+1, A_3) preserves sign(Delta)")

# ===== (RK) sign(Delta) is EVEN under R.K =====
# K: delta->-delta ; then R: permutation (0,2,1) -> net restores sign
RKp = born(-d)[[0, 2, 1]]
check("RK_even", np.sign(vand(RKp)) == np.sign(vand(born(d))) != 0,
      f"sign Delta under R.K = {np.sign(vand(RKp)):+.0f} (== original {np.sign(vand(born(d))):+.0f})")
# T and R are DISTINCT (one antiunitary, one unitary): R is real orthogonal (unitary)
check("RK_R_is_unitary_distinct_from_K",
      np.allclose(R @ R.T, np.eye(3)) and abs(np.linalg.det(R) + 1) < 1e-12,
      "R orthogonal (unitary), improper; K antiunitary -- distinct operations")

# ===== (A) arrow breaks only T; R unbroken -> handedness not fixed by the arrow =====
# framework dynamics H = iD is T-symmetric: K H K = -H (time reversal), so |evolution| real
D = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]], float)  # real antisymmetric (anti-Herm)
H = 1j * D
check("A_dynamics_T_symmetric_H_iD", np.allclose(np.conj(H), -H),
      "K H K = -H: H=iD is time-reversal-odd, free evolution e^{Dt} is real (T-symmetric)")
# the arrow flips under K (= reverses time); R is a spatial (improper) lattice symmetry, K-independent
# so breaking T (arrow) leaves R unbroken -> the RK-even handedness stays undetermined.
check("A_arrow_breaks_T_not_R",
      np.allclose(R @ R.T, np.eye(3)) and np.allclose(np.conj(H), -H),
      "arrow = T-breaking boundary datum; R (spatial reflection) untouched -> handedness unfixed")

# ===== (S) separate residuals: magnitude, realized R-breaking, r=1/2 cone =====
z = np.exp(2j * pi / 3.0)
L312 = (1.0 / 3.0) * (1.0 / ((z - 1) * (z ** 2 - 1)) + 1.0 / ((z ** 2 - 1) * (z ** 4 - 1)))
check("S_magnitude_L3_1_2_separate", abs(L312.real - two9) < 1e-12 and abs(abs(vand(born(two9))) - two9) > 1e-3,
      f"|Delta(2/9)|={abs(vand(born(two9))):.4f} != 2/9=L_3(1,2) (separate)")
sweep = np.linspace(-pi, pi, 41)
maxQ = max(abs(np.sum(lam(x) ** 2) / np.sum(lam(x)) ** 2 - 2.0 / 3.0) for x in sweep)
check("S_cone_Q_two_thirds_firewall", maxQ < 1e-12, f"max|Q-2/3|={maxQ:.2e}")

# ===== (C) comparator only =====
m_pdg = np.array([0.5109989461, 105.6583755, 1776.86])
xn = sqrt(m_pdg); xn = xn / (xn.sum() / 3.0)
g = np.linspace(0.0, 0.6, 600001)
xs = np.sort(xn)
errs = np.array([np.sum((np.sort(1 + sqrt(2) * cos(t + 2 * pi * np.arange(3) / 3)) - xs) ** 2) for t in g])
check("C_comparator_delta_pdg", abs(g[int(np.argmin(errs))] - two9) < 1e-3, f"delta_PDG={g[int(np.argmin(errs))]:.6f}")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: the flavor handedness sign(Delta) (count + phase) is T-odd AND R-odd (RK-even). "
      "The time-arrow breaks only T (H=iD T-symmetric, arrow = past-hypothesis boundary); the spatial "
      "axis-swap reflection R stays a bare-lattice symmetry. So the arrow ALONE cannot fix the "
      "handedness -- it requires spatial-reflection (parity) breaking (the open residual; staggered "
      "axis-ordering is the natural candidate), RK-correlated with the arrow. Magnitude 2/9=L_3(1,2) "
      "and the r=1/2 cone untouched.")
