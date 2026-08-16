---
claim_id: f_cut_cov3_max_three_bit_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed 3-bit remaining-bit predicate equals cov3=220 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_max_three_bit_selector_search_2026_08_15.py
---

# Three-Bit Remaining-Bit Search For Max(3) Coverage `cov3=220`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fillability on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`, tested against every displayed 3-bit remaining-bit AND
and every displayed 3-bit remaining-bit OR of
`{wt1, opp2, adj2, vertex3, mixed3}` for equality with `cov3=220`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_max_three_bit_selector_search_2026_08_15.py`](../scripts/f_cut_cov3_max_three_bit_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

The first Max(3) remaining-bit menu showed that no 1-bit or 2-bit AND/OR equals
`cov3=220` among the 32 maps, with `N_max = 2`. That leftover left open the
next width: every AND of three remaining bits and every OR of three remaining
bits. This note completes that menu. Next width after the first failed Max(3) menu.
Not leftover-character of the failed 1-bit / 2-bit AND/OR menu.

The restricted identity `q3v3m3` — among the eight maps in `Q_*` with
`wt1=1` and `adj2=1`, `cov3=220` iff `vertex3=mixed3=1` — is the `Q_*`
restriction, not a 32-wide 3-bit. q3v3m3 is the Q_* restriction, not a 32-wide 3-bit
remaining-bit predicate, and is not displayed as one here.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f)` for the number of unordered 3-site seeds from which `f` fills.
Then `cov3=220` is the Boolean Max(3) predicate.

- Theorem 1. No displayed 3-bit AND or 3-bit OR equals `cov3=220`. One
  lex-first remaining-bit miss is reported for each displayed `Q`.
- Theorem 2. `N_max = 2`. For each displayed `Q`, the pair
  `(N_Q, N_both)` is reported in the table below.
- Theorem 3. The menu is displayed. Do not adopt a bit.

Do not write a remaining-bit formula into Admissibility. Displayed, not
adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly by whether all 220 three-site seeds fill. Whether cov3=220 equals any displayed 3-bit AND or 3-bit OR is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_max_three_bit_selector_search
target_blocker_text: "whether a displayed 3-bit remaining-bit predicate equals cov3=220 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the remaining-bit Max(3) 3-bit selector search; do not adopt a displayed bit"
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

The three-site seeds are the `C(12,3) = 220` unordered triples of vertices
of `T`. Then `cov3(f)` is the number of those triples from which `f` fills,
and `cov3=220` is the Boolean Max(3) predicate.

The displayed remaining-bit predicates are every AND of three remaining
bits and every OR of three remaining bits, in remaining-bit order. There
are twenty displayed candidates. Displayed, not adopted.

## Theorem 1 — no displayed 3-bit AND or 3-bit OR equals `cov3=220`; one lex-first miss each

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov3` on the
220 three-site seeds. Then `cov3(f) = 220` is not equivalent to any
displayed 3-bit AND or any displayed 3-bit OR.

`N_max = 2`. The maximizers are `f_L1` with remaining bits
`(1, 0, 1, 1, 1)` and `f1` with remaining bits `(1, 1, 1, 1, 1)`. The
lex-first remaining-bit miss of each displayed `Q`, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is:

| displayed `Q` | `cov3=220` iff `Q` | lex-first miss | `cov3` of miss | `Q` at miss |
|---|---|---|---:|---|
| `wt1 AND opp2 AND adj2` | no | `(1, 0, 1, 1, 1)` | 220 | 0 |
| `wt1 AND opp2 AND vertex3` | no | `(1, 0, 1, 1, 1)` | 220 | 0 |
| `wt1 AND opp2 AND mixed3` | no | `(1, 0, 1, 1, 1)` | 220 | 0 |
| `wt1 AND adj2 AND vertex3` | no | `(1, 0, 1, 1, 0)` | 188 | 1 |
| `wt1 AND adj2 AND mixed3` | no | `(1, 0, 1, 0, 1)` | 96 | 1 |
| `wt1 AND vertex3 AND mixed3` | no | `(1, 0, 0, 1, 1)` | 72 | 1 |
| `opp2 AND adj2 AND vertex3` | no | `(0, 1, 1, 1, 0)` | 44 | 1 |
| `opp2 AND adj2 AND mixed3` | no | `(0, 1, 1, 0, 1)` | 16 | 1 |
| `opp2 AND vertex3 AND mixed3` | no | `(0, 1, 0, 1, 1)` | 0 | 1 |
| `adj2 AND vertex3 AND mixed3` | no | `(0, 0, 1, 1, 1)` | 24 | 1 |
| `wt1 OR opp2 OR adj2` | no | `(0, 0, 1, 0, 0)` | 0 | 1 |
| `wt1 OR opp2 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `wt1 OR opp2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `wt1 OR adj2 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `wt1 OR adj2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `wt1 OR vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `opp2 OR adj2 OR vertex3` | no | `(0, 0, 0, 1, 0)` | 0 | 1 |
| `opp2 OR adj2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `opp2 OR vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `adj2 OR vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |

The six 3-bit ANDs that require `opp2` are first missed by remaining bits
`(1, 0, 1, 1, 1)`: that map has `cov3 = 220` and the AND is false. The four
3-bit ANDs that omit `opp2` are first missed by a remaining-bit tuple on
which the AND is true and `cov3 < 220`. Every 3-bit OR is first missed by
a remaining-bit tuple on which the OR is true and `cov3 = 0`.

## Theorem 2 — `N_max` and, for each displayed `Q`, `N_Q` and `N_both`

Among the 32 maps, `N_max = 2` maps have `cov3 = 220`. For each displayed
`Q`, write `N_Q` for the number of maps with `Q` true and `N_both` for
the number with both `Q` and `cov3=220`.

| displayed `Q` | `N_Q` | `N_max` | `N_both` |
|---|---:|---:|---:|
| `wt1 AND opp2 AND adj2` | 4 | 2 | 1 |
| `wt1 AND opp2 AND vertex3` | 4 | 2 | 1 |
| `wt1 AND opp2 AND mixed3` | 4 | 2 | 1 |
| `wt1 AND adj2 AND vertex3` | 4 | 2 | 2 |
| `wt1 AND adj2 AND mixed3` | 4 | 2 | 2 |
| `wt1 AND vertex3 AND mixed3` | 4 | 2 | 2 |
| `opp2 AND adj2 AND vertex3` | 4 | 2 | 1 |
| `opp2 AND adj2 AND mixed3` | 4 | 2 | 1 |
| `opp2 AND vertex3 AND mixed3` | 4 | 2 | 1 |
| `adj2 AND vertex3 AND mixed3` | 4 | 2 | 2 |
| `wt1 OR opp2 OR adj2` | 28 | 2 | 2 |
| `wt1 OR opp2 OR vertex3` | 28 | 2 | 2 |
| `wt1 OR opp2 OR mixed3` | 28 | 2 | 2 |
| `wt1 OR adj2 OR vertex3` | 28 | 2 | 2 |
| `wt1 OR adj2 OR mixed3` | 28 | 2 | 2 |
| `wt1 OR vertex3 OR mixed3` | 28 | 2 | 2 |
| `opp2 OR adj2 OR vertex3` | 28 | 2 | 2 |
| `opp2 OR adj2 OR mixed3` | 28 | 2 | 2 |
| `opp2 OR vertex3 OR mixed3` | 28 | 2 | 2 |
| `adj2 OR vertex3 OR mixed3` | 28 | 2 | 2 |

Every 3-bit AND has `N_Q = 4 ≠ 2`. Every 3-bit OR has `N_Q = 28 ≠ 2`.
Equivalence fails because those triples are not `(2, 2, 2)`.

The six ANDs that include `opp2` have `N_both = 1`: they catch `f1` and
miss `f_L1`. The four ANDs that omit `opp2` have `N_both = 2`: they contain
both maximizers and two extra non-max maps. Every 3-bit OR contains both
maximizers (`N_both = 2`) and twenty-six extra non-max maps. Those still
fail iff.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies every displayed
3-bit OR, fails every displayed 3-bit AND that requires `opp2`, and has
`cov3 = 220`. That is consistent with Theorem 2 and does not restore any
equivalence.

## Theorem 3 — display; do not adopt a bit

The menu, the counts, and the lex-first misses are displayed data. Do not
adopt a bit. Do not adopt a 3-bit AND. Do not adopt a 3-bit OR. Do not
adopt `f_L1`. Do not write a remaining-bit formula into Admissibility.
Admissibility does not name these remaining-bit formulas.

The identities that fail here are finite facts about occupancy-to-lock on
this two-cube with off-patch `o=0`. They are not a physical
formation-site selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 three-site seeds, off-patch `o=0` | declared finite patch |
| each 3-bit AND and each 3-bit OR versus `cov3=220` | all fail; one lex-first miss each |
| `N_max = 2` and per-`Q` `(N_Q, N_both)` | proved by exhaustive scoring |
| leftover-character of the 1-bit / 2-bit AND/OR menu | refused; next width at same Max(3) |
| `q3v3m3` as a 32-wide 3-bit | refused; it is a `Q_*` restriction |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the failed 1-bit / 2-bit AND/OR Max(3) menu:
that search already showed `N_max = 2` and that no 1-bit predicate, no
2-bit AND, and no 2-bit OR equals `cov3=220`. The present count is the
next width: the ten 3-bit ANDs and the ten 3-bit ORs.

q3v3m3 is the Q_* restriction, not a 32-wide 3-bit. Among the eight maps
with `wt1=1` and `adj2=1`, `cov3=220` iff `vertex3=mixed3=1`. That is a
restriction of the search domain, not a displayed 3-bit AND or OR on all
32 maps.

The note is not a restatement of the `cov3>0` 3-bit search: maximizers of
`cov3` are scored here, not positivity.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write a remaining-bit formula into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed 3-bit remaining-bit predicate equals `cov3=220` inside `F_cut` on this patch. |
| V2 | The first failed Max(3) menu scored 1-bit predicates and 2-bit AND/OR. Current main has no landed 3-bit remaining-bit Max(3) search for `cov3=220`. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared 3-bit candidate menu. |
| V5 | Equivalence fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov3=220` is not any displayed 3-bit AND
or 3-bit OR among the 32 `F_cut` maps on this patch. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 1-bit / 2-bit AND/OR menu | treat the search as a restatement of the first failed Max(3) menu | **ATTEMPTED** |
| `q3v3m3` as 32-wide 3-bit | treat the `Q_*` restriction as a displayed 3-bit AND on all 32 | **ATTEMPTED** |
| leftover of the `cov3>0` 3-bit search | replace Max(3) equality by positivity | **ATTEMPTED** |
| adopt a bit | write a remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed 1-bit / 2-bit AND/OR tests, the twenty failed 3-bit tests, the
`Q_*` restriction, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 three-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed 3-bit menu are declared. Equivalence of `cov3=220` with a 3-bit
AND or OR is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether a
displayed 3-bit remaining-bit predicate equals `cov3=220` on the declared
patch, completing the next width after the first failed Max(3) menu, and
not a `Q_*` restriction restated as a 32-wide 3-bit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `N_max` and per-`Q` `(N_Q, N_both)` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector outside the
displayed 3-bit menu, a genuine restriction of the search domain, and any
independently derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the 1-bit / 2-bit AND/OR menu already failed at Max(3), so a
3-bit AND or a 3-bit OR must recover `cov3=220`, or else `q3v3m3` already
is that 3-bit.

**Answer:** Every 3-bit AND has `N_Q = 4 ≠ 2`. Every 3-bit OR has
`N_Q = 28 ≠ 2`. The six ANDs that require `opp2` miss `f_L1`. The four
ANDs that omit `opp2` include two extra non-max maps. Every OR includes
twenty-six extra non-max maps. `q3v3m3` is a `Q_*` restriction, not a
32-wide 3-bit. No match. Displayed predicates are not adopted.

### N8 — cross-cycle echo

The first failed Max(3) menu already showed that no 1-bit or 2-bit AND/OR
equals `cov3=220`. The `Q_*` restriction already showed a two-bit
conjunction inside those eight maps. Echoing either fact is not a
substitute for the 32-wide 3-bit Max(3) count: the lex-first misses and
the triples `(N_Q, N_max, N_both)` are 32-wide 3-bit facts.

No-Go Discipline disposition: **PASS** for the finite candidate census
and the narrow equivalence failures. FAIL / DO NOT SHIP for “`cov3=220`
is a displayed 3-bit AND or OR” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, tests every displayed 3-bit AND and every displayed
3-bit OR against `cov3=220`, reports one lex-first miss of each, and
reports `N_max = 2` together with each `(N_Q, N_both)`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
