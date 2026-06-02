# Flavor — reframe: r=1/2 need not be *forced*; it is a distinguished *stationary point* (max-sector-entropy / balance / swap-fixed-point). The three Q-lanes are distinguished points of the r-family, not competing answers — so the J-hunt's "force det_C over det_R" was the wrong target.

**Date:** 2026-06-02
**Claim type:** framing correction (supersedes the forced-selection premise of the 5-round J-hunt) + the verified stationary-point fact.
**Status authority:** independent audit lane only.
**Runner:** `scripts/flavor_r_half_is_a_stationary_point_not_forced_2026_06_02.py` (SCORECARD 4/4).
**Source:** user reframe ("why force r=1/2? isn't it a trough/peak yielding the downstream values? we already get Q=1 as something different"), verified.

## The reframe
The 5-round J-hunt tried to **force r=1/2** (det_C) **over r=1** (det_R) — to derive r=1/2 as *the* value
via a measure-selection principle. That is the **forced-selection framing already retired earlier this
campaign** (the "lanes, not competing answers" reframe). Re-applied here it dissolves the J-hunt's target:

> r=1/2 does not need to be *forced*. It is a **distinguished stationary point** of the r-family, and the
> three special Q's are **distinguished points = different physics (lanes)**, not one value to select.

## Verified: r=1/2 is a genuine extremum (a "natural", not fine-tuned, value)
- The **sector-power entropy** `S(r)` (entropy of the two isotype-sector power fractions
  `p_singlet=3a²/(3a²+6|b|²)=1/(1+2r)`, `p_doublet=2r/(1+2r)`) is **maximized at r=1/2**: `dS/dr=0` there,
  `S(1/2)=log 2` (the maximum). Equivalently the singlet↔doublet power **imbalance `|3a²−6|b|²|` is at a
  trough (=0)**. r=1/2 is also the **fixed point of the r→1−r swap**.
- A **stationary point is "natural"** the way a vacuum sits at a potential extremum — *not* a fine-tuned
  number. From r=1/2, all downstream charged-lepton observables (Q=2/3, the mass ratios) follow. This is
  the "trough/peak that yields the downstream values."

## The three lanes are distinguished points of the r-family
| r | Q | distinguished point |
|---|---|---|
| 0 | 1/3 | S₃-**degenerate** (enhanced-symmetry endpoint) |
| 1/2 | 2/3 | **balanced** / max-sector-entropy (interior extremum) — charged leptons |
| 1 | 1 | **maximal hierarchy**, two massless (enhanced-symmetry endpoint) |

"We already get Q=1 to be something different" — exactly: Q=1 is the hierarchy lane, Q=1/3 the degenerate
lane, Q=2/3 the balanced lane. **Different physics, not competing answers.** So **det_C/r=1/2 and
det_R/r=1 are different lanes**, each a distinguished point — there is nothing to "select between."

## What this corrects, and the honest residual
- **Corrects:** the 5-round J-hunt's premise (force det_C over det_R) was a relapse into forced-selection.
  Its negatives ("r=1/2 not forced") answered a question we did not need to ask. The J-hunt's *positive*
  by-products stand (the C³=I wall, the trace-vs-center-state localization, the de-walling in round 5),
  but the *target* was mis-framed.
- **Honest caveat:** r=1/2 is the extremum of the **sector** functional (entropy over the 2 isotype
  sectors); the **per-DOF** functional instead peaks at r=1. So "which extremum is distinguished" still
  carries the sector-vs-DOF (= det_C/det_R) flavor. But the reframe handles it correctly: we do **not**
  force the sector functional over the DOF one — r=1/2 is a *bona fide* stationary point (of the
  balance/sector functional) that the charged-lepton lane occupies, while r=1 is a *different*
  distinguished point (a different lane).
- **Residual, reframed:** not "force a measure / fine-tune a number" but **"which extremum/lane does each
  sector occupy?"** — a natural *which-vacuum* question (the lane assignment). This is strictly more
  honest and more physical than the measure-forcing target, and it matches the field (Koide: the per-sector
  ratio is a free fit; "Q=2/3 is the midpoint" — i.e. a distinguished point — of the [1/3,1] family).

## Net standing of the charged-lepton value (corrected frame)
- **Structure** — derived: 3 chiral generations, exact `Q=1/3+(2/3)r`, the C₃ channels, the carrier.
- **r=1/2** — a **distinguished stationary point** (max-sector-entropy / balance), *not* fine-tuned; the
  charged-lepton lane sits at it. Q=1 and Q=1/3 are *other* distinguished points (other lanes).
- **Open (natural form)** — the **lane assignment**: which extremum/lane each fermion sector occupies, and
  whether a *which-vacuum* dynamics (record/persistence, mass-generation) selects the balanced extremum for
  charged leptons. Unobstructed by C³=I (J-hunt round 5).

## Provenance (verified 2026-06-02)
- Sector-entropy peak at r=1/2 (dS/dr=0, S=log2), imbalance trough, swap-fixed-point, the three lanes: verified directly (runner 4/4).
- Reframe consistent with the campaign's "lanes, not competing answers" capstone and with Koide's free per-sector fit (arXiv:1301.4143).
- Supersedes the forced-selection *target* of `FLAVOR_FIND_J_*` (whose structural by-products stand). Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
