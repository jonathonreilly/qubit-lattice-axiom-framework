# Color Depolarization: Single-Frame Dephasing Insufficiency and Multi-Frame Exhibit

**Date:** 2026-06-09
**Claim type:** bounded_theorem
**Type:** bounded theorem (finite-dimensional channel boundary and sufficiency
exhibit)
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.py`](../scripts/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.py)
**Runner cache:**
[`logs/runner-cache/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.txt`](../logs/runner-cache/frontier_color_depolarization_single_frame_dephasing_and_multiframe_exhibit_2026_06_09.txt)

## Scope

This note concerns the finite `3 x 3` color reduced density `rho_color` and the
unpolarized condition `rho_color = I_3/3` isolated by
[`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md).
It asks which supplied record/instrument channels can or cannot drive the
order parameter

`P(rho) = Tr(rho^2) - 1/3 = ||traceless(rho)||_F^2`

to zero.

The result is not a derivation of color depolarization from the minimal axioms.
It is a channel boundary plus an exact exhibit of one admission-bearing route.

## Theorem Boundary

For the supplied color carrier:

1. `I_3/3` is the unique `SU(3)`-invariant color density.
2. A single dephasing-only projective record step in one orthonormal color
   frame does not depolarize generic states. It fixes the whole diagonal
   population simplex in that frame, not only the point `I_3/3`.
3. A color-blind scalar-projector instrument on the triplet is inert: the only
   invariant projector is `I_3`, so the Lueders channel is the identity on
   `rho_color`.
4. A uniform multi-frame or finite-irreducible averaging structure can
   depolarize exactly. The runner exhibits:
   - computational-frame dephasing followed by Fourier-frame dephasing, which
     reaches `I_3/3` exactly because the overlaps are all `1/3`;
   - the uniform nine-element Heisenberg-Weyl twirl, which reaches `I_3/3`
     exactly in one averaged step.
5. The uniform weight is load-bearing. A non-uniform finite average over the
   same displacement family does not reach `I_3/3`.

This is a sufficiency exhibit, not a necessity theorem for multiple record
frames.

## Relation to the Single-Frame Matter-Mixing Route

The landed source note
[`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
shows a different supplied channel:

`Phi(rho) = D_B(U rho U^dagger)`,

with one fixed record frame `B` and a coherent matter color unitary `U` between
record steps. In that channel, the decision is whether the unistochastic matrix
`T_U[i,j] = |<e_i|U|e_j>|^2` is Perron primitive. A second record frame is
sufficient but not necessary once a matter-mixing unitary is part of the
supplied dynamics.

Therefore the honest conclusion here is narrow:

- dephasing in a single fixed record frame, by itself, is insufficient;
- the color-blind scalar instrument is insufficient;
- uniform multi-frame/twirl averaging is one exact admission-bearing
  sufficiency route;
- Record does not supply the averaging weights, frames, matter unitary, or
  depolarizing dynamics.

## Record Boundary

Record is durable registration of a realized outcome in a supplied readout
context. It supplies no readout context, decomposition, weighting,
normalization, probability rule, measurement/decoherence dynamics, source or
action bridge, time metric, or arbitrary observable identification. A twirl, a
uniform finite average, or a multi-frame cycle is a weighting over instruments;
that weighting must be supplied as a named admission.

The same boundary applies to the single-frame matter-mixing route: Record does
not supply the record frame, the unitary `U`, or Perron-primitivity of `T_U`.

## No-Go Discipline Gate

Status: PASS for the narrow negative boundary only: dephasing in one fixed
record frame, with no intervening mixing dynamics and no second instrument, does
not depolarize generic color states.

- **N1 alternatives.** The review considered five distinct routes: dephasing
  in one fixed frame (tested and closed for generic depolarization);
  color-blind scalar Lueders registration (tested and inert); uniform
  multi-frame averaging (tested and sufficient, therefore outside the negative
  boundary); single-frame matter mixing through
  [`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
  (not closed, and explicitly allowed); and generalized instruments or
  continuous dynamics (not tested here, explicitly outside scope).
- **N2 wall independence.** No independent wall set is claimed. The only scoped
  boundary is the fixed-point simplex of the dephasing-only channel.
- **N3 hidden-wall scan.** The supplied objects are explicit: color carrier,
  one dephasing frame, color-blind projector, uniform averaging weights when
  used, or the adjacent supplied matter-unitary criterion.
- **N4 residual matching.** The negative residual matches only the
  dephasing-only fixed-simplex obstruction and color-blind inertness. It is not
  used as evidence against matter-mixing or generalized-instrument routes.
- **N5 rhetoric audit.** The phrase "single frame" means dephasing-only in one
  fixed record frame. It does not mean every channel that contains one record
  frame.
- **N6 partial-closure scan.** The adjacent matter-mixing criterion is a
  partial-closure route; this note preserves it and narrows away from the
  stronger multi-frame necessity claim.
- **N7 steelman.** A hostile reviewer would object that a single fixed frame
  plus a sufficiently mixing matter unitary can depolarize. That objection is
  correct and is included as a guard and runner check.
- **N8 cross-cycle echo.** The common overclaim pattern is treating one failed
  route as route closure. This note does not do that; it lands only the failed
  dephasing-only route and the sufficient multi-frame exhibit.

## Load-Bearing Inputs

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the color carrier and `SU(3)` action context.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  records that Record supplies no continuous Markov generator, rate, weighting,
  or normalization.
- [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
  is the retained no-go boundary for generator embeddability from Record alone.
- [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
  records the post-append narrowed boundary: occurrence is axiom content, but
  the instrument choice, averaging weight, normalization, and rate are not
  forced by the minimal axioms.
- [`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md)
  supplies the adjacent unpolarized-density condition.
- [`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
  supplies the adjacent guard that multi-frame averaging is sufficient but not
  necessary in the presence of a supplied mixing matter unitary.

## Guards

- **No necessity claim.** This note does not say every depolarizing route needs
  multiple record frames.
- **No dynamics claim.** It does not derive a gauge-link generator, rate,
  matter unitary, mixing regime, or blocking isometry.
- **No Record promotion.** Record does not provide the averaging weights or the
  matter-mixing unitary.
- **Covariance is not contraction.** The identity channel is covariant and
  inert.
- **No purity-conservation claim.** A global unitary on color plus environment
  can change reduced color purity; the theorem does not rely on conservation of
  reduced purity.

## Computed Content

The runner checks:

- the one-dimensional `SU(3)` invariant-density space;
- the order-parameter identity `P(rho) = Tr(rho^2) - 1/3`;
- the diagonal fixed-point simplex for one dephasing frame;
- color-blind scalar-projector inertness;
- exact two-frame MUB depolarization;
- exact Heisenberg-Weyl uniform-twirl depolarization;
- non-uniform-weight failure;
- covariance-not-contraction and reduced-purity guards;
- an explicit single-frame-plus-mixing-unitary witness, to prevent the
  multi-frame exhibit from being misread as a necessity theorem.

No Monte Carlo fit, measured value, new axiom, new framework primitive, audit
verdict, or retained-status change is imported.
