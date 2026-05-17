# Block 17 Report — gauge-vacuum plaquette residual environment finite-box stripping uniqueness

**Branch:** `physics-loop/gvp-residual-environment-identification-block17-2026-05-17`
**Target row:** `gauge_vacuum_plaquette_residual_environment_identification_theorem_note`
(637 desc, `audited_conditional`, class F renaming)
**Status delivered:** scope-bounded positive narrow theorem
(`bounded_theorem`, class-A finite-dimensional algebra) on the
*algebraic uniqueness* of the stripped residual factor on the finite
character-basis truncation. Parent `audited_conditional` row **not**
promoted; the all-weight identification gate remains explicit.

## What landed

1. **Source theorem note:**
   `docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_FINITE_BOX_STRIPPING_UNIQUENESS_NARROW_NOTE_2026-05-17.md`
   Positive narrow theorem: at finite-box scope `0 <= p,q <= NMAX`, the
   source-sector decomposition `(D|_B)` algebraically inverts to a
   *unique* stripped residual factor `(S)`, because both
   `exp[(beta/2) J|_B]` and `D_beta^loc|_B` are strictly positive (hence
   invertible) on the finite character-basis truncation. Five
   conclusions (U1)-(U5): half-slice multiplier invertibility, local-
   factor invertibility, stripping uniqueness, structural-class
   transport, and finite-box agreement with the bounded companion's
   canonical Wilson `rho_(p,q)(6)` coefficients.

2. **Paired runner:**
   `scripts/frontier_gauge_vacuum_plaquette_residual_environment_finite_box_stripping_uniqueness_narrow.py`
   `THEOREM PASS=6 SUPPORT=3 FAIL=0`. Verifies invertibility certificates
   (`||M M^{-1} - I|| ~ 4e-64`, `||D D^{-1} - I|| ~ 8e-62`), round-trip
   identity on two distinct positive diagonal candidate residuals
   (`~5e-51` worst error), structural-class transport (`~5e-51` worst
   error), and bounded-companion cross-check on `rho_(p,q)(6)`
   (`~5e-51`). Uses mpmath at `dps = 60` because the local Wilson factor
   has condition number `~10^13` even at this modest finite box.

3. **Cached output:**
   `logs/runner-cache/frontier_gauge_vacuum_plaquette_residual_environment_finite_box_stripping_uniqueness_narrow.txt`

4. **Block artifacts** (this directory):
   - `V1_V5_SCRATCH.md` — distinct-angle scratch (V1-V4 rejected, V5 chosen)
   - `BLOCK_REPORT.md` — this file

## V1-V5 chosen angle

- V1-V4 rejected: each would either attempt to close the explicit
  parent open gate (all-weight identification, analytic `P(6)` — both
  too big for 90 min under A_min) or duplicate prior cycles (iter b7
  witness replacement, block 13 U(1) sign-alternation).
- **V5 (chosen):** prove the algebraic uniqueness of the stripped
  residual factor on the finite box via invertibility of the half-slice
  multiplier and the local Wilson factor, plus structural-class
  transport and a numerical cross-check against the bounded companion's
  canonical Wilson coefficients.

## Distinct sub-problem (block-lane independence)

This block is on the **algebraic uniqueness** of the stripped finite-box
residual factor, distinct from:
- **Block 03 / iter b7 (PR #1217):** replaced the parent runner's
  hand-picked witness sequence with canonical Wilson single-link
  boundary character coefficients on the finite box. That was
  numerical witness sourcing; this block is a structural uniqueness
  lemma about the decomposition `(D)` itself.
- **Block 13 (PR #1444):** U(1) sign-alternation of `c_{2k}` for
  `K_1(t) = log I_0(t)` via the Bessel Riccati recurrence, on the
  *infinite-hierarchy obstruction* parent row, not this row.
- **Parent all-weight gate:** identification of `R_beta^env` with
  `C_(Z_beta^env)` at all weights — explicitly the parent's open gate
  and outside this block's scope.

## Hard rules compliance

- A_min only: ingredients (`J`, `D_beta^loc`, `a_(p,q)(beta)`,
  `rho_(p,q)(6)`) imported from cited audited authorities (transfer-
  operator / character-recurrence note retained, local-environment
  factorization theorem retained-bounded, bounded coefficient companion
  retained-bounded via two-integrator cross-check). No new primitives.
- Source-only PR: theorem note + runner + cache + block artifacts only.
- No CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS, DERIVATION_VALIDATION_MAP,
  audit-data, README, or lane-registry touches.
- No main push, no merge.

## Honest scope

- Parent row `gauge_vacuum_plaquette_residual_environment_identification_theorem_note`
  remains `audited_conditional`.
- The parent's explicit open gates remain:
  (1) all-weight identification of `R_beta^env` with the compressed
      unmarked spatial Wilson environment operator;
  (2) full unmarked spatial Wilson environment tensor-transfer / Perron
      closure;
  (3) analytic closure of canonical `P(6)`.
- The new narrow uniqueness theorem closes the specific renaming defect
  identified by the auditor *at finite-box scope only*: the parent's
  stripped residual is no longer just "a named positive diagonal central
  conjugation-symmetric operator" — it is *the unique* algebraic
  stripping of the source-sector decomposition `(D|_B)`, and it
  numerically agrees with the bounded companion's canonical Wilson
  single-link boundary character coefficients to mpmath precision.
- The note explicitly does NOT promote the parent row or claim
  retained-grade status.
