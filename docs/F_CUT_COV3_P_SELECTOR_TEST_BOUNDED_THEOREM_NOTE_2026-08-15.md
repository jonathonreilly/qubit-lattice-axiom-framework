---
claim_id: f_cut_cov3_p_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov3>0 equals P, and whether positivity implies P, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov3_p_selector_test_2026_08_15.py
---

# Whether `cov3>0` Equals Displayed `P`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 3-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `P`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov3_p_selector_test_2026_08_15.py`](../scripts/f_cut_cov3_p_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c3q10 showed that cov3>0 does not imply Q10 for the displayed
remaining-bit predicate `(adj2=1) or (vertex3=1) or (mixed3=1)`. Investment
#6494 already named as cov2>0 the remaining-bit predicate

```text
P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0).
```

`P` is not a pure AND/OR of remaining bits. Not leftover-character of the
1–5-bit remaining-bit menu. This note tests that named selector at the
seed size where Q10-imply failed (`k=3`).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov3(f) = |{S : |S|=3 and f fills from S}|`. Then:

- Theorem 1. `cov3>0` is not equivalent to `P`. Positivity does not
  imply `P`. One lex-first remaining-bit miss is reported.
- Theorem 2. `N_pos = 20`, `N_P = 14`, `N_both = 13`.
- Theorem 3. `P` is displayed. Do not adopt P.

Do not write `P` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 220 three-site seeds of the two-cube. Whether cov3>0 equals displayed P, and whether positivity implies P, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov3_p_selector_test
target_blocker_text: "whether cov3>0 equals P among the 32 F_cut maps, and whether positivity implies P"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 3-site positivity-versus-P comparison; do not adopt displayed P"
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
predicate. `P` is a displayed remaining-bit formula, not axiom content.

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

The three-site seeds are the `C(12,3) = 220` subsets of size 3 in `T`. Then
`cov3(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov3(f)>0`. Duality is not assumed: `cov3` is scored on
those 220 seeds.

The displayed remaining-bit predicate is

```text
P(f) := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0).
```

That is `wt1` and at least one of `adj2`, `vertex3`, `mixed3`. Opp2 is
free in `P`. Displayed, not adopted.

## Theorem 1 — `cov3>0` is not equivalent to `P`; one lex-first miss

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov3` on the
220 three-site seeds. Then `cov3(f) > 0` is not equivalent to `P`. There
are eight mismatches. Positivity does not imply `P`.

The one `P`-true map with `cov3 = 0` is
`(1, 0, 0, 0, 1)`.

The seven `P`-false maps with `cov3 > 0` are
`(0, 0, 1, 1, 0)` (`cov3 = 24`), `(0, 0, 1, 1, 1)` (`cov3 = 24`),
`(0, 1, 1, 0, 0)` (`cov3 = 16`), `(0, 1, 1, 0, 1)` (`cov3 = 16`),
`(0, 1, 1, 1, 0)` (`cov3 = 44`), `(0, 1, 1, 1, 1)` (`cov3 = 44`),
and `(1, 1, 0, 0, 0)` (`cov3 = 4`).

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 1, 1, 0)`: `cov3 = 24`
and `P` is false (`wt1 = 0`). That same map is the lex-first witness that
positivity does not imply `P`.

The map `(1, 1, 0, 0, 0)` is the unique remaining-bit tuple at which
Q10-imply already failed (`cov3 = 4` and `Q10` false). It likewise has
`P` false, so the same witness refuses `cov3>0 ⇒ P`.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `P` and has
`cov3 = 220`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_P`, `N_both`

Among the 32 maps:

- `N_pos = 20` maps have `cov3 > 0`;
- `N_P = 14` maps satisfy `P`;
- `N_both = 13` maps satisfy both.

The counts already refuse equivalence: `N_both = 13` is strictly smaller
than both `N_pos` and `N_P`. The eight mismatches of Theorem 1 account
for the gap of seven on the positivity side and one on the `P` side.

## Theorem 3 — display; do not adopt P

`P` is the remaining-bit predicate already named as cov2>0. On this
patch it does not equal 3-site positivity, and positivity does not imply
`P`. Displayed, not adopted. Do not adopt P. Do not write `P` into
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
| two-cube, 220 three-site seeds, off-patch `o=0` | declared finite patch |
| `P` as `(wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)` | displayed, not adopted |
| `cov3>0` iff `P` | fails; lex-first miss `(0, 0, 1, 1, 0)` |
| positivity implies `P` | fails; witness `(0, 0, 1, 1, 0)` |
| `N_pos = 20`, `N_P = 14`, `N_both = 13` | proved by exhaustive scoring |
| leftover-character of the 1–5-bit remaining-bit menu | refused; `P` is not a pure AND/OR |
| leftover-character of c3q10 / Q10-imply | refused; named `P` at the same `k` |
| leftover-character of naming `P` as `cov2>0` | refused; new seed size |
| adoption of `P` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the 1–5-bit remaining-bit menu: that menu was
the pure AND and the pure OR of remaining bits of each width. `P` is
not a pure AND/OR. The present object is whether the separately named
identity already named as cov2>0 equals 3-site positivity, and whether
positivity implies `P`.

Not leftover-character of c3q10: that closed `cov3>0` does not imply
`Q10` at this same seed size. Echoing that `Q10` implication failure is
not a substitute for the named-`P` comparison. The test is at the
Q10-imply seed size because that is where one-sided positivity first
failed for the 3-bit OR.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `P` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 3-site positivity equals displayed `P` inside `F_cut` on this patch, and whether positivity implies `P`. |
| V2 | Current main has the axiom memo, the failed 1–5-bit AND/OR menu for `cov3>0`, the named identity `P=cov2>0`, and the c3q10 fact that `cov3>0` does not imply `Q10`, but no landed 3-site positivity-versus-`P` implication test. |
| V3 | The 32 maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a named mixed remaining-bit predicate at the seed size where Q10-imply failed. |
| V5 | Equivalence fails, positivity does not imply `P`, one lex-first miss is reported, and displayed `P` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov3>0` is not `P`, and positivity does not imply `P`. Displayed
`P` is not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of the 1–5-bit remaining-bit menu | treat the mixed predicate as leftover-character of the pure AND/OR menu | **ATTEMPTED** |
| leftover of c3q10 / Q10-imply | treat the named-`P` test as leftover-character of the `Q10` implication failure | **ATTEMPTED** |
| leftover of naming `P` as `cov2>0` | treat three-site positivity as leftover-character of the two-site closed form | **ATTEMPTED** |
| adopt `P` | write `(wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the 1–5-bit AND/OR menu, the `Q10` implication,
the two-site naming of `P`, and the off-patch convention are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 three-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`P` are declared. Equivalence of `cov3>0` with `P` is not silently
assumed, and the implication `cov3>0 ⇒ P` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
3-site positivity equals displayed `P` on the declared patch, as a
test of the named `cov2>0` selector at the seed size where Q10-imply
failed, and not leftover-character of the 1–5-bit remaining-bit menu.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 220 seeds | no physical law selection |
| per block | `N_pos`, `N_P`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`P` or `cov3>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `P` already equals positivity at `k=2`, so the same
selector must be the `k=3` selector, positivity must imply `P`, and
that match must be written into Admissibility.

**Answer:** `P` fails at `k=3`: fourteen maps satisfy `P` and twenty
maps have `cov3>0`, but only thirteen satisfy both. The lex-first miss
`(0, 0, 1, 1, 0)` has `cov3 = 24` and `P` false, so positivity does
not imply `P`. The Q10-imply witness `(1, 1, 0, 0, 0)` has `cov3 = 4`
and `P` false as well. Displayed `P` is not adopted.

### N8 — cross-cycle echo

The 1–5-bit remaining-bit menu already showed that no pure AND or OR of
those widths equals `cov3>0`. Investment c3q10 already showed that
`cov3>0` does not imply `Q10`. Naming `P` as `cov2>0` already closed
the two-site identity. Echoing any of those facts is not a substitute
for the three-site `P` count: the lex-first miss and the triple
`(N_pos, N_P, N_both) = (20, 14, 13)` are three-site facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow nonequivalence report. FAIL / DO NOT SHIP for “displayed `P`
is the physical rule” or “adopt P.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov3` on the
220 three-site seeds, compares positivity with displayed `P`, reports that
the two are not equivalent, reports that positivity does not imply `P`,
reports one lex-first miss `(0, 0, 1, 1, 0)` with `cov3 = 24`, and reports
`N_pos = 20`, `N_P = 14`, and `N_both = 13`. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.
