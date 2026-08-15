---
claim_id: two_axis_unbalanced_formation_member_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "f_two is a cube-covariant formation predicate inequivalent to L1's n≠0 on the 64 cells and on the two-cube first wave. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_unbalanced_formation_member_2026_08_15.py
---

# Two-Axis Unbalanced Formation Member

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one cube-covariant boolean formation predicate on occupancy
6-tuples, compared with L1's `n ≠ 0` rule on the same 64 cells and on the
displayed two-cube first wave. The member is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_unbalanced_formation_member_2026_08_15.py`](../scripts/two_axis_unbalanced_formation_member_2026_08_15.py)

## Result up front

Let `C = {0,1}^6` be occupancy on the six directed nearest-neighbor slots
`(+x,-x,+y,-y,+z,-z)`. For `c ∈ C` write

```text
u(c) = |{ μ : c_{+μ} ≠ c_{-μ} }| ∈ {0,1,2,3}.
```

L1's displayed predicate on this test object is `f_L1(c) = 1` iff `u(c) ≥ 1`,
equivalently `n ≠ 0` for the linear imbalance `n_μ = c_{+μ} − c_{-μ}`. The
two-axis member is

```text
f_two(c) = 1  iff  u(c) ≥ 2.
```

The 24 proper cube rotations permute the six slots and therefore permute the
three axes. They leave `u` invariant, so `f_two` is cube-covariant. It is not
linear in `c` and it is not the predicate `n ≠ 0`. The two maps disagree on
the 24 cells with exactly one unbalanced axis.

On the displayed twelve-vertex two-cube of construction `#6320`, with seed
lock at `(0,0,0)` and off-patch occupancy `o = 0` (L1's displayed vacuum
default, not adopted here), L1's first wave is the three axis sites
`(1,0,0)`, `(0,1,0)`, `(0,0,1)`, each with `u = 1`. The first wave of
`f_two` is empty. The members are therefore inequivalent as occupancy-to-lock
steps on the same patch type.

The Admissibility formation slot therefore has more than one displayed
cube-covariant point. This note does not adopt `f_two`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Cube covariance of f_two, the exact 24-cell disagreement with f_L1, and the empty versus three-site first-wave split on the displayed two-cube are finite exact identities; no physical formation rule is selected."
trace_class: negative_route_pruning
target_claim_id: unique_displayed_l1_formation_member
target_blocker_text: "L1's n≠0 occupancy-to-lock step is the only displayed cube-covariant formation member on the 64 occupancy cells"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "further structure beyond cube covariance is required before any displayed occupancy-to-lock predicate can be adopted"
conditional_surface_status: "exact on the 64 occupancy 6-tuples and the displayed twelve-vertex two-cube; no physical law, rate, or site selector"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current Lattice and Admissibility wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Admissibility names one fixed covariant rule and leaves form open: read with
Record, the distribution is conditional on formation at that site; it does not
supply the formation site, probability, or rate.

Record states:

Records form.

When present, a record locks exactly one admissible local possibility.

Those sentences identify the covariance group and the open formation slot.
They do not name a boolean formation predicate on occupancy 6-tuples. The
alphabet `{0,1}` on the six slots is a declared finite test object, not a
replacement of the one-site possibility domain `M_2(C)`. The two-cube, the
seed lock, and the off-patch default `o = 0` are displayed construction data
from `#6320`, not axiom text.

## Exact objects

Write slots in the order `(+x,-x,+y,-y,+z,-z)`. A cell is a 6-tuple
`c ∈ C = {0,1}^6`. The proper cube rotation group `G` is the set of
`3×3` signed permutation matrices of determinant `+1`. Each `R ∈ G` sends
slot `v` to `R v` and acts on cells by

```text
(R·c)_{R v} = c_v.
```

The three axis pairs are `(+x,-x)`, `(+y,-y)`, `(+z,-z)`. The imbalance
vector and its support count are

```text
n_μ(c) = c_{+μ} − c_{-μ},
u(c)   = |{ μ : n_μ(c) ≠ 0 }| = |{ μ : c_{+μ} ≠ c_{-μ} }|.
```

Then `u(c) ∈ {0,1,2,3}` and `n(c) = 0` if and only if `u(c) = 0`.

```text
f_L1(c)  = 1  iff  u(c) ≥ 1,
f_two(c) = 1  iff  u(c) ≥ 2.
```

The displayed two-cube of `#6320` has vertices

```text
A = {0,1}^3,
B = {1,2} × {0,1}^2,
P = A ∪ B
```

(`|P| = 12`). The seed lock is `(0,0,0)`. Occupancy of a locked site is `1`.
Occupancy of an unlocked on-patch site is `0`. Occupancy of an off-patch
site is the displayed default `o = 0`. The occupancy 6-tuple at an on-patch
site is the six neighbor occupancies. The first wave of a predicate `f` is
the set of unlocked sites in `P` at which `f` equals `1` after the seed.

Neither `f_L1` nor `f_two` is adopted as a physical law.

## Theorem 1 — `f_two` is cube-covariant

`G` has 24 elements: six images for the first axis, four remaining images
for the second, and the third axis then fixed by orientation. Inversion is
absent. The induced action on the six slots is 24 distinct permutations.

A proper cube rotation permutes the three axis pairs and may swap the two
slots of a pair. It cannot change whether a pair is balanced. Therefore
`u(R·c) = u(c)` for every `R ∈ G` and every `c ∈ C`, and

```text
f_two(R·c) = f_two(c).
```

The same invariance holds for `f_L1`. Direct evaluation on all 64 cells and
all 24 slot permutations confirms both identities.

## Theorem 2 — the predicates disagree on a nonempty set

The maps `f_L1` and `f_two` agree on cells with `u = 0` (both vanish) and on
cells with `u ≥ 2` (both equal `1`). They disagree exactly on the cells with
`u = 1`: there `f_L1 = 1` and `f_two = 0`.

There are three choices of the unbalanced axis, two occupancy patterns on
that axis, and two balanced patterns on each of the other two axes, hence

```text
3 × 2 × 2 × 2 = 24
```

such cells. Direct listing of all 64 cells confirms that `f_L1` and `f_two`
disagree on exactly 24 cells. In particular the disagreement set is nonempty
(cardinality `24 ≥ 1`).

The predicate `f_two` is not `n ≠ 0`, because those 24 cells have `n ≠ 0`
and `f_two = 0`. It is not linear in `c`: over `GF(2)`, the two one-axis
cells with support on distinct axes sum to a two-axis cell, so

```text
f_two(c) = 0,   f_two(c') = 0,   f_two(c + c') = 1,
```

which forbids additivity. The zero set of `f_two` is therefore not the kernel
of a linear form on `C`.

## Theorem 3 — inequivalent first waves on the displayed two-cube

After the seed lock at `(0,0,0)`, the only on-patch sites whose neighbor
6-tuple has `u ≥ 1` are the three axis neighbors of the seed,

```text
(1,0,0), (0,1,0), (0,0,1).
```

Each of those sites has the seed in one directed slot and `0` in the other
five slots, so `u = 1` there. L1 therefore forms exactly those three sites
as its first wave.

Because those sites have `u = 1`, `f_two` vanishes on them. No other
unlocked site in `P` has `u ≥ 2`. The first wave of `f_two` is empty.

The two predicates therefore induce distinct occupancy-to-lock steps on the
same twelve-vertex patch. The two-axis member is not an occupancy-step clone
of L1: the patch type is unchanged and the formation predicate is different.

The off-patch default `o = 0` is L1's displayed vacuum assignment, used here
only to hold the two-cube data fixed. It is not adopted.

## Obligation graph

| obligation | exact disposition |
|---|---|
| `|C| = 64` | enumerated binary 6-tuples |
| `|G| = 24`, orientation-preserving | signed permutations of determinant `+1` |
| `u` invariant under `G` | axis pairs are permuted |
| `f_two` cube-covariant | Theorem 1 |
| `f_two` not `n ≠ 0` | 24 cells with `u = 1` |
| `f_two` not linear in `c` | `GF(2)` additivity fails |
| disagreement set | exactly the 24 cells with `u = 1` |
| disagreement nonempty | `24 ≥ 1` |
| L1 first wave on `#6320` two-cube | three axis sites |
| `f_two` first wave on the same patch | empty |
| adopt `f_two` | not claimed |

## Imports and non-claims

The only scientific dependency is the current four-axiom authority linked
above, used only to pin the proper-cube covariance group and the open
formation slot. The two-cube, seed, and `o = 0` default are displayed
construction data. No observational comparator is admitted. No dynamics,
Hamiltonian, or record-production process is constructed.

This note displays one additional cube-covariant point of the Admissibility
formation class. It does not adopt that point. It does not write axiom
sentences. It is not leftover-character of L1 and not a new spatial patch.

## Value and no-go boundary

The positive content is the exact covariance of `f_two`, the exact 24-cell
disagreement with `f_L1`, and the empty-versus-three first-wave split on the
displayed two-cube. The negative content is only uniqueness of L1 as a
displayed cube-covariant occupancy-to-lock step on this test object. Further
structure could still select a member. No global impossibility of a formation
rule is claimed.
