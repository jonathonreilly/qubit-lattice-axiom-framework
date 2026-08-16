---
claim_id: two_cube_tick1_labeling_chiral_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0 and seed +, whether any of the 8 tick-1 {+,−} labelings of the three axis sites makes the July-3 k=3 pair fire at tick 2 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_tick1_labeling_chiral_fire_2026_08_15.py
---

# Two-Cube Tick-1 Labeling Chiral Fire (Displayed, Not Adopted)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact eight-labeling census on the same twelve-vertex two-cube
that occupancy tick-1 uses. Off-patch occupancy is `o=0`. The origin seed is
locked with displayed content `+`. Tick 1 forms the three axis sites by
`n≠0`. Each of those sites is then labeled independently by `{+,−}`. Tick 2
uses the July-3 unique `k=3` pair on neighbor contents `{0,+,−}`. The census
is displayed, not adopted. L1 is not attached. No 4×4×4 or other new patch
is opened. Same two-cube only; this is not a new patch.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_tick1_labeling_chiral_fire_2026_08_15.py`](../scripts/two_cube_tick1_labeling_chiral_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment `#6632` displayed that the July-3 `k=3` pair is a `P`-odd
predicate on `{0,+,−}^6`. Investment `#6634` (wav2run) executed one labeling
— lock labels from the sign of `n_μ`, which assigns `−` at each tick-1 axis
site — and obtained `N_new=0`. That closed one labeling. This residual is
not leftover-char of wav2run. The question here is whether *any* of the
eight `{+,−}` assignments to the three tick-1 sites makes tick-2 `N_new>0`.

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
n_μ = (o_{+μ} − o_{−μ}) / 3.
```

That is `f_L1`, occupancy-only. Existing locks are not overwritten. New
locks are always `(1,0,0)`, `(0,1,0)`, `(0,0,1)`. Labeling of those three
sites is then enumerated: each site receives an independent letter in
`{+,−}`, eight assignments. The seed stays `+`. Sign of `n_μ` is one of
those eight (all `−`); it is not privileged.

**Tick 2.** Neighbor alphabet `{0,+,−}`. Absence, including off-patch
`o=0`, is the letter `0`. A locked neighbor contributes its Record
content. Formation uses the July-3 unique `k=3` chiral pair: the proper
orbit of the runner-anchored representative

```text
r = (0, +, 0, −, +, −)
```

on the ordered directions `(+x,−x,+y,−y,+z,−z)`. Existing locks are not
overwritten.

For each of the eight labelings, every unread patch site sees at most two
locked neighbors. Its six-tuple therefore uses the letter `0` at least four
times and is not handed fully-mixed. Direct evaluation gives `N_new = 0` on
every labeling. Report that none of the 8 labelings has N_new>0. There is no
lex-first firing labeling and no new sites to report.

`N_fire = 0`. Among the empty collection of firing labelings there is no
new-lock set, so the `P`-odd comparison of a fired new-lock set with its
`P`-image has empty domain.

Displayed, not adopted. Do not write a labeling rule into Admissibility. Do not attach L1.

claim_scope: On the two-cube with off-patch o=0 and seed +, whether any of the 8
tick-1 {+,−} labelings of the three axis sites makes the July-3 k=3 pair fire at
tick 2 is reported. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact eight-labeling census on a supplied twelve-vertex patch: occupancy tick-1, free {+,−} labels on the three axis sites, July-3 k=3 pair at tick-2, reported N_new, N_fire, and P-oddness of any fired new-lock set. Displayed, not adopted."
trace_class: displayed_rival
target_claim_id: two_cube_tick1_labeling_chiral_fire
target_blocker_text: "among the 8 tick-1 labelings, does any make tick-2 N_new>0"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "leave the census displayed; do not adopt a labeling rule, do not attach L1, and do not write a labeling rule into Admissibility"
conditional_surface_status: "exact for the named twelve-vertex two-cube, off-patch o=0, origin seed +, occupancy tick-1, eight tick-1 {+,−} labelings, and the July-3 k=3 pair re-earned as tick-2 formation"
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

Tick-1 lock *sites* are occupancy-only. Tick-1 lock *labels* are the eight
assignments of `{+,−}` to `(1,0,0)`, `(0,1,0)`, `(0,0,1)` in that order.
Lexicographic order on those triples uses `+` before `−`. The seed label
`+` is displayed and is not overwritten.

Tick-2 formation is the indicator of the proper cubic orbit of

```text
r = (0, +, 0, −, +, −).
```

Every axis of `r` is bi-colored and the letter counts are `2/2/2`. That
orbit has 24 colorings; `P` exchanges it with a disjoint 24-orbit. The
union is exactly the 48 handed fully-mixed colorings. Tick 2 does not
overwrite existing locks. Labels do not feed occupancy: every labeling
shares the same four locked sites after tick 1.

## Theorem 1 — N_new for each of the eight labelings

For each of the 8 labelings, `N_new` at tick 2 is reported. Whether any
labeling has `N_new>0`. If yes, one lex-first labeling and its new sites.
If none, report that.

*Proof.* On this patch the unread sites that see a nonzero occupancy
vector from the origin seed are exactly `(1,0,0)`, `(0,1,0)`, and
`(0,0,1)`. No other on-patch site has `n≠0` after the seed. Those three
sites are then labeled by each of the eight `{+,−}` triples.

After tick 1 the unread on-patch sites are

```text
(1,1,0), (1,0,1), (0,1,1), (1,1,1), (2,0,0), (2,1,0), (2,0,1), (2,1,1).
```

Each sees at most two locked neighbors, independently of the three labels.
Its six-tuple therefore uses the letter `0` at least four times and cannot
be handed fully-mixed. The July-3 pair therefore returns false at every
unread site, for every labeling. Direct evaluation of all eight six-tuples
confirms `N_new = 0` throughout. None of the 8 labelings has `N_new>0`.
There is no lex-first firing labeling.

## Theorem 2 — N_fire and P-oddness among those that fire

`N_fire` is the number of labelings with `N_new>0`. Among those that fire,
whether the new-lock set is `P`-odd (differs from its `P`-image).

*Proof.* Theorem 1 gives `N_new = 0` on every labeling, so `N_fire = 0`.
The collection of firing new-lock sets is empty. The `P`-odd comparison is
therefore not instantiated. Emptiness of that collection is the report,
not a claim that a nonexistent new-lock set is `P`-even or `P`-odd.

The July-3 pair remains a `P`-odd predicate on `{0,+,−}^6`. On this
two-cube after occupancy tick-1, no tick-1 `{+,−}` labeling makes that
predicate fire.

## Theorem 3 — displayed, not adopted

Displayed, not adopted. Do not write a labeling rule into Admissibility. Do not attach L1.

The only load-bearing statements are Theorems 1 and 2. No labeling of the
three axis sites is selected as a physical rule. Occupancy tick-1 is used
as a displayed formation step, not as an attachment of L1. No axiom,
primitive, or registry is edited.

## What this note does and does not claim

- It reports `N_new` for each of the eight tick-1 labelings, whether any
  has `N_new>0`, `N_fire`, and the empty-domain `P`-odd question among
  firers.
- It does not attach L1. `f_L1` remains `n≠0`, not Hamming, and lock labels
  do not feed `n`.
- It does not write a labeling rule into Admissibility.
- It is not leftover-char of wav2run: wav2run closed the single sign-of-
  `n_μ` labeling; this census is the remaining eight-assignment question.
- It does not reopen parked exercises.
- It does not open a 4×4×4 or other new patch.
- Formation site, probability, process, and rate remain unsupplied.

## No-Go Discipline

The negative statement is only: on this two-cube, none of the eight tick-1
`{+,−}` labelings makes the July-3 pair fire at tick 2. It is not a no-go
against every future content-conditioned execution.

### N1 — materially distinct route scan

| route | marker | outcome |
|---|---|---|
| occupancy-only tick-1, `f_L1` is `n≠0` | **EXECUTED** | three axis locks, labels free |
| Hamming neighbor count as formation | **REFUSED** | opposite-pair occupancy is not `n≠0` |
| all eight tick-1 `{+,−}` labelings at tick-2 | **EXECUTED** | `N_new = 0` on each; `N_fire = 0` |
| sign of `n_μ` only (wav2run) | **REFUSED** | leftover-char of wav2run; one labeling |
| occupancy tick-2 on the same patch | **REFUSED** | leftover-character of L1 two-tick composition |
| write a labeling rule into Admissibility | **REFUSED** | displayed, not adopted |
| attach L1 | **REFUSED** | do not attach L1 |
| 4×4×4 or other new patch | **REFUSED** | same two-cube only |

### N2 — wall independence

One census report is claimed. Emptiness of every new set is not a second
impossibility wall.

### N3 — hidden-wall scan

The patch, seed label, occupancy kernel, eight labelings, `P`, and the
July-3 pair are declared. No dynamics, no 4×4×4 patch, and no axiom edit is
imported.

### N4 — residual matching

The residual answered is whether any of the eight tick-1 labelings makes
the already-displayed `P`-odd pair fire at tick 2. It is not leftover-char
of wav2run (that closed one labeling).

### N5 — certificate granularity

```text
per-element: executed — occupancy n and the six-letter coloring at each unread site, each of 8 labelings
per-site: executed — twelve-vertex two-cube, off-patch o=0
per-mode: not applicable
per-block: executed — eight N_new values, N_fire, empty firer P-odd domain
lattice-wide: not executed — no new spatial patch
```

### N6 — partial-closure paths

A later execution could change the seed label, grow the patch, or refuse
content-conditioned formation. Adopting a labeling rule would be an
axiom-level or rule-level act and is out of scope.

### N7 — steelman

The strongest objection is that eight zeros were already implied by
wav2run's "at most two locked neighbors" geometry, so the census is
redundant. The residual was still the eight-assignment question: labels
could have mattered if any unread site had seen four locked neighbors.
None does. The runner enumerates all eight rather than inferring from one.

### N8 — cross-cycle echo

July-3 theorem 3 is used as a named finite fact and is re-earned on the
same six directions. No status is borrowed from that note's audit row.

## Verification

Run:

```bash
python3 scripts/two_cube_tick1_labeling_chiral_fire_2026_08_15.py
```

The runner reconstructs the twelve-vertex two-cube, forms occupancy
tick-1, assigns each of the eight `{+,−}` labelings to the three axis
sites, re-earns the unique `k=3` pair, reports `N_new` per labeling,
`N_fire`, and the empty firer `P`-odd domain, and refuses axiom edits.
Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
