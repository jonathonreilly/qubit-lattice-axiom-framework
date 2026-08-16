---
claim_id: july3_k3_pair_occupied_slot_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the July-3 unique k=3 chiral-pair 6-tuples, the occupied-slot count min/max/histogram, and whether that min exceeds the seed-grown front’s max occupied NN of 3, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/july3_k3_pair_occupied_slot_census_2026_08_15.py
---

# Occupied-Slot Census Of The July-3 Unique k=3 Chiral Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupied-slot counts on the two proper-cubic orbits that
form the unique `k = 3` chiral pair of six-direction condition 6-tuples.
The histogram is displayed on that named alphabet model. It is not adopted
as Admissibility content and is not attached to L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/july3_k3_pair_occupied_slot_census_2026_08_15.py`](../scripts/july3_k3_pair_occupied_slot_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

July-3 Theorem 3 isolates a unique chiral pair at three condition letters:
the two `G+` orbits of handed fully-mixed 6-tuples. Letters are `{0,1,2}`
with `0` the empty/unread letter. The occupied-slot count of a 6-tuple is
the number of nonzero slots.

Direct enumeration of those two orbits gives `N_pair = 48` tuples (two
orbits of size 24). Every member has occupied-slot count exactly 4. The
histogram is therefore `{4: 48}`, with minimum 4 and maximum 4.

The seed-grown front bound used for comparison is the need6 geometry fact
that a seed-grown front site has at most 3 occupied nearest neighbors
(`#6636`). Because every pair member has 4 occupied slots, no such front
site can present a 6-tuple that equals any pair member.

This is not leftover-char of pluschi, which inspected the single lex-first
representative `(0,1,0,2,1,2)` and asked whether that one tuple fires. It
is not need6, which is a front-geometry bound only. The census is over
every tuple in both chiral orbits.

The histogram is displayed, not adopted. It is not written into
Admissibility. It is not attached to L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite orbit listing of the unique k=3 chiral pair and the occupied-slot histogram on that set are exact; the front comparison uses the cited max occupied-NN bound of 3; no axiom sentence is rewritten."
trace_class: negative_route_pruning
target_claim_id: july3_k3_pair_occupied_slot_census
target_blocker_text: "among all 6-tuples in the two chiral G+ orbits, whether the occupied-slot minimum is at least 4, so a seed-grown front with max occupied NN of 3 cannot match any pair member"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact on the July-3 named k=3 alphabet model with 0 unread; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded census; do not write the histogram into Admissibility and do not attach L1"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

Quoted from the live memo, verbatim:

```text
Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

A site with no record cannot be read.
```

This note does not choose that rule and does not add a histogram clause to
it. Letter `0` is the empty/unread letter on the July-3 three-letter
model. Occupied means nonzero. The note does not assign a readout value to
absence.
- **July-3 Theorem 3.** At `k = 3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns: every axis bi-colored with
  two distinct values, every value used twice. The runner re-earns the
  pair by enumerating `G+` orbits; it does not import an external list.
- **Cited comparison bound, not re-derived.** Seed-grown front sites have
  at most 3 occupied nearest neighbors (`#6636`, need6 geometry). That
  integer is a comparison input. This note does not re-prove front growth.
- **External empirical inputs:** none.
- **Not attached:** L1 is not a premise and is not a conclusion. The
  census is not leftover-char of pluschi.

## Exact Objects

The six nearest-neighbor directions, in the July-3 order, are

```text
(+x, -x, +y, -y, +z, -z).
```

A `k = 3` condition 6-tuple is an element of `{0,1,2}^6`. Letter `0` is
empty/unread. The occupied-slot count is

```text
occ(c) = |{ i in {0,...,5} : c_i != 0 }|.
```

`G+` is the 24-element proper cubic group of determinant-`+1` signed
permutation matrices. It acts on 6-tuples by the induced permutation of
the six axis directions. Spatial inversion `P = -I` is the central
improper element; it swaps opposite directions and therefore exchanges
some `G+` orbits.

A chiral pair is a pair of distinct `G+` orbits exchanged by `P`. July-3
Theorem 3 states there is exactly one such pair at `k = 3`. Write
`Pair` for the union of those two orbits, and `N_pair = |Pair|`.

The seed-grown front comparison integer is

```text
occ_front_max = 3.
```

## Theorem 1 — Occupied-Slot Census On The Unique Pair

`N_pair = 48`. The occupied-slot minimum on `Pair` is 4, the maximum is
4, and the histogram is `{4: 48}`.

*Proof.* The 24 proper signed permutation matrices are generated
exhaustively. Their action on the 729 colorings `{0,1,2}^6` partitions
them into 57 `G+` orbits, matching the July-3 Burnside count. Exactly two
of those orbits fail to meet their `P`-images; they form one pair, and
each has size 24, so `N_pair = 48`. The lex-first representatives are

```text
(0,1,0,2,1,2)    and    (0,1,0,2,2,1).
```

Every tuple in `Pair` is fully mixed: each axis is bi-colored and the
letter counts are `2/2/2`. In particular letter `0` occurs twice, so

```text
occ(c) = 6 - 2 = 4
```

for every `c` in `Pair`. Direct counting of the 48 tuples reproduces the
same histogram `{4: 48}`.

## Theorem 2 — Front Sites Cannot Match Any Pair Member

The occupied-slot minimum on `Pair` is at least 4. Compared with the
cited seed-grown front bound `occ_front_max = 3` (`#6636`), no
seed-grown front site can present a 6-tuple equal to any member of
`Pair`.

*Proof.* Theorem 1 gives `min occ(Pair) = 4`. A site whose occupied
nearest-neighbor count is at most 3 has `occ <= 3`, so it lies outside
`Pair`. Equality of 6-tuples would require equal occupied-slot counts.
The mismatch is therefore on every pair member, not on a single
representative.

This is a support-count obstruction on the named `k = 3` model. It does
not assert that the physical admissibility rule is the chiral pair, and
it does not identify the three letters with a derived physical alphabet.

## Theorem 3 — Displayed, Not Adopted

The histogram `{4: 48}` is a finite report on the July-3 named alphabet
model. It is displayed. It is not adopted.

In particular:

- the histogram is not written into Admissibility;
- no axiom sentence is edited;
- the census is not attached to L1.

Admissibility continues to say only that there is one fixed
nearest-neighbor rule, covariant under translations and proper cubic
rotations, and that the local distribution varies with the
nearest-neighbor conditions. Which histogram a named test alphabet
happens to carry is not that rule.

## What This Note Does And Does Not Claim

- **It does claim** the exact pair cardinality, the occupied-slot
  min/max/histogram, and the comparison `4 > 3` against the cited front
  bound.
- **It does not claim** that pluschi's leftover-char on
  `(0,1,0,2,1,2)` is the pair obstruction. That representative does have
  two empty slots, but so does every other pair member.
- **It does not claim** need6. Need6 is the front-geometry bound that a
  seed-grown front site has at most 3 occupied nearest neighbors. This
  note only compares its census to that integer.
- **It does not adopt** the histogram as Admissibility content and does
  not attach L1.
- **It does not** select the physical condition alphabet, derive a
  formation process, or decide whether the framework's fixed rule is
  chiral.

## Machine-Readable Report

```text
N_pair = 48
occupied_min = 4
occupied_max = 4
occupied_histogram = {4: 48}
occ_front_max = 3
min_occupied_ge_4 = true
front_site_can_match_pair_member = false
displayed_not_adopted = true
attached_to_L1 = false
written_into_admissibility = false
```
