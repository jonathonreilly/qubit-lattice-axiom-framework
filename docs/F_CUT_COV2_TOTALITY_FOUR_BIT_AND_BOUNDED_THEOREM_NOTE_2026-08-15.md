---
claim_id: f_cut_cov2_totality_four_bit_and_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov2=66 is equivalent to wt1=1 and adj2=1 and opp2=1 and vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov2_totality_four_bit_and_2026_08_15.py
---

# Two-Site Totality Versus the Four-Bit AND on All 32 `F_cut` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 2-site coverage on the twelve-vertex
two-cube with off-patch occupancy `0`, scored on every one of the 32
cube-covariant cut maps `F_cut`. The scored identity is whether
`cov2=66` if and only if the four-bit remaining-bit AND
`Q66 := wt1 ∧ adj2 ∧ opp2 ∧ vertex3` holds.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov2_totality_four_bit_and_2026_08_15.py`](../scripts/f_cut_cov2_totality_four_bit_and_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment tot2opp named that, among the four tot `Q_*` maps
(`wt1=1`, `adj2=1`, and `vertex3=1`), `cov2=66` is equivalent to
`opp2=1`. That four-map slice together with `Q_*` is the four-bit AND

```text
Q66(f) := (wt1=1) ∧ (adj2=1) ∧ (opp2=1) ∧ (vertex3=1).
```

This note asks the new global question on the whole 32-map class:
whether two-site totality `cov2=66` is equivalent to `Q66`. New global
2-site totality selector, not a rename of the four-map tot2opp census
and not leftover-character of Max(2).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple has `wt1=adj2=vertex3=1`
and `opp2=0`, so `Q66(f_L1)=0`.

On the two-cube with off-patch `o=0`, write `cov2(f)` for the number of
two-site seeds from which `f` fills. There are `C(12,2)=66` two-site
seeds. Totality means `cov2(f)=66`.

**Theorem 1.** Among all 32 `F_cut` maps, cov2=66 is equivalent to
`Q66`. The two maps with `Q66=1` have `cov2=66`. The thirty maps with
`Q66=0` have `cov2<66`. There is no counterexample. Thus
`cov2=66` if and only if `Q66` on this 32-map set.

**Theorem 2.** The three census integers on the 32-map set are

```text
N_Q66 = 2
N_tot2 = 2
N_both = 2.
```

**Theorem 3.** The identity is displayed only. Do not adopt a bit. Do not
write `Q66` into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are scored exactly on the sixty-six two-site seeds. Equivalence of cov2=66 with the four-bit AND Q66 is a finite Boolean identity on this patch, and it holds. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov2_totality_four_bit_and
target_blocker_text: "whether cov2=66 is equivalent to wt1 and adj2 and opp2 and vertex3 among all 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded global two-site totality four-bit AND identity; do not adopt Q66"
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
predicate. The four remaining bits below are displayed remaining-bit
data, not axiom content.

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

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The two-site seeds are the sixty-six pairs `{x,y}` for distinct `x,y ∈ T`.
Then `cov2(f)` is the number of those pairs from which `f` fills. Totality
on this patch means `cov2(f)=66`.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. Tot `Q_*` is
the further cut `vertex3=1` inside `Q_*`. `Q66` is the further cut
`opp2=1` inside tot `Q_*`. It holds on exactly two of the 32 maps. The
present census scores every one of the 32 maps.

## Theorem 1 — two-site totality versus `Q66` on all 32

Direct evolution on the sixty-six two-site seeds scores every `F_cut`
map. The two remaining-bit tuples with `Q66=1` and their coverages are

```text
(1, 1, 1, 1, 0)  cov2=66  Q66=1
(1, 1, 1, 1, 1)  cov2=66  Q66=1
```

Those two are exactly Max(2). Every other remaining-bit tuple has
`Q66=0` and `cov2<66`. In particular `f_L1 = (1, 0, 1, 1, 1)` has
`Q66=0` and `cov2=62`. On this 32-map set, the identity

```text
cov2(f) = 66  ⇔  Q66(f) = 1
```

holds. Every map with `cov2=66` has `Q66=1`. Every map with `Q66=1`
has `cov2=66`. There is no lex-first counterexample: the thirty maps
with `Q66=0` fail totality.

## Theorem 2 — the three census integers

Write `N_Q66` for the number of `F_cut` maps with `Q66=1`, `N_tot2` for
the number with `cov2=66`, and `N_both` for the number with both. Then

```text
N_Q66 = 2
N_tot2 = 2
N_both = 2.
```

These three integers are counted from the scored 32-map table. They
coincide because the identity of Theorem 1 holds.

## Theorem 3 — display, not adoption

The success of `cov2=66 ⇔ Q66` on all 32 `F_cut` maps is displayed
data. Do not adopt a bit. Do not adopt `Q66`. Do not adopt `wt1`. Do
not adopt `adj2`. Do not adopt `opp2`. Do not adopt `vertex3`. Do not
adopt tot `Q_*`. Do not adopt `f_L1`. Do not write `Q66` into Admissibility. Admissibility does
not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q66` as `wt1=1`, `adj2=1`, `opp2=1` and `vertex3=1` | two maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| `cov2=66` iff `Q66` on those 32 | holds |
| `N_Q66`, `N_tot2`, `N_both` | 2, 2, 2 |
| leftover of tot2opp | refused; that named the four-map `opp2` census |
| leftover of Max(2) | refused; that named the two maps with `cov2=66` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot2opp: that named `cov2=66` iff `opp2=1`
inside the four tot `Q_*` maps. The present object is two-site totality
versus the four-bit AND on the whole 32-map class.

Not leftover-character of Max(2): that named the two maps with
`cov2=66`. The present object is whether those two are exactly the
`Q66=1` slice of all 32. On this 32-map set they are.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov2=66` is equivalent to `Q66` among all 32 `F_cut` maps. |
| V2 | Current main has the axiom memo and the tot2opp investment name, but no landed global two-site totality-versus-four-bit-AND census. |
| V3 | The 32 maps and sixty-six seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class. |
| V5 | The identity is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: a four-map tot2opp census is not a
32-map `Q66` identity, and a displayed remaining-bit census on `F_cut`
is not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of tot2opp | treat the 32-map iff as the already-named four-map `opp2` census | **ATTEMPTED** |
| leftover of Max(2) | treat the iff as a rename of the two Max(2) maps | **ATTEMPTED** |
| adopt the bit | write `Q66` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the four-map tot2opp census, the two-map Max(2)
set, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
four-bit AND `wt1=1`, `adj2=1`, `opp2=1` and `vertex3=1` are declared.
Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov2=66` equals `Q66` on all 32 `F_cut` maps, not leftover-character
of tot2opp and not a Max(2) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the 32 `F_cut` maps scored on 66 seeds | no physical law selection |
| per block | the two-site totality–`Q66` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q66`, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** tot2opp already recorded that the two tot `Q_*` maps with
`opp2=1` are exactly the `cov2=66` pair, so the 32-map iff is leftover.

**Answer:** tot2opp asked whether `cov2=66` equals `opp2=1` on four
maps. It did not score the other 28. The present object names the
identity `cov2=66 ⇔ Q66` on the whole 32-map set, reports `N_Q66`,
`N_tot2`, and `N_both`, and displays the four-bit AND without adopting
it.

### N8 — cross-cycle echo

Investment tot2opp already showed that `cov2=66` is `opp2=1` on tot
`Q_*`. Max(2) already named the two totality maps. Echoing either fact
is not a substitute for testing `cov2=66` against `Q66` on all 32.

No-Go Discipline disposition: **PASS** for the finite 32-map census
and the displayed identity. FAIL / DO NOT SHIP for
“adopt a bit,” “`Q66` is the physical rule,” or “write `Q66` into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov2` on
the sixty-six two-site seeds, decides whether `cov2=66` if and only if
`Q66`, reports the lex-first counterexample if the identity fails, and
reports `N_Q66`, `N_tot2`, and `N_both`. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no
audit verdict.
