---
claim_id: two_axis_same_lock_yprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the own outgoing *set* at t+1 on the four y-probes of the two-axis same-lock seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py
---

# Own Outgoing Set Existential Opposite Reverse And Face At t+1 On Four Two-Axis Same-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own outgoing *set* `O(q,τ)` at
each probe's `τ=t+1` on the four y-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Same process and y-probes as nm2sl. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Reverse holds if and only if some lock in
`O(A,τ)` is the vector opposite of some lock in `O(B,τ)`. Face holds if
and only if some lock in `O(C,τ)` is the vector opposite of some lock in
`O(D,τ)`. Empty or `UNDEFINED` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Timed: the cut is
`τ=t+1`, not formation tick `t`. Uniqueness of incoming or outgoing locks
is not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1. This is not leftover of axis-cover.
This is not exist-opposite of `M`. Occupancy of sites is not used. This
display does not use occupancy.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on existence of an opposite pair in
the own outgoing sets. Named signs `{+,−}` are a coarser readout and are
not used. A singleton unique lock letter is a different readout and is not
used as the object: report `O`. A `Z^3` sum of those locks is a different
readout and is not used. The construction does not sum. Occupancy of sites
is not used. A six-neighbor star is not the letter. Axis-cover of `M` and
`O` is a different predicate and is leftover. Exist-opposite of `M` with
`M` is a different predicate and is leftover.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own outgoing set O at t+1 on the four y-probes of the two-axis same-lock seed, reverse hold from exist-opposite of O(A,τ) and O(B,τ), face hold from exist-opposite of O(C,τ) and O(D,τ); uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face
target_blocker_text: "display reverse and face from the own outgoing set at t+1 on the four y-probes of the two-axis same-lock seed, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face from own outgoing set at t+1 displayed; do not write existential opposite into Admissibility, do not reduce to exist-opposite of M, do not reduce to axis-cover leftover, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own outgoing set at t+1 on the four y-probes of the two-axis same-lock seed; displayed, not adopted"
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
outgoing exist-opposite is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nm2sl.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. Independently, `(0,0,1)` locks
`+e_2` and `(0,1,1)` locks `+e_2`. Neither pair is opposite. This seed is
not the one-axis two-site same-lock seed `{0,(0,1,0)}` both locking `+e_1`.
This seed is not the opposite two-site seed `+e_1/−e_1`. This seed is not
the two-axis opposite seed that would lock the second pair as `+e_2/−e_2`.

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

## Named incoming set `M`, outgoing set `O`, and exist-opposite at `τ=t+1`

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
does not replace `O` by `M`. Occupancy of sites is not used. O is not M.

Reverse holds if and only if some `a` in `O(A,τ)` and some `b` in `O(B,τ)`
have `a+b=(0,0,0)`. Face holds if and only if some `c` in `O(C,τ)` and some
`d` in `O(D,τ)` have `c+d=(0,0,0)`. Empty or `UNDEFINED` on either side is
`UNDEFINED`. Nonempty with no opposite pair fails. Mixed remains a set.

The timed cut is required. At formation tick `t` itself, `O` is empty at
each of the four y-probes, so exist-opposite reverse and face at `t` are
`UNDEFINED`. At `τ=t+1` the outgoing dual is nonempty.

Exist-opposite of `M` scores some pair in `M(A,τ)` against `M(B,τ)`, or in
`M(C,τ)` against `M(D,τ)`. That leftover is not this display. Axis-cover of
`M` and `O` scores complementary unsigned axes at one probe; cover reverse
HOLDs and cover face fail on this member. That leftover is not this
display. Internal exist-opposite inside one `O` set is a different
predicate: `O(A,τ)` has no internal opposite pair.

## Theorem 1 — ticks, `M`, and `O` at `τ=t+1`

On this process the four y-probes form. Direct enumeration of the displayed
two-axis same-lock process on `B_3(0)` reports:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1}
```

`A` is a seed at tick 0. Mixed remains a set: `O(A,τ)` has two outgoing
steps, `O(B,τ)` has three, and `O(C,τ)` has four. Unique letters would
assign `UNDEFINED` at those mixed outgoing sets. Here uniqueness is not
required. `M` at `τ` equals `M` at `t`. Empty `O` at formation tick `t`
makes exist-opposite `UNDEFINED`; the `t+1` cut is required.

On the one-axis same-lock leftover `{0,(0,1,0)}` both locking `+e_1`, the
same y-probes instead form at ticks `0,2,1,3`, and `O(A,τ)` includes `+e_3`
because `(0,1,1)` is then a formed child rather than a seed. That leftover
is not this display. Seed `(0,1,1)` keeps letter `+e_2`, so `+e_3` is not
in `M((0,1,1),τ)` and is not in `O(A,τ)`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if some lock in `O(A,τ)` is the vector opposite
of some lock in `O(B,τ)`. Both sides are nonempty and defined, so this is
not `UNDEFINED`. Witness: `−e_3` in `O(A,τ)` and `+e_3` in `O(B,τ)`. Reverse
HOLDs. This is not exist-opposite of `M`. M exist-opposite reverse fail:
both `M(A,τ)` and `M(B,τ)` are `{+e_1}`. Unique-letter reverse is
`UNDEFINED` at mixed `O(A,τ)`. Internal exist-opposite inside `O(A,τ)`
fails because `{+e_2, −e_3}` has no opposite pair.

Reverse: hold

witness (−e_3, +e_3)

This is not `fail` and not `UNDEFINED`. Reverse holds.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if some lock in `O(C,τ)` is the vector opposite of
some lock in `O(D,τ)`. Both sides are nonempty and defined, so this is not
`UNDEFINED`. Witness: `−e_1` in `O(C,τ)` and `+e_1` in `O(D,τ)`. Face HOLDs.
This is not leftover of axis-cover. Axis-cover HOLDs at `C` and fails at
`D`, so cover face fail, while exist-opposite of `O` face HOLDs. M
exist-opposite face fail: `M(C,τ)={+e_2}` and `M(D,τ)={−e_3}` are not
opposite.

Face: hold

witness (−e_1, +e_1)

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds.

Face holds.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require either set to be a singleton.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace exist-opposite of `O` by exist-opposite of `M`.
- It does not replace exist-opposite of `O` by axis-cover of `M` and `O`.
- It does not score reverse as an opposite pair inside one `O` set.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use occupancy of sites.
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
two-axis same-lock process, the incoming and outgoing sets at `t+1`, and the
exist-opposite reverse/face bits from own outgoing `O` are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; `{+e_1}`, `{+e_1}`, `{+e_2}`, `{−e_3}` |
| `O` at `τ=t+1` | Theorem 1; `{+e_2, −e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`, `{+e_1}` |
| reverse from exist-opposite of `O(A,τ)` and `O(B,τ)` | Theorem 2; `hold` |
| face from exist-opposite of `O(C,τ)` and `O(D,τ)` | Theorem 3; `hold` |
| unique incoming or outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| exist-opposite of `M` | not this display; M exist-opposite reverse fail; M exist-opposite face fail |
| leftover of axis-cover | not this display; cover reverse hold, cover face fail |
| empty `O` at formation tick `t` | not this cut; exist-opposite `UNDEFINED` at `t` |
| one-axis same-lock leftover | not this display; ticks `0,2,1,3` and `O(A)` includes `+e_3` |
| two-axis opposite leftover | not this display; `M(A)={−e_1}` and `O(D)` includes `−e_1` |
| global later T | not used |
| exist-opposite of `O` as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: exist-opposite of own outgoing `O` at `t+1` on the four y-probes of the two-axis same-lock seed, and reverse/face from that. |
| V2 | Current main has no landed own-outgoing exist-opposite reverse/face at `t+1` on these four two-axis same-lock y-probes. |
| V3 | `O` at four probes and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the own outgoing set at the per-probe `t+1` cut and scores existence of a vector-opposite pair across reverse and face. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace exist-opposite of `O` by exist-opposite of
`M`, and does not identify this display with leftover of axis-cover. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| exist-opposite of `M` | score some pair in `M(A,τ)` against `M(B,τ)` | M exist-opposite reverse fail and M exist-opposite face fail; both `M(A)` and `M(B)` are `{+e_1}` | ATTEMPTED |
| leftover of axis-cover | score complementary unsigned axes of `M` and `O` | cover HOLDs at `A`,`B`,`C` and fails at `D`; cover reverse hold and cover face fail, while `O` exist-opposite face HOLDs | ATTEMPTED |
| unique letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)`, `O(B,τ)`, and `O(C,τ)` remain sets; unique-letter reverse is `UNDEFINED` while reverse HOLDs | ATTEMPTED |
| empty `O` at `t` | score exist-opposite at formation tick `t` | empty `O` at each probe at `t` makes reverse and face `UNDEFINED`; the timed cut is `τ=t+1` | ATTEMPTED |
| internal opposite inside one `O` | score an opposite pair inside `O(A,τ)` alone | `O(A,τ)={+e_2, −e_3}` has no internal opposite; reverse HOLDs from `−e_3` against `+e_3` in `O(B,τ)` | ATTEMPTED |
| one-axis same-lock leftover | drop the second pair and keep only `{0,(0,1,0)}` both `+e_1` | ticks become `0,2,1,3` and `O(A,τ)` gains `+e_3` | ATTEMPTED |
| two-axis opposite leftover | lock the pairs as `+e_1/−e_1` and `+e_2/−e_2` | `M(A)` there is `{−e_1}` and `O(D)` includes `−e_1`; here `M(A)={+e_1}` and `O(D)={+e_1}` | ATTEMPTED |
| nsopp exist-opposite of `M` | reuse opposite `+e_1/−e_1` y-probes | that leftover has M exist-opposite reverse hold; this member has M exist-opposite reverse fail | ATTEMPTED |
| sum of a set | replace each `O` by its `Z^3` sum | the construction does not sum; `sum O(A)=(0,1,−1)` and `sum O(B)=(0,1,0)` do not cancel | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by exist-opposite of `O` | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of exist-opposite of `O`
with exist-opposite of `M`, missing identification of exist-opposite of `O`
with leftover of axis-cover, and missing Record identification of the bits
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2`,
perpendicular step rule, incoming-step lock, own incoming set and own
outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`, four
y-probes with seed `A`, reverse as exist-opposite of `O(A,τ)` and
`O(B,τ)`, face as exist-opposite of `O(C,τ)` and `O(D,τ)`, and mixed
remains a set are declared. No uniqueness of locks, no exist-opposite of
`M` as the scored object, no leftover of axis-cover as the scored object,
no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock in own outgoing `O` at a probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `O` reports, reverse/face from exist-opposite of `O` | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Timed exist-opposite of `O` is only axis-cover reverse/face;
same-lock cover already reverse-HOLDs and face-fails; exist-opposite of
`M` already answered signed reverse; mixed outgoing sets should make the
predicate `UNDEFINED`; empty leftover of `O` at `t` already answered the
cut; the second same-lock pair is just the one-axis child `(0,1,1)`.

**Answer:** Axis-cover face fails at `D` because `Axis(M)={e_3}` and
`Axis(O)={e_1}` miss `e_2`, while exist-opposite of `O` face HOLDs from
`−e_1` in `O(C,τ)` against `+e_1` in `O(D,τ)`. M exist-opposite reverse
fail because both sides are `{+e_1}`. Mixed `O(A,τ)` remains
`{+e_2, −e_3}` and reverse HOLDs from `−e_3` against `+e_3` in `O(B,τ)`.
Empty `O` at `t` makes exist-opposite `UNDEFINED`; the timed cut is
`τ=t+1`. Seed `(0,1,1)` keeps letter `+e_2`, so `O(A,τ)` does not contain
`+e_3`.

### N8 — cross-cycle echo

nm2sl reports axis-cover of `M` and `O` at `t+1` on these same four
y-probes and the same two-axis same-lock seed: cover reverse hold, cover
face fail. One-axis same-lock leftover forms the same probes at ticks
`0,2,1,3` and puts `+e_3` in `O(A,τ)`. Opposite two-site leftover locks
`A` as `−e_1`. This note is not those displays: it reports own outgoing
`O` at `τ=t+1`, exist-opposite reverse hold, and exist-opposite face hold.

**Gate disposition:** PASS for the own-outgoing exist-opposite `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
exist-opposite of `M`,” “the predicate equals leftover of axis-cover,”
“the predicate equals the unique singleton lock vector,” “the predicate
equals empty `O` at `t`,” “bits are Admissibility,” “reverse fails,” or
“face fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
scores exist-opposite of `O` at reverse and at face, and checks Theorems
1--3. It also checks that exist-opposite of `M` fails reverse and fails
face, that leftover of axis-cover face-fails, that mixed outgoing sets
remain sets, that uniqueness is not required, that occupancy of sites is
not used, that empty `O` at `t` is `UNDEFINED`, that the seed is not the
one-axis leftover, and that a formation member from already-recorded
six-neighbor locks is not attached. No runner cache is written.
