---
claim_id: yt_c3_orbit_member_readout_covariance_no_go_note_2026-05-27
claim_type: no_go
actual_current_surface_status: no-go / open orbit-member readout law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Orbit-Member Readout Covariance No-Go

**Date:** 2026-05-27  
**Status:** no-go for deriving the physical nontrivial top line from C3
orbit-member covariance alone. This note does not claim retained or
proposed-retained `Y_T` closure.  
**Runner:**
`scripts/frontier_yt_c3_orbit_member_readout_covariance_no_go.py`  
**Output:**
`outputs/yt_c3_orbit_member_readout_covariance_no_go_2026-05-27.json`

## Question

The previous phase-orbit selector no-go showed that a real C3-invariant scalar
phase potential can select a phase orbit, not a physical member of that orbit.
Can the missing member/readout law be derived from C3 covariance itself, so
that `P_0` is excluded and the physical top line is forced to be
`P_omega` or `P_omega2`?

## Answer

No.

On a strict C3 phase orbit

```text
O_phi = {phi, phi + 2 pi/3, phi + 4 pi/3},
```

the C3 action on orbit members is free.  Therefore the quotient map

```text
q: O_phi -> O_phi / C3
```

has no C3-equivariant section.  A section would have to choose one member
`s(q(O_phi))` while satisfying

```text
s(q(O_phi)) = g s(q(O_phi))
```

for the generator `g`, which is impossible on a free three-member orbit.

If equivariance is relaxed, there are three equally C3-compatible
symmetry-breaking sections.  On the primitive cubic orbit they give different
top rows:

```text
section 0: phi = 0        -> P_0      -> A/sqrt(3)
section 1: phi = 2 pi/3   -> P_omega2 -> A/sqrt(12)
section 2: phi = 4 pi/3   -> P_omega  -> A/sqrt(12)
```

Thus C3 covariance alone cannot supply the needed orbit-member law.  A
positive route must add an accepted physical anchor: a same-surface
orientation/basepoint/readout theorem that excludes the singlet member and
supplies W/top matrix elements, or strict top/W pole rows.

## First-Principles / Elon Exercise

Minimal premise set used:

- finite C3 action on the connected unit phase circle;
- finite C3 spectral projectors and line-response algebra;
- already-derived `B_x` source tangent and same-surface factorization support;
- the previous phase-orbit selector no-go as the immediate dependency;
- no observed masses, fitted selectors, or target values.

Adversarial checks:

1. **Equivariant section.** Fails. A free C3 orbit has no fixed member, so a
   C3-equivariant section of the orbit quotient cannot exist.
2. **C3-invariant scalar potential plus readout covariance.** Fails. The
   potential selects the orbit; covariance does not choose a representative.
3. **Symmetry-breaking section.** Fails as closure. The three sections are
   equally admissible before adding a physical anchor, and one selects `P_0`.
4. **Choose the nontrivial section.** Not allowed as a proof. That is exactly
   the missing same-surface orbit-member/top-line premise.
5. **Use strict rows instead.** Still live, but absent on the current branch.

Forbidden proof inputs are absent: `H_unit`, old Ward authority,
`yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets,
`alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors, and target value
insertion.

## Finite Witness

For

```text
H(phi) = cos(phi) B_x + sin(phi) B_y,
```

the strict primitive orbit has three possible member sections:

```text
phi = 0        -> top line P_0      -> |dM_t/dell| = A/sqrt(3)
phi = 2 pi/3   -> top line P_omega2 -> |dM_t/dell| = A/sqrt(12)
phi = 4 pi/3   -> top line P_omega  -> |dM_t/dell| = A/sqrt(12)
```

The same statement holds on a generic strict orbit: C3 translation cycles the
largest line through `P_0`, `P_omega2`, and `P_omega`.  The readout choice,
not the orbit or C3 covariance, determines which row is read.

## No-Go Audit

This prunes the shortcut:

```text
C3-covariant orbit-member/readout structure
  -> nontrivial C3 physical top line
  -> A/sqrt(12).
```

The implication is false on the actual current surface.  C3 covariance
forbids an equivariant section of a free orbit, and symmetry-breaking sections
include a singlet-row witness.  The missing object is an accepted physical
anchor for the orbit member, not another C3 invariance condition.

## Literature / Math Search

No external numerical, phenomenological, or literature value is load-bearing.
The runner performs the finite math search directly: it classifies sections of
the three-member C3 orbit, checks that no equivariant section exists, and
enumerates the three symmetry-breaking section witnesses.  Standard group
action language is used only as mathematical notation, not as an imported
physics authority.

## What Remains Open

Positive closure still requires one of:

- accepted strict same-source top/W pole rows with contact, FV/IR, and
  model-class controls; or
- an accepted same-surface orientation/basepoint/orbit-member readout theorem
  that excludes `P_0` and supplies W/top source-generator matrix elements on
  one accepted backend.

## Non-Claims

This note does not:

- claim retained or proposed-retained `Y_T` closure;
- refute a future accepted orbit-member/readout theorem;
- refute future strict W/top pole rows;
- derive the accepted Y_T phase potential;
- isolate the physical top pole;
- derive `m_t`, physical-scale `g_2`, or numerical `y_t(v)`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go / open orbit-member readout law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  C3 covariance does not choose a physical member of a free C3 phase orbit.
  There is no C3-equivariant section of the orbit quotient, and the three
  symmetry-breaking sections include a singlet-row witness as well as the two
  target-row witnesses.  The actual surface still lacks an accepted physical
  orbit-member/readout law or strict W/top pole rows.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: produce accepted strict top/W pole rows, or derive an accepted
  same-surface orientation/basepoint/orbit-member top-line law with W/top
  matrix elements
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_orbit_member_readout_covariance_no_go.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
