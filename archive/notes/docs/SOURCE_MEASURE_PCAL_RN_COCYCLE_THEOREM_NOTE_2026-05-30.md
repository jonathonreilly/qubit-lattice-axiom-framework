---
claim_id: source_measure_pcal_rn_cocycle_theorem_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Source/Measure P-Cal RN-Cocycle Theorem

**Claim type:** bounded_theorem / exact-support theorem.
**Role:** first source/measure P-cal retirement route for the Y_T source-scale
blocker.
**Status:** exact-support.  This note proves the RN-cocycle route once
physical source interventions are identified with normalized sharp-record
Radon-Nikodym cocycles.  It does not by itself assert unbounded retained Y_T
closure.
**Primary runner:** `scripts/frontier_source_measure_pcal_rn_cocycle.py`
**Generated output:** `outputs/source_measure_pcal_rn_cocycle_2026-05-30.json`

## Theorem

On the qubit-on-`Z^3` sharp-record surface, with sharp projective records as in
[`LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md),
let an ideal unrefined projective measurement have signed record
`epsilon in {-1,+1}`.  If a physical source intervention is represented by a
normalized positive Radon-Nikodym cocycle over those records with primitive
origin score `epsilon`, then the source family is

```text
R_h(epsilon) = exp(h epsilon - W(h)),
E_0[R_h] = 1,
```

and normalization forces

```text
W(h) = log E_0 exp(h epsilon).
```

Sequential independent records multiply their RN densities, and therefore
their log densities add.  The primitive source coordinate has Fisher norm one
at the origin.  A rescaled family

```text
R_h^(lambda)(epsilon) = exp(h lambda epsilon - W_lambda(h))
```

has Fisher norm `lambda^2`, so it is not the primitive unit source coordinate
unless `lambda = 1`.

This is the exact RN-cocycle form of the P-cal premise:

```text
physical scalar generator = potential for canonical normalized-trace
expectation field, with <1> = 1.
```

It shows that once source interventions are record-RN cocycles, the logarithm,
source-action unit, and `lambda = 1` are not separate choices.

## RN cocycle proof

The ideal projective measurement rule gives

```text
P_+ = (I + sigma_z)/2,
P_- = (I - sigma_z)/2,
epsilon = P_+ - P_- = sigma_z,
epsilon^2 = I.
```

For a finite reference record measure `P_0`, a source intervention changes the
measure by a positive RN density `R_h = dP_h/dP_0`.  The source family is
normalized by definition:

```text
E_0[R_h] = 1.
```

If the source has primitive signed-record score at the origin,

```text
d log R_h / dh |_{h=0} = epsilon,
```

the canonical exponential representative is

```text
R_h(epsilon) = exp(h epsilon - W(h)).
```

Normalization determines the scalar generator uniquely:

```text
1 = E_0 exp(h epsilon - W(h))
  = exp(-W(h)) E_0 exp(h epsilon),
```

hence

```text
W(h) = log E_0 exp(h epsilon).
```

No independent scalar-additivity postulate is used in this calculation.  The
logarithm appears as the unique normalizer of the RN source cocycle.

For two independent sharp records, the joint RN density is

```text
R_h(epsilon_1, epsilon_2) = R_h(epsilon_1) R_h(epsilon_2),
```

so the source/action increment is additive:

```text
log R_h(epsilon_1, epsilon_2)
  = log R_h(epsilon_1) + log R_h(epsilon_2).
```

The additivity is therefore the RN chain rule for sequential record updates,
not an extra selection rule on an arbitrary scalar family.

## Connection to P-cal

The live residual in
[`OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md`](OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md)
is P-cal:

```text
the physical scalar generator is the potential for the canonical
normalized-trace Gibbs/KMS expectation field, normalized so <1> = 1.
```

This note gives the sharp-record RN-cocycle form of that premise.  On a finite
qubit record space, the normalized trace supplies the reference expectation
`E_0`.  A source intervention is a normalized positive measure update, so its
RN density has expectation one.  The primitive source score is the signed
record itself.  Those three facts force `W = log E_0 exp(h O)`.

The note does not hide the remaining decision: independent audit must decide
whether "physical source intervention is an RN cocycle over sharp records" is
already native to the qubit/LSP source-measure surface or remains a distinct
source-action convention.  If it is native, this theorem retires P-cal for the
sharp-record source sector.  If it is not native, this theorem is exact support
for the same one-line premise and the status remains bounded.

## Application to Y_T

For the normalized six-component one-Higgs top source operator,

```text
O_top = sum_{i=1}^6 O_i / sqrt(6),
```

the coefficient vector has unit norm.  A scaled top source has score
`lambda O_top` and Fisher norm `lambda^2`.  Therefore the RN-cocycle primitive
source unit gives

```text
lambda = 1,
y_33 = 1/sqrt(6).
```

This is the same scalar targeted in
[`YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md`](YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md)
and discussed historically in
`YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md`. That old
decision supplies no premise or dependency readiness today.
The new contribution is that the source unit is now expressed as a
sharp-record RN-cocycle theorem candidate; its authority depends on independent
audit of the stated conditions, not on the historical decision.

## Status boundary

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure_candidate
target_blocker_text: "P-cal / primitive source-action unit"
source_of_blocker_text: "observable-principle P-cal residual and Y_T primitive-unit source/action no-go"
reachability_to_target: partially_closes
artifact_role: theorem
closed_if_audit_accepts_rn_cocycle_as_native_source_measure:
  - P-cal for sharp-record RN source sector
  - lambda = 1 for normalized Y_T top source
  - y_33 = 1/sqrt(6) on that sector
remaining_if_not_accepted:
  - physical source intervention is an RN cocycle over sharp records
  - strict same-source top/W response certificate
proposal_allowed: false
proposal_allowed_reason: >
  This block proves the RN-cocycle algebra and its Y_T lambda consequence, but
  the source-measure semantic identification still requires independent audit.
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Non-claims

This note does not claim:

- unbounded retained Y_T closure on the current surface;
- that independent audit has accepted the RN-cocycle source-measure
  identification;
- that generic non-sharp/non-RN source interventions are covered;
- a production top-correlator measurement;
- a strict same-source top/W pole-response certificate;
- derivation of `v = 246 GeV`, Planck scale, `g_2`, or running bridges;
- use of `H_unit`, `yt_ward_identity`, `y_t_bare`, observed top masses, PDG
  values, `alpha_LM`, plaquette/u0, or a fitted selector.

## Verification

Run:

```text
python3 scripts/frontier_source_measure_pcal_rn_cocycle.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
