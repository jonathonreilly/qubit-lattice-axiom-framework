---
claim_id: f_cut_cov11_q6_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov11>0 equals wt1∨adj2∨vertex3, and whether positivity implies that OR, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov11_q6_selector_test_2026_08_15.py
---

# Whether `cov11>0` Equals Displayed `wt1 ∨ adj2 ∨ vertex3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 11-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q6`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov11_q6_selector_test_2026_08_15.py`](../scripts/f_cut_cov11_q6_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c7q6 showed that `cov7>0` implies `Q6`. Investment c11sel
showed `N_pos = 24` at `k=11` and that `N_Q6 = 28` for the named 3-bit
OR. The remaining-bit predicate `Q6` was already named by the identity
`Q6=cov6>0`:

```text
Q6(f) := (wt1 = 1) or (adj2 = 1) or (vertex3 = 1).
```

This note tests that named 3-bit OR at `k=11`. New k for the named 3-bit
OR. Not leftover-character of c7q6, and not leftover-character of c11sel.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov11(f) = |{S : |S|=11 and f fills from S}|`. Then:

- Theorem 1. `cov11>0` is not equivalent to `Q6`. Positivity implies
  `Q6`. One lex-first remaining-bit miss is reported.
- Theorem 2. `N_pos = 24`, `N_Q6 = 28`, `N_both = 24`.
- Theorem 3. `Q6` is displayed. Do not adopt Q6.

Do not write `Q6` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 12 eleven-site seeds of the two-cube. Whether cov11>0 equals displayed Q6, and whether positivity implies that OR, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov11_q6_selector_test
target_blocker_text: "whether cov11>0 equals wt1 or adj2 or vertex3 among the 32 F_cut maps, and whether positivity implies that OR"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 11-site positivity-versus-Q6 comparison; do not adopt displayed Q6"
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

The eleven-site seeds are the `C(12,11) = 12` subsets of size 11 in `T`.
Then `cov11(f)` is the number of those subsets from which `f` fills. The
boolean scored here is `cov11(f)>0`. Duality is not assumed: `cov11` is
scored on those 12 seeds.

The displayed remaining-bit predicate is

```text
Q6(f) := (wt1=1) or (adj2=1) or (vertex3=1).
```

That is `wt1∨adj2∨vertex3`. Opp2 and mixed3 are free in `Q6`.
Displayed, not adopted.

## Theorem 1 — `cov11>0` is not equivalent to `Q6`; positivity implies `Q6`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov11` on the
12 eleven-site seeds. Then `cov11(f) > 0` is not equivalent to `Q6`. There
are four mismatches. Positivity implies `Q6`.

The four `Q6`-true maps with `cov11 = 0` are
`(1, 0, 0, 0, 0)`, `(1, 1, 0, 0, 0)`, `(1, 0, 0, 0, 1)`, and
`(1, 1, 0, 0, 1)`. There is no `Q6`-false map with `cov11 > 0`.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(1, 0, 0, 0, 0)`: `cov11 = 0`
and `Q6` is true (`wt1 = 1`).

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q6` and has
`cov11 = 12`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q6`, `N_both`

Among the 32 maps:

- `N_pos = 24` maps have `cov11 > 0`;
- `N_Q6 = 28` maps satisfy `Q6`;
- `N_both = 24` maps satisfy both.

The counts already refuse equivalence: `N_both = 24` equals `N_pos` and is
strictly smaller than `N_Q6`. The four mismatches of Theorem 1 are all on
the `Q6` side. Necessity holds; sufficiency fails.

## Theorem 3 — display; do not adopt Q6

`Q6` is the remaining-bit predicate already named by `Q6=cov6>0`. On this
patch it is necessary for 11-site positivity and is not equal to 11-site
positivity. Displayed, not adopted. Do not adopt Q6. Do not write `Q6`
into Admissibility. Admissibility does not name this remaining-bit
formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 12 eleven-site seeds, off-patch `o=0` | declared finite patch |
| `Q6` as `(wt1=1) or (adj2=1) or (vertex3=1)` | displayed, not adopted |
| `cov11>0` iff `Q6` | fails; lex-first miss `(1, 0, 0, 0, 0)` |
| positivity implies `Q6` | holds; no `Q6`-false positive |
| `N_pos = 24`, `N_Q6 = 28`, `N_both = 24` | proved by exhaustive scoring |
| leftover-character of c7q6 | refused; new k for the same named OR |
| leftover-character of c11sel | refused; named 3-bit OR, not a remaining-bit menu search |
| adoption of `Q6` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c7q6: that already showed that `cov7>0` implies
`Q6` at a different seed size. Echoing that seven-site implication is not
a substitute for the eleven-site comparison.

Not leftover-character of c11sel: that already reported `N_pos = 24` and
the size `N_Q6 = 28` of the named 3-bit OR, and searched displayed 1-bit
and 2-bit remaining-bit predicates. The present object is whether the
separately named identity `Q6=cov6>0` equals 11-site positivity, and
whether positivity implies that OR. New k for the named 3-bit OR.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q6` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 11-site positivity equals displayed `Q6` inside `F_cut` on this patch, and whether positivity implies that OR. |
| V2 | Current main has the axiom memo, but no landed 11-site positivity-versus-`Q6` test. |
| V3 | The 32 maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a newly displayed 3-bit OR at this seed size. |
| V5 | Equivalence fails, positivity implies `Q6`, one lex-first miss is reported, and displayed `Q6` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov11>0` is not `Q6`, while positivity does imply `Q6`. Displayed
`Q6` is not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c7q6 | treat the test as leftover-character of “`cov7>0` implies `Q6`” | **ATTEMPTED** |
| leftover of c11sel | treat the test as leftover-character of the 11-site remaining-bit search | **ATTEMPTED** |
| implication as equivalence | replace the iff test by the one-sided implication that holds | **ATTEMPTED** |
| adopt `Q6` | write `(wt1=1) or (adj2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the seven-site implication, the eleven-site
remaining-bit search, the one-sided implication, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 12 eleven-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q6` are declared. Equivalence of `cov11>0` with `Q6` is not silently
assumed. The implication `cov11>0 ⇒ Q6` is scored, not imported.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
11-site positivity equals displayed `Q6` on the declared patch, as a
named 3-bit OR at a new k, and not leftover-character of c7q6 or c11sel.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 12 seeds | no physical law selection |
| per block | `N_pos`, `N_Q6`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q6` or `cov11>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c7q6 already showed that positivity implies `Q6`, and
c11sel already reported `N_pos = 24` with `N_Q6 = 28`, so the same 3-bit
OR must be the k=11 selector, the implication must be an equivalence, and
that match must be written into Admissibility.

**Answer:** `Q6` is necessary at `k=11` and is not sufficient: twenty-eight
maps satisfy `Q6` and twenty-four maps have `cov11>0`, and all
twenty-four positive maps satisfy `Q6`. The lex-first miss
`(1, 0, 0, 0, 0)` has `cov11 = 0` and `Q6` true. Displayed `Q6` is not
adopted.

### N8 — cross-cycle echo

Investment c7q6 already showed that `cov7>0` implies `Q6`. Investment
c11sel already reported `N_pos = 24` and `N_Q6 = 28` at this seed size.
Echoing either fact is not a substitute for the eleven-site `Q6`
comparison: the lex-first miss and the triple
`(N_pos, N_Q6, N_both) = (24, 28, 24)` are eleven-site facts about this
named 3-bit OR.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow nonequivalence report. FAIL / DO NOT SHIP for “displayed `Q6`
is the physical rule” or “adopt Q6.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov11` on the
12 eleven-site seeds, compares positivity with displayed `Q6`, reports that
the two are not equivalent, reports that positivity implies `Q6`,
reports one lex-first miss `(1, 0, 0, 0, 0)` with `cov11 = 0`, and reports
`N_pos = 24`, `N_Q6 = 28`, and `N_both = 24`. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.
