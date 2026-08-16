---
claim_id: f_cut_max11_extra_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which the four F_cut maps in Max(11) minus Max(1) do not all fill or all miss is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_max11_extra_first_split_2026_08_15.py
---

# First Bounded Seed That Splits The Four `Max(11)` Extra Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of the 32 cube-covariant
complement-even predicates that vanish on empty and full, on the
twelve-vertex two-cube, with off-patch occupancy `0`. The four
`F_cut` maps that attain maximum 11-site coverage and miss maximum
1-site coverage are reconfirmed. The lex-first seed of size at most
3 on which those four fill-bits are not all equal is displayed. No
map is adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_max11_extra_first_split_2026_08_15.py`](../scripts/f_cut_max11_extra_first_split_2026_08_15.py)
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
class. The set `Max(11) \ Max(1)` is leftover-character inventory of two
coverage rankings: #6476 named the set. This note asks a new uniqueness
of the set: on which lex-first seed of size at most 3 the four extras
do not all fill or all miss.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered `k`-set of vertices
is a `k`-site seed. There are `C(12,1)=12` one-site seeds and
`C(12,11)=12` eleven-site seeds. Off-patch neighbors have occupancy `0`.
Each tick, every unlocked on-patch vertex evaluates `f` on its
six-neighbor occupancy tuple and locks if `f=1`. The process is
synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov_k(f) = |{ S : |S|=k and f fills from S }|.
```

`Max(k)` is the set of maps in `F_cut` that attain `m_k = max cov_k`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`.

**Theorem 1.** Exhaustive ranking of the 32 maps gives

```text
m1 = 12
N_max1 = 4
m11 = 12
N_max11 = 8.
```

The four remaining-bit tuples

```text
(0, 0, 1, 1, 0), (0, 0, 1, 1, 1), (0, 1, 1, 1, 0), (0, 1, 1, 1, 1)
```

all lie in `Max(11)` and none lie in `Max(1)`. Each has `cov11=12` and
`cov1=0`. These are exactly the members of `Max(11) \ Max(1)`. The map
`f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and lies in `Max(1)`,
so it is not one of the four extras.

**Theorem 2.** Among all seeds of size at most 3, ordered by increasing
cardinality and then by the lexicographic order of the sorted vertex
tuple, the first seed on which the four fill-bits are not all equal is
the 3-site seed

```text
((0, 0, 0), (0, 1, 1), (2, 0, 0)).
```

No empty, 1-site, or 2-site seed splits the four extras: all 1 + 12 + 66
of those seeds give fill-bits `(0, 0, 0, 0)`.

**Theorem 3.** On that displayed seed the four fill-bits, in the Theorem 1
order, are

```text
(0, 0, 1, 1).
```

So the two extras with `opp2=0` miss and the two extras with `opp2=1`
fill. Displayed, not adopted. Do not write the seed into Admissibility.
Do not adopt a map.

Not leftover-character of #6476 (that named the set). This is a new
uniqueness of the set: the first bounded seed that dynamizes the four
extras into two pairs.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the pair (m1,N_max1)=(12,4), the pair (m11,N_max11)=(12,8), membership of the four named extras in Max(11) minus Max(1), and the lex-first |S|<=3 split seed with fill-bits (0,0,1,1) are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_max11_extra_first_split
target_blocker_text: "whether the four Max(11) minus Max(1) extras are dynamically one object on some |S|<=3 seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the first bounded split of the four extras; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and all seeds of size at most 3; no Z^3-wide law and no physical selector"
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
- the complete set of 12 one-site seeds and 12 eleven-site seeds;
- the complete set of seeds of size at most 3 (`1+12+66+220=299`).

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Reconfirm that the four remaining-bit tuples named above are
exactly `Max(11) \ Max(1)`, and report the lex-first seed of size at
most 3 on which their four fill-bits are not all equal.

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
```

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)`. It is not one of the
four extras. Neither the extras nor `f_L1` is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov_k(f)` is the number of `k`-site seeds whose halt set has
cardinality 12, `m_k` is the maximum of `cov_k` over `F_cut`, and
`Max(k)` is the set of maps attaining `m_k`. The four extras are the
remaining-bit members of `Max(11) \ Max(1)`. The fill-bits of a seed `S`
are the four Booleans that say whether each extra fills from `S`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. Exhaustive
ranking of the 32 maps on all 12 one-site seeds and all 12 eleven-site
seeds gives

```text
m1 = 12
N_max1 = 4
m11 = 12
N_max11 = 8.
```

The four remaining-bit tuples `(0, 0, 1, 1, 0)`, `(0, 0, 1, 1, 1)`,
`(0, 1, 1, 1, 0)`, and `(0, 1, 1, 1, 1)` each have `cov11=12` and
`cov1=0`. They are exactly `Max(11) \ Max(1)`.

**Theorem 2.** Exhaustive search of the 299 seeds of size at most 3, in
lex order by increasing `|S|` and then by the sorted vertex tuple, finds
a first split at

```text
S = ((0, 0, 0), (0, 1, 1), (2, 0, 0)).
```

Every strictly earlier seed in that order, including every seed of size
at most 2, gives identical fill-bits on the four extras.

**Theorem 3.** The four fill-bits on `S` are `(0, 0, 1, 1)`. The extras
are therefore not dynamically one object: two miss and two fill. The
split is exactly the `opp2` bit. Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 12 one-site and 12 eleven-site seeds | `C(12,1)` and `C(12,11)` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `(m1, N_max1)` and `(m11, N_max11)` | exhaustive 32-map ranking of `cov1` and `cov11` |
| four extras in `Max(11) \ Max(1)` | the four named remaining-bit tuples, each with `cov11=12` and `cov1=0` |
| lex-first `|S|≤3` split | seed `((0, 0, 0), (0, 1, 1), (2, 0, 0))` |
| fill-bits on that seed | `(0, 0, 1, 1)` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the fill-bits are a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score only the listing of `Max(11) \ Max(1)`: that leftover is #6476,
   which named the set and did not dynamize it.
5. Restrict the search to `|S|≤2`: every such seed gives fill-bits
   `(0, 0, 0, 0)`, so the four extras remain one miss-class.
6. Assert that the four extras fill or miss together on every `|S|≤3`
   seed: the displayed 3-site seed with fill-bits `(0, 0, 1, 1)` refutes
   that they are dynamically one object.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the #6476 listing of
  `Max(11) \ Max(1)` in place of this first bounded split.
- No adoption of the displayed seed or of either fill-pair.
- No blank-block or 4-site variant.

## No-Go Discipline Gate

The only negative claim is that the four extras are not dynamically one
object on every seed of size at most 3. The positive pair
`(S, fill-bits)=(((0, 0, 0), (0, 1, 1), (2, 0, 0)), (0, 0, 1, 1))` is an
exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `Max(11)` and `Max(1)` reconfirm | Score every `F_cut` map on all 12 one-site and all 12 eleven-site seeds. | Theorem 1 and checks `thm1-max11-contains-four-extras` / `thm1-max1-excludes-four-extras`. | **ATTEMPTED** |
| lex-first `|S|≤3` split | Search all 299 bounded seeds in lex order. | Theorem 2 and checks `thm2-first-split-seed` / `thm2-no-smaller-split`. | **ATTEMPTED** |
| fill-bits on the displayed seed | Evaluate the four extras on `S`. | Theorem 3 and check `thm3-displayed-fill-bits` give `(0, 0, 1, 1)`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the four extras are not dynamically one
object. The displayed seed and the fill-bit tuple are two certificates of
the same split, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| displayed seed / fill-bits `(0, 0, 1, 1)` | yes: a split seed is a split | yes: unequal fill-bits name a split | collapse into the one-object failure |
| `m11=12` / four extras in `Max(11)` | no: a max does not name the extras | no: membership does not replace the max | independent positive integers versus the set |
| leftover of #6476 / this split | no: that leftover named the set | no: a first seed does not replace the listing | different object |
| static `|F_cut|=32` / the split seed | no: membership is not dynamics | no: a seed does not replace the three-cut class | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| seeds of size at most 3 | explicit search bound; a larger seed is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit extras | displayed #6476 set, not a selected law |
| fill-bits `(0, 0, 1, 1)` | displayed witness against one-object dynamics, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:89` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:133` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:138` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:51` | 12 one-site seeds | `C(12,1)` unordered singles on the two-cube | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:54` | 12 eleven-site seeds | `C(12,11)` unordered 11-sets on the two-cube | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:69` | four extras | remaining-bit tuples of `Max(11) \ Max(1)` | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:75` | displayed seed | lex-first `|S|≤3` split | yes |
| `scripts/f_cut_max11_extra_first_split_2026_08_15.py:326` | first-split search | increasing `|S|` then lex of the sorted tuple | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | `cov1` and `cov11` are this class; other classes are unclaimed |
| per block | yes: the four extras and one seed | the extras split on `S`; they are not dynamically one object |
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
four extras do share `cov11=12` and `cov1=0`, and they do miss together
on every seed of size at most 2. That common miss-class does not make
them dynamically one object on every `|S|≤3` seed and does not select
any of them as the physical rule. The remaining physical choice — which,
if any, `F_cut` map is the Admissibility occupancy predicate — stays
explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that #6476 already named the four extras, so
a first split seed might be called leftover decoration of that listing,
or of the fact that the four tuples differ already on `opp2` and
`mixed3`. That objection is correctly about the static bit-tuples. It
does not overturn the stated theorem: among all seeds of size at most 3,
the four extras first disagree dynamically on the displayed 3-site seed,
with fill-bits `(0, 0, 1, 1)`. The split is a dynamics fact, not a
leftover of listing the set.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the two coverage rankings, and the 299-seed search are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first bounded split of the four extras
or restores the claim that they are dynamically one object on every
seed of size at most 3.

No-Go Discipline disposition: **PASS** for the one-object failure and the
exact pair `(S, fill-bits)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 1-site seed and
every 11-site seed, reports `m1 = 12`, `N_max1 = 4`, `m11 = 12`, and
`N_max11 = 8`, reconfirms that the four named extras are exactly
`Max(11) \ Max(1)`, searches all seeds of size at most 3 in lex order,
reports the first split seed `((0, 0, 0), (0, 1, 1), (2, 0, 0))` with
fill-bits `(0, 0, 1, 1)`, checks that `f_L1` is not Hamming parity, and
does not adopt a map. Declared audit inputs are this note and the axiom
memo. No runner cache is written.
