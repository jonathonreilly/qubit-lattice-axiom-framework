# Supplied basin and reduced-current coordinate diagnostics

**Date:** 2026-04-21; correction 2026-10-21
**Type:** bounded_theorem
**Status:** supplied finite algebra and diagnostics; physical selection open
**Primary runner:** `scripts/frontier_dm_pmns_native_current_last_mile_reduction_2026_04_21.py`

## Correction and scope

The former synthesis treated a finite basin table as an exhaustive exact-target theorem and treated recovery of affine coordinates as selection of their physical values. Those implications are withdrawn. The [source-cubic comparison](DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md) establishes signs for five supplied numerical rows. Under an additional chamber convention, three of those rows survive, and an independently imposed positive cubic selects Basin 1 among them. It supplies neither completeness nor the physical positivity/branch law.

The [graded-current identity](DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md) recovers delta and q from two supplied current values. It does not select those values. Thus neither result removes the physical source-selection obligations. An asserted local source manifold, even if separately established, would not by itself identify a physical point or close these obligations.

## Exact supplied reduced-family identity

Let Eij be the ordinary 3-by-3 matrix units and supply real x,u,v,w. Define

    A = x I + (u+i v) E12 + w E23 + (u-i v) E31.

Supply the character current from the three probes at phi=0,2pi/3,4pi/3:

    P(phi) = cos(phi)(E12+E31) + sin(phi)i(E12-E31) + E23,
    h(phi) = Re Tr(P(phi)^dagger A),
    J = (h(0)+omega h(2pi/3)+omega^2 h(4pi/3))/3,
    omega = exp(2pi i/3).

Direct contraction gives h(phi)=2u cos(phi)+2v sin(phi)+w. The three-point Fourier sums give J=u+i v. Hence (u,v) -> (Re J,Im J) has identity Jacobian. Neither x nor w is recovered by J. Distinct full matrices can therefore have the same current; this is a coordinate identity on a supplied family, not an exhaustive characterization of physical PMNS data or a law selecting nonzero J.

## Finite controls and unresolved bridges

The runner preserves the two supplied reduced matrices and their current readouts. It also evaluates three specific fixtures: I, the supplied hw=1 response fixture, and 1.13 I reconstructed at lambda=.31. Their currents vanish. The hw=1 fixture uses the three coordinate projectors, sums them to I, and its active response reconstructs that identity. These are concrete examples, not a classification of every possible native route. The .27 passive-response parameter is supplied as before.

The finite five-row sign checks preserve N and P as counterexamples to unrestricted determinant/cubic sign equivalence. Two documentary checks verify that the corrected upstream notes state their limits; text matching is not mathematical evidence for those limits. Vacuous literal-True closure stamps were removed.

Open obligations include physical admissibility of the chamber branch, complete solution coverage, a positivity selector, a physical source-manifold bridge, and selection of current values. Nonzero current activation alone is not a prediction of the required values. No whole-neutrino, Koide, quark, or scale conclusion follows.

## Recovery

Original note and runner are recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under their existing paths. The pre-correction consumer run against the repaired dependencies failed three checks; that failure is preserved in the review evidence. This source is current bounded scientific material, not a historical exemption.
