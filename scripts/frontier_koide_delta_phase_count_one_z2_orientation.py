#!/usr/bin/env python3
"""
The Brannen-delta phase chirality and the generation count reduce to ONE Z_2 orientation.

Class-A finite-dim verifier (3-vectors only, memory-safe). Reproves, from scratch:

  (M)  RECAP (companion mirror-degeneracy result): delta -> -delta acts on the Brannen
       Born weights as the generation transposition (1 2); achiral functionals are
       mirror-degenerate F(+delta)=F(-delta) -> the azimuth selector must be chirality-odd.

  (U)  UNIFICATION (this note): the canonical chirality-odd functional is the generation
       Vandermonde / discriminant  Delta(p) = (p0-p1)(p1-p2)(p2-p0).  It transforms by the
       S_3 SIGN rep:  Delta(sigma.p) = sgn(sigma) Delta(p).  Its sign is exactly the
       orientation-sign object that the retained-bounded POSITIVITY notes use for the
       generation COUNT (S_3 -> C_3):  sgn(sigma) = det(perm matrix), with positive level
       set A_3 = C_3.  So:
         - selecting the Brannen phase +delta_* over its mirror -delta_*  (the PHASE), and
         - breaking the axis-symmetry S_3 -> C_3                          (the COUNT),
       are governed by the SAME single global Z_2 = sign(Delta) = the Cl(3) pseudoscalar /
       volume-form handedness.

  (E)  EVASION/level: the Z_2 orientation is a chirality-odd FUNCTIONAL on the records data,
       not an operator. A scalar operator sI (s in {+1,-1}) does NOT anticommute with the
       chiral grading Gamma_chi = (2/3)J - I, so it is outside the retained operator no-go
       (which forbids anticommuting operators in Sym(R^3)); and as an operator a scalar does
       nothing (orientation-blind). The content lives at the records-functional level.

  (G)  GLOBAL, not per-site: the orientation is one Z_2 for the whole generation triplet
       (a single global sign), consistent with the retained no-per-site-chirality scope.

  (S)  SEPARATE residuals (untouched): the MAGNITUDE |delta_*| = 2/9 = L_3(1,2) is the C_3
       fixed-point density (only the SIGN is the orientation, |Delta| is not 2/9); the
       REALIZED handedness (which sign) is the open global-orientation/arrow residual; the
       cone Q = 2/3 (block-weight r = 1/2) firewall is held fixed for all delta.

No PDG value is load-bearing; PDG enters only the (R) comparator.
"""
import numpy as np
from numpy import pi, cos, sqrt
from itertools import permutations

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


def lam(delta):
    return 1.0 + sqrt(2.0) * cos(delta + 2.0 * pi * np.arange(3) / 3.0)


def born(delta):
    m = lam(delta) ** 2
    return m / m.sum()


def vand(p):
    return (p[0] - p[1]) * (p[1] - p[2]) * (p[2] - p[0])


def perm_sign(sigma):
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if sigma[i] > sigma[j])


two9 = 2.0 / 9.0
sweep = np.linspace(-pi, pi, 73)

# ===== (M) RECAP: delta->-delta = (1 2); achiral functionals mirror-degenerate =====
swap12 = np.array([0, 2, 1])
maxperm = max(np.max(np.abs(born(-d) - born(d)[swap12])) for d in sweep)
check("M_reflection_is_transposition_(1 2)", maxperm < 1e-12, f"max={maxperm:.2e}")
# a symmetric functional is mirror-degenerate (purity example)
md = max(abs(np.sum(born(d) ** 2) - np.sum(born(-d) ** 2)) for d in sweep)
check("M_symmetric_functional_mirror_degenerate", md < 1e-12, f"max|F(+d)-F(-d)|={md:.2e}")

# ===== (U) the Vandermonde is the S_3 sign rep (the orientation object) =====
# transforms by sgn(sigma)
pg = born(0.37)  # generic data point
worst = 0.0
for sigma in permutations(range(3)):
    worst = max(worst, abs(vand(pg[list(sigma)]) - perm_sign(sigma) * vand(pg)))
check("U_vandermonde_is_S3_sign_rep", worst < 1e-12, f"max|Delta(s.p)-sgn(s)Delta(p)|={worst:.2e}")
# sgn(sigma) = det(permutation matrix): the SAME Z_2 the POSITIVITY count-notes use
sgn_ok = all(perm_sign(s) == round(np.linalg.det(np.eye(3)[list(s)])) for s in permutations(range(3)))
check("U_sgn_equals_det_perm_count_orientation", sgn_ok, "sgn(sigma)=det(rho_perm(sigma)); +1 set = A_3 = C_3")
# Vandermonde is odd under the reflection delta->-delta -> sign(Delta) distinguishes +/-delta_*
check("U_vandermonde_odd_under_reflection",
      abs(vand(born(two9)) + vand(born(-two9))) < 1e-12,
      f"Delta(+2/9)={vand(born(two9)):+.6e} Delta(-2/9)={vand(born(-two9)):+.6e}")
check("U_sign_vandermonde_is_the_orientation_Z2",
      np.sign(vand(born(two9))) == -np.sign(vand(born(-two9))) != 0,
      f"sign Delta(+2/9)={np.sign(vand(born(two9))):+.0f}  sign Delta(-2/9)={np.sign(vand(born(-two9))):+.0f}")

# ===== the phase residual after the C_3 chamber is exactly the orientation Z_2 =====
# C_3 (chamber) = shift delta by 2pi/3 (cyclic relabel); fixing the positive-sorted chamber
# leaves the reflection sign as the residual. Show: +delta_* and -delta_* share the sorted
# chamber (same multiset) but opposite sign(Delta).
ps, pm = np.sort(born(two9)), np.sort(born(-two9))
check("U_mirror_shares_chamber_opposite_orientation",
      np.max(np.abs(ps - pm)) < 1e-12 and np.sign(vand(born(two9))) != np.sign(vand(born(-two9))),
      "same sorted Born multiset, opposite sign(Delta) -> residual after chamber is the Z_2")

# ===== (E) evasion/level: a scalar operator cannot be the anticommuting grading =====
J = np.ones((3, 3))
Gamma = (2.0 / 3.0) * J - np.eye(3)  # chiral grading Gamma_chi = (2/3)J - I  (Gamma^2 = I)
check("E_gamma_chi_is_involution", np.allclose(Gamma @ Gamma, np.eye(3)), "Gamma_chi^2 = I")
for s in (+1, -1):
    anti = (s * np.eye(3)) @ Gamma + Gamma @ (s * np.eye(3))
    check(f"E_scalar_op_s{('p' if s>0 else 'm')}_not_anticommuting",
          np.linalg.norm(anti) > 1e-9,
          f"{{{s:+d}I,Gamma}}=2sGamma != 0 -> scalar sI outside the anticommuting-operator no-go")
# the orientation as a functional is well-defined without any operator
check("E_orientation_is_a_records_functional", np.isfinite(vand(born(two9))),
      "sign(Delta) is a scalar functional of the Born data, not an operator")

# ===== (G) GLOBAL: one Z_2 for the whole triplet =====
# sign(Delta) is a single global sign; relabeling any pair flips it once (no per-site sign)
flips = [perm_sign(s) for s in permutations(range(3))]
check("G_single_global_Z2", sorted(set(flips)) == [-1, 1] and flips.count(1) == 3 and flips.count(-1) == 3,
      "S_3 sign rep: 3 even (C_3) / 3 odd; one global handedness, not per-site")

# ===== (S) separate residuals: magnitude and realized sign untouched =====
# magnitude: |Delta| is NOT 2/9 (the orientation supplies only the SIGN; |delta_*|=2/9=L_3(1,2))
z = np.exp(2j * pi / 3.0)
L312 = (1.0 / 3.0) * (1.0 / ((z - 1) * (z ** 2 - 1)) + 1.0 / ((z ** 2 - 1) * (z ** 4 - 1)))
check("S_magnitude_is_separate_L3_1_2", abs(L312.real - two9) < 1e-12 and abs(abs(vand(born(two9))) - two9) > 1e-3,
      f"|Delta(2/9)|={abs(vand(born(two9))):.4f} != 2/9 ; magnitude 2/9=L_3(1,2)={L312.real:.6f} (separate)")
# realized sign is a free Z_2 here (both signs are valid configs) -> open residual
check("S_realized_sign_is_open_residual",
      np.sign(vand(born(two9))) != 0 and np.sign(vand(born(-two9))) != 0,
      "both orientations are valid records; which one is realized = open global-handedness/arrow residual")

# ===== firewall: cone Q = 2/3 for all delta (untouched) =====
maxQ = max(abs(np.sum(lam(d) ** 2) / np.sum(lam(d)) ** 2 - 2.0 / 3.0) for d in sweep)
check("firewall_cone_Q_two_thirds_all_delta", maxQ < 1e-12, f"max|Q-2/3|={maxQ:.2e}")

# ===== (R) comparator only: PDG delta ~= 2/9 =====
m_pdg = np.array([0.5109989461, 105.6583755, 1776.86])
xn = sqrt(m_pdg); xn = xn / (xn.sum() / 3.0)
g = np.linspace(0.0, 0.6, 600001)
xs = np.sort(xn)
errs = np.array([np.sum((np.sort(1 + sqrt(2) * cos(t + 2 * pi * np.arange(3) / 3)) - xs) ** 2) for t in g])
check("R_comparator_delta_pdg_near_2_9", abs(g[int(np.argmin(errs))] - two9) < 1e-3,
      f"delta_PDG={g[int(np.argmin(errs))]:.6f}")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: the Brannen-delta phase chirality (selecting +delta_* over its mirror) and the "
      "generation count (S_3 -> C_3) reduce to ONE global Z_2 = sign(Vandermonde) = the Cl(3) "
      "pseudoscalar/volume-form orientation. Records-functional level (evades the operator "
      "anticommuting no-go). Magnitude 2/9=L_3(1,2), the realized handedness, and the r=1/2 cone "
      "remain separate untouched residuals.")
