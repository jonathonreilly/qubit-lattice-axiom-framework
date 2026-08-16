---
claim_id: f_cut_q8_extra_six_site_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (0,1,0,0,0) on the lex-first 6-site seed f1 fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q8_extra_six_site_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of the Lex-First Q8-True `cov6=0` Extra

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the twelve-vertex two-cube
with off-patch occupancy `0`, for the cube-covariant cut map whose
remaining-bit tuple is `(0, 1, 0, 0, 0)`. The lex-first 6-site seed that
`f1` fills, the first remaining-bit refuse of that extra from that seed,
and `N_refuse` on that first tick are reported.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q8_extra_six_site_first_refuse_2026_08_15.py`](../scripts/f_cut_q8_extra_six_site_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investments #6552 and #6555 name the Q8-true extras with `cov6=0`: the
remaining-bit tuples `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)`. This note
names the first remaining-bit refuse of the lex-first extra
`f_e = (0, 1, 0, 0, 0)` on the lex-first 6-site seed that `f1` fills. That
refuse is the mechanism of the extras on this seed: they are Q8-true only
through `opp2`, and the first remaining-bit demand they meet is not `opp2`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`: it fires on every
remaining-bit orbit. Q8 is the remaining-bit predicate
`wt1=1` or `adj2=1` or `opp2=1` or `vertex3=1`. Q6 is
`wt1=1` or `adj2=1` or `vertex3=1`. Both extras have `opp2=1` and
`wt1=adj2=vertex3=0`, so both are Q8-true and Q6-false.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. The lex-first 6-site seed that `f1` fills is
  `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1)}`. The first
  remaining-bit refuse of `f_e = (0, 1, 0, 0, 0)` from `S` is tick `0`,
  site `(1, 1, 0)`, remaining-bit type `adj2`.
- Theorem 2. On that first tick, `N_refuse = 4`.
- Theorem 3. The seed and the refuse are displayed only. Do not adopt a
  remaining bit. Do not write the refuse into Admissibility.

Displayed, not adopted.

Not leftover-character of #6552. Not leftover-character of #6555. Those
named the extras and scored `cov6=0`. The object here is the first
remaining-bit refuse.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first 6-site f1 fill and the first remaining-bit refuse of F_cut (0,1,0,0,0) from that seed are finite exact names on the two-cube. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q8_extra_six_site_first_refuse
target_blocker_text: "name the first remaining-bit refuse of the lex-first Q8-true cov6=0 extra on the lex-first 6-site seed f1 fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first remaining-bit refuse of the extra; do not adopt a displayed bit"
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
under those motions. Record is not used as a formation-site selector: the
dynamics here are a declared occupancy-to-lock predicate on a finite patch.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil
  `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Name the lex-first 6-site seed that `f1` fills and the first
remaining-bit refuse of `F_cut` `(0, 1, 0, 0, 0)` from that seed, together
with `N_refuse` on that first tick.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The 6-site seeds are the `924` unordered 6-subsets of `T`, listed in
lexicographic site order induced by
`(x,y,z)` with `x ∈ {0,1,2}`, `y ∈ {0,1}`, `z ∈ {0,1}`. Then `cov6(f)` is
the number of those seeds from which `f` fills.

A remaining-bit refuse of a map `f` from a seed `S` is an unlocked site
whose six-neighbor occupancy is a remaining-bit type (so `f1` returns 1)
on which `f` returns 0. The first such refuse is the least tick, then the
lexicographically first site at that tick. `N_refuse` is the number of
remaining-bit refuses on that first tick.

## Theorems

### Theorem 1 — seed `S` and the first remaining-bit refuse

The lex-first 6-site seed that `f1` fills is

```text
S = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1)}.
```

`f1` fills from `S`. The extra `f_e = (0, 1, 0, 0, 0)` does not fill from
`S`. The partner extra `(0, 1, 0, 0, 1)` also does not fill from `S`. Both
extras have `cov6 = 0` on the 924 six-site seeds.

From `S`, the six unlocked sites at tick `0` and their axis types are

```text
(1,1,0)  type (2,0,1)  adj2
(1,1,1)  type (2,0,1)  adj2
(2,0,0)  type (1,0,2)  wt1
(2,0,1)  type (1,0,2)  wt1
(2,1,0)  type (0,0,3)  empty
(2,1,1)  type (0,0,3)  empty
```

Empty is not a remaining-bit type. The remaining-bit demands are therefore
`adj2` and `wt1`. The extra `f_e` fires only on `opp2` (and, for the
partner, also on `mixed3`). It returns 0 on every remaining-bit demand
present at the seed. The first remaining-bit refuse of `f_e` from `S` is
therefore

- tick `0`,
- site `(1, 1, 0)`,
- remaining-bit type `adj2`.

That is the mechanism of the extras on this seed: Q8-true only through
`opp2`, first remaining-bit refuse of type `adj2`.

### Theorem 2 — `N_refuse` on the first tick

On that first tick the remaining-bit refuses are the four unlocked
remaining-bit sites

```text
(1,1,0) adj2
(1,1,1) adj2
(2,0,0) wt1
(2,0,1) wt1
```

so `N_refuse = 4`. The two empty sites at `x=2`, `y=1` are not remaining-bit
refuses.

### Theorem 3 — display; do not adopt a bit

The seed, the refuse `(tick, site, type) = (0, (1, 1, 0), adj2)`, and
`N_refuse = 4` are displayed only. Do not adopt a remaining bit. Do not
write the refuse into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | remaining-bit class declared |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 924 six-site seeds, off-patch 0 | declared finite patch |
| extras `(0,1,0,0,0)` and `(0,1,0,0,1)` Q8-true, `cov6=0` | reconfirmed by the census |
| lex-first 6-site seed that `f1` fills | named |
| first remaining-bit refuse of `f_e` from `S` | tick `0`, site `(1,1,0)`, type `adj2` |
| `N_refuse` on that first tick | `4` |
| leftover-character of #6552/#6555 | refused; new refuse object |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6552: that scored the Q8-true versus `cov6>0`
inclusion and named the extras. Not leftover-character of #6555: that
scored coverage of the extras. The present object is the first
remaining-bit refuse of `(0, 1, 0, 0, 0)` on the lex-first 6-site `f1`
fill.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the refuse into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of the lex-first Q8-true `cov6=0` extra on the lex-first 6-site `f1` fill. |
| V2 | Current main has no landed 6-site remaining-bit refuse for these extras. |
| V3 | The 924 seeds, occupancy-to-lock evolution, and remaining-bit types are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it names a refuse of a declared finite map. |
| V5 | It is not a physical selector: the refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch the extra `(0, 1, 0, 0, 0)`
first refuses remaining-bit type `adj2` from the lex-first 6-site `f1`
fill, with `N_refuse = 4`. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover extras census | treat the refuse as leftover-character of #6552/#6555 | **ATTEMPTED** |
| adopt a remaining bit | write `adj2` or `(0, 1, 0, 0, 0)` into Admissibility | **ATTEMPTED** |
| Q8 as 6-site selector | claim Q8-true iff `cov6>0` | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch refuse to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The first refuse, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, and the `F_cut` remaining-bit order are declared.
Adoption of a remaining bit is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of the lex-first extra, not leftover-character of #6552/#6555 and
not Hamming identification of `f_L1`.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | extras scored on 924 six-site seeds | no physical law selection |
| per block | first remaining-bit refuse of `f_e` from `S` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, the
partner extra's refuse class, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Q8 already names the extras, so the refuse adds nothing.

**Answer:** Q8-true is thirty maps. Only two have `cov6=0`. Q8 is not the
6-site vanishing predicate. The first remaining-bit refuse of the lex-first
extra is a new 6-site object.

### N8 — cross-cycle echo

Investments #6552 and #6555 already named the extras and scored `cov6=0`.
Echoing that pair is not a substitute for the refuse
`(tick, site, type) = (0, (1, 1, 0), adj2)` or for `N_refuse = 4`.

No-Go Discipline disposition: **PASS** for the finite first remaining-bit
refuse of the extra. FAIL / DO NOT SHIP for “the displayed refuse is the
physical rule” or “Q8 equals `cov6>0`.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner names the lex-first 6-site seed that `f1` fills,
reports the first remaining-bit refuse of `F_cut` `(0, 1, 0, 0, 0)` from
that seed, and reports `N_refuse` on that first tick. It reconfirms that
both extras are Q8-true with `cov6=0`. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit verdict.
