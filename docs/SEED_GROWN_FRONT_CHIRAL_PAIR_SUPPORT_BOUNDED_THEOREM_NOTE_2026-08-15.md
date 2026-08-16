---
claim_id: seed_grown_front_chiral_pair_support_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On Z^3 seed-grown ℓ¹ balls of radius 0..4, whether any next-shell site has 6 occupied neighbors — the support the July-3 k=3 chiral pair needs — is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/seed_grown_front_chiral_pair_support_2026_08_15.py
---

# Seed-Grown Front Support Of The July-3 Unique k=3 Chiral Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** integer geometry of seed-grown ℓ¹ occupancy balls of radius
`t = 0,1,2,3,4` on `Z^3`, scored only as six-neighbor occupancy of the next
shell. No new occupancy member is grown on a new patch. The unique `k = 3`
chiral pair of
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
is used only as the already-classified support that needs six occupied
neighbors. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none. It does not attach L1.
**Primary runner:**
[`scripts/seed_grown_front_chiral_pair_support_2026_08_15.py`](../scripts/seed_grown_front_chiral_pair_support_2026_08_15.py)

## Result Up Front

Let

`B_t = { v ∈ Z^3 : |v|_1 ≤ t }`

be the occupied seed-grown ℓ¹ ball of radius `t`, and let the next unread
shell be

`S_{t+1} = { v ∈ Z^3 : |v|_1 = t+1 }`.

The occupied six-neighbors of `v ∈ S_{t+1}` are those of the six axial
neighbors `v ± e_i` that lie in `B_t`.

The July-3 classification supplies exactly one chiral pair at condition
alphabet size `k = 3`. Its members are the handed fully-mixed patterns:
every axis is bi-colored with two distinct contents. That pattern is a
coloring of all six nearest-neighbor slots, so it can fire only when a site
has **six occupied neighbors**.

For each `t ∈ {0,1,2,3,4}` the maximum occupied six-neighbor count on
`S_{t+1}` is strictly less than 6, and the number of next-shell sites with
six occupied neighbors is exactly 0. The unique `k = 3` pair therefore has
empty support on every such front.

The displayed consequence is that seed-grown six-neighbor occupancy growth
cannot turn on that unique `k = 3` chiral channel. The consequence is
**displayed, not adopted**. It is not written into Admissibility. It is not
an occupancy primitive. It is not leftover character of the mixlab one-wave
census (that census closed eight labelings at `t = 1`); the residual scored
here is only ℓ¹-ball geometry versus the pair’s six-neighbor support.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The Record unread boundary used only to name the next shell as unread is:

A site with no record cannot be read.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

Occupancy in this note is the geometric set `B_t`. The axiom
does not supply the formation site, probability, or rate, and this
note does not add one.
Admissibility is not edited. The six-neighbor condition domain is used only
to identify which occupied slots a next-shell site can see.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact six-neighbor occupancy counts on seed-grown ℓ¹ shells of radius 1..5; the unique k=3 pair support is empty on those fronts. Displayed, not adopted."
trace_class: negative_route_pruning
target_claim_id: admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
target_blocker_text: "whether ordinary seed-grown six-neighbor occupancy growth can present the six occupied neighbors the unique k=3 chiral pair requires"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "If a later construction wants the unique k=3 pair on a growing front, it must supply a different occupancy set than the seed-grown ℓ¹ ball, or a different neighbor predicate than the six axial neighbors."
conditional_surface_status: "exact for B_t and S_{t+1} at t=0..4; not an Admissibility edit and not a physical formation law"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)` and `e_1, e_2, e_3` for the standard basis of `Z^3`.
The open six-neighbor set is

`N(v) = { v ± e_1, v ± e_2, v ± e_3 }`.

The taxicab norm is `|v|_1 = |v_1| + |v_2| + |v_3|`. Occupied neighbors of a
next-shell site are

`N_occ(v; t) = N(v) ∩ B_t`.

The fully-mixed `k = 3` support predicate used here is the occupancy
necessary condition only: `|N_occ(v; t)| = 6`. Distinct contents on each
axis are not scored; they cannot occur unless all six slots are occupied.

## Theorem 1 — Next-Shell Occupied Six-Neighbor Count Is At Most Three

For each `t ∈ {0,1,2,3,4}` and every `v ∈ S_{t+1}`,

`|N_occ(v; t)| = # { i ∈ {1,2,3} : v_i ≠ 0 } ≤ 3 < 6`.

*Proof.* Fix `v` with `|v|_1 = t+1` and an axis `i`.

- If `v_i > 0`, then `|v - e_i|_1 = t` and `|v + e_i|_1 = t+2`, so exactly
  one of the two axial neighbors lies in `B_t`.
- If `v_i < 0`, then `|v + e_i|_1 = t` and `|v - e_i|_1 = t+2`, again
  exactly one occupied axial neighbor.
- If `v_i = 0`, then both `|v ± e_i|_1 = t+2`, so neither axial neighbor
  lies in `B_t`.

Summing over the three axes gives the identity. A next-shell site has at
least one nonzero coordinate, so the count is in `{1,2,3}`. In particular
the maximum over `S_{t+1}` is strictly less than 6.

The same identity holds for every `t ≥ 0`. The executed census below
restricts to the requested radii `t = 0,1,2,3,4`.

## Theorem 2 — Unique k=3 Pair Support Is Empty On Each Front

Write `N_shell = |S_{t+1}|`, `max_occ_nn = max_{v ∈ S_{t+1}} |N_occ(v; t)|`,
and `N_with_6 = |{ v ∈ S_{t+1} : |N_occ(v; t)| = 6 }|`.

The primary runner enumerates every integer point in the box
`[-r, r]^3` with `r = t+1` and scores the next shell exactly. The finite
table is

| `t` | `N_shell` | `max_occ_nn` | `N_with_6` |
|---:|---:|---:|---:|
| 0 | 6 | 1 | 0 |
| 1 | 18 | 2 | 0 |
| 2 | 38 | 3 | 0 |
| 3 | 66 | 3 | 0 |
| 4 | 102 | 3 | 0 |

For every listed `t`, `max_occ_nn < 6` and `N_with_6 = 0`. Therefore the
July-3 unique `k = 3` pair has empty support on every such front: no unread
next-shell site presents the six occupied neighbors the fully-mixed
coloring requires.

As a shell-cardinality cross-check, `|S_r| = 4r^2 + 2` for each `r ≥ 1`,
so the five shell sizes are `6,18,38,66,102`.

Interior contrast, not a counterexample to the theorem: for `t ≥ 1` the
already-occupied origin has `|N(0) ∩ B_t| = 6`. The theorem scores only
unread sites on `S_{t+1}`.

## Theorem 3 — Displayed Non-Turn-On (Not Adopted)

Displayed: seed-grown six-neighbor occupancy growth on the ℓ¹ balls `B_t`
cannot turn on the unique `k = 3` chiral channel, because that channel’s
support is empty on every next shell scored in Theorem 2.

This line is **displayed, not adopted**. It is not an Admissibility clause,
not a physical rule determination, and not a claim that no other occupancy
set can ever present six occupied neighbors. It does not attach L1. It does
not grow a new occupancy member on a new patch.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current six-neighbor Lattice and Admissibility premises | quoted; no edit |
| current Record unread/lock/content boundary | quoted as naming only; no formation law added |
| July-3 unique `k = 3` fully-mixed pair | cited as already-classified support needing six occupied neighbors |
| occupied six-neighbor identity on `S_{t+1}` | proved by one-axis case analysis |
| census `t = 0..4` of `N_shell`, `max_occ_nn`, `N_with_6` | exact finite enumeration |
| `N_with_6 = 0` and `max_occ_nn < 6` | proved |
| Admissibility rewrite or occupancy primitive | not claimed; displayed, not adopted |
| mixlab leftover-character of eight `t = 1` labelings | not this residual |

## Boundary And Imports

No observation, fitted parameter, continuum limit, or new axiom is imported.
The occupancy set is the ordinary seed-grown ℓ¹ ball. Six-neighbor occupancy
is not a content coloring: the theorem stops at the necessary occupancy
count the fully-mixed pair requires.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the unique `k = 3` pair can fire on the next shell of a seed-grown ℓ¹ ball. |
| V2 | Current main classifies the pair but does not score its six-neighbor support on `B_t`. |
| V3 | The identity and the five-radius census are independently finite and exact. |
| V4 | The note is more than a restatement of Admissibility because it enumerates occupied six-neighbor counts on a named growing set. |
| V5 | The non-turn-on line is displayed, not adopted, so it is not a physical compiler or axiom sentence. |

## No-Go Discipline Gate

The negative content is narrow: on seed-grown ℓ¹ balls of radius `0..4`, no
next-shell site has six occupied six-neighbors. No global chirality
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| seed-grown ℓ¹ ball, six-neighbor occupancy | score `S_{t+1}` | executed; support empty |
| interior of `B_t` | score already-occupied sites | origin has six occupied neighbors for `t ≥ 1`; not an unread front |
| different occupancy set | occupy a set that is not an ℓ¹ ball | live; not scored |
| different neighbor predicate | replace six-neighbors by a larger star | different premise |
| content coloring on a full six-tuple | assign distinct axis contents | blocked already by missing occupancy |
| mixlab leftover-character at `t = 1` | enumerate eight labelings after one wave | closed elsewhere; not this residual |
| write the non-turn-on line into Admissibility | axiom edit | refused; displayed, not adopted |

### N2 — wall independence

Empty six-neighbor support on this occupancy set is independent of the
separate questions of which contents would occupy a full six-tuple, how
records form, and whether the physical rule is chiral. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The occupancy set is the ℓ¹ ball. The neighbor predicate is the six axial
neighbors. Radii are `t = 0,1,2,3,4`. The fully-mixed pair is used only
through its necessary occupancy count of six. Formation, contents, and
axiom edits are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies the cubic six-neighbor substrate and the
local-condition sentence. July-3 supplies the unique `k = 3` pair. The
residual scored here is the occupancy-support gap between those two
surfaces.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | every next-shell site in the `t = 0..4` boxes | no infinite-radius numeric table beyond the identity |
| per site | occupied six-neighbor count | no content coloring |
| per mode | no mode calculation | no spectral claim |
| per block | five radii and the one-axis identity | no new occupancy member |
| lattice wide | identity for all `t ≥ 0`; census only through `t = 4` | no physical rule determination |

### N6 — live partial-closure paths

Live routes are a different occupancy set, a different neighbor predicate,
or a separately derived reason that the physical rule does not use the
unique `k = 3` pair. Ordinary seed-grown ℓ¹ six-neighbor growth is no longer
a live route to turning that pair on.

### N7 — hostile steelman

**Steelman:** After a few growth steps the front should look locally like a
filled six-tuple, so the unique chiral pair should fire.

**Answer:** Six-neighbor steps change ℓ¹ radius by exactly one. A next-shell
site therefore sees only the inward axial unit on each of its nonzero
coordinates, hence at most three occupied six-neighbors, never six.

### N8 — cross-cycle echo

July-3 classified the pair; it did not score growing occupancy. The mixlab
one-wave leftover-character census closed eight labelings at `t = 1` and is
not reused here. This note does not reopen either surface.

**Gate disposition:** PASS for the finite occupancy census, the occupied
six-neighbor identity, and the empty unique-`k = 3` support on these fronts.
FAIL / DO NOT SHIP for “Admissibility is rewritten,” “the pair can never
fire on any set,” “records form on `S_{t+1}`,” or “L1 is attached.”

## Primary Runner

The primary runner enumerates `B_t` and `S_{t+1}` for `t = 0,1,2,3,4`,
recomputes `N_shell`, `max_occ_nn`, and `N_with_6`, checks the
nonzero-coordinate identity, pins the current Lattice / Admissibility /
Record sentences, and checks that the non-turn-on line is displayed, not
adopted. It writes no cache and authors no audit verdict.
