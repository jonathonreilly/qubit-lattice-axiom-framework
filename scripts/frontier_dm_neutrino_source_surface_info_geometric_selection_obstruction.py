#!/usr/bin/env python3
"""Conditional scalar-baseline information geometry: local expansion and domain.

Only the four displayed functionals are compared. The baseline m I, m > 0,
is supplied; this runner does not derive it for the live affine sheet.
The Gaussian comparison requires H=m I+J positive definite. At m=1 the
entire specified chamber boundary is outside that domain, so the former
full-KL boundary-minimizer comparison and universal no-go are withdrawn.
"""

from __future__ import annotations

import math

import numpy as np

from frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary import (
  tdelta,
  tq,
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
  global PASS_COUNT, FAIL_COUNT
  status = "PASS" if condition else "FAIL"
  if condition:
    PASS_COUNT += 1
  else:
    FAIL_COUNT += 1
  msg = f" [{status} ({cls})] {name}"
  if detail:
    msg += f" ({detail})"
  print(msg)
  return condition


# ---------------------------------------------------------------------------
# Atlas-native constants
# ---------------------------------------------------------------------------

E1_EXACT = math.sqrt(8.0 / 3.0)      # chamber intercept
SQRT6_3 = math.sqrt(6.0) / 3.0      # Frobenius-isotropic chamber-boundary
                     # minimizer delta_* = q_+*

# Chamber: q_+ >= sqrt(8/3) - delta  (closed half-plane)


def boundary_q(delta: float) -> float:
  return E1_EXACT - delta


def gaussian_kl2(d: float, q: float, m: float = 1.0) -> float:
  """Twice real-Gaussian KL for covariances H^-1 and (m I)^-1.

  Uses eigenvalue ratios to evaluate tr(m H^-1)-3+log(det H/m^3).
  This is not the Grassmann log-absolute-determinant outside the SPD cone.
  """
  if not math.isfinite(m) or m <= 0.0:
    raise ValueError("Gaussian baseline m must be positive and finite")
  H = m * np.eye(3) + d * tdelta() + q * tq()
  ratios = np.linalg.eigvalsh(H) / m
  if not np.all(np.isfinite(ratios)) or np.any(ratios <= 0.0):
    raise ValueError("Gaussian covariance requires positive-definite H")
  x = ratios - 1.0
  return float(np.sum(-x / (1.0 + x) + np.log1p(x)))


# ---------------------------------------------------------------------------
# PART A: Quadratic Unanimity Theorem
# ---------------------------------------------------------------------------

def part_a_quadratic_unanimity() -> None:
  """
  PART A: Quadratic-order unanimity of info-geometric functionals.

  We verify that the following four functionals all have the SAME
  leading-order isotropic quadratic form (up to positive multiplicative
  constants that preserve argmin on the chamber):

  (1) F1(d, q) = -W[m I; J_act(d, q)] truncated at quadratic order
  (2) F2(d, q) = 2 KL[N_J || N_0] truncated at quadratic order
  (3) F3(d, q) = -Hess(W)|_0[J_act,J_act], twice Gaussian Fisher
  (4) F4(d, q) = Tr(J_act^2) / m^2  (Frobenius squared distance)

  All four quadratic parts have form c * (delta^2 + q_+^2) / m^2, c > 0,
  therefore they share the same chamber-boundary argmin.
  """
  print("\n" + "=" * 88)
  print("PART A: QUADRATIC-ORDER UNANIMITY OF INFO-GEOMETRIC FUNCTIONALS")
  print("=" * 88)

  Td = tdelta()
  Tq = tq()
  m = 1.0 # Gaussian baseline requires positive m

  # Verify Frobenius isotropy on the 2-plane {T_delta, T_q}:
  tr_dd = float(np.real(np.trace(Td @ Td)))
  tr_qq = float(np.real(np.trace(Tq @ Tq)))
  tr_dq = float(np.real(np.trace(Td @ Tq)))

  check(
    "Tr(T_delta^2) = Tr(T_q^2) = 6 (Frobenius isotropy at quadratic order)",
    abs(tr_dd - 6.0) < 1e-12 and abs(tr_qq - 6.0) < 1e-12,
    f"Tr(T_d^2) = {tr_dd}, Tr(T_q^2) = {tr_qq}",
  )

  check(
    "Tr(T_delta T_q) = 0 (no off-diagonal Frobenius coupling)",
    abs(tr_dq) < 1e-12,
    f"Tr(T_d T_q) = {tr_dq}",
  )

  # (1) -W quadratic Hessian at J=0 (axiom-native generator)
  # From the Schur-baseline closure: -W[J_act] = 3 |w|^2 / m^2 + O(|w|^3)
  #                      = 3 (delta^2 + q_+^2) / m^2 at O(2)
  # where w = q_+ + i delta.
  h = 1e-5

  def W_det(d: float, q: float) -> float:
    H = m * np.eye(3, dtype=complex) + d * Td + q * Tq
    return math.log(abs(np.real(np.linalg.det(H)))) - math.log(abs(m ** 3))

  dd_W = (W_det(h, 0.0) - 2.0 * W_det(0.0, 0.0) + W_det(-h, 0.0)) / h ** 2
  qq_W = (W_det(0.0, h) - 2.0 * W_det(0.0, 0.0) + W_det(0.0, -h)) / h ** 2
  dq_W = (W_det(h, h) - W_det(h, -h) - W_det(-h, h) + W_det(-h, -h)) / (4.0 * h ** 2)

  # Hessian of -W is the positive quadratic form. -d^2 W / d d^2 = 6/m^2 etc.
  F1_dd = -dd_W
  F1_qq = -qq_W
  F1_dq = -dq_W

  ok_F1 = (
    abs(F1_dd - 6.0 / m ** 2) < 1e-3
    and abs(F1_qq - 6.0 / m ** 2) < 1e-3
    and abs(F1_dq) < 1e-3
  )
  check(
    "F1 = -W quadratic Hessian is 6/m^2 * I_2 (isotropic)",
    ok_F1,
    f"dd={F1_dd:.4f}, qq={F1_qq:.4f}, cross={F1_dq:.2e}",
  )

  # (2) 2 KL[N_J || N_0] quadratic form via direct numerical Hessian
  # For Sigma_0 = (m I)^{-1}, Sigma_J = (m I + J)^{-1}:
  #  2 KL = tr(Sigma_0^{-1} Sigma_J) - 3 - log det(Sigma_0^{-1} Sigma_J)
  def KL2_sym(d: float, q: float) -> float:
    return gaussian_kl2(d, q, m)

  dd_KL = (KL2_sym(h, 0.0) - 2.0 * KL2_sym(0.0, 0.0) + KL2_sym(-h, 0.0)) / h ** 2
  qq_KL = (KL2_sym(0.0, h) - 2.0 * KL2_sym(0.0, 0.0) + KL2_sym(0.0, -h)) / h ** 2
  dq_KL = (KL2_sym(h, h) - KL2_sym(h, -h) - KL2_sym(-h, h) + KL2_sym(-h, -h)) / (4.0 * h ** 2)

  # The coefficient matters: the old minus-log bug also looked isotropic.
  # Correct F2=3(d^2+q^2)/m^2+O(3), Hessian=6 I/m^2.
  ok_F2_iso = (
    abs(dd_KL - 6.0 / m**2) < 1e-3
    and abs(qq_KL - 6.0 / m**2) < 1e-3
    and abs(dq_KL) < 1e-3
  )
  check(
    "F2 = 2 KL quadratic Hessian is 6 I/m^2 (rejects old 18 I/m^2)",
    ok_F2_iso,
    f"dd={dd_KL:.4f}, qq={qq_KL:.4f}, cross={dq_KL:.2e}",
  )

  # (3) Curvature convention g_F = -Hess(W); already computed above,
  # twice the real-Gaussian Fisher quadratic in this convention.
  check(
    "F3 = -Hess(W) curvature quadratic (twice real-Gaussian Fisher)",
    ok_F1,
    "g_F(J_act, J_act) = 6 (delta^2 + q_+^2) / m^2",
  )

  # (4) Frobenius squared distance Tr(J^2)/m^2 on the 2-plane:
  def F4(d: float, q: float) -> float:
    J = d * Td + q * Tq
    return float(np.real(np.trace(J @ J))) / m ** 2

  # Symbolic coefficient: 6(d^2 + q^2)/m^2 by the Frobenius isotropy
  ok_F4 = abs(F4(1.0, 0.0) - 6.0 / m ** 2) < 1e-9 and abs(F4(0.0, 1.0) - 6.0 / m ** 2) < 1e-9
  check(
    "F4 = Tr(J^2)/m^2 is 6(delta^2 + q_+^2)/m^2 (isotropic)",
    ok_F4,
    f"F4(1,0) = {F4(1.0, 0.0)}, F4(0,1) = {F4(0.0, 1.0)}",
  )

  # Their quadratic parts have the form c_i * (delta^2 + q_+^2), c_i > 0,
  # so they share the same chamber-boundary argmin.
  # Minimize delta^2 + (E1 - delta)^2 over delta in R:
  #  d/ddelta [ d^2 + (E1-d)^2 ] = 2d - 2(E1-d) = 0 => d = E1/2 = sqrt(6)/3
  d_star = E1_EXACT / 2.0
  q_star = E1_EXACT - d_star
  check(
    "Common chamber-boundary minimizer: (delta_*, q_+*) = (sqrt(6)/3, sqrt(6)/3)",
    abs(d_star - SQRT6_3) < 1e-12 and abs(q_star - SQRT6_3) < 1e-12,
    f"d_* = {d_star:.10f}, sqrt(6)/3 = {SQRT6_3:.10f}",
  )

  # Verify this IS the foot-of-perpendicular from origin to boundary line
  # (any isotropic quadratic has this minimum on a line constraint).
  check(
    "The common minimum is the foot of perpendicular from origin to chamber boundary",
    abs(d_star - q_star) < 1e-12,
    "isotropic quadratic + linear boundary => perpendicular-foot argmin",
  )


# ---------------------------------------------------------------------------
# PART B: Local Cubic Coefficients
# ---------------------------------------------------------------------------

def part_b_cubic_splitting() -> None:
  """Check cubic trace coefficients, without inferring global minimizers."""
  print("\n" + "=" * 88)
  print("PART B: LOCAL CUBIC COEFFICIENTS")
  print("=" * 88)

  Td = tdelta()
  Tq = tq()

  tr_ddd = float(np.real(np.trace(Td @ Td @ Td)))
  tr_qqq = float(np.real(np.trace(Tq @ Tq @ Tq)))
  tr_ddq = float(np.real(np.trace(Td @ Td @ Tq)))
  tr_dqq = float(np.real(np.trace(Td @ Tq @ Tq)))

  check(
    "Tr(T_delta^3) = 0 (cubic vanishes on delta-axis)",
    abs(tr_ddd) < 1e-10,
    f"Tr(T_d^3) = {tr_ddd}",
  )
  check(
    "Tr(T_q^3) = 6 (cubic is nonzero on q-axis — breaks Frobenius isotropy)",
    abs(tr_qqq - 6.0) < 1e-10,
    f"Tr(T_q^3) = {tr_qqq}",
  )
  check(
    "Tr(T_delta^2 T_q) = -6 (asymmetric cross-cubic)",
    abs(tr_ddq + 6.0) < 1e-10,
    f"Tr(T_d^2 T_q) = {tr_ddq}",
  )
  check(
    "Tr(T_delta T_q^2) = 0 (asymmetric cross-cubic)",
    abs(tr_dqq) < 1e-10,
    f"Tr(T_d T_q^2) = {tr_dqq}",
  )

  # Verify identification with Z_3 norm form cubic 2 Re(w^3) = 2 q_+ (q_+^2 - 3 delta^2):
  # For J = d T_d + q T_q:
  #  tr(J^3) = d^3 tr(T_d^3) + 3 d^2 q tr(T_d^2 T_q) + 3 d q^2 tr(T_d T_q^2) + q^3 tr(T_q^3)
  #     = 0 - 18 d^2 q + 0 + 6 q^3
  #     = 6 q (q^2 - 3 d^2) == 3 * 2 Re(w^3) with w = q + i d
  # Check:
  for d_val, q_val in [(0.3, 0.7), (-0.2, 0.4), (SQRT6_3, SQRT6_3)]:
    J_val = d_val * Td + q_val * Tq
    tr_J3 = float(np.real(np.trace(J_val @ J_val @ J_val)))
    pred = 6.0 * q_val * (q_val ** 2 - 3.0 * d_val ** 2)
    ok = abs(tr_J3 - pred) < 1e-10
    check(
      f"tr(J^3) = 6 q (q^2 - 3 d^2) identity, (d,q)=({d_val:.3f},{q_val:.3f})",
      ok,
      f"tr={tr_J3:.6f}, pred={pred:.6f}",
    )

  # SPD H with trace 3m has tr(H^2)<9m^2, hence tr(J^2)<6m^2.
  # On d+q=E1, tr(J^2)=6(d^2+q^2)>=3 E1^2=8.
  check("m=1 chamber boundary violates necessary SPD trace bound",
        3.0 * E1_EXACT**2 > 6.0,
        "tr(J^2)>=8, but positive H=I+J requires tr(J^2)<6")
  try:
    gaussian_kl2(SQRT6_3, SQRT6_3)
  except ValueError:
    rejected = True
  else:
    rejected = False
  check("Gaussian KL rejects the inadmissible boundary foot", rejected)
  print("No Gaussian full-boundary minimizer comparison is made.")


def main() -> int:
  part_a_quadratic_unanimity()
  part_b_cubic_splitting()
  print("Local Taylor coefficients differ at cubic order; this does not prove")
  print("different global minima or impossibility of a source selector.")
  print("The physical selection principle remains an open obligation.")
  print(f"TOTAL: PASS = {PASS_COUNT}, FAIL = {FAIL_COUNT}")
  return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
  raise SystemExit(main())
