# Lattice-Quantum-Record Framework Publication Package

This directory is the public scientific package for the current `main` branch.

Use it if you want:

- the paper-facing claim surface
- the current prediction and falsification surface
- the domain map of the science surfaced in the repo
- the canonical validation and reproduction path

**Audit status note:** this package is now under the repo audit lane. Source
notes self-declare only `proposed_retained` / `proposed_promoted`; only
[../../audit/AUDIT_LEDGER.md](../../audit/AUDIT_LEDGER.md) can ratify a row as
retained-grade through `effective_status`. Retained-grade statuses are
`retained`, `retained_no_go`, and `retained_bounded`; boxed
`decoration_under_*` rows may be cited only as decorations under their retained
parent, not as independent retained rows. `promoted` is publication-capture
language, not an audit `effective_status`. Tables in this directory remain the
manuscript-capture surface, but until the audit ledger marks a row clean, read
legacy `retained` / `promoted` wording as proposed package status.

## Read In This Order

1. [Generated front-door status snapshot](../../repo/FRONT_DOOR_STATUS.md)
2. [Minimal Lattice/Quantum/Record axiom memo](../../MINIMAL_AXIOMS_2026-06-05.md)
3. [Public arXiv draft](./ARXIV_DRAFT.md)
4. [Current falsifiable predictions](./FALSIFIABLE_PREDICTIONS_2026-06-08.md)
5. [Prediction surface](./PREDICTION_SURFACE_2026-04-15.md)
6. [Quantitative summary table with audit badges](./QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md)
7. [Reproduce guide](./REPRODUCE.md)
8. [Manuscript claims with audit badges](./CLAIMS_TABLE_EFFECTIVE_STATUS.md)
9. [Science map by domain](./SCIENCE_MAP.md)
10. [Inputs and qualifiers](./INPUTS_AND_QUALIFIERS_NOTE.md)
11. [What this paper does not claim](./WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)
12. [Derivation / validation map with audit badges](./DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md)
13. [Results index with audit badges](./RESULTS_INDEX_EFFECTIVE_STATUS.md)
14. [Derivation atlas with audit badges](./DERIVATION_ATLAS_EFFECTIVE_STATUS.md)
15. [Full claim ledger with audit badges](./FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md)

For the full package-capture inventory, use:

- [PUBLICATION_MATRIX.md](./PUBLICATION_MATRIX.md)

## Current Audit-Badged State

This README is a navigation surface, not a status authority. Current status is
owned by:

- [../../repo/FRONT_DOOR_STATUS.md](../../repo/FRONT_DOOR_STATUS.md) for the
  generated front-door aggregate snapshot
- [../../audit/AUDIT_LEDGER.md](../../audit/AUDIT_LEDGER.md) for row-level
  audit verdicts and scopes
- the generated effective-status mirrors linked above for claim, quantitative,
  validation, results, atlas, and full-ledger publication views
- [PUBLICATION_AUDIT_DIVERGENCE.md](./PUBLICATION_AUDIT_DIVERGENCE.md) for
  publication rows whose manuscript wording is ahead of audit ratification

When reading the package tables, treat these as curation categories rather than
audit badges:

- framework/backbone rows: Lattice, Quantum, Record, the `Cl(3,0)` reading,
  dimension, gauge, GR, and QG/continuum routes
- quantitative and flavor rows: electroweak/QCD/Yukawa inputs, CKM atlas rows,
  `alpha_s` derived rows, top transport, and related corollaries
- structural/corollary rows: strong CP, Lorentz, topology, hypercharge/anomaly,
  cosmology, Hubble, `N_eff`, matter-radiation equality, GR/QG, and spectral
  tower rows
- dark-matter, charged-lepton, and bounded companion rows: manuscript-capture
  surfaces whose audit grade must be checked row by row

Known audit-sensitive examples include the CKM atlas, `alpha_s` derived notes,
`N_eff`, matter-radiation equality, Hubble structural rows, DM transport,
hypercharge/anomaly rows, and GR/QG rows. Do not infer retained grade from their
appearance in this package; use each row's ledger `effective_status` or the
generated effective-status mirror.

## What Is Publicly Surfaced Here

The package is organized around four distinct surfaces:

1. `claims`
   what the paper may claim safely
2. `predictions`
   what the prediction surface currently lists, including bounded and delayed-observability
   rows
3. `science by domain`
   where each major physics area lives in the repo
4. `validation`
   how to reproduce the active package and pair claims with runners/logs

Those surfaces are intentionally separate:

- [CLAIMS_TABLE.md](./CLAIMS_TABLE.md) is the short manuscript claim surface
- [PREDICTION_SURFACE_2026-04-15.md](./PREDICTION_SURFACE_2026-04-15.md) is the
  shortest public prediction/falsification surface
- [SCIENCE_MAP.md](./SCIENCE_MAP.md) is the domain-organized science map
- [DERIVATION_VALIDATION_MAP.md](./DERIVATION_VALIDATION_MAP.md) and
  [REPRODUCE.md](./REPRODUCE.md) are the evidence and reproduction surfaces

## Science By Domain

- spacetime, gravity, and quantum gravity:
  [GRAVITY_PUBLICATION_PACKAGE_SUMMARY_2026-04-15.md](./GRAVITY_PUBLICATION_PACKAGE_SUMMARY_2026-04-15.md),
  [SCIENCE_MAP.md](./SCIENCE_MAP.md)
- gauge, matter, and strong CP:
  [SCIENCE_MAP.md](./SCIENCE_MAP.md),
  [DERIVATION_VALIDATION_MAP.md](./DERIVATION_VALIDATION_MAP.md)
- quantitative electroweak, QCD, Yukawa, Higgs:
  [QUANTITATIVE_SUMMARY_TABLE.md](./QUANTITATIVE_SUMMARY_TABLE.md),
  [USABLE_DERIVED_VALUES_INDEX.md](./USABLE_DERIVED_VALUES_INDEX.md),
  [hadron mass open lane](../../lanes/open_science/01_HADRON_MASS_PROGRAM_OPEN_LANE_2026-04-26.md)
- flavor, CKM, quark, charged leptons:
  [CLAIMS_TABLE.md](./CLAIMS_TABLE.md),
  [SCIENCE_MAP.md](./SCIENCE_MAP.md)
- neutrino and dark matter:
  [SCIENCE_MAP.md](./SCIENCE_MAP.md),
  [PUBLICATION_MATRIX.md](./PUBLICATION_MATRIX.md)
- cosmology and companion phenomenology:
  [PREDICTION_SURFACE_2026-04-15.md](./PREDICTION_SURFACE_2026-04-15.md),
  [SCIENCE_MAP.md](./SCIENCE_MAP.md)
- absolute-scale / Planck-scale lane:
  [SCIENCE_MAP.md](./SCIENCE_MAP.md),
  [INPUTS_AND_QUALIFIERS_NOTE.md](./INPUTS_AND_QUALIFIERS_NOTE.md),
  [PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md](../../PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md),
  [PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md](../../PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md),
  [PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md](../../PLANCK_SOURCE_UNIT_NORMALIZATION_SUPPORT_THEOREM_NOTE_2026-04-25.md),
  [PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md](../../PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md),
  [PLANCK_FINITE_RESPONSE_NO_GO_NOTE_2026-04-24.md](../../PLANCK_FINITE_RESPONSE_NO_GO_NOTE_2026-04-24.md),
  [PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md](../../PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md),
  [AREA_LAW_MULTIPOCKET_SELECTOR_NO_GO_NOTE_2026-04-25.md](../../AREA_LAW_MULTIPOCKET_SELECTOR_NO_GO_NOTE_2026-04-25.md),
  [PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md](../../PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md)

## Validation and Reproduction

Use these in order:

1. [REPRODUCE.md](./REPRODUCE.md)
2. [RELEASE_ENVIRONMENT.md](./RELEASE_ENVIRONMENT.md)
3. [DERIVATION_VALIDATION_MAP.md](./DERIVATION_VALIDATION_MAP.md)
4. [RESULTS_INDEX.md](./RESULTS_INDEX.md)

Validation rule:

- use the note as the claim boundary
- use the runner as the executable check
- use the map and results index to find the canonical path
- use the package qualifiers before promoting any bounded/support row

The archival selective freeze is still kept for provenance, but it is not the
same thing as the current active package state:

- [REPRODUCIBILITY_FREEZE_2026-04-14.md](./REPRODUCIBILITY_FREEZE_2026-04-14.md)

## Package Boundaries

- framework/input boundary:
  [MINIMAL_AXIOMS_2026-06-05.md](../../MINIMAL_AXIOMS_2026-06-05.md)
- explicit package qualifiers:
  [INPUTS_AND_QUALIFIERS_NOTE.md](./INPUTS_AND_QUALIFIERS_NOTE.md)
- explicit non-claims:
  [WHAT_THIS_PAPER_DOES_NOT_CLAIM.md](./WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)
- optional reduction/support context:
  [SINGLE_AXIOM_INFORMATION_NOTE.md](../../SINGLE_AXIOM_INFORMATION_NOTE.md),
  [SINGLE_AXIOM_HILBERT_NOTE.md](../../SINGLE_AXIOM_HILBERT_NOTE.md)

## Package Rule

- if a result is manuscript-facing, it must appear in
  [CLAIMS_TABLE.md](./CLAIMS_TABLE.md)
- if a result is publication-captured, it must appear in
  [PUBLICATION_MATRIX.md](./PUBLICATION_MATRIX.md)
- if a result is meant to be validated, it must be reachable from
  [DERIVATION_VALIDATION_MAP.md](./DERIVATION_VALIDATION_MAP.md),
  [RESULTS_INDEX.md](./RESULTS_INDEX.md), and [REPRODUCE.md](./REPRODUCE.md)
- if a result is only historical, route-local, or superseded, it should not be
  treated as the public package authority
