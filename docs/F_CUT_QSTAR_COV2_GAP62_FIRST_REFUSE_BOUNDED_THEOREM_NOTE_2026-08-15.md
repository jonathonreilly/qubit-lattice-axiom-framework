---
claim_id: f_cut_qstar_cov2_gap62_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (1,0,1,1,0) on the lex-first 2-site seed f0 fills and (1,0,1,1,0) misses is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov2_gap62_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of the Lex-First `Q_*` `cov2=62` Map

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution of the named `Q_*` map
`f_g` with remaining bits `(1, 0, 1, 1, 0)` on the twelve-vertex
two-cube with off-patch occupancy `0`, started from the lex-first
two-site seed that `f0` fills and `f_g` misses, reporting the first
remaining-bit refuse.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov2_gap62_first_refuse_2026_08_15.py`](../scripts/f_cut_qstar_cov2_gap62_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment tot2q named that among the eight `Q_*` maps the remaining-bit
tuple `(1, 0, 1, 1, 0)` has `vertex3=1` and `cov2=62`, while
`Max(2) = {f0, f1}` have `cov2=66`. This note does not restate that
census. It names the first remaining-bit refuse of
`f_g = (1, 0, 1, 1, 0)` on the lex-first 2-site seed that `f0` fills and
`f_g` misses. Mechanism of the 62-gap.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has 8 maps.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

Write `f_g` for the `F_cut` map with remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)`. Write `f0` for
`(1, 1, 1, 1, 0)` and `f1` for `(1, 1, 1, 1, 1)`. Both `f0` and `f1` are
the two `Max(2)` maps with `cov2=66`. On the two-cube with off-patch
`o=0`:

- Theorem 1. The lex-first 2-site seed `f0` fills and `f_g` does not is
  `S = {(0,0,0), (2,0,0)}`. The first remaining-bit refuse of `f_g` from
  `S` is the `opp2` neighborhood `(1, 1, 0, 0, 0, 0)` at site `(1,0,0)`,
  at tick 1.
- Theorem 2. On that first refuse tick, `N_refuse = 1`.
- Theorem 3. That refuse is displayed. Do not adopt a bit.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One named Q_* map is evolved exactly from the lex-first two-site seed that f0 fills and f_g misses on the twelve-vertex two-cube. The first remaining-bit refuse (tick, site, remaining-bit type) and N_refuse on that tick are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov2_gap62_first_refuse
target_blocker_text: "first remaining-bit refuse of (1,0,1,1,0) on the lex-first 2-site seed that f0 fills and (1,0,1,1,0) misses"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q_* 62-gap first remaining-bit refuse; do not adopt a displayed bit"
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
predicate. The `opp2` refuse below is displayed remaining-bit data, not
axiom content.

## Premises and declared mathematical objects

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil
  `{±e_x, ±e_y, ±e_z}` at every site, in order
  `(+x,-x,+y,-y,+z,-z)`;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the subclass `Q_*` of those maps with remaining bits `wt1=1` and `adj2=1`;
- the named map `f_g` with remaining bits `(1, 0, 1, 1, 0)`;
- the named map `f0` with remaining bits `(1, 1, 1, 1, 0)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** On the run of `f_g` from the lex-first 2-site seed `f0` fills
and `f_g` misses, report the first remaining-bit refuse (tick, site,
remaining-bit type) and the number of remaining-bit refuses on that first
tick.

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

The two-site seeds are the sixty-six pairs `{x,y}` for distinct `x,y ∈ T`,
listed in lexicographic site order induced by `(x,y,z)`. Then `cov2(f)` is
the number of those pairs from which `f` fills.

A neighborhood is a remaining-bit neighborhood when its axis type is one of
the five remaining types or a complement partner of one of them. Empty and
full are not remaining bits. The first remaining-bit refuse on a run is the
first remaining-bit neighborhood, in tick order and then two-cube lex order
of sites, at which `f` returns 0. Tick 1 is the first evaluation on the
seed occupancy. `N_refuse` on a tick is the number of unlocked sites whose
neighborhood is a remaining-bit type and whose predicate value is 0.

## Theorems

### Theorem 1 — first remaining-bit refuse: tick, site, type

`f_g` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 1, 0)`.
`f0` is the `F_cut` map with remaining-bit tuple `(1, 1, 1, 1, 0)`.
Direct scoring of the sixty-six two-site seeds gives `cov2(f_g)=62` and
`cov2(f0)=66`. The four seeds `f0` fills and `f_g` misses, in
lexicographic order of sorted site pairs, are

```text
{(0,0,0), (2,0,0)}
{(0,0,1), (2,0,1)}
{(0,1,0), (2,1,0)}
{(0,1,1), (2,1,1)}
```

The lex-first of those seeds is `S = {(0,0,0), (2,0,0)}`. `f0` fills from
`S`. `f_g` does not fill from `S`: the run of `f_g` halts at the eight-site
set of the two end faces `x=0` and `x=2`, with lock-count history
`(2, 6, 8)`.

Tick 1 is the first evaluation on the seed occupancy. The unlocked
remaining-bit neighborhoods at that tick are four `wt1` sites, which
`f_g` accepts, and one `opp2` site, which `f_g` refuses. Empty
neighborhoods also refuse, and empty is not a remaining bit.

The lex-first refused remaining-bit neighborhood, in two-cube site order,
is

```text
site (1,0,0), neighborhood (1, 1, 0, 0, 0, 0), axis type (0, 1, 2) = opp2
```

The first remaining-bit refuse of `f_g` from `S` is therefore `opp2` at
site `(1,0,0)`, at tick 1. No `mixed3` neighborhood appears before that
refuse.

### Theorem 2 — `N_refuse` on that first tick

On tick 1 the only remaining-bit refuse is that single `opp2` site
`(1,0,0)`. So `N_refuse = 1` on the first refuse tick.

Site `(1,0,0)` sees both seed sites as opposite `x`-neighbors. The six
bits are `(1, 1, 0, 0, 0, 0)`: both ends of the long `x` axis are occupied
and the other two axes are empty. That is a filled axis. `f_g` has
`opp2=0`, so it refuses. `f0` has `opp2=1`, so it locks the mid-edge and
later fills. That is the mechanism of the 62-gap.

### Theorem 3 — display; do not adopt a bit

The first refuse is an `opp2` neighborhood, and `f_g` has `opp2=0` while
`f0` has `opp2=1`. That is the mechanism of the 62-gap on this seed:
`f_g` shares `wt1=1`, `adj2=1`, and `vertex3=1` with `f0`, grows through
those remaining bits on the end faces, and stops at the first `opp2`
midplane site.

Displayed, not adopted. Do not adopt a bit. Do not adopt `opp2`. Do not write `opp2` into Admissibility. Do not write `Q_*` or `opp2=1` into
Admissibility. Admissibility does not name this remaining-bit formula.

The refuse is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| `f_g` remaining bits `(1, 0, 1, 1, 0)` | defined |
| `f0` remaining bits `(1, 1, 1, 1, 0)` | defined |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| lex-first seed `f0` fills and `f_g` misses | `S = {(0,0,0), (2,0,0)}` |
| first remaining-bit refuse is `opp2` at `(1,0,0)`, tick 1 | proved by evolution |
| `N_refuse = 1` on that first tick | proved by the same tick |
| leftover of tot2q | refused; that named the eight-map census |
| leftover of the four-seed miss list | refused; this is a refuse mechanism |
| leftover of the `f_L1` miss mechanism | refused; that compared `f_L1` with `f1` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot2q: that asked whether `cov2=66` is
equivalent to `vertex3=1` among the eight `Q_*` maps and reported that
`(1, 0, 1, 1, 0)` has `cov2=62`. The present object is the first
remaining-bit refuse of that map on the lex-first seed `f0` fills and
it misses.

Not leftover-character of the four-seed miss list: naming
`{(0,0,0),(2,0,0)}` and its three translates is not the refuse on the
run of `f_g` from that seed.

Not leftover-character of the `f_L1` two-site miss mechanism: that
compared `f_L1 = (1, 0, 1, 1, 1)` with `f1` on the four seeds `f_L1`
misses. The present map is `f_g = (1, 0, 1, 1, 0)` versus `f0`.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of `f_g` from the lex-first seed `f0` fills and `f_g` misses. |
| V2 | Current main has the tot2q census, but no landed 62-gap remaining-bit refuse of `(1, 0, 1, 1, 0)`. |
| V3 | The named maps, the sixty-six seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a named map on a declared run. |
| V5 | It is not a physical selector: the `opp2` refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch, `f_g` refuses its first
remaining-bit neighborhood in the `opp2` class, and that refuse is not
a reason to write `opp2=1` into Admissibility. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover tot2q census | treat the refuse as leftover-character of the eight-map iff | **ATTEMPTED** |
| leftover four-seed list | treat the refuse as leftover-character of naming the four misses | **ATTEMPTED** |
| leftover `f_L1` miss mechanism | treat `f_g` versus `f0` as leftover-character of `f_L1` versus `f1` | **ATTEMPTED** |
| adopt a bit | write `opp2=1` or `Q_*` into Admissibility | **ATTEMPTED** |
| empty as remaining-bit | count a tick-1 empty refuse as the first remaining-bit refuse | **ATTEMPTED** |

### N2 — wall independence

The `opp2` refuse, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, two-cube lex site order, and the `F_cut`
remaining-bit order are declared. Adoption of `opp2` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is the first
remaining-bit refuse of `f_g` from the lex-first seed `f0` fills and
`f_g` misses, not leftover-character of tot2q and not leftover-character
of the `f_L1` miss mechanism.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_g` evolved from the lex-first miss seed | no physical law selection |
| per block | first remaining-bit refuse and `N_refuse` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
the other `cov2=62` map `f_L1`, a selector other than a remaining-bit
refuse, and any independently derived physical map from `F_cut` into
Admissibility.

### N7 — hostile steelman

**Steelman:** tot2q already named `cov2=62` for `(1, 0, 1, 1, 0)`, and
the four opposite-end seeds are already the `f_L1` misses, so the refuse
adds nothing and the only way to close the gap is to adopt `opp2=1`.

**Answer:** tot2q scored an eight-map identity. The four-seed list names
misses, not a refuse. `f_L1` is `(1, 0, 1, 1, 1)`, not `f_g`. On `S`,
`wt1=1` accepts the end-face growth and the first remaining-bit refuse
is `opp2`. The contrast `f0` with `opp2=1` fills. The extra that would
write `opp2` into Admissibility is not present.

### N8 — cross-cycle echo

Investment tot2q already showed that `(1, 0, 1, 1, 0)` has `cov2=62`.
Echoing that count is not a substitute for the refuse on the run. This
note reports the first remaining-bit refuse of `f_g` from `S`.

No-Go Discipline disposition: **PASS** for the finite `f_g` refuse and
the narrow non-adoption of a bit. FAIL / DO NOT SHIP for “`opp2` is the
physical rule” or “`Q_*` is written into Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds `f_g` from remaining bits `(1, 0, 1, 1, 0)`
and `f0` from `(1, 1, 1, 1, 0)`, finds the lex-first two-site seed `f0`
fills and `f_g` misses, and reports the first remaining-bit refuse as
the `opp2` neighborhood `(1, 1, 0, 0, 0, 0)` at `(1,0,0)` on tick 1,
with `N_refuse = 1` on that tick. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.
