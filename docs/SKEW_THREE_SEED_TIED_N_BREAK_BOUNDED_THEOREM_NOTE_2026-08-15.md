---
claim_id: skew_three_seed_tied_n_break_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the union of three radius-2 ℓ¹ balls at 0, (2,0,0), and (1,2,1), whether any unread 4-occupied-NN site has unequal ambiguous n or a non-swapping stabilizer, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_tied_n_break_2026_08_15.py
---

# Off-Axis Third Seed Breaks Tied-n Swap By Unequal Ambiguous n

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the union `U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` inside
the box `|x|,|y|,|z| ≤ 6`. Occupancy geometry and the occupancy kernel
`n = d/3` only. One off-axis triple only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_tied_n_break_2026_08_15.py`](../scripts/skew_three_seed_tied_n_break_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment `#6653` (axis-aligned L of three radius-2 balls): on
`U3 = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((0,2,0))`, every unread site with
four occupied nearest neighbors still has `N_uneq = N_noswap = 0`. The
residual asked here is whether moving the third center off the
coordinate L, to `(1,2,1)`, produces an unread 4-occupied-NN site whose
ambiguous neighbors have unequal `n`, or a tied pair whose stabilizer
contains no slot-swap.

Write `B_2(c) = { p ∈ Z^3 : |p − c|_1 ≤ 2 }` and

```text
U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1)).
```

A site is occupied when it lies in `U`. Unread sites are the points of
the box that are not in `U`. For any site `w`, the occupancy dipole is
`d_μ(w) = occ(w + e_μ) − occ(w − e_μ)` with `occ ∈ {0,1}` the
indicator of `U`, and `n(w) = d(w)/3`. A neighbor of an unread site
`v` is ambiguous when it is occupied and `|supp n| ≠ 1`.

`G+` is the 24 proper cube rotations, acting in the 3-vector
representation. For a tied opposite-slot pair sharing one kernel `n`,

```text
Stab_{G+}(n) = { g in G+ : g · n = n }.
```

**Theorem 1.** Inside the box there are exactly `N_4 = 7` unread sites
with four occupied 6-nearest neighbors. Four of them have two ambiguous
neighbors with unequal `n`: `N_uneq = 4`. None of them has a tied pair
whose stabilizer contains no slot-swap: `N_noswap = 0`.

**Theorem 2.** Because `N_uneq + N_noswap = 4 > 0`, the off-axis triple
does break the obstruction on this `U`. The lex-first breaker is
`v = (−1, 1, 1)`. At that site the three ambiguous kernels are not all
equal, there is no tied opposite pair, and opposite labels are
equivariance-allowed.

**Theorem 3.** Displayed, not adopted. Do not write the triple into
Admissibility. Do not attach L1. Do not launch a 4th equal-radius ball clone.

This is not leftover-char of 3ball (that center was `(0,2,0)`). The
present report enumerates `U` occupancy and the kernels `n = d/3`; it
does not reuse the axis-aligned three-seed census as input.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite occupancy census of U in the radius-6 box computes N_4, N_uneq, and N_noswap exactly and exhibits a lex-first unread 4-occupied-NN site with unequal ambiguous n."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_tied_n_break
target_blocker_text: "whether moving the third radius-2 center off the coordinate L to (1,2,1) presents an unread 4-occupied-NN site with unequal ambiguous n or a non-swapping stabilizer"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for U, finite G+ of order 24, n = d/3 from occupancy, and the box |x|,|y|,|z|≤6; the off-axis triple is displayed, not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "independent audit of the displayed U census; do not adopt the triple, attach L1, or launch a 4th equal-radius ball clone"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Objects

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility covariance clause is quoted only as the existing
spatial-covariance contract. It is not edited. In particular this note does
not insert the off-axis triple into that clause.

Declared mathematical scaffolding, not a new axiom and not a new patch
family:

- `B_2(c)` is the closed radius-2 ℓ¹ ball on `Z^3`;
- `U` is the union of those balls at `0`, `(2,0,0)`, and `(1,2,1)`;
- the search box is `|x|,|y|,|z| ≤ 6`;
- `n = d/3` is the occupancy dipole at a site, scored from membership in
  `U` only;
- ambiguous means occupied and `|supp n| ≠ 1`;
- a tied pair at unread `v` is a pair of opposite occupied neighbors
  that are both ambiguous and share one kernel `n`;
- `G+` is exactly the 24 determinant-`+1` signed permutations of the
  three coordinate axes (finite `G+` = 24 only);
- a slot-swap in `Stab_{G+}(n)` is an element sending one tied slot
  vector to the opposite slot vector.

Investment `#6653` is used only as the axis-aligned three-seed context.
It is not re-proved here and is not given an audit verdict. One off-axis
triple only.

## Theorem 1 — census of unread 4-occupied-NN sites

The three balls each have 25 sites. Their pairwise overlaps are 7, 4,
and 4, and the triple overlap has 2 sites, so `|U| = 62`. Every point
of `U` lies strictly inside the box.

An exhaustive scan of the `13^3 = 2197` box sites finds exactly seven
unread locations whose six-nearest-neighbor occupancy is 4. In lex
order on `Z^3`:

```text
v = (−1, 1, 1)                         N_uneq witness
  occupied: +x, +y, −y, −z
  n(+x) = (1/3, 0, −1/3)               ambiguous
  n(+y) = (1/3, 0, 0)                  unique-axis
  n(−y) = (1/3, 0, −1/3)               ambiguous
  n(−z) = (1/3, −1/3, 0)               ambiguous
  no tied opposite pair

v = (0, 1, 2)                          N_uneq witness
  occupied: +x, +y, −y, −z
  n(+x) = (0, 1/3, −1/3)               ambiguous
  n(+y) = (1/3, 0, −1/3)               ambiguous
  n(−y) = (0, 0, −1/3)                 unique-axis
  n(−z) = (1/3, 0, −1/3)               ambiguous
  no tied opposite pair

v = (1, −1, −1)
  occupied: +x, −x, +y, +z
  n(+x) = n(−x) = (0, 1/3, 1/3)        ambiguous, tied
  n(+y) = (0, 0, 1/3)                  unique-axis
  n(+z) = (0, 1/3, 0)                  unique-axis
  |Stab_{G+}(n)| = 2 with slot-swap
  s : (x, y, z) ↦ (−x, z, y) sends +x to −x

v = (1, −1, 1)
  occupied: +x, −x, +y, −z
  n(+x) = n(−x) = n(+y) = (0, 1/3, −1/3)
                                       ambiguous; +x/−x tied
  n(−z) = (0, 1/3, 0)                  unique-axis
  |Stab_{G+}(n)| = 2 with slot-swap
  s : (x, y, z) ↦ (−x, −z, −y) sends +x to −x

v = (1, 0, 2)
  occupied: +x, −x, +y, −z
  n(+x) = n(−x) = (0, 0, −1/3)         unique-axis
  n(+y) = n(−z) = (0, 1/3, −1/3)       ambiguous, equal, not opposite
  no tied opposite pair

v = (2, 1, 2)                          N_uneq witness
  occupied: −x, +y, −y, −z
  n(−x) = (0, 1/3, −1/3)               ambiguous
  n(+y) = (−1/3, 0, −1/3)              ambiguous
  n(−y) = (0, 0, −1/3)                 unique-axis
  n(−z) = (−1/3, 0, −1/3)              ambiguous
  no tied opposite pair

v = (3, 1, 1)                          N_uneq witness
  occupied: −x, +y, −y, −z
  n(−x) = (−1/3, 0, −1/3)              ambiguous
  n(+y) = (−1/3, 0, 0)                 unique-axis
  n(−y) = (−1/3, 0, −1/3)              ambiguous
  n(−z) = (−1/3, −1/3, 0)              ambiguous
  no tied opposite pair
```

Thus `N_4 = 7`, `N_uneq = 4`, and `N_noswap = 0`. The two sites that
still carry a tied opposite pair inherit a slot-swap in `Stab_{G+}(n)`.
The four unequal-`n` sites have no tied opposite pair at all.

Moving the third center off the coordinate L changes the axis-aligned
4-NN list: the U3 sites `(−1, 1, −1)` disappear, and `(0, 1, 2)`,
`(1, 0, 2)`, `(2, 1, 2)`, and `(3, 1, 1)` appear. The new sites are not
a rotate of the axis-aligned L.

## Theorem 2 — lex-first breaker and equivariance-allowed opposite labels

`N_uneq + N_noswap = 4 > 0`. The lex-first such unread site is
`v = (−1, 1, 1)`.

At that site the occupied star is `+x, +y, −y, −z`. The unique-axis
neighbor is `+y` with `n = (1/3, 0, 0)`. The three ambiguous kernels
are

```text
n(+x) = n(−y) = (1/3, 0, −1/3),
n(−z) = (1/3, −1/3, 0).
```

Those kernels are not all equal, so `N_uneq` counts the site. There is
no opposite occupied pair that is both ambiguous and shares one kernel,
so there is no `Stab_{G+}(n)` slot-swap to apply.

A `{+,−}` labeling that depends on `n` may therefore assign different
letters to `−z` and to the `{+x, −y}` pair. The only opposite occupied
pair is `+y` and `−y`, and those two neighbors also have unequal `n`.
Restricting equivariance to `g ∈ Stab_{G+}(n)` does not force those
opposite slots to share a letter. Opposite labels are
equivariance-allowed.

This off-axis triple therefore breaks the obstruction that survived on
the axis-aligned L: unequal ambiguous `n` is realized, and at the
lex-first witness opposite labels are equivariance-allowed.

## Theorem 3 — displayed, not adopted

The off-axis triple and the occupancy kernels scored on `U` are
reported finite data. Displayed, not adopted. Do not write the triple
into Admissibility. Do not attach L1. Do not launch a 4th equal-radius
ball clone. Finite `G+` = 24 only. Score geometry and `n` only. No new
patch family. No axiom edit. One off-axis triple only.

## Mutation Checks

1. Replacing `B_2((1,2,1))` by `B_2((0,2,0))` recovers the axis-aligned
   census `N_4 = 4`, `N_uneq = 0`, `N_noswap = 0`; the off-axis center
   is load-bearing for the unequal-`n` sites.
2. Dropping the third ball recovers the two-ball 4-NN family
   `{(1, ±1, ±1)}` and loses every `N_uneq` witness.
3. A site with three or more occupied neighbors that failed
   `|supp n| ≠ 1` equally is counted in `N_uneq` exactly when any two of
   those kernels differ; four such unread 4-occupied-NN sites occur in
   the box.

## What This Does Not Claim

- The off-axis triple is not added to Admissibility, Lattice, Qubit, or
  Record.
- L1 is not attached. No new patch family is introduced. A fourth
  equal-radius ball is not launched.
- The leftover-char of 3ball is not reused as a hypothesis: the kernels
  here are recomputed from `U` occupancy at center `(1,2,1)`.
- Continuous `SO(3)`, a larger octahedral group, or any group other than
  the 24 proper cube rotations is outside the theorem.
- Other seed placements, other radii, or a larger box are outside the
  theorem.
- No formation rule, Record lock, or physical occupancy process is
  selected.
- No no-go against non-equivariant rules is claimed. No firing count is
  claimed: the report is the unread 4-occupied-NN census and the
  equivariance status of opposite labels at the lex-first breaker.

These are scope boundaries. Accordingly no no-go verdict is authored here.

## Primary Runner

The primary runner builds `U`, scans the box, computes `n = d/3` at
every occupied neighbor of every unread 4-occupied-NN site, evaluates
`N_4`, `N_uneq`, and `N_noswap`, reports the lex-first breaker, and
checks the displayed-not-adopted / no-L1 / no-triple-in-Admissibility /
no-fourth-ball / no axiom-edit boundary. It writes no runner cache and
authors no audit verdict.
