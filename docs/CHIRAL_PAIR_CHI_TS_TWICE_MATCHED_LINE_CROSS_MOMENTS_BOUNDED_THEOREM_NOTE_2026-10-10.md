---
claim_id: chiral_pair_chi_ts_twice_matched_line_cross_moments_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the 48 signed permutations of (1, 2, 3), the doubled matched line is the rational span of the chirality cap plus the transverse-sign cap plus twice the matched transverse cross. That sum has two nonzero parity-kernel coefficients and one nonzero excluded coefficient. Its matched coefficient is 2 and its chirality coefficient is 1, so it is not a scale of the equal-coefficient line. Its transverse-sign coefficient is 1, so it is not a scale of the doubled transverse-sign line. Both ratio spans of the oblique-matched plane have chirality coefficient 0, so the line lies outside both spans. For every ordered pair of absolute heights among 1, 2, and 3, a nonzero scale of the line has partner rank 10, so the only ten-kernel partner is 0. At coefficient 1, against the height-2 chirality cap, the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3), rights (1, -2, -3) and (-3, 2, -1), centre pairs (0, 1) and (-2, -1), and kernel cross sum 2. Twice the line has centre pairs (0, 1) and (-4, -1) and kernel cross sum 4. The equal-coefficient vector on the same bond has centre pairs (0, 1) and (-1, -1) and kernel cross sum 1. A different ratio of these three kernels is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_chi_twice_ts_matched_line_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_chi_ts_matched_line_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_chi_ts_twice_matched_line_cross_moments_2026_10_10.py
---

# Chirality, transverse sign, and doubled matched cross

**Date:** 2026-10-11

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_chi_ts_twice_matched_line_cross_moments_2026_10_10.py`](../scripts/chiral_pair_chi_ts_twice_matched_line_cross_moments_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the doubled transverse-sign line](CHIRAL_PAIR_CHI_TWICE_TS_MATCHED_LINE_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
[the equal-coefficient line](CHIRAL_PAIR_CHI_TS_MATCHED_LINE_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the ratio-span note](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "On the doubled matched line, every nonzero scale has partner rank 10, so the only ten-kernel partner is 0."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Decide whether the chirality cap plus twice the transverse-sign cap plus twice the matched transverse cross can pair with a nonzero ten-kernel vector and still have every cross moment equal to 0. That ratio is outside the equal-coefficient line, the doubled transverse-sign line, and the doubled matched line. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); chirality coefficient 1, transverse-sign coefficient 1, matched coefficient 2; witness directions (-1, 0, 0) and (0, -1, 0)"
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

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
the chirality cap plus the transverse-sign cap plus twice the matched
transverse cross can pair with a nonzero ten-kernel vector and still
have every kernel cross sum equal to 0.

**Ansatz.** The line is the rational span of that sum. A vector on the
line is a scale `s` of the chirality cap, the transverse-sign cap, and
twice the matched transverse cross. The chirality cap and the
transverse-sign cap are parity kernels. The matched transverse cross is
an excluded kernel. The matched coefficient is twice the chirality
coefficient, so the sum is not a scale of the equal-coefficient line.
The transverse-sign coefficient equals the chirality coefficient, so the
sum is not a scale of the doubled transverse-sign line. Both ratio spans
of the oblique-matched plane have chirality coefficient 0, and this sum
has chirality coefficient 1, so the line is outside both spans. A
different ratio of these three kernels is not on the line. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`,
and for every rational `s` not 0, the only ten-kernel vector whose
kernel cross sums against `s` times the sum all vanish is 0.

At coefficient 1, the bond on `-e_x` and `-e_y` from heights 1 and 2
fails against the chirality cap. The lefts are `(-1, -2, -3)` and
`(-1, -2, 3)`. The rights are `(1, -2, -3)` and `(-3, 2, -1)`. The
centre pairs are `(0, 1)` and `(-2, -1)`. The first left contributes 0.
The second left contributes 2. The kernel cross sum is `2`. Twice the
line has centre pairs `(0, 1)` and `(-4, -1)` and kernel cross sum `4`.
The equal-coefficient vector on the same bond has centre pairs `(0, 1)`
and `(-1, -1)` and kernel cross sum `1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The sum has nonzero coefficients only on
the chirality cap, the transverse-sign cap, and the matched cross, and
those coefficients are `1`, `1`, and `2`. Each generator of either
ratio span has chirality coefficient 0, so no linear combination of
those generators has chirality coefficient 1. A scale of the
equal-coefficient sum has equal chirality and matched coefficients, and
this sum does not. A scale of the doubled transverse-sign sum has
transverse-sign coefficient twice the chirality coefficient, and this
sum does not.

Each centre value is linear in the coefficient vector, so every partner
row of a scale `s` is `s` times the partner row of the sum. The runner
checks that the doubled vector doubles every partner row on each
ordered height pair. The partner rank of the sum is 10 on each of
those six pairs. A nonzero scale therefore also has partner rank 10,
and the only partner is 0. The witness bonds are direct centre sums.

**Obligations.** Proved here: the line lies outside the
equal-coefficient line, the doubled transverse-sign line, and both
ratio spans, the partner rank is 10 on every ordered height pair, the
scaling of the partner rows, and the cross sums `2`, `4`, and `1`.
Cited from the equal-coefficient note and the doubled transverse-sign
note, and not re-proved: the chirality cap and the transverse-sign cap
are parity kernels, and the matched cross is an excluded kernel. Cited
from the ratio-span note, and not re-proved: the two triples are the
ratio spans. The strongest missing lemma is whether the chirality cap
plus twice the transverse-sign cap plus twice the matched cross can
pair with a nonzero ten-kernel vector and still have every cross moment
equal to 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not take a different ratio of these three kernels.
- It does not re-prove the equal-coefficient line, the doubled transverse-sign line, or the ratio spans.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_chi_ts_twice_matched_line_cross_moments_2026_10_10.py`
checks the line, the six partner ranks, and the witness bonds.
`TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner ranks, and the witness sums are
enumerated here. The equal-coefficient note and the doubled
transverse-sign note name those lines and the parity kernels. The
ratio-span note names the two triples. The order-blind converse is not
applied.


## No-Go Discipline Gate

**Packet status: incomplete; no PASS claimed.** This is a partial narrowing
proposal under the displayed finite ansatz, not a framework-wide exclusion.

- **N1:** The actual routes here are the finite orbit/slice reduction and
  the explicit algebraic argument in the Proof. Related coefficient choices
  are not five independent approach families. The five-family packet is
  absent; no route count or retained prior authority is invented.
- **N2:** The alphabet, covariance, support and coefficient restrictions
  define one ansatz. No count of independent physical walls is asserted.
- **N3:** The uniform finite-record model and any order-blind converse are
  explicit mathematical inputs. They supply no physical selection, formation
  rate, empirical scale or additional framework primitive.
- **N4:** The Imports and Obligations identify which parent result is used.
  A finite kernel rank, a two-centre cross sum and a normalized neighbour
  product are different statements; none is substituted for another.
- **N5:** The primary runner reports the finite resolution it executes.
  Mode spectra, evolving site ensembles and lattice-wide dynamics are not
  computed. Any all-window consequence uses the cited analytical converse
  with strict positivity, not a lattice simulation.
- **N6:** No new axiom is requested or declared necessary. Expanding the
  ansatz is legitimate further work and is not ruled out by these results.
- **N7:** The strongest broader escape is to allow additional support
  signatures or coupled height sectors: cancellation can change when the
  partner domain changes. A full-space classification must derive the joint
  slice and product equations and prove their solution set; the present
  restricted result supplies no such closure. Inside the stated ansatz the
  displayed exact proof, rather than failure to find an escape, is the claim.
- **N8:** The cited parent and companion notes exhibit successive escapes
  from smaller cap and cross spans. Those examples explicitly prohibit
  treating any restricted span classification as closure of the full bond
  space. Historical next-step statements are local frontiers, not evidence
  that later companion results remain unproved.
