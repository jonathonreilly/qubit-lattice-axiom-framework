---
claim_id: f_cut_q10_true_mix1_ten_site_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (0,0,0,0,1) on the lex-first 10-site f1 fill is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q10_true_mix1_ten_site_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of the Q10-True Extra `F_cut` `(0,0,0,0,1)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the twelve-vertex two-cube
with off-patch occupancy `0`, for the cube-covariant cut map whose
remaining-bit tuple is `(0, 0, 0, 0, 1)`. The lex-first 10-site seed that
`f1` fills, the first remaining-bit refuse of that extra from that seed,
and `N_refuse` on that first tick are reported.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q10_true_mix1_ten_site_first_refuse_2026_08_15.py`](../scripts/f_cut_q10_true_mix1_ten_site_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investments c2q10, c4q10, c5q10, c6q10, and c8q10 name the lex-first
Q10-versus-`cov_k>0` miss: the remaining-bit tuple
`f_m = (0, 0, 0, 0, 1)`, which is Q10-true and has `cov_k=0` at
`k ∈ {2,4,5,6,8}`. This note names the first remaining-bit refuse of
that extra on the lex-first 10-site seed that `f1` fills. That refuse
is the mechanism of the Q10-true extra on this seed: it is Q10-true
only through `mixed3`, and the first remaining-bit demand it meets is
not `mixed3`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. The
remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`: it fires on every
remaining-bit orbit. Q10 is the remaining-bit predicate
`adj2=1` or `vertex3=1` or `mixed3=1`. The extra `f_m` has
`mixed3=1` and `wt1=opp2=adj2=vertex3=0`, so it is Q10-true.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. The lex-first 10-site seed that `f1` fills is
  `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1),(2,0,0),(2,0,1)}`.
  The first remaining-bit refuse of `f_m = (0, 0, 0, 0, 1)` from `S` is
  tick `0`, site `(2, 1, 0)`, remaining-bit type `adj2`.
- Theorem 2. On that first tick, `N_refuse = 2`.
- Theorem 3. The seed and the refuse are displayed only. Do not adopt a
  remaining bit. Do not write the refuse into Admissibility.

Displayed, not adopted.

Not leftover-character of c2q10. Not leftover-character of c4q10.
Not leftover-character of c5q10. Not leftover-character of c6q10.
Not leftover-character of c8q10. Those named the miss `(0, 0, 0, 0, 1)`
and scored `Q10=1` with `cov_k=0`. The object here is the first
remaining-bit refuse.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first 10-site f1 fill and the first remaining-bit refuse of F_cut (0,0,0,0,1) from that seed are finite exact names on the two-cube. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q10_true_mix1_ten_site_first_refuse
target_blocker_text: "name the first remaining-bit refuse of the Q10-true extra (0,0,0,0,1) on the lex-first 10-site seed f1 fills"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first remaining-bit refuse of the Q10-true extra; do not adopt a displayed bit"
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

**Target.** Name the lex-first 10-site seed that `f1` fills and the first
remaining-bit refuse of `F_cut` `(0, 0, 0, 0, 1)` from that seed, together
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

### Theorem 1 — seed `S` and the first remaining-bit refuse

The lex-first 10-site seed that `f1` fills is

```text
S = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1), (2,0,0), (2,0,1)}.
```

`f1` fills from `S`. The extra `f_m = (0, 0, 0, 0, 1)` does not fill from
`S`. The extra is Q10-true and has `cov2=cov4=cov5=cov6=cov8=0`. It has
`cov10=4` on the 66 ten-site seeds.

From `S`, the two unlocked sites at tick `0` and their axis types are

```text
(2,1,0)  type (2,0,1)  adj2
(2,1,1)  type (2,0,1)  adj2
```

Both demands are remaining-bit type `adj2`. The extra `f_m` fires only on
`mixed3`. It returns 0 on every remaining-bit demand present at the seed.
The first remaining-bit refuse of `f_m` from `S` is therefore

- tick `0`,
- site `(2, 1, 0)`,
- remaining-bit type `adj2`.

That is the mechanism of the Q10-true extra on this seed: Q10-true only
through `mixed3`, first remaining-bit refuse of type `adj2`.

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
| extra `(0,0,0,0,1)` Q10-true, `cov_k=0` at `k=2,4,5,6,8` | reconfirmed by the census |
| lex-first 10-site seed that `f1` fills | named |
| first remaining-bit refuse of `f_m` from `S` | tick `0`, site `(2,1,0)`, type `adj2` |
| `N_refuse` on that first tick | `2` |
| leftover-character of c2q10/c4q10/c5q10/c6q10/c8q10 | refused; new refuse object |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c2q10, c4q10, c5q10, c6q10, or c8q10: those
scored whether `Q10` equals `cov_k>0` and named the lex-first miss
`(0, 0, 0, 0, 1)`. The present object is the first remaining-bit refuse
of that extra on the lex-first 10-site `f1` fill.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the refuse into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of the Q10-true extra `(0, 0, 0, 0, 1)` on the lex-first 10-site `f1` fill. |
| V2 | Current main has no landed 10-site remaining-bit refuse for this extra. |
| V3 | The 66 seeds, occupancy-to-lock evolution, and remaining-bit types are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it names a refuse of a declared finite map. |
| V5 | It is not a physical selector: the refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch the extra `(0, 0, 0, 0, 1)`
first refuses remaining-bit type `adj2` from the lex-first 10-site `f1`
fill, with `N_refuse = 2`. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover miss census | treat the refuse as leftover-character of c2q10/c4q10/c5q10/c6q10/c8q10 | **ATTEMPTED** |
| adopt a remaining bit | write `adj2` or `(0, 0, 0, 0, 1)` into Admissibility | **ATTEMPTED** |
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
refuse of the Q10-true extra, not leftover-character of the
Q10-versus-`cov_k` selector tests and not Hamming identification of `f_L1`.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | extra scored on the 66 ten-site seeds and on the `k=2,4,5,6,8` seeds | no physical law selection |
| per block | first remaining-bit refuse of `f_m` from `S` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, the
class refuse of other Q10-true `cov_k=0` maps, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Q10 already names the extra, so the refuse adds nothing.

**Answer:** Q10-true is twenty-eight maps. The lex-first miss versus
`cov2/4/5/6/8` is one remaining-bit tuple. The first remaining-bit refuse
of that extra on the lex-first 10-site `f1` fill is a new 10-site object:
tick, site, and type, not the class predicate.

### N8 — cross-cycle echo

Investments c2q10, c4q10, c5q10, c6q10, and c8q10 already named the miss
`(0, 0, 0, 0, 1)` and scored `cov_k=0`. Echoing that miss is not a
substitute for the refuse `(tick, site, type) = (0, (2, 1, 0), adj2)` or
for `N_refuse = 2`.

No-Go Discipline disposition: **PASS** for the finite first remaining-bit
refuse of the extra. FAIL / DO NOT SHIP for “the displayed refuse is the
physical rule” or “adopt Q10 as Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner names the lex-first 10-site seed that `f1` fills,
reports the first remaining-bit refuse of `F_cut` `(0, 0, 0, 0, 1)` from
that seed, and reports `N_refuse` on that first tick. It reconfirms that
the extra is Q10-true with `cov2=cov4=cov5=cov6=cov8=0`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
