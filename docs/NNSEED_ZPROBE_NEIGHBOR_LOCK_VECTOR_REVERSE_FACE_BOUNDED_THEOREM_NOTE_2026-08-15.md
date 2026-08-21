---
claim_id: nnseed_zprobe_neighbor_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique already-recorded 6-NN lock vectors on the four nnseed z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_zprobe_neighbor_lock_vector_reverse_face_2026_08_15.py
---

# Unique Lock Vector From Already-Recorded Six-Neighbor Locks On Four Nnseed Z-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique lock vector in `{±e_i}` or `UNDEFINED` read from already-recorded
six-neighbor locks at the formation tick of the four nnseed z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(0,1,1)` of the displayed two-site
nnseed process, scored as reverse and face. The unique vector is the singleton
lock in `{±e_i}` of those already-recorded neighbors, or `UNDEFINED` if the
lock list is empty or mixed. Reverse holds iff `L(A)` and `L(B)` are defined
and `L(A)+L(B)=(0,0,0)`. Face holds iff `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. Occupancy `n` is not used. The probe's own incoming lock
is not used. Uniqueness of incoming locks is not required. This is not the
named-sign unique letter leftover on these same four z-probes. This is not
unique `f(n)` and is not ndot. Displayed, not adopted. This note does not
write the unique vector into Admissibility and does not attach a formation
member from already-recorded six-neighbor lock vectors. This is not a
sixteen-combination free lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_zprobe_neighbor_lock_vector_reverse_face_2026_08_15.py`](../scripts/nnseed_zprobe_neighbor_lock_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming locks are unit nearest-neighbor steps.
The unique letter scored here is a vector in `{±e_i}`, or `UNDEFINED`. Named
signs `{+,−}` of those locks are a different alphabet and are not identified
with the unique vector.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of already-recorded six-neighbor lock lists and the unique lock vector on the four nnseed z-probes, with reverse UNDEFINED and face fail; uniqueness of incoming locks is not claimed and the vectors are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_zprobe_neighbor_lock_vector_reverse_face
target_blocker_text: "display reverse and face from the unique already-recorded 6-NN lock vector on the four nnseed z-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector into Admissibility, do not use occupancy n, and do not identify the vector with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock vectors from already-recorded six-neighbor locks on the four nnseed z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
already-recorded six-neighbor lock lists and unique vectors are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (0,1,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`.

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

## Unique lock vector from already-recorded six-neighbor locks

At the formation tick of a probe `q`, collect the locks of already-recorded
six-neighbors of `q`. A neighbor is already recorded if and only if it formed
strictly earlier. The probe itself is still unread. This display does not use
occupancy `n`. It does not use the probe's own incoming lock.

If the set of those lock vectors is a singleton `{v}` subset `{±e_i}`, the
unique letter is `v`. Else (empty, mixed, or no recorded neighbor) the unique
letter is `UNDEFINED`.

A process-determined unique vector at a probe is a value in `{±e_i}` assigned
by that named construction from already-recorded six-neighbor locks, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a named sign of those locks, or of the probe's own
incoming step, with the unique vector is refused. Reverse and face are scored
on that unique vector. They are not scored on a sixteen-combination free
lettering of the four z-probes. Uniqueness of incoming locks is not required.

This is not a unique letter of occupancy `n`. It is not unique `f(n)` and is
not ndot. A leftover named-sign unique-letter display on these same four
z-probes mapped each collected lock `±e_i` to `{+,−}` and assigned `+` at
every z-probe, including `B`, because `+e_3` and `+e_1` share a named sign.
The unique *vector* at `B` is `UNDEFINED` because those two locks are distinct
elements of `{±e_i}`. Named-sign reverse and face on that leftover were both
`none`. Vector reverse and face are a different pair of predicates.

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

## Theorem 1 — recorded-neighbor lock list and unique vector at each z-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
z-probes. Formation ticks are `t(A)=1`, `t(B)=2`, `t(C)=4`, `t(D)=1`. Those
ticks locate the already-recorded six-neighbor set. They are not occupancy
kernels and are not the reverse/face scoring.

At each formation tick the already-recorded six-neighbor lock list and unique
vector are:

```text
A: +e_1 at (0, 0, 0);                                      L(A) = +e_1
B: +e_3 at (0, 1, 1), +e_1 at (1, 1, 0);                    L(B) = UNDEFINED
C: +e_3 at (1, 0, 2), +e_3 at (-1, 0, 2),
   +e_3 at (0, -1, 2), +e_3 at (0, 0, 1);                   L(C) = +e_3
D: +e_2 at (0, 1, 0);                                      L(D) = +e_2
```

`A`'s already-recorded neighbor is the origin locking `+e_1`. `D`'s
already-recorded neighbor is the seed `(0, 1, 0)` locking `+e_2`. `C`'s
already-recorded neighbors all lock `+e_3`. `B`'s already-recorded neighbors
lock two distinct vectors `+e_3` and `+e_1`, so `L(B)` is `UNDEFINED`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`; `C` has three). That non-uniqueness is not a
unique-vectoring of already-recorded neighbor locks. The unique vectors are
not identified with those incoming steps. Uniqueness is not required.

`A`, `C`, and `D` each have a singleton recorded-neighbor lock set. Only `B`
is `UNDEFINED`.

## Theorem 2 — reverse report

Reverse holds iff `L(A)` and `L(B)` are defined and `L(A)+L(B)=(0,0,0)`.
The unique vectors are `L(A)=+e_1` and `L(B)=UNDEFINED`. Reverse is
`UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold` and not `fail`. A named-sign readout of the same neighbor
locks assigned `+` at both `A` and `B` and scored reverse as `none`; that
object is not used. Unique `f(n)`, ndot, occupancy-kernel `{+,−}` pairs, and a
sixteen-combination free lettering are different objects and are not used.

## Theorem 3 — face report

Face holds iff `L(C)` and `L(D)` are defined and `L(C)+L(D)=(0,0,0)`. The
unique vectors are `L(C)=+e_3` and `L(D)=+e_2`. Their sum is `(0,1,1)`, which
is not `(0,0,0)`. Face does not hold.

Report: `fail`.

Displayed, not adopted. The vectors are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique vectors with the probe's own incoming `{±e_i}`.
- It does not use occupancy `n`.
- It is not unique `f(n)`.
- It is not ndot.
- It does not reprint the named-sign unique letters on these four z-probes.
- It does not reprint already-recorded six-neighbor unique vectors on the
  four x-probes.
- It does not attach a formation member from already-recorded six-neighbor
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
nnseed process, the already-recorded six-neighbor lock lists, the unique
vector from those locks, and the reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| already-recorded six-neighbor lock lists at each z-probe formation tick | Theorem 1 |
| unique vector from those locks | Theorem 1; `+e_1`, `UNDEFINED`, `+e_3`, `+e_2` |
| reverse and face | Theorems 2–3; `UNDEFINED` and `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| unique `f(n)` | not this display |
| ndot contraction letter | not this display |
| probe's own incoming lock as the letter | not used |
| named-sign unique letter leftover on these z-probes | not this display |
| x-probe neighbor-lock unique vectors | not this display |
| formation member from already-recorded six-neighbor lock vectors | not attached |
| sixteen-combination free lettering independent of neighbor-lock vectors | not enumerated |
| unique vectors as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock vector from already-recorded six-neighbor locks on the four nnseed z-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector neighbor-lock reverse/face report on these four nnseed z-probes. |
| V3 | Recorded-neighbor lock lists, unique vectors, and the `UNDEFINED`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads already-recorded six-neighbor locks at formation and names their common vector in `{±e_i}`. |
| V5 | It is not an adopted content rule: the vectors remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those vectors into
Admissibility, does not identify them with the probe's own incoming steps,
does not use occupancy `n`, is not unique `f(n)`, is not ndot, and is not the
named-sign leftover on these z-probes. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named-sign unique letter on these z-probes | map each lock `±e_i` to `{+,−}` | refused; that leftover assigned `+` at `B`; unique vector at `B` is `UNDEFINED` |
| reverse/face from named signs | reuse leftover reverse `L(A)=+` and `L(B)=−` | different object; named-sign reverse was `none`; vector reverse is `UNDEFINED` |
| identify unique vector with the probe's own incoming `{±e_i}` | map `C`'s incoming `{−e_1,+e_2,+e_1}` to a unique vector | refused; those incoming steps are mixed; `L(C)=+e_3` from already-recorded neighbor locks |
| reverse/face from self-incoming vectors | reuse incoming steps at the four z-probes | different object; `C` would be `UNDEFINED` |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| unique `f(n)` | assign one letter as a function of occupancy `n` | different object; not unique `f(n)` |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| reverse/face from formation-tick inequalities | score z-probes by formation order | different object; not this display |
| formdraw occupancy-kernel `{+,−}` pairs | keep both letters whenever occupancy `n ≠ 0` | different object; unique vector is a singleton or `UNDEFINED` |
| sixteen-combination free letters on the four z-probes | ignore neighbor-lock vectors and letter independently | different object; not enumerated |
| x-probe neighbor-lock unique vectors | copy vectors from the x-probes | refused; these are the z-probes `A=(0,0,1)`, `C=(0,0,2)`, `D=(0,1,1)` |
| attach a formation member from already-recorded six-neighbor lock vectors | form the probes by a neighbor-lock vector instead of perp-step | refused; not attached |
| adopt vectors into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` and all three at `C` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor lock vectors, and missing Record identification of the unique
vector bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, unique vector from already-recorded six-neighbor
locks, four z-probes, and reverse/face definitions are declared. No uniqueness
of incoming locks, no occupancy `n`, no unique `f(n)`, no ndot, no named-sign
collapse of `{±e_i}`, no formation attachment from already-recorded
six-neighbor lock vectors, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` and `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique vector from recorded-neighbor locks | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique vectors and two hold/fail/`UNDEFINED` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide vectoring rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once an already-recorded neighbor exists at a forming z-probe,
the site should lock that unique vector as incoming content, reverse and face
should hold whenever named signs agree, and occupancy `n` or unique `f(n)` or
ndot should track that sign.

**Answer:** The named construction assigns unique vectors `+e_1`,
`UNDEFINED`, `+e_3`, `+e_2` at `A,B,C,D` from already-recorded six-neighbor
locks. Occupancy `n` is not used. This is not unique `f(n)` and is not ndot.
Named signs at `B` would agree and are not used. Reverse is `UNDEFINED`. Face
fails. The bits remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique-letter neighbor-lock display on these same four nnseed
z-probes closed reverse/face as `none`/`none` with named-sign letters `+`,
`+`, `+`, `+`. This note is not that display: the unique vectors are `+e_1`,
`UNDEFINED`, `+e_3`, `+e_2`, reverse is `UNDEFINED`, and face fails. A leftover
formdraw occupancy-kernel display on these same four z-probes closed
reverse/face as `some`/`some` because both `{+,−}` were kept at `n ≠ 0`. This
note does not reuse occupancy `n`. Unique `f(n)` and ndot letterings are
different objects and are not used.

**Gate disposition:** PASS for the unique-vector already-recorded
six-neighbor-lock reverse/face reports on the four nnseed z-probes above.
FAIL / DO NOT SHIP for “the unique vector equals the probe's own incoming
step,” “the unique vector is the named-sign leftover,” “vectors are
Admissibility,” “the letter is occupancy `n`,” “unique `f(n)`,” “ndot,” or
“reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, collects already-recorded six-neighbor locks at each
z-probe's formation tick, reads the unique lock vector at the four z-probes,
and checks Theorems 1--3. It also checks that the probe's own incoming step is
not the unique vector, that occupancy `n` is not used, that the scoring is not
unique `f(n)` and not ndot, that the scoring is not named-sign lettering, and
that a formation member from already-recorded six-neighbor lock vectors is not
attached. No runner cache is written.
