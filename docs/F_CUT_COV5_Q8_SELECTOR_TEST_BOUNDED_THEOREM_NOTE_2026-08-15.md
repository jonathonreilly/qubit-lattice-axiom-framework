---
claim_id: f_cut_cov5_q8_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov5>0 equals wt1∨adj2∨opp2∨vertex3, and whether positivity implies that OR, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov5_q8_selector_test_2026_08_15.py
---

# Whether `cov5>0` Equals `wt1 ∨ adj2 ∨ opp2 ∨ vertex3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 5-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored on every one
of the 32 cube-covariant cut maps `F_cut`. The scored identities are
whether `cov5>0` if and only if the displayed four-bit OR
`Q8 := wt1 ∨ adj2 ∨ opp2 ∨ vertex3` holds, and whether positivity
implies that OR.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov5_q8_selector_test_2026_08_15.py`](../scripts/f_cut_cov5_q8_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c3q8 showed that `cov3>0` implies
`Q8 := wt1 ∨ adj2 ∨ opp2 ∨ vertex3`. Investment c11q8 showed that
`cov11>0` also implies that same named OR. Investment c5sel showed
`N_pos = 21` and `N_Q8 = 30` in the remaining-bit menu. This note tests
whether the same displayed named `Q8` also equals `cov5>0`, and whether
five-site positivity still implies that OR. New k for the named 4-bit
OR. Not leftover-character of c5sel, not leftover-character of c3q8,
and not leftover-character of c11q8.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`. Mixed3 is
free.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple has `wt1=adj2=vertex3=1`,
so `Q8(f_L1)=1`.

On the two-cube with off-patch `o=0`, write
`cov5(f) = |{S : |S|=5 and f fills from S}|`. There are `C(12,5)=792`
five-site seeds. The boolean scored here is `cov5(f)>0`.

**Theorem 1.** Among all 32 `F_cut` maps, `cov5>0` is not equivalent to
`Q8`. The identity fails. The lex-first remaining-bit miss is
`(0, 0, 0, 1, 0)`: that map has `Q8=1` and `cov5=0`. Positivity does
imply `Q8`: no `Q8`-false map has `cov5>0`.

**Theorem 2.** The three census integers on the 32-map set are

```text
N_pos = 21
N_Q8 = 30
N_both = 21.
```

**Theorem 3.** The identity is displayed only. Displayed, not adopted.
Do not adopt Q8. Do not write `Q8` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are scored exactly on the 792 five-site seeds. Whether cov5>0 equals wt1 or adj2 or opp2 or vertex3, and whether positivity implies that OR, are finite Boolean facts on this patch. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov5_q8_selector_test
target_blocker_text: "whether cov5>0 equals wt1 or adj2 or opp2 or vertex3 among the 32 F_cut maps after Q8 already names a four-bit OR at k=3 and k=11"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded cov5>0 versus Q8 identity; do not adopt Q8"
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
`N_free = 5` and `|F_cut| = 32`. Mixed3 is free under `Q8`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The five-site seeds are the `C(12,5) = 792` subsets of size 5 in `T`.
Then `cov5(f)` is the number of those subsets from which `f` fills. The
boolean scored here is `cov5(f)>0`.

`Q8` is the remaining-bit predicate

```text
Q8(f) := (wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1).
```

It holds on exactly 30 of the 32 maps: the two maps with
`(wt1, opp2, adj2, vertex3) = (0, 0, 0, 0)` are `Q8=0`. Duality is not
assumed: `cov5` is scored on the 792 five-site seeds.

## Theorem 1 — `cov5>0` versus `Q8` on all 32

Direct evolution on the 792 five-site seeds scores every `F_cut` map.
The identity

```text
cov5(f) > 0  ⇔  Q8(f) = 1
```

fails. The lex-first remaining-bit miss is `(0, 0, 0, 1, 0)`: `Q8=1`
and `cov5=0`. That map is vertex3-only. The eleven maps with `cov5=0` are

```text
(0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (0, 0, 0, 1, 1),
(0, 1, 0, 0, 0), (0, 1, 0, 0, 1), (0, 1, 0, 1, 0), (0, 1, 0, 1, 1),
(1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 1, 0, 0, 0).
```

The nine mismatches are the `Q8`-true zeros `(0, 0, 0, 1, 0)`,
`(0, 0, 0, 1, 1)`, `(0, 1, 0, 0, 0)`, `(0, 1, 0, 0, 1)`,
`(0, 1, 0, 1, 0)`, `(0, 1, 0, 1, 1)`, `(1, 0, 0, 0, 0)`,
`(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 0)`. Every `Q8`-false map has
`cov5=0`, so positivity implies `Q8`. The converse fails. In particular
`f_L1 = (1, 0, 1, 1, 1)` has `Q8=1` and `cov5=792 > 0`, so it is not a
miss.

## Theorem 2 — the three census integers

Write `N_pos` for the number of `F_cut` maps with `cov5>0`, `N_Q8` for
the number with `Q8=1`, and `N_both` for the number with both. Then

```text
N_pos = 21
N_Q8 = 30
N_both = 21.
```

These three integers are counted from the scored 32-map table. They
fail to coincide because the identity of Theorem 1 fails: nine `Q8`
maps have `cov5=0`, and no positive map has `Q8=0`.

## Theorem 3 — display, not adoption

The failure of `cov5>0 ⇔ Q8` on all 32 `F_cut` maps, and the fact
that positivity implies `Q8`, are displayed data. Displayed, not adopted.
Do not adopt Q8. Do not adopt a bit. Do not adopt `wt1`. Do not adopt
`adj2`. Do not adopt `opp2`. Do not adopt `vertex3`. Do not adopt
`mixed3`. Do not adopt `f_L1`. Do not write `Q8` into Admissibility.
Admissibility does not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q8` as `wt1=1` or `adj2=1` or `opp2=1` or `vertex3=1` | thirty maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 five-site seeds, off-patch `o=0` | declared finite patch |
| `cov5>0` iff `Q8` on those 32 | fails; lex-first miss `(0, 0, 0, 1, 0)` |
| positivity implies `Q8` | holds; no `Q8`-false positive |
| `N_pos`, `N_Q8`, `N_both` | 21, 30, 21 |
| leftover of c5sel | refused; that closed `N_pos=21` and `N_Q8=30` |
| leftover of c3q8 | refused; that closed `cov3>0` implies `Q8` |
| leftover of c11q8 | refused; that closed `cov11>0` implies `Q8` |
| adoption of `Q8` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c5sel: that closed that `N_pos = 21` and
`N_Q8 = 30` in the remaining-bit menu. The present object is whether
the named c3q8/c11q8 predicate `Q8` equals five-site positivity. New k
for the named 4-bit OR.

Not leftover-character of c3q8: that closed that `cov3>0` implies `Q8`.
The present object is the same displayed formula against `cov5>0`, not
a restatement of the three-site implication.

Not leftover-character of c11q8: that closed that `cov11>0` implies
`Q8`. The present object is the same displayed formula against
`cov5>0`, not a restatement of the eleven-site implication.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt Q8.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov5>0` equals `Q8` among all 32 `F_cut` maps, and whether positivity implies `Q8`. |
| V2 | Current main has the axiom memo and the named `cov3>0` and `cov11>0` imply-`Q8` identities, but no landed `Q8`-versus-`cov5>0` test. |
| V3 | The 32 maps and 792 seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a new displayed predicate. |
| V5 | The identity fails, positivity implies `Q8`, both facts are displayed, and `Q8` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `Q8` is not `cov5>0` among the 32
`F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c5sel | treat the `Q8` test as leftover-character of the `N_pos=21` and `N_Q8=30` menu | **ATTEMPTED** |
| leftover of c3q8 | treat the `k=5` test as leftover-character of `cov3>0` implies `Q8` | **ATTEMPTED** |
| leftover of c11q8 | treat the `k=5` test as leftover-character of `cov11>0` implies `Q8` | **ATTEMPTED** |
| adopt Q8 | write `Q8` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the c5sel `N_pos=21` and `N_Q8=30` menu, the
c3q8 three-site implication, the c11q8 eleven-site implication, and
the off-patch convention are distinct. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 five-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
four-bit OR `wt1=1` or `adj2=1` or `opp2=1` or `vertex3=1` are declared.
Equality of `Q8` with `cov5>0` is not silently assumed. Duality is
not assumed. Mixed3 is free.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov5>0` equals `Q8` on all 32 `F_cut` maps, and whether positivity
implies that OR, not leftover-character of c5sel, not leftover-character
of c3q8, and not leftover-character of c11q8.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the 32 `F_cut` maps scored on 792 seeds | no physical law selection |
| per block | the `cov5>0`–`Q8` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q8`, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c3q8 and c11q8 already recorded that positivity at `k=3`
and `k=11` implies `Q8`, and c5sel already scored `N_pos = 21` with
`N_Q8 = 30`, so naming `Q8` at `k=5` cannot add a fact.

**Answer:** `Q8` fails to equal `cov5>0`. `N_pos = 21`, `N_Q8 = 30`,
and `N_both = 21`. The lex-first miss is `(0, 0, 0, 1, 0)`. Positivity
implies `Q8`, but `Q8` is not `cov5>0`. New k for the named 4-bit
OR. Do not adopt Q8.

### N8 — cross-cycle echo

Investment c5sel already showed `N_pos = 21` and `N_Q8 = 30`.
Investment c3q8 already showed that `cov3>0` implies `Q8`.
Investment c11q8 already showed that `cov11>0` implies `Q8`. Echoing
any of those facts is not a substitute for testing `cov5>0` against
named `Q8` on all 32. New k for the named 4-bit OR.

No-Go Discipline disposition: **PASS** for the finite 32-map census
and the displayed failed identity. FAIL / DO NOT SHIP for
“adopt Q8,” “`Q8` is the physical rule,” or “write `Q8` into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov5` on
the 792 five-site seeds, decides whether `cov5>0` if and only if
`Q8`, reports the lex-first miss if the identity fails, reports whether
positivity implies `Q8`, and reports `N_pos`, `N_Q8`, and `N_both`.
Declared audit inputs are this note and the axiom memo; the runner
writes no cache and authors no audit verdict.
