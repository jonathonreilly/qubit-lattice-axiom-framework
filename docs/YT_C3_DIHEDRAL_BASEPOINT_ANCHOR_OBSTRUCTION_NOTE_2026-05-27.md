---
claim_id: yt_c3_dihedral_basepoint_anchor_obstruction_note_2026-05-27
claim_type: no_go
actual_current_surface_status: no-go / open physical basepoint anchor law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Dihedral Basepoint Anchor Obstruction

**Date:** 2026-05-27  
**Status:** no-go for deriving the physical nontrivial top line from the
existing C3/dihedral reflection structure alone. This note does not claim
retained or proposed-retained `Y_T` closure.  
**Runner:** `scripts/frontier_yt_c3_dihedral_basepoint_anchor_obstruction.py`  
**Output:**
`outputs/yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json`

## Question

The previous orbit-member covariance no-go showed that C3 covariance cannot
select a representative of a selected free phase orbit. Can the remaining
physical basepoint be supplied by the already-present reflection/dihedral
structure, without adding a new same-surface physical readout law?

## Answer

No.

On the primitive selected orbit

```text
{phi = 0, 2 pi/3, 4 pi/3},
```

the C3 generator cycles the three members. Full C3 or D3 naturality therefore
cannot select one member: C3 already acts freely and transitively.

The existing real-record reflection axis is the one used earlier to exchange
the two nontrivial character lines. On the primitive orbit it fixes the real
axis member

```text
phi = 0 -> P_0 -> A/sqrt(3)
```

and swaps the two target-row members

```text
phi = 2 pi/3 <-> 4 pi/3
P_omega2 <-> P_omega.
```

So the reflection/basepoint structure already available on the current
surface does not exclude `P_0`; it fixes it. Choosing one of the rotated
reflection axes would fix a nontrivial member, but the choice of that rotated
axis is exactly an extra C3 basepoint/section input. It is not derived by
C3/D3 naturality.

## Assumptions / Imports Exercise

Minimal premise set:

- finite C3 action on the selected primitive phase orbit;
- the existing record reflection `R_0` with `R_0 C R_0 = C^2`;
- finite C3 spectral-line response algebra from the current stack;
- the previous phase-orbit and orbit-member covariance no-gos;
- no observed masses, fitted selectors, target values, or old Ward authority.

Load-bearing attempts rejected:

1. **Full C3/D3 naturality.** Fails because the group action is transitive;
   no member is invariant under the C3 generator.
2. **Existing real-record reflection.** Fails for positive closure because
   it fixes the singlet member `phi=0`, not a nontrivial line.
3. **Rotated reflection axis.** Fails as a derivation because selecting which
   reflected axis is physical is equivalent to adding the missing basepoint
   section.
4. **Orientation sign.** Already pruned as sufficient data; it does not
   derive a quantitative phase/member law or W/top matrix elements.
5. **Strict pole rows.** Still live, but absent on the current branch.

Forbidden proof inputs are absent: `H_unit`, old Ward authority,
`yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets,
`alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors, and target value
insertion.

## First-Principles / Elon Exercise

The hard premise being tested is:

```text
existing same-surface C3/dihedral reflection data
  -> physical basepoint anchor excluding P_0.
```

Adversarial stress tests:

- If the law is C3-natural, it has to commute with the free C3 action. No
  fixed section exists.
- If the law uses the already-derived real-record reflection axis, the fixed
  member is the real-axis singlet.
- If the law uses a rotated reflection axis, the rotation label is a new
  physical basepoint import.
- If the law breaks the symmetry to one of the two nontrivial members, the
  breaking is the desired theorem, not a consequence of the existing inputs.

Thus the route is blocked at the exact point the prior handoff named:
accepted physical orientation/basepoint authority remains load-bearing.

## Finite Witness

Index the primitive orbit members by `0,1,2`:

```text
0 -> phi = 0        -> P_0      -> A/sqrt(3)
1 -> phi = 2 pi/3   -> P_omega2 -> A/sqrt(12)
2 -> phi = 4 pi/3   -> P_omega  -> A/sqrt(12)
```

The C3 generator acts as

```text
k -> k + 1 mod 3.
```

The existing real-record reflection is

```text
R_0: k -> -k mod 3.
```

It fixes only `k=0`, the singlet row, and swaps `k=1` with `k=2`. The other
two reflections fix `k=1` and `k=2`, respectively, but choosing either of
those reflection axes is equivalent to choosing the nontrivial orbit member by
hand.

## Stuck Fan-Out

| Attack frame | Outcome |
|---|---|
| C3-invariant section | no section exists on a free orbit |
| Full D3-natural section | no section exists because C3 is a subgroup |
| Existing record reflection axis | fixed member is `P_0`, giving `A/sqrt(3)` |
| Rotated reflection axis | can target `P_omega` or `P_omega2`, but imports the basepoint |
| Strict pole-row bypass | remains live, but branch artifacts still mark it absent |

## No-Go Audit

This prunes the shortcut:

```text
existing C3/dihedral reflection structure
  -> physical basepoint/orbit-member anchor excluding P_0
  -> nontrivial C3 physical top line
  -> A/sqrt(12).
```

The implication is false on the actual current surface. The existing
reflection anchor fixes the singlet row, while a nontrivial reflected axis is
an extra physical basepoint import.

## Literature / Math Search

No external numerical, phenomenological, or literature value is load-bearing.
The runner performs the finite D3 action enumeration directly. Standard
finite-group terms such as "free action", "transitive action", and
"reflection axis" are used only as mathematical notation.

## What Remains Open

Positive closure still requires one of:

- accepted strict same-source top/W pole rows with contact, FV/IR, and
  model-class controls; or
- an accepted same-surface physical orientation/basepoint/orbit-member theorem
  that excludes `P_0` and supplies W/top source-generator matrix elements on
  one accepted backend.

## Non-Claims

This note does not:

- claim retained or proposed-retained `Y_T` closure;
- refute a future accepted physical basepoint theorem;
- refute future strict W/top pole rows;
- derive the accepted Y_T phase potential;
- isolate the physical top pole;
- derive `m_t`, physical-scale `g_2`, or numerical `y_t(v)`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go / open physical basepoint anchor law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  Full C3/D3 naturality cannot select a member of a free phase orbit, and the
  existing real-record reflection axis fixes the singlet member P_0. Rotated
  reflection axes can fix nontrivial members only after importing the missing
  physical basepoint section. The actual surface still lacks accepted
  physical basepoint/orbit-member authority or strict W/top pole rows.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: produce accepted strict top/W pole rows, or derive an accepted
  same-surface physical orientation/basepoint/orbit-member top-line law with
  W/top matrix elements
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_dihedral_basepoint_anchor_obstruction.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
