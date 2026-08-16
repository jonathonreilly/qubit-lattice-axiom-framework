---
claim_id: f_cut_cov6_positive_q4_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 6-site coverage is equivalent to (wt1=1) or (adj2=1) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov6_positive_q4_2026_08_15.py
---

# Whether Positive 6-Site Coverage Equals Q4 Among the 32 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 924 six-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov6_positive_q4_2026_08_15.py`](../scripts/f_cut_cov6_positive_q4_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6518 showed that `cov4>0` if and only if the remaining-bit
predicate `Q4(f) := (wt1=1) or (adj2=1)` among the 32 maps. Investment #6476
showed that `Max(k)=Max(12-k)` only for `k=4,5`. This note repeats the same
displayed predicate on a new seed cardinality: six-site seeds. New k for Q4,
not leftover-character of those two investments and not a Max(6) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov6(f) = |{S : |S|=6 and f fills from S}|`. Then:

- Theorem 1. `cov6(f) > 0` is not equivalent to `Q4(f)` among the 32 maps.
  The lex-first remaining-bit counterexample is `(0, 0, 0, 1, 0)`, which has
  `Q4 = 0` and `cov6 = 4`.
- Theorem 2. `N_Q4 = 24`, `N_pos = 28`, `N_both = 24`.
- Theorem 3. `Q4` is displayed. Displayed, not adopted.

Do not adopt Q4. Do not write `Q4` into Admissibility. The extra that would
have made 6-site positivity the same selector as 4-site positivity is not
present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 924 six-site seeds of the two-cube. Whether cov6>0 equals Q4, and the counts N_Q4, N_pos, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov6_positive_q4
target_blocker_text: "whether cov6>0 is the same selector Q4 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 6-site positivity-versus-Q4 comparison; do not adopt the displayed predicate Q4"
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
predicate. `Q4` is a displayed remaining-bit formula, not axiom content.

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

The six-site seeds are the `C(12,6) = 924` subsets of size 6 in `T`. Then
`cov6(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov6(f)>0`.

The displayed remaining-bit predicate is

```text
Q4(f) := (wt1 = 1) or (adj2 = 1).
```

Opp2, vertex3, and mixed3 are free in `Q4`. Displayed, not adopted.

## Theorem 1 — `cov6>0` is not `Q4`; lex-first witness

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov6` on the 924
six-site seeds. Then `cov6(f) > 0` is not equivalent to `Q4(f)`.

The lex-first remaining-bit counterexample, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 0, 1, 0)`. That map has
`wt1 = 0` and `adj2 = 0`, so `Q4` is false, and `cov6 = 4 > 0`.

## Theorem 2 — `N_Q4`, `N_pos`, `N_both`

Among the 32 maps:

- `N_Q4 = 24` maps satisfy `Q4`;
- `N_pos = 28` maps have `cov6 > 0`;
- `N_both = 24` maps satisfy both.

Every `Q4`-true map has `cov6 > 0`. Equivalence fails only in the other
direction: four `Q4`-false maps still have positive 6-site coverage. Those
four are exactly the maps with `wt1 = 0`, `adj2 = 0`, and `vertex3 = 1`:

- `(0, 0, 0, 1, 0)` with `cov6 = 4`;
- `(0, 0, 0, 1, 1)` with `cov6 = 12`;
- `(0, 1, 0, 1, 0)` with `cov6 = 20`;
- `(0, 1, 0, 1, 1)` with `cov6 = 28`.

The four maps with `wt1 = 0`, `adj2 = 0`, and `vertex3 = 0` have `cov6 = 0`.

## Theorem 3 — display; do not adopt `Q4`

`Q4` is the same remaining-bit predicate that #6518 found equivalent to
`cov4>0`. On six-site seeds it is not the positivity selector. Displayed,
not adopted. Do not adopt Q4. Do not write `Q4` into Admissibility.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q4` and has
`cov6 = 920`. That is consistent with Theorem 2 and does not restore
equivalence.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 924 six-site seeds, off-patch `o=0` | declared finite patch |
| `Q4` as `(wt1=1) or (adj2=1)` | displayed, not adopted |
| `cov6>0` iff `Q4` | fails; lex-first witness `(0, 0, 0, 1, 0)` |
| `N_Q4 = 24`, `N_pos = 28`, `N_both = 24` | proved by exhaustive scoring |
| leftover-character of #6518 or #6476 | refused; new k for Q4 |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6518: that closed `cov4>0` iff `Q4` on four-site
seeds. The present count is `cov6` on 924 six-site seeds, a different seed
family.

Not leftover-character of #6476: that compared `Max(k)` with `Max(12-k)`
and found equality only for `k=4,5`. The present object is 6-site
positivity versus displayed `Q4`, not a maximizer complementarity.

The note is not a Max(6) ranking and not a seed-table: maximizers of `cov6`
are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q4` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 6-site positivity is the same selector as `Q4` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6518 fact that `cov4>0` is `Q4`, but no landed 6-site positivity-versus-`Q4` comparison. |
| V3 | The 32 maps, 924 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against displayed `Q4`. |
| V5 | Equivalence fails, and displayed `Q4` is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov6>0` is not equivalent to `Q4` among the
32 `F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6518 | treat the 6-site comparison as leftover-character of `cov4>0` iff `Q4` | **ATTEMPTED** |
| leftover of #6476 | treat the count as leftover-character of `Max(k)=Max(12-k)` | **ATTEMPTED** |
| Max(6) rename | replace positivity-versus-`Q4` by a 6-site maximizer ranking | **ATTEMPTED** |
| adopt `Q4` | write `(wt1=1) or (adj2=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed equivalence, the Hamming contrast, the #6518 four-site identity,
and the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
predicate `Q4` are declared. Equivalence of `cov6>0` with `Q4` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether 6-site
positivity equals `Q4` on the declared patch, not leftover-character of
#6518 or #6476, and not a Max(6) ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 924 seeds | no physical law selection |
| per block | `N_Q4`, `N_pos`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q4` or `cov6>0`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6518 already showed that positivity is `Q4`, so every later
`k` inherits the same selector.

**Answer:** Inheritance fails at `k=6`. Twenty-four maps satisfy `Q4` and
all of them have `cov6>0`, but twenty-eight maps have `cov6>0`. The
lex-first witness `(0, 0, 0, 1, 0)` has `Q4` false and `cov6 = 4`.
Displayed `Q4` is not adopted.

### N8 — cross-cycle echo

Investment #6518 already showed that `cov4>0` is `Q4`. Investment #6476
already compared complementary maximizers. Echoing either fact is not a
substitute for the six-site count: `k=6` is a new seed family, and the
lex-first witness and the triple `(N_Q4, N_pos, N_both)` are six-site facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow equivalence failure. FAIL / DO NOT SHIP for “`cov6>0` is `Q4`” or
“displayed `Q4` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov6` on the
924 six-site seeds, compares positivity with displayed `Q4`, reports the
lex-first remaining-bit counterexample `(0, 0, 0, 1, 0)`, and reports
`N_Q4 = 24`, `N_pos = 28`, and `N_both = 24`. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.
