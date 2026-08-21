---
claim_id: nnseed_yprobe_neighbor_lock_sum_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the sum of already-recorded 6-NN locks on the four nnseed y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_yprobe_neighbor_lock_sum_reverse_face_2026_08_15.py
---

# Sum Of Already-Recorded Six-Neighbor Locks On Four Nnseed Y-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the vector sum in `Z^3` of already-recorded six-neighbor incoming
locks at the formation tick of the four nnseed y-probes `A_y=(0,1,0)`,
`B=(1,1,1)`, `C_y=(0,2,0)`, `D_y=(1,1,0)` of the displayed two-site nnseed
process, scored as reverse and face. `A_y` is a seed. Already-recorded means
strictly earlier; the same-tick partner is not already-recorded. If the list
of those locks is empty, the letter is `UNDEFINED`. Reverse holds if and only
if both letters are defined and sum to `(0,0,0)`. Face holds if and only if
both letters are defined and sum to `(0,0,0)`. Uniqueness is not required.
This is not a unique leftover vector, not occupancy-kernel `n`, and not a
named `{+,−}` PVM letter. Displayed, not adopted. This note does not write
the sum letter into Admissibility and does not attach a formation member
beyond the displayed perp-step incoming-lock process.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_yprobe_neighbor_lock_sum_reverse_face_2026_08_15.py`](../scripts/nnseed_yprobe_neighbor_lock_sum_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. The scored letter at a probe is the vector sum of already-recorded
six-neighbor locks, or `UNDEFINED`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of the sum of already-recorded 6-NN locks on the four nnseed y-probes, with reverse UNDEFINED because S(A_y) is empty and face fail because L(C_y)+L(D_y)=(0,6,0); uniqueness is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_yprobe_neighbor_lock_sum_reverse_face
target_blocker_text: "display reverse and face from the sum of already-recorded 6-NN locks on the four nnseed y-probes"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the sum letter into Admissibility, and do not replace it by leftover unique vector, occupancy-kernel n, or PVM letters."
conditional_surface_status: "exact on B_3(0) for the sum of already-recorded 6-NN locks on the four nnseed y-probes; displayed, not adopted"
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
already-recorded six-neighbor lock sums are scored:

```text
A_y = (0,1,0),  B = (1,1,1),  C_y = (0,2,0),  D_y = (1,1,0).
```

These are the nsiso y-probe sites. Formation ticks of those sites locate the
already-recorded six-neighbor set. The ticks are not the reverse/face scoring.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`.

`A_y` is the seed site `(0,1,0)`. It is already formed at tick 0. It is not
re-formed by a later incoming step.

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
`q`. A seed site is already formed, so it is not re-formed.

## Named sum letter

At the formation tick of a probe `q`, let `S` be the list of incoming locks
of already-recorded six-neighbors of `q`. A neighbor is already-recorded if
and only if it formed strictly earlier. The probe itself is still unread.
The same-tick partner is not already-recorded. In particular, at `t(A_y)=0`
the origin is the same-tick partner of `A_y` and does not contribute a lock
to `S`.

Walk the six steps in the order `+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`. For each
already-recorded neighbor, append that neighbor's incoming lock vectors, in
sorted coordinate order, to `S`. If a neighbor carries several earliest
incoming locks, every such lock is appended. Uniqueness is not required.

If `S` is empty, the letter is `UNDEFINED`. Else the letter is the vector
sum of `S` in `Z^3`.

That sum is not occupancy-kernel `n`. It is not a unique leftover vector of
an unrecorded six-neighbor step. It is not a named rank-1 PVM letter in
`{+,−}`. Incoming `{±e_i}` tags of the probe itself are not that assignment.

Reverse and face (displayed):

```text
reverse  <=>  L(A_y) and L(B) are defined and L(A_y)+L(B)=(0,0,0)
face     <=>  L(C_y) and L(D_y) are defined and L(C_y)+L(D_y)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. Otherwise the report is `hold` or `fail`.

Admissibility is not edited. The sum letters are not written into
Admissibility.

## Theorem 1 — lock list and sum letter at each y-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
y-probes. Formation ticks are `t(A_y)=t(0,1,0)=0`, `t(B)=t(1,1,1)=2`,
`t(C_y)=t(0,2,0)=3`, `t(D_y)=t(1,1,0)=1`. Those ticks match the nsiso y-probe
formation order and locate the already-recorded set. They are not the
reverse/face letter.

At the seed tick of `A_y` the already-recorded six-neighbor lock list is
empty, so no sum letter is assigned. At the formation ticks of `B`, `C_y`,
and `D_y` the list is nonempty, so the letter is the vector sum:

```text
S(A_y) = empty,                                      L(A_y) = UNDEFINED
S(B)   = (+e_3, +e_1),                               L(B)   = (1, 0, 1)
S(C_y) = (+e_2, +e_2, +e_2, +e_2, +e_2),             L(C_y) = (0, 5, 0)
S(D_y) = (+e_2),                                     L(D_y) = (0, 1, 0)
```

Already-recorded six-neighbors at those formation ticks:

- `A_y`: no already-recorded six-neighbor; the origin is the same-tick partner
  and is not already-recorded;
- `B`: `(0,1,1)` locks `+e_3` and `(1,1,0)` locks `+e_1`;
- `C_y`: `(1,2,0)`, `(-1,2,0)`, `(0,1,0)`, `(0,2,1)`, and `(0,2,-1)` all lock
  `+e_2`;
- `D_y`: `(0,1,0)` locks `+e_2`.

`A_y` carries the seed lock `+e_2`. Incoming locks of the grown sites exist
and need not be unique (`B` has two earliest incoming steps; `C_y` has four).
That non-uniqueness is not the sum letter. The sum letter is read from
already-recorded neighbors, not from the probe's own incoming steps.

On `C_y` there is a unique unrecorded six-neighbor step `+e_2`. That leftover
vector is not `L(C_y)=(0,5,0)`. This display is not the unique-vector leftover
construction.

## Theorem 2 — reverse report

Reverse is `L(A_y)+L(B)=(0,0,0)` with both letters defined. `L(A_y)` is
`UNDEFINED` because `S(A_y)` is empty. A letter needed by the comparison is
`UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold` and not `fail`. A unique leftover vector, an
occupancy-kernel letter, a named `{+,−}` PVM letter, a named-sign readout of
the probe's own incoming steps, and a formation-tick inequality are different
objects and are not used.

## Theorem 3 — face report

Face is `L(C_y)+L(D_y)=(0,0,0)` with both letters defined. Both letters are
defined: `L(C_y)=(0,5,0)` and `L(D_y)=(0,1,0)`, so

```text
L(C_y)+L(D_y) = (0, 6, 0) ≠ (0, 0, 0).
```

Report: `fail`.

This is not `hold` and not `UNDEFINED`. Displayed, not adopted. The letters
are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock of the probe itself.
- It is not a unique leftover vector.
- It is not occupancy-kernel `n`.
- It is not a named `{+,−}` PVM letter.
- It does not treat the same-tick seed partner as already-recorded.
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
only as the quoted one-site algebra. It uses Record only as a boundary: a
present lock is content. It does not rewrite Admissibility. The nnseed
process, the already-recorded six-neighbor lock list, the vector-sum letter,
and the reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| already-recorded 6-NN lock list `S` and vector-sum letter at each y-probe | Theorem 1; `S(A_y)` empty; `L(C_y)=(0,5,0)`, `L(D_y)=(0,1,0)` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `fail` |
| unique incoming lock of the probe | not required |
| unique leftover vector | not this display |
| occupancy-kernel `n` | not this display |
| named `{+,−}` PVM letter | not this display |
| same-tick seed partner counted as already-recorded | not executed |
| sum letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: sum of already-recorded 6-NN locks on the four nnseed y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed already-recorded 6-NN lock-sum reverse/face report on these four nnseed y-probes. |
| V3 | Lock lists, vector sums, and the `UNDEFINED`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it sums already-recorded neighbor locks at formation. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not replace them by a unique leftover vector, does not
read occupancy-kernel `n`, does not assign `{+,−}` PVM letters, and does not
count the same-tick seed partner as already-recorded. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique leftover vector | take the unique unrecorded six-neighbor step | different object; leftover at `C_y` is `+e_2`, not `(0,5,0)` |
| occupancy-kernel `n` | score `n_μ=(o_{+μ}−o_{−μ})/3` | different object; not this display |
| named `{+,−}` PVM letter | assign both `P_±` whenever `n≠0` | different object; the letter here is a vector in `Z^3` |
| reverse/face from the probe's own incoming steps | reuse the probe lock as the letter | different object; `S` is neighbor locks |
| reverse/face from formation-tick inequalities | score y-probes by nsiso tick order | different object; ticks locate `S` only |
| count same-tick seed partner as already-recorded | put `L(0)=+e_1` into `S(A_y)` | refused; already-recorded is strictly earlier |
| adopt letters into Admissibility | rewrite the local rule by the sum | refused; displayed, not adopted |
| unique incoming lock required | demand one lock per grown site | uniqueness is not required |

### N2 — wall independence

Missing physical adoption, missing leftover identification, and missing Record
identification of the sum bits are distinct open premises. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, already-recorded neighbor lock list, seed occupancy
excluding the same-tick partner, vector-sum letter, four y-probes, and
reverse/face definitions are declared. No uniqueness, no leftover
identification, no occupancy-kernel letter, no PVM letter, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` and `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each incoming lock in `S` and each coordinate of the sum | no continuum alphabet |
| per site | `A_y,B,C_y,D_y` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four letters and `UNDEFINED`/`fail` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among possible incoming locks.
None is taken here.

### N7 — hostile steelman

**Steelman:** `A_y` is a seed, so `S` should include the origin partner,
`L(A_y)` should be `+e_1`, reverse should fail as a vector sum, `C_y` should
lock the unique leftover `+e_2`, and face should hold or be adopted as
Admissibility content.

**Answer:** Already-recorded locks are strictly earlier than the formation
tick. The same-tick partner is not in `S`, so `S(A_y)` is empty and reverse
is `UNDEFINED`. The letter at `C_y` is the sum of five already-recorded
`+e_2` locks, namely `(0,5,0)`, not the leftover step `+e_2`. Face fails
because `(0,5,0)+(0,1,0)=(0,6,0)`. The bits remain displayed. Uniqueness is
not required. This is not a unique leftover vector, not occupancy-kernel `n`,
and not a `{+,−}` PVM letter. Tick reverse FAIL / face HOLD is a different
object.

### N8 — cross-cycle echo

A prior display scored named rank-1 PVM letters from occupancy-kernel `n` on
the four nnseed y-probes and reported reverse `UNDEFINED` / face `some`,
because `n(A_y)=0`. A second prior display scored formation-tick inequalities
on the same y-probes and reported reverse FAIL / face HOLD. A third prior
display summed already-recorded 6-NN locks on the four nnseed x-probes and
reported reverse fail / face hold. This note is not those displays: it sums
already-recorded 6-NN locks on the four y-probes, where `S(A_y)` is empty and
`L(C_y)+L(D_y)=(0,6,0)`. Unique leftover vectors on those y-probes are not
used.

**Gate disposition:** PASS for the already-recorded 6-NN lock-sum reverse/face
reports on the four nnseed y-probes above. FAIL / DO NOT SHIP for “the sum
letter equals the leftover unique vector,” “letters are Admissibility,”
“same-tick seed partner occupies `A_y`,” “occupancy-kernel `n` is the
letter,” or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, lists already-recorded six-neighbor incoming locks at
each y-probe's formation tick, sums those locks in `Z^3` or reports
`UNDEFINED`, and checks Theorems 1--3. It also checks that the probe's own
incoming steps are not the sum letter, that the unique leftover vector at
`C_y` is not `L(C_y)`, that the same-tick seed partner is not
already-recorded, that reverse is `UNDEFINED` and face is `fail`, and that
formation ticks match the nsiso y-probe order. No runner cache is written.
