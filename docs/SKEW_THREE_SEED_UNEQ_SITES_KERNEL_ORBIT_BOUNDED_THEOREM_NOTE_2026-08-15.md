---
claim_id: skew_three_seed_uneq_sites_kernel_orbit_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union, whether the distinct ambiguous occupancy kernels at each of the four unequal-n unread 4-NN sites lie in one G+ orbit is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_uneq_sites_kernel_orbit_2026_08_15.py
---

# Distinct Ambiguous Kernels At The Four Unequal-n Sites Lie In One G+ Orbit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the union `U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` inside
the box `|x|,|y|,|z| ≤ 6`. Occupancy geometry and the occupancy kernel
`n = d/3` only. The four `#6654` unequal-n unread 4-occupied-NN sites
only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_uneq_sites_kernel_orbit_2026_08_15.py`](../scripts/skew_three_seed_uneq_sites_kernel_orbit_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Investment `#6654` (off-axis three radius-2 balls): on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` there are four unread
4-occupied-NN sites whose ambiguous neighbors have unequal `n`.
Investment `#6657` scored only the lex-first of those sites and found
that its two distinct `n` lie in one `G+` orbit while the firing
`f(n)` assigned them opposite letters, so `N_commute = 1/24`. The
residual here is not leftover-char of skeweq (one site). It is whether,
at *each* of the four unread 4-NN sites, the distinct ambiguous `n`
are `G+`-equivalent. If some site had kernels in different orbits, an
equivariant `10 → f(n)` could assign different letters and might fire.

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
representation. Two kernels are `G+`-equivalent when some `g ∈ G+`
sends one to the other.

**Theorem 1.** The four unequal-n unread 4-NN sites, in lex order, each
have exactly two distinct ambiguous kernels, and those two kernels are
`G+`-equivalent. Thus `N_same_orb = 4` and `N_split = 0`.

**Theorem 2.** Because `N_split = 0`, every unequal-n site still has
orbit-tied kernels, so any `G+`-equivariant `f(n)` is constant on
those kernels.

**Theorem 3.** Displayed, not adopted. Do not write orbits into
Admissibility. Do not attach L1. No 4th ball.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite occupancy census of U in the radius-6 box recomputes the four unequal-n unread 4-NN sites and scores G+ equivalence of their distinct ambiguous n exactly."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_uneq_sites_kernel_orbit
target_blocker_text: "at each of the four N_uneq unread 4-NN sites, whether the distinct ambiguous n are G+-equivalent"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for U, finite G+ of order 24, n = d/3 from occupancy, and the box |x|,|y|,|z|≤6; orbits are displayed, not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "independent audit of the four-site orbit census; do not write orbits into Admissibility, attach L1, or launch a 4th ball"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises And Declared Objects

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility covariance clause is quoted only as the existing
spatial-covariance contract. It is not edited. In particular this note does
not insert orbits, an `f(n)` table, or the off-axis triple into that clause.

Declared mathematical scaffolding, not a new axiom and not a new patch
family:

- `B_2(c)` is the closed radius-2 ℓ¹ ball on `Z^3`;
- `U` is the union of those balls at `0`, `(2,0,0)`, and `(1,2,1)`;
- the search box is `|x|,|y|,|z| ≤ 6`;
- `n = d/3` is the occupancy dipole at a site, scored from membership in
  `U` only;
- ambiguous means occupied and `|supp n| ≠ 1`;
- `G+` is exactly the 24 determinant-`+1` signed permutations of the
  three coordinate axes (finite `G+` = 24 only);
- two kernels are equivalent when some `g ∈ G+` sends one to the other.

Investment `#6654` is used only as the four-site residual that asked
the present orbit question. Investment `#6657` is used only as the
one-site commutation context. Neither is re-proved here and neither
is given an audit verdict. One off-axis triple only.

## Theorem 1 — four-site orbit census

The three balls each have 25 sites. Their pairwise overlaps are 7, 4,
and 4, and the triple overlap has 2 sites, so `|U| = 62`. Every point
of `U` lies strictly inside the box.

An exhaustive scan of the `13^3 = 2197` box sites recovers exactly
four unread locations with four occupied 6-nearest neighbors and
unequal ambiguous `n`. In lex order on `Z^3`, the distinct ambiguous
kernels and one connecting rotation are:

```text
v = (−1, 1, 1)
  distinct n: (1/3, 0, −1/3), (1/3, −1/3, 0)
  G+-equivalent: yes
  g : (x, y, z) ↦ (x, z, −y)

v = (0, 1, 2)
  distinct n: (0, 1/3, −1/3), (1/3, 0, −1/3)
  G+-equivalent: yes
  g : (x, y, z) ↦ (y, −x, z)

v = (2, 1, 2)
  distinct n: (0, 1/3, −1/3), (−1/3, 0, −1/3)
  G+-equivalent: yes
  g : (x, y, z) ↦ (−y, x, z)

v = (3, 1, 1)
  distinct n: (−1/3, 0, −1/3), (−1/3, −1/3, 0)
  G+-equivalent: yes
  g : (x, y, z) ↦ (x, z, −y)
```

Each displayed `g` is a determinant-`+1` signed permutation, hence an
element of `G+`. Each two-support kernel with components in
`{−1/3, 0, 1/3}` lies in one `G+` orbit of size 12 (stabilizer order
2). The four pairs above are therefore pairs inside that single orbit.

Thus `N_same_orb = 4` and `N_split = 0`. There is no lex-first split
site.

Scoring all four `#6654` sites. This is not leftover-char of skeweq
(one site): `#6657` reported the orbit relation only at
`v = (−1, 1, 1)`.

## Theorem 2 — equivariant `f(n)` is constant on those kernels

Because `N_split = 0`, every unequal-n site still has orbit-tied
kernels. A function of `n` that commutes with `G+` must take the same
value on a kernel and on every `G+` image of that kernel. Therefore
any `G+`-equivariant `f(n)` is constant on those kernels.

In particular the residual that an equivariant `10 → f(n)` might
assign different letters at some unread 4-NN site, and might fire for
that reason, does not occur on this `U`. Unequal `n` still permits a
*non*-equivariant table to assign opposite letters, as `#6657`
displayed at the lex-first site. Equivariance forbids that split.

If `N_split > 0` the lex-first such site would be reported. That
branch is empty here.

## Theorem 3 — displayed, not adopted

The four-site orbit census is reported finite data. Displayed, not
adopted. Do not write orbits into Admissibility. Do not attach L1.
No 4th ball. Do not write an `f(n)` table into Admissibility. Finite
`G+` = 24 only. Score geometry and `n` only. No new patch family. No
axiom edit. One off-axis triple only.

## Mutation Checks

1. Including unique-axis occupied neighbors (`|supp n| = 1`) alongside
   the ambiguous kernels mixes the 1-support orbit with the 2-support
   orbit and would falsely report `N_split > 0` at every listed site.
   The filter `|supp n| ≠ 1` is load-bearing.
2. Replacing `G+` by `{id}` would report `N_split = 4`, because the
   two distinct kernels at each site are unequal as vectors.
3. Restricting the census to the single site `v = (−1, 1, 1)` recovers
   the skeweq one-site orbit relation and hides the other three
   unequal-n sites.

## What This Does Not Claim

- Orbits, the off-axis triple, and any `f(n)` table are not added to
  Admissibility, Lattice, Qubit, or Record.
- L1 is not attached. No new patch family is introduced. A fourth
  equal-radius ball is not launched.
- The leftover-char of skeweq is not reused as a hypothesis: the
  kernels here are recomputed from `U` occupancy at all four sites.
- Continuous `SO(3)`, a larger octahedral group, or any group other
  than the 24 proper cube rotations is outside the theorem.
- Other seed placements, other radii, or a larger box are outside the
  theorem.
- No formation rule, Record lock, or physical occupancy process is
  selected.
- No firing count is claimed. No no-go against non-equivariant rules
  is claimed. The report is the four-site `G+` orbit census and the
  constancy of any equivariant `f(n)` on those kernels.

These are scope boundaries. Accordingly no no-go verdict is authored here.

## Primary Runner

The primary runner builds `U`, scans the box, recomputes the four
unequal-n unread 4-occupied-NN sites, scores `G+` equivalence of the
distinct ambiguous `n`, evaluates `N_same_orb` and `N_split`, reports
a connecting rotation at each site, and checks the displayed-not-adopted
/ no-L1 / no-orbits-in-Admissibility / no-fourth-ball / no axiom-edit
boundary. It writes no runner cache and authors no audit verdict.
