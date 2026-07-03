# The Hierarchy Magnitude's 4π Boundary Is Coupling/Geometry, Not Gaussian Measure

**Date:** 2026-06-06; source-boundary repair 2026-06-08; runner-marker
repair 2026-06-09
**Type:** boundary correction / status relocation
**Claim type:** bounded_theorem
**Status:** source-side bounded support. This row repairs the 4π-vs-2π boundary
inside the supplied hierarchy formula and explicitly leaves the readout,
convention, dressing, and value-gate residuals open. It sets no audit status; the
audit lane owns final classification.
`actual_current_surface_status=bounded-support; audit_required_before_effective_retained=true; bare_retained_allowed=false`.
**Runner:** [`scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py`](../scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py)
(`TOTAL: PASS=62 FAIL=0`).
**Cached log:** `logs/runner-cache/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.txt`

## 2026-06-08 Source-Boundary Repair

The conditional audit found that the prior packet mixed a correct 4π/2π
arithmetic boundary with unclosed claims about the hierarchy magnitude's physical
readout/convention/dressing chain, and that the runner included a PASS condition
using observed `M_Pl` and `v`. This repair removes that observed-value check and
states the narrower source boundary:

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The repair originally stacked on the temporal-count source packet from #3260.
That packet has now landed on `main`, so this row consumes it as current source
context while still requiring independent audit for this 4π boundary.

## 2026-06-09 Runner-Marker Repair

The latest audit found that the source-boundary math closed but the completed
runner/cache still checked three stale minimal-block readout markers from the
pre-cleanup wording. The minimal-block row is now a route-specific
`retained_no_go` packet:
`MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06` proves that Record plus RP
two-step positivity does not select `L_t=2` over the OS continuum, while
leaving a future UV/minimal-block readout bridge open. The runner now checks
that current no-go wording instead of the obsolete demotion strings.

## Statement

**T1. Formula-local 4π/2π boundary.** Given the supplied hierarchy-formula slot
`alpha_bare = g_bare^2/(4π)` and exponent `16`, replacing the coupling
normalization `4π` with a Gaussian `2π` changes the factor by exactly

```text
((1/(2π)) / (1/(4π)))^16 = 2^16.
```

This is pure algebra inside the supplied formula. It does not consume observed
`M_Pl`, observed `v`, PDG values, fitted `u_0`, or a value match.

**T2. Framework-local geometric 4π.** The framework-local `Z^3`
nearest-neighbor graph-Laplacian Green-kernel packet derives the continuum-leading
coefficient `G(r) ~ 1/(4π r)` from the native lattice symbol
`2 sum_mu(1-cos k_mu) -> |k|^2` and the `S^2` solid angle. This supplies the
native geometric 4π. It does not by itself derive that a physical static-source
readout must use that kernel as a coupling potential.

**T3. Count-16 algebra.** One coupling normalization raised to exponent count 16
is algebraically the same number as sixteen identical factors:

```text
(4π)^-16 = ((4π)^-1)^16.
```

Therefore the "4π has multiplicity 1, not 16" objection is too strong as a
decomposition demand once the formula supplies an exponent count. The count
source is not re-proved here; it is supplied by the stacked temporal-count packet,
and the minimal-record readout selection remains demoted/open as stated there.

**Therefore:** this row removes the specific `2^16` Gaussian-measure objection
to the supplied 4π formula slot. It does not close the hierarchy value gate and
does not prove the physical coupling/readout/dressing chain.

## Source Packet

| role | source | current source status |
|---|---|---|
| `Z^3` Green-kernel 4π geometry | [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md), runner [`lattice_greens_z3_asymptotic_normalization_certificate.py`](../scripts/lattice_greens_z3_asymptotic_normalization_certificate.py), cache [`lattice_greens_z3_asymptotic_normalization_certificate.txt`](../logs/runner-cache/lattice_greens_z3_asymptotic_normalization_certificate.txt) | `retained_bounded` |
| native BZ Haar normalization | [`BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26`](BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md), runner [`bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py`](../scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py), cache [`bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.txt`](../logs/runner-cache/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.txt) | `retained_bounded` |
| `g_bare` constraint/convention restatement | [`G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`](G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md), runner [`frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.py`](../scripts/frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.py), cache [`frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.txt`](../logs/runner-cache/frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.txt) | `retained` |
| exponent count-16 boundary | [`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06`](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md), runner [`magnitude_temporal_factor_is_count_not_rate_2026_06_06.py`](../scripts/magnitude_temporal_factor_is_count_not_rate_2026_06_06.py), cache [`magnitude_temporal_factor_is_count_not_rate_2026_06_06.txt`](../logs/runner-cache/magnitude_temporal_factor_is_count_not_rate_2026_06_06.txt) | `retained_bounded` count-not-rate boundary |
| minimal-block readout selection | [`MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06`](MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06.md), runner [`magnitude_reads_minimal_record_block_2026_06_06.py`](../scripts/magnitude_reads_minimal_record_block_2026_06_06.py), cache [`magnitude_reads_minimal_record_block_2026_06_06.txt`](../logs/runner-cache/magnitude_reads_minimal_record_block_2026_06_06.txt) | `retained_no_go` route-specific readout-scale boundary |

## Honest Residual

The source-boundary repair does not close these load-bearing pieces:

| piece | role | current source status |
|---|---|---|
| `static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27` | physical readout `V(r) = -C g^2 G(r)` linking coupling to the native Green kernel | `unaudited`; accepted-premise/import boundary |
| `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27` | `alpha := g^2/(4π)` convention bridge | `unaudited`; accepted premise |
| `cl3_normalization_i3_accepted_premise_bridge_bounded_note_2026-05-27` | `Tr(T_a T_b)=delta_ab/2` normalization bridge | `unaudited`; accepted premise |
| `hierarchy_formula_honest_status_note_2026-05-10` | per-mode dressing/value-gate honesty, including P3 | `unaudited`; value gate remains open |

These are the remaining science targets. The 4π boundary being repaired here is
not a substitute for deriving I1/I2/I3/P3.

## What This Note Does Not Claim

- Does **not** derive the magnitude `v` or close the hierarchy value gate.
- Does **not** consume observed `M_Pl`, observed `v`, PDG values, or a fitted
  `u_0` in any PASS condition.
- Does **not** promote the static-source readout, alpha convention, Cl3
  normalization, per-mode dressing, or minimal-block readout selection.
- Does **not** claim that Green-kernel 4π geometry alone supplies a physical
  coupling/readout theorem.
- Sets no audit status.

## Validation

`scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py`
(`PASS=62 FAIL=0`): the runner verifies the status firewall and source packet;
the formula-local `4π`/`2π` algebra with no observed-value constants; the
native `Z^3` Green-kernel solid-angle normalization; the count-16 algebra; and
the readout/convention/dressing residuals remaining explicitly open.

## Reading Rule

This note is the claim boundary for: the supplied hierarchy formula's `4π` slot
is not a Gaussian `2π` measure slot, and the exact `2^16` objection is a
measure/coupling conflation inside that supplied formula. It does not close the
formula's physical readout, convention, dressing, or value gate.
