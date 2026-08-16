---
claim_id: f_cut_wt1_two_site_fillable_equivalence_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, having positive 2-site coverage is not equivalent to f(wt1)=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_two_site_fillable_equivalence_2026_08_15.py
---

# F_cut Positive Two-Site Coverage Is Not The Wt1 Bit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 32 cube-covariant complement-even formation predicates that
vanish on empty and full, run as occupancy dynamics on the twelve-vertex
two-cube with off-patch occupancy `0`, scored by whether they fill at least
one of the 66 unordered 2-site seeds.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_two_site_fillable_equivalence_2026_08_15.py`](../scripts/f_cut_wt1_two_site_fillable_equivalence_2026_08_15.py)

## Result Up Front

Write `V={0,1,2}×{0,1}×{0,1}` for the twelve-vertex two-cube. Every unordered
pair of vertices is a 2-site seed; there are `C(12,2)=66` such seeds.
Off-patch neighbors have occupancy `0`. For each of the 32 `F_cut` maps,
let

`cov2(f)=|{S : |S|=2 and |locks_halt(f,S)|=12}|`.

Then `cov2(f)>0` means `f` fills at least one two-site seed. The remaining
bit `wt1` is the value of `f` on the weight-one orbit. Every map with
`f(wt1)=0` has `cov2=0`. The converse fails: not every map with `f(wt1)=1`
has `cov2>0`. The census is

```text
N_wt1 = 16
N_pos = 14
N_both = 14
```

so having positive 2-site coverage is **not** equivalent to `f(wt1)=1`.
The lex-first counterexample remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3)=(1, 0, 0, 0, 0)` has `f(wt1)=1` and
`cov2=0`. A second witness is `(1, 1, 0, 0, 0)`.

`f_L1` is the unbalanced-axis predicate (`n≠0` on the six-neighbor occupancy
tuple; not Hamming parity). It evaluates to `(1, 0, 1, 1, 1)`, so
`f_L1(wt1)=1`, and it has `cov2(f_L1)=62`. That positive-control map is
not a unique selector and is not adopted.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) remains
untouched:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

This note displays a selector on a finite predicate class. It does not write
`wt1` into Admissibility and does not adopt any remaining-bit tuple.
Displayed, not adopted.

Not leftover-character of #6482 (that only scored the 16 maps with
`wt1=0`). Not leftover-character of #6429 (that ranked Max(2) on the full
32). This is a new selector question: whether the `wt1` bit is exactly the
2-site fillability bit.

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

`f_L1(c)=1` if and only if some axis is unbalanced. That rule evaluates to
`(1, 0, 1, 1, 1)` and is therefore one `F_cut` element. Hamming parity
`|c|_1 mod 2` evaluates to `(1, 0, 0, 1, 1)` and is a different element.

A run from a seed `S` starts with `S` locked. Each tick, every unlocked
on-patch site evaluates `f` on its current six-neighbor occupancy tuple and
locks if `f=1`. Halt is the first fixed point (at most twelve ticks). Fill
means halt lock-count `12`. Coverage `cov2(f)` counts how many of the 66
two-site seeds fill.

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

Reconfirm the one-way fact on the `wt1=0` half. There are 16 remaining-bit
tuples with `f(wt1)=0`. Exhaustive evaluation of `cov2` on those 16 maps
gives `cov2=0` for each of them. A single occupied neighbor never starts a
fill from a 2-site seed when the weight-one orbit is silent, and turning on
any combination of `opp2`, `adj2`, `vertex3`, and `mixed3` does not repair
that silence. This is the same 16-map score as #6482, recomputed here as
the first half of the biconditional.

## Theorem 2

Enumerate all 32 remaining-bit tuples. Write

- `N_wt1` for the number of maps with `f(wt1)=1`,
- `N_pos` for the number of maps with `cov2(f)>0`,
- `N_both` for the number of maps with both.

The exact integers are `N_wt1 = 16`, `N_pos = 14`, `N_both = 14`. Therefore
`cov2(f)>0` if and only if `f(wt1)=1` is false. The two counterexample
tuples are

`(1, 0, 0, 0, 0)` and `(1, 1, 0, 0, 0)`.

Both have `f(wt1)=1` and `cov2=0`. The lex-first of these is
`(1, 0, 0, 0, 0)`: only the weight-one (and complementary weight-five)
orbit fires. From every 2-site seed the run stalls at halt lock-count at
most `10`. Firing `opp2` as well, as in `(1, 1, 0, 0, 0)`, still never
fills. Positive coverage first appears when `wt1=1` and at least one of
`adj2`, `vertex3`, `mixed3` is on.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, is one of the 14 maps with
`cov2>0`; its coverage is `62`. The two maps that attain `cov2=66` are
`(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)`. Those ranking facts are displayed
only as controls; this note does not re-rank Max(2).

## Theorem 3

The failed equivalence, the triple `(N_wt1, N_pos, N_both)=(16, 14, 14)`,
and the counterexample tuple `(1, 0, 0, 0, 0)` are displayed. They are not
adopted. Do not adopt `wt1`. The Admissibility sentence is not edited. In
particular `wt1` is not written into the nearest-neighbor rule, and `f_L1`
remains the unbalanced-axis predicate `n≠0` rather than Hamming parity.
Do not write wt1 into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact enumeration of 32 F_cut maps on the twelve-vertex two-cube; cov2>0 versus f(wt1) is a displayed selector, not a physical law."
trace_class: upstream_support
target_claim_id: admissibility_formation_predicate_selection
target_blocker_text: "select a formation predicate from the axioms rather than by a displayed finite extra"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep wt1 and the 2-site fillability bit as displayed extras; do not promote either to Admissibility."
conditional_surface_status: "exact for the declared two-cube, off-patch o=0, and the 32 F_cut maps; no axiom selector"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundary And Non-Claims

- The 66 seeds and the integer `cov2(f)` are constructed objects on one
  twelve-vertex patch. They are not a lattice-wide formation law.
- Off-patch occupancy `0` is a declared default. Blank-block (undefined
  off-patch slots) is a different rule and is not run here.
- `F_cut` is the three-cut subclass of cube-covariant predicates. Maps
  outside that subclass are not ranked.
- No remaining-bit tuple is written into Admissibility.
- No Record readout, content alphabet, or formation rate is selected.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether positive 2-site coverage detects the single remaining bit `wt1` inside `F_cut`. |
| V2 | Current main has the axiom memo but no landed census of this `cov2>0` versus `f(wt1)` comparison. |
| V3 | All orbit sizes, the 32-map table, and every halt lock-count are finite and exact. |
| V4 | The theorem is more than restating the #6482 one-way score: it separates that implication from a failed biconditional. |
| V5 | Displayed, not adopted. The extras remain conditional. |

## No-Go Discipline Gate

The negative content is narrow: on this patch and class, `cov2(f)>0` does
not characterize `f(wt1)=1`. No global formation impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| silent `wt1` | set `f(wt1)=0` | executed; every such map has `cov2=0` |
| `wt1` alone | tuple `(1,0,0,0,0)` | executed counterexample; `cov2=0` |
| `wt1` and `opp2` without the other three | tuple `(1,1,0,0,0)` | executed; still `cov2=0` |
| `wt1` plus at least one of `adj2`, `vertex3`, `mixed3` | the 14 maps with `cov2>0` | executed fill of at least one seed |
| Hamming parity | `|c|_1 mod 2` | different `F_cut` tuple `(1,0,0,1,1)` with `cov2=16` |
| `f_L1` | remaining bits `(1,0,1,1,1)` | `cov2=62`; positive control, not a selector |

### N2 — wall independence

The missing axiom-level selector, physical formation rate, and Record
content map are distinct open premises. This note claims no wall collection.

### N3 — hidden-condition scan

The six-neighbor order, off-patch default, simultaneous lock update, and
`F_cut` cuts are declared. No continuum, Hamming, or fitted prefactor is
used.

### N4 — source residual matching

The axiom memo supplies the cubic nearest-neighbor substrate, the
local-distribution sentence, and the formation-site/probability/rate
boundary used here. The residual is a displayed extra on a finite class,
matching those sources rather than an axiom edit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | all 32 remaining-bit tuples | no ranking of the 512 maps with only `f(empty)=0` |
| per seed | all 66 two-site seeds | no claim about 1-site or k-site seeds for k>2 |
| per tick | halt lock-counts for every map-seed pair | no physical clock |
| lattice wide | checked and not executed | no infinite-volume formation law |

### N6 — live partial-closure paths

Live routes are an independent derivation of a formation predicate from
Admissibility, a justification of the off-patch default, and a Record
content identification. Other seeds and other cuts remain live.

### N7 — hostile steelman

**Steelman:** Because every `wt1=0` map has `cov2=0`, the `wt1` bit should
be exactly the 2-site fillability bit.

**Answer:** Silence of `wt1` does force `cov2=0`, but firing `wt1` is not
enough to fill. The lex-first map with `f(wt1)=1` and every other remaining
bit off stalls at halt lock-count at most 10 on every 2-site seed. Positive
coverage requires an extra orbit among `adj2`, `vertex3`, and `mixed3`.

### N8 — cross-cycle echo

This is a new selector, not leftover-character of #6482 (that only scored
the 16) and not leftover-character of #6429 (that ranked Max(2)). The 66
seeds and the 32 maps are recomputed here.

**Gate disposition:** PASS for the finite failed equivalence and the
displayed counterexample. FAIL / DO NOT SHIP for “`wt1` is Admissibility”
or “`wt1` selects 2-site fillability.”

## Inputs And Dependency Roles

- **Framework context:** the Lattice nearest-neighbor cubic graph and the
  Admissibility condition-domain sentence.
- **Explicit bounded mathematical input:** the two-cube vertex set, off-patch
  occupancy `0`, the ten-orbit classification, the three `F_cut` cuts, and
  the simultaneous lock-update rule.
- **Not imported:** any unmerged census of a different seed, any Hamming
  identity for `f_L1`, and any axiom edit.

## Primary Runner

The primary runner recomputes the ten orbits, the 32 `F_cut` maps, `cov2`
on the 66 two-site seeds, the failed biconditional, the counts
`N_wt1`, `N_pos`, `N_both`, the lex-first counterexample, the one-way
`wt1=0` implication, and the current premise boundary. It authors no audit
verdict.
