---
claim_id: y_symmetric_three_site_incoming_axis_agreement_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Incoming-axis agreement of M at t+1 on the four #7211 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py
---

# Incoming-Axis Agreement Of M At t+1 Reverse And Face On Four #7211 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** incoming-axis agreement of earliest incoming set `M` at each
probe's `τ=t+1`, and reverse/face from that agreement, on the four nmsyop
#7211 y-probes in `B_3(0)={n:n·n<=9}`. Same process as nsyopp #7132. Let
`t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is
the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds are a singleton seed letter. Unformed at
`τ` is `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Empty Axis is empty, not `UNDEFINED`.
Reverse HOLDs if and only if `Axis(M)(A)` equals `Axis(M)(B)` as sets and
both are nonempty. Face HOLDs if and only if `Axis(M)(C)` equals
`Axis(M)(D)` as sets and both are nonempty. Empty Axis fails, and is not
`UNDEFINED`. This is transfer of nmmaxis incoming-axis agreement onto
HOLDING `M` #7211. This is not leftover of #7211 exist-opposite of signed
`M`. This is not leftover of leftover-of-`M` alone. This is not leftover
of leftover of `M` and outgoing dual together. This is not leftover of
two-site incoming-axis agreement #7167 as this member. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Axis is the unsigned lattice direction of a signed lock. Reverse and
face are scored on equality of nonempty unsigned incoming-axis sets at
`τ=t+1`. Named signs `{+,−}` are a coarser readout and are not used. A
singleton unique lock letter is a different readout and is not used as the
object. Existential opposite of signed locks is a different readout and is
not used as incoming-axis agreement. Leftover of `{e_1,e_2,e_3}` minus
`Axis(M)` is a different readout and is not used. A `Z^3` sum of those
locks is a different readout and is not used. Occupancy of sites is not
used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of Axis(M) at t+1 on the four #7211 y-probes, reverse hold from equal nonempty Axis(M) at A and B, face fail from unequal nonempty Axis(M) at C and D; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_incoming_axis_agreement_tplus1_reverse_face
target_blocker_text: "display incoming-axis agreement of M at t+1 on the four #7211 y-probes, and reverse/face from that, HOLD iff Axis(M) sets equal and nonempty"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep Axis(M) at t+1 displayed; do not write incoming-axis agreement into Admissibility, do not reduce to exist-opposite of signed M, do not replace Axis(M) by leftover of M alone, do not replace Axis(M) by leftover of M and outgoing dual, do not require a unique lock vector, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for Axis(M) at t+1 on the four #7211 y-probes and reverse/face from incoming-axis agreement; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose incoming
axis of `M` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nmsyop #7211.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named incoming-axis agreement of `M` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Duplicate incoming steps collapse in the set.
The construction does not require `M(q,τ)` to be a singleton. It does not
sum `M`. Occupancy of sites is not used.

Unsigned axis of a defined lock set:

```text
Axis(M) = { e_i | some ±e_i in M }.
```

If `M` is `UNDEFINED`, then `Axis(M)` is `UNDEFINED`. Empty `M` yields empty
Axis, which fails reverse or face, and is not `UNDEFINED`. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis.

Reverse incoming-axis agreement holds if and only if `Axis(M)(A)` and
`Axis(M)(B)` are defined, equal as sets, and nonempty. Face incoming-axis
agreement holds if and only if `Axis(M)(C)` and `Axis(M)(D)` are defined,
equal as sets, and nonempty. Either side `UNDEFINED` is `UNDEFINED`. Empty
Axis fails. Nonempty unequal axis sets fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying existential opposite of
signed locks with incoming-axis agreement is refused: exist-opposite HOLDs
from `+e_2` against `−e_2` at `C` and `D` while `Axis(M)(C)={e_2}` is not
equal to `Axis(M)(D)={e_2, e_3}`. Identifying leftover of `M` alone with
incoming-axis agreement is refused: leftover of `M` at `A` is `{e_2,e_3}`,
the complement of `Axis(M)(A)={e_1}`.

Admissibility is not edited. Incoming-axis agreement is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks, `M`, and `Axis(M)` at `τ=t+1`

On this process the four y-probes form. Compare to nmsyop #7211: that leftover
reports own incoming `M` with exist-opposite reverse hold and face hold.
This display reads unsigned incoming axis of timed `M` at `τ=t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2, +e_3, −e_3}
Axis(M)(A, τ) = {e_1}
Axis(M)(B, τ) = {e_1}
Axis(M)(C, τ) = {e_2}
Axis(M)(D, τ) = {e_2, e_3}
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three earliest
incoming steps `−e_2`, `+e_3`, and `−e_3`, so
`Axis(M)(D,τ)={e_2, e_3}` is a two-element axis set, not `UNDEFINED`. Unique
letters would assign `UNDEFINED` at mixed `D` and would leave face
`UNDEFINED`. Here uniqueness is not required. `M` at `τ=t+1` equals `M` at
`t`: earliest incoming is frozen. New records in `B_3(0)` between `t` and
`t+1` that meet a probe's six-neighbors do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Investment nmsyop #7211: exist-opposite of signed `M` HOLDs reverse and
face. Letter-opposite on one axis occupies that axis. Incoming-axis
agreement is unsigned set equality of occupied axes. Leftover of `M` alone
at `A` and `B` is `{e_2,e_3}`, nonempty and equal; that complement is not
`Axis(M)`. Two-site incoming-axis agreement on #7167 reports the same four
`Axis(M)` sets on these y-probes, but its seed omits the y-mirror, so
`(0,-1,0)` forms at tick 1 rather than tick 0. Same four axis sets are not
the same member.

## Theorem 2 — reverse from incoming-axis agreement at `τ`

Reverse incoming-axis agreement holds if and only if `Axis(M)(A)` and
`Axis(M)(B)` are defined, equal as sets, and nonempty. Both axis sets are
`{e_1}`. Reverse holds.

Reverse incoming-axis at τ: hold

This is not `fail` and not `UNDEFINED`. Reverse holds because
`Axis(M)(A)=Axis(M)(B)={e_1}` is nonempty. Exist-opposite reverse of signed
`M` also holds, from `−e_1` against `+e_1`, but that leftover scores a
signed opposite pair, not unsigned axis-set equality. Leftover-of-`M`
reverse would hold because leftover of `M` at `A` and at `B` is `{e_2,e_3}`;
that complement is not this letter. Leftover of `M` and outgoing dual
together is empty at `A` and at `B`, so that leftover reverse fails. Unique
already-recorded neighbor letters on this seed report reverse fails.
Transfer of nmmaxis incoming-axis agreement onto this HOLDING `M` member
reports reverse hold from singleton `Axis(M)(A)={e_1}`.

Reverse holds.

## Theorem 3 — face from incoming-axis agreement at `τ`

Face incoming-axis agreement holds if and only if `Axis(M)(C)` and
`Axis(M)(D)` are defined, equal as sets, and nonempty. Both axis sets are
defined and nonempty: `Axis(M)(C)={e_2}` and `Axis(M)(D)={e_2, e_3}`. Those
sets are unequal. Face fails.

Face incoming-axis at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `UNDEFINED`. Face fails. Unique-L leftover reports face
`UNDEFINED` from mixed `D`. Exist-opposite face of signed `M` holds from
`+e_2` against `−e_2` inside mixed `M(D,τ)`. Hold of exist-opposite face
while incoming-axis face fails is the discriminator against #7211
exist-opposite of `M`. Leftover-of-`M` face also fails, from `{e_1,e_3}`
against `{e_1}`, but those leftover sets are not `Axis(M)`. Mixed stays a
set: `e_3` in `Axis(M)(D)` is kept, and that extra axis is why face fails.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `Axis(M)` to be a singleton.
- It does not sum the incoming set.
- It does not replace `Axis(M)` by leftover of `M` alone.
- It does not replace `Axis(M)` by leftover of `M` and outgoing dual.
- It does not replace incoming-axis agreement by existential opposite of
  signed locks.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint #7211 exist-opposite of `M`.
- It does not reprint two-site incoming-axis agreement #7167 as this member.
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
y-symmetric three-site process, `Axis(M)` at `t+1`, and the reverse/face bits
from incoming-axis agreement are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsyopp #7132 y-symmetric three-site seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t`; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` |
| `Axis(M)` at `τ` | Theorem 1; `{e_1}`, `{e_1}`, `{e_2}`, `{e_2, e_3}` |
| reverse from incoming-axis agreement at `τ` | Theorem 2; `hold` |
| face from incoming-axis agreement at `τ` | Theorem 3; `fail` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of #7211 exist-opposite of `M` | not this display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover of `M` and outgoing dual | not this display |
| leftover of two-site incoming-axis agreement #7167 as this member | not this display |
| global later T | not used |
| incoming-axis agreement as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: incoming-axis agreement of `M` at `t+1` on the four #7211 y-probes, and reverse/face from that. |
| V2 | Current main has no landed incoming-axis-agreement reverse/face of timed `M` on these four #7211 y-probes. |
| V3 | `Axis(M)` at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned occupied axes of own incoming at the `t+1` cut and scores equality of nonempty axis sets. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique incoming lock, does not replace `Axis(M)` by leftover of `M` alone,
does not replace incoming-axis agreement by existential opposite of signed
locks, does not identify this display with #7211 exist-opposite HOLD, and
does not identify it with two-site incoming-axis agreement #7167 as this
member. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_2,e_3}`, the complement of `Axis(M)(A)={e_1}`; same hold/fail bits, different letter | ATTEMPTED |
| leftover of `M` and outgoing dual | score unoccupied axes of the union | leftover of the union is empty at each probe, so that leftover reverse fails while incoming-axis reverse holds | ATTEMPTED |
| #7211 exist-opposite | reuse signed reverse hold and face hold of `M` | those bits HOLD/HOLD; incoming-axis reverse holds and face fails because `Axis(M)(C)` is not `Axis(M)(D)` | ATTEMPTED |
| two-site incoming-axis #7167 | reuse Axis(M) hold/fail on `{0,(0,1,0)}` | same four `Axis(M)` sets, different seed: y-mirror is tick 0 here and tick 1 there | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` remains a set; unique-L face would be `UNDEFINED` while incoming-axis face fails | ATTEMPTED |
| exist-opposite of axis vectors | score `a+b=(0,0,0)` inside `Axis(M)` | reverse is set equality of nonempty unsigned axes, not opposite of unsigned axes | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes extra neighbor letters; incoming axis is unsigned occupied directions of own earliest `M` | ATTEMPTED |
| sum of a set | replace `Axis(M)` by a `Z^3` sum | the construction does not sum; `Axis(M)(D)` stays `{e_2, e_3}` while the signed sum of `M(D,τ)` cancels to `−e_2` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by incoming-axis agreement | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `Axis(M)` with leftover
of `M` alone, missing identification of incoming-axis agreement with
existential opposite of signed locks, and missing Record identification of
incoming-axis reverse are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis of `M`, empty
Axis fail not `UNDEFINED`, four y-probes with seed `A`, and mixed remains a
set are declared. No uniqueness of incoming locks, no six-neighbor lock
union as the scored object, no occupancy of sites, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned occupied lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming axis sets, reverse/face from incoming-axis agreement | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for incoming-axis reverse/face,
a formation-rate rule, and a physical selector among occupied axes. None is
taken here.

### N7 — hostile steelman

**Steelman:** Incoming-axis reverse hold is only #7211 exist-opposite HOLD of
signed `M`; face fail is only refusing that leftover; leftover of `M` alone
already gives the same hold/fail bits from complementary unoccupied axes;
empty Axis should be `UNDEFINED` like empty exist-opposite; unsigned axis
equality is only named-sign collapse; and the four `Axis(M)` sets already
appeared on two-site incoming-axis agreement #7167.

**Answer:** Letter opposite on one axis occupies that axis. Exist-opposite
face HOLDs from `+e_2` against `−e_2` while `Axis(M)(C)={e_2}` is not equal
to `Axis(M)(D)={e_2, e_3}`, so incoming-axis face fails. Leftover of `M`
alone is the complement of `Axis(M)`; same hold/fail bits do not make the
letter the same. Empty Axis fails by declaration, and is not `UNDEFINED`.
Named signs lost the axis. Two-site incoming-axis agreement #7167 reports
the same four `Axis(M)` sets on a different seed: the y-mirror is tick 0 on
this y-symmetric three-site process.

### N8 — cross-cycle echo

A unique-L display on these same #7211 y-probes would assign
`L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and report reverse
hold with face `UNDEFINED`. A #7211 exist-opposite display reports reverse
hold and face hold from signed incoming sets. Leftover of `M` alone reports
reverse hold and face fail from complementary unoccupied axes `{e_2,e_3}`
and `{e_1,e_3}` versus `{e_1}`. Leftover of `M` and outgoing dual together
reports reverse fail and face fail from empty leftover. Two-site
incoming-axis agreement #7167 reports the same four `Axis(M)` sets on the
two-site seed. This note is not those displays: the letter is `Axis(M)` at
`t+1` on the y-symmetric three-site seed, reverse holds, and face fails.

**Gate disposition:** PASS for the incoming-axis-agreement reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals exist-opposite of signed `M`,” “the predicate
equals leftover of `M` alone,” “bits are Admissibility,” “the letter is
occupancy of sites,” “empty Axis is `UNDEFINED`,” “reverse fails,” or
“face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads each probe's own incoming set from records with
tick `<= t+1`, forms `Axis(M)`, scores reverse and face by incoming-axis
agreement, and checks Theorems 1--3. It also checks that the construction
is not named-sign lettering, that mixed remains a set, that the construction
does not sum, that occupancy of sites is not used, that a formation member
from already-recorded six-neighbor locks is not attached, that the letter is
not leftover of unique-L, that the letter is not leftover of #7211
exist-opposite of `M`, and that the letter is not leftover of leftover-of-`M`
alone. No runner cache is written.
