---
claim_id: sparsest_one_site_filler_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among cube-covariant 1-site fillers on the two-cube with off-patch o=0, the minimal support size is 26 and N_min = 1 maps achieve it. f_L1 is not the unique minimizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/sparsest_one_site_filler_2026_08_15.py
---

# Sparsest One-Site Filler On The Two-Cube

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact support census among the cube-covariant occupancy
predicates that fill the twelve-vertex two-cube from a 1-site seed with
off-patch occupancy `o=0`. No occupancy axiom is added. No physical
selector is inferred.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/sparsest_one_site_filler_2026_08_15.py`](../scripts/sparsest_one_site_filler_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the six nearest-neighbor occupancy bits of one site. A cell is a
6-tuple `c ∈ {0,1}^6` recording occupancy of `+x,-x,+y,-y,+z,-z`. The
24 proper cube rotations act on those signed directions and partition the
64 cells into 10 orbits. A cube-covariant predicate is a `{0,1}`-label of
orbits. Restrict to `f(empty)=0`. There are `2^9 = 512` such maps.

The displayed two-cube is the twelve-vertex set
`{0,1,2} × {0,1} × {0,1}` (two unit cubes sharing the face `x=1`).
Off-patch neighbors have occupancy `0`. Seed-lock `(0,0,0)`. Each tick
locks every unlocked on-patch vertex whose current 6-tuple has `f=1`.
Halt is the first fixed point (at most 12 ticks). A map *fills* when all
12 vertices are locked at halt.

Define `f_L1(c)=1` if and only if some axis is unbalanced:
`c_{+μ} ≠ c_{-μ}` for some `μ ∈ {x,y,z}`. Equivalently the cubic occupancy
kernel `n_μ = c_{+μ} − c_{-μ}` satisfies `n ≠ 0`. This is **never**
Hamming parity `|c|_1 mod 2`.

Among the 512 maps, exactly `N_fill = 96` fill, and `f_L1` is one of them.
For a filler `f` write

```text
supp(f) = |{ c ∈ {0,1}^6 : f(c)=1 }| = Σ_{orbits O with f|O=1} |O|.
```

The minimum is `m = 26`, attained by exactly `N_min = 1` filler. That
unique minimizer is **not** `f_L1` (`supp(f_L1)=56`). It is the
axis-transversal predicate

```text
f_min(c)=1  iff  c ≠ empty and c_{+μ}+c_{-μ} ≤ 1 for every axis μ.
```

So `supp(f_min)=3^3−1=26`. Sparsity among 1-site fillers therefore
selects `f_min`, not `f_L1`. Displayed, not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 10-orbit catalog, the 512-map fill census, and the support minimum among the 96 fillers are finite exact enumerations; f_L1 is exhibited as a filler that is not the unique support-minimizer. No occupancy axiom is adopted."
trace_class: negative_route_pruning
target_claim_id: sparsest_one_site_filler_bounded_theorem
target_blocker_text: "does support-minimality among cube-covariant 1-site fillers select f_L1 without an extra axiom"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the finite census; any physical use of f_min or f_L1 must be separately derived"
conditional_surface_status: "exact for the twelve-vertex two-cube, off-patch o=0, and the 512 empty-vanishing cube-covariant maps; infinite-lattice fill remains unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** Reconfirm that 96 of the 512 empty-vanishing
cube-covariant maps fill the twelve-vertex two-cube from the 1-site seed
with off-patch `o=0`, and that `f_L1` is among them. Compute
`m = min supp(f)` over those fillers and `N_min = |{fillers : supp=m}|`.
Decide whether `N_min=1` and that unique minimizer is `f_L1`. If not,
display a sparser or tied filler. Displayed, not adopted.

| Obligation | Disposition |
|---|---|
| 24 proper rotations and 10 orbits on `{0,1}^6` | proved here in Theorem 1 |
| `N_fill=96` and `f_L1` fills | proved here in Theorem 1 |
| `m` and `N_min` | proved here in Theorem 2 |
| unique minimizer is not `f_L1`; `f_min` is displayed | proved here in Theorem 3 |
| Hamming parity is not `f_L1` and does not fill | mutation, Theorem 3 |
| Lattice nearest-neighbor / proper-cubic covariance | quoted from the live axiom memo |
| adoption of `f_min` or `f_L1` as an axiom | refused; remains open |

No terminal lemma equivalent to the target is left open. The fill count
itself is only reconfirmed so that the support minimum is taken over the
correct 96-element set.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice nearest-neighbor adjacency, proper cubic rotations, and
  one covariant nearest-neighbor admissibility rule. As the registered
  `minimal_axioms` premise, it is not a bounded-status source.
- The twelve-vertex two-cube, the seed `(0,0,0)`, and the off-patch default
  `o=0` are displayed hypotheses, not derived physical selectors.
- Occupancy predicates, including `f_L1` and `f_min`, are displayed maps
  on `{0,1}^6`. The axioms do not select either map.
- No measured, fitted, observational, or phenomenological value is used.

## Exact Objects

A cell is written in the order `(c_{+x},c_{-x},c_{+y},c_{-y},c_{+z},c_{-z})`.
The proper cube group is the 24 signed-permutation matrices of determinant
`+1`. A rotation `R` acts by `(R·c)_{R d} = c_d` on signed directions `d`.

The 10 orbits, ordered by representative and listed with size and a
geometric name, are:

| Orbit | Size | Weight | Representative | Geometry |
|---|---:|---:|---|---|
| 0 | 1 | 0 | `(0,0,0,0,0,0)` | empty |
| 1 | 6 | 1 | `(0,0,0,0,0,1)` | one signed direction |
| 2 | 3 | 2 | `(0,0,0,0,1,1)` | both signs of one axis |
| 3 | 12 | 2 | `(0,0,0,1,0,1)` | two axes, one sign each |
| 4 | 12 | 3 | `(0,0,0,1,1,1)` | one pair plus one single |
| 5 | 3 | 4 | `(0,0,1,1,1,1)` | both signs of two axes |
| 6 | 8 | 3 | `(0,1,0,1,0,1)` | all three axes, one sign each |
| 7 | 12 | 4 | `(0,1,0,1,1,1)` | one pair plus two singles |
| 8 | 6 | 5 | `(0,1,1,1,1,1)` | all but one signed direction |
| 9 | 1 | 6 | `(1,1,1,1,1,1)` | full |

`f_L1` is 1 exactly on the unbalanced orbits `{1,3,4,6,7,8}`, so
`supp(f_L1)=6+12+12+8+12+6=56`. Hamming parity `|c|_1 mod 2` is 1 on
`{1,4,6,8}` and is a different map.

`f_min` is 1 exactly on the nonempty axis-transversals `{1,3,6}`, so
`supp(f_min)=6+12+8=26`.

The two-cube vertices are all `(x,y,z)` with `x∈{0,1,2}` and
`y,z∈{0,1}`. A neighbor off this set contributes occupancy `0`.

## Theorem 1 — fill census and `f_L1`

There are 24 proper cube rotations and 10 orbits. Exactly 512
cube-covariant maps vanish on the empty orbit. Exhaustive execution of
the lock tick on the twelve-vertex two-cube with seed `(0,0,0)` and
off-patch `o=0` yields `N_fill=96`. The map `f_L1` is cube-covariant,
vanishes on empty, and locks all 12 vertices after four ticks, with
lock counts `(1,4,8,11,12)`.

## Theorem 2 — minimal support among fillers

For each of the 96 fillers, `supp(f)` is the sum of the sizes of the
orbits labelled 1. The observed support histogram has unique minimum
bin `26`. Hence `m=26` and `N_min=1`.

No filler is supported only on the weight-1 orbit (`supp=6`): that map
halts at 7 locks. The pair of orbits `{1,3}` (`supp=18`) halts at 11
locks. Those two sparser candidates are therefore not fillers.

## Theorem 3 — the unique minimizer is not `f_L1`

The unique filler with `supp=26` is `f_min`, the nonempty
axis-transversal predicate displayed above. It is a strict subset of
`f_L1` and is not Hamming parity. It fills, with the same lock-count
sequence `(1,4,8,11,12)` as `f_L1`.

`f_L1` itself has support 56 and is therefore not a support-minimizer.
Hamming parity is cube-covariant and empty-vanishing, but it is not
`f_L1` and it does not fill: it halts at 9 locks.

Sparsity among 1-site fillers therefore does not select `f_L1`. The
displayed unique minimizer is not adopted as an axiom.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on cells,
   and Hamming halts at 9 locks.
2. Claim `f_L1` is the unique support-minimizer: `supp(f_L1)=56≠26`.
3. Treat the 512-count as the theorem: that only enumerates maps, not
   the support minimum among fillers.
4. Drop orbits 3 and 6 from `f_min`: the weight-1 orbit alone is not a
   filler.
5. Replace the proper 24-element group by a different action: the 10-orbit
   catalog and the 512-count are those of the proper cube group quoted
   from Lattice.
6. Adopt `f_min` as an axiom because it is the unique minimizer: the
   census is a displayed finite fact, not a framework edit.

## What This Does Not Claim

- No adoption of `f_min`, `f_L1`, or any other occupancy predicate.
- No fill statement off the twelve-vertex two-cube or for a seed other
  than `(0,0,0)` with off-patch `o=0`.
- No identification of occupancy bits with Record content or with a
  physical formation rate.
- No Hamming-parity rewrite of `f_L1`.
- No selection of a leftover character of the 96-count: the object here
  is the support minimum among those fillers.

## No-Go Discipline Gate

The negative claim is only this: among cube-covariant 1-site fillers on
the displayed two-cube, support-minimality does not select `f_L1`. It is
not a claim that `f_L1` fails to fill, and it is not a claim that no
sparse filler exists.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| Hamming rewrite of `f_L1` | Compare `f_L1` with `|c|_1 mod 2` on all 64 cells and run both fill dynamics. | Theorem 3 and runner checks `l1-not-hamming` / `mutation-hamming-nine-locks`: the maps differ; Hamming halts at 9 locks. | **ATTEMPTED** |
| `f_L1` as unique minimizer | Compute `supp(f_L1)` and the unique `supp=26` filler. | Theorems 2–3 and checks `l1-support-56` / `thm3-unique-is-not-l1`. | **ATTEMPTED** |
| leftover 96-count | Stop after `N_fill=96`. | Theorem 2 continues to the support minimum; the 96-count is only the domain of that minimum. | **ATTEMPTED** |
| weight-1-only sparsity | Run the orbit-1 predicate (`supp=6`). | Theorem 2 and check `mutation-weight-one-only`: 7 locks, not a filler. | **ATTEMPTED** |
| different rotation group | Rebuild orbits from the 24 determinant-`+1` signed permutations. | Theorem 1 and checks `rotations-24` / `orbits-10` recover the 10-orbit catalog used by the 512-count. | **ATTEMPTED** |
| axiom adoption of `f_min` | Read the note's adoption boundary. | Machine status `hypothetical_axiom_status` and the displayed-not-adopted sentence refuse the edit. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: sparsity does not select `f_L1`. The
Hamming mismatch, the support comparison `56≠26`, and the explicit
display of `f_min` are three certificates of that one conclusion; they
collapse rather than count as independent walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| Hamming ≠ `f_L1` / `f_L1` not minimizer | no: a different non-filler does not classify supports of actual fillers | no: a larger-support filler need not be Hamming | independent certificates, one conclusion |
| unique `f_min` / `f_L1` not minimizer | yes, once `f_min ≠ f_L1` is checked | yes, because `N_min=1` and the minimizer is `f_min` | collapse into the unique-minimizer statement |
| weight-1 non-fill / unique `f_min` | no: it only removes one sparser candidate | no: uniqueness among fillers does not by itself name every failed sparser map | checked alternative, not a second wall |

Infinite-lattice fill and axiom adoption are not counted as walls: this
note makes no negative theorem about them and simply does not claim them.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “twelve-vertex two-cube”, seed `(0,0,0)`, `o=0` | explicit theorem hypotheses |
| “cube-covariant” | proper cube rotations from the quoted Lattice sentence |
| “filler” | lock-all-12 on this finite patch, not a lattice-wide law |
| “`f_L1` is `n ≠ 0`” | displayed definition; never Hamming parity |
| “`f_min` is an axis-transversal” | displayed unique minimizer; not an adopted rule |
| “Displayed, not adopted” | explicit refusal of an axiom edit |

### N4 — citation-to-residual matching

| Evidence path | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Lattice sentence | rotation group and nearest-neighbor 6-tuple | proper cubic rotations and NN adjacency only | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Admissibility covariance | one covariant nearest-neighbor rule | covariance of the *class* of maps; no map selected | yes; selector stays open |
| `scripts/sparsest_one_site_filler_2026_08_15.py` `thm1-n-fill-96` | fill census domain | `N_fill=96` and `f_L1` fills | yes |
| `scripts/sparsest_one_site_filler_2026_08_15.py` `thm2-minimum-26` | support minimum | `m=26`, `N_min=1` | yes |
| `scripts/sparsest_one_site_filler_2026_08_15.py` `thm3-unique-is-not-l1` | uniqueness of `f_L1` by sparsity | unique minimizer is `f_min`, not `f_L1` | yes |
| `scripts/sparsest_one_site_filler_2026_08_15.py` `l1-not-hamming` | Hamming rewrite | `f_L1` disagrees with `|c|_1 mod 2` | yes |

No evidence citation is used to claim that an occupancy axiom, a physical
Record readout, or an infinite-lattice fill law has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 cells | each cell contributes to `supp(f)` by its orbit |
| per site | yes: all 12 two-cube vertices | fill means those 12 lock; no other sites are tested |
| per mode | yes: the 512 empty-vanishing cube-covariant maps | the 96 fillers and their supports are the executed family |
| per block | yes: support minimum among fillers | unique minimum 26 is `f_min`, not `f_L1` |
| lattice wide | no | no infinite-lattice fill or adopted occupancy rule is asserted |

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies an occupancy predicate, and none is
reclassified as an import or wall.

Two partial-closure mechanisms were tested rather than suppressed.
`f_L1` does fill, so the negative is not “`f_L1` fails”. The
axis-transversal `f_min` does fill and is strictly sparser, so the
negative is not “no sparse filler exists”. The remaining physical
choice—whether either map is the actual Admissibility rule—stays
explicit and does not require an axiom edit to state honestly.

### N7 — hostile steelman

The strongest objection is that `f_min` is just `f_L1` restricted to the
cells that actually appear in the two-cube 1-site dynamics, so sparsity
still “selects L1 in practice.” That objection is false on the executed
family: both maps see the same first-wave weight-1 cells, but later
ticks expose weight-2 and weight-3 cells, and `f_min` accepts only the
axis-transversal ones. The maps disagree on 30 cells
(`56−26=30`), including the weight-3 pair-plus-single orbit, which
`f_L1` accepts and `f_min` rejects. They are distinct cube-covariant
fillers. Sparsity selects the smaller one.

### N8 — cross-cycle echo

The 96-count is the fill census of the same 512-map class. This note
recomputes that count only to fix the domain of the support minimum. It
does not treat the 96-count as a leftover character, and it does not
borrow a Hamming rewrite of `f_L1`. No earlier landed surface on
`origin/main` retires the support-minimizer question.

No-Go Discipline disposition: **PASS** for the algebraic negative
boundary stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

## Runner Contract

The companion runner rebuilds the 24 proper rotations and 10 orbits,
enumerates the 512 empty-vanishing cube-covariant maps, executes the
1-site fill dynamics, reconfirms `N_fill=96` and that `f_L1` fills,
computes the support minimum `m=26` with `N_min=1`, exhibits `f_min` as
that unique minimizer, rejects the Hamming rewrite, and checks the
displayed-not-adopted axiom boundary. Declared audit inputs are this
note and the axiom memo. The runner writes no cache and no citation
manifest.
