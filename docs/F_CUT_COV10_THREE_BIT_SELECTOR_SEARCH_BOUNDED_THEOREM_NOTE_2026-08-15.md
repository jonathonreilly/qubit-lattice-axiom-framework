---
claim_id: f_cut_cov10_three_bit_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed 3-bit remaining-bit predicate equals cov10>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov10_three_bit_selector_search_2026_08_15.py
---

# Three-Bit Remaining-Bit Search For A Selector Equal To `cov10>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 10-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against every displayed
3-bit remaining-bit AND and every displayed 3-bit remaining-bit OR of
`{wt1, opp2, adj2, vertex3, mixed3}`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov10_three_bit_selector_search_2026_08_15.py`](../scripts/f_cut_cov10_three_bit_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

The first remaining-bit menu at new `k=10` (investment #6566) showed that
no displayed 1-bit remaining-bit predicate and no 2-bit OR equals
`cov10>0`, with `N_pos = 28`. That leftover left open the next width:
every AND of three remaining bits and every OR of three remaining bits.
This note completes that menu. Same pattern as #6524 after #6514.
Next width after the first failed menu at the same new `k=10`. Not
leftover-character of that 1-bit / 2-bit OR menu and not a Max(10) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov10(f) = |{S : |S|=10 and f fills from S}|`. Then:

- Theorem 1. One displayed 3-bit OR equals `cov10>0`:
  `adj2 OR vertex3 OR mixed3`. No displayed 3-bit AND equals `cov10>0`.
  One lex-first remaining-bit miss is reported for each failed displayed
  `Q`.
- Theorem 2. `N_pos = 28`. For each displayed `Q`, the pair
  `(N_Q, N_both)` is reported in the table below.
- Theorem 3. The menu is displayed. Do not adopt a bit.

Do not write a remaining-bit formula into Admissibility. Displayed, not
adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 66 ten-site seeds of the two-cube. Whether cov10>0 equals any displayed 3-bit AND or 3-bit OR is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov10_three_bit_selector_search
target_blocker_text: "whether a displayed 3-bit remaining-bit predicate equals cov10>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 10-site 3-bit positivity selector search; do not adopt a displayed bit"
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

The ten-site seeds are the `C(12,10) = 66` subsets of size 10 in `T`. Then
`cov10(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov10(f)>0`. Duality is not assumed: `cov10` is scored on
those 66 seeds.

The displayed remaining-bit predicates are every AND of three remaining
bits and every OR of three remaining bits, in remaining-bit order. There
are twenty displayed candidates. Displayed, not adopted.

## Theorem 1 — one displayed 3-bit OR equals `cov10>0`; lex-first misses of the rest

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov10` on the
66 ten-site seeds. Then `cov10(f) > 0` if and only if
`adj2 OR vertex3 OR mixed3`. No displayed 3-bit AND equals `cov10>0`.
The other nine displayed 3-bit ORs fail.

`N_pos = 28`. The four maps with `cov10 = 0` are exactly the maps with
`(adj2, vertex3, mixed3) = (0, 0, 0)`:

```text
(0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (1, 0, 0, 0, 0), (1, 1, 0, 0, 0).
```

The lex-first remaining-bit miss of each failed displayed `Q`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, is:

| displayed `Q` | `cov10>0` iff `Q` | lex-first miss | `cov10` of miss | `Q` at miss |
|---|---|---|---:|---|
| `wt1 AND opp2 AND adj2` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 AND opp2 AND vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 AND opp2 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 AND adj2 AND vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 AND adj2 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 AND vertex3 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `opp2 AND adj2 AND vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `opp2 AND adj2 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `opp2 AND vertex3 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `adj2 AND vertex3 AND mixed3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 OR opp2 OR adj2` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 OR opp2 OR vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 OR opp2 OR mixed3` | no | `(0, 0, 0, 1, 0)` | 28 | 0 |
| `wt1 OR adj2 OR vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `wt1 OR adj2 OR mixed3` | no | `(0, 0, 0, 1, 0)` | 28 | 0 |
| `wt1 OR vertex3 OR mixed3` | no | `(0, 0, 1, 0, 0)` | 18 | 0 |
| `opp2 OR adj2 OR vertex3` | no | `(0, 0, 0, 0, 1)` | 4 | 0 |
| `opp2 OR adj2 OR mixed3` | no | `(0, 0, 0, 1, 0)` | 28 | 0 |
| `opp2 OR vertex3 OR mixed3` | no | `(0, 0, 1, 0, 0)` | 18 | 0 |
| `adj2 OR vertex3 OR mixed3` | yes | none | — | — |

Every displayed 3-bit AND is missed first by remaining bits
`(0, 0, 0, 0, 1)`: `cov10 = 4 > 0` and the AND is false. Each failed
3-bit OR is missed first by a remaining-bit tuple on which the OR is
false and `cov10 > 0`. The matching OR has no miss.

## Theorem 2 — `N_pos` and, for each displayed `Q`, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 28` maps have `cov10 > 0`. For each displayed
`Q`, write `N_Q` for the number of maps with `Q` true and `N_both` for
the number with both `Q` and `cov10>0`.

| displayed `Q` | `N_Q` | `N_pos` | `N_both` |
|---|---:|---:|---:|
| `wt1 AND opp2 AND adj2` | 4 | 28 | 4 |
| `wt1 AND opp2 AND vertex3` | 4 | 28 | 4 |
| `wt1 AND opp2 AND mixed3` | 4 | 28 | 4 |
| `wt1 AND adj2 AND vertex3` | 4 | 28 | 4 |
| `wt1 AND adj2 AND mixed3` | 4 | 28 | 4 |
| `wt1 AND vertex3 AND mixed3` | 4 | 28 | 4 |
| `opp2 AND adj2 AND vertex3` | 4 | 28 | 4 |
| `opp2 AND adj2 AND mixed3` | 4 | 28 | 4 |
| `opp2 AND vertex3 AND mixed3` | 4 | 28 | 4 |
| `adj2 AND vertex3 AND mixed3` | 4 | 28 | 4 |
| `wt1 OR opp2 OR adj2` | 28 | 28 | 25 |
| `wt1 OR opp2 OR vertex3` | 28 | 28 | 25 |
| `wt1 OR opp2 OR mixed3` | 28 | 28 | 25 |
| `wt1 OR adj2 OR vertex3` | 28 | 28 | 26 |
| `wt1 OR adj2 OR mixed3` | 28 | 28 | 26 |
| `wt1 OR vertex3 OR mixed3` | 28 | 28 | 26 |
| `opp2 OR adj2 OR vertex3` | 28 | 28 | 26 |
| `opp2 OR adj2 OR mixed3` | 28 | 28 | 26 |
| `opp2 OR vertex3 OR mixed3` | 28 | 28 | 26 |
| `adj2 OR vertex3 OR mixed3` | 28 | 28 | 28 |

Every 3-bit AND has `N_Q = 4 ≠ 28`. Every 3-bit OR has `N_Q = 28`.
Equivalence holds only for `adj2 OR vertex3 OR mixed3`, the unique
displayed row with `N_Q = 28`, `N_pos = 28`, and `N_both = 28`. The other
3-bit ORs share `N_Q = 28` and miss three or two positive maps.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies every displayed
3-bit OR, fails every displayed 3-bit AND that requires `opp2`, and has
`cov10 = 66`. That is consistent with Theorem 2 and does not restore any
failed equivalence.

## Theorem 3 — display; do not adopt a bit

The menu, the counts, the matching OR, and the lex-first misses are
displayed data. Do not adopt a bit. Do not adopt a 3-bit AND. Do not adopt a 3-bit OR. Do not adopt `f_L1`. Do not write a remaining-bit
formula into Admissibility. Admissibility does not name these
remaining-bit formulas.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 66 ten-site seeds, off-patch `o=0` | declared finite patch |
| each 3-bit AND and each 3-bit OR versus `cov10>0` | one OR matches; lex-first miss of each failed `Q` |
| `N_pos = 28` and per-`Q` `(N_Q, N_both)` | proved by exhaustive scoring |
| leftover-character of the 1-bit / 2-bit OR menu | refused; next width at same `k` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the failed 1-bit / 2-bit OR menu at `k=10`:
investment #6566 already showed `N_pos = 28` and that no 1-bit predicate
or 2-bit OR equals `cov10>0`. The present count is the next width: the
ten 3-bit ANDs and the ten 3-bit ORs.

Same pattern as #6524 after #6514: after the first failed menu, the next
width is scored at the same `k`. This is not a restatement of #6524,
which scored `cov3>0`, and not leftover-character of #6566.

The note is not a Max(10) ranking and not a seed-table: maximizers of
`cov10` are not selected, and no seed census of a named map is compiled
beyond the positivity boolean.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write a remaining-bit formula into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed 3-bit remaining-bit predicate equals `cov10>0` inside `F_cut` on this patch. |
| V2 | The first failed menu at this `k` scored 1-bit predicates and 2-bit ORs (#6566). Current main has no landed 3-bit remaining-bit positivity search for `cov10>0`. |
| V3 | The 32 maps, 66 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared 3-bit candidate menu. |
| V5 | Equivalence holds for one displayed 3-bit OR, the rest fail, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
no displayed 3-bit AND equals `cov10>0`, and nine of the ten displayed
3-bit ORs fail. The one matching OR is displayed, not adopted. No global
compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 1-bit / 2-bit OR menu | treat the search as a restatement of the failed 1-bit / 2-bit OR tests | **ATTEMPTED** |
| leftover of #6524 | treat 10-site 3-bit positivity as leftover-character of the `cov3` 3-bit search | **ATTEMPTED** |
| Max(10) rename | replace the fillability search by a maximum-`cov10` ranking | **ATTEMPTED** |
| adopt a bit | write a remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed 1-bit / 2-bit OR tests, the twenty 3-bit tests, the Hamming
contrast, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 66 ten-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed 3-bit menu are declared. Equivalence of `cov10>0` with a 3-bit
AND or OR is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether a
displayed 3-bit remaining-bit predicate equals `cov10>0` on the declared
patch, completing the next width after the first failed menu at this
`k`, and not a Max(10) ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 66 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `(N_Q, N_both)` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector outside the
displayed 3-bit menu, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the 1-bit / 2-bit OR menu already failed at this `k`, so a
3-bit AND or a 3-bit OR must recover `cov10>0`, and that match must be
written into Admissibility.

**Answer:** One displayed 3-bit OR, `adj2 OR vertex3 OR mixed3`, equals
`cov10>0`, with `(N_Q, N_pos, N_both) = (28, 28, 28)`. Every 3-bit AND
has `N_Q = 4 ≠ 28`. The other 3-bit ORs have `N_both` equal to 25 or 26.
The lex-first AND miss `(0, 0, 0, 0, 1)` has `cov10 = 4` and every
displayed AND false. Displayed predicates are not adopted.

### N8 — cross-cycle echo

The first failed menu at `k=10` (#6566) already showed that no 1-bit or
2-bit OR equals `cov10>0`. Investment #6524 already showed that no
displayed 3-bit `Q` equals `cov3>0`. Echoing either fact is not a
substitute for the ten-site 3-bit count: the matching OR, the lex-first
misses, and the triples `(N_Q, N_pos, N_both)` are ten-site 3-bit facts.

No-Go Discipline disposition: **PASS** for the finite candidate census
and the narrow equivalence report. FAIL / DO NOT SHIP for “a displayed
3-bit AND or OR is the physical rule” or “a displayed bit is adopted.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov10` on the
66 ten-site seeds, tests every displayed 3-bit AND and every displayed
3-bit OR against `cov10>0`, reports that `adj2 OR vertex3 OR mixed3`
equals `cov10>0`, reports one lex-first miss of each failed `Q`, and
reports `N_pos = 28` together with each `(N_Q, N_both)`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.
