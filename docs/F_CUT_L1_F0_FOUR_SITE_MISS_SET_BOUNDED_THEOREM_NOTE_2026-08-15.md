---
claim_id: f_cut_l1_f0_four_site_miss_set_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 4-site miss set of f_L1 is not equal to the 4-site miss set of F_cut (1,1,1,1,0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_l1_f0_four_site_miss_set_2026_08_15.py
---

# Four-Site Miss Sets of `f_L1` and `F_cut` `(1,1,1,1,0)` Are Not Equal

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock census of all four-site seeds on the
twelve-vertex two-cube with off-patch occupancy `0`, comparing the miss
set of `f_L1` with the miss set of the `F_cut` map `(1,1,1,1,0)`. No
seed is listed. No map is adopted. No Admissibility selector is written.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_l1_f0_four_site_miss_set_2026_08_15.py`](../scripts/f_cut_l1_f0_four_site_miss_set_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The two-cube is the twelve-site block `{0,1,2} × {0,1} × {0,1}`. The
off-patch occupancy is the explicit default `0`; a blank-block is a different rule.
There are exactly `C(12,4) = 495` unordered four-site seeds.

The map `f_L1` fires at a site if and only if some cubic axis of its
nearest-neighbor occupancy is unbalanced: `n_unbalanced ≠ 0`, equivalently
`n_μ ≠ 0` on at least one axis. In the five remaining `F_cut` bits
`(wt1, opp2, adj2, vertex3, mixed3)` this is the tuple `(1,0,1,1,1)`.
This is not Hamming parity of the six neighbor bits.

The compared `F_cut` map is `f0 = (1,1,1,1,0)`: it fires on every remaining
orbit except `mixed3`. The bit `mixed3 = 0` is the only difference between
`f0` and the all-ones remaining map `f1 = (1,1,1,1,1)`. Neither map is
adopted.

Starting from a seed as the locked set and iterating occupancy-to-lock with
off-patch occupancy `0`, `f_L1` fills from `489` seeds, so `|M_L1| = 6`.
That reconfirms the `#6460` count; the object here is not that count.
Independently, `f0` fills from `459` seeds, so `|M_f0| = 36`. The
intersection has `|M_L1 ∩ M_f0| = 4`. Therefore `M_L1 ≠ M_f0`. The
equality bit is `0`.

These cardinals and the equality bit are displayed, not adopted. Do not
list the seeds. Do not adopt a map. They are not written into
Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhaustive four-site census determines |M_f0|=36, |M_L1 ∩ M_f0|=4, and equality bit 0."
trace_class: frontier_discovery
target_claim_id: f_cut_l1_f0_four_site_miss_set
target_blocker_text: "is L1’s 4-site miss set a theorem of mixed3=0, or a different set than f0’s?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the two-cube with off-patch occupancy 0; no seed or map is adopted"
hypothetical_axiom_status: "none; f_L1, f0, and the miss-set cardinals are displayed occupancy data, not axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the two miss-set cardinals and the equality bit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences quoted below supply cubic nearest-neighbor wording and the lock
  rule. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the two-cube, off-patch occupancy
  `0`, the unbalanced-axis predicate `f_L1`, and the remaining-bit map
  `f0 = (1,1,1,1,0)` are supplied finite data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a seed or of either map by
  Admissibility or Record remains a separate, open obligation.

## Exact Objects

Sites are points of `Z^3`. The two-cube is

```text
V = {0,1,2} × {0,1} × {0,1},    |V| = 12.
```

On-patch occupancy of a site is the lock bit. Off-patch occupancy is `0`.
For a locked set `L ⊂ V` and a site `x ∈ V`, each cubic axis `μ` contributes
one pair `(c_{μ+}, c_{μ-})` of neighbor occupancies. Write

```text
n_unbalanced = |{μ : c_{μ+} ≠ c_{μ-}}|,
n_both       = |{μ : c_{μ+} = c_{μ-} = 1}|,
n_empty      = |{μ : c_{μ+} = c_{μ-} = 0}|.
```

The pair `(n_unbalanced, n_both, n_empty)` is the axis type. Empty
`(0,0,3)` and full `(0,3,0)` never fire in `F_cut`. The five remaining
types, with complement identification `f(c) = f(1-c)`, are

```text
wt1=(1,0,2), opp2=(0,1,2), adj2=(2,0,1), vertex3=(3,0,0), mixed3=(1,1,1).
```

Then `f_L1(x; L) = 1` if and only if `n_unbalanced ≠ 0`, which is the
remaining tuple `(1,0,1,1,1)`. Hamming parity of the six neighbor bits is
a different map: `opp2` has Hamming weight `2` and `n_unbalanced = 0`, so
`f_L1` refuses it; `mixed3` has Hamming weight `3` and `n_unbalanced = 1`,
so Hamming fires it while `f0` refuses it.

A four-site seed is an unordered 4-subset of `V`. Occupancy-to-lock starts
from `L_0 = S` and at each tick adds every unlocked two-cube site at which
the displayed map fires. The seed fills when some `L_t = V`. The miss sets
are

```text
M_L1 = {S ⊂ V : |S| = 4 and S does not fill under f_L1},
M_f0 = {S ⊂ V : |S| = 4 and S does not fill under f0}.
```

The claimed object is the pair of cardinals `|M_f0|` and `|M_L1 ∩ M_f0|`
together with the equality bit of `M_L1` against `M_f0`. It is not `N_orb`.
It is not a 6-row leftover table. Not leftover-character of
`#6460`, which named only the counts `cov4(L1) = 489` and unique-max
`cov4(f1) = 495`.

## Exact Target And Proof Obligations

The exact target is `|M_f0|`, the intersection cardinal, and whether the
two miss sets are equal.

1. enumerate all `495` four-site seeds and reconfirm `|M_L1| = 6`;
2. compute `|M_f0|` by independent occupancy-to-lock runs under `f0`;
3. compute `|M_L1 ∩ M_f0|` and the equality bit, display that bit, and
   refuse to list seeds or adopt a map.

All three obligations are closed below and in the runner. There is no
missing lemma for this bounded census. Listing the seeds, writing a
selector into Admissibility, or promoting the count `#6460` to a leftover
table would be a different claim.

## Theorem 1 — `|M_f0| = 36`

There are exactly `495` four-site seeds. Independent occupancy-to-lock
runs with off-patch occupancy `0` give `|M_L1| = 6`, reconfirming
`cov4(L1) = 489`. The same seed list under `f0` gives `cov4(f0) = 459`.
Therefore `|M_f0| = 36`.

The all-ones remaining map `f1` fills every four-site seed, so
`cov4(f1) = 495`. The `36` misses of `f0` are therefore exactly the
four-site seeds that require the `mixed3` bit. That supporting split is
not a seed list.

## Theorem 2 — `|M_L1 ∩ M_f0| = 4` and `M_L1 ≠ M_f0`

The two independently computed miss sets satisfy

```text
|M_L1 ∩ M_f0| = 4.
```

Since `|M_L1| = 6` and `|M_f0| = 36`, the intersection being strictly
smaller than both sides implies `M_L1 ≠ M_f0`. Equivalently, two of the
six `f_L1` misses fill under `f0`, and thirty-two of the thirty-six `f0`
misses fill under `f_L1`. The 4-site miss set of `f_L1` is therefore not
a theorem of `mixed3 = 0`.

## Theorem 3 — display the equality bit

The equality bit of the two miss sets is `0`. Displayed, not adopted.
Do not list the seeds. Do not adopt a map. Do not adopt `f_L1` or `f0`.
Do not write either map, either miss set, or the equality bit into
Admissibility.

## Physical-Interpretation Boundary

The proved output is the displayed inequality of two finite miss sets on a
supplied two-cube. This note neither assigns those seeds a physical label
nor changes the Lattice, Qubit, Admissibility, or Record sentences.
`f_L1` and `f0` are displayed occupancy data, not axiom content, and no
additional axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `f_L1` is not Hamming parity of the six neighbor bits;
2. `f0` is not Hamming parity: `mixed3` has odd Hamming weight and is
   refused by `f0`;
3. the claimed object is not `N_orb` and not a 6-row leftover table of
   `M_L1`.

## What This Does Not Claim

- Neither `f_L1` nor `f0` is selected by Admissibility or Record.
- No four-site seed is a preferred physical initial condition.
- Coverage on other patches, other occupancy defaults, or other maps in
  `F_cut` is not computed here except the supporting `f1` census that
  fills all `495` seeds.
- The common halt patterns of either miss set are not promoted to a
  dynamics law.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

> A readout value is determined by record content alone.

> A site with no record cannot be read.

> does not supply the formation site, probability, or rate

Their dependency role is limited to cubic nearest-neighbor vocabulary and
the lock rule. This theorem separately supplies the two-cube, the
off-patch default `0`, the unbalanced-axis predicate, and the remaining-bit
tuple `(1,1,1,1,0)`.

## Runner Contract

The companion runner re-enumerates all `495` four-site seeds, recomputes
`M_L1` and `M_f0` by independent occupancy-to-lock runs, and reports
`|M_f0|`, `|M_L1 ∩ M_f0|`, and the equality bit. It does not print the
seeds. It checks the three mutations, quotes the live axiom sentences, and
records the import boundary. Declared review inputs are this note and the
axiom memo only.
