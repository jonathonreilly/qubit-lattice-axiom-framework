---
claim_id: two_axis_opposite_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# One-In Two-Out Split At t+1 Versus t+2 Reverse And Face Composition On Four Z-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out split at t+1 versus t+2 on the four z-probes of the
two-axis opposite seed, reverse/face at each cut, and composition, are
reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Same process and z-probes as nm2axz. Let `t(q)` be the formation tick of
probe `q`. Cuts are `τ1=t+1` and `τ2=t+2`. There is no global T.
Do not score τ=t. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton seed
letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis of
a defined lock set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at
`q` if and only if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union
`Axis(O)` equals `{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O` is
`UNDEFINED`. Else fail. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Empty O at t fails split as leftover of
nm2splt2z and is not scored here. 2-in 1-out is fail of this object, not
UNDEFINED. Reverse HOLDs if and only if split HOLDs at `A` and at `B` at
that cut. Face HOLDs if and only if split HOLDs at `C` and at `D` at that
cut. Composition HOLDs if and only if split at `τ1` equals split at `τ2` at
`A`, `B`, `C`, and `D`. This is not leftover of nm2ax12z, which scores only
`τ=t+1`. This is not leftover of nm2splt2z, which scores `τ=t` versus
`t+1` from empty `O` at `t` and composition fail. This is not leftover of
nmcover axis-cover. This is not leftover of nm2axz axis-cover. This is not
leftover of leftover-of-`M` alone. This is not leftover of leftover-of-`O`
alone. This is not leftover-empty fail of leftover axis. This is not leftover
of nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This
is not leftover of nmot2opp two-tick composition of empty-then-HOLD `O`.
This is not leftover of nmoutopp untimed eventual-`O`. This is not leftover
of mixed #7188 fail/fail. This is not leftover of the 1-axis opposite
two-site seed. This is not leftover of the same-lock two-site seed. This is
not leftover of reverse/face bit composition as a substitute for the four
split bits. This is not leftover of 2-in 1-out composition, which HOLDs
here because 2-in 1-out fails at both cuts. This is not leftover of cover
composition, which also HOLDs here without `|Axis(M)|=1`. The second pair
is a new seed, not a formed child. Uniqueness is not required. Mixed remains
a set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on
`B_3(0)={n:n·n<=9}` and the four named z-probes. Incoming lock letters are
unit nearest-neighbor steps. `O` is the outgoing dual of those incoming
sets at the per-probe cuts `τ1=t+1` and `τ2=t+2`. Axis is the unsigned
lattice direction of a signed lock. Cover is the complementary occupation
of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`. Split is cover together with
`|Axis(M)|=1`. Reverse and face are scored on split HOLD at the paired
probes at each cut. Composition is equality of the four split bits across
the two cuts. Named signs `{+,−}` are a coarser readout and are not used.
A singleton unique lock letter is a different readout and is not used as
the object. Existential opposite of signed locks is a different readout
and is not used as the split reverse. Axis-cover without the one-axis
incoming cardinality is a different readout and is not used.
Leftover-empty fail of unsigned leftover axis sets is a different readout
and is not used. A `Z^3` sum of those locks is a different readout and is
not used. Occupancy of sites is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out split of M and O at t+1 versus t+2 on the four z-probes of the two-axis opposite seed, HOLDING 3-split freeze with reverse hold, face hold, and composition hold; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis opposite seed, reverse/face at each cut, and composition, not nm2splt2z t versus t+1, not cover, not exist-opposite"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out split at t+1 versus t+2 displayed; do not write split into Admissibility, do not score tau=t, do not reduce to cover, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, do not replace composition by reverse/face bit stability, do not replace composition by 2-in 1-out composition, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. Same process and
z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
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

## Named 1-in 2-out split of `M` and `O` at `τ1=t+1` and `τ2=t+2`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Cuts are `τ1=t+1` and `τ2=t+2`. There is no global T.
Do not score τ=t.

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

Cover at a probe at a cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

If `q` is unformed at that cut, then cover is `UNDEFINED`. Overlapping axes
fail. Incomplete union fails. Axis is unsigned: `+e_i` and `−e_i` occupy
the same axis.

Split at a probe at a cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

Empty O at t fails split as leftover of nm2splt2z and is not scored here.
2-in 1-out is fail of this object, not UNDEFINED: cover HOLD with
`|Axis(M)|=2` (hence `|Axis(O)|=1`) is split fail. Cover without the
one-axis incoming cardinality is not this object. Unique letters are not
this object. One-in one-out with leftover axis is cover fail and therefore
split fail.

Reverse 1-in 2-out at a cut holds if and only if split HOLDs at `A` and at
`B` at that cut. Face 1-in 2-out at a cut holds if and only if split HOLDs
at `C` and at `D` at that cut. Either side `UNDEFINED` is `UNDEFINED`. Else
if both sides HOLD, reverse or face HOLDs. Else fail.

Composition HOLDs if and only if split at `τ1` equals split at `τ2` at
`A`, `B`, `C`, and `D`. Else fail. Reverse/face bit stability is a leftover
predicate and is not this composition. 2-in 1-out composition is a leftover
predicate and is not this composition. Cover composition is a leftover
predicate and is not this composition.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
split reverse is refused: leftover-empty fail scores empty leftover as
fail. Identifying axis-cover reverse/face of the 1-axis opposite two-site
seed with this reverse/face is refused. Identifying nm2ax12z split reverse
hold and face hold at `t+1` only with this freeze is refused: that leftover
does not score `τ=t+2`. Identifying nm2splt2z composition fail at `t`
versus `t+1` with this freeze is refused: Do not score τ=t. Identifying
exist-opposite of signed `O` with split reverse is refused: exist-opposite
face of signed `O` fails while split face HOLDs.

## Theorem 1 — ticks, `M`, `O`, and split at `τ1=t+1` and `τ2=t+2`

On this process the four z-probes form. Compare to the 1-axis opposite
two-site seed: that member forms `A` at tick 1 as a child locking `+e_3`,
forms `B` at tick 2, forms `C` at tick 4 with mixed 2-in 1-out `M` at
`t+1`, and forms `D` at tick 2. Here the second pair is a new seed, not a
formed child, so `(0,0,1)` is already recorded at tick 0 with lock `+e_2`
and `(0,1,1)` is already recorded at tick 0 with lock `−e_2`. This display
reads the 1-in 2-out split of timed `M` and `O` at `τ1=t+1` and `τ2=t+2`.
Do not score τ=t.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ1) = {+e_2}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_3}
M(D, τ1) = {+e_1}
M(A, τ2) = {+e_2}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_3}
M(D, τ2) = {+e_1}
O(A, τ1) = {+e_1, −e_1, +e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, −e_2}
O(D, τ1) = {−e_2, +e_3, −e_3}
O(A, τ2) = {+e_1, −e_1, +e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, −e_2}
O(D, τ2) = {−e_2, +e_3, −e_3}
Axis(M)(A, τ2) = {e_2}
Axis(O)(A, τ2) = {e_1, e_3}
Axis(M)(B, τ2) = {e_1}
Axis(O)(B, τ2) = {e_2, e_3}
Axis(M)(C, τ2) = {e_3}
Axis(O)(C, τ2) = {e_1, e_2}
Axis(M)(D, τ2) = {e_1}
Axis(O)(D, τ2) = {e_2, e_3}
|Axis(M)|(A, τ2) = 1
|Axis(O)|(A, τ2) = 2
|Axis(M)|(B, τ2) = 1
|Axis(O)|(B, τ2) = 2
|Axis(M)|(C, τ2) = 1
|Axis(O)|(C, τ2) = 2
|Axis(M)|(D, τ2) = 1
|Axis(O)|(D, τ2) = 2
cover(A, τ1) = hold
cover(B, τ1) = hold
cover(C, τ1) = hold
cover(D, τ1) = hold
cover(A, τ2) = hold
cover(B, τ2) = hold
cover(C, τ2) = hold
cover(D, τ2) = hold
split(A, τ1) = hold
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = hold
split(A, τ2) = hold
split(B, τ2) = hold
split(C, τ2) = hold
split(D, τ2) = hold
```

`A` is a seed at tick 0 with seed letter `+e_2`. `M` is frozen from `t+1`
to `t+2` at each probe. `O` is nonempty at `τ1` and frozen equal at `τ2`.
Mixed remains a set: `O(A,τ1)` has three outgoing steps and `O(D,τ1)` has
three outgoing steps. Unique letters would assign `UNDEFINED` at mixed `O`.
Here uniqueness is not required. At each probe at both cuts, `Axis(M)` and
`Axis(O)` are complementary: their union is `{e_1,e_2,e_3}` and their
intersection is empty. Cover therefore HOLDs at each probe at both cuts,
and split HOLDs because `|Axis(M)|=1`. 2-in 1-out is fail of this object,
not UNDEFINED; that identity remains, and it is not the report at any of
these four probes at either cut. Leftover of the union is empty at each
probe at both cuts; leftover-empty fail of that leftover is not this
object. O is not M.

Investment nm2axz cover on these four z-probes at `t+1`: cover HOLDs at
every probe. Investment nm2ax12z split on these four z-probes at `t+1`:
split HOLDs at every probe, reverse hold, face hold. Those leftovers do not
score `τ=t+2`. Investment nm2splt2z composition of split at `t` versus
`t+1` fails from empty `O` at `t`. Do not score τ=t. This note is the
first display of split at `t+1` versus `t+2` now that `O` is nonempty. The
HOLDING 3-split freezes.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` at `τ1` and do not enter earliest `M`. Site
`(0,1,1)` is a seed, so it is not a new 6-NN of `A`. Between `t+1` and
`t+2` a new 6-NN of `A` forms at `(0,-1,1)` with incoming `{+e_3}`. The
step from `A` to that site is `−e_2`, which is not in that incoming set,
so the new neighbor does not enter `O`. `O` therefore freezes.

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
new 6-NN of A at t(A)+2: (0, -1, 1)
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B` at
that cut. Face 1-in 2-out holds if and only if split HOLDs at `C` and at
`D` at that cut.

Reverse 1-in 2-out at τ1: hold
Reverse 1-in 2-out at τ2: hold
Face 1-in 2-out at τ1: hold
Face 1-in 2-out at τ2: hold

At `τ1` every split HOLDs from nonempty complementary `O`, so reverse
HOLDs and face HOLDs. At `τ2` the same four split bits HOLD, so reverse
HOLDs and face HOLDs. Cover reverse and cover face HOLD at both cuts.
Leftover-empty reverse fails at both cuts because leftover of the union is
empty. Leftover of `M` reverse fails because leftover of `M` at `A` is
`{e_1, e_3}` and at `B` is `{e_2, e_3}`: nonempty and unequal. Leftover of
`O` reverse fails because leftover of `O` at `A` is `{e_2}` and at `B` is
`{e_1}`: nonempty and unequal. Exist-opposite reverse of signed `M` fails.
Exist-opposite reverse of signed `O` holds at both cuts. Exist-opposite
face of signed `O` fails. Those leftovers are not this display.

Leftover of nm2splt2z at `τ=t` is reverse fail and face fail from empty
`O`. Do not score τ=t.

The four y-probes of this same seed give split reverse hold and split face
fail at `t+1` and the same bits at `t+2`. The four x-probes give split
reverse fail and split face fail at both cuts. Those probe-direction
readouts are not this z-probe display.

## Theorem 3 — composition hold / fail

Composition HOLDs if and only if split at `τ1` equals split at `τ2` at
`A`, `B`, `C`, and `D`. Each probe reports hold at `τ1` and hold at `τ2`.
The bits are equal. Composition holds.

Composition of split bits: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Reverse/face bit composition also HOLDs on this member because reverse
stays hold and face stays hold. That leftover is not this letter:
composition is equality of the four split bits, not equality of the two
reverse/face bits. 2-in 1-out composition HOLDs because 2-in 1-out fails at
both cuts at every probe. Cover composition HOLDs because cover HOLDs at
both cuts; cover without `|Axis(M)|=1` is not this object. Frozen `M` is
equal at the two cuts and is not this composition. Frozen `O` is equal at
the two cuts and is not this composition by itself: the letter is 1-in
2-out split of `M` and `O`. nmot2opp scores exist-opposite of `O`.
nm2ax12z scores only `t+1`. nm2splt2z scores `t` versus `t+1` with
composition fail from empty `O` at `t`. Mixed #7188 two-tick composition
reported fail/fail with composition HOLD. This member reports hold then
hold, with composition hold. This is not the two-tick lock-count clock
composition.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` at both cuts and split HOLDs at `D`
at both cuts.

Composition holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require split sides to be singletons.
- It does not sum either set.
- It does not replace split by leftover-empty fail.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by existential opposite of signed locks.
- It does not replace split by axis-cover without `|Axis(M)|=1`.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not score `τ=t`.
- It does not treat empty `O` at `t` as this letter.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  split display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  split display.
- It does not reprint nm2ax12z 1-in 2-out at `t+1` only as this freeze.
- It does not reprint nm2splt2z composition fail at `t` versus `t+1`.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this split display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not replace composition by reverse/face bit stability.
- It does not replace composition by 2-in 1-out composition.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite seed process, 1-in 2-out split of `M` and `O` at `t+1`
versus `t+2`, reverse/face at each cut, and composition of those split bits
are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ1=t+1` and `τ2=t+2` | Theorem 1; frozen equal |
| `O` at `τ1=t+1` | Theorem 1; HOLDING outgoing dual |
| `O` at `τ2=t+2` | Theorem 1; frozen equal to `τ1` |
| split at `τ1` | Theorem 1; HOLD at each probe |
| split at `τ2` | Theorem 1; HOLD at each probe; freeze |
| reverse at `τ1` and at `τ2` | Theorem 2; hold then hold |
| face at `τ1` and at `τ2` | Theorem 2; hold then hold |
| composition of split bits | Theorem 3; hold |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this split display |
| leftover of exist-opposite HOLD | not this split display |
| leftover of nmcover axis-cover HOLD | not this split display |
| leftover of nm2axz axis-cover HOLD | not this split display |
| leftover of nm2ax12z `t+1` only | not this freeze |
| leftover of nm2splt2z `t` versus `t+1` | not this freeze; Do not score τ=t |
| y-probe or x-probe split on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| leftover of reverse/face bit composition | not this display |
| leftover of 2-in 1-out composition | not this display; that leftover HOLDs |
| leftover of cover composition | not this display; that leftover HOLDs |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| empty `O` at `t` as this letter | refused; Do not score τ=t |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out split at `t+1` versus `t+2` on the four z-probes of the two-axis opposite seed, reverse/face at each cut, and composition. |
| V2 | Current main has no landed 1-in 2-out split at `t+1` versus `t+2` reverse/face composition on these four z-probes of the two-axis opposite seed. |
| V3 | Split reports at two cuts, the four reverse/face bits, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out split of own incoming and own outgoing at `t+1` and at `t+2` and scores composition as equality of those four split bits. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover-empty fail, does not
replace split by leftover of `M` alone or leftover of `O` alone, does not
replace split by existential opposite of signed locks, does not replace
split by nmcover axis-cover, does not replace split by nm2axz axis-cover,
does not replace this freeze by nm2ax12z at `t+1` only, does not replace
this freeze by nm2splt2z at `t` versus `t+1`, does not identify this
display with the 1-axis opposite two-site seed, and does not identify it
with nmunopp union. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2splt2z `t` versus `t+1` | reuse composition fail from empty `O` at `t` | Do not score τ=t; here `O` is nonempty and the HOLDING 3-split freezes | ATTEMPTED |
| nm2ax12z `t+1` only | reuse split reverse hold and face hold at `t+1` | that leftover does not score `τ=t+2`; here freeze of those bits is the letter | ATTEMPTED |
| nmcover axis-cover | score reverse/face as cover HOLD | on the 1-axis opposite two-site seed cover HOLDs at every z-probe at `t+1` so cover face HOLDs, while split face fails at `C` from 2-in 1-out; cover without `|Axis(M)|=1` is not this object | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs at `t+1` and split HOLDs at `t+1` because `|Axis(M)|=1`; 2-in 1-out remains cover HOLD and split fail on the 1-axis z-probes; neither leftover scores freeze at `t+2` as this 1-in 2-out object | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at each probe at both cuts, leftover reverse and face fail, while split reverse and face HOLD | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal, reverse would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal, reverse would fail | ATTEMPTED |
| exist-opposite | reuse signed reverse/face of `O` | exist-opposite face of signed `O` fails while split face HOLDs | ATTEMPTED |
| reverse/face bit composition | score composition on reverse/face bits | those bits also freeze here, but the letter is equality of the four split bits | ATTEMPTED |
| 2-in 1-out composition | score composition on 2-in 1-out bits | 2-in 1-out fails at both cuts, so that leftover HOLDs; it is not 1-in 2-out | ATTEMPTED |
| cover composition | score composition on cover bits | cover also freezes; cover without `|Axis(M)|=1` is not this object | ATTEMPTED |
| nmot2opp `O` two-tick | reuse exist-opposite of `O` at `t` versus `t+1` | empty then HOLD `O` with `UNDEFINED` then hold is not HOLDING split freeze | ATTEMPTED |
| nmt2opp `M` two-tick | reuse frozen `M` | `M` is frozen; this letter is split of `M` and `O` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; split is unsigned 1-in 2-out of `M` and `O` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ1)` remains a set; split still HOLDs at both cuts | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| empty `O` as this letter | treat empty outgoing at `t` as the freeze | Do not score τ=t; empty O at t fails split as leftover of nm2splt2z | ATTEMPTED |
| new 6-NN enters `O` | treat `(0,-1,1)` as a new outgoing of `A` at `t+2` | that neighbor locks `{+e_3}`; step `−e_2` from `A` is not in its incoming set | ATTEMPTED |
| letter intersection as split | score reverse/face inside `M ∩ O` | letter intersection empty is not 1-in 2-out; opposite signs can share an axis | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, split fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` at both cuts | ATTEMPTED |
| y-probe split | score the four y-probes on this seed | y-probe face fails at `D`; this letter is the four z-probes | ATTEMPTED |
| x-probe split | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores 1-in 2-out of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports hold then hold, with composition hold | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is cover plus `|Axis(M)|=1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | cuts are `τ1=t+1` and `τ2=t+2` per probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover of
`M` alone, missing identification of split with leftover-empty fail, missing
identification of split with existential opposite of signed locks, missing
identification of split with nmcover axis-cover, missing identification of
split with nm2axz axis-cover, missing identification of this freeze with
nm2ax12z at `t+1` only, missing identification of this freeze with
nm2splt2z at `t` versus `t+1`, missing identification of this seed with the
1-axis opposite two-site seed, and missing Record identification of split
reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe cuts
`τ1=t+1` and `τ2=t+2`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, Do not score τ=t,
2-in 1-out as fail not `UNDEFINED`, four z-probes with seed `A`,
second pair as a new seed not a formed child, mixed remains a set, and
composition as equality of the four split bits are declared. No uniqueness
of incoming locks, no six-neighbor lock union as the scored object, no
lock-count clock, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold` reports and composition hold do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split reports at t+1 and at t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** New 6-NN of `A` at `t+2` must enter `O`, so freeze fails;
empty `O` at `t` is the letter; composition of reverse/face bits is the
letter; cover freeze is this letter; 2-in 1-out composition HOLD means
split composition HOLD; nm2ax12z already displayed split reverse hold and
face hold; nm2splt2z already displayed two-tick composition; leftover of
`M` alone already answers reverse; and exist-opposite already answers
reverse.

**Answer:** The new 6-NN `(0,-1,1)` locks `{+e_3}`; the step from `A` is
`−e_2`, which is not in that incoming set, so it does not enter `O`. `O`
is frozen. Do not score τ=t. Empty O at t fails split as leftover of
nm2splt2z. Split bits stay hold at each of `A`, `B`, `C`, and `D`, so
composition of those four bits HOLDs. Reverse/face bit composition also
HOLDs on this member, but it is a leftover predicate. Cover also freezes,
but cover without `|Axis(M)|=1` is not this object. 2-in 1-out fails at
both cuts, so 2-in 1-out composition HOLDs as a leftover. nm2ax12z scores
only `t+1`. nm2splt2z scores `t` versus `t+1` with composition fail.
Leftover of `M` alone at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`:
nonempty unequal, so leftover-of-`M` reverse fails while split reverse
HOLDs. Exist-opposite face of signed `O` fails while split face HOLDs.
Reverse 1-in 2-out is HOLD iff split at `A` and at `B` at that cut, not
leftover of nm2ax12z or nm2splt2z.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M` on
the 1-axis opposite two-site seed. nmcover axis-cover on that seed reported
cover HOLD at each of the four z-probes, reverse hold, and face hold, with
split face fail from 2-in 1-out at `C`. nm2axz cover on this two-axis seed
reported cover HOLD at each of the four z-probes, reverse hold, and face
hold, with `|Axis(M)|=1` at each probe. nm2ax12z reported 1-in 2-out split
HOLD at `t+1` on these four z-probes, reverse hold, and face hold, without
scoring `τ=t+2`. nm2splt2z reported 1-in 2-out split fail at `t` from empty
`O` and HOLD at `t+1`, reverse fail then hold, face fail then hold, and
composition fail. The four y-probes of this same seed reported split reverse
hold and split face fail at `t+1`, frozen at `t+2`. nmot2opp reported empty
then HOLD `O` with exist-opposite `UNDEFINED` then hold. This note is not
those displays: it reports 1-in 2-out split at `t+1` versus `t+2` on the
two-axis opposite seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=1`,
split HOLD at `τ1`, split HOLD at `τ2`, reverse hold then hold, face hold
then hold, and composition hold. Do not score τ=t.

**Gate disposition:** PASS for the 1-in 2-out `t+1` versus `t+2` reverse/face
and composition reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals nmcover axis-cover HOLD,” “the
predicate equals nm2axz axis-cover HOLD,” “the predicate equals nm2ax12z
at `t+1` only,” “the predicate equals nm2splt2z at `t` versus `t+1`,”
“the predicate equals the 1-axis opposite two-site seed,” “the predicate
equals nmunopp union,” “the predicate equals 2-in 1-out composition HOLD,”
“bits are Admissibility,” “2-in 1-out is UNDEFINED,” “score `τ=t`,”
“composition fail,” or “split fails at `τ2`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
at that probe's `t+2`, reports unsigned axis of each, reports cover of the
pair, reports `|Axis(M)|` and the 1-in 2-out split at each cut, lists new
records in `B_3(0)` between `t` and `t+1` and between `t+1` and `t+2` that
meet a probe's six-neighbors, reports reverse and face at each cut, reports
composition of the four split bits, and checks Theorems 1--3. It also
checks that Do not score τ=t, that leftover empty O at t fails split and
makes nm2splt2z composition fail, that split HOLDs at `A`, `B`, `C`, and
`D` at `t+1` and at `t+2`, that 2-in 1-out is fail not `UNDEFINED`, that
2-in 1-out composition HOLDs as a leftover, that the 1-axis opposite
two-site seed is a different member with split face fail at `C`, that
leftover-empty fail is a different reverse and face, that leftover of `M`
alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that unique-letter split is `UNDEFINED` at mixed `O`, that
the new 6-NN of `A` at `t+2` does not enter `O`, that the construction does
not sum, that a formation member from already-recorded six-neighbor locks
is not attached, that the second pair is a new seed not a formed child,
that the y-probes and x-probes of this seed are not this letter, and that
the display is not the two-tick lock-count clock composition. No runner
cache is written.
