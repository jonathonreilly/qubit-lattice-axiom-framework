# Lattice-Qubit-Admissibility-Record Framework

This repository contains the public scientific package for a four-axiom
discrete-physics program:

1. **Lattice** — physical sites are the points of the cubic lattice `Z^3`,
   with nearest-neighbor adjacency, standard translations, and proper cubic
   rotations about each site. No site is privileged.
2. **Qubit** — each site has a domain of local possibilities whose full
   one-site algebraic presentation is `M_2(C)` (equivalently, real
   `Cl(3,0)`). No possibility is privileged.
3. **Admissibility** — one fixed nearest-neighbor rule, covariant under the
   lattice motions, determines the available possibilities at each site;
   availability varies with the nearest-neighbor conditions.
4. **Record** — records form. When present, a record locks exactly one
   admissible local possibility; a site never carries more than one record;
   records are permanent. Only records are readable, and scalar readout is
   additive over finite disjoint record collections.

The canonical axiom memo is
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](docs/MINIMAL_AXIOMS_2026-06-29.md).
It is edited in place only under explicit owner approvals, each recorded in
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](docs/audit/AXIOM_MINIMALITY_POLICY.md)
section 6. The earlier three-axiom base (Lattice, Quantum, Record), the
`Quantum` axiom name, and the still older `A1`/`A2`/`A3` numbering are
historical; new repo surfaces use the four names above unless quoting an
older document.

Beyond the axioms, the complete foundation surface is deliberately small:

- **Approved primitives (3):** the scale reference `a^{-1}` (units only),
  kinetic isotropy `c_t = c_s` (regulator graining), and the realized-state
  interface (a slot for one law-admissible realized state, never a state
  selection). Registered in
  [`docs/audit/data/axiom_premise_nodes.json`](docs/audit/data/axiom_premise_nodes.json).
- **Open derivation obligations (2):** the AC occupancy statistical grain and
  R-eta h-class/h-unit readout. They carry zero premise weight and are tracked
  in [`docs/audit/data/derivation_obligations.json`](docs/audit/data/derivation_obligations.json).
  Superseded admission-era decisions are non-authoritative provenance in
  [`docs/audit/data/premise_decision_history.json`](docs/audit/data/premise_decision_history.json).
  There is no admission registry or third supplied-premise class.
- **Scope condition (not a premise):** the past-hypothesis low-entropy
  magnitude; results that need it are explicit conditionals.

Everything else — probability and Born weights, measurement and readout
contexts, record-formation rules (which admissible possibility a new record
locks, at which site, with what weight, at what rate), dynamics and time
metric, kinetic branch selection, source/action structure,
physical-observable identification — is downstream content that must be
derived through retained-grade work or added through explicit axiom/approved-
primitive review before it can bear load. That discipline is what the audit
ledger enforces.

## Read First

Use these entrypoints in order:

1. [Generated front-door status snapshot](docs/repo/FRONT_DOOR_STATUS.md)
2. [Minimal axiom memo](docs/MINIMAL_AXIOMS_2026-06-29.md)
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

The repo remains in an audit-transition state. The 2026-06-29 foundation
reset from the three-axiom base to the four-axiom base invalidated every audit
that rested directly on the old axiom text; the premise-hash guard enforced
that reset. Some direct `minimal_axioms` dependents have since received
post-reset audits, while many remain unaudited or in progress. A much larger
legacy cohort still predates the reset, but those rows are not automatically
axiom-dependent: their scoped ledger entries and citation edges determine
whether re-audit is required. The generated
[`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md) always has
the current counts, refreshed by `bash docs/audit/scripts/run_pipeline.sh`.

Source notes and publication tables still contain legacy `retained` /
`promoted` wording, but the publication-facing authority is the audit-derived
`effective_status` in
[`docs/audit/AUDIT_LEDGER.md`](docs/audit/AUDIT_LEDGER.md). Retained-grade
`effective_status` values are `retained`, `retained_no_go`, and
`retained_bounded`; boxed `decoration_under_*` rows are decorations under a
retained parent, not independent retained rows. `promoted` is
publication-capture language, not an audit `effective_status`. Treat any
source-note or manuscript wording as proposed unless the effective-status
view marks the cited authority retained-grade.

Older notes that state or cite the three-axiom base are being brought current
under a staged narrative scrub
([`docs/repo/FOUR_AXIOM_NARRATIVE_SCRUB_PLAN_2026-07-04.md`](docs/repo/FOUR_AXIOM_NARRATIVE_SCRUB_PLAN_2026-07-04.md));
until that completes, read pre-2026-06-29 axiom descriptions as historical.

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
closures. The catalog predates the 2026-06-29 reset; its falsifier thresholds
and named external comparison bands stand, but quote it with its stated
conditionality rather than copying a number bare.

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

- **Framework baseline:** Lattice, Qubit, Admissibility, and Record are the
  named axiom surface. Admissibility constrains which possibilities are
  available at each site; it supplies no dynamics, probabilities, kinetic
  branch, or observable identification. Record names formation at occurrence
  strength ("records form") but remains deliberately narrow: it supplies no
  formation rule, Born weights, measurement dynamics, physical persistence
  dynamics, source/action identification, or downstream selectors by itself.
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
audit-retained. It also does not claim that the four axioms derive
probability, measurement, arrow of time, selector weights, kinetic branch
selection, or physical observable identification. The explicit non-claims and
qualifiers live in:

- [Inputs and qualifiers](docs/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md)
- [What this paper does not claim](docs/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)
- [Publication/audit divergence report](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md)
