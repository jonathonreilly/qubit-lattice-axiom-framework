---
claim_id: nnseed_sametick_neighbor_lock_sum_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the same-tick-inclusive sum of 6-NN locks on the four nnseed x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_sametick_neighbor_lock_sum_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Sum Of Six-Neighbor Locks Reverse And Face On Four Nnseed X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** letter in `Z^3` or `UNDEFINED` read as the same-tick-inclusive sum
of six-neighbor lock vectors at the formation tick of four x-probes of the
displayed two-site nnseed process, scored as reverse and face. The letter is
the vector sum of locks of 6-NN formed at tick ≤ t(q), q excluded, or
`UNDEFINED` if that list is empty. Mixed lists remain defined. Occupancy `n`
is not used. The probe's own incoming lock is not used. This is not named-sign
lettering. This is not leftover of nfsum strictly-earlier sums. Uniqueness of
incoming locks is not required. Displayed, not adopted. This note does not
write the sum letter into Admissibility and does not attach a formation
member from same-tick-inclusive six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_sametick_neighbor_lock_sum_reverse_face_2026_08_15.py`](../scripts/nnseed_sametick_neighbor_lock_sum_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Incoming lock letters are unit nearest-neighbor
steps. The scored letter is a vector in `Z^3`, or `UNDEFINED`. Named signs
`{+,−}` are a coarser readout and are not the letter. Strictly-earlier
recorded-neighbor sums are a different readout and are not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick-inclusive six-neighbor lock lists and the Z^3 sum letter on the four nnseed x-probes, with reverse fail and face hold; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_sametick_neighbor_lock_sum_reverse_face
target_blocker_text: "display reverse and face from the same-tick-inclusive sum of 6-NN locks on the four nnseed x-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the sum letter into Admissibility, do not reduce to named sign, do not reuse strictly-earlier nfsum sums, do not use occupancy n, and do not identify the letter with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for sum letters from same-tick-inclusive six-neighbor locks on the four nnseed x-probes; displayed, not adopted"
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

No larger host is used. The four probes are the only sites whose
same-tick-inclusive six-neighbor lock lists and sum letters are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

That incoming lock is not the sum letter scored below.

## Named sum letter from same-tick-inclusive six-neighbor locks

At the formation tick of a probe `q`, let `S` be the list of locks of 6-NN
of `q` formed at tick ≤ t(q), `q` excluded. Same-tick neighbors count. A
strictly earlier neighbor is included because its tick is less than `t(q)`.
The probe itself is excluded. This display does not use occupancy `n`. It
does not use the probe's own incoming lock.

If `S` is empty, the letter is `UNDEFINED`. Else the letter is the vector sum
of `S` in `Z^3`. Mixed lists remain defined: mixed no longer kills the letter.
The construction does not require `S` to be a singleton. It is not leftover of
nfsum strictly-earlier sums.

A process-determined sum letter at a probe is a value in `Z^3` assigned by
that named construction from same-tick-inclusive six-neighbor locks, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a named sign of those locks with the sum letter is
refused: named-sign lettering lost the axis. Reverse and face are scored on
the sum vector. They are not scored on `{+,−}` names and are not an
occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is not zero, the
comparison fails. The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Sum letters are not written into Admissibility.

## Theorem 1 — same-tick-inclusive lock list and sum letter at each probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
probes. At each formation tick the same-tick-inclusive six-neighbor lock list
and sum letter are:

```text
A: +e_1 at (0, 0, 0), +e_1 at (1, 1, 0), +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);     L(A) = (5, 0, 0)
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1), +e_1 at (1, 1, 0);     L(B) = (2, 0, 1)
C: −e_2 at (1, 0, 0);                        L(C) = −e_2
D: +e_2 at (0, 1, 0);                        L(D) = +e_2
```

`A` at tick 2 includes three same-tick neighbors `(1, -1, 0)`, `(1, 0, 1)`,
and `(1, 0, -1)`, each locking `+e_1`, in addition to the strictly earlier
origin and `D`. `B` at tick 2 includes the same-tick neighbor `(1, 0, 1)`
locking `+e_1` in addition to `(0, 1, 1)` and `D`. `C` and `D` have no
same-tick six-neighbor; their lists match the strictly earlier lists.

`C`'s included neighbor is `A` locking `−e_2`. `D`'s included neighbor is the
seed `(0, 1, 0)` locking `+e_2`. The sum letters at `C` and `D` are opposite
axis vectors. Named-sign lettering of the same lists is `C−/D+` and lost the
axis: those signs are not opposites in the `C+` and `D−` face predicate, while
`L(C)+L(D)=(0,0,0)`.

`B`'s same-tick-inclusive neighbor locks are `+e_3`, `+e_1`, and `+e_1`. Those
vectors are mixed. Unique lock-vector lettering would report `UNDEFINED`. The
sum letter is `(2, 0, 1)`. They share a named sign `+`; reducing to named sign
would hide that mix.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`). That non-uniqueness is not a unique-lettering of
same-tick-inclusive neighbor lock vectors. The sum letters are not identified
with those incoming steps. Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. The sum letters are `L(A)=(5, 0, 0)` and
`L(B)=(2, 0, 1)`, so `L(A)+L(B)=(7, 0, 1)`. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Strictly-earlier nfsum sums on the
same probes are `(2, 0, 0)` and `(1, 0, 1)` and also fail reverse, but those
are a different object: this letter includes same-tick neighbors. Unique
lock-vector lettering of the same lists would assign `L(B)=UNDEFINED` and
would report reverse `UNDEFINED`. That readout is a different object and is
not used. A named-sign readout of the same neighbor locks would assign
`L(A)=+` and `L(B)=+` and would report reverse fail for a different reason.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. The sum letters are `L(C)=−e_2` and `L(D)=+e_2`,
so `L(C)+L(D)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The letters are not written into Admissibility.

Named-sign lettering of the same lists is `C−/D+`. Face as `C+` and `D−`
fails on those signs. The vectors remain opposites. This note keeps the
vectors.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify sum letters with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive lock list to be a singleton.
- It does not reuse strictly-earlier nfsum sums as this letter.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from same-tick-inclusive six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  same-tick-inclusive lock vectors.
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

This display uses Lattice to name `B_3(0)` and the four probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
nnseed process, the same-tick-inclusive six-neighbor lock lists, the sum letter
from those locks, and the reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| same-tick-inclusive six-neighbor lock lists at each probe formation tick | Theorem 1 |
| sum letter from those locks | Theorem 1; `(5, 0, 0)`, `(2, 0, 1)`, `−e_2`, `+e_2` |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| leftover of nfsum strictly-earlier sums | not used; same-tick neighbors count |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the letter | not used |
| formation member from same-tick-inclusive six-neighbor locks | not attached |
| sum letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick-inclusive sum letter from 6-NN locks on the four nnseed x-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive neighbor-lock-sum reverse/face report on these four nnseed x-probes. |
| V3 | Same-tick-inclusive lock lists, sum letters, and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads 6-NN lock vectors formed at tick ≤ t(q) and scores their sum. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not reuse strictly-earlier nfsum sums, and does not use occupancy
`n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| leftover of nfsum strictly-earlier sums | drop same-tick neighbors | refused; leftover; `L(A)` would be `(2, 0, 0)` while this letter is `(5, 0, 0)` |
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; `L(B)` would be `UNDEFINED` while the sum is `(2, 0, 1)` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `C−/D+` fails face while `−e_2+(+e_2)=0` |
| identify sum letter with the probe's own incoming `{±e_i}` | map `A`'s incoming `−e_2` to `L(A)` | refused; `L(A)=(5, 0, 0)` from same-tick-inclusive neighbor locks |
| reverse/face from self-incoming named signs | reuse incoming `+e_1` at both `C` and `D` | different object; both `+e_1`; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from same-tick-inclusive six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `Z^3` sums | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from same-tick-inclusive
six-neighbor locks, and missing Record identification of the sum letter are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, sum letter from same-tick-inclusive six-neighbor
locks formed at tick ≤ t(q), four probes, and reverse/face as vector-sum zero
are declared. No uniqueness of incoming locks, no occupancy `n`, no named-sign
reduction, no leftover of nfsum strictly-earlier sums, no formation attachment
from same-tick-inclusive six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each sum letter from same-tick-inclusive lock vectors | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four sum letters and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `Z^3` sums. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a same-tick or earlier neighbor exists at a forming probe, the
site should lock that unique vector as incoming content, mixed neighbor locks
should make the letter `UNDEFINED`, reverse and face should both hold, named
signs should suffice because they keep orientation, occupancy `n` should
track that vector, and the strictly-earlier nfsum sums already answer the
question.

**Answer:** The named construction assigns sum letters `(5, 0, 0)`,
`(2, 0, 1)`, `−e_2`, `+e_2` at `A,B,C,D` from same-tick-inclusive six-neighbor
locks. Mixed no longer kills the letter. Occupancy `n` is not used. Named
signs lost the axis. This is not leftover of nfsum. Reverse fails. Face holds.
The bits remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique-letter-of-occupancy display on the same four nnseed probes
closed reverse/face as `none`/`none` because occupancy at `C` and at `D`
agrees. An occupancy-kernel inner product on the same probes reports reverse
and face fail. A named-sign neighbor-lock lettering on the same lists reports
`C−/D+` and face fail, having lost the axis. Unique lock-vector lettering of
the same lists reports reverse `UNDEFINED` because `L(B)` is mixed vectors,
while face holds. Strictly-earlier nfsum sums report reverse fail and face
hold with letters `(2, 0, 0)` and `(1, 0, 1)` at `A` and `B`. This note is not
those displays: same-tick neighbors count, mixed no longer kills the letter,
`L(A)=(5, 0, 0)`, `L(B)=(2, 0, 1)`, reverse fails, and `L(C)+L(D)=(0,0,0)` so
face holds. A self-incoming named-sign readout on the same process has `C` and
`D` both `+e_1`. This note does not reuse that scoring.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock-sum
reverse/face reports above. FAIL / DO NOT SHIP for “the sum letter equals the
named sign,” “the sum letter equals the unique singleton lock vector,” “the
sum letter equals the probe's own incoming step,” “the sum letter equals the
strictly-earlier nfsum leftover,” “letters are Admissibility,” “the letter is
occupancy `n`,” or “reverse holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, collects same-tick-inclusive six-neighbor locks at each
probe's formation tick, reads the `Z^3` sum letter at the four probes, and
checks Theorems 1--3. It also checks that the construction is not leftover of
nfsum strictly-earlier sums, that it is not named-sign lettering, that mixed
lists remain defined, that the probe's own incoming step is not the sum
letter, that occupancy `n` is not used, and that a formation member from
same-tick-inclusive six-neighbor locks is not attached.
No runner cache is written.
