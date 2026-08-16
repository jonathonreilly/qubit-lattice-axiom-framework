---
claim_id: f_cut_cov5_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov5>0 equals adj2∨vertex3∨mixed3 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov5_q10_selector_test_2026_08_15.py
---

# Q10 Selector Test For `cov5>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 5-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against the newly named
3-bit OR `Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov5_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov5_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 showed that `cov10>0` if and only if
`Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)`. Investment c5sel showed
that `N_pos = 21` and that `cov5>0` is not Q4, not Q6, and not a 1-bit
or 2-bit OR. This note asks a new `k` question: whether `cov5>0` equals
that newly named 3-bit OR. New k for the newly named 3-bit OR. Not
leftover-character of c10bit3. Not leftover-character of c5sel. not a Max(5) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov5(f) = |{S : |S|=5 and f fills from S}|`. Then:

- Theorem 1. `cov5>0` is not equivalent to `Q10`. One lex-first
  remaining-bit miss is reported.
- Theorem 2. `N_pos = 21`, `N_Q10 = 28`, and `N_both = 21`.
- Theorem 3. `Q10` is displayed. Do not adopt Q10.

Do not adopt a bit. Do not write a remaining-bit formula into
Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 792 five-site seeds of the two-cube. Whether cov5>0 equals Q10 is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov5_q10_selector_test
target_blocker_text: "whether cov5>0 equals adj2 or vertex3 or mixed3 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 5-site Q10 selector test; do not adopt Q10"
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
predicate. The displayed `Q10` formula is not axiom content.

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

The five-site seeds are the `C(12,5) = 792` subsets of size 5 in `T`. Then
`cov5(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov5(f)>0`. Duality is not assumed: `cov5` is scored on
those 792 seeds.

The displayed remaining-bit predicate is
`Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)`, equivalently
`adj2 OR vertex3 OR mixed3`. Displayed, not adopted.

## Theorem 1 — `cov5>0` is not equivalent to `Q10`; one lex-first miss

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov5` on the
792 five-site seeds. Then `cov5(f) > 0` is not equivalent to `Q10`.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 0, 0, 1)`: `cov5 = 0`
and `Q10` is true (`mixed3 = 1`). There is no miss in the opposite
direction: every map with `cov5 > 0` has `Q10` true.

| displayed `Q` | `cov5>0` iff `Q` | lex-first miss | `cov5` of miss | `Q` at miss |
|---|---|---|---:|---|
| `adj2 OR vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, has `Q10` true and
`cov5 = 792`. That is consistent with Theorem 1 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q10`, `N_both`

Among the 32 maps, `N_pos = 21` maps have `cov5 > 0`. Write `N_Q10` for
the number of maps with `Q10` true and `N_both` for the number with both
`Q10` and `cov5>0`. Then `N_Q10 = 28` and `N_both = 21`.

| displayed `Q` | `N_Q10` | `N_pos` | `N_both` |
|---|---:|---:|---:|
| `adj2 OR vertex3 OR mixed3` | 28 | 21 | 21 |

The four maps with `(adj2, vertex3, mixed3) = (0, 0, 0)` are `Q10`-false
and have `cov5 = 0`. The remaining twenty-eight maps are `Q10`-true.
Seven of those twenty-eight have `cov5 = 0`. The lex-first of those seven
is `(0, 0, 0, 0, 1)`. Equivalence would require
`(N_Q10, N_pos, N_both) = (21, 21, 21)` or `(28, 28, 28)`; the observed
triple is `(28, 21, 21)`.

## Theorem 3 — display; do not adopt Q10

`Q10`, the counts, and the lex-first miss are displayed data. Do not
adopt Q10. Do not adopt a bit. Do not adopt `f_L1`. Do not write a
remaining-bit formula into Admissibility. Admissibility does not name
these remaining-bit formulas.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 five-site seeds, off-patch `o=0` | declared finite patch |
| `cov5>0` versus `Q10` | not equivalent; lex-first miss reported |
| `N_pos = 21`, `N_Q10 = 28`, `N_both = 21` | proved by exhaustive scoring |
| leftover-character of c10bit3 or c5sel | refused; new `k` for the newly named 3-bit OR |
| adoption of `Q10` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c10bit3: that investment showed `cov10>0` iff
`Q10` on the same 32 maps. A ten-site positivity identity is not a
five-site positivity identity.

Not leftover-character of c5sel: that investment showed `N_pos = 21` and
that `cov5>0` is not Q4, not Q6, and not a displayed 1-bit or 2-bit OR.
The present count is a new `k` for the newly named 3-bit OR, not a
restatement of that first failed menu.

The note is not a Max(5) ranking and not a seed-table: maximizers of
`cov5` are not selected, and no seed census of a named map is compiled
beyond the positivity boolean.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write a remaining-bit formula into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov5>0` equals the newly named 3-bit OR `Q10` inside `F_cut` on this patch. |
| V2 | c10bit3 named `Q10` as the `cov10>0` selector. c5sel scored `cov5>0` against `Q4`, `Q6`, and the 1-bit / 2-bit OR menu. Current main has no landed focused `Q10` test at `k=5`. |
| V3 | The 32 maps, 792 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared newly named 3-bit OR. |
| V5 | Equivalence fails, one lex-first miss is reported, and `Q10` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov5>0` is not equivalent to `Q10`. The displayed OR is not adopted. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c10bit3 | treat the five-site test as a restatement of `cov10>0` iff `Q10` | **ATTEMPTED** |
| leftover of c5sel | treat the test as leftover-character of the failed `Q4` / 1-bit / 2-bit OR menu | **ATTEMPTED** |
| Max(5) rename | replace the fillability search by a maximum-`cov5` ranking | **ATTEMPTED** |
| adopt Q10 | write `Q10` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The `Q10` versus `cov5>0` test, the Hamming contrast, the c10bit3
ten-site identity, the c5sel first failed menu, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 five-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed `Q10` predicate are declared. Equivalence of `cov5>0` with
`Q10` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov5>0` equals the newly named 3-bit OR on the declared patch, a new
`k` after c10bit3 named that OR, and not a Max(5) ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 792 seeds | no physical law selection |
| per block | `N_pos`, `N_Q10`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector outside
`Q10`, and any independently derived physical map from `F_cut` into
Admissibility.

### N7 — hostile steelman

**Steelman:** c10bit3 already showed `cov10>0` iff `Q10`, and c5sel
already showed `N_pos = 21` with every displayed 1-bit / 2-bit OR and
`Q4` failing, so `Q10` must recover `cov5>0` and must be written into
Admissibility.

**Answer:** `Q10` has `(N_Q10, N_pos, N_both) = (28, 21, 21)`. Seven
`Q10`-true maps have `cov5 = 0`. The lex-first miss `(0, 0, 0, 0, 1)`
has `cov5 = 0` and `Q10` true. Displayed predicates are not adopted.

### N8 — cross-cycle echo

Investment c10bit3 already showed that `adj2 OR vertex3 OR mixed3`
equals `cov10>0`. Investment c5sel already showed that `cov5>0` is not
Q4 and that `N_pos = 21`. Echoing either fact is not a substitute for
the five-site `Q10` count: the failed equivalence, the lex-first miss,
and the triple `(N_Q10, N_pos, N_both)` are five-site facts.

No-Go Discipline disposition: **PASS** for the finite selector test and
the narrow nonequivalence report. FAIL / DO NOT SHIP for “`Q10` is the
physical rule” or “a displayed bit is adopted.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov5` on the
792 five-site seeds, tests `Q10` against `cov5>0`, reports that the
equivalence fails, reports the lex-first miss `(0, 0, 0, 0, 1)`, and
reports `N_pos = 21`, `N_Q10 = 28`, and `N_both = 21`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
