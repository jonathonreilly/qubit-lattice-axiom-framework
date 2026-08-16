---
claim_id: two_ball_slot_odd_tie_label_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On U at the two positive unread sites, whether the slot-odd tie-break of equal-n neighbors yields a July-3 pair member, and whether that tie-break is cube-equivariant on the star, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_slot_odd_tie_label_2026_08_15.py
---

# Two-Ball Slot-Odd Equal-n Tie Label

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the occupancy union `U = B_2(0) ∪ B_2((2,0,0))` and the two
positive unread 6-neighbor stars at `v1=(1,-1,1)` and `v2=(1,1,-1)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_slot_odd_tie_label_2026_08_15.py`](../scripts/two_ball_slot_odd_tie_label_2026_08_15.py)

Framework context on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The
July-3 `k=3` pair is the unique chiral pair of proper-cube orbits on
six-tuples with letters `{0,1,2}` constructed in
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
Theorem 3. That construction is used here as a finite coloring census. Its
ledger row is `unaudited`; this note does not inherit retained-grade status
from it.

## Result Up Front

On `U`, both positive unread sites have a unique-axis fragment and a pair of
ambiguous opposite neighbors with equal occupancy-kernel `n`. Completing the
tied pair by the displayed slot-odd rule — `label(+μ)=+` and `label(−μ)=−` —
produces

```text
c(v1) = (+, −, −, 0, 0, +)
c(v2) = (+, −,  0, +, −, 0)
```

in direction order `(+x,−x,+y,−y,+z,−z)`. Each 6-tuple is a July-3 `k=3`
pair member, so `N_fire=1` at each site.

The same completion, acting on a star by rotating `n` and the six slots
together, fails to commute with the 24 proper cube rotations: it commutes
for 3 of 24 rotations at each of the two stars. The displayed rule is
therefore not cube-equivariant on the star.

Displayed, not adopted. Do not write the slot-odd tie-break into
Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite occupancy arithmetic on one two-ball union and two 6-neighbor stars, plus a 24-element commutation count for a displayed star map. No physical rule is selected."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "when occupancy-kernel n is tied on opposite occupied slots, does a slot-odd completion fire the July-3 pair, and is that completion cube-equivariant on the star?"
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "keep the slot-odd map displayed only; do not adopt it as the fixed Admissibility rule"
conditional_surface_status: "exact on U and the two named stars; the displayed tie-break is not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

Lattice and Admissibility are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Lattice supplies the six directions. The occupancy set `U` is a displayed
ℓ¹ geometry, not a derived growth law. Record is used only to name unread
sites as sites off `U`. No formation rate, no scalar collection functional,
and no value at absence is used.

## Exact Objects

Write `B_2(p) = {x in Z^3 : ||x-p||_1 ≤ 2}` and

`U = B_2(0) ∪ B_2((2,0,0))`.

The runner lists `|U|=43`. The unread sites scored here are only
`v1=(1,-1,1)` and `v2=(1,1,-1)`. Direction order is

```text
(+x, −x, +y, −y, +z, −z).
```

An occupied neighbor of `v` is a 6-neighbor that lies in `U`. Empty slots
stay `0`. At an occupied neighbor `w`, the occupancy kernel is the
three-component difference of occupancy across opposite neighbors of `w`,

`n(w) = d(w)/3`, `d_μ(w) = 1_U(w+e_μ) − 1_U(w−e_μ)`.

If `n` has exactly one nonzero component, that slot is unique-axis and keeps
`sign` of that component as its letter in `{+,−}`. If two opposite occupied
slots carry the same `n` with more than one nonzero component, those slots
are tied. The displayed slot-odd completion sets

`label(+μ)=+`, `label(−μ)=−`.

July-3 pair membership uses letters `{0,1,2}` with `0` empty, `+ → 1`,
`− → 2`. The unique `k=3` chiral pair is the two proper-cube orbits
exchanged by inversion. That set equals the 48 fully-mixed axis-bicolored
6-tuples: each letter appears twice, and opposite slots differ. The runner
enumerates both presentations and checks they coincide.

A proper cube rotation `g` acts on a star by sending each slot `μ` to `gμ`
and each kernel `n` to `g n`. Letters move with their slots. The completion
is cube-equivariant when completing after `g` equals transporting the
completed letters by `g`, for every one of the 24 determinant-one signed
permutations of the axes.

## Theorem 1 — the two completed 6-tuples both fire

At `v1` the occupied mask is `(1,1,1,0,0,1)`. The `+x` and `−x` neighbors
both carry `n=(0, 1/3, −1/3)`, so they are tied. Unique-axis labels are
`+y ↦ −` and `−z ↦ +`. Slot-odd fills the tied pair as `+x ↦ +`, `−x ↦ −`,
hence

`c(v1)=(+, −, −, 0, 0, +)`.

At `v2` the occupied mask is `(1,1,0,1,1,0)`. The `+x` and `−x` neighbors
both carry `n=(0, −1/3, 1/3)`. Unique-axis labels are `−y ↦ +` and
`+z ↦ −`. Slot-odd again fills `+x ↦ +`, `−x ↦ −`, hence

`c(v2)=(+, −, 0, +, −, 0)`.

Both colorings lie in the 48-member July-3 pair, so each site has
`N_fire=1`. A local-in-`n` map cannot separate the tied pair; the displayed
rule uses the slot, not only `n`.

## Theorem 2 — slot-odd is not cube-equivariant on the star

Let `R` be the displayed completion (unique-axis signs on unambiguous
occupied slots; slot-odd on tied equal-`n` opposite slots). On each of the
two actual stars, `R(g · star) = g · R(star)` holds for 3 of the 24 proper
rotations and fails for the other 21. The three successes are the even
permutations of the three axes with all signs positive.

The obstruction is the named `+μ` versus `−μ` assignment: a proper rotation
that sends `+x` to `−x` transports `c(v1)` to a 6-tuple whose tied pair is
`(−, +)` on the image `x`-axis, while rebuilding `R` after the rotation
again writes `(+, −)` on that named axis. Therefore the displayed tie-break
is not equivariant under the 24 proper cube rotations of the star.

## Theorem 3 — displayed, not adopted

The two firings and the commutation count are a report on one displayed
completion of two stars on `U`. They do not select a physical
Admissibility rule. Do not write slot-odd into Admissibility. The axiom
memo is not edited.

## What this note does not claim

- It does not adopt slot-odd, unique-axis signs, or the two-ball union as
  the fixed nearest-neighbor rule.
- It does not claim cube covariance of any other tie-break, and it does not
  repair slot-odd by a further convention.
- It does not grow a new occupancy member, score any unread site other than
  `v1` and `v2`, or attach a larger box.
- It does not treat the July-3 census as retained-grade; the pair is
  reconstructed from the same proper-orbit definition used in the July-3
  source note.
- It supplies no dynamics, formation site, readout bridge, or comparator.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| reconstruct `U` and the two unread stars | ℓ¹ membership on the two radius-2 balls; masks as above |
| compute `n=d/3` at occupied neighbors | opposite-occupancy difference at each neighbor |
| complete unique-axis and tied slots | signs of unique components; slot-odd on equal-`n` pairs |
| test July-3 membership | both completions lie in the 48-member pair |
| test star equivariance | 3/24 proper rotations commute at each star |
| adopt the map as Admissibility | refused; displayed only |
