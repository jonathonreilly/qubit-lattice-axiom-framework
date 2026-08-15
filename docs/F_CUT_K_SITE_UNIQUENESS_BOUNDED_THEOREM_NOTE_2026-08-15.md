---
claim_id: f_cut_k_site_uniqueness_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the seed sizes k in {1,5,6,7,8,9,10,11} at which coverage has a unique maximizer are reported, and that maximizer is named as f_L1 or f1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k_site_uniqueness_2026_08_15.py
---

# For Which Seed Sizes Is `F_cut` Coverage Unique

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage uniqueness set of the 32
cube-covariant complement-even predicates that vanish on empty and full, on
the twelve-vertex two-cube, over all k-site seeds for each
`k ∈ {1,5,6,7,8,9,10,11}`, with off-patch occupancy `0`. Seed sizes 2, 3,
and 4 are cited from #6429, #6453, and #6460 and are not re-censused. The
unbalanced-axis map `f_L1` and the remaining-bit tuple `f1=(1,1,1,1,1)` are
displayed as named members. Neither is adopted as the physical
Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k_site_uniqueness_2026_08_15.py`](../scripts/f_cut_k_site_uniqueness_2026_08_15.py)
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

That static cardinality is leftover-character inventory of the three-cut
class. A single-k coverage ranking of the same 32 maps is also leftover
inventory of one seed cardinality. New selector, not leftover of one k.
This note asks the new ranking object: among all 32 maps, for each census
seed size, how many k-site seeds does each fill, at which k is the
maximizer unique, and is that unique maximizer `f_L1` or `f1`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered k-set of vertices is
a k-site seed. Off-patch neighbors have occupancy `0`. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy tuple
and locks if `f=1`. The process is synchronous and stops at a fixed point
in at most 12 ticks. Fill means `|locks_halt|=12`. Coverage is

```text
cov_k(f) = |{ S : |S|=k and f fills from S }|.
```

Do not list the seeds. Do not re-census k=2,3,4.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`.
The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

**Theorem 1.** Exhaustive ranking of the 32 maps on every k-site seed for
each census size gives

```text
m_1 = 12
N_max_1 = 4
m_5 = 792
N_max_5 = 2
m_6 = 924
N_max_6 = 1
m_7 = 792
N_max_7 = 2
m_8 = 495
N_max_8 = 1
m_9 = 220
N_max_9 = 4
m_10 = 66
N_max_10 = 4
m_11 = 12
N_max_11 = 8.
```

**Theorem 2.** Write `K_unique = {k ∈ 1..11 : N_max_k = 1}`. Citing #6429
(`N_max_2 = 2`), #6453 (`N_max_3 = 2`), and #6460 (`N_max_4 = 1` is `f1`)
without recomputing those three as the claim,

```text
K_unique = {4, 6, 8}.
```

**Theorem 3.** For each `k ∈ K_unique` the unique maximizer is `f1`, not
`f_L1`. At the two newly ranked members, `cov_6(f1)=924=m_6` while
`cov_6(f_L1)=920`, and `cov_8(f1)=495=m_8` while `cov_8(f_L1)=494`. The
k=4 member is the cited #6460 identity. Displayed, not adopted.

Do not write the ranking into Admissibility.

Not leftover-character of #6429 (that was the 2-site ranking; different |S|).
Not leftover-character of #6453 (that was the 3-site ranking; different |S|).
Not leftover-character of #6460 (that was the 4-site ranking; different |S|;
one of the three members of `K_unique`, not the uniqueness set). New
selector, not leftover of one k.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f_L1 and f1, the eight census pairs (m_k,N_max_k), the cited N_max values at k=2,3,4, the uniqueness set K_unique={4,6,8}, and the name f1 of each unique maximizer are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_k_site_uniqueness
target_blocker_text: "for which seed sizes other than 2, 3, 4 does F_cut coverage select one map, and is that map f_L1 or f1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut k-site uniqueness set; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and the eight census seed sizes, citing #6429/#6453/#6460 for k=2,3,4; no Z^3-wide law and no physical selector"
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
- the cited ranking pairs `N_max_2=2` (#6429), `N_max_3=2` (#6453), and
  `N_max_4=1` with unique maximizer `f1` (#6460).

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Rank the 32 members of `F_cut` by k-site fill coverage on the
two-cube for each `k ∈ {1,5,6,7,8,9,10,11}`, form
`K_unique = {k ∈ 1..11 : N_max_k = 1}` by adjoining the cited values at
k=2,3,4, and name each unique maximizer as `f_L1` or `f1`.

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
`(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f_L1(c)     = 1  iff  u(c) ≥ 1,
f1(c)       = 1  iff  c is neither empty nor full,
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and `f1` has
remaining-bit tuple `(1, 1, 1, 1, 1)`. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov_k(f)` is the number of k-site seeds whose halt set has
cardinality 12, `m_k` is the maximum of `cov_k` over `F_cut`, and
`N_max_k` is the number of maps attaining `m_k`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. The map
`f1` is the complementary remaining-bit tuple with `opp2` on. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive ranking of
all 32 maps on every census seed size gives the eight pairs

```text
(m_1, N_max_1) = (12, 4)
(m_5, N_max_5) = (792, 2)
(m_6, N_max_6) = (924, 1)
(m_7, N_max_7) = (792, 2)
(m_8, N_max_8) = (495, 1)
(m_9, N_max_9) = (220, 4)
(m_10, N_max_10) = (66, 4)
(m_11, N_max_11) = (12, 8).
```

**Theorem 2.** The uniqueness set, using the cited values `N_max_2=2`
(#6429), `N_max_3=2` (#6453), and `N_max_4=1` (#6460) and the eight
computed `N_max_k`, is

```text
K_unique = {4, 6, 8}.
```

Those three cited cardinalities are not recomputed here.

**Theorem 3.** For each `k ∈ K_unique` the unique maximizer is `f1`, not
`f_L1`. At k=6 the unique remaining-bit tuple is `(1, 1, 1, 1, 1)` with
`cov_6=924`. At k=8 the unique remaining-bit tuple is again
`(1, 1, 1, 1, 1)` with `cov_8=495`. The k=4 member is the cited #6460
identity that `N_max_4=1` is `f1`. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f1` is in `F_cut` | vanish on empty and full, and complement-even on every remaining orbit |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| eight census seed counts | `C(12,k)` for `k ∈ {1,5,6,7,8,9,10,11}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| eight pairs `(m_k, N_max_k)` | exhaustive 32-map ranking of `cov_k` on each census size |
| cited `N_max_2,N_max_3,N_max_4` | #6429, #6453, #6460; not recomputed |
| `K_unique={4,6,8}` | `{k ∈ 1..11 : N_max_k=1}` |
| unique maximizer name | `f1` at each of 4, 6, 8; not `f_L1` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the uniqueness set is a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score only 2-site seeds: that leftover is #6429, a different `|S|`.
5. Score only 3-site seeds: that leftover is #6453, a different `|S|`.
6. Score only 4-site seeds: that leftover is #6460, a different `|S|`.
7. Assert that `f_L1` is the unique maximizer at some `k ∈ K_unique`: at
   each such k the unique maximizer is `f1`.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site, 3-site, or 4-site
  `F_cut` ranking in place of this multi-k uniqueness set.
- No list of the k-site seeds, and not a recensus of k=2,3,4.
- No blank-block variant.

## No-Go Discipline Gate

The only negative claim is uniqueness of `f_L1` as the unique-k maximizer:
on this patch, whenever coverage has a unique maximizer in `1..11`, that
map is `f1`, not `f_L1`. The positive set `K_unique={4,6,8}` and the eight
census pairs are an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| eight-k coverage ranking | Score every map in `F_cut` by `cov_k` for each census k. | Theorem 1 and check `thm1-m-and-n-max-census`. | **ATTEMPTED** |
| uniqueness set | Form `{k ∈ 1..11 : N_max_k=1}` from the census and the three citations. | Theorem 2 and checks `thm2-k-unique-set` / `thm2-cites-without-recensus`. | **ATTEMPTED** |
| unique maximizer name | Ask whether each unique maximizer is `f_L1` or `f1`. | Theorem 3 and check `thm3-unique-maximizers-are-f1`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of `f_L1` as the unique-k
maximizer fails. The three identities “unique maximizer at 4, 6, 8 is
`f1`” are three certificates of the same non-uniqueness of `f_L1` on
`K_unique`, so they collapse rather than count as three walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| unique maximizer is `f1` at k=6 / `cov_6(f_L1)=920` | yes: the unique maximizer is not `f_L1` | yes: a strictly smaller score is non-uniqueness of `f_L1` | collapse into the uniqueness failure |
| unique maximizer is `f1` at k=8 / unique maximizer is `f1` at k=6 | yes: both name `f1` on `K_unique` | yes: both name `f1` on `K_unique` | collapse into the uniqueness failure |
| static `|F_cut|=32` / `K_unique` | no: membership is not dynamics | no: a uniqueness set does not replace the three-cut class | separate exact counts |
| leftover of #6429 / this set | no: that leftover scored `|S|=2` | no: a multi-k set does not replace the 2-site ranking | different object |
| leftover of #6453 / this set | no: that leftover scored `|S|=3` | no: a multi-k set does not replace the 3-site ranking | different object |
| leftover of #6460 / this set | no: that leftover scored `|S|=4` | no: a uniqueness set does not replace the 4-site ranking | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| census seed sizes `{1,5,6,7,8,9,10,11}` | explicit seed class; a single-k ranking is a different residual |
| cited k=2,3,4 | explicit non-recensus; those pairs are inherited, not recomputed |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit tuple `(1, 1, 1, 1, 1)` | displayed unique maximizer on `K_unique`, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:77` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:121` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:126` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:130` | `f1` definition | remaining bits `(1, 1, 1, 1, 1)` | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:51` | census seed sizes | `k ∈ {1,5,6,7,8,9,10,11}` | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:52` | cited `N_max` at 2,3,4 | #6429, #6453, #6460; not recomputed | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:321` | `cov_k(f)` | number of k-site seeds a map fills | yes |
| `scripts/f_cut_k_site_uniqueness_2026_08_15.py:329` | unique maximizer name | `f1` or `f_L1` from remaining bits | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the ranking is this class on each census seed size; other classes are unclaimed |
| per block | yes: the set `K_unique` | uniqueness of `f_L1` fails because each unique maximizer is `f1` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F_cut` and does attain the coverage maximum at several
non-unique seed sizes. That positive member does not make `f_L1` a unique
maximizer at any `k ∈ 1..11` and does not select it as the physical rule.
The remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that `f1` was already the unique 4-site
maximizer (#6460), so adjoining k=6 and k=8 might be called leftover
decoration of that one k, or a seed-table that only scores `f_L1` against
`f1`. That objection is correctly about the existence of a unique
maximizer at `|S|=4`. It does not overturn the stated theorem: among all
32 maps in `F_cut`, the set of seed sizes in `1..11` at which coverage
has a unique maximizer is `{4,6,8}`, and that maximizer is `f1` at each
member. That is a new multi-k selector, not leftover-character of #6429,
#6453, or #6460, and not leftover of one k.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, and eight-k 32-map ranking are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` k-site uniqueness set or restores
uniqueness of `f_L1` as a maximizer inside the 32-map class.

No-Go Discipline disposition: **PASS** for the uniqueness failure of
`f_L1` on `K_unique` and the exact set `{4, 6, 8}` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every k-site seed for
each `k ∈ {1,5,6,7,8,9,10,11}`, reports each `(m_k, N_max_k)`, forms
`K_unique = {4, 6, 8}` by citing #6429/#6453/#6460 for k=2,3,4 without
recensing those three, checks that `f_L1` is not Hamming parity, and
names the unique maximizer at each member of `K_unique` as `f1`.
Declared audit inputs are this note and the axiom memo. No runner cache
is written.
