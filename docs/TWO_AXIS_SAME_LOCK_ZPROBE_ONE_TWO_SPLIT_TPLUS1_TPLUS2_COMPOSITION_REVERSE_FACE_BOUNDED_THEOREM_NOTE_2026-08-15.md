---
claim_id: two_axis_same_lock_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# One-In Two-Out Axis Split At t+1 Versus t+2 Reverse Face And Composition On Four Z-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M` and
outgoing dual `O` at each probe's `τ1=t+1` versus `τ2=t+2`, reverse/face from
that split at each cut, and composition HOLD iff split at `τ1` equals split
at `τ2` at `A,B,C,D`, on the four z-probes of the two-axis same-lock seed
in `B_3(0)={n:n·n<=9}`. Same process and z-probes as nm2slz. `M`, `O`, and
split as nm2sl12z. Process: two disjoint same-lock pairs. Seed at tick 0:
origin locks `+e_1`, `(0,1,0)` locks `+e_1`, `(0,0,1)` locks `+e_2`,
`(0,1,1)` locks `+e_2`. Neither pair is opposite. The second pair is a new
seed, not a formed child. Perp-step, incoming lock. Let `t(q)` be the
formation tick of probe `q`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is
no global T. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`.
Empty O fails split. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail.
Split HOLDs at `q` if and only if cover HOLDs and `|Axis(M)|=1` (hence
`|Axis(O)|=2`). 2-in 1-out is fail of this object, not UNDEFINED. Reverse
HOLDs if and only if split HOLDs at `A` and at `B`. Face HOLDs if and only
if split HOLDs at `C` and at `D`. Composition HOLD if and only if split at
`τ1` equals split at `τ2` at `A`, at `B`, at `C`, and at `D`. This is not
leftover of nm2sl12z `t+1`-only split reverse fail and face hold. This is
not leftover of nm2splt2slz split at `t` versus `t+1`. This is not leftover
of nm2t2slz frozen-`M` composition HOLD. This is not leftover of
reverse/face-bit composition. This is not leftover of nmcover axis-cover.
This is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover-empty fail of leftover axis.
This is not leftover of the 1-axis opposite two-site seed. This is not
leftover of mixed #7188 fail/fail. Uniqueness is not required. Mixed
remains a set. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed lock.
Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and
`Axis(O)`. Split is cover together with `|Axis(M)|=1`. Reverse and face are
scored on split HOLD at the paired probes at each cut. Composition is
equality of the four split reports across the two cuts. Named signs `{+,−}`
are a coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. Frozen `M` two-tick
equality is a different readout and is not used as the composition object.
Reverse/face-bit equality is a different readout and is not used as the
composition object. Existential opposite of signed locks is a different
readout and is not used as the split reverse. Axis-cover without the
one-axis incoming cardinality is a different readout and is not used.
Leftover-empty fail of unsigned leftover axis sets is a different readout
and is not used. A `Z^3` sum of those locks is a different readout and is
not used. Occupancy of sites is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, split fail at A and hold at B,C,D at both cuts so the four split reports freeze, reverse fail at both cuts, face hold at both cuts, and composition HOLD because split at t+1 equals split at t+2 at A,B,C,D; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_one_two_split_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition HOLD iff split at t+1 equals split at t+2 at A,B,C,D"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out split at t+1 versus t+2 displayed; do not write split into Admissibility, do not replace split composition by frozen-M equality, do not replace split composition by reverse/face-bit equality, do not reduce to nm2sl12z t+1-only reverse fail face hold, do not reduce to nm2splt2slz t versus t+1 composition fail, do not replace split by leftover-empty fail, do not replace split by existential opposite of signed locks, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
`D=(1,1,0)`. `A` is a seed of the second same-lock pair. Same process and
z-probes as nm2slz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. The first
pair is `{0, (0,1,0)}` with same locks `L(0)=+e_1` and
`L(0,1,0)=+e_1`. The second pair is `{(0,0,1), (0,1,1)}` with same
locks `L(0,0,1)=+e_2` and `L(0,1,1)=+e_2`. Neither pair is opposite. The
second pair is a new seed, not a formed child of the first pair. This is
not leftover of the 1-axis opposite two-site seed: on that seed those two
sites form at tick 1 with incoming `+e_3`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the two-axis opposite seed
`+e_1/−e_1` and `+e_2/−e_2`. This seed is not the z-symmetric three-site
seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site
seed that also records `(0,-1,0)` at tick 0.

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

## Named 1-in 2-out split at `τ1=t+1` versus `τ2=t+2`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.

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
axis. Empty `O` makes `Axis(O)` empty, so cover fails.

Split at a probe at the same cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

Empty O fails split. 2-in 1-out is fail of this object, not UNDEFINED:
cover HOLD with `|Axis(M)|=2` (hence `|Axis(O)|=1`) is split fail. Cover
without the one-axis incoming cardinality is not this object.

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`. Face
1-in 2-out holds if and only if split HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

Composition of split (displayed):

```text
composition HOLDs iff split(A,τ1)=split(A,τ2)
and split(B,τ1)=split(B,τ2)
and split(C,τ1)=split(C,τ2)
and split(D,τ1)=split(D,τ2).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
split report changes from `t+1` to `t+2`, composition fails. Equality of the
four `M` sets is a different object. Equality of the four `O` sets is a
different object. Equality of reverse/face bits is a different object:
reverse may match while a probe's split still changes. This letter is
equality of the four split reports.

Admissibility is not edited. Split is not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks, `M`, `O`, and split at `τ1=t+1` and at `τ2=t+2`

On this process the four z-probes form. Own incoming sets at each probe's
`τ1=t+1` equal the own incoming sets at `τ2=t+2`. Earliest incoming is frozen.
Outgoing duals at these two cuts are equal as sets on all four z-probes.
That set-equality is computed, not adopted as the composition object. Split
fails at `A` from axis overlap of seed letter `+e_2` with outgoing `+e_2`.
Split HOLDs at `B`, `C`, and `D`. The four split reports freeze from `t+1`
to `t+2`.

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
O(A, τ1) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, −e_2}
O(D, τ1) = {−e_2, +e_3, −e_3}
O(A, τ2) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, −e_2}
O(D, τ2) = {−e_2, +e_3, −e_3}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = hold
split(A, τ2) = fail
split(B, τ2) = hold
split(C, τ2) = hold
split(D, τ2) = hold
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`, so it is an
outgoing neighbor of `A` already at formation. Mixed remains a set:
`O(A,τ1)` has four outgoing steps and `O(D,τ1)` has three outgoing steps.
Unique letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is
not required.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O`. Site `(0,1,1)` is a seed, so it is not a new 6-NN
of `A`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
```

Between `t+1` and `t+2` a new 6-NN of `A` forms and does not enter `O`.
`B`, `C`, and `D` have no new 6-NN at `t+2`:

```text
new 6-NN of A at t(A)+2: (0, -1, 1)
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

Site `(0,-1,1)` forms at tick 2 with earliest incoming `{+e_3}`. The step
from `A` to that site is `−e_2`, which is not in that incoming set, so
`(0,-1,1)` does not enter O. Freeze of `O` on these two cuts is not the
claim that no new six-neighbor record exists.

Investment nm2sl12z already reported split reverse fail and face HOLD at
`t+1` on this member. That leftover does not score split at `t+2` and does
not score composition. Investment nm2splt2slz already reported split at `t`
versus `t+1`: empty `O` at `t` fails split at `B,C,D`, face fails then HOLDs,
and composition fails. That leftover does not score `t+2`. Investment
nm2t2slz already reported frozen `M` composition HOLD on this member. That
leftover does not score `O` or split. This is the first display of split at
`t+1` versus `t+2` on this member.

Compare to the 1-axis opposite two-site seed: that member forms `A` at tick
1 as a child locking `+e_3`, forms `B` at tick 2, forms `C` at tick 4 with
mixed 2-in 1-out `M`, and forms `D` at tick 2. At `t+1` and at `t+2` split
HOLDs at `A` and `B`, fails at `C` from 2-in 1-out, and HOLDs at `D`, so
reverse HOLDs and face fails, and that composition also HOLDs. Here
`t(A)=0` and split HOLDs at `C` at both cuts.

Compare to the two-axis opposite seed: at `t+1` and at `t+2` split HOLDs at
`A`, `B`, `C`, and `D`, so reverse HOLDs and face HOLDs, and that
composition HOLDs. Same-lock reverse stays fail because `A` never becomes
1-in 2-out. Opposite reverse HOLDs. Both seeds freeze composition from
`t+1` to `t+2`. Discriminator versus opposite is reverse.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`. At
`τ1` split fails at `A` and HOLDs at `B`. Reverse fails. At `τ2` the same
pair of reports. Reverse fails again.

Reverse 1-in 2-out at τ1: fail
Reverse 1-in 2-out at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse also
fails at both cuts on this member because cover matches split here. That
agreement is an accident of this seed: on the 1-axis opposite two-site
seed, cover HOLDs at `C` while split fails from 2-in 1-out. Leftover-empty
reverse fails at both cuts. Exist-opposite reverse of signed `M` fails.
Exist-opposite reverse of signed `O` at `t+1` HOLDs. Those leftovers are
not this reverse. Reverse fails because `A` is not 1-in 2-out at either
cut.

Reverse fails at τ1.
Reverse fails at τ2.

Face 1-in 2-out holds if and only if split HOLDs at `C` and at `D`. At `τ1`
both splits HOLD. Face HOLDs. At `τ2` both splits HOLD. Face HOLDs. Reverse
fails and face HOLDs at `t+1`: that is the nm2sl12z leftover, now placed
next to the same bits at `t+2`. nm2splt2slz had face fail then HOLD because
Empty O at t fails split; those cuts are not this letter.

Face 1-in 2-out at τ1: hold
Face 1-in 2-out at τ2: hold

This is not `UNDEFINED`. Leftover-empty face fails at both cuts because
leftover of the union is empty at `C` and at `D`, while split face HOLDs.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed `O`
fails. Cover face matches split face on this member at both cuts and
remains a different predicate. The four y-probes of this same seed give
split reverse hold and split face fail at `t+1` and at `t+2`. The four
x-probes give split reverse fail and split face fail at both cuts. Those
probe-direction readouts are not this z-probe display.

Face HOLDs at τ1.
Face HOLDs at τ2.

## Theorem 3 — composition of split at `t+1` versus `t+2`

Composition HOLD if and only if split at `τ1` equals split at `τ2` at `A`,
at `B`, at `C`, and at `D`. Split at `A` is `fail` at both cuts. Split at
`B`, at `C`, and at `D` is `hold` at both cuts. None is `UNDEFINED`. The
four split reports freeze.

Composition of split at t+1 versus t+2: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the four split reports, not equality of the four `M` sets and
not equality of the four `O` sets: those set equalities happen here, and
nm2splt2slz already showed they can disagree with split equality, because
`M` was frozen from `t` to `t+1` while split at `B`, `C`, and `D` changed.
Reverse/face-bit composition also HOLDs here because reverse stays fail
and face stays hold, but that leftover would HOLD on a member whose
reverse and face bits matched while some probe's split still changed: if
`A` stays fail, `B` changes hold to fail, and `C,D` stay hold, reverse
stays fail and face stays hold while split composition fails. This letter
is equality of the four split reports.

This is not leftover of nm2sl12z `t+1`-only split: that display does not
score split at `t+2` and does not score composition. This is not leftover
of nm2splt2slz `t` versus `t+1`: that composition fails. This is not
leftover of nm2ax12z opposite split reverse hold and face hold at `t+1`.
This is not leftover of mixed #7188 fail/fail.

Composition HOLDs.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require split sides to be singletons.
- It does not sum either set.
- It does not replace split composition by frozen-`M` equality.
- It does not replace split composition by frozen-`O` equality.
- It does not replace split composition by reverse/face-bit equality.
- It does not replace split by leftover-empty fail.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by existential opposite of signed locks.
- It does not replace split by axis-cover without `|Axis(M)|=1`.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2sl12z `t+1`-only reverse fail and face hold as this
  two-cut display.
- It does not reprint nm2splt2slz `t` versus `t+1` composition fail as this
  freeze.
- It does not reprint nm2t2slz frozen-`M` composition HOLD as this split
  composition.
- It does not reprint nm2ax12z opposite reverse hold and face hold.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint the two-tick lock-count clock composition. This is
  not the two-tick lock-count clock composition.
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
two-axis same-lock seed process, 1-in 2-out axis split of `M` and `O` at `t+1`
versus `t+2`, reverse/face from that split at each cut, and composition of
those four split reports are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ1=t+1` and at `τ2=t+2` | Theorem 1; frozen equal |
| `O` at `τ1=t+1` and at `τ2=t+2` | Theorem 1; equal as sets; new 6-NN of `A` at `t+2` does not enter `O` |
| split at `τ1` and at `τ2` | Theorem 1; fail, hold, hold, hold at both cuts |
| reverse from 1-in 2-out at `τ1` and `τ2` | Theorem 2; `fail`, `fail` |
| face from 1-in 2-out at `τ1` and `τ2` | Theorem 2; `hold`, `hold` |
| composition of split at `t+1` versus `t+2` | Theorem 3; `HOLD` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of frozen-`M` composition | not this display |
| leftover of frozen-`O` composition | not this display |
| leftover of reverse/face-bit composition | not this display |
| leftover-empty fail of leftover axis | not this split display |
| leftover of exist-opposite HOLD | not this split display |
| leftover of nmcover axis-cover | not this split display |
| leftover of nm2sl12z `t+1`-only split | not this two-cut display |
| leftover of nm2splt2slz `t` versus `t+1` | not this freeze |
| leftover of nm2t2slz frozen-`M` composition | not this split composition |
| leftover of nm2ax12z opposite split HOLD | not this display |
| y-probe or x-probe split on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out split at `t+1` versus `t+2` on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition. |
| V2 | Current main has no landed 1-in 2-out `t+1` versus `t+2` composition reverse/face report on these four z-probes of this two-axis same-lock seed. |
| V3 | Split reports at two cuts, the four reverse/face bits, and composition as split equality are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out split of own incoming and own outgoing at `t+1` and at `t+2` and scores equality of those four split reports. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split composition by frozen-`M` equality,
does not replace split composition by reverse/face-bit equality, does not
reduce them to nm2sl12z `t+1`-only reverse fail face hold, does not reduce
them to nm2splt2slz `t` versus `t+1` composition fail, does not replace
split by leftover-empty fail, does not replace split by leftover of `M`
alone or leftover of `O` alone, does not replace split by existential
opposite of signed locks, does not replace split by nmcover axis-cover, and
does not identify this display with the 1-axis opposite two-site seed. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2sl12z `t+1` only | reuse reverse fail and face hold at `t+1` | that leftover does not score split at `t+2` and does not score composition | ATTEMPTED |
| nm2splt2slz `t` vs `t+1` | reuse composition fail from empty `O` at `t` | that leftover scores `t` versus `t+1`; here `O` is already nonempty and split freezes, so composition HOLDs | ATTEMPTED |
| nm2t2slz frozen `M` | HOLD iff `M(t)=M(t+1)` | `M` is frozen at every pair of cuts; split composition failed from `t` to `t+1` and HOLDs from `t+1` to `t+2` | ATTEMPTED |
| frozen `O` composition | HOLD iff `O(t+1)=O(t+2)` | `O` happens to be equal here; a new 6-NN of `A` at `t+2` does not enter `O`; the scored object is split equality | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | bits match here; they would still match if `B` changed hold to fail while `A` stayed fail and face stayed hold, and split composition would fail | ATTEMPTED |
| nmcover axis-cover | score reverse/face as cover HOLD | on the 1-axis opposite two-site seed cover HOLDs at `C` while split fails from 2-in 1-out; cover without `|Axis(M)|=1` is not this object | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at `t+1` and at `t+2`, leftover face fails, while split face HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` is frozen with `M` and does not see outgoing duals | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `t+1` at `C` is `{e_3}` and at `D` is `{e_1}`, nonempty unequal, while split face HOLDs | ATTEMPTED |
| exist-opposite | reuse signed reverse and face of `M` or of `O` | exist-opposite face of signed `M` fails while split face HOLDs; exist-opposite reverse of signed `O` HOLDs while split reverse fails | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ1)` remains a set; unique-letter `O` at mixed `A` is `UNDEFINED` while split fails | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, split fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| two-axis opposite split | reuse reverse hold and face hold | opposite `A` is 1-in 2-out at `t+1` and at `t+2`; same-lock `A` never is; reverse stays fail | ATTEMPTED |
| y-probe split | score the four y-probes on this seed | y-probe reverse HOLDs and face fails at both cuts; this letter is the four z-probes | ATTEMPTED |
| x-probe split | score the four x-probes on this seed | x-probe reverse fails and face fails at both cuts; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores 1-in 2-out of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports face hold at both cuts | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is cover plus `|Axis(M)|=1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split composition with
frozen-`M` equality, missing identification of split composition with
reverse/face-bit equality, missing identification of split with leftover of
`M` alone, missing identification of split with leftover-empty fail,
missing identification of split with existential opposite of signed locks,
missing identification of this display with nm2sl12z `t+1`-only split,
missing identification of this display with nm2splt2slz `t` versus `t+1`,
and missing Record identification of split reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1` and
`τ2=t+2`, empty `O` fails split, unsigned axis, cover as complementary
occupation of `{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, 2-in 1-out
as fail not `UNDEFINED`, composition as equality of the four split reports,
four z-probes with seed `A`, second pair as a new seed not a formed child,
and mixed remains a set are declared. No uniqueness of incoming locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
frozen-`M` leftover as the composition object, no reverse/face-bit leftover
as the composition object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold`/`fail` reports at two cuts, and composition HOLD, do not close
that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split reports at two cuts, reverse/face at each cut, and composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Split `t+1` versus `t+2` composition should be refused as
leftover because nm2sl12z already reported reverse fail and face hold at
`t+1`; nm2splt2slz already scored two cuts; nm2t2slz already HOLDs
composition because `M` is frozen; `O` is equal as sets so frozen-`O`
already answers freeze; cover reverse and cover face already match split
reverse and split face on this seed; leftover of `M` alone already answers
reverse; composition of reverse/face bits already HOLDs because neither
bit changes; opposite two-axis split already freezes composition from
`t+1` to `t+2`; and `A` overlapping `e_2` is only axis-cover fail.

**Answer:** nm2sl12z scores one cut. nm2splt2slz scores `t` versus `t+1`,
where empty `O` fails split and composition fails. This letter scores
`t+1` versus `t+2` after `O` is nonempty. Frozen `M` composition HOLDs at
every pair of cuts and is a different object: it HOLDs from `t` to `t+1`
while split composition fails there. Frozen `O` composition HOLDs here by
accident of these two cuts; a new 6-NN of `A` at `t+2` exists and does not
enter `O`, and the scored object remains split equality. Cover matches
split on this member at both cuts by accident of `|Axis(M)|=1` wherever
cover HOLDs; on the 1-axis opposite two-site seed, cover HOLDs at `C` and
split fails from 2-in 1-out. Leftover of `M` alone is frozen with `M` and
cannot see outgoing duals. Reverse/face-bit composition HOLDs here because
neither bit changes, but it would still HOLD if `B` changed while `A`
stayed fail and face stayed hold. Opposite two-axis split also freezes
composition, yet opposite reverse HOLDs because `A` is 1-in 2-out;
same-lock reverse stays fail. Cover fail at `A` is the reason split fails
at `A`; split still requires `|Axis(M)|=1` in addition to cover.
Composition of split HOLDs.

### N8 — cross-cycle echo

nm2sl12z reported 1-in 2-out reverse fail and face hold at `t+1` on these
same-lock z-probes. nm2splt2slz reported split fail at every probe at `t`,
split fail at `A` and hold at `B,C,D` at `t+1`, reverse fail at both cuts,
face fail then hold, and composition fail. nm2t2slz reported frozen-`M`
reverse fail, face fail, and composition HOLD on the same seed. nm2ax12z
reported 1-in 2-out reverse hold and face hold at `t+1` on the opposite
seed. The 1-axis opposite two-site seed reported split reverse hold and
split face fail at `t+1` from 2-in 1-out at `C`. The four y-probes of this
same seed reported split reverse hold and split face fail at `t+1`. This
note is not those displays: it reports 1-in 2-out axis split of `M` and
`O` at `t+1` versus `t+2` on the four z-probes of the two-axis same-lock
seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and `t(D)=1`, split fail at `A`
and hold at `B,C,D` at both cuts, reverse fail at both cuts, face hold at
both cuts, and composition HOLD because split at `t+1` equals split at
`t+2` at `A`, `B`, `C`, and `D`. Discriminator versus nm2sl12z is the
`t+2` cut and composition. Discriminator versus nm2splt2slz is composition
HOLD versus composition fail. Discriminator versus opposite is reverse
fail at both cuts.

**Gate disposition:** PASS for the 1-in 2-out `t+1` versus `t+2`
reverse/face and composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the predicate
equals exist-opposite HOLD,” “the predicate equals nmcover axis-cover
HOLD,” “the predicate equals nm2sl12z `t+1`-only split,” “the predicate
equals nm2splt2slz `t` versus `t+1`,” “the predicate equals nm2t2slz
frozen-`M` composition HOLD,” “composition equals reverse/face-bit
equality,” “bits are Admissibility,” “2-in 1-out is UNDEFINED,”
“composition fails,” “face 1-in 2-out fails at τ1,” or “split at t+1 does
not equal split at t+2.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
at `t+2`, reports the 1-in 2-out split at each cut, lists new records in
`B_3(0)` at `t+1` and at `t+2` that meet a probe's six-neighbors, scores
reverse and face from split at each cut, scores composition as equality of
the four split reports, and checks Theorems 1--3. It also checks that
reverse fails at both cuts, that face HOLDs at both cuts, that composition
HOLDs, that `t` versus `t+1` composition fails as a leftover, that
frozen-`M` composition HOLDs as a leftover, that reverse/face-bit
composition is not the scored object, that 2-in 1-out is fail not
`UNDEFINED`, that the 1-axis opposite two-site seed is a different member
with split face fail at `C`, that the two-axis opposite seed HOLDs reverse
at `t+1` and at `t+2`, that leftover-empty fail is a different reverse and
face, that mixed sets remain sets, that the construction does not sum, that
a formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, that the
y-probes and x-probes of this seed are not this letter, and that the
display is not the two-tick lock-count clock composition. No runner cache
is written.
