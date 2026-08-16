---
claim_id: f_cut_q6_q8_coverage_inclusion_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether Q6-implies-Q8 as predicates and the two coverage-inclusion facts are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q6_q8_coverage_inclusion_2026_08_15.py
---

# Whether `Q6` Implies `Q8` And The Two Coverage-Inclusion Facts

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock relation of displayed remaining-bit
predicates `Q6` and `Q8` on the twelve-vertex two-cube with off-patch
occupancy `0`, among the thirty-two cube-covariant cut maps `F_cut`,
together with the two coverage-inclusion facts on the 924 six-site seeds
and the 495 eight-site seeds.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q6_q8_coverage_inclusion_2026_08_15.py`](../scripts/f_cut_q6_q8_coverage_inclusion_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6531 showed that `cov6>0` equals
`Q6 := (wt1=1) or (adj2=1) or (vertex3=1)`. Investment #6539 showed that
`cov8>0` equals
`Q8 := (wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)`. Boolean
`Q6` implies `Q8`. This note tests that remaining-bit implication on the
32 maps and the two coverage corollaries: every `Q8`-false map has
`cov6=0`, and whether every `Q6`-false map has `cov8=0`. New relation of
the two selectors. Not leftover-character of #6531. Not leftover-character
of #6539. Those notes scored one seed family each. The present object is
the joint predicate relation and the two inclusion facts.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

The displayed remaining-bit predicates are

```text
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1)
Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1)
```

On the two-cube with off-patch occupancy `0`, write
`cov6(f) = |{S : |S|=6 and f fills from S}|` and
`cov8(f) = |{S : |S|=8 and f fills from S}|`. Then:

- Theorem 1. `N_Q6 = 28`, `N_Q8 = 30`, `N_both = 28`. `Q6` implies `Q8`
  as remaining-bit predicates.
- Theorem 2. Every `Q8`-false map has `cov6=0`. It is not true that
  every `Q6`-false map has `cov8=0`: the two extras are
  `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)`, each with `cov6 = 0` and
  `cov8 = 1`.
- Theorem 3. `Q6` and `Q8` are displayed. Displayed, not adopted. Do
  not adopt a bit.

Do not adopt `Q6`. Do not adopt `Q8`. Do not write `Q6` into
Admissibility. Do not write `Q8` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits. Whether Q6 implies Q8 as predicates, the counts N_Q6, N_Q8, N_both, and the two coverage-inclusion facts on six-site and eight-site seeds are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q6_q8_coverage_inclusion
target_blocker_text: "whether Q6 implies Q8 as remaining-bit predicates and whether the two coverage-inclusion facts hold among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q6/Q8 predicate implication and the two coverage-inclusion facts; do not adopt displayed Q6 or Q8"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current premise boundary

The only scientific dependency is the current four-axiom authority linked
above. The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom memo says the distribution concerns which possibility a forming
record locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. `Q6` and `Q8` are displayed remaining-bit formulas, not axiom
content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different rule and is not used.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0.
Complement swaps `n_both` with `n_empty`. The five remaining bits of
`F_cut`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values
on orbit types `(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The six-site seeds are the `C(12,6) = 924` subsets of size 6 in `T`. The
eight-site seeds are the `C(12,8) = 495` subsets of size 8 in `T`. Then
`cov6(f)` and `cov8(f)` are the numbers of those subsets from which `f`
fills.

Displayed, not adopted.

## Theorem 1 — `N_Q6`, `N_Q8`, `N_both`; `Q6` implies `Q8`

Enumerate all 32 remaining-bit tuples of `F_cut`. Then

```text
N_Q6 = 28
N_Q8 = 30
N_both = 28
```

`Q6` implies `Q8` as remaining-bit predicates: every map with
`wt1 = 1` or `adj2 = 1` or `vertex3 = 1` also has at least one of
`wt1`, `adj2`, `opp2`, `vertex3` equal to 1. The four `Q6`-false maps
are those with `wt1 = adj2 = vertex3 = 0`:

- `(0, 0, 0, 0, 0)`
- `(0, 0, 0, 0, 1)`
- `(0, 1, 0, 0, 0)`
- `(0, 1, 0, 0, 1)`

The two `Q8`-false maps are those with `wt1 = opp2 = adj2 = vertex3 = 0`:

- `(0, 0, 0, 0, 0)`
- `(0, 0, 0, 0, 1)`

The two `Q8`-true `Q6`-false maps are exactly `(0, 1, 0, 0, 0)` and
`(0, 1, 0, 0, 1)`, the maps whose only firing remaining bit among the
`Q8` disjuncts is `opp2`. `f_L1`, with remaining bits `(1, 0, 1, 1, 1)`,
satisfies both `Q6` and `Q8`.

## Theorem 2 — the two coverage-inclusion facts

Score `cov6` on the 924 six-site seeds and `cov8` on the 495 eight-site
seeds. Then every Q8-false map has `cov6=0`: both `(0, 0, 0, 0, 0)` and
`(0, 0, 0, 0, 1)` fill no six-site seed.

It is not every Q6-false map has `cov8=0`. The two extras are

```text
(0, 1, 0, 0, 0)    cov6 = 0    cov8 = 1
(0, 1, 0, 0, 1)    cov6 = 0    cov8 = 1
```

Those two maps are `Q6`-false and `Q8`-true. They are the only
`Q6`-false maps with positive eight-site coverage. So the predicate
implication `Q6 ⇒ Q8` has a matching coverage corollary in one
direction (every `Q8`-false map has `cov6=0`) and a two-map failure in
the converse direction (not every `Q6`-false map has `cov8=0`).

## Theorem 3 — display; do not adopt `Q6` or `Q8`

`Q6` and `Q8` are displayed remaining-bit predicates. On this patch
`Q6` implies `Q8`, every `Q8`-false map has `cov6=0`, and two
`Q6`-false maps still have `cov8=1`. Displayed, not adopted. Do not
adopt a bit. Do not adopt `Q6`. Do not adopt `Q8`. Do not write `Q6`
into Admissibility. Do not write `Q8` into Admissibility.

The implication and the two inclusion facts are finite facts about
occupancy-to-lock on this two-cube with off-patch `o=0`. They are not a
physical formation-site selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 924 six-site and 495 eight-site seeds, off-patch `o=0` | declared finite patch |
| `Q6` as `(wt1=1) or (adj2=1) or (vertex3=1)` | displayed, not adopted |
| `Q8` as `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` | displayed, not adopted |
| `Q6` implies `Q8` | holds; `N_Q6 = 28`, `N_Q8 = 30`, `N_both = 28` |
| every `Q8`-false map has `cov6=0` | holds on the two `Q8`-false maps |
| every `Q6`-false map has `cov8=0` | fails; extras `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)` |
| leftover-character of #6531 or #6539 | refused; new relation of the two selectors |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6531: that closed `cov6>0` iff `Q6` on
six-site seeds. Not leftover-character of #6539: that closed `cov8>0`
iff `Q8` on eight-site seeds. The present object is whether `Q6`
implies `Q8` as remaining-bit predicates and whether the two
coverage-inclusion facts hold. New relation of the two selectors.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q6` into Admissibility. Do not write `Q8` into
Admissibility.

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `Q6` implies `Q8` as remaining-bit predicates and whether the two coverage-inclusion facts hold inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the single-k identities for `Q6` and `Q8`, but no landed joint inclusion of the two selectors. |
| V3 | The 32 maps, 924 six-site seeds, and 495 eight-site seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against two displayed remaining-bit predicates. |
| V5 | `Q6` implies `Q8` on this patch, one coverage inclusion holds and one fails, and neither predicate is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: not every `Q6`-false map has `cov8=0`,
and displayed `Q6` and `Q8` are not axiom content. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6531 / #6539 | treat the relation as leftover-character of one seed-family identity | **ATTEMPTED** |
| `Q6` fails to imply `Q8` | find a `Q6`-true `Q8`-false remaining-bit tuple | **ATTEMPTED** |
| some `Q8`-false map has `cov6>0` | find a `Q8`-false six-site fill | **ATTEMPTED** |
| every `Q6`-false map has `cov8=0` | treat the converse coverage inclusion as a fact | **ATTEMPTED** |
| adopt `Q6` or `Q8` | write either predicate into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the single-k leftover, the failed converse
coverage inclusion, and the off-patch convention are distinct. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, the 495 eight-site seeds,
off-patch occupancy `0`, occupancy-to-lock ticks, the `F_cut`
remaining-bit order, and displayed `Q6` and `Q8` are declared. Unique
selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether `Q6`
implies `Q8` as predicates and whether the two coverage-inclusion facts
hold on the declared patch, not leftover-character of #6531 or #6539.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 924 and 495 seeds | no physical law selection |
| per block | `N_Q6`, `N_Q8`, `N_both`, and the two inclusion facts | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q6` or `Q8`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** once `cov6>0` iff `Q6` and `cov8>0` iff `Q8` are known,
`Q6` implies `Q8` is just the Boolean subset of disjuncts, so both
coverage inclusions are automatic and no new census is needed.

**Answer:** the predicate implication is Boolean and holds
(`N_Q6 = 28`, `N_Q8 = 30`, `N_both = 28`). The coverage corollary in
the `Q8`-false direction holds. The converse coverage inclusion is not
automatic: two `Q6`-false maps still have `cov8 = 1`. That failure is
the new relation of the two selectors, not a restatement of either
single-k identity.

### N8 — cross-cycle echo

Investment #6531 already showed that `cov6>0` equals `Q6`. Investment
#6539 already showed that `cov8>0` equals `Q8`. Echoing those
identities is not a substitute for testing the implication and the two
coverage-inclusion facts on the same 32 maps.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow converse-inclusion failure. FAIL / DO NOT SHIP for “adopt a bit”
or “displayed `Q6` or `Q8` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov6` on the
924 six-site seeds and `cov8` on the 495 eight-site seeds, reports
`N_Q6 = 28`, `N_Q8 = 30`, and `N_both = 28`, reports that `Q6` implies
`Q8`, reports that every `Q8`-false map has `cov6=0`, and reports that
not every `Q6`-false map has `cov8=0`. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.
