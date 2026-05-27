---
claim_id: yt_c3_connected_reflection_even_source_direction_candidate_note_2026-05-27
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Connected Reflection-Even Source-Direction Candidate

**Claim type:** bounded theorem / exact support candidate.  
**Role:** records the strongest positive non-compute C3 source-direction
candidate found so far.  
**Status:** exact support only; no retained or proposed-retained Y_T closure.

**Primary runner:**
`scripts/frontier_yt_c3_connected_reflection_even_source_direction_candidate.py`  
**Generated output:**
`outputs/yt_c3_connected_reflection_even_source_direction_candidate_2026-05-27.json`

## Purpose

The live C3 route needs a physical source direction in the C3-invariant
Hermitian tangent space:

```text
span(B_a, B_x, B_y).
```

The preceding boundary packets show that C3 invariance, unit Fisher length,
LSP projective readout, and positivity/orientation support do not select that
direction by themselves.  This note records a narrower positive candidate:

```text
connected source tangent + reflection-even neutral source
  -> B_x
```

and computes its C3 spectral-line responses.

## Candidate Premises

The candidate adds two physical-source premises that are plausible but not yet
accepted for Y_T:

1. **Connected source tangent:** the identity direction is a normalization
   direction and is quotiented out, as in normalized connected source
   responses.  This removes `B_a`.
2. **Reflection-even neutral scalar source:** the physical neutral Higgs/Y_T
   source is even under the reflection that sends `C -> C^2`.  This removes
   the orientation-odd splitter `B_y`.

Inside the C3 Hermitian tangent space, those two premises leave one ray:
the constraint pair leaves the unique unit direction `B_x` up to sign.

```text
B_x = (C + C^2) / sqrt(6)
```

up to an overall source sign.

## Finite Algebra

Use the orthonormal C3 tangent basis:

```text
B_a = I / sqrt(3),
B_x = (C + C^2) / sqrt(6),
B_y = i(C - C^2) / sqrt(6).
```

The connected trace condition removes `B_a`, and reflection parity gives:

```text
R B_x R = B_x,
R B_y R = -B_y.
```

So connected + reflection-even selects `B_x`.

For C3 spectral projectors:

```text
P_0, P_omega, P_omega2,
```

the `B_x` responses are:

```text
Tr(P_0 B_x)      =  2/sqrt(6),
Tr(P_omega B_x)  = -1/sqrt(6),
Tr(P_omega2 B_x) = -1/sqrt(6).
```

Thus the nontrivial C3 character lines carry exactly the target magnitude:

```text
|Tr(P_omega B_x)| = |Tr(P_omega2 B_x)| = 1/sqrt(6).
```

This is the first clean C3 source-direction candidate that naturally produces
the coefficient magnitude without inserting `kappa` or using the old
`H_unit`/Ward route.

## What This Supports

Conditional on all three extra physical identifications:

```yaml
connected_source_tangent_is_physical: true
neutral_scalar_source_is_reflection_even: true
physical_top_line_is_nontrivial_C3_character: true
```

the local top source response has magnitude:

```text
1/sqrt(6).
```

The result is source-direction support, not a full top/Yukawa theorem.

## What Remains Open

This note does not close Y_T because it does not derive:

- that the physical Y_T source is the connected source tangent on this
  generation surface;
- that the neutral scalar/Y_T source must be reflection-even in this C3
  generation commutant;
- that the physical top pole line is one of the nontrivial C3 character lines
  rather than the `P_0` line;
- the accepted same-surface C3 generation dynamics and eigenvalue ordering;
- the same-surface W response, top/W pole rows, contact subtraction, FV/IR
  controls, or matching/running.

If the top line is `P_0`, the same `B_x` source gives `2/sqrt(6)`, not the
target magnitude.  Therefore top-line assignment remains load-bearing.

## Relation To Prior Boundaries

- [`YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md`](YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md)
  prunes C3 + unit normalization alone.  This note adds connectedness and
  reflection parity, so it does not contradict that no-go.
- [`YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md`](YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md)
  prunes projective readout as a source-direction selector.  This note does
  not use LSP as the selector.
- [`YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md`](YT_POSITIVITY_ORIENTATION_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md)
  prunes orientation support as a Y_T source theorem.  This note uses
  reflection-even neutrality, not orientation-odd splitting.
- `YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26`
  is context for the connected-source premise, but this note does not import it
  as retained Y_T authority.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive the physical top line;
- derive strict top/W pole-response evidence;
- derive `m_t`, physical-scale `g_2`, or numerical `y_t(v)`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  targets, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: |
  Connected + reflection-even source conditions select B_x, and B_x has
  response magnitude 1/sqrt(6) on nontrivial C3 character lines. The physical
  connected-source premise, reflection-even premise, and top-line assignment
  are not yet derived on the accepted same-surface dynamics.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive connected/reflection-even physical source authority and
  nontrivial top-line assignment from same-surface C3 dynamics, or produce
  strict same-source top/W pole-response evidence.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_connected_reflection_even_source_direction_candidate.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
