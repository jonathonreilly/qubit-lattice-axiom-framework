---
claim_id: f_cut_opp2_long_axis_fill_equivalence_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, filling all four long-axis 2-site seeds is not equivalent to f(opp2)=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_opp2_long_axis_fill_equivalence_2026_08_15.py
---

# F_cut Long-Axis Four-Seed Fill Is Not The Opp2 Bit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 32 cube-covariant complement-even formation predicates that
vanish on empty and full, run as occupancy dynamics on the twelve-vertex
two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_opp2_long_axis_fill_equivalence_2026_08_15.py`](../scripts/f_cut_opp2_long_axis_fill_equivalence_2026_08_15.py)

## Result Up Front

Write `V={0,1,2}×{0,1}×{0,1}` for the twelve-vertex two-cube. Let `M` be the
four long-axis 2-site seeds

`{((0,0,0),(2,0,0)), ((0,0,1),(2,0,1)), ((0,1,0),(2,1,0)), ((0,1,1),(2,1,1))}`.

These are exactly the four 2-site seeds from which the unbalanced-axis
predicate `f_L1` (`n≠0` on the six-neighbor occupancy tuple; not Hamming
parity) fails to lock all twelve vertices. For each of the 32 `F_cut` maps,
let

`k(f)=|{S∈M : |locks_halt(f,S)|=12}|`.

Then `f_L1` has `k=0` and `f_L1(opp2)=0`. Filling every seed in `M` is
**not** equivalent to `f(opp2)=1`, and `k(f)=0` is **not** equivalent to
`f(opp2)=0`. The lex-first counterexample remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3)=(0, 1, 0, 0, 0)` has `k=0` while
`f(opp2)=1`. Every silent-`opp2` map still has `k=0`, so that one direction
holds; the converse fails. The four maps that do attain `k=4` are exactly
those with `(wt1, opp2, adj2)=(1,1,1)`.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) remains
untouched:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

This note displays a selector on a finite predicate class. It does not write
`opp2` into Admissibility and does not adopt any remaining-bit tuple.

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
means halt lock-count `12`.

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

`f_L1` lies in `F_cut`, has `f(opp2)=0`, and has `k(f_L1)=0`. On each seed
in `M` the lock history is `(2, 6, 8)`: the two long-axis endpoints grow
along the two short axes and then stall, leaving the shared-face slice
unlocked. The same predicate fills from the 1-site seed `{(0,0,0)}` with
history `(1, 4, 8, 11, 12)`, so the misses are seed-dependent rather than a
global failure to form.

## Theorem 2

Enumerate all 32 remaining-bit tuples. The pairs `(k(f), f(opp2))` occupy
only three bins:

- 16 maps with `f(opp2)=0`, all of them `k=0`;
- 12 maps with `f(opp2)=1` and `k=0`;
- 4 maps with `f(opp2)=1` and `k=4`.

Therefore `k(f)=4` if and only if `f(opp2)=1` is false, and `k(f)=0` if and
only if `f(opp2)=0` is false. The lex-first counterexample tuple is
`(0, 1, 0, 0, 0)`, which has `k=0`. Its first-seed history is `(2, 3)`: the
middle long-axis site locks by `opp2`, then the run halts because `wt1=0`.
A second displayed witness with `wt1=1` is `(1, 1, 0, 1, 1)`, which reaches
halt lock-count `9` and still misses every seed in `M`.

The four maps with `k=4` are

`(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)`.

So filling all four long-axis seeds detects the conjunction
`wt1=adj2=opp2=1`, not the single bit `opp2`. No value `k∈{1,2,3}` occurs:
by the residual long-axis symmetry of the two-cube, a map fills every seed
in `M` or none.

## Theorem 3

The failed equivalence and the counterexample tuple are displayed. They are
not adopted. The Admissibility sentence is not edited. In particular `opp2`
is not written into the nearest-neighbor rule, and `f_L1` remains the
unbalanced-axis predicate `n≠0` rather than Hamming parity.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact enumeration of 32 F_cut maps on the twelve-vertex two-cube; k(f) versus f(opp2) is a displayed selector, not a physical law."
trace_class: upstream_support
target_claim_id: admissibility_formation_predicate_selection
target_blocker_text: "select a formation predicate from the axioms rather than by a displayed finite extra"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep opp2 and the long-axis four-seed count as displayed extras; do not promote either to Admissibility."
conditional_surface_status: "exact for the declared two-cube, off-patch o=0, and the 32 F_cut maps; no axiom selector"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundary And Non-Claims

- The four seeds and the integer `k(f)` are constructed objects on one
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
| V1 | It answers whether the four long-axis 2-site seeds detect the single remaining bit `opp2` inside `F_cut`. |
| V2 | Current main has the axiom memo but no landed census of this `k(f)` versus `f(opp2)` comparison. |
| V3 | All orbit sizes, the 32-map table, and every halt lock-count are finite and exact. |
| V4 | The theorem is more than restating `n≠0`: it separates a one-way implication from a failed biconditional. |
| V5 | Displayed, not adopted. The extras remain conditional. |

## No-Go Discipline Gate

The negative content is narrow: on this patch and class, `k(f)=4` does not
characterize `f(opp2)=1`. No global formation impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| silent `opp2` | set `f(opp2)=0` | executed; every such map has `k=0` |
| `opp2` alone | set `f(opp2)=1` with `wt1=0` | executed counterexample; `k=0` |
| `opp2` and `wt1` without `adj2` | tuple `(1,1,0,*,*)` | executed; still `k=0` |
| conjunction `wt1=adj2=opp2=1` | the four `k=4` maps | executed fill of every seed in `M` |
| Hamming parity | `|c|_1 mod 2` | different `F_cut` tuple; also `k=0` |
| 1-site seed | run `f_L1` from `{(0,0,0)}` | fills; misses are seed-dependent |

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
| per seed | all four long-axis endpairs | no claim about the other 62 two-site seeds |
| per tick | halt histories for `f_L1` and the displayed counterexamples | no physical clock |
| lattice wide | checked and not executed | no infinite-volume formation law |

### N6 — live partial-closure paths

Live routes are an independent derivation of a formation predicate from
Admissibility, a justification of the off-patch default, and a Record
content identification. Other seeds and other cuts remain live.

### N7 — hostile steelman

**Steelman:** Because `f_L1` misses `M` by refusing `opp2`, filling all four
seeds should be the same extra as `f(opp2)=1`.

**Answer:** Silent `opp2` does force `k=0`, but firing `opp2` is not enough
to fill. The lex-first map with `f(opp2)=1` and `f(wt1)=0` locks only the
middle long-axis site and stops at three locks. The four-seed fill therefore
detects a three-bit conjunction, not the single bit.

### N8 — cross-cycle echo

This is a new selector, not a leftover listing of `f_L1`'s four misses and
not a first-neighborhood comparison of one rival map. The four seeds are
recomputed here from the `n≠0` rule.

**Gate disposition:** PASS for the finite failed equivalence and the
displayed counterexample. FAIL / DO NOT SHIP for “`opp2` is Admissibility”
or “the four seeds select `f_L1`.”

## Inputs And Dependency Roles

- **Framework context:** the Lattice nearest-neighbor cubic graph and the
  Admissibility condition-domain sentence.
- **Explicit bounded mathematical input:** the two-cube vertex set, off-patch
  occupancy `0`, the ten-orbit classification, the three `F_cut` cuts, and
  the simultaneous lock-update rule.
- **Not imported:** any unmerged census of a different seed, any Hamming
  identity for `f_L1`, and any axiom edit.

## Primary Runner

The primary runner recomputes the ten orbits, the 32 `F_cut` maps, `k(f)`
on the four long-axis seeds, the failed biconditionals, the lex-first
counterexample, the one-way silent implication, and the current premise
boundary. It authors no audit verdict.
