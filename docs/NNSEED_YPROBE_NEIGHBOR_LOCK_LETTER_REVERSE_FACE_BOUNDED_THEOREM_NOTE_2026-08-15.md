---
claim_id: nnseed_yprobe_neighbor_lock_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the unique letter of already-recorded 6-NN locks on the four nnseed y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_yprobe_neighbor_lock_letter_reverse_face_2026_08_15.py
---

# Unique Letter From Already-Recorded Six-Neighbor Locks On Four Nnseed Y-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{+,−}` or `UNDEFINED` read from the named signs of
already-recorded six-neighbor locks at the formation tick of four y-probes of
the displayed two-site nnseed process, scored as reverse and face. The unique
letter is the singleton named sign of those locks, or `UNDEFINED` if the lock
list is empty or mixed. Occupancy `n` is not used. The probe's own incoming
lock is not used. Uniqueness of incoming locks is not required. `A` is a seed
(`t=0`). Displayed, not adopted. This note does not write the unique letter
into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This is not a sixteen-combination free
lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_yprobe_neighbor_lock_letter_reverse_face_2026_08_15.py`](../scripts/nnseed_yprobe_neighbor_lock_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a `{+,−}` name of the common named sign of
already-recorded six-neighbor locks, or `UNDEFINED`. Those two alphabets are
not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of already-recorded six-neighbor lock lists and the unique named-sign letter on the four nnseed y-probes, with reverse UNDEFINED and face none; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_yprobe_neighbor_lock_letter_reverse_face
target_blocker_text: "display reverse and face from the unique letter of already-recorded 6-NN locks on the four nnseed y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique letter into Admissibility, do not use occupancy n, and do not identify the letter with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique letters from already-recorded six-neighbor locks on the four nnseed y-probes; displayed, not adopted"
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
already-recorded six-neighbor lock lists and unique letters are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

`A` is a seed. Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

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

That incoming lock is not the unique letter scored below.

## Named unique letter from already-recorded six-neighbor locks

At the formation tick of a y-probe `q`, collect the locks of already-recorded
six-neighbors of `q`. A neighbor is already recorded if and only if it formed
strictly earlier. A same-tick partner is not already-recorded. The probe
itself is still unread. This display does not use occupancy `n`. It does not
use the probe's own incoming lock.

Map each collected lock `±e_i` to its named sign:

```text
+    if the lock is in {+e_1, +e_2, +e_3}
−    if the lock is in {−e_1, −e_2, −e_3}.
```

If the set of those signs is a singleton `{s}`, the unique letter is `s`.
Else (empty, mixed, or no recorded neighbor) the unique letter is
`UNDEFINED`.

A process-determined unique letter at a probe is a value in `{+,−}` assigned
by that named construction from already-recorded six-neighbor locks, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a named sign of the probe's own incoming step with
the unique letter is refused. Reverse and face are scored on that unique
letter. They are not scored on a sixteen-combination free lettering of the
four y-probes. Uniqueness of incoming locks is not required.

This is not a unique letter of occupancy `n`. This is not an `n·v` contraction
letter. A leftover unique-letter-of-`n` display on four x-probes closed
`none`/`none` because occupancy at those `C` and `D` sites agreed. Neighbor-lock
letters need not agree with occupancy letters. This is also not the
self-incoming named-sign readout: `A` is a seed locking `+e_2`, while `C`
keeps mixed incoming steps.

Reverse and face (displayed):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `all`, `some`, `none`, or `UNDEFINED`.
Because the unique letter is a single value per probe, the scored comparisons
are not a sixteen-combination free lettering, and `some` is not produced.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique letter at each y-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
y-probes. Formation ticks are `t(A)=t(0,1,0)=0`, `t(B)=t(1,1,1)=2`,
`t(C)=t(0,2,0)=3`, `t(D)=t(1,1,0)=1`. At each formation tick the
already-recorded six-neighbor lock list and unique letter are:

```text
A: (empty);                                                      L(A) = UNDEFINED
B: +e_3 at (0, 1, 1), +e_1 at (1, 1, 0);                         L(B) = +
C: +e_2 at (1, 2, 0), +e_2 at (-1, 2, 0), +e_2 at (0, 1, 0),
   +e_2 at (0, 2, 1), +e_2 at (0, 2, -1);                         L(C) = +
D: +e_2 at (0, 1, 0);                                            L(D) = +
```

`A` is a seed at tick 0. Its six-neighbors are the same-tick partner at the
origin and later sites. Same-tick is not already-recorded, so the recorded
neighbor lock list is empty and `L(A)` is `UNDEFINED`. `C`'s already-recorded
neighbors all lock `+e_2`. `D`'s already-recorded neighbor is the seed
`(0, 1, 0)` locking `+e_2`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps; `C` has four). That non-uniqueness is not a unique-lettering of
already-recorded neighbor locks. The unique letters are not identified with
those incoming steps. Uniqueness is not required.

Only `A` is `UNDEFINED`, and that is from an empty recorded-neighbor lock
list, not from mixed named signs.

## Theorem 2 — reverse report

Reverse is `L(A)=+` and `L(B)=−`. The unique letters are `L(A)=UNDEFINED` and
`L(B)=+`. A needed letter is `UNDEFINED`.

Report: `UNDEFINED`.

This is not `all`, not `some`, and not `none`. A named-sign readout of
the probe's own incoming step is a different object and is not used. A
sixteen-combination free lettering is a different object and is not used.

## Theorem 3 — face report

Face is `L(C)=+` and `L(D)=−`. The unique letters are `L(C)=+` and
`L(D)=+`. Face does not hold.

Report: `none`.

This is not `all`, not `some`, and not `UNDEFINED`. Displayed, not adopted.
The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique letters with the probe's own incoming `{±e_i}`.
- It does not use occupancy `n`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock signs.
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
nnseed process, the already-recorded six-neighbor lock lists, the unique
letter from those named signs, and the reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| already-recorded six-neighbor lock lists at each y-probe formation tick | Theorem 1 |
| unique letter from the named signs of those locks | Theorem 1; `UNDEFINED`, `+`, `+`, `+` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `none` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| probe's own incoming lock as the letter | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| sixteen-combination free lettering independent of neighbor-lock signs | not enumerated |
| unique letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique letter from already-recorded six-neighbor locks on the four nnseed y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-letter neighbor-lock reverse/face report on these four nnseed y-probes. |
| V3 | Recorded-neighbor lock lists, unique letters, and the `UNDEFINED`/`none` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads already-recorded six-neighbor locks at formation and names their common sign. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with the probe's own incoming steps,
and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify unique letter with named sign of the probe's own incoming `{±e_i}` | map `A`'s seed lock `+e_2` to `+` | refused; `L(A)=UNDEFINED` from an empty already-recorded neighbor list |
| reverse/face from self-incoming named signs | reuse mixed incoming steps at `C` | different object; `C` keeps mixed incoming steps; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| both named rank-1 occupancy-kernel letters | keep `{+,−}` whenever occupancy `n ≠ 0` | different object; occupancy `n` is not used |
| sixteen-combination free letters on the four y-probes | ignore neighbor-lock signs and letter independently | different object; not enumerated |
| attach a formation member from already-recorded six-neighbor locks | form the y-probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept |
| treat a same-tick seed partner as already-recorded | count the origin lock at `A` | refused; already-recorded means strictly earlier |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique letter
bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, unique letter from already-recorded six-neighbor
lock signs, four y-probes, seed `A` at tick 0, and reverse/face definitions
are declared. No uniqueness of incoming locks, no occupancy `n`, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` and `none` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from recorded-neighbor lock signs | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique letters and `UNDEFINED`/`none` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once an already-recorded neighbor exists at a forming probe, the
site should lock that unique letter as incoming content, reverse and face
should hold on all combinations or be adopted as Admissibility content, and
occupancy `n` should track that sign. The seed partner at the origin should
count as already-recorded at `A`.

**Answer:** The named construction assigns unique letters `UNDEFINED`, `+`,
`+`, `+` at `A,B,C,D` from already-recorded six-neighbor lock signs. `A` is a
seed; same-tick is not already-recorded. Occupancy `n` is not used. Reverse
is `UNDEFINED`. Face does not hold. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique-letter already-recorded-neighbor-lock display on four
nnseed x-probes closed reverse/face as `none`/`none` with letters `+`, `+`,
`−`, `+`. Those probes are not these y-probes, and that display had no seed
probe. A leftover unique-letter-of-occupancy display is a different object:
this note does not use occupancy `n`. A self-incoming named-sign readout of
the seed lock at `A` would be `+`; this note reports `UNDEFINED` from an
empty recorded-neighbor list.

**Gate disposition:** PASS for the unique-letter already-recorded
six-neighbor-lock reverse/face reports above. FAIL / DO NOT SHIP for “the
unique letter equals the probe's own incoming step sign,” “letters are
Admissibility,” “the letter is occupancy `n`,” or “reverse/face holds on all
combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, collects already-recorded six-neighbor locks at each
y-probe's formation tick, reads the unique named-sign letter at the four
y-probes, and checks Theorems 1--3. It also checks that the probe's own
incoming step is not the unique letter, that occupancy `n` is not used, and
that a formation member from already-recorded six-neighbor locks is not
attached. No runner cache is written.
