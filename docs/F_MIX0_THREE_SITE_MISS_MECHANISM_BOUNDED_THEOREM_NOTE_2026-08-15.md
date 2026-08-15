---
claim_id: f_mix0_three_site_miss_mechanism_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first neighborhood at which F_cut (1,0,1,1,0) refuses and (1,1,1,1,1) fires, on the lex-first 3-site seed f_mix0 does not fill, is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py
---

# First Refused Neighborhood On The Lex-First Three-Site Miss Of `f_mix0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** independent occupancy-to-lock runs from the lexicographically
first unordered 3-site seed that `f_mix0` does not fill, on the
twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}` with off-patch occupancy
`0`. The `F_cut` map `f1` with remaining-bit tuple `(1, 1, 1, 1, 1)`
fills that seed. The first neighborhood at which `f_mix0=0` and `f1=1`
is reported by tick, site, and axis type. That type is not mixed3.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py`](../scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut| = 32`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered triple of vertices
is a 3-site seed. There are `C(12,3)=220` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Three-site coverage is

```text
cov3(f) = |{ S : |S|=3 and f fills from S }|.
```

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`.

Write `f_mix0` for the `F_cut` map with remaining-bit tuple
`(1, 0, 1, 1, 0)` and `f1` for the `F_cut` map with remaining-bit tuple
`(1, 1, 1, 1, 1)`. They differ on `opp2` and on `mixed3` (and on the
complements of those two types). Neither map is adopted.

New mechanism. New object. Not leftover of #6459: that note reported
only `cov3(f_mix0)=188`. Not leftover of #6461 or #6456: those were
`f0=(1,1,1,1,0)` and its eight 3-site misses. Not leftover of mix0c3geo
(`do_not_land`): that residual asked for the miss-orbit count of the
thirty-two unfilled seeds. This residual names the first refused
neighborhood on the lex-first miss.

**Theorem 1.** Independent recomputation of every 3-site seed reconfirms
`cov3(f_mix0)=188` and `cov3(f1)=220`. The lex-first 3-site miss is

```text
S = {(0,0,0),(0,0,1),(2,0,0)}
```

On that seed, `f_mix0` does not fill: lock-count history `(3, 8, 10)`.
`f1` fills: history `(3, 9, 12)`.

**Theorem 2.** On that lex-first miss, the first neighborhood at which
`f_mix0` refuses and `f1` fires is

```text
t = 1
x = (1, 0, 0)
axis type = opp2 = (0, 1, 2)
```

The six-neighbor occupancy is `(1, 1, 0, 0, 0, 0)`: both ends of the
long `x` axis are occupied and the other two axes are empty. That is a
filled axis. An extra `f_mix0` refuses. The same first event is seen on
the independent `f_mix0` run and on the independent `f1` run.

**Theorem 3.** That first axis type is not mixed3. mixed3 is `(1, 1, 1)`
and does not appear as the first refusal. Display. Do not adopt mixed3.
Do not write it into Admissibility. The thirty-two missed seeds are not
listed.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first 3-site miss of f_mix0, the independent f1 fill, and the first refused neighborhood (tick, site, axis type) are enumerated. The first type is not mixed3. mixed3 is displayed, not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: f_mix0_three_site_miss_mechanism
target_blocker_text: "why mix0 is not a 3-site maximizer; the first neighborhood at which f_mix0 refuses and f1 fires, on the lex-first 3-site miss, remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first refused neighborhood; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f_mix0 and f1 on this twelve-vertex patch with off-patch o=0 and the lex-first 3-site miss; no Z^3-wide law and no physical selector"
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
laws. Admissibility does not supply the formation site, probability, or rate.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the 24 proper signed-permutation rotations of the three axes
  (`det = +1`);
- occupancy 6-tuples on the ordered neighbor stencil
  `(+x,-x,+y,-y,+z,-z)`;
- the two-cube vertex set `{0,1,2}×{0,1}×{0,1}`;
- the off-patch occupancy default `0`;
- the complete set of 220 unordered 3-site seeds;
- independent lock-step runs of `f_mix0` and of `f1` from the lex-first miss.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** Reconfirm `cov3(f_mix0)=188` and that `f1` fills the
lex-first 3-site miss by an independent run, then name the first
`(tick, site, axis type)` at which `f_mix0` refuses and `f1` fires, and
state whether that type is mixed3.

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
`f(c)=f(1-c)`. The remaining-bit tuple is those five free bits in the
order `(wt1, opp2, adj2, vertex3, mixed3)`.

Define

```text
f_mix0(c) = remaining-value of (1, 0, 1, 1, 0),
f1(c)     = remaining-value of (1, 1, 1, 1, 1),
f_L1(c)   = 1  iff  u(c) ≥ 1.
```

So `f_mix0` has remaining-bit tuple `(1, 0, 1, 1, 0)` and `f1` has
`(1, 1, 1, 1, 1)`. They differ on `opp2` and on `mixed3`. Neither map
is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

An independent run of `f` from a seed is that iteration started at the
seed and continued to a fixed point. A miss is a 3-site seed whose
`f_mix0` halt set has cardinality strictly less than 12. The lex-first
miss is the lexicographically first such seed in sorted-site order.
The first refused neighborhood on a run is the lexicographically first
unlocked site, at the earliest tick, whose neighborhood has `f_mix0=0`
and `f1=1`. Tick `t = 1` is the first evaluation on the seed occupancy.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The unbalanced-axis map `f_L1` is one element of
`F_cut`. It is not Hamming parity. On the twelve-vertex two-cube with
off-patch occupancy `0`, exhaustive fill census of all 220 three-site
seeds reconfirms `cov3(f_mix0)=188` and `cov3(f1)=220`. The lex-first
miss is the seed named above. Independent runs give lock-count histories
`(3, 8, 10)` for `f_mix0` (unfilled) and `(3, 9, 12)` for `f1` (filled).

**Theorem 2.** On that lex-first miss, the first neighborhood with
`f_mix0(nbhd)=0` and `f1(nbhd)=1` is tick `t = 1`, site `(1, 0, 0)`,
axis type `opp2` `= (0, 1, 2)`. Coverage maximizers that fire `opp2`
form on that filled axis; an extra `f_mix0` refuses.

**Theorem 3.** That first axis type is not mixed3. Display. Do not adopt
mixed3. Do not write it into Admissibility. The first refused
neighborhood is a displayed census output, not a selected occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| `cov3(f_mix0)=188` | exhaustive 220-seed fill census |
| `f1` fills the lex-first miss | independent run fills with history `(3, 9, 12)` |
| `f_mix0` misses that seed | independent run halt history `(3, 8, 10)` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 220 three-site seeds | `C(12,3)` unordered triples |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| first refused neighborhood | `t = 1`, site `(1, 0, 0)`, axis type `opp2` |
| first type is not mixed3 | the first refusal is `opp2`, not `(1, 1, 1)` |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not this
   miss-seed residual.
2. Replace off-patch occupancy `0` by a blank-block: first-wave
   candidates become undefined; that is a different census.
3. Compare `f_mix0` only to `f_L1` on this seed: that leftover of
   #6437 names a later `mixed3` split; the first `f_mix0=0` and
   `f1=1` event is `opp2` at tick 1.
4. Report only `cov3(f_mix0)=188`: that leftover of #6459 names the
   miss count, not the first refused neighborhood.
5. Adopt `mixed3` as the physical rule: the note displays that the
   first type is not mixed3 and writes nothing into Admissibility.
6. Score only the `f1` run: the theorem requires independent runs of
   both maps from the lex-first miss.
7. Report the miss-orbit count of the thirty-two unfilled seeds: that
   is mix0c3geo (`do_not_land`), not this mechanism.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover restatement of the #6459 coverage count.
- No leftover restatement of the #6461/#6456 `f0` eight-miss residual.
- No miss-orbit count and no thirty-two-row seed list.
- No adoption of mixed3.
- No blank-block or 2-site-only variant.

## No-Go Discipline Gate

The only negative claim is that `f_mix0` refuses a filled-axis
neighborhood that `f1` fires, on the lex-first 3-site miss. The
first refused neighborhood is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| cov3 reconfirm | Score every 3-site seed under `f_mix0` and under `f1`. | Theorem 1 and check `thm1-cov3-reconfirm`. | **ATTEMPTED** |
| lex-first fill split | Confirm `f1` fills `S` and `f_mix0` does not. | Theorem 1 and check `thm1-lex-first-fill-split`. | **ATTEMPTED** |
| lex-first refusal | Name the first `(t, x, axis type)` on `S`. | Theorem 2 and check `thm2-lex-first-refusal`. | **ATTEMPTED** |
| display, do not adopt | Ask whether mixed3 is the first type and whether it is written into Admissibility. | Theorem 3 and checks `thm3-type-is-not-mixed3` / `thm3-display-not-adopt-mixed3`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `f_mix0` refuses `opp2` on this
lex-first miss while `f1` fires it. Naming the first refused
neighborhood and stating that the type is not mixed3 are two
certificates of the same filled-axis refusal, so they collapse rather
than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| cov3=188 / lex-first miss | no: a count does not name a seed | no: one seed does not give the count | independent exact objects |
| lex-first `(t,x,type)` / not mixed3 | yes: the type is `opp2` | no: “not mixed3” does not name the site | collapse into the refused-axis type |
| leftover of #6459 / this first refusal | no: that leftover is the miss count | no: a neighborhood does not replace that count | different object |
| leftover of #6461/#6456 / this first refusal | no: those leftovers are `f0` | no: a `f_mix0` neighborhood does not replace `f0` | different object |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| lex-first 3-site miss | explicit seed; a 2-site leftover is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| first axis type `opp2` | displayed mechanism, not a selected law |
| mixed3 | displayed as not the first type, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:94` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:138` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:143` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:157` | `f_mix0` definition | remaining-bit tuple `(1, 0, 1, 1, 0)` | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:162` | `f1` definition | remaining-bit tuple `(1, 1, 1, 1, 1)` | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:55` | 220 three-site seeds | `C(12,3)` unordered triples on the two-cube | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:217` | independent runs | lock-step evolution from the lex-first miss | yes |
| `scripts/f_mix0_three_site_miss_mechanism_2026_08_15.py:279` | first refused neighborhood | earliest `(tick, site, axis type)` with `f_mix0=0` and `f1=1` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f_mix0` and `f1` from the lex-first miss | independent runs; `f1` fills; `f_mix0` misses |
| per block | yes: the first refused neighborhood | tick, site, and axis type; that type is not mixed3 |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_mix0`
does lie in `F_cut` and does fill 188 of the 220 three-site seeds. That
positive member does not make `f_mix0` a maximizer and does not write
mixed3 into Admissibility. The remaining physical choice — which, if any,
`F_cut` map is the Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f_mix0` is already known to miss
thirty-two 3-site seeds because its remaining bits `opp2` and `mixed3`
are `0`, so naming the first refused neighborhood might be called
leftover-character of the coverage ranking. That objection is correctly
about the miss count and the remaining-bit tuple. It does not overturn
the stated theorem: the new object is the first `(tick, site, axis type)`
on the lex-first miss, together with the statement that the type is not
mixed3. Displaying `opp2` names that mechanism. mixed3 is not adopted.

A second steelman is that this is leftover of #6437, the `f_mix0`
versus `f_L1` split on the same seed. That leftover lives at a later
tick and is a `mixed3` neighborhood. The first `f_mix0=0` and `f1=1`
event is `opp2` at tick 1, because `f1` fires the filled axis that both
`f_mix0` and `f_L1` refuse. Different object.

A third steelman is that this is leftover of mix0c3geo. That residual
asks for the miss-orbit count of the thirty-two seeds. This note does
not report that count and does not list those seeds (`do_not_land`).

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f_mix0`, `f1`, `cov3=188`, and the first refused neighborhood are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first refused neighborhood or writes
mixed3 into Admissibility.

No-Go Discipline disposition: **PASS** for the cov3 reconfirm, the
independent `f1` fill, and the displayed first refused neighborhood
stated above.

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

The companion runner reconstructs the 24 rotations and 10 orbits, evaluates
`f_mix0` and `f1` independently from every 3-site seed, reconfirms
`cov3(f_mix0)=188` and that `f1` fills the lex-first miss, names the first
refused neighborhood by tick, site, and axis type, checks that the type
is not mixed3, checks that `f_L1` is not Hamming parity, and does not
adopt mixed3. Declared audit inputs are this note and the axiom memo.
No runner cache is written.
