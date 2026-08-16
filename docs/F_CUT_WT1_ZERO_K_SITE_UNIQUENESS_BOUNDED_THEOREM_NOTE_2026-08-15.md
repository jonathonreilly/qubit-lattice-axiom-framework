---
claim_id: f_cut_wt1_zero_k_site_uniqueness_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 16 F_cut maps with wt1=0 on the two-cube with off-patch o=0, the seed sizes at which coverage has a unique maximizer are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py
---

# For Which Seed Sizes Is Coverage Unique Inside The Sixteen `wt1=0` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage uniqueness set of the 16
cube-covariant complement-even predicates that vanish on empty and full and
have remaining bit `wt1=0`, on the twelve-vertex two-cube, over all k-site
seeds for each `k ∈ {4,5,6,7,8,9,10,11}`, with off-patch occupancy `0`.
Seed sizes 1, 2, and 3 are cited (none fill all 12 at k=1; #6482 m2=0
`N_max=16`; #6483 m3=44 `N_max=2`) and are not re-censused. The unique
remaining-bit tuple on `K_unique` is displayed. No map is adopted as the
physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py`](../scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so

```text
|F_cut| = 32.
```

The five remaining bits, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Exactly one of those bits is `wt1`. The subclass scored here
is the 16 maps with remaining bit `wt1=0`. Write

```text
|F_W0| = 16.
```

That static split of `F_cut` is leftover-character inventory. A single-k
coverage ranking of the same 16 maps is also leftover inventory of one seed
cardinality. New selector, not leftover of one k. This note asks the new
ranking object: among the 16 maps with `wt1=0`, for each census seed size,
how many k-site seeds does each fill, and at which k is the maximizer
unique.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered k-set of vertices is
a k-site seed. Off-patch neighbors have occupancy `0`. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy tuple
and locks if `f=1`. The process is synchronous and stops at a fixed point
in at most 12 ticks. Fill means `|locks_halt|=12`. Coverage is

```text
cov_k(f) = |{ S : |S|=k and f fills from S }|.
```

Do not list the seeds. Do not re-census k=1,2,3.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. f_L1 has remaining-bit tuple `(1, 0, 1, 1, 1)`, so remaining bit
`wt1=1`. It is outside the scored
subclass and is not a candidate for a subclass maximizer.

**Theorem 1.** Exhaustive ranking of the 16 maps with remaining bit
`wt1=0` on every k-site seed for each census size gives

```text
m_4 = 300
N_max_4 = 1
m_5 = 656
N_max_5 = 1
m_6 = 864
N_max_6 = 1
m_7 = 776
N_max_7 = 1
m_8 = 493
N_max_8 = 1
m_9 = 220
N_max_9 = 2
m_10 = 66
N_max_10 = 2
m_11 = 12
N_max_11 = 4.
```

**Theorem 2.** Write `K_unique = {k ∈ 1..11 : N_max_k = 1}`. Citing that
none fill all 12 at k=1 (so `N_max_1 = 16`), #6482 (`m2=0`,
`N_max_2 = 16`), and #6483 (`m3=44`, `N_max_3 = 2`) without recomputing
those three as the claim,

```text
K_unique = {4, 5, 6, 7, 8}.
```

**Theorem 3.** For each `k ∈ K_unique` the unique remaining-bit tuple is

```text
(0, 1, 1, 1, 1).
```

Displayed, not adopted. Do not adopt a map.

Do not write the ranking into Admissibility.

Not leftover-character of #6482 (that was the 2-site ranking; different |S|).
Not leftover-character of #6483 (that was the 3-site ranking; different |S|).
New selector, not leftover of one k.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the 16-element wt1=0 subclass, the eight census pairs (m_k,N_max_k), the cited N_max values at k=1,2,3, the uniqueness set K_unique={4,5,6,7,8}, and the unique remaining-bit tuple (0,1,1,1,1) are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_wt1_zero_k_site_uniqueness
target_blocker_text: "does any |S| select a unique member of the 16-map wt1=0 half"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the wt1=0 k-site uniqueness set; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the wt1=0 half of F_cut on this twelve-vertex patch with off-patch o=0 and the eight census seed sizes, citing k=1 and #6482/#6483 for k=2,3; no Z^3-wide law and no physical selector"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Mathematical Objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3`, nearest-neighbor adjacency, and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule covariant
under those rotations. Record supplies permanence of a lock and unreadability
of an absent record. Qubit is unused beyond the ambient one-site algebra
boundary: the maps here are Boolean occupancy predicates, not `M_2(C)`-valued
laws.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- the complete set of k-site seeds for each census `k`;
- the remaining-bit filter `wt1=0`;
- the cited ranking facts that none fill all 12 at k=1, `m2=0` with
  `N_max_2=16` (#6482), and `m3=44` with `N_max_3=2` (#6483).

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Rank the 16 members of `F_cut` with remaining bit `wt1=0` by
k-site fill coverage on the two-cube for each `k ∈ {4,5,6,7,8,9,10,11}`,
form `K_unique = {k ∈ 1..11 : N_max_k = 1}` by adjoining the cited values
at k=1,2,3, and display the unique remaining-bit tuple at each member of
`K_unique`.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

| remaining name | `(u,b,e)` | orbit size | complement image |
|---|---|---:|---|
| empty | `(0,0,3)` | 1 | full |
| full | `(0,3,0)` | 1 | empty |
| `opp2` | `(0,1,2)` | 3 | `(0,2,1)` |
| `wt1` | `(1,0,2)` | 6 | `(1,2,0)` |
| `adj2` | `(2,0,1)` | 12 | `(2,1,0)` |
| `mixed3` | `(1,1,1)` | 12 | itself |
| `vertex3` | `(3,0,0)` | 8 | itself |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`. The remaining-bit tuple is those five bits in the order
`(wt1, opp2, adj2, vertex3, mixed3)`. The scored subclass is the 16
tuples whose first coordinate is `0`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and lies outside the
subclass. Neither `f_L1` nor the displayed unique remaining-bit tuple is
adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov_k(f)` is the number of k-site seeds whose halt set has
cardinality 12, `m_k` is the maximum of `cov_k` over the 16 maps with
`wt1=0`, and `N_max_k` is the number of those maps attaining `m_k`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly 16 of
those maps have remaining bit `wt1=0`. The unbalanced-axis map `f_L1` is
one element of `F_cut` and is not Hamming parity; its remaining bit
`wt1` is `1`, so it is not among the 16. On the twelve-vertex two-cube
with off-patch occupancy `0`, exhaustive ranking of the 16 maps on every
census seed size gives the eight pairs

```text
(m_4, N_max_4) = (300, 1)
(m_5, N_max_5) = (656, 1)
(m_6, N_max_6) = (864, 1)
(m_7, N_max_7) = (776, 1)
(m_8, N_max_8) = (493, 1)
(m_9, N_max_9) = (220, 2)
(m_10, N_max_10) = (66, 2)
(m_11, N_max_11) = (12, 4).
```

**Theorem 2.** The uniqueness set, using the cited values `N_max_1=16`
(none fill all 12), `N_max_2=16` (#6482), and `N_max_3=2` (#6483) and
the eight computed `N_max_k`, is

```text
K_unique = {4, 5, 6, 7, 8}.
```

Those three cited cardinalities are not recomputed here.

**Theorem 3.** For each `k ∈ K_unique` the unique remaining-bit tuple is
`(0, 1, 1, 1, 1)`. Displayed, not adopted. Do not adopt a map.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after empty/full are forced to `0` |
| 16 maps with `wt1=0` | the remaining bit on orbit `(1,0,2)` and its complement `(1,2,0)` is fixed to `0`; the other four free bits vary |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` and has remaining bits `(1, 0, 1, 1, 1)` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| eight census seed counts | `C(12,k)` for `k ∈ {4,5,6,7,8,9,10,11}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| eight pairs `(m_k, N_max_k)` | exhaustive 16-map ranking of `cov_k` on each census size |
| cited `N_max_1,N_max_2,N_max_3` | none fill all 12, #6482, #6483; not recomputed |
| `K_unique={4,5,6,7,8}` | `{k ∈ 1..11 : N_max_k=1}` |
| unique remaining-bit tuple | `(0, 1, 1, 1, 1)` at each of 4, 5, 6, 7, 8; displayed, not adopted |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member
   with `wt1=1`.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the uniqueness set is a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Flip remaining bit `wt1` to `1`: the scored class is no longer `F_W0`.
5. Score only 2-site seeds: that leftover is #6482, a different `|S|`.
6. Score only 3-site seeds: that leftover is #6483, a different `|S|`.
7. Restrict uniqueness to a single census k: that leftover is one
   cardinality, not the set `K_unique`.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site or 3-site `wt1=0`
  ranking in place of this multi-k uniqueness set.
- No list of the k-site seeds, and not a recensus of k=1,2,3.
- No blank-block variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of a maximizer outside
`{4,5,6,7,8}`: on this patch, coverage of the `wt1=0` half has a unique
maximizer exactly at those five seed sizes. The positive set
`K_unique={4, 5, 6, 7, 8}` and the eight census pairs are an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and `wt1=0` | Force vanish-on-empty, vanish-on-full, `f(c)=f(1-c)`, and remaining bit `wt1=0`. | Theorem 1 and check `thm1-f-cut-and-wt1-zero-cardinality` give `|F_cut|=32` and `|F_W0|=16`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-k coverage ranking | Score every map in `F_W0` by `cov_k` for each census k. | Theorem 1 and check `thm1-m-and-n-max-census`. | **ATTEMPTED** |
| uniqueness set | Form `{k ∈ 1..11 : N_max_k=1}` from the census and the three citations. | Theorem 2 and checks `thm2-k-unique-set` / `thm2-cites-without-recensus`. | **ATTEMPTED** |
| unique remaining tuple | Display the remaining-bit tuple at each unique maximizer. | Theorem 3 and check `thm3-unique-remaining-tuple`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of a maximizer fails at
k=1,2,3,9,10,11. The five identities “unique remaining-bit tuple at 4, 5,
6, 7, 8 is `(0, 1, 1, 1, 1)`” are five certificates of the same uniqueness
set, so they collapse rather than count as five walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| unique tuple at k=4 / unique tuple at k=5 | yes: both name `(0, 1, 1, 1, 1)` on `K_unique` | yes: both name the same tuple on `K_unique` | collapse into the uniqueness set |
| static `|F_W0|=16` / `K_unique` | no: membership is not dynamics | no: a uniqueness set does not replace the remaining-bit filter | separate exact counts |
| leftover of #6482 / this set | no: that leftover scored `|S|=2` | no: a multi-k set does not replace the 2-site ranking | different object |
| leftover of #6483 / this set | no: that leftover scored `|S|=3` | no: a multi-k set does not replace the 3-site ranking | different object |
| leftover of one census k / this set | no: that leftover scored one `|S|` | no: a uniqueness set does not replace a single-k ranking | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| remaining bit `wt1=0` | explicit subclass filter; the complementary 16 maps are excluded |
| census seed sizes `{4,5,6,7,8,9,10,11}` | explicit seed class; a single-k ranking is a different residual |
| cited k=1,2,3 | explicit non-recensus; those pairs are inherited, not recomputed |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(0, 1, 1, 1, 1)` | displayed unique maximizer on `K_unique`, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:78` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:122` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:127` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:52` | census seed sizes | `k ∈ {4,5,6,7,8,9,10,11}` | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:53` | cited `N_max` at 1,2,3 | none fill all 12, #6482, #6483; not recomputed | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:63` | `f_L1` remaining bits | `(1, 0, 1, 1, 1)` lies outside `wt1=0` | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:64` | unique remaining tuple | `(0, 1, 1, 1, 1)` | yes |
| `scripts/f_cut_wt1_zero_k_site_uniqueness_2026_08_15.py:314` | `cov_k(f)` | number of k-site seeds a map fills | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in the `wt1=0` half of `F_cut` | the ranking is this subclass on each census seed size; other classes are unclaimed |
| per block | yes: the set `K_unique` | uniqueness holds exactly at `k ∈ {4,5,6,7,8}` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
subclass does have a unique maximizer at five seed sizes, always the same
remaining-bit tuple `(0, 1, 1, 1, 1)`. That positive identity does not
select the tuple as the physical rule. The remaining physical choice —
which, if any, `F_cut` map is the Admissibility occupancy predicate —
stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that #6483 already exhibited a two-element
maximizer class at `|S|=3`, so adjoining later k might be called leftover
decoration of that one ranking, or a seed-table that only scores the
generous remaining-bit tuple `(0, 1, 1, 1, 1)`. That objection is
correctly about the existence of a non-unique maximizer at `|S|=3`. It
does not overturn the stated theorem: among the 16 maps with `wt1=0`, the
set of seed sizes in `1..11` at which coverage has a unique maximizer is
`{4,5,6,7,8}`, and that maximizer is the remaining-bit tuple
`(0, 1, 1, 1, 1)` at each member. That is a new multi-k selector, not
leftover-character of #6482 or #6483, and not leftover of one k.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the `wt1=0` filter, and eight-k 16-map ranking are recomputed
here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `wt1=0` k-site uniqueness set or restores
a unique maximizer at a seed size outside `{4, 5, 6, 7, 8}`.

No-Go Discipline disposition: **PASS** for the uniqueness set
`K_unique={4, 5, 6, 7, 8}` and the exact eight census pairs stated above.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

## Runner Contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
`F_cut`, restricts to the 16 maps with remaining bit `wt1=0`, evaluates
those maps on the two-cube from every k-site seed for each
`k ∈ {4,5,6,7,8,9,10,11}`, reports each `(m_k, N_max_k)`, forms
`K_unique = {4, 5, 6, 7, 8}` by citing that none fill all 12 at k=1 and
#6482/#6483 for k=2,3 without recensing those three, checks that `f_L1`
is not Hamming parity and lies outside the subclass, and displays the
unique remaining-bit tuple `(0, 1, 1, 1, 1)` at each member of
`K_unique`. Declared audit inputs are this note and the axiom memo. No
runner cache is written.
