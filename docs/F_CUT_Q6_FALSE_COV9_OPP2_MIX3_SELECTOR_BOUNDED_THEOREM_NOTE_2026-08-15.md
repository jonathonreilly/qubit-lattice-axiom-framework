---
claim_id: f_cut_q6_false_cov9_opp2_mix3_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 4 F_cut maps with wt1=adj2=vertex3=0 on the two-cube with off-patch o=0, whether cov9>0 equals opp2=mixed3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q6_false_cov9_opp2_mix3_selector_2026_08_15.py
---

# Whether `cov9>0` Equals `opp2 ∧ mixed3` On The Four Q6-False Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 9-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored on the four
cube-covariant cut maps in `F_cut` that have `wt1=adj2=vertex3=0`. The
scored identity is whether `cov9>0` if and only if the displayed
predicate `Q := (opp2=1) and (mixed3=1)` holds among those four maps.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q6_false_cov9_opp2_mix3_selector_2026_08_15.py`](../scripts/f_cut_q6_false_cov9_opp2_mix3_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c9q6 named that the unique Q6-false positive remaining-bit
tuple is `(0, 1, 0, 0, 1)`. Q6-false is the four maps with
`wt1=adj2=vertex3=0`. This note tests whether `cov9>0` if and only if
`opp2 ∧ mixed3` among those four. Names the k=9 extra. Not
leftover-character of #6531 and not leftover-character of the 32-map
k=9 ranking.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

Q6-false is the subclass

```text
{ f in F_cut : wt1 = adj2 = vertex3 = 0 }.
```

Those four remaining-bit tuples are

```text
(0, 0, 0, 0, 0)
(0, 0, 0, 0, 1)
(0, 1, 0, 0, 0)
(0, 1, 0, 0, 1).
```

The displayed remaining-bit predicate on that subclass is

```text
Q := (opp2=1) and (mixed3=1).
```

Exactly one of the four tuples satisfies `Q`, namely `(0, 1, 0, 0, 1)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple has
`wt1=adj2=vertex3=1`, so `f_L1` is not Q6-false.

On the two-cube with off-patch occupancy `0`, write
`cov9(f) = |{S : |S|=9 and f fills from S}|`. There are `C(12,9)=220`
nine-site seeds. The boolean scored here is `cov9(f)>0`. Do not list the
seeds.

**Theorem 1.** Among the 4 Q6-false maps, `cov9>0` if and only if `Q`.
There is no counterexample. The unique positive map is the remaining-bit
tuple `(0, 1, 0, 0, 1)`, with `cov9 = 4`. The other three maps have
`cov9 = 0`.

**Theorem 2.** The three census integers on the 4-map set are

```text
N_pos = 1
N_Q = 1
N_both = 1.
```

**Theorem 3.** The identity is displayed only. Displayed, not adopted.
Do not adopt a bit. Do not write `Q` into Admissibility.

Do not adopt `Q`. Names the k=9 extra.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four Q6-false F_cut maps are scored exactly on the 220 nine-site seeds. Whether cov9>0 equals opp2 and mixed3 among those four is a finite Boolean identity on this patch. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_q6_false_cov9_opp2_mix3_selector
target_blocker_text: "whether cov9>0 equals opp2 and mixed3 among the four Q6-false F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q6-false cov9>0 versus opp2-and-mixed3 identity; do not adopt a bit"
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
predicate. `Q` is a displayed remaining-bit formula, not axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different
rule and is not used.

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

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`. Then
`cov9(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov9(f)>0`. Duality is not assumed: `cov9` is scored on
those 220 seeds.

Q6-false is the four maps with `wt1=adj2=vertex3=0`. The displayed
predicate on that subclass is

```text
Q := (opp2=1) and (mixed3=1).
```

Wt1, adj2, and vertex3 are already fixed at 0 on the subclass. Displayed,
not adopted.

## Theorem 1 — `cov9>0` iff `Q` among the four maps

Enumerate all 32 remaining-bit tuples of `F_cut`, keep the four with
`wt1=adj2=vertex3=0`, and score `cov9` on the 220 nine-site seeds. Then
`cov9(f) > 0` if and only if `Q` among those four. There is no
counterexample and therefore no lex-first miss.

The four scores are

| remaining bits `(wt1, opp2, adj2, vertex3, mixed3)` | `Q` | `cov9` | `cov9>0` |
|---|---:|---:|---:|
| `(0, 0, 0, 0, 0)` | 0 | 0 | 0 |
| `(0, 0, 0, 0, 1)` | 0 | 0 | 0 |
| `(0, 1, 0, 0, 0)` | 0 | 0 | 0 |
| `(0, 1, 0, 0, 1)` | 1 | 4 | 1 |

The unique Q6-false positive is `(0, 1, 0, 0, 1)`. That is exactly the
unique `Q`-true map on the subclass. Names the k=9 extra.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, is outside the four-map
set. Its membership in `F_cut` does not restore or break the four-map
identity.

## Theorem 2 — `N_pos`, `N_Q`, `N_both`

Among the 4 Q6-false maps:

- `N_pos = 1` map has `cov9 > 0`;
- `N_Q = 1` map satisfies `Q`;
- `N_both = 1` map satisfies both.

The counts agree with Theorem 1: `N_pos = N_Q = N_both = 1`.

## Theorem 3 — display; do not adopt a bit

`Q` is the remaining-bit predicate `(opp2=1) and (mixed3=1)` on the
Q6-false subclass. On this patch it equals 9-site positivity among those
four maps. Displayed, not adopted. Do not adopt a bit. Do not write `Q`
into Admissibility. Admissibility does not name this remaining-bit
formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| Q6-false as the four maps with `wt1=adj2=vertex3=0` | filtered from `F_cut` |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 nine-site seeds, off-patch `o=0` | declared finite patch |
| `Q` as `(opp2=1) and (mixed3=1)` | displayed, not adopted |
| `cov9>0` iff `Q` among the four | holds; no miss |
| unique positive `(0, 1, 0, 0, 1)` with `cov9 = 4` | proved by exhaustive scoring |
| `N_pos = 1`, `N_Q = 1`, `N_both = 1` | proved by exhaustive scoring |
| leftover-character of #6531 | refused; names the k=9 extra |
| leftover-character of the 32-map k=9 ranking | refused; new four-map object |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6531: that already named `Q6=cov6>0` as
`(wt1=1) or (adj2=1) or (vertex3=1)` on the 32-map class. The present
object is whether 9-site positivity equals `opp2 ∧ mixed3` on the four
Q6-false maps. Names the k=9 extra. New k-selector on a new subclass.

Not leftover-character of the 32-map k=9 ranking: that ranked all 32
maps by `cov9`. Echoing that ranking is not a substitute for the
four-map positivity-versus-`Q` identity.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 9-site positivity equals displayed `Q` inside the four Q6-false maps on this patch. |
| V2 | Current main has the axiom memo and the already named k=6 selector #6531, but no landed Q6-false 9-site positivity-versus-`opp2 ∧ mixed3` test. |
| V3 | The four maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared four-map subclass against a newly displayed two-bit AND. |
| V5 | Equivalence holds, the unique positive is named, and displayed `Q` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: displayed `Q` is not axiom content, and
no bit is adopted. The positive content is the four-map identity
`cov9>0` iff `Q`. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6531 | treat the test as leftover-character of already named `Q6=cov6>0` | **ATTEMPTED** |
| leftover of the 32-map k=9 ranking | treat four-map positivity as leftover-character of the 32-map census | **ATTEMPTED** |
| rename of mixed3 alone | identify `Q` with the standalone `mixed3` bit | **ATTEMPTED** |
| adopt a bit | write `opp2` or `mixed3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the already named k=6 selector, the 32-map k=9
ranking, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the Q6-false
filter `wt1=adj2=vertex3=0`, and displayed `Q` are declared. Equivalence
of `cov9>0` with `Q` is scored, not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
9-site positivity equals displayed `Q` on the four Q6-false maps, as a
new k=9 extra versus an already named k=6 selector, and not leftover-character of #6531.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all four Q6-false maps scored on 220 seeds | no physical law selection |
| per block | `N_pos`, `N_Q`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q` or `cov9>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** investment c9q6 already named `(0, 1, 0, 0, 1)` as the
unique Q6-false positive, so writing `opp2 ∧ mixed3` into Admissibility
is only naming that already unique map, and Hamming would have given the
same four-map identity.

**Answer:** the four-map identity is a k=9 occupancy-to-lock fact, not a
physical selector. Hamming is a different `F_cut` map and is not the
unbalanced-axis reading `n ≠ 0`. Displayed `Q` is not adopted. Do not
adopt a bit.

### N8 — cross-cycle echo

Investment #6531 already named `Q6=cov6>0` on the 32-map class.
Investment c9q6 already named the unique Q6-false positive
`(0, 1, 0, 0, 1)`. Echoing either fact is not a substitute for the
nine-site four-map count: the identity `cov9>0` iff `Q` and the triple
`(N_pos, N_Q, N_both) = (1, 1, 1)` are nine-site facts. Names the k=9
extra.

No-Go Discipline disposition: **PASS** for the finite comparison and the
four-map equivalence report. FAIL / DO NOT SHIP for “displayed `Q` is
the physical rule” or “adopt a bit.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, keeps the four
Q6-false maps with `wt1=adj2=vertex3=0`, scores `cov9` on the 220
nine-site seeds, compares positivity with displayed `Q`, reports that
the two are equivalent among those four, reports the unique positive
`(0, 1, 0, 0, 1)` with `cov9 = 4`, and reports `N_pos = 1`,
`N_Q = 1`, and `N_both = 1`. Declared audit inputs are this note and
the axiom memo; the runner writes no cache and authors no audit verdict.
