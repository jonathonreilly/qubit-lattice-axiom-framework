---
claim_id: two_axis_opposite_xprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the own outgoing *set* at t+1 on the four x-probes of the two-axis opposite seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py
---

# Own Outgoing Set Existential Opposite At t+1 Reverse And Face On Four X-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own outgoing *set* `O(q,τ)` at
each probe's `τ=t+1` on the four x-probes of the two-axis opposite seed in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2axx. Process: two
disjoint opposite pairs. Seed at tick 0: origin locks `+e_1`, `(0,1,0)`
locks `−e_1`, `(0,0,1)` locks `+e_2`, `(0,1,1)` locks `−e_2`. The second
pair is a new seed, not a formed child. Perp-step, incoming lock. Let
`t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. There is no
global T. `M(q,τ)` is the set of earliest incoming nearest-neighbor steps
at `q` using only records with tick `<= τ`. Seeds are a singleton seed
letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Reverse
holds if and only if some lock in `O(A,τ)` is the vector opposite of some
lock in `O(B,τ)`. Face holds if and only if some lock in `O(C,τ)` is the
vector opposite of some lock in `O(D,τ)`. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`; nonempty with no opposite pair fails.
nm2axo O HOLDING on y-probes. nm2axx cover FAIL/FAIL on x-probes.
Discriminator: does signed O still HOLD where cover fails? It does not:
reverse fails and face fails. This is not leftover of axis-cover FAIL/FAIL
of `M` and `O` at `t+1`. This is not leftover of M exist-opposite. This is
not leftover of unique-L. This is not leftover of nm2axo y-probe HOLD/HOLD.
This is not leftover of nmoutopp untimed eventual-`O`. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1. This note does not write existential
opposite into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Mixed remains a set. Unique `L` is not the object. The six-neighbor star is
not the letter. Occupancy of sites is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
O is not M.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on existence of an opposite pair in the
own outgoing sets at that same cut. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used as the object: report `O`. A `Z^3` sum of
those locks is a different readout and is not used. The construction does
not sum. Occupancy of sites is not used. A six-neighbor star is not the
letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of O(q, tau) as the probe's own outgoing dual of M at t+1 on the four x-probes of the two-axis opposite seed, mixed remains a set, with reverse fail and face fail from existential opposite; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_own_outgoing_set_existential_opposite_tplus1_reverse_face
target_blocker_text: "display reverse and face from the own outgoing set at t+1 on the four x-probes of the two-axis opposite seed, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not identify the sets with unique-L leftover, do not identify the sets with axis-cover FAIL/FAIL, do not identify the sets with M exist-opposite, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own outgoing set at t+1 on the four x-probes of the two-axis opposite seed, reverse fail and face fail; displayed, not adopted"
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
outgoing sets at `τ=t+1` are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are the nsopp x-probes. These are not the y-probes `A=(0,1,0)`,
`B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are not the z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. The first
pair is `{0, (0,1,0)}` with opposite locks `L(0)=+e_1` and
`L(0,1,0)=−e_1`. The second pair is `{(0,0,1), (0,1,1)}` with opposite
locks `L(0,0,1)=+e_2` and `L(0,1,1)=−e_2`. The second pair is a new seed,
not a formed child of the first pair. This is not nsopp leftover: on the
one-axis seed those two sites form at tick 1 with incoming `+e_3`. This
seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
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

## Named existential opposite from the own outgoing set at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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
not require `O` to be a singleton. It does not sum `O`. Unique `L(q)` is not
used as the letter. This display does not use a six-neighbor star. Occupancy
of sites is not used. It is not a unique lock-vector leftover and not a sum
leftover. It is not leftover of unique-L. It is not leftover of M
exist-opposite. It is not leftover of axis-cover. O is not M.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in O(A,τ) and some b in O(B,τ) with a+b=(0,0,0)
face     <=>  some c in O(C,τ) and some d in O(D,τ) with c+d=(0,0,0)
```

If `O(A,τ)` or `O(B,τ)` is empty or `UNDEFINED`, reverse is `UNDEFINED`. Else
reverse fails if no such pair exists. If `O(C,τ)` or `O(D,τ)` is empty or
`UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks, `M`, and `O` at `τ=t+1`

On this process the four x-probes form. Those ticks locate the earliest
incoming set and the outgoing dual at the per-probe cut `τ=t+1`. They are
not occupancy kernels and are not a global later T.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {−e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ)` has three outgoing
steps, `O(C,τ)` has three, and `O(D,τ)` has two. `O(A,τ)` is a singleton
`{+e_1}`. Unique letters would assign `UNDEFINED` at mixed `O(B)`, `O(C)`,
and `O(D)`. Here uniqueness is not required. `M` is frozen from `t` to
`t+1`. O is not M. `M` and `O` are disjoint at each of the four probes.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

At `t`, `O(A,t)`, `O(B,t)`, and `O(C,t)` are empty, while `O(D,t)={−e_1}`.
Empty `O` at `t` is not this letter. This display reads `O` at `τ=t+1`.

Compare to #7167 1-axis. Same x-probes, same perp-step incoming lock, one
opposite pair `{0,(0,1,0)}` with `+e_1/−e_1` only. On that 1-axis seed the
runner reports `t(A)=3`, `t(B)=2`, `t(C)=4`, `t(D)=3`, and the same
outgoing sets at `t+1`. The two-axis seed advances `t(A)` from 3 to 2,
`t(B)` from 2 to 1, `t(C)` from 4 to 3, and `t(D)` from 3 to 2 because
`(0,0,1)` and `(0,1,1)` are seeds rather than formed children. Reverse of
1-axis `O` fails. Face of 1-axis `O` fails. Tick advance is not identity of
the letter: the scored object is signed `O` at each probe's own `t+1`.

Axis-cover of `M` and `O` at this same cut fails at `A`, HOLDs at `B`,
HOLDs at `C`, and fails at `D` because `Axis(M)∪Axis(O)` at `A` and at `D`
misses `e_2`. That leftover of axis-cover reports reverse fail and face
fail. Cover HOLDs at `B` and at `C`. This display scores signed
exist-opposite of `O` alone. Cover HOLD at `B` is not exist-opposite HOLD.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse of `O` at `τ` holds if and only if there exist `a` in `O(A,τ)` and
`b` in `O(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty:
`O(A,τ)={+e_1}` and `O(B,τ)={+e_2, +e_3, −e_3}`. No pair adds to zero:
`+e_1` has no opposite in `O(B,τ)`. Reverse fails.

Reverse of O at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Unique-L leftover of
`O` reports reverse `UNDEFINED` because `O(B,τ)` is mixed. M exist-opposite
reverse fails from `−e_3` in `M(A,τ)` against `+e_1` in `M(B,τ)`. Those
incoming letters are disjoint from `O` at each reverse probe. Axis-cover
reverse fails from cover fail at `A`, while cover HOLDs at `B`. Reverse
fails here because a pair from `O(A,τ)` and `O(B,τ)` is not opposite.
Y-probe exist-opposite reverse HOLDs on this same seed from
`O(A,τ)={+e_2, −e_3}` against `O(B,τ)={+e_2, +e_3, −e_3}`.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face of `O` at `τ` holds if and only if there exist `c` in `O(C,τ)` and
`d` in `O(D,τ)` with `c+d=(0,0,0)`. Both sets are nonempty:
`O(C,τ)={−e_2, +e_3, −e_3}` and `O(D,τ)={+e_1, −e_1}`. No pair adds to
zero: `±e_1` at `D` has no opposite in `O(C,τ)`, and `−e_2` at `C` has no
opposite in `O(D,τ)`. Face fails.

Face of O at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. Unique-L leftover of
`O` reports face `UNDEFINED` from mixed outgoing sets at `C` and at `D`.
M exist-opposite face fails because `M(C,τ)={+e_1}` has no opposite in
`M(D,τ)={−e_3}`. Axis-cover face fails because cover fails at `D`, while
cover HOLDs at `C`. Exist-opposite face of signed `O` also fails, but from
the signed pair `{−e_2, +e_3, −e_3}` against `{+e_1, −e_1}`, not from the
unsigned leftover `{e_2}` at `D`. Named-sign lettering lost the axis in
mixed `{+,−}` at `B`, `C`, and `D`. Y-probe exist-opposite face HOLDs on
this same seed. Face already fails at each probe's own `t+1` from the own
outgoing set.

Face fails.

## What this note does not claim

- It does not select a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own outgoing set to be a singleton.
- It does not sum the own outgoing set.
- It does not use occupancy of sites as the letter.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique-L letters on these x-probes as the object.
- It does not reprint M exist-opposite as the letter.
- It does not reprint axis-cover of `M` and `O` as the letter.
- It does not reprint y-probe HOLD/HOLD as this x-probe letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not treat the second pair as a formed child of nsopp leftover.
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
two-axis opposite-pair process, the own outgoing sets at `t+1`, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| compare O to M | Theorem 1; disjoint at each probe; O is not M |
| reverse from exist-opposite of `O` at `τ` | Theorem 2; `fail` |
| face from exist-opposite of `O` at `τ` | Theorem 3; `fail` |
| comparison to #7167 1-axis | Theorem 1; 1-axis ticks `3,2,4,3`; same `O` sets |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of M exist-opposite | not this display |
| leftover of axis-cover | not this display |
| leftover of nm2axo y-probe HOLD/HOLD | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| second pair as formed child | refused; new seed |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the discriminator: own outgoing set at `t+1` on the four x-probes of the two-axis opposite seed, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed timed own-outgoing-set existential-opposite reverse/face report on these four x-probes of the two-axis opposite seed. |
| V3 | Own outgoing sets at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own outgoing dual of `M` at `t+1` and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not sum the lock set, does not reprint unique-L, does not
reprint M exist-opposite as the letter, does not reprint axis-cover as the
letter, does not use a six-neighbor star, and does not use occupancy of
sites. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of axis-cover | score reverse/face as complementary unsigned axes of `M` and `O` | axis-cover reverse fails and face fails, but cover HOLDs at `B` and at `C`; this reverse fails from `{+e_1}` against `{+e_2,+e_3,−e_3}` | ATTEMPTED |
| leftover of M exist-opposite | reuse signed reverse/face of `M` at `τ` | M reverse fails and M face fails from `{−e_3}` against `{+e_1}` and `{+e_1}` against `{−e_3}`; those incoming sets are disjoint from `O` | ATTEMPTED |
| unique-L leftover | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter reverse of `O` is `UNDEFINED` while reverse fails | ATTEMPTED |
| sum of the same outgoing sets | replace `O` by the `Z^3` sum | the construction does not sum; sum of mixed `O(B,τ)` cancels to `+e_2` while `O(B,τ)` stays a three-element set | ATTEMPTED |
| nm2axo y-probes | score `A=(0,1,0)`, `C=(0,2,0)` | leftover; y-probe reverse HOLDs and face HOLDs while x-probe reverse fails and face fails | ATTEMPTED |
| z-probes on the same process | score `A=(0,0,1)`, `C=(0,0,2)` | leftover; z-probe reverse HOLDs and face fails; `O(A)` there is `{+e_1,−e_1,+e_3}`, not `{+e_1}` | ATTEMPTED |
| nmsimopp one-axis simultaneous | reuse 1-axis `M` and `O` together at `t+1` | different seed; two-axis advances ticks from `3,2,4,3` to `2,1,3,2` | ATTEMPTED |
| nmoutopp untimed eventual-`O` | wait for all later children | `τ(q)=t(q)+1` is per-probe; no untimed eventual set | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is a different signed letter; this display reads `O` alone | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| occupancy of sites | assign one letter from occupancy | occupancy of sites is not used | ATTEMPTED |
| occupancy-kernel inner product | score an occupancy inner product | different object; not an occupancy-kernel inner product | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | this display does not use a six-neighbor star | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores exist-opposite of own outgoing at `t+1` | ATTEMPTED |
| nsopp leftover child | treat `(0,0,1)` and `(0,1,1)` as formed children | they are tick-0 seeds with `+e_2/−e_2`, not tick-1 children with incoming `+e_3` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of this display with
axis-cover, missing identification of this display with M exist-opposite,
and missing Record identification of exist-opposite reverse are distinct
open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-axis opposite seed locks `+e_1/−e_1` and `+e_2/−e_2`,
perpendicular step rule, incoming-step lock, own outgoing dual from records
with tick `<= τ`, per-probe `τ=t+1`, four x-probes with `A` not a seed,
second pair is a new seed, mixed remains a set, and reverse/face as existence
of a pair that sums to zero are declared. No uniqueness of outgoing locks, no
occupancy of sites, no named-sign reduction, no singleton leftover as the
object, no sum leftover, no unique-L leftover, no M exist-opposite leftover,
no leftover of axis-cover, no six-neighbor star as the letter, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own outgoing set at `t+1` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four outgoing sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The own outgoing set at `t+1` is leftover of unique-L because
`O(A)` is already a singleton `{+e_1}`; the sets should be replaced by their
sums; axis-cover already answered FAIL/FAIL; M exist-opposite already
answered signed FAIL/FAIL; y-probe HOLD/HOLD already answered timed `O`;
named signs should suffice because they keep orientation; and occupancy of
sites should track that vector.

**Answer:** The named construction reports outgoing sets `{+e_1}`,
`{+e_2, +e_3, −e_3}`, `{−e_2, +e_3, −e_3}`, `{+e_1, −e_1}` at `A,B,C,D`
from the probe's own outgoing dual of `M` at `τ=t+1`. Mixed remains a set.
The construction does not sum. Occupancy of sites is not used. Named signs
lost the axis. No pair from `O(A,τ)` and `O(B,τ)` is opposite, so reverse
fails. No pair from `O(C,τ)` and `O(D,τ)` is opposite, so face fails.
Unique-L leftover of `O` reports reverse `UNDEFINED` and face `UNDEFINED`
from mixed outgoing sets at `B`, `C`, and `D`. M exist-opposite reports
reverse fail and face fail from incoming sets that are disjoint from `O`
at each probe. Axis-cover reports reverse fail and face fail from incomplete
unsigned union at `A` and at `D`, while cover HOLDs at `B` and at `C`.
Y-probe exist-opposite HOLDs reverse and face on this same seed. Fail from
outgoing `{+e_1}` at reverse and `{−e_2,+e_3,−e_3}` at face, while cover
HOLDs at `B` and at `C` and y-probe O HOLDs, is a discriminator. The sets
are not those leftovers. The bits remain displayed. Outgoing-lock uniqueness
is not required. O is not M.

### N8 — cross-cycle echo

#7167 1-axis on these x-probes reports the same `O` sets with later ticks
`3,2,4,3` and reverse fail, face fail. Axis-cover on these x-probes reports
reverse fail and face fail from leftover `{e_2}` at `A` and at `D`, while
cover HOLDs at `B` and at `C`. M exist-opposite on this seed reports reverse
fail and face fail from incoming `{−e_3}` against `{+e_1}`. Unique lock-vector
lettering of the outgoing sets would report reverse `UNDEFINED` and face
`UNDEFINED` because reverse and face mix at `B`, `C`, and `D`. nm2axo y-probe
exist-opposite reports reverse hold and face hold. A sum leftover of the
same lists would replace mixed `O(B,τ)` by `+e_2` after cancelling `+e_3`
and `−e_3`. This note is not those displays: mixed remains a set, the
construction does not sum, the letter is the own outgoing set at `t+1` on
the four x-probes of the two-axis opposite seed, reverse fails, and face
fails.

**Gate disposition:** PASS for the own-outgoing-set existential-opposite
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals the sum of the lock set,” “the predicate
equals leftover of axis-cover,” “the predicate equals leftover of M
exist-opposite,” “bits are Admissibility,” “the letter is occupancy of
sites,” “the sets equal unique-L leftover,” “reverse holds,” or “face
holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own outgoing dual of
the incoming set from the record prefix at that probe's `t+1`, scores
reverse and face by existential opposite, compares the same observables on
the #7167 1-axis seed, and checks Theorems 1--3. It also checks that mixed
sets remain sets, that unique-letter reverse of `O` is `UNDEFINED`, that
axis-cover HOLDs at `B` and at `C` while this reverse fails, that M is
disjoint from `O`, that y-probe exist-opposite HOLDs on this same seed,
that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a new seed, and that the display is not leftover of axis-cover. No runner
cache is written.
