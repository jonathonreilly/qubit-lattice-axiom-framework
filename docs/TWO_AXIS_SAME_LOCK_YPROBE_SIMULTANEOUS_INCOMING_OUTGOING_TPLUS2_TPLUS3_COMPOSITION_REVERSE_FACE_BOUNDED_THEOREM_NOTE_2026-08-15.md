---
claim_id: two_axis_same_lock_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+2 versus t+3 on the four y-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py
---

# T-Plus-Two Versus T-Plus-Three Composition Of Simultaneous Incoming And Outgoing Reverse And Face On Four Two-Axis Same-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `t+2` versus `t+3`, reverse/face from simultaneous HOLD at
each cut, and composition of both sets, on the four y-probes of the
two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes
as nm2slo. Let `t(q)` be the formation tick of probe `q`. Let
`τ1(q)=t(q)+2` and `τ2(q)=t(q)+3`. There is no global T. Do not score τ=t.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Simultaneous HOLDs at `q,τ` if and only if both `M` and `O`
are defined nonempty and `M ∩ O` is empty. `UNDEFINED` if `M` or `O` is
`UNDEFINED`. Else fail. Reverse at a cut HOLDs if and only if simultaneous
HOLDs at `A` and at `B` at that cut. Face likewise on `C,D`. Composition
HOLD if and only if `M(q,τ1)=M(q,τ2)` and `O(q,τ1)=O(q,τ2)` at `A`,`B`,`C`,
and `D`. Displayed, not adopted. This is the first display of simultaneous
`M` and `O` freeze from `t+2` to `t+3` on the nm2simt2sly HOLDING member.
This is not leftover of nm2simt2sly simultaneous freeze t+1 versus t+2.
This is not leftover of nm2simsly simultaneous at t+1. This is not leftover
of nm2ot3sly O freeze. This is not leftover of `M` two-tick. This is not
leftover of empty `O` at formation tick `t` with composition fail. This is
not leftover of nm2slo timed-O. This is not leftover of axis-cover. This is
not leftover of exist-opposite of `M`. This is not leftover of the one-axis
same-lock seed. This is not leftover of the two-axis opposite seed. This is
not leftover of unique own-outgoing letters. This is not leftover of mixed
#7188 fail/fail. This is not the two-tick lock-count clock composition.
Uniqueness of incoming or outgoing locks is not required. Mixed remains a
set. Occupancy `n` is not used. The construction does not use occupancy.
O is not M. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut.
Simultaneous is signed-letter disjointness of nonempty `M` and nonempty `O`
at the same cut. Reverse and face are scored on simultaneous HOLD at the
paired probes at that probe's `t+2` and at `t+3`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. Existential opposite of
signed locks is a different readout and is not used as the simultaneous
reverse. Unsigned axis-cover of `M` and `O` is a different readout and is
not used. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy of sites is not used. A six-neighbor star is not the
letter. This display does not use occupancy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M and O at each of the four two-axis same-lock y-probes at t+2 and at t+3, with reverse hold then hold, face hold then hold, and composition HOLD because M(tau1)=M(tau2) and O(tau1)=O(tau2) at A,B,C,D; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face
target_blocker_text: "display simultaneous M and O freeze from t+2 to t+3 on the four two-axis same-lock y-probes, reverse/face from sim at each cut, and whether those M and O sets compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M and O at t+2 versus t+3 displayed; do not write simultaneous into Admissibility, do not reduce to leftover of nm2simt2sly simultaneous freeze t+1 versus t+2, do not reduce to leftover of nm2simsly simultaneous at t+1, do not reduce to leftover of nm2ot3sly O freeze, do not replace simultaneous by leftover of M two-tick, do not score tau=t, do not replace simultaneous by exist-opposite of O, do not replace O by M, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for t+2 versus t+3 composition of simultaneous M and O reverse/face on the four two-axis same-lock y-probes, no global T; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
simultaneous `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is a seed. Same process and y-probes as nm2slo.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. Independently, `(0,0,1)` locks
`+e_2` and `(0,1,1)` locks `+e_2`. Neither pair is opposite. This seed is
not the one-axis two-site same-lock seed `{0,(0,1,0)}` both locking `+e_1`.
This seed is not the two-axis opposite seed that would lock the second pair
as `+e_2/−e_2`. This seed is not the y-symmetric three-site seed
`{0,(0,1,0),(0,-1,0)}`.

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

## Named simultaneous `M` and `O` at `t+2` and at `t+3`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+2` and `τ2(q)=t(q)+3`. There is no global T.
Do not score `τ=t`.

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
Occupancy `n` is not used. O is not M.

Simultaneous at a probe at a cut:

```text
sim(q,τ) HOLDs iff M and O are defined nonempty and M ∩ O is empty.
```

If `q` is unformed at `τ`, then simultaneous is `UNDEFINED`. Empty `M` or
empty `O` fails. Nonempty overlapping letters fail.

Reverse simultaneous holds if and only if simultaneous HOLDs at `A` and at
`B` at that cut. Face simultaneous holds if and only if simultaneous HOLDs
at `C` and at `D` at that cut. Either side `UNDEFINED` is `UNDEFINED`. Else
if both sides HOLD, reverse or face HOLDs. Else fail.

Composition HOLD if and only if `M(A,τ1)=M(A,τ2)`, `M(B,τ1)=M(B,τ2)`,
`M(C,τ1)=M(C,τ2)`, `M(D,τ1)=M(D,τ2)`, `O(A,τ1)=O(A,τ2)`, `O(B,τ1)=O(B,τ2)`,
`O(C,τ1)=O(C,τ2)`, and `O(D,τ1)=O(D,τ2)`. Else composition fails.
Displayed, not adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover of nm2ot3sly O
freeze with this letter is refused: that leftover freezes `O` and scores
exist-opposite of `O`, not simultaneous of `M` and `O`. Identifying leftover
of nm2simt2sly simultaneous freeze t+1 versus t+2 with this letter is
refused: that leftover already HOLDs reverse, face, and composition from
`t+1` to `t+2` and has no `t+3` freeze. Identifying leftover of nm2simsly
simultaneous at t+1 with this letter is refused: that leftover has no
`t+2` freeze. Identifying leftover of `M` two-tick with this letter
is refused: incoming is frozen from formation, and empty `O` at `t` makes
simultaneous fail at `τ=t`.

## Theorem 1 — ticks, `M`, `O`, and sim at `τ1` and at `τ2`

On this process the four y-probes form. Incoming is frozen at formation:
`M(q,τ2)=M(q,τ1)=M(q,t)` at every scored probe. Outgoing is empty at `t` at
each of the four probes, then filled at `t+1`, then frozen from `t+1` to
`t+2` on the nm2simt2sly leftover, then frozen from `t+2` to `t+3` here.
Compare to nm2simt2sly simultaneous freeze t+1 versus t+2: that leftover
reports reverse hold, face hold, and composition HOLD with no `t+3` cut.
Compare to nm2simsly simultaneous at t+1: that leftover reports the
`t+1` simultaneous HOLD with no `t+2` cut. Compare to nm2ot3sly O freeze:
that leftover reports `O` freeze and exist-opposite reverse/face, not
simultaneous. Compare to empty `O` at formation tick `t`: that leftover
scores `τ=t` versus `t+1` and reports empty `O` at `t` with composition
fail. Do not score `τ=t`. Both `M` and `O` freeze from `t+2` to `t+3`:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ1) = {+e_1}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_2}
M(D, τ1) = {−e_3}
O(A, τ1) = {+e_2, −e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ1) = {+e_1}
sim(A, τ1) = hold
sim(B, τ1) = hold
sim(C, τ1) = hold
sim(D, τ1) = hold
M(A, τ2) = {+e_1}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_2}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_2, −e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ2) = {+e_1}
sim(A, τ2) = hold
sim(B, τ2) = hold
sim(C, τ2) = hold
sim(D, τ2) = hold
```

`A` is a seed at tick 0. Mixed remains a set: `O(A,τ1)` has two outgoing
steps `+e_2` and `−e_3`, `O(B,τ1)` has three, and `O(C,τ1)` has four.
Unique own-outgoing letters would assign `UNDEFINED` at `A`, `B`, and `C`
at both cuts. Here uniqueness is not required. `M` and `O` are disjoint at
each of the four probes at both scored cuts. O is not M.

New records in `B_3(0)` at `t+2` that meet a probe's six-neighbors already
failed to enter `O` on the nm2simt2sly leftover. At `A`, those two
six-neighbors form at `t+2` and lock `−e_3`, not the step from `A`. At
`B`, one further six-neighbor forms at `t+3`. That site locks a mixed
incoming set without `+e_1`, so it does not enter `O(B,τ2)`:

```text
new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)
new 6-NN of B at t(B)+2: {}
new 6-NN of C at t(C)+2: {}
new 6-NN of D at t(D)+2: {}
new 6-NN of A at t(A)+3: {}
new 6-NN of B at t(B)+3: (2, 1, 1)
new 6-NN of C at t(C)+3: {}
new 6-NN of D at t(D)+3: {}
```

`D=(1,1,0)` and `(-1,1,0)` meet `A` at `t(A)+2` along `±e_1`. Seed `A`
locks `+e_1`, so a perp-step from `A` cannot take those steps. Both sites
lock `−e_3`, so those records do not enter `O(A)` at `τ1`. At `t(B)+3`,
`(2,1,1)` meets `B` along `+e_1`. That site forms at tick 4 with incoming
`{−e_2, +e_3, −e_3}`, so `+e_1` is not in `M((2,1,1),τ2)` and does not
enter `O(B)`. No new earliest incoming or outgoing step enters `M` or `O`
at any scored probe between `τ1` and `τ2`. Therefore `M(q,τ2)` equals
`M(q,τ1)` and `O(q,τ2)` equals `O(q,τ1)` at every scored probe.
Simultaneous HOLDs at each probe at both cuts.

M exist-opposite reverse fail: both `M(A,τ1)` and `M(B,τ1)` are `{+e_1}`.
Those incoming letters are absent from `O(A,τ1)` and `O(B,τ1)`. Axis-cover
leftover reports cover reverse hold and cover face fail because the unsigned
union misses e_2 at `D`. On the one-axis same-lock leftover `{0,(0,1,0)}`
both locking `+e_1`, the same y-probes form at ticks `0,2,1,3`, and `O(A)`
includes `+e_3`. That leftover is not this display. On the two-axis opposite
leftover, `M(A)={−e_1}` and `O(D)` includes `−e_1`.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse holds if and only if simultaneous HOLDs at `A` and at `B` at that
cut. At `τ1` both simultaneous reports HOLD. Reverse holds. At `τ2` both
simultaneous reports HOLD again, so reverse holds again.

Reverse at τ1: hold
Reverse at τ2: hold

Face holds if and only if simultaneous HOLDs at `C` and at `D` at that cut.
At `τ1` both simultaneous reports HOLD. Face holds. At `τ2` both
simultaneous reports HOLD again, so face holds again.

Face at τ1: hold
Face at τ2: hold

Unique own-outgoing letters on these y-probes report reverse `UNDEFINED` and
face `UNDEFINED` from mixed `O` at both cuts. M exist-opposite reverse fail
and M exist-opposite face fail. Axis-cover leftover reports cover reverse
hold and cover face fail. nm2slo timed-O leftover reports exist-opposite of
signed `O` reverse hold and face hold with no simultaneous test. Empty `O`
at `t` leftover reports simultaneous fail then hold because `O` is empty at
`τ=t`. Those are different objects. Reverse holds at `τ1` because
simultaneous HOLDs at `A` and at `B`. Reverse holds at `τ2` because those
simultaneous reports do not change.

## Theorem 3 — composition

Composition HOLD if and only if `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A`,
`B`, `C`, and `D`. Those eight equalities hold. Reverse is `hold` at `τ1`
and `hold` at `τ2`. Face is `hold` at `τ1` and `hold` at `τ2`. The bits
match because both sets match.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. New six-neighbor records
of `B` at `t+3` do not enter the outgoing dual: they lock a mixed set
without `+e_1`, not the step from `B`. `M(q,τ2)=M(q,τ1)` and
`O(q,τ2)=O(q,τ1)` at every scored probe. Simultaneous HOLDs at both cuts.

This is not leftover of empty `O` at `t` with composition fail: that leftover
reports simultaneous fail then hold because `O` enlarges from `t` to `t+1`.
Do not score `τ=t`. This is not leftover of nm2simt2sly simultaneous freeze
t+1 versus t+2: that leftover HOLDs reverse, face, and composition from
`t+1` to `t+2` with no `t+3` freeze. This is not leftover of nm2simsly
simultaneous at t+1: that leftover has no `t+2` freeze. This is not leftover
of nm2ot3sly O freeze: that leftover scores exist-opposite of `O`, not
simultaneous of `M` and `O`. This is not leftover of `M` two-tick: that
leftover freezes earliest incoming at formation, so `M(τ1)=M(t)`, while
empty `O` at `t` makes simultaneous fail; M exist-opposite reverse fail.
This is not leftover of nm2slo timed-O. This is not leftover of unique
own-outgoing letters (reverse `UNDEFINED`, face `UNDEFINED`). This is not
leftover of axis-cover (cover face fail). This is not leftover of
exist-opposite of `M`. This is not the two-tick lock-count clock
composition. This is not leftover of mixed #7188 fail/fail: that mixed
display reported reverse fail and face fail with composition HOLD. This is
not leftover of the one-axis same-lock seed. This is not leftover of the
two-axis opposite seed. The freeze of both `M` and `O` from `t+2` to `t+3`
is displayed on this two-axis same-lock seed, including at `B` where a new
six-neighbor record forms at `t+3` and still does not enter `O`.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require simultaneous sides to be singletons.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace simultaneous by leftover of `M` two-tick.
- It does not replace simultaneous by leftover of nm2ot3sly O freeze.
- It does not replace simultaneous by leftover of nm2simt2sly simultaneous freeze t+1 versus t+2.
- It does not replace simultaneous by leftover of nm2simsly simultaneous at t+1.
- It does not replace simultaneous by leftover of nm2slo timed-O.
- It does not replace simultaneous by leftover of axis-cover.
- It does not replace simultaneous by exist-opposite of `M`.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not score `τ=t`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-outgoing lock-vector letters as the object.
- It does not reprint empty-`O`-at-`t` fail/hold composition fail.
- It does not reprint the one-axis same-lock leftover.
- It does not reprint the two-axis opposite leftover.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy `n`.
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
two-axis same-lock process, simultaneous `M` and `O` at `t+2` and at `t+3`,
and the reverse/face/composition bits are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ1` and at `τ2` | Theorem 1; equal singleton sets; freeze |
| `O` at `τ1` and at `τ2` | Theorem 1; equal mixed or singleton sets; freeze |
| sim at `τ1` and at `τ2` | Theorem 1; HOLD at each probe at both cuts |
| compare O to M | Theorem 1; disjoint; O is not M |
| reverse and face at `τ1` and at `τ2` | Theorem 2; `hold` / `hold` at reverse; `hold` / `hold` at face |
| composition | Theorem 3; HOLD because `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A,B,C,D` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2simt2sly simultaneous freeze t+1 versus t+2 | not this display; no `t+3` cut there |
| leftover of nm2simsly simultaneous at t+1 | not this display; no `t+2` cut there |
| leftover of nm2ot3sly O freeze | not this display; exist-opposite of `O`, not sim |
| leftover of `M` two-tick | not this display; M exist-opposite reverse fail |
| leftover of empty `O` at `t` fail/hold | not this display; Do not score `τ=t` |
| leftover of nm2slo timed-O | not this display |
| leftover of unique own-outgoing letters | not this display |
| leftover of axis-cover | not this display; cover reverse hold, cover face fail |
| leftover of exist-opposite of `M` | not this display; M exist-opposite reverse fail |
| one-axis same-lock leftover | not this display; ticks `0,2,1,3` and `O(A)` includes `+e_3` |
| two-axis opposite leftover | not this display; `M(A)={−e_1}` and `O(D)` includes `−e_1` |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| simultaneous as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: simultaneous `M` and `O` at `t+2` versus `t+3` on the four two-axis same-lock y-probes, reverse/face at each cut, and whether those `M` and `O` sets compose. |
| V2 | Current main has no landed t+2 versus t+3 simultaneous reverse/face composition on these four two-axis same-lock y-probes. |
| V3 | Simultaneous `M` and `O` at two cuts and the `hold`/`HOLD` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads signed-letter disjointness of own incoming and own outgoing at two cuts and scores composition of both sets. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace simultaneous by leftover of `M` two-tick, does
not replace simultaneous by leftover of nm2ot3sly O freeze, does not
replace simultaneous by leftover of nm2simt2sly simultaneous freeze t+1
versus t+2, does not replace simultaneous by leftover of nm2simsly
simultaneous at t+1, does not identify this display with nm2slo timed-O,
does not reduce to leftover of axis-cover, and does not score `τ=t`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2simt2sly simultaneous freeze t+1 versus t+2 | score `t+1` versus `t+2` | that leftover reports reverse hold, face hold, and composition HOLD with no `t+3` freeze | ATTEMPTED |
| nm2simsly simultaneous at t+1 | score only `τ=t+1` | that leftover reports simultaneous HOLD reverse hold face hold with no `t+2` freeze | ATTEMPTED |
| nm2ot3sly O freeze | score `O(τ1)=O(τ2)` and exist-opposite of `O` | that leftover freezes `O` and scores exist-opposite reverse/face, not simultaneous of `M` and `O` | ATTEMPTED |
| empty `O` at `t` | score simultaneous at `t` versus `t+1` | that leftover reports fail then hold with composition fail; Do not score `τ=t` | ATTEMPTED |
| `M` two-tick | reuse earliest incoming `M` at `t` versus `t+1` | `M` is frozen from formation and disjoint from `O`; empty `O` at `t` fails simultaneous; M exist-opposite reverse fail | ATTEMPTED |
| nm2slo timed-O | reuse exist-opposite of signed `O` | exist-opposite of `O` HOLDs reverse and face; simultaneous is per-probe letter-disjoint nonempty `M` and `O` | ATTEMPTED |
| leftover of axis-cover | score complementary unsigned axes of `M` and `O` | cover HOLDs at `A`,`B`,`C` and fails at `D`; cover reverse hold and cover face fail, while simultaneous face HOLDs | ATTEMPTED |
| exist-opposite of `M` | score some pair in `M(A,τ)` against `M(B,τ)` | M exist-opposite reverse fail and M exist-opposite face fail; both `M(A)` and `M(B)` are `{+e_1}` | ATTEMPTED |
| unique own-outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | `O(A,τ1)` has two earliest outgoing steps; mixed remains a set; unique-letter reverse and face at both cuts are `UNDEFINED` | ATTEMPTED |
| one-axis same-lock leftover | drop the second pair and keep only `{0,(0,1,0)}` both `+e_1` | ticks become `0,2,1,3` and `O(A,τ1)` gains `+e_3` | ATTEMPTED |
| two-axis opposite leftover | lock the pairs as `+e_1/−e_1` and `+e_2/−e_2` | `M(A)` there is `{−e_1}` and `O(D)` includes `−e_1`; here `M(A)={+e_1}` and `O(D)={+e_1}` | ATTEMPTED |
| empty `O` as `UNDEFINED` | treat empty outgoing dual as unformed | leftover at `τ=t`; the probe is formed; empty `O` is empty, not `UNDEFINED`; this display does not score that cut | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)+1` | that leftover includes `+e_1` at `A` from the origin partner; `O(A,τ1)` does not contain `+e_1` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores simultaneous of own incoming and outgoing at two cuts, not a lock-count clock | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process and probes; this member reports hold then hold, with composition HOLD | ATTEMPTED |
| sum of `O` | replace each set by its `Z^3` sum | the construction does not sum; `sum O(A)=(0,1,−1)` and `sum O(B)=(0,1,0)` do not cancel | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+2` and `τ2(q)=t(q)+3` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by simultaneous | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of simultaneous freeze
with leftover of `M` two-tick, missing identification of simultaneous freeze
with leftover of nm2ot3sly O freeze, missing identification of simultaneous
freeze with leftover of nm2simt2sly simultaneous freeze t+1 versus t+2,
missing identification of simultaneous freeze with leftover of nm2simsly
simultaneous at t+1, missing identification of simultaneous with
exist-opposite of signed `O`, missing identification of simultaneous with
unsigned axis-cover, and missing Record identification of simultaneous
reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2`,
perpendicular step rule, incoming-step lock, own incoming set and own
outgoing dual from records with tick `<= τ`, per-probe `τ1=t+2` and
`τ2=t+3`, simultaneous as defined nonempty disjoint `M` and `O`, reverse
and face from sim, four y-probes with seed `A`, empty `O` empty not
`UNDEFINED`, mixed remains a set, Do not score `τ=t`, and composition as
equality of both `M` and `O` at the two cuts are declared. No uniqueness
of locks, no six-neighbor lock union as the scored object, no lock-count
clock, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock among `{±e_1,±e_2,±e_3}` in `M` or in `O` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `M` and `O` reports at two cuts plus sim/reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for simultaneous reverse/face,
a formation-rate rule, and a physical selector among disjoint incoming and
outgoing letters. None is taken here.

### N7 — hostile steelman

**Steelman:** After the nm2simt2sly `t+1` versus `t+2` freeze, simultaneous
should change at `t+3` the way `O` grew at `t+1`, so composition should
fail; freeze is only because the host is `B_3(0)`; `M` freeze from `t`
already answered two-tick composition; nm2ot3sly already displayed `O`
freeze so adding `M` is tautological; nm2simt2sly already displayed reverse
hold, face hold, and composition HOLD so this freeze is tautological;
nm2simsly already displayed reverse hold and face hold so this freeze is
tautological; y-symmetric and two-site opposite leftovers already answered
the same freeze on other seeds so this member is redundant; mixed `A` at
`τ1` should make reverse `UNDEFINED`; six-neighbor lock union already
answered hold/hold on this same process; axis-cover already answered reverse
hold; exist-opposite of `M` already answered signed reverse; mixed #7188
already answered two-tick composition as fail/fail with composition HOLD;
the two-tick lock-count clock already answered two-tick composition; named
signs should suffice; and composition HOLD is only tautological because no
children form at `t+3`.

**Answer:** A new six-neighbor record of `B` does form at `t+3`:
`(2,1,1)`. It locks `{−e_2, +e_3, −e_3}`, not the step from `B`, so it
does not enter `O`. `M(τ2)=M(τ1)` and `O(τ2)=O(τ1)` is the displayed freeze
after the nm2simt2sly `t+1` versus `t+2` cut, including at a probe whose
six-neighborhood is still filling. Empty `O` at `t` scored `τ=t` versus
`t+1` and reported composition fail; Do not score `τ=t`. `M` two-tick is a
different object: incoming is frozen from formation, disjoint from `O`,
empty `O` at `t` fails simultaneous, and M exist-opposite reverse fail.
nm2ot3sly is a different letter: it freezes `O` and scores exist-opposite of
`O`, not simultaneous of `M` and `O`. nm2simt2sly is a different pair of
cuts: it HOLDs reverse, face, and composition from `t+1` to `t+2` and has
no `t+3` freeze. nm2simsly is a different cut: it has no `t+2` freeze.
Y-symmetric and two-site opposite leftovers use different seeds; ticks here
are `0,1,1,2` and `O(A,τ1)` does not contain `+e_3`. Mixed `A` at `τ1`
remains the set `{+e_2, −e_3}`; reverse is `hold`, not `UNDEFINED`.
Six-neighbor lock union is a different object: it includes `+e_1` at `A`
while `O(A,τ1)` does not. Axis-cover face fails at `D`. M exist-opposite
reverse fail because both sides are `{+e_1}`. Mixed #7188 fail/fail is a
different process. The two-tick lock-count clock composition is a different
member. Named signs lost the axis. Composition HOLD is the displayed fact
that both `M(τ2)=M(τ1)` and `O(τ2)=O(τ1)` on this process; it is not an
Admissibility rewrite.

### N8 — cross-cycle echo

nm2simt2sly simultaneous freeze t+1 versus t+2 reported reverse hold, face
hold, and composition HOLD from simultaneous of `M` and `O` at `t+1` versus
`t+2` with no `t+3` cut. nm2simsly simultaneous at t+1 reported reverse hold
and face hold from simultaneous of `M` and `O` at `t+1` with no `t+2` cut.
nm2ot3sly O freeze reported reverse hold and face hold from exist-opposite
of `O` at `t+1` versus `t+2`. nm2slo timed-O reported exist-opposite HOLD of
signed `O` at `t+1` with no freeze. Axis-cover of `M` and `O` on these same
four y-probes and the same two-axis same-lock seed reports cover reverse
hold and cover face fail. One-axis same-lock leftover forms the same probes
at ticks `0,2,1,3` and puts `+e_3` in `O(A,τ)`. Two-axis opposite leftover
locks `A` as `−e_1` and puts `−e_1` in `O(D)`. Empty `O` at `t` reports
simultaneous fail then hold with composition fail because `O` enlarges from
`t` to `t+1`. `M` two-tick composition on this seed reports M exist-opposite
reverse fail and M exist-opposite face fail. Mixed #7188 two-tick
composition reported reverse fail and face fail with composition HOLD. A
two-tick lock-count clock composition scored a different clock, not
simultaneous of own incoming and outgoing. This note is not those displays:
simultaneous `M` and `O` at `t+2` versus `t+3` on the two-axis same-lock
seed, reverse is hold then hold, face is hold then hold, and composition
HOLD because `M(τ2)=M(τ1)` and `O(τ2)=O(τ1)` at `A,B,C,D`. Do not score
`τ=t`.

**Gate disposition:** PASS for the t+2 versus t+3 simultaneous reverse/face
composition reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals leftover of `M` two-tick,” “the predicate equals leftover
of nm2ot3sly O freeze,” “the predicate equals leftover of nm2simt2sly
simultaneous freeze t+1 versus t+2,” “the predicate equals leftover of
nm2simsly simultaneous at t+1,” “the predicate equals empty `O` at `t`
fail/hold,” “the predicate equals leftover of nm2slo timed-O,” “the
predicate equals leftover of axis-cover,” “the predicate equals
exist-opposite of `M`,” “the predicate equals the one-axis same-lock seed,”
“the predicate equals the two-axis opposite seed,” “the predicate equals
six-neighbor lock union,” “the predicate equals the two-tick lock-count
clock,” “the predicate equals mixed #7188 fail/fail,” “bits are
Admissibility,” “reverse fails at `τ1`,” “face fails at `τ1`,” “composition
fail,” or “`O` enlarges from `t+2` to `t+3`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each y-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+2` and
at `t+3`, reports simultaneous of the pair at each cut, lists new records
in `B_3(0)` at `t+2` and at `t+3` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that mixed `O(A,τ1)` remains a set,
that unique-letter simultaneous at mixed `O` is `UNDEFINED`, that `O` is
disjoint from `M`, that a formation member from already-recorded
six-neighbor locks is not attached, that `τ=t` is not scored, that new
six-neighbor records of `B` at `t+3` do not enter `O`, and that the display
is not leftover of axis-cover, leftover of `M` two-tick, leftover of
nm2ot3sly O freeze, leftover of nm2simt2sly simultaneous freeze t+1 versus
t+2, leftover of nm2simsly simultaneous at t+1, leftover of nm2slo timed-O,
or exist-opposite of `M`.
No runner cache is written.
