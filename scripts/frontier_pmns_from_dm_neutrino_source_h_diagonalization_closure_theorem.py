#!/usr/bin/env python3
"""Conditional PMNS map and finite fit on a supplied affine Hermitian chart.

H(m, delta, q_+) = H_base + m T_m + delta T_delta + q_+ T_q,
with supplied constants gamma=1/2, E1=sqrt(8/3), E2=sqrt(8)/3 and
chamber q_+ + delta >= E1. The matrices below define this calculation;
their physical selection is not derived by this runner.

The charged-lepton axis basis U_e=I and row permutation (2,1,0) are
separate supplied choices. Eigenvector columns are sorted by ascending
H eigenvalue; permuting flavor rows is distinct from sorting those columns.
At nondegenerate spectra and nonzero angle denominators the resulting
unitary defines rephasing-invariant angles and a phase using atan2.
Singular phase denominators return NaN; no globally smooth eigenbasis map
across spectral degeneracies is asserted.

Sixty seeded finite starts and local refinement fit the historical targets
(s12^2,s13^2,s23^2)=(0.307,0.0218,0.545). The search reports its actual
accepted starts and distinct rounded candidates. It is not an exhaustive
uniqueness proof or proof of Jacobian nonsingularity. A scipy-free fallback
uses one local initial point and supplies no multistart evidence.

At the located fit (0.657061,0.933806,0.715042), the conditional phase is
260.88 degrees and |J| approximately 0.0328. Neither is a current
experimental conclusion. Nine modulus comparisons use supplied historical
NuFit 5.3 intervals; the J band and phase sign are numerical checks only.
Five supplied comparison points and sampled Fourier slots are finite
controls, not certification of the selector derivations behind their names.
No physical branch, basis, hierarchy pairing or retained status is derived.
"""

from __future__ import annotations

import itertools
import math

AUDIT_TIMEOUT_SEC = 30

import numpy as np

np.set_printoptions(precision=8, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "D") -> bool:
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
# Supplied chart constants
# ---------------------------------------------------------------------------

GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
OMEGA = np.exp(2j * math.pi / 3.0)

UZ3 = (1.0 / math.sqrt(3.0)) * np.array(
  [
    [1.0, 1.0, 1.0],
    [1.0, OMEGA, OMEGA * OMEGA],
    [1.0, OMEGA * OMEGA, OMEGA],
  ],
  dtype=complex,
)

T_M = np.array(
  [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex
)
T_DELTA = np.array(
  [[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex
)
T_Q = np.array(
  [[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex
)
H_BASE = np.array(
  [
    [0.0, E1, -E1 - 1j * GAMMA],
    [E1, 0.0, -E2],
    [-E1 + 1j * GAMMA, -E2, 0.0],
  ],
  dtype=complex,
)


def H(m: float, delta: float, q_plus: float) -> np.ndarray:
  return H_BASE + m * T_M + delta * T_DELTA + q_plus * T_Q


# ---------------------------------------------------------------------------
# Conditional PMNS map: eigenbasis columns and separately supplied flavor rows
# ---------------------------------------------------------------------------

PMNS_PERMUTATION = (2, 1, 0) # supplied flavor row ordering; not an eigenvalue-column permutation


def pmns_matrix(m: float, delta: float, q_plus: float) -> tuple[np.ndarray, np.ndarray]:
  """Return (eigenvalues_ascending, PMNS) for H(m, delta, q_+)."""
  Hm = H(m, delta, q_plus)
  w, V = np.linalg.eigh(Hm)
  order = np.argsort(np.real(w))
  w = np.real(w[order])
  V = V[:, order]
  PMNS = V[list(PMNS_PERMUTATION), :]
  return w, PMNS


def pmns_observables(m: float, delta: float, q_plus: float) -> dict:
  w, P = pmns_matrix(m, delta, q_plus)
  return observables_from_pmns(P, w)


def observables_from_pmns(P: np.ndarray, w: np.ndarray | None = None) -> dict:
  """Extract PDG invariants from a supplied unitary with the chosen ordering."""
  s13sq = abs(P[0, 2]) ** 2
  c13sq = max(1.0 - s13sq, 1e-18)
  s12sq = abs(P[0, 1]) ** 2 / c13sq
  s23sq = abs(P[1, 2]) ** 2 / c13sq
  s12 = math.sqrt(max(s12sq, 0.0))
  c12 = math.sqrt(max(1.0 - s12sq, 0.0))
  s13 = math.sqrt(max(s13sq, 0.0))
  c13 = math.sqrt(max(c13sq, 0.0))
  s23 = math.sqrt(max(s23sq, 0.0))
  c23 = math.sqrt(max(1.0 - s23sq, 0.0))
  # Jarlskog invariant
  J = (P[0, 0] * P[0, 1].conjugate() * P[1, 0].conjugate() * P[1, 1]).imag
  denom = s12 * c12 * s23 * c23 * s13 * c13 * c13
  sin_dcp = J / denom if denom > 1e-18 else 0.0
  sin_dcp = max(-1.0, min(1.0, sin_dcp))
  # PDG modulus identity fixes the quadrant that asin(J/denom) loses.
  cos_denom = 2.0 * s12 * c12 * s23 * c23 * s13
  if cos_denom > 1e-18 and denom > 1e-18:
    cos_dcp = (abs(P[1, 0]) ** 2 - s12sq * c23**2
               - c12**2 * s23sq * s13sq) / cos_denom
    cos_dcp = max(-1.0, min(1.0, cos_dcp))
    dcp_deg = math.degrees(math.atan2(sin_dcp, cos_dcp)) % 360.0
  else:
    # The Dirac phase is unidentifiable at a vanishing mixing denominator.
    cos_dcp = dcp_deg = float("nan")
  return {
    "eigvals": w,
    "PMNS": P,
    "abs_PMNS": np.abs(P),
    "s12sq": s12sq,
    "s13sq": s13sq,
    "s23sq": s23sq,
    "sin2_2t12": 4.0 * s12sq * (1.0 - s12sq),
    "sin2_2t13": 4.0 * s13sq * (1.0 - s13sq),
    "sin2_2t23": 4.0 * s23sq * (1.0 - s23sq),
    "J": J,
    "sin_dcp": sin_dcp,
    "cos_dcp": cos_dcp,
    "dcp_deg": dcp_deg,
  }


# ---------------------------------------------------------------------------
# Part 1: supplied-chart structural checks on H and K_Z3
# ---------------------------------------------------------------------------


def part1_structural_checks() -> None:
  print()
  print("=" * 88)
  print("Part 1: supplied-chart structural checks on H(m, delta, q_+) and K_Z3")
  print("=" * 88)

  # Five supplied comparison points from the historical survey
  candidates = [
    ("A Schur-Q", 0.5, math.sqrt(6) / 3.0, math.sqrt(6) / 3.0),
    ("B det-crit", 0.613, 0.964, 1.552),
    ("C Tr(H^2)-bdy", 0.385, 1.268, 0.365),
    ("D K12 char", 0.0, 0.800, 1.000),
    (
      "E par-mix F1",
      4 * math.sqrt(2) / 9,
      math.sqrt(6) / 2 - math.sqrt(2) / 18,
      math.sqrt(6) / 6 + math.sqrt(2) / 18,
    ),
  ]

  a_star_ref = None
  b_star_ref = None
  for label, m, d, q in candidates:
    Hm = H(m, d, q)
    check(
      f"H({label}) is Hermitian",
      np.allclose(Hm, Hm.conj().T, atol=1e-14),
    )
    K = UZ3.conj().T @ Hm @ UZ3
    check(
      f"K_Z3({label}) is Hermitian",
      np.allclose(K, K.conj().T, atol=1e-12),
    )
    if a_star_ref is None:
      a_star_ref = K[0, 1]
      b_star_ref = K[0, 2]
    check(
      f"K[0,1] = a_* frozen at {label}",
      abs(K[0, 1] - a_star_ref) < 1e-12,
      f"a_*={a_star_ref:.8f}, diff={abs(K[0,1]-a_star_ref):.2e}",
    )
    check(
      f"K[0,2] = b_* frozen at {label}",
      abs(K[0, 2] - b_star_ref) < 1e-12,
      f"b_*={b_star_ref:.8f}, diff={abs(K[0,2]-b_star_ref):.2e}",
    )

  # K11, K22, K12 (doublet block) ARE chamber-varying
  K_A = UZ3.conj().T @ H(*(candidates[0][1:])) @ UZ3
  K_B = UZ3.conj().T @ H(*(candidates[1][1:])) @ UZ3
  check(
    "K_doublet varies on chamber (|K_A - K_B| > 0.1)",
    np.linalg.norm(K_A[1:, 1:] - K_B[1:, 1:]) > 0.1,
  )


# ---------------------------------------------------------------------------
# Part 2: the PMNS map (m, delta, q_+) -> (theta_12, theta_13, theta_23)
#     varies across the chamber
# ---------------------------------------------------------------------------


def part2_pmns_varies_on_chamber() -> None:
  print()
  print("=" * 88)
  print("Part 2: PMNS angles as f(H) vary across the chamber")
  print("=" * 88)

  candidates = [
    ("A Schur-Q", 0.5, math.sqrt(6) / 3.0, math.sqrt(6) / 3.0),
    ("B det-crit", 0.613, 0.964, 1.552),
    ("C Tr(H^2)-bdy", 0.385, 1.268, 0.365),
    ("D K12 char", 0.0, 0.800, 1.000),
    (
      "E par-mix F1",
      4 * math.sqrt(2) / 9,
      math.sqrt(6) / 2 - math.sqrt(2) / 18,
      math.sqrt(6) / 6 + math.sqrt(2) / 18,
    ),
  ]

  angles_list = []
  for label, m, d, q in candidates:
    obs = pmns_observables(m, d, q)
    angles_list.append((obs["s12sq"], obs["s13sq"], obs["s23sq"]))
    print(
      f" {label:15s} (m,d,q)=({m:.4f},{d:.4f},{q:.4f}) "
      f"s12^2={obs['s12sq']:.4f} s13^2={obs['s13sq']:.4f} "
      f"s23^2={obs['s23sq']:.4f} sin(d_CP)={obs['sin_dcp']:.3f}"
    )

  s12_spread = max(a[0] for a in angles_list) - min(a[0] for a in angles_list)
  s13_spread = max(a[1] for a in angles_list) - min(a[1] for a in angles_list)
  s23_spread = max(a[2] for a in angles_list) - min(a[2] for a in angles_list)

  check("sin^2 theta_12 varies on chamber (spread > 0.1)", s12_spread > 0.1,
     f"spread={s12_spread:.4f}")
  check("sin^2 theta_13 varies on chamber (spread > 0.01)", s13_spread > 0.01,
     f"spread={s13_spread:.4f}")
  check("sin^2 theta_23 varies on chamber (spread > 0.01)", s23_spread > 0.01,
     f"spread={s23_spread:.4f}")


# ---------------------------------------------------------------------------
# Part 3: finite multistart fitted candidate (m_*, delta_*, q_+*)
# ---------------------------------------------------------------------------

TARGET_S12SQ = 0.307  # supplied historical angle target
TARGET_S13SQ = 0.0218 # supplied historical angle target
TARGET_S23SQ = 0.545  # supplied historical angle target


def chi2_chamber(m: float, delta: float, q_plus: float) -> float:
  """Unweighted squared residual to supplied historical angles; not statistical chi^2."""
  if q_plus + delta < E1 - 1e-9:
    return 1e12
  obs = pmns_observables(m, delta, q_plus)
  return (
    (obs["s12sq"] - TARGET_S12SQ) ** 2
    + (obs["s13sq"] - TARGET_S13SQ) ** 2
    + (obs["s23sq"] - TARGET_S23SQ) ** 2
  )


def part3_unique_chamber_solution() -> tuple[float, float, float]:
  print()
  print("=" * 88)
  print("Part 3: numerical chamber candidate (m_*, delta_*, q_+*) via multi-start")
  print("=" * 88)

  try:
    from scipy.optimize import minimize, fsolve # noqa: F401
  except ImportError:
    print(" scipy unavailable; running deterministic Newton fallback")
    return _newton_fallback_solution()

  def f_chi2(x):
    m, d, q = x
    return chi2_chamber(m, d, q)

  def f_equations(x):
    m, d, q = x
    obs = pmns_observables(m, d, q)
    return [
      obs["s12sq"] - TARGET_S12SQ,
      obs["s13sq"] - TARGET_S13SQ,
      obs["s23sq"] - TARGET_S23SQ,
    ]

  rng = np.random.default_rng(2026_04_17)
  minima = []
  for _ in range(60):
    x0 = [
      rng.uniform(0.1, 1.5),
      rng.uniform(-0.5, 1.5),
      rng.uniform(-0.5, 1.5),
    ]
    if x0[1] + x0[2] < E1:
      x0[2] = E1 - x0[1] + 0.1
    res = minimize(
      f_chi2,
      x0,
      method="Nelder-Mead",
      options=dict(xatol=1e-10, fatol=1e-14, maxiter=20000),
    )
    if res.fun < 1e-4:
      minima.append(tuple(np.round(res.x, 6)))

  unique = set(minima)
  check(
    f"accepted random starts converge to one rounded chamber solution",
    len(unique) == 1,
    f"{len(unique)} distinct minima; ~{len(minima)} accepted",
  )
  if not unique:
    print(" FAIL: no chamber solution found")
    return 0.0, 0.0, 0.0

  (m_star, d_star, q_star) = sorted(unique)[0]
  print(f" pinned (m_*, delta_*, q_+*) = ({m_star:.6f}, {d_star:.6f}, {q_star:.6f})")

  # Sharpen with fsolve
  sol = fsolve(
    f_equations,
    [m_star, d_star, q_star],
    full_output=True,
    xtol=1e-14,
  )
  m_star, d_star, q_star = sol[0]
  print(f" fsolve-sharpened  = ({m_star:.12f}, {d_star:.12f}, {q_star:.12f})")

  obs = pmns_observables(m_star, d_star, q_star)
  check(
    f"pinned s12^2 = {TARGET_S12SQ} (machine-precise)",
    abs(obs["s12sq"] - TARGET_S12SQ) < 1e-10,
    f"val={obs['s12sq']:.12f}",
  )
  check(
    f"pinned s13^2 = {TARGET_S13SQ} (machine-precise)",
    abs(obs["s13sq"] - TARGET_S13SQ) < 1e-10,
    f"val={obs['s13sq']:.12f}",
  )
  check(
    f"pinned s23^2 = {TARGET_S23SQ} (machine-precise)",
    abs(obs["s23sq"] - TARGET_S23SQ) < 1e-10,
    f"val={obs['s23sq']:.12f}",
  )
  check(
    "pinned (delta_*, q_+*) lies strictly inside chamber (q_+ + delta > sqrt(8/3))",
    q_star + d_star > E1 + 1e-6,
    f"dist = q_+ + delta - sqrt(8/3) = {q_star + d_star - E1:.6f}",
  )
  return m_star, d_star, q_star


def _newton_fallback_solution() -> tuple[float, float, float]:
  # Simple Newton iteration as scipy fallback.
  x = np.array([0.657061, 0.933806, 0.715042])
  for _ in range(50):
    obs = pmns_observables(*x)
    F = np.array(
      [obs["s12sq"] - TARGET_S12SQ,
       obs["s13sq"] - TARGET_S13SQ,
       obs["s23sq"] - TARGET_S23SQ]
    )
    if np.linalg.norm(F) < 1e-12:
      break
    eps = 1e-6
    J = np.zeros((3, 3))
    for k in range(3):
      x1 = x.copy(); x1[k] += eps
      o1 = pmns_observables(*x1)
      dF = np.array(
        [o1["s12sq"] - obs["s12sq"],
         o1["s13sq"] - obs["s13sq"],
         o1["s23sq"] - obs["s23sq"]]
      )
      J[:, k] = dF / eps
    try:
      dx = np.linalg.solve(J, -F)
    except np.linalg.LinAlgError:
      break
    x = x + dx
  return tuple(x)


# ---------------------------------------------------------------------------
# Part 4: supplied historical modulus intervals at the fitted point
# ---------------------------------------------------------------------------


def part4_pdg_ranges(m_star: float, d_star: float, q_star: float) -> None:
  print()
  print("=" * 88)
  print("Part 4: supplied historical NuFit 5.3 modulus intervals at fitted point")
  print("=" * 88)

  obs = pmns_observables(m_star, d_star, q_star)
  # Supplied approximate historical NuFit 5.3 NO intervals; not a likelihood
  pdg_lo = np.array(
    [[0.801, 0.513, 0.143],
     [0.234, 0.471, 0.637],
     [0.271, 0.477, 0.613]]
  )
  pdg_hi = np.array(
    [[0.845, 0.579, 0.155],
     [0.500, 0.689, 0.776],
     [0.525, 0.694, 0.756]]
  )

  U = obs["abs_PMNS"]
  print(" |U_PMNS| at pinned point:")
  for row in U:
    print(f"  [{row[0]:.4f}, {row[1]:.4f}, {row[2]:.4f}]")

  for i in range(3):
    for j in range(3):
      inside = pdg_lo[i, j] <= U[i, j] <= pdg_hi[i, j]
      check(
        f"|U_{i+1}{j+1}| in supplied historical interval [{pdg_lo[i,j]:.3f},{pdg_hi[i,j]:.3f}]",
        inside,
        f"val={U[i,j]:.4f}",
      )


# ---------------------------------------------------------------------------
# Part 5: conditional fitted delta_CP and Jarlskog
# ---------------------------------------------------------------------------


def part5_delta_cp(m_star: float, d_star: float, q_star: float) -> None:
  print()
  print("=" * 88)
  print("Part 5: conditional fitted delta_CP and Jarlskog at pinned chamber point")
  print("=" * 88)

  obs = pmns_observables(m_star, d_star, q_star)
  print(f" J (Jarlskog)  = {obs['J']:+.6f}")
  print(f" sin(delta_CP)  = {obs['sin_dcp']:+.4f}")
  print(f" cos(delta_CP)  = {obs['cos_dcp']:+.4f}")
  print(f" delta_CP (deg, atan2) = {obs['dcp_deg']:.2f}")

  # Historical numerical band only; no experimental confidence claim
  check(
    "|Jarlskog| lies in supplied numerical band [0.025,0.040]",
    0.025 <= abs(obs["J"]) <= 0.040,
    f"|J|={abs(obs['J']):.4f}",
  )
  # Sign control at this conditional candidate; no experimental inference.
  check(
    "sin(delta_CP) negative at supplied fitted candidate",
    obs["sin_dcp"] < 0.0,
  )


# ---------------------------------------------------------------------------
# Part 6: finite comparisons against five supplied historical points
# ---------------------------------------------------------------------------


def part6_candidate_cross_check(m_star: float, d_star: float, q_star: float) -> None:
  print()
  print("=" * 88)
  print("Part 6: finite comparison against five supplied historical points")
  print("=" * 88)

  candidates = {
    "A Schur-Q": (0.5, math.sqrt(6) / 3.0, math.sqrt(6) / 3.0),
    "B det-crit": (0.613, 0.964, 1.552),
    "C Tr(H^2)-bdy": (0.385, 1.268, 0.365),
    "D K12 char": (0.0, 0.800, 1.000),
    "E par-mix F1": (
      4 * math.sqrt(2) / 9,
      math.sqrt(6) / 2 - math.sqrt(2) / 18,
      math.sqrt(6) / 6 + math.sqrt(2) / 18,
    ),
  }
  matches = []
  for label, (m, d, q) in candidates.items():
    dist = math.sqrt((d - d_star) ** 2 + (q - q_star) ** 2)
    print(
      f" {label:15s} (d,q)=({d:.4f},{q:.4f})  "
      f"distance to pinned (d_*,q_*) = {dist:.4f}"
    )
    if dist < 1e-3:
      matches.append(label)

  check(
    "fitted (delta_*, q_+*) differs by >=1e-3 from five supplied points",
    not matches,
    f"matches={matches}",
  )


# ---------------------------------------------------------------------------
# Part 7: numerical Fourier-slot comparisons
# ---------------------------------------------------------------------------


def part7_frozen_slots_closed_form() -> None:
  print()
  print("=" * 88)
  print("Part 7: sampled singlet-doublet slots a_*, b_*")
  print("=" * 88)

  # Compute a_* = K[0,1] at one supplied chamber point.
  m, d, q = 0.5, math.sqrt(6) / 3.0, math.sqrt(6) / 3.0
  K = UZ3.conj().T @ H(m, d, q) @ UZ3
  a_star = K[0, 1]
  b_star = K[0, 2]
  # Numerical values for the supplied affine structure.
  print(f" a_* = K[0,1] = {a_star.real:.10f} + i {a_star.imag:.10f}")
  print(f" b_* = K[0,2] = {b_star.real:.10f} + i {b_star.imag:.10f}")
  print(f" |a_*| = {abs(a_star):.10f}")
  print(f" |b_*| = {abs(b_star):.10f}")

  # Second chamber point to confirm chamber-blindness
  m2, d2, q2 = 0.2, 1.1, 0.9
  K2 = UZ3.conj().T @ H(m2, d2, q2) @ UZ3
  check(
    "a_* agrees at two sampled chamber points",
    abs(K2[0, 1] - a_star) < 1e-12,
  )
  check(
    "b_* agrees at two sampled chamber points",
    abs(K2[0, 2] - b_star) < 1e-12,
  )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
  print("=" * 88)
  print("CONDITIONAL PMNS MAP AND FINITE FIT ON A SUPPLIED CHART")
  print("=" * 88)
  print()
  print("Attack line: L1 (direct diagonalization of H).")
  print("Supplied inputs: affine chart, charged-lepton axis basis U_e=I,")
  print("flavor row permutation (2,1,0), and three historical angle targets.")
  print("Eigenvector columns are sorted by ascending H eigenvalue.")
  print("Finite fit and interval checks supply no current experimental likelihood.")

  part1_structural_checks()
  part2_pmns_varies_on_chamber()
  m_star, d_star, q_star = part3_unique_chamber_solution()
  part4_pdg_ranges(m_star, d_star, q_star)
  part5_delta_cp(m_star, d_star, q_star)
  part6_candidate_cross_check(m_star, d_star, q_star)
  part7_frozen_slots_closed_form()

  print()
  print("=" * 88)
  print(f" PASS = {PASS_COUNT}")
  print(f" FAIL = {FAIL_COUNT}")
  print("=" * 88)

  # Summary
  print()
  print("Summary:")
  print(f" Pinned chamber point (m_*, delta_*, q_+*) = "
     f"({m_star:.6f}, {d_star:.6f}, {q_star:.6f})")
  obs = pmns_observables(m_star, d_star, q_star)
  print(f" Conditional fitted delta_CP = {obs['dcp_deg']:+.2f} deg (sin = {obs['sin_dcp']:+.4f})")
  print(f" Jarlskog J     = {obs['J']:+.6f}")
  print(" Physical source/basis/branch selection and global uniqueness remain open.")

  return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
  raise SystemExit(main())
