---
claim_id: f_cut_fillers_l1_bit_and_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut 1-site fillers, N_and match L1's remaining orbit bits (opp2=0, adj2=1, vertex3=1, mixed3=1). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_fillers_l1_bit_and_2026_08_15.py
---

# AND Of L1's Remaining Bits Among The Eight `F_cut` Fillers

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact AND-census of independently motivated remaining orbit
bits on the eight cube-covariant complement-even 1-site fillers of the
twelve-vertex two-cube with off-patch occupancy `0`. The unbalanced-axis
map `f_L1` is displayed as the unique match. It is not adopted as the
physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_fillers_l1_bit_and_2026_08_15.py`](../scripts/f_cut_fillers_l1_bit_and_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The 24 proper cube rotations act on neighbor 6-tuples in `{0,1}^6` and
partition those 64 cells into 10 orbits. Cube-covariant predicates are the
`{0,1}`-assignments to those orbits. The three displayed cuts

1. vanish on empty: `f(empty)=0`,
2. vanish on full: `f(full)=0`,
3. complement-even: `f(c)=f(1-c)`

leave five free bits, so `|F_cut|=32`. On the two-cube
`{0,1,2}×{0,1}×{0,1}`, seed `(0,0,0)` starts locked. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. Fill means
`|locks_halt|=12`. Reconstructing that dynamics on every map in `F_cut`
yields exactly eight fillers.

That eight-element fill set is leftover-character inventory of the
`F_cut` fill census (#6399). It is not the residual of this note. This
note asks the conjunction question: how many of those eight match L1's
remaining orbit bits.

The axis type of a 6-tuple `c` is the triple `(u,b,e)` with `u+b+e=3`,
where `u` is the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`.
The remaining free orbits after the vanish cuts, and the names used here,
are

| name | `(u,b,e)` | geometric reading | L1 value |
|---|---|---|---:|
| `wt1` | `(1,0,2)` | one-axis contrast; a 1-site wave | 1 |
| `opp2` | `(0,1,2)` | opposite pair; balanced axis silent | 0 |
| `adj2` | `(2,0,1)` | two-axis contrast forms | 1 |
| `vertex3` | `(3,0,0)` | three-axis contrast; cube-vertex type | 1 |
| `mixed3` | `(1,1,1)` | mixed triple | 1 |

Complement-even forces `wt5=wt1`, `adj4=adj2`, and `opp4=opp2`. The bit
`wt1=1` is already required to have a 1-site first wave: a seed neighbor
sees a weight-1 6-tuple, so `wt1=0` empties the first wave and cannot
fill. The remaining independently motivated bits are therefore
`opp2=0`, `adj2=1`, `vertex3=1`, and `mixed3=1`.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

**Theorem 1.** `f_L1` is in the eight fillers and matches the bit tuple
`(wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,1,1)`.

**Theorem 2.** `N_and` is the number of the eight fillers matching that
tuple.

**Theorem 3.**

```text
N_and = 1.
```

The extras select L1 among the `F_cut` 1-site fillers. Displayed, not
adopted. Do not write the tuple into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the eight F_cut 1-site fillers, membership of f_L1, the remaining-bit tuple, and the exact AND count N_and=1 are enumerated. The tuple is displayed, not written into Admissibility."
trace_class: upstream_support
target_claim_id: f_cut_fillers_l1_bit_and
target_blocker_text: "whether the remaining orbit bits opp2=0, adj2=1, vertex3=1, mixed3=1 select L1 uniquely among the eight F_cut 1-site fillers"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the N_and census; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the eight F_cut 1-site fillers on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the 1-site seed `(0,0,0)`;
- the named remaining bits `opp2`, `adj2`, `vertex3`, `mixed3`, with
  `wt1` already required for a 1-site wave.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of #6399. Not leftover-character of the static eight-filler count.

## Exact Target And Objects

**Target.** Count how many of the eight `F_cut` 1-site fillers match L1's
remaining orbit bits, and decide whether that conjunction selects `f_L1`
inside the eight.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The ten axis-type classes `(u,b,e)` are exactly the ten orbits. Complement
sends `(u,b,e)` to `(u,e,b)`.

| `(u,b,e)` | name | orbit size | complement image |
|---|---|---:|---|
| `(0,0,3)` | empty | 1 | `(0,3,0)` full |
| `(0,3,0)` | full | 1 | `(0,0,3)` empty |
| `(0,1,2)` | `opp2` | 3 | `(0,2,1)` `opp4` |
| `(0,2,1)` | `opp4` | 3 | `(0,1,2)` `opp2` |
| `(1,0,2)` | `wt1` | 6 | `(1,2,0)` `wt5` |
| `(1,2,0)` | `wt5` | 6 | `(1,0,2)` `wt1` |
| `(2,0,1)` | `adj2` | 12 | `(2,1,0)` `adj4` |
| `(2,1,0)` | `adj4` | 12 | `(2,0,1)` `adj2` |
| `(1,1,1)` | `mixed3` | 12 | `(1,1,1)` |
| `(3,0,0)` | `vertex3` | 8 | `(3,0,0)` |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are three complement-pair bits and two complement-fixed orbit bits,
so `|F_cut|=32`.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The eight fillers are the maps in `F_cut` whose halt set has cardinality
12. Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1.
```

The remaining-bit tuple of a filler is the assignment
`(wt1,opp2,adj2,vertex3,mixed3)`. The L1 values of that tuple are
`(1,0,1,1,1)`. `N_and` is the number of fillers whose remaining-bit
tuple equals that L1 tuple.

The bits are independently motivated, not fitted to isolate L1 after
the fill census:

- `wt1=1` is already required to have a 1-site wave;
- `opp2=0` is balanced-axis silence: a fully occupied opposite pair
  with no contrast does not form;
- `adj2=1` is two-axis contrast formation;
- `vertex3=1` is three-axis contrast formation;
- `mixed3=1` is mixed-triple formation.

Do not write the tuple into Admissibility.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly eight
members of `F_cut` fill the twelve-vertex two-cube from seed `(0,0,0)`
with off-patch occupancy `0`. The unbalanced-axis map `f_L1` is one of
those eight. It is not Hamming parity. Its remaining-bit tuple is
`(wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,1,1)`, and complement-even forces
`wt5=1`, `adj4=1`, `opp4=0`. Its lock cardinalities are
`(1,4,8,11,12)` and its halt tick is `4`.

**Theorem 2.** Exhaustive comparison of the eight reconstructed fillers
against that tuple gives

```text
N_and = 1.
```

**Theorem 3.** Because `N_and = 1`, no second match is displayed. The
conjunction of the remaining bits selects `f_L1` among the eight `F_cut`
1-site fillers. Displayed, not adopted. The tuple is not an Admissibility
clause.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| eight fillers | exhaustive 32-run census of `F_cut` to a fixed point with `|locks|=12` |
| `f_L1` is in the eight | halt set has cardinality 12 at tick 4 |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit `adj2` has even weight and `f_L1=1` |
| L1 bit tuple | `wt1=1`, `opp2=0`, `adj2=1`, `vertex3=1`, `mixed3=1` |
| complement-even complements | `wt5`, `adj4`, `opp4` equal `wt1`, `adj2`, `opp2` |
| `wt1=1` required | a 1-site first wave sees a `wt1` cell |
| `N_and` | count of the eight whose remaining bits equal L1's |
| second match | none; `N_and=1` |
| physical Admissibility selection | open and not claimed; the tuple is not written in |

Every leaf needed for the stated AND census is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on `adj2`,
   and Hamming is not a filler.
2. Flip any one of `opp2`, `adj2`, `vertex3`, `mixed3` away from L1's
   value: the resulting filler, when it exists, is a different map, so
   `N_and` would miss L1 or count a non-L1 filler.
3. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`, and the eight-filler set is a different census.
4. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
5. Assert `N_and>1`: the reconstructed eight contain only one match.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the static 32 or of the eight-filler
  census (#6399) in place of this AND count.
- No blank-block, 2-site, or 3-site variant.
- No axiom edit: the tuple is displayed, not written into Admissibility.

## No-Go Discipline Gate

The only negative claim is uniqueness of a second match: there is none,
because `N_and=1`. The positive count `N_and=1` is an exact enumeration,
not a wall, and it is not an Admissibility clause.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| eight-filler reconstruction | Run every map in `F_cut` to a fixed point and keep `|locks|=12`. | Theorem 1 and check `thm1-eight-fillers` give eight fillers. | **ATTEMPTED** |
| L1 membership and tuple | Evaluate `f_L1` on the named orbits and on the two-cube. | Theorem 1 and check `thm1-f-L1-in-eight-and-tuple`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| `N_and` census | Filter the eight fillers by the remaining-bit tuple. | Theorem 2 and check `thm2-n-and` give `N_and = 1`. | **ATTEMPTED** |
| second match | Ask whether another filler shares the tuple. | Theorem 3 and check `thm3-unique-no-second-match`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: a second match is absent. The count
`N_and=1` and the explicit uniqueness check are two certificates of the
same fact, so they collapse rather than count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_and=1` / no second match | yes: a count of one is uniqueness inside the eight | yes: uniqueness is a count of one | collapse into the same exact count |
| `f_L1` fills / Hamming does not | no: one map filling does not classify Hamming | no: Hamming failing does not prove `f_L1` fills | independent positive/negative members, not two walls |
| eight-filler count / `N_and` | no: membership in the eight is not the AND | no: an AND count does not replace the fill census | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| the eight fillers | explicit `F_cut` 1-site fill set; the other 24 maps in `F_cut` are excluded |
| remaining bits | explicit geometric motivations; not a leftover-character of #6399 |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| `N_and=1` | displayed uniqueness inside the eight, not an Admissibility clause |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:78` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:122` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:127` | Hamming mutation | `|c|_1 mod 2` is a different map | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:53` | remaining bits | named tuple `(wt1,opp2,adj2,vertex3,mixed3)` | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:265` | eight-filler reconstruction | `F_cut` maps with `|locks|=12` | yes |
| `scripts/f_cut_fillers_l1_bit_and_2026_08_15.py:348` | `N_and` | AND cardinality inside the eight | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut`, then every filler | the AND is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(eight fillers, N_and)` | uniqueness inside the eight is `N_and=1` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: the
conjunction of independently motivated remaining bits selects `f_L1`
among the eight `F_cut` 1-site fillers. That unique match does not write
the tuple into Admissibility and does not select `f_L1` as the physical
rule. The remaining physical choice — which, if any, occupancy predicate
is the Admissibility rule — stays explicit.

### N7 — hostile steelman

The strongest objection is that the remaining bits are just L1's own
orbit values, so `N_and=1` is leftover-character of the eight-filler
census: among eight maps that already vary exactly on
`(opp2,mixed3,vertex3)` with `wt1=adj2=1` forced by fill, picking L1's
three remaining values is tautological. That objection is correctly about
the algebraic shape of the eight. It does not overturn the stated
theorem. The bits are independently motivated (`opp2=0` is balanced-axis
silence; `adj2=1` is two-axis contrast; `vertex3=1` and `mixed3=1` are
the two weight-3 formation bits), and `N_and` is their conjunction count
inside the eight, not the eight-count itself. A second match would have
been displayed. None exists.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
eight fillers, remaining-bit tuple, and `N_and` are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

The eight-filler fill census (#6399) is the class this note filters. It
is not a parent and does not close `N_and`.

No earlier mechanism retires the remaining-bit AND or writes the tuple
into Admissibility.

No-Go Discipline disposition: **PASS** for the uniqueness of the match
and the exact count `N_and = 1` stated above.

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
`F_cut`, reconstructs the eight 1-site fillers, checks that `f_L1` is
among them and matches `(wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,1,1)`,
reports `N_and = 1`, and checks that no second match exists. Declared
audit inputs are this note and the axiom memo. No runner cache is
written.
