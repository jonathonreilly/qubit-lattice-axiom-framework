---
claim_id: nnseed_yprobe_sametick_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite same-tick-inclusive 6-NN locks on the four nnseed y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_yprobe_sametick_existential_opposite_reverse_face_2026_08_15.py
---

# Existential Opposite Same-Tick-Inclusive Neighbor-Lock Reverse And Face On Four Nnseed Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite same-tick-inclusive
six-neighbor locks at the formation tick of the four nnseed y-probes
`A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)` of the displayed two-site
nnseed process. At a probe `q`, `S(q)` is the set of locks of six-neighbors
of `q` that formed at tick `≤ t(q)` and are not `q`. Same-tick partner
counts. Reverse holds if and only if some lock in `S(A)` is the vector
opposite of some lock in `S(B)`. Face holds if and only if some lock in
`S(C)` is the vector opposite of some lock in `S(D)`. Empty `S` on either
side of a comparison is `UNDEFINED`; nonempty with no opposite pair fails.
Occupancy `n` is not used. The probe's own incoming lock is not used. This
is not named-sign lettering. This is not a unique lock-vector leftover and
not a sum leftover. This is not the strictly-earlier leftover of already-
recorded six-neighbor lock sets on these same four y-probes. Uniqueness of
incoming locks is not required. Uniqueness of the lock set is not required.
`A` is a seed (`t=0`). Displayed, not adopted. This note does not write
existential opposite into Admissibility and does not attach a formation
member from same-tick-inclusive six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_yprobe_sametick_existential_opposite_reverse_face_2026_08_15.py`](../scripts/nnseed_yprobe_sametick_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used. A `Z^3` sum of those locks is a different
readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick-inclusive six-neighbor lock sets on the four nnseed y-probes, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_yprobe_sametick_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite same-tick-inclusive 6-NN locks on the four nnseed y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, and do not identify the sets with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks on the four nnseed y-probes; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
same-tick-inclusive six-neighbor lock sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(0,1,1)`. `A` is a seed.

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

That incoming lock is not a member of `S(q)` scored below.

## Named existential opposite from same-tick-inclusive six-neighbor locks

At the formation tick of a y-probe `q`, let `S(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ t(q)` and are not `q`. A
same-tick partner counts. The probe itself is excluded. This display does
not use occupancy `n`. It does not use the probe's own incoming lock.
Duplicate locks at two neighbors collapse in the set. The construction does
not require `S(q)` to be a singleton. It does not sum `S(q)`. It is not a
unique lock-vector leftover and not a sum leftover. A leftover strictly-
earlier collector on these same four y-probes dropped same-tick partners, so
`A` had an empty neighbor list.

Incoming `{±e_i}` tags of the probe itself are not `S(q)`. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis. Reverse and face are scored on existence of a pair
of lock vectors that add to zero. They are not scored on `{+,−}` names and
are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S(A) and some b in S(B) with a+b=(0,0,0)
face     <=>  some c in S(C) and some d in S(D) with c+d=(0,0,0)
```

If `S(A)` or `S(B)` is empty, reverse is `UNDEFINED`. Else reverse fails if
no such pair exists. If `S(C)` or `S(D)` is empty, face is `UNDEFINED`. Else
face fails if no such pair exists. The report is one of `hold`, `fail`, or
`UNDEFINED`. Because the scored object is a set, mixed neighbor locks remain
defined. Unique-vector leftover of the same lists would assign `UNDEFINED`
at `B` and would report reverse `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock sets at each y-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
y-probes. Formation ticks are `t(A)=t(0,1,0)=0`, `t(B)=t(1,1,1)=2`,
`t(C)=t(0,2,0)=3`, `t(D)=t(1,1,0)=1`. Those ticks locate the
same-tick-inclusive six-neighbor set. They are not occupancy kernels and are
not the reverse/face scoring.

At each formation tick the same-tick-inclusive six-neighbor lock list and
lock set are:

```text
A: +e_1 at (0, 0, 0);                                            S(A) = {+e_1}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1), +e_1 at (1, 1, 0);       S(B) = {+e_1, +e_3}
C: +e_2 at (1, 2, 0), +e_2 at (-1, 2, 0), +e_2 at (0, 1, 0),
   +e_2 at (0, 2, 1), +e_2 at (0, 2, -1);                         S(C) = {+e_2}
D: +e_2 at (0, 1, 0);                                            S(D) = {+e_2}
```

`A` is a seed at tick 0. Its same-tick partner is the origin, locking `+e_1`.
Same-tick counts, so the recorded neighbor lock set is that origin lock and
`S(A)={+e_1}`. `C`'s same-tick-inclusive neighbors all lock `+e_2`. `D`'s
recorded neighbor is the seed `(0, 1, 0)` locking `+e_2`. `B`'s recorded
neighbors lock two distinct vectors `+e_3` and `+e_1` (the same-tick site
`(1, 0, 1)` adds another `+e_1` and does not remove the mix). Unique
lock-vector lettering would report `UNDEFINED` at `B`. The lock set
`S(B)={+e_1, +e_3}` remains defined. A sum leftover would replace `S(B)` by
`(1, 0, 1)`. This display keeps the set and does not sum. They share a named
sign `+`; reducing to named sign would hide that mix.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`; `C` has four mixed self-incoming steps). That
non-uniqueness is not a unique-lettering of same-tick-inclusive neighbor
lock vectors. The lock sets are not identified with those incoming steps.
Uniqueness is not required.

`A`, `C`, and `D` each have a singleton recorded-neighbor lock set. `B` is
mixed and remains a set.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S(A)` and `b` in `S(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `S(A)={+e_1}` and
`S(B)={+e_1, +e_3}`. The pairs are `+e_1++e_1=(2,0,0)` and
`+e_1++e_3=(1,0,1)`. No aggregation of `B`'s `{+e_1,+e_3}` is opposite `A`'s
`+e_1`. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign `S(B)` mixed and would report reverse `UNDEFINED`
because `B` is mixed. That readout is a different object and is not used.
A strictly-earlier leftover of the same y-probes would leave `S(A)` empty
and would report reverse `UNDEFINED` because `A` is empty. Here same-tick
counts, so `S(A)` is nonempty. A sum leftover of the same lists would
replace the sets by `(1, 0, 0)` and `(1, 0, 1)` and would report reverse
fail for a different reason. A named-sign readout of the same neighbor
locks would assign `+` and `+` and would report reverse fail for a different
reason.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S(C)` and `d` in `S(D)` with
`c+d=(0,0,0)`. Both sets are nonempty: `S(C)={+e_2}` and `S(D)={+e_2}`, so
`+e_2+(+e_2)=(0,2,0)`, which is not `(0,0,0)`. Face does not hold.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

A leftover strictly-earlier existential-opposite display on the four
x-probes reports face `hold` because those lock sets are `{−e_2}` and
`{+e_2}`. Those probes are not these y-probes. Named-sign lettering of the
present lists is `C+/D+`. Face as `C+` and `D−` fails on those signs, and
the vectors are not opposites either. This note keeps the vectors.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify lock sets with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the recorded-neighbor lock set to be a singleton.
- It does not sum the recorded-neighbor lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not reprint the strictly-earlier leftover lock sets on these four
  y-probes.
- It does not reprint already-recorded six-neighbor lock sets on the four
  x-probes.
- It does not reprint already-recorded six-neighbor lock sets on the four
  z-probes.
- It does not attach a formation member from same-tick-inclusive
  six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock vectors. Reverse and face are not a sixteen-combination
  free lettering of the four y-probes.
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
nnseed process, the same-tick-inclusive six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| same-tick-inclusive six-neighbor lock sets at each y-probe formation tick | Theorem 1 |
| lock sets `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_3}`, `{+e_2}`, `{+e_2}` |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| strictly-earlier leftover on these y-probes | not this display |
| x-probe neighbor-lock existential opposite | not this display |
| z-probe neighbor-lock existential opposite | not this display |
| formation member from same-tick-inclusive six-neighbor locks | not attached |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of same-tick-inclusive six-neighbor locks on the four nnseed y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed existential-opposite same-tick-inclusive neighbor-lock reverse/face report on these four nnseed y-probes. |
| V3 | Recorded-neighbor lock sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors at formation and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not use occupancy `n`, and is not
the strictly-earlier leftover on these y-probes. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse would be `UNDEFINED` because `B` is mixed, while both sets are nonempty |
| strictly-earlier leftover on these y-probes | drop same-tick partners | refused; leftover assigned empty `S(A)` and reverse `UNDEFINED`; here `S(A)={+e_1}` |
| reverse/face from that leftover | reuse leftover reverse with empty `A` | different object; leftover reverse was `UNDEFINED` because `A` was empty; here reverse fails because no pair is opposite |
| sum of the same neighbor locks | replace `S` by the `Z^3` sum | refused; leftover; no aggregation of `B`'s `{+e_1,+e_3}` is opposite `A`'s `+e_1` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `C+/D+` fails face as `C+` and `D−` while the vectors remain `{+e_2}` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s seed lock `+e_2` into `S(A)` | refused; `S(A)={+e_1}` from the origin partner, not from `A`'s own incoming step |
| reverse/face from self-incoming vectors | reuse mixed incoming steps at `C` | different object; `C` would be mixed |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score y-probes by formation order | different object; not this display |
| x-probe neighbor-lock existential opposite | copy sets from the x-probes | refused; these are the y-probes `A=(0,1,0)`, `C=(0,2,0)`, `D=(1,1,0)` |
| z-probe neighbor-lock existential opposite | copy sets from the z-probes | refused; these are the y-probes |
| attach a formation member from same-tick-inclusive six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` and all four at `C` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from same-tick-inclusive
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, lock set of same-tick-inclusive six-neighbors,
existential opposite, four y-probes, seed `A` at tick 0, and reverse/face as
existence of a pair that sums to zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no singleton leftover, no
sum leftover, no strictly-earlier leftover, no formation attachment from
same-tick-inclusive six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a recorded-neighbor set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a same-tick seed partner exists at forming `A`, mixed
neighbor locks at `B` should make reverse `UNDEFINED`, the sets should be
replaced by their sums, reverse and face should copy the x-probe strictly-
earlier leftover (`fail`/`hold`), named signs should suffice because they
keep orientation, occupancy `n` should track that vector, and including
same-tick should not be a new display.

**Answer:** The named construction reports lock sets `{+e_1}`, `{+e_1, +e_3}`,
`{+e_2}`, `{+e_2}` at `A,B,C,D` from same-tick-inclusive six-neighbor locks.
Mixed remains a set. The construction does not sum. Occupancy `n` is not
used. Named signs lost the axis. No pair from `S(A)` and `S(B)` is opposite,
so reverse fails. Face fails. Unique-vector leftover of the same lists would
report reverse `UNDEFINED` because `B` is mixed; that leftover is not this
display. The bits remain displayed. Incoming-lock uniqueness is not
required. `A` is a seed; same-tick counts. This is not the strictly-earlier
leftover.

### N8 — cross-cycle echo

A leftover unique-vector same-tick-inclusive neighbor-lock display on these
same four nnseed y-probes closed reverse/face as `UNDEFINED`/`fail` because
`B` is mixed. This note is not that display: mixed remains a set, reverse
fails, and face fails. A leftover strictly-earlier unique-vector display on
these same four y-probes closed reverse/face as `UNDEFINED`/`fail` with empty
`S(A)`. This note is not that display: same-tick counts, so `S(A)={+e_1}`.
A leftover named-sign unique-letter display on these same four y-probes
closed reverse/face as `UNDEFINED`/`none` with named-sign letters
`UNDEFINED`, `+`, `+`, `+`. This note is not that display. A leftover
formdraw occupancy-kernel display on these same four y-probes closed
reverse/face as `UNDEFINED`/`some` because both `{+,−}` were kept at `n ≠ 0`
on formed sites. This note does not reuse occupancy `n`. An x-probe
strictly-earlier existential-opposite display closed reverse `fail` and face
`hold` on `{+e_1}`, `{+e_1,+e_3}`, `{−e_2}`, `{+e_2}`. Those probes are not
these y-probes; here face fails because `S(C)={+e_2}` and `S(D)={+e_2}`.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock
existential-opposite reverse/face reports on the four nnseed y-probes above.
FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the predicate
equals the unique singleton lock vector,” “the predicate equals the sum of
the lock set,” “the lock set equals the probe's own incoming step,” “the
predicate is the strictly-earlier leftover,” “bits are Admissibility,” “the
letter is occupancy `n`,” or “reverse holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, collects same-tick-inclusive six-neighbor locks at each
y-probe's formation tick, reads the lock sets at the four y-probes, and checks
Theorems 1--3. It also checks that the construction is not named-sign
lettering, that mixed sets remain defined, that the construction does not
sum, that the probe's own incoming step is not the lock set, that occupancy
`n` is not used, that the scoring is not the strictly-earlier leftover, and
that a formation member from same-tick-inclusive six-neighbor locks is not
attached. No runner cache is written.
