# Route 2 Tensorized Schur/Dirichlet Primitive

**Status:** bounded - tensorized Schur/Dirichlet primitive candidate
**Date:** 2026-04-14  
**Purpose:** build the smallest tensorized Schur/Dirichlet boundary primitive
compatible with the current exact scalar Schur backbone and the existing
bounded two-channel tensor prototype

## Verdict

The exact tensor carrier is still absent on the current support stack.

But the current Route-2 frontier is now strong enough to define a genuine
tensorized Schur/Dirichlet primitive candidate that does **not** repeat the
no-go:

- exact scalar Schur boundary action
- exact scalar support endpoint law on `A1`
- bounded bright tensor prototype on the two aligned channels
  - `E_x`
  - `T1x`

The smallest tensor extension that survives the current evidence is therefore
not a new bulk metric ansatz. It is a **source-centered two-channel boundary
completion** attached to the exact scalar Schur action.

## Cited scalar backbone (tier inherited; see §Upstream-tier accounting below)

The route-2 scalar backbone, with **cited** upstream tiers (per the
2026-05-17 ledger snapshot, the composite is at most
`audited_conditional` via the cap-uniqueness companion and `unaudited`
via the anomaly-forced-time companion):

- cited `S^3` spatial composite (`audited_clean` via boundary-link
  companion; `audited_conditional` via cap-uniqueness companion)
- cited anomaly-forced time with `d_t = 1` (companion `unaudited`;
  admissions (i)-(iv) per the upstream
  [F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md))
- bounded composite background `PL S^3 x R` (inherits the weakest
  upstream tier)
- bounded slice generator `Lambda_R` (from
  [`OH_SCHUR_BOUNDARY_ACTION_NOTE.md`](OH_SCHUR_BOUNDARY_ACTION_NOTE.md),
  `retained_bounded` on the strong-field bridge surface only)
- bounded microscopic Schur boundary action (same source; same tier
  qualifier)

The scalar boundary action is the Dirichlet/Schur quadratic

- `I_R(f ; j) = 1/2 f^T Lambda_R f - j^T f`

with `Lambda_R` symmetric positive definite on the current restricted class.

This scalar backbone wording was corrected 2026-05-17: prior text said
"exact" for each bullet, but per the 2026-05-17 ledger, the composite
sits at the weakest upstream tier. The tensor-extension content below
(§Tensorized Schur/Dirichlet primitive candidate and below) is
unaffected by this tier-qualifier correction.

## Exact scalar support reduction

On the seven-site star support, the surviving exact scalar on the current
`A1` block is

- `delta_A1(q) = phi_support(center)/Q - phi_support(arm_mean)/Q`.

The exact projective family law is

- `delta_A1(r) = 1 / (6 (1 + sqrt(6) r))`.

The exact endpoint values are

- `delta_A1(e0) = 1/6`
- `delta_A1(s / sqrt(6)) = 0`.

That scalar support law is exact and stays the only exact support datum the
current support-side Schur stack can produce.

## Bounded tensor prototype

The current bounded tensor prototype remains the bright-channel pair

- `Theta_R^(0)(q) = (gamma_E(q), gamma_T(q))`

on the microscopic support block

- `A1 x {E_x, T1x}`.

This prototype is bounded, not exact, because it still comes from the current
tensor-boundary-drive frontier rather than from an exact tensor-valued support
observable.

The canonical source-side comparison surface is:

- `Theta_R^(0)(e0) = (-3.772329e-04, +3.359952e-04)`
- `Theta_R^(0)(s / sqrt(6)) = (-2.010572e-04, +4.031968e-04)`

and the current affine fit in `delta_A1` tracks the canonical `A1` family and
the audited `O_h` / finite-rank baselines at the already-observed bounded
accuracy.

## Tensorized Schur/Dirichlet primitive candidate

The smallest tensor extension consistent with the current evidence is the
source-centered quadratic completion

- `I_TS^(0)(f, a ; j) = I_R(f ; j) + 1/2 ||a - Theta_R^(0)(delta_A1(f))||^2`

where:

- `f` is the exact scalar shell trace
- `a = (a_E, a_T)` is the two-channel bright boundary vector
- `Theta_R^(0)(delta_A1(f))` injects the bounded tensor prototype as the
  source-side tensor carrier

Equivalently, this is the block-diagonal tensorized boundary action

- `I_TS^(0)(f, a ; j) = 1/2 f^T Lambda_R f - j^T f + 1/2 (a - Theta_R^(0))^T (a - Theta_R^(0))`

with a minimal positive-definite tensor kernel

- `K_TS = I_2`.

This is the smallest tensorized Schur/Dirichlet primitive that adds a genuine
two-channel tensor boundary sector without pretending the exact tensor carrier
already exists.

## Why this is the right bounded extension

The current exact support-side machinery is scalar/rank-one on `A1`:

1. the exact support Hessian has no mixed `A1`-bright block
2. the exact support-to-active operator is rank one and charge-only
3. the exact support scalar `delta_A1` is blind to `E_x` and `T1x`

Therefore the exact tensor carrier is absent.

But the frontier also shows that the tensor boundary drive itself is already
bright on exactly two aligned source channels:

- `E_x`
- `T1x`

So the smallest useful tensorization is precisely a two-channel boundary
completion around the exact scalar Schur action, not a larger bulk ansatz.

## What the candidate does

The candidate primitive does three useful things:

1. it preserves the exact scalar Schur/Dirichlet backbone
2. it packages the existing bright tensor prototype as a boundary field
3. it gives the cleanest possible tensorized comparison surface for future
   exact work

In other words, it is the minimal tensorized Schur primitive worth keeping on
the Route-2 frontier until a genuine exact tensor carrier is derived.

## What it does not do

This note still does **not** claim:

1. an exact tensor-valued support observable on `A1 x {E_x, T1x}`
2. an exact tensor endpoint coefficient theorem
3. an exact support-to-slice time-coupling law
4. full GR on Route 2

The exact tensor carrier is still missing. This note gives the smallest
bounded tensorized Schur/Dirichlet primitive compatible with the current
evidence.

## Atlas-facing interpretation

This object is the right future atlas tool candidate for Route 2:

- bounded scalar Schur boundary action: `retained_bounded` tool (on
  the strong-field bridge surface only; not on the full retained-grade
  dynamical sector)
- tensorized Schur/Dirichlet primitive: bounded candidate
- exact tensor carrier: still missing

That separation matters. The atlas should reuse the exact scalar backbone and
the bounded tensor completion separately, not collapse them into one ambiguous
claim.

## Bottom line

The smallest tensorized Schur/Dirichlet primitive currently supported by the
Route-2 frontier is:

- bounded scalar boundary action `I_R` (`retained_bounded` on the
  strong-field bridge surface only)
- plus a two-channel boundary completion centered on
  `Theta_R^(0)(q) = (gamma_E(q), gamma_T(q))`

It is bounded, not exact, but it is the cleanest new tensor extension of the
Schur/Dirichlet machinery that the current atlas supports.

## Upstream-tier accounting (2026-05-17)

Per the 2026-05-17 ledger snapshot, the cited upstreams sit at:

| Upstream | `claim_type` | `audit_status` | `effective_status` |
|---|---|---|---|
| `s3_general_r_derivation_note` | `positive_theorem` | (per ledger) | (per ledger) |
| `s3_boundary_link_theorem_note` | `bounded_theorem` | `audited_clean` | `retained_bounded` |
| `s3_cap_uniqueness_note` | `bounded_theorem` | `audited_conditional` | `audited_conditional` |
| `anomaly_forces_time_theorem` | `bounded_theorem` | `unaudited` | `unaudited` |
| `oh_schur_boundary_action_note` | `bounded_theorem` | (per ledger) | `retained_bounded` |

**Tier accounting:** the composite `PL S^3` background inherits the
weakest of the two cited PL companions' tiers, currently
`audited_conditional` (via cap-uniqueness). Combined with the
currently-`unaudited` `ANOMALY_FORCES_TIME_THEOREM`, the composite
`PL S^3 x R` background is `unaudited`. The Schur action and
`Lambda_R` are `retained_bounded` only on the strong-field bridge
surface, not on the full retained-grade dynamical sector. Earlier body
wording that called all of these "exact" was tier-loose and has been
corrected inline.

**Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`:** the
tensorized primitive imports `d_t = 1` from the upstream parent. Per
the parent's recent
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
`d_t = 1` decomposes into a derived part (Step 3:
`d_t ∈ {1, 3, 5, ...}`) and an inherited part (admission (iv)
excludes `d_t > 1`). Any future revision of admission (iv) propagates
into this note's clock-step input. The tensor-extension content
itself (`I_TS^(0)`, two-channel completion, `K_TS = I_2`) is unaffected.

## Fix record (2026-05-17, downstream surgical-fix wave)

Two hostile-audit-grade fixes applied:

- **F-A (over-claim "exact" for scalar backbone):** §Exact scalar
  backbone block had 5 "exact" bullets ("exact `S^3` spatial closure",
  "exact anomaly-forced time", "exact background `PL S^3 x R`", "exact
  slice generator `Lambda_R`", "exact microscopic Schur boundary
  action") plus an "exact scalar Schur boundary action: retained tool"
  bullet in §Atlas-facing interpretation and an "exact scalar boundary
  action `I_R`" bullet in §Bottom line. Per the 2026-05-17 ledger,
  none of the upstreams is at `retained_clean` and the composite is
  at most `audited_conditional` (via cap-uniqueness) / `unaudited`
  (via anomaly-forced time). Section heading renamed "Exact scalar
  backbone" → "Cited scalar backbone"; bullets corrected to tier-honest
  wording. The `retained_bounded` qualifier is preserved for the Schur
  action on the strong-field bridge surface only.
- **F-B (admission-inheritance disclosure):** new
  "Upstream-tier accounting (2026-05-17)" section now records the
  full tier table and the parent's admission-(iv) inheritance route.

See companion fix-record:
[`S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_DOWNSTREAM_FIX_NOTE_2026-05-17.md`](S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_DOWNSTREAM_FIX_NOTE_2026-05-17.md).

Paired verifier:
`scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py`.

None of these edits change the tensorized Schur/Dirichlet primitive
candidate `I_TS^(0)(f, a; j)`, the source-side comparison-surface
numerics, the `K_TS = I_2` kernel, the rank-one obstruction argument,
or the "What it does not do" claim list.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [s3_general_r_derivation_note](S3_GENERAL_R_DERIVATION_NOTE.md)
- [anomaly_forces_time_theorem](ANOMALY_FORCES_TIME_THEOREM.md)
- [oh_schur_boundary_action_note](OH_SCHUR_BOUNDARY_ACTION_NOTE.md)
