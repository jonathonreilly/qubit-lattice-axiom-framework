---
claim_id: f_cut_q4_false_class_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether every Q4-false F_cut map first refuses remaining-bit type wt1 from the lex-first 4-site seed f1 fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_class_refuse_2026_08_15.py
---

# Q4-False Class First Remaining-Bit Refuse On A Four-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution on the twelve-vertex two-cube
with off-patch occupancy `0`. Each of the eight Q4-false `F_cut` maps is
run from the lex-first 4-site seed that `f1` fills. The first remaining-bit
refuse type of each map, or `N_refuse=0`, is reported. Whether every such
first refuse is type `wt1` is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_class_refuse_2026_08_15.py`](../scripts/f_cut_q4_false_class_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6529 asks whether the first remaining-bit refuse of the
lex-first Q4-false map `f_q0=(0,0,0,0,0)` on the lex-first 4-site seed
`f1` fills is a class fact for all eight Q4-false maps (`wt1=0` and
`adj2=0`), or whether a lex-first counterexample exists. Not leftover-character
of the single-map first refuse of `f_q0`. Not a remaining-bit search at
k=6/8.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the `F_cut` map with remaining-bit tuple `(1, 1, 1, 1, 1)`.
Write `Q4(f)` for the predicate `(wt1=1) or (adj2=1)`. Q4-false maps are
the eight remaining-bit tuples with `wt1=0` and `adj2=0`.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. For each of the eight Q4-false maps, the first remaining-bit
  refuse from
  `S = {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}`
  is type `wt1` `= (1, 0, 2)` at `t = 1`, site `(1, 0, 0)`, neighborhood
  `(0, 1, 0, 0, 0, 0)`, with `N_refuse = 4`, not `0`.
- Theorem 2. Every Q4-false first refuse is type `wt1`. There is no
  lex-first counterexample tuple.
- Theorem 3. That class fact is displayed. Do not adopt Q4.

Do not write Q4 into Admissibility. The class first-refuse type is a
displayed census output, not a selected occupancy law.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each of the eight Q4-false F_cut maps is scored from the lex-first 4-site seed f1 fills. Every first remaining-bit refuse is type wt1. Q4 is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_class_refuse
target_blocker_text: "whether the wt1 first refuse of f_q0 on the lex-first 4-site f1 fill is unique for the eight Q4-false maps remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed Q4-false class first-refuse types; do not adopt Q4"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3` with nearest-neighbor adjacency and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule, covariant
under those motions. Record supplies permanence of a lock and unreadability
of an absent record. Admissibility does not supply the formation site,
probability, or rate. Qubit is unused beyond the ambient one-site algebra
boundary: the maps here are Boolean occupancy predicates, not `M_2(C)`-valued
laws.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the five remaining bits in the order `(wt1, opp2, adj2, vertex3, mixed3)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** For each of the eight Q4-false `F_cut` maps, name the first
remaining-bit refuse type from the lex-first 4-site seed `f1` fills, or
report `N_refuse=0`. Then report whether every such first refuse is type
`wt1`, or name the lex-first counterexample tuple and its first refuse
type.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

A remaining-bit neighborhood is a six-neighbor occupancy whose axis type
is one of those five remaining orbits or the complement of one of them.
Empty and full are not remaining-bit types.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

There are `C(12,4)=495` unordered 4-site seeds. Tick `t = 1` is the first
evaluation on the seed occupancy. Sites are scanned in the two-cube order
`(x,y,z)` with `x` fastest in `{0,1,2}` then `y,z` in `{0,1}`. The first
remaining-bit refuse of `f` from a seed is the earliest tick and, at that
tick, the first unlocked site whose neighborhood is a remaining-bit type
and has `f=0`. If no such site exists, `N_refuse=0`.

Define

```text
Q4(f)     = 1  iff  wt1(f)=1 or adj2(f)=1,
Q4-false  = { f in F_cut : wt1(f)=0 and adj2(f)=0 },
f1        = remaining-value of (1, 1, 1, 1, 1),
f_q0      = remaining-value of (0, 0, 0, 0, 0).
```

The eight Q4-false remaining-bit tuples, in lex order, are

```text
(0, 0, 0, 0, 0)
(0, 0, 0, 0, 1)
(0, 0, 0, 1, 0)
(0, 0, 0, 1, 1)
(0, 1, 0, 0, 0)
(0, 1, 0, 0, 1)
(0, 1, 0, 1, 0)
(0, 1, 0, 1, 1).
```

`f_q0` is the lex-first member.

## Theorems

### Theorem 1 — first refuse type of each Q4-false map from `S`

`f1` has remaining-bit tuple `(1, 1, 1, 1, 1)`. The lex-first 4-site
seed in two-cube combination order is

```text
S = {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}.
```

`f1` fills `S` with lock-count history `(4, 8, 12)`. `f_L1` also fills
`S` with the same history; that is a contrast, not an adopted selector.
`f_L1` is not Hamming parity.

For each of the eight Q4-false maps, the first remaining-bit refuse from
`S` is

```text
t = 1
x = (1, 0, 0)
remaining-bit type = wt1 = (1, 0, 2)
neighborhood = (0, 1, 0, 0, 0, 0)
N_refuse = 4
```

No member has `N_refuse=0`. None of the eight maps adds a site from `S`:
every lock-count history is `(4)`.

The four mid-layer sites `(1,y,z)` all see the same `wt1` neighborhood
and are refused together. The four far-layer sites `(2,y,z)` see empty,
which is not a remaining-bit type. Because every Q4-false map has
`wt1=0`, the first remaining-bit type that appears from `S` is refused
by the whole class.

### Theorem 2 — every first refuse is type `wt1`, or a counterexample

Every Q4-false first refuse is type `wt1`. There is no lex-first
counterexample tuple: scanning the eight maps in lex order, no member
has `N_refuse=0` and no member first-refuses a remaining-bit type other
than `wt1`.

The free bits `opp2`, `vertex3`, and `mixed3` do not change the first
refuse from `S`. Those types do not appear among the seed neighborhoods
of unlocked sites.

### Theorem 3 — display; do not adopt Q4

The class first-refuse type is `wt1`. That is a uniqueness statement for
the eight Q4-false maps on this seed: the single-map refuse of `f_q0` is
the class refuse. Display. Do not adopt Q4.
Do not write it into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| `f1` remaining bits `(1, 1, 1, 1, 1)` | defined; displayed, not adopted |
| eight Q4-false remaining-bit tuples | named; lex-first is `f_q0` |
| two-cube, 495 four-site seeds, off-patch 0 | declared finite patch |
| `f1` fills `S` | proved by evolution; history `(4, 8, 12)` |
| first remaining-bit refuse of each of the eight | type `wt1` at `t=1`, `(1,0,0)` |
| `N_refuse = 4`, not `0`, for each of the eight | four mid-layer `wt1` refuses |
| no lex-first counterexample | proved by the eight-row census |
| leftover-character of the single-map refuse | refused; new object is the class |
| remaining-bit search at k=6/8 | refused; this is the 4-site class |
| physical Admissibility selector / adopted Q4 | open; displayed, not adopted |

## Boundary and imports

Not leftover-character of the single-map first refuse of `f_q0=(0,0,0,0,0)`
on `S`. That names one row. The present object is uniqueness of the first
remaining-bit refuse type for the whole Q4-false class.

Not a remaining-bit search at k=6/8. The seed here is the lex-first
4-site fill of `f1`. Coverage at six or eight sites is a different census.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write Q4 into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It reports whether every Q4-false map first-refuses type `wt1` from the 4-site seed `f1` fills. |
| V2 | The single-map refuse of `f_q0` is named; class uniqueness on that seed is not. |
| V3 | The 32 maps, the eight Q4-false tuples, and occupancy-to-lock from `S` are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: Q4 is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: every Q4-false map refuses a `wt1`
neighborhood on the lex-first 4-site seed `f1` fills, so Q4 is not
adopted as an Admissibility selector. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover single-map refuse | treat the class as leftover-character of the `f_q0` refuse | **ATTEMPTED** |
| remaining-bit search at k=6/8 | replace the 4-site seed by a six- or eight-site search | **ATTEMPTED** |
| first remaining-bit refuse of each of the eight | name each first remaining-bit type from `S`, or `N_refuse=0` | **ATTEMPTED** |
| lex-first counterexample | find a Q4-false tuple whose first refuse is not `wt1` | **ATTEMPTED** |
| adopt Q4 | write Q4 into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The failed Hamming identification, the leftover single-map refuse, and
the k=6/8 remaining-bit search are distinct. This note claims no complete
wall collection. The eight identical `wt1` first refuses are eight rows
of one class certificate, so they collapse rather than count as eight
walls.

### N3 — hidden-condition scan

The two-cube, the 495 four-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the eight
Q4-false maps are declared. Unique selection of Q4 is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is uniqueness of the first
remaining-bit refuse type for the Q4-false class from `S`, not leftover-character
of the single-map refuse and not a remaining-bit search at k=6/8.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all eight Q4-false maps scored from `S` | no physical law selection |
| per block | each first remaining-bit refuse type named | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than Q4, and any independently derived physical map from
`F_cut` into Admissibility. The primitive registry was checked: the only
dependency used is `minimal_axioms`. No approved primitive supplies these
Boolean occupancy maps.

### N7 — hostile steelman

**Steelman:** every Q4-false map has `wt1=0`, so refusing `wt1` from `S`
is leftover-character of the single-map refuse of `f_q0`.

**Answer:** the single-map refuse names one remaining-bit tuple. The new
object is the eight-row census: whether any free-bit combination
(`opp2`, `vertex3`, `mixed3`) changes the first refuse type, or whether
`N_refuse=0` for some member. Displaying that every first refuse is
`wt1` names that class fact. Q4 is not adopted.

### N8 — cross-cycle echo

Nearby occupancy and covariance surfaces use the same two-cube and
`F_cut` remaining bits. They do not name the first remaining-bit refuse
type of every Q4-false map from a 4-site seed `f1` fills. Echoing the
single-map refuse or a k=6/8 remaining-bit search is not a substitute
for this class census.

No-Go Discipline disposition: **PASS** for the eight named Q4-false
maps, the `f1` fill of `S`, the displayed first remaining-bit refuse
types, and the absence of a lex-first counterexample. FAIL / DO NOT SHIP
for “Q4 is the physical rule” or “the displayed refuse is written into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

## Runner contract

The companion runner enumerates the eight Q4-false remaining-bit maps,
checks that `f1` fills the lex-first 4-site seed `S`, names the first
remaining-bit refuse type of each map from `S` or reports `N_refuse=0`,
checks that every first refuse is type `wt1` with no lex-first
counterexample, and does not adopt Q4. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.
