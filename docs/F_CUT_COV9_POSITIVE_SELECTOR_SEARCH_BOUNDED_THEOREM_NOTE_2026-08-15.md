---
claim_id: f_cut_cov9_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov9>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov9_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search for a Positive 9-Site Coverage Selector

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 220 nine-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against a displayed remaining-bit
family.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov9_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov9_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6514 showed that no 1-bit remaining-bit predicate and no
`wt1`-AND-bit predicate equals `cov3>0`. Investment #6524 showed that
no 3-bit AND/OR, and not P/Q4/Q1, equals `cov3>0`. Investment #6533
showed that no 4-bit AND/OR equals `cov3>0`. Investment #6544 showed
that no 5-bit AND/OR equals `cov3>0`. Investment #6476 duality is only
for Max at k=4,5, not positivity. This note searches a new displayed
family on the nine-site seeds: whether `cov9>0` iff `Q_*`, iff `Q4`,
iff `Q6`, iff `Q8`, or iff any displayed 1-bit or 2-bit OR. New k.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov9(f) = |{S : |S|=9 and f fills from S}|`. The boolean scored here is
`cov9(f)>0`. Then:

- Theorem 1. `cov9>0` is not `Q_*`, not `Q4`, not `Q6`, not `Q8`, and
  not any displayed 1-bit or 2-bit OR. None of the displayed remaining-bit
  predicates equals `cov9>0`. The lex-first remaining-bit miss of each
  displayed `Q` is named below.
- Theorem 2. `N_pos = 26`. For each displayed `Q`, `N_Q` and `N_both` are
  reported below.
- Theorem 3. The displayed family is displayed. Displayed, not adopted.
  Do not adopt a bit.

Do not write any displayed remaining-bit formula into Admissibility. The
extra that would have made `Q_*`, `Q4`, `Q6`, `Q8`, a 1-bit, or a 2-bit
OR the positivity selector at `k=9` is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 220 nine-site seeds of the two-cube. Whether any displayed remaining-bit predicate equals cov9>0, and the counts N_pos, N_Q, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov9_positive_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov9>0 among the 32 F_cut maps after the failed 1-5-bit searches at cov3>0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded remaining-bit search against cov9>0; do not adopt a displayed bit"
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

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`. Then
`cov9(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov9(f)>0`.

The displayed remaining-bit family, in this order, is:

1. `Q_*(f) := (wt1 = 1) and (adj2 = 1)`;
2. `Q4(f) := (wt1 = 1) or (adj2 = 1)`;
3. `Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1)`;
4. `Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1)`;
5. each 1-bit: `bit:wt1`, `bit:opp2`, `bit:adj2`, `bit:vertex3`, `bit:mixed3`;
6. every 2-bit OR: `wt1|opp2`, `wt1|adj2`, `wt1|vertex3`, `wt1|mixed3`,
   `opp2|adj2`, `opp2|vertex3`, `opp2|mixed3`, `adj2|vertex3`,
   `adj2|mixed3`, `vertex3|mixed3`.

Displayed, not adopted. `wt1|adj2` is the same formula as `Q4`.

## Theorem 1 — whether `cov9>0` iff `Q_*`, iff `Q4`, iff `Q6`, iff `Q8`, or iff any 1-bit or 2-bit OR

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov9` on the 220
nine-site seeds. For each displayed `Q`, compare the set of maps with
`Q` true to the set of maps with `cov9>0`.

None of the displayed remaining-bit predicates equals `cov9>0`. In
particular `Q_*`, `Q4`, `Q6`, `Q8`, every 1-bit, and every 2-bit OR fail.

The six maps with `cov9 = 0` are

```text
(0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 1, 0, 0, 0),
(1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 1, 0, 0, 0).
```

The two `Q8`-false maps are both zeros: `(0, 0, 0, 0, 0)` and
`(0, 0, 0, 0, 1)`. Four further zeros are `Q8`-true:
`(0, 1, 0, 0, 0)`, `(1, 0, 0, 0, 0)`, `(1, 0, 0, 0, 1)`,
`(1, 1, 0, 0, 0)`. Two maps with `adj2 = 0` and `vertex3 = 0` still
have `cov9 = 4 > 0`: `(0, 1, 0, 0, 1)` and `(1, 1, 0, 0, 1)`. Those
two are the extras that keep `adj2|vertex3` from equaling positivity.

The lex-first remaining-bit miss of each displayed `Q`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, is:

- `Q_*`: lex-first miss `(0, 0, 0, 1, 0)`
- `Q4`: lex-first miss `(0, 0, 0, 1, 0)`
- `Q6`: lex-first miss `(0, 1, 0, 0, 1)`
- `Q8`: lex-first miss `(0, 1, 0, 0, 0)`
- `bit:wt1`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:opp2`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `bit:mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `wt1|opp2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1|adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1|vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `wt1|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `opp2|adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `opp2|vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `opp2|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `adj2|vertex3`: lex-first miss `(0, 1, 0, 0, 1)`
- `adj2|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `vertex3|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`

## Theorem 2 — `N_pos` and, for each displayed Q, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 26` maps have `cov9>0`.

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number of maps with both `Q` true and `cov9>0`:

- `Q_*`: N_Q = 8, N_both = 8
- `Q4`: N_Q = 24, N_both = 21
- `Q6`: N_Q = 28, N_both = 25
- `Q8`: N_Q = 30, N_both = 26
- `bit:wt1`: N_Q = 16, N_both = 13
- `bit:opp2`: N_Q = 16, N_both = 14
- `bit:adj2`: N_Q = 16, N_both = 16
- `bit:vertex3`: N_Q = 16, N_both = 16
- `bit:mixed3`: N_Q = 16, N_both = 14
- `wt1|opp2`: N_Q = 24, N_both = 20
- `wt1|adj2`: N_Q = 24, N_both = 21
- `wt1|vertex3`: N_Q = 24, N_both = 21
- `wt1|mixed3`: N_Q = 24, N_both = 20
- `opp2|adj2`: N_Q = 24, N_both = 22
- `opp2|vertex3`: N_Q = 24, N_both = 22
- `opp2|mixed3`: N_Q = 24, N_both = 20
- `adj2|vertex3`: N_Q = 24, N_both = 24
- `adj2|mixed3`: N_Q = 24, N_both = 22
- `vertex3|mixed3`: N_Q = 24, N_both = 22

No displayed row has `N_Q = N_both = N_pos`. The row `Q8` has
`N_both = N_pos = 26` with `N_Q = 30`: every positive map is `Q8`-true,
but four `Q8`-true maps have `cov9 = 0`. The row `adj2|vertex3` has
`N_Q = N_both = 24` against `N_pos = 26`.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, has `cov9 = 220 > 0`. That
is consistent with Theorem 2 and does not restore equality for any
displayed `Q`.

## Theorem 3 — display; do not adopt a bit

Every predicate above is displayed. Displayed, not adopted. Do not adopt a
bit. Do not write any displayed remaining-bit formula into Admissibility.
Do not adopt `Q_*`. Do not adopt `Q4`. Do not adopt `Q6`. Do not adopt
`Q8`. Do not adopt a 1-bit. Do not adopt a 2-bit OR.

That no displayed remaining-bit predicate equals `cov9>0` is a finite
fact about occupancy-to-lock on this two-cube with off-patch `o=0`. It
is not a physical formation-site selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 nine-site seeds, off-patch `o=0` | declared finite patch |
| displayed `Q_*`, `Q4`, `Q6`, `Q8`, 1-bit, 2-bit OR family | displayed, not adopted |
| `cov9>0` iff `Q_*` | fails; lex-first miss named |
| `cov9>0` iff `Q4` | fails; lex-first miss named |
| `cov9>0` iff `Q6` | fails; lex-first miss named |
| `cov9>0` iff `Q8` | fails; lex-first miss named |
| `cov9>0` iff any 1-bit | fails; lex-first miss of each named |
| `cov9>0` iff a 2-bit OR | fails; lex-first miss of each named |
| `N_pos = 26` and per-`Q` `N_Q`, `N_both` | proved by exhaustive scoring |
| leftover-character of #6514 | refused; New k |
| leftover-character of #6524 | refused; New k |
| leftover-character of #6533 | refused; New k |
| leftover-character of #6544 | refused; New k |
| leftover Max duality of #6476 | refused; duality is only for Max at k=4,5 |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6514: that closed that no 1-bit remaining-bit
predicate and no `wt1`-AND-bit predicate equals `cov3>0`. The present
object is positivity at a new seed size, not a restatement of the 1-bit
search at `k=3`.

Not leftover-character of #6524: that closed that no 3-bit AND/OR, and
not P/Q4/Q1, equals `cov3>0`. A failed 3-bit menu at `k=3` does not
score `Q_*`, `Q4`, `Q6`, `Q8`, the 1-bits, or the 2-bit ORs against
`cov9>0`.

Not leftover-character of #6533: that closed that no 4-bit AND/OR equals
`cov3>0`. Four-bit width at complementary size is not a nine-site
remaining-bit search.

Not leftover-character of #6544: that closed that no 5-bit AND/OR equals
`cov3>0`. Exhausting remaining-bit width at `k=3` does not identify
`cov9>0` with any displayed `Q` at `k=9`.

#6476 duality is only for Max at k=4,5, not positivity. Complement
maximizer-set equality at those two sizes does not identify `cov9>0`
with `cov3>0` and does not name a remaining-bit selector.

The note is not a Max(9) ranking and not a seed-table: maximizers of
`cov9` are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt a bit.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit predicate equals `cov9>0` inside `F_cut` on this patch. |
| V2 | Current main has the failed 1–5-bit searches at `k=3` and Max duality at `k=4,5`, but no landed remaining-bit search at `k=9`. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a displayed remaining-bit family. |
| V5 | Equality fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `Q_*`, `Q4`, `Q6`, `Q8`, every displayed
1-bit, and every displayed 2-bit OR fail to equal `cov9>0` among the 32
`F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6514 | treat the search as leftover-character of the failed 1-bit / `wt1`-AND menu at `cov3>0` | **ATTEMPTED** |
| leftover of #6524 | treat the search as leftover-character of the failed 3-bit menu at `cov3>0` | **ATTEMPTED** |
| leftover of #6533 | treat the search as leftover-character of the failed 4-bit menu at `cov3>0` | **ATTEMPTED** |
| leftover of #6544 | treat the search as leftover-character of the failed 5-bit menu at `cov3>0` | **ATTEMPTED** |
| leftover of #6476 | treat Max duality at k=4,5 as positivity at k=9 | **ATTEMPTED** |

### N2 — wall independence

The failed `Q_*` / `Q4` / `Q6` / `Q8` / 1-bit / 2-bit-OR equalities, the
Hamming contrast, the complementary-size 1–5-bit leftovers, and the
off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
family are declared. Equality of any displayed `Q` with `cov9>0` is not
silently assumed. #6476 duality is only for Max at k=4,5, not positivity.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether a displayed
remaining-bit predicate equals 9-site positivity on the declared patch, not
leftover-character of #6514, #6524, #6533, or #6544, and not Max duality.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `N_Q`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector outside the displayed remaining-bit family, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** after no 1–5-bit selector equalled `cov3>0`, either `Q_*`,
`Q4`, `Q6`, `Q8`, a 1-bit, a 2-bit OR, or Max duality at the complementary
size must be the positivity selector at `k=9`.

**Answer:** `Q_*`, `Q4`, `Q6`, `Q8`, every 1-bit, and every 2-bit OR fail.
Duality is only for Max at k=4,5, not positivity. `N_pos = 26` and no
displayed row has `N_Q = N_both = N_pos`. No bit is adopted.

### N8 — cross-cycle echo

Investment #6514 already showed no 1-bit remaining-bit predicate equals
`cov3>0`. Investment #6524 already showed no 3-bit AND/OR equals
`cov3>0`. Investment #6533 already showed no 4-bit AND/OR equals
`cov3>0`. Investment #6544 already showed no 5-bit AND/OR equals
`cov3>0`. Echoing those failures at complementary size is not a
substitute for scoring the displayed remaining-bit family against
`cov9>0`. The lex-first misses and the per-`Q` pair `(N_Q, N_both)` are
the new search facts. New k.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow equality report. FAIL / DO NOT SHIP for “a displayed remaining-bit
predicate is the physical rule” or “a displayed bit is adopted.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov9` on the
220 nine-site seeds, compares positivity with each displayed remaining-bit
predicate, reports that none of `Q_*`, `Q4`, `Q6`, `Q8`, the 1-bits, or
the 2-bit ORs equals `cov9>0`, names the lex-first miss of each displayed
`Q`, and reports `N_pos = 26` together with per-`Q` `N_Q` and `N_both`.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.
