# Focused four-column competition review

Disposition: PASS for the conditional leading coefficient model, finite numerical evidence and auxiliary small-K/t droplet expansion, subject to the narrow frozen-checkpoint provenance clarification below. No repo edits, audit verdict, or heavy replay performed. Reviewed HEAD69bf1e3b365d77238b4931d60f9d772e45314a4c plus working candidate; parent short replay remains a separate gate.

Read the complete note/aggregate, native coefficient-model/charge/momentum/microscopic scripts and provenance; reused INDEPENDENT_FOUR_COLUMN_COMPETITION, QUOTIENT, CHARGES, DROPLET and COLUMN_SOURCE_ALL_LENGTH checks. The droplet check was independently derived earlier in this same reviewer session. All source/result hashes currently in PROVENANCE.json verify.

## Mathematical and claim assessment

The L4 return classification correctly adds complete pair-column flips to the local fourth-order plaquette calculation. It excludes other nonconstant operators by spin-flip count, scalar folded terms and transverse circumference>4. The note avoids asserting an even-power remainder on odd-period tori. The direct16-spin control checks both full polar-aligned operators, not just a selected coefficient.

The readout identity C4=(3/Jz)H4+(3lambda4/128)sumP is algebraically correct. It separates the conserved uniform Hamiltonian contribution from the inelastic uniform plaquette contribution, includes direct source dressing, and does not transport that decomposition uncritically to finite q. The fixed-L all-length derivative proof retains the crossed Wick term and uses free solvability only at source parameter zero; its leading-coefficient versus full finite-g distinction is explicit. The resulting q0 physical weight is the square of3lambda4/128 times the normalized plaquette weight, with the per-physical-site factor1/4 correctly stated.

The full coefficient computations retain all defect numbers in an explicitly selected subsystem sector. Normalized plaquette fibers and, on even-even tori, the additional global-Z restriction are supported by independent full-space intertwining controls. The charge model correctly uses affine row/column constraints. Its coordinate-array dot product is the matrix element of the declared boundary seed, not an overlap of orthogonal physical charge sectors. Static DeltaC and DeltaE conversion formulas are consistent with K=9Jz lambda4/64. No force law, statistics, apparatus or gravity identification is inferred.

The auxiliary droplet coefficients, connected cancellation, positive25/48 curvature and weight1 were independently confirmed earlier. K/t=9/8 is explicitly outside that small-K/t control; finite native-ratio coefficient-model spectra are kept separate. The table entries and residuals inspected agree with frozen JSON. Finite positive momentum shifts are not called a measured continuum curvature. Unresolved Ritz nodes and visible size dependence remain preserved, and no infinite-grid pole or global-sector ground certificate is asserted.

Open ends, selected state/sectors, supplied anisotropy, and finite column length remain explicit premises. In particular the note does not rename the open slab as a finite object already embedded in an uncut bulk. That limitation is material and appropriately points to the next calculation.

## Frozen input clarification

neutral_four_column_momentum_six.py loads /private/tmp/neutral_four_column_gs_6x6.npz. This checkpoint is not included in PROVENANCE.json and the current reproduction paragraph does not describe how to produce it. Add the ordered native-ratio recipe: run neutral_four_column_model_v2.py 6 6 32, which generates the checkpoint, then neutral_four_column_momentum_six.py 6 6. State its ratio8/9 and dependency, and record the original checkpoint hash if retained. This does not require shipping the large NPZ or another heavy replay. Hashes of source/output alone do not identify an undeclared input checkpoint.

The short aggregate honestly distinguishes live5x5/local/microscopic controls from frozen5x6/6x6 outputs. It verifies their declared hashes and does not falsely report large reruns. The optional zip comparisons could assert matching row identities/counts for future robustness, but no present row mismatch was found.

## Source hashes
- `docs/NATIVE_FOUR_COLUMN_COMPETITION_NOTE_2026-10-18.md`: `9b7f9210d6378c5b35e32d62145aae377077e5d61f97cb89556b3ba9fb6d293e`
- `scripts/native_four_column_competition.py`: `becd7d23818e38b6cc04434bf0aad8c8a266f6aed385fd6ba3685f95ed83b68b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/PROVENANCE.json`: `db617f5c9a188723cfc26b2647564e84abe173673fab1d57168ec5272a4349b5`

## Same-session affected-fix confirmation

Confirmed the manifest now declares the6x6 checkpoint, original SHA256, native ratio and ordered generating/consumer commands; the canonical note gives the same recipe and numerical-regeneration caveat. Independently checked the retained original NPZ against its declared SHA256: match. The uncommitted checkpoint can be regenerated from supplied source, while original identity is preserved. Final focused disposition: PASS, no remaining required scientific or provenance fix. Parent source-bound replay and publication mechanics remain separate.

Final affected hashes:
- `docs/NATIVE_FOUR_COLUMN_COMPETITION_NOTE_2026-10-18.md`: `9b7f9210d6378c5b35e32d62145aae377077e5d61f97cb89556b3ba9fb6d293e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/column_four_results/PROVENANCE.json`: `db617f5c9a188723cfc26b2647564e84abe173673fab1d57168ec5272a4349b5`
