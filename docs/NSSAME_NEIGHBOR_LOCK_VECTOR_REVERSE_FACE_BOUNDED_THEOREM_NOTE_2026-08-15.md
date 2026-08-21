---
claim_id: nssame_neighbor_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique already-recorded 6-NN lock vectors on the four nssame probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nssame_neighbor_lock_vector_reverse_face_2026_08_15.py
---

# Unique Neighbor-Lock Vector From Already-Recorded Six-Neighbor Locks On Four Nssame Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique lock vector in `{±e_i}` or `UNDEFINED` read from the
already-recorded six-neighbor locks at the formation tick of four probes of
the displayed two-site same-lock nssame process, scored as reverse and face.
The unique letter is the singleton lock vector of those neighbors, or
`UNDEFINED` if the lock list is empty or not a singleton. Occupancy `n` is
not used. The probe's own incoming lock is not used. Uniqueness of incoming
locks is not required. This is not sign-lettering. Displayed, not adopted.
This note does not write the unique vector into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks. This is
not a sixteen-combination free lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nssame_neighbor_lock_vector_reverse_face_2026_08_15.py`](../scripts/nssame_neighbor_lock_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a vector in `{±e_i}` when already-recorded
six-neighbor locks agree on that one vector, or `UNDEFINED`. Those two
alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of already-recorded six-neighbor lock lists and the unique lock vector on the four nssame probes, with reverse fail and face UNDEFINED; uniqueness of incoming locks is not claimed and the vectors are not adopted."
trace_class: frontier_discovery
target_claim_id: nssame_neighbor_lock_vector_reverse_face
target_blocker_text: "display reverse and face from unique already-recorded 6-NN lock vectors on the four nssame probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique lock vector into Admissibility, do not use occupancy n, and do not identify the letter with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock vectors from already-recorded six-neighbor locks on the four nssame probes; displayed, not adopted"
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
already-recorded six-neighbor lock lists and unique letters are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

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

That incoming lock is not the unique letter scored below.

This same-lock seed is outside the proper cubic orbit of the mixed-lock
two-site seed with letters `+e_1` and `+e_2`.

## Unique lock vector from already-recorded six-neighbor locks

At the formation tick of a probe `q`, collect the locks of already-recorded
six-neighbors of `q`. A neighbor is already recorded if and only if it formed
strictly earlier. The probe itself is still unread. This display does not use
occupancy `n`. It does not use the probe's own incoming lock.

If that set of lock vectors is a singleton `{v}` subset `{±e_i}`, the unique
letter is `v`. Else (empty, mixed, or no recorded neighbor) the unique letter
is `UNDEFINED`.

A process-determined unique letter at a probe is a value in `{±e_i}` assigned
by that named construction from already-recorded six-neighbor locks, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a lock vector of the probe's own incoming step with
the unique letter is refused. Reverse and face are scored on that unique
vector. They are not scored on a sixteen-combination free lettering of the
four probes. Uniqueness of incoming locks is not required.

This is not sign-lettering. Named-sign collapse of `{±e_i}` to `{+,−}` is a
different object: `+e_1` and `+e_3` share a named sign and are distinct
vectors. This is not a unique letter of occupancy `n`. Occupancy bits at a
probe can be well-defined while the recorded-neighbor lock vectors mix.
Neighbor-lock vectors need not exist whenever occupancy exists.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is the origin,
the comparison is `hold`. If both letters are defined and the vector sum is
not the origin, the comparison is `fail`.

Admissibility is not edited. Unique vectors are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique vector at each probe

Direct enumeration of the displayed nssame process on `B_3(0)` forms all four
probes. At each formation tick the already-recorded six-neighbor lock list
and unique letter are:

```text
A: +e_1 at (0, 0, 0), +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);  L(A) = +e_1
B: +e_3 at (0, 1, 1);                                                             L(B) = +e_3
C: −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);                      L(C) = UNDEFINED
D: +e_1 at (0, 1, 0), +e_1 at (1, 2, 0), +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);  L(D) = +e_1
```

`C`'s already-recorded neighbor is `A`. The incoming locks kept at `A` are
`+e_2`, `+e_3`, and `−e_3`. Those lock vectors are not a singleton, so
`L(C)` is `UNDEFINED`. `D`'s already-recorded neighbors all lock `+e_1`.

Incoming locks exist and need not be unique (`A` keeps three earliest
incoming steps). That non-uniqueness is not a unique-lettering of
already-recorded neighbor locks at `A`: those neighbor locks all equal
`+e_1`. The unique letters are not identified with those incoming steps.
Uniqueness is not required.

No probe has an empty recorded-neighbor lock list. Only `C` is `UNDEFINED`,
and that is from mixed lock vectors, not from emptiness.

## Theorem 2 — reverse report

Reverse holds iff `L(A)` and `L(B)` are defined and `L(A)+L(B)=(0,0,0)`. The
unique letters are `L(A)=+e_1` and `L(B)=+e_3`. Both are defined. Their sum
is `(1,0,1)`, not the origin. Reverse does not hold.

Report: `fail`.

This is not `hold` and not `UNDEFINED`. A named-sign readout of the probe's
own incoming step is a different object and is not used. A sixteen-combination
free lettering is a different object and is not used. Sign-lettering of the
same neighbor locks would collapse `L(B)` to `+` and is not this display.

## Theorem 3 — face report

Face holds iff `L(C)` and `L(D)` are defined and `L(C)+L(D)=(0,0,0)`. The
unique letter at `C` is `UNDEFINED`, and `L(D)=+e_1`. Face is `UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold` and not `fail`. Displayed, not adopted. The vectors are
not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique letters with the probe's own incoming `{±e_i}`.
- It does not use occupancy `n`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock vectors.
- It does not collapse lock vectors to named signs.
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
nssame process, the already-recorded six-neighbor lock lists, the unique
lock vector from those neighbor locks, and the reverse/face predicates are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site same-lock seed `+e_1/+e_1` |
| already-recorded six-neighbor lock lists at each probe formation tick | Theorem 1 |
| unique lock vector from those neighbor locks | Theorem 1; `+e_1`, `+e_3`, `UNDEFINED`, `+e_1` |
| reverse and face | Theorems 2–3; `fail` and `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| probe's own incoming lock as the letter | not used |
| named-sign collapse of `{±e_i}` | not used; not sign-lettering |
| formation member from already-recorded six-neighbor locks | not attached |
| sixteen-combination free lettering independent of neighbor-lock vectors | not enumerated |
| unique vectors as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock vector from already-recorded six-neighbor locks on the four nssame probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector neighbor-lock reverse/face report on these four nssame probes. |
| V3 | Recorded-neighbor lock lists, unique vectors, and the `fail`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads already-recorded six-neighbor locks at formation and names their common vector. |
| V5 | It is not an adopted content rule: the vectors remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those vectors into
Admissibility, does not identify them with the probe's own incoming steps,
and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify unique letter with the probe's own incoming `{±e_i}` | map `A`'s mixed incoming `{+e_2,+e_3,−e_3}` to `UNDEFINED` | refused; `L(A)=+e_1` from already-recorded neighbor locks |
| reverse/face from self-incoming lock vectors | reuse mixed incoming at `A` and at `D` | different object; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy at `C` can exist while `L(C)` is `UNDEFINED` |
| reverse/face from named signs `{+,−}` | collapse each lock to its named sign | refused; not sign-lettering; `L(B)=+e_3` is not `+` |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| both named rank-1 occupancy-kernel letters | keep `{+,−}` whenever occupancy `n ≠ 0` | different object; occupancy `n` is not used |
| sixteen-combination free letters on the four probes | ignore neighbor-lock vectors and letter independently | different object; not enumerated |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock vector instead of perp-step | refused; not attached |
| adopt vectors into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; the three earliest incoming steps at `A` are kept, and that mix is why `L(C)` is `UNDEFINED` |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique letter
bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site same-lock seed, perpendicular step rule,
incoming-step lock, unique letter from already-recorded six-neighbor lock
vectors, four probes, and reverse/face definitions are declared. No uniqueness
of incoming locks, no occupancy `n`, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail` and `UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from recorded-neighbor lock vectors | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique lock vectors and `hold`/`fail`/`UNDEFINED` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once an already-recorded neighbor exists at a forming probe, the
site should lock that unique vector as incoming content, reverse should hold
because the neighbor locks are unit steps, face should hold or at least fail
on a defined pair, and occupancy `n` should track that vector. Mixed incoming
locks at `A` should not make `C` `UNDEFINED`; some combination should still
score face.

**Answer:** The named construction assigns unique letters `+e_1`, `+e_3`,
`UNDEFINED`, `+e_1` at `A,B,C,D` from already-recorded six-neighbor lock
vectors. Occupancy `n` is not used. Reverse is `fail` because
`(+e_1)+(+e_3)≠0`. Face is `UNDEFINED` because the recorded-neighbor vectors
at `C` mix. The bits remain displayed. Incoming-lock uniqueness is not
required.

### N8 — cross-cycle echo

A named-sign neighbor-lock display on this same process collapses every
recorded-neighbor lock to `{+,−}` and can score reverse as `none` with
`L(A)=+` and `L(B)=+`. That is not this display: here `L(B)=+e_3` and reverse
is `fail`. A mixed-lock two-site neighbor-lock display on the same four
probes can close unique letters at every probe because that seed is not this
same-lock seed and is not in its proper cubic orbit. A leftover
unique-letter-of-occupancy display is a different object: occupancy bits need
not mix when lock vectors mix. A self-incoming lock-vector readout on this
same process sees mixed incoming steps at `A` and at `D`. This note does not
reuse those scorings.

**Gate disposition:** PASS for the unique-vector already-recorded
six-neighbor-lock reverse/face reports above. FAIL / DO NOT SHIP for “the
unique letter equals the probe's own incoming step,” “vectors are
Admissibility,” “the letter is occupancy `n`,” or “reverse/face holds on all
combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site same-lock
perp-step incoming-lock process, collects already-recorded six-neighbor locks
at each probe's formation tick, reads the unique lock vector at the four
probes, and checks Theorems 1--3. It also checks that the probe's own
incoming step is not the unique letter, that occupancy `n` is not used, and
that a formation member from already-recorded six-neighbor locks is not
attached. No runner cache is written.
