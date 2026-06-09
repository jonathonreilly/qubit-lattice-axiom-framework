# Lattice-Quantum-Record Framework

This repository contains the public scientific package for a three-axiom
discrete-physics program:

1. **Lattice** - the site set is `Z^3` with nearest-neighbor cubic adjacency.
2. **Quantum** - one qubit lives at every site, equivalently one-site
   `M_2(C)` / real `Cl(3,0)` local algebra.
3. **Record** - durable realized-outcome registration with finite scalar
   additivity on a fixed readout context.

The canonical axiom memo is
[`docs/MINIMAL_AXIOMS_2026-06-05.md`](docs/MINIMAL_AXIOMS_2026-06-05.md).
Old `A1` / `A2` / `A3` numbering is historical; new repo surfaces should use
the names Lattice, Quantum, and Record unless quoting older notes.

## Read First

Use these entrypoints in order:

1. [Generated front-door status snapshot](docs/repo/FRONT_DOOR_STATUS.md)
2. [Minimal axiom memo](docs/MINIMAL_AXIOMS_2026-06-05.md)
3. [Publication package README](docs/publication/ci3_z3/README.md)
4. [Current falsifiable predictions catalog](docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md)
5. [Manuscript claims with audit badges](docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md)
6. [Quantitative table with audit badges](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md)
7. [Publication/audit divergence report](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md)
8. [Reproduce guide](docs/publication/ci3_z3/REPRODUCE.md)
9. [Science map by domain](docs/publication/ci3_z3/SCIENCE_MAP.md)
10. [Open science lanes](docs/lanes/open_science/README.md)
11. [Full audit ledger](docs/audit/AUDIT_LEDGER.md)

## Current Status

The repo is in an audit-transition state. Source notes and publication tables
still contain legacy `retained` / `promoted` wording, but the publication-facing
authority is the audit-derived `effective_status` in
[`docs/audit/AUDIT_LEDGER.md`](docs/audit/AUDIT_LEDGER.md). Retained-grade
`effective_status` values are `retained`, `retained_no_go`, and
`retained_bounded`; boxed `decoration_under_*` rows are decorations under a
retained parent, not independent retained rows. `promoted` is
publication-capture language, not an audit `effective_status`. The fastest
current summary is the generated
[`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md), refreshed by
`bash docs/audit/scripts/run_pipeline.sh`.

The pipeline currently derives:

- the audit ledger and effective-status counts;
- the audit queue and cycle-break targets;
- publication-package effective-status mirrors; and
- the publication/audit divergence report.

This matters because the public package is ahead of the fully ratified audit
surface in places. Treat any source-note or manuscript wording as proposed
unless the effective-status view marks the cited authority retained-grade.

## Falsifiable Forecasts

The current sharp forecast catalog is
[`docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md`](docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md).
It highlights three near-term tests:

- PMNS `delta_CP` in the third quadrant near maximal,
  `delta_CP in [251.86 deg, 270.00 deg]`;
- PMNS `theta_23` in the upper octant, with certified
  `s_23^2 > 0.5277` on the stated comparison rectangle; and
- absolute Higgs-vacuum stability as the framework-side discriminator against
  SM metastability.

Those forecasts are explicitly conditional and currently not unconditional
closures. The catalog records the falsifier thresholds and the named external
comparison bands; quote it rather than copying a number without its
conditionality.

## Reusable Numbers

For numeric reuse, start from the audit-badged generated views:

- [Usable derived values](docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md)
- [Quantitative summary table](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md)

Important current values include the electroweak scale `v`, the canonical
plaquette/coupling package, CKM atlas quantities, the YT/top and Higgs
identification-conditioned rows, neutrino observable bounds, and the
cosmology/DM structural support rows. Each value must carry the claim class
and qualifier shown in those generated tables.

## Lane State

The active science is organized by domain in
[`docs/publication/ci3_z3/SCIENCE_MAP.md`](docs/publication/ci3_z3/SCIENCE_MAP.md)
and by work lane in [`docs/lanes`](docs/lanes/README.md).

High-level state:

- **Framework baseline:** Lattice, Quantum, and Record are the named axiom
  surface; the Record axiom is deliberately narrow and does not supply Born
  weights, measurement dynamics, physical persistence dynamics, source/action
  identification, or downstream selectors by itself.
- **Ratified backbone:** the audit ledger contains retained-grade positive,
  no-go, bounded, and boxed-decoration rows. Use
  [`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md) for the
  current generated counts.
- **Publication package:** manuscript and quantitative surfaces exist, but the
  effective-status mirrors show which cited authorities are audit-retained and
  which remain unaudited, conditional, renaming-only, numerical-match, or open.
- **Open flagship work:** charged-lepton mass retention remains open, including
  Koide `Q = 2/3`, `delta = 2/9`, and the absolute lepton scale. CKM-side
  Koide support is package-captured but does not close charged-lepton Koide.
- **Critical open science lanes:** hadron masses, atomic scales, non-top quark
  masses, neutrino quantitative closure, Hubble constant closure, and
  charged-lepton mass retention are tracked in
  [`docs/lanes/open_science/README.md`](docs/lanes/open_science/README.md).
- **Bounded companions:** Higgs/vacuum, down-type mass ratios, neutrino
  observable bounds, proton lifetime, neutron EDM continuation, taste-scalar,
  gravitational decoherence, compact-object/cosmology, and related rows remain
  useful only with their stated bounded or conditional qualifiers.
- **Historical/comparison programs:** mirror, ordered-lattice, generated
  geometry, action-law, coin-walk, controls, and moonshot lanes remain in
  [`docs/lanes`](docs/lanes/README.md) for provenance and comparison.

## Validation

Use the publication package's validation path:

1. [REPRODUCE.md](docs/publication/ci3_z3/REPRODUCE.md)
2. [DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md](docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md)
3. [RESULTS_INDEX_EFFECTIVE_STATUS.md](docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md)

For audit status, run:

```bash
bash docs/audit/scripts/run_pipeline.sh
```

That refreshes the ledger, queue, generated publication effective-status views,
divergence report, and front-door status snapshot.

## Boundaries

This repository does not claim that every publication-captured row is already
audit-retained. It also does not claim that Record alone derives probability,
measurement, arrow of time, selector weights, or physical observable
identification. The explicit non-claims and qualifiers live in:

- [Inputs and qualifiers](docs/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md)
- [What this paper does not claim](docs/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)
- [Publication/audit divergence report](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md)
