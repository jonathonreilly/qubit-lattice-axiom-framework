Reviewer model: claude-opus-5-5

# LCONV55 — Is the multiscale small-field chain convex? (node A residual (LC°))

UTC start: 2026-10-29T01:21:17Z
Author: Opus 5.5 worker (claude-opus-5-5). Append-only. No git. Writes only this file and `checks/lc55_*`.

## PRE-STATED (written before any derivation)

Targets:
- T1 (multiscale claim). Decide whether the lowest Hessian eigenvalue of the gauge-fixed soft-scheme
  chain action, on the MULTISCALE small-field region (smallness at every level), is bounded below by
  c * (free Laplacian) with c > 0 uniform in k and T. Identify which constraint (level, threshold)
  removes the lattice Nielsen-Olesen (NO) negative mode, and whether the lane's actual thresholds
  (epsilon_1 et al., in the order SMALLNESS_DAG.md gives) are small enough.
- T2 (coordinates). Decide whether convexity (LC-2') is provable in the exponential/axial coordinates
  of the small-field core, or whether background-covariant coordinates around the critical tower
  (BFT-0/1/2 on C_glob, GV55.md) do better.
- T3 (LC-3'). State the large-field Peierls bound node A needs and what RLARGE / HW / PLD supply.
- T4. If convexity fails on node A's region, give the smallest modification of the region or of the
  tilt that restores it, and check whether node A's consumers tolerate it.

What would count as a refutation of the multiscale claim ("smallness at every level restores convexity"):
- an explicit configuration inside the multiscale small-field region (all levels' constraints satisfied
  at the lane's thresholds) with a Hessian direction of negative Rayleigh quotient, or a Rayleigh quotient
  that is not bounded below by a positive constant times the free Laplacian uniformly in k, T;
- or an exact scaling argument that the NO threshold is not crossed by the constraints at any level
  (i.e. the constraint at every level permits a background strength above the NO threshold for some
  mode the constraint does not control).
What would count as CONFIRMING it: an exact (rational/symbolic) lower bound on the Hessian quadratic
form, valid on the whole multiscale region at the lane's thresholds, with the constraint that does the
work identified; plus a designed-FAIL control (a configuration that violates exactly that constraint)
in which the negative mode reappears.
A precise statement of what is missing counts as a first-class result if neither can be settled.

