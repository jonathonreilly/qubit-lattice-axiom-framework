---
claim_id: f_cut_cov11_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov11>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov11_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search For A Selector Equal To `cov11>0`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 11-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against displayed `Q_*`,
displayed `Q4`, and every displayed 1-bit or 2-bit remaining-bit OR.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov11_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov11_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6516 showed that `cov1>0` if and only if
`Q_*(f) := (wt1=1) and (adj2=1)`. Investment #6518 showed that `cov4>0`
if and only if `Q4(f) := (wt1=1) or (adj2=1)`. Investment #6476 showed
that `Max(k)=Max(12-k)` only for `k=4,5`. Duality is not assumed. This
note asks a new `k` question: whether `cov11>0` equals `Q_*`, equals
`Q4`, or equals any displayed 1-bit remaining-bit predicate or any
displayed 2-bit OR. New k. Not leftover-character of those investments
and not a Max(11) rename.

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

- Theorem 1. `cov11>0` is not equivalent to `Q_*`, is not equivalent to
  `Q4`, and is not equivalent to any displayed 1-bit predicate. Exactly
  one displayed 2-bit OR equals `cov11>0`, namely `adj2 OR vertex3`.
  One lex-first remaining-bit miss is reported for each failing
  displayed `Q`.
- Theorem 2. `N_pos = 24`. For each displayed `Q`, the pair
  `(N_Q, N_both)` is reported in the table below.
- Theorem 3. The menu is displayed. Do not adopt a bit.

Do not adopt Q_*. Do not adopt Q4. Do not adopt `adj2 OR vertex3`. Do
not write a remaining-bit formula into Admissibility. Displayed, not
adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 12 eleven-site seeds of the two-cube. Whether cov11>0 equals Q_*, Q4, or any displayed 1-bit or 2-bit OR is a finite exact fact. Duality is not assumed. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov11_positive_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov11>0 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 11-site positivity selector search; do not adopt a displayed bit"
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

The eleven-site seeds are the `C(12,11) = 12` subsets of size 11 in `T`.
Then `cov11(f)` is the number of those subsets from which `f` fills. The
boolean scored here is `cov11(f)>0`.

The displayed remaining-bit predicates are:

```text
Q_*(f) := (wt1 = 1) and (adj2 = 1).
Q4(f) := (wt1 = 1) or (adj2 = 1).
```

together with each standalone remaining bit and each OR of two remaining
bits, in remaining-bit order. `Q4` is the same formula as `wt1 OR adj2`.
Displayed, not adopted. Duality is not assumed.

## Theorem 1 — `cov11>0` equals one displayed 2-bit OR; one lex-first miss of each failure

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov11` on the
12 eleven-site seeds. Then `cov11(f) > 0` is not equivalent to `Q_*`, is
not equivalent to `Q4`, and is not equivalent to any displayed 1-bit
predicate. Exactly one displayed 2-bit OR equals `cov11>0`, namely
`adj2 OR vertex3`.

`N_pos = 24`. The lex-first remaining-bit miss of each failing displayed
`Q`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, is:

| displayed `Q` | `cov11>0` iff `Q` | lex-first miss | `cov11` of miss | `Q` at miss |
|---|---|---|---:|---|
| `wt1` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `opp2` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `adj2` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `vertex3` | no | `(0, 0, 1, 0, 0)` | 4 | 0 |
| `mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `wt1 OR opp2` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `wt1 OR adj2` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `wt1 OR vertex3` | no | `(0, 0, 1, 0, 0)` | 4 | 0 |
| `wt1 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `opp2 OR adj2` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `opp2 OR vertex3` | no | `(0, 0, 1, 0, 0)` | 4 | 0 |
| `opp2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `adj2 OR vertex3` | yes | none | — | — |
| `adj2 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `vertex3 OR mixed3` | no | `(0, 0, 0, 0, 1)` | 0 | 1 |
| `Q_*` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |
| `Q4` | no | `(0, 0, 0, 1, 0)` | 8 | 0 |

The named `Q_*` miss is remaining bits `(0, 0, 0, 1, 0)`: `Q_*` is false
and `cov11 = 8`. The named `Q4` miss is the same remaining-bit tuple:
`Q4` is false and `cov11 = 8`. The matching formula
`adj2 OR vertex3` has no miss.

## Theorem 2 — `N_pos` and, for each displayed `Q`, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 24` maps have `cov11 > 0`. For each displayed
`Q`, write `N_Q` for the number of maps with `Q` true and `N_both` for
the number with both `Q` and `cov11>0`.

| displayed `Q` | `N_Q` | `N_pos` | `N_both` |
|---|---:|---:|---:|
| `wt1` | 16 | 24 | 12 |
| `opp2` | 16 | 24 | 12 |
| `adj2` | 16 | 24 | 16 |
| `vertex3` | 16 | 24 | 16 |
| `mixed3` | 16 | 24 | 12 |
| `wt1 OR opp2` | 24 | 24 | 18 |
| `wt1 OR adj2` | 24 | 24 | 20 |
| `wt1 OR vertex3` | 24 | 24 | 20 |
| `wt1 OR mixed3` | 24 | 24 | 18 |
| `opp2 OR adj2` | 24 | 24 | 20 |
| `opp2 OR vertex3` | 24 | 24 | 20 |
| `opp2 OR mixed3` | 24 | 24 | 18 |
| `adj2 OR vertex3` | 24 | 24 | 24 |
| `adj2 OR mixed3` | 24 | 24 | 20 |
| `vertex3 OR mixed3` | 24 | 24 | 20 |
| `Q_*` | 8 | 24 | 8 |
| `Q4` | 24 | 24 | 20 |

Every `Q_*`-true count agrees with `N_Q_* = 8` and `N_both = 8`. Every
`Q4`-true count agrees with `N_Q4 = 24` and `N_both = 20`. Equivalence
fails because those triples are not `(24, 24, 24)`. The displayed
`adj2 OR vertex3` count agrees with `N_both = 24`.

`Q_*` is strictly smaller than positivity: all eight `Q_*` maps have
`cov11>0`, and sixteen further maps have `cov11>0` with `Q_*` false.
`Q4` is incomparable with positivity: four `Q4`-true maps have
`cov11 = 0`, namely `(1, 0, 0, 0, 0)`, `(1, 1, 0, 0, 0)`,
`(1, 0, 0, 0, 1)`, and `(1, 1, 0, 0, 1)`, and four `Q4`-false maps have
`cov11>0`.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q_*`, `Q4`,
and `adj2 OR vertex3`, and has `cov11 = 12`. That is consistent with
Theorem 2 and does not restore the failed equivalences.

## Theorem 3 — display; do not adopt a bit

The menu, the counts, the matching 2-bit OR, and the lex-first misses
are displayed data. Do not adopt a bit. Do not adopt Q_*. Do not adopt
Q4. Do not adopt `adj2 OR vertex3`. Do not adopt `f_L1`. Do not write
`Q_*` into Admissibility. Do not write `Q4` into Admissibility.
Admissibility does not name these remaining-bit formulas.

The identities that hold or fail here are finite facts about
occupancy-to-lock on this two-cube with off-patch `o=0`. They are not a
physical formation-site selector and not an axiom edit. Duality is not
assumed.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 12 eleven-site seeds, off-patch `o=0` | declared finite patch |
| `cov11>0` iff `Q_*` | fails; lex-first miss `(0, 0, 0, 1, 0)` |
| `cov11>0` iff `Q4` | fails; lex-first miss `(0, 0, 0, 1, 0)` |
| each 1-bit versus `cov11>0` | all fail; one lex-first miss each |
| each 2-bit OR versus `cov11>0` | only `adj2 OR vertex3` matches |
| `N_pos = 24` and per-`Q` `(N_Q, N_both)` | proved by exhaustive scoring |
| leftover-character of #6516 or #6476 | refused; new k |
| Max complementarity / duality | not assumed |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6516: that closed `cov1>0` iff `Q_*` on
one-site seeds. The present count is `cov11` on 12 eleven-site seeds, a
different seed family. Duality is not assumed, so the `k=1` identity is
not inherited.

Not leftover-character of #6476: that compared `Max(k)` with `Max(12-k)`
and found equality only for `k=4,5`. The present object is 11-site
positivity versus displayed remaining-bit predicates, not a maximizer
complementarity.

The note is not a Max(11) ranking and not a seed-table: maximizers of
`cov11` are not selected, and no seed census of a named map is compiled
beyond the positivity boolean.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q_*` into Admissibility. Do not write `Q4` into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit predicate equals `cov11>0` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6516 identity at `k=1`, but no landed 11-site remaining-bit positivity search. |
| V3 | The 32 maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared candidate menu. |
| V5 | Equivalence fails for `Q_*`, `Q4`, and every 1-bit; one displayed 2-bit OR matches and is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov11>0` is not `Q_*`, not `Q4`, and not
any displayed 1-bit among the 32 `F_cut` maps on this patch. The one
matching 2-bit OR is displayed, not adopted. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6516 | treat 11-site positivity as leftover-character of `cov1>0` iff `Q_*` | **ATTEMPTED** |
| leftover of #6476 | treat the count as leftover-character of `Max(k)=Max(12-k)` | **ATTEMPTED** |
| inherited duality | identify `cov11>0` with `cov1>0` by `k` with `12-k` | **ATTEMPTED** |
| adopt a bit | write a remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed `Q_*` and `Q4` equivalences, the Hamming contrast, the #6476
maximizer complementarity, and the off-patch convention are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 12 eleven-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed menu are declared. Duality is not assumed. Equivalence of
`cov11>0` with `Q_*` or `Q4` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether a
displayed remaining-bit predicate equals `cov11>0` on the declared patch,
not leftover-character of #6516 or #6476, and not a Max(11)
ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 12 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `(N_Q, N_both)` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside the displayed remaining-bit menu, and any
independently derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6516 already showed that positivity is `Q_*`, and #6476
would make `k=11` the complementary twin of `k=1`, so `cov11>0` must
inherit `Q_*` or at least `Q4`.

**Answer:** Duality is not assumed and inheritance fails at `k=11`.
Twenty-four maps have `cov11>0`, eight satisfy `Q_*`, and twenty-four
satisfy `Q4` with only twenty both. The lex-first `Q_*` miss
`(0, 0, 0, 1, 0)` has `Q_*` false and `cov11 = 8`. The same tuple is
the lex-first `Q4` miss. One displayed 2-bit OR, `adj2 OR vertex3`,
matches and is not adopted.

### N8 — cross-cycle echo

Investment #6516 already showed that `cov1>0` is `Q_*`. Investment #6476
already compared complementary maximizers and found equality only for
`k=4,5`. Echoing either fact is not a substitute for the eleven-site
count: `k=11` is a new seed family, duality is not assumed, and the
lex-first misses and the triples `(N_Q, N_pos, N_both)` are eleven-site
facts.

No-Go Discipline disposition: **PASS** for the finite candidate census
and the narrow equivalence report. FAIL / DO NOT SHIP for “`cov11>0` is
`Q_*`,” “`cov11>0` is `Q4`,” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov11` on the
12 eleven-site seeds, tests displayed `Q_*`, displayed `Q4`, and every
displayed 1-bit or 2-bit OR against `cov11>0`, reports one lex-first miss
of each failure, and reports `N_pos = 24` together with each
`(N_Q, N_both)`. Declared audit inputs are this note and the axiom memo;
the runner writes no cache and authors no audit verdict.
