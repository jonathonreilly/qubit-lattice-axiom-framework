# T73 pre-registration (written before any test script was run)

Attacker: Claude Sonnet 5.5 (same family as the supervisor; same-family check).

## Question the test decides

Wall T73 says: the axioms fix no entropy and the five candidates disagree.
Two hypotheses:

- H_canon: the axioms plus the natural symmetric reading pick out one
  record-ensemble entropy, up to a small spread, so the candidates that are
  functionals of the record ensemble (flat count S0 = ln N, process-weighted
  S1) are nearly the same number and the same scaling class. The wall would
  then be a bookkeeping gap.
- H_measure: on ONE fixed support (the same admissible frozen sets), the
  outcome measure alone moves the entropy across scaling classes (log, boundary,
  volume) and across coefficients. The wall is then equivalent to the
  unsupplied formation measure (site, order, rate), not to a choice among five
  rival derivations.

## System (fixed support)

Crowding rule m = 0 of probe 19: an empty site may form a record iff none of its
nearest neighbours is recorded. Frozen sets = maximal independent sets (MIS) of
the grid graph. Sealed boxes: d = 1 chains L <= 24; d = 2 boxes L = 2..5 (L = 6 if
time allows), open boundary. Records permanent, at most one per site.

## Test A (measure-free vs process entropy; exact)

Compute N (check against probe 19 table 2, 10, 42, 358 for L = 2..5), S0 = ln N,
and for the uniform random-order sequential process (RSA: each step picks one
eligible site uniformly) the exact Renyi entropies S1, S2, S_inf of the frozen
state. Also a one-parameter local covariant family: pick an eligible site with
weight w^(number of eligible neighbours of that site), w in {0.1, 0.3, 1, 3, 10}.

- H_canon reading: S1/S0 >= 0.95 for all L >= 4 (d = 2) and for all L >= 10
  (d = 1), and varying w moves S1/S0 by less than 5 percent.
- H_measure reading (expected): S1/S0 clearly below 1 (Dosli\'c et al.), and
  (S0 - S1)/L in d = 1 tends to a positive constant (the two measures are
  exponentially far apart in volume), and the w family spreads S1/S0 by more
  than 10 percent.

## Test B (measure dials the scaling class on the same support; 2D, L = 3..10)

Three axiom-compliant permanent-record formation laws on the same sealed L x L
box with the same support (every output must be a MIS, verified exhaustively for
L <= 7):

- V (volume law): uniform random-order sequential formation.
- S (seed law): deterministic raster formation started at a uniformly random
  site and a uniformly random box symmetry; entropy computed exactly by
  enumerating the L^2 x 8 start choices.
- R (ring law): the boundary ring is filled first by a renewal measure with
  weight w^(number of gap-3) (exact ring enumeration), then the interior is
  filled by a fixed raster order; the outcome measure is the pushed-forward ring
  measure. The state contains the ring, so the map is injective and
  H(final) = H(ring).

PASS (H_measure): S_V grows like L^2 (linear fit of S_V/L^2 flat and > 0.1 at
L = 4, 5), S_S <= ln(8 L^2) (log class), S_R = c(w) * (ring length) with c(w)
continuous, spanning (0, ln 1.3247 = 0.2812) per ring site, so c = 1/4 is
reached by a specific w*. All three have the same support.
FAIL (H_canon): the symmetric/local/permanent constraints exclude law R or law S
(some output not a MIS), or S_V is not in the volume class.

## What each outcome would mean

- PASS on A and B: T73 is priced at the formation-measure gate (site/order/rate
  plus odds), because entropy of the ensemble is a functional of (support, measure,
  partition) and the axioms give only the support; the lane's five-way
  disagreement is measure/state/action dependence, not five rival derivations.
- FAIL on A (S1/S0 ~ 1): the flat count would be a good proxy for the
  process entropy and the wall would shrink to a scale question.
- FAIL on B: the measure is constrained by the axioms' symmetry more than
  expected, and T73 is a real wall on its own.

Not tested (stated up front): entanglement (candidate d) and Wald (candidate e)
are functionals of a wave state and an action; they are compared to the rest
only by type, not numerically. The rank fraction is not an entropy (proved,
AREA_LAW_PRIMITIVE_EDGE_ENTROPY_SELECTOR_NO_GO_NOTE_2026-04-25.md:36-53).
