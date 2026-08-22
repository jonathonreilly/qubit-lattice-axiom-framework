---
claim_id: opposite_lock_yprobe_outgoing_axis_agreement_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Outgoing-axis agreement of O at t+1 on the four #7208 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_outgoing_axis_agreement_tplus1_reverse_face_2026_08_15.py
---

# Outgoing-Axis Agreement Of Own-Outgoing At t+1 Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** outgoing-axis agreement of the outgoing dual `O` at each probe's
`τ=t+1`, and reverse/face from that agreement, on the four nsmopp #7208
y-probes in `B_3(0)={n:n·n<=9}`. Same process as nsopp #7093. Dual of
incoming-axis agreement of `M`. Let `t(q)` be the formation tick of probe
`q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i | some ±e_i
in S}`. Empty Axis fails, not `UNDEFINED`. Reverse HOLDs if and only if
`Axis(O)` at `A` equals `Axis(O)` at `B` and both are nonempty. Face HOLDs
if and only if `Axis(O)` at `C` equals `Axis(O)` at `D` and both are
nonempty. This is not leftover of incoming-axis agreement of `M`. This is
not leftover of leftover-of-O. This is not leftover of leftover-empty.
This is not leftover of exist-opposite of signed `O`. This is not leftover
of axis-cover of `M` and `O`. This is not leftover of nmot2opp two-tick
composition. This is not leftover of nmoutopp untimed eventual-`O`. This
is not leftover of mixed #7188 fail/fail. Uniqueness is not required.
Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1. Occupancy of sites is not used. The
construction does not use occupancy. The construction does not use a
six-neighbor star. This is not named-sign lettering. This is not a unique
lock-vector leftover and not a sum leftover. This is not leftover of
unique-L.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_outgoing_axis_agreement_tplus1_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_outgoing_axis_agreement_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Reverse
and face are scored on equality of nonempty `Axis(O)` at the paired probes.
Named signs `{+,−}` are a coarser readout and are not used. A singleton
unique lock letter is a different readout and is not used as the object.
Existential opposite of signed locks is a different readout and is not used
as the reverse. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. Incoming-axis agreement of `M` is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter. This display is not an occupancy-kernel
inner product.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of Axis(O) at t+1 on the four #7208 y-probes, reverse hold from nonempty equal Axis(O) at A and B, face fail from nonempty unequal Axis(O) at C and D; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_outgoing_axis_agreement_tplus1_reverse_face
target_blocker_text: "display outgoing-axis agreement of O at t+1 on the four #7208 y-probes, and reverse/face from that, dual of incoming-axis agreement of M"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep outgoing-axis agreement of O at t+1 displayed; do not write agreement into Admissibility, do not reduce to leftover of incoming-axis agreement of M, do not reduce to leftover-of-O, do not replace agreement by exist-opposite of signed O, do not replace agreement by leftover-empty fail, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for outgoing-axis agreement of O at t+1 on the four #7208 y-probes and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose outgoing
axis is scored:

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

## Named outgoing-axis agreement of `O` at `τ=t+1`

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
not require `O` to be a singleton. It does not sum the set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Empty Axis fails, not `UNDEFINED`. Unformed is `UNDEFINED`. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis.

Reverse outgoing-axis agreement holds if and only if `Axis(O)` at `A`
equals `Axis(O)` at `B` as sets and both are nonempty. Face outgoing-axis
agreement holds if and only if `Axis(O)` at `C` equals `Axis(O)` at `D` as
sets and both are nonempty. Either side `UNDEFINED` is `UNDEFINED`. Empty
Axis on either side fails, not `UNDEFINED`. Else if both sides are nonempty
and equal, reverse or face HOLDs. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
outgoing-axis agreement is refused: leftover-empty fail scores empty leftover
of `M` union `O` as fail. Identifying leftover-of-O with `Axis(O)` is
refused: leftover-of-O is `{e_1,e_2,e_3}` minus `Axis(O)`. Identifying
incoming-axis agreement of `M` with this dual is refused: `Axis(M)` is not
`Axis(O)`. Identifying exist-opposite of signed `O` with this reverse is
refused: exist-opposite scores a pair that sums to zero, not unsigned axis
equality.

## Theorem 1 — ticks, `O`, and `Axis(O)` at `τ=t+1`

On this process the four y-probes form. Compare to incoming-axis agreement
of `M`: that leftover reports `Axis(M)(A,τ)={e_1}=Axis(M)(B,τ)` and
`Axis(M)(C,τ)={e_2}` unequal to `Axis(M)(D,τ)={e_2,e_3}`. This display
reads the outgoing dual at the same cut:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
O(A, τ) = {+e_2, +e_3, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
Axis(O)(A, τ) = {e_2, e_3}
Axis(O)(B, τ) = {e_2, e_3}
Axis(O)(C, τ) = {e_1, e_3}
Axis(O)(D, τ) = {e_1}
```

`A` is a seed at tick 0. Mixed remains a set: `O(A,τ)` has three outgoing
steps and `O(C,τ)` has four. Unique letters would assign `UNDEFINED` at
mixed probes. Here uniqueness is not required. `Axis(O)` at `A` equals
`Axis(O)` at `B` and both are nonempty. `Axis(O)` at `C` is nonempty and
unequal to nonempty `Axis(O)` at `D`. O is not M. Incoming `Axis(M)` at
`A` is `{e_1}`, not `{e_2, e_3}`. Leftover of `O` at `A` is `{e_1}`, the
complement of `Axis(O)`, not `Axis(O)`.

On this process complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)` makes leftover of `M` equal `Axis(O)` as sets. That equality
is a fact of complementary cover, not the object: the letter is `Axis(O)`,
read from the outgoing dual, not leftover of `M`.

At formation tick `t`, `O(A,t)` does not yet include the three new
six-neighbors that form at `t+1`, so `Axis(O)` at `t` is not the scored
cut. The scored cut is `τ=t+1`.

## Theorem 2 — reverse from outgoing-axis agreement at `τ`

Reverse outgoing-axis agreement holds if and only if `Axis(O)` at `A`
equals `Axis(O)` at `B` and both are nonempty. Both axes are `{e_2, e_3}`.
Reverse HOLDs.

Reverse: hold

Both sides are defined and nonempty, so this is not `UNDEFINED` and not
`fail`. Incoming-axis agreement of `M` also HOLDs reverse, but from
`{e_1}` at `A` and at `B`, not from `{e_2, e_3}`. Leftover of `O` HOLDs
reverse from `{e_1}` at `A` and at `B`, the complement, not `Axis(O)`.
Exist-opposite reverse of signed `O` HOLDs from opposite signs inside
`O(A)` and `O(B)`. Leftover-empty reverse fails because leftover of the
union is empty. Those leftovers are not this display. Reverse at formation
tick `t` fails because `Axis(O)` at `A` is then empty. Reverse at `t+1`
HOLDs.

Reverse holds.

## Theorem 3 — face from outgoing-axis agreement at `τ`

Face outgoing-axis agreement holds if and only if `Axis(O)` at `C` equals
`Axis(O)` at `D` and both are nonempty. `Axis(O)(C,τ)={e_1, e_3}` and
`Axis(O)(D,τ)={e_1}` are both nonempty and unequal. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. Incoming-axis
agreement of `M` also fails face, but from `{e_2}` versus `{e_2, e_3}`,
not from `{e_1, e_3}` versus `{e_1}`. Leftover of `O` fails face from
`{e_2}` versus `{e_2, e_3}`. Exist-opposite face of signed `O` HOLDs from
`+e_1` in `O(C)` against `−e_1` in `O(D)`. Axis-cover face HOLDs from
complementary occupation at `C` and at `D`. Leftover-empty face fails from
empty leftover. Face fail of unsigned outgoing-axis agreement while
exist-opposite of signed `O` HOLDs is the discriminator against signed
opposite.

Empty Axis does not make reverse `UNDEFINED`. Empty Axis fails. Face
fails from nonempty unequal axes.

Face fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum the outgoing set.
- It does not replace `O` by `M`.
- It does not replace `Axis(O)` by leftover of `O`.
- It does not replace `Axis(O)` by leftover of `M`.
- It does not replace agreement by leftover-empty fail.
- It does not replace agreement by existential opposite of signed locks.
- It does not replace agreement by axis-cover of `M` and `O`.
- It does not replace agreement by incoming-axis agreement of `M`.
- It does not replace `O` by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
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
opposite-lock two-site process, outgoing-axis agreement of `O` at `t+1`, and
the reverse/face bits from that agreement are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(O)` at `τ` | Theorem 1; `{e_2,e_3}`, `{e_2,e_3}`, `{e_1,e_3}`, `{e_1}` |
| reverse from outgoing-axis agreement at `τ` | Theorem 2; `hold` |
| face from outgoing-axis agreement at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of incoming-axis agreement of `M` | not this display |
| leftover of leftover-of-O | not this display |
| leftover of leftover-empty | not this display |
| leftover of exist-opposite of signed `O` | not this display |
| leftover of axis-cover of `M` and `O` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| outgoing-axis agreement as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: outgoing-axis agreement of `O` at `t+1` on the four #7208 y-probes, and reverse/face from that. |
| V2 | Current main has no landed outgoing-axis-agreement reverse/face of timed `O` on these four #7208 y-probes. |
| V3 | Axis reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axes of own outgoing at the `t+1` cut and scores reverse/face on nonempty equality. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace agreement by leftover-empty fail, does not
replace agreement by leftover of `O`, does not replace agreement by
incoming-axis agreement of `M`, and does not replace agreement by
exist-opposite of signed `O`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| incoming-axis agreement of `M` | score reverse/face from `Axis(M)` | reverse would hold and face would fail from `{e_1}` versus `{e_2}`/`{e_2,e_3}`, not from `{e_2,e_3}` versus `{e_1,e_3}`/`{e_1}` | ATTEMPTED |
| leftover of `O` | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and `B` is `{e_1}`, not `{e_2,e_3}` | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at each probe, leftover reverse and face fail, while outgoing-axis reverse HOLDs | ATTEMPTED |
| exist-opposite of signed `O` | score a pair in `O` that sums to zero | exist-opposite reverse HOLDs and face HOLDs, while unsigned axis face fails | ATTEMPTED |
| axis-cover of `M` and `O` | score complementary occupation of three axes | cover HOLDs reverse and face; this display fails face | ATTEMPTED |
| leftover of `M` | score `{e_1,e_2,e_3}` minus `Axis(M)` | on this process leftover of `M` equals `Axis(O)` as sets because of complementary cover; the letter is still `Axis(O)`, read from `O`, not leftover of `M` | ATTEMPTED |
| unique letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(A,τ)` and mixed `O(C,τ)` remain sets; reverse still HOLDs and face still fails | ATTEMPTED |
| formation-tick `O` | score `Axis(O)` at `t` instead of `t+1` | `Axis(O)` at `A` is empty at `t`, so reverse at `t` fails while reverse at `t+1` HOLDs | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `τ` | that leftover includes `e_1` at `A` from the origin partner; `Axis(O)` at `A` is `{e_2,e_3}` | ATTEMPTED |
| nmot2opp two-tick composition | score match of reverse/face bits of `O` at `t` versus `t+1` | different member; this display scores unsigned axis agreement at `t+1` only | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed reverse-fail face-fail | different process; this member reports reverse hold and face fail | ATTEMPTED |
| sum of a set | replace `Axis(O)` by a `Z^3` sum | the construction does not sum; sum of mixed `O(A,τ)` cancels to `+e_2` while `Axis(O)` stays `{e_2,e_3}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by outgoing-axis agreement | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `Axis(O)` with leftover
of `M`, missing identification of agreement with leftover-empty fail, missing
identification of agreement with exist-opposite of signed `O`, and missing
Record identification of outgoing-axis reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, reverse/face as nonempty equality of
`Axis(O)`, empty Axis fails not `UNDEFINED`, four y-probes with seed `A`,
and mixed remains a set are declared. No uniqueness of outgoing locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` occupied by `O` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `Axis(O)` reports, reverse/face from nonempty equality | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for outgoing-axis reverse/face,
a formation-rate rule, and a physical selector among unsigned outgoing axes.
None is taken here.

### N7 — hostile steelman

**Steelman:** `Axis(O)` is leftover of `M` because complementary cover makes
them equal as sets, so this is leftover-of-`M` agreement; leftover of `O`
is incoming-axis agreement of `M`; exist-opposite of signed `O` already
answered reverse; empty `O` should be `UNDEFINED` like unformed; and face
fail is only leftover-empty fail.

**Answer:** Complementary cover on this process makes leftover of `M` equal
`Axis(O)` as sets. The object is still `Axis(O)`: unsigned axes occupied by
the outgoing dual at `t+1`. Leftover of `M` is defined from `M`. Leftover of
`O` at `A` is `{e_1}`, not `{e_2,e_3}`. Exist-opposite of signed `O` HOLDs
face while unsigned axis face fails. Empty `O` is empty, not `UNDEFINED`;
empty Axis fails. Leftover-empty reverse fails; outgoing-axis reverse HOLDs.
The bits remain displayed. Outgoing-lock uniqueness is not required.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M`.
Incoming-axis agreement of `M` at `t+1` reports reverse hold from `{e_1}`
and face fail from `{e_2}` versus `{e_2,e_3}`. Leftover of `O` reports
reverse hold from `{e_1}` and face fail from `{e_2}` versus `{e_2,e_3}`.
Exist-opposite of signed `O` reports reverse hold and face hold. Axis-cover
of `M` and `O` reports reverse hold and face hold. Leftover-empty reports
reverse fail and face fail. This note is not those displays: it reports
`Axis(O)` at `τ=t+1` as `{e_2,e_3}`, `{e_2,e_3}`, `{e_1,e_3}`, `{e_1}`,
reverse hold, and face fail.

**Gate disposition:** PASS for the outgoing-axis-agreement `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named sign,”
“the predicate equals leftover of `O`,” “the predicate equals incoming-axis
agreement of `M`,” “the predicate equals exist-opposite of signed `O`,”
“bits are Admissibility,” “reverse fails,” or “face HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's outgoing dual at `τ=t+1`, forms
`Axis(O)`, scores reverse and face by nonempty equality of those axis sets,
and checks Theorems 1--3. It also checks that the construction is not
named-sign lettering, that mixed remains a set, that the construction does
not sum, that occupancy of sites is not used, that a formation member from
already-recorded six-neighbor locks is not attached, that the sets are not
leftover of incoming-axis agreement, that the sets are not leftover of
leftover-of-O, that the sets are not leftover of leftover-empty, and that
the reverse is not leftover of exist-opposite of signed `O`. No runner
cache is written.
