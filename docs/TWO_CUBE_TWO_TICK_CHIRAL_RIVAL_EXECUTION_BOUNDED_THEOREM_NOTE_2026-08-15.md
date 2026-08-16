---
claim_id: two_cube_two_tick_chiral_rival_execution_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether executing occupancy tick-1 then the July-3 k=3 pair at tick-2 yields a P-odd lock set while preserving tick-1 locks is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_two_tick_chiral_rival_execution_2026_08_15.py
---

# Two-Cube Two-Tick Chiral Rival Execution (Displayed, Not Adopted)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact execution of occupancy tick-1 then the July-3 unique `k=3`
chiral pair at tick-2 on the same twelve-vertex two-cube that L1 uses. Off-patch
occupancy is `o=0`. The origin seed is locked with displayed content `+`. The
rival is displayed, not adopted. L1 is not attached. No 4×4×4 or other new
patch is opened.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_two_tick_chiral_rival_execution_2026_08_15.py`](../scripts/two_cube_two_tick_chiral_rival_execution_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment leftover-character is refused. `#6632` displayed that the July-3
`k=3` pair is a `P`-odd predicate on `{0,+,−}^6`. L1 two-tick composition
keeps labels out of `n`. Those leftovers are not this residual. The residual
answered here is only the *execution* of that pair as tick 2 on the same
two-cube, not a new patch.

`f_L1` is `n≠0`, not Hamming. This note does not attach L1.

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] x [0,1] x [0,1].
```

The twelve-vertex patch is the union of those cubes. Occupancy off this
patch is `0`. The origin seed `(0,0,0)` is already locked with displayed
content `+`.

**Tick 1.** An unread patch site forms if and only if the occupancy vector
`n` is nonzero, with

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

That is `f_L1`, occupancy-only. Newly formed sites receive lock labels from
the sign of `n_μ` along the unique occupied axis. If several components of
`n` are nonzero, the displayed default label is `+`. Existing locks are not
overwritten.

New locks: `(1,0,0)`, `(0,1,0)`, `(0,0,1)`. Each has a unique nonzero
component `n_μ = −1/3`, so each receives lock label `−`. The tick-1 lock
set is

```text
L_1 = {(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

The occupancy predicate is `P`-even: swapping opposite neighbor occupancy
bits sends `n → −n` and leaves `n≠0` unchanged. So the tick-1 lock set is
`P`-even (occupancy-only).

**Tick 2.** Neighbor alphabet `{0,+,−}`. Absence, including off-patch
`o=0`, is the letter `0`. A locked neighbor contributes its Record
content. Formation uses the July-3 unique `k=3` chiral pair: the proper
orbit of the runner-anchored representative

```text
r = (0, +, 0, −, +, −)
```

on the ordered directions `(+x,−x,+y,−y,+z,−z)`. Existing locks are not
overwritten.

No unread patch site sees a handed fully-mixed six-tuple. The newly formed
set is empty:

```text
N_new = 0.
```

The tick-2 lock set is therefore `L_2 = L_1`. Spatial inversion `P = −I`
sends that set to

```text
P(L_2) = {(0,0,0), (−1,0,0), (0,−1,0), (0,0,−1)}.
```

The pair `(tick-2 lock set, P of that set)` differs, so tick-2 execution is
`P`-odd on this patch. Tick-1 locks persist at tick 2 (permanence).

Displayed rival execution, not adopted. Do not write the pair into Admissibility. Do not attach L1.

claim_scope: On the two-cube with off-patch o=0, whether executing occupancy
tick-1 then the July-3 k=3 pair at tick-2 yields a P-odd lock set while
preserving tick-1 locks is reported. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-tick execution on a supplied twelve-vertex patch: occupancy tick-1, July-3 k=3 pair at tick-2, reported N_new, permanence, and whether the tick-2 lock set equals its spatial P image. Displayed, not adopted."
trace_class: displayed_rival
target_claim_id: two_cube_two_tick_chiral_rival_execution
target_blocker_text: "run the July-3 k=3 pair as tick 2 on the same two-cube"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "leave the executed rival displayed; do not adopt it, do not attach L1, and do not write the pair into Admissibility"
conditional_surface_status: "exact for the named twelve-vertex two-cube, off-patch o=0, origin seed +, occupancy tick-1, and the July-3 k=3 pair re-earned as tick-2 formation"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

Quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site, probability,
or rate.

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

July-3 theorem 3 is used as a named finite object, not as an axiom edit:
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).
At `k=3` there is exactly one chiral pair, whose members are the handed
fully-mixed patterns. The paired runner re-earns that pair on the six axis
directions and does not consume a cache.

## Algebra

Order the six nearest-neighbor directions as

```text
(+x, −x, +y, −y, +z, −z).
```

Spatial inversion `P = −I` swaps opposite directions and sends a site
`(x,y,z)` to `(−x,−y,−z)`.

Occupancy of a site is `1` if that site is on-patch and locked, else `0`.
Off-patch occupancy is identically `0`. The occupancy vector at an unread
site is `n` with components `n_μ = (o_{+μ} − o_{−μ}) / 3`. Formation at
tick 1 is `n≠0`. That is not the Hamming count of occupied neighbors:
opposite-pair occupancy cancels and does not form.

A forming tick-1 site receives the sign of its unique nonzero `n_μ` as a
lock label in `{+,−}`. Several nonzero components use the displayed default
`+`. The seed label `+` is displayed and is not overwritten.

Tick-2 formation is the indicator of the proper cubic orbit of

```text
r = (0, +, 0, −, +, −).
```

Every axis of `r` is bi-colored and the letter counts are `2/2/2`. That
orbit has 24 colorings; `P` exchanges it with a disjoint 24-orbit. The
union is exactly the 48 handed fully-mixed colorings. Tick 2 does not
overwrite existing locks.

## Theorem 1 — tick-1 lock set is P-even; tick-1 locks persist

Tick-1 lock set is `P`-even (occupancy-only). Tick-1 locks persist at tick 2
(permanence).

*Proof.* On this patch the unread sites that see a nonzero occupancy
vector from the origin seed are exactly `(1,0,0)`, `(0,1,0)`, and
`(0,0,1)`. For each of those sites, `P` acting on the six occupancy bits
swaps the two slots of the unique occupied axis and leaves `n≠0`
unchanged, so the same three sites form. No other on-patch site has
`n≠0` after the seed. Thus `L_1` is the occupancy-only lock set, and the
formation predicate is `P`-even.

At `(1,0,0)` one has `n = (−1/3, 0, 0)`, and cyclically for the other two
axis sites. Each therefore locks `−`. The seed stays `+`.

Tick 2 is forbidden to overwrite existing locks. Record permanence is the
quoted axiom sentence. The runner checks `L_1 ⊂ L_2` and that every tick-1
label is unchanged. That is permanence.

## Theorem 2 — N_new and the pair (tick-2 lock set, P of that set)

Tick-2 newly formed set is nonempty or empty; report `N_new`. The pair
(tick-2 lock set, `P` of that set) is reported. If they differ, tick-2
execution is `P`-odd on this patch.

*Proof.* After tick 1 the unread on-patch sites are

```text
(1,1,0), (1,0,1), (0,1,1), (1,1,1), (2,0,0), (2,1,0), (2,0,1), (2,1,1).
```

Each sees at most two locked neighbors, so its six-tuple uses the letter
`0` at least four times and is not handed fully-mixed. Direct evaluation
gives `f(c)=0` and `f(P·c)=0` at every unread site. Therefore
`N_new = 0` and `L_2 = L_1`.

Spatial inversion of that lock set is

```text
P(L_2) = {(0,0,0), (−1,0,0), (0,−1,0), (0,0,−1)}.
```

The three negative-axis sites are off-patch. Hence `L_2 ≠ P(L_2)`, and
tick-2 execution is `P`-odd on this patch.

The emptiness of the new set is part of the report, not a defect of the
check. The July-3 pair remains a `P`-odd predicate on `{0,+,−}^6`; on this
two-cube after occupancy tick-1 it simply does not fire. The `P`-odd
comparison required here is the comparison of the executed lock *set* with
its spatial image.

This execution is not the occupancy two-tick composition. Occupancy tick-2
would form `(1,1,0)`, `(1,0,1)`, `(0,1,1)`, and `(2,0,0)`. Those sites stay
unread under the chiral pair.

## Theorem 3 — displayed rival execution, not adopted

Displayed rival execution, not adopted. Do not write the pair into Admissibility. Do not attach L1.

The only load-bearing statements are Theorems 1 and 2. The pair is not
selected as the framework's fixed admissibility rule. Occupancy tick-1 is
used as a displayed formation step, not as an attachment of L1. No axiom,
primitive, or registry is edited.

## What this note does and does not claim

- It reports the formed set, permanence of tick-1 locks, `N_new`, and
  whether the tick-2 lock set equals its spatial `P` image.
- It does not attach L1. `f_L1` remains `n≠0`, not Hamming, and lock labels
  do not feed `n`.
- It does not write the pair into Admissibility.
- It is not leftover-character of `#6632` (predicate only) or of L1
  two-tick composition.
- It does not reopen parked exercises.
- It does not open a 4×4×4 or other new patch.
- Formation site, probability, process, and rate remain unsupplied.

## No-Go Discipline

The negative statement is only: on this two-cube, occupancy tick-1 followed
by the July-3 pair at tick-2 adds no new lock. It is not a no-go against
every future content-conditioned execution.

### N1 — materially distinct route scan

| route | marker | outcome |
|---|---|---|
| occupancy-only tick-1, `f_L1` is `n≠0` | **EXECUTED** | three axis locks; `P`-even predicate |
| Hamming neighbor count as formation | **REFUSED** | opposite-pair occupancy is not `n≠0` |
| July-3 `k=3` pair as tick-2 | **EXECUTED** | `N_new = 0`; `L_2 ≠ P(L_2)` |
| occupancy tick-2 on the same patch | **REFUSED** | leftover-character of L1 two-tick composition |
| write the pair into Admissibility | **REFUSED** | displayed, not adopted |
| attach L1 | **REFUSED** | do not attach L1 |
| 4×4×4 or other new patch | **REFUSED** | same two-cube only |

### N2 — wall independence

One execution report is claimed. Emptiness of the new set is not a second
impossibility wall.

### N3 — hidden-wall scan

The patch, seed label, occupancy kernel, lock-label rule, `P`, and the
July-3 pair are declared. No dynamics, no 4×4×4 patch, and no axiom edit is
imported.

### N4 — residual matching

The residual answered is the execution of the already-displayed `P`-odd
predicate as tick 2 on the two-cube. It is not the leftover character of
the predicate-only display or of occupancy two-tick composition.

### N5 — certificate granularity

```text
per-element: executed — occupancy n and the six-letter coloring at each unread site
per-site: executed — twelve-vertex two-cube, off-patch o=0
per-mode: not applicable
per-block: executed — tick-1 lock set, N_new, L_2 versus P(L_2)
lattice-wide: not executed — no new spatial patch
```

### N6 — partial-closure paths

A later execution could change the seed label, allow a later occupancy
tick before the pair, or refuse content-conditioned formation. Adopting
the pair would be an axiom-level or rule-level act and is out of scope.

### N7 — steelman

The strongest objection is that `L_2 ≠ P(L_2)` is inherited from the
origin seed and off-patch `o=0`, not from a fired chiral pair. That is
true and is reported: `N_new = 0`, so the pair does not add the odd
grade. The required comparison is still the executed lock set against its
spatial image. Both facts are part of the report.

### N8 — cross-cycle echo

July-3 theorem 3 is used as a named finite fact and is re-earned on the
same six directions. No status is borrowed from that note's audit row.

## Verification

Run:

```bash
python3 scripts/two_cube_two_tick_chiral_rival_execution_2026_08_15.py
```

The runner reconstructs the twelve-vertex two-cube, executes occupancy
tick-1 with sign labels, re-earns the unique `k=3` pair, reports `N_new`,
compares the tick-2 lock set with its spatial `P` image, checks
permanence, and refuses axiom edits. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
