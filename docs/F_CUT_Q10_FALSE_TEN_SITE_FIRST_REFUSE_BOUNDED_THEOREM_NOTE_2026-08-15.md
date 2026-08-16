---
claim_id: f_cut_q10_false_ten_site_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of the lex-first Q10-false F_cut map on the lex-first 10-site f1 fill is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q10_false_ten_site_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of the Lex-First Q10-False Map

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the twelve-vertex two-cube
with off-patch occupancy `0`, for the cube-covariant cut map whose
remaining-bit tuple is `(0, 0, 0, 0, 0)`. The lex-first 10-site seed that
`f1` fills, the first remaining-bit refuse of that map from that seed,
and `N_refuse` on that first tick are reported.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q10_false_ten_site_first_refuse_2026_08_15.py`](../scripts/f_cut_q10_false_ten_site_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 names the four `cov10=0` maps: they are exactly the
maps with `(adj2, vertex3, mixed3)=(0, 0, 0)`. This note names the first
remaining-bit refuse of the lex-first such map
`f_z = (0, 0, 0, 0, 0)` on the lex-first 10-site seed that `f1` fills.
That refuse is the mechanism of the Q10 zeros on this seed: they are
Q10-false, so they fire on neither `adj2` nor `vertex3` nor `mixed3`, and
the first remaining-bit demand they meet is `adj2`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`: it fires on every
remaining-bit orbit. Q10 is the remaining-bit predicate
`adj2=1` or `vertex3=1` or `mixed3=1`. The four Q10-false maps are
`(0, 0, 0, 0, 0)`, `(0, 1, 0, 0, 0)`, `(1, 0, 0, 0, 0)`, and
`(1, 1, 0, 0, 0)`. Each has `cov10=0`. The lex-first of them is
`f_z = (0, 0, 0, 0, 0)`.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. The lex-first remaining-bit map with
  `adj2=vertex3=mixed3=0` is `f_z = (0, 0, 0, 0, 0)`. The lex-first
  10-site seed that `f1` fills is
  `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1),(2,0,0),(2,0,1)}`.
  The first remaining-bit refuse of `f_z` from `S` is tick `0`,
  site `(2, 1, 0)`, remaining-bit type `adj2`.
- Theorem 2. On that first tick, `N_refuse = 2`.
- Theorem 3. The seed and the refuse are displayed only. Do not adopt a
  remaining bit. Do not write the refuse into Admissibility.

Displayed, not adopted.

Not leftover-character of c10bit3. Not leftover-character of #6566. Those
named the 3-bit selector `Q10` and scored `N_pos=28`. The object here is
the first remaining-bit refuse.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first 10-site f1 fill and the first remaining-bit refuse of F_cut (0,0,0,0,0) from that seed are finite exact names on the two-cube. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q10_false_ten_site_first_refuse
target_blocker_text: "name the first remaining-bit refuse of the lex-first Q10-false map on the lex-first 10-site seed f1 fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first remaining-bit refuse of the Q10-false map; do not adopt a displayed bit"
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

**Target.** Name the lex-first Q10-false remaining-bit map `f_z`, the
lex-first 10-site seed that `f1` fills, and the first remaining-bit refuse
of `f_z` from that seed, together with `N_refuse` on that first tick.

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

The 10-site seeds are the `66` unordered 10-subsets of `T`, listed in
lexicographic site order induced by
`(x,y,z)` with `x ∈ {0,1,2}`, `y ∈ {0,1}`, `z ∈ {0,1}`. Then `cov10(f)` is
the number of those seeds from which `f` fills.

A remaining-bit refuse of a map `f` from a seed `S` is an unlocked site
whose six-neighbor occupancy is a remaining-bit type (so `f1` returns 1)
on which `f` returns 0. The first such refuse is the least tick, then the
lexicographically first site at that tick. `N_refuse` is the number of
remaining-bit refuses on that first tick.

## Theorems

### Theorem 1 — map `f_z`, seed `S`, and the first remaining-bit refuse

The four remaining-bit maps with `adj2=vertex3=mixed3=0` are

```text
(0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (1, 0, 0, 0, 0), (1, 1, 0, 0, 0).
```

These are exactly the four maps with `cov10=0`, and exactly the Q10-false
maps. The lex-first of them is

```text
f_z = (0, 0, 0, 0, 0).
```

The lex-first 10-site seed that `f1` fills is

```text
S = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1), (2,0,0), (2,0,1)}.
```

`f1` fills from `S`. The zero `f_z` does not fill from `S`. The other three
Q10-false maps also do not fill from `S`. All four have `cov10 = 0` on the
66 ten-site seeds.

From `S`, the two unlocked sites at tick `0` and their axis types are

```text
(2,1,0)  type (2,0,1)  adj2
(2,1,1)  type (2,0,1)  adj2
```

Both demands are remaining-bit type `adj2`. The zero `f_z` fires on no
remaining-bit orbit. It returns 0 on every remaining-bit demand present at
the seed. The first remaining-bit refuse of `f_z` from `S` is therefore

- tick `0`,
- site `(2, 1, 0)`,
- remaining-bit type `adj2`.

That is the mechanism of the Q10 zeros on this seed: Q10-false, first
remaining-bit refuse of type `adj2`.

### Theorem 2 — `N_refuse` on the first tick

On that first tick the remaining-bit refuses are the two unlocked
remaining-bit sites

```text
(2,1,0) adj2
(2,1,1) adj2
```

so `N_refuse = 2`.

### Theorem 3 — display; do not adopt a bit

The seed, the refuse `(tick, site, type) = (0, (2, 1, 0), adj2)`, and
`N_refuse = 2` are displayed only. Do not adopt a remaining bit. Do not
write the refuse into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | remaining-bit class declared |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 66 ten-site seeds, off-patch 0 | declared finite patch |
| four Q10-false maps, `cov10=0` | reconfirmed by the census |
| lex-first 10-site seed that `f1` fills | named |
| first remaining-bit refuse of `f_z` from `S` | tick `0`, site `(2,1,0)`, type `adj2` |
| `N_refuse` on that first tick | `2` |
| leftover-character of c10bit3/#6566 | refused; new refuse object |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c10bit3: that scored whether a displayed 3-bit
AND or 3-bit OR equals `cov10>0` and named `Q10 = adj2 OR vertex3 OR mixed3`.
Not leftover-character of #6566: that scored the 1-bit and 2-bit OR menu
at the same `k=10`. The present object is the first remaining-bit refuse of
`(0, 0, 0, 0, 0)` on the lex-first 10-site `f1` fill.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the refuse into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of the lex-first Q10-false map on the lex-first 10-site `f1` fill. |
| V2 | Current main has no landed 10-site remaining-bit refuse for the Q10 zeros. |
| V3 | The 66 seeds, occupancy-to-lock evolution, and remaining-bit types are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it names a refuse of a declared finite map. |
| V5 | It is not a physical selector: the refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch the zero `(0, 0, 0, 0, 0)`
first refuses remaining-bit type `adj2` from the lex-first 10-site `f1`
fill, with `N_refuse = 2`. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover zeros census | treat the refuse as leftover-character of c10bit3/#6566 | **ATTEMPTED** |
| adopt a remaining bit | write `adj2` or `(0, 0, 0, 0, 0)` into Admissibility | **ATTEMPTED** |
| Q10 as 10-site selector adoption | write Q10-true iff `cov10>0` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch refuse to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The first refuse, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 66 ten-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, and the `F_cut` remaining-bit order are declared.
Adoption of a remaining bit is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of the lex-first Q10-false map, not leftover-character of c10bit3 or
#6566 and not Hamming identification of `f_L1`.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | Q10-false maps scored on 66 ten-site seeds | no physical law selection |
| per block | first remaining-bit refuse of `f_z` from `S` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, the
class refuse of all four Q10-false maps, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Q10 already names the zeros, so the refuse adds nothing.

**Answer:** Q10-false is four maps. All four have `cov10=0`. The first
remaining-bit refuse of the lex-first zero is a new 10-site object: tick,
site, and type, not the class predicate.

### N8 — cross-cycle echo

Investment c10bit3 already named `Q10 = adj2 OR vertex3 OR mixed3` and
scored `cov10=0` on the four zeros. Echoing that class is not a substitute
for the refuse `(tick, site, type) = (0, (2, 1, 0), adj2)` or for
`N_refuse = 2`.

No-Go Discipline disposition: **PASS** for the finite first remaining-bit
refuse of the Q10-false map. FAIL / DO NOT SHIP for “the displayed refuse is
the physical rule” or “adopt Q10 as Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner names the lex-first 10-site seed that `f1` fills,
reports the first remaining-bit refuse of `F_cut` `(0, 0, 0, 0, 0)` from
that seed, and reports `N_refuse` on that first tick. It reconfirms that
the four Q10-false maps are exactly the maps with `cov10=0`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
