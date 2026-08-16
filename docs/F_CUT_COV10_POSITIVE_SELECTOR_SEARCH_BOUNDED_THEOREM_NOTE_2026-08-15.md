---
claim_id: f_cut_cov10_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov10>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov10_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search for a Positive 10-Site Coverage Selector

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 66 ten-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against a displayed remaining-bit
family.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov10_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov10_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6494 showed that `P = cov2>0`, with
`P := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`. Investment #6476 showed
that `Max(k)=Max(12-k)` only for `k=4,5`. This note searches a new displayed
family on the ten-site seeds: `P`, `Q4`, each 1-bit, and every 2-bit OR of
the five remaining bits. New k-selector after `P=cov2>0`. Duality is not
assumed: the search does not import Max(k)=Max(12-k).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov10(f) = |{S : |S|=10 and f fills from S}|`. The boolean scored here is
`cov10(f)>0`. Then:

- Theorem 1. None of the displayed remaining-bit predicates equals `cov10>0`.
  The lex-first remaining-bit miss of each displayed `Q` is named below.
- Theorem 2. `N_pos = 28`. For each displayed `Q`, `N_Q` and `N_both` are
  reported below.
- Theorem 3. The displayed family is displayed. Displayed, not adopted.
  Do not adopt a bit.

Do not write any displayed remaining-bit formula into Admissibility. The
extra that would have made `P`, `Q4`, a 1-bit, or a 2-bit OR the positivity
selector at `k=10` is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 66 ten-site seeds of the two-cube. Whether any displayed remaining-bit predicate equals cov10>0, and the counts N_pos, N_Q, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov10_positive_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov10>0 among the 32 F_cut maps after P=cov2>0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded remaining-bit search against cov10>0; do not adopt a displayed bit"
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
predicate. No displayed remaining-bit formula is axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different rule and is not used.

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

The ten-site seeds are the `C(12,10) = 66` subsets of size 10 in `T`. Then
`cov10(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov10(f)>0`. Duality is not assumed: `cov10` is scored on
those 66 seeds and does not import `Max(k)=Max(12-k)`.

The displayed remaining-bit family, in this order, is:

1. `P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`;
2. `Q4(f) := (wt1 = 1) or (adj2 = 1)`;
3. each 1-bit: `bit:wt1`, `bit:opp2`, `bit:adj2`, `bit:vertex3`, `bit:mixed3`;
4. every 2-bit OR: `wt1|opp2`, `wt1|adj2`, `wt1|vertex3`, `wt1|mixed3`,
   `opp2|adj2`, `opp2|vertex3`, `opp2|mixed3`, `adj2|vertex3`,
   `adj2|mixed3`, `vertex3|mixed3`.

Displayed, not adopted. `wt1|adj2` is the same formula as `Q4`.

## Theorem 1 — none of the displayed Q equals `cov10>0`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov10` on the 66
ten-site seeds. For each displayed `Q`, compare the set of maps with
`Q` true to the set of maps with `cov10>0`.

None of the displayed remaining-bit predicates equals `cov10>0`.

The four maps with `cov10 = 0` are

```text
(0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (1, 0, 0, 0, 0), (1, 1, 0, 0, 0).
```

They are exactly the maps with `(adj2, vertex3, mixed3) = (0, 0, 0)`. The
fourteen `P`-false maps that still have `cov10>0` begin at the lex-first
miss `(0, 0, 0, 0, 1)`.

The lex-first remaining-bit miss of each displayed `Q`, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is:

- `P`: lex-first miss `(0, 0, 0, 0, 1)`
- `Q4`: lex-first miss `(0, 0, 0, 0, 1)`
- `bit:wt1`: lex-first miss `(0, 0, 0, 0, 1)`
- `bit:opp2`: lex-first miss `(0, 0, 0, 0, 1)`
- `bit:adj2`: lex-first miss `(0, 0, 0, 0, 1)`
- `bit:vertex3`: lex-first miss `(0, 0, 0, 0, 1)`
- `bit:mixed3`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1|opp2`: lex-first miss `(0, 0, 0, 0, 1)`
- `wt1|adj2`: lex-first miss `(0, 0, 0, 0, 1)`
- `wt1|vertex3`: lex-first miss `(0, 0, 0, 0, 1)`
- `wt1|mixed3`: lex-first miss `(0, 0, 0, 1, 0)`
- `opp2|adj2`: lex-first miss `(0, 0, 0, 0, 1)`
- `opp2|vertex3`: lex-first miss `(0, 0, 0, 0, 1)`
- `opp2|mixed3`: lex-first miss `(0, 0, 0, 1, 0)`
- `adj2|vertex3`: lex-first miss `(0, 0, 0, 0, 1)`
- `adj2|mixed3`: lex-first miss `(0, 0, 0, 1, 0)`
- `vertex3|mixed3`: lex-first miss `(0, 0, 1, 0, 0)`

## Theorem 2 — `N_pos` and, for each displayed Q, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 28` maps have `cov10>0`.

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number of maps with both `Q` true and `cov10>0`:

- `P`: N_Q = 14, N_both = 14
- `Q4`: N_Q = 24, N_both = 22
- `bit:wt1`: N_Q = 16, N_both = 14
- `bit:opp2`: N_Q = 16, N_both = 14
- `bit:adj2`: N_Q = 16, N_both = 16
- `bit:vertex3`: N_Q = 16, N_both = 16
- `bit:mixed3`: N_Q = 16, N_both = 16
- `wt1|opp2`: N_Q = 24, N_both = 21
- `wt1|adj2`: N_Q = 24, N_both = 22
- `wt1|vertex3`: N_Q = 24, N_both = 22
- `wt1|mixed3`: N_Q = 24, N_both = 22
- `opp2|adj2`: N_Q = 24, N_both = 22
- `opp2|vertex3`: N_Q = 24, N_both = 22
- `opp2|mixed3`: N_Q = 24, N_both = 22
- `adj2|vertex3`: N_Q = 24, N_both = 24
- `adj2|mixed3`: N_Q = 24, N_both = 24
- `vertex3|mixed3`: N_Q = 24, N_both = 24

The row `wt1|adj2` recovers the `Q4` counts `N_Q = 24`, `N_both = 22`
against the same `N_pos = 28`. No displayed row has `N_Q = N_both = N_pos`.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, has `cov10 = 66 > 0`. That
is consistent with Theorem 2 and does not restore equality for any
displayed `Q`.

## Theorem 3 — display; do not adopt a bit

Every predicate above is displayed. Displayed, not adopted. Do not adopt a
bit. Do not write any displayed remaining-bit formula into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 66 ten-site seeds, off-patch `o=0` | declared finite patch |
| displayed `P`, `Q4`, 1-bit, 2-bit OR family | displayed, not adopted |
| some displayed `Q` equals `cov10>0` | fails; none; lex-first miss of each named |
| `N_pos = 28` and per-`Q` `N_Q`, `N_both` | proved by exhaustive scoring |
| leftover-character of #6494 | refused; new k-selector after `P=cov2>0` |
| leftover-character of #6476 | refused; duality is not assumed |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6494: that closed `cov2>0` as `P`, with
`P := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`. The present object is a
search over a displayed remaining-bit family on the ten-site seeds, not a
restatement that `P` equals two-site positivity.

Not leftover-character of #6476: that closed `Max(k)=Max(12-k)` only for
`k=4,5`. Duality is not assumed here. New k-selector: `cov10` is scored on
the 66 ten-site seeds and does not import `Max(k)=Max(12-k)`.

The note is not a Max(10) ranking and not a seed-table: maximizers of
`cov10` are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt a bit.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit predicate equals `cov10>0` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6494 fact that `P=cov2>0`, but no landed remaining-bit search at `k=10`. |
| V3 | The 32 maps, 66 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a displayed remaining-bit family. |
| V5 | Equality fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: none of the displayed remaining-bit
predicates equals `cov10>0` among the 32 `F_cut` maps on this patch. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6494 | treat the search as leftover-character of `P=cov2>0` | **ATTEMPTED** |
| leftover of #6476 | replace the `k=10` score by `Max(k)=Max(12-k)` | **ATTEMPTED** |
| adopt a bit | write a displayed remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed equalities, the Hamming contrast, the #6494 `P` identity, the
#6476 Max restriction, and the off-patch convention are distinct. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 66 ten-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
family are declared. Equality of any displayed `Q` with `cov10>0` is not
silently assumed. Duality is not assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether a displayed
remaining-bit predicate equals 10-site positivity on the declared patch, not
leftover-character of #6494, and not a Max-duality ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 66 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `N_Q`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector outside the displayed remaining-bit family, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** after `P=cov2>0`, and with Max duality only at `k=4,5`, a
1-bit, `P`, `Q4`, or some 2-bit OR must be the positivity selector at
`k=10`.

**Answer:** None of those seventeen displayed predicates equals `cov10>0`.
`N_pos = 28`. `P` has `N_Q = 14` and `N_both = 14`. `Q4` has `N_Q = 24`
and `N_both = 22`. The closest 2-bit OR rows have `N_Q = 24` and
`N_both = 24`, and still miss `(0, 0, 0, 0, 1)`, `(0, 0, 0, 1, 0)`, or
`(0, 0, 1, 0, 0)`. No bit is adopted.

### N8 — cross-cycle echo

Investment #6494 already showed that `cov2>0` is `P`. Echoing that
two-site identity is not a substitute for scoring the displayed
remaining-bit family at `k=10`: the seventeen lex-first misses and the
per-`Q` pair `(N_Q, N_both)` are the new search facts. Duality is not
assumed.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow equality failure. FAIL / DO NOT SHIP for “a displayed remaining-bit
predicate equals `cov10>0`” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov10` on the
66 ten-site seeds, compares positivity with each displayed remaining-bit
predicate, reports that none equals `cov10>0`, names the lex-first miss of
each displayed `Q`, and reports `N_pos = 28` together with per-`Q` `N_Q`
and `N_both`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.
