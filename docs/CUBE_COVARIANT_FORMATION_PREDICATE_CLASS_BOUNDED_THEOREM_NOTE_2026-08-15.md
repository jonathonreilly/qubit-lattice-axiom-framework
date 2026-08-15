---
claim_id: cube_covariant_formation_predicate_class_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 64 occupancy 6-tuples, the cube-covariant boolean formation predicates form a set of size 2^{10}=1024. L1's n≠0 rule is one element. No physical law is adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_covariant_formation_predicate_class_2026_08_15.py
---

# Cube-Covariant Formation Predicate Class

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the finite set of boolean maps on occupancy 6-tuples that are
constant on proper-cube-rotation orbits. No member of the set is selected as
a physical formation rule.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_covariant_formation_predicate_class_2026_08_15.py`](../scripts/cube_covariant_formation_predicate_class_2026_08_15.py)

## Result up front

Let `C = {0,1}^6` be occupancy on the six directed nearest-neighbor slots
`(+x,-x,+y,-y,+z,-z)`. Let `G` be the 24 proper cube rotations, acting by
permuting those six slots. A formation predicate is a map `f: C → {0,1}`. It
is cube-covariant when `f(R·c) = f(c)` for every `R ∈ G` and every `c ∈ C`.

`G` partitions `C` into orbits. Cube-covariant predicates are exactly the
boolean functions constant on those orbits, so the class `F_G` has cardinality
`2^{N_orb}`. Enumerating the 64 cells and the 24 rotations in exact integer
arithmetic gives

```text
N_orb = 10
|F_G| = 1024
```

L1's predicate `form` iff `n ≠ 0`, written `f_L1(c) = 0` exactly when
`c_{+μ} = c_{-μ}` on all three axes, is one element of `F_G`. It is not the
only element. The four maps `f_empty`, `f_any`, `f_full`, and `f_two` defined
below are cube-covariant and pairwise distinct from `f_L1`. The class split
between `f_L1` and `f_two` is the 24 cells with exactly one unbalanced axis.

This note counts a finite function class. It does not adopt a member. It is
not leftover-character of L1, not a new spatial patch, and not Aut-pick.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 10-orbit partition of the 64 occupancy 6-tuples and the resulting 1024 cube-covariant boolean maps are finite exact counts; no physical formation rule is selected."
trace_class: negative_route_pruning
target_claim_id: unique_cube_covariant_formation_predicate
target_blocker_text: "uniqueness of L1's n≠0 formation predicate among cube-covariant boolean maps on the six-neighbor occupancy 6-tuple"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "a physical formation rule, if claimed, must be selected by further structure beyond cube covariance on occupancy 6-tuples"
conditional_surface_status: "exact for boolean maps on the 64 occupancy 6-tuples; no physical law, rate, or site selector"
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
occupancy alphabet `{0,1}` on the six slots is a declared finite test object
for the class count, not a replacement of the one-site possibility domain
`M_2(C)`.

## Exact objects

Write slots in the order `(+x,-x,+y,-y,+z,-z)`. A cell is a 6-tuple
`c ∈ C = {0,1}^6`. The proper cube rotation group `G` is the set of
`3×3` signed permutation matrices of determinant `+1`. Each `R ∈ G` sends
slot `v` to `R v` and acts on cells by

```text
(R·c)_{R v} = c_v.
```

The three axis pairs are `(+x,-x)`, `(+y,-y)`, `(+z,-z)`. Define

```text
n(c) = |{ μ : c_{+μ} ≠ c_{-μ} }|.
```

Then `n(c) = 0` if and only if `c_{+μ} = c_{-μ}` for all three axes.

A formation predicate is any boolean map `f: C → {0,1}`. The cube-covariant
class is

```text
F_G = { f : C → {0,1} : f(R·c) = f(c) for all R ∈ G, c ∈ C }.
```

L1's predicate on this test object is

```text
f_L1(c) = 0  if n(c) = 0,
f_L1(c) = 1  otherwise.
```

Equivalently, `f_L1(c) = 0` iff `c_{+μ} = c_{-μ}` for all three axes. Four
further maps on the same domain are

```text
f_empty(c) = [c = 000000],
f_any(c)   = [sum(c) ≥ 1],
f_full(c)  = [c = 111111],
f_two(c)   = [n(c) ≥ 2].
```

None of these five maps is adopted as a physical law.

## Theorem 1 — orbit count and class cardinality

`G` has 24 elements: six images for the first axis, four remaining images
for the second, and the third axis then fixed by orientation. Inversion is
absent. The induced action on the six slots is 24 distinct permutations.

Direct enumeration of the 64 cells under those 24 permutations yields
`N_orb = 10` orbits. The orbit sizes, sorted, are

```text
[1, 1, 3, 3, 6, 6, 8, 12, 12, 12].
```

They sum to 64. Burnside's lemma in exact integer arithmetic gives the same
count: if `cyc(R)` is the number of cycles of the slot permutation of `R`,

```text
(1/24) ∑_{R ∈ G} 2^{cyc(R)} = 10.
```

A boolean map is cube-covariant if and only if it is constant on each orbit.
Choosing a value in `{0,1}` independently on each orbit therefore gives

```text
|F_G| = 2^{N_orb} = 1024.
```

## Theorem 2 — L1 is one point of the class, not the only point

The function `n` is constant on each `G`-orbit, because a proper cube rotation
permutes the three axis pairs and may swap the two slots of a pair, but cannot
change whether a pair is balanced. Hence `f_L1` is constant on orbits, so
`f_L1 ∈ F_G`.

The same invariance shows `f_empty`, `f_any`, `f_full`, and `f_two` lie in
`F_G`. They are pairwise distinct from `f_L1` on `C`:

- `f_empty(000000) = 1` while `f_L1(000000) = 0`;
- `f_any(111111) = 1` while `f_L1(111111) = 0`;
- `f_full(111111) = 1` while `f_L1(111111) = 0`;
- `f_two` vanishes on every cell with `n = 1`, while `f_L1` equals `1` there.

So uniqueness of `f_L1` inside `F_G` fails by explicit counterexamples. The
count `|F_G| = 1024` already implies the same conclusion. Cube covariance on
occupancy 6-tuples does not select a formation rule.

## Theorem 3 — class split between `f_L1` and `f_two`

The predicates `f_L1` and `f_two` agree on cells with `n = 0` (both vanish)
and on cells with `n ≥ 2` (both equal `1`). They disagree exactly on the cells
with `n = 1`.

There are three choices of the unbalanced axis, two occupancy patterns on that
axis, and two balanced patterns on each of the other two axes, hence

```text
3 × 2 × 2 × 2 = 24
```

such cells. Direct listing of all 64 cells confirms that `f_L1` and `f_two`
disagree on exactly 24 cells. That disagreement is the class split
at-least-one unbalanced axis versus at-least-two.

## Obligation graph

| obligation | exact disposition |
|---|---|
| `|C| = 64` | enumerated binary 6-tuples |
| `|G| = 24`, orientation-preserving | signed permutations of determinant `+1` |
| compute `N_orb` | enumeration plus Burnside; `N_orb = 10` |
| compute `|F_G|` | `2^{N_orb} = 1024` |
| `f_L1 ∈ F_G` | `n` is an orbit invariant |
| four further points of `F_G` distinct from `f_L1` | explicit evaluation on `C` |
| `f_L1` versus `f_two` split | 24 cells with `n = 1` |
| adopt a member of `F_G` as physical law | not claimed |
| leftover-character of L1 | outside the object; not claimed |
| formation site, probability, or rate | open; not supplied |

## Imports and non-claims

The only scientific dependency is the current four-axiom authority linked
above, used only to pin the proper-cube covariance group and the open
formation slot. No observational comparator is admitted. No dynamics,
Hamiltonian, or record-production process is constructed. The five named
maps are witnesses inside a finite function class; the note does not adopt
any of them.

This is not a leftover-character theorem for L1, not a spatial-patch
construction, and not an Aut-pick of a preferred representative.

## Value and no-go boundary

The positive content is the exact integer pair `(N_orb, |F_G|)` and the
explicit witnesses that `f_L1` is not the unique point of `F_G`. The negative
content is only uniqueness of that one predicate from cube covariance on
occupancy 6-tuples. Further structure could still select a member. No global
impossibility of a formation rule is claimed.
