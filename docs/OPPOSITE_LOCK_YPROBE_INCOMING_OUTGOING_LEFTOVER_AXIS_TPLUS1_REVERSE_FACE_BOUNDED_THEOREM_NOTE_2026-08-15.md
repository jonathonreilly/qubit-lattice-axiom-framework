---
claim_id: opposite_lock_yprobe_incoming_outgoing_leftover_axis_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Leftover lattice axis of M and O at t+1 on the four #7208 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_incoming_outgoing_leftover_axis_tplus1_reverse_face_2026_08_15.py
---

# Leftover Lattice Axis Of Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** leftover lattice axis of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that
leftover axis set, on the four nsmopp #7208 y-probes in
`B_3(0)={n:n·n<=9}`. Same process as nsopp #7093. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is
formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty
`O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Leftover axis is
`Lx(q)={e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))` when both `M` and
`O` are defined. Unformed at `τ` is `UNDEFINED`. Empty leftover is empty,
not `UNDEFINED`. Reverse holds if and only if `Lx(A)=Lx(B)` as sets and
both are defined and nonempty. Face holds if and only if `Lx(C)=Lx(D)`
as sets and both are defined and nonempty. Empty leftover fails, and is
not `UNDEFINED`. This is not leftover of nmsimopp exist-opposite of `M`
and of `O` at `t+1`. This is not leftover of leftover-of-`M` alone. This is
not leftover of leftover-of-`O` alone. This is not leftover of nmunopp union. This is
not leftover of nmt2opp `M` frozen at `t`. This is not leftover of
nmot2opp two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. Uniqueness
of leftover axes is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_incoming_outgoing_leftover_axis_tplus1_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_incoming_outgoing_leftover_axis_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Leftover
axis is the unsigned directions among `{e_1,e_2,e_3}` not occupied by
`M` or `O`. Reverse and face are scored on equality of nonempty leftover
axis sets. Named signs `{+,−}` are a coarser readout and are not used. A
singleton unique lock letter is a different readout and is not used as the
object. Existential opposite of signed locks is a different readout and is
not used as the leftover reverse. A `Z^3` sum of those locks is a different
readout and is not used. Occupancy of sites is not used. A six-neighbor star
is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of leftover lattice axis of M and O at t+1 on the four #7208 y-probes, empty leftover at each probe, reverse fail and face fail from leftover-axis equality; uniqueness of leftover axes is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_incoming_outgoing_leftover_axis_tplus1_reverse_face
target_blocker_text: "display leftover lattice axis of M and O at t+1 on the four #7208 y-probes, and reverse/face from that leftover axis set, no unique leftover required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep leftover lattice axis of M and O at t+1 displayed; do not write leftover-axis equality into Admissibility, do not reduce to leftover of M alone or leftover of O alone, do not replace leftover-axis equality by existential opposite of signed locks, do not replace leftover by six-neighbor lock union, do not identify the display with nmsimopp exist-opposite HOLD, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for leftover lattice axis of M and O at t+1 on the four #7208 y-probes and reverse/face from that leftover; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose leftover
axis of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nsmopp #7208.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named leftover axis `Lx` of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `M` or `O` to be a singleton. It does not sum either set. It
does not replace `O` by `M`. It does not wait for a global later T.
Occupancy of sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Leftover lattice axis of `M` and `O` at the same cut:

```text
Lx(q) = {e_1,e_2,e_3} minus (Axis(M(q,τ)) union Axis(O(q,τ)))
```

when both `M` and `O` are defined. If `q` is unformed at `τ`, then `Lx(q)`
is `UNDEFINED`. Empty leftover is empty, not `UNDEFINED`. The construction
does not require leftover to be a singleton. Leftover of `M` alone is
`{e_1,e_2,e_3}` minus `Axis(M)`, a different object. Leftover of `O` alone
is a different object. Axis is unsigned: `+e_i` and `−e_i` occupy the same
axis.

Reverse leftover-axis holds if and only if `Lx(A)` and `Lx(B)` are defined,
equal as sets, and nonempty. Face leftover-axis holds if and only if
`Lx(C)` and `Lx(D)` are defined, equal as sets, and nonempty. Empty leftover
on either side of a comparison fails; it is not `UNDEFINED`. Either side
`UNDEFINED` is `UNDEFINED`. Nonempty unequal leftovers fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying existential opposite of
signed locks with leftover reverse is refused: leftover reverse is equality
of nonempty unsigned leftover axis sets.

## Theorem 1 — ticks, `M`, `O`, `Axis`, and `Lx` at `τ=t+1`

On this process the four y-probes form. Compare to nmsimopp: that leftover
reports `M` and `O` together at `τ=t+1` with empty letter intersection and
exist-opposite reverse hold and face hold from each signed set. This display
reads unsigned leftover axis of those same timed sets:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2, +e_3, −e_3}
O(A, τ) = {+e_2, +e_3, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
Axis(M)(A, τ) = {e_1}
Axis(O)(A, τ) = {e_2, e_3}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_2}
Axis(O)(C, τ) = {e_1, e_3}
Axis(M)(D, τ) = {e_2, e_3}
Axis(O)(D, τ) = {e_1}
Lx(A) = {}
Lx(B) = {}
Lx(C) = {}
Lx(D) = {}
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three earliest
incoming steps and `O(A,τ)` has three outgoing steps. Unique letters would
assign `UNDEFINED` at mixed probes. Here uniqueness is not required.
At each probe, `Axis(M)` and `Axis(O)` are complementary: their union is
`{e_1,e_2,e_3}` and their intersection is empty. Leftover of the union is
therefore empty at each probe. Empty leftover is empty, not `UNDEFINED`.
If `M` and `O` had occupied only two of the three lattice axes, leftover
would have been the unoccupied third direction. On these four y-probes they
occupy all three, so leftover is empty. O is not M.

Investment nmsimopp: `M∩O` is empty at `τ` and both signed reverse/face
HOLD. Letter-disjointness is not axis leftover. Opposite signs on one axis
would be letter-disjoint while occupying that axis. Here the sets are also
axis-disjoint and complementary. Leftover of `M` alone at `A` and `B` is
`{e_2,e_3}`, nonempty and equal. Leftover of `O` alone at `A` and `B` is
`{e_1}`, nonempty and equal. Those one-sided leftovers are not this object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

## Theorem 2 — reverse from leftover axis at `τ`

Reverse leftover-axis holds if and only if `Lx(A)` and `Lx(B)` are defined,
equal as sets, and nonempty. Both leftover sets are `{}`. Empty leftover
fails, and is not `UNDEFINED`. Reverse fails.

Reverse leftover axis at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Leftover-of-`M` reverse
would hold because leftover of `M` at `A` and at `B` is `{e_2, e_3}`.
Leftover-of-`O` reverse would hold because leftover of `O` at `A` and at
`B` is `{e_1}`. Exist-opposite reverse of signed `M` holds. Those leftovers
are not this display.

## Theorem 3 — face from leftover axis at `τ`

Face leftover-axis holds if and only if `Lx(C)` and `Lx(D)` are defined,
equal as sets, and nonempty. Both leftover sets are `{}`. Empty leftover
fails, and is not `UNDEFINED`. Face fails.

Face leftover axis at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-of-`M` face would fail because leftover of `M` at `C` is
`{e_1, e_3}` and leftover of `M` at `D` is `{e_1}`: nonempty and
unequal. Leftover of `O` at `C` is `{e_2}` and leftover of `O` at
`D` is `{e_2, e_3}`: nonempty and unequal. Exist-opposite face of
signed `M` holds and exist-opposite face of signed `O` holds. This
display scores leftover-axis equality of the union leftover, which is
empty at `C` and at `D`, so face fails.

Empty leftover does not make reverse `UNDEFINED`. Empty is fail.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require leftover to be a singleton.
- It does not sum either set.
- It does not replace leftover of the union by leftover of `M` alone.
- It does not replace leftover of the union by leftover of `O` alone.
- It does not replace leftover-axis equality by existential opposite of
  signed locks.
- It does not replace `O` by `M`.
- It does not replace leftover by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this leftover display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy of sites as the letter.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock two-site process, leftover lattice axis of `M` and `O` at
`t+1`, and the reverse/face bits from leftover-axis equality are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| leftover `Lx` at `τ` | Theorem 1; empty at each probe |
| reverse from leftover axis at `τ` | Theorem 2; `fail` |
| face from leftover axis at `τ` | Theorem 3; `fail` |
| unique leftover axis | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nmsimopp exist-opposite HOLD | not this leftover-axis display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| leftover-axis equality as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: leftover lattice axis of `M` and `O` at `t+1` on the four #7208 y-probes, and reverse/face from that leftover. |
| V2 | Current main has no landed leftover-axis reverse/face of timed `M` and `O` on these four #7208 y-probes. |
| V3 | Leftover axis sets at one cut and the two leftover reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned leftover axis of own incoming and own outgoing at the same `t+1` cut and scores equality of nonempty leftover axis sets. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique leftover, does not replace leftover of the union by leftover of `M`
alone or leftover of `O` alone, does not replace leftover-axis equality by
existential opposite of signed locks, does not identify this display with
nmsimopp exist-opposite HOLD, and does not identify it with nmunopp union.
No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and `B` is `{e_2,e_3}`, nonempty equal, reverse would hold | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and `B` is `{e_1}`, nonempty equal, reverse would hold | ATTEMPTED |
| nmsimopp exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | those bits HOLD; leftover-axis reverse and face fail because leftover is empty | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; leftover is unsigned unoccupied axes of the union | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` and mixed `O(A,τ)` remain sets; leftover is still empty | ATTEMPTED |
| exist-opposite of leftover axes | score `a+b=(0,0,0)` inside leftover axis vectors | leftover reverse is set equality of nonempty leftovers, not opposite of unsigned axes | ATTEMPTED |
| letter intersection as leftover | score reverse/face inside `M ∩ O` | letter intersection empty is not axis leftover; opposite signs can share an axis | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; leftover axis is unsigned unoccupied directions | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores leftover axis of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports leftover empty and leftover reverse fail face fail | ATTEMPTED |
| sum of a set | replace leftover by a `Z^3` sum | the construction does not sum; leftover is a set of unsigned axes | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by leftover-axis equality | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of leftover of the union
with leftover of `M` alone, missing identification of leftover-axis equality
with existential opposite of signed locks, and missing Record identification
of leftover reverse are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, leftover of
`Axis(M)` union `Axis(O)`, empty leftover fail not `UNDEFINED`, four
y-probes with seed `A`, and mixed remains a set are declared. No uniqueness
of leftover, no six-neighbor lock union as the scored object, no lock-count
clock, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
leftover `fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned leftover lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four leftover axis sets, reverse/face from leftover-axis equality | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for leftover reverse/face, a
formation-rate rule, and a physical selector among leftover axes. None is
taken here.

### N7 — hostile steelman

**Steelman:** Leftover empty is only nmsimopp `M∩O` empty; leftover reverse
fail is only refusing exist-opposite HOLD; leftover of `M` alone already
gives a third direction `{e_2,e_3}` at `A`; leftover of `O` alone already
gives `{e_1}`; empty leftover should be `UNDEFINED` like empty exist-opposite;
and complementary occupation is only three-axis covering, not a leftover.

**Answer:** Letter intersection empty is signed-letter disjointness.
Opposite signs on one axis are letter-disjoint and occupy that axis.
Leftover of the union is unsigned unoccupied directions of `M` and `O`
together. Leftover of `M` alone and leftover of `O` alone are nonempty
one-sided leftovers; they are not leftover of the union. Empty leftover
fails by declaration, and is not `UNDEFINED`. Complementary occupation
is why leftover of the union is empty on these four y-probes: `M` and `O`
occupy two complementary axis collections whose union is all three axes.
Reverse leftover-axis is equality of nonempty leftover axis sets, not
exist-opposite of signed locks.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M`.
nmsimopp reported `M` and `O` together at `τ=t+1`, empty letter
intersection, reverse hold and face hold from `M`, and reverse hold and
face hold from `O`. nmunopp reported reverse hold and face hold from the
untimed union. This note is not those displays: it reports leftover lattice
axis of `M` and `O` at `τ=t+1`, empty leftover at each of the four y-probes,
reverse fail, and face fail.

**Gate disposition:** PASS for the leftover-axis `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
nmsimopp exist-opposite HOLD,” “the predicate equals nmunopp union,”
“bits are Admissibility,” “leftover is nonempty,” “reverse leftover-axis
holds,” “face leftover-axis holds,” or “empty leftover is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's own earliest incoming set and own
outgoing dual from the record prefix at that probe's `t+1`, reports unsigned
axis of each, reports leftover of the union, lists new records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors, and checks Theorems
1--3. It also checks that leftover is empty at each probe, that empty leftover
fails reverse and face and is not `UNDEFINED`, that leftover of `M` alone
and leftover of `O` alone are different objects whose reverse would hold,
that mixed sets remain sets, that unique-letter leftover is still empty,
that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, and that the display
is not the two-tick lock-count clock composition. No runner cache is
written.
