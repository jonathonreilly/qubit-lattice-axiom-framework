---
claim_id: skew_three_seed_delta_sign_product_execution_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether the delta-sign-product 6-tuple (+,0,+,−,0,−) fires the July-3 k=3 pair is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_delta_sign_product_execution_2026_08_15.py
---

# Delta-Sign-Product 6-Tuple Execution On The Off-Axis Three-Ball Union

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact membership and one-step execution of one displayed 6-tuple
on the locked union of three radius-2 taxicab balls, at one unread center.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_delta_sign_product_execution_2026_08_15.py`](../scripts/skew_three_seed_delta_sign_product_execution_2026_08_15.py)

No runner cache is written.

## Result Up Front

Let `B_2(s)` be the closed taxicab ball of radius 2 about `s` in `Z^3`.
The locked set is the already-occupied union

`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`.

The unread test site is `v = (-1,1,1)`. Direction order is
`(+x, -x, +y, -y, +z, -z)`. The displayed neighbor 6-tuple is the already
labeled delta-sign-product member

`c = (+, 0, +, −, 0, −)`.

This 6-tuple is used only as a neighbor-content assignment on the star of
`v`. It is not a leftover character computation: membership of `c` is an
input, and the residual scored here is one execution step of the July-3
`k=3` pair on that star.

Three exact statements survive.

1. `v` is not in `U`. After the step, every site of `U` remains locked.
2. The July-3 `k=3` pair fires at `v` for this `c`: `N_new=1`, and the new
   lock is `v`. The 6-tuple is a pair member.
3. The execution is displayed, not adopted. The 6-tuple is not written into
   Admissibility. This note does not attach L1. Do not attach L1. No
   fourth seed ball is introduced.

## Current Premise Boundary

The Lattice, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

*Reading notes (interpretive, non-governing).* (2) Read with Record, the
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site, probability,
or rate.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

The live Admissibility sentences do not name `c`, the delta-sign-product
rule, or the July-3 pair. Record supplies permanence of existing locks and
unreadability at absence. Formation of `v` is a displayed extra step, not
axiom content.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the locked three-ball union, the unread site v is outside U, the displayed 6-tuple is a July-3 k=3 pair member, and one pair step forms exactly v while leaving U locked. The 6-tuple and pair are displayed extras."
trace_class: upstream_support
target_claim_id: admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
target_blocker_text: "run the already-labeled delta-sign-product 6-tuple as a July-3 k=3 pair step at unread v on the locked three-ball union"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the 6-tuple and pair displayed; do not write them into Admissibility; do not attach L1; do not add a fourth seed ball."
conditional_surface_status: "exact for this U, this v, and this displayed 6-tuple; not an adopted law"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Seeds `S = {0, (2,0,0), (1,2,1)}`. Occupied set

`U = ∪_{s in S} B_2(s)`, `B_2(s) = {x in Z^3 : ||x − s||_taxicab ≤ 2}`.

The six-neighbor star at `v` is

`N(v) = {v ± e_1, v ± e_2, v ± e_3}`

in the order `(+x, -x, +y, -y, +z, -z)`, namely

`((0,1,1), (-2,1,1), (-1,2,1), (-1,0,1), (-1,1,2), (-1,1,0))`.

Letters are `{0, +, −}` with `0` empty. Encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`.
The July-3 `k=3` pair is the unique pair of proper-cube orbits of 3-letter
6-tuples that are not proper-equivalent to their inversion images. That set
has 48 members. A displayed pair step at an unread site forms that site if
and only if the encoded 6-tuple lies in the pair; existing locks are not
removed.

Only `U` and the star at `v` are scored.

## Theorem 1 — Unread Center And Permanence

Direct taxicab distances:

`||v − 0||_taxicab = 3`, `||v − (2,0,0)||_taxicab = 5`,
`||v − (1,2,1)||_taxicab = 3`.

Each exceeds 2, so `v ∉ U`. The six neighbors split as

| slot | neighbor | in `U` | `c` |
|---|---|---|---|
| `+x` | `(0,1,1)` | yes, `B_2(0)` | `+` |
| `−x` | `(-2,1,1)` | no | `0` |
| `+y` | `(-1,2,1)` | yes, `B_2((1,2,1))` | `+` |
| `−y` | `(-1,0,1)` | yes, `B_2(0)` | `−` |
| `+z` | `(-1,1,2)` | no | `0` |
| `−z` | `(-1,1,0)` | yes, `B_2(0)` | `−` |

After the step of Theorem 2, the locked set is `U ∪ {v}`. Every site of
`U` remains locked. Permanence is the Record sentence that records are
permanent, applied to the already-locked union; the step does not overwrite
those sites.

## Theorem 2 — Pair Membership And Fire

The encoded 6-tuple is

`encode(c) = (1, 0, 1, 2, 0, 2)`.

This coloring lies in the 48-member July-3 `k=3` pair. Therefore `c` is a
pair member. Because `v` is unread and `c` is a member, the displayed pair
step forms `v` and only `v`:

`N_new = 1`, new lock `= v`.

A same-support non-member, for example `(+, 0, +, +, 0, −)`, does not fire.
The all-empty 6-tuple does not fire. A second step at the already-locked
`v` adds no further lock.

## Theorem 3 — Displayed, Not Adopted

Displayed, not adopted. The live Admissibility memo still says only that
one fixed nearest-neighbor rule exists and that the local distribution is
determined by nearest-neighbor conditions. It does not name `c`, the
delta-sign-product labeling, or the July-3 pair. This note does not write
`c` into Admissibility. This note does not attach L1. Do not attach L1. No
fourth seed ball is added. Cube covariance of the labeling, nearest-neighbor determinacy of
the product, and any physical selection among pair members remain unclaimed.

## Honest-Auditor / Boundary

The theorem is finite exact algebra on one locked union and one star. It
does not select a physical admissibility rule, does not derive formation
rate, and does not enlarge the axiom memo. Hostile reading: “a pair member
on a locked union is already the law.” Answer: membership and one displayed
step are not adoption; the axiom text is unchanged.

**Gate disposition:** PASS for unreadness of `v`, permanence of `U`, pair
membership of `c`, and `N_new=1` with new lock `v`. FAIL / DO NOT SHIP for
“Admissibility now contains `c`,” “L1 is attached,” or “a fourth seed ball
is required.”

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, the 48-member pair, the
one-step execution, the silent controls, and the display-only hygiene. It
authors no audit verdict.
