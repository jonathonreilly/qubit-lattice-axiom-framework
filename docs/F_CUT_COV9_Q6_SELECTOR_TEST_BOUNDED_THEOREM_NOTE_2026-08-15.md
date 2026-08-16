---
claim_id: f_cut_cov9_q6_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov9>0 equals wt1∨adj2∨vertex3, and whether positivity implies that OR, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov9_q6_selector_test_2026_08_15.py
---

# Whether `cov9>0` Equals Displayed `wt1 ∨ adj2 ∨ vertex3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 9-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q6`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov9_q6_selector_test_2026_08_15.py`](../scripts/f_cut_cov9_q6_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c5q6 showed that `cov5>0` implies `Q6`, with `N_pos = 21`,
`N_Q6 = 28`, and `N_both = 21`. Investment c7q6 showed that `cov7>0`
implies `Q6`, with `N_pos = 24`, `N_Q6 = 28`, and `N_both = 24`.
Investment c11q6 showed that `cov11>0` implies `Q6`, with `N_pos = 24`,
`N_Q6 = 28`, and `N_both = 24`. Investment c9sel already reported
`N_pos = 26` and `N_Q6 = 28` inside a remaining-bit menu search at
nine-site seeds. The 3-bit OR

```text
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1).
```

was already named at k=6 by `Q6=cov6>0`. This note tests that named
3-bit OR at nine-site seeds. New k for the named 3-bit OR. Not
leftover-character of c5q6, not leftover-character of c7q6, not
leftover-character of c11q6, and not leftover-character of c9sel.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov9(f) = |{S : |S|=9 and f fills from S}|`. Then:

- Theorem 1. `cov9>0` is not equivalent to `Q6`. Positivity does not
  imply `Q6`. One lex-first remaining-bit miss is reported.
- Theorem 2. `N_pos = 26`, `N_Q6 = 28`, `N_both = 25`.
- Theorem 3. `Q6` is displayed. Do not adopt Q6.

Do not write `Q6` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 220 nine-site seeds of the two-cube. Whether cov9>0 equals displayed Q6, and whether positivity implies that OR, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov9_q6_selector_test
target_blocker_text: "whether cov9>0 equals wt1 or adj2 or vertex3 among the 32 F_cut maps, and whether positivity implies that OR"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 9-site positivity-versus-Q6 comparison; do not adopt displayed Q6"
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
predicate. `Q6` is a displayed remaining-bit formula, not axiom content.

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

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`. Then
`cov9(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov9(f)>0`. Duality is not assumed: `cov9` is scored on
those 220 seeds.

The displayed remaining-bit predicate is

```text
Q6(f) := (wt1=1) or (adj2=1) or (vertex3=1).
```

That is `wt1∨adj2∨vertex3`. Opp2 and mixed3 are free in `Q6`.
Displayed, not adopted.

## Theorem 1 — `cov9>0` is not equivalent to `Q6`; positivity does not imply `Q6`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov9` on the
220 nine-site seeds. Then `cov9(f) > 0` is not equivalent to `Q6`. There
are four mismatches. Positivity does not imply `Q6`: there is one
`Q6`-false positive.

The three `Q6`-true maps with `cov9 = 0` are
`(1, 0, 0, 0, 0)`, `(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 0)`.

The unique `Q6`-false map with `cov9 > 0` is `(0, 1, 0, 0, 1)`:
`wt1 = 0`, `adj2 = 0`, `vertex3 = 0`, and `cov9 = 4`. That witness
refuses `cov9>0 ⇒ Q6`.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 1, 0, 0, 1)`: `cov9 = 4`
and `Q6` is false.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q6` and has
`cov9 = 220`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q6`, `N_both`

Among the 32 maps:

- `N_pos = 26` maps have `cov9 > 0`;
- `N_Q6 = 28` maps satisfy `Q6`;
- `N_both = 25` maps satisfy both.

The counts already refuse equivalence and refuse the one-sided
implication: `N_both = 25` is strictly smaller than both `N_pos = 26`
and `N_Q6 = 28`. Three mismatches are `Q6`-true zeros. One mismatch is
the `Q6`-false positive of Theorem 1. Necessity fails; sufficiency fails.

## Theorem 3 — display; do not adopt Q6

`Q6` is the remaining-bit predicate already named at k=6. On this patch
it does not equal 9-site positivity, and positivity does not imply `Q6`.
Displayed, not adopted. Do not adopt Q6. Do not write `Q6` into
Admissibility. Admissibility does not name this remaining-bit formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 nine-site seeds, off-patch `o=0` | declared finite patch |
| `Q6` as `(wt1=1) or (adj2=1) or (vertex3=1)` | displayed, not adopted |
| `cov9>0` iff `Q6` | fails; lex-first miss `(0, 1, 0, 0, 1)` |
| positivity implies `Q6` | fails; unique `Q6`-false positive `(0, 1, 0, 0, 1)` |
| `N_pos = 26`, `N_Q6 = 28`, `N_both = 25` | proved by exhaustive scoring |
| leftover-character of c5q6 | refused; named 3-bit OR at a new k |
| leftover-character of c7q6 | refused; named 3-bit OR at a new k |
| leftover-character of c11q6 | refused; named 3-bit OR at a new k |
| leftover-character of c9sel | refused; dedicated iff and imply test |
| leftover-character of the naming of `Q6` at k=6 | refused; same OR, new comparison to `cov9>0` |
| adoption of `Q6` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c5q6: that already showed that `cov5>0` implies
`Q6`, with `N_pos = 21`, `N_Q6 = 28`, and `N_both = 21`. Echoing a
five-site implication is not a substitute for the nine-site iff test.

Not leftover-character of c7q6: that already showed that `cov7>0` implies
`Q6`, with `N_pos = 24`, `N_Q6 = 28`, and `N_both = 24`. Echoing a
seven-site implication is not a substitute for the nine-site iff test.

Not leftover-character of c11q6: that already showed that `cov11>0`
implies `Q6`, with `N_pos = 24`, `N_Q6 = 28`, and `N_both = 24`. Echoing
an eleven-site implication is not a substitute for the nine-site iff test.

Not leftover-character of c9sel: that remaining-bit menu already reported
`N_pos = 26` and `N_Q6 = 28` and that `cov9>0` is not equivalent to `Q6`.
A search report is not a substitute for the dedicated positivity-versus-`Q6`
iff and implication theorems at this seed size.

New k for the named 3-bit OR: naming `wt1∨adj2∨vertex3` at k=6 is not a
substitute for scoring it against `cov9>0` on the 32 maps.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q6` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 9-site positivity equals displayed `Q6` inside `F_cut` on this patch, and whether positivity implies that OR. |
| V2 | Current main has the axiom memo. Investments c5q6, c7q6, and c11q6 already showed that `cov5>0`, `cov7>0`, and `cov11>0` imply `Q6`. Investment c9sel already reported `N_pos = 26` and `N_Q6 = 28`. There is no landed 9-site positivity-versus-`Q6` iff and imply test. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a named 3-bit OR at a new seed size. |
| V5 | Equivalence fails, positivity does not imply `Q6`, one lex-first miss is reported, and displayed `Q6` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov9>0` is not `Q6`. Positivity does not imply `Q6`. Displayed `Q6` is
not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c5q6 | treat the test as leftover-character of “`cov5>0` implies `Q6`” | **ATTEMPTED** |
| leftover of c7q6 | treat the test as leftover-character of “`cov7>0` implies `Q6`” | **ATTEMPTED** |
| leftover of c11q6 | treat the test as leftover-character of “`cov11>0` implies `Q6`” | **ATTEMPTED** |
| leftover of c9sel | treat the dedicated test as leftover-character of the nine-site menu counts | **ATTEMPTED** |
| adopt `Q6` | write `(wt1=1) or (adj2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the c5q6 implication, the c7q6 implication, the
c11q6 implication, the c9sel menu counts, and the naming of `Q6` at k=6
are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q6` are declared. Equivalence of `cov9>0` with `Q6` is not silently
assumed. The implication `cov9>0 ⇒ Q6` is scored and fails; it is not
imported from the odd-k implications.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
9-site positivity equals displayed `Q6` on the declared patch, and
whether positivity implies that OR, as the named 3-bit OR at a new k,
and not leftover-character of c5q6, leftover-character of c7q6,
leftover-character of c11q6, or leftover-character of c9sel.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `N_pos`, `N_Q6`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q6` or `cov9>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c5q6, c7q6, and c11q6 already showed that positivity
implies the named 3-bit OR `Q6` at three nearby seed sizes, and c9sel
already counted `N_pos = 26` and `N_Q6 = 28`, so either the nine-site
comparison is leftover-character of those reports, or the same
implication must hold at k=9 and must be written into Admissibility as
the physical selector.

**Answer:** `Q6` fails equivalence at this k, and positivity does not
imply `Q6`: twenty-eight maps satisfy `Q6` and twenty-six maps have
`cov9>0`, but only twenty-five maps satisfy both. The lex-first miss
`(0, 1, 0, 0, 1)` has `cov9 = 4` and `Q6` false. The three `Q6`-true
zeros are `(1, 0, 0, 0, 0)`, `(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 0)`.
Displayed `Q6` is not adopted.

### N8 — cross-cycle echo

Investment c5q6 already showed that `cov5>0` implies `Q6`, with
`(N_pos, N_Q6, N_both) = (21, 28, 21)`. Investment c7q6 already showed
that `cov7>0` implies `Q6`, with `(N_pos, N_Q6, N_both) = (24, 28, 24)`.
Investment c11q6 already showed that `cov11>0` implies `Q6`, with
`(N_pos, N_Q6, N_both) = (24, 28, 24)`. Investment c9sel already
reported `N_pos = 26` and `N_Q6 = 28` inside a menu search. The naming
of `Q6` at k=6 already wrote `wt1∨adj2∨vertex3`. Echoing any of those
facts is not a substitute for the nine-site `Q6` iff test: the lex-first
miss and the triple `(N_pos, N_Q6, N_both) = (26, 28, 25)` are nine-site
facts about this named OR.

No-Go Discipline disposition: **PASS** for the finite comparison, the
narrow nonequivalence report, and the failed implication. FAIL / DO NOT SHIP
for “displayed `Q6` is the physical rule” or “adopt Q6.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov9` on the
220 nine-site seeds, compares positivity with displayed `Q6`, reports that
the two are not equivalent, reports that positivity does not imply `Q6`,
reports one lex-first miss `(0, 1, 0, 0, 1)` with `cov9 = 4`, and reports
`N_pos = 26`, `N_Q6 = 28`, and `N_both = 25`. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.
