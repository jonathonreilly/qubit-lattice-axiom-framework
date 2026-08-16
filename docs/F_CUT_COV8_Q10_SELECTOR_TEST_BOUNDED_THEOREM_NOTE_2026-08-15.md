---
claim_id: f_cut_cov8_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov8>0 equals adj2∨vertex3∨mixed3 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov8_q10_selector_test_2026_08_15.py
---

# Whether `cov8>0` Equals `adj2 ∨ vertex3 ∨ mixed3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 8-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored on every one
of the 32 cube-covariant cut maps `F_cut`. The scored identity is
whether `cov8>0` if and only if the displayed three-bit OR
`Q10 := adj2 ∨ vertex3 ∨ mixed3` holds.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov8_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov8_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 named that `cov10>0` if and only if
`Q10 := adj2 ∨ vertex3 ∨ mixed3`. Investment #6539 named that
`Q8 := wt1 ∨ adj2 ∨ opp2 ∨ vertex3` equals `cov8>0`. This note tests
whether the same displayed `Q10` also equals `cov8>0`. New predicate
versus an already named k=8 selector. Not leftover-character of #6539
and not leftover-character of c10bit3.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple has `adj2=vertex3=mixed3=1`,
so `Q10(f_L1)=1`.

On the two-cube with off-patch `o=0`, write
`cov8(f) = |{S : |S|=8 and f fills from S}|`. There are `C(12,8)=495`
eight-site seeds. The boolean scored here is `cov8(f)>0`.

**Theorem 1.** Among all 32 `F_cut` maps, `cov8>0` is not equivalent to
`Q10`. The identity fails. The lex-first remaining-bit miss is
`(0, 0, 0, 0, 1)`: that map has `Q10=1` and `cov8=0`.

**Theorem 2.** The three census integers on the 32-map set are

```text
N_pos = 30
N_Q10 = 28
N_both = 27.
```

**Theorem 3.** The identity is displayed only. Displayed, not adopted.
Do not adopt Q10. Do not write `Q10` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are scored exactly on the 495 eight-site seeds. Whether cov8>0 equals adj2 or vertex3 or mixed3 is a finite Boolean identity on this patch, and it fails. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov8_q10_selector_test
target_blocker_text: "whether cov8>0 equals adj2 or vertex3 or mixed3 among the 32 F_cut maps after Q8 already names cov8>0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded cov8>0 versus Q10 identity; do not adopt Q10"
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
predicate. The three remaining bits below are displayed remaining-bit
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

The eight-site seeds are the `C(12,8) = 495` subsets of size 8 in `T`.
Then `cov8(f)` is the number of those subsets from which `f` fills. The
boolean scored here is `cov8(f)>0`.

`Q10` is the remaining-bit predicate

```text
Q10(f) := (adj2=1) or (vertex3=1) or (mixed3=1).
```

It holds on exactly 28 of the 32 maps: the four maps with
`(adj2, vertex3, mixed3) = (0, 0, 0)` are `Q10=0`. `Q8` is the already
named k=8 selector `wt1 ∨ adj2 ∨ opp2 ∨ vertex3`. Duality is not
assumed: `cov8` is scored on the 495 eight-site seeds.

## Theorem 1 — `cov8>0` versus `Q10` on all 32

Direct evolution on the 495 eight-site seeds scores every `F_cut` map.
The identity

```text
cov8(f) > 0  ⇔  Q10(f) = 1
```

fails. The lex-first remaining-bit miss is `(0, 0, 0, 0, 1)`: `Q10=1`
and `cov8=0`. That map is mixed3-only. The two maps with `cov8=0` are

```text
(0, 0, 0, 0, 0), (0, 0, 0, 0, 1).
```

The three `Q10`-false maps that still have `cov8>0` are
`(0, 1, 0, 0, 0)`, `(1, 0, 0, 0, 0)`, and `(1, 1, 0, 0, 0)`. Those four
mismatches are why `Q10` is not the already named k=8 positivity
selector. In particular `f_L1 = (1, 0, 1, 1, 1)` has `Q10=1` and
`cov8=494 > 0`, so it is not a miss.

## Theorem 2 — the three census integers

Write `N_pos` for the number of `F_cut` maps with `cov8>0`, `N_Q10` for
the number with `Q10=1`, and `N_both` for the number with both. Then

```text
N_pos = 30
N_Q10 = 28
N_both = 27.
```

These three integers are counted from the scored 32-map table. They
fail to coincide because the identity of Theorem 1 fails: one `Q10`
map has `cov8=0`, and three positive maps have `Q10=0`.

## Theorem 3 — display, not adoption

The failure of `cov8>0 ⇔ Q10` on all 32 `F_cut` maps is displayed
data. Displayed, not adopted. Do not adopt Q10. Do not adopt a bit. Do
not adopt `adj2`. Do not adopt `vertex3`. Do not adopt `mixed3`. Do not
adopt `Q8`. Do not adopt `f_L1`. Do not write `Q10` into Admissibility.
Admissibility does not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q10` as `adj2=1` or `vertex3=1` or `mixed3=1` | twenty-eight maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch `o=0` | declared finite patch |
| `cov8>0` iff `Q10` on those 32 | fails; lex-first miss `(0, 0, 0, 0, 1)` |
| `N_pos`, `N_Q10`, `N_both` | 30, 28, 27 |
| leftover of #6539 | refused; that named `Q8=cov8>0` |
| leftover of c10bit3 | refused; that named `Q10=cov10>0` |
| adoption of `Q10` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6539: that closed `cov8>0` as
`Q8 := wt1 ∨ adj2 ∨ opp2 ∨ vertex3`. The present object is whether the
c10bit3 predicate `Q10` also equals eight-site positivity. New
predicate versus an already named k=8 selector.

Not leftover-character of c10bit3: that closed `cov10>0` as `Q10`.
The present object is the same displayed formula against `cov8>0`, not
a restatement of the ten-site identity.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt Q10.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov8>0` equals `Q10` among all 32 `F_cut` maps. |
| V2 | Current main has the axiom memo and the named `Q8=cov8>0` identity, but no landed `Q10`-versus-`cov8>0` test. |
| V3 | The 32 maps and 495 seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a new displayed predicate. |
| V5 | The identity fails, is displayed, and `Q10` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `Q10` is not `cov8>0` among the 32
`F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6539 | treat the `Q10` test as leftover-character of `Q8=cov8>0` | **ATTEMPTED** |
| leftover of c10bit3 | treat the `k=8` test as leftover-character of `Q10=cov10>0` | **ATTEMPTED** |
| adopt Q10 | write `Q10` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the #6539 `Q8` identity, the c10bit3 `cov10`
identity, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
three-bit OR `adj2=1` or `vertex3=1` or `mixed3=1` are declared.
Equality of `Q10` with `cov8>0` is not silently assumed. Duality is
not assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov8>0` equals `Q10` on all 32 `F_cut` maps, not leftover-character
of #6539 and not leftover-character of c10bit3.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the 32 `F_cut` maps scored on 495 seeds | no physical law selection |
| per block | the `cov8>0`–`Q10` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q10`, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c10bit3 already recorded that `Q10` is positivity at
`k=10`, and #6539 already named a remaining-bit OR for `cov8>0`, so
`Q10` must also be the k=8 positivity selector.

**Answer:** `Q10` fails at `k=8`. `N_pos = 30`, `N_Q10 = 28`, and
`N_both = 27`. The lex-first miss is `(0, 0, 0, 0, 1)`. The already
named k=8 selector is `Q8`, not `Q10`. Do not adopt Q10.

### N8 — cross-cycle echo

Investment #6539 already showed that `cov8>0` is `Q8`. Investment
c10bit3 already showed that `cov10>0` is `Q10`. Echoing either fact
is not a substitute for testing `cov8>0` against `Q10` on all 32.
New predicate versus an already named k=8 selector.

No-Go Discipline disposition: **PASS** for the finite 32-map census
and the displayed failed identity. FAIL / DO NOT SHIP for
“adopt Q10,” “`Q10` is the physical rule,” or “write `Q10` into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov8` on
the 495 eight-site seeds, decides whether `cov8>0` if and only if
`Q10`, reports the lex-first miss if the identity fails, and reports
`N_pos`, `N_Q10`, and `N_both`. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.
