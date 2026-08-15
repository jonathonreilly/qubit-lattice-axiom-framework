---
claim_id: f_cut_fillers_sparsest_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the eight F_cut 1-site fillers on the two-cube with off-patch o=0, the minimal support is 36 and N_min_cut = 1 maps achieve it. f_L1 is not the unique minimizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_fillers_sparsest_2026_08_15.py
---

# Sparsest Filler Inside The Three-Cut Class `F_cut`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact support census among the eight cube-covariant
complement-even 1-site fillers of the twelve-vertex two-cube that vanish
on empty and full, with off-patch occupancy `o=0`. The unbalanced-axis
map `f_L1` is displayed as one filler. It is not adopted as the physical
Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_fillers_sparsest_2026_08_15.py`](../scripts/f_cut_fillers_sparsest_2026_08_15.py)
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
`|locks_halt|=12`.

Exactly eight members of `F_cut` fill. That 8-count is leftover-character
inventory of the `F_cut` fill census. It is not the residual of this note.
The unique support-26 filler among the 96 cube-covariant 1-site fillers is
outside `F_cut`. That 96-map support minimum is a different leftover
inventory. This note asks the restricted question: among those eight
`F_cut` fillers, who is sparsest?

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The definition is never Hamming.

For a map `f` write

```text
supp(f) = |{ c ∈ {0,1}^6 : f(c)=1 }|.
```

**Theorem 1.** The eight `F_cut` 1-site fillers reconfirm. `f_L1` is one
of them, and `supp(f_L1)=56`.

**Theorem 2.** Let `m_cut` be the minimum of `supp` over those eight, and
let `N_min_cut` be the number of those eight that attain `m_cut`. Then

```text
m_cut = 36,    N_min_cut = 1.
```

**Theorem 3.** `N_min_cut=1`, but that unique minimizer is **not**
`f_L1`. It is the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 0, 0).
```

Displayed, not adopted. The three cuts plus sparsity therefore do not
select `f_L1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, the eight 1-site fillers, and the support minimum among those eight are enumerated. Uniqueness of f_L1 as the F_cut support-minimizer is false on this patch. No physical law is selected."
trace_class: negative_route_pruning
target_claim_id: f_cut_fillers_sparsest
target_blocker_text: "whether support-minimality among the eight F_cut 1-site fillers selects f_L1 without an extra axiom"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut support census; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0; no Z^3-wide law and no physical selector"
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
- the 1-site seed `(0,0,0)`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

Not leftover-character of the 96-map support minimum. Not leftover-character
of the static 32-count of `F_cut` or of the 8-count of `F_cut` fillers.

## Exact Target And Objects

**Target.** Among the eight `F_cut` 1-site fillers, compute the support
minimum and decide whether `f_L1` is the unique minimizer.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

| `(u,b,e)` | displayed name | orbit size | complement image |
|---|---|---:|---|
| `(0,0,3)` | empty | 1 | `(0,3,0)` full |
| `(0,3,0)` | full | 1 | `(0,0,3)` empty |
| `(0,1,2)` | `opp2` | 3 | `(0,2,1)` |
| `(0,2,1)` | complement of `opp2` | 3 | `(0,1,2)` |
| `(1,0,2)` | `wt1` | 6 | `(1,2,0)` |
| `(1,2,0)` | complement of `wt1` | 6 | `(1,0,2)` |
| `(2,0,1)` | `adj2` | 12 | `(2,1,0)` |
| `(2,1,0)` | complement of `adj2` | 12 | `(2,0,1)` |
| `(1,1,1)` | `mixed3` | 12 | `(1,1,1)` |
| `(3,0,0)` | `vertex3` | 8 | `(3,0,0)` |

`F_cut` is the class of cube-covariant maps with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. The empty/full pair is forced to `0`. The remaining free
data are the three complement-pair bits `wt1`, `opp2`, `adj2` and the two
complement-fixed orbit bits `vertex3`, `mixed3`, so `|F_cut|=32`. Each
member is recorded as the remaining-bit tuple

```text
(wt1, opp2, adj2, vertex3, mixed3) ∈ {0,1}^5.
```

Support is then exact:

```text
supp = 12·wt1 + 6·opp2 + 24·adj2 + 8·vertex3 + 12·mixed3.
```

Define

```text
f_L1(c) = 1  iff  u(c) ≥ 1.
```

Its remaining-bit tuple is `(1, 0, 1, 1, 1)`, so `supp(f_L1)=56`. This is
never Hamming `|c|_1 mod 2`, whose tuple is `(1, 0, 0, 1, 1)`.

A locked set `S` determines occupancies: a lattice neighbor in `S` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `S` by

```text
S ∪ { v in two-cube \ S : f(neighborhood_6(v; S)) = 1 }.
```

The eight `F_cut` fillers and their supports are the exact finite domain
of `m_cut`.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. Exactly eight
members of `F_cut` fill the twelve-vertex two-cube from seed `(0,0,0)`
with off-patch occupancy `0`. The unbalanced-axis map `f_L1` is one of
those eight. It is not Hamming parity. Its support is

```text
supp(f_L1) = 56.
```

Lock cardinalities of `f_L1` are `(1,4,8,11,12)` and the halt tick is `4`.

**Theorem 2.** Exhaustive support evaluation of those eight fillers gives

```text
m_cut = 36,    N_min_cut = 1.
```

The eight remaining-bit tuples and supports are

| `(wt1, opp2, adj2, vertex3, mixed3)` | `supp` | halt history |
|---|---:|---|
| `(1, 0, 1, 0, 0)` | 36 | `(1,4,8,10,11,12)` |
| `(1, 1, 1, 0, 0)` | 42 | `(1,4,8,10,11,12)` |
| `(1, 0, 1, 1, 0)` | 44 | `(1,4,8,11,12)` |
| `(1, 0, 1, 0, 1)` | 48 | `(1,4,8,10,11,12)` |
| `(1, 1, 1, 1, 0)` | 50 | `(1,4,8,11,12)` |
| `(1, 1, 1, 0, 1)` | 54 | `(1,4,8,10,11,12)` |
| `(1, 0, 1, 1, 1)` (`f_L1`) | 56 | `(1,4,8,11,12)` |
| `(1, 1, 1, 1, 1)` | 62 | `(1,4,8,11,12)` |

**Theorem 3.** `N_min_cut=1`, so there is a unique `F_cut` support
minimizer, and it is **not** `f_L1`. The unique minimizer is the displayed
tuple `(1, 0, 1, 0, 0)`: on the `wt1` and `adj2` complement-pairs, off on
`opp2`, `vertex3`, and `mixed3`. Displayed, not adopted.

The unique support-26 filler among the 96 empty-vanishing cube-covariant
1-site fillers is a different map: it fails complement-evenness, so it
lies outside `F_cut`. Restricting the same minimizer to `F_cut` therefore
opens a new domain; it does not inherit that 26-support winner.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| eight `F_cut` fillers | exhaustive 32-run census to a fixed point with `|locks_halt|=12` |
| `f_L1` is in `F_cut` and fills | remaining-bit tuple `(1,0,1,1,1)`; halt set has cardinality 12 |
| `supp(f_L1)=56` | `12+24+8+12` from the `wt1`, `adj2`, `vertex3`, and `mixed3` orbits |
| `f_L1` is not Hamming | Hamming is `(1,0,0,1,1)` and does not fill |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `m_cut` and `N_min_cut` | exhaustive support evaluation of the eight fillers |
| uniqueness of `f_L1` as `F_cut` sparsest | false; displayed tuple `(1,0,1,0,0)` has support 36 |
| 96-map support-26 winner | outside `F_cut`; not this domain |
| physical Admissibility selection | open and not claimed |

Every leaf needed for the stated census is discharged. No `Z^3`-wide
formation law is claimed.

## Mutations

1. Replace `f_L1` by Hamming `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming does not fill.
2. Replace the eight-element `F_cut` domain by the 96 empty-vanishing
   fillers: the unique support minimum becomes 26 and still is not
   `f_L1`, but that winner is outside `F_cut`.
3. Replace off-patch occupancy `0` by a blank-block: first-wave candidates
   become undefined; that is a different census.
4. Drop complement-even or the vanish-on-full cut: the class is no longer
   the 32-element `F_cut`.
5. Assert that `f_L1` is the unique `F_cut` support-minimizer: the
   displayed tuple `(1, 0, 1, 0, 0)` refutes uniqueness.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character count of the 96-map support minimum, of the
  static 32, or of the 8-count of `F_cut` fillers in place of this
  restricted support census.
- No blank-block, 2-site, or 3-site variant.

## No-Go Discipline Gate

The only negative claim is uniqueness: `f_L1` is not the unique support
minimizer among the eight `F_cut` 1-site fillers. The pair
`(m_cut, N_min_cut)=(36,1)` is an exact enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class and eight fillers | Force the three cuts and run every map in `F_cut`. | Theorem 1 and checks `thm1-f-cut-cardinality` / `thm1-eight-fillers`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-l1-not-hamming` separate the maps. | **ATTEMPTED** |
| `f_L1` support | Count `{c : f_L1(c)=1}` on the 64 cells. | Theorem 1 and check `thm1-l1-support-56` give `56`. | **ATTEMPTED** |
| `F_cut` support census | Evaluate `supp` on each of the eight fillers. | Theorem 2 and checks `thm2-m-cut` / `thm2-n-min-cut`. | **ATTEMPTED** |
| uniqueness of `f_L1` | Ask whether the unique `m_cut` map is `f_L1`. | Theorem 3 and checks `thm3-unique-is-not-l1` / `thm3-displayed-tuple`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: uniqueness of `f_L1` as the `F_cut`
sparsest filler fails. The explicit displayed tuple and the pair
`(m_cut, N_min_cut)=(36,1)` with that tuple not equal to `f_L1` are two
certificates of the same non-uniqueness, so they collapse rather than
count as two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `m_cut=36` / displayed `(1,0,1,0,0)` | yes: that tuple has support 36 | yes: a support-36 `F_cut` filler is the minimum | collapse into the uniqueness failure |
| eight fillers / `supp(f_L1)=56` | no: a fill count does not evaluate support | no: one support does not list the eight | independent positive members, not two walls |
| 96-map support-26 winner / `F_cut` minimum | no: that winner is outside `F_cut` | no: an `F_cut` minimum does not classify the 96 | separate domains |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| “the eight fillers” | explicit 1-site fill subset of `F_cut` |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| tuple `(1, 0, 1, 0, 0)` | displayed witness against uniqueness, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:78` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:122` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:127` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:269` | support | exact orbit-size sum on remaining bits | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:303` | class census | exact eight fillers and their supports | yes |
| `scripts/f_cut_fillers_sparsest_2026_08_15.py:131` | 96-map winner | unique support-26 map is outside `F_cut` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit and counted in `supp(f)` |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut`; the eight fillers | the support domain is this class on this seed; other seeds are unclaimed |
| per block | yes: the pair `(m_cut, N_min_cut)` | uniqueness of `f_L1` fails because the unique minimizer is `(1,0,1,0,0)` |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies the Boolean occupancy maps, and none is
reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: `f_L1`
does fill this patch from the 1-site seed, does lie in `F_cut`, and has a
definite support `56`. That positive member does not make `f_L1` the
sparsest `F_cut` filler and does not select it as the physical rule. The
remaining physical choice — which, if any, `F_cut` map is the
Admissibility occupancy predicate — stays explicit.

### N7 — hostile steelman

The strongest objection is that `f_L1` might still be the unique sparsest
map once one restricts to cells that occur along its own 1-site filling
trajectory, so a “dynamically occurring support” could restore uniqueness.
That objection is correctly about a smaller class. It does not overturn
the stated theorem: among all eight `F_cut` fillers, the unique
support-minimizer is the displayed tuple `(1, 0, 1, 0, 0)`, whose support
is `36` rather than `56`. That is a class-level extra sparser filler, not
a trajectory-level identity.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the eight fillers, and their supports are recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/CUBIC_NN_CONDITION_DOMAIN_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-13.md` | nearest-neighbor condition domain | the six-direction occupancy stencil is the Boolean shadow of that domain |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the `F_cut` support census or restores
uniqueness of `f_L1` as the sparsest of the eight.

No-Go Discipline disposition: **PASS** for the uniqueness failure and the
exact pair `(m_cut, N_min_cut)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube, isolates the eight fillers,
computes `supp` on each, reports `m_cut = 36` and `N_min_cut = 1`, checks
that `f_L1` fills with `supp(f_L1)=56` and is not Hamming parity, and
exhibits the displayed unique minimizer `(1, 0, 1, 0, 0)`. Declared audit
inputs are this note and the axiom memo. No runner cache is written.
