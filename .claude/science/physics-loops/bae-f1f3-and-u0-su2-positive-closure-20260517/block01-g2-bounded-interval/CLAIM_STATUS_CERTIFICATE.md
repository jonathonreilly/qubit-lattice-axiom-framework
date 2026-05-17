# CLAIM STATUS CERTIFICATE — Block 01 (g_2(v) bounded interval given u_0 import)

**Date:** 2026-05-17
**Cycle:** 1 / Agent C of `bae-f1f3-and-u0-su2-positive-closure-20260517` campaign
**Block:** 01-g2-bounded-interval
**Branch:** `physics-loop/g2-bounded-interval-block01-20260517`
**Slug:** `bae-f1f3-and-u0-su2-positive-closure-20260517` (cycle 1 / agent C)
**Primary artifact:** `docs/G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`
**Primary runner:** `scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`

## Status fields

```yaml
actual_current_surface_status: bounded_theorem (narrow Pattern A rescope) with named external admission for u_0(SU(2))
target_claim_type: bounded_theorem
conditional_surface_status: bounded interval [0.65939, 0.68283] conditional on literature u_0(SU(2)) in [0.96, 0.98]
hypothetical_axiom_status: null
admitted_observation_status: literature u_0(SU(2)) import (Trottier hep-lat/9803024 + Munster) named-external-admission; ln(M_Pl/v) = 38.44 named-external-admission
claim_type_reason: |
  Pattern A narrow rescope of the EW_COUPLING_DERIVATION_NOTE Part 3
  BOUNDED status, isolating ONLY the algebraic-substitution implication
  conditional on the literature import for u_0(SU(2)). Five
  retained / retained_bounded primitives (b_2 = 19/6, native SU(2),
  g_2^2 |_lattice = 1/4, Wilson canonical normalization, vertex-power
  tadpole identity) plus two named external admissions (u_0 interval,
  scale ratio) substitute into the 1-loop running surface to give a
  closed-form bounded interval. No PDG g_2(v) value consumed; no fitted
  selector; no admitted lattice plaquette evaluation. The literature
  u_0(SU(2)) import is explicitly classified as NAMED EXTERNAL
  ADMISSION per the legitimate `import -> bounded retained -> retire
  import` path. The R1 residual (framework-internal derivation of
  numerical u_0(SU(2))) remains OPEN.
audit_required_before_effective_retained: true
bare_retained_allowed: false
proposal_allowed: true
proposal_allowed_reason: |
  Per the V1-V5 Promotion Value Gate (REVIEW_HISTORY): the bounded
  interval is a genuine NEW algebraic substitution implication not
  derivable from existing retained primitives alone (the literature
  u_0 import is the load-bearing new content for the v-scale interval).
  The Pattern A narrow rescope mirrors `CKM_MAGNITUDES_STRUCTURAL_COUNTS_NARROW`
  template formatting and inherits the exact substitution-only proof
  class. The named external admission is explicitly labeled and the
  R1 derivation gap is preserved as the open residual.
```

## 7-criterion bounded-theorem certificate

| # | Criterion | Pass? | Notes |
|---|---|---|---|
| 1 | `proposal_allowed: true` | **YES** | Pattern A narrow rescope of EW_COUPLING_DERIVATION Part 3 with named external admission |
| 2 | No open imports masquerading as retained | **YES** | Literature `u_0(SU(2))` import explicitly classified as NAMED EXTERNAL ADMISSION; scale ratio admitted as named admission |
| 3 | No load-bearing observed/fitted/admitted unit conventions | **YES** | Wilson normalization is retained_bounded; tadpole identity is retained; no PDG `g_2(v)` consumed |
| 4 | Every load-bearing dep retained | **YES** | All 5 cited upstreams verified `retained` or `retained_bounded` on live ledger 2026-05-17 |
| 5 | Runner checks dep classes | **YES** | sympy exact verification of (R1), (R3), (M1), (G1)-(G5), (C1)-(C5); PASS=18 FAIL=0 |
| 6 | Review-loop disposition | **PASS** (self-review) | Recorded in `REVIEW_HISTORY.md` |
| 7 | PR body says independent audit required | **YES** | Note carries `**Status authority:** independent audit lane only` |

**Result:** Honest tier: **bounded_theorem (Pattern A narrow rescope) with named external admission**.

## Promotion Value Gate (V1-V5)

Recorded in `REVIEW_HISTORY.md` §1. Disposition: **PASS**.

## Cluster-cap / volume-cap

- Volume cap: 1 of 5 used (this campaign cycle 1 agent C).
- Cluster cap (`g_2_*` / `ew_coupling_*` family): 1 of 2 used.
- Corollary churn: first cycle of this campaign; not applicable yet.

## Imports retired

None. This cycle classifies the literature `u_0(SU(2))` import as a
NAMED EXTERNAL ADMISSION (legitimate import → bounded retained → retire
import path). The retirement step (deriving numerical `u_0(SU(2))` from
retained primitives) remains the open R1 residual.

## Imports newly exposed

| Item | Class | Notes |
|---|---|---|
| `u_0(SU(2)) ∈ [0.96, 0.98]` | named external admission | Trottier hep-lat/9803024 (1998); Münster strong-coupling expansion. Explicitly labeled in note §X1. |
| `ln(M_Pl / v) = 38.44` | named external admission | Standard scale-ratio fact; framework's retained v = 246.28 GeV + standard M_Pl ~ 1.22e19 GeV fix this. Explicitly labeled in note §X6. |
| 1-loop Peskin-Schroeder RGE form | implicit via retained `SU2_WEAK_BETA_COEFFICIENT_NARROW` (X4 of that note) | Standard QFT 1-loop running equation. Not a new admission for this note. |

## Honest classification

**Pattern A narrow bounded theorem with named external admission:**
- Substitutes 5 retained / retained_bounded primitives plus 2 named
  external admissions into the 1-loop Peskin-Schroeder running equation
- Yields the bounded interval `g_2(v=246 GeV) ∈ [0.65939, 0.68283]`
- Endpoints verified at 30-decimal-digit sympy precision
- Monotonicity exact: `d/du_0 [1/α_2(v)] = 32 π u_0 > 0`
- Endpoint reversal forced (g_2 decreasing in u_0)
- Interval brackets observed `g_2(v) = 0.646` within ~2% on g_lo side
  (recorded as runner context-only check, NOT load-bearing on closure)

This is **NOT** a closure of `EW_COUPLING_DERIVATION_NOTE` Part 3
BOUNDED status and **NOT** a derivation of `u_0(SU(2))` numerical.
It is honest bounded-interval rescope content with explicit roadmap
for the residual R1 (framework-internal `u_0(SU(2))` derivation).

## Repo-weaving recommendation (for later integration, NOT executed in this PR)

For the later review/integration process:

- Reference this note in `EW_COUPLING_DERIVATION_NOTE.md` Part 3 as a
  Pattern A narrow rescope giving the explicit bounded interval
  conditional on literature import.
- Reference this note in `G_WEAK_FROM_FRAMEWORK_STRETCH_ATTEMPT_NOTE_2026-05-03.md`
  as the v-scale narrow rescope inheriting the same lattice-scale
  anchor `g_2² |_lattice = 1/4`.
- After audit ratification: the bounded-interval claim graduates to
  retained_bounded; the named external admission `(X1)` remains open
  until R1 closes.
- The post-R1-closure follow-up note would retire the literature
  import and convert the interval into a derived point value; this
  cycle does NOT attempt that retirement.

## Stop conditions checked

- Runtime exhaustion: no
- Volume cap: no (1 of 5)
- Cluster cap: no (1 of 2 in this family)
- Corollary exhaustion: no (first cycle of this campaign)
- Value-gate exhaustion: no (V1-V5 PASS)
- Tooling: no

## Next action

Commit + push + open PR. Title: `[physics-loop] g2-bounded — bounded
theorem (g_2(v) interval given u_0 import)`. Body documents V1-V5,
named external admission classification, runner PASS=18/0, and the
open R1 residual.
