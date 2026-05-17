# Block 19 Report: gvp-spatial-environment-character-measure

**Date:** 2026-05-17
**Worktree:** `/private/tmp/physics-loop-2026-05-17/block19-gvp-spatial-environment-character-measure`
**Branch:** `physics-loop/gvp-spatial-environment-character-measure-block19-2026-05-17`
**Lane:** gauge_vacuum_plaquette (continues blocks 13, 17 in this campaign).
**Target row:** `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note`
**Audit state of target:** `audited_conditional` (class F renaming), 639
descendants, load_bearing_score 15.902, criticality critical.

## Audit load-bearing step closed at finite-box scope

> The residual source-sector environment operator is exactly convolution by
> the normalized boundary class function, i.e. `R_beta^env = C_(Z_beta^env)`.
>
> -- audit load_bearing_step (class F)

The auditor's `notes_for_re_audit_if_any` flagged:

> supply a retained-grade derivation or runner-backed certificate identifying
> the full unmarked spatial Wilson residual compression R_beta^env with
> normalized convolution by Z_beta^env, not only the single-link bounded
> witness.

The full multi-link Wilson tensor-transfer derivation is the parent-of-parent
named open gate
(`gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note`)
and explicitly out of scope at 90 min.

## V1-V5 outcome

- V1 (all-weight Wilson tensor-transfer): out of scope, multi-decade open
  problem. SKIP.
- V2 (U(1) restriction): duplicates block 13 spirit. SKIP.
- V3 (third independent integrator): numerical confirmation churn,
  duplicates iter b7. SKIP.
- V4 (sympy NMAX > 3 swap-commutator): structural repeat of block 17. SKIP.
- V5 (finite-box inverse Peter-Weyl convolution-realization uniqueness):
  the symmetric counterpart of block 17 in the character-measure layer.
  **THIS IS THE BUILT ANGLE.**

V1-V5 reasoning is detailed in `V1_V5_SCRATCH.md`.

## What was built (positive narrow theorem)

A bounded narrow positive theorem at finite-box scope `0 <= p, q <= NMAX = 4`,
on the marked-plaquette SU(3) class-function sector:

- (M1) existence of the finite-box truncated boundary class function
  `Z_beta^env|_B` defined by
  `Z_beta^env|_B(W) := z_(0,0)^env(beta) sum_{(p,q) in B}
                       d_(p,q) rho_(p,q) chi_(p,q)(W)`;
- (M2) forward convolution-realization at finite-box scope:
  `R_beta^env|_B = C_(Z_beta^env|_B)|_B`;
- (M3) **inverse Peter-Weyl finite-box uniqueness**: the normalized
  finite-box truncated central class function realizing `R_beta^env|_B`
  as a convolution operator is unique;
- (M4) joint uniqueness at finite-box scope of both sides of the parent's
  identification `R_beta^env|_B = C_(Z_beta^env|_B)|_B` — left side via
  block 17 stripping-uniqueness, right side via (M3) inverse Peter-Weyl
  uniqueness;
- (M5) witness-source consistency: instantiating
  `rho_(p,q) := rho_(p,q)(6)` from the bounded companion's canonical
  single-link Wilson character integrals gives the canonical Wilson
  boundary class function as the explicit unique finite-box realization;
- (M6) sympy NMAX_SYM = 2 symbolic verification of (M3) and the
  normalized-truncation uniqueness consequence.

The narrow note's primary content is (M3): the **inverse-direction**
convolution-realization uniqueness, which the audit's load-bearing class-F
step requires for the parent's Theorem 3 to identify *unique* objects on
both sides rather than be a renaming.

## Relation to block 17

| Side of (E) | Uniqueness theorem | Closes |
|---|---|---|
| left side `R_beta^env|_B` | block 17 stripping-uniqueness | "operator is unique" |
| right side `C_(Z_beta^env)|_B` (this block) | inverse Peter-Weyl uniqueness (M3) | "measure is unique" |

Block 17 closed the forward direction (from the source-sector decomposition
to the unique residual factor). Block 19 closes the inverse direction
(from the unique residual factor to the unique normalized boundary class
function realizing it as convolution). Together they remove the class-F
renaming defect at finite-box scope.

## Deliverables

- Source note:
  `docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_FINITE_BOX_CONVOLUTION_REALIZATION_UNIQUENESS_NARROW_NOTE_2026-05-17.md`
- Runner:
  `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_finite_box_convolution_realization_uniqueness_narrow.py`
- Runner cache:
  `logs/runner-cache/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_finite_box_convolution_realization_uniqueness_narrow.txt`
- Block artifacts:
  `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block19/V1_V5_SCRATCH.md`
  + this report.

Runner result: `THEOREM PASS=13 FAIL=0`.

## What this does NOT close

- The full multi-link unmarked spatial Wilson environment tensor-transfer
  at all character weights (parent-of-parent open gate).
- Analytic closure of canonical `P(6)`.
- The parent spatial-environment character-measure note's all-weight
  scope (remains `audited_conditional`).
- The parent residual-environment identification note's all-weight scope
  (sister parent remains `audited_conditional`).
- Repo-wide repinning of the canonical plaquette.

## Hard rules check

- A_min only: consumes retained transfer-operator / character-recurrence
  J, retained-bounded local-environment factorization D_beta^loc, the
  bounded companion's runner-computed rho_(p,q)(6), and block 17's
  stripping-uniqueness as named scoped inputs. No new framework primitives.
- Source-only PR: only added docs (source note + block artifacts),
  scripts/ (runner), and logs/runner-cache/ (runner output). No
  CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS, DERIVATION_VALIDATION_MAP,
  audit-data, README, or lane-registry touches.
- Status authority: independent audit lane only; note labels itself
  bounded_theorem with claim scope explicit.
- No main push, no merge.

## Honest status

The narrow note closes the inverse-Peter-Weyl finite-box uniqueness of the
boundary class function `Z_beta^env|_B` realizing the (block-17-unique)
residual factor `R_beta^env|_B` as a normalized convolution operator on
the finite weight box `0 <= p, q <= 4`. Combined with block 17 (forward
direction stripping uniqueness), this closes the parent's audited
class-F renaming defect at finite-box scope: both objects in the named
identification `R_beta^env = C_(Z_beta^env)` are now uniquely determined at
finite-box scope. The full all-weight identification continues to depend on
the open multi-link Wilson environment tensor-transfer parent-of-parent
gate. The parent note's audit state (audited_conditional) at full
all-weight scope is unchanged by this narrow source proposal.
