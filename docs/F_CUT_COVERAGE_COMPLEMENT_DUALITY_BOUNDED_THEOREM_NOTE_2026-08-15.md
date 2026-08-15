---
claim_id: f_cut_coverage_complement_duality_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the set of coverage maximizers at seed size k is not equal to the set at seed size 12-k for k=1,2,3 and is equal for k=4,5. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_coverage_complement_duality_2026_08_15.py
---

# `F_cut` Coverage Maximizer Sets At `k` And `12-k`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact set comparison of `F_cut` coverage maximizers on the
twelve-vertex two-cube with off-patch occupancy `0`. For each seed size
`k=1..5`, the set `Max(k)` of remaining-bit tuples attaining `cov_k=m_k`
is compared with `Max(12-k)`. The five equality bits are displayed. No
complement duality is adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_coverage_complement_duality_2026_08_15.py`](../scripts/f_cut_coverage_complement_duality_2026_08_15.py)
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

On the two-cube `{0,1,2}×{0,1}×{0,1}` there are `C(12,k)` unordered
`k`-site seeds. Off-patch neighbors have occupancy `0`. Each tick, every
unlocked on-patch vertex evaluates `f` on its six-neighbor occupancy
tuple and locks if `f=1`. The process is synchronous and stops at a fixed
point in at most 12 ticks. Fill means `|locks_halt|=12`. Coverage at seed
size `k` is

```text
cov_k(f) = |{ S : |S|=k and f fills from S }|.
```

Write `m_k = max cov_k` over `F_cut` and `N_max_k` for the number of
maps attaining `m_k`. The set `Max(k)` is the set of remaining-bit
tuples with `cov_k = m_k`. The five remaining bits, in the displayed
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full
are forced to `0`.

Claim #6465 reported the pairs `(m_k, N_max_k)`. Those counts have
palindromic `m_k` under `k ↔ 12-k` (1↔11, 2↔10, 3↔9, 5↔7, 4↔8):
`m_k = C(12,k) = m_{12-k}`. The `N_max_k` column is not palindromic at
`k=1,2,3`. Not leftover-character of #6465: that only reported
`(m_k, N_max_k)`. This note is not a recensus of those integers. The
new object is whether `Max(k)=Max(12-k)` as remaining-bit-tuple sets.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
The all-ones remaining-bit tuple is `(1, 1, 1, 1, 1)`.

**Theorem 1.** Exhaustive recomputation of `cov_k` on all 32 maps and
all `C(12,k)` seeds, for each `k=1..11`, reconfirms the #6465 pairs and
names the maximizer sets. For `k=1..5`,

```text
Max(1)  ≠ Max(11)
Max(2)  ≠ Max(10)
Max(3)  ≠ Max(9)
Max(4)  = Max(8)
Max(5)  = Max(7)
```

as sets of remaining-bit tuples. Explicitly,

```text
Max(1)  = {(1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)}
Max(11) = {(0, 0, 1, 1, 0), (0, 0, 1, 1, 1), (0, 1, 1, 1, 0), (0, 1, 1, 1, 1),
           (1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)}
Max(2)  = {(1, 1, 1, 1, 0), (1, 1, 1, 1, 1)}
Max(10) = {(0, 0, 1, 1, 1), (0, 1, 1, 1, 1), (1, 0, 1, 1, 1), (1, 1, 1, 1, 1)}
Max(3)  = {(1, 0, 1, 1, 1), (1, 1, 1, 1, 1)}
Max(9)  = {(0, 0, 1, 1, 1), (0, 1, 1, 1, 1), (1, 0, 1, 1, 1), (1, 1, 1, 1, 1)}
Max(4)  = Max(8) = {(1, 1, 1, 1, 1)}
Max(5)  = Max(7) = {(1, 0, 1, 1, 1), (1, 1, 1, 1, 1)}
```

Cited #6465 pairs, recomputed:

```text
k=1  (m_1, N_max_1)   = (12, 4)
k=2  (m_2, N_max_2)   = (66, 2)
k=3  (m_3, N_max_3)   = (220, 2)
k=4  (m_4, N_max_4)   = (495, 1)
k=5  (m_5, N_max_5)   = (792, 2)
k=7  (m_7, N_max_7)   = (792, 2)
k=8  (m_8, N_max_8)   = (495, 1)
k=9  (m_9, N_max_9)   = (220, 4)
k=10 (m_10, N_max_10) = (66, 4)
k=11 (m_11, N_max_11) = (12, 8)
```

In particular `m_1 = 12` and `N_max_1 = 4`.

**Theorem 2.** The equality 5-tuple, with entry `k` equal to `1` iff
`Max(k)=Max(12-k)` for `k=1..5`, is

```text
E = (0, 0, 0, 1, 1)
```

**Theorem 3.** Display `E`. Do not adopt a duality. Do not write the duality into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the cited #6465 (m_k, N_max_k) pairs, the named Max(k) remaining-bit sets, and the equality 5-tuple E=(0,0,0,1,1) are enumerated. The bits are displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_coverage_complement_duality
target_blocker_text: "whether Max(k) equals Max(12-k) as remaining-bit-tuple sets is unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed equality 5-tuple; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut maximizer sets on this twelve-vertex patch with off-patch o=0 and all k-site seeds; no Z^3-wide law and no physical selector"
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
- the complete family of `C(12,k)` unordered `k`-site seeds for
  `k=1..11`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6465 (that only reported `(m_k, N_max_k)`).
The pairs are cited and recomputed only so the attaining remaining-bit
sets can be compared. This is not a recensus.

## Exact Target And Objects

**Target.** Cite the #6465 pairs `(m_k, N_max_k)`, recompute the
maximizer sets `Max(k)`, and name whether `Max(k)=Max(12-k)` for each
`k=1..5`.

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

so `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)`. Neither `f_L1` nor
any other remaining-bit tuple is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

Then `cov_k(f)` is the number of `k`-site seeds whose halt set has
cardinality 12, `m_k` is the maximum of `cov_k` over `F_cut`, and
`N_max_k` is the number of maps attaining `m_k`. The maximizer set
`Max(k)` is the set of remaining-bit tuples with `cov_k=m_k`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut`. It is not Hamming parity. On the
twelve-vertex two-cube with off-patch occupancy `0`, exhaustive ranking of
all 32 maps on all `C(12,k)` seeds reconfirms the #6465 pairs
`(m_k, N_max_k)` listed above and names `Max(k)` for each complementary
pair. Among `k=1..5`, set equality `Max(k)=Max(12-k)` holds only at
`k=4` and `k=5`.

**Theorem 2.** The equality 5-tuple is

```text
E = (0, 0, 0, 1, 1).
```

**Theorem 3.** Display `E`. Do not adopt a duality. Do not write the duality into Admissibility. The bits are a displayed comparison, not a selected
occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| `C(12,k)` k-site seeds | unordered `k`-subsets of the twelve vertices |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| cited #6465 pairs | `(m_k, N_max_k)` as listed; recomputed, then used only to name the attaining sets |
| `Max(k)` versus `Max(12-k)` | remaining-bit-tuple sets compared for each `k=1..5` |
| equality 5-tuple | `E = (0, 0, 0, 1, 1)` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not used as a
   maximizer label.
2. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
4. Report only `(m_k, N_max_k)`: that leftover is the #6465 count table,
   not the named maximizer sets.
5. Score only one seed size: that one-`k` leftover is a ranking, not the
   complementary-set comparison.
6. Adopt `E` as a physical duality: the note displays the bits and writes
   no duality into Admissibility.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the #6465 pairs
  `(m_k, N_max_k)` in place of the named set comparison.
- No adopted complement duality on seed size.

## No-Go Discipline Gate

The only negative claim is that `Max(k)` is not identically
`Max(12-k)` for every `k=1..5`. The equality 5-tuple is an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| cite #6465 pairs | Recompute `(m_k, N_max_k)` against the cited complementary pairs. | Theorem 1 and check `thm1-cite-6465-pairs`. | **ATTEMPTED** |
| recompute maximizer sets | Name `Max(k)` and compare with `Max(12-k)` for `k=1..5`. | Theorem 1, Theorem 2, and checks `thm1-set-equality-bits` / `thm2-equality-5-tuple`. | **ATTEMPTED** |
| display, do not adopt | Ask whether `E` is written into Admissibility as a duality. | Theorem 3 and check `thm3-display-not-adopt-duality`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: set equality fails at `k=1,2,3`. The
cardinality mismatch `N_max_k ≠ N_max_{12-k}` at those `k` and the
named set comparison are two certificates of the same failure, so they
collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_max_1=4` / `N_max_11=8` | yes: unequal counts imply unequal sets | no: unequal sets need not have unequal counts | count mismatch is a certificate of set mismatch at `k=1` |
| set mismatch at `k=1` / set mismatch at `k=2` | no | no | independent seed sizes |
| static `|F_cut|=32` / equality 5-tuple | no: membership is not dynamics | no: comparing maximizer sets does not replace the three-cut class | separate exact counts |
| leftover of #6465 / this set comparison | no: that leftover reported only `(m_k, N_max_k)` | no: naming `E` does not replace the count residual | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| all `C(12,k)` k-site seeds | explicit seed class; a one-seed fill is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| equality 5-tuple `E = (0, 0, 0, 1, 1)` | displayed comparison, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:86` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:130` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:135` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:48` | twelve two-cube vertices | `{0,1,2}×{0,1}×{0,1}` | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:275` | `cov_k(f)` | number of `k`-site seeds a map fills | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:62` | cited #6465 pairs | `(m_k, N_max_k)` used only to name attaining sets | yes |
| `scripts/f_cut_coverage_complement_duality_2026_08_15.py:74` | equality 5-tuple | displayed `E = (0, 0, 0, 1, 1)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | `Max(k)` is named inside this class on all `C(12,k)` seeds |
| per block | yes: the equality 5-tuple | `Max(k)=Max(12-k)` fails at `k=1,2,3` and holds at `k=4,5` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: at
`k=4` and `k=5` the maximizer sets do coincide, and at every complementary
pair the *coverage* maximum `m_k` is palindromic. Those positive
agreements do not make `Max(k)=Max(12-k)` a theorem for every `k=1..5`
and do not select a physical duality. The remaining physical choice —
which, if any, `F_cut` map is the Admissibility occupancy predicate —
stays explicit.

### N7 — hostile steelman

The strongest objection is that because `m_k=m_{12-k}` the maximizer
sets might be called leftover-character of the #6465 count table, or
that unequal `N_max` at `k=1,2,3` already answers the set question
without naming tuples. That objection is correctly about the count
pairs. It does not overturn the stated theorem: #6465 stopped at
`(m_k, N_max_k)`; the set residual is whether the attaining remaining-bit
tuples coincide. Displaying `E = (0, 0, 0, 1, 1)` names that comparison.
No duality is adopted.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the 32-map `k`-site rankings, and the equality 5-tuple are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the named set comparison or writes a
complement duality into Admissibility.

No-Go Discipline disposition: **PASS** for the named equality 5-tuple
and the recomputed #6465 pairs `(m_k, N_max_k)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every `k`-site seed
for `k=1..11`, reconfirms the cited #6465 pairs `(m_k, N_max_k)`, names
`Max(k)` by remaining-bit tuple, reports `E = (0, 0, 0, 1, 1)`, checks
that `f_L1` is not Hamming parity, and does not adopt a duality.
Declared audit inputs are this note and the axiom memo.
No runner cache is written.
