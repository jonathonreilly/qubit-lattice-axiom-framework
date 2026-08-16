---
claim_id: f_cut_cov5_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov5>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov5_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search For A Selector Equal To `cov5>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 5-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q4`,
displayed `Q6`, and every displayed 1-bit or 2-bit remaining-bit OR.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov5_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov5_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6518 showed that `cov4>0` if and only if
`Q4(f) := (wt1=1) or (adj2=1)`. Investment #6531 showed that `cov6>0` if
and only if `Q6(f) := (wt1=1) or (adj2=1) or (vertex3=1)`. Investment
#6476 showed that `Max(k)=Max(12-k)` only for `k=4,5`. This note asks a
new `k` question: whether `cov5>0` equals `Q4`, equals `Q6`, or equals
any displayed 1-bit remaining-bit predicate or any displayed 2-bit OR.
New k. Not leftover-character of those three investments and not a
Max(5) rename.

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

- Theorem 1. `cov5>0` is not equivalent to `Q4`, not equivalent to `Q6`,
  and not equivalent to any displayed 1-bit predicate or 2-bit OR. One
  lex-first remaining-bit miss is reported for each displayed `Q`.
- Theorem 2. `N_pos = 21`. For each displayed `Q`, the pair
  `(N_Q, N_both)` is reported in the table below.
- Theorem 3. The menu is displayed. Do not adopt a bit.

Do not adopt Q4. Do not adopt Q6. Do not write a remaining-bit formula
into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 792 five-site seeds of the two-cube. Whether cov5>0 equals Q4, Q6, or any displayed 1-bit or 2-bit OR is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov5_positive_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov5>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 5-site positivity selector search; do not adopt a displayed bit"
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
predicate. The candidates below are displayed remaining-bit formulas, not
axiom content.

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
scored here is `cov5(f)>0`.

The displayed remaining-bit predicates are:

```text
Q4(f) := (wt1 = 1) or (adj2 = 1).
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1).
```

together with each standalone remaining bit and each OR of two remaining
bits, in remaining-bit order. `Q4` is the same formula as `wt1 OR adj2`.
Displayed, not adopted.

## Theorem 1 — no displayed `Q` equals `cov5>0`; one lex-first miss each

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov5` on the
792 five-site seeds. Then `cov5(f) > 0` is not equivalent to `Q4`, is not
equivalent to `Q6`, and is not equivalent to any displayed 1-bit
predicate or 2-bit OR.

`N_pos = 21`. The lex-first remaining-bit miss of each displayed `Q`, in
the order `(wt1, opp2, adj2, vertex3, mixed3)`, is:

| displayed `Q` | `cov5>0` iff `Q` | lex-first miss | `cov5` of miss | `Q` at miss |
|---|---|---|---:|---|
| `wt1` | no | `(0, 0, 1, 0, 0)` | 168 | 0 |
| `opp2` | no | `(0, 0, 1, 0, 0)` | 168 | 0 |
| `adj2` | no | `(1, 0, 0, 1, 0)` | 208 | 0 |
| `vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `wt1 OR opp2` | no | `(0, 0, 1, 0, 0)` | 168 | 0 |
| `wt1 OR adj2` | no | `(1, 0, 0, 0, 0)` | 0 | 1 |
| `wt1 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `wt1 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `opp2 OR adj2` | no | `(0, 1, 0, 0, 0)` | 0 | 1 |
| `opp2 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `opp2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `adj2 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `adj2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `Q4` | no | `(1, 0, 0, 0, 0)` | 0 | 1 |
| `Q6` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |

The named `Q4` miss is remaining bits `(1, 0, 0, 0, 0)`: `Q4` is true and
`cov5 = 0`. The named `Q6` miss is remaining bits `(0, 0, 0, 1, 0)`: `Q6`
is true and `cov5 = 0`.

## Theorem 2 — `N_pos` and, for each displayed `Q`, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 21` maps have `cov5 > 0`. For each displayed
`Q`, write `N_Q` for the number of maps with `Q` true and `N_both` for
the number with both `Q` and `cov5>0`.

| displayed `Q` | `N_Q` | `N_pos` | `N_both` |
|---|---:|---:|---:|
| `wt1` | 16 | 21 | 13 |
| `opp2` | 16 | 21 | 11 |
| `adj2` | 16 | 21 | 16 |
| `vertex3` | 16 | 21 | 12 |
| `mixed3` | 16 | 21 | 11 |
| `wt1 OR opp2` | 24 | 21 | 17 |
| `wt1 OR adj2` | 24 | 21 | 21 |
| `wt1 OR vertex3` | 24 | 21 | 17 |
| `wt1 OR mixed3` | 24 | 21 | 17 |
| `opp2 OR adj2` | 24 | 21 | 19 |
| `opp2 OR vertex3` | 24 | 21 | 17 |
| `opp2 OR mixed3` | 24 | 21 | 16 |
| `adj2 OR vertex3` | 24 | 21 | 20 |
| `adj2 OR mixed3` | 24 | 21 | 19 |
| `vertex3 OR mixed3` | 24 | 21 | 17 |
| `Q4` | 24 | 21 | 21 |
| `Q6` | 28 | 21 | 21 |

Every `Q4`-true count agrees with `N_Q4 = 24` and `N_both = 21`. Every
`Q6`-true count agrees with `N_Q6 = 28` and `N_both = 21`. Equivalence
fails because those triples are not `(21, 21, 21)`.

Every `Q4`-true map is not required for positivity: three `Q4`-true maps
have `cov5 = 0`, namely `(1, 0, 0, 0, 0)`, `(1, 1, 0, 0, 0)`, and
`(1, 0, 0, 0, 1)`. Every map with `cov5>0` does satisfy `Q4`, so
`cov5>0` implies `Q4` and is strictly smaller. `Q6` likewise contains
every positive map and seven extra zeros.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q4` and `Q6`
and has `cov5 = 792`. That is consistent with Theorem 2 and does not
restore any equivalence.

## Theorem 3 — display; do not adopt a bit

The menu, the counts, and the lex-first misses are displayed data. Do not
adopt a bit. Do not adopt Q4. Do not adopt Q6. Do not adopt `f_L1`. Do
not write `Q4` or `Q6` into Admissibility. Admissibility does not name
these remaining-bit formulas.

The identities that fail here are finite facts about occupancy-to-lock on
this two-cube with off-patch `o=0`. They are not a physical
formation-site selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 five-site seeds, off-patch `o=0` | declared finite patch |
| `cov5>0` iff `Q4` | fails; lex-first miss `(1, 0, 0, 0, 0)` |
| `cov5>0` iff `Q6` | fails; lex-first miss `(0, 0, 0, 1, 0)` |
| each 1-bit and each 2-bit OR versus `cov5>0` | all fail; one lex-first miss each |
| `N_pos = 21` and per-`Q` `(N_Q, N_both)` | proved by exhaustive scoring |
| leftover-character of #6518, #6531, or #6476 | refused; new k |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6518: that closed `cov4>0` iff `Q4` on
four-site seeds. The present count is `cov5` on 792 five-site seeds, a
different seed family.

Not leftover-character of #6531: that closed `cov6>0` iff `Q6` on
six-site seeds. The present object is 5-site positivity, not a six-site
identity.

Not leftover-character of #6476: that compared `Max(k)` with `Max(12-k)`
and found equality only for `k=4,5`. The present object is 5-site
positivity versus displayed remaining-bit predicates, not a maximizer
complementarity.

The note is not a Max(5) ranking and not a seed-table: maximizers of
`cov5` are not selected, and no seed census of a named map is compiled
beyond the positivity boolean.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q4` into Admissibility. Do not write `Q6` into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit predicate equals `cov5>0` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6518 / #6531 identities at `k=4` and `k=6`, but no landed 5-site remaining-bit positivity search. |
| V3 | The 32 maps, 792 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared candidate menu. |
| V5 | Equivalence fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov5>0` is not `Q4`, not `Q6`, and not
any displayed 1-bit or 2-bit OR among the 32 `F_cut` maps on this patch.
No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6518 | treat 5-site positivity as leftover-character of `cov4>0` iff `Q4` | **ATTEMPTED** |
| leftover of #6531 | treat 5-site positivity as leftover-character of `cov6>0` iff `Q6` | **ATTEMPTED** |
| leftover of #6476 | treat the count as leftover-character of `Max(k)=Max(12-k)` | **ATTEMPTED** |
| adopt a bit | write a remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed `Q4` and `Q6` equivalences, the Hamming contrast, the #6476
maximizer complementarity, and the off-patch convention are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 five-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed menu are declared. Equivalence of `cov5>0` with `Q4` or `Q6`
is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether a
displayed remaining-bit predicate equals `cov5>0` on the declared patch,
not leftover-character of #6518, #6531, or #6476, and not a Max(5)
ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 792 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `(N_Q, N_both)` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside the displayed remaining-bit menu, and any
independently derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6518 already showed that positivity is `Q4`, #6531 already
showed that positivity is `Q6`, and #6476 already showed that `k=5` is
the complementary twin of `k=4`, so `cov5>0` must inherit `Q4` or `Q6`.

**Answer:** Inheritance fails at `k=5`. Twenty-one maps have `cov5>0`,
twenty-four satisfy `Q4`, and twenty-eight satisfy `Q6`. The lex-first
`Q4` miss `(1, 0, 0, 0, 0)` has `Q4` true and `cov5 = 0`. The lex-first
`Q6` miss `(0, 0, 0, 1, 0)` has `Q6` true and `cov5 = 0`. No displayed
1-bit or 2-bit OR matches. Displayed predicates are not adopted.

### N8 — cross-cycle echo

Investment #6518 already showed that `cov4>0` is `Q4`. Investment #6531
already showed that `cov6>0` is `Q6`. Investment #6476 already compared
complementary maximizers. Echoing any of those facts is not a substitute
for the five-site count: `k=5` is a new seed family, and the lex-first
misses and the triples `(N_Q, N_pos, N_both)` are five-site facts.

No-Go Discipline disposition: **PASS** for the finite candidate census
and the narrow equivalence failures. FAIL / DO NOT SHIP for “`cov5>0` is
`Q4`,” “`cov5>0` is `Q6`,” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov5` on the
792 five-site seeds, tests displayed `Q4`, displayed `Q6`, and every
displayed 1-bit or 2-bit OR against `cov5>0`, reports one lex-first miss
of each, and reports `N_pos = 21` together with each `(N_Q, N_both)`.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.
