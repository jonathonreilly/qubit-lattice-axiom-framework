---
claim_id: nssame_sametick_neighbor_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the unique same-tick-inclusive 6-NN lock vector on the four nssame probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nssame_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py
---

# Unique Lock Vector From Same-Tick-Inclusive Six-Neighbor Locks On Four Nssame Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique lock vector in `{±e_i}` or `UNDEFINED` read from
same-tick-inclusive six-neighbor locks at the formation tick of four probes of
the displayed two-site same-lock nssame process, scored as reverse and face.
The unique vector is the singleton lock in `{±e_i}` of those neighbors formed
at tick `≤ t(q)` and not equal to `q`, or `UNDEFINED` if the lock list is
empty or mixed. Same-tick partner counts. Reverse holds iff `L(A)` and `L(B)`
are defined and `L(A)+L(B)=(0,0,0)`. Face holds iff `L(C)` and `L(D)` are
defined and `L(C)+L(D)=(0,0,0)`. Occupancy `n` is not used. The probe's own
incoming lock is not used. Uniqueness of incoming locks is not required. This
is not the strictly-earlier leftover of unique already-recorded six-neighbor
lock vectors on these same four x-probes. This is not unique `f(n)` and is not
ndot. Displayed, not adopted. This note does not write the unique vector into
Admissibility and does not attach a formation member from same-tick-inclusive
six-neighbor lock vectors. This is not a sixteen-combination free lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nssame_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py`](../scripts/nssame_sametick_neighbor_lock_vector_reverse_face_2026_08_15.py)

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
claim_type_reason: "Exact report of same-tick-inclusive six-neighbor lock lists and the unique lock vector on the four nssame probes, with reverse UNDEFINED and face UNDEFINED; uniqueness of incoming locks is not claimed and the vectors are not adopted."
trace_class: frontier_discovery
target_claim_id: nssame_sametick_neighbor_lock_vector_reverse_face
target_blocker_text: "display reverse and face from the unique same-tick-inclusive 6-NN lock vector on the four nssame probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector into Admissibility, do not use occupancy n, and do not identify the vector with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock vectors from same-tick-inclusive six-neighbor locks on the four nssame probes; displayed, not adopted"
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

These are the same x-probes as the nssame formdraw occupancy-kernel display
and as the strictly-earlier unique already-recorded six-neighbor lock-vector
display on this process. They are not the y-probes `A=(0,1,0)`, `C=(0,2,0)`
and not the z-probes `A=(0,0,1)`, `C=(0,0,2)`.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
the same lock `L(0)=L(0,1,0)=+e_1`.

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

This same-lock seed is outside the proper cubic orbit of the mixed-lock
two-site seed with letters `+e_1` and `+e_2`.

## Unique lock vector from same-tick-inclusive six-neighbor locks

At the formation tick of a probe `q`, collect the locks of six-neighbors of
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
lettering of the four probes. Uniqueness of incoming locks is not required.

This is not a unique letter of occupancy `n`. It is not unique `f(n)` and is
not ndot. A leftover strictly-earlier unique-vector display on these same four
x-probes dropped same-tick partners, so `A` and `D` excluded each other and
`B` excluded `(1,0,1)`. Named-sign collapse of `{±e_i}` is a different
alphabet and is not used.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)
```

If a vector needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `hold`, `fail`, or `UNDEFINED`. Because the
unique letter is a single vector per probe, the scored comparisons are not a
sixteen-combination free lettering, and `some` is not produced. Leftover
named-sign reports used `all` / `some` / `none`; those are not this display.

Admissibility is not edited. Unique vectors are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique vector at each probe

Direct enumeration of the displayed nssame process on `B_3(0)` forms all four
probes. Formation ticks are `t(A)=3`, `t(B)=2`, `t(C)=4`, `t(D)=3`. Those
ticks locate the same-tick-inclusive six-neighbor set. They are not occupancy
kernels and are not the reverse/face scoring.

At each formation tick the same-tick-inclusive six-neighbor lock list and
unique vector are:

```text
A: +e_1 at (0, 0, 0), −e_2 at (1, 1, 0), −e_3 at (1, 1, 0), +e_3 at (1, 1, 0),
   +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);  L(A) = UNDEFINED
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1);                      L(B) = UNDEFINED
C: −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0),
   +e_1 at (2, 1, 0);                                        L(C) = UNDEFINED
D: +e_1 at (0, 1, 0), +e_1 at (1, 2, 0), −e_3 at (1, 0, 0), +e_3 at (1, 0, 0),
   +e_2 at (1, 0, 0), +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);  L(D) = UNDEFINED
```

`A` and `D` form together at tick 3. Same-tick counts, so `D` is a recorded
neighbor of `A` and `A` is a recorded neighbor of `D`. `D`'s incoming locks
are `−e_2`, `+e_3`, and `−e_3`; those vectors mix with the already-recorded
`+e_1` neighbors of `A`, so `L(A)` is `UNDEFINED`. `A`'s incoming locks are
`+e_2`, `+e_3`, and `−e_3`; those mix with the already-recorded `+e_1`
neighbors of `D`, so `L(D)` is `UNDEFINED`. `B`'s same-tick partner `(1, 0, 1)`
locks `+e_1` while `(0, 1, 1)` locks `+e_3`, so `L(B)` is `UNDEFINED`. `C`'s
already-recorded neighbor is `A` with mixed incoming locks, and the same-tick
site `(2, 1, 0)` adds `+e_1`; the set remains mixed, so `L(C)` is `UNDEFINED`.

Incoming locks exist and need not be unique (`A` keeps three earliest incoming
steps; `D` keeps three). That non-uniqueness is not a unique-vectoring of
same-tick-inclusive neighbor locks. The unique vectors are not identified with
those incoming steps. Uniqueness is not required.

No probe has a singleton recorded-neighbor lock set. All four unique letters
are `UNDEFINED`.

## Theorem 2 — reverse report

Reverse holds iff `L(A)` and `L(B)` are defined and `L(A)+L(B)=(0,0,0)`.
The unique vectors are `L(A)=UNDEFINED` and `L(B)=UNDEFINED`. Reverse is
`UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold` and not `fail`. The strictly-earlier leftover scored reverse
as `fail` from `L(A)=+e_1` and `L(B)=+e_3`. Here same-tick partners mix both
lists, so both letters are `UNDEFINED` and reverse is `UNDEFINED`. Unique
`f(n)`, ndot, occupancy-kernel `{+,−}` pairs, and a sixteen-combination free
lettering are different objects and are not used.

## Theorem 3 — face report

Face holds iff `L(C)` and `L(D)` are defined and `L(C)+L(D)=(0,0,0)`. The
unique vectors are `L(C)=UNDEFINED` and `L(D)=UNDEFINED`. Face is `UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold` and not `fail`. Displayed, not adopted. The strictly-earlier
leftover already had `L(C)=UNDEFINED` and scored face as `UNDEFINED`; here
same-tick also makes `L(D)` mixed, so face remains `UNDEFINED` for a different
reason at `D`. The vectors are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique vectors with the probe's own incoming `{±e_i}`.
- It does not use occupancy `n`.
- It does not attach a formation member from same-tick-inclusive six-neighbor
  lock vectors.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock vectors.
- It does not collapse lock vectors to named signs.
- It does not reuse the strictly-earlier leftover unique-vector display on
  these four probes.
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
nssame process, the same-tick-inclusive six-neighbor lock lists, the unique
vector from those locks, and the reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site same-lock seed `+e_1/+e_1` |
| same-tick-inclusive six-neighbor lock lists at each probe formation tick | Theorem 1 |
| unique vector from those locks | Theorem 1; `UNDEFINED`, `UNDEFINED`, `UNDEFINED`, `UNDEFINED` |
| reverse and face | Theorems 2–3; `UNDEFINED` and `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| unique `f(n)` | not this display |
| ndot contraction letter | not this display |
| probe's own incoming lock as the letter | not used |
| strictly-earlier unique-vector leftover on these x-probes | not this display |
| named-sign unique letter leftover on these x-probes | not this display |
| y-probe neighbor-lock unique vectors | not this display |
| z-probe neighbor-lock unique vectors | not this display |
| formation member from same-tick-inclusive six-neighbor lock vectors | not attached |
| sixteen-combination free lettering independent of neighbor-lock vectors | not enumerated |
| unique vectors as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock vector from same-tick-inclusive six-neighbor locks on the four nssame probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector same-tick-inclusive neighbor-lock reverse/face report on these four nssame probes. |
| V3 | Recorded-neighbor lock lists, unique vectors, and the `UNDEFINED`/`UNDEFINED` reports are independently finite and exact. |
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
| strictly-earlier unique-vector leftover on these x-probes | drop same-tick partners | refused; leftover assigned `L(A)=+e_1`, `L(B)=+e_3`, reverse `fail`; here both are `UNDEFINED` |
| reverse/face from that leftover | reuse leftover reverse `fail` with defined `A` and `B` | different object; leftover reverse was `fail`; here reverse is `UNDEFINED` because `A` and `B` mix |
| named-sign unique letter on these x-probes | map each lock `±e_i` to `{+,−}` | refused; unique vector at `A` is `UNDEFINED` because `+e_1` and `−e_2` are distinct |
| reverse/face from named signs | collapse same-tick mix to one named sign | different object; named signs are not this display |
| identify unique vector with the probe's own incoming `{±e_i}` | map `A`'s mixed incoming `{+e_2,+e_3,−e_3}` to `UNDEFINED` and stop | refused; the unique letter is from neighbor locks, not from `A`'s own incoming step |
| reverse/face from self-incoming vectors | reuse mixed incoming at `A` and at `D` | different object; self-incoming at `B` is the singleton `+e_1` |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| unique `f(n)` | assign one letter as a function of occupancy `n` | different object; not unique `f(n)` |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| formdraw occupancy-kernel `{+,−}` pairs | keep both letters whenever occupancy `n ≠ 0` | different object; unique vector is a singleton or `UNDEFINED` |
| sixteen-combination free letters on the four probes | ignore neighbor-lock vectors and letter independently | different object; not enumerated |
| y-probe neighbor-lock unique vectors | copy vectors from the y-probes | refused; these are the x-probes `A=(1,0,0)`, `C=(2,0,0)`, `D=(1,1,0)` |
| z-probe neighbor-lock unique vectors | copy vectors from the z-probes | refused; these are the x-probes |
| attach a formation member from same-tick-inclusive six-neighbor lock vectors | form the probes by a neighbor-lock vector instead of perp-step | refused; not attached |
| adopt vectors into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; the three earliest incoming steps at `A` and at `D` are kept |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from same-tick-inclusive
six-neighbor lock vectors, and missing Record identification of the unique
vector bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site same-lock seed, perpendicular step rule,
incoming-step lock, unique vector from same-tick-inclusive six-neighbor locks,
four x-probes, and reverse/face definitions are declared. No uniqueness of
incoming locks, no occupancy `n`, no unique `f(n)`, no ndot, no named-sign
collapse of `{±e_i}`, no formation attachment from same-tick-inclusive
six-neighbor lock vectors, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` and `UNDEFINED` reports do not close that residual.

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

**Steelman:** Once a same-tick partner exists at forming `A`, the site should
lock that unique vector as incoming content, reverse should copy the
strictly-earlier leftover `fail` because `B` still has a recorded `+e_3`
neighbor, named signs at `A` should collapse the mix, and occupancy `n` or
unique `f(n)` or ndot should track that sign. Including same-tick should copy
the leftover at `C` and therefore should not be a new display.

**Answer:** The named construction assigns unique vectors `UNDEFINED`,
`UNDEFINED`, `UNDEFINED`, `UNDEFINED` at `A,B,C,D` from same-tick-inclusive
six-neighbor locks. Occupancy `n` is not used. This is not unique `f(n)` and
is not ndot. Named signs at `A` would mix `+` with `−` from `−e_2` and are not
used. Reverse is `UNDEFINED` because `A` and `B` are mixed. Face is
`UNDEFINED`. The bits remain displayed. Incoming-lock uniqueness is not
required. Same-tick counts. This is not the strictly-earlier leftover.

### N8 — cross-cycle echo

A leftover unique-vector neighbor-lock display on these same four nssame
x-probes closed reverse/face as `fail`/`UNDEFINED` with strictly-earlier
vectors `+e_1`, `+e_3`, `UNDEFINED`, `+e_1` because same-tick partners were
dropped. This note is not that display: same-tick counts, so `A` includes `D`,
`B` includes `(1, 0, 1)`, `D` includes `A`, every unique letter is
`UNDEFINED`, reverse is `UNDEFINED`, and face is `UNDEFINED`. A leftover
unique-letter neighbor-lock display on these same four x-probes collapses
`{±e_i}` to named signs. This note is not that display. A leftover formdraw
occupancy-kernel display on these same four x-probes reads occupancy `n` and
does not assign a unique vector. This note does not reuse occupancy `n`.
Unique `f(n)` and ndot letterings are different objects and are not used. A
y-probe unique-vector same-tick display closed reverse `UNDEFINED` and face
`fail`; those probes are not these x-probes.

**Gate disposition:** PASS for the unique-vector same-tick-inclusive
six-neighbor-lock reverse/face reports on the four nssame probes above.
FAIL / DO NOT SHIP for “the unique vector equals the probe's own incoming
step,” “the unique vector is the strictly-earlier leftover,” “vectors are
Admissibility,” “the letter is occupancy `n`,” “unique `f(n)`,” “ndot,” or
“reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site same-lock
perp-step incoming-lock process, collects same-tick-inclusive six-neighbor
locks at each probe's formation tick, reads the unique lock vector at the four
probes, and checks Theorems 1--3. It also checks that the probe's own incoming
step is not the unique vector, that occupancy `n` is not used, that the
scoring is not unique `f(n)` and not ndot, that the scoring is not named-sign
lettering, that the scoring is not the strictly-earlier leftover, and that a
formation member from same-tick-inclusive six-neighbor lock vectors is not
attached. No runner cache is written.
