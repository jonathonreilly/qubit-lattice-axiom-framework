---
claim_id: two_axis_same_lock_xprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "O at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Own Outgoing Set Freeze At t+1 Versus t+2 Reverse And Face On Four Two-Axis Same-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** own outgoing set `O` at each probe's `τ1=t+1` versus `τ2=t+2`,
reverse/face from exist-opposite in `O` at each cut, and composition of
those four sets, on the four x-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2slpx. Process: two
disjoint same-lock pairs. Seed at tick 0: origin locks `+e_1`, `(0,1,0)`
locks `+e_1`, `(0,0,1)` locks `+e_2`, `(0,1,1)` locks `+e_2`. Neither pair
is opposite. The second pair is a new seed, not a formed child. Perp-step,
incoming lock. Let `t(q)` be the formation tick of probe `q`. Let
`τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T. Do not score
`τ=t`. `M(r,τ)` is the set of earliest incoming nearest-neighbor steps at
`r` using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Reverse
holds if and only if some lock in `O(A,τ)` is the vector opposite of some
lock in `O(B,τ)`. Face holds if and only if some lock in `O(C,τ)` is the
vector opposite of some lock in `O(D,τ)`. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`; nonempty with no opposite pair fails.
Composition HOLDs if and only if `O(τ1)=O(τ2)` at `A`, `B`, `C`, and `D`.
This is the transfer of O freeze onto same-lock x-probes. This is not
leftover of two-axis opposite O freeze. This is not leftover of nmot2
`O` at `t` versus `t+1`. This is not leftover of nmt2 `M` two-tick. This is
not leftover of nmout eventual-`O`. This is not leftover of axis-cover.
This is not leftover of M exist-opposite. This is not leftover of unique-L.
This is not leftover of y-probe O exist-opposite. This is not leftover of
z-probe O exist-opposite. This is not leftover of forall-perp reverse/face
on these x-probes. Uniqueness is not required. Mixed remains a set.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
This note does not write existential opposite into Admissibility and does
not attach a formation member from already-recorded six-neighbor locks.
This display does not use occupancy. Mixed remains a set. Unique `L` is not
the object. The six-neighbor star is not the letter. Occupancy of sites is
not used. This is not named-sign lettering. This is not a unique lock-vector
leftover and not a sum leftover. O is not M. The construction does not sum.
It does not use a six-neighbor star. It is not leftover of unique-L. It is
not the two-tick lock-count clock composition.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Reverse and face are scored on existence of an
opposite pair in the own outgoing sets at each cut. Composition is equality
of those four own outgoing sets. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock-vector letter is a different
readout and is not used as the object: report `O`. A `Z^3` sum of those
locks is a different readout and is not used. The construction does not
sum. Occupancy of sites is not used. A six-neighbor star is not the letter.
O is not M. The own outgoing set is the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of O(q, tau) as the probe's own outgoing dual of M at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, mixed remains a set, reverse fail and face fail from existential opposite at each cut, and composition HOLD; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display O at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not identify the sets with unique-L leftover, do not identify the sets with axis-cover FAIL/FAIL, do not identify the sets with M exist-opposite, do not identify the sets with two-axis opposite O freeze, do not identify the bits with forall-perp HOLD/HOLD, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for O at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
outgoing sets at `τ1=t+1` and `τ2=t+2` are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed child
of the first pair, and neither pair is opposite. This seed is not the 1-axis
same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone. This seed is
not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is
not the y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.
This seed is not the z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named own outgoing set at `τ1=t+1` versus `τ2=t+2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.
Do not score τ=t.

`M(r,τ)` is the set of earliest incoming nearest-neighbor steps at `r`
using only records with tick `<= τ`. If `r` is unformed at `τ`, then
`M(r,τ)` is `UNDEFINED`. If `r` is a seed and `τ >= 0`, then `M(r,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `O` to be a singleton. It does not sum the set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Reverse holds if and only if there exist `a` in `O(A,τ)` and `b` in
`O(B,τ)` with `a+b=(0,0,0)`. Face holds if and only if there exist `c` in
`O(C,τ)` and `d` in `O(D,τ)` with `c+d=(0,0,0)`. Either side `UNDEFINED`
or empty is `UNDEFINED`. Else if some pair is opposite, HOLD. Else fail.

Composition of `O` (displayed):

```text
composition HOLDs iff O(A,τ1)=O(A,τ2)
and O(B,τ1)=O(B,τ2)
and O(C,τ1)=O(C,τ2)
and O(D,τ1)=O(D,τ2).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
own outgoing set changes from `t+1` to `t+2`, composition fails. Equality
of reverse/face bits is a different object. This letter is equality of the
four `O` sets.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail or
axis-cover with this reverse/face is refused: axis-cover fails at `A` and
at `D` because the unsigned union misses `e_2`, while it HOLDs at `B` and
at `C`; signed `O` reverse fails and face fails at both cuts. Identifying
two-axis opposite O freeze with this letter is refused: opposite `O(D)`
is `{+e_1, −e_1}` while this member has `O(D)={+e_1}`. Identifying nmot2
`O` at `t` versus `t+1` is refused: at `t`, `O` is empty at all four
x-probes, so reverse and face are `UNDEFINED`. Identifying nmt2 `M`
two-tick is refused: O is not M. Identifying nmout eventual-`O` is
refused: eventual `O` has no `t+1` versus `t+2` cut. Identifying unique-L
leftover is refused: mixed `O(B)` and mixed `O(C)` remain sets, and
unique-L reverse and face are `UNDEFINED` while exist-opposite reverse
fails and face fails. Identifying forall-perp reverse/face is refused:
forall-perp HOLDs at `A`,`B`,`C`,`D` while exist-opposite reverse fails
and face fails.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks and `O` at `τ1=t+1` and at `τ2=t+2`

On this process the four x-probes form. Own outgoing sets at each probe's
`τ1=t+1` equal the own outgoing sets at `τ2=t+2`. Outgoing dual is frozen
from `t+1` to `t+2`.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1}
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ1)` has three outgoing
steps and `O(C,τ1)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at those mixed outgoing sets and would leave reverse and face
`UNDEFINED`. Here uniqueness is not required. At every scored x-probe,
`O` is empty at `t`. Do not score `τ=t`. That leftover of nmot2 has reverse
`UNDEFINED`, face `UNDEFINED`, and composition fail from `t` to `t+1`.
This letter starts at `τ1=t+1`. O is not M: `M(A,τ1)={−e_3}` while
`O(A,τ1)={+e_1}`.

New records in `B_3(0)` that meet a probe's six-neighbors:

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

No new six-neighbor of any scored x-probe forms at `t+2`. Frozen `O` from
`t+1` to `t+2` is the first display of that freeze on this same-lock
x-probe member.

Compare to two-axis opposite O freeze: same x-probes, same perp-step, but
opposite partner letters. Opposite `O(D,τ1)={+e_1, −e_1}` includes `−e_1`.
This member has `O(D)={+e_1}` and still freezes from `t+1` to `t+2`.
Reverse fail and face fail agree by accident of the shared letters at
`A`,`B`,`C`. The set at `D` is not equal.

Compare to 1-axis same-lock. Same x-probes, same perp-step incoming lock,
one same-lock pair `{0,(0,1,0)}` with `+e_1/+e_1` only. On that 1-axis
seed the runner reports `t(A)=3`, `t(B)=2`, `t(C)=4`, `t(D)=3`,
`O(A,τ1)={+e_1}`, reverse fail, and face fail. Here `t(A)=2` and
`M(A)={−e_3}` is not the mixed 1-axis incoming `{+e_2,+e_3,−e_3}`.
Axis-cover on that 1-axis leftover HOLDs at all four x-probes. Here cover
fails at `A` and at `D`.

On the same two-axis same-lock seed, nm2slpx forall-perp of `M` versus `O`
HOLDs at `A`,`B`,`C`,`D`, so forall-perp reverse HOLDs and face HOLDs.
Exist-opposite of signed `O` reverse fails and face fails. Those leftovers
are not this freeze letter.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse holds if and only if there exist `a` in `O(A,τ)` and `b` in
`O(B,τ)` with `a+b=(0,0,0)`. At `τ1` both sets are nonempty:
`O(A,τ1)={+e_1}` and `O(B,τ1)={+e_2, +e_3, −e_3}`, so no pair sums to
zero. Reverse fails. At `τ2` the same sets remain, so reverse fails again.
Reverse fails at `τ1` and at `τ2`.

Reverse at τ1: fail
Reverse at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Unique-L leftover
reports reverse `UNDEFINED` from mixed `O(B)`. Axis-cover reverse fails by
the site split at `A`. Forall-perp reverse HOLDs. Y-probe O exist-opposite
reverse HOLDs on a different probe set. Z-probe O exist-opposite reverse
HOLDs on a different probe set. Those leftovers are not this display.
Reverse fails because the pair from `O(A,τ)` and `O(B,τ)` includes no
opposite.

Reverse fails at τ1 and at τ2.

Face holds if and only if there exist `c` in `O(C,τ)` and `d` in `O(D,τ)`
with `c+d=(0,0,0)`. At `τ1` both sets are nonempty:
`O(C,τ1)={−e_2, +e_3, −e_3}` and `O(D,τ1)={+e_1}`, so no pair sums to
zero. Face fails. At `τ2` the same mixed sets remain, so face fails
again. Face fails at `τ1` and at `τ2`.

Face at τ1: fail
Face at τ2: fail

This is not `hold` and not `UNDEFINED`. Face fails. Unique-L leftover
reports face `UNDEFINED` from mixed `O(C)`. Axis-cover face fails from
cover fail at `D`. Forall-perp face HOLDs. Y-probe O exist-opposite face
HOLDs. Z-probe O exist-opposite face fails on a different probe set and a
different `O(C)`. Named-sign lettering lost the axis.

Face fails at τ1 and at τ2.

## Theorem 3 — composition of `O` at `t+1` versus `t+2`

Composition HOLD if and only if `O(t+1)=O(t+2)` at `A`, at `B`, at `C`, and
at `D`. Each of the four own outgoing sets at `τ2` equals the same set at
`τ1`. None is `UNDEFINED`.

Composition of O: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the four `O` sets, not equality of reverse/face bits: those
bits also match here (`fail`/`fail` at both cuts) by accident of frozen
sets, and reverse/face-bit composition is a different object.
No new six-neighbor records between `t+1` and `t+2` enter `O`.

This is not leftover of two-axis opposite O freeze: that leftover has
`−e_1` in `O(D)`. This is not leftover of nmot2 `O` at `t` versus `t+1`:
empty `O` at `t` is not `O` at `t+1`, so that leftover composition fails.
This is not leftover of nmt2 `M` two-tick. This is not leftover of nmout
eventual-`O`. This is not leftover of axis-cover. This is not leftover of
forall-perp HOLD/HOLD. This is not leftover of mixed #7188 fail/fail.

Composition HOLDs.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own outgoing set to be a singleton.
- It does not sum the own outgoing set.
- It does not use occupancy of sites as the letter.
- It does not replace `O` by `M`.
- It does not replace exist-opposite of signed `O` by axis-cover of `M` and
  `O`.
- It does not replace composition of the four `O` sets by reverse/face-bit
  equality.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not reprint two-axis opposite O freeze as this member.
- It does not reprint nmot2 `O` at `t` versus `t+1`.
- It does not reprint nmt2 `M` two-tick.
- It does not reprint nmout eventual-`O`.
- It does not reprint nm2slpx forall-perp reverse hold and face hold.
- It does not reprint 1-axis same-lock reverse fail and face fail as this
  member.
- It does not reprint y-probe O exist-opposite reverse hold and face hold.
- It does not reprint z-probe O exist-opposite reverse hold and face fail.
- It does not reprint M exist-opposite reverse fail and face fail as this
  member.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not treat the second same-lock pair as a formed child of the first.
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
two-axis same-lock four-site process, the own outgoing sets at `t+1` and at
`t+2`, the existential-opposite reverse/face predicates at each cut, and
composition as equality of those four sets are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `O` at `τ1=t+1` and at `τ2=t+2` | Theorem 1; frozen equal; `O(A)={+e_1}` |
| reverse from exist-opposite of `O` at `τ1` and `τ2` | Theorem 2; `fail`, `fail` |
| face from exist-opposite of `O` at `τ1` and `τ2` | Theorem 2; `fail`, `fail` |
| composition of `O` at `t+1` versus `t+2` | Theorem 3; `HOLD` |
| comparison to two-axis opposite O freeze | Theorem 1; opposite `O(D)` includes `−e_1` |
| comparison to 1-axis same-lock | Theorem 1; 1-axis `t(A)=3` and mixed `M(A)` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of axis-cover | not this display |
| leftover of M exist-opposite | not this display |
| leftover of two-axis opposite O freeze | not this display |
| leftover of nmot2 `O` at `t` versus `t+1` | not this display |
| leftover of nmt2 `M` two-tick | not this display |
| leftover of nmout eventual-`O` | not this display |
| leftover of y-probe O exist-opposite | not this display |
| leftover of z-probe O exist-opposite | not this display |
| leftover of forall-perp reverse/face | not this display |
| leftover of reverse/face-bit composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of two-tick lock-count clock | not this display |
| second pair as formed child | refused; new seed |
| y-probe or z-probe `O` on this seed | not this letter |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `O` at `t+1` versus `t+2` on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition or `UNDEFINED`. |
| V2 | Current main has no landed own-outgoing-set freeze `t+1` versus `t+2` reverse/face report on these four x-probes of this two-axis same-lock seed. |
| V3 | Own outgoing sets at two cuts, the four reverse/face bits, and composition as set equality are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own outgoing set at `t+1` and at `t+2` and scores set equality together with existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not sum the lock set, does not replace `O` by `M`, does
not replace exist-opposite by axis-cover, does not replace set equality by
reverse/face-bit equality, does not identify this display with two-axis
opposite O freeze, does not identify it with nmot2 `O` at `t` versus
`t+1`, and does not identify it with forall-perp reverse hold and face
hold. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique-L leftover | require a singleton `{v}` else `UNDEFINED` | mixed `O(B,τ)` and mixed `O(C,τ)` have three steps; unique-L reverse and face are `UNDEFINED` while exist-opposite reverse fails and face fails | ATTEMPTED |
| two-axis opposite O freeze | reuse opposite seed `+e_1/−e_1` and `+e_2/−e_2` | opposite `O(D)` includes `−e_1`; this member has `O(D)={+e_1}` | ATTEMPTED |
| nmot2 `O` at `t` versus `t+1` | score freeze from formation tick | `O` empty at all four x-probes at `t`, reverse `UNDEFINED`, composition fail; this letter starts at `t+1` | ATTEMPTED |
| nmt2 `M` two-tick | score equality of incoming sets | M exist-opposite reverse fail and face fail; O is not M; `M(A)={−e_3}` is not `O(A)` | ATTEMPTED |
| nmout eventual-`O` | score neighbor locks with no tick cut | eventual `O` has no `t+1` versus `t+2` report | ATTEMPTED |
| axis-cover | score reverse/face from complementary unsigned axes of `M` and `O` | cover fails at `A` and at `D` and HOLDs at `B` and at `C`; signed `O` reverse fails and face fails | ATTEMPTED |
| M exist-opposite | reuse signed reverse and face of `M` | `M` reverse fail and face fail coincide as bits; the sets are not `O` | ATTEMPTED |
| 1-axis same-lock | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis `t(A)=3` and mixed `M(A)`; here `t(A)=2` and `M(A)={−e_3}` | ATTEMPTED |
| y-probe O exist-opposite | score the four y-probes on this seed | y-probe reverse HOLDs and face HOLDs; this letter is the four x-probes | ATTEMPTED |
| z-probe O | score the four z-probes on this seed | z-probe reverse HOLDs and face fails; this letter is the four x-probes | ATTEMPTED |
| forall-perp reverse/face | score every `m·o=0` at t+1 | forall-perp reverse HOLDs and face HOLDs; exist-opposite reverse fails and face fails | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | the scored object is equality of the four `O` sets; bit match is an accident of frozen sets | ATTEMPTED |
| sum of the same outgoing sets | replace `O` by the `Z^3` sum | the construction does not sum; sum of mixed `O(B)` is `+e_2`, not an opposite of `O(A)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover union at `A` is `{+e_1,−e_3}`; own outgoing at `A` is `{+e_1}` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed reverse-fail face-fail | different process; z-symmetric on these x-probes reports reverse fail and face hold | ATTEMPTED |
| two-tick lock-count clock | replace `O` by a count of locks | counts are not lock sets and are not this letter | ATTEMPTED |
| nsopp leftover child | treat `(0,0,1)` and `(0,1,1)` as formed children | they are tick-0 seeds with `+e_2/+e_2`, not tick-1 children | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of signed-`O`
exist-opposite with axis-cover, missing identification with two-axis
opposite O freeze, missing identification with nmot2 `O` at `t` versus
`t+1`, missing identification with 1-axis same-lock ticks, missing
identification of set equality with reverse/face-bit equality, and missing
Record identification of exist-opposite reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed locks `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own outgoing dual
from records with tick `<= τ`, per-probe `τ1=t+1` and `τ2=t+2`, mixed
remains a set, existential opposite, composition as equality of the four
`O` sets, four x-probes with non-seed `A`, second pair is a new seed, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no six-neighbor lock union as the scored
object, no occupancy of sites as the letter, no named-sign reduction, no
singleton leftover as the object, no sum leftover, no unique-L leftover,
no axis-cover leftover, no nmot2 leftover as the scored cut, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
exist-opposite reverse-fail and face-fail reports, and composition HOLD of
frozen `O`, do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in the probe's own outgoing set `O(q, tau)` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four outgoing sets at t+1 and t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Same-lock x-probe O freeze should be refused as leftover
because two-axis opposite O freeze already reported reverse fail, face
fail, and composition HOLD on these x-probes; nm2slpx already displayed
forall-perp HOLD/HOLD at `t+1`; axis-cover already answered three-axis
occupation; unique-L already fails at mixed `B`; `O` is frozen by
construction of earliest incoming of neighbors, so composition HOLD is
tautological; reverse/face bits already match, so bit composition is
enough; 1-axis same-lock already reports the same `O` letters; nmot2
already scored `O` across two ticks; M exist-opposite already fails both
bits; and empty `O` should be `UNDEFINED` like unformed.

**Answer:** Opposite O freeze includes `−e_1` at `D`. This member has
`O(D)={+e_1}`. nm2slpx scores forall-perp of `M` versus `O` at `t+1` only:
forall-perp reverse HOLDs and face HOLDs. This letter scores exist-opposite
of `O` at `t+1` and at `t+2` plus set equality. Those bits disagree with
forall-perp. Unique-L reverse is `UNDEFINED` at mixed `O(B)` while
exist-opposite reverse fails. Frozen earliest incoming of neighbors is
exactly the two-tick fact being displayed: no new six-neighbor of any
scored x-probe forms at `t+2`, and `O` is unchanged. Reverse/face-bit
equality is a different object: it would HOLD even if some `O` changed
while the exist-opposite bits stayed `fail`/`fail`. 1-axis same-lock has
`t(A)=3` and mixed `M(A)`; this member has `t(A)=2` and `M(A)={−e_3}`.
nmot2 scores `O` at `t` versus `t+1`, where reverse is `UNDEFINED` and
composition fails. Empty `O` is empty, not `UNDEFINED`; unformed at `τ` is
`UNDEFINED`. Reverse fails at `τ1` and at `τ2`. Face fails at `τ1` and at
`τ2`. Composition of `O` HOLDs.

### N8 — cross-cycle echo

nm2slpx reported forall-perp reverse hold and face hold on these same-lock
x-probes at `t+1`. Two-axis opposite O freeze reported reverse fail, face
fail, and composition HOLD with `O(D)` including `−e_1`. 1-axis same-lock
reported reverse fail and face fail with `t(A)=3`. Two-axis same-lock
y-probes report reverse hold and face hold. Two-axis same-lock z-probes
report reverse hold and face fail. This note is not those displays: it
reports `O` at `t+1` versus `t+2` on two disjoint same-lock pairs with
x-probes, mixed `O(B)` and mixed `O(C)`, reverse fail at both cuts, face
fail at both cuts, and composition HOLD because `O(t+1)=O(t+2)` at
`A,B,C,D`. Discriminator versus opposite O freeze is the missing `−e_1`
at `D`. Discriminator versus forall-perp is both exist-opposite bits.
Discriminator versus 1-axis is `t(A)` and `M(A)`. Discriminator versus
y-probes is reverse fail. Discriminator versus z-probes is reverse fail.

**Gate disposition:** PASS for the own-outgoing-set freeze `t+1` versus
`t+2` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals the sum of the lock set,” “the predicate
equals axis-cover,” “the predicate equals M exist-opposite,” “the
predicate equals two-axis opposite O freeze,” “the predicate equals nmot2
`O` at `t` versus `t+1`,” “the predicate equals 1-axis same-lock,”
“the predicate equals forall-perp,” “composition equals reverse/face-bit
equality,” “bits are Admissibility,” “reverse exist-opposite holds,” or
“face exist-opposite holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each x-probe's own outgoing dual
from the record prefix at that probe's `t+1` and at `t+2`, scores reverse
and face by existential opposite at each cut, scores composition as
equality of the four `O` sets, lists new records in `B_3(0)` between `t`
and `t+1` and between `t+1` and `t+2` that meet a probe's six-neighbors,
compares the same observables on the 1-axis same-lock seed and on the
two-axis opposite seed, and checks Theorems 1--3. It also checks that
reverse fails and face fails at both cuts, that composition HOLDs, that
mixed remains a set, that unique-L leftover is `UNDEFINED` at mixed
`O(B)`, that axis-cover leftover fails at `A` and at `D`, that two-axis
opposite O freeze includes `−e_1` at `D`, that nmot2 leftover at `t` is
`UNDEFINED` reverse, that the construction does not sum, that a formation
member from already-recorded six-neighbor locks is not attached, that the
second pair is a new seed, and that the display is not 1-axis same-lock
and not y-probe O exist-opposite. No runner cache is written.
