---
claim_id: nnseed_later_tick_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite 6-NN locks at the first later tick when all four nnseed x-probes are recorded are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_later_tick_existential_opposite_reverse_face_2026_08_15.py
---

# Later-Tick Existential Opposite Neighbor-Lock Reverse And Face On Four Nnseed X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite six-neighbor locks at
the first later tick in `B_3(0)` at which all four nnseed x-probes are
recorded. Let `t(q)` be the formation tick of probe `q`. Let `T` be the
maximum of `t(A)`, `t(B)`, `t(C)`, `t(D)` among those defined in `B_3(0)`.
At tick `T`, `S_*(q)` is the set of locks of six-neighbors of `q` that
formed at tick `≤ T` and are not `q`. Reverse holds if and only if some
lock in `S_*(A)` is the vector opposite of some lock in `S_*(B)`. Face
holds if and only if some lock in `S_*(C)` is the vector opposite of some
lock in `S_*(D)`. Empty `S_*` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Occupancy `n` is not
used. The probe's own incoming lock is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of nfexist: nfexist reads already-recorded
six-neighbor locks at each probe's own formation tick, a different set.
Uniqueness of incoming locks is not required. Uniqueness of the lock set
is not required. Displayed, not adopted. This note does not write
existential opposite into Admissibility and does not attach a formation
member from later-tick six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_later_tick_existential_opposite_reverse_face_2026_08_15.py`](../scripts/nnseed_later_tick_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
later-tick six-neighbor lock sets. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock-vector letter is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of later-tick six-neighbor lock sets on the four nnseed x-probes at the first T with all four recorded, with reverse fail and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_later_tick_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite 6-NN locks at the first later tick when all four nnseed x-probes are recorded, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, and do not identify the sets with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for existential opposite of later-tick six-neighbor locks on the four nnseed x-probes; displayed, not adopted"
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

No larger host is used. The four probes are the only sites whose later-tick
six-neighbor lock sets are scored:

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

That incoming lock is not a member of `S_*(q)` scored below unless it appears
as a lock of some six-neighbor of `q`.

## Named existential opposite from later-tick six-neighbor locks

Let `t(q)` be the formation tick of probe `q` when that tick is defined in
`B_3(0)`. Let `T` be the maximum of those four ticks. This `T` is the first
tick in `B_3(0)` at which all four x-probes are recorded.

At tick `T`, for each probe `q`, let `S_*(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ T` and are not `q`. Same-tick
and later-than-formation neighbors count whenever they have formed by `T`.
The probe itself is excluded. This display does not use occupancy `n`. It
does not use the probe's own incoming lock. Duplicate locks at two neighbors
collapse in the set. The construction does not require `S_*(q)` to be a
singleton. It does not sum `S_*(q)`. It is not a unique lock-vector leftover
and not a sum leftover. It is not leftover of nfexist.

Incoming `{±e_i}` tags of the probe itself are not `S_*(q)`. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis. Reverse and face are scored on existence of a pair
of lock vectors that add to zero. They are not scored on `{+,−}` names and
are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S_*(A) and some b in S_*(B) with a+b=(0,0,0)
face     <=>  some c in S_*(C) and some d in S_*(D) with c+d=(0,0,0)
```

If `S_*(A)` or `S_*(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S_*(C)` or `S_*(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — later-tick lock sets at each probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
probes. The formation ticks are `t(A)=2`, `t(B)=2`, `t(C)=3`, `t(D)=1`. All
four are defined in `B_3(0)`, so

```text
T = max{t(A), t(B), t(C), t(D)} = 3.
```

At tick `T=3` the six-neighbor lock lists and lock sets are:

```text
A: +e_1 at (2, 0, 0), +e_1 at (0, 0, 0), +e_1 at (1, 1, 0),
   +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);
   S_*(A) = {+e_1}
B: +e_1 at (2, 1, 1), +e_3 at (0, 1, 1), +e_3 at (1, 2, 1),
   +e_2 at (1, 2, 1), +e_1 at (1, 2, 1), +e_1 at (1, 0, 1),
   +e_3 at (1, 1, 2), +e_1 at (1, 1, 0);
   S_*(B) = {+e_1, +e_2, +e_3}
C: −e_2 at (1, 0, 0);
   S_*(C) = {−e_2}
D: +e_2 at (0, 1, 0), +e_2 at (1, 2, 0), −e_2 at (1, 0, 0),
   +e_3 at (1, 1, 1), +e_1 at (1, 1, 1), −e_3 at (1, 1, -1),
   +e_1 at (1, 1, -1);
   S_*(D) = {+e_1, +e_2, −e_2, +e_3, −e_3}
```

`C`'s later-tick neighbor is `A` locking `−e_2`. `D`'s later-tick neighbors
include the seed `(0, 1, 0)` locking `+e_2`. Some lock at `C` is the vector
opposite of some lock at `D`. Named-sign lettering of the same lists is
`C−` against a mixed `D` set and lost the axis: those signs are not opposites
in the `C+` and `D−` face predicate, while `−e_2+(+e_2)=(0,0,0)`.

`B`'s later-tick neighbor locks are `+e_1`, `+e_2`, and `+e_3`. Those three
vectors are mixed. Unique lock-vector lettering would report `UNDEFINED` at
`B`. The lock set `S_*(B)={+e_1, +e_2, +e_3}` remains defined. A sum leftover
would replace `S_*(B)` by `(1, 1, 1)` and `S_*(D)` by `(1, 0, 0)`. This
display keeps the set and does not sum. They share a named sign `+` at `B`;
reducing to named sign would hide that mix.

The nfexist already-recorded sets at formation are `{+e_1}`, `{+e_1, +e_3}`,
`{−e_2}`, `{+e_2}`. Those are different sets: `S_*(B)` contains `+e_2` and
`S_*(D)` is not a singleton. This note is not leftover of nfexist.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`). That non-uniqueness is not a unique-lettering of
later-tick neighbor lock vectors. The lock sets are not identified with
those incoming steps. Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S_*(A)` and `b` in `S_*(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `S_*(A)={+e_1}` and
`S_*(B)={+e_1, +e_2, +e_3}`. The pairs are `+e_1++e_1=(2,0,0)`,
`+e_1++e_2=(1,1,0)`, and `+e_1++e_3=(1,0,1)`. No pair is opposite. Reverse
fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign `S_*(B)` mixed and would report reverse `UNDEFINED`.
That readout is a different object and is not used. A sum leftover of the
same lists would replace the sets by `(1, 0, 0)` and `(1, 1, 1)` and would
report reverse fail for a different reason. A named-sign readout of the same
neighbor locks would assign `+` and `+` at `A` and `B` and would report
reverse fail for a different reason. The nfexist formation-time sets also
fail reverse, but those are different sets.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S_*(C)` and `d` in `S_*(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S_*(C)={−e_2}` and
`S_*(D)={+e_1, +e_2, −e_2, +e_3, −e_3}`, so `−e_2+(+e_2)=(0,0,0)`. Face
holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

Named-sign lettering of the same lists is `C−` against a mixed `D`. Face as
`C+` and `D−` fails on those signs. The vectors remain opposites. This note
keeps the vectors. A sum leftover of `S_*(D)` would replace the set by
`+e_1` and would fail face, while existential opposite holds. Unique
lock-vector lettering of `S_*(D)` is mixed and would report face
`UNDEFINED`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify lock sets with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the later-tick lock set to be a singleton.
- It does not sum the later-tick lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from later-tick six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  later-tick lock vectors.
- It does not reprint nfexist formation-time already-recorded lock sets.
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
nnseed process, the later-tick six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| later-tick six-neighbor lock sets at first `T` with all four x-probes recorded | Theorem 1 |
| lock sets `S_*(A)`, `S_*(B)`, `S_*(C)`, `S_*(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_2, +e_3}`, `{−e_2}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| formation member from later-tick six-neighbor locks | not attached |
| leftover of nfexist formation-time sets | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of 6-NN locks at the first later tick when all four nnseed x-probes are recorded, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed later-tick existential-opposite neighbor-lock reverse/face report on these four nnseed x-probes. |
| V3 | Later-tick lock sets and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at a later common tick and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not reprint nfexist, and does not
use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same neighbor locks | replace `S_*` by the `Z^3` sum | refused; leftover; sum of `S_*(D)` is `+e_1` and would fail face while `−e_2+(+e_2)=0` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `C−` against mixed `D` fails face while `−e_2+(+e_2)=0` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s incoming `−e_2` into `S_*(A)` | refused; `S_*(A)={+e_1}` from later-tick neighbor locks |
| reverse/face from self-incoming named signs | reuse incoming `+e_1` at both `C` and `D` | different object; both `+e_1`; not this display |
| leftover of nfexist | reuse formation-time already-recorded sets `{+e_1}`, `{+e_1, +e_3}`, `{−e_2}`, `{+e_2}` | refused; different set; `S_*(B)` contains `+e_2` and `S_*(D)` is mixed |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from later-tick six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from later-tick
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, later-tick lock set of six-neighbors formed by the
first `T` at which all four x-probes are recorded, existential opposite, four
probes, and reverse/face as existence of a pair that sums to zero are
declared. No uniqueness of incoming locks, no occupancy `n`, no named-sign
reduction, no singleton leftover, no sum leftover, no nfexist leftover, no
formation attachment from later-tick six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a later-tick set | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a six-neighbor exists at the later common tick, the site
should lock that unique vector as incoming content, mixed neighbor locks
should make reverse `UNDEFINED`, the sets should be replaced by their sums,
reverse and face should both hold, named signs should suffice because they
keep orientation, occupancy `n` should track that vector, and the nfexist
formation-time sets already answered the question.

**Answer:** The named construction reports lock sets `{+e_1}`,
`{+e_1, +e_2, +e_3}`, `{−e_2}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` at
`A,B,C,D` from later-tick six-neighbor locks at `T=3`. Mixed remains a set.
The construction does not sum. Occupancy `n` is not used. Named signs lost
the axis. No pair from `S_*(A)` and `S_*(B)` is opposite, so reverse fails.
Face holds. The sets are not leftover of nfexist. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique-letter-of-occupancy display on the same four nnseed probes
closed reverse/face as `none`/`none` because occupancy at `C` and at `D`
agrees. An occupancy-kernel inner product on the same probes reports reverse
and face fail. A named-sign neighbor-lock lettering on the later-tick lists
reports `C−` against mixed `D` and face fail, having lost the axis. Unique
lock-vector lettering of the same lists reports reverse `UNDEFINED` because
the lock vectors at `B` are mixed, and face `UNDEFINED` because the lock
vectors at `D` are mixed. A sum leftover of the same lists reports face fail
because the sum of `S_*(D)` is `+e_1`. The nfexist formation-time display
reports reverse fail and face hold on different sets `{+e_1}`,
`{+e_1, +e_3}`, `{−e_2}`, `{+e_2}`. This note is not those displays: mixed
remains a set, the construction does not sum, no pair from `S_*(A)` and
`S_*(B)` is opposite, reverse fails, and `−e_2+(+e_2)=(0,0,0)` so face
holds. A self-incoming named-sign readout on the same process has `C` and
`D` both `+e_1`. This note does not reuse that scoring.

**Gate disposition:** PASS for the later-tick six-neighbor-lock
existential-opposite reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal nfexist,” or “reverse holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, takes `T` as the first tick at which all four x-probes
are recorded, collects six-neighbor locks formed by `T` at each probe with
the probe excluded, reads the lock sets at the four probes, and checks
Theorems 1--3. It also checks that the construction is not named-sign
lettering, that mixed sets remain defined, that the construction does not
sum, that the probe's own incoming step is not the lock set, that occupancy
`n` is not used, that a formation member from later-tick six-neighbor locks
is not attached, and that the sets are not leftover of nfexist. No runner
cache is written.
