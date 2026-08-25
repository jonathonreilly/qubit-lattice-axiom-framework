---
claim_id: two_axis_same_lock_xprobe_own_incoming_set_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "M two-tick composition on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_own_incoming_set_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of Own Incoming Set Reverse And Face On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** own incoming set `M` at each probe's formation tick `t` versus
`t+1`, reverse/face as exist-opposite in `M` at each cut, and composition
HOLD iff `M(t)=M(t+1)` at `A,B,C,D`, on the four x-probes of the two-axis
same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2slpx.
Process: two disjoint same-lock pairs. Seed at tick 0: origin locks `+e_1`,
`(0,1,0)` locks `+e_1`, `(0,0,1)` locks `+e_2`, `(0,1,1)` locks `+e_2`.
Neither pair is opposite. The second pair is a new seed, not a formed
child. Perp-step, incoming lock.
Let `t(q)` be the formation tick of probe `q`. Let `τ0(q)=t(q)` and
`τ1(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick
`<= τ`. Seeds are a singleton seed letter. Mixed remains a set. Unformed
at `τ` is `UNDEFINED`. Reverse at a cut holds if and only if some lock in
`M(A,·)` is the vector opposite of some lock in `M(B,·)`. Face holds if
and only if some lock in `M(C,·)` is the vector opposite of some lock in
`M(D,·)`. Empty or `UNDEFINED` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Composition HOLD if and
only if `M(τ0)=M(τ1)` at `A`, at `B`, at `C`, and at `D`. Unique `L` is
not the object: report `M`. Occupancy of sites is not used. This is not
named-sign lettering. This is not a unique lock-vector leftover and not a
sum leftover. This is not leftover of unique-L. This is not leftover of
nm2slx axis-cover of `M` and `O`. This is not leftover of nm2ax12x 1-in
2-out split. This is not leftover of nm2slpx forall-perp. This is not
leftover of nm2simslx simultaneous. This is not leftover of nm2readslx
neighbor-read. This is not leftover of exist-opposite of `M` at `t+1`
only. This is not leftover of nmsimopp exist-opposite of `M` and of `O`
at `t+1`. This is not leftover of timed `O` exist-opposite. This is not
leftover of nm2t2sly same-lock y two-tick. This is not leftover of nm2t2x
opposite two-tick composition. This is not leftover of nm2t2slz same-lock
z two-tick. This is not leftover of nmt2opp `M` frozen at `t` as a
different seed. This is not leftover of mixed #7188 fail/fail. This is
not leftover of reverse/face-bit composition as a substitute for equality
of the four `M` sets. This is not leftover of the two-tick lock-count
clock composition. This is not leftover of a six-neighbor star.
Uniqueness of incoming locks is not required.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
This note does not write existential opposite into Admissibility and does
not attach a formation member from already-recorded six-neighbor locks.
The six-neighbor star is not the letter.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_own_incoming_set_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_own_incoming_set_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own incoming sets at the per-probe cuts `τ0=t` and `τ1=t+1`. Composition is
equality of those four own incoming sets across the two cuts. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique
lock-vector letter is a different readout and is not used as the object:
report `M`. A `Z^3` sum of those locks is a different readout and is not
used. The construction does not sum. Occupancy of sites is not used. A
six-neighbor star is not the letter. Reverse/face-bit equality is a
different readout and is not used as the composition object.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M(q,τ) as the probe's own incoming set of earliest NN steps at t and at t+1 on the four x-probes of the two-axis same-lock seed, mixed remains a set, reverse fail and face fail at each cut from no opposite pair in signed M, and composition HOLD because M(t)=M(t+1) at A,B,C,D; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_own_incoming_set_two_tick_composition_reverse_face
target_blocker_text: "display M at t versus t+1, reverse/face from exist-opposite in M at each cut, and composition HOLD iff M(t)=M(t+1) at A,B,C,D on the four x-probes of the two-axis same-lock seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep M two-tick composition displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not replace M by O, do not replace exist-opposite by axis-cover, do not replace exist-opposite by forall-perp, do not replace exist-opposite by simultaneous M and O, do not replace exist-opposite by neighbor-read, do not replace set equality by reverse/face-bit equality, do not identify the report with 1-axis same-lock mixed M, do not identify it with nm2t2x opposite two-tick, do not identify it with nm2t2sly same-lock y two-tick, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for two-tick composition of the own incoming set on the four x-probes of the two-axis same-lock seed; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose own
incoming sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and x-probes as nm2slpx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. The first
pair is `{0, (0,1,0)}` with same locks `L(0)=+e_1` and
`L(0,1,0)=+e_1`. The second pair is `{(0,0,1), (0,1,1)}` with same
locks `L(0,0,1)=+e_2` and `L(0,1,1)=+e_2`. Neither pair is opposite. The
second pair is a new seed, not a formed child of the first pair. This is
not nsopp leftover: on the one-axis seed those two sites form at tick 1
with incoming `+e_3`. This seed is not the perp two-site seed `+e_1/+e_2`.
This seed is not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`.
This seed is not the z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.
This seed is not the y-symmetric three-site seed that also records
`(0,-1,0)` at tick 0.

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

## Named two-tick composition of the own incoming set

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Mixed remains a set. Unique `L(q)` is not used
as the letter. Occupancy of sites is not used. Duplicate incoming steps
collapse in the set. The construction does not require `M(q,τ)` to be a
singleton. It does not sum `M(q,τ)`. It is not a unique lock-vector
leftover and not a sum leftover. It is not leftover of unique-L. It is
not leftover of nm2slx axis-cover of `M` and `O`. New records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors do not enter
earliest `M`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names.

Reverse and face at a cut (displayed):

```text
reverse  <=>  some a in M(A,τ) and some b in M(B,τ) with a+b=(0,0,0)
face     <=>  some c in M(C,τ) and some d in M(D,τ) with c+d=(0,0,0)
```

If `M(A,τ)` or `M(B,τ)` is empty or `UNDEFINED`, reverse is `UNDEFINED`.
Else reverse fails if no such pair exists. If `M(C,τ)` or `M(D,τ)` is empty
or `UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`. Either side
`UNDEFINED` is `UNDEFINED`.

Composition of `M` (displayed):

```text
composition HOLDs iff M(A,τ0)=M(A,τ1)
and M(B,τ0)=M(B,τ1)
and M(C,τ0)=M(C,τ1)
and M(D,τ0)=M(D,τ1).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
own incoming set changes from `t` to `t+1`, composition fails. Equality of
reverse/face bits is a different object: those bits may match while some
`M` set changes, and they may fail to match while the four `M` sets stay
equal. This letter is equality of the four `M` sets.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks and `M` at `τ0=t` and at `τ1=t+1`

On this process the four x-probes form. Own incoming sets at each probe's
`τ0=t` equal the own incoming sets at `τ1=t+1`. Earliest incoming is frozen.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ0) = {−e_3}
M(B, τ0) = {+e_1}
M(C, τ0) = {+e_1}
M(D, τ0) = {−e_3}
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set as a construction rule. On this
two-axis seed each of `M(A,τ0)`, `M(B,τ0)`, `M(C,τ0)`, and `M(D,τ0)` is a
singleton, and each equals the corresponding set at `τ1`. Unique-L leftover
would assign the same four letters. Here uniqueness is not required and
the object is still the set `M`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Those new neighbors enter later outgoing duals and do not enter earliest
`M`. Frozen `M` is the first display of two-tick composition on this
same-lock member: nm2simslx simultaneous HOLDs reverse and face from
nonempty disjoint `M` and `O` at `t+1`, nm2slpx forall-perp HOLDs reverse
and face from every integer dot `m·o=0`, and nm2readslx neighbor-read HOLDs
reverse and face. Those leftovers are different objects from equality of
the four incoming sets. nm2t2x already reported the same four `M` letters,
reverse fail, face fail, and composition HOLD on the two-axis opposite
seed. That leftover is a different seed.

Compare to 1-axis same-lock mixed M. Same x-probes, same perp-step incoming
lock, one same-lock pair `{0,(0,1,0)}` with `+e_1/+e_1` only. On that
1-axis seed the runner reports `t(A)=3`, `t(B)=2`, `t(C)=4`, `t(D)=3`,
mixed `M(A,τ)={+e_2, +e_3, −e_3}`, `M(B,τ)={+e_1}`, `M(C,τ)={+e_1}`, mixed
`M(D,τ)={−e_2, +e_3, −e_3}`, reverse fail, and face fail. The two-axis
seed advances `t(A)` from 3 to 2, `t(B)` from 2 to 1, `t(C)` from 4 to 3,
and `t(D)` from 3 to 2, replaces mixed `M(A,τ)` by `{−e_3}`, replaces
mixed `M(D,τ)` by `{−e_3}`, and keeps reverse FAIL and face fail.
Reverse FAIL uses a singleton `M(A,τ0)={−e_3}` against `{+e_1}`:
`−e_3+(+e_1)` is not zero. Face fail uses singleton `M(C,τ0)={+e_1}`
against `M(D,τ0)={−e_3}`: `+e_1+(−e_3)` is not zero.

On the same two-axis same-lock seed, nm2slx axis-cover of `M` and `O` fails
at `A` and at `D` because the unsigned union misses e_2, so cover reverse
FAIL and cover face FAIL. nm2ax12x 1-in 2-out split also fails reverse and
face from those cover fails, even though `|Axis(M)|=1` at each probe.
Signed own incoming `M` two-tick composition on those cover-FAIL x-probes
is this letter: the four `M` sets are frozen, reverse fails at both cuts,
and face fails at both cuts. Discriminator versus nm2slx is the object:
cover is unsigned leftover axis, this letter is equality of the four
incoming sets. Discriminator versus nm2t2x is the seed: opposite partner
letters `−e_1` and `−e_2` versus same-lock `+e_1/+e_1` and `+e_2/+e_2`.
Four `M` letters agree by accident of earliest incoming on these x-probes.
Discriminator versus nm2t2sly is the probe set: y-probe `A` is a seed with
`{+e_1}` at tick 0; this `A` is unformed until tick 2 with `{−e_3}`.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse holds if and only if there exist `a` in `M(A,τ)` and `b` in
`M(B,τ)` with `a+b=(0,0,0)`. At `τ0` both sets are nonempty:
`M(A,τ0)={−e_3}` and `M(B,τ0)={+e_1}`, so `−e_3+(+e_1)` is not zero.
Reverse fails. At `τ1` the same singletons remain, so reverse fails again.
Reverse FAIL uses a singleton `M(A,τ)`.

Reverse exist-opposite at τ0: fail
Reverse exist-opposite at τ1: fail

Both sides are defined, so this is not `UNDEFINED`. Unique-L leftover also
reports reverse fail from unique `L(A)=−e_3` and `L(B)=+e_1`. Axis-cover
reverse fails. 1-in 2-out split reverse fails. Timed `O` exist-opposite
reverse fails. Forall-perp reverse HOLDs. Simultaneous reverse HOLDs.
Neighbor-read reverse HOLDs. Same-lock y-probe signed-`M` reverse fails
from `{+e_1}` against `{+e_1}`. Opposite y-probe signed-`M` reverse HOLDs
from `{−e_1}` against `{+e_1}`. Opposite x-probe two-tick reverse fails
from the same four `M` letters on a different seed. Those leftovers are
not this display. Reverse fails because the pair from `M(A,τ)` and
`M(B,τ)` is not opposite.

Reverse fails at τ0.
Reverse fails at τ1.

Face holds if and only if there exist `c` in `M(C,τ)` and `d` in `M(D,τ)`
with `c+d=(0,0,0)`. At `τ0` both sets are nonempty: `M(C,τ0)={+e_1}` and
`M(D,τ0)={−e_3}`, so `+e_1+(−e_3)` is not zero. Face fails. At `τ1` the
same singletons remain, so face fails again.

Face exist-opposite at τ0: fail
Face exist-opposite at τ1: fail

This is not `hold` and not `UNDEFINED`. Face fails. Unique-L leftover also
reports face fail from unique `L(C)=+e_1` and `L(D)=−e_3`. Axis-cover face
fails, which agrees on the bit and is not this face fail: cover scores
unsigned leftover axis e_2 at `D`, while exist-opposite scores signed
`{+e_1}` against `{−e_3}`. 1-in 2-out split face fails. Timed `O`
exist-opposite face fails by accident of the outgoing letters
`O(C,τ)={−e_2,+e_3,−e_3}` against `O(D,τ)={+e_1}` and is not this
incoming-set report. Forall-perp face HOLDs. Simultaneous face HOLDs.
Neighbor-read face HOLDs. 1-axis same-lock mixed M face fails from mixed
`M(D,τ)` with no opposite of `+e_1`. Same-lock y-probe signed-`M` face
fails on a different probe set. Named-sign lettering lost the axis.
Signed-`M` exist-opposite does not HOLD reverse or face at either cut on
these same-lock x-probes: reverse fails and face fails at `t` and at
`t+1`. Transfer of nm2t2sly reverse fail / face fail copies the two-tick
composition object; it does not copy the y-probes. Transfer of nm2t2x
fail/fail copies those bits; it does not copy the opposite seed.

Face fails at τ0.
Face fails at τ1.

## Theorem 3 — composition of `M` at `t` versus `t+1`

Composition HOLD if and only if `M(t)=M(t+1)` at `A`, at `B`, at `C`, and
at `D`. Each of the four own incoming sets at `τ1` equals the same set at
`τ0`. None is `UNDEFINED`.

Composition of M at t versus t+1: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the four `M` sets, not equality of reverse/face bits: those
bits also match here (`fail`/`fail` at both cuts) by accident of frozen
singletons, and reverse/face-bit composition is a different object.
New six-neighbor records between `t` and `t+1` do not enter earliest `M`.

This is not leftover of exist-opposite of `M` at `t+1` only: that display
does not score `M` at `t`, does not score reverse/face at `t`, and does
not score two-tick set equality. This is not leftover of nmt2opp `M`
frozen at `t` as a different seed: nmt2opp uses the 1-axis y-probes. This
is not leftover of nm2slpx forall-perp HOLDING reverse and face. This is
not leftover of nm2simslx simultaneous HOLDING reverse and face. This is
not leftover of nm2readslx neighbor-read HOLDING reverse and face. This
is not leftover of nm2slx cover FAIL/FAIL. This is not leftover of nm2t2x
opposite two-tick composition. This is not leftover of nm2t2sly same-lock
y two-tick. This is not leftover of mixed #7188 fail/fail.

Composition HOLDs.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set to be a singleton.
- It does not sum the own incoming set.
- It does not use occupancy of sites as the letter.
- It does not replace `M` by `O`.
- It does not replace exist-opposite of signed `M` by axis-cover of `M` and
  `O`.
- It does not replace exist-opposite of signed `M` by forall-perp of `M`
  versus `O`.
- It does not replace exist-opposite of signed `M` by simultaneous nonempty
  disjoint `M` and `O`.
- It does not replace composition of the four `M` sets by reverse/face-bit
  equality.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not reprint 1-axis same-lock mixed M reverse fail and face fail as
  this member.
- It does not reprint nm2t2sly y-probe signed-`M` reverse fail and face fail.
- It does not reprint nm2slx axis-cover reverse fail and face fail.
- It does not reprint nm2ax12x 1-in 2-out reverse fail and face fail.
- It does not reprint nm2slpx forall-perp reverse hold and face hold.
- It does not reprint nm2simslx simultaneous reverse hold and face hold.
- It does not reprint nm2readslx neighbor-read reverse hold and face hold.
- It does not reprint exist-opposite of `M` at `t+1` only.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint timed `O` exist-opposite as this incoming-set report.
- It does not reprint nm2t2x opposite two-tick composition as this seed.
- It does not reprint nm2t2slz z-probe two-tick composition as this letter.
- It does not reprint nmt2opp `M` frozen at `t` as this two-axis seed.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint the two-tick lock-count clock composition.
- It does not treat the second pair as a formed child of nsopp leftover.
- It does not score the y-probes or the z-probes as this letter.
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
two-axis same-lock-pair process, the own incoming sets at `t` and at `t+1`,
the existential-opposite reverse/face predicates at each cut, and
composition as equality of those four sets are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ0=t` and at `τ1=t+1` | Theorem 1; frozen equal |
| reverse FAIL uses a singleton `M(A,τ)` | Theorem 1; yes; `{−e_3}` |
| reverse from exist-opposite of `M` at `τ0` and `τ1` | Theorem 2; `fail`, `fail` |
| face from exist-opposite of `M` at `τ0` and `τ1` | Theorem 2; `fail`, `fail` |
| composition of `M` at `t` versus `t+1` | Theorem 3; `HOLD` |
| comparison to 1-axis same-lock mixed M | Theorem 1; mixed `M(A)` and `M(D)` at later ticks |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of nm2slx axis-cover | not this display |
| leftover of nm2ax12x 1-in 2-out split | not this display |
| leftover of nm2slpx forall-perp | not this display |
| leftover of nm2simslx simultaneous | not this display |
| leftover of nm2readslx neighbor-read | not this display |
| leftover of `t+1`-only exist-opposite | not this display |
| leftover of timed `O` exist-opposite | not this display |
| leftover of nmsimopp exist-opposite of `M` and of `O` | not this display |
| leftover of nm2t2sly same-lock y two-tick | not this display |
| leftover of nm2t2x opposite two-tick | not this display |
| leftover of nm2t2slz same-lock z two-tick | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of reverse/face-bit composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of two-tick lock-count clock | not this display |
| second pair as formed child | refused; new seed |
| y-probe or z-probe signed-`M` on this seed | not this letter |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `M` at `t` versus `t+1` on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition or `UNDEFINED`. |
| V2 | Current main has no landed own-incoming-set two-tick composition reverse/face report on these four x-probes of this two-axis same-lock seed. |
| V3 | Own incoming sets at two cuts, the four reverse/face bits, and composition as set equality are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set at `t` and at `t+1` and scores set equality together with existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not sum the lock set, does not replace `M` by `O`, does
not replace exist-opposite by axis-cover, does not replace exist-opposite
by forall-perp, does not replace exist-opposite by simultaneous `M` and
`O`, does not replace set equality by reverse/face-bit equality, does not
identify this display with 1-axis same-lock mixed M, does not identify it
with nm2t2x opposite two-tick, does not identify it with nm2t2sly same-lock
y two-tick, does not identify it with nm2slx axis-cover, does not identify
it with nm2slpx forall-perp, does not identify it with nm2simslx
simultaneous, does not identify it with nm2readslx neighbor-read, and does
not identify it with timed `O` exist-opposite. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique-L leftover | require a singleton `{v}` else `UNDEFINED` | on this seed `M` is already singleton at each probe, so unique-L reverse fail and face fail agree by accident; the object is still the set `M`; 1-axis mixed `M(A)` makes unique-L `UNDEFINED` | ATTEMPTED |
| 1-axis same-lock mixed M | reuse reverse fail and face fail of own incoming `M` on these x-probes | 1-axis `M(A,τ)` is mixed `{+e_2,+e_3,−e_3}` at tick 3; two-axis `M(A,τ)` is `{−e_3}` at tick 2 | ATTEMPTED |
| nm2slx axis-cover | score reverse/face from complementary unsigned axes of `M` and `O` | cover reverse fail and face fail agree on bits because union misses e_2 at `A` and at `D`; cover uses `O` and leftover axis, not signed `M` set equality | ATTEMPTED |
| nm2ax12x 1-in 2-out | score reverse/face from cover with `\|Axis(M)\|=1` | split reverse fail and face fail from cover fail at `A` and at `D`; `|Axis(M)|` is already 1 | ATTEMPTED |
| nm2slpx forall-perp | score reverse/face from every `m·o=0` | forall-perp reverse HOLD and face HOLD; this letter reverse fail and face fail | ATTEMPTED |
| nm2simslx simultaneous | score reverse/face from nonempty disjoint `M` and `O` | simultaneous reverse HOLD and face HOLD; this letter reverse fail and face fail | ATTEMPTED |
| nm2readslx neighbor-read | HOLD reverse/face iff some formed 6-NN recovers `M` | neighbor-read reverse HOLD and face HOLD; this letter reverse fail and face fail | ATTEMPTED |
| `t+1` only | score exist-opposite of `M` at `t+1` without `t` | that leftover does not report `M` at `t` and does not score two-tick set equality | ATTEMPTED |
| timed `O` exist-opposite | score reverse/face inside `O(A,τ)` and `O(B,τ)` | timed `O` reverse fails from `{+e_1}` against `{+e_2,+e_3,−e_3}` while `O` is not `M` | ATTEMPTED |
| nm2t2sly same-lock y two-tick | reuse y-probe reverse fail face fail composition HOLD | y-probe `A` is a seed with `{+e_1}` at tick 0; this letter is the four x-probes with `A` unformed until tick 2 and `M={−e_3}` | ATTEMPTED |
| nm2t2x opposite two-tick | reuse hold/fail composition HOLD of opposite partner letters | same ticks and four `M` letters by accident; opposite seed uses `−e_1` and `−e_2`; this seed is same-lock `+e_1/+e_1` and `+e_2/+e_2` | ATTEMPTED |
| nmsimopp exist-opposite of `M` and of `O` | require both `M` and `O` exist-opposite | this display scores only own incoming `M` at two cuts | ATTEMPTED |
| nm2t2slz z-probe two-tick | reuse z-probe frozen `M` reverse fail face fail composition HOLD | z-probe `A` is a seed with `{+e_2}` at tick 0; this letter is the four x-probes with `A` unformed until tick 2 | ATTEMPTED |
| nmt2opp `M` frozen at `t` | reuse 1-axis y-probe two-tick `M` | different seed and different probes | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | the scored object is equality of the four `M` sets; bit match is an accident of frozen singletons | ATTEMPTED |
| sum of the same incoming sets | replace `M` by the `Z^3` sum | the construction does not sum; sum of a singleton agrees by accident and is not the letter | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover at `A` includes origin partner `+e_1`; own incoming `M(A,τ)` is `{−e_3}` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; z-symmetric on these x-probes reports mixed `M(A)={+e_2,−e_2}` | ATTEMPTED |
| two-tick lock-count clock | replace `M` by a count of locks | counts are not lock sets and are not this letter | ATTEMPTED |
| nsopp leftover child | treat `(0,0,1)` and `(0,1,1)` as formed children | they are tick-0 seeds with `+e_2/+e_2`, not tick-1 children with incoming `+e_3` | ATTEMPTED |
| z-probe signed-`M` | score the four z-probes on this seed | z-probe `M(A,τ)={+e_2}` at tick 0; this letter is the four x-probes with unformed `A` until tick 2 | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of signed-`M`
exist-opposite with axis-cover, missing identification with forall-perp,
missing identification with simultaneous `M` and `O`, missing
identification with neighbor-read, missing identification with 1-axis
same-lock mixed M, missing identification with nm2t2x opposite two-tick,
missing identification with nm2t2sly same-lock y two-tick, missing
identification of set equality with reverse/face-bit equality, and missing
Record identification of exist-opposite reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-axis same-lock seed locks `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
from records with tick `<= τ`, per-probe `τ0=t` and `τ1=t+1`, mixed remains
a set, existential opposite, composition as equality of the four `M` sets,
four x-probes with unformed `A` until tick 2, second pair is a new seed,
neither pair is opposite, and reverse/face as existence of a pair that
sums to zero are declared. No uniqueness of incoming locks, no six-neighbor
lock union as the scored object, no occupancy of sites as the letter, no
named-sign reduction, no singleton leftover as the object, no sum leftover,
no unique-L leftover, no axis-cover leftover, no forall-perp leftover, no
simultaneous leftover, no neighbor-read leftover, no nm2t2x leftover, no
nm2t2sly leftover, no timed-`O` leftover, no reverse/face-bit leftover as
the composition object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
exist-opposite reverse-fail and face-fail reports, and composition HOLD of
frozen `M`, do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets at two cuts, reverse/face at each cut, and composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Signed-`M` two-tick composition should be refused as leftover
because nm2t2x already reported reverse fail and face fail at `t` and at
`t+1` with composition HOLD and the same four `M` letters; nm2slx already
fails reverse and face from cover; nm2ax12x already fails reverse and face
from 1-in 2-out; timed `O` already fails both bits; unique-L already gives
the same four letters; `M` is frozen by construction of earliest incoming,
so composition HOLD is tautological; reverse/face bits already match, so
bit composition is enough; forall-perp already HOLDs reverse and face;
simultaneous already HOLDs reverse and face; neighbor-read already HOLDs
reverse and face; nm2t2sly already answered same-lock two-tick; 1-axis
same-lock mixed M already answered these x-probes with fail/fail; and empty
`M` should be `UNDEFINED` like unformed.

**Answer:** nm2t2x uses opposite partner letters `−e_1` and `−e_2`. This
letter uses same-lock `+e_1/+e_1` and `+e_2/+e_2`. The four `M` letters
agree by accident of earliest incoming on these x-probes. Those leftover
bits agree, so the discriminator is the seed, not a reprint of the
opposite process. nm2slx scores unsigned leftover axis of `M` and `O` at
`t+1` only. This letter scores `M` at `t` and at `t+1`, reverse/face at
each cut, and composition as equality of the four sets. Cover FAIL and
1-in 2-out FAIL are unsigned complementary occupation of `{e_1,e_2,e_3}`
at one probe. Exist-opposite is a signed pair across two probes. They
agree on the bits here by accident of leftover e_2 at `A` and at `D`
versus `{−e_3}` against `{+e_1}`; they are not the same object because
cover uses `O` and misses e_2 while exist-opposite never reads `O`.
Unique-L agrees because this seed happens to have singleton `M` at each
of `A,B,C,D`; mixed remains a set as the construction, and uniqueness is
not required. Frozen earliest incoming is exactly the two-tick fact being
displayed on this same-lock member: new six-neighbor records between `t`
and `t+1` exist and do not enter `M`. Reverse/face-bit equality is a
different object: it would HOLD even if some `M` changed while the
exist-opposite bits stayed `fail`. Forall-perp reverse HOLDs and face
HOLDs from every integer dot zero; this letter reverse fails and face
fails. Simultaneous reverse HOLDs and face HOLDs from nonempty disjoint
`M` and `O`; this letter does not score `O`. Neighbor-read reverse HOLDs
and face HOLDs from a recovered neighbor copy of `M`; this letter does
not score neighbor copies. nm2t2sly uses the four y-probes with seed `A`
and `M(A,τ)={+e_1}`; this letter uses the four x-probes with unformed `A`
until tick 2 and `M(A,τ)={−e_3}`. 1-axis same-lock mixed M has mixed
`M(A,τ)={+e_2,+e_3,−e_3}` at tick 3; two-axis `M(A,τ)` is `{−e_3}` at
tick 2. Empty `M` is `UNDEFINED` on a comparison side; unformed at `τ` is
`UNDEFINED`. Reverse exist-opposite fails at both cuts. Face fails at
both cuts. Composition of `M` HOLDs.

### N8 — cross-cycle echo

1-axis same-lock mixed M reported reverse fail and face fail from own
incoming `M` on these same x-probes with mixed `M(A)` and mixed `M(D)` at
later ticks. nm2t2sly reported same-lock y-probe reverse fail, face fail,
and composition HOLD. nm2t2x reported opposite x-probe reverse fail, face
fail, and composition HOLD with the same four `M` letters. nm2slx reported
axis-cover reverse fail and face fail on these x-probes. nm2ax12x reported
1-in 2-out reverse fail and face fail. nm2slpx reported forall-perp reverse
hold and face hold. nm2simslx reported simultaneous reverse hold and face
hold. nm2readslx reported neighbor-read reverse hold and face hold. This
note is not those displays: it reports two-tick composition of signed own
incoming `M` on the four x-probes of the two-axis same-lock seed, reverse
fail at `t` and at `t+1`, face fail at `t` and at `t+1`, and composition
HOLD because `M(t)=M(t+1)` at `A,B,C,D`. Discriminator versus 1-axis
same-lock mixed M is singleton `{−e_3}` at `A` and at `D` versus mixed
three-sets, together with the advanced ticks. Discriminator versus HOLDING
forall-perp, HOLDING simultaneous, and HOLDING neighbor-read is both
exist-opposite bits. Discriminator versus FAILING cover and FAILING split
is the object: signed `M` set equality, not unsigned leftover axis.
Discriminator versus nm2t2x is the same-lock seed. Discriminator versus
nm2t2sly is the four x-probes with unformed `A` until tick 2.

**Gate disposition:** PASS for the own-incoming-set two-tick composition
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals the sum of the lock set,” “the predicate equals
axis-cover,” “the predicate equals 1-in 2-out split,” “the predicate equals
forall-perp,” “the predicate equals simultaneous `M` and `O`,” “the
predicate equals neighbor-read,” “the predicate equals timed `O`
exist-opposite,” “the predicate equals 1-axis same-lock mixed M,” “the
predicate equals nm2t2x opposite two-tick,” “the predicate equals nm2t2sly
same-lock y two-tick,” “composition equals reverse/face-bit equality,”
“bits are Admissibility,” “reverse exist-opposite holds,” or “face
exist-opposite holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set from the record prefix at that probe's `t` and at `t+1`, scores reverse
and face by existential opposite at each cut, scores composition as
equality of the four `M` sets, lists new records in `B_3(0)` between `t`
and `t+1` that meet a probe's six-neighbors, compares the same observables
on the 1-axis same-lock mixed M seed and on the two-axis opposite seed, and
checks Theorems 1--3. It also checks that reverse fails and face fails at
both cuts, that composition HOLDs, that mixed remains a set, that unique-L
leftover is a different object even when letters agree, that nm2slx
axis-cover leftover fails both bits from leftover e_2, that nm2ax12x 1-in
2-out leftover fails both bits, that nm2slpx forall-perp leftover HOLDs
both bits, that nm2simslx simultaneous leftover HOLDs both bits, that
nm2readslx neighbor-read leftover HOLDs both bits, that timed `O`
exist-opposite is not the scored object, that reverse/face-bit composition
is not the scored object, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the second pair is a new seed, that the display is not 1-axis
same-lock mixed M, not nm2t2x opposite two-tick, and not nm2t2sly same-lock
y two-tick. No runner cache is written.
