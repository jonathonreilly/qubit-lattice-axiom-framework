---
claim_id: nnseed_sametick_neighbor_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique same-tick-inclusive 6-NN lock vectors on the four nnseed x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py
---

# Unique Lock Vector From Same-Tick-Inclusive Six-Neighbor Locks On Four Nnseed X-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique lock vector in `{±e_i}` or `UNDEFINED` read from same-tick-inclusive
six-neighbor locks at the formation tick of the four nnseed x-probes
`A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)` of the displayed two-site
nnseed process, scored as reverse and face. The unique vector is the singleton
lock in `{±e_i}` of those neighbors formed at tick `≤ t(q)` and not equal to
`q`, or `UNDEFINED` if the lock list is empty or mixed. Same-tick partner
counts. Reverse holds iff `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. Face holds iff `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. Occupancy `n` is not used. The probe's own incoming lock
is not used. Uniqueness of incoming locks is not required. This is not the
strictly-earlier leftover of unique already-recorded six-neighbor lock vectors
on these same four x-probes. This is not unique `f(n)` and is not ndot.
Displayed, not adopted. This note does not write the unique vector into
Admissibility and does not attach a formation member from same-tick-inclusive
six-neighbor lock vectors. This is not a sixteen-combination free lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py`](../scripts/nnseed_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming locks are unit nearest-neighbor steps.
The unique letter scored here is a unique *vector* in `{±e_i}`, or
`UNDEFINED`. Named signs `{+,−}` of those locks are a different alphabet and
are not identified with the unique vector.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick-inclusive six-neighbor lock lists and the unique lock vector on the four nnseed x-probes, with reverse UNDEFINED and face hold; uniqueness of incoming locks is not claimed and the vectors are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_sametick_neighbor_lock_vector_reverse_face
target_blocker_text: "display reverse and face from the unique same-tick-inclusive 6-NN lock vector on the four nnseed x-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector into Admissibility, do not use occupancy n, and do not identify the vector with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock vectors from same-tick-inclusive six-neighbor locks on the four nnseed x-probes; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
same-tick-inclusive six-neighbor lock lists and unique vectors are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(0,1,1)`.

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

That incoming lock is not the unique vector scored below.

## Unique lock vector from same-tick-inclusive six-neighbor locks

At the formation tick of an x-probe `q`, collect the locks of six-neighbors of
`q` that formed at tick `≤ t(q)` and are not `q`. A same-tick partner counts.
The probe itself is excluded. This display does not use occupancy `n`. It does
not use the probe's own incoming lock.

If the set of those lock vectors is a singleton `{v}` subset `{±e_i}`, the
unique letter is `v`. Else (empty, mixed, or no recorded neighbor) the unique
letter is `UNDEFINED`.

A process-determined unique vector at a probe is a value in `{±e_i}` assigned
by that named construction from same-tick-inclusive six-neighbor locks, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a named sign of those locks, or of the probe's own
incoming step, with the unique vector is refused. Reverse and face are scored
on that unique vector. They are not scored on a sixteen-combination free
lettering of the four x-probes. Uniqueness of incoming locks is not required.

This is not a unique letter of occupancy `n`. It is not unique `f(n)` and is
not ndot. A leftover strictly-earlier unique-vector display on these same four
x-probes dropped same-tick partners, so `A` listed only two already-recorded
neighbors and `B` listed only two. Here same-tick partners at `A` and at `B`
count. Named-sign collapse of `{±e_i}` is a different alphabet and is not
used.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)
```

If a vector needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is not zero, the
comparison fails. The report is one of `hold`, `fail`, or `UNDEFINED`. Because
the unique letter is a single vector per probe, the scored comparisons are not
a sixteen-combination free lettering, and `some` is not produced. Leftover
named-sign reports used `all` / `some` / `none`; those are not this display.

Admissibility is not edited. Unique vectors are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique vector at each x-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
x-probes. Formation ticks are `t(A)=t(1,0,0)=2`, `t(B)=t(1,1,1)=2`,
`t(C)=t(2,0,0)=3`, `t(D)=t(1,1,0)=1`. Those ticks locate the
same-tick-inclusive six-neighbor set. They are not occupancy kernels and are
not the reverse/face scoring.

At each formation tick the same-tick-inclusive six-neighbor lock list and
unique vector are:

```text
A: +e_1 at (0, 0, 0), +e_1 at (1, 1, 0), +e_1 at (1, -1, 0),
   +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);                         L(A) = +e_1
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1), +e_1 at (1, 1, 0);       L(B) = UNDEFINED
C: −e_2 at (1, 0, 0);                                            L(C) = −e_2
D: +e_2 at (0, 1, 0);                                            L(D) = +e_2
```

`A` forms at tick 2. Its same-tick partners `(1,-1,0)`, `(1,0,1)`, and
`(1,0,-1)` each lock `+e_1`, matching the two strictly-earlier neighbors, so
the recorded-neighbor lock set remains the singleton `{+e_1}` and `L(A)` is `+e_1`.
`B` forms at the same tick; the same-tick site `(1,0,1)` adds another
`+e_1` and does not remove the mix with `+e_3` at `(0,1,1)`, so `L(B)` is
`UNDEFINED`. `C` has one recorded neighbor `A` locking `−e_2`. `D` has one
recorded neighbor, the seed `(0,1,0)` locking `+e_2`. The unique vector
letters at `C` and `D` are opposite axis vectors, so `L(C)+L(D)=(0,0,0)`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`). That non-uniqueness is not a unique-vectoring of
same-tick-inclusive neighbor locks. The unique vectors are not identified with
those incoming steps. Uniqueness is not required.

`A`, `C`, and `D` each have a singleton recorded-neighbor lock set. `B` is
`UNDEFINED`.

## Theorem 2 — reverse report

Reverse holds iff `L(A)` and `L(B)` are defined and `L(A)+L(B)=(0,0,0)`.
The unique vectors are `L(A)=+e_1` and `L(B)=UNDEFINED`. Reverse is
`UNDEFINED`.

Reverse: UNDEFINED

Report: `UNDEFINED`.

This is not `hold` and not `fail`. The strictly-earlier leftover also scored
reverse as `UNDEFINED` from mixed `+e_3` and `+e_1` at `B`, but from a shorter
list that dropped the same-tick partner `(1,0,1)`. Here that partner counts;
`B` remains mixed. Unique `f(n)`, ndot, occupancy-kernel `{+,−}` pairs, and a
sixteen-combination free lettering are different objects and are not used. A
named-sign readout of the same neighbor locks would assign `L(A)=+` and
`L(B)=+` and would report reverse fail. That readout is a different object
and is not used.

## Theorem 3 — face report

Face holds iff `L(C)` and `L(D)` are defined and `L(C)+L(D)=(0,0,0)`. The
unique vectors are `L(C)=−e_2` and `L(D)=+e_2`, so `L(C)+L(D)=(0,0,0)`. Face
holds.

Face: hold

Report: `hold`.

Displayed, not adopted. The vectors are not written into Admissibility.

Named-sign lettering of the same lists is `C−/D+`. Face as `C+` and `D−`
fails on those signs. The vectors remain opposites. This note keeps the
vectors.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique vectors with the probe's own incoming `{±e_i}`.
- It does not use occupancy `n`.
- It is not unique `f(n)`.
- It is not ndot.
- It does not reprint the named-sign unique letters on these four x-probes.
- It does not reprint the strictly-earlier leftover unique vectors on these
  four x-probes.
- It does not reprint same-tick-inclusive six-neighbor unique vectors on the
  four y-probes.
- It does not reprint already-recorded six-neighbor unique vectors on the
  four z-probes.
- It does not attach a formation member from same-tick-inclusive six-neighbor
  lock vectors.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock vectors.
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
nnseed process, the same-tick-inclusive six-neighbor lock lists, the unique
vector from those locks, and the reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| same-tick-inclusive six-neighbor lock lists at each x-probe formation tick | Theorem 1 |
| unique vector from those locks | Theorem 1; `+e_1`, `UNDEFINED`, `−e_2`, `+e_2` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| unique `f(n)` | not this display |
| ndot contraction letter | not this display |
| probe's own incoming lock as the letter | not used |
| strictly-earlier unique-vector leftover on these x-probes | not this display |
| named-sign unique letter leftover on these x-probes | not this display |
| y-probe same-tick unique vectors | not this display |
| z-probe neighbor-lock unique vectors | not this display |
| formation member from same-tick-inclusive six-neighbor lock vectors | not attached |
| sixteen-combination free lettering independent of neighbor-lock vectors | not enumerated |
| unique vectors as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock vector from same-tick-inclusive six-neighbor locks on the four nnseed x-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector same-tick-inclusive neighbor-lock reverse/face report on these four nnseed x-probes. |
| V3 | Recorded-neighbor lock lists, unique vectors, and the `UNDEFINED`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor locks at formation and names their common vector in `{±e_i}`. |
| V5 | It is not an adopted content rule: the vectors remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those vectors into
Admissibility, does not identify them with the probe's own incoming steps,
does not use occupancy `n`, is not unique `f(n)`, is not ndot, and is not the
strictly-earlier leftover on these x-probes. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| strictly-earlier unique-vector leftover on these x-probes | drop same-tick partners | refused; leftover listed two neighbors at `A` and two at `B`; here same-tick partners count |
| reverse/face from that leftover | reuse leftover reverse `UNDEFINED` and face `hold` from the shorter lists | different object; letters happen to match, lists do not |
| named-sign unique letter on these x-probes | map each lock `±e_i` to `{+,−}` | refused; unique vector at `B` is `UNDEFINED` because `+e_3` and `+e_1` are distinct |
| reverse/face from named signs | reuse leftover reverse fail `+/+` and face fail `C−/D+` | different object; named signs lost the axis; vector reverse is `UNDEFINED` and face holds |
| identify unique vector with the probe's own incoming `{±e_i}` | map `A`'s incoming `−e_2` to `L(A)` | refused; `L(A)=+e_1` from same-tick-inclusive neighbor locks |
| reverse/face from self-incoming vectors | reuse incoming `+e_1` at both `C` and `D` | different object; both `+e_1`; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| unique `f(n)` | assign one letter as a function of occupancy `n` | different object; not unique `f(n)` |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| reverse/face from formation-tick inequalities | score x-probes by formation order | different object; not this display |
| formdraw occupancy-kernel `{+,−}` pairs | keep both letters whenever occupancy `n ≠ 0` | different object; unique vector is a singleton or `UNDEFINED` |
| sixteen-combination free letters on the four x-probes | ignore neighbor-lock vectors and letter independently | different object; not enumerated |
| y-probe same-tick unique vectors | copy vectors from the y-probes | refused; these are the x-probes `A=(1,0,0)`, `C=(2,0,0)`, `D=(1,1,0)` |
| z-probe neighbor-lock unique vectors | copy vectors from the z-probes | refused; these are the x-probes |
| attach a formation member from same-tick-inclusive six-neighbor lock vectors | form the probes by a neighbor-lock vector instead of perp-step | refused; not attached |
| adopt vectors into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from same-tick-inclusive
six-neighbor lock vectors, and missing Record identification of the unique
vector bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, unique vector from same-tick-inclusive six-neighbor
locks, four x-probes, and reverse/face as vector-sum zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no unique `f(n)`, no ndot, no
named-sign collapse of `{±e_i}`, no formation attachment from
same-tick-inclusive six-neighbor lock vectors, and no Admissibility rewrite
are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique vector from recorded-neighbor locks | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique vectors and two hold/fail/`UNDEFINED` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide vectoring rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Including same-tick partners on these x-probes should copy the
strictly-earlier leftover because the unique letters still read `+e_1`,
`UNDEFINED`, `−e_2`, `+e_2`, reverse is still `UNDEFINED`, and face still
holds, so this is not a new display. Named signs should suffice because they
keep orientation, occupancy `n` should track the vector, and `A` should lock
its own incoming `−e_2`.

**Answer:** The named construction assigns unique vectors `+e_1`,
`UNDEFINED`, `−e_2`, `+e_2` at `A,B,C,D` from same-tick-inclusive
six-neighbor locks. The lock lists at `A` and at `B` include same-tick
partners that the leftover dropped. Occupancy `n` is not used. This is not
unique `f(n)` and is not ndot. Named signs lost the axis. Reverse is
`UNDEFINED` because `B` is mixed. Face holds. The bits remain displayed.
Incoming-lock uniqueness is not required. This is not the strictly-earlier
leftover.

### N8 — cross-cycle echo

A leftover unique-vector neighbor-lock display on these same four nnseed
x-probes closed reverse/face as `UNDEFINED`/`hold` with strictly-earlier
vectors `+e_1`, `UNDEFINED`, `−e_2`, `+e_2` from already-recorded neighbors
only. This note is not that display: same-tick counts, so `A` lists five
`+e_1` neighbors and `B` lists the extra same-tick `+e_1` at `(1,0,1)`, while
`L(B)` remains `UNDEFINED` from mixed `+e_3` and `+e_1`, reverse is
`UNDEFINED`, and face holds. A leftover named-sign neighbor-lock lettering on
the same lists reports `C−/D+` and face fail, having lost the axis. A leftover
unique-letter-of-occupancy display on the same four nnseed probes closed
reverse/face as `none`/`none` because occupancy at `C` and at `D` agrees. An
occupancy-kernel inner product on the same probes reports reverse and face
fail. Unique `f(n)` and ndot letterings are different objects and are not
used. A y-probe same-tick unique-vector display closed reverse `UNDEFINED` and
face `fail`; those probes are not these x-probes.

**Gate disposition:** PASS for the unique-vector same-tick-inclusive
six-neighbor-lock reverse/face reports on the four nnseed x-probes above.
FAIL / DO NOT SHIP for “the unique vector equals the probe's own incoming
step,” “the unique vector is the strictly-earlier leftover,” “vectors are
Admissibility,” “the letter is occupancy `n`,” “unique `f(n)`,” “ndot,” or
“reverse holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, collects same-tick-inclusive six-neighbor locks at each
x-probe's formation tick, reads the unique lock vector at the four probes, and
checks Theorems 1--3. It also checks that the construction is not the
strictly-earlier leftover, that the probe's own incoming step is not the unique
vector, that occupancy `n` is not used, and that a formation member from
same-tick-inclusive six-neighbor lock vectors is not attached. No runner cache
is written.
