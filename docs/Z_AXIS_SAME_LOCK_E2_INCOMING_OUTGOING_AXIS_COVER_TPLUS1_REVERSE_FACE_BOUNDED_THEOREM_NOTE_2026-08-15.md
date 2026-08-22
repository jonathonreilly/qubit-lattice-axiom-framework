---
claim_id: z_axis_same_lock_e2_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four #7199 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_axis_same_lock_e2_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Axis-Cover Of Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four #7199 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that cover, on the
four nsze2sam #7199 y-probes in `B_3(0)={n:n·n<=9}`. Same process as z-axis
same-lock `+e_2/+e_2`. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis
of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs
at `q` if and only if `Axis(M)` intersect `Axis(O)` is empty and
`Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O`
is `UNDEFINED`. Else fail. Reverse HOLDs if and only if cover HOLDs at `A`
and at `B`. Face HOLDs if and only if cover HOLDs at `C` and at `D`. This
is HOLD iff cover, not leftover-empty fail. This is not leftover of #7199
exist-opposite of `M` (fail/fail on these y-probes). This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover of exist-opposite of `O`. This is not leftover of nsze2inc
z-axis opposite `±e_2`. This is not leftover of nszsaminc z-axis same-lock
`+e_1`. This is not leftover of nsopp y-probes with seed site `A`. This is
not leftover of mixed #7188 fail/fail. This is not leftover of `M` frozen
at `t` as this cover display: at `t`, `O` is empty and cover fails. This is
not leftover of nmot2opp two-tick composition as an adopted clock. This is
not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
nmunopp untimed union. Uniqueness is not required. Mixed remains a set.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_axis_same_lock_e2_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/z_axis_same_lock_e2_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Reverse and face are scored on cover HOLD at the paired probes. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
cover reverse. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of axis-cover of M and O at t+1 on the four #7199 y-probes, complementary cover at each probe, reverse hold and face hold from cover; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_axis_same_lock_e2_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display axis-cover of M and O at t+1 on the four #7199 y-probes, and reverse/face from that cover, HOLD iff cover, not leftover-empty fail and not exist-opposite of M"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep axis-cover of M and O at t+1 displayed; do not write cover into Admissibility, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace cover by existential opposite of signed locks, do not replace cover by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for axis-cover of M and O at t+1 on the four #7199 y-probes and reverse/face from that cover; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose axis-cover
of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is not a seed. Same process and y-probes as nsze2sam #7199.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,0,1)}` is recorded at formation tick 0 with
same locks `L(0)=+e_2` and `L(0,0,1)=+e_2`. This seed is not nsze2inc
(`+e_2/−e_2`). This seed is not nszsaminc (`+e_1/+e_1`). This seed is not
the perp two-site seed `+e_1/+e_2` on `{0,(0,1,0)}`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the
y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.

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

## Named axis-cover of `M` and `O` at `τ=t+1`

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

Cover at a probe at the same cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

If `q` is unformed at `τ`, then cover is `UNDEFINED`. Overlapping axes fail.
Incomplete union fails. Axis is unsigned: `+e_i` and `−e_i` occupy the same
axis. Leftover of the union is `{e_1,e_2,e_3}` minus
`(Axis(M) union Axis(O))`. Empty leftover is leftover fail of leftover
axis; this display is HOLD iff cover, not leftover-empty fail. Leftover of
`M` alone is `{e_1,e_2,e_3}` minus `Axis(M)`, a different object. Leftover
of `O` alone is a different object.

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`. Face
axis-cover holds if and only if cover HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
cover reverse is refused: leftover-empty fail scores empty leftover as
fail, while cover HOLDs from complementary occupation of all three axes.

## Theorem 1 — ticks, `M`, `O`, `Axis`, and cover at `τ=t+1`

On this process the four y-probes form. Compare to leftover-empty fail:
that leftover reports empty leftover at each probe and leftover reverse
fail and leftover face fail. Compare to #7199 exist-opposite of `M`: that
readout reports reverse fail and face fail. This display reads
complementary axis-cover of those same timed sets:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
M(A, τ) = {+e_1, −e_1, +e_3}
M(B, τ) = {+e_2}
M(C, τ) = {+e_2}
M(D, τ) = {+e_2}
O(A, τ) = {+e_2}
O(B, τ) = {+e_1, −e_1, +e_3}
O(C, τ) = {+e_1, −e_1, −e_3}
O(D, τ) = {+e_1, −e_1, −e_3}
Axis(M)(A, τ) = {e_1, e_3}
Axis(O)(A, τ) = {e_2}
Axis(M)(B, τ) = {e_2}
Axis(O)(B, τ) = {e_1, e_3}
Axis(M)(C, τ) = {e_2}
Axis(O)(C, τ) = {e_1, e_3}
Axis(M)(D, τ) = {e_2}
Axis(O)(D, τ) = {e_1, e_3}
cover(A) = hold
cover(B) = hold
cover(C) = hold
cover(D) = hold
```

`A` is not a seed: it forms at tick 3 with mixed incoming `{+e_1, −e_1, +e_3}`.
Mixed remains a set: `M(A,τ)` has three earliest incoming steps and
`O(B,τ)` has three outgoing steps. Unique letters would assign `UNDEFINED`
at mixed `M(A,τ)`. Here uniqueness is not required.
At each probe, `Axis(M)` and `Axis(O)` are complementary: their union is
`{e_1,e_2,e_3}` and their intersection is empty. Cover therefore HOLDs at
each probe. Leftover of the union is empty at each probe; leftover-empty
fail of that leftover is not this object.
O is not M.

`M` at `τ` equals `M` at `t`. `O` at `t` is empty at each of the four
y-probes, so cover at `t` fails. Cover at `τ=t+1` HOLDs. Frozen `M` at `t`
is not this cover display.

Leftover of `M` alone at `A` is `{e_2}` and leftover of `M` alone at `B` is
`{e_1, e_3}`: nonempty and unequal, so leftover-of-`M` reverse fails.
Leftover of `O` alone at `A` is `{e_1, e_3}` and leftover of `O` alone at
`B` is `{e_2}`: nonempty and unequal, so leftover-of-`O` reverse fails.
Those one-sided leftovers are not this object. Exist-opposite of signed
`M` is fail/fail. Exist-opposite of signed `O` is reverse fail and face
hold. Cover reverse and cover face HOLD.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0)
new 6-NN of B at t(B)+1: (2, 1, 1), (0, 1, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0), (0, 1, 0), (1, 1, -1)
```

## Theorem 2 — reverse from axis-cover at `τ`

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`.
Both covers HOLD. Reverse HOLDs. This is HOLD iff cover, not leftover-empty
fail.

Reverse axis-cover at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Cover
reverse HOLDs from complementary occupation of all three axes. Leftover-of-
`M` reverse would fail because leftover of `M` at `A` is `{e_2}` and
leftover of `M` at `B` is `{e_1, e_3}`. Leftover-of-`O` reverse would fail
because leftover of `O` at `A` is `{e_1, e_3}` and leftover of `O` at `B`
is `{e_2}`. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` fails. Those leftovers are not this display.

Reverse holds.

## Theorem 3 — face from axis-cover at `τ`

Face axis-cover holds if and only if cover HOLDs at `C` and at `D`. Both
covers HOLD. Face HOLDs.

Face axis-cover at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-empty face fails because leftover of the union is empty at `C`
and at `D`. Cover face HOLDs from complementary occupation of all three
axes. Leftover-of-`M` face would hold because leftover of `M` at `C` and
at `D` is `{e_1, e_3}`. Leftover of `O` at `C` and at `D` is `{e_2}`:
nonempty and equal, so leftover-of-`O` face would hold. Exist-opposite
face of signed `M` fails. Exist-opposite face of signed `O` holds. This
display scores cover of `M` and `O`, which HOLDs at `C` and at `D`, so
face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs.

Face holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require cover sides to be singletons.
- It does not sum either set.
- It does not replace cover by leftover-empty fail.
- It does not replace cover by leftover of `M` alone.
- It does not replace cover by leftover of `O` alone.
- It does not replace cover by existential opposite of signed locks.
- It does not reprint #7199 exist-opposite of `M` fail/fail as this member.
- It does not replace `O` by `M`.
- It does not replace cover by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this cover display.
- It does not reprint nmot2opp two-tick composition.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint nsze2inc opposite `±e_2` as this seed.
- It does not reprint nszsaminc same-lock `+e_1` as this seed.
- It does not reprint nsopp y-probes with seed site `A`.
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
z-axis same-lock two-site process, axis-cover of `M` and `O` at `t+1`, and the
reverse/face bits from cover are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; z-axis same-lock `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| cover at `τ` | Theorem 1; HOLD at each probe |
| reverse from axis-cover at `τ` | Theorem 2; `hold` |
| face from axis-cover at `τ` | Theorem 3; `hold` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this cover display |
| leftover of #7199 exist-opposite of `M` | not this cover display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of nsze2inc opposite `±e_2` | not this seed |
| leftover of nszsaminc same-lock `+e_1` | not this seed |
| leftover of nsopp y-probes | not this seed; `A` is not a seed |
| global later T | not used |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: axis-cover of `M` and `O` at `t+1` on the four #7199 y-probes, and reverse/face from that cover. |
| V2 | Current main has no landed axis-cover reverse/face of timed `M` and `O` on these four #7199 y-probes. |
| V3 | Cover reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-cover of own incoming and own outgoing at the same `t+1` cut and scores HOLD iff cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace cover by leftover-empty fail, does not
replace cover by leftover of `M` alone or leftover of `O` alone, does not
replace cover by existential opposite of signed locks, does not identify
this display with #7199 exist-opposite of `M` fail/fail, and does not
identify it with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at each probe, leftover reverse and face fail, while cover HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_2}` and at `B` is `{e_1,e_3}`, reverse would fail, while cover reverse HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_1,e_3}` and at `B` is `{e_2}`, reverse would fail, while cover reverse HOLDs | ATTEMPTED |
| #7199 exist-opposite of `M` | reuse signed reverse fail and face fail of `M` | those bits fail for a signed pair; cover HOLDs from unsigned complementary axes of `M` versus `O` at one probe | ATTEMPTED |
| exist-opposite of `O` | reuse signed reverse fail and face hold of `O` | reverse of signed `O` fails while cover reverse HOLDs | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; cover is unsigned complementary axes of `M` and `O` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(A,τ)` remains a set; unique-letter cover is `UNDEFINED` at `A`; cover still HOLDs | ATTEMPTED |
| exist-opposite of leftover axes | score `a+b=(0,0,0)` inside leftover axis vectors | leftover reverse is leftover-empty fail here; cover reverse is HOLD iff cover | ATTEMPTED |
| letter intersection as cover | score reverse/face inside `M ∩ O` | letter intersection empty is not axis-cover; opposite signs can share an axis | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover is a six-neighbor lock set; cover is unsigned complementary axes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores axis-cover of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed reverse-fail face-fail | different process; this member reports cover HOLD and reverse hold face hold | ATTEMPTED |
| nsze2inc opposite `±e_2` | reuse seed `+e_2/−e_2` | seed partner lock at `(0,0,1)` is `+e_2`, not `−e_2` | ATTEMPTED |
| nszsaminc same-lock `+e_1` | reuse seed `+e_1/+e_1` | seed letters are `+e_2/+e_2`; `t(A)=3` not `1` | ATTEMPTED |
| nsopp y-probes | reuse seed `{0,(0,1,0)}` with seed site `A` | `A` is not a seed; `t(A)=3` | ATTEMPTED |
| sum of a set | replace cover by a `Z^3` sum | the construction does not sum; cover is a complementary pair of unsigned axis sets | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover of
`M` alone, missing identification of cover with leftover-empty fail, missing
identification of cover with existential opposite of signed locks, and
missing Record identification of cover reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_2` and `+e_2`, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`, HOLD
iff cover not leftover-empty fail, four y-probes with `A` not a seed, and
mixed remains a set are declared. No uniqueness of incoming locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover `hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four cover reports, reverse/face from cover HOLD | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cover reverse/face, a
formation-rate rule, and a physical selector among complementary axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Cover HOLD is only leftover empty; leftover-empty fail already
answered the three-axis occupation; leftover of `M` alone already gives a
third direction `{e_2}` at `A`; leftover of `O` alone already gives
`{e_1,e_3}`; complementary occupation is only empty letter intersection;
exist-opposite of `M` already scored this member fail/fail; and empty `M`
or empty `O` should be `UNDEFINED` like unformed.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Cover HOLDs when leftover of the union is empty *and*
`Axis(M)` and `Axis(O)` are disjoint and their union is `{e_1,e_2,e_3}`.
Letter intersection empty is signed-letter disjointness. Opposite signs on
one axis are letter-disjoint and occupy that axis, so they are not cover.
Leftover of `M` alone and leftover of `O` alone are nonempty one-sided
leftovers; they are not complementary cover of the pair. Exist-opposite of
signed `M` is fail/fail on this member; cover reverse is hold. Empty `M` or
empty `O` is empty, not `UNDEFINED`. Reverse axis-cover is HOLD iff cover
at `A` and at `B`, not leftover-empty fail.

### N8 — cross-cycle echo

nsze2sam #7199 reported reverse hold and face hold from same-tick-inclusive
six-neighbor locks union own incoming lock, while own incoming `M` as
exist-opposite is reverse fail and face fail. This note is not those
displays: it reports axis-cover of `M` and `O` at `τ=t+1`, cover HOLD at
each of the four y-probes, reverse hold, and face hold. HOLD iff cover, not
leftover-empty fail.

**Gate disposition:** PASS for the axis-cover `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover-empty fail,” “the
predicate equals leftover of `M` alone,” “the predicate equals leftover of
`O` alone,” “the predicate equals #7199 exist-opposite of `M`,” “the
predicate equals nmunopp union,” “bits are Admissibility,” “cover fails,”
“reverse axis-cover fails,” or “face axis-cover fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-axis same-lock
`+e_2/+e_2` perp-step incoming-lock process, reads each probe's own
earliest incoming set and own outgoing dual from the record prefix at that
probe's `t+1`, reports unsigned axis of each, reports cover of the pair,
lists new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that cover HOLDs at
each probe, that leftover-empty fail is a different reverse and face, that
leftover of `M` alone and leftover of `O` alone are different objects, that
exist-opposite of `M` is fail/fail, that mixed sets remain sets, that
unique-letter cover is `UNDEFINED` at mixed `M`, that the construction does
not sum, that a formation member from already-recorded six-neighbor locks
is not attached, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
