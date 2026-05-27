---
claim_id: yt_positivity_orientation_c3_source_direction_boundary_note_2026-05-27
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Positivity/Orientation C3 Source-Direction Boundary

**Claim type:** no-go / negative route pruning.
**Role:** checks whether the existing positivity/orientation C3 material closes
the remaining Y_T C3 source-direction gate.
**Status:** exact obstruction to the shortcut

```text
positivity/orientation selects C3
  -> physical Y_T C3 source tangent.
```

This packet does not claim retained or proposed-retained Y_T closure.

**Primary runner:**
`scripts/frontier_yt_positivity_orientation_c3_source_direction_boundary.py`
**Generated output:**
`outputs/yt_positivity_orientation_c3_source_direction_boundary_2026-05-27.json`

## Question

The live C3 route now needs a physical source direction in the
three-dimensional C3-invariant Hermitian tangent space.  The repo already has
support that an orientation-preserving determinant criterion selects the
subgroup `C3 = A3` from `S3`, and quark-sector support that the oriented C3
normal form contains a reflection-odd splitter.

Does that material select the Y_T top source tangent?

## Answer

No.  The positivity/orientation row selects the `C3` subgroup at the
group-theory level.  The oriented splitter row identifies the
reflection-odd axis

```text
K_C3 = (C - C^2) / (i sqrt(3)).
```

Neither result selects the full physical source tangent or the top-line
source-generator matrix element.

There are two separate boundaries:

1. `C3` subgroup selection allows the full C3 Hermitian commutant
   `span(B_a, B_x, B_y)`, so the source direction remains free.
2. If one additionally chooses the orientation-odd splitter axis, that is a
   degeneracy-splitting direction, not a Y_T source coefficient theorem.  Pure
   `B_y` gives top-line responses `{0, -1/sqrt(2), +1/sqrt(2)}` across the
   three C3 spectral lines, not a derived `1/sqrt(6)` coefficient, and the
   physical top-line assignment remains open.

## Finite Witness

Let

```text
B_a = I / sqrt(3),
B_x = (C + C^2) / sqrt(6),
B_y = i(C - C^2) / sqrt(6).
```

Under a reflection `R C R = C^2`:

```text
R B_a R = B_a,
R B_x R = B_x,
R B_y R = -B_y.
```

Thus `B_y` is the orientation-odd splitter axis, while `B_a` and `B_x` are
orientation-even.  But positivity/orientation selection of the subgroup `C3`
does not by itself remove the even axes.

For the C3 spectral projectors `P_0, P_ω, P_{ω^2}`, the pure orientation-odd
unit tangent responses are:

```text
Tr(P_0 B_y)     = 0,
Tr(P_ω B_y)     = -1/sqrt(2),
Tr(P_{ω^2} B_y) = +1/sqrt(2).
```

So even the strongest orientation-axis reading still does not produce the Y_T
coefficient without an additional theorem specifying the physical top line,
source normalization, and source-generator matrix element.

## What This Prunes

This prunes:

```text
positivity/orientation C3 selection
  -> coefficient-certified Y_T source direction.
```

It also prunes:

```text
orientation-odd splitter axis alone
  -> y_t/g source coefficient 1/sqrt(6).
```

## What Remains Live

The live positive routes are unchanged:

```text
derive accepted same-surface C3 generation dynamics and source law
  -> top spectral line and source-generator matrix element
  -> sparse top/W response certificate.
```

or:

```text
produce strict same-source top/W pole-response evidence directly.
```

## Relation To Existing Support

- [`POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md`](POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md)
  selects `C3` from `S3` only under an admitted orientation-preserving subgroup
  criterion and explicitly leaves the bridge from framework positivity to the
  hw=1 triplet open.
- [`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`](QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md)
  identifies the C3-oriented splitter and explicitly leaves a source/readout
  theorem open.
- [`YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md`](YT_C3_SOURCE_DIRECTION_SELECTION_NO_GO_NOTE_2026-05-27.md)
  shows unit source normalization fixes scale, not C3 direction.
- [`YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md`](YT_LSP_PROJECTIVE_C3_SOURCE_DIRECTION_BOUNDARY_NOTE_2026-05-27.md)
  shows projective readout support also does not select the direction.

This note only prevents an overbroad use of positivity/orientation support. It
does not weaken that support and does not refute the C3 spectral route.

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive `y_t`, `m_t`, or a physical top/W response ratio;
- derive the accepted same-surface C3 dynamics or source law;
- derive the physical top spectral line or top-line ordering;
- refute positivity/orientation support;
- refute the C3 spectral mass-eigenprojector route;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  targets, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
proposal_allowed_reason: |
  Positivity/orientation support selects C3 at subgroup level and can identify
  an orientation-odd splitter axis, but it does not derive the physical Y_T
  source tangent, top-line assignment, or source-generator matrix element.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive physical C3 source direction from same-surface dynamics,
  or produce strict same-source top/W pole-response evidence.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_positivity_orientation_c3_source_direction_boundary.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
