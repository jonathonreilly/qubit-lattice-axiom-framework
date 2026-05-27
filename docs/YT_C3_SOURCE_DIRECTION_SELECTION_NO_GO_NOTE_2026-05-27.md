---
claim_id: yt_c3_source_direction_selection_no_go_note_2026-05-27
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Source-Direction Selection No-Go

**Claim type:** no-go / negative route pruning.  
**Role:** narrows the remaining C3 circulant source-law target.  
**Status:** exact obstruction to deriving the top response from C3 invariance
plus unit source normalization alone; no retained or proposed-retained Y_T
closure.  
**Primary runner:** `scripts/frontier_yt_c3_source_direction_selection_no_go.py`  
**Generated output:** `outputs/yt_c3_source_direction_selection_no_go_2026-05-27.json`

## Question

The previous no-go showed that C3 spectral projectors do not determine
`a'(h), x'(h), y'(h)`.  Could the primitive RN/Fisher source law fix the missing
direction by requiring a unit source tangent?

## Answer

No.  A unit source tangent fixes scale, not direction.

The C3-invariant Hermitian tangent space is three-dimensional:

```text
delta H = da I + dx (C + C^2) + i dy (C - C^2).
```

After Frobenius/Fisher unit normalization, there remains a two-sphere of unit
directions.  The top-line response is a linear functional on that sphere.  It
is not fixed unless an additional physical target operator/source direction is
derived.

## Finite Witness

Use the orthonormal C3-invariant tangent basis:

```text
B_a = I / sqrt(3),
B_x = (C + C^2) / sqrt(6),
B_y = i(C - C^2) / sqrt(6).
```

All three have unit Frobenius norm.  On the `lambda_0` spectral line:

```text
d lambda_0(B_a) = 1/sqrt(3),
d lambda_0(B_x) = 2/sqrt(6),
d lambda_0(B_y) = 0.
```

So two equally normalized admissible C3 source tangents give different top
responses.  Fisher/unit-source normalization therefore cannot by itself derive
the `1/sqrt(6)` top response.

## What This Prunes

This prunes:

```text
C3 invariance + unit source normalization
  -> unique C3 source direction
  -> coefficient-certified top response.
```

It does not prune:

```text
derive a physical target operator/source direction inside the C3 tangent space
  -> compute top response.
```

## What Would Close

Positive closure through this route must add:

```yaml
physical_c3_source_direction_derived: true
source_direction_not_fitted_to_target: true
top_line_ordering_derived: true
top_line_matrix_element_derived: true
same_surface_w_response: true
top_w_response_certificate_passes: true
no_forbidden_imports: true
```

This is exactly the remaining hard object: a framework-native physical source
direction in the C3 circulant coefficient space.

Equivalently, the remaining hard object is a physical source direction in the C3 circulant coefficient space.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- refute the C3 spectral route;
- refute the primitive RN/Fisher source law;
- deny that a later physical target operator could fix the direction;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG targets, `alpha_LM`,
  plaquette/u0, Planck, alpha_s, or a fitted selector as proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
proposal_allowed_reason: |
  Unit source normalization leaves a two-sphere of C3-invariant tangent
  directions. The top response is a linear functional on that sphere and is
  not fixed without a derived physical source direction.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive the physical source direction/target operator in the C3
  circulant tangent space, or produce strict pole-row evidence.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_source_direction_selection_no_go.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
