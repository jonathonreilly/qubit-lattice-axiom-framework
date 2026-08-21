---
claim_id: three_site_zprobe_own_incoming_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the probe's own unique incoming lock vector on the four three-site z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_site_zprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py
---

# Own Incoming Lock Vector Reverse And Face On Four Three-Site Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{±e_i}` or `UNDEFINED` read from the probe's own
unique earliest incoming lock on four z-probes of the displayed three-site
perp-step incoming-lock process, scored as reverse and face. The unique
letter is that singleton incoming lock vector, or `UNDEFINED` if several
earliest incoming steps exist. Seeds keep their seed letters. `A` is not a
seed. Occupancy `n` is not used. Already-recorded six-neighbor locks are not
the letter. This is not named-sign lettering. Uniqueness of incoming locks is
not required. This is not leftover of the unique already-recorded
six-neighbor lock-vector lists on these same three-site z-probes. This is
not the four three-site y-probes. This is not the four three-site-seed
x-probes. This is not the four opposite-lock z-probes. This is not the perp
two-site seed `+e_1/+e_2` (different seed). Displayed, not adopted. This note
does not write the unique vector letter into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_site_zprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py`](../scripts/three_site_zprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a lock vector in `{±e_i}`, or `UNDEFINED`. Named
signs `{+,−}` are a coarser readout and are not the unique letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own unique incoming lock vectors on the four three-site z-probes, with reverse UNDEFINED and face UNDEFINED; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: three_site_zprobe_own_incoming_lock_vector_reverse_face
target_blocker_text: "display reverse and face from the probe's own unique incoming lock vector on the four three-site z-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector letter into Admissibility, do not reduce to named sign, do not use occupancy n, do not use already-recorded six-neighbor locks as the unique letter, and do not treat this as leftover of the three-site z-probe neighbor-lock lists, the three-site y-probes, the three-site-seed x-probes, the opposite-lock z-probes, or the perp two-site seed."
conditional_surface_status: "exact on B_3(0) for own unique incoming lock-vector letters on the four three-site z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose own unique
incoming lock vectors are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the three-record set `{0, (0,1,0), (1,0,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(1,0,0)=+e_2`. Seeds
have their seed letters. This seed is not the two-site opposite-lock seed
`+e_1/−e_1`. This seed is not the perp two-site seed `+e_1/+e_2`.

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

## Named unique letter from the probe's own incoming lock

Letter at a formed probe `q` is `q`'s own unique incoming lock: the singleton
earliest incoming step in `{±e_i}`. If several earliest incoming steps exist,
the unique letter is `UNDEFINED`. Seeds have their seed letters. Probe `A` is
not a seed. This display does not use occupancy `n`. It does not use
already-recorded six-neighbor locks as the unique letter. It does not use a
six-neighbor star.

A process-determined unique letter at a probe is a value in `{±e_i}` assigned
by that named construction from the probe's own unique incoming lock, or
`UNDEFINED`. Already-recorded six-neighbor lock vectors are not that
assignment. Identifying a named sign of those locks with the unique letter is
refused: named-sign lettering lost the axis. Reverse and face are scored on
the unique lock vector. They are not scored on `{+,−}` names.

This is not leftover of the unique already-recorded six-neighbor lock-vector
lists on these same three-site z-probes: that leftover assigned `L(A)=+e_1`
from the already-recorded neighbor at the origin and reported reverse fail
with face fail. Record readout at A is A's own incoming lock `+e_3`. Record
readout at C is C's own incoming lock.

This is not the four three-site y-probes: those sites used seed `A=(0,1,0)`
with letter `−e_1`.

This is not the four three-site-seed x-probes: those sites used seed
`A=(1,0,0)` with letter `+e_2`.

This is not the four opposite-lock z-probes: those sites used the two-site
opposite-lock seed `{0,(0,1,0)}` and reported reverse fail from unique
incoming `+e_1` at `B`. Here the third seed lock `+e_2` mixes the earliest
incoming set at `B` and forms `D` at tick 1 with incoming `+e_3`.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is the origin,
the comparison is `hold`. If both letters are defined and the vector sum is
not the origin, the comparison is `fail`. The report is one of `hold`,
`fail`, or `UNDEFINED`.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — own incoming lock (or UNDEFINED) at each z-probe

Direct enumeration of the displayed three-site process on `B_3(0)` forms all
four z-probes. Formation ticks locate the earliest incoming set. They are
not occupancy kernels and are not the reverse/face scoring. Formation ticks
are `t(A)=1`, `t(B)=2`, `t(C)=4`, `t(D)=1`. The own unique incoming lock
vector at each z-probe is:

```text
A: incoming +e_3;                     L(A) = +e_3
B: incoming +e_1, +e_2;               L(B) = UNDEFINED
C: incoming +e_1, +e_2;               L(C) = UNDEFINED
D: incoming +e_3;                     L(D) = +e_3
```

`A` forms at tick 1 from the origin by the incoming step `+e_3`. That step is
a singleton in `{±e_i}`, so `L(A)=+e_3`. `A` is not a seed. `B` has two
earliest incoming steps `+e_1` and `+e_2`. Those vectors are not a singleton,
so `L(B)` is `UNDEFINED`. `C` has two earliest incoming steps `+e_1` and
`+e_2`. Those vectors are not a singleton, so `L(C)` is `UNDEFINED`. `D`
forms at tick 1 from the third seed `(1,0,0)` by the incoming step `+e_3`.
That step is a singleton in `{±e_i}`, so `L(D)=+e_3`.

Record readout at A is A's own incoming lock, not an already-recorded
neighbor lock at the origin. Record readout at C is C's own incoming lock.

Incoming locks exist and need not be unique. Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. The unique letters are `L(A)=+e_3` and
`L(B)=UNDEFINED`. Reverse is `UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. The leftover unique already-recorded
six-neighbor lock-vector lists on these same three-site z-probes assigned
`L(A)=+e_1` and `L(B)=+e_3` and reported reverse fail. That leftover is a
different object: here Record readout at A is A's own incoming lock `+e_3`,
not the origin's already-recorded `+e_1`. The own unique incoming lock-vector
display on the four three-site y-probes assigned `L(A)=−e_1` from the seed
letter at `(0,1,0)` and reported reverse `UNDEFINED` because seed `A` was
`(0,1,0)`. Those are not these z-probes. The own unique incoming lock-vector
display on the four opposite-lock z-probes assigned `L(A)=+e_3` and
`L(B)=+e_1` and reported reverse fail. Those used a different seed: here `B`
mixes `+e_1` and `+e_2`. A named-sign readout of `A` would assign `+` and
would hide the axis. That readout is a different object and is not used.
Reverse UNDEFINED is displayed, not adopted.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. The unique letters are `L(C)=UNDEFINED` and
`L(D)=+e_3`. Face is `UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The letters are not written into Admissibility.

This is not `hold` and not `fail`. The leftover already-recorded
six-neighbor lists on these three-site z-probes assigned `L(C)=+e_3` and
`L(D)=+e_2` and reported face fail. That leftover is a different object: here
Record readout at C is C's own mixed incoming lock, so face is `UNDEFINED`.
On the perp two-site seed `+e_1/+e_2` (different seed), an own-incoming
z-probe readout assigned `D` the letter `+e_1`. Here `D` locks `+e_3` from
the third seed, and `C` mixes two earliest incoming steps, so face is
`UNDEFINED`.

## What this note does not claim

- It does not require a unique incoming lock.
- It does not use already-recorded six-neighbor locks as the unique letter.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not use a six-neighbor star.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a free lettering independent of own incoming lock
  vectors.
- It does not enlarge the host beyond `B_3(0)`.
- It does not treat this display as leftover of the unique already-recorded
  six-neighbor lock-vector lists on these same three-site z-probes.
- It does not treat this display as the four three-site y-probes.
- It does not treat this display as the four three-site-seed x-probes.
- It does not treat this display as the four opposite-lock z-probes.
- It does not treat this display as the perp two-site seed `+e_1/+e_2`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It does not adopt reverse or face as an Admissibility rule.

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
three-site process, the own unique incoming lock vectors, and the reverse/face
predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three-site seed `+e_1/−e_1/+e_2` |
| own unique incoming lock vector at each z-probe | Theorem 1; `+e_3`, `UNDEFINED`, `UNDEFINED`, `+e_3` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| already-recorded six-neighbor locks as the letter | not used |
| leftover of those neighbor-lock lists on these z-probes | different object; reverse fail and face fail are not this reverse or face |
| four three-site y-probes | different sites; seed `A=(0,1,0)` is not this formed `A` |
| four three-site-seed x-probes | different sites; seed `A=(1,0,0)` is not this formed `A` |
| four opposite-lock z-probes | different seed; reverse fail is not this reverse |
| perp two-site seed `+e_1/+e_2` | different seed; not this display |
| six-neighbor star | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| unique letters as Admissibility content | not adopted |
| reverse or face as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: the probe's own unique incoming lock vector on the four three-site z-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-incoming-lock-vector reverse/face report on these four three-site z-probes. |
| V3 | Own incoming lock sets, unique vector letters, and the `UNDEFINED`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own unique incoming lock and scores the vector sum. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not use already-recorded six-neighbor locks as the unique
letter, does not reduce them to named signs, does not use occupancy `n`, and
does not use a six-neighbor star. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| leftover unique already-recorded six-neighbor lock vectors on these z-probes | assign `L(A)=+e_1` from the origin neighbor and report reverse fail with face fail | refused; Record readout at A is A's own incoming lock `+e_3`, reverse `UNDEFINED`, face `UNDEFINED` |
| own unique incoming lock on the four three-site y-probes | reuse seed `A=(0,1,0)` with letter `−e_1` | refused; these z-probes have formed `A=(0,0,1)` |
| own unique incoming lock on the four three-site-seed x-probes | reuse seed `A=(1,0,0)` with letter `+e_2` | refused; these z-probes have formed `A=(0,0,1)` |
| own unique incoming lock on the four opposite-lock z-probes | reuse unique incoming `+e_1` at `B` and report reverse fail | refused; here `B` mixes `+e_1` and `+e_2` because of the third seed |
| own unique incoming lock on the perp two-site seed | reuse `+e_1/+e_2` | different seed; not this three-site display |
| named-sign lettering of the same incoming locks | map `±e_i` to `{+,−}` | refused; lost the axis |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; occupancy `n` is not used |
| six-neighbor star | score a star of neighbor locks as the letter | refused; a six-neighbor star is not used |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept, and both at `C` are kept |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique vector
letter are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three-site seed locks `+e_1`, `−e_1`, and `+e_2`,
perpendicular step rule, incoming-step lock, unique letter from the probe's
own unique incoming lock, four z-probes, formed `A` at tick 1, and reverse/face
as vector-sum zero are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no already-recorded six-neighbor lock as the
letter, no six-neighbor star, and no Admissibility rewrite are silently
assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from own incoming lock | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique letters and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Three-site seed locks should force reverse to hold as an adopted
rule, leftover neighbor-lock lists on these z-probes should be the unique
letter because they already scored the same four sites and reported reverse
fail with face fail, the opposite-lock z-probe own incoming readout should be
imported because reverse failed there, the three-site y-probe own incoming
readout should be imported because those y-probes already used own incoming
locks, named signs should suffice because they keep orientation, occupancy `n`
should track that vector, and face should fail because leftover `C` and `D`
were unique.

**Answer:** The named construction assigns unique letters `+e_3`,
`UNDEFINED`, `UNDEFINED`, `+e_3` at `A,B,C,D` from each probe's own unique
incoming lock. `A` is not a seed. Occupancy `n` is not used. Named signs lost
the axis. Reverse is `UNDEFINED` because `B` mixes `+e_1` and `+e_2`; it is
not adopted. Face is `UNDEFINED` because `C` mixes. The leftover neighbor-lock
lists on these z-probes are a different object. The four three-site y-probes
are different sites. The four three-site-seed x-probes are different sites.
The four opposite-lock z-probes are a different seed. The perp two-site seed
is a different seed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique already-recorded six-neighbor lock-vector display on these
same three-site z-probes assigned `L(A)=+e_1`, `L(B)=+e_3`, `L(C)=+e_3`,
`L(D)=+e_2` and reported reverse fail with face fail. An own unique incoming
lock-vector display on the four three-site y-probes assigned `L(A)=−e_1`,
`L(B)=UNDEFINED`, `L(C)=+e_2`, `L(D)=UNDEFINED` and reported reverse
`UNDEFINED` with face `UNDEFINED`. An own unique incoming lock-vector display
on the four three-site-seed x-probes assigned `L(A)=+e_2`, `L(B)=UNDEFINED`,
`L(C)=+e_1`, `L(D)=UNDEFINED` and reported reverse `UNDEFINED` with face
`UNDEFINED`. An own unique incoming lock-vector display on the four
opposite-lock z-probes assigned `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`,
`L(D)=+e_1` and reported reverse fail with face `UNDEFINED`. An own unique
incoming lock-vector display on the perp two-site seed `+e_1/+e_2` (different
seed) is a different seed. This note is not those displays: Record readout at
each z-probe is that probe's own incoming lock, reverse `UNDEFINED` because
`A` locks `+e_3` and `B` mixes, and face is `UNDEFINED` because `C` mixes.

**Gate disposition:** PASS for the own unique incoming lock-vector
reverse/face reports on the four three-site z-probes above. FAIL / DO NOT SHIP
for “the unique letter equals the named sign,” “the unique letter equals an
already-recorded six-neighbor lock,” “letters are Admissibility,” “the letter
is occupancy `n`,” “reverse holds,” “face holds,” “this is leftover of the
three-site z-probe neighbor-lock lists,” “this is the four three-site
y-probes,” “this is the four three-site-seed x-probes,” or “this is the four
opposite-lock z-probes.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-site perp-step
incoming-lock process, reads each z-probe's own unique incoming lock vector at
the four z-probes, and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that already-recorded six-neighbor
locks are not the unique letter, that occupancy `n` is not used, that a
six-neighbor star is not used, that the seed is not the two-site opposite-lock
seed, that the seed is not the perp two-site seed, that the probes are not the
four three-site y-probes, that the probes are not the four three-site-seed
x-probes, and that a formation member from already-recorded six-neighbor
locks is not attached. No runner cache is written.
