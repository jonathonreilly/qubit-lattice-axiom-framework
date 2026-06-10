# Unraveled Record Trajectories Supply a Conditional Non-Degenerate Step Distribution on the Induced Link

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the supplied `C^3` carrier, the
named quadratic hopping, the named weak record instrument classes, supplied
instrument strength `ε`, and Born outcome weights routed through the existing
Born-rule dependency chain. It proves that exact outcome-tree unravelings give
a non-degenerate single-edge induced-link step distribution on a guarded
generic full-rank domain. It does not supply Born weights from Record, a
continuous generator, a stationary law, central increments, identical edge
laws, cross-edge independence, a CLT, or a new measure/weight premise.
**Script:** `scripts/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=18 FAIL=0`,
exact deterministic outcome-tree enumeration, no Monte Carlo.

## What This Answers

The interleaved mean-map note
[`INTERLEAVED_MEAN_MAP_PERIPHERAL_COUNT_COLLAPSE_ALMOST_PERIODICITY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-06-10`](INTERLEAVED_MEAN_MAP_PERIPHERAL_COUNT_COLLAPSE_ALMOST_PERIODICITY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-06-10.md)
shows mean-level convergence of the named record-interleaved map and explicitly
does not supply a step measure. This note studies the separate
outcome-resolved question: if the named weak instruments are unraveled with
Born outcome weights, what single-edge induced-link increments do the exact
finite outcome trees produce?

The answer is conditional but real: on the generic full-rank domain of the
matter-bilinear polar construction, the Born-weighted outcome tree produces a
strictly non-degenerate single-edge step distribution for both named weak
instrument classes. The result is not a CLT delivery. It leaves the stationarity,
centrality, edge-identity, and many-edge structure requirements open.

## Born And Record Boundary

Born weights are an explicit dependency, not a consequence of Record. The
dependency chain used here is:

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md);
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md);
- [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md).

The post-record probability firewall
[`POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06`](POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md)
is respected: Record supplies durable realized-outcome registration, not the
outcome weights used in this unraveling. This note is therefore bounded by the
Born assembly dependency and cannot be read as Record-supplied probability.

## Results

**(U1) Exact unraveling.** For both named weak two-outcome instrument classes,
the runner verifies Kraus completeness. The Born weights in the finite
depth-five tree sum to `1` to numerical precision, and the Born-weighted average
of conditional states exactly reproduces the deterministic channel. This is
unraveling consistency, not a new probability rule.

**(U2) Guarded full-rank domain and non-degenerate spread.** The induced link
increment `dU = U_eff(n)U_eff(n-1)†` is defined only when the inter-site
coherence block has full rank. The rank requirement is the same precondition as
the color-link construction
[`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md).
The runner exhibits the excluded rank-deficient locus: sub-minimal occupancy
`K < 3` forces rank deficiency, and the `nf=1` per-color sea has a scalar
cross-block with spread-degenerate polar increments. On the guarded generic
full-rank domain, including a full-rank near-sea witness, both the color-blind
and frame-naming weak instruments have strictly positive Born-weighted step
spread. The spread scales down in the weak-instrument limit, as expected.

**(U3) Four residuals remain before any heat-kernel CLT use.** The heat-kernel
CLT note
[`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`](EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md)
requires more than a non-degenerate single-edge distribution. This runner
exhibits four remaining inputs:

- stationarity: increments are state-dependent;
- centrality: on generic states `E[dU]` is non-scalar, with an
  `ε`-independent off-scalar component in the tested instances;
- edge identity: the displayed edge laws differ at order one;
- many-edge structure: cross-edge independence and convolution structure are
  not tested here.

These are open inputs, not a no-go closure.

**(U4) Covariance split and weak-record regime.** The color-blind instrument
unraveling is exactly covariant under the checked conjugate-representation Fock
lift. The frame-naming instrument breaks covariance at order one, as expected
from the supplied frame datum. This re-exhibits the covariance split already
present in the record-instrument and trajectory notes:
[`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md)
and
[`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md).
Finite `ε` is the weak-record regime; it is not in tension with the projective
full-strength erasure limit of the record-instrument note.

## Boundary

This note adds a conditional route ingredient: a non-degenerate
Born-weighted single-edge step distribution on the guarded generic domain. It
does not close the route to a heat-kernel CLT, does not identify the physical
gauge field, and does not derive a dynamics or instrument-selection rule. It
also does not use Record as a probability source. The remaining open inputs are
stationarity, centrality, edge identity, and many-edge independence/convolution.
The four-hats stratification
[`FOUR_HATS_FRAME_CONNECTION_GENERATOR_STRATIFICATION_NON_REDUCTION_NARROW_THEOREM_NOTE_2026-06-09`](FOUR_HATS_FRAME_CONNECTION_GENERATOR_STRATIFICATION_NON_REDUCTION_NARROW_THEOREM_NOTE_2026-06-09.md)
and the unistochastic pointer-frame fork
[`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
remain separate context for the frame/instrument selection question.

No new axiom or primitive is introduced. No new Record-supplied measure,
weight, probability rule, or normalization rule is introduced. `r` is
untouched. The audit lane grades.

## Reproduction

```bash
python3 scripts/frontier_unraveled_record_step_distribution_nondegenerate_2026_06_10.py
```

Expected scorecard: `TOTAL: PASS=18 FAIL=0`.
