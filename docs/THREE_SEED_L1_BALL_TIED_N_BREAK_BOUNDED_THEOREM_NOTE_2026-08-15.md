---
claim_id: three_seed_l1_ball_tied_n_break_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the union of three radius-2 ℓ¹ balls at 0, (2,0,0), and (0,2,0), whether any unread 4-occupied-NN site has unequal ambiguous n or a non-swapping stabilizer, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_seed_l1_ball_tied_n_break_2026_08_15.py
---

# Three Radius-2 ℓ¹ Seeds Do Not Break Tied-n Swap Symmetry

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the union `U3 = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((0,2,0))` inside
the box `|x|,|y|,|z| ≤ 6`. Occupancy geometry and the occupancy kernel
`n = d/3` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_seed_l1_ball_tied_n_break_2026_08_15.py`](../scripts/three_seed_l1_ball_tied_n_break_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment `#6652` (two-ball stabilizer): on
`U2 = B_2(0) ∪ B_2((2,0,0))`, every unread site with four occupied
nearest neighbors carries a tied pair of ambiguous slots with a common
kernel `n`, and `Stab_{G+}(n)` contains an element swapping those slots,
so no cube-equivariant `{+,−}` labeling can fire. The residual asked
here is whether adjoining a third radius-2 ℓ¹ ball at `(0,2,0)` produces
an unread 4-occupied-NN site whose ambiguous neighbors have unequal `n`,
or a tied pair whose stabilizer contains no slot-swap.

Write `B_2(c) = { p ∈ Z^3 : |p − c|_1 ≤ 2 }` and

```text
U3 = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((0,2,0)).
```

A site is occupied when it lies in `U3`. Unread sites are the points of
the box that are not in `U3`. For any site `w`, the occupancy dipole is
`d_μ(w) = occ(w + e_μ) − occ(w − e_μ)` with `occ ∈ {0,1}` the
indicator of `U3`, and `n(w) = d(w)/3`. A neighbor of an unread site
`v` is ambiguous when it is occupied and `|supp n| ≠ 1`.

`G+` is the 24 proper cube rotations, acting in the 3-vector
representation. For a tied opposite-slot pair sharing one kernel `n`,

```text
Stab_{G+}(n) = { g in G+ : g · n = n }.
```

**Theorem 1.** Inside the box there are exactly `N_4 = 4` unread sites
with four occupied 6-nearest neighbors. None of them has two ambiguous
neighbors with unequal `n`: `N_uneq = 0`. None of them has a tied pair
whose stabilizer contains no slot-swap: `N_noswap = 0`.

**Theorem 2.** Because `N_uneq + N_noswap = 0`, the third seed does not
break the obstruction on this `U3`. Opposite labels are not
equivariance-allowed at any of the four sites: each carries a unique
tied ambiguous pair with equal `n`, and `Stab_{G+}(n)` contains an
element swapping those two slots.

**Theorem 3.** Displayed, not adopted. Do not write three-seed geometry
into Admissibility. Do not attach L1.

This is not leftover-char of nstab and not leftover-char 10 of nstab
(the two-ball stabilizer). The present report enumerates `U3` occupancy
and the kernels `n = d/3`; it does not reuse the two declared two-ball
kernels as input.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite occupancy census of U3 in the radius-6 box computes N_4, N_uneq, and N_noswap exactly and shows the third seed leaves the tied-n swap obstruction intact."
trace_class: frontier_discovery
target_claim_id: three_seed_l1_ball_tied_n_break
target_blocker_text: "whether adjoining B_2((0,2,0)) to the two-ball union presents an unread 4-occupied-NN site with unequal ambiguous n or a non-swapping stabilizer"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for U3, finite G+ of order 24, n = d/3 from occupancy, and the box |x|,|y|,|z|≤6; three-seed geometry is displayed, not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "independent audit of the displayed U3 census; do not adopt three-seed geometry or attach L1"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Objects

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility covariance clause is quoted only as the existing
spatial-covariance contract. It is not edited. In particular this note does
not insert three-seed geometry into that clause.

Declared mathematical scaffolding, not a new axiom and not a new patch
family:

- `B_2(c)` is the closed radius-2 ℓ¹ ball on `Z^3`;
- `U3` is the union of those balls at `0`, `(2,0,0)`, and `(0,2,0)`;
- the search box is `|x|,|y|,|z| ≤ 6`;
- `n = d/3` is the occupancy dipole at a site, scored from membership in
  `U3` only;
- ambiguous means occupied and `|supp n| ≠ 1`;
- a tied pair at unread `v` is a pair of opposite occupied neighbors
  that are both ambiguous and share one kernel `n`;
- `G+` is exactly the 24 determinant-`+1` signed permutations of the
  three coordinate axes (finite `G+` = 24 only);
- a slot-swap in `Stab_{G+}(n)` is an element sending one tied slot
  vector to the opposite slot vector.

Investment `#6652` is used only as the two-ball stabilizer context. It
is not re-proved here and is not given an audit verdict.

## Theorem 1 — census of unread 4-occupied-NN sites

The three balls each have 25 sites. Their pairwise overlaps are 7, 7,
and 3, and the triple overlap has 2 sites, so `|U3| = 60`. Every point
of `U3` lies strictly inside the box.

An exhaustive scan of the `13^3 = 2197` box sites finds exactly four
unread locations whose six-nearest-neighbor occupancy is 4:

```text
v1 = (1, −1, 1)
  occupied: +x, −x, +y, −z
  n(+x) = n(−x) = (0, 1/3, −1/3)     ambiguous, tied
  n(+y) = (0, 0, −1/3)               unique-axis
  n(−z) = (0, 1/3, 0)                unique-axis

v2 = (1, −1, −1)
  occupied: +x, −x, +y, +z
  n(+x) = n(−x) = (0, 1/3, 1/3)      ambiguous, tied
  n(+y) = (0, 0, 1/3)                unique-axis
  n(+z) = (0, 1/3, 0)                unique-axis

v3 = (−1, 1, 1)
  occupied: +x, +y, −y, −z
  n(+y) = n(−y) = (1/3, 0, −1/3)     ambiguous, tied
  n(+x) = (0, 0, −1/3)               unique-axis
  n(−z) = (1/3, 0, 0)                unique-axis

v4 = (−1, 1, −1)
  occupied: +x, +y, −y, +z
  n(+y) = n(−y) = (1/3, 0, 1/3)      ambiguous, tied
  n(+x) = (0, 0, 1/3)                unique-axis
  n(+z) = (1/3, 0, 0)                unique-axis
```

Lex order on `Z^3` is `v4`, `v3`, `v2`, `v1`. Each site has exactly two
ambiguous neighbors, those two neighbors share one kernel, and
`N_uneq = 0`. Each site has exactly one tied pair.

For each of those four kernels, `|Stab_{G+}(n)| = 2`. The non-identity
element swaps the tied slots:

- at `v1`, `n = (0, 1/3, −1/3)` and `s : (x, y, z) ↦ (−x, −z, −y)`
  sends `+x` to `−x`;
- at `v2`, `n = (0, 1/3, 1/3)` and `s : (x, y, z) ↦ (−x, z, y)`
  sends `+x` to `−x`;
- at `v3`, `n = (1/3, 0, −1/3)` and `s : (x, y, z) ↦ (−z, −y, −x)`
  sends `+y` to `−y`;
- at `v4`, `n = (1/3, 0, 1/3)` and `s : (x, y, z) ↦ (z, −y, x)`
  sends `+y` to `−y`.

Thus `N_noswap = 0`.

The third ball does change the two-ball 4-NN list: the U2 sites
`(1, 1, ±1)` are no longer unread 4-occupied-NN locations on `U3`, and
`v3`, `v4` appear from the new seed. The new sites are the y-axis
rotates of the surviving x-axis pair, and they inherit the same
swap-in-stabilizer obstruction.

## Theorem 2 — the third seed does not break the obstruction

`N_uneq + N_noswap = 0`. There is therefore no lex-first breaker to
exhibit. On this `U3` the third seed does not break the obstruction.

Restricting equivariance to `g ∈ Stab_{G+}(n)` still forces
`λ(g · slot, n) = λ(slot, n)`. Because a stabilizer element swaps the
tied slots at every census site, every `G+`-equivariant `{+,−}`
labeling that depends on `n` assigns those two slots the same letter.
Opposite labels are not equivariance-allowed.

A function of `n` alone likewise cannot split a tied pair: the two
ambiguous neighbors share `n` at every census site. Unequal-`n`
labeling is unavailable on this union.

## Theorem 3 — displayed, not adopted

Three-seed geometry and the occupancy kernels scored on `U3` are
reported finite data. Displayed, not adopted. Do not write three-seed
geometry into Admissibility. Do not attach L1. Finite `G+` = 24 only.
Score geometry and `n` only. No new patch family. No axiom edit.

## Mutation Checks

1. Dropping `B_2((0,2,0))` recovers the two-ball 4-NN family
   `{(1, ±1, ±1)}` instead of the mixed `{ (1, −1, ±1), (−1, 1, ±1) }`
   list; the third seed is load-bearing for which four sites appear.
2. Replacing `G+` by a single orientation-reversing signed permutation
   can enlarge a stabilizer, so the swap report is specific to
   determinant `+1`.
3. A site with three or more occupied neighbors that failed `|supp n| ≠ 1`
   equally would be counted in `N_uneq` if any two kernels differed; no
   such unread 4-occupied-NN site occurs in the box.

## What This Does Not Claim

- Three-seed geometry is not added to Admissibility, Lattice, Qubit, or
  Record.
- L1 is not attached. No new patch family is introduced.
- The leftover-char of nstab is not reused as a hypothesis: the kernels
  here are recomputed from `U3` occupancy.
- Continuous `SO(3)`, a larger octahedral group, or any group other than
  the 24 proper cube rotations is outside the theorem.
- Other seed placements, other radii, or a larger box are outside the
  theorem.
- No formation rule, Record lock, or physical occupancy process is
  selected.
- No no-go against non-equivariant rules is claimed.

These are scope boundaries. Accordingly no no-go verdict is authored here.

## Primary Runner

The primary runner builds `U3`, scans the box, computes `n = d/3` at
every occupied neighbor of every unread 4-occupied-NN site, evaluates
`N_4`, `N_uneq`, and `N_noswap`, and checks the displayed-not-adopted /
no-L1 / no-three-seed-in-Admissibility / no axiom-edit boundary. It
writes no runner cache and authors no audit verdict.
