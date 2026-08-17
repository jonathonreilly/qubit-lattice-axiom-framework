---
claim_id: named_three_slot_hopcost_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among 27 named (seed, equal, unequal) hop-costs on B_6(0), those that reverse diamond at (4,0,0) vs (2,2,2) and beat ℓ¹ variance are counted. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/named_three_slot_hopcost_b6_2026_08_15.py
---

# Named Three-Slot Hop-Cost Census On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** finite census of the 27 named `(c_seed, c_eq, c_uneq)` hop-costs on
the directed nearest-neighbor graph of `B_6(0)`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/named_three_slot_hopcost_b6_2026_08_15.py`](../scripts/named_three_slot_hopcost_b6_2026_08_15.py)

## Result Up Front

Let `B_6(0) = { v in Z^3 : |v|_1 <= 6 }`. This ball has 377 sites. On a
directed nearest-neighbor edge `v -> w` write `|σ_v|` for the number of
nonzero Cartesian coordinates of `v`, and assign the named three-slot cost

```text
c(v -> w) = c_seed    if |σ_v| = 0,
            c_eq      if |σ_v| = |σ_w|,
            c_uneq    otherwise,
```

with each slot in `{1,2,3}`. Arrival time `t` is the Dijkstra distance from
the origin on this finite directed graph. The diamond comparator at the axis
and body-diagonal probes is the integer cut

```text
12 t(4,0,0)^2  >  16 t(2,2,2)^2.
```

The `ℓ¹` comparator is the unit table `t(v) = |v|_1`. Variance means the
population variance of `|v|_2 / t(v)` on the 376 nonzero sites.

**Theorem 1.** `N_rev = 0`. None of the 27 named triples reverse the diamond.
The lex-first reversing triple does not exist, so no reversing times are
attached.

**Theorem 2.** `N_beat = 0`. Among those reversals, none can beat the `ℓ¹`
variance because the reversal set is empty.

**Theorem 3.** Displayed, not adopted. No triple is written into
Admissibility. Uniqueness is not claimed. Do not attach L1.

The investment member `(c_seed, c_eq, c_uneq) = (3,3,1)` is included in the
census. It gives `t(4,0,0)=12` and `t(2,2,2)=14`, hence
`12 t(4,0,0)^2 = 1728 < 3136 = 16 t(2,2,2)^2`, so it does not reverse. That
is consistent with `N_rev = 0`.

A matching member would be a finite named rule that both reverses the diamond
and beats `ℓ¹` variance. No such member exists inside this 27-element family.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact 27-Dijkstra census on B_6(0): N_rev=0 and N_beat=0. Displayed, not adopted. No Admissibility edit."
trace_class: negative_route_pruning
target_claim_id: named_three_slot_diamond_and_variance_member
target_blocker_text: "name a finite hop-cost rule that reverses diamond at (4,0,0) vs (2,2,2) and beats l1 variance of |v|_2/t"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Leave the 27-element three-slot family; a matching member must come from a different finite named rule, not from rescanning occupancy 8-tuples."
conditional_surface_status: "exact on B_6(0) for the 27 named triples; no physical hop-cost is selected"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

The current Admissibility wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Those sentences type a covariant local constraint. They do not name a hop-cost,
a seed-exit slot, an equal-support slot, or an unequal-support slot. This note
does not add one.

The current Lattice wording supplies the cubic lattice `Z^3` with
nearest-neighbor adjacency. The finite ball `B_6(0)` and the three-slot cost
are declared computational inputs, not added axiom wording.

## Exact Objects

Sites are points of `Z^3`. The finite host is `B_6(0)`, cardinality 377. The
directed graph uses the six axis-adjacent neighbors, restricted so that both
endpoints lie in the ball. That graph has 1752 directed edges. Support
cardinalities on those edges occupy the nine pairs

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2), (3,3).
```

The three-slot rule names every pair: seed-exit is `(0,1)`, equal-support is
any `(k,k)` with `k>0`, and unequal-support is the rest. The census therefore
does not rescan the `3^8 = 6561` occupancy 8-tuples on a smaller orbit list.
It runs 27 Dijkstras.

The probes are `p_axis = (4,0,0)` and `p_body = (2,2,2)`. Their Euclidean
squares are `|p_axis|_2^2 = 16` and `|p_body|_2^2 = 12`. The diamond cut is
exactly

```text
t(p_axis)^2 / 16  >  t(p_body)^2 / 12,
```

written with integer cross-multiplication as `12 t(p_axis)^2 > 16 t(p_body)^2`.

Variance on a complete arrival table `t` is

```text
μ(t)   = (1/376) sum_{v ≠ 0} |v|_2 / t(v),
Var(t) = (1/376) sum_{v ≠ 0} ( |v|_2 / t(v) − μ(t) )^2.
```

The `ℓ¹` table is `t_1(v) = |v|_1`. A reversal beats `ℓ¹` when
`Var(t) < Var(t_1)`.

## Exact Theorem

**Theorem 1 (reversal count).** Let `F` be the lex-ordered set
`{1,2,3}^3` of named triples `(c_seed, c_eq, c_uneq)`. For each member run
Dijkstra on `B_6(0)` from the origin. Then

```text
N_rev = # { ρ in F : 12 t_ρ(4,0,0)^2 > 16 t_ρ(2,2,2)^2 } = 0.
```

The lex-first reversing triple does not exist.

**Theorem 2 (variance-beating count).** Let `R` be the reversal set of
Theorem 1. Then

```text
N_beat = # { ρ in R : Var(t_ρ) < Var(t_1) } = 0.
```

There is no lex-first beating reversal and therefore no pair of variances to
report from `R`.

**Theorem 3 (adoption boundary).** The 27 tables are displayed finite
comparators. They are not adopted as the Admissibility rule. Uniqueness is not
claimed. Do not attach L1: the unit table is a comparator only.

## Arrival Census

Every triple produces a finite arrival time at every site of `B_6(0)`. The
probe times are:

| `(c_seed, c_eq, c_uneq)` | `t(4,0,0)` | `t(2,2,2)` | `12 t_axis^2` | `16 t_body^2` | reverse |
|---|---:|---:|---:|---:|---|
| `(1,1,1)` | 4 | 6 | 192 | 576 | no |
| `(1,1,2)` | 4 | 8 | 192 | 1024 | no |
| `(1,1,3)` | 4 | 10 | 192 | 1600 | no |
| `(1,2,1)` | 7 | 9 | 588 | 1296 | no |
| `(1,2,2)` | 7 | 11 | 588 | 1936 | no |
| `(1,2,3)` | 7 | 13 | 588 | 2704 | no |
| `(1,3,1)` | 10 | 12 | 1200 | 2304 | no |
| `(1,3,2)` | 10 | 14 | 1200 | 3136 | no |
| `(1,3,3)` | 10 | 16 | 1200 | 4096 | no |
| `(2,1,1)` | 5 | 7 | 300 | 784 | no |
| `(2,1,2)` | 5 | 9 | 300 | 1296 | no |
| `(2,1,3)` | 5 | 11 | 300 | 1936 | no |
| `(2,2,1)` | 8 | 10 | 768 | 1600 | no |
| `(2,2,2)` | 8 | 12 | 768 | 2304 | no |
| `(2,2,3)` | 8 | 14 | 768 | 3136 | no |
| `(2,3,1)` | 11 | 13 | 1452 | 2704 | no |
| `(2,3,2)` | 11 | 15 | 1452 | 3600 | no |
| `(2,3,3)` | 11 | 17 | 1452 | 4624 | no |
| `(3,1,1)` | 6 | 8 | 432 | 1024 | no |
| `(3,1,2)` | 6 | 10 | 432 | 1600 | no |
| `(3,1,3)` | 6 | 12 | 432 | 2304 | no |
| `(3,2,1)` | 9 | 11 | 972 | 1936 | no |
| `(3,2,2)` | 9 | 13 | 972 | 2704 | no |
| `(3,2,3)` | 9 | 15 | 972 | 3600 | no |
| `(3,3,1)` | 12 | 14 | 1728 | 3136 | no |
| `(3,3,2)` | 12 | 16 | 1728 | 4096 | no |
| `(3,3,3)` | 12 | 18 | 1728 | 5184 | no |

The largest ratio `t(4,0,0)/t(2,2,2)` in the table is `12/14`, attained at
`(3,3,1)`. The diamond cut requires the stricter
`t(4,0,0)/t(2,2,2) > 2/sqrt(3)`. Because `(12/14)^2 = 144/196 < 4/3`, every
row fails the cut. This is why `N_rev = 0`.

The unit row `(1,1,1)` reproduces `t = |·|_1` at both probes, as required of
the `ℓ¹` comparator.

## Why The Family Cannot Reverse

On this host an origin-to-axis geodesic uses one seed-exit hop and then three
equal-support hops along a coordinate axis. An origin-to-body geodesic uses
one seed-exit hop, two unequal-support hops that raise the support cardinality
from 1 to 3, and three equal-support hops that finish the remaining
coordinate steps. Those hop-type counts already force

```text
t(4,0,0)  =  c_seed + 3 c_eq,
t(2,2,2)  =  c_seed + 3 c_eq + 2 c_uneq
```

for every positive triple, and the Dijkstra tables confirm both identities.
Hence `t(4,0,0) < t(2,2,2)` whenever `c_uneq > 0`, so the axis/body ratio
cannot reach `2/sqrt(3)`. Enlarging the ball cannot help these two probes:
both already lie in `B_6(0)`, and every cheaper path would still have to
realize those support changes.

Some non-reversing members do have `Var(t) < Var(t_1)`. That is irrelevant to
Theorem 2, which counts beating only inside the reversal set. The investment
triple is one such non-reversing tighter-variance table; it is not a matching
member.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| host `B_6(0)` of 377 sites | closed by enumeration |
| 27 named triples, 27 Dijkstras | closed |
| diamond cut at `(4,0,0)` vs `(2,2,2)` | closed; `N_rev = 0` |
| variance beating inside the reversal set | closed; `N_beat = 0` |
| lex-first reversing or beating triple | does not exist |
| write a triple into Admissibility | not executed |
| attach the `ℓ¹` comparator as law | not executed |
| uniqueness of a named hop-cost | not claimed |
| scan of 6561 occupancy 8-tuples | not executed |
| matching member outside this family | open |

## Imports And Non-Claims

No observation, fit, continuum limit, or Newtonian comparator is imported.
The only lattice input is the current cubic nearest-neighbor structure. The
only axiom input is the current wording that Admissibility is one fixed
covariant nearest-neighbor rule and does not already name these costs.

The theorem does not say that no finite named hop-cost can reverse the
diamond. It says that none of these 27 do, and therefore none of them both
reverse and beat `ℓ¹` variance.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the named residual: which of the 27 reverse the diamond and beat `ℓ¹` variance. |
| V2 | The investment already knew that `(3,3,1)` fails the diamond; the new content is the exhaustive 27-element count `N_rev = 0`, `N_beat = 0`. |
| V3 | Both counts are independently checkable by 27 finite Dijkstras and integer comparison. |
| V4 | The closed hop-type identities explain why the family is structurally unable to reverse, not merely unlucky at one triple. |
| V5 | The census is displayed, not adopted; the matching-member residual is left open outside this family. |

## No-Go Discipline Gate

The negative claim is restricted to the 27 named triples on `B_6(0)`. No
global hop-cost impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unit triple `(1,1,1)` | recover the `ℓ¹` table | exact; does not reverse |
| investment `(3,3,1)` | seed-exit 3, equal 3, unequal 1 | `t(4,0,0)=12`, `t(2,2,2)=14`; does not reverse |
| remaining 25 triples | vary each slot through `{1,2,3}` | all 27 fail the diamond cut |
| 6561 occupancy 8-tuples | assign independent costs to eight older orbits | not executed; forbidden by the residual |
| other named finite rules | change the slot definition | live; outside this census |
| infinite-lattice Dijkstra | allow paths that leave `B_6(0)` | not executed; the host is the ball |

### N2 — wall independence

A differently named finite rule, a different occupancy weight, or a different
finite host is an independent route. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The ball radius, the three slots, the cost range `{1,2,3}`, the diamond
probes, and the variance domain are explicit. No continuum isotropic law is
assumed.

### N4 — source residual matching

The residual asked which of the 27 reverse the diamond and beat `ℓ¹`
variance, and whether a matching member exists in that list. The census
answers both counts and records that no matching member is present.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | one named triple | no exhaustion of every conceivable cost table |
| per site | times at two probes; variance on `B_6(0) \ {0}` | no physical clock at a site |
| per mode | seed, equal, unequal | no other occupancy typing |
| per block | 27 Dijkstras on one ball | no axiom edit |
| lattice wide | checked and not executed | no infinite-lattice theorem |

### N6 — live partial-closure paths

A different finite named rule, a different support weight, or a larger named
family can still supply a matching member. Those paths remain live.

### N7 — hostile steelman

**Steelman:** Because some triples already beat `ℓ¹` variance, the family
almost works and should be adopted.

**Answer:** Variance beating without diamond reversal is not a matching
member. Theorem 3 refuses adoption and refuses uniqueness.

### N8 — cross-cycle echo

The investment already recorded that `(3,3,1)` does not reverse on `B_6(0)`.
The present census does not reopen that member as a law; it only closes the
27-element neighborhood around it.

**Gate disposition:** PASS for the finite counts `N_rev = 0` and
`N_beat = 0` on `B_6(0)`. FAIL / DO NOT SHIP for “no hop-cost can reverse
the diamond,” “the `ℓ¹` table is physical law,” or any Admissibility edit.

## Primary Runner

The primary runner rebuilds `B_6(0)`, runs the 27 Dijkstras, checks the
integer diamond cut, checks that the reversal and beating counts are zero,
checks that `(3,3,1)` and `(1,1,1)` match the displayed times, and checks
that the current axiom memo is unedited. It writes no cache and authors no audit verdict.
