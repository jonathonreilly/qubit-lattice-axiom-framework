---
claim_id: y_symmetric_three_site_xprobe_own_incoming_set_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from own incoming set on the four #7176 x-probes are reported. No S⁺. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_xprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py
---

# Own Incoming Set Existential Opposite Reverse And Face On Four #7176 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own incoming *set* `M(q)` on the
four nsyopinx #7176 x-probes in `B_3(0)={n:n·n<=9}`. Same process as nsyopp
#7132. Same x-probes as nsopp #7093. Let `t(q)` be the formation tick of
probe `q`. `M(q)` is the set of earliest incoming nearest-neighbor steps at
`q`. Seeds use their seed letter as a singleton. Mixed stays a set. Unformed
is `UNDEFINED`. Reverse holds if and only if some lock in `M(A)` is the
vector opposite of some lock in `M(B)`. Face holds if and only if some lock
in `M(C)` is the vector opposite of some lock in `M(D)`. Empty or
`UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with no
opposite pair fails. Unique `L` is not the object. The six-neighbor star
`S^+` is not the letter. Occupancy `n` is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of unique-L on these x-probes, which is `UNDEFINED`
when mixed. This is not leftover of #7176 `S^+` exist-opposite, which HOLDs
and Reverse HOLD does not use L(A). Reverse HOLD uses a six-neighbor star at
`A`, not the own incoming set. The own incoming set does not use a
six-neighbor star. Uniqueness of incoming locks is not required. Displayed,
not adopted. Do not write into Admissibility. Do not attach L1. This note
does not write existential opposite into Admissibility and does not attach a
formation member from already-recorded six-neighbor locks. This display
does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_xprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_xprobe_own_incoming_set_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own incoming sets. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock-vector letter is a different readout and is
not used as the object: report `M`. A `Z^3` sum of those locks is a
different readout and is not used. The construction does not sum. No S⁺.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M(q) as the probe's own incoming set of earliest NN steps on the four #7176 x-probes, mixed stays a set, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_xprobe_own_incoming_set_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from the own incoming set on the four #7176 x-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with unique-L leftover, and do not identify the sets with #7176 S^+ leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own incoming set on the four #7176 x-probes; displayed, not adopted"
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
incoming sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is not a seed. Same process as nsyopp #7132. Same x-probes
as nsopp #7093 and as nsyopinx #7176.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Mixed stays a set. Uniqueness is not required. A later parent
does not re-form `q`.

## Named existential opposite from the own incoming set

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. Unique `L(q)` is not used as the letter. This
display does not use a six-neighbor star. Occupancy `n` is not used.
Duplicate incoming steps collapse in the set. The construction does not
require `M(q)` to be a singleton. It does not sum `M(q)`. It is not a unique
lock-vector leftover and not a sum leftover. It is not leftover of unique-L
on these x-probes. It is not leftover of #7176 same-tick union own `S^+`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in M(A) and some b in M(B) with a+b=(0,0,0)
face     <=>  some c in M(C) and some d in M(D) with c+d=(0,0,0)
```

If `M(A)` or `M(B)` is empty or `UNDEFINED`, reverse is `UNDEFINED`. Else
reverse fails if no such pair exists. If `M(C)` or `M(D)` is empty or
`UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks and own incoming sets at each x-probe

Direct enumeration of the displayed nsyopp #7132 process on `B_3(0)` forms
all four x-probes. The formation ticks are `t(A)=3`, `t(B)=2`, `t(C)=4`,
`t(D)=3`. `A` is not a seed. Those ticks locate the earliest incoming set.
They are not occupancy kernels and are not a global later T.

Own incoming sets at each probe's own formation tick are:

```text
A: incoming −e_3, +e_3;
   t(A)=3;  M(A) = {+e_3, −e_3}
B: incoming +e_1;
   t(B)=2;  M(B) = {+e_1}
C: incoming +e_1;
   t(C)=4;  M(C) = {+e_1}
D: incoming −e_2, −e_3, +e_3;
   t(D)=3;  M(D) = {−e_2, +e_3, −e_3}
```

`A` is not a seed. Mixed stays a set: `A` has two earliest incoming steps
`−e_3` and `+e_3`, so `M(A)={+e_3, −e_3}` is a two-element set, not
`UNDEFINED`. `D` has three earliest incoming steps `−e_2`, `−e_3`, and
`+e_3`, so `M(D)={−e_2, +e_3, −e_3}` is a three-element set, not
`UNDEFINED`. Unique-L leftover would assign `L(A) = UNDEFINED` and
`L(D) = UNDEFINED` from those mixes and would leave reverse `UNDEFINED` and
face `UNDEFINED`. Here uniqueness is not required and mixed stays a set.

Compare to #7176 `S^+`. Same-tick union own leftover on this process
reports

```text
L(A) = UNDEFINED;  S^+(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(B) = {+e_1, +e_3}
S^+(C) = {+e_1, +e_3, −e_3}
S^+(D) = {+e_1, −e_1, +e_3, −e_3}
```

and Reverse HOLD does not use L(A). That leftover is a six-neighbor star,
not the own incoming set. `M(A)` omits `+e_1`, `+e_2`, and `−e_2` that enter
`S^+(A)` from already-recorded neighbors. Same-tick `(1,-1,0)` supplies
`+e_2` into `S^+(A)`; that letter is not incoming at `A`. `M(B)` and `M(C)`
are the singleton `{+e_1}`; the #7176 neighbor stars at `B`, `C`, and `D` are
larger. No S⁺.

Incoming locks exist and need not be unique (`A` has two earliest incoming
steps `−e_3` and `+e_3`; `D` has three earliest incoming steps `−e_2`,
`−e_3`, and `+e_3`). That non-uniqueness does not empty `M(A)` or `M(D)`.
Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `M(A)` and `b` in `M(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `M(A)={+e_3, −e_3}` and
`M(B)={+e_1}`. Neither `+e_3+(+e_1)` nor `−e_3+(+e_1)` is the origin.
Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse fails. Unique-L leftover
reports reverse `UNDEFINED` from mixed `A`. #7176 `S^+` leftover reports
reverse hold from `−e_3` in `S^+(A)` against `+e_3` in `S^+(B)`, and Reverse
HOLD does not use L(A). Fail while `S^+` HOLD is a discriminator of the own
incoming set against the six-neighbor star. The own incoming set does not
use a six-neighbor star. Reverse fails because no pair from `M(A)` and
`M(B)` is opposite.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `M(C)` and `d` in `M(D)` with
`c+d=(0,0,0)`. Both sets are nonempty: `M(C)={+e_1}` and
`M(D)={−e_2, +e_3, −e_3}`. None of `+e_1+(−e_2)`, `+e_1+(+e_3)`, or
`+e_1+(−e_3)` is the origin. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. Unique-L leftover
reports face `UNDEFINED` from mixed `D`. #7176 `S^+` leftover reports face
hold from neighbor stars at `C` and `D`. Fail while `S^+` HOLD is the same
discriminator on the face pair. Named-sign lettering lost the axis in mixed
`{+,−}` at `A` and at `D`. Face already fails at each probe's own formation
tick from the own incoming set.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set to be a singleton.
- It does not sum the own incoming set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these x-probes as the object.
- It does not reprint #7176 `S^+` as the letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
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
y-symmetric three-site process, the own incoming sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsyopp #7132 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `3` |
| own incoming sets `M(A)`, `M(B)`, `M(C)`, `M(D)` | Theorem 1; `{+e_3, −e_3}`, `{+e_1}`, `{+e_1}`, `{−e_2, +e_3, −e_3}` |
| compare to #7176 `S^+(A)` | Theorem 1; `{+e_1, +e_2, −e_2, +e_3, −e_3}`; Reverse HOLD does not use L(A) |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of #7176 `S^+` exist-opposite | not this display |
| six-neighbor star as the letter | not used |
| leftover of two-site opposite-lock x-probe own incoming set | not this display |
| leftover of y-symmetric three-site y-probe own incoming set | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own incoming set on the four #7176 x-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-incoming-set existential-opposite reverse/face report on these four #7176 x-probes. |
| V3 | Own incoming sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint #7176 `S^+` as the letter, does not use a six-neighbor
star, and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; reverse and face would be `UNDEFINED` when mixed while the own incoming set is nonempty and both bits fail |
| #7176 `S^+` exist-opposite | reuse same-tick six-neighbor locks union `L(q)` | refused; leftover; that readout HOLDs reverse and face, and Reverse HOLD does not use L(A), while the own incoming set fails both |
| sum of the same incoming sets | replace `M` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `M(A)` cancels to the origin while `M(A)` stays a two-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `M` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `A` and all three at `D` are kept and mixed stays a set |
| two-site opposite-lock x-probe own incoming set | reuse seed `{0,(0,1,0)}` | refused; leftover; that display reports `M(A)={+e_2, +e_3, −e_3}` with incoming `+e_2`, while this `M(A)` omits `+e_2` |
| y-symmetric three-site y-probe own incoming set | reuse y-probes `A=(0,1,0)`, `C=(0,2,0)` | refused; leftover; that frame reports reverse hold and face hold from seed `A` and from `+e_2` at `C` against `−e_2` at `D` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set of
earliest nearest-neighbor steps, mixed stays a set, existential opposite,
four x-probes with non-seed `A`, and reverse/face as existence of a pair that
sums to zero are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no singleton leftover as the object, no sum
leftover, no unique-L leftover, no #7176 `S^+` leftover, no six-neighbor
star as the letter, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The own incoming set is leftover of unique-L because mixed `A`
and mixed `D` should make reverse and face `UNDEFINED`, the sets should be
replaced by their sums, #7176 `S^+` already answered exist-opposite with
HOLD that does not use `L(A)`, named signs should suffice because they keep
orientation, occupancy `n` should track that vector, two-site opposite-lock
x-probes already fail both bits, and y-symmetric y-probes already answered
hold.

**Answer:** The named construction reports incoming sets `{+e_3, −e_3}`,
`{+e_1}`, `{+e_1}`, `{−e_2, +e_3, −e_3}` at `A,B,C,D` from the probe's own
earliest incoming steps. Mixed stays a set. The construction does not sum.
Occupancy `n` is not used. Named signs lost the axis. No pair from `M(A)`
and `M(B)` is opposite, so reverse fails. No pair from `M(C)` and `M(D)` is
opposite, so face fails. Unique-L leftover reports reverse `UNDEFINED` and
face `UNDEFINED` from mixed `A` and mixed `D`. #7176 `S^+` leftover reports
reverse hold and face hold from neighbor stars, and Reverse HOLD does not
use L(A). Fail while `S^+` HOLD is a discriminator. Two-site opposite-lock
x-probe own incoming set reports `M(A)={+e_2, +e_3, −e_3}` with incoming
`+e_2`; this `M(A)` omits `+e_2` because the y-mirror seed removes that
incoming. Y-symmetric three-site y-probe own incoming set reports reverse
hold and face hold from a different frame whose `A` is a seed. The sets are
not those leftovers. The bits remain displayed. Incoming-lock uniqueness is
not required.

### N8 — cross-cycle echo

A unique-L display on these same #7176 x-probes would assign
`L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=UNDEFINED` and report
reverse `UNDEFINED` with face `UNDEFINED`. A #7176 same-tick union own
display reports `S^+(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}` with reverse hold
and face hold, and Reverse HOLD does not use L(A). Unique lock-vector
lettering of the incoming sets would report reverse `UNDEFINED` and face
`UNDEFINED` because `A` and `D` mix. A sum leftover of the same lists would
replace mixed `M(A)` by the origin after cancelling `+e_3` and `−e_3`.
Two-site opposite-lock x-probe own incoming set reports `M(A)` with extra
`+e_2`. Y-symmetric three-site y-probe own incoming set reports reverse hold
and face hold. nszmenu mixed `M` reverse-fails and face-fails while `S^+`
HOLDs. This note is not those displays: mixed stays a set, the construction
does not sum, the letter is the own incoming set, reverse fails, and face
fails.

**Gate disposition:** PASS for the own-incoming-set existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the sets equal unique-L leftover,” “the sets
equal #7176 `S^+` leftover,” “reverse holds,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads each probe's own incoming set of earliest
nearest-neighbor steps, scores reverse and face by existential opposite,
compares `M` to #7176 `S^+`, and checks Theorems 1--3. It also checks that
the construction is not named-sign lettering, that mixed stays a set, that
the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique-L, and that the sets are not
leftover of #7176 `S^+`. No runner cache is written.
