---
claim_id: yt_c3_real_record_reflection_even_source_theorem_note_2026-05-27
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T C3 Real-Record Reflection-Even Source Theorem

**Claim type:** bounded_theorem / exact support.
**Role:** derives the reflection-even source premise for the C3 `B_x` route
from real finite-record source semantics.
**Status:** exact support; no retained or proposed-retained Y_T closure by
this note.
**Primary runner:**
`scripts/frontier_yt_c3_real_record_reflection_even_source.py`
**Generated output:**
`outputs/yt_c3_real_record_reflection_even_source_2026-05-27.json`

## Question

After normalized RN/Fisher source semantics remove the identity direction, the
C3 tangent still has two connected directions:

```text
x B_x + y B_y.
```

This note asks whether the finite-record source law selects the
reflection-even direction by excluding the reflection-odd `B_y`.

## Answer

Yes, narrowly.  A primitive finite-record source generator is a real observable
on a finite record space.  In the retained real `hw=1` generation basis, the
C3 cycle `C` is a real permutation matrix.  The C3 Hermitian tangent basis is

```text
B_a = I/sqrt(3)
B_x = (C + C^2)/sqrt(6)
B_y = i(C - C^2)/sqrt(6).
```

The `B_a` and `B_x` matrices are real.  The `B_y` matrix is purely imaginary;
equivalently, the B_y matrix is purely imaginary in the real record basis
and reflection-odd.  Therefore a real finite-record source generator in this
C3 tangent space has `y=0`.

Combining with the normalized-RN connected-source theorem:

```text
real record source + normalized source
  -> connected and reflection-even
  -> B_x up to sign.
```

## Finite Algebra

Let `R` be the reflection that exchanges the two nontrivial C3 directions,
so that

```text
R C R = C^2.
```

Then

```text
R B_x R =  B_x,
R B_y R = -B_y.
```

For a general C3 Hermitian tangent

```text
G = a B_a + x B_x + y B_y,
```

the imaginary part is exactly the `y B_y` part.  Requiring `G` to be real in
the finite-record basis forces `y=0`.  After the connected-source theorem
removes `a B_a`, the only remaining unit direction is `B_x` up to sign.

## What This Burns Down

This burns down the second premise in the C3 source-direction route:

```text
reflection-even neutral source
```

is now exact support under real finite-record source semantics.

Together with
`YT_C3_CONNECTED_SOURCE_FROM_NORMALIZED_RN_THEOREM_NOTE_2026-05-27.md`, the
C3 source direction is `B_x` up to sign.

## What Remains Open

The remaining C3 route gate is now only:

```text
derive that the physical top row is a nontrivial C3 character line,
```

or bypass it with strict same-source top/W pole-response evidence.

The top-line boundary is still load-bearing because:

```text
top = P_0       -> |Tr(P_0 B_x)|      = 2/sqrt(6)
top = P_omega   -> |Tr(P_omega B_x)|  = 1/sqrt(6)
top = P_omega2  -> |Tr(P_omega2 B_x)| = 1/sqrt(6).
```

## Non-Claims

This note does not:

- claim retained or proposed-retained Y_T closure;
- derive the physical top C3 line;
- derive strict top/W pole-response evidence;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: |
  Real finite-record source semantics exclude the imaginary reflection-odd B_y
  tangent, and normalized RN source semantics remove B_a. The source direction
  is therefore B_x up to sign, but the nontrivial top-line assignment and
  strict top/W response evidence remain open.
bare_retained_allowed: false
audit_required_before_effective_retained: true
first_open_gate_after_this_note: nontrivial top-line assignment
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_real_record_reflection_even_source.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
