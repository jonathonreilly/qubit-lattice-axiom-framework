---
claim_id: f_cut_cov9_q8_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov9>0 equals wt1∨adj2∨opp2∨vertex3, and whether positivity implies that OR, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov9_q8_selector_test_2026_08_15.py
---

# Whether `cov9>0` Equals Displayed `wt1 ∨ adj2 ∨ opp2 ∨ vertex3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 9-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q8`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov9_q8_selector_test_2026_08_15.py`](../scripts/f_cut_cov9_q8_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c9q6 showed that `cov9>0` is not equivalent to
`Q6 := wt1 ∨ adj2 ∨ vertex3`, and that positivity does not imply `Q6`.
The unique `Q6`-false positive is `(0, 1, 0, 0, 1)`: that map has
`opp2=1`, so it is `Q8`-true. Investment c9sel already reported
`N_pos = 26` and `N_Q8 = 30` inside a remaining-bit menu search at
nine-site seeds. The 4-bit OR

```text
Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1).
```

is the displayed remaining-bit predicate scored here. New k for Q8.
May still imply even though Q6-imply failed. Not leftover-character of
c9q6 and not leftover-character of c9sel.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`. Mixed3 is
free under `Q8`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov9(f) = |{S : |S|=9 and f fills from S}|`. Then:

- Theorem 1. `cov9>0` is not equivalent to `Q8`. Positivity does imply
  `Q8`. One lex-first remaining-bit miss is reported.
- Theorem 2. `N_pos = 26`, `N_Q8 = 30`, `N_both = 26`.
- Theorem 3. `Q8` is displayed. Do not adopt Q8.

Do not write `Q8` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 220 nine-site seeds of the two-cube. Whether cov9>0 equals displayed Q8, and whether positivity implies that OR, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov9_q8_selector_test
target_blocker_text: "whether cov9>0 equals wt1 or adj2 or opp2 or vertex3 among the 32 F_cut maps, and whether positivity implies that OR"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 9-site positivity-versus-Q8 comparison; do not adopt displayed Q8"
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
predicate. `Q8` is a displayed remaining-bit formula, not axiom content.

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

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`. Then
`cov9(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov9(f)>0`. Duality is not assumed: `cov9` is scored on
those 220 seeds.

The displayed remaining-bit predicate is

```text
Q8(f) := (wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1).
```

That is `wt1∨adj2∨opp2∨vertex3`. Mixed3 is free in `Q8`.
Displayed, not adopted.

## Theorem 1 — `cov9>0` is not equivalent to `Q8`; positivity does imply `Q8`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov9` on the
220 nine-site seeds. Then `cov9(f) > 0` is not equivalent to `Q8`. There
are four mismatches. Positivity does imply `Q8`: there is no
`Q8`-false positive.

The four `Q8`-true maps with `cov9 = 0` are
`(0, 1, 0, 0, 0)`, `(1, 0, 0, 0, 0)`, `(1, 0, 0, 0, 1)`, and
`(1, 1, 0, 0, 0)`.

The two `Q8`-false maps are both zeros: `(0, 0, 0, 0, 0)` and
`(0, 0, 0, 0, 1)`. No `Q8`-false map has `cov9 > 0`.

The unique `Q6`-false map with `cov9 > 0` is `(0, 1, 0, 0, 1)`:
`wt1 = 0`, `adj2 = 0`, `vertex3 = 0`, `opp2=1`, and `cov9 = 4`. That
witness is `Q8`-true, so it does not refuse `cov9>0 ⇒ Q8`.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 1, 0, 0, 0)`: `cov9 = 0`
and `Q8` is true.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q8` and has
`cov9 = 220`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q8`, `N_both`

Among the 32 maps:

- `N_pos = 26` maps have `cov9 > 0`;
- `N_Q8 = 30` maps satisfy `Q8`;
- `N_both = 26` maps satisfy both.

The counts already refuse equivalence and confirm the one-sided
implication: `N_both = 26` equals `N_pos = 26` and is strictly smaller
than `N_Q8 = 30`. Four mismatches are `Q8`-true zeros. No mismatch is a
`Q8`-false positive. Sufficiency of `Q8` for positivity fails; necessity
holds.

## Theorem 3 — display; do not adopt Q8

`Q8` is the remaining-bit predicate `wt1∨adj2∨opp2∨vertex3`. On this
patch it does not equal 9-site positivity, and positivity does imply
`Q8`. Displayed, not adopted. Do not adopt Q8. Do not write `Q8` into
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
| `Q8` as `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` | displayed, not adopted |
| `cov9>0` iff `Q8` | fails; lex-first miss `(0, 1, 0, 0, 0)` |
| positivity implies `Q8` | holds; no `Q8`-false positive |
| `N_pos = 26`, `N_Q8 = 30`, `N_both = 26` | proved by exhaustive scoring |
| leftover-character of c9q6 | refused; Q6-imply failed, Q8-imply is a new fact |
| leftover-character of c9sel | refused; dedicated iff and imply test |
| leftover-character of the naming of `Q8` | refused; same OR, new comparison to `cov9>0` |
| adoption of `Q8` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c9q6: that already showed that `cov9>0` is
not equivalent to `Q6` and that positivity does not imply `Q6`, with
unique `Q6`-false positive `(0, 1, 0, 0, 1)`. That witness has
`opp2=1`, so it is `Q8`-true. Echoing a failed three-bit implication is
not a substitute for the four-bit iff and imply test.

Not leftover-character of c9sel: that remaining-bit menu already reported
`N_pos = 26` and `N_Q8 = 30` and that `cov9>0` is not equivalent to `Q8`.
A search report is not a substitute for the dedicated positivity-versus-`Q8`
iff and implication theorems at this seed size.

New k for Q8: naming `wt1∨adj2∨opp2∨vertex3` is not a substitute for
scoring it against `cov9>0` on the 32 maps. May still imply even though
Q6-imply failed.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q8` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 9-site positivity equals displayed `Q8` inside `F_cut` on this patch, and whether positivity implies that OR. |
| V2 | Current main has the axiom memo. Investment c9q6 already showed that positivity does not imply `Q6`. Investment c9sel already reported `N_pos = 26` and `N_Q8 = 30`. There is no landed 9-site positivity-versus-`Q8` iff and imply test. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a named 4-bit OR. |
| V5 | Equivalence fails, positivity does imply `Q8`, one lex-first miss is reported, and displayed `Q8` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov9>0` is not `Q8`. Positivity does imply `Q8`. Displayed `Q8` is
not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c9q6 | treat the test as leftover-character of the failed `Q6` implication | **ATTEMPTED** |
| leftover of c9sel | treat the dedicated test as leftover-character of the nine-site menu counts | **ATTEMPTED** |
| adopt `Q8` | write `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the c9q6 failed implication, the c9sel menu
counts, and the naming of `Q8` are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q8` are declared. Equivalence of `cov9>0` with `Q8` is not silently
assumed. The implication `cov9>0 ⇒ Q8` is scored and holds; it is not
imported from the failed `Q6` implication.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
9-site positivity equals displayed `Q8` on the declared patch, and
whether positivity implies that OR, as New k for Q8, and not
leftover-character of c9q6 or leftover-character of c9sel.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `N_pos`, `N_Q8`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q8` or `cov9>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c9q6 already showed that positivity fails to imply the
named 3-bit OR `Q6` at this same seed size, and c9sel already counted
`N_pos = 26` and `N_Q8 = 30`, so either the nine-site `Q8` comparison
is leftover-character of those reports, or the failed `Q6` implication
must also fail for `Q8`.

**Answer:** `Q8` fails equivalence at this k, but positivity does imply
`Q8`: thirty maps satisfy `Q8` and twenty-six maps have `cov9>0`, and
all twenty-six positive maps satisfy `Q8`. The unique `Q6`-false
positive `(0, 1, 0, 0, 1)` has `opp2=1` and is `Q8`-true. The
lex-first miss `(0, 1, 0, 0, 0)` has `cov9 = 0` and `Q8` true. The
four `Q8`-true zeros are `(0, 1, 0, 0, 0)`, `(1, 0, 0, 0, 0)`,
`(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 0)`. Displayed `Q8` is not
adopted.

### N8 — cross-cycle echo

Investment c9q6 already showed that `cov9>0` is not equivalent to `Q6`
and that positivity does not imply `Q6`, with unique false positive
`(0, 1, 0, 0, 1)`. Investment c9sel already reported `N_pos = 26` and
`N_Q8 = 30` inside a menu search. Echoing either fact is not a
substitute for the dedicated nine-site `Q8` iff and imply test: the
lex-first miss and the triple `(N_pos, N_Q8, N_both) = (26, 30, 26)`
are nine-site facts about this named OR. New k for Q8.

No-Go Discipline disposition: **PASS** for the finite comparison, the
narrow nonequivalence report, and the one-sided implication. FAIL / DO NOT SHIP
for “displayed `Q8` is the physical rule” or “adopt Q8.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov9` on the
220 nine-site seeds, compares positivity with displayed `Q8`, reports that
the two are not equivalent, reports that positivity does imply `Q8`,
reports one lex-first miss `(0, 1, 0, 0, 0)` with `cov9 = 0`, and reports
`N_pos = 26`, `N_Q8 = 30`, and `N_both = 26`. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.
