---
claim_id: f_cut_qstar_cov2_gap62_miss_seeds_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the four two-site seeds that F_cut (1,0,1,1,0) misses, and the orbit count of that set, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov2_gap62_miss_seeds_2026_08_15.py
---

# Four Two-Site Seeds That `F_cut` `(1,0,1,1,0)` Misses

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 2-site coverage of the one named
`Q_*` map `f_g` with remaining bits `(1, 0, 1, 1, 0)` on the
twelve-vertex two-cube with off-patch occupancy `0`. The four two-site
seeds that map misses are listed in lexicographic order, and the
orbit count of that four-set under two-cube-preserving rotations is
reported. Displayed, not adopted. One map only; not a two-map
share-test.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov2_gap62_miss_seeds_2026_08_15.py`](../scripts/f_cut_qstar_cov2_gap62_miss_seeds_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment tot2why named that `f_g = (1, 0, 1, 1, 0)` has `cov2=62` on
the two-cube, so it misses four of the sixty-six two-site seeds, and
then reported the first remaining-bit refuse on the lex-first of those
misses. A parked share-test would have compared two maps' miss sets.
This note names the four miss seeds of `f_g` only, in lex order, and
the orbit count of that four-set. One map. Not a two-map share-test.

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
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)`.

On the two-cube with off-patch `o=0`:

- Theorem 1. The four 2-site seeds `f_g` misses, in lex order, are
  `{(0,0,0), (2,0,0)}`, `{(0,0,1), (2,0,1)}`, `{(0,1,0), (2,1,0)}`,
  and `{(0,1,1), (2,1,1)}`. Direct scoring gives `cov2(f_g)=62`.
- Theorem 2. Under the two-cube-preserving proper cube rotations about
  the box center, that four-set is a single orbit: `N_orb = 1`.
- Theorem 3. The four seeds and `N_orb` are displayed. Do not adopt a
  seed.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One named Q_* map is scored exactly on the sixty-six two-site seeds of the twelve-vertex two-cube. The four misses and the G-orbit count of that four-set are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov2_gap62_miss_seeds
target_blocker_text: "the four two-site seeds that (1,0,1,1,0) misses, in lex order, and N_orb of that four-set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q_* 62-gap miss-seed list and its orbit count; do not adopt a displayed seed"
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
record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

Admissibility is not a dynamics axiom.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. The four miss seeds and the integer `N_orb` below are
displayed remaining-bit data, not axiom content.

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
- the eight two-cube-preserving rotations: those proper cube rotations
  about the box center `(1, 1/2, 1/2)` that permute the twelve sites;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the subclass `Q_*` of those maps with remaining bits `wt1=1` and `adj2=1`;
- the named map `f_g` with remaining bits `(1, 0, 1, 1, 0)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** On the two-cube with off-patch `o=0`, list the four two-site
seeds that `f_g` misses, in lex order, and report `N_orb` of that
four-set under two-cube-preserving rotations.

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
the number of those pairs from which `f` fills. A miss is a two-site seed
from which `f` does not fill.

Let `M` be the four-set of two-site seeds that `f_g` misses. Let `G` be
the group of two-cube-preserving rotations: those proper cube rotations
about `(1, 1/2, 1/2)` that permute the twelve sites. Sixteen of the
twenty-four ambient proper cubic matrices send at least one site off the
two-cube and are not used. The remaining eight induce `G`. `N_orb` is
the number of `G`-orbits in `M`.

## Theorems

### Theorem 1 — the four 2-site seeds `f_g` misses, in lex order

`f_g` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 1, 0)`.
Direct scoring of the sixty-six two-site seeds gives `cov2(f_g)=62`.
The four seeds `f_g` misses, in lexicographic order of sorted site
pairs, are

```text
{(0,0,0), (2,0,0)}
{(0,0,1), (2,0,1)}
{(0,1,0), (2,1,0)}
{(0,1,1), (2,1,1)}
```

Each is a long-axis displacement-`(2,0,0)` pair. Each has halt
lock-count 8 and lock-count history `(2, 6, 8)`. No other two-site seed
is a miss of `f_g`. This is a one-map miss list. It is not a two-map
share-test.

### Theorem 2 — `N_orb` of that four-set

Act with `G` on the four-set `M`. The four long-axis pairs form a
single orbit under the two-cube-preserving rotations:

```text
N_orb = 1
```

The orbit has size `4`. The lex representative of that orbit is
`{(0,0,0), (2,0,0)}`. Sixteen ambient proper cubes are discarded
because they do not permute the twelve sites. The remaining eight
generate one orbit on `M`.

### Theorem 3 — display; do not adopt a seed

The four miss seeds and the integer `N_orb = 1` are displayed census
output. Do not adopt a seed. Do not write the four-set into
Admissibility. Do not write `Q_*` or `f_g` into Admissibility.
Admissibility does not name this remaining-bit formula.

Displayed, not adopted. The list is a finite fact about occupancy-to-lock
on this two-cube with off-patch `o=0`. It is not a physical
formation-site selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| `f_g` remaining bits `(1, 0, 1, 1, 0)` | defined |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| four miss seeds of `f_g` in lex order | proved by the 66-seed census |
| `N_orb` of that four-set under two-cube rotations | `1` |
| leftover of tot2why | refused; that named the first remaining-bit refuse |
| leftover of tot2q | refused; that named the eight-map census |
| leftover of a two-map share-test | refused; one map only |
| leftover of the `f_L1` miss list | refused; that is a different map |
| adoption of a seed | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot2why: that asked for the first remaining-bit
refuse of `f_g` on the lex-first miss seed. The present object is the
four-set itself and its orbit count.

Not leftover-character of tot2q: that scored whether `cov2=66` is
equivalent to `vertex3=1` among the eight `Q_*` maps and reported that
`(1, 0, 1, 1, 0)` has `cov2=62`. A coverage integer is not a named
four-set and not `N_orb`.

Not leftover-character of a two-map share-test: a parked share-test
would have compared two maps' miss sets. This note scores `f_g` only.

Not leftover-character of the `f_L1` two-site miss list: that map is
`(1, 0, 1, 1, 1)`, not `f_g`. The present list is the miss set of
`f_g` alone.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the four two-site seeds `f_g` misses and the orbit count of that set. |
| V2 | Current main has no landed one-map miss list plus `N_orb` for `(1, 0, 1, 1, 0)`. |
| V3 | The named map, the sixty-six seeds, and the eight-element group action are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a named map and a supplied group. |
| V5 | It is not a physical selector: the four seeds are displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch, `f_g` misses four named
two-site seeds that form one `G`-orbit, and that list is not a reason
to write a seed into Admissibility. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover tot2why refuse | treat the four-set as leftover-character of the first refuse | **ATTEMPTED** |
| leftover tot2q census | treat `cov2=62` as a naming of the four | **ATTEMPTED** |
| leftover two-map share-test | compare two maps' miss sets | **ATTEMPTED** |
| leftover `f_L1` miss list | treat `f_g` misses as leftover-character of `f_L1` | **ATTEMPTED** |
| adopt a seed | write one miss into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the off-patch convention, and the non-adoption of
a seed are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, two-cube lex site order, the `F_cut`
remaining-bit order, and the restriction to two-cube-preserving
rotations are declared. Adoption of a seed is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is the
four-seed miss list of `f_g` and `N_orb` of that set, not leftover-
character of tot2why and not leftover-character of a two-map
share-test.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_g` scored on all sixty-six two-site seeds | no physical law selection |
| per block | four-set list and `N_orb` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
the other `cov2=62` map `f_L1` as its own one-map list, a parked
two-map share-test, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** tot2why already printed the four long-axis pairs as the
seeds `f0` fills and `f_g` misses, and a coverage integer of `62`
already counts them, so listing the four and calling them one orbit
adds nothing; the only way to close the gap is to adopt a seed.

**Answer:** tot2why reported a refuse on one run. A coverage integer is
not a list. A parked share-test would have compared two maps. This
note scores `f_g` only, names the four misses in lex order, and reports
`N_orb = 1` under two-cube-preserving rotations. The extra that would
write a seed into Admissibility is not present.

### N8 — cross-cycle echo

Investment tot2why already used the lex-first of these four seeds as
the start of a refuse run. Echoing that seed is not a substitute for
the four-set and its orbit count. This note reports the four miss
seeds of `f_g` and `N_orb = 1`.

No-Go Discipline disposition: **PASS** for the finite `f_g` miss list
and the narrow non-adoption of a seed. FAIL / DO NOT SHIP for “this
seed is the physical rule” or “`Q_*` is written into Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds `f_g` from remaining bits `(1, 0, 1, 1, 0)`,
scores all sixty-six two-site seeds, lists the four misses in
lexicographic order, and reports `N_orb = 1` for that four-set under
the two-cube-preserving rotations. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.
