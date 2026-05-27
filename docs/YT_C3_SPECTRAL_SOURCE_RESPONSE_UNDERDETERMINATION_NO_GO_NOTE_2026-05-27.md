---
claim_id: yt_c3_spectral_source_response_underdetermination_no_go_note_2026-05-27
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Spectral Source-Response Underdetermination No-Go

**Claim type:** no-go / negative route pruning.  
**Role:** narrows the live C3 spectral-projector route.  
**Status:** exact obstruction to deriving the top source response from C3
spectral projectors alone; no retained or proposed-retained Y_T closure.  
**Primary runner:**
`scripts/frontier_yt_c3_spectral_source_response_underdetermination_no_go.py`  
**Generated output:**
`outputs/yt_c3_spectral_source_response_underdetermination_no_go_2026-05-27.json`

## Question

The C3 spectral route remains live: a C3-preserving Hermitian circulant
operator can have three distinct mass eigenprojectors.  Is that enough to fix
the physical top source response and recover the local `1/sqrt(6)` coefficient?

## Answer

No.  Spectral projectors are not source-response coefficients.

For a C3-preserving generation operator

```text
H(h) = a(h) I + q(h) C + conjugate(q(h)) C^2,
q(h) = x(h) + i y(h),
```

the three spectral eigenvalues are:

```text
lambda_0 = a + 2 x,
lambda_1 = a - x - sqrt(3) y,
lambda_2 = a - x + sqrt(3) y.
```

If the top line is, for example, the `lambda_0` line, then its same-source
response is:

```text
d lambda_top / dh = a'(h) + 2 x'(h).
```

C3 representation theory fixes the projector algebra, but it does not fix
`a'(h)`, `x'(h)`, or `y'(h)`.  Therefore the top response remains tunable until
the same-surface source law for the circulant coefficients is derived.

## Finite Witness

Take the same C3 spectral projector `P_0` and the same nondegenerate base
operator at `h = 0`.  Compare two source paths:

```text
Path A: a(h) = a0 + h/sqrt(6),  x(h)=x0,          y(h)=y0
Path B: a(h) = a0 + 2h/sqrt(6), x(h)=x0,          y(h)=y0
```

Both preserve:

- C3 invariance;
- the same spectral projector at `h = 0`;
- nondegeneracy for sufficiently small `h`;
- no old Ward or `H_unit` proof input.

But their top-line responses differ:

```text
Path A: d lambda_0/dh = 1/sqrt(6)
Path B: d lambda_0/dh = 2/sqrt(6).
```

Thus the spectral projector route needs a source-response theorem, not just
projector algebra.

## What This Prunes

This prunes:

```text
C3 spectral projectors + nondegeneracy
  -> coefficient-certified top response.
```

It does not prune:

```text
accepted same-surface C3 source law for a(h), x(h), y(h)
  -> coefficient-certified top response.
```

That second route remains the best non-compute route if a native source law can
be derived.

## What Would Close

Positive closure through this route must supply:

```yaml
accepted_c3_circulant_generation_operator: true
same_surface_source_law_for_a_x_y: true
top_line_ordering_derived: true
d_lambda_top_dh_derived: true
d_lambda_top_dh_equals_color_isospin_coefficient: true
same_surface_w_response: true
top_w_response_certificate_passes: true
no_forbidden_imports: true
```

Equivalently, strict same-source pole-row data can bypass the algebraic source
law if it directly measures the coefficient-bearing top response.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- refute the C3 spectral projector route;
- refute the native no-`kappa` backend candidate;
- derive or import observed masses;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG targets, `alpha_LM`,
  plaquette/u0, Planck, alpha_s, or a fitted selector as proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
proposal_allowed_reason: |
  C3 spectral projectors do not determine source responses. The top response
  depends on the h-derivatives of the circulant coefficients a,x,y, which are
  not derived on the current surface.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive the accepted same-surface source law for the C3 circulant
  coefficients, or produce strict top/W pole-row evidence.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_spectral_source_response_underdetermination_no_go.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
