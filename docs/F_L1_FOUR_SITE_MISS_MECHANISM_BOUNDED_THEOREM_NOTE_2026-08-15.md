---
claim_id: f_l1_four_site_miss_mechanism_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first neighborhood at which f_L1 refuses and f1 fires, on the lex-first 4-site seed f_L1 does not fill, is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_l1_four_site_miss_mechanism_2026_08_15.py
---

# First Refused Neighborhood On The Six `f_L1` Four-Site Miss Seeds

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** independent occupancy-to-lock runs from each of the six
unordered 4-site seeds that `f_L1` does not fill, on the twelve-vertex
two-cube `{0,1,2}×{0,1}×{0,1}` with off-patch occupancy `0`. The
`F_cut` map `f1` with remaining-bit tuple `(1, 1, 1, 1, 1)` fills each
of those six seeds. On the lex-first miss, the first neighborhood at
which `f_L1=0` and `f1=1` is reported by tick, site, and axis type. The
other five misses share that first axis type. That type is `opp2`, so
the 4-site miss is the same extra as the 2-site long-axis miss.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_l1_four_site_miss_mechanism_2026_08_15.py`](../scripts/f_l1_four_site_miss_mechanism_2026_08_15.py)
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

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 4-set of vertices is
a 4-site seed. There are `C(12,4)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov4(f) = |{ S : |S|=4 and f fills from S }|.
```

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 1)`.

Write `f1` for the `F_cut` map with remaining-bit tuple `(1, 1, 1, 1, 1)`.
That map fills every 4-site seed. It is displayed, not adopted.

New mechanism. Not leftover of the 6-count: a coverage ranking that
`cov4(f_L1)=489` names the miss cardinality, not the first refused
neighborhood. The first axis type is `opp2`, so the 4-site miss is the
same extra as the 2-site long-axis miss. That identity is displayed. It
is not an adopted selector.

**Theorem 1.** Independent recomputation of every 4-site seed reconfirms
exactly six misses for `f_L1`, and `f1` fills each of them. In
lexicographic order of sorted site 4-tuples the misses are

```text
{(0,0,0),(0,0,1),(2,0,0),(2,0,1)}
{(0,0,0),(0,1,0),(2,0,0),(2,1,0)}
{(0,0,0),(0,1,1),(2,0,0),(2,1,1)}
{(0,0,1),(0,1,0),(2,0,1),(2,1,0)}
{(0,0,1),(0,1,1),(2,0,1),(2,1,1)}
{(0,1,0),(0,1,1),(2,1,0),(2,1,1)}
```

On each, `f_L1` halts unfilled with lock-count history `(4, 8)` and
`f1` fills with history `(4, 10, 12)`. Equivalently
`cov4(f_L1) = 489` and `cov4(f1) = 495`.

**Theorem 2.** On the lex-first miss
`{(0,0,0),(0,0,1),(2,0,0),(2,0,1)}`, the first neighborhood at which
`f_L1` refuses and `f1` fires is

```text
t = 1
x = (1, 0, 0)
axis type = opp2 = (0, 1, 2)
```

The six-neighbor occupancy is `(1, 1, 0, 0, 0, 0)`: both ends of the
long `x` axis are occupied and the other two axes are empty. That is a
filled axis. An extra `f_L1` refuses. The same first event is seen on
the independent `f_L1` run and on the independent `f1` run. A second
simultaneous event at the same tick is the partner mid-axis site
`(1, 0, 1)` with the same axis type.

**Theorem 3.** The other five miss seeds have the same first axis type
`opp2`. Their first refused sites are `(1, 0, 0)`, `(1, 0, 0)`,
`(1, 0, 1)`, `(1, 0, 1)`, and `(1, 1, 0)` respectively, each at `t = 1`.
Because that type is `opp2`, the 4-site miss is the same extra as the
2-site long-axis miss. Display. Do not adopt opp2.
Do not write it into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The six f_L1 4-site misses, the independent f1 fills, and the first refused neighborhood on the lex-first miss (tick, site, axis type) are enumerated. opp2 is displayed, not written into Admissibility."
trace_class: frontier_discovery
target_claim_id: f_l1_four_site_miss_mechanism
target_blocker_text: "the first neighborhood at which f_L1 refuses and f1 fires, on the lex-first 4-site miss, remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first refused neighborhood; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for f_L1 and f1 on this twelve-vertex patch with off-patch o=0 and the six 4-site misses; no Z^3-wide law and no physical selector"
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
- the complete set of 495 unordered 4-site seeds;
- independent lock-step runs of `f_L1` and of `f1` from each miss.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

New mechanism. Not leftover of the 6-count. That leftover names
`cov4(f_L1)=489`. This residual is the first refused neighborhood on a
seed `f_L1` does not fill. The first axis type being `opp2` identifies
the same extra as the 2-site long-axis miss; it does not adopt that extra.

## Exact Target And Objects

**Target.** Reconfirm the six 4-site misses of `f_L1` and that `f1`
fills each of them by an independent run, then name the first
`(tick, site, axis type)` at which `f_L1` refuses and `f1` fires on the
lex-first miss.

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
f_L1(c) = 1  iff  u(c) ≥ 1,
f1(c)   = remaining-value of (1, 1, 1, 1, 1).
```

So `f_L1` has remaining-bit tuple `(1, 0, 1, 1, 1)` and `f1` has
`(1, 1, 1, 1, 1)`. They differ on `opp2` and on its complement
`(0, 2, 1)`. Neither map is adopted.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

An independent run of `f` from a seed is that iteration started at the
seed and continued to a fixed point. A miss is a 4-site seed whose
`f_L1` halt set has cardinality strictly less than 12. The first refused
neighborhood on a run is the lexicographically first unlocked site, at
the earliest tick, whose neighborhood has `f_L1=0` and `f1=1`. Tick
`t = 1` is the first evaluation on the seed occupancy.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The unbalanced-axis map `f_L1` is one element of
`F_cut`. It is not Hamming parity. On the twelve-vertex two-cube with
off-patch occupancy `0`, exhaustive fill census of all 495 four-site
seeds reconfirms exactly six `f_L1` misses, listed above in lex order.
The `F_cut` map `f1` with remaining-bit tuple `(1, 1, 1, 1, 1)` fills
each of those six seeds on an independent run. The lock-count histories
are `(4, 8)` for `f_L1` and `(4, 10, 12)` for `f1`.

**Theorem 2.** On the lex-first miss
`{(0,0,0),(0,0,1),(2,0,0),(2,0,1)}`, the first neighborhood with
`f_L1(nbhd)=0` and `f1(nbhd)=1` is tick `t = 1`, site `(1, 0, 0)`,
axis type `opp2` `= (0, 1, 2)`. Coverage maps that fire `opp2` form on
that filled axis; an extra `f_L1` refuses.

**Theorem 3.** The other five miss seeds have the same first axis type.
Because that type is `opp2`, the 4-site miss is the same extra as the
2-site long-axis miss. Display. Do not adopt opp2. Do not write it into
Admissibility. The first refused neighborhood is a displayed census
output, not a selected occupancy law.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| six `f_L1` misses | exhaustive 495-seed fill census; lex list as above |
| `f1` fills each miss | independent run from each of the six seeds fills with history `(4, 10, 12)` |
| `cov4(f_L1)=489`, `cov4(f1)=495` | 495 minus six misses; `f1` fills every 4-site seed |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| 495 four-site seeds | `C(12,4)` unordered 4-sets |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| first refused neighborhood | `t = 1`, site `(1, 0, 0)`, axis type `opp2` on the lex-first miss |
| same first axis type on the other five | each first refusal is `opp2` at `t = 1` |
| same extra as the 2-site long-axis miss | first axis type is `opp2`; displayed, not adopted |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity: Hamming is a different `F_cut` map
   (it disagrees on the two-unbalanced-axis orbit) and is not this
   miss-set residual.
2. Replace off-patch occupancy `0` by a blank-block: first-wave
   candidates become undefined; that is a different census.
3. Report only `cov4(f_L1)=489`: that leftover names the miss count, not
   the first refused neighborhood.
4. Adopt `opp2` as the physical rule: the note displays the first axis
   type and writes nothing into Admissibility.
5. Score only the `f1` run: the theorem requires independent runs of
   both maps from each miss.
6. Treat a later tick as first: on every miss the first refusal is at
   `t = 1` on the seed occupancy itself.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover restatement of the six-count coverage ranking.
- No adoption of `opp2`.
- No blank-block or 2-site variant as the claimed object.

## No-Go Discipline Gate

The only negative claim is that `f_L1` refuses a filled-axis
neighborhood that `f1` fires, on each of the six 4-site misses. The
first refused neighborhood is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| six-miss reconfirm | Score every 4-site seed under `f_L1` and under `f1`. | Theorem 1 and check `thm1-six-misses-and-f1-fills`. | **ATTEMPTED** |
| lex-first refusal | Name the first `(t, x, axis type)` on `{(0,0,0),(0,0,1),(2,0,0),(2,0,1)}`. | Theorem 2 and check `thm2-lex-first-refusal`. | **ATTEMPTED** |
| other-five type | Compare first axis types on the remaining five misses. | Theorem 3 and check `thm3-other-five-same-axis-type`. | **ATTEMPTED** |
| display, do not adopt | Ask whether `opp2` is written into Admissibility. | Theorem 3 and check `thm3-display-not-adopt-opp2`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: `f_L1` refuses `opp2` on these six
misses while `f1` fires it. Naming the first refused neighborhood and
stating that the other five share the same first axis type are two
certificates of the same filled-axis refusal, so they collapse rather
than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| six misses / first `opp2` refusal | no: a miss list does not name a neighborhood | no: one neighborhood does not list the six seeds | independent exact objects |
| lex-first `(t,x,type)` / other-five type | yes: the type is the shared mechanism | no: a shared type does not name the lex-first site | collapse into the refused-axis type |
| `cov4(f_L1)=489` / six named misses | yes: six misses give the count | yes: the count is the size of the six-set | collapse into the miss set |
| 2-site long-axis extra / this first refusal | yes: both extras are `opp2` | no: the 4-site `(t,x)` is not the 2-site site list | same extra, different seed class |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| six 4-site misses | explicit seed class; a two-site miss list is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| first axis type `opp2` | displayed mechanism, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:100` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:144` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:149` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:163` | `f1` definition | remaining-bit tuple `(1, 1, 1, 1, 1)` | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:54` | 495 four-site seeds | `C(12,4)` unordered 4-sets on the two-cube | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:214` | independent runs | lock-step evolution from each miss seed | yes |
| `scripts/f_l1_four_site_miss_mechanism_2026_08_15.py:275` | first refused neighborhood | earliest `(tick, site, axis type)` with `f_L1=0` and `f1=1` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: `f_L1` and `f1` from each miss | independent runs; `f1` fills; `f_L1` misses |
| per block | yes: the first refused neighborhood | tick, site, and axis type on the lex-first miss; same type on the other five |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does lie in `F_cut` and does fill 489 of the 495 four-site seeds. That
positive member does not make `f_L1` a maximizer and does not write
`opp2` into Admissibility. The remaining physical choice — which, if any,
`F_cut` map is the Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f_L1` is already known to miss six
4-site seeds because its remaining bit `opp2` is `0`, so naming the
first refused neighborhood might be called leftover-character of the
coverage ranking or of the miss-set list. That objection is correctly
about the miss count and the remaining-bit tuple. It does not overturn
the stated theorem: the new object is the first `(tick, site, axis type)`
on the lex-first miss, together with the statement that the other five
misses share that first axis type. Displaying `opp2` names that
mechanism and identifies the same extra as the 2-site long-axis miss.
`opp2` is not adopted.

A second steelman is that this cannot be a new mechanism if the extra is
the same `opp2` bit that already explains the 2-site long-axis misses.
The seed class is new — six 4-site seeds, not four 2-site seeds — and
the first refused 4-site neighborhood was unnamed. The identity of the
extra is the displayed conclusion, not a reason to skip the census.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`f_L1`, `f1`, the six misses, and the first refused neighborhood are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the first refused 4-site neighborhood or
writes `opp2` into Admissibility.

No-Go Discipline disposition: **PASS** for the six-miss reconfirm, the
independent `f1` fills, and the displayed first refused neighborhood
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
`f_L1` and `f1` independently from every 4-site seed, reconfirms the six
`f_L1` misses and that `f1` fills each of them, names the first refused
neighborhood on the lex-first miss by tick, site, and axis type, checks
that the other five misses share that first axis type, checks that
`f_L1` is not Hamming parity, and does not adopt `opp2`. Declared audit
inputs are this note and the axiom memo. No runner cache is written.
