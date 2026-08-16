---
claim_id: f_cut_q4_false_four_site_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first refused neighborhood of the lex-first Q4-false F_cut map on the lex-first 4-site seed f1 fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_four_site_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse Of A Q4-False Map On A Four-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution on the twelve-vertex two-cube
with off-patch occupancy `0`. The lex-first Q4-false `F_cut` map is run
from the lex-first 4-site seed that `f1` fills. The first remaining-bit
neighborhood that map refuses is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_four_site_first_refuse_2026_08_15.py`](../scripts/f_cut_q4_false_four_site_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6518 recorded that among the 32 `F_cut` maps,
`cov4(f)>0` if and only if `Q4(f) := (wt1=1) or (adj2=1)`. Q4-false maps
therefore have `wt1=0`, `adj2=0`, and `cov4=0`. That leftover names the
coverage predicate. This note names the first remaining-bit neighborhood
a lex-first Q4-false map refuses on a 4-site seed that `f1` fills.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the `F_cut` map with remaining-bit tuple `(1, 1, 1, 1, 1)`.
Write `f_q0` for the lex-first remaining-bit map with `wt1=0` and
`adj2=0`, namely `(0, 0, 0, 0, 0)`. Write `Q4(f)` for the predicate
`(wt1=1) or (adj2=1)`. Then `Q4(f_q0)=0`.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. `f_q0` is named. `Q4(f_q0)=0` and `cov4(f_q0)=0`. The
  lex-first 4-site seed `S = {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}` is
  filled by `f1`.
- Theorem 2. The first remaining-bit refuse of `f_q0` from `S` is
  `t = 1`, site `(1, 0, 0)`, remaining-bit type `wt1` `= (1, 0, 2)`,
  neighborhood `(0, 1, 0, 0, 0, 0)`. `N_refuse = 4`, not `0`.
- Theorem 3. That refuse is displayed. Do not adopt Q4.

Do not write Q4 into Admissibility. The first remaining-bit refuse is a
displayed census output, not a selected occupancy law.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first Q4-false F_cut map is named, Q4 and cov4 are reconfirmed to vanish, f1 fills the lex-first 4-site seed, and the first remaining-bit refuse is enumerated. Q4 is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_four_site_first_refuse
target_blocker_text: "the first remaining-bit neighborhood a lex-first Q4-false map refuses on a 4-site seed f1 fills remains unnamed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first remaining-bit refuse; do not adopt Q4"
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

**Target.** Name the lex-first Q4-false `F_cut` map, reconfirm that it has
`Q4=0` and `cov4=0`, confirm that `f1` fills the lex-first 4-site seed,
and report the first remaining-bit neighborhood that map refuses from
that seed.

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
rule from `L_0 = S` reaches `L = T` in at most 13 ticks. Coverage is

```text
cov4(f) = |{ S : |S|=4 and f fills from S }|.
```

There are `C(12,4)=495` unordered 4-site seeds. Tick `t = 1` is the first
evaluation on the seed occupancy. Sites are scanned in the two-cube order
`(x,y,z)` with `x` fastest in `{0,1,2}` then `y,z` in `{0,1}`. The first
remaining-bit refuse of `f` from a seed is the earliest tick and, at that
tick, the first unlocked site whose neighborhood is a remaining-bit type
and has `f=0`. If no such site exists, `N_refuse=0`.

Define

```text
Q4(f)  = 1  iff  wt1(f)=1 or adj2(f)=1,
f1     = remaining-value of (1, 1, 1, 1, 1),
f_q0   = remaining-value of (0, 0, 0, 0, 0).
```

`f_q0` is the lex-first remaining-bit map with `wt1=0` and `adj2=0`.

## Theorems

### Theorem 1 — name `f_q0`; Q4 and coverage vanish; `f1` fills `S`

`f_q0` is the `F_cut` map with remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 0, 0, 0)`. Then
`Q4(f_q0)=0` because both `wt1` and `adj2` are 0. Exhaustive fill
census of all 495 four-site seeds gives `cov4(f_q0)=0`.

`f1` has remaining-bit tuple `(1, 1, 1, 1, 1)`. The lex-first 4-site
seed in two-cube combination order is

```text
S = {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}.
```

`f1` fills `S` with lock-count history `(4, 8, 12)`. `f_L1` also fills
`S` with the same history; that is a contrast, not an adopted selector.
`f_L1` is not Hamming parity.

### Theorem 2 — first remaining-bit refuse, or `N_refuse=0`

From `S`, `f_q0` never adds a site: the lock-count history is `(4)`.
The first remaining-bit refuse is

```text
t = 1
x = (1, 0, 0)
remaining-bit type = wt1 = (1, 0, 2)
neighborhood = (0, 1, 0, 0, 0, 0)
```

The four mid-layer sites `(1,y,z)` all see the same `wt1` neighborhood
and are refused together. The four far-layer sites `(2,y,z)` see empty,
which is not a remaining-bit type. So `N_refuse = 4`, not `0`.

`f1` fires that same `wt1` neighborhood. The refuse is the Q4-false
bit `wt1=0` on the first remaining-bit type that appears from `S`.

### Theorem 3 — display; do not adopt Q4

The first remaining-bit refuse is `wt1`. That is the mechanism of Q4
on this seed class: a Q4-false map has `wt1=0` and `adj2=0`, so it
refuses the first remaining-bit neighborhood that appears from the
lex-first 4-site seed `f1` fills. Display. Do not adopt Q4.
Do not write it into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| `f1` remaining bits `(1, 1, 1, 1, 1)` | defined; displayed, not adopted |
| `f_q0` remaining bits `(0, 0, 0, 0, 0)` | named as lex-first Q4-false map |
| `Q4(f_q0)=0` and `cov4(f_q0)=0` | proved by bits and 495-seed census |
| two-cube, 495 four-site seeds, off-patch 0 | declared finite patch |
| `f1` fills `S` | proved by evolution; history `(4, 8, 12)` |
| first remaining-bit refuse `wt1` at `t=1`, `(1,0,0)` | proved by seed-occupancy scan |
| `N_refuse = 4`, not `0` | four mid-layer `wt1` refuses |
| leftover-character of #6518 | refused; new object is the refuse |
| physical Admissibility selector / adopted Q4 | open; displayed, not adopted |

## Boundary and imports

Not leftover-character of #6518: that recorded `cov4>0` iff Q4. The
present object is the first remaining-bit neighborhood `f_q0` refuses
from the lex-first 4-site seed `f1` fills.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write Q4 into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of a Q4-false map on a 4-site seed `f1` fills. |
| V2 | Current main has the Q4 coverage predicate (#6518) but no landed first-refuse mechanism for a Q4-false map. |
| V3 | The 32 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: Q4 is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: the lex-first Q4-false map refuses a
`wt1` neighborhood on the lex-first 4-site seed `f1` fills, so Q4 is
not adopted as an Admissibility selector. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6518 | treat the refuse as leftover-character of `cov4>0` iff Q4 | **ATTEMPTED** |
| name `f_q0` | take a non-lex-first Q4-false remaining-bit tuple | **ATTEMPTED** |
| first remaining-bit refuse | name the first remaining-bit `(t, x, type)` from `S` | **ATTEMPTED** |
| `N_refuse=0` | claim no remaining-bit refuse occurs | **ATTEMPTED** |
| adopt Q4 | write Q4 into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The failed Hamming identification, the leftover #6518 coverage
predicate, and the off-patch convention are distinct. This note claims
no complete wall collection. The first remaining-bit refuse and
`N_refuse=4` are two certificates of the same `wt1` refusal, so they
collapse rather than count as two walls.

### N3 — hidden-condition scan

The two-cube, the 495 four-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
lex-first Q4-false map are declared. Unique selection of Q4 is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of `f_q0` from `S`, not leftover-character of #6518.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_q0` and `f1` scored from `S`; `cov4(f_q0)` on 495 seeds | no physical law selection |
| per block | first remaining-bit refuse named by tick, site, and type | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than Q4, and any independently derived physical map from
`F_cut` into Admissibility. The primitive registry was checked: the only
dependency used is `minimal_axioms`. No approved primitive supplies these
Boolean occupancy maps.

### N7 — hostile steelman

**Steelman:** Q4-false already means `wt1=0` and `adj2=0`, so refusing
`wt1` from `S` is leftover-character of #6518.

**Answer:** #6518 names the coverage predicate `cov4>0` iff Q4. The new
object is the first remaining-bit `(tick, site, type)` on the lex-first
4-site seed `f1` fills. Displaying `wt1` names that mechanism. Q4 is
not adopted.

### N8 — cross-cycle echo

Nearby occupancy and covariance surfaces use the same two-cube and
`F_cut` remaining bits. They do not name the first remaining-bit refuse
of a Q4-false map from a 4-site seed `f1` fills. Echoing the coverage
predicate is not a substitute for this refuse.

No-Go Discipline disposition: **PASS** for the named `f_q0`, the
vanishing of Q4 and `cov4`, the `f1` fill of `S`, and the displayed
first remaining-bit refuse. FAIL / DO NOT SHIP for “Q4 is the physical
rule” or “the displayed refuse is written into Admissibility.”

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

The companion runner names `f_q0` as remaining bits `(0, 0, 0, 0, 0)`,
reconfirms `Q4(f_q0)=0` and `cov4(f_q0)=0`, checks that `f1` fills the
lex-first 4-site seed `S`, names the first remaining-bit refuse by tick,
site, and remaining-bit type, reports `N_refuse = 4`, and does not adopt
Q4. Declared audit inputs are this note and the axiom memo; the runner
writes no cache and authors no audit verdict.
