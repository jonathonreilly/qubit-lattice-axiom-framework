---
claim_id: yt_c3_nontrivial_top_line_assignment_boundary_note_2026-05-27
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Nontrivial Top-Line Assignment Boundary

**Claim type:** no_go / negative route pruning.  
**Role:** tests the remaining shortcut after the connected/reflection-even
`B_x` source candidate.  
**Status:** no retained or proposed-retained Y_T closure by this note.  
**Primary runner:**
`scripts/frontier_yt_c3_nontrivial_top_line_assignment_boundary.py`  
**Generated output:**
`outputs/yt_c3_nontrivial_top_line_assignment_boundary_2026-05-27.json`

## Question

The connected/reflection-even C3 candidate proves:

```text
connected source tangent + reflection-even neutral source
  -> B_x = (C + C^2)/sqrt(6).
```

The tempting shortcut is:

```text
B_x source direction
  -> Y_T coefficient 1/sqrt(6).
```

This note checks that shortcut directly.

## Answer

The shortcut does not close.  The same connected/reflection-even source
direction gives different responses on the three C3 character lines:

```text
Tr(P_0 B_x)       =  2/sqrt(6)
Tr(P_omega B_x)   = -1/sqrt(6)
Tr(P_omega2 B_x)  = -1/sqrt(6).
```

Therefore the `1/sqrt(6)` coefficient follows only after adding the physical
premise:

```text
the physical top row is a nontrivial C3 character line.
```

That premise is useful and narrow, but it is not derived by the current C3,
LSP, positivity/orientation, or connected/reflection-even support packets.

## Finite Witness

Let

```text
C e_1 = e_2,   C e_2 = e_3,   C e_3 = e_1,
B_x = (C + C^2) / sqrt(6).
```

Let `omega = exp(2 pi i / 3)`. The C3 spectral projectors are:

```text
P_0       = (I + C + C^2) / 3
P_omega   = (I + omega^-1 C + omega^-2 C^2) / 3
P_omega2  = (I + omega^-2 C + omega^-4 C^2) / 3.
```

All three are rank-one C3 spectral projectors.  The LSP sharp-projective rule
supplies `K_P = P` for any one of them once supplied.  Nothing in that rule
chooses which projector is the physical top row.

The two assignments below satisfy the same current support:

```text
Assignment A: top line = P_0       -> response magnitude 2/sqrt(6)
Assignment B: top line = P_omega   -> response magnitude 1/sqrt(6)
```

They differ only by the physical top-line assignment.  Hence that assignment
is load-bearing.

## Relation To Existing Retained Generation Algebra

The retained three-generation observable package supplies the `C^3` carrier,
translation-character rank-one sectors, and the induced C3 cycle.  It also
explicitly does not identify those abstract sectors with a physical quark
generation label or a top pole row.

This note respects that boundary.  It uses the C3 character projectors as exact
finite algebra and does not treat any one of them as the physical top row.

## What This Prunes

This prunes:

```text
connected/reflection-even C3 source direction alone
  -> physical Y_T coefficient 1/sqrt(6).
```

It does not prune the positive route:

```text
connected/reflection-even C3 source direction
  + physical top is nontrivial C3 line
  -> coefficient magnitude 1/sqrt(6).
```

The positive route remains live if the nontrivial top-line premise is derived
from same-surface dynamics or strict pole-row evidence.

## What Remains Open

To turn this into retained-positive Y_T closure, a future theorem or
certificate must supply at least one of:

1. an accepted same-surface dynamics theorem excluding the C3 singlet line as
   the physical top row;
2. an accepted top-pole/eigenvalue ordering theorem that identifies the top as
   one of the nontrivial C3 character lines;
3. strict same-source top/W pole-response rows whose top row directly measures
   the coefficient.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive the physical top row;
- derive strict top/W pole-response evidence;
- refute the connected/reflection-even `B_x` candidate;
- refute the C3 spectral-projector route;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: exact-support if nontrivial top-line assignment is supplied
proposal_allowed: false
proposal_allowed_reason: |
  The connected/reflection-even B_x source candidate gives 1/sqrt(6) only on
  nontrivial C3 character lines. The physical top-line assignment is not
  derived on the current surface.
bare_retained_allowed: false
audit_required_before_effective_retained: true
route_still_live: derive nontrivial top-line assignment from same-surface dynamics or produce strict same-source top/W pole rows
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_nontrivial_top_line_assignment_boundary.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

