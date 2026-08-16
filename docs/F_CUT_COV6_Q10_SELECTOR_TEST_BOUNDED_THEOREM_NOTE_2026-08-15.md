---
claim_id: f_cut_cov6_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov6>0 equals adj2∨vertex3∨mixed3 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov6_q10_selector_test_2026_08_15.py
---

# Whether `cov6>0` Equals Displayed `adj2 ∨ vertex3 ∨ mixed3`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 6-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q10`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov6_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov6_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 showed that `Q10=cov10>0` for the displayed remaining-bit
predicate

```text
Q10(f) := (adj2 = 1) or (vertex3 = 1) or (mixed3 = 1).
```

Investment #6531 already named `Q6=cov6>0`. This note tests the new
predicate `Q10` against that already named k=6 selector. New predicate
versus an already named k=6 selector. Not leftover-character of #6531,
not leftover-character of the `cov10>0` 3-bit OR, and not a rename of
`Q6`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov6(f) = |{S : |S|=6 and f fills from S}|`. Then:

- Theorem 1. `cov6>0` is not equivalent to `Q10`. One lex-first
  remaining-bit miss is reported.
- Theorem 2. `N_pos = 28`, `N_Q10 = 28`, `N_both = 26`.
- Theorem 3. `Q10` is displayed. Do not adopt Q10.

Do not write `Q10` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 924 six-site seeds of the two-cube. Whether cov6>0 equals displayed Q10 is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov6_q10_selector_test
target_blocker_text: "whether cov6>0 equals adj2 or vertex3 or mixed3 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 6-site positivity-versus-Q10 comparison; do not adopt displayed Q10"
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
predicate. `Q10` is a displayed remaining-bit formula, not axiom content.

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

The six-site seeds are the `C(12,6) = 924` subsets of size 6 in `T`. Then
`cov6(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov6(f)>0`. Duality is not assumed: `cov6` is scored on
those 924 seeds.

The displayed remaining-bit predicate is

```text
Q10(f) := (adj2 = 1) or (vertex3 = 1) or (mixed3 = 1).
```

That is `adj2∨vertex3∨mixed3`. Wt1 and opp2 are free in `Q10`.
Displayed, not adopted.

## Theorem 1 — `cov6>0` is not equivalent to `Q10`; one lex-first miss

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov6` on the
924 six-site seeds. Then `cov6(f) > 0` is not equivalent to `Q10`. There
are four mismatches.

The two `Q10`-true maps with `cov6 = 0` are
`(0, 0, 0, 0, 1)` and `(0, 1, 0, 0, 1)`.

The two `Q10`-false maps with `cov6 > 0` are
`(1, 0, 0, 0, 0)` (`cov6 = 4`) and `(1, 1, 0, 0, 0)` (`cov6 = 12`).

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 0, 0, 1)`: `cov6 = 0`
and `Q10` is true (`mixed3 = 1`).

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q10` and has
`cov6 = 920`. That is consistent with Theorem 2 and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q10`, `N_both`

Among the 32 maps:

- `N_pos = 28` maps have `cov6 > 0`;
- `N_Q10 = 28` maps satisfy `Q10`;
- `N_both = 26` maps satisfy both.

The counts already refuse equivalence: `N_both = 26` is strictly smaller
than both `N_pos` and `N_Q10`. The four mismatches of Theorem 1 account
for the gap of two on each side.

## Theorem 3 — display; do not adopt Q10

`Q10` is the remaining-bit predicate that investment c10bit3 displayed
as equal to `cov10>0`. On this patch it does not equal 6-site positivity.
Displayed, not adopted. Do not adopt Q10. Do not write `Q10` into
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
| two-cube, 924 six-site seeds, off-patch `o=0` | declared finite patch |
| `Q10` as `(adj2=1) or (vertex3=1) or (mixed3=1)` | displayed, not adopted |
| `cov6>0` iff `Q10` | fails; lex-first miss `(0, 0, 0, 0, 1)` |
| `N_pos = 28`, `N_Q10 = 28`, `N_both = 26` | proved by exhaustive scoring |
| leftover-character of #6531 | refused; new predicate versus already named k=6 selector |
| leftover-character of `Q10=cov10>0` | refused; new k for the same displayed OR |
| adoption of `Q10` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6531: that already named `Q6=cov6>0` as
`(wt1=1) or (adj2=1) or (vertex3=1)`. The present object is whether the
new displayed 3-bit OR `Q10` equals that same already named k=6
selector. New predicate versus an already named k=6 selector.

Not leftover-character of c10bit3: that closed `Q10=cov10>0` at a
different seed size. Echoing that ten-site identity is not a substitute
for the six-site comparison.

The note is not a rename of `Q6`. The two displayed ORs differ on the
four remaining-bit tuples of Theorem 1.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q10` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 6-site positivity equals displayed `Q10` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo, the already named k=6 selector #6531, and the c10bit3 fact `Q10=cov10>0`, but no landed 6-site positivity-versus-`Q10` test. |
| V3 | The 32 maps, 924 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a newly displayed 3-bit OR. |
| V5 | Equivalence fails, one lex-first miss is reported, and displayed `Q10` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the 32 `F_cut` maps on this patch,
`cov6>0` is not `Q10`. Displayed `Q10` is not axiom content. No global
compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6531 | treat the test as leftover-character of already named `Q6=cov6>0` | **ATTEMPTED** |
| leftover of `Q10=cov10>0` | treat six-site positivity as leftover-character of the ten-site OR | **ATTEMPTED** |
| rename of `Q6` | identify `Q10` with the already named k=6 selector | **ATTEMPTED** |
| adopt `Q10` | write `(adj2=1) or (vertex3=1) or (mixed3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the already named k=6 selector, the ten-site OR,
and the off-patch convention are distinct. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q10` are declared. Equivalence of `cov6>0` with `Q10` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
6-site positivity equals displayed `Q10` on the declared patch, as a
new predicate versus an already named k=6 selector, and not leftover-character of #6531.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 924 seeds | no physical law selection |
| per block | `N_pos`, `N_Q10`, and `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q10` or `cov6>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c10bit3 already showed that `Q10` equals positivity at
`k=10`, and #6531 already named positivity at `k=6`, so the same 3-bit
OR must be the k=6 selector, and that match must be written into
Admissibility.

**Answer:** `Q10` fails at `k=6`: twenty-eight maps satisfy `Q10` and
twenty-eight have `cov6>0`, but only twenty-six satisfy both. The
lex-first miss `(0, 0, 0, 0, 1)` has `cov6 = 0` and `Q10` true.
Displayed `Q10` is not adopted.

### N8 — cross-cycle echo

Investment #6531 already named `Q6=cov6>0`. Investment c10bit3 already
showed `Q10=cov10>0`. Echoing either fact is not a substitute for the
six-site `Q10` count: the lex-first miss and the triple
`(N_pos, N_Q10, N_both) = (28, 28, 26)` are six-site facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow nonequivalence report. FAIL / DO NOT SHIP for “displayed `Q10`
is the physical rule” or “adopt Q10.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov6` on the
924 six-site seeds, compares positivity with displayed `Q10`, reports that
the two are not equivalent, reports one lex-first miss
`(0, 0, 0, 0, 1)` with `cov6 = 0`, and reports `N_pos = 28`,
`N_Q10 = 28`, and `N_both = 26`. Declared audit inputs are this note and
the axiom memo; the runner writes no cache and authors no audit verdict.
