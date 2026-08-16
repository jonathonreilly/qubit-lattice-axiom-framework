---
claim_id: f_cut_cov7_q4_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov7>0 equals wt1∨adj2, and whether positivity implies that OR, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov7_q4_selector_test_2026_08_15.py
---

# Whether `cov7>0` Equals Displayed `wt1 ∨ adj2`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 7-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q4`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov7_q4_selector_test_2026_08_15.py`](../scripts/f_cut_cov7_q4_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c3q10 showed that `cov7>0` is not `Q10` and that positivity
does not imply `Q10`. The unique `Q10`-false positive is `(1, 1, 0, 0, 0)`,
with `N_pos = 24`, `N_Q10 = 28`, and `N_both = 19`. The remaining-bit
predicate `Q4` was already named at `k=4` by the identity `Q4=cov4>0`:

```text
Q4(f) := (wt1 = 1) or (adj2 = 1).
```

This note tests that named 2-bit OR at the `k` where Q10-imply failed.
Named 2-bit OR at the k where Q10-imply failed. Not leftover-character of
the failed Q10-imply test, and not leftover-character of the k=4 Q4 naming.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov7(f) = |{S : |S|=3 and f fills from S}|`. Then:

- Theorem 1. `cov7>0` is not equivalent to `Q4`. Positivity implies
  `Q4`. One lex-first remaining-bit miss is reported.
- Theorem 2. `N_pos = 24`, `N_Q4 = 24`, `N_both = 20`.
- Theorem 3. `Q4` is displayed. Do not adopt Q4.

Do not write `Q4` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 792 seven-site seeds of the two-cube. Whether cov7>0 equals displayed Q4, and whether positivity implies that OR, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov7_q4_selector_test
target_blocker_text: "whether cov7>0 equals wt1 or adj2 among the 32 F_cut maps, and whether positivity implies that OR"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 7-site positivity-versus-Q4 comparison; do not adopt displayed Q4"
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
predicate. `Q4` is a displayed remaining-bit formula, not axiom content.

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

The seven-site seeds are the `C(12,7) = 792` subsets of size 3 in `T`. Then
`cov7(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov7(f)>0`. Duality is not assumed: `cov7` is scored on
those 792 seeds.

The displayed remaining-bit predicate is

```text
Q4(f) := (wt1=1) or (adj2=1).
```

That is `wt1∨adj2`. Opp2, vertex3, and mixed3 are free in `Q4`.
Displayed, not adopted.

## Theorem 1 — `cov7>0` is not equivalent to `Q4`; positivity does not imply `Q4`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov7` on the
792 seven-site seeds. Then `cov7(f) > 0` is not equivalent to `Q4`. There
are eight mismatches. Positivity does not imply `Q4`.

The four `Q4`-true maps with `cov7 = 0` are
`(1, 0, 0, 0, 0)`, `(1, 1, 0, 0, 0)`, `(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 1)`. The four `Q4`-false maps with `cov7 > 0` are `(0, 0, 0, 1, 0)`, `(0, 1, 0, 1, 0)`, `(0, 0, 0, 1, 1)`, and `(0, 1, 0, 1, 1)`.

The unique `Q10`-false positive `(1, 1, 0, 0, 0)` has `cov7 = 4` and
satisfies `Q4` (`wt1 = 1`). That witness refuses `cov7>0 ⇒ Q10` and does
not refuse `cov7>0 ⇒ Q4`.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 0, 1, 0)`: `cov7 = 16`
and `Q4` is false (`wt1 = adj2 = 0`).

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q4` and has
`cov7 = 792`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q4`, `N_both`

Among the 32 maps:

- `N_pos = 24` maps have `cov7 > 0`;
- `N_Q4 = 24` maps satisfy `Q4`;
- `N_both = 20` maps satisfy both.

The counts already refuse equivalence: `N_both = 20` equals `N_pos` and is
strictly smaller than `N_Q4`. The eight mismatches of Theorem 1 are all on
the `Q4` side. Necessity fails and sufficiency fails.

## Theorem 3 — display; do not adopt Q4

`Q4` is the remaining-bit predicate already named at `k=4` by
`Q4=cov4>0`. On this patch it is not necessary for 7-site positivity and is
not equal to 7-site positivity. Displayed, not adopted. Do not adopt Q4.
Do not write `Q4` into Admissibility. Admissibility does not name this
remaining-bit formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 seven-site seeds, off-patch `o=0` | declared finite patch |
| `Q4` as `(wt1=1) or (adj2=1)` | displayed, not adopted |
| `cov7>0` iff `Q4` | fails; lex-first miss `(0, 0, 0, 1, 0)` |
| positivity does not imply `Q4` | fails; four `Q4`-false positives |
| `N_pos = 24`, `N_Q4 = 24`, `N_both = 20` | proved by exhaustive scoring |
| leftover-character of the failed Q10-imply test | refused; named 2-bit OR at that k |
| leftover-character of the k=4 Q4 naming | refused; new seed size for the same OR |
| adoption of `Q4` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the failed Q10-imply test: that already showed
that `cov7>0` is not `Q10` and that positivity does not imply `Q10`, with
unique `Q10`-false positive `(1, 1, 0, 0, 0)`. The present object is
whether the separately named identity `Q4=cov4>0` equals 7-site
positivity, and whether positivity implies that OR. Named 2-bit OR at the
k where Q10-imply failed.

Not leftover-character of the k=4 Q4 naming: that closed `Q4=cov4>0` at
a different seed size. Echoing that four-site identity is not a substitute
for the seven-site comparison.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q4` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 7-site positivity equals displayed `Q4` inside `F_cut` on this patch, and whether positivity implies that OR. |
| V2 | Current main has the axiom memo and the c3q10 fact that positivity does not imply `Q10`, but no landed 7-site positivity-versus-`Q4` test. |
| V3 | The 32 maps, 792 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a newly displayed 2-bit OR at this seed size. |
| V5 | Equivalence fails, positivity does not imply `Q4`, one lex-first miss is reported, and displayed `Q4` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov7>0` is not `Q4`, while positivity does imply `Q4`. Displayed
`Q4` is not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of the failed Q10-imply test | treat the test as leftover-character of c3q10 | **ATTEMPTED** |
| leftover of the k=4 Q4 naming | treat seven-site positivity as leftover-character of `Q4=cov4>0` | **ATTEMPTED** |
| implication as equivalence | replace the iff test by the one-sided implication that holds | **ATTEMPTED** |
| adopt `Q4` | write `(wt1=1) or (adj2=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the failed Q10-imply test, the four-site OR, the
one-sided implication, and the off-patch convention are distinct. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 seven-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q4` are declared. Equivalence of `cov7>0` with `Q4` is not silently
assumed. The implication `cov7>0 ⇒ Q4` is scored, not imported.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
7-site positivity equals displayed `Q4` on the declared patch, as a
named 2-bit OR at the k where Q10-imply failed, and not leftover-character
of the failed Q10-imply test.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 792 seeds | no physical law selection |
| per block | `N_pos`, `N_Q4`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q4` or `cov7>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `Q4` already equals positivity at `k=4`, and the unique
`Q10`-false positive `(1, 1, 0, 0, 0)` has `wt1 = 1`, so the same 2-bit
OR must be the k=7 selector, the implication must be an equivalence, and
that match must be written into Admissibility.

**Answer:** `Q4` is necessary at `k=7` and is not sufficient: twenty-four
maps satisfy `Q4` and twenty-four maps have `cov7>0`, and only twenty positive
maps satisfy `Q4`. The lex-first miss `(0, 0, 0, 1, 0)` has `cov7 = 16`
and `Q4` true. Displayed `Q4` is not adopted.

### N8 — cross-cycle echo

The failed Q10-imply test already showed that `cov7>0` is not `Q10` and
that positivity does not imply `Q10`. The k=4 naming already showed
`Q4=cov4>0`. Echoing either fact is not a substitute for the seven-site
`Q4` count: the lex-first miss and the triple
`(N_pos, N_Q4, N_both) = (20, 24, 20)` are seven-site facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow nonequivalence report. FAIL / DO NOT SHIP for “displayed `Q4`
is the physical rule” or “adopt Q4.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov7` on the
792 seven-site seeds, compares positivity with displayed `Q4`, reports that
the two are not equivalent, reports that positivity does not imply `Q4`,
reports one lex-first miss `(0, 0, 0, 1, 0)` with `cov7 = 16`, and reports
`N_pos = 24`, `N_Q4 = 24`, and `N_both = 20`. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.
