---
claim_id: f_cut_l1_f0_six_site_miss_set_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 6-site miss set of f_L1 is not equal to the 6-site miss set of F_cut (1,1,1,1,0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_l1_f0_six_site_miss_set_2026_08_15.py
---

# Six-Site Miss Sets Of f_L1 And F_cut (1,1,1,1,0) Are Not Equal

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock fill on the twelve-vertex two-cube with
off-patch occupancy `0`; comparison of the two 6-site miss sets of `f_L1`
and of the displayed F_cut map with remaining bits `(1,1,1,1,0)`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_l1_f0_six_site_miss_set_2026_08_15.py`](../scripts/f_cut_l1_f0_six_site_miss_set_2026_08_15.py)

## Result up front

The current Lattice and Admissibility authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
`Z^3` with nearest-neighbor adjacency and one fixed covariant
nearest-neighbor rule. It does not select a lock predicate.

On the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}`, take every unordered
6-site seed. New |S|. There are

```text
|S| = C(12,6) = 924
```

such seeds. Off-patch occupancy `0` is the explicit default used here; a
blank-block is a different rule and is not used.

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently if
`n_μ = c_{+μ} − c_{-μ}` is nonzero on at least one axis. This is **not** Hamming parity. In remaining-bit order `(wt1, opp2, adj2, vertex3, mixed3)`
one has `f_L1 = (1, 0, 1, 1, 1)`.

The displayed comparison map is the F_cut member `f0 = (1, 1, 1, 1, 0)`.
Do not adopt a map. Do not write them into Admissibility.

Let `M_f` be the set of 6-site seeds from which `f` does not fill all twelve
vertices. Independent occupancy-to-lock runs give

```text
cov6(f_L1) = 920,   |M_L1| = 4,
|M_f0| = 20,
|M_L1 ∩ M_f0| = 0,
equality bit = 0.
```

So the 6-site miss set of `f_L1` is not equal to the 6-site miss set of
F_cut `(1,1,1,1,0)`. The four-site comparison is a different `|S|` and is
not reused as a leftover. Do not list the seeds. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two 6-site miss-set cardinalities, their intersection, and the equality bit are exact finite enumerations on the declared two-cube. No physical lock map is selected."
trace_class: upstream_support
target_claim_id: f_cut_six_site_miss_set_comparison
target_blocker_text: "at the first unique coverage size above 4, is L1's miss set a theorem of mixed3=0?"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "keep both maps displayed; do not promote mixed3=0 or n≠0 to the physical Admissibility rule from this finite comparison"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0 and seed size 6; no physical law selection"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies the cubic lattice, nearest-neighbor adjacency, and
proper cubic rotations. Admissibility supplies one fixed covariant
nearest-neighbor rule, not the lock predicate used here.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the twelve-vertex two-cube `{0,1,2}×{0,1}×{0,1}` inside `Z^3`;
- the six signed coordinate directions as the nearest-neighbor stencil;
- off-patch occupancy `0` for any neighbor outside the two-cube;
- the ten axis-type orbits of `{0,1}^6` under the 24 proper cube rotations;
- the F_cut class: cube-covariant maps with `f(empty)=f(full)=0` and
  `f(c)=f(1-c)`;
- remaining-bit order `(wt1, opp2, adj2, vertex3, mixed3)` for the five free
  F_cut bits;
- occupancy-to-lock: a vacant two-cube site locks at the next tick iff the
  lock predicate returns 1 on its six-neighbor occupancy.

No observational comparator, literature constant, or Record scalar is
imported. A site with no record cannot be read; the present dynamics only
track which two-cube sites are locked.

## Exact target and objects

**Target.** On this two-cube, compute the 6-site miss sets of `f_L1` and of
`f0`, report `|M_f0|`, report `|M_L1 ∩ M_f0|`, and display the equality bit.

An axis type of a six-bit occupancy `c` is the triple

```text
(n_unbalanced, n_both, n_empty),
```

counting axes with `c_+ ≠ c_-`, axes with both ends occupied, and axes with
both ends empty. Complement swaps occupied and empty balanced axes.

`f_L1(c)=1` if and only if some axis is unbalanced. Equivalently,
`n_μ = c_{+μ} − c_{-μ}` is nonzero on at least one axis. This is **not** Hamming parity `|c|_1 mod 2`. The remaining-bit tuple is `(1, 0, 1, 1, 1)`.

`f0` is the F_cut map with remaining-bit tuple `(1, 1, 1, 1, 0)`: it fires
on every remaining orbit except mixed3. Empty and full stay 0, and complement
pairs agree.

A seed fills when iterated occupancy-to-lock, starting from that seed and
off-patch occupancy `0`, locks all twelve two-cube sites. Halt is a fixed
locked set of size less than 12, or a 13-tick bound that is never met on
this finite arena.

```text
M_f = { T ⊂ two-cube : |T|=6 and f does not fill from T }.
```

The seeds themselves are not listed.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| fix the two-cube and off-patch rule | twelve vertices; off-patch occupancy `0`; blank-block is a different rule |
| enumerate 6-site seeds | `|S| = C(12,6) = 924` |
| define `f_L1` as `n≠0` | 1 iff some axis is unbalanced; not Hamming |
| define `f0` as remaining bits `(1, 1, 1, 1, 0)` | F_cut member; mixed3 = 0; displayed, not adopted |
| reconfirm `|M_L1|` | `|M_L1| = 4`, so `cov6(f_L1) = 920` |
| compute `|M_f0|` | Theorem 1: `|M_f0| = 20` |
| compute the intersection and equality | Theorem 2: `|M_L1 ∩ M_f0| = 0`, so the sets are not equal |
| display the equality bit | Theorem 3: equality bit = 0 |
| list the missed seeds | refused; Do not list the seeds |
| adopt either map as the physical rule | refused; Do not adopt a map |

Every leaf needed for the stated finite comparison is discharged. Adoption
and seed listing are outside the target.

## Theorem 1 — `|M_f0|`

The two-cube has twelve sites and `|S| = 924` unordered 6-site seeds.
Independent occupancy-to-lock runs of `f_L1` reconfirm

```text
cov6(f_L1) = 920,   |M_L1| = 4.
```

The same enumeration for `f0` gives

```text
|M_f0| = 20.
```

Equivalently `cov6(f0) = 904`. Both maps lie in F_cut. They differ on the
mixed3 orbit, so they are not the same remaining-bit tuple.

This is a new `|S|`. It is not a leftover table from the 4-site miss-set
comparison.

## Theorem 2 — intersection and equality

The same 924 seeds, scored independently under both maps, give

```text
|M_L1 ∩ M_f0| = 0.
```

Therefore `M_L1 ≠ M_f0`. In particular `M_L1` is not a subset of `M_f0`,
and mixed3 = 0 is not a theorem of the 6-site miss set of `f_L1`.

The 4-site comparison is a different seed size. Its intersection count is
not transferred.

## Theorem 3 — equality bit

Display the equality bit. It is

```text
equality bit = 0.
```

The 6-site miss set of `f_L1` is not equal to the 6-site miss set of
F_cut `(1,1,1,1,0)`. Do not list the seeds. Do not adopt a map. Displayed,
not adopted.

## No-Go Discipline Gate

The only negative statement is the finite equality bit: on this two-cube,
these two 6-site miss sets are not equal. No wall is claimed about all
physical Admissibility rules.

### N1 — alternative route enumeration

| route | what it would attempt | why it fails here | marker |
|---|---|---|---|
| transfer the 4-site intersection | treat a 4-site overlap as forcing 6-site set equality | different `|S|`; the 6-site intersection is independently 0 | **ATTEMPTED** |
| mixed3 = 0 as a miss-set theorem | identify `M_L1` with the miss set of remaining bits `(1,1,1,1,0)` | `|M_L1|=4`, `|M_f0|=20`, intersection 0 | **ATTEMPTED** |
| replace `f_L1` by Hamming parity | score misses with `|c|_1 mod 2` | `f_L1` is `n≠0`; Hamming is a different map | **ATTEMPTED** |
| infer set equality from coverage ranks | conclude equality from `cov6` numbers alone | coverage counts do not determine set identity; the intersection is computed | **ATTEMPTED** |
| adopt `f0` or `f_L1` as Admissibility | write either remaining-bit tuple into the axiom | the axiom supplies a covariant rule, not this lock map | **ATTEMPTED** |
| leftover-character listing | replace the set comparison by a leftover row table | the object is cardinalities and the equality bit | **ATTEMPTED** |

### N2 — wall-independence audit

No independent walls are claimed. The inequality is one finite bit on one
declared arena. Collapsed wall count: 0.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| twelve-vertex two-cube | explicit arena, not a hidden `Z^3`-wide claim |
| off-patch occupancy `0` | explicit default; blank-block is a different rule |
| seed size 6 | explicit new `|S|` |
| F_cut remaining bits | explicit class coordinates |
| occupancy-to-lock | explicit discrete dynamics |
| “displayed, not adopted” | scope limit, not a hidden selector |

### N4 — citation-to-residual matching

| Evidence path | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Lattice paragraph | ambient lattice and rotations | the two-cube sits in `Z^3` with the six-direction stencil | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` Admissibility paragraph | covariant nearest-neighbor rule | used only as parent authority; no physical rule is selected | yes; adoption stays open |
| this note's companion runner | 6-site miss-set comparison | `|M_f0|`, intersection, equality bit | yes |

No earlier 4-site count is used as a substitute for the 6-site enumeration.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 neighbor 6-tuples | each map is constant on axis-type orbits |
| per site | yes: all twelve two-cube vertices | the same stencil is used at each vertex |
| per mode | yes: `f_L1` and `f0` | both maps are scored on every 6-site seed |
| per block | yes: the two miss sets | `|M_f0|=20`, intersection 0, equality bit 0 |
| lattice wide | no | no `Z^3`-wide formation law or physical selector is asserted |

### N6 — partial closure and primitive scan

The only dependency is the registered `minimal_axioms` node. No approved
primitive is used or added. No axiom or approved primitive is added.
Convention-renaming of remaining bits would not identify the two miss sets.

### N7 — hostile steelman

The strongest objection is that emptiness of the intersection is an artifact
of the twelve-vertex two-cube, so a larger fragment or a two-cube-preserving
orbit quotient might still make the missed *types* coincide even if the raw
seeds do not. That objection changes the object. The theorem compares the
raw 6-site seed sets on the declared arena and reports they are not equal.
It does not classify orbit types and does not lift the bit to `Z^3`.

### N8 — cross-cycle echo

A 4-site miss-set comparison on the same arena already failed equality:
`|M_L1|=6` and `|M_f0|=36` met in four seeds, not in the whole L1 miss set.
The 2-site maximizer `f0` has an empty 2-site miss set while `f_L1` misses
four 2-site seeds. Those are different `|S|` values. None of them replaces
the 6-site computation, and none of them makes the 6-site sets equal.

No-Go Discipline disposition: **PASS** for the narrow finite inequality
`M_L1 ≠ M_f0` on 6-site seeds.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner Contract

The companion runner rebuilds the axis-type orbits, confirms `f_L1` is the
unbalanced-axis predicate and is not Hamming, confirms `f0` has remaining
bits `(1, 1, 1, 1, 0)`, enumerates all 924 six-site seeds, computes both
miss-set cardinalities and their intersection, and displays the equality
bit. It does not print the missed seeds. Declared audit inputs are this
note and the axiom memo.

```text
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_L1_F0_SIX_SITE_MISS_SET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
```

## What is not claimed

The theorem does not select a physical Admissibility rule, a formation
process, a rate, or a `Z^3`-wide lock law. It does not list the seeds. It
does not adopt a map. Displayed, not adopted.
