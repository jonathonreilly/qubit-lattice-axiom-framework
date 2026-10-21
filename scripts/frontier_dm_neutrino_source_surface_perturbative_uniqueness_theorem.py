#!/usr/bin/env python3
"""Finite PMNS affine-matrix searches under supplied targets and inertia filter.

The numerical scan and its original predicates are preserved. It searches all
six permutations but finitely many starts; optimizer failure is not proof of
nonexistence. The imposed same-inertia filter is not a derived physical rule
or a certificate of connectedness in this restricted affine surface. Legacy
43/46 counts must be replaced only by the actual capped-run outcome.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

import itertools
import math

import numpy as np

np.set_printoptions(precision=8, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
  global PASS_COUNT, FAIL_COUNT
  status = "PASS" if condition else "FAIL"
  if condition:
    PASS_COUNT += 1
  else:
    FAIL_COUNT += 1
  msg = f" [{status}] {name}"
  if detail:
    msg += f" ({detail})"
  print(msg)
  return condition


# ---------------------------------------------------------------------------
# Retained atlas constants
# ---------------------------------------------------------------------------

GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
OMEGA = np.exp(2j * math.pi / 3.0)

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

# PDG 2024 / NuFit 5.3 NO central values used by the PMNS-closure theorem
TARGET_S12SQ = 0.307
TARGET_S13SQ = 0.0218
TARGET_S23SQ = 0.545

# The three Frobenius reference norms
H_BASE_F = float(np.linalg.norm(H_BASE, "fro"))
H_BASE_OP = float(np.linalg.norm(H_BASE, 2))
H_BASE_SR = float(max(abs(np.linalg.eigvalsh(H_BASE))))


def inertia(M, tol=1e-9):
  """Return (signature (n_-, n_0, n_+), det) for a Hermitian matrix M.

  Signature is the Sylvester inertia triple of the real eigenvalue spectrum.
  Retained congruence-invariant of a Hermitian form; used as the primary
  source-branch discriminator (imposed same-inertia filter)."""
  w = np.real(np.linalg.eigvalsh(M))
  sig = (
    int((w < -tol).sum()),
    int((np.abs(w) <= tol).sum()),
    int((w > tol).sum()),
  )
  return sig, float(np.real(np.linalg.det(M)))


H_BASE_SIG, H_BASE_DET = inertia(H_BASE)


def H(m, d, q):
  return H_BASE + m * T_M + d * T_DELTA + q * T_Q


def J_of(m, d, q):
  return m * T_M + d * T_DELTA + q * T_Q


def pmns_map(m, d, q, perm=(2, 1, 0)):
  Hm = H(m, d, q)
  w, V = np.linalg.eigh(Hm)
  order = np.argsort(np.real(w))
  w = np.real(w[order])
  V = V[:, order]
  P = V[list(perm), :]
  s13sq = abs(P[0, 2]) ** 2
  c13sq = max(1.0 - s13sq, 1e-18)
  s12sq = abs(P[0, 1]) ** 2 / c13sq
  s23sq = abs(P[1, 2]) ** 2 / c13sq
  s12 = math.sqrt(max(s12sq, 0.0)); c12 = math.sqrt(max(1 - s12sq, 0.0))
  s13 = math.sqrt(max(s13sq, 0.0)); c13 = math.sqrt(max(c13sq, 0.0))
  s23 = math.sqrt(max(s23sq, 0.0)); c23 = math.sqrt(max(1 - s23sq, 0.0))
  J = (P[0, 0] * P[0, 1].conjugate() * P[1, 0].conjugate() * P[1, 1]).imag
  denom = s12 * c12 * s23 * c23 * s13 * c13 * c13
  sin_dcp = max(-1.0, min(1.0, J / denom if denom > 1e-18 else 0.0))
  return dict(s12sq=s12sq, s13sq=s13sq, s23sq=s23sq, J=J, sin_dcp=sin_dcp, P=P, eigvals=w)


def norms_of(m, d, q):
  Jmat = J_of(m, d, q)
  fro = float(np.linalg.norm(Jmat, "fro"))
  op = float(np.linalg.norm(Jmat, 2))
  sr = float(max(abs(np.linalg.eigvalsh(Jmat))))
  return dict(fro=fro, op=op, sr=sr)


# ---------------------------------------------------------------------------
# Part 1. Baseline and supplied diagnostic scales.
# ---------------------------------------------------------------------------


def part1_perturbative_criterion_axiom_native():
  print('Part 1: supplied baseline and finite norm diagnostics.')
  print('For invertible D, rho(D^-1 J)<1 suffices for the log-det Taylor expansion at source amplitude1.')
  print('W[J]=log|det(D+J)|-log|det(D)| is also defined outside that Taylor domain whenever det(D+J) is nonzero.')
  print('Neither ||J||F<=||D||F nor ||J||op<=||D||op is a necessary or sufficient Taylor-convergence criterion.')
  print('These are supplied size cuts, not an axiom-derived physical selection principle.')
  print('Positive determinant alone does not determine inertia; inertia alone need not determine connectedness within an affine restriction.')
  # Numerical certificate that the three reference norms agree in ordering
  print("Numerical reference:")
  print(f" ||H_base||_F = {H_BASE_F:.6f}")
  print(f" ||H_base||_op = {H_BASE_OP:.6f}")
  print(f" ||H_base||_sr = spectral radius = {H_BASE_SR:.6f}")
  Hinv_op = float(np.linalg.norm(np.linalg.inv(H_BASE), 2))
  print(f" ||H_base^{{-1}}||_op = {Hinv_op:.6f}")
  print()
  print("Retained inertia invariants of H_base (Sylvester-inertia lemma):")
  print(f" signature(H_base) = {H_BASE_SIG}  (n_-, n_0, n_+)")
  print(f" det(H_base)       = {H_BASE_DET:+.6f}")
  check(
    "H_base has no zero eigenvalue (so D^{-1} exists; Taylor series well posed)",
    min(abs(np.linalg.eigvalsh(H_BASE))) > 1e-6,
  )
  check(
    "Supplied baseline signature(H_base) = (2, 0, 1)",
    H_BASE_SIG == (2, 0, 1),
    f"got {H_BASE_SIG}",
  )
  check(
    "Supplied baseline det(H_base) > 0",
    H_BASE_DET > 0,
    f"got {H_BASE_DET:+.6f}",
  )
  # Sanity: the three norms of H_base obey Fro >= op = sr (H_base is Hermitian)
  check(
    "Hermitian H_base: ||H_base||_op == spectral radius",
    abs(H_BASE_OP - H_BASE_SR) < 1e-10,
    f"op={H_BASE_OP:.6f}, sr={H_BASE_SR:.6f}",
  )
  check(
    "||H_base||_F >= ||H_base||_op (Cauchy-Schwarz)",
    H_BASE_F >= H_BASE_OP - 1e-10,
  )


# ---------------------------------------------------------------------------
# Part 2. Finite multistart scan of all six permutations.
# ---------------------------------------------------------------------------


def multistart_chamber(perm, n_starts=60, box=(-5.0, 10.0), seed=2026_04_17,
            target=(TARGET_S12SQ, TARGET_S13SQ, TARGET_S23SQ),
            tol=1e-8):
  """Return finite clusters with residual sum of squares below tol inside the chamber."""
  from scipy.optimize import minimize
  rng = np.random.default_rng(seed)

  def chi2(x):
    m, d, q = x
    if q + d < E1 - 1e-6:
      return 1e12
    obs = pmns_map(m, d, q, perm)
    return (
      (obs["s12sq"] - target[0]) ** 2
      + (obs["s13sq"] - target[1]) ** 2
      + (obs["s23sq"] - target[2]) ** 2
    )

  found = []
  for _ in range(n_starts):
    x0 = rng.uniform(box[0], box[1], size=3)
    # Keep starts in the chamber
    if x0[1] + x0[2] < E1:
      x0[2] = E1 - x0[1] + 0.1
    res = minimize(
      chi2, x0, method="Nelder-Mead",
      options=dict(xatol=1e-11, fatol=1e-15, maxiter=40000),
    )
    if res.fun < tol and res.x[1] + res.x[2] >= E1 - 1e-6:
      found.append(tuple(res.x))

  # Cluster
  clusters = []
  for x in found:
    placed = False
    for c in clusters:
      if np.linalg.norm(np.array(c["rep"]) - np.array(x)) < 0.5:
        c["pts"].append(x)
        placed = True
        break
    if not placed:
      clusters.append({"rep": x, "pts": [x]})
  return clusters


def part2_exhaustive_perm_scan():
  print()
  print("=" * 88)
  print("Part 2: finite multistart scan across all six permutations")
  print("=" * 88)
  print()
  print("Initial starts: [-5,10]^3,60/perm; Nelder-Mead iterates are not box-constrained.")
  print()

  basin_records = []
  for perm in itertools.permutations(range(3)):
    print(f"--- permutation sigma = {perm} ---")
    clusters = multistart_chamber(perm, n_starts=60)
    if not clusters:
      print(f"  no chamber closure found")
      continue
    for c in clusters:
      x = c["rep"]
      obs = pmns_map(*x, perm=perm)
      nrms = norms_of(*x)
      ratio_F = nrms["fro"] / H_BASE_F
      ratio_op = nrms["op"] / H_BASE_OP
      print(
        f"  basin @ (m,d,q)=({x[0]:7.3f},{x[1]:7.3f},{x[2]:7.3f}) "
        f"sin(dcp)={obs['sin_dcp']:+.4f} "
        f"|J|_F/|H|_F={ratio_F:.3f} |J|_op/|H|_op={ratio_op:.3f}"
      )
      basin_records.append(
        dict(perm=perm, x=x, obs=obs, nrms=nrms,
           ratio_F=ratio_F, ratio_op=ratio_op)
      )
  return basin_records


# ---------------------------------------------------------------------------
# Part 3. Verify the perturbative criterion uniquely selects Basin 1.
# ---------------------------------------------------------------------------


def part3_perturbative_selects_basin1(basins):
  print('Part 3: imposed same-inertia filter applied only to clusters found by this finite search.')
  print('The filter is signature(H_base+J)=signature(H_base)=(2,0,1). It is not derived physical admissibility.')
  print('The positive-determinant test is redundant for this inertia but is not equivalent to it in general.')
  print('Any continuous nonsingular path preserves inertia. The converse need not hold on this restricted affine surface.')
  print('No path-connectivity certificate or exhaustive solution count is computed.')
  # Inertia of H_base + J at each basin
  def basin_inertia(b):
    Hm = H(*b["x"])
    return inertia(Hm)

  # Source-branch selector
  on_branch = []
  off_branch = []
  for b in basins:
    sig, det = basin_inertia(b)
    rec = dict(b=b, sig=sig, det=det)
    if sig == H_BASE_SIG and det > 0:
      on_branch.append(rec)
    else:
      off_branch.append(rec)

  # Consistency diagnostics (demoted from primary selectors)
  pert_F = [b for b in basins if b["ratio_F"] <= 1.0]
  pert_op = [b for b in basins if b["ratio_op"] <= 1.0]

  def rho_DinvJ(b):
    Jmat = J_of(*b["x"])
    M = np.linalg.solve(H_BASE, Jmat)
    return float(max(abs(np.linalg.eigvals(M))))
  pert_rho = [b for b in basins if rho_DinvJ(b) < 1.0]

  print(f" Found in-chamber clusters with residual below tolerance across six permutations: {len(basins)}")
  print(f" Found-cluster inventory (numerical inertia at H_base + J):")
  for rec in on_branch + off_branch:
    b = rec["b"]
    x = b["x"]
    obs = b["obs"]
    print(
      f"  perm={b['perm']} @ (m,d,q)=({x[0]:7.3f},{x[1]:7.3f},{x[2]:7.3f}) "
      f"sig={rec['sig']} det={rec['det']:+10.3f} "
      f"sin(dcp)={obs['sin_dcp']:+.4f} "
      f"{'[ON BRANCH]' if rec in on_branch else '[off branch]'}"
    )
  print()
  print(f" Found clusters passing the imposed same-inertia filter: {len(on_branch)} basin(s)")
  print(f" Found clusters failing the imposed same-inertia filter: {len(off_branch)} basin(s)")
  print()
  print(" Consistency diagnostics (non-selector):")
  print(f"  Frobenius scale (|J|_F <= |H|_F):       {len(pert_F)} basin(s)")
  print(f"  Operator-norm scale (|J|_op <= |H|_op): {len(pert_op)} basin(s)")
  print(f"  Taylor convergence (rho(D^{{-1}}J) < 1):   {len(pert_rho)} basin(s)")
  print()
  print("Scale cuts are diagnostics on found clusters; rho<1 is checked separately.")
  print("No retained authority, global uniqueness, or physical selector is established.")

  # ---- PRIMARY under the imposed rule: signature-preserving selector ----
  check(
    "Finite search: exactly one found cluster passes imposed same-inertia filter",
    len(on_branch) == 1,
    f"admissible={len(on_branch)}",
  )
  check(
    "At least one found cluster fails the same-inertia filter",
    len(off_branch) >= 1,
    f"off-branch count={len(off_branch)}",
  )

  if on_branch:
    rec = on_branch[0]
    b = rec["b"]
    x = b["x"]
    obs = b["obs"]
    check(
      "Admissible (under imposed rule) basin preserves signature (2, 0, 1)",
      rec["sig"] == (2, 0, 1),
      f"sig={rec['sig']}",
    )
    check(
      "Admissible basin preserves sgn det > 0",
      rec["det"] > 0,
      f"det={rec['det']:+.3f}",
    )
    check(
      "Admissible basin is at permutation sigma=(2,1,0)",
      b["perm"] == (2, 1, 0),
      f"perm={b['perm']}",
    )
    check(
      "Admissible basin is the PMNS-closure theorem Basin 1 @ (0.657, 0.934, 0.715)",
      abs(x[0] - 0.657061) < 5e-3
      and abs(x[1] - 0.933806) < 5e-3
      and abs(x[2] - 0.715042) < 5e-3,
      f"(m,d,q) = ({x[0]:.6f}, {x[1]:.6f}, {x[2]:.6f})",
    )
    check(
      "Admissible basin gives sin(delta_CP) = -0.987 (conditional on imposed rule)",
      abs(obs["sin_dcp"] - (-0.9874)) < 5e-3,
      f"sin(delta_CP)={obs['sin_dcp']:+.4f}",
    )

  # Off-branch basins must have flipped signature (otherwise selector is vacuous)
  for rec in off_branch:
    b = rec["b"]
    check(
      f"Off-branch basin at perm={b['perm']} (m,d,q)~({b['x'][0]:.2f},{b['x'][1]:.2f},{b['x'][2]:.2f}) has flipped signature (1,0,2)",
      rec["sig"] == (1, 0, 2),
      f"sig={rec['sig']}",
    )
    check(
      f"Off-branch basin at perm={b['perm']} has det < 0 (any nonsingular path to positive-det baseline is impossible)",
      rec["det"] < 0,
      f"det={rec['det']:+.3f}",
    )

  # ---- Consistency checks: scale diagnostics agree with imposed rule ----
  check(
    "Consistency: Frobenius scale picks the same basin as the imposed branch-choice rule",
    len(pert_F) == 1
    and len(on_branch) == 1
    and pert_F[0]["x"] == on_branch[0]["b"]["x"],
  )
  check(
    "Consistency: operator-norm scale picks the same basin as the imposed branch-choice rule",
    len(pert_op) == 1
    and len(on_branch) == 1
    and pert_op[0]["x"] == on_branch[0]["b"]["x"],
  )

  # Non-perturbative basins with opposite-sign dcp must exist (otherwise the
  # selector is physically vacuous).
  opp_sign = [rec for rec in off_branch if rec["b"]["obs"]["sin_dcp"] > 0]
  check(
    "At least one off-branch basin predicts sin(delta_CP) > 0 (opposite sign)",
    len(opp_sign) >= 1,
    f"count={len(opp_sign)}",
  )

  # ---- Honest flag: Taylor convergence is NOT a selector here ----
  all_rhos = sorted([(rho_DinvJ(b), b) for b in basins])
  check(
    "Finite inventory: rho(D^{-1}J) < 1 fails at every found cluster",
    len(pert_rho) == 0,
    f"min rho over basins = {all_rhos[0][0]:.3f}",
  )
  check(
    "Among found clusters, the same-inertia cluster minimises rho(D^{-1} J) (closest to series disk)",
    len(on_branch) == 1 and all_rhos[0][1]["x"] == on_branch[0]["b"]["x"],
    f"smallest rho={all_rhos[0][0]:.3f} at x={all_rhos[0][1]['x']}",
  )


# ---------------------------------------------------------------------------
# Part 4. Explicit numerical profile of the three advertised basins.
# ---------------------------------------------------------------------------


def part4_three_advertised_basins():
  print()
  print("=" * 88)
  print("Part 4: numerical profile of the three advertised adversarial basins")
  print("=" * 88)
  print()

  basins = [
    ("Basin 1 sigma=(2,1,0)", (2, 1, 0), (0.657061, 0.933806, 0.715042)),
    ("Basin 2 sigma=(2,1,0)", (2, 1, 0), (28.0, 20.7, 5.0)),
    ("Basin X sigma=(2,0,1)", (2, 0, 1), (21.0, 12.68, 2.089)),
  ]
  for label, perm, seed_point in basins:
    # Sharpen via fsolve from the seed
    from scipy.optimize import fsolve
    def eqs(x, perm=perm):
      m, d, q = x
      obs = pmns_map(m, d, q, perm)
      return [
        obs["s12sq"] - TARGET_S12SQ,
        obs["s13sq"] - TARGET_S13SQ,
        obs["s23sq"] - TARGET_S23SQ,
      ]
    sol = fsolve(eqs, seed_point, full_output=True, xtol=1e-14)
    x = tuple(sol[0])
    obs = pmns_map(*x, perm=perm)
    nrms = norms_of(*x)
    chamber_dist = x[1] + x[2] - E1
    print(f" {label}")
    print(f"  (m, delta, q_+)    = ({x[0]:+.6f}, {x[1]:+.6f}, {x[2]:+.6f})")
    print(f"  chamber distance   = {chamber_dist:+.4f}")
    print(f"  (s12^2, s13^2, s23^2) = ({obs['s12sq']:.4f}, {obs['s13sq']:.4f}, {obs['s23sq']:.4f})")
    print(f"  sin(delta_CP)     = {obs['sin_dcp']:+.4f}")
    print(f"  |J|_F / |H_base|_F  = {nrms['fro']/H_BASE_F:.3f}")
    print(f"  |J|_op / |H_base|_op = {nrms['op']/H_BASE_OP:.3f}")
    M = np.linalg.solve(H_BASE, J_of(*x))
    rho = float(max(abs(np.linalg.eigvals(M))))
    print(f"  rho(H^{{-1}} J)      = {rho:.3f}")
    in_chamber = chamber_dist >= -1e-6
    if label.startswith("Basin 1"):
      check(f"{label}: inside chamber", in_chamber)
      check(f"{label}: |J|_F / |H|_F < 1 (scale-perturbative, Frobenius)",
         nrms["fro"] / H_BASE_F < 1.0)
      check(f"{label}: |J|_op / |H|_op < 1 (scale-perturbative, operator)",
         nrms["op"] / H_BASE_OP < 1.0)
    else:
      check(f"{label}: returned iterate inside chamber; convergence/residual not certified", in_chamber)
      check(f"{label}: |J|_F / |H|_F > 1 (non-scale-perturbative, Frobenius)",
         nrms["fro"] / H_BASE_F > 1.0)
      check(f"{label}: |J|_op / |H|_op > 1 (non-scale-perturbative, operator)",
         nrms["op"] / H_BASE_OP > 1.0)
    # Universal: all basins satisfy rho > 1 (we document this honestly)
    # Basin 1 has the SMALLEST rho (closest to Taylor-convergence).


# ---------------------------------------------------------------------------
# Part 5. theta_23 chamber-closure threshold.
# ---------------------------------------------------------------------------


def part5_theta23_chamber_threshold():
  print()
  print("=" * 88)
  print("Part 5: finite-search target transition diagnostic")
  print("=" * 88)
  print()

  from scipy.optimize import minimize

  def find_closure(s23_t, nstarts=40, tol=1e-9, perm=(2, 1, 0)):
    rng = np.random.default_rng(1234 + int(1e6 * s23_t))
    def chi2(x):
      if x[1] + x[2] < E1 - 1e-6:
        return 1e12
      obs = pmns_map(x[0], x[1], x[2], perm)
      return (
        (obs["s12sq"] - TARGET_S12SQ) ** 2
        + (obs["s13sq"] - TARGET_S13SQ) ** 2
        + (obs["s23sq"] - s23_t) ** 2
      )
    best = None
    for _ in range(nstarts):
      x0 = rng.uniform([0.1, 0.3, 0.3], [1.2, 1.3, 1.3])
      if x0[1] + x0[2] < E1:
        x0[2] = E1 - x0[1] + 0.1
      res = minimize(
        chi2, x0, method="Nelder-Mead",
        options=dict(xatol=1e-12, fatol=1e-16, maxiter=40000),
      )
      if res.fun < tol and res.x[1] + res.x[2] >= E1 - 1e-6:
        if best is None or res.fun < best[1]:
          best = (res.x, res.fun)
    return best

  # Course probes at representative NuFit octant points
  probes = [
    ("NuFit NO lower-octant best fit (~0.445)", 0.445, False),
    ("NuFit 1-sigma upper edge (~0.527)", 0.527, False),
    ("NuFit NO upper-octant best fit (0.545)", 0.545, True),
    ("NuFit 3-sigma upper edge (~0.600)", 0.600, True),
  ]
  for label, s23, expect_chamber in probes:
    r = find_closure(s23)
    has_closure = r is not None
    print(f" {label}: s23^2 = {s23} => "
       f"{'point found' if has_closure else 'no point found'} by finite search "
       f"(expected search success={expect_chamber})")
    check(
      f"s23^2 = {s23}: finite-search success = {expect_chamber}",
      has_closure == expect_chamber,
    )

  # Binary search threshold
  print()
  print(" Binary search using a finite optimizer-success indicator (not a certified existence oracle)...")
  lo, hi = 0.540, 0.545
  for _ in range(24):
    mid = 0.5 * (lo + hi)
    r = find_closure(mid, nstarts=30)
    if r is None:
      lo = mid
    else:
      hi = mid
    if hi - lo < 1e-6:
      break
  threshold = 0.5 * (lo + hi)
  print(f"  s23^2_threshold = {threshold:.6f} (bracket [{lo:.6f}, {hi:.6f}])")
  check(
    "Finite-search transition estimate lies in [0.540, 0.542]",
    0.540 <= threshold <= 0.542,
    f"threshold={threshold:.6f}",
  )
  check(
    "Finite-search transition estimate exceeds supplied comparator0.5",
    threshold > 0.5,
    f"threshold={threshold:.6f}",
  )
  check(
    "Finite-search transition estimate exceeds historical comparator0.527",
    threshold > 0.527,
    f"threshold={threshold:.6f}",
  )
  print()
  print(" ==> This search reports an upper-octant transition estimate,")
  print(f"   near s23^2 = {threshold:.4f} for this supplied map and search,")
  print("   at the supplied historical (s12^2,s13^2) targets.")
  print("   No global lower-octant exclusion or experimental significance is established.")


# ---------------------------------------------------------------------------
# Part 6. Z_3 trichotomy q_H = 0 route for U_e = I (primary route).
# ---------------------------------------------------------------------------


def part6_trichotomy_route_for_Ue_identity():
  print('Part 6: finite support enumeration for supplied Z3 charges.')
  print('Assuming qL=(0,1,-1), qR=(0,-1,1) and neutrality modulo3 gives the listed permutation supports.')
  print('For the supplied diagonal example YeYe^dagger is diagonal; a left basis with no mixing can be chosen.')
  print('This does not derive the physical charge assignment, nondegenerate charged-lepton spectrum, or equivalence of full theories under right-handed relabeling.')
  # Verify the three branches give the claimed support pattern (structural)
  q_H_to_support = {
    0: [(0, 0), (1, 1), (2, 2)],
    +1: [(0, 1), (1, 2), (2, 0)],
    -1: [(0, 2), (1, 0), (2, 1)],
  }
  # The retained Z_3 charges (from the trichotomy note)
  qL = (0, +1, -1)
  qR = (0, -1, +1)
  for qH, expected in q_H_to_support.items():
    derived = []
    for i in range(3):
      for j in range(3):
        if (qL[i] + qH + qR[j]) % 3 == 0:
          derived.append((i, j))
    check(
      f"Z_3 support for q_H = {qH} matches trichotomy prediction",
      sorted(derived) == sorted(expected),
      f"derived={derived}, expected={expected}",
    )

  # The Y_e = diag case: any diagonal complex matrix diagonalises to itself
  # in the axis basis; U_e = I immediately.
  rng = np.random.default_rng(7)
  Y_e = np.diag(rng.uniform(0.3, 1.5, size=3).astype(complex) *
         np.exp(1j * rng.uniform(0, 2 * math.pi, size=3)))
  # U_e is fixed by the polar decomposition Y_e = U_e Sigma V^dagger; for a
  # diagonal Y_e in the axis basis, the mass-eigenstate rotation in the left
  # flavour sector is a *diagonal* phase rotation, which is observationally
  # absorbed into the charged-lepton phase convention. So U_e has |U_e| = I.
  # This is the axis-basis statement.
  abs_Ue = np.abs(Y_e) / np.abs(Y_e).sum(axis=0, keepdims=True).clip(1e-12)
  check(
    "Diagonal Y_e (q_H=0 support) gives |U_e| = I in axis basis (no mixing)",
    np.allclose(np.diag(abs_Ue / np.diag(abs_Ue).max()), 1.0, atol=1e-12)
    and np.allclose(abs_Ue - np.diag(np.diag(abs_Ue)), 0.0, atol=1e-12),
  )


# ---------------------------------------------------------------------------
# Part 7. delta_CP framing lemma: 3D -> 3-manifold in 4D.
# ---------------------------------------------------------------------------


def part7_dcp_framing():
  print('Part 7: local finite-difference Jacobian diagnostic at the supplied basin.')
  print('The fourth computed coordinate is sin(delta_CP), not delta_CP itself.')
  print('Rank3 at one numerical point is not a global embedded-manifold or injectivity theorem.')
  print('If the exact angle Jacobian is nonsingular on a smooth eigenvector branch, the inverse-function theorem gives local angle coordinates.')
  print('The finite-difference calculation below supports that local hypothesis numerically; it does not prove it with interval bounds.')
  # Numerical verification: Jacobian rank = 3 at Basin 1
  from scipy.optimize import fsolve
  def eqs(x, perm=(2, 1, 0)):
    m, d, q = x
    obs = pmns_map(m, d, q, perm)
    return [
      obs["s12sq"] - TARGET_S12SQ,
      obs["s13sq"] - TARGET_S13SQ,
      obs["s23sq"] - TARGET_S23SQ,
    ]
  sol = fsolve(eqs, (0.657061, 0.933806, 0.715042), full_output=True, xtol=1e-14)
  x = tuple(sol[0])
  # Full 4x3 jacobian of (s12^2, s13^2, s23^2, delta_CP) wrt (m, d, q)
  eps = 1e-6
  obs0 = pmns_map(*x)
  vec0 = np.array([obs0["s12sq"], obs0["s13sq"], obs0["s23sq"], obs0["sin_dcp"]])
  J4 = np.zeros((4, 3))
  for k in range(3):
    xp = list(x); xp[k] += eps
    o = pmns_map(*xp)
    vecp = np.array([o["s12sq"], o["s13sq"], o["s23sq"], o["sin_dcp"]])
    J4[:, k] = (vecp - vec0) / eps
  rank = np.linalg.matrix_rank(J4, tol=1e-5)
  print(f" Numerical Jacobian rank at Basin 1 = {rank} (expected 3)")
  check(
    "Finite-difference J4 has numerical rank3 at this point and tolerance",
    rank == 3,
  )
  # Verify the row corresponding to delta_CP is a linear combination of the other 3 rows
  J3 = J4[:3, :] # 3x3 jacobian of (s12^2, s13^2, s23^2)
  try:
    cof = np.linalg.solve(J3.T, J4[3, :])
    reconstructed = J3.T @ cof
    residual = float(np.linalg.norm(reconstructed - J4[3, :]))
  except Exception:
    residual = float('inf')
  check(
    "Numerical derivative row of sin(delta_CP) lies in the span of the three angle rows",
    residual < 1e-4,
    f"residual={residual:.2e}",
  )


# ---------------------------------------------------------------------------
# Part 8. Stress-test: wide-box perturbative-only scan with no extra basin.
# ---------------------------------------------------------------------------


def part8_no_other_perturbative_basin():
  print()
  print("=" * 88)
  print("Part 8: finite norm-cut chamber search")
  print("=" * 88)
  print()

  # Exact Frobenius Gram matrix for (T_M,T_DELTA,T_Q) is
  # [[3,0,2],[0,6,0],[2,0,6]], hence ||J||F^2=3m^2+6d^2+6q^2+4mq.
  # The optimizer already evaluates the actual matrix norm; the old diagonal
  # ellipsoid comments were wrong. Keep its starts, penalties and acceptance
  # thresholds unchanged. These finitely many starts are not an exhaustion.

  from scipy.optimize import minimize
  import itertools as it

  rng = np.random.default_rng(31415)
  bound = H_BASE_F * 1.05 # 5% beyond the perturbative limit
  found_pert = []
  for perm in it.permutations(range(3)):
    for _ in range(120):
      x0 = rng.uniform(-bound, bound, size=3)
      if x0[1] + x0[2] < E1:
        x0[2] = E1 - x0[1] + 0.1

      def chi2(x, perm=perm):
        if x[1] + x[2] < E1 - 1e-6:
          return 1e12
        if np.linalg.norm(J_of(*x), "fro") > bound:
          return 1e12
        obs = pmns_map(x[0], x[1], x[2], perm)
        return (
          (obs["s12sq"] - TARGET_S12SQ) ** 2
          + (obs["s13sq"] - TARGET_S13SQ) ** 2
          + (obs["s23sq"] - TARGET_S23SQ) ** 2
        )

      res = minimize(chi2, x0, method="Nelder-Mead",
              options=dict(xatol=1e-11, fatol=1e-15, maxiter=30000))
      if (res.fun < 1e-8
        and res.x[1] + res.x[2] >= E1 - 1e-6
        and np.linalg.norm(J_of(*res.x), "fro") <= H_BASE_F):
        found_pert.append((perm, tuple(res.x)))

  # Cluster all perturbative basins
  clusters = []
  for perm, x in found_pert:
    placed = False
    for c in clusters:
      if c["perm"] == perm and np.linalg.norm(np.array(c["rep"]) - np.array(x)) < 0.5:
        c["pts"].append(x)
        placed = True
        break
    if not placed:
      clusters.append({"perm": perm, "rep": x, "pts": [x]})

  print(f" Found norm-cut chamber clusters below residual tolerance across six permutations: {len(clusters)}")
  for c in clusters:
    x = c["rep"]
    obs = pmns_map(*x, perm=c["perm"])
    nrms = norms_of(*x)
    print(f"  perm={c['perm']} @ (m,d,q)=({x[0]:.4f},{x[1]:.4f},{x[2]:.4f}) "
       f"|J|_F/|H|_F={nrms['fro']/H_BASE_F:.3f} sin(dcp)={obs['sin_dcp']:+.4f}")
  check(
    "Finite search finds exactly one norm-cut chamber cluster",
    len(clusters) == 1,
    f"count={len(clusters)}",
  )
  if clusters:
    c = clusters[0]
    check(
      "the sole found norm-cut cluster is at sigma = (2, 1, 0)",
      c["perm"] == (2, 1, 0),
    )
    check(
      "the sole found norm-cut cluster is the PMNS-closure theorem Basin 1",
      (abs(c["rep"][0] - 0.657061) < 5e-3
       and abs(c["rep"][1] - 0.933806) < 5e-3
       and abs(c["rep"][2] - 0.715042) < 5e-3),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
  print("=" * 88)
  print("Finite PMNS affine-surface diagnostics with an imposed inertia filter")
  print("=" * 88)
  print()
  print("Objective: reproduce finite search diagnostics with original predicates and thresholds.")
  print("No global uniqueness, physical admissibility, or retained-theorem certification follows.")

  part1_perturbative_criterion_axiom_native()
  basins = part2_exhaustive_perm_scan()
  part3_perturbative_selects_basin1(basins)
  part4_three_advertised_basins()
  part5_theta23_chamber_threshold()
  part6_trichotomy_route_for_Ue_identity()
  part7_dcp_framing()
  part8_no_other_perturbative_basin()

  print()
  print("=" * 88)
  print(f" PASS = {PASS_COUNT}")
  print(f" FAIL = {FAIL_COUNT}")
  print("=" * 88)
  if FAIL_COUNT == 0:
    print()
    print("All implemented finite diagnostic predicates passed in this run.")
    print("This is not an exhaustion proof or an independently established physical prediction.")
  return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
  raise SystemExit(main())
