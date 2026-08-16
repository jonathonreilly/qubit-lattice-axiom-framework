---
claim_id: f_cut_qstar_cov9_max_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with off-patch o=0, whether maximal cov9 equals vertex3=mixed3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov9_max_selector_2026_08_15.py
---

# Whether Maximal `cov9` Among `Q_*` Equals Displayed `vertex3 ∧ mixed3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 9-site coverage of the eight
cube-covariant cut maps in `Q_*` — the `F_cut` subclass with `wt1=1`
and `adj2=1` — on the twelve-vertex two-cube with off-patch occupancy
`0`, over all 220 unordered 9-site seeds, and whether maximal `cov9`
among those eight equals the displayed conjunction `vertex3=1` and
`mixed3=1`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov9_max_selector_2026_08_15.py`](../scripts/f_cut_qstar_cov9_max_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment: among `Q_*`, tot3/5/7/10 iff `vertex3 ∧ mixed3`. Max(4/6/8)
is unique `f1`. Test whether maximal `cov9` iff that same cut among the
eight. New odd k. `f_L1` is `n ≠ 0`, not Hamming.

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
forced to `0`. Write `Q_*` for the eight maps with `wt1=1` and `adj2=1`.
Those eight remaining-bit tuples, in remaining-bit lex order, are

```text
(1, 0, 1, 0, 0), (1, 0, 1, 0, 1), (1, 0, 1, 1, 0), (1, 0, 1, 1, 1),
(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

Not leftover-character of tot3, tot5, tot7, or tot10: those closed
totality at other odd seed sizes as the same displayed cut. Not
leftover-character of Max(4/6/8): those even-k maximizers were unique
`f1`. The present object is maximal `cov9` among the same eight maps.
New odd k inside `Q_*`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 9-set of vertices is
a 9-site seed. There are `C(12,9)=220` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. The process
is synchronous and stops at a fixed point in at most 13 ticks. Fill means
`|locks_halt|=12`. Coverage is

```text
cov9(f) = |{ S : |S|=9 and f fills from S }|.
```

Write `m9` for the maximum of `cov9` among the eight. Duality is not
assumed: `cov9` is scored on the 220 nine-site seeds and does not import
`Max(k)=Max(12-k)` or the three-site census. Off-patch occupancy `0` is
an explicit default. A blank-block is a different rule and is not used.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`,
which sits in `Q_*`. Displayed `Q` is

```text
Q(f) := (vertex3=1) and (mixed3=1).
```

That cut holds on exactly two of the eight: `(1, 0, 1, 1, 1)` and
`(1, 1, 1, 1, 1)`.

**Theorem 1.** Among the eight `Q_*` maps, maximal `cov9` is equivalent
to `vertex3=1` and `mixed3=1`. Exhaustive evaluation on all 220
nine-site seeds, in remaining-bit lex order, gives

```text
cov9((1, 0, 1, 0, 0)) = 68
cov9((1, 0, 1, 0, 1)) = 72
cov9((1, 0, 1, 1, 0)) = 200
cov9((1, 0, 1, 1, 1)) = 220
cov9((1, 1, 1, 0, 0)) = 72
cov9((1, 1, 1, 0, 1)) = 72
cov9((1, 1, 1, 1, 0)) = 204
cov9((1, 1, 1, 1, 1)) = 220
```

So `m9 = 220 = C(12,9)`. The two maximizers are exactly the two `Q`
maps. The identity holds.

**Theorem 2.** The three census integers on the eight-map set are

```text
N_max = 2
N_Q = 2
N_both = 2
```

Because those three counts agree and the maximizers are exactly the `Q`
maps, there is no lex-first miss. In particular `f_L1 = (1, 0, 1, 1, 1)`
attains `cov9 = 220` and satisfies `Q`.

**Theorem 3.** The identity is displayed only. Displayed, not adopted.
Do not adopt a bit. Do not write Q into Admissibility. Admissibility does
not name this remaining-bit formula.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q_* maps are scored exactly on the 220 nine-site seeds. Whether maximal cov9 equals vertex3=mixed3=1 is a finite Boolean identity on this patch. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov9_max_selector
target_blocker_text: "whether maximal cov9 among the eight Q_* maps equals vertex3=mixed3=1 after tot3/5/7/10 already named that cut and Max(4/6/8) was unique f1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Max(9) versus Q identity; do not adopt a bit"
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
predicate. The two remaining bits below are displayed remaining-bit
data, not axiom content.

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
on orbit types `(1, 0, 2)`, `(0, 1, 2)`, `(2, 0, 1)`, `(3, 0, 0)`, `(1, 1, 1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

| remaining name | `(u,b,e)` | orbit size | complement image |
|---|---|---:|---|
| empty | `(0,0,3)` | 1 | full |
| full | `(0,3,0)` | 1 | empty |
| `opp2` | `(0,1,2)` | 3 | `(0,2,1)` |
| `wt1` | `(1,0,2)` | 6 | `(1,2,0)` |
| `adj2` | `(2,0,1)` | 12 | `(2,1,0)` |
| `mixed3` | `(1,1,1)` | 12 | itself |
| `vertex3` | `(3,0,0)` | 8 | itself |

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has three free bits
(`opp2`, `vertex3`, `mixed3`) and size 8.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`.
Then `cov9(f)` is the number of those subsets from which `f` fills.
Duality is not assumed: `cov9` is scored on those 220 seeds.

`Q` is the remaining-bit predicate

```text
Q(f) := (vertex3=1) and (mixed3=1).
```

It holds on exactly two of the eight maps. Displayed, not adopted.

## Theorem 1 — maximal `cov9` versus `Q` on the eight

Direct evolution on the 220 nine-site seeds scores every `Q_*` map.
The identity

```text
cov9(f) = m9  ⇔  Q(f) = 1
```

holds among the eight, with `m9 = 220`. The eight-line census in
remaining-bit lex order is the table in the Result up front. The two
maps that attain 220 are `(1, 0, 1, 1, 1)` and `(1, 1, 1, 1, 1)`. Those
are exactly the maps with `vertex3=mixed3=1`. The six maps with `Q=0`
have `cov9 ∈ {68, 72, 200, 204}`.

In particular `f_L1 = (1, 0, 1, 1, 1)` has `Q=1` and `cov9=220`. The
map `f1 = (1, 1, 1, 1, 1)` has the same pair. Unlike Max(4/6/8), the
odd-k maximum is not unique `f1`.

## Theorem 2 — the three census integers

Write `N_max` for the number of `Q_*` maps with `cov9 = m9`, `N_Q` for
the number with `Q=1`, and `N_both` for the number with both. Then

```text
N_max = 2
N_Q = 2
N_both = 2
```

These three integers are counted from the scored eight-map table. They
coincide because the identity of Theorem 1 holds. There is no lex-first
miss.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q` and has
`cov9 = 220`. That is consistent with Theorem 2.

## Theorem 3 — display, not adoption

The identity `Max(9) ⇔ Q` on the eight `Q_*` maps is displayed data.
Displayed, not adopted. Do not adopt a bit. Do not adopt `vertex3`. Do
not adopt `mixed3`. Do not adopt `f_L1`. Do not write Q into
Admissibility. Admissibility does not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as the eight maps with `wt1=1` and `adj2=1` | remaining-bit lex order |
| `Q` as `vertex3=1` and `mixed3=1` | two maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 nine-site seeds, off-patch `o=0` | declared finite patch |
| maximal `cov9` iff `Q` on those eight | holds; `m9=220` |
| `N_max`, `N_Q`, `N_both` | 2, 2, 2; no lex-first miss |
| leftover of tot3/5/7/10 | refused; those are other odd k |
| leftover of Max(4/6/8) | refused; those even maxima were unique `f1` |
| adoption of `Q` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot3, tot5, tot7, or tot10: those closed
totality at `k ∈ {3,5,7,10}` as `vertex3 ∧ mixed3`. The present object
is maximal `cov9` at new odd k.

Not leftover-character of Max(4/6/8): those even-k tests found a unique
maximizer `f1` and a `Q`-true miss at `f_L1`. Here both `Q` maps attain
the nine-site ceiling.

Duality is not assumed: `C(12,9)=C(12,3)=220`, but the nine-site scores
are not the three-site scores and are computed on the 220 nine-site seeds.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write Q into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether maximal `cov9` equals `Q` among the eight `Q_*` maps. |
| V2 | tot3/5/7/10 already named that cut at other odd seed sizes. Max(4/6/8) was unique `f1`. Current main has no landed focused Max(9) test inside `Q_*`. |
| V3 | The eight maps and 220 seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a named displayed 2-bit AND. |
| V5 | The identity holds, is displayed, and `Q` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The positive content is narrow: maximal `cov9` equals `Q` among the
eight `Q_*` maps on this patch. No global compiler necessity is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of tot3 | treat the nine-site test as leftover-character of tot3 | **ATTEMPTED** |
| leftover of tot5/7/10 | treat the test as leftover-character of those odd-k totals | **ATTEMPTED** |
| leftover of Max(4/6/8) | treat the test as leftover-character of the even-k unique-`f1` maxima | **ATTEMPTED** |
| adopt Q | write `Q` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the tot3/5/7/10 odd-k identities, the Max(4/6/8)
even-k unique-`f1` facts, and the off-patch convention are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the `Q_*`
cut `wt1=adj2=1`, and the two-bit AND `vertex3=1` and `mixed3=1` are
declared. Equality of `Q` with maximal `cov9` is not silently assumed.
Duality is not assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
maximal `cov9` equals `Q` on the eight `Q_*` maps, not leftover-character
of tot3 and not leftover-character of Max(4/6/8). New odd k.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight `Q_*` maps scored on 220 seeds | no physical law selection |
| per block | the Max(9)–`Q` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q`, and any independently derived physical map
from `F_cut` into Admissibility.

Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of
them supplies a Boolean occupancy map, a seed-coverage ranking, or an
Admissibility selector.

### N7 — hostile steelman

**Steelman:** tot3/5/7/10 already recorded that `Q` is totality at those
odd sizes, so the same 2-bit AND must also be the k=9 maximizer and
must be written into Admissibility; alternatively Max(4/6/8) already
showed unique `f1`, so Max(9) must be unique `f1` as well.

**Answer:** the nine-site census is independent. `N_max = 2`, `N_Q = 2`,
and `N_both = 2`. Both `Q` maps attain `cov9 = 220`. Max(9) is not
unique `f1`. Duality is not assumed. Do not adopt a bit.

### N8 — cross-cycle echo

Investment tot3/5/7/10 already showed that totality at those odd sizes
is `Q`. Investment Max(4/6/8) already showed unique `f1` at those even
sizes. Echoing either fact is not a substitute for testing maximal
`cov9` against named `Q` on the eight. New odd k.

No-Go Discipline disposition: **PASS** for the finite eight-map census
and the displayed identity. FAIL / DO NOT SHIP for
“adopt Q,” “`Q` is the physical rule,” or “write Q into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the eight `Q_*` maps, scores `cov9` on
the 220 nine-site seeds, decides whether maximal `cov9` if and only if
`Q`, reports the lex-first miss if the identity fails, and reports
`N_max`, `N_Q`, and `N_both`. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.
