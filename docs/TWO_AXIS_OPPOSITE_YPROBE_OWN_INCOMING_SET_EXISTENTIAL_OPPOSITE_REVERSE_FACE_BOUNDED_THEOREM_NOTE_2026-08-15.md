---
claim_id: two_axis_opposite_yprobe_own_incoming_set_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the own incoming *set* at t+1 on the four y-probes of the two-axis opposite seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py
---

# Own Incoming Set Existential Opposite Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own incoming *set* `M(q,τ)` at
each probe's `τ=t+1` on the four y-probes of the two-axis opposite seed in
`B_3(0)={n:n·n<=9}`. Process: two disjoint opposite pairs. Seed at tick 0:
origin locks `+e_1`, `(0,1,0)` locks `−e_1`, `(0,0,1)` locks `+e_2`,
`(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed child.
Perp-step, incoming lock. Let `t(q)` be the formation tick of probe `q`.
Let `τ(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick
`<= τ`. Seeds are a singleton seed letter. Mixed remains a set. Unformed
at `τ` is `UNDEFINED`. Reverse holds if and only if some lock in `M(A,τ)`
is the vector opposite of some lock in `M(B,τ)`. Face holds if and only if
some lock in `M(C,τ)` is the vector opposite of some lock in `M(D,τ)`.
Empty or `UNDEFINED` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Unique `L` is not the object: report
`M`. Occupancy of sites is not used. This is not named-sign lettering.
This is not a unique lock-vector leftover and not a sum leftover. This is
not leftover of unique-L. This is not leftover of nm2ax axis-cover of `M`
and `O`. This is not leftover of nmsimopp exist-opposite of `M` and of
`O` at `t+1`. This is not leftover of timed `O` exist-opposite. This is
not leftover of nmt2opp `M` frozen at `t` as a different seed. This is not
leftover of mixed #7188 fail/fail. Uniqueness of incoming locks is not
required. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. This note does not write existential opposite into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks. The six-neighbor star is not the letter.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own incoming sets at the per-probe cut `τ=t+1`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used as the object: report `M`. A `Z^3` sum of
those locks is a different readout and is not used. The construction does
not sum. Occupancy of sites is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M(q,τ) as the probe's own incoming set of earliest NN steps at τ=t+1 on the four y-probes of the two-axis opposite seed, mixed remains a set, with reverse hold from singleton M(A,τ) and face fail from no opposite pair in M(C,τ) and M(D,τ); uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_own_incoming_set_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from the own incoming set at t+1 on the four y-probes of the two-axis opposite seed, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not replace M by O, do not replace exist-opposite by axis-cover, do not identify the report with 1-axis HOLDING M, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own incoming set at t+1 on the four y-probes of the two-axis opposite seed; displayed, not adopted"
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
incoming sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

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

## Named existential opposite from the own incoming set at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Mixed remains a set. Unique `L(q)` is not used
as the letter. Occupancy of sites is not used. Duplicate incoming steps
collapse in the set. The construction does not require `M(q,τ)` to be a
singleton. It does not sum `M(q,τ)`. It is not a unique lock-vector
leftover and not a sum leftover. It is not leftover of unique-L. It is
not leftover of axis-cover of `M` and `O`. New records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors do not enter
earliest `M`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names.

Reverse and face (displayed):

```text
reverse  <=>  some a in M(A,τ) and some b in M(B,τ) with a+b=(0,0,0)
face     <=>  some c in M(C,τ) and some d in M(D,τ) with c+d=(0,0,0)
```

If `M(A,τ)` or `M(B,τ)` is empty or `UNDEFINED`, reverse is `UNDEFINED`.
Else reverse fails if no such pair exists. If `M(C,τ)` or `M(D,τ)` is empty
or `UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`. Either side
`UNDEFINED` is `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks and `M` at `τ=t+1`

On this process the four y-probes form. Own incoming sets at each probe's
`τ=t+1` are frozen equal to `M` at `t`.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
```

`A` is a seed at tick 0. Mixed remains a set as a construction rule. On
this two-axis seed each of `M(A,τ)`, `M(B,τ)`, `M(C,τ)`, and `M(D,τ)` is
a singleton. Unique-L leftover would assign the same four letters. Here
uniqueness is not required and the object is still the set `M`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Those new neighbors enter later outgoing duals and do not enter earliest
`M`. Because `(0,1,1)` is a seed, it is not a new 6-NN of `A`.

Compare to 1-axis HOLDING M. Same y-probes, same perp-step incoming lock,
one opposite pair `{0,(0,1,0)}` with `+e_1/−e_1` only. On that 1-axis seed
the runner reports `t(A)=0`, `t(B)=2`, `t(C)=1`, `t(D)=3`,
`M(A,τ)={−e_1}`, `M(B,τ)={+e_1}`, `M(C,τ)={+e_2}`, mixed
`M(D,τ)={−e_2, +e_3, −e_3}`, reverse hold, and 1-axis face hold. The
two-axis seed advances `t(B)` from 2 to 1 and `t(D)` from 3 to 2, replaces
mixed `M(D,τ)` by `{−e_3}`, keeps reverse HOLD, and turns face from HOLD
to fail. Reverse HOLD uses a singleton `M(A,τ)`. Face fail uses singleton
`M(D,τ)={−e_3}` against `M(C,τ)={+e_2}`: `+e_2+(−e_3)` is not zero.

## Theorem 2 — reverse from exist-opposite of `M` at `τ`

Reverse holds if and only if there exist `a` in `M(A,τ)` and `b` in
`M(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty: `M(A,τ)={−e_1}` and
`M(B,τ)={+e_1}`, so `−e_1+(+e_1)=(0,0,0)`. Reverse HOLDs. Reverse HOLD
uses a singleton `M(A,τ)`.

Reverse exist-opposite at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Unique-L leftover also
reports reverse hold from unique `L(A)=−e_1` and `L(B)=+e_1`. Axis-cover
reverse HOLDs. Timed `O` exist-opposite reverse HOLDs. Those leftovers are
not this display. Reverse holds because the pair from `M(A,τ)` and
`M(B,τ)` is opposite.

Reverse holds.

## Theorem 3 — face from exist-opposite of `M` at `τ`

Face holds if and only if there exist `c` in `M(C,τ)` and `d` in `M(D,τ)`
with `c+d=(0,0,0)`. Both sets are nonempty: `M(C,τ)={+e_2}` and
`M(D,τ)={−e_3}`, so `+e_2+(−e_3)` is not zero. Face fails.

Face exist-opposite at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. Unique-L leftover also
reports face fail from unique `L(C)=+e_2` and `L(D)=−e_3`. Axis-cover face
fails. Timed `O` exist-opposite face HOLDs, which is not this face fail.
1-axis HOLDING M face HOLDs, which is the discriminator. Named-sign
lettering lost the axis. Signed-M exist-opposite does not HOLD both reverse
and face on this new member: reverse HOLDs and face fails.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set to be a singleton.
- It does not sum the own incoming set.
- It does not use occupancy of sites as the letter.
- It does not replace `M` by `O`.
- It does not replace exist-opposite of signed `M` by axis-cover of `M` and
  `O`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not reprint 1-axis HOLDING M reverse hold and face hold as this
  member.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint timed `O` exist-opposite as this incoming-set report.
- It does not reprint nmt2opp `M` frozen at `t` as this two-axis seed.
- It does not reprint mixed #7188 fail/fail as this member.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite-pair process, the own incoming sets at `t+1`, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| reverse HOLD uses a singleton `M(A,τ)` | Theorem 1; yes; `{−e_1}` |
| reverse from exist-opposite of `M` at `τ` | Theorem 2; `hold` |
| face from exist-opposite of `M` at `τ` | Theorem 3; `fail` |
| comparison to 1-axis HOLDING M | Theorem 1; 1-axis face hold, two-axis face fail |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of nm2ax axis-cover | not this display |
| leftover of timed `O` exist-opposite | not this display |
| leftover of nmsimopp exist-opposite of `M` and of `O` | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| second pair as formed child | refused; new seed |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own incoming set at `t+1` on the four y-probes of the two-axis opposite seed, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-incoming-set existential-opposite reverse/face report on this two-axis opposite seed. |
| V3 | Own incoming sets at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set at `t+1` and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not sum the lock set, does not replace `M` by `O`, does
not replace exist-opposite by axis-cover, does not identify this display
with 1-axis HOLDING M, and does not identify it with timed `O`
exist-opposite. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique-L leftover | require a singleton `{v}` else `UNDEFINED` | on this seed `M` is already singleton at each probe, so unique-L reverse hold and face fail agree by accident; the object is still the set `M` | ATTEMPTED |
| 1-axis HOLDING M | reuse reverse hold and face hold of #7167 own incoming `M` | 1-axis face HOLDs from mixed `M(D,τ)={−e_2, +e_3, −e_3}` against `{+e_2}`; two-axis face fails from `{−e_3}` against `{+e_2}` | ATTEMPTED |
| nm2ax axis-cover | score reverse/face from complementary unsigned axes of `M` and `O` | cover reverse hold and face fail agree on bits; cover is unsigned complementary axes of `M` versus `O` at one probe, not signed opposite across a pair | ATTEMPTED |
| timed `O` exist-opposite | score reverse/face inside `O(A,τ)` and `O(B,τ)` | timed `O` face HOLDs while signed-`M` face fails | ATTEMPTED |
| nmsimopp exist-opposite of `M` and of `O` | require both `M` and `O` exist-opposite | this display scores only own incoming `M` at `t+1` | ATTEMPTED |
| sum of the same incoming sets | replace `M` by the `Z^3` sum | the construction does not sum; sum of a singleton agrees by accident and is not the letter | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes the origin partner `+e_1` at `A`; own incoming `M(A,τ)` is `{−e_1}` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse hold and face fail | ATTEMPTED |
| nsopp leftover child | treat `(0,0,1)` and `(0,1,1)` as formed children | they are tick-0 seeds with `+e_2/−e_2`, not tick-1 children with incoming `+e_3` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of signed-`M`
exist-opposite with axis-cover, missing identification with 1-axis HOLDING
M, and missing Record identification of exist-opposite reverse are distinct
open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-axis opposite seed locks `+e_1/−e_1` and `+e_2/−e_2`,
perpendicular step rule, incoming-step lock, own incoming set from records
with tick `<= τ`, per-probe `τ=t+1`, mixed remains a set, existential
opposite, four y-probes with seed `A`, second pair is a new seed, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no six-neighbor lock union as the scored
object, no occupancy of sites as the letter, no named-sign reduction, no
singleton leftover as the object, no sum leftover, no unique-L leftover, no
axis-cover leftover, no timed-`O` leftover, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
exist-opposite reverse-hold and face-fail reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Signed-`M` exist-opposite HOLDs on this new member because
cover reverse HOLDs; unique-L already gives the same four letters; 1-axis
HOLDING M already answered exist-opposite with reverse hold and face hold;
axis-cover reverse hold and face fail already are the bits; timed `O`
exist-opposite already HOLDs reverse; and empty `M` should be `UNDEFINED`
like unformed.

**Answer:** Cover HOLD is unsigned complementary occupation of `{e_1,e_2,e_3}`
by `Axis(M)` and `Axis(O)` at one probe. Exist-opposite is a signed pair
across two probes. They agree on reverse hold and face fail here by
accident of the letters, not by identity of the objects. Unique-L agrees
because this seed happens to have singleton `M` at each of `A,B,C,D`; mixed
remains a set as the construction, and uniqueness is not required. 1-axis
HOLDING M face HOLDs from mixed `M(D,τ)={−e_2, +e_3, −e_3}` against
`{+e_2}`; two-axis face fails from `{−e_3}` against `{+e_2}`. That is the
discriminator. Timed `O` face HOLDs, so outgoing exist-opposite is not this
incoming-set report. Empty `M` is `UNDEFINED` on a comparison side; unformed
at `τ` is `UNDEFINED`. Reverse exist-opposite HOLDs. Face fails. Signed-`M`
exist-opposite does not HOLD both bits on this new member.

### N8 — cross-cycle echo

1-axis HOLDING M reported reverse hold and face hold from own incoming `M`
on these same y-probes. nm2ax reported axis-cover reverse hold and face
fail. nmsimopp reported `M` and `O` together at `τ=t+1`. This note is not
those displays: it reports exist-opposite of signed own incoming `M` at
`τ=t+1` on the two-axis opposite seed, reverse hold, and face fail.
Discriminator versus 1-axis HOLDING M is face fail.

**Gate disposition:** PASS for the own-incoming-set existential-opposite
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals the sum of the lock set,” “the predicate
equals axis-cover,” “the predicate equals timed `O` exist-opposite,” “the
predicate equals 1-axis HOLDING M,” “bits are Admissibility,” “reverse
exist-opposite fails,” or “face exist-opposite holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set from the record prefix at that probe's `t+1`, scores reverse and face by
existential opposite, lists new records in `B_3(0)` between `t` and `t+1`
that meet a probe's six-neighbors, compares the same observables on the
1-axis HOLDING M seed, and checks Theorems 1--3. It also checks that reverse
HOLDs and face fails, that mixed remains a set, that unique-L leftover is a
different object even when letters agree, that axis-cover leftover is a
different object, that timed `O` exist-opposite face HOLDs, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that the second pair is a new seed, and
that the display is not 1-axis HOLDING M. No runner cache is written.
