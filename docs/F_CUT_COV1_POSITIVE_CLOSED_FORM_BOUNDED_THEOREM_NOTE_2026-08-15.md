---
claim_id: f_cut_cov1_positive_closed_form_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether positive 1-site coverage is equivalent to P is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov1_positive_closed_form_2026_08_15.py
---

# Whether Positive 1-Site `F_cut` Coverage Is The Selector `P`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 1-site coverage of the 32 cube-covariant
complement-even predicates that vanish on empty and full, on the
twelve-vertex two-cube, with off-patch occupancy `0`. The remaining-bit
predicate `P` is displayed as a candidate selector for `cov_1(f)>0`.
Neither `P` nor any map is adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov1_positive_closed_form_2026_08_15.py`](../scripts/f_cut_cov1_positive_closed_form_2026_08_15.py)
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
class. The 2-site selector `P` for positive coverage is leftover inventory
of a different seed cardinality. New k, not leftover of the cov2 selector.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each singleton vertex is a 1-site
seed. Off-patch neighbors have occupancy `0`. A blank-block is a different
rule; it is not used. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process is
synchronous and stops at a fixed point in at most 12 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov_1(f) = |{ S : |S|=1 and f fills from S }|.
```

Do not list the seeds.

`f_L1(c)=1` if and only if some axis is unbalanced: `c_{+μ} ≠ c_{-μ}` for
at least one `μ ∈ {x,y,z}`. Equivalently, some discrete neighbor contrast
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming.

The five remaining bits of an `F_cut` map, in the displayed order
`(wt1, opp2, adj2, vertex3, mixed3)`, are the values on the three
complement-pairs and two complement-fixed orbits after empty and full are
forced to `0`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write

```text
P(f) := (wt1=1) and (adj2,vertex3,mixed3) ≠ (0,0,0).
```

`P` is a predicate on remaining bits. It is displayed only.

**Theorem 1.** Among the 32 maps, `cov_1(f)>0` if and only if `P(f)` is
not equivalent. One counterexample remaining-bit tuple is

```text
(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 1)
```

for which `P` holds and `cov_1 = 0`. This is the lexicographically first
remaining-bit counterexample.

**Theorem 2.** The 32-map census of the displayed predicate and of
positive 1-site coverage is

```text
N_P = 14
N_pos = 8
N_both = 8.
```

Every map with `cov_1(f)>0` satisfies `P`. Six maps satisfy `P` and have
`cov_1(f)=0`.

**Theorem 3.** The failure of the equivalence, the counterexample tuple,
and the three counts are displayed only. Do not adopt `P`. Do not write `P` into Admissibility.

Displayed, not adopted.

Not leftover-character of #6494 (that was `P` for `cov_2`; different |S|).
Not leftover-character of #6495 (that was that both exceptions have
`cov_1=0`; not the 32-map equivalence). New k.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ten-orbit reconstruction, the 32-element F_cut, membership of f_L1, the predicate P, the 1-site coverage of every map, the failure of cov1>0 iff P, one remaining-bit counterexample, and the triple (N_P, N_pos, N_both) are enumerated. No physical law is selected."
trace_class: upstream_support
target_claim_id: f_cut_cov1_positive_closed_form
target_blocker_text: "whether cov1>0 is the same selector P among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the F_cut 1-site positive-coverage comparison with P; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for F_cut on this twelve-vertex patch with off-patch o=0 and 1-site seeds; no Z^3-wide law and no physical selector"
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
- the complete set of 1-site seeds;
- the remaining-bit predicate `P`.

No observational comparator, literature constant, Wilson weight, rate, or
generator is imported. No Record scalar functional appears.

## Exact Target And Objects

**Target.** For every member of `F_cut`, compute `cov_1(f)` on the
two-cube and evaluate `P(f)` on its remaining bits. Report whether
`cov_1(f)>0` if and only if `P(f)`. If the biconditional fails, display
one remaining-bit counterexample. Report `N_P`, `N_pos`, and `N_both`.

Write a neighbor configuration as `c ∈ {0,1}^6`. A proper cube rotation `R`
acts by `(R·c)(d) = c(R^{-1}d)` on the six face directions `d`. A map
`f:{0,1}^6 → {0,1}` is cube-covariant when `f(R·c)=f(c)` for every such `R`.
Equivalently, `f` is constant on each orbit.

The axis type of `c` is the triple `(u,b,e)` with `u+b+e=3`, where `u` is
the number of axes with `c_{+} ≠ c_{-}`, `b` the number with
`(c_{+},c_{-})=(1,1)`, and `e` the number with `(c_{+},c_{-})=(0,0)`. These
ten types are exactly the ten orbits. Complement sends `(u,b,e)` to
`(u,e,b)`.

The remaining-bit order is

```text
wt1 = (1,0,2), opp2 = (0,1,2), adj2 = (2,0,1),
vertex3 = (3,0,0), mixed3 = (1,1,1).
```

`P` ignores `opp2` and requires `wt1=1` together with a nonzero triple
`(adj2,vertex3,mixed3)`.

**Theorem 1.** Exhaustive evaluation of all 32 maps on the twelve 1-site
seeds shows that `cov_1>0` iff `P` is not equivalent. The
lexicographically first remaining-bit counterexample is `(1, 0, 0, 0, 1)`:
`wt1=1`, `opp2=0`, `adj2=0`, `vertex3=0`, `mixed3=1`, so `P` holds, and
that map fills from none of the twelve singletons.

**Theorem 2.** Counting the 32 remaining-bit assignments gives
`N_P = 14`, `N_pos = 8`, `N_both = 8`.

**Theorem 3.** Displayed, not adopted.

## Proof-Obligation Graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells with the listed sizes |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free after the vanish cuts |
| `f_L1` is in `F_cut` | `u` is rotation- and complement-invariant and `u(empty)=u(full)=0` |
| `f_L1` is not Hamming | the two-unbalanced-axis orbit has even weight and `f_L1=1` |
| two-cube has twelve vertices | `{0,1,2}×{0,1}×{0,1}` |
| twelve 1-site seeds | `C(12,1)=12` |
| off-patch occupancy `0` | declared stencil default; not a blank-block |
| `P` on remaining bits | `(wt1=1)` and `(adj2,vertex3,mixed3)≠(0,0,0)` |
| `cov_1>0` iff `P` | not equivalent; first counterexample `(1, 0, 0, 0, 1)` |
| `(N_P, N_pos, N_both)` | `(14, 8, 8)` from the 32-map census |

## Counterfactual And Mutation Table

1. Replace `f_L1` by Hamming parity `|c|_1 mod 2`: the maps disagree on the
   two-unbalanced-axis orbit, and Hamming is a different `F_cut` member.
2. Change the off-patch default away from `0`: the occupancy stencil
   changes and the coverage counts are a different object.
3. Drop any of the three cuts: the class is no longer the 32-element
   `F_cut`.
4. Score 2-site seeds: that leftover is #6494, a different `|S|`.
5. Restrict to the two #6495 exceptions: that leftover reports
   `cov_1=0` on a pair, not the 32-map biconditional.
6. Adopt `P` as the Admissibility rule: Theorem 3 forbids the adoption;
   `P` is displayed only.

## What This Does Not Claim

- No physical Admissibility selector and no adopted occupancy law.
- No Qubit rewrite and no `M_2(C)`-valued conditional probability.
- No `Z^3`-wide formation, rate, or generator.
- No identification of `f_L1` with Hamming parity.
- No leftover-character restatement of the 2-site selector `P` in place
  of this 1-site equivalence.
- No list of the 1-site seeds.
- No blank-block variant.
- No adoption of `P`.

## No-Go Discipline Gate

The only negative claim is the biconditional itself: on this patch,
`cov_1(f)>0` is not equivalent to `P(f)` among the 32 maps. The counts
`N_P=14`, `N_pos=8`, `N_both=8` and the counterexample tuple are an exact
enumeration, not a wall.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| orbit reconstruction | Recompute the 24 rotations and the 10 axis-type orbits. | Theorem 1 and checks `thm1-twenty-four-rotations` / `thm1-ten-orbits`. | **ATTEMPTED** |
| three-cut class | Force vanish-on-empty, vanish-on-full, and `f(c)=f(1-c)`. | Theorem 1 and check `thm1-f-cut-cardinality` give `|F_cut|=32`. | **ATTEMPTED** |
| Hamming-as-`f_L1` | Test whether `|c|_1 mod 2` equals the unbalanced-axis predicate. | Theorem 1 and check `thm1-f-L1-not-hamming` separate the maps. | **ATTEMPTED** |
| 1-site coverage census | Score every map in `F_cut` by `cov_1` on the twelve singletons. | Theorem 1 and check `thm1-two-cube-and-one-site-seeds`. | **ATTEMPTED** |
| remaining-bit predicate `P` | Evaluate `(wt1=1)` and `(adj2,vertex3,mixed3)≠(0,0,0)` on each map. | Theorem 2 and check `thm2-counts`. | **ATTEMPTED** |
| biconditional | Ask whether `cov_1>0` iff `P` on all 32 maps. | Theorem 1 and checks `thm1-equivalence-fails` / `thm1-counterexample-tuple`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative conclusion: the biconditional `cov_1>0` iff `P`
fails. The counterexample tuple and the gap `N_P−N_both=6` are two
certificates of the same failure, so they collapse rather than count as
two walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| counterexample `(1, 0, 0, 0, 1)` / `N_P≠N_pos` | yes: one witness falsifies iff | yes: unequal counts falsify iff | collapse into the biconditional failure |
| leftover of #6494 / this census | no: that leftover scored `|S|=2` | no: a 1-site census does not replace the 2-site selector | different object |
| leftover of #6495 / this census | no: that leftover reported `cov_1=0` on two exceptions | no: the 32-map biconditional is not a pair of zeros | different object |
| static `|F_cut|=32` / the counts | no: membership is not dynamics | no: a coverage census does not replace the three-cut class | separate exact counts |

Physical law selection is not a wall: this note makes no negative theorem
about the existence of a selector and simply does not claim one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “work on the twelve-vertex two-cube” | explicit patch hypothesis; not a `Z^3` theorem |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| `F_cut` | explicit three-cut class; the other 992 covariant maps are excluded |
| 1-site seeds | explicit seed class; a 2-site selector is a different residual |
| “lock” | Record permanence on this Boolean occupancy model, not a possibility-valued law |
| “cube-covariant” | invariance under the 24 proper rotations, cited to Lattice/Admissibility |
| Hamming parity | displayed mutation only |
| remaining-bit predicate `P` | displayed candidate selector, not a selected law |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:73` | 24 proper rotations | signed permutations with determinant `+1` | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:117` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:122` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:50` | 1-site seed size | `SEED_K = 1` | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:309` | `cov_1(f)` | number of 1-site seeds a map fills | yes |
| `scripts/f_cut_cov1_positive_closed_form_2026_08_15.py:317` | predicate `P` | `(wt1=1)` and `(adj2,vertex3,mixed3)≠(0,0,0)` | yes |

No evidence citation is used to claim that a physical occupancy law, a
formation rate, or a `Z^3`-wide selector has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each is assigned its axis-type orbit; no broader cell class is classified |
| per site | yes: the twelve two-cube vertices | each uses the same six-direction stencil with off-patch occupancy `0` |
| per mode | yes: every map in `F_cut` | the comparison is this class on 1-site seeds; other classes are unclaimed |
| per block | yes: the biconditional on the 32 | `cov_1>0` iff `P` fails; one remaining-bit witness is displayed |
| lattice wide | no | no `Z^3`-wide formation or Admissibility selector is asserted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector, and none is reclassified as an import or wall.

One partial-closure mechanism is displayed rather than suppressed: every
map with `cov_1>0` does satisfy `P`, so `P` is necessary for positive
1-site coverage on this patch. Necessity is not sufficiency: six maps in
`P` have `cov_1=0`. The remaining physical choice — which, if any,
`F_cut` map is the Admissibility occupancy predicate — stays explicit.

The open derivation-obligation registry
(`docs/audit/data/derivation_obligations.json`) names no occupancy-to-lock
coverage target; those open gates are unused here.

### N7 — hostile steelman

The strongest objection is that #6494 already named `P` as the selector
for positive 2-site coverage, and that #6495 already recorded `cov_1=0`
on two exceptions, so a 1-site census of the same 32 maps might be called
leftover decoration of those two surfaces. That objection is correctly
about the 2-site selector and about a pair of zeros. It does not overturn
the stated theorem: among all 32 maps in `F_cut`, `cov_1>0` is not
equivalent to `P`, with `N_P=14`, `N_pos=8`, `N_both=8`, and first
counterexample `(1, 0, 0, 0, 1)`. That is a new k, not leftover-character
of #6494 or #6495.

### N8 — cross-cycle echo

Repository search found nearby occupancy and covariance surfaces. They are
context, not load-bearing dependencies. The 24 rotations, 10 orbits,
`F_cut`, the 1-site coverage of all 32 maps, and the predicate `P` are
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No earlier mechanism retires the 1-site biconditional or restores
`cov_1>0` iff `P` inside the 32-map class.

No-Go Discipline disposition: **PASS** for the failure of `cov_1>0` iff
`P` and the exact triple `(N_P, N_pos, N_both)=(14, 8, 8)` stated above.

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
`F_cut`, evaluates all 32 maps on the two-cube from every 1-site seed,
evaluates `P` on remaining bits, reports that `cov_1>0` iff `P` fails,
displays the lexicographically first remaining-bit counterexample
`(1, 0, 0, 0, 1)`, reports `N_P=14`, `N_pos=8`, `N_both=8`, and checks
that `f_L1` is not Hamming parity. Declared audit inputs are this note
and the axiom memo. No runner cache is written.
