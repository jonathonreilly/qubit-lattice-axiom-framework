---
claim_id: f_cut_cov3_positive_closed_form_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, positive 3-site coverage is not equivalent to P. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_positive_closed_form_2026_08_15.py
---

# F_cut Positive Three-Site Coverage Is Not The Selector P

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 32 cube-covariant complement-even formation predicates that
vanish on empty and full, run as occupancy dynamics on the twelve-vertex
two-cube with off-patch occupancy `0`, scored by whether they fill at least
one of the 220 unordered 3-site seeds.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_positive_closed_form_2026_08_15.py`](../scripts/f_cut_cov3_positive_closed_form_2026_08_15.py)

## Result Up Front

Write `V={0,1,2}×{0,1}×{0,1}` for the twelve-vertex two-cube. Every unordered
triple of vertices is a 3-site seed; there are `C(12,3)=220` such seeds.
Off-patch neighbors have occupancy `0`. For each of the 32 `F_cut` maps,
let

`cov3(f)=|{S : |S|=3 and |locks_halt(f,S)|=12}|`.

Then `cov3(f)>0` means `f` fills at least one three-site seed. Remaining-bit
tuples are written in the order `(wt1, opp2, adj2, vertex3, mixed3)`. Define
the displayed selector

`P(f) := (wt1=1) and (adj2, vertex3, mixed3) ≠ (0, 0, 0)`.

Investment #6494 established that `cov2(f)>0` if and only if `P(f)` on this
same class and patch. This note asks a new selector question at a new seed
size `k=3`: whether `cov3(f)>0` is the same bit. It is not a Max(3) rename
and not leftover-character of #6494.

The exact census is

```text
N_P = 14
N_pos = 20
N_both = 13
```

so `cov3(f)>0` is **not** equivalent to `P(f)`. The lex-first counterexample
remaining-bit tuple is

`(wt1, opp2, adj2, vertex3, mixed3)=(0, 0, 1, 1, 0)`,

which has `P=0` and `cov3=24`. One witness in the other direction is
`(1, 0, 0, 0, 1)`, which has `P=1` and `cov3=0` (while `cov2=8`).

`f_L1` is the unbalanced-axis predicate (`n≠0` on the six-neighbor occupancy
tuple; not Hamming parity). It evaluates to `(1, 0, 1, 1, 1)`, so `P(f_L1)=1`,
and it has `cov3(f_L1)=220`. That positive-control map is not a unique
selector and is not adopted.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) remains
untouched:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

This note displays a selector comparison on a finite predicate class. It does
not write `P` into Admissibility and does not adopt any remaining-bit tuple.
Displayed, not adopted.

Not leftover-character of #6494 (that was `cov2>0` iff `P`). Not a Max(3)
rename of the 3-site coverage ranking. New `k`, new selector question.

## Exact Objects And The Dynamics

The six-neighbor occupancy cell at a site is the `{0,1}^6` tuple of locked
status on the ordered shifts `±e_1, ±e_2, ±e_3`. Off-patch neighbors contribute
occupancy `0`. A cell is assigned one of ten orbits under the 24 proper cube
rotations:

| orbit | representative type | size |
|---|---|---|
| empty | all unoccupied | 1 |
| wt1 | a single occupied slot | 6 |
| opp2 | both ends of one axis occupied | 3 |
| adj2 | two occupied slots on distinct axes | 12 |
| vertex3 | one slot on each axis, no opposite pair | 8 |
| mixed3 | one full axis plus one extra slot | 12 |
| opp4 | complement of opp2 | 3 |
| adj4 | complement of adj2 | 12 |
| wt5 | complement of wt1 | 6 |
| full | all occupied | 1 |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Complement-evenness identifies `wt5` with `wt1`, `opp4` with
`opp2`, and `adj4` with `adj2`, and leaves `vertex3` and `mixed3`
complement-fixed, so `|F_cut|=2^5=32`. Remaining-bit tuples are written in
the order `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. That rule evaluates to `(1, 0, 1, 1, 1)` and is therefore one
`F_cut` element. Hamming parity evaluates to `(1, 0, 0, 1, 1)` and is a
different element.

A run from a seed `S` starts with `S` locked. Each tick, every unlocked
on-patch site evaluates `f` on its current six-neighbor occupancy tuple and
locks if `f=1`. Halt is the first fixed point (at most twelve ticks). Fill
means halt lock-count `12`. Coverage `cov3(f)` counts how many of the 220
three-site seeds fill.

`P` is a boolean on remaining bits, not a formation law: it is the
conjunction of `wt1=1` with the statement that at least one of `adj2`,
`vertex3`, `mixed3` fires. The bit `opp2` is free in `P`. Exactly 14 of the
32 maps satisfy `P`.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility identifies the six-neighbor condition domain and covariance
under proper cubic rotations. It
does not supply the formation site, probability, or rate.
The boolean occupancy predicates and the lock-update rule are explicit
bounded mathematical input, not axiom text.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Permanence of a lock once formed is used only as the declared update rule on
this finite patch. No physical readout, content map, or formation rate is
identified.

## Theorem 1

Whether `cov3(f)>0` if and only if `P(f)`, for all 32 maps. The biconditional
is false. One counterexample remaining-bit tuple is
`(0, 0, 1, 1, 0)`: `P=0` and `cov3=24`. The same enumeration also produces
the opposite-direction witness `(1, 0, 0, 0, 1)` (`P=1`, `cov3=0`). Either
tuple already kills the claimed equivalence.

The control `#6494` recomputes on the same 32 maps: `cov2(f)>0` if and only
if `P(f)`. That 2-site fact is not the 3-site fact.

## Theorem 2

Enumerate all 32 remaining-bit tuples. Write

- `N_P` for the number of maps with `P(f)=1`,
- `N_pos` for the number of maps with `cov3(f)>0`,
- `N_both` for the number of maps with both.

The exact integers are `N_P = 14`, `N_pos = 20`, `N_both = 13`. Therefore
`N_P ≠ N_pos` and `N_both` is strictly smaller than both, so the two
predicates are distinct.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, is one of the 13 maps in the
intersection; its 3-site coverage is `220`. Those ranking facts are displayed
only as controls; this note does not re-rank Max(3).

## Theorem 3

The failed equivalence, the triple `(N_P, N_pos, N_both)=(14, 20, 13)`, and
the counterexample tuple `(0, 0, 1, 1, 0)` are displayed. They are not
adopted. Do not adopt `P`. The Admissibility sentence is not edited. In
particular `P` is not written into the nearest-neighbor rule, and `f_L1`
remains the unbalanced-axis predicate `n≠0` rather than Hamming parity.
Do not write P into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact enumeration of 32 F_cut maps on the twelve-vertex two-cube; cov3>0 versus P is a displayed selector comparison, not a physical law."
trace_class: upstream_support
target_claim_id: admissibility_formation_predicate_selection
target_blocker_text: "select a formation predicate from the axioms rather than by a displayed finite extra"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep P and the 3-site fillability bit as displayed extras; do not promote either to Admissibility."
conditional_surface_status: "exact for the declared two-cube, off-patch o=0, and the 32 F_cut maps; no axiom selector"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundary And Non-Claims

- The 220 seeds and the integer `cov3(f)` are constructed objects on one
  twelve-vertex patch. They are not a lattice-wide formation law.
- Off-patch occupancy `0` is a declared default. A blank-block is a different rule and is not run here.
- `F_cut` is the three-cut subclass of cube-covariant predicates. Maps
  outside that subclass are not ranked.
- No remaining-bit tuple is written into Admissibility.
- `P` is displayed, not adopted.
- No Record readout, content alphabet, or formation rate is selected.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether positive 3-site coverage detects the displayed selector `P` inside `F_cut`. |
| V2 | Current main has the axiom memo but no landed census of this `cov3>0` versus `P` comparison. |
| V3 | All orbit sizes, the 32-map table, and every halt lock-count are finite and exact. |
| V4 | The theorem is more than restating #6494: it tests a new seed size rather than renaming Max(3). |
| V5 | Displayed, not adopted. The extras remain conditional. |

## No-Go Discipline Gate

The negative content is narrow: on this patch and class, `cov3(f)>0` does
not characterize `P(f)`. No global formation impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| adopt `P` | write `P` into Admissibility | **ATTEMPTED** |
| leftover `#6494` | treat `cov3>0` iff `P` as leftover of `cov2>0` iff `P` | **ATTEMPTED** |
| Max(3) rename | replace the selector question by a 3-site coverage ranking | **ATTEMPTED** |
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The missing axiom-level selector, physical formation rate, and Record
content map are distinct open premises. This note claims no wall collection.

### N3 — hidden-condition scan

The six-neighbor order, off-patch default, simultaneous lock update, and
`F_cut` cuts are declared. No continuum, Hamming, or fitted prefactor is
used. Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor substrate, the
local-distribution sentence, and the formation-site/probability/rate
boundary used here. The residual is a displayed extra on a finite class,
matching those sources rather than an axiom edit. The residual is not
leftover-character of #6494 and is not a Max(3) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | all 32 remaining-bit tuples | no ranking of the 512 maps with only `f(empty)=0` |
| per seed | all 220 three-site seeds | no claim that the Max(3) ranking is this selector |
| per tick | halt lock-counts for every map-seed pair | no physical clock |
| per block | `N_P`, `N_pos`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no infinite-volume formation law |

### N6 — live partial-closure paths

Live routes are an independent derivation of a formation predicate from
Admissibility, a justification of the off-patch default, and a Record
content identification. Other seeds and other cuts remain live.

### N7 — hostile steelman

**Steelman:** Because `P` is exactly the 2-site fillability bit (#6494), the
same `P` should be the 3-site fillability bit.

**Answer:** The 2-site and 3-site positive-coverage bits are different. Seven
maps with `P=0` still fill at least one 3-site seed, and the map
`(1, 0, 0, 0, 1)` satisfies `P` and has `cov2=8` but `cov3=0`. Lex-first
counterexample `(0, 0, 1, 1, 0)` has `P=0` and `cov3=24`.

### N8 — cross-cycle echo

This is a new selector at a new `k`, not leftover-character of #6494 and
not a Max(3) rename. The 220 seeds and the 32 maps are recomputed here.

No-Go Discipline disposition: **PASS** for the finite failed equivalence and
the displayed counterexample. FAIL / DO NOT SHIP for “`P` is Admissibility”
or “`P` selects 3-site fillability.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Inputs And Dependency Roles

- **Framework context:** the Lattice nearest-neighbor cubic graph and the
  Admissibility condition-domain sentence.
- **Explicit bounded mathematical input:** the two-cube vertex set, off-patch
  occupancy `0`, the ten-orbit classification, the three `F_cut` cuts, and
  the simultaneous lock-update rule.
- **Not imported:** any unmerged Max(3) ranking as a substitute for this
  selector, any Hamming identity for `f_L1`, and any axiom edit.

## Primary Runner

The primary runner recomputes the ten orbits, the 32 `F_cut` maps, `cov3`
on the 220 three-site seeds, the failed biconditional against `P`, the
counts `N_P`, `N_pos`, `N_both`, the lex-first counterexample, the #6494
`cov2` control, and the current premise boundary. It authors no audit
verdict. Declared audit inputs are this note and the axiom memo; the runner
writes no cache.
