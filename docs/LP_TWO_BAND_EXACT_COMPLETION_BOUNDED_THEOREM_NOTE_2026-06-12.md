# Full Two-Band Peierls Perturbation Agrees With the Landed Small-B Finite-Difference Response Off m = 0 (Fixed B = 1e-3 Estimator, Fixed Tolerances; Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_lp_two_band_exact_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_lp_two_band_exact_2026_06_12.txt`
**Status:** source proposal; the audit lane grades.
**Status authority:** independent audit lane. This source note does not set or predict an audit outcome and does not edit audit-owned registry, ledger, queue, or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency. The independent audit lane owns status.

## Claim

On the finite free staggered `d = 2` Harper cell used by the landed LP-failure
runner, the native second-order Peierls perturbation calculation agrees, at the fixed
`2e-2` tolerance and with the `B = 1e-3` finite-difference estimator (its
finite-`B` floor disclosed below), with the small-`B` Hofstadter response at the
fixed landed boundary probe
`mu = 1.7086`, for `m = 0, 0.2, 0.3, 0.5`.  The calculation is finite
dimensional: it expands the Peierls phase directly as
`H(B) = H0 + B H1 + B^2 H2 + O(B^3)` and evaluates the grand-potential
curvature with the full two-band sum, including the interband `H1` matrix
elements.

## What Changed Relative To The LP-Failure Note

The predecessor established the anchor surface:

- the intraband Landau-Peierls boundary matches at `m = 0` within `2e-2`
  (a predecessor curvature-form statement; NOT re-asserted for the PT split here);
- the same intraband identification fails off `m = 0`, with landed deviations
  `0.042`, `0.046`, and `0.201` on the named rows.

Those landed deviations are carried as printed provenance (not gates — the LP
curvature-form split and the velocity-gauge PT split below are **different
decompositions** of the same response and are not compared term-by-term). The
computed opening gate is a `B`-step-halving control on the exact reference,
which **discloses the landed estimator's finite-`B` floor**: the non-flux-
quantized small-`B` second difference drifts `5.6e-3` (relative, at `m = 0.2`)
between `B` and `B/2`, directed toward the PT value — an order of magnitude
below the landed intraband failures, gated under a fixed `1e-2` floor. A
flux-quantized reference is the named follow-on (Landau-reorganization-dominated
and unconverged at accessible sizes `LX <= 240`, so it cannot gate here). The runner then tests the corrected object: the complete second-order
Peierls response of the finite one-particle matrix.

**The structure of the completion is a near-cancellation**: at every tested mass
the intraband and interband PT terms are each more than `5x` the net response
(gated; at `m = 0.5` they are `+3.18` and `-3.15` against a net `0.031`), and the
interband magnitude grows strictly with mass (gated). The full sum matches the
exact reference at relative deviation `<= 7.9e-3` at every mass — including the
masses where the intraband-only form failed at `0.04-0.20`. The interband
contribution is gated nontrivial at `m = 0.5`, so the positive result is not a
silent replay of the intraband kernel.

## Scope

Free one-particle matrices only; no Fock-space construction.  Finite magnetic
cell `Q = 24`, `Ly = 2`, staggered mass `m (-1)^(x+y)`, nearest-neighbor hopping,
and grand-potential response at finite temperature.  This is a finite-lattice
small-`B` response statement at a fixed boundary probe, not a continuum theorem,
not a full boundary-root theorem, and not a flow claim.

No new axiom, primitive, measure, or weight is introduced.  The audit lane grades.

## Dependencies

- [`LP_IDENTIFICATION_FAILS_OFF_M0_BOUNDED_THEOREM_NOTE_2026-06-12.md`](LP_IDENTIFICATION_FAILS_OFF_M0_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the landed Harper-cell anchor, finite-field boundary probe, and off-`m = 0`
  intraband-LP deviation table used here as comparison context.
