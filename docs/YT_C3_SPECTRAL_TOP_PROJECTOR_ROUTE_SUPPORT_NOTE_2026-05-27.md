---
claim_id: yt_c3_spectral_top_projector_route_support_note_2026-05-27
claim_type_author_hint: bounded_support
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Spectral Top-Projector Route Support

**Claim type:** bounded support / route repair.  
**Role:** keeps open the positive C3-preserving spectral-projector route after
the top-sector corner-label obstruction.  
**Status:** exact support for a live route, not retained or proposed-retained
Y_T closure.  
**Primary runner:** `scripts/frontier_yt_c3_spectral_top_projector_route_support.py`  
**Generated output:**
`outputs/yt_c3_spectral_top_projector_route_support_2026-05-27.json`

## Question

The top-sector projector obstruction shows that current C3-symmetric inputs do
not canonically pick one of the three **corner-label** projectors as physical
`P_top`.

Does that obstruction also rule out a C3-preserving mass-eigenprojector route?

## Answer

No.  A C3-preserving Hermitian circulant operator on the generation triplet can
have three distinct Fourier-character eigenvalues:

```text
H(a,q) = a I + q C + conjugate(q) C^2,
lambda_k = a + 2 |q| cos(theta + 2 pi k / 3).
```

For generic `q`, the three eigenvalues are distinct, and the spectral
projectors onto the C3 character lines are canonical projectors of that
operator.  This gives a live positive route:

```text
accepted C3-preserving same-surface dynamics
  -> nondegenerate spectral projectors
  -> top pole = derived ordered spectral line
  -> source-generator matrix element
  -> strict top/W response readout.
```

This does not close Y_T because the current branch still does not derive the
accepted operator `H(a,q)`, the phase/order selecting the top line, or the
source-generator matrix elements.  It only prevents an overbroad reading of the
corner-label no-go.

## Finite Algebra

Let `C` be the 3-cycle on `V_gen = C^3`.  The C3-invariant Hermitian circulant
family is:

```text
H = a I + q C + q_bar C^2.
```

It commutes with `C`, so it is diagonalized by the C3 character vectors:

```text
f_k = (1, omega^k, omega^(2k)) / sqrt(3),  k = 0,1,2.
```

The corresponding projectors

```text
P_k = |f_k><f_k|
```

are spectral projectors when the eigenvalues are distinct.  This is a
mass-eigenline route, not a corner-label route.

## What This Repairs

The previous obstruction remains correct for:

```text
C3-invariant premises alone -> chosen corner projector P_i.
```

The live route is instead:

```text
derived C3-preserving dynamics -> chosen spectral projector P_k by eigenvalue.
```

Those are different statements.  The second route still needs a physical
dynamics theorem or strict pole-row data; but it is not killed by the
corner-label no-go.

Summary: this route is not killed by the corner-label no-go.

## What Would Close

A positive Y_T theorem through this route must supply:

```yaml
accepted_c3_circulant_generation_operator: true
operator_derived_on_same_surface: true
nondegenerate_eigenvalues: true
top_line_ordering_derived: true
top_projector_is_spectral_projector: true
source_generator_matrix_element_derived: true
same_surface_w_projector_and_response: true
contact_subtraction_done: true
fv_ir_controls_pass: true
same_model_class: true
no_forbidden_imports: true
```

The missing hard parts are the physical source law for `a,q`, the ordering of
the spectral lines, and the source-generator matrix element on the top line.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive the physical top projector;
- derive the C3 circulant mass/source law;
- derive the source-generator matrix element;
- import observed masses or Koide/charged-lepton values as proof inputs;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG targets, `alpha_LM`,
  plaquette/u0, Planck, alpha_s, or a fitted selector as proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: |
  The finite C3 spectral algebra supplies a live projector route, but the
  accepted same-surface dynamics, eigenvalue ordering, and source-generator
  matrix elements are not derived.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive the accepted C3-preserving circulant generation operator
  and its top-line source response, or produce strict pole-row evidence.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_spectral_top_projector_route_support.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
