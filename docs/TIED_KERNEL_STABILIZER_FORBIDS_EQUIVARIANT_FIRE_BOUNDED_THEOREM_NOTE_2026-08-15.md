---
claim_id: tied_kernel_stabilizer_forbids_equivariant_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether the G+ stabilizer of the tied occupancy kernels at the two positive two-ball sites contains an element swapping the tied slots, and whether that forbids every cube-equivariant firing labeling, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/tied_kernel_stabilizer_forbids_equivariant_fire_2026_08_15.py
---

# The Stabilizer Of A Tied Occupancy Kernel Forbids Equivariant Fire

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** finite `G+` of order 24 acting in the 3-vector representation on
the two declared tied occupancy kernels. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/tied_kernel_stabilizer_forbids_equivariant_fire_2026_08_15.py`](../scripts/tied_kernel_stabilizer_forbids_equivariant_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment context from the equal-`n` and opposite-label firings
(`#6648`/`#6649`, `#6646`/`#6649`): the two positive two-ball sites carry
tied `+x`/`-x` slots with a common occupancy kernel `n` on those neighbors,
while a firing at either site requires opposite `{+,−}` letters on those
two slots. A leftover slot-odd rule can fire, but it is not
`G+`-equivariant. That leftover-char of slotn is not the residual here.

Let `G+` be the 24 proper cube rotations. The action is the ordinary
3-vector representation: `g · n` is the rotated vector. The declared
kernels are

```text
n1 = (0, 1/3, −1/3)   at site v1,
n2 = (0, −1/3, 1/3)   at site v2.
```

Tied slots at both sites are `+x` and `−x`. Write

```text
Stab(n) = { g in G+ : g · n = n }.
```

**Theorem 1.** `|Stab(n1)| = |Stab(n2)| = 2`. In each stabilizer the
non-identity element sends `+x` to `−x` (and `−x` to `+x`). Explicitly
that element is the rotation `x ↦ −x`, `y ↦ −z`, `z ↦ −y`.

**Theorem 2.** Every `G+`-equivariant `{+,−}` labeling of the six slots
that depends on `n` is invariant under `Stab(n)`. Because a stabilizer
element swaps the tied slots, the two slots receive the same letter
whenever the neighbors share that `n`. Combined with the investment that
firings have opposite `x`-labels, no `G+`-equivariant local rule fires at
that site. The slot-odd opposite-`x` assignment is a non-equivariant
witness: it fires and fails stabilizer invariance. This is not
leftover-char of slotn.

**Theorem 3.** Displayed, not adopted. Do not write Stab into Admissibility.
Do not attach L1. Finite `G+` = 24 only. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite enumeration of the 24 proper cube rotations computes Stab(n1) and Stab(n2) exactly and shows a tied-slot swap, which forces every equivariant {+,-} labeling to use the same letter on +x and -x."
trace_class: frontier_discovery
target_claim_id: tied_kernel_stabilizer_forbids_equivariant_fire
target_blocker_text: "whether the G+ stabilizer of the tied occupancy kernels swaps the tied slots and thereby forbids every cube-equivariant firing labeling"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for finite G+ of order 24 and the two declared kernels; Stab is displayed, not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "independent audit of the displayed finite stabilizer report; do not adopt Stab as axiom content"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Objects

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility covariance clause is quoted only as the existing
spatial-covariance contract. It is not edited. In particular this note does
not insert `Stab` into that clause.

Declared mathematical scaffolding, not a new axiom:

- `G+` is exactly the 24 determinant-`+1` signed permutations of the three
  coordinate axes (finite `G+` = 24 only);
- the six neighbor slots are `±x`, `±y`, `±z`;
- `n1` and `n2` are the two declared tied occupancy kernels above;
- a `{+,−}` labeling depending on `n` is a function
  `λ(slot, n) ∈ {+, −}`;
- `G+`-equivariance means `λ(g · slot, g · n) = λ(slot, n)`.

Investment statements `#6646`/`#6648`/`#6649` are used only as the
equal-`n` / opposite-`x`-label firing context. They are not re-proved here
and are not given an audit verdict.

## Theorem 1 — orders and the tied-slot swap

Every `g ∈ G+` is a signed permutation matrix of determinant `+1`. For
`g · n1 = n1`, the unique zero coordinate of `n1` forces `g` to send the
`x`-axis to the `x`-axis. The eight such rotations are the stabilizer of
the unsigned `x`-axis. Direct evaluation on `n1 = (0, 1/3, −1/3)` leaves
exactly two survivors:

1. the identity, which fixes every slot;
2. `s : (x, y, z) ↦ (−x, −z, −y)`, which sends `+x` to `−x`.

The same pair is `Stab(n2)`, because `s · n2 = n2` as well. Thus
`|Stab(n1)| = |Stab(n2)| = 2`, and each stabilizer contains an element
swapping the tied slots.

Orbit-stabilizer is consistent and unused as an extra premise: the `G+`
orbit of `n1` has `24/2 = 12` distinct images.

## Theorem 2 — equivariant labels cannot fire

Restrict equivariance to `g ∈ Stab(n)`. Then `g · n = n`, so
`λ(g · slot, n) = λ(slot, n)`. Taking the swapper `s` of Theorem 1 gives

```text
λ(−x, n) = λ(+x, n).
```

The six slots are paired by `s` into `{+x, −x}`, `{+y, −z}`, and
`{−y, +z}`. There are therefore `2^3 = 8` stabilizer-invariant labelings
of the six slots at a fixed `n`, and every one of them gives `+x` and `−x`
the same letter.

There are `32` labelings with opposite `x`-letters. None of them is
stabilizer-invariant. Combined with the investment that a firing requires
opposite `x`-labels, no `G+`-equivariant local rule fires at `v1` or `v2`
for these kernels.

A slot-odd assignment with `λ(+x) ≠ λ(−x)` is a firing witness that fails
stabilizer invariance, hence fails `G+`-equivariance. That is one
non-equivariant rule. It is not leftover-char of slotn, and this note does
not attach L1.

If no stabilizer element had swapped the tied slots, opposite labels would
have been stabilizer-allowed. That counterfactual does not occur for `n1`
or `n2`.

## Theorem 3 — displayed, not adopted

`Stab` is a reported finite-group invariant of the declared kernels.
Displayed, not adopted. Do not write Stab into Admissibility. Do not
attach L1. Finite `G+` = 24 only. No axiom edit.

## Mutation Checks

1. The identity lies in both stabilizers and does not swap `+x` with `−x`;
   the swapper is a distinct second element.
2. Replacing `G+` by a single orientation-reversing signed permutation can
   enlarge the set that fixes `n1`, so the order-`2` count is specific to
   determinant `+1`.
3. Any opposite-`x` labeling, including slot-odd, fails the stabilizer
   invariance test used in Theorem 2.

## What This Does Not Claim

- `Stab` is not added to Admissibility, Lattice, Qubit, or Record.
- The leftover-char of slotn is not reused and L1 is not attached.
- Continuous `SO(3)`, a larger octahedral group, or any group other than
  the 24 proper cube rotations is outside the theorem.
- The investment that firings need opposite `x`-labels is not re-derived.
- No formation rule, Record lock, or physical occupancy process is selected.
- No no-go against non-equivariant rules is claimed: slot-odd remains a
  non-equivariant firing witness.

These are scope boundaries. Accordingly no no-go verdict is authored here.

## Primary Runner

The primary runner enumerates the 24 rotations, computes both stabilizers,
checks the tied-slot swap, exhausts the `64` six-slot labelings for
stabilizer invariance, and pins the displayed-not-adopted / no-L1 / no
axiom-edit boundary. It writes no runner cache and authors no audit
verdict.
