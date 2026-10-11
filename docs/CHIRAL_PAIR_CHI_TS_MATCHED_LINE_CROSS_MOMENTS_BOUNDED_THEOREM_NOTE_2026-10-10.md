---
claim_id: chiral_pair_chi_ts_matched_line_cross_moments_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the equal-coefficient line is the rational span of the sum of the chirality cap, the transverse-sign cap, and the matched transverse cross. That sum has two nonzero parity-kernel coefficients and one nonzero excluded coefficient, and its chirality coefficient is 1. Both ratio spans of the oblique-matched plane have chirality coefficient 0, so the line lies outside both spans. For every ordered pair of absolute heights among 1, 2, and 3, a nonzero scale of the line has partner rank 10, so the only ten-kernel partner is 0. At coefficient 1, against the height-2 chirality cap, the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3), rights (1, -3, -2) and (-3, 2, -1), centre pairs (2, 1) and (-2, -1), and kernel cross sum 4. Twice the line has centre pairs (4, 1) and (-4, -1) and kernel cross sum 8. A different ratio of these three kernels is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_chi_ts_matched_line_cross_moments_2026_10_10.py
---

# Chirality, transverse sign, and matched cross

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_chi_ts_matched_line_cross_moments_2026_10_10.py`](../scripts/chiral_pair_chi_ts_matched_line_cross_moments_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the ratio-span note](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
[the parity-span note](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [scaled cross-dot basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the equal-coefficient line, every nonzero scale has partner rank 10, so the only ten-kernel partner is 0."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether the chirality cap plus twice the transverse-sign cap plus the matched transverse cross can pair with a nonzero ten-kernel vector and still have every cross moment equal to 0. That ratio is outside the equal-coefficient line. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); equal coefficients on the chirality cap, the transverse-sign cap, and the matched cross; witness directions (-1, 0, 0) and (0, -1, 0)"
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

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
the sum of the chirality cap, the transverse-sign cap, and the matched
transverse cross can pair with a nonzero ten-kernel vector and still
have every kernel cross sum equal to 0.

**Ansatz.** The line is the rational span of that sum. A vector on the
line is a scale `s` of the three kernels with equal coefficients. The
chirality cap and the transverse-sign cap are parity kernels. The
matched transverse cross is an excluded kernel. Both ratio spans of the
oblique-matched plane have chirality coefficient 0, and this sum has
chirality coefficient 1, so the line is outside both spans. A different
ratio of these three kernels is not on the line. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is
not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`,
and for every rational `s` not 0, the only ten-kernel vector whose
kernel cross sums against `s` times the sum all vanish is 0.

At coefficient 1, the bond on `-e_x` and `-e_y` from heights 1 and 2
fails against the chirality cap. The lefts are `(-1, -2, -3)` and
`(-1, -2, 3)`. The rights are `(1, -3, -2)` and `(-3, 2, -1)`. The
centre pairs are `(2, 1)` and `(-2, -1)`. The kernel cross sum is `4`.
Twice the line has centre pairs `(4, 1)` and `(-4, -1)` and kernel
cross sum `8`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The sum has nonzero coefficients only on
the chirality cap, the transverse-sign cap, and the matched cross.
Each generator of either ratio span has chirality coefficient 0, so no
linear combination of those generators has chirality coefficient 1.

Each centre value is linear in the coefficient vector, so every partner
row of a scale `s` is `s` times the partner row of the sum. The runner
checks that the doubled vector doubles every partner row on each
ordered height pair. The partner rank of the sum is 10 on each of
those six pairs. A nonzero scale therefore also has partner rank 10,
and the only partner is 0. The two witness bonds are direct centre
sums.

**Obligations.** Proved here: the line lies outside both ratio spans,
the partner rank is 10 on every ordered height pair, the scaling of
the partner rows, and the cross sums `4` and `8`. Cited from the
parity-span note, and not re-proved: the chirality cap and the
transverse-sign cap are parity kernels, and the matched cross is
outside that span. Cited from the basis note, and not re-proved: the
ten named kernels are a basis of one opposite-height ansatz. Cited
from the ratio-span note, and not re-proved: the two triples are the
ratio spans. The strongest missing lemma is whether the chirality cap
plus twice the transverse-sign cap plus the matched cross can pair
with a nonzero ten-kernel vector and still have every cross moment
equal to 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not take a different ratio of these three kernels.
- It does not re-prove the ratio spans or the parity span.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_chi_ts_matched_line_cross_moments_2026_10_10.py`
checks the line, the six partner ranks, and the two witness bonds.
`TOTAL: PASS=7 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner ranks, and the witness sums are
enumerated here. The parity-span note names the parity kernels. The
basis note supplies the ten-kernel basis. The ratio-span note names
the two triples. The order-blind converse is not applied.
