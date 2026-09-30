# T01 pre-registration (written before any simulation was run)

Wall T01: no formation order / rate / unit for "records form".
Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check only).

## What is being decided

The lane says the wall is "priced": it equals adopting one formation clause.
That reading has two ways to be wrong.

* (W-a) MISFRAMED for local physics: the clause dependence found on finite
  windows (plaquette, 2x3, cube) is a finite-window artefact. If so, all
  covariant clauses would give the same local record statistics on Z^3 and
  nothing would have to be priced for local physics.
* (W-b) MISFRAMED for phases: the clause changes the finished statistics but
  never the phase diagram (the ordered/disordered threshold), so the price
  would only be a UV nuisance.

The test settles both on a 3D periodic torus, exactly and by Monte Carlo.

## Setup (fixed before running)

* Rule: six-axis menu {+x,-x,+y,-y,+z,-z}; pair weight phi(a,b) = p (equal),
  q (opposite), r (orthogonal, 4 of them). A forming site with recorded
  neighbours draws a with probability proportional to prod_y phi(a, v_y);
  uniform if no neighbour is recorded. (The lane's rule; landed in
  docs/ADMISSIBILITY_RULE_HOW_RECORDS_FORM_...2026-09-20.md, Premises.)
* Clauses (all covariant, local, value-blind, single-site):
  U  : hazard 1 (state-blind; iid priorities)
  E  : hazard (1+k)^2, k = number of already recorded neighbours ("eager")
  A  : hazard 1/(1+k) ("averse")
  S  : static Gibbs law of the same rule (heat-bath), as comparator only.
* Lattice: d = 3 torus, L in {4, 6, 8, 12, 16}; weights (3,1,2) for local
  statistics; (p,1,2) with p in a scan for the threshold.

## Observables

* a1 = P(equal axis) on nearest-neighbour edges (per-sample average over all edges).
* a_opp, a_orth on edges; a_diag = P(equal axis) on face-diagonal pairs.
* Q = <|m|^4>/<|m|^2>^2 with m = mean of the unit vectors of the records
  (Gaussian disordered limit 5/3, fully ordered limit 1). Its L-crossing gives
  the ordering threshold p_c.
* s = mean over sites of [log gamma(v_x | 6 nbrs) + H(gamma(.|6 nbrs))], gamma the
  rule's full conditional (the static specification). s = 0 exactly for S.

## Validation before any claim (a failing validation voids the run)

V1. Monte Carlo of U on the open 4-cycle (plaquette) at (3,1,2) reproduces the
    exact order-averaged edge-agreement probability (exact enumeration over
    24 orders) within 4 standard errors; same for E and A with exact
    race-order probabilities.
V2. The static heat-bath reproduces s = 0 within 4 SE, and its Q-crossing for
    (p,1,2) lies in (3.5, 3.8) (the located value in the lane is 3.6-3.7).

## Readings

* Local test (W-a), at (3,1,2), d=3:
  PASS (clause dependence is real in the thermodynamic limit; price stands):
    |a1(U) - a1(E)| >= 5 SE and |a1(U) - a1(A)| >= 5 SE at L = 12, with the
    same sign as at L = 6 and magnitude at L = 12 at least 0.5 of that at L = 6.
  FAIL (finite-window artefact => MISFRAMED for local physics):
    any of those differences < 3 SE at L = 12, or shrinking below 0.25 of the
    L = 6 value.
  Also record a1(S) versus a1(U): whether the static law is separated from the
  blind clause in the bulk (expected yes: s(U) != 0).
* Phase test (W-b): threshold p_c(U), p_c(E), p_c(A) from Q crossings (L = 8, 12, 16).
  PASS (the clause moves the phase boundary): p_c differ pairwise by >= 0.5 in p
    (on the (p,1,2) line) beyond the crossing resolution (bootstrap SE).
  FAIL (clause-independent threshold within resolution): pairwise differences < 0.25.
  In between: report as inconclusive.

## Exact side-checks (Python, fractions)

X1. Plaquette: the 24 orders give 4 distinct laws; the value-blind clocks U, E, A
    are 3-parameter barycentric mixtures of these 4 (the whole clause freedom
    on the plaquette is the law of the induced orientation class).
X2. Blind lemma: for hazard f(k), path-of-3 (z-x-y): P(x before y) = 1/3 + (1/3) f1/(f0+f1)
    = 1/2 iff f1 = f0; with the 2-neighbour cases (star/cycle windows) f2 = f0.
    Claim: an order law that is the same whether or not extra sites are present
    (projective order law) forces a constant hazard.
X3. The ten orbits of NN occupancy patterns under the 24 proper cubic rotations
    (count = 10) match the lane's "six-dimensional cone on ten orbits".
