---
claim_id: source_measure_sharp_record_tangent_space_theorem_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Source/Measure Sharp-Record Tangent-Space Theorem

**Claim type:** bounded_theorem / exact-support theorem.
**Role:** third source/measure P-cal retirement route; strengthens the RN
cocycle route by deriving the primitive source unit from finite sharp-record
probability geometry.
**Status:** exact-support.  This note proves that finite sharp-record
probability space has a canonical RN score tangent space and Fisher unit
normalization.  It does not by itself assert unbounded retained Y_T closure.
**Primary runner:** `scripts/frontier_source_measure_sharp_record_tangent_space.py`
**Generated output:** `outputs/source_measure_sharp_record_tangent_space_2026-05-30.json`

## Theorem

On a finite sharp-record sample space, with the projective record surface as in
[`LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md),
and with reference probability `P_0`, every smooth absolutely-continuous
record-probability intervention `P_h` has a Radon-Nikodym density

```text
R_h = dP_h / dP_0
```

and an origin score tangent

```text
s = d log R_h / dh |_{h=0}.
```

Because `E_0[R_h]=1`, every score tangent has zero reference mean:

```text
E_0[s] = 0.
```

The canonical quadratic form on this tangent space is the Fisher pairing

```text
<s,t>_F = E_0[s t].
```

For the LSP sharp signed record `epsilon in {-1,+1}` with the normalized
trace/uniform pre-source reference,

```text
E_0[epsilon] = 0,
E_0[epsilon^2] = 1.
```

Thus the primitive signed record is already a unit source tangent.  A scaled
source `lambda epsilon` has Fisher norm `lambda^2` and is not the primitive
unit tangent unless `lambda = 1`.

## Tangent-space proof

In the two-outcome sharp-record case `P_0=(1/2,1/2)`, any probability tangent
has form

```text
dp = (a, -a).
```

The RN score is

```text
s = dp / P_0 = (2a, -2a),
```

with zero reference mean.  Its Fisher norm is

```text
E_0[s^2] = 4a^2.
```

The primitive signed-record tangent is `s = (+1,-1)`, corresponding to
`dp=(1/2,-1/2)`, and has norm one.  There is no hidden continuous scale in
this tangent vector: multiplying it by `lambda` multiplies the Fisher norm by
`lambda^2`.

## Exponential chart

Every score tangent `O` has a canonical normalized positive exponential chart

```text
R_h = exp(h O - W(h)),
W(h) = log E_0 exp(h O).
```

This chart is not an extra logarithm premise; the scalar `W` is forced by
normalization:

```text
1 = E_0[R_h] = exp(-W(h)) E_0 exp(h O).
```

This recovers the RN-cocycle theorem and the P-cal generator on the sharp
record sector.

## Y_T source unit

For the normalized six-component top source tangent

```text
O_top = sum_i O_i / sqrt(6),
```

the Fisher norm is one.  A scaled family `lambda O_top` has norm `lambda^2`.
Therefore the finite sharp-record source tangent geometry selects

```text
lambda = 1,
y_33 = 1/sqrt(6).
```

## Status boundary

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure_candidate
target_blocker_text: "P-cal / primitive source-action unit"
source_of_blocker_text: "observable-principle P-cal residual and Y_T primitive source-unit no-go"
reachability_to_target: partially_closes
artifact_role: theorem
closed_if_audit_accepts_record_probability_intervention_as_physical_source:
  - canonical RN score tangent space
  - primitive Fisher source unit
  - P-cal exponential chart on sharp-record sector
  - lambda = 1 for normalized Y_T top source
remaining_if_not_accepted:
  - physical source intervention means a smooth record-probability intervention
  - strict same-source top/W response certificate
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Non-claims

This note does not claim:

- unbounded retained Y_T closure on the current surface;
- that independent audit has accepted record-probability interventions as the
  complete physical-source semantics;
- a strict same-source top/W pole-response certificate;
- derivation of `v`, Planck scale, `g_2`, or running bridges;
- use of `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG values, `alpha_LM`,
  plaquette/u0, or a fitted selector.

## Verification

Run:

```text
python3 scripts/frontier_source_measure_sharp_record_tangent_space.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
