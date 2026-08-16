---
claim_id: f_cut_cov6_zero_class_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether every Q4-false vertex3=0 F_cut map first refuses remaining-bit type adj2 from the lex-first 6-site seed f1 fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov6_zero_class_refuse_2026_08_15.py
---

# Whether Every `cov6=0` Q4-False `vertex3=0` Map First-Refuses `adj2`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock remaining-bit refuse of the four
Q4-false `vertex3=0` `F_cut` maps on the lex-first six-site seed that
`f1` fills, on the twelve-vertex two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov6_zero_class_refuse_2026_08_15.py`](../scripts/f_cut_cov6_zero_class_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment q6zero named the first remaining-bit refuse of the lex-first
`cov6=0` map `f_z=(0,0,0,0,0)` on the lex-first 6-site seed that `f1`
fills: tick `1`, site `(1, 1, 0)`, type `adj2`. The four Q4-false maps
with `vertex3=0` all have `cov6=0`. Those four remaining-bit tuples are
`(0, 0, 0, 0, 0)`, `(0, 0, 0, 0, 1)`, `(0, 1, 0, 0, 0)`, and
`(0, 1, 0, 0, 1)`. This note asks whether that first refuse is a class
fact: whether every one of those four first refuses remaining-bit type
`adj2` on that same seed, or whether a lex-first counterexample exists.
Not leftover-character of the single-map first refuse of `f_z=(0,0,0,0,0)`.
The new object is the four-row census. Mechanism of the `cov6` zeros.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

Write `f1` for remaining bits `(1, 1, 1, 1, 1)` and `f_z` for remaining
bits `(0, 0, 0, 0, 0)`. Q4-false means `wt1=0` and `adj2=0`. The four
maps above are exactly the Q4-false maps with `vertex3=0`.

On the two-cube with off-patch occupancy `0`, a remaining-bit refuse of a
map `f` from a locked set `L` is an unlocked on-patch site whose
six-neighbor occupancy has a remaining-bit orbit type and `f=0` on that
neighborhood. Empty and full are forced bits, not remaining bits. Then:

- Theorem 1. For each of the four, the first remaining-bit refuse from
  `S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}`
  is type `adj2` `= (2, 0, 1)` at tick `1`, site `(1, 1, 0)`, with
  `N_refuse = 4`, not `0`.
- Theorem 2. Every first refuse is type `adj2`. There is no lex-first
  counterexample tuple.
- Theorem 3. That class fact is displayed. Displayed, not adopted.

Do not adopt a bit. Do not write `adj2` into Admissibility.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block is a different rule and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each of the four Q4-false vertex3=0 F_cut maps is scored from the lex-first 6-site seed f1 fills. Every first remaining-bit refuse is type adj2. The refuse is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_cov6_zero_class_refuse
target_blocker_text: "whether the adj2 first refuse of f_z on the lex-first 6-site f1 fill is unique for the four Q4-false vertex3=0 maps remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed cov6=0 class first-refuse types; do not adopt a remaining bit"
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
predicate. The remaining-bit type `adj2` is a displayed refuse label, not
axiom content.

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

The map `f1` is the remaining-bit assignment that sends every remaining
orbit to `1`. The map `f_z` sends every remaining orbit to `0`. Because
empty and full are already `0`, `f_z` is the zero map on `{0,1}^6`.

A locked set `L` determines occupancies: a lattice neighbor in `L` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `L` by

```text
L ∪ { v in two-cube \ L : f(neighborhood_6(v; L)) = 1 }.
```

Tick `1` is the first such step from the seed. Fill means the halt set has
cardinality 12. There are `C(12,6)=924` unordered 6-site seeds. Seeds are
ordered by the lex order of the twelve vertices
`(x,y,z)` with `x` slowest and `z` fastest, then by combination order.
Coverage `cov6(f)` is the number of those 924 seeds from which `f` fills.

A remaining-bit refuse of `f` at locked set `L` is an unlocked on-patch
site `v` whose neighborhood axis-type is a remaining-bit orbit (or that
orbit's complement) and `f(neighborhood_6(v; L))=0`. The first remaining-bit
refuse from a seed is the lex-first such site on the earliest tick that has
any. If no such site exists, `N_refuse=0`. `N_refuse` on a tick that has
refuses is the number of remaining-bit refuses at the locked set just
before that tick.

Define

```text
Q4(f)            = 1  iff  wt1(f)=1 or adj2(f)=1,
Q4-false         = { f in F_cut : wt1(f)=0 and adj2(f)=0 },
cov6=0 class     = { f in Q4-false : vertex3(f)=0 },
f1               = remaining-value of (1, 1, 1, 1, 1),
f_z              = remaining-value of (0, 0, 0, 0, 0).
```

The four class remaining-bit tuples, in lex order, are

```text
(0, 0, 0, 0, 0)
(0, 0, 0, 0, 1)
(0, 1, 0, 0, 0)
(0, 1, 0, 0, 1).
```

`f_z` is the lex-first member.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and is not Hamming parity. The map
`f1` has remaining bits `(1, 1, 1, 1, 1)` and fills the lex-first 6-site
seed

```text
S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}.
```

The map `f1` fills `S`. Each of the four Q4-false `vertex3=0` maps has
`cov6=0` and does not fill `S`. From `S` at tick `1`, the unlocked sites
and neighborhood types are

```text
(1, 1, 0)  adj2     (2, 0, 1)   neighborhood (0, 1, 0, 1, 0, 0)
(1, 1, 1)  adj2     (2, 0, 1)   neighborhood (0, 1, 0, 1, 0, 0)
(2, 0, 0)  wt1      (1, 0, 2)   neighborhood (0, 1, 0, 0, 0, 0)
(2, 0, 1)  wt1      (1, 0, 2)   neighborhood (0, 1, 0, 0, 0, 0)
(2, 1, 0)  empty    (0, 0, 3)
(2, 1, 1)  empty    (0, 0, 3)
```

Empty is not a remaining-bit type. Every class map has `wt1=0` and
`adj2=0`, so each refuses the four remaining-bit neighborhoods. For each
of the four, the first remaining-bit refuse from `S` is therefore tick
`1`, site `(1, 1, 0)`, remaining-bit type `adj2`, with `N_refuse = 4`.

**Theorem 2.** Every first refuse is type `adj2`. There is no lex-first
counterexample tuple: scanning the four maps in lex order, no member has
`N_refuse=0` and no member first-refuses a remaining-bit type other than
`adj2`.

The free bits `opp2` and `mixed3` do not change the first refuse from
`S`. Those types do not appear among the seed neighborhoods of unlocked
sites. Because `vertex3=0` is already the class cut, it is not a free
bit inside the class.

**Theorem 3.** The class first-refuse type is `adj2`. That is a uniqueness
statement for the four Q4-false `vertex3=0` maps on this seed: the
single-map refuse of `f_z` is the class refuse. The refuse is displayed.
No remaining bit is adopted as the physical Admissibility rule.
Displayed, not adopted.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free |
| `f1` fills `S` | remaining bits `(1, 1, 1, 1, 1)` fill the lex-first 6-site seed |
| four class maps | Q4-false and `vertex3=0`; lex-first is `f_z` |
| `cov6=0` | each of the four fills none of the 924 six-site seeds |
| first refuse of each of the four | tick `1`, site `(1, 1, 0)`, type `adj2` |
| `N_refuse` | `4` remaining-bit refuses on that tick, for each of the four |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` |
| no lex-first counterexample | proved by the four-row census |
| displayed refuse | not adopted |

## What this does not claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the other 28 maps in `F_cut`.
- No adoption of `adj2`, `wt1`, or `f_z`.
- No blank-block or Hamming-as-`f_L1` identification.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It reports whether every Q4-false `vertex3=0` map first-refuses type `adj2` from the 6-site seed `f1` fills. |
| V2 | The single-map refuse of `f_z` is named; class uniqueness on that seed is not. |
| V3 | The 32 maps, the four class tuples, the 924 seeds, and occupancy-to-lock from `S` are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: the refuse is displayed and is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: every Q4-false `vertex3=0` map refuses an
`adj2` neighborhood on the lex-first 6-site seed `f1` fills, so `adj2` is
not adopted as an Admissibility selector. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover single-map refuse | treat the class as leftover-character of the `f_z` refuse | **ATTEMPTED** |
| leftover of `cov6=0` | treat the refuse type as leftover-character of the coverage zeros | **ATTEMPTED** |
| first remaining-bit refuse of each of the four | name each first remaining-bit type from `S`, or `N_refuse=0` | **ATTEMPTED** |
| lex-first counterexample | find a class tuple whose first refuse is not `adj2` | **ATTEMPTED** |
| adopt a bit | write `adj2` or `f_z` into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The failed Hamming identification, the leftover single-map refuse, and
the leftover coverage-zero class are distinct. This note claims no complete
wall collection. The four identical `adj2` first refuses are four rows
of one class certificate, so they collapse rather than count as four
walls.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the four
Q4-false `vertex3=0` maps are declared. Unique selection of `adj2` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is uniqueness of the first
remaining-bit refuse type for the `cov6=0` Q4-false `vertex3=0` class from
`S`, not leftover-character of the single-map refuse of `f_z`, and not a
Hamming identification.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all four Q4-false `vertex3=0` maps scored from `S` | no physical law selection |
| per block | each first remaining-bit refuse type named | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, the
other four Q4-false maps with `vertex3=1`, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** every class map has `adj2=0`, so refusing `adj2` from `S`
is leftover-character of the single-map refuse of `f_z`.

**Answer:** the single-map refuse names one remaining-bit tuple. The new
object is the four-row census: whether the free bits `opp2` and `mixed3`
change the first refuse type, or whether `N_refuse=0` for some member.
Displaying that every first refuse is `adj2` names that class fact.
`adj2` is not adopted.

### N8 — cross-cycle echo

Investment q6zero already named the first remaining-bit refuse of `f_z`
on this seed. Echoing that single row is not a substitute for the first
remaining-bit refuse type of every Q4-false `vertex3=0` map from the
lex-first 6-site `f1` fill.

No-Go Discipline disposition: **PASS** for the four named class maps, the
`f1` fill of `S`, the displayed first remaining-bit refuse types, and the
absence of a lex-first counterexample. FAIL / DO NOT SHIP for “`adj2` is
the physical rule” or “displayed `f_z` is adopted.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
`F_cut`, names the four Q4-false `vertex3=0` maps, names the lex-first
6-site seed that `f1` fills, evaluates the first remaining-bit refuse of
each map from that seed or reports `N_refuse=0`, checks that every first
refuse is type `adj2` with no lex-first counterexample, and does not adopt
a bit. Declared audit inputs are this note and the axiom memo; the runner
writes no cache and authors no audit verdict.
