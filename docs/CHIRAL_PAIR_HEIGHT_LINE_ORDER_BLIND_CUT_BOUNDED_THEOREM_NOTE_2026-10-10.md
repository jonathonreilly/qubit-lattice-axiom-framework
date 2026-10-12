---
claim_id: chiral_pair_height_line_order_blind_cut_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the height-linear family phi_d(a, b) = 1 + c (a·d)(b·(-d)) is bond-symmetric and soldered for every rational c, and every far-end sum equals 48. At c = 1/10 the factor is strictly positive and not constant, and the uniform two-neighbour moment on the opposite z-directions at (1, 2, 3) is 71/50. Order-blindness therefore cuts the normalised soldered bond space. The order-blind subset is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_height_line_order_blind_cut_2026_10_10.py
---

# A height-linear line on the chiral pair is not order-blind

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_height_line_order_blind_cut_2026_10_10.py`](../scripts/chiral_pair_height_line_order_blind_cut_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "At coefficient 1/10 the height-linear factor is strictly positive and its opposite-direction moment is 71/50."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a strictly positive order-blind factor on the 48-point chiral pair lies outside the exhibited chiral-cap line. Do not repeat the dimension count."
conditional_surface_status: "48 signed permutations of (1, 2, 3); height-linear family 1 + c (a·d)(b·(-d)); uniform two-neighbour moments; coefficient 1/10"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Quoted premises

Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site."

Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations."

Reading note (2), interpretive: "Read with Record, the distribution
concerns which possibility a forming record locks, conditional on
formation at that site; it does not supply the formation site,
probability, or rate."

Theorem 2 of the parent, for a strictly positive translation-covariant
nearest-neighbour rule that is order-blind on the 7-site cross: "with
phi_d(a, b) = phi_-d(b, a) and E_r0[prod_{(d, b) in N} phi_d(., b)] = 1
for every N." The parent converse is not applied. The parent leaves the
sentence "Other generic orbits and higher-rank bond spaces are not
classified."

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
order-blindness cuts the normalised soldered bond space.

**Ansatz.** The height-linear family is

```text
phi_d(a, b) = 1 + c (a·d) (b·(-d))
```

with `c` rational. The direction `d` is an axis step, and both records
lie in the alphabet. The factor uses no base site, so a translation
leaves it unchanged. The normalised representative is `phi / 48`. The
parent's chiral-cap family is not this ansatz. A bond factor outside
this line is not classified here.

**Conclusion.** The family is bond-symmetric and soldered for the tested
coefficient, and every far-end sum equals 48. At `c = 1/10` every value
is strictly positive, the factor is not constant, and the uniform
average of the product on `e_z` and `-e_z` at `(1, 2, 3)` is `71/50`.
Theorem 2 would force that average to equal 1. The factor is therefore
not order-blind. It lies in the normalised space of the chiral-pair
bond note, so order-blindness cuts that space.

**Proof.** The runner enumerates the proper rotations and the alphabet.
The alphabet is the union of the two proper orbits, and `(2, 1, 3)`
lies in the second. Direct comparison gives bond symmetry and soldered
covariance at `c = 1/10`.

The same coefficient makes every sum over the right-hand record equal
48, so the quotient by 48 has far-end sum 1. One coordinate has mean 0
and second moment `14/3`. For every pair of records, the uniform
product on the opposite z-directions equals

```text
1 + (14/3) c^2 h1 h2
```

where `h1` and `h2` are the z-coordinates of the two right-hand records.
At `c = 1/10` and both records `(1, 2, 3)`, both heights are 3, and the
value is `71/50`. The same coefficient keeps every perpendicular product
on `e_x` and `e_z` equal to 1, and the opposite product at `c = 0` equals
1. The witness value is the opposite-direction failure.

**Obligations.** Proved here: bond symmetry, soldered covariance, the
far-end sums, the second moment `14/3`, the opposite-moment identity,
the witness `71/50`, strict positivity, and the perpendicular moments.
Cited from Theorem 2, and not re-proved: a strictly positive
translation-covariant order-blind rule has every neighbour-product
average equal to 1. Cited from the chiral-pair bond note, and not
re-proved: far-end sum 1 is the normalisation of that bond space. The
dimension count is not repeated. The parent converse is not applied.
The strongest missing lemma is an order-blind factor on this alphabet
outside the exhibited chiral-cap line. This ansatz does not contain
that classification.

## What this does not do

- It does not select a scale. The coefficient `1/10` is a witness.
- It does not classify the order-blind subset of the normalised space.
- It does not re-derive the parent's chiral-cap family.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_height_line_order_blind_cut_2026_10_10.py` repeats
the symmetry, the far-end sums, the moment identity, and the witness
`71/50`. `TOTAL: PASS=12 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the alphabet, and the height-linear moments are
enumerated here. Theorem 2 supplies the moment obstruction. The
chiral-pair bond note supplies the meaning of far-end sum 1. The parent
converse is not applied.
