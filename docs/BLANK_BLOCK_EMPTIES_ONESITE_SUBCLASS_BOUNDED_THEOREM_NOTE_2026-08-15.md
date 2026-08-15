---
claim_id: blank_block_empties_onesite_subclass_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the twelve-vertex two-cube, replacing off-patch o=0 by blank-block empties the 1-site first wave for every cube-covariant f, including every f with f(wt1)=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/blank_block_empties_onesite_subclass_2026_08_15.py
---

# Blank-Block Empties The One-Site First Wave For The Whole Ready Subclass

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the twelve-vertex two-cube; cube-covariant boolean formation
predicates on occupancy 6-tuples; blank-block versus the off-patch occupancy-0
default. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/blank_block_empties_onesite_subclass_2026_08_15.py`](../scripts/blank_block_empties_onesite_subclass_2026_08_15.py)

## Result up front

Treat a 1-site seed at `(0,0,0)` on the twelve-vertex two-cube
`A ∪ B` with `A = {0,1}^3` and `B = {1,2} × {0,1}^2`. A cube-covariant
formation predicate is a function `f : {0,1}^6 → {0,1}` constant on orbits of
the 24 proper cube rotations acting on the six directed nearest-neighbor
slots. Write `wt1` for the orbit of weight-1 cells (exactly one occupied
slot). The subclass `f(wt1)=1` is the isolated one-axis contrast class: a
site whose six-tuple is one occupied neighbor and five zeros is ready when
off-patch occupancy is defaulted to `0`.

Blank-block is a different neighbor rule. If any of the six lattice neighbors
is off-patch, the 6-tuple is undefined and the site is not ready; `f` is not
evaluated. That rule empties the first wave after the seed, for every
cube-covariant `f`, including every member of `f(wt1)=1`. So every
1-site-ready member needs the vacuum default `o=0` on this patch. The need
is class-level, not only for L1.

L1 is the displayed member `f_L1(c)=1` iff some axis is unbalanced
(`c_{+μ} ≠ c_{-μ}`), equivalently `n≠0` with `n` the number of unbalanced
axes. It is not Hamming parity `|c|_1 mod 2`. Those two maps agree on `wt1`
and disagree on two-axis weight-2 cells such as `(1,0,1,0,0,0)`.

This is not a second vacalt. Vacalt compared L1 under `o=0` with L1 under
blank-block. The present object is the whole `f(wt1)=1` subclass. It is also
not leftover character of the blank-versus-zero selector count: the census
here is a first-wave emptiness statement on one patch, not an orbit count of
maps on `{0,1,blank}^6`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite two-cube neighbor listing and exact first-wave emptiness under blank-block; no formation law is adopted and no vacuum axiom is written."
trace_class: selector_identification
target_claim_id: onesite_ready_vacuum_default_class
target_blocker_text: "1-site formation on the two-cube under blank-block has an empty first wave for every cube-covariant f, so a vacuum default is extra data for the whole f(wt1)=1 subclass"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep blank-block and the o=0 default as named extra selectors; do not write either as axiom text"
conditional_surface_status: "exact only for the supplied twelve-vertex two-cube, 1-site seed, and blank-block rule"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
nearest-neighbor adjacency on `Z^3` and one fixed covariant admissibility
rule for the local possibility distribution. It says:

```text
For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.
```

Admissibility does not name a formation predicate, a vacuum default, or a
blank-block rule. Record says that records form, that a present record locks
exactly one admissible local possibility, and that a site with no record
cannot be read. Record does not assign occupancy `0` to an unread neighbor
and does not define readiness.

The two-cube, the seed, the class of cube-covariant `f`, blank-block, and
the `o=0` default are declared test objects. None of them is written into
the axiom memo.

## Exact objects

Slots are the six directed nearest neighbors in the order
`(+x,-x,+y,-y,+z,-z)`. The 24 proper cube rotations permute those slots.
Weight-1 cells form one orbit of size six. Cube-covariant predicates are
exactly the `{0,1}`-colorings of the occupancy orbits.

A site `v` on the patch is **blank-blocked** when at least one of
`v±e_x`, `v±e_y`, `v±e_z` lies off the twelve-vertex set. Under
blank-block such a `v` is not ready.

Under the `o=0` default, an off-patch neighbor is occupancy `0` and an
on-patch unread neighbor is occupancy `0`. The resulting 6-tuple is always
defined, and `v` is ready when `f` of that 6-tuple is `1`.

After only the seed, a neighbor is occupied-as-record only if it is the
seed. No unlocked site then has six record neighbors.

## Theorem 1 — the three first-wave candidates are blank-blocked

Under `o=0`, the unlocked sites `(1,0,0)`, `(0,1,0)`, and `(0,0,1)` each
see a weight-1 6-tuple: the seed occupies exactly one slot and the other
five slots are `0`. Those three sites are the first-wave candidates for
every `f` with `f(wt1)=1`.

Each of those three sites has at least one off-patch lattice neighbor.
Blank-block therefore leaves all three unready, independently of `f`.

## Theorem 2 — the first wave is empty for every cube-covariant `f`

The two-cube is the `3×2×2` box `{0,1,2}×{0,1}×{0,1}`. Every site, seed
included, has `y∈{0,1}` and therefore misses at least one of `±e_y`; the
same holds for `z`. No site has all six lattice neighbors on-patch.

After only the seed, no unlocked on-patch site has all six neighbors
on-patch and occupied-as-records. Blank-block therefore finds no ready
site. The first wave is empty for every cube-covariant `f`, including every
`f` with `f(wt1)=1`. The paired runner enumerates the whole covariant class
and the `f(wt1)=1` subclass and checks emptiness directly.

## Theorem 3 — the vacuum default is class-level extra

Under `o=0`, the same seed makes those three axis sites ready for every
`f` with `f(wt1)=1`, and in particular for `f_L1`. If also `f(empty)=0`,
as holds for `f_L1`, they are the entire first wave; if `f(empty)=1`, the
eight leftover unlocked sites see the all-zero 6-tuple and join the `o=0`
wave. Blank-block removes every one of those candidates. Therefore 1-site
formation on this patch requires the `o=0` default for the entire
`f(wt1)=1` subclass, not only for L1.

No member is adopted. Blank-block is not written as axiom text. Unread
is not occupancy `0` in the Record axiom.

## What this does not claim

- It does not adopt L1, blank-block, or the `o=0` default as physical law.
- It does not write a vacuum axiom or amend Lattice, Qubit, Admissibility,
  or Record.
- It does not identify `f_L1` with Hamming parity `|c|_1 mod 2`.
- It does not count halt fillings, later ticks, or maps on `{0,1,blank}^6`.
- It does not claim a formation rate, clock, or full-lattice history.
- It does not treat this two-cube as the only possible patch.

## Displayed claim scope

On the twelve-vertex two-cube, replacing off-patch o=0 by blank-block
empties the 1-site first wave for every cube-covariant f, including every f
with f(wt1)=1. Displayed, not adopted.
