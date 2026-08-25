---
claim_id: two_axis_opposite_xprobe_simultaneous_incoming_outgoing_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_simultaneous_incoming_outgoing_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Simultaneous Own-Incoming And Own-Outgoing Freeze t+1 Versus t+2 Reverse And Face On Four Two-Axis Opposite X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ1=t+1` versus `τ2=t+2`, reverse/face from simultaneous HOLD
at each cut, and composition of `M` and `O`, on the four x-probes of the
two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same perp-step incoming-lock
process and x-probes as nm2axpx. Let `t(q)` be the formation tick of probe
`q`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T. Do not score τ=t. `M(q,τ)` is the set of earliest incoming nearest-neighbor steps
at `q` using only records with tick `<= τ`. Seeds are a singleton seed
letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`.
Intersection is `M(q,τ) ∩ O(q,τ)`; unformed is `UNDEFINED`. Empty
intersection is empty, not `UNDEFINED`. Simultaneous HOLDs at `q,τ` if and
only if both `M` and `O` are defined nonempty and `M ∩ O` is empty.
`UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail. Reverse HOLDs at a cut
if and only if simultaneous HOLDs at `A` and at `B`. Face HOLDs if and only
if simultaneous HOLDs at `C` and at `D`. Composition HOLDs if and only if
`M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A`, `B`, `C`, and `D`. This is HOLD
iff simultaneous, not leftover-empty fail of leftover axis. This is the
first simultaneous freeze display of `M` and `O` from `t+1` to `t+2` on
the nm2simx HOLDING sim x-probe member. nm2simx reports simultaneous HOLD
at one cut `τ=t+1` with reverse hold and face hold. nm2ot3x reports O
freeze composition HOLD with exist-opposite reverse fail and face fail.
nm2axx cover reverse FAIL face FAIL (union misses e_2 at `A` and at `D`;
axes still disjoint). nm2axpx forall-perp reverse HOLD face HOLD on these
same probes is a different predicate. This is not leftover of nm2simx.
This is not leftover of nm2ot3x. This is not leftover of nm2axx cover.
This is not leftover of nm2axpx forall-perp. This is not leftover of
nm2simz z-probe simultaneous. This is not leftover-empty fail. This is
not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover of nmsimopp exist-opposite of
`M` and of `O` at `t+1`. This is not leftover of nmunopp union. This is
not leftover of nmt2opp `M` frozen at `t`. This is not leftover of
nmot2opp two-tick composition. This is not leftover of nmoutopp untimed
eventual-`O`. This is not leftover of mixed #7188 fail/fail. Uniqueness is
not required. Mixed remains a set. Occupancy of sites is not used.
Occupancy `n` is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_simultaneous_incoming_outgoing_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_simultaneous_incoming_outgoing_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Simultaneous is signed-letter disjointness of nonempty
`M` and nonempty `O` at the same cut. Reverse and face are scored on
simultaneous HOLD at the paired probes. Composition is equality of both `M`
and `O` across the two cuts. Named signs `{+,−}` are a coarser readout and
are not used. A singleton unique lock letter is a different readout and is
not used as the object. Existential opposite of signed locks is a different
readout and is not used as the simultaneous reverse. Unsigned axis-cover of
`M` and `O` is a different readout and is not used. Forall-orthogonal of
`M` versus `O` is a different readout and is not used. Leftover-empty fail
of unsigned leftover axis sets is a different readout and is not used. A
`Z^3` sum of those locks is a different readout and is not used. Occupancy
of sites is not used. The construction does not use occupancy. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M and O at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut from simultaneous HOLD, and composition of M and O; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_simultaneous_incoming_outgoing_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display simultaneous M and O freeze from t+1 to t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut from sim, and composition"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M and O freeze displayed; do not write simultaneous or composition into Admissibility, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace simultaneous reverse by existential opposite of signed locks, do not replace simultaneous by unsigned axis-cover, do not replace simultaneous by forall-perp, do not replace either set by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
simultaneous `M` and `O` freeze is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and x-probes as nm2axpx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. First pair:
`L(0)=+e_1` and `L(0,1,0)=−e_1`. Second pair: `L(0,0,1)=+e_2` and
`L(0,1,1)=−e_2`. The second pair is a new seed, not a formed child of the
first pair. This seed is not the one-axis opposite two-site seed alone.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
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

## Named simultaneous `M` and `O` at `τ1=t+1` and `τ2=t+2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T. Do not
score τ=t.

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
Occupancy of sites is not used. Occupancy `n` is not used. O is not M.

Intersection at the same cut:

```text
(M ∩ O)(q,τ) = M(q,τ) ∩ O(q,τ).
```

If `q` is unformed at `τ`, then the intersection is `UNDEFINED`. Empty
intersection is empty, not `UNDEFINED`.

Simultaneous at a probe at the same cut:

```text
sim(q,τ) HOLDs iff M and O are defined nonempty and M ∩ O is empty.
```

If `q` is unformed at `τ`, then simultaneous is `UNDEFINED`. Empty `M` or
empty `O` fails. Nonempty overlapping letters fail. Simultaneous is signed
letter disjointness: `+e_i` and `−e_i` are distinct letters. Unsigned
axis-cover is a different object: opposite signs occupy the same axis, so
letter-disjoint sets can fail cover. Leftover of the union of unsigned
axes is `{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))`. Empty leftover is
leftover fail of leftover axis; this display is HOLD iff simultaneous, not
leftover-empty fail. Forall-perp is a different object: `{+e_1}` and
`{−e_1}` are letter-disjoint and have integer dot `-1`.

Reverse simultaneous holds at a cut if and only if simultaneous HOLDs at
`A` and at `B`. Face simultaneous holds if and only if simultaneous HOLDs
at `C` and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both
sides HOLD, reverse or face HOLDs. Else fail.

Composition holds if and only if `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A`,
`B`, `C`, and `D`. Any `UNDEFINED` side is `UNDEFINED`. Else if the four
`M` pairs and the four `O` pairs are equal, composition HOLDs. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
simultaneous reverse is refused: leftover-empty fail scores empty leftover
axis as fail. Identifying unsigned axis-cover with simultaneous is refused:
on this seed x-probe `A` has letter-disjoint nonempty `M` and `O` and fails
complementary occupation of `{e_1,e_2,e_3}` because the union misses e_2.
Identifying forall-perp with simultaneous is refused: integer-dot zero is
not signed-letter disjointness. Identifying nm2ot3x exist-opposite reverse
fail with this reverse is refused: exist-opposite of signed `O` fails while
simultaneous reverse HOLDs. Identifying nm2simx one-cut simultaneous with
this freeze is refused: that leftover scores only `τ=t+1`.

## Theorem 1 — ticks, `M`, `O`, and sim at `τ1` and `τ2`

On this process the four x-probes form. Compare to leftover axis: leftover
of the unsigned-axis union is `{e_2}` at `A` and at `D` and empty at `B`
and at `C`, so leftover reverse fail and leftover face fail. Compare to
axis-cover on these x-probes: that leftover reports complementary unsigned
axes HOLD at `B` and at `C` and FAIL at `A` and at `D` (union misses e_2;
axes still disjoint), so cover reverse FAIL face FAIL. Compare to nm2axpx
forall-perp: that leftover reports forall-perp HOLD at each probe. Compare
to nm2ot3x: that leftover reports `O` freeze with exist-opposite reverse
fail and face fail. This display reads signed-letter simultaneous of those
same timed sets at both cuts, and freeze of both `M` and `O`:

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
sim(A, τ1) = hold
sim(B, τ1) = hold
sim(C, τ1) = hold
sim(D, τ1) = hold
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1, −e_1}
sim(A, τ2) = hold
sim(B, τ2) = hold
sim(C, τ2) = hold
sim(D, τ2) = hold
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ)` has three outgoing steps,
`O(C,τ)` has three outgoing steps, and `O(D,τ)` has two outgoing steps on
one axis. Unique letters would assign `UNDEFINED` at mixed `O` and would
leave reverse and face `UNDEFINED`. Here uniqueness is not required. `M` is
frozen from `t` to `t+1` and remains frozen from `τ1` to `τ2`. At `t`, `O`
is empty at `A`, `B`, and `C`, so simultaneous fails at those probes; at
`D`, `O(D,t)={−e_1}` is already nonempty and simultaneous HOLDs at the
own-tick cut while cover still fails. At `τ1=t+1` and at `τ2=t+2`, `O` is
nonempty at every scored probe, intersection is empty, and simultaneous
HOLDs. At each probe, `M` and `O` are defined nonempty and disjoint as
signed letters. Simultaneous therefore HOLDs at each probe at both cuts.
Leftover of the unsigned-axis union is `{e_2}` at `A` and at `D` and empty
at `B` and at `C`; leftover-empty fail of that leftover is not this object.
Axis-cover fails at `A` and at `D` because the union misses e_2; that
unsigned complementary occupation is not this letter. Forall-perp HOLDs at
each of these four x-probes; integer-dot zero is not this letter. O is not
M.

On the one-axis opposite two-site seed, `A=(1,0,0)` forms later than tick
2. Here the second pair is seeded at tick 0, and `A` forms at tick 2.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. No new six-neighbor
of any scored probe forms at `t+2`, so neither `M` nor `O` can grow between
`τ1` and `τ2`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
new 6-NN of A at t(A)+2: none
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse simultaneous holds if and only if simultaneous HOLDs at `A` and at
`B`. Both simultaneous reports HOLD at `τ1` and at `τ2`. Reverse HOLDs at
both cuts. Face simultaneous holds if and only if simultaneous HOLDs at `C`
and at `D`. Both simultaneous reports HOLD at `τ1` and at `τ2`. Face HOLDs
at both cuts. This is HOLD iff simultaneous, not leftover-empty fail.

Reverse simultaneous at τ1: hold
Reverse simultaneous at τ2: hold
Face simultaneous at τ1: hold
Face simultaneous at τ2: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the unsigned-axis union is `{e_2}` at `A` and
empty at `B`. Simultaneous reverse HOLDs from signed-letter disjoint
nonempty `M` and `O` at both reverse probes. Leftover-of-`M` reverse would
fail because leftover of `M` at `A` is `{e_1, e_2}` and leftover of `M` at
`B` is `{e_2, e_3}`: nonempty and unequal. Leftover-of-`O` reverse would
fail because leftover of `O` at `A` is `{e_2, e_3}` and leftover of `O` at
`B` is `{e_1}`: nonempty and unequal. Exist-opposite reverse of signed `M`
fails. Exist-opposite reverse of signed `O` fails. Those leftovers are not
this display. Unsigned axis-cover reverse FAILs on these x-probes because
cover fails at `A`. Forall-perp reverse HOLDs on these x-probes; that is
not this letter. nm2ot3x scores exist-opposite of `O` and reports reverse
fail face fail at both cuts; that leftover is not this reverse.

Reverse holds at τ1 and at τ2.
Face holds at τ1 and at τ2.

## Theorem 3 — composition of `M` and `O`

Composition holds if and only if `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A`,
`B`, `C`, and `D`. Both `M` and `O` freeze at every scored probe.

Composition of M and O: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Scoring `τ=t` is leftover of nmot2opp: `O` is empty at `A`, `B`, and `C` at
formation, so simultaneous fails there, and composition of the pair
`(t, t+1)` fails. Scoring O freeze only is leftover of nm2ot3x: that
leftover HOLDs on these probes but pairs with exist-opposite reverse fail.
Scoring one-cut simultaneous is leftover of nm2simx: that leftover HOLDs
reverse and face at `τ=t+1` only. Bit-stability of reverse/face is a
leftover predicate; this letter scores equality of the `M` sets and the
`O` sets themselves. Composition of M and O: hold, while reverse and face
remain hold at both cuts from simultaneous.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Simultaneous HOLDs.

On the same seed the four y-probes give simultaneous reverse hold and
simultaneous face hold, but y-probe axis-cover face fails at `D`. The four
z-probes give simultaneous reverse hold and simultaneous face hold, and
z-probe axis-cover also HOLDs at each z-probe. Those probe-direction
readouts are not this x-probe display. Letter-disjoint nonempty is not
complementary axis-cover. Cover fail at `A` and at `D` is the split that
this member first displayed for simultaneous at one cut and now displays
as freeze.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require simultaneous sides to be singletons.
- It does not sum either set.
- It does not replace simultaneous by leftover-empty fail.
- It does not replace simultaneous by leftover of `M` alone.
- It does not replace simultaneous by leftover of `O` alone.
- It does not replace simultaneous by existential opposite of signed locks.
- It does not replace simultaneous by unsigned axis-cover of `M` and `O`.
- It does not replace simultaneous by forall-perp of `M` versus `O`.
- It does not replace simultaneous by 1-in 2-out axis split.
- It does not replace `O` by `M`.
- It does not replace simultaneous by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this simultaneous display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint nm2simx one-cut simultaneous as this freeze.
- It does not reprint nm2ot3x O-only freeze with exist-opposite reverse fail.
- It is not named-sign lettering: a named sign would have lost the axis.
- It is not a unique lock-vector leftover and does not sum; it is not a sum leftover.
- It is not leftover of unique-L.
- It does not treat the second opposite pair as a formed child of the first.
- It does not score the y-probes or the z-probes as this letter.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite process, simultaneous `M` and `O` at `t+1` versus `t+2`,
reverse/face bits from simultaneous HOLD, and composition are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ1` and `τ2` | Theorem 1; frozen equal across the two cuts |
| `O` at `τ1` and `τ2` | Theorem 1; frozen outgoing dual |
| sim at `τ1` and `τ2` | Theorem 1; HOLD at each probe at both cuts |
| reverse from simultaneous at `τ1` and `τ2` | Theorem 2; `hold`/`hold` |
| face from simultaneous at `τ1` and `τ2` | Theorem 2; `hold`/`hold` |
| composition of `M` and `O` | Theorem 3; `hold` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this simultaneous freeze |
| leftover of nm2axx axis-cover FAIL | not this simultaneous freeze |
| leftover of nm2axpx forall-perp HOLD | not this simultaneous freeze |
| leftover of nm2simx one-cut simultaneous | not this freeze letter |
| leftover of nm2ot3x O-only freeze | not this joint freeze |
| leftover of nm2simz z-probe simultaneous | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmsimopp exist-opposite HOLD | not this simultaneous display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| one-axis opposite leftover of the second pair | not this seed |
| y-probe or z-probe simultaneous on this seed | not this letter |
| global later T | not used |
| simultaneous as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: do `M` and `O` both freeze from `t+1` to `t+2` on the HOLDING sim x member, and reverse/face from sim at each cut. |
| V2 | Current main has no landed simultaneous freeze reverse/face of timed `M` and `O` on these four x-probes of this two-axis opposite seed. |
| V3 | Simultaneous reports at two cuts, reverse/face bits, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads signed-letter disjointness of own incoming and own outgoing at `t+1` versus `t+2` and scores composition of both sets. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace simultaneous by leftover-empty fail, does not
replace simultaneous by leftover of `M` alone or leftover of `O` alone,
does not replace simultaneous by existential opposite of signed locks, does
not replace simultaneous by unsigned axis-cover, does not replace
simultaneous by forall-perp, does not identify this display with nmsimopp
exist-opposite HOLD, does not identify it with nmunopp union, does not
identify it with nm2simx one-cut simultaneous, and does not identify it
with nm2ot3x O-only freeze. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the unsigned-axis union is `{e_2}` at `A` and at `D` and empty at `B` and at `C`, leftover reverse and face fail, while simultaneous HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal, reverse would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal, reverse would fail | ATTEMPTED |
| nmsimopp exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | signed `M` reverse fails and signed `O` reverse fails; simultaneous reverse HOLDs from per-probe letter-disjoint nonempty `M` and `O` | ATTEMPTED |
| nm2axx axis-cover | reuse complementary unsigned axes of `M` and `O` | cover reverse FAIL face FAIL because the union misses e_2 at `A` and at `D`; simultaneous HOLDs | ATTEMPTED |
| nm2axpx forall-perp | reuse every integer dot `m·o=0` | `{+e_1}` and `{−e_1}` are letter-disjoint and have integer dot `-1`; forall-perp is not simultaneous | ATTEMPTED |
| nm2simx one-cut | score simultaneous only at `τ=t+1` | this letter also scores `τ2=t+2` and composition of `M` and `O` | ATTEMPTED |
| nm2ot3x O freeze | score `O(τ1)=O(τ2)` with exist-opposite reverse/face | O freeze HOLDs, but exist-opposite reverse and face fail; this reverse is from simultaneous | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters without a disjointness test against the pair | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)`, `O(C,τ)`, and `O(D,τ)` remain sets; simultaneous still HOLDs; unique-letter reverse is `UNDEFINED` | ATTEMPTED |
| exist-opposite of leftover axes | score `a+b=(0,0,0)` inside leftover axis vectors | leftover reverse is leftover-empty fail here; simultaneous reverse is HOLD iff simultaneous | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover is neighbor locks; simultaneous is own `M` against own `O` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores simultaneous freeze of own incoming and outgoing | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports simultaneous HOLD and reverse hold face hold | ATTEMPTED |
| one-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/−e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/−e_2` at tick 0 | ATTEMPTED |
| y-probe simultaneous | score the four y-probes on this seed | y-probe `A` locks `−e_1` at tick 0; this letter is the four x-probes with non-seed `A` locking `−e_3` at tick 2 | ATTEMPTED |
| z-probe simultaneous | score the four z-probes on this seed | z-probe `A` is a seed locking `+e_2`; this letter is the four x-probes | ATTEMPTED |
| sum of a set | replace simultaneous by a `Z^3` sum | the construction does not sum; simultaneous is signed-letter disjointness of two sets | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by simultaneous freeze | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of simultaneous with
leftover of `M` alone, missing identification of simultaneous with
leftover-empty fail, missing identification of simultaneous with
existential opposite of signed locks, missing identification of
simultaneous with unsigned axis-cover, missing identification of
simultaneous with forall-perp, missing identification of this freeze with
nm2simx one-cut or nm2ot3x O-only freeze, and missing Record identification
of simultaneous reverse are distinct open premises. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite-pair seed locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ1=t+1` and `τ2=t+2`, simultaneous as defined nonempty disjoint `M` and
`O`, HOLD iff simultaneous not leftover-empty fail, composition as equality
of both `M` and `O`, four x-probes with non-seed `A`, and mixed remains a
set are declared. No uniqueness of incoming locks, no six-neighbor lock
union as the scored object, no lock-count clock, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
simultaneous freeze `hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock among `{±e_1,±e_2,±e_3}` in `M` or in `O` at `t+1` and `t+2` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four sim reports at t+1 and t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for simultaneous reverse/face,
a formation-rate rule, and a physical selector among disjoint incoming and
outgoing letters. None is taken here.

### N7 — hostile steelman

**Steelman:** Simultaneous freeze HOLD is only leftover empty; leftover-empty
fail already answered three-axis occupation; leftover of `M` alone already
gives a third direction; complementary occupation is only nm2axx cover;
empty letter intersection is only nmsimopp; forall-perp already HOLDs on
these x-probes; nm2simx already HOLDs simultaneous at `t+1`; nm2ot3x already
HOLDs O freeze; the second pair is only a child of the first pair; mixed `O`
should make the predicate `UNDEFINED`; and empty `M` or empty `O` should be
`UNDEFINED` like unformed.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that leftover as reverse fail and face
fail. On these x-probes leftover of the unsigned-axis union is `{e_2}` at
`A` and at `D` and empty at `B` and at `C`, so leftover reverse and face
fail while simultaneous HOLDs. Simultaneous HOLDs when `M` and `O` are
defined nonempty and signed-letter disjoint. Opposite signs on one axis
are letter-disjoint and occupy that axis, so they can HOLD simultaneous
and fail cover. On this seed, x-probe `A` HOLDs simultaneous with
`M={−e_3}` and `O={+e_1}` and fails cover because the union misses e_2.
x-probe `D` HOLDs simultaneous with mixed `O={+e_1, −e_1}` and fails cover
for the same missing axis. Cover HOLDs at `B` and at `C`, but that is
unsigned complementary axes, not this letter. Forall-perp also HOLDs at
each of these four x-probes; `{+e_1}` and `{−e_1}` are letter-disjoint with
integer dot `-1`, so simultaneous is not forall-perp. nm2simx scores only
the one-cut simultaneous; this letter also scores `τ2` and composition of
both `M` and `O`. nm2ot3x scores O freeze with exist-opposite reverse fail
and face fail; this reverse is from simultaneous and HOLDs. Leftover of `M`
alone and leftover of `O` alone are nonempty one-sided leftovers and are
unequal across reverse here. The second pair is seeded at tick 0 with
`+e_2/−e_2`, not formed at tick 1 with `+e_3`. Mixed `O(B,τ)` remains a
set and simultaneous at `B` HOLDs. Empty `M` or empty `O` fails by
declaration, and is not `UNDEFINED`. Reverse simultaneous is HOLD iff
simultaneous at `A` and at `B`, not leftover-empty fail.

### N8 — cross-cycle echo

nm2axx reported axis-cover of `M` versus `O` on these four x-probes with
reverse fail and face fail because the union misses e_2; axes still
disjoint. nm2axpx reported forall-orthogonal `M` versus `O` on these same
four x-probes with reverse hold and face hold. nm2simx reported
simultaneous `M` and `O` at `τ=t+1` on these four x-probes with reverse
hold and face hold. nm2ot3x reported O freeze from `τ1` to `τ2` with
exist-opposite reverse fail and face fail and composition HOLD. nm2simz
reported simultaneous `M` and `O` at `τ=t+1` on the four z-probes with
reverse hold and face hold, where cover also HOLDs at each z-probe.
Leftover axis reported leftover reverse fail and leftover face fail. This
note is not those displays: it reports simultaneous `M` and `O` at `t+1`
versus `t+2` on the four x-probes of the two-axis opposite seed,
simultaneous HOLD at each of the four x-probes at both cuts, reverse hold
and face hold at each cut, and composition HOLD of both `M` and `O`. HOLD
iff simultaneous, not leftover-empty fail, not axis-cover, not forall-perp,
not exist-opposite of `M` or of `O`, not leftover of nm2simx, and not
leftover of nm2ot3x.

**Gate disposition:** PASS for the simultaneous freeze `t+1` versus `t+2`
reverse/face/composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the predicate
equals nmsimopp exist-opposite HOLD,” “the predicate equals nm2axx
axis-cover,” “the predicate equals nm2axpx forall-perp,” “the predicate
equals nmunopp union,” “the predicate equals nm2simx one-cut simultaneous,”
“the predicate equals nm2ot3x O-only freeze,” “bits are Admissibility,”
“simultaneous fails,” “reverse simultaneous fails,” or “face simultaneous
fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports simultaneous of the pair at each cut, lists new records in
`B_3(0)` between `t` and `t+1` and between `t` and `t+2` that meet a
probe's six-neighbors, reports reverse and face from simultaneous HOLD at
each cut, reports composition of `M` and `O`, and checks Theorems 1--3. It
also checks that simultaneous HOLDs at each probe at both cuts, that
leftover-empty fail is a different reverse and face, that leftover of `M`
alone and leftover of `O` alone are different objects, that mixed sets
remain sets, that unique-letter simultaneous is `UNDEFINED` at mixed `O`,
that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a seed and not a formed child, that unsigned axis-cover is a different
letter and FAILs reverse and face on these x-probes, that forall-perp is a
different letter, that nm2ot3x exist-opposite reverse fail is a different
letter, that nm2simx one-cut simultaneous is a different letter, and that
the display is not the two-tick lock-count clock composition. No runner
cache is written.
