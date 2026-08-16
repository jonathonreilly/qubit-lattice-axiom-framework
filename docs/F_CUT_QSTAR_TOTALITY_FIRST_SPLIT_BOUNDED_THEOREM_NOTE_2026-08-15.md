---
claim_id: f_cut_qstar_totality_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 2 at which f_L1 and the lex-first Q_* map with vertex3=0 disagree on fill is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_totality_first_split_2026_08_15.py
---

# First `|S|≤2` Fill Split Inside `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill comparison of `f_L1` with the
lex-first `Q_*` map that has `vertex3=0`, on the twelve-vertex two-cube
with off-patch occupancy `0`, over all seeds of size at most 2.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_totality_first_split_2026_08_15.py`](../scripts/f_cut_qstar_totality_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6473 ranked 1-site coverage on this two-cube: Max(1) is 4 of the
8 `Q_*` maps. If a totality selector inside `Q_*` holds, those 4 are exactly
the maps with `vertex3=1`. This note does not re-rank Max(1). New split
inside `Q_*`: the first seed of size at most 2 at which a tot map fills and
a non-tot `Q_*` map does not.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has 8 maps.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
Write `f_tot = f_L1`.

On the two-cube with off-patch occupancy `0`, write
`cov1(f) = |{x : f fills from {x}}|`. Seeds of size at most 2 are ordered
by increasing size, then by `combinations` of the two-cube vertices in the
declared site order.

- Theorem 1. Name `f_nt`. The lex-first `Q_*` remaining-bit tuple with
  `vertex3=0` is `(1, 0, 1, 0, 0)`. Both `f_L1` and `f_nt` have `Q_*`.
  Then `cov1(f_L1) = 12` and `cov1(f_nt) = 8`.
- Theorem 2. The lex-first seed of size at most 2 at which they disagree
  on fill, with `f_L1` filling and `f_nt` not filling, is `{(1, 0, 0)}`.
- Theorem 3. Display. Do not adopt a bit.

Do not write the ranking into Admissibility. The displayed seed and the
displayed `f_nt` tuple are not a physical selector.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps and the 8 Q_* maps are enumerated by remaining bits. f_nt is named as the lex-first Q_* map with vertex3=0. Both cov1 values and the lex-first |S|<=2 fill disagreement with f_L1 are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_totality_first_split
target_blocker_text: "first |S|<=2 seed at which f_L1 fills and the lex-first Q_* map with vertex3=0 does not"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q_* totality first-split seed; do not adopt a displayed bit"
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
  complement symmetry `f(c)=f(1-c)`;
- the subclass `Q_*` of those maps with remaining bits `wt1=1` and `adj2=1`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Name the lex-first `Q_*` map with `vertex3=0`, reconfirm that
both it and `f_L1` lie in `Q_*`, report both one-site coverages, and name
the lex-first seed of size at most 2 at which they disagree on fill.

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

The bounded seeds are all `S ⊂ T` with `|S| ≤ 2`, ordered first by size,
then by combinations of the declared two-cube site order
`(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), …`. There are 12 one-site
seeds and 66 two-site seeds, so 78 bounded seeds.

## Theorems

### Theorem 1 — name `f_nt`; both maps have `Q_*`; both `cov1`

`f_L1` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 1, 1)`.
Equivalently, `f_L1(c)=1` if and only if some axis is unbalanced. This is
**not** Hamming parity.

`Q_*` is the eight-member subclass of `F_cut` with `wt1=1` and `adj2=1`.
Among those eight remaining-bit tuples, the four with `vertex3=0` are

```text
(1, 0, 1, 0, 0), (1, 0, 1, 0, 1), (1, 1, 1, 0, 0), (1, 1, 1, 0, 1).
```

The lex-first of these is `(1, 0, 1, 0, 0)`. Write `f_nt` for that map.

Both `f_L1` and `f_nt` have `Q_*`: both have `Q_*`, and each has `wt1=1`
and `adj2=1`. Direct
evolution on the twelve one-site seeds gives `cov1(f_L1) = 12` and
`cov1(f_nt) = 8`.

### Theorem 2 — lex-first `|S|≤2` fill disagreement

On the 78 bounded seeds, ordered by increasing size and then by the
declared site-combination order, the first seed at which `f_L1` fills and
`f_nt` does not is the one-site seed `{(1, 0, 0)}`.

The four earlier one-site seeds `{(0,0,0)}`, `{(0,0,1)}`, `{(0,1,0)}`, and
`{(0,1,1)}` are filled by both maps. So the first disagreement in the
declared order is exactly `{(1, 0, 0)}`.

### Theorem 3 — display; do not adopt a bit

The named map `f_nt` with remaining-bit tuple `(1, 0, 1, 0, 0)` and the
named seed `{(1, 0, 0)}` are displayed. Neither bit assignment nor the
seed is written into Admissibility. Displayed, not adopted.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| `f_nt` as lex-first `Q_*` with `vertex3=0` | named `(1, 0, 1, 0, 0)` |
| both maps have `Q_*` | reconfirmed |
| `cov1(f_L1) = 12`, `cov1(f_nt) = 8` | proved by evolution |
| two-cube, off-patch 0, seeds of size at most 2 | declared finite patch |
| lex-first fill split `{(1, 0, 0)}` | proved by ordered search |
| unique physical selector | refused; displayed, not adopted |
| leftover-character of #6473 | refused; new split inside `Q_*` |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6473: that ranked Max(1) among the 32 `F_cut`
maps and found that the four maximizers are 4 of the 8 `Q_*` maps. The
present object is the first bounded seed at which a tot map in `Q_*` fills
and a non-tot `Q_*` map does not. New split inside `Q_*`, not a restatement
of the Max(1) count.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the ranking into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `f_L1` and the lex-first non-tot `Q_*` map first disagree on a seed of size at most 2. |
| V2 | Current main has the Max(1) ranking (#6473) but no landed first-split seed inside `Q_*`. |
| V3 | The 8 `Q_*` maps, 78 bounded seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it names a displayed seed in a declared class. |
| V5 | It is not a physical selector: the displayed map and seed are not adopted. |

## No-Go Discipline gate

The negative content is narrow: the displayed `f_nt` bit and the displayed
seed do not select a physical occupancy law. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover Max(1) ranking | treat the first split as leftover-character of #6473 | **ATTEMPTED** |
| adopt a bit | write `(1, 0, 1, 0, 0)` or the seed into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch split to a `Z^3` formation law | **ATTEMPTED** |
| other `Q_*` non-tot map | replace lex-first `vertex3=0` by a later tuple | **ATTEMPTED** |

### N2 — wall independence

The failed Hamming identification, the leftover-#6473 contrast, and the
off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 78 bounded seeds, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the size-then-lex seed order are
declared. Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first `|S|≤2` fill
split inside `Q_*` on the declared patch, not leftover-character of #6473.

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:119` | `f_L1` definition | unbalanced-axis predicate, not Hamming | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:124` | Hamming mutation | `|c|_1 mod 2` is a different `F_cut` map | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:128` | `Q_*` definition | remaining bits `wt1=1` and `adj2=1` | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:291` | bounded seed order | size at most 2, size-then-lex | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:302` | first split | `f_L1` fills and `f_nt` does not | yes |
| `scripts/f_cut_qstar_totality_first_split_2026_08_15.py:61` | displayed seed | `{(1, 0, 0)}` | yes |

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_L1` and `f_nt` scored on 78 bounded seeds | no physical law selection |
| per block | first `|S|≤2` fill split inside `Q_*` | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
Approved primitives are `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. None of them
supplies a Boolean occupancy map, a seed-coverage split, or an
Admissibility selector, and none is reclassified as an import or wall.

Live routes include a different seed family, a different off-patch rule, a
later non-tot `Q_*` map, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Max(1) already showed that four `Q_*` maps fill every one-site
seed, so a one-site miss for `f_nt` is leftover-character of #6473.

**Answer:** #6473 ranked the maximum and its multiplicity. It did not name
`f_nt`, did not report `cov1(f_nt)`, and did not name the first bounded seed
at which `f_L1` fills and `f_nt` does not. That first seed is a new split
inside `Q_*`.

### N8 — cross-cycle echo

Investment #6473 already showed that Max(1) is 4 of the 8 `Q_*` maps. Echoing
that multiplicity is not a substitute for naming `f_nt` and the first
`|S|≤2` fill disagreement with `f_L1`.

No-Go Discipline disposition: **PASS** for the finite split and the
narrow non-adoption. FAIL / DO NOT SHIP for “`f_nt` is the physical rule”
or “the displayed seed is adopted.”

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

The companion runner enumerates the 32 `F_cut` maps and the 8 `Q_*` maps,
names `f_nt` as the lex-first remaining-bit tuple with `vertex3=0` inside
`Q_*`, reconfirms that both `f_L1` and `f_nt` have `Q_*`, reports both
`cov1` values, and finds the lex-first seed of size at most 2 at which
`f_L1` fills and `f_nt` does not. Declared audit inputs are this note and
the axiom memo; the runner writes no cache and authors no audit verdict.
