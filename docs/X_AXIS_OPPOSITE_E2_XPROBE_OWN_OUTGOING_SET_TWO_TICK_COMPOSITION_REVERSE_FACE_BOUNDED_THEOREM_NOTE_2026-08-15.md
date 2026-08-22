---
claim_id: x_axis_opposite_e2_xprobe_own_outgoing_set_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from O at t versus t+1 on the four #7214 x-probes, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_axis_opposite_e2_xprobe_own_outgoing_set_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of Own-Outgoing Reverse And Face On Four #7214 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from each probe's own outgoing dual `O` of the
earliest incoming nearest-neighbor step set `M` at that probe's formation
tick `t` versus `t+1`, on the four nmxe2x #7214 x-probes in
`B_3(0)={n:n·n<=9}`, no global T. Same process and x-probes as nmxe2x
#7214. Let `t(q)` be the formation tick of probe `q`. Let `τ0(q)=t(q)` and
`τ1(q)=t(q)+1`. `M(r,τ)` is the set of earliest incoming nearest-neighbor
steps at `r` using only records with tick `<= τ`. Seeds are a singleton
seed letter. Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual
of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in
`B_3(0)` and `e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty
`O` is empty, not `UNDEFINED`. O is not M. O is not a six-neighbor star.
Reverse at a cut holds if and only if `A` and `B` are formed by that cut
and some `a` in `O(A,·)` and some `b` in `O(B,·)` have `a+b=(0,0,0)`. Face
likewise on `C,D`. Empty or `UNDEFINED` on either side is `UNDEFINED`.
Composition HOLD if and only if the `t+1` reverse/face bits equal the `t`
bits. This is not leftover of nmt2x2 `M` two-tick HOLD/HOLD. This is not
leftover of nmoutx2 eventual-`O` hold/hold. This is not leftover of unique
own-outgoing letters. This is not leftover of mixed #7188 fail/fail. This
is not leftover of nmot2opp y-probe delayed `O`. This is not the two-tick
lock-count clock composition. Uniqueness of outgoing locks is not required.
Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_axis_opposite_e2_xprobe_own_outgoing_set_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/x_axis_opposite_e2_xprobe_own_outgoing_set_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut.
Reverse and face are scored on existence of an opposite pair in each probe's
own outgoing set at that probe's `t` and at `t+1`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. A `Z^3` sum of those locks
is a different readout and is not used. Occupancy `n` is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own outgoing duals O at each of the four #7214 x-probes at t and at t+1, with reverse UNDEFINED then hold, face UNDEFINED then hold, and composition fail because t+1 bits do not equal t bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_axis_opposite_e2_xprobe_own_outgoing_set_two_tick_composition_reverse_face
target_blocker_text: "display reverse and face from own outgoing sets at t versus t+1 on the four #7214 x-probes, no global T, and whether those bits compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to a unique outgoing letter, do not replace O by M, do not replace O by six-neighbor lock union, do not replace O by a lock-count clock, do not identify the bits with nmt2x2 M HOLD/HOLD, do not identify the bits with nmoutx2 eventual-O hold/hold, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for two-tick composition of own-outgoing reverse/face on the four #7214 x-probes, no global T; displayed, not adopted"
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
outgoing sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. `A` is a seed. Same process and x-probes as
nmxe2x #7214.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_2` and `L(1,0,0)=−e_2`. This seed is not the
same-lock two-site seed `+e_2/+e_2`. This seed is not the nspar two-site
seed `+e_1/−e_1`. This seed is not the x-axis opposite ±e_3 two-site seed
`+e_3/−e_3`.

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

## Named outgoing set `O` at `t` and at `t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

`M(r,τ)` is the set of earliest incoming nearest-neighbor steps at `r`
using only records with tick `<= τ`. If `r` is unformed at `τ`, then
`M(r,τ)` is `UNDEFINED`. If `r` is a seed and `τ >= 0`, then `M(r,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed in B_3(0) and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate outgoing steps collapse in the set. The
construction does not require `O(q,τ)` to be a singleton. It does not sum
`O(q,τ)`. It does not replace `O` by `M`. It does not replace `O` by locks
of six-neighbors of `q`. It does not wait for a global later T. Occupancy
`n` is not used. O is not M.

Reverse at a cut holds if and only if `A` and `B` are formed by that cut
and some `a` in `O(A,·)` and some `b` in `O(B,·)` have `a+b=(0,0,0)`. Face
at a cut holds if and only if `C` and `D` are formed by that cut and some
`c` in `O(C,·)` and some `d` in `O(D,·)` have `c+d=(0,0,0)`. Empty or
`UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with
no opposite pair fails.

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Else composition fails. Displayed, not
adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `O`.

## Theorem 1 — ticks and `O` at `τ0` and at `τ1`

On this process the four x-probes form. Compare to M two-tick of nmt2x2:
that leftover reports `M(q,τ1)=M(q,τ0)` at every scored probe. The own
outgoing duals at each probe's `t` are not equal to the own outgoing duals
at `t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
O(A, τ0) = {}
O(B, τ0) = {}
O(C, τ0) = {}
O(D, τ0) = {−e_2}
O(A, τ1) = {+e_1, +e_3, −e_3}
O(B, τ1) = {+e_1, +e_3, −e_3}
O(C, τ1) = {+e_2, −e_2, +e_3, −e_3}
O(D, τ1) = {+e_2, −e_2}
```

`A` is a seed at tick 0. Empty `O` at `τ0` for `A`, `B`, and `C` is empty,
not `UNDEFINED`: those probes are formed, and no neighbor `q+e` yet carries
`e` in `M(q+e,τ0)`. Mixed remains a set: `O(A,τ1)` has three outgoing steps
`+e_1`, `+e_3`, and `−e_3`. Unique own-outgoing letters would assign
`UNDEFINED` at `A`, `B`, and `C` at `τ1`. Here uniqueness is not required.
`O(D,τ0)` is the singleton `{−e_2}` because seed `A` already carries seed
letter `−e_2` along the step from `D` to `A`. That dual is not a child of
`D`.

New records in `B_3(0)` between `τ0` and `τ1` that meet a probe's
six-neighbors are exactly the sites that enlarge `O`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)
new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (1, 2, 0)
```

Those new neighbors enter `O(q,τ1)` because each locks the step from the
probe as earliest incoming. Therefore `O(q,τ1)` is strictly larger than
`O(q,τ0)` at every scored probe.

Compare O to M of nmt2x2 / nmxe2x #7214. Same process reports

```text
M(A, τ0) = {−e_2}
M(B, τ0) = {+e_2}
M(C, τ0) = {+e_1}
M(D, τ0) = {−e_1, +e_3, −e_3}
```

with `M(q,τ1)=M(q,τ0)` at each probe. `M` and `O` are disjoint at each of
the four probes at both cuts. Reverse HOLD of #7214 uses `−e_2` in `M(A)`
against `+e_2` in `M(B)`. Those incoming letters are absent from `O(A,τ1)`
and `O(B,τ1)`. Reverse HOLD of #7214 does not use an incoming letter that
is also outgoing. O is not M. No six-neighbor star.

This is not leftover of nmt2x2 `M` two-tick: that leftover freezes earliest
incoming at formation, so `M(τ1)=M(τ0)`. This is not leftover of nmoutx2
eventual-`O`: that leftover reads `M` of neighbors without a `t` versus
`t+1` cut and reports the `τ1` sets already at formation. This is not
leftover of unique own-outgoing letters.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse holds if and only if some `a` in `O(A,·)` and some `b` in `O(B,·)`
have `a+b=(0,0,0)`. At `τ0` both sets are empty, so reverse is `UNDEFINED`.
At `τ1` the sets are `{+e_1, +e_3, −e_3}` and `{+e_1, +e_3, −e_3}`. The pair
`+e_3+(−e_3)` sums to zero. Reverse holds.

Reverse at τ0: UNDEFINED
Reverse at τ1: hold

Face holds if and only if some `c` in `O(C,·)` and some `d` in `O(D,·)` have
`c+d=(0,0,0)`. At `τ0` the sets are `{}` and `{−e_2}`. Empty on the `C` side
makes face `UNDEFINED`. At `τ1` the sets are `{+e_2, −e_2, +e_3, −e_3}` and
`{+e_2, −e_2}`. The pair `+e_2+(−e_2)` sums to zero. Face holds.

Face at τ0: UNDEFINED
Face at τ1: hold

Unique own-outgoing letters on these x-probes report reverse `UNDEFINED` and
face `UNDEFINED` from mixed `O` at `τ1`. nmt2x2 `M` two-tick leftover
reports reverse hold and face hold at both cuts. nmoutx2 eventual-`O`
leftover reports reverse hold and face hold from the `τ1` sets with no
empty `τ0` cut. Those are different objects. Reverse is `UNDEFINED` at `τ0`
because `O(A,τ0)` and `O(B,τ0)` are empty. Reverse holds at `τ1` because a
pair from `O(A,τ1)` and `O(B,τ1)` is opposite.

## Theorem 3 — composition

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Reverse is `UNDEFINED` at `τ0` and `hold`
at `τ1`. Face is `UNDEFINED` at `τ0` and `hold` at `τ1`. The bits do not
match.

Composition: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. The `t+1` reverse/face
bits are not a function of the `t` stack on this process: new six-neighbor
records between the cuts enter the outgoing dual.

This is not leftover of nmt2x2 `M` two-tick HOLD/HOLD: that leftover
reports reverse hold and face hold at both cuts with composition HOLD
because earliest incoming is frozen at formation. This is not leftover of
nmoutx2 eventual-`O` hold/hold. This is not leftover of unique
own-outgoing letters (reverse `UNDEFINED`, face `UNDEFINED`). This is not
the two-tick lock-count clock composition. This is not leftover of mixed
#7188 fail/fail: that mixed display reported reverse fail and face fail
with composition HOLD. This is not leftover of nmot2opp y-probe delayed
`O`: that leftover used y-probes and seed `+e_1/−e_1`.

## What this note does not claim

- It does not select a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the outgoing set to be a singleton.
- It does not sum the outgoing set.
- It does not replace `O` by `M`.
- It does not replace `O` by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-outgoing lock-vector letters on these
  x-probes as the object.
- It does not reprint nmt2x2 `M` two-tick HOLD/HOLD.
- It does not reprint nmoutx2 eventual-`O` hold/hold.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint nmot2opp y-probe delayed `O` as this member.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
x-axis opposite ±e_2 two-site process, the own outgoing sets at `t` and at
`t+1`, and the reverse/face/composition bits are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; x-axis opposite ±e_2 seed `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `O` at `τ0` and at `τ1` | Theorem 1; empty or singleton at `τ0`; enlarged at `τ1` |
| compare O to M two-tick of nmt2x2 | Theorem 1; disjoint; O is not M; M frozen, O not frozen |
| reverse and face at `τ0` and at `τ1` | Theorem 2; `UNDEFINED` / `hold` at reverse; `UNDEFINED` / `hold` at face |
| composition | Theorem 3; fail because bits do not match |
| unique outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nmt2x2 `M` two-tick HOLD/HOLD | not this display |
| leftover of nmoutx2 eventual-`O` hold/hold | not this display |
| leftover of unique own-outgoing letters | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of nmot2opp y-probe delayed `O` | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `O` at `t` versus `t+1` on the four #7214 x-probes, reverse/face, and whether those bits compose. |
| V2 | Current main has no landed two-tick own-outgoing-set reverse/face composition on these four #7214 x-probes. |
| V3 | Own outgoing sets at two cuts and the `UNDEFINED`/`hold`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own outgoing dual at two cuts and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing letter, does not replace `O` by `M`, does not replace `O`
by six-neighbor lock union, does not identify this display with the
two-tick lock-count clock, does not identify the bits with nmt2x2
`M` HOLD/HOLD, and does not identify the bits with mixed #7188 fail/fail.
No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nmt2x2 `M` two-tick | reuse earliest incoming `M` at `t` versus `t+1` | `M` is frozen and disjoint from `O`; that leftover is HOLD/HOLD with composition HOLD | ATTEMPTED |
| nmoutx2 eventual-`O` | read `O` from eventual neighbor `M` with no `t`/`t+1` cut | that leftover already reports the `τ1` sets and hold/hold; it hides empty `O` at `τ0` | ATTEMPTED |
| unique own-outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | `O(A,τ1)` has three earliest outgoing steps; mixed remains a set; unique-letter reverse and face at `τ1` are `UNDEFINED` | ATTEMPTED |
| empty `O` as `UNDEFINED` | treat empty outgoing dual as unformed | the probe is formed; empty `O` is empty, not `UNDEFINED`; reverse/face are `UNDEFINED` from the empty comparison | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_2` at `A` from the origin partner; `O(A,τ0)` is empty | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores own outgoing step sets, not a lock-count clock | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process and probes; this member reports `UNDEFINED` then hold, with composition fail | ATTEMPTED |
| nmot2opp y-probe delayed `O` | reuse the y-probe seed `+e_1/−e_1` delayed-`O` report | different seed and probes; this member scores the #7214 x-probes | ATTEMPTED |
| sum of `O` | replace each set by its `Z^3` sum | the construction does not sum; sum of mixed `O(A,τ1)` cancels to `+e_1` while the set stays three-element | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis; mixed `A` at `τ1` would drop the axes of `e_1` and `e_3` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading `O` | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, and
missing Record identification of existential opposite are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_2` and `−e_2`, perpendicular step
rule, incoming-step lock, own outgoing dual from records with tick `<= τ`,
per-probe `τ0=t` and `τ1=t+1`, existential opposite, four x-probes with seed
`A`, empty `O` empty not `UNDEFINED`, mixed remains a set, and composition
as equality of the two-cut bits are declared. No uniqueness of outgoing
locks, no six-neighbor lock union as the scored object, no lock-count
clock, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest outgoing nearest-neighbor step in `O` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four outgoing sets at two cuts plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** New six-neighbor records between `t` and `t+1` should leave
`O` frozen the way nmt2x2 left `M` frozen, so reverse and face should
already HOLD at `t` as in nmoutx2; empty `O` should make the set
`UNDEFINED`; mixed `A` at `τ1` should make reverse `UNDEFINED`;
six-neighbor lock union already answered hold/hold on this same process;
nmt2x2 `M` two-tick already answered composition HOLD; mixed #7188 already
answered two-tick composition as fail/fail with composition HOLD; the
two-tick lock-count clock already answered two-tick composition; named
signs should suffice; nmot2opp already answered delayed `O` on y-probes;
and composition fail is only tautological because children form at `t+1`.

**Answer:** `O` is the outgoing dual of earliest incoming from the record
prefix. New six-neighbor records at `t+1` lock the step from the probe, so
they enter `O`. Empty `O` at formed `A`, `B`, and `C` at `τ0` is empty, not
`UNDEFINED`. Mixed `A` at `τ1` remains the set `{+e_1, +e_3, −e_3}`; reverse
is `hold`, not `UNDEFINED`. nmoutx2 eventual-`O` is a different cut: it
reads neighbor `M` after children exist. nmt2x2 `M` two-tick is a different
object: incoming is frozen and disjoint from `O`. Six-neighbor lock union is
a different object. Mixed #7188 fail/fail is a different process. The
two-tick lock-count clock composition is a different member. nmot2opp is a
different seed and probe set. Named signs lost the axis. Composition fail
is the displayed fact that the `t+1` bits do not equal the `t` bits on this
process; it is not an Admissibility rewrite.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same x-probes assigned
`−e_2`, `+e_2`, `+e_1`, `UNDEFINED` and reported reverse hold with face
`UNDEFINED`. nmxe2x #7214 own incoming exist-opposite reported reverse hold
and face hold from `M`. nmt2x2 `M` two-tick composition reported reverse
hold and face hold at both cuts with composition HOLD because `M` is frozen.
nmoutx2 eventual-`O` reported reverse hold and face hold from the `τ1`
outgoing sets with no empty `τ0` cut. Mixed #7188 two-tick composition
reported reverse fail and face fail with composition HOLD. nmot2opp
reported delayed `O` on y-probes. A two-tick lock-count clock composition
scored a different clock, not own outgoing step sets. This note is not
those displays: `O` is the own outgoing dual at `t` versus `t+1` on the
four #7214 x-probes, reverse is `UNDEFINED` then hold, face is `UNDEFINED`
then hold, and composition fail because those bits change from `t` to
`t+1`.

**Gate disposition:** PASS for the two-tick own-outgoing-set reverse/face
composition reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals `M` two-tick of nmt2x2,” “the predicate equals nmoutx2
eventual-`O`,” “the predicate equals six-neighbor lock union,” “the
predicate equals the two-tick lock-count clock,” “the predicate equals
mixed #7188 fail/fail,” “bits are Admissibility,” “reverse holds at `τ0`,”
“face holds at `τ0`,” “composition HOLD,” or “`O` is frozen at `t+1`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the x-axis opposite ±e_2
perp-step incoming-lock process, reads each probe's own outgoing dual of
the earliest incoming set from the record prefix at that probe's `t` and
at `t+1`, lists new records in `B_3(0)` between those cuts that meet a
probe's six-neighbors, and checks Theorems 1--3. It also checks that empty
`O` is empty not `UNDEFINED`, that mixed `O(A,τ1)` remains a set, that
unique-letter reverse at `τ1` is `UNDEFINED`, that `O` is disjoint from
`M`, that a formation member from already-recorded six-neighbor locks is
not attached, and that the display is not nmt2x2 `M` two-tick HOLD/HOLD.
No runner cache is written.
