---
claim_id: nnseed_plaquette_holonomy_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from plaquette opposite-vertex holonomy on the nnseed seed-square Q and on the 4-cycle R containing A and B are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_plaquette_holonomy_reverse_face_2026_08_15.py
---

# Plaquette Opposite-Vertex Holonomy Reverse And Face On The Nnseed Seed-Square And On The Four-Cycle Containing A And B

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** own-incoming lock letters on the seed-square
`Q={0,(1,0,0),(1,1,0),(0,1,0)}` and on the 4-cycle
`R={(1,0,0),(1,1,0),(1,1,1),(1,0,1)}` of the displayed two-site nnseed
process, scored as reverse and face by opposite-vertex holonomy. The letter
at a recorded site is that site's own incoming lock in `{±e_i}`; seeds use
their seed letters. Uniqueness of incoming locks is not required. This is
not a leftover of star aggregation of six-neighbor lock lists. Occupancy
`n` is not used. Displayed, not adopted. This note does not write the
letters into Admissibility and does not attach a formation member from
plaquette opposite-vertex holonomy.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_plaquette_holonomy_reverse_face_2026_08_15.py`](../scripts/nnseed_plaquette_holonomy_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
together with the two named 4-cycles. Incoming lock letters are unit
nearest-neighbor steps. The scored letter is one such step when the incoming
set is a singleton, or a recorded non-unique incoming set. Star aggregation
of six-neighbor lock lists is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own-incoming locks, cycle sum H on the nnseed seed-square Q, and reverse fail plus face fail from opposite-vertex holonomy on Q and on the 4-cycle R containing A and B; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_plaquette_holonomy_reverse_face
target_blocker_text: "display reverse and face from plaquette opposite-vertex holonomy on the nnseed seed-square Q and on the 4-cycle R containing A and B, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the letters into Admissibility, do not reuse star aggregation of six-neighbor lock lists, do not use occupancy n, and do not require unique incoming locks."
conditional_surface_status: "exact on B_3(0) for own-incoming locks and opposite-vertex holonomy on Q and R; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

Letter at a recorded site `q` is `q`'s own unique incoming lock in `{±e_i}`
when that incoming set is a singleton. Seeds use their seed letters. If the
incoming set has more than one earliest step, the site is recorded with a
non-unique incoming set; uniqueness is not required, and the reverse/face
predicates then fail rather than becoming `UNDEFINED`.

## Face plaquette and reverse 4-cycle

Face plaquette, the seed-square, in cyclic order
`(0, e_1, e_1+e_2, e_2)`:

```text
Q = {0, (1,0,0), (1,1,0), (0,1,0)}.
```

Let `T_Q` be the first tick all four sites of `Q` are recorded. At `T_Q`
report the four own-incoming locks and the cycle sum

```text
H = L(0)+L(e_1)+L(e_1+e_2)+L(e_2).
```

Face holds iff opposite vertices have opposite locks:

```text
L(0)+L(e_1+e_2)=(0,0,0) and L(e_1)+L(e_2)=(0,0,0).
```

If any of the four is unrecorded in `B_3(0)`, face is `UNDEFINED`.

Reverse 4-cycle containing `A=(1,0,0)` and `B=(1,1,1)`, in cyclic order:

```text
R = {(1,0,0), (1,1,0), (1,1,1), (1,0,1)}.
```

At `T_R = min(t(A),t(B))` (formation ticks). Reverse holds iff all four of
`R` are recorded by `T_R` and opposite vertices have opposite locks:

```text
L(A)+L(B)=(0,0,0) and L(1,1,0)+L(1,0,1)=(0,0,0).
```

If some vertex of `R` is unrecorded at `T_R`, reverse is `UNDEFINED`. Else
fail.

The report is one of `hold`, `fail`, or `UNDEFINED`. Admissibility is not
edited. Letters are not written into Admissibility.

## Theorem 1 — ticks, own-incoming locks, and cycle sum

Direct enumeration of the displayed nnseed process on `B_3(0)` forms every
vertex of `Q` and of `R`.

```text
T_Q = 2
L(0) = +e_1
L(e_1) = −e_2
L(e_1+e_2) = +e_1
L(e_2) = +e_2
H = (2, 0, 0)

T_R = 2
L(A) = −e_2
L(1,1,0) = +e_1
L(B) = +e_1, +e_3
L(1,0,1) = +e_1
```

`T_Q=2` is the formation tick of `e_1=A`. The other three vertices of `Q`
are already recorded: the two seeds at tick 0 and `(1,1,0)` at tick 1.
`T_R=min(t(A),t(B))=min(2,2)=2`. All four vertices of `R` are recorded by
`T_R`: `(1,1,0)` at tick 1, and `A`, `B`, and `(1,0,1)` at tick 2.

Every vertex of `Q` has a unique incoming lock. `B` has two earliest
incoming steps `+e_1` and `+e_3`. That non-uniqueness is reported; uniqueness
is not required. The letters are the sites' own incoming locks. They are not
a leftover of star aggregation of six-neighbor lock lists.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if all four of `R` are recorded by `T_R` and
opposite vertices have opposite locks. All four of `R` are recorded by
`T_R=2`, so reverse is not `UNDEFINED`. `L(B)` is the non-unique pair
`+e_1, +e_3`, so `L(A)+L(B)=(0,0,0)` does not hold. Independently,
`L(1,1,0)+L(1,0,1)=+e_1+(+e_1)=(2, 0, 0)`, which is not zero. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Star aggregation of six-neighbor
lock lists on x-probes is a different object and is not used.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if opposite vertices of `Q` have opposite locks. All
four sites of `Q` are recorded in `B_3(0)`, so face is not `UNDEFINED`.
`L(e_1)+L(e_2)=−e_2+(+e_2)=(0,0,0)`, but
`L(0)+L(e_1+e_2)=+e_1+(+e_1)=(2, 0, 0)`, which is not zero. The cycle sum
is `H=(2, 0, 0)`. Face fails.

Face: fail

Displayed, not adopted. The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reuse star aggregation of six-neighbor lock lists as this letter.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from plaquette opposite-vertex
  holonomy.
- It does not census a sixteen-combination free lettering independent of
  own-incoming locks.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)`, the seed-square `Q`, and the
4-cycle `R`. It uses Qubit only as the algebra of the local possibility
domain. It uses Record only as a boundary: a present lock is content. It
does not rewrite Admissibility. The nnseed process, the own-incoming locks,
the cycle sum `H`, and the reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| own-incoming locks on `Q` at `T_Q` and on `R` at `T_R` | Theorem 1 |
| cycle sum `H` on `Q` | Theorem 1; `(2, 0, 0)` |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| leftover of star aggregation of six-neighbor lock lists | not used; letter is own incoming lock |
| occupancy-kernel inner product | not used |
| formation member from plaquette opposite-vertex holonomy | not attached |
| letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: plaquette opposite-vertex holonomy on the nnseed seed-square `Q` and on the 4-cycle `R` containing `A` and `B`, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed plaquette-holonomy reverse/face report on this seed-square and this 4-cycle. |
| V3 | Own-incoming locks, `T_Q`, `T_R`, `H`, and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads own-incoming locks on two named 4-cycles and scores opposite-vertex holonomy. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not require unique incoming locks, does not reuse star
aggregation of six-neighbor lock lists, and does not use occupancy `n`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| leftover of star aggregation of six-neighbor lock lists | replace own incoming lock by the sum of 6-NN locks | refused; leftover; `L(A)` would be `(5, 0, 0)` while this letter is `−e_2` |
| unique lock-vector lettering of neighbor locks | require a singleton neighbor-lock set | refused; leftover; different object |
| named-sign lettering of incoming locks | map `±e_i` to `{+,−}` | refused; lost the axis; face uses vector opposites |
| reverse/face from occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from plaquette opposite-vertex holonomy | form sites by holonomy instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by cycle sums | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per site | uniqueness is not required; both earliest incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from plaquette
opposite-vertex holonomy, and missing Record identification of the own-incoming
letter are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, letter as own incoming lock, seed-square `Q`,
4-cycle `R`, `T_Q` as first tick all of `Q` are recorded, `T_R=min(t(A),t(B))`,
and reverse/face as opposite-vertex lock sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no leftover of star
aggregation of six-neighbor lock lists, no formation attachment from
plaquette opposite-vertex holonomy, and no Admissibility rewrite are silently
assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each letter from own incoming lock | no continuum alphabet |
| per site | `Q` and `R` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | eight incoming reports, one cycle sum, two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among incoming locks. None is
taken here.

### N7 — hostile steelman

**Steelman:** Once four sites of a unit square are recorded, opposite vertices
should carry opposite incoming locks, the cycle sum should vanish, reverse
through `A` and `B` should hold, uniqueness should be forced, and a star
aggregation of six-neighbor lock lists already answers reverse and face on
the x-probes.

**Answer:** The named construction assigns own-incoming letters
`+e_1`, `−e_2`, `+e_1`, `+e_2` on `Q` with `H=(2, 0, 0)`, and
`−e_2`, `+e_1`, `{+e_1,+e_3}`, `+e_1` on `R`. Uniqueness is not required.
Occupancy `n` is not used. This is not a leftover of star aggregation of
six-neighbor lock lists. Reverse fails. Face fails. The bits remain
displayed.

### N8 — cross-cycle echo

A neighbor-lock reverse-on-x display closed as star aggregation of
six-neighbor lock lists, scoring reverse fail and face hold from those
neighbor sums. This note is not that display: the letter is the site's own
incoming lock, the face object is the seed-square `Q` rather than probes
`C` and `D`, and the reverse object is the 4-cycle `R` containing `A` and
`B`. Here `H=(2, 0, 0)`, reverse fails, and face fails. A self-incoming
named-sign readout on the same process has `C` and `D` both `+e_1`. This
note does not reuse that scoring.

**Gate disposition:** PASS for the plaquette opposite-vertex holonomy
reverse/face reports above. FAIL / DO NOT SHIP for “the letter equals a
star aggregation of six-neighbor lock lists,” “incoming locks are unique,”
“letters are Admissibility,” “the letter is occupancy `n`,” “reverse holds,”
or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, reads own-incoming locks on `Q` at `T_Q` and on `R`
at `T_R`, forms the cycle sum `H`, and checks Theorems 1--3. It also checks
that the construction is not a leftover of star aggregation of six-neighbor
lock lists, that uniqueness of incoming locks is not required, that occupancy
`n` is not used, and that a formation member from plaquette opposite-vertex
holonomy is not attached.
No runner cache is written.
