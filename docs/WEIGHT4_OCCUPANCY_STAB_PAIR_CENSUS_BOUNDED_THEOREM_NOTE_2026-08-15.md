---
claim_id: weight4_occupancy_stab_pair_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 15 weight-4 occupancy masks, the counts |Stab|, N_pair_support, and N_stab_ok are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/weight4_occupancy_stab_pair_census_2026_08_15.py
---

# Weight-4 Occupancy Stabilizer Versus July-3 Pair Members (Bounded Census Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 15 occupancy bitstrings of weight 4 on the six nearest-neighbor
slots `(+x, −x, +y, −y, +z, −z)`. Score occupancy masks only.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/weight4_occupancy_stab_pair_census_2026_08_15.py`](../scripts/weight4_occupancy_stab_pair_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment staborb/orbfire scored one three-ball occupancy
`σ = (1, 0, 1, 1, 0, 1)` and found `|Stab(σ)| = 2` with `N_stab_ok = 0`
(the order-2 swapper forces a monochrome `y` axis; every pair member is
`y`-bicolored). That is one mask. The residual here is not leftover of
staborb (one mask). Among all 15 occupancy masks of weight 4 (pair-support
type), how many have `N_stab_ok > 0`?

Slots are

`(+x, −x, +y, −y, +z, −z)`.

`G+` is the 24 proper cube rotations acting on those slots. Weight-4
masks are the 15 bitstrings in `{0,1}^6` with four `1`s. The pair is the
July-3 `k = 3` chiral pair (48 maps). For each mask `σ` the runner
rebuilds `Stab(σ)`, `N_pair_support` (pair members with that support),
and `N_stab_ok` (those invariant under `Stab(σ)`).

**Theorem 1.** The table of 15 rows is recorded below:
`σ`, `|Stab(σ)|`, `N_pair_support`, `N_stab_ok`.
`N_ok_masks = 0`. There is no lex-first such `σ`.

**Theorem 2.** `N_ok_masks = 0`. If yes, no occupancy of pair-support type admits a Stab-invariant pair member, so no NN-determined G+-equivariant pair labeling exists on any 4-occupied 6-star.

**Theorem 3.** Displayed, not adopted. Do not write a mask or pair member into Admissibility. Do not attach L1. Do not add a 4th ball. Qubit remains `M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither a weight-4 occupancy mask nor any July-3 pair
member as the framework's fixed rule. The covariance clause is the reason
a local labeling that is a function of occupancy must be stabilizer-invariant
on each occupancy orbit. Formation site and rate remain outside the axiom
memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 15 weight-4 occupancy masks against the 24-element cube rotation group and the 48-member July-3 pair. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: weight4_occupancy_stab_pair_census
target_blocker_text: "on the 15 weight-4 occupancy masks, the counts |Stab|, N_pair_support, and N_stab_ok"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 15-row table and N_ok_masks; do not write a mask or pair member into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the 15 weight-4 occupancy masks; N_ok_masks=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Direction order is `(+x, −x, +y, −y, +z, −z)`. An occupancy mask is a
6-bit indicator of which of those six nearest-neighbor slots are occupied.
The weight-4 masks are the 15 bitstrings of Hamming weight 4. They are
scored as abstract occupancy objects: occupancy masks only.

`G+` is the 24 determinant-`+1` signed permutation matrices of the three
axes. A matrix `g` permutes the six axis directions: the bit (or letter)
at slot `μ` moves to slot `gμ`. The occupancy stabilizer is

`Stab(σ) = { g in G+ : g · σ = σ }`.

The July-3 `k = 3` chiral pair is the unique pair of `G+` orbits of
handed fully-mixed 6-tuples on the three-letter alphabet `{0,1,2}` with
`0` empty. Fully mixed means every axis is bi-colored and each letter is
used twice. The pair is reconstructed by enumerating the 24 proper
rotations on `{0,1,2}^6`; it has 48 members (two orbits of size 24).

Support of a 6-tuple is the 6-bit indicator of slots with a nonzero
letter. `N_pair_support` is the number of pair members whose support
equals `σ`. `N_stab_ok` is the number of those members `c` with
`g · c = c` for every `g` in `Stab(σ)`.

`N_ok_masks` is the number of weight-4 masks with `N_stab_ok > 0`. If
that set is nonempty, the lex-first such `σ` is reported. If it is empty,
there is no lex-first such `σ`.

A local (NN-determined) labeling is a function `f` of occupancy. On the
`G+` orbit of a mask `σ`, equivariance forces `f(σ)` to be
`Stab(σ)`-invariant. Therefore a positive `N_stab_ok` would be the
number of NN-determined `G+`-extendable pair members on that occupancy.

## Theorem 1 — fifteen-row census

Lexicographic listing of the 15 weight-4 masks, each rebuilt against the
24 proper rotations and the 48-member pair, gives

| `σ` | `|Stab(σ)|` | `N_pair_support` | `N_stab_ok` |
|---|---|---|---|
| `(0, 0, 1, 1, 1, 1)` | 8 | 0 | 0 |
| `(0, 1, 0, 1, 1, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 0, 1, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 1, 0, 1)` | 2 | 4 | 0 |
| `(0, 1, 1, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 0, 0, 1, 1, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 0, 1, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 1, 0, 1)` | 2 | 4 | 0 |
| `(1, 0, 1, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 0, 0, 1, 1)` | 8 | 0 | 0 |
| `(1, 1, 0, 1, 0, 1)` | 2 | 4 | 0 |
| `(1, 1, 0, 1, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 1, 0, 0, 1)` | 2 | 4 | 0 |
| `(1, 1, 1, 0, 1, 0)` | 2 | 4 | 0 |
| `(1, 1, 1, 1, 0, 0)` | 8 | 0 | 0 |

So

`N_ok_masks = 0`.

There is no lex-first such `σ`.

The three masks that empty an entire axis have `|Stab(σ)| = 8` and
`N_pair_support = 0`: a fully mixed pair member cannot leave one axis
monochrome empty. The remaining twelve masks empty two perpendicular
slots. Each of those has `|Stab(σ)| = 2` and `N_pair_support = 4`. The
staborb three-ball mask `(1, 0, 1, 1, 0, 1)` is one of those twelve
rows; the other eleven are its `G+` images or the matching perpendicular
empty-pair type. The 48 pair members are partitioned by those twelve
supports (`12 × 4 = 48`). Every one of those twelve rows has
`N_stab_ok = 0`: the non-identity stabilizer element swaps the two
slots of the remaining fully occupied axis, while every pair member
bicolors that axis.

This is not leftover of staborb (one mask) and not leftover of orbfire
(execution of Stab-ok members on that one star). Score occupancy masks
only.

## Theorem 2 — no fair weight-4 occupancy

`N_ok_masks = 0`. If yes, no occupancy of pair-support type admits a Stab-invariant pair member, so no NN-determined G+-equivariant pair labeling exists on any 4-occupied 6-star.

The implication is for every weight-4 occupancy, not only the one
three-ball star already scored by staborb/orbfire. A nearest-neighbor
determined labeling is a function of occupancy. Cube-equivariance on
the occupancy orbit requires the value at `σ` to be `Stab(σ)`-invariant.
No July-3 pair member meets that test on any of the 15 pair-support-type
masks.

## Theorem 3 — displayed, not adopted

The 15-row table and the count `N_ok_masks = 0` are displayed member
data. They are not the framework's fixed Admissibility rule. This note
does not write any such mask or pair member into Admissibility. Do not
write a mask or pair member into Admissibility. Do not attach L1. Do
not add a 4th ball. Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 15 weight-4 occupancy masks,
  `|Stab(σ)|`, `N_pair_support`, and `N_stab_ok` are the table above,
  and `N_ok_masks = 0`.
- **What is displayed only.** The table and the zero count are one
  rival census. They are not adopted.
- **What is not claimed.** No attachment of any mask or pair member to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no fourth
  equal-radius ball; no leftover of staborb's one mask; no leftover of
  orbfire's fire count on that star; no compiler no-go.
- **Mutation controls.** A rebuilt table with any `N_stab_ok > 0`
  fails the `N_ok_masks = 0` report. A note that writes a mask or pair
  member into Admissibility, attaches L1, or authors an audit verdict
  fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 15 weight-4 occupancy masks, the 24
proper cube rotations acting on slots, the reconstructed July-3 pair,
`Stab(σ)`, `N_pair_support`, `N_stab_ok`, `N_ok_masks`, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.
