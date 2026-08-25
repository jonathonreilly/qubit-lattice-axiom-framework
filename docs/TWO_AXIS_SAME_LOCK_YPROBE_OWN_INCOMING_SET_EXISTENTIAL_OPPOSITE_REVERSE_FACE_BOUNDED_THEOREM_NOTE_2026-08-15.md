---
claim_id: two_axis_same_lock_yprobe_own_incoming_set_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the own incoming *set* at t+1 on the four y-probes of the two-axis same-lock seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py
---

# Own Incoming Set Existential Opposite Reverse And Face On Four Two-Axis Same-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own incoming *set* `M(q,τ)` at
each probe's `τ=t+1` on the four y-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick `<= τ`.
Seeds are a singleton seed letter. Mixed remains a set. Unformed at `τ` is
`UNDEFINED`. Reverse HOLDs if and only if some lock in `M(A,τ)` is the
vector opposite of some lock in `M(B,τ)`. Face HOLDs if and only if some
lock in `M(C,τ)` is the vector opposite of some lock in `M(D,τ)`. Empty or
`UNDEFINED` on either side is `UNDEFINED`; nonempty with no opposite pair
fails. Unique `L` is not the object. This display does not use occupancy of
sites as the letter: occupancy of sites is not used. This
is not named-sign lettering. This is not a unique lock-vector leftover and
not a sum leftover. This is not leftover of unique-L. This is not leftover
of axis-cover of `M` and `O` at `t+1`. This is not leftover of exist-opposite
of `O`. This is not leftover of 1-axis same-lock signed-M. This is not
leftover of two-axis opposite signed-M. Neither pair is opposite.
Uniqueness is not required. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own incoming sets at the per-probe cut `τ=t+1`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object: report `M`. A `Z^3` sum of
those locks is a different readout and is not used. The construction does
not sum. Occupancy of sites is not used. A six-neighbor star is not the
letter. Axis-cover of `M` and `O` is a different readout and is not used as
this reverse. Existential opposite of outgoing `O` is a different readout.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M(q,τ) as the probe's own incoming set of earliest NN steps at t+1 on the four y-probes of the two-axis same-lock seed, mixed remains a set, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_own_incoming_set_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from the own incoming set at t+1 on the four y-probes of the two-axis same-lock seed, compare to two-axis opposite signed-M, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not replace M by O, do not replace signed-M by axis-cover, do not replace this member by two-axis opposite, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own incoming set at t+1 on the four y-probes of the two-axis same-lock seed; displayed, not adopted"
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

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed child
of the first pair, and neither pair is opposite. This seed is not the 1-axis
same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone. This seed is
not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is
not the y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.
This seed is not the x-axis same-lock seed `{0,(1,0,0)}` with `+e_2/+e_2`.

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
the singleton seed letter. Duplicate incoming steps collapse in the set.
The construction does not require `M` to be a singleton. It does not sum
`M`. Occupancy of sites is not used. It does not wait for a global later T.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in M(A,τ) and some b in M(B,τ) with a+b=(0,0,0)
face     <=>  some c in M(C,τ) and some d in M(D,τ) with c+d=(0,0,0)
```

If `M(A,τ)` or `M(B,τ)` is empty or `UNDEFINED`, reverse is `UNDEFINED`.
Else reverse fails if no such pair exists. If `M(C,τ)` or `M(D,τ)` is empty
or `UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks and `M` at `τ=t+1`

On this process the four y-probes form. Compare to two-axis opposite
signed-M: the four-site seed with locks `+e_1/−e_1` and `+e_2/−e_2` reports
`M(A,τ)={−e_1}` and `M(B,τ)={+e_1}`, so signed-M reverse HOLDs, while this
same-lock member has `M(A,τ)={+e_1}` and `M(B,τ)={+e_1}`, so reverse fails.
Compare to 1-axis same-lock signed-M: the two-site seed `{0,(0,1,0)}` with
locks `+e_1/+e_1` reports reverse fail and face hold, with `t(D)=3` and
mixed `M(D,τ)={−e_2,+e_3,−e_3}`. This two-axis same-lock member adds a
second same-lock pair as a new seed. Face fails because `M(D,τ)={−e_3}`
has no opposite of `M(C,τ)={+e_2}`.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
```

`A` is a seed at tick 0. Earliest `M` is frozen from `t` to `τ=t+1` at each
of the four probes: later records in the prefix do not add a new earliest
incoming step. Uniqueness is not required. On this member each of the four
scored sets happens to be a singleton. Mixed remains a set on the process:
1-axis same-lock `M(D,τ)` is mixed. That mix is not this member.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `M(A,τ)` and `b` in
`M(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty:
`M(A,τ)={+e_1}` and `M(B,τ)={+e_1}`, so `+e_1+(+e_1)=(2,0,0)≠(0,0,0)`.
No opposite pair exists. Reverse fails.

Reverse exist-opposite at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Two-axis opposite
signed-M reverse HOLDs from `{−e_1}` against `{+e_1}`. Axis-cover reverse
of `M` and `O` HOLDs on this same member. Exist-opposite reverse of `O`
HOLDs. Those leftovers are not this display. Signed-M reverse fails
because neither pair of the two-axis same-lock seed is opposite.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `M(C,τ)` and `d` in `M(D,τ)`
with `c+d=(0,0,0)`. Both sets are nonempty: `M(C,τ)={+e_2}` and
`M(D,τ)={−e_3}`, so `+e_2+(−e_3)=(0,1,−1)≠(0,0,0)`. No opposite pair
exists. Face fails. Face is not `UNDEFINED`.

Face exist-opposite at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. 1-axis same-lock
signed-M face HOLDs from mixed `M(D,τ)={−e_2,+e_3,−e_3}` against
`M(C,τ)={+e_2}`. Two-axis opposite signed-M face also fails from
`M(D,τ)={−e_3}`. Axis-cover face of `M` and `O` fails on this member.
Exist-opposite face of `O` HOLDs. Those leftovers are not this display.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set to be a singleton.
- It does not sum the own incoming set.
- It does not replace `M` by `O`.
- It does not replace signed-M exist-opposite by axis-cover of `M` and `O`.
- It does not replace signed-M by leftover of unique-L.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint 1-axis same-lock signed-M reverse-fail face-hold as
  this member.
- It does not reprint two-axis opposite signed-M reverse-hold face-fail.
- It does not reprint nsopp exist-opposite HOLD.
- It does not reprint x-axis same-lock y-probe signed-M.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis same-lock four-site process, own incoming sets at `t+1`, and the
reverse/face bits from existential opposite of signed `M` are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| reverse from exist-opposite of `M` at `τ` | Theorem 2; `fail` |
| face from exist-opposite of `M` at `τ` | Theorem 3; `fail` |
| compare to two-axis opposite signed-M | Theorem 1; opposite reverse HOLDs from `{−e_1}` against `{+e_1}`; this member reverse-fails |
| compare to 1-axis same-lock signed-M | Theorem 1; 1-axis reverse-fails and face-holds with mixed `M(D)`; this member face-fails |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of axis-cover of `M` and `O` | not this display |
| leftover of exist-opposite of `O` | not this display |
| leftover of 1-axis same-lock signed-M | not this display |
| leftover of two-axis opposite signed-M | not this display |
| leftover of nsopp exist-opposite HOLD | not this display |
| leftover of x-axis same-lock y-probe signed-M | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own incoming set at `t+1` on the four y-probes of the two-axis same-lock seed, compared to two-axis opposite signed-M, and reverse/face from existential opposite. |
| V2 | Current main has no landed own-incoming-set existential-opposite reverse/face report on these four two-axis same-lock y-probes. |
| V3 | Own incoming sets at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set at `t+1` and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace signed-M by axis-cover, does not replace
signed-M by exist-opposite of `O`, and does not identify this display with
1-axis same-lock signed-M or with two-axis opposite. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| two-axis opposite signed-M | reuse seed `+e_1/−e_1` and `+e_2/−e_2` | `M(A)` there is `{−e_1}` and reverse HOLDs; here `M(A)={+e_1}` and reverse fails | ATTEMPTED |
| 1-axis same-lock signed-M | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis face HOLDs at mixed `M(D,τ)` with `t(D)=3`; here `t(D)=2`, `M(D)={−e_3}`, face fails | ATTEMPTED |
| axis-cover of `M` and `O` | score complementary unsigned axes | cover reverse HOLDs and cover face fails on this member; signed-M reverse fails | ATTEMPTED |
| exist-opposite of `O` | reuse signed reverse and face of `O` | O exist-opposite reverse hold and face hold; signed-M reverse fail and face fail | ATTEMPTED |
| unique-L leftover | replace mixed sets by a singleton or `UNDEFINED` | unique-L happens to match because these four `M` are singletons; mixed remains a set on 1-axis `D` | ATTEMPTED |
| sum of a set | replace `M` by a `Z^3` sum | the construction does not sum; sum of a singleton is that letter, not the set object | ATTEMPTED |
| nsopp exist-opposite HOLD | reuse opposite `+e_1/−e_1` y-probes | that leftover has M exist-opposite reverse hold and face hold; this member fails both | ATTEMPTED |
| x-axis same-lock y-probe | reuse seed `{0,(1,0,0)}` with `+e_2/+e_2` | different seed axis; `M(A)` there is not `{+e_1}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores exist-opposite of own incoming at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member is two-axis same-lock with singleton `M(D)={−e_3}` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of signed-M with
axis-cover, missing identification of this member with two-axis opposite
signed-M, missing identification of this member with 1-axis same-lock
signed-M, and missing Record identification of exist-opposite reverse are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed, perpendicular step
rule, incoming-step lock, own incoming set from records with tick `<= τ`,
per-probe `τ=t+1`, existential opposite, four y-probes with seed `A`, and
mixed remains a set are declared. No uniqueness of incoming locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
exist-opposite reverse fail and face fail reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets plus reverse/face as hold, fail, or UNDEFINED | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Two-axis same-lock signed-M is still reverse HOLD because
two-axis opposite HOLDs reverse and same-lock is only a sign flip; cover
already HOLDs reverse on this member; 1-axis same-lock already answered
signed-M; unique-L already matches the singletons; and exist-opposite of
`O` already answered reverse/face.

**Answer:** Reverse fails because `M(A,τ)={+e_1}` and `M(B,τ)={+e_1}` are
not opposite. Two-axis opposite has `M(A,τ)={−e_1}` against
`M(B,τ)={+e_1}` and reverse HOLDs. Axis-cover reverse HOLDs on this
member while signed-M reverse fails. 1-axis same-lock reverse-fails and
face-holds from mixed `M(D,τ)`; this member face-fails from singleton
`M(D,τ)={−e_3}`. Unique-L matching singletons is not the object: mixed
remains a set. Exist-opposite of `O` reverse-holds and face-holds, while
signed-M reverse-fails and face-fails. Neither pair of this seed is
opposite.

### N8 — cross-cycle echo

1-axis same-lock signed-M on `{0,(0,1,0)}` with `+e_1/+e_1` reports reverse
fail and face hold with `t(D)=3`. Two-axis opposite reports reverse hold
and face fail with opposite seed letters. Axis-cover of `M` and `O` on this
same two-axis same-lock seed reports reverse hold and face fail. This note
is not those displays: it reports own incoming sets at `τ=t+1` on two
disjoint same-lock pairs, reverse fail, and face fail. Signed-M
exist-opposite is not leftover of two-axis opposite and not leftover of
axis-cover.

**Gate disposition:** PASS for the own-incoming-set existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “the predicate equals axis-cover
of `M` and `O`,” “the predicate equals exist-opposite of `O`,” “the
predicate equals 1-axis same-lock signed-M,” “the predicate equals two-axis
opposite,” “bits are Admissibility,” “reverse exist-opposite HOLDs,” or
“face exist-opposite HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set from the record prefix at that probe's `t+1`, scores reverse and face
by existential opposite, compares to two-axis opposite signed-M and to
1-axis same-lock signed-M, and checks Theorems 1--3. It also checks that
signed-M reverse fails and face fails, that axis-cover reverse is a
different reverse, that exist-opposite of `O` is a different object, that
mixed sets remain sets, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not the two-tick lock-count clock composition. No
runner cache is written.
