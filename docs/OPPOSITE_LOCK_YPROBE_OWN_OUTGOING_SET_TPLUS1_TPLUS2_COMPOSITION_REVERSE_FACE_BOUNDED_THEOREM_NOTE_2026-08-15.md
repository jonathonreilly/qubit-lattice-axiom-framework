---
claim_id: opposite_lock_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from O at t+1 versus t+2 on the four #7208 y-probes, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# T+1 Versus T+2 Composition Of Own-Outgoing Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from each probe's own outgoing dual `O` of the
earliest incoming nearest-neighbor step set `M` at that probe's formation
tick plus one `t+1` versus `t+2`, on the four nsmopp #7208 y-probes in
`B_3(0)={n:n·n<=9}`, no global T. Same process as nsopp #7093. Let `t(q)`
be the formation tick of probe `q`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`.
Do not score `τ=t`. `M(r,τ)` is the set of earliest incoming nearest-neighbor
steps at `r` using only records with tick `<= τ`. Seeds are a singleton seed
letter. Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`:
the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)`
and `e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. O is not M. O is not a six-neighbor star. Reverse at
a cut holds if and only if `A` and `B` are formed by that cut and some `a`
in `O(A,·)` and some `b` in `O(B,·)` have `a+b=(0,0,0)`. Face likewise on
`C,D`. Empty or `UNDEFINED` on either side is `UNDEFINED`. Composition HOLD
if and only if the `t+2` reverse/face bits equal the `t+1` bits. This is not
leftover of nmot2opp `O` at `t` versus `t+1` (UNDEFINED at `t`, HOLD at
`t+1`, composition fail). This is not leftover of nmt2opp `M` two-tick
HOLD/HOLD. This is not leftover of nmoutopp eventual-`O` hold/hold. This is
not leftover of unique own-outgoing letters. This is not leftover of mixed
#7188 fail/fail. This is not the two-tick lock-count clock composition.
Uniqueness of outgoing locks is not required. Mixed remains a set.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut.
Reverse and face are scored on existence of an opposite pair in each probe's
own outgoing set at that probe's `t+1` and at `t+2`. Named signs `{+,−}` are
a coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. A `Z^3` sum of those locks
is a different readout and is not used. Occupancy `n` is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own outgoing duals O at each of the four #7208 y-probes at t+1 and at t+2, with reverse hold then hold, face hold then hold, and composition HOLD because t+2 bits equal t+1 bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display reverse and face from own outgoing sets at t+1 versus t+2 on the four #7208 y-probes, no global T, and whether those bits compose; first display whether O freezes once it appears"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to a unique outgoing letter, do not replace O by M, do not replace O by six-neighbor lock union, do not replace O by a lock-count clock, do not identify the bits with nmot2opp t versus t+1 UNDEFINED/hold composition fail, do not identify the bits with nmt2opp M HOLD/HOLD, do not identify the bits with nmoutopp eventual-O hold/hold, do not attach L1, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for t+1 versus t+2 composition of own-outgoing reverse/face on the four #7208 y-probes, no global T; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose own
outgoing sets are scored:

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

## Named outgoing set `O` at `t+1` and at `t+2`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.
Do not score τ=t.

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

Composition HOLD if and only if reverse at `τ2` equals reverse at `τ1` and
face at `τ2` equals face at `τ1`. Else composition fails. Displayed, not
adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `O`.

## Theorem 1 — ticks and `O` at `τ1` and at `τ2`

On this process the four y-probes form. Leftover nmot2opp scored `O` at `t`
versus `t+1` and found empty or singleton `O` at `t`, then enlarged `O` at
`t+1`, with composition fail. Do not score `τ=t`. The first display of `O`
at `t+1` versus `t+2` on #7167 is that outgoing freezes once it appears:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
O(A, τ1) = {+e_2, +e_3, −e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
O(A, τ2) = {+e_2, +e_3, −e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ2) = {+e_1, −e_1}
```

`A` is a seed at tick 0. Mixed remains a set: `O(A,τ1)` and `O(A,τ2)` each
have three outgoing steps `+e_2`, `+e_3`, and `−e_3`. Unique own-outgoing
letters would assign `UNDEFINED` at `A`, `B`, and `C` at both cuts. Here
uniqueness is not required. `O(q,τ2)=O(q,τ1)` at every scored probe.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors are exactly the sites that first fill `O` at `τ1`. Between
`t+1` and `t+2` no new six-neighbor of any scored probe forms:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
new 6-NN of A at t(A)+2: none
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

Those `t+1` neighbors enter `O(q,τ1)` because each locks the step from the
probe as earliest incoming. No further six-neighbor of a probe forms at
`t+2`, and earliest incoming of already-formed neighbors is frozen, so
`O(q,τ2)` equals `O(q,τ1)`.

Compare O to M of nmt2opp / nsmopp #7208. Same process reports

```text
M(A, τ1) = {−e_1}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_2}
M(D, τ1) = {−e_2, +e_3, −e_3}
```

with `M(q,τ2)=M(q,τ1)` at each probe. `M` and `O` are disjoint at each of
the four probes at both scored cuts. Reverse HOLD of #7208 uses `−e_1` in
`M(A)` against `+e_1` in `M(B)`. Those incoming letters are absent from
`O(A,τ1)` and `O(B,τ1)`. O is not M. No six-neighbor star.

This is not leftover of nmot2opp: that leftover scored `τ=t` against `t+1`
and reported empty `O` at `t` for `A`, `B`, and `C`, reverse UNDEFINED then
hold, face UNDEFINED then hold, composition fail. Do not score `τ=t`. This
is not leftover of nmt2opp `M` two-tick: that leftover freezes earliest
incoming at formation. This is not leftover of nmoutopp eventual-`O`: that
leftover reads `M` of neighbors without a `t+1` versus `t+2` cut. This is
not leftover of unique own-outgoing letters.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse holds if and only if some `a` in `O(A,·)` and some `b` in `O(B,·)`
have `a+b=(0,0,0)`. At `τ1` the sets are `{+e_2, +e_3, −e_3}` and
`{+e_2, +e_3, −e_3}`. The pair `+e_3+(−e_3)` sums to zero. Reverse holds.
At `τ2` the sets are the same, so reverse holds again.

Reverse at τ1: hold
Reverse at τ2: hold

Face holds if and only if some `c` in `O(C,·)` and some `d` in `O(D,·)` have
`c+d=(0,0,0)`. At `τ1` the sets are `{+e_1, −e_1, +e_3, −e_3}` and
`{+e_1, −e_1}`. The pair `+e_1+(−e_1)` sums to zero. Face holds. At `τ2`
the sets are the same, so face holds again.

Face at τ1: hold
Face at τ2: hold

Unique own-outgoing letters on these y-probes report reverse `UNDEFINED` and
face `UNDEFINED` from mixed `O` at `τ1` and at `τ2`. nmt2opp `M` two-tick
leftover reports reverse hold and face hold at both cuts. nmoutopp
eventual-`O` leftover reports reverse hold and face hold from the same
outgoing sets with no `t+1` versus `t+2` cut. nmot2opp leftover reports
reverse UNDEFINED at `t` and hold at `t+1`. Those are different objects.
Reverse holds at `τ1` and at `τ2` because a pair from `O(A,·)` and `O(B,·)`
is opposite, and the sets do not change.

## Theorem 3 — composition

Composition HOLD if and only if reverse at `τ2` equals reverse at `τ1` and
face at `τ2` equals face at `τ1`. Reverse is `hold` at `τ1` and `hold` at
`τ2`. Face is `hold` at `τ1` and `hold` at `τ2`. The bits match.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. The `t+2` reverse/face
bits are the same function of the `t+1` stack on this process: no new
six-neighbor records between those cuts enter the outgoing dual. Outgoing
freezes once it appears.

This is not leftover of nmot2opp: that leftover's composition fail is the
`t` versus `t+1` delay, not this freeze. This is not leftover of nmt2opp
`M` two-tick HOLD/HOLD: that leftover reports reverse hold and face hold at
both cuts with composition HOLD because earliest incoming is frozen at
formation. This is not leftover of nmoutopp eventual-`O` hold/hold. This is
not leftover of unique own-outgoing letters (reverse `UNDEFINED`, face
`UNDEFINED`). This is not the two-tick lock-count clock composition. This
is not leftover of mixed #7188 fail/fail: that mixed display reported
reverse fail and face fail with composition HOLD.

## What this note does not claim

- It does not select a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the outgoing set to be a singleton.
- It does not sum the outgoing set.
- It does not replace `O` by `M`.
- It does not replace `O` by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not score `τ=t`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-outgoing lock-vector letters on these
  y-probes as the object.
- It does not reprint nmot2opp `O` at `t` versus `t+1` UNDEFINED/hold
  composition fail.
- It does not reprint nmt2opp `M` two-tick HOLD/HOLD.
- It does not reprint nmoutopp eventual-`O` hold/hold.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy `n`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It does not attach L1.

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
opposite-lock two-site process, the own outgoing sets at `t+1` and at `t+2`,
and the reverse/face/composition bits are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `O` at `τ1` and at `τ2` | Theorem 1; filled at `τ1`; equal at `τ2` |
| compare O to M two-tick of nmt2opp | Theorem 1; disjoint; O is not M; M frozen, O frozen after it appears |
| reverse and face at `τ1` and at `τ2` | Theorem 2; `hold` / `hold` at reverse; `hold` / `hold` at face |
| composition | Theorem 3; HOLD because bits match |
| unique outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nmot2opp `O` at `t` versus `t+1` | not this display; Do not score `τ=t` |
| leftover of nmt2opp `M` two-tick HOLD/HOLD | not this display |
| leftover of nmoutopp eventual-`O` hold/hold | not this display |
| leftover of unique own-outgoing letters | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| attach L1 | not attached |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `O` at `t+1` versus `t+2` on the four #7208 y-probes, reverse/face, whether those bits compose, and whether outgoing freezes once it appears. |
| V2 | Current main has no landed t+1 versus t+2 own-outgoing-set reverse/face composition on these four #7208 y-probes. |
| V3 | Own outgoing sets at two cuts and the `hold`/`HOLD` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own outgoing dual at two delayed cuts and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing letter, does not replace `O` by `M`, does not replace `O`
by six-neighbor lock union, does not identify this display with the
two-tick lock-count clock, does not identify the bits with nmot2opp
`t` versus `t+1` UNDEFINED/hold composition fail, does not identify the
bits with nmt2opp `M` HOLD/HOLD, and does not identify the bits with mixed
#7188 fail/fail. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nmot2opp `O` at `t` versus `t+1` | reuse empty `O` at formation against `O` at `t+1` | that leftover is UNDEFINED then hold with composition fail; this member does not score `τ=t` | ATTEMPTED |
| nmt2opp `M` two-tick | reuse earliest incoming `M` at two cuts | `M` is frozen and disjoint from `O`; that leftover is HOLD/HOLD on incoming letters | ATTEMPTED |
| nmoutopp eventual-`O` | read `O` from eventual neighbor `M` with no `t+1`/`t+2` cut | that leftover already reports the filled sets and hold/hold; it hides the delayed cut pair | ATTEMPTED |
| unique own-outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | `O(A,τ1)` has three earliest outgoing steps; mixed remains a set; unique-letter reverse and face at `τ1` and `τ2` are `UNDEFINED` | ATTEMPTED |
| empty `O` as `UNDEFINED` | treat empty outgoing dual as unformed | leftover empty `O` at `t` is empty, not `UNDEFINED`; this member does not score that cut | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; scored `O(A,τ1)` is `{+e_2, +e_3, −e_3}` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores own outgoing step sets, not a lock-count clock | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process and probes; this member reports hold then hold, with composition HOLD | ATTEMPTED |
| sum of `O` | replace each set by its `Z^3` sum | the construction does not sum; sum of mixed `O(A,τ1)` cancels to `+e_2` while the set stays three-element | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis; mixed `A` at `τ1` would drop the axes of `e_2` and `e_3` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading `O` | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| attach L1 | promote the freeze to an L1 law | refused; Do not attach L1 | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, and
missing Record identification of existential opposite are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own outgoing dual from records with tick `<= τ`,
per-probe `τ1=t+1` and `τ2=t+2`, existential opposite, four y-probes with seed
`A`, mixed remains a set, Do not score `τ=t`, and composition as equality of
the two-cut bits are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no global
later T, no formation attachment from already-recorded six-neighbor locks,
no L1 attachment, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest outgoing nearest-neighbor step in `O` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four outgoing sets at two cuts plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Because nmot2opp already showed `O` delayed at `t` then HOLD
at `t+1` with composition fail, the `t+1` versus `t+2` cut is only a reprint
of that delay; new six-neighbor records between `t+1` and `t+2` should keep
changing `O`; mixed `A` at `τ1` should make reverse `UNDEFINED`;
six-neighbor lock union already answered hold/hold on this same process;
nmt2opp `M` two-tick already answered composition HOLD; mixed #7188 already
answered two-tick composition as fail/fail with composition HOLD; the
two-tick lock-count clock already answered two-tick composition; named
signs should suffice; freeze is only tautological because children form at
`t+1`; and composition HOLD should be written into Admissibility or
attached as L1.

**Answer:** nmot2opp scored `τ=t` against `t+1`. This member does not score
`τ=t`. New six-neighbor records at `t+1` lock the step from the probe, so
they enter `O` by `τ1`. No new six-neighbor of a probe forms at `t+2`, so
`O` freezes once it appears. Mixed `A` at `τ1` remains the set
`{+e_2, +e_3, −e_3}`; reverse is `hold`, not `UNDEFINED`. nmoutopp
eventual-`O` is a different cut: it reads neighbor `M` after children exist.
nmt2opp `M` two-tick is a different object: incoming is frozen and disjoint
from `O`. Six-neighbor lock union is a different object. Mixed #7188
fail/fail is a different process. The two-tick lock-count clock composition
is a different member. Named signs lost the axis. Composition HOLD is the
displayed fact that the `t+2` bits equal the `t+1` bits on this process; it
is not an Admissibility rewrite. Do not attach L1.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same y-probes assigned
`−e_1`, `+e_1`, `+e_2`, `UNDEFINED` and reported reverse hold with face
`UNDEFINED`. nsmopp #7208 own incoming exist-opposite reported reverse hold
and face hold from `M`. nmt2opp `M` two-tick composition reported reverse
hold and face hold at both cuts with composition HOLD because `M` is frozen.
nmoutopp eventual-`O` reported reverse hold and face hold from the filled
outgoing sets with no delayed cut pair. nmot2opp own-outgoing two-tick
composition reported reverse UNDEFINED then hold, face UNDEFINED then hold,
and composition fail because `O` at `t` is empty or singleton and enlarges
at `t+1`. Mixed #7188 two-tick composition reported reverse fail and face
fail with composition HOLD. A two-tick lock-count clock composition scored
a different clock, not own outgoing step sets. This note is not those
displays: `O` is the own outgoing dual at `t+1` versus `t+2`, reverse is
hold then hold, face is hold then hold, and composition HOLD because those
bits freeze once outgoing appears.

**Gate disposition:** PASS for the t+1 versus t+2 own-outgoing-set
reverse/face composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals `M` two-tick of nmt2opp,”
“the predicate equals nmoutopp eventual-`O`,” “the predicate equals
six-neighbor lock union,” “the predicate equals the two-tick lock-count
clock,” “the predicate equals mixed #7188 fail/fail,” “the predicate
equals nmot2opp `t` versus `t+1` UNDEFINED/hold composition fail,” “bits
are Admissibility,” “reverse is UNDEFINED at `τ1`,” “face is UNDEFINED at
`τ1`,” “composition fail,” “`O` still grows from `t+1` to `t+2`,” or
“attach L1.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's own outgoing dual of the earliest
incoming set from the record prefix at that probe's `t+1` and at `t+2`, lists
new records in `B_3(0)` at `t+1` and at `t+2` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that mixed
`O(A,τ1)` remains a set, that unique-letter reverse at `τ1` and `τ2` is
`UNDEFINED`, that `O` is disjoint from `M`, that leftover nmot2opp `τ=t`
is UNDEFINED then hold with composition fail, that a formation member from
already-recorded six-neighbor locks is not attached, and that L1 is not
attached. No runner cache is written.
