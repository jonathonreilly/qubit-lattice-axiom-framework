# Matched finite-population curvature: publication handoff

This milestone supplies a reproducible finite numerical comparison for a
specified 864-state ring component. A fixed 1024-replica design preserves the
canonical preparation, three fields, projection ages and complete covariance
across populations 64, 128, 256 and 512. The held population is compared with
the prespecified three-population fit. This reduces ambiguity in what the
estimator measures; it does not establish its infinite-population law, a size
trend or a physical photon prediction.

Publication base: current main `30a9461ee19a49b99fa6628fe942f08e504e8903`,
verified September 30, 2026. The mathematical parent and its runner are
byte-identical to the completed experiment's closure. Prior PR9354 was closed
after reviewed incorporation into main; this delta adds only the new finite
population experiment and its complete executable source. No prior closed PR
is reopened. No new statistical sample has been added during publication.

Science source: `docs/RING_COMPONENT_MATCHED_POPULATION_CURVATURE_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-09-27.md`.
Primary: `scripts/ring_component_matched_population_curvature_2026_09_27.py`.
Imported local implementation: `scripts/ring_matched_population_kernel_2026_09_27.py`
and `scripts/ring_matched_population_reference_2026_09_27.py`.
The parent is `docs/FINITE_PROJECTION_MIXED_ENERGY_AND_CURVATURE_TARGET_BOUNDED_THEOREM_NOTE_2026-09-27.md`.

Reproduction: from this checkout run the primary through
`scripts/runner_cache.py` `execute_and_write_cache` with declared timeout14400.
The final literal-envelope run completed September 30 at 07:25:37 UTC,
2666.325 seconds, exit 0 and empty stderr. Its primary source has only one
trailing-whitespace correction relative to the September 27 composition check;
the parsed AST is identical. A fresh canonical cache binds that changed hash.
The full output has64 progress rows to1024 and
a final complete result. All880 numerical summary fields, complete covariance,
matched reference and replica-means digest exactly match the original fixed
confirmation. Cache SHA256:
`2c2eadebe0344d8ad0d24cbd0e5ac6c59680f71583eaa73b4eaf36a3130c94a8`.
The full 65 JSON objects were compared against the September 27 run: all
scientific fields are exactly equal; only the final elapsed time differs.
Input fingerprint:
`8d32678b85ad86f2e745533ee3df728d24aaab9f7f4d299637fa4ecbf1af0c15`.
Raw arrays remain private recovery evidence; the public runner regenerates all
needed data, optionally retaining it with `--retain-raw PATH`.

Independent checking used a distinct coordinate/plaquette construction of the
component and sparse evolution of the matched reference, then scalar-fsum
replica averages, explicit covariance sums and normal-equation reconstruction.
The extraction plan was frozen before exposing primary summaries;865 numeric
comparisons agree within5.9e-14. The public composition check covers the exact
source carried here up to the verified AST-identical whitespace repair;
861 comparisons agree within1.6e-14. It does not constitute
an independent new stochastic sample or physical experiment.

Six mutation families were rejected in separate scratch comparisons: guide
exponent, field diagonal, replica SE, field covariance, held population and
age window. Some rejections use frozen independent fixtures, not intrinsic
public-runner assertions. No claims depend on the later private systematic
resampling diagnostic, which is not included in this PR.

The physical preparation, observable/detector identification, units, volume
limit and finite-population error control remain open. No supplied guide,
normalization or coupling is claimed to be an unfitted physical prediction.
No mass/cosmological inference, audit verdict or science merge is authorized
by this publication. Combined landing validation and independent source
review remain separate from author checks.

## Family evaluation

OPEN. This finite numerical experiment adds a distinct missing comparison to
the earlier exact path/projection/Rayleigh identities. Those identities
identify an exact-distribution target and one-walker boundary but do not
supply the finite-population behavior of the implemented resampling protocol.
The new evidence holds preparation, fields and ages fixed, retains the full
replica covariance and evaluates a population held out of the fixed fit.
That is additional computational evidence, not a relabeling or a new physical
interpretation of the same matrix identity. The independently checked geometry
and extraction establish what is being compared while leaving extrapolation
and physical identification unproved. The full small-component construction,
source protocol and reproduction are carried in one note and three source
files. One combined review can therefore inspect the complete new experiment
and its uncertainty interpretation without following a sequence of support-only
PRs. The previous estimator PR has already been incorporated into main; a
single incremental milestone is a coherent review unit. This author judgment
governs opening the PR only and grants no scientific audit status.

## Next scientific obligation

Bound the complete recursive normalized finite-population curvature functional
for the actual generated ordering and establish the physical preparation and
source-to-detector map before using size comparisons as physical evidence.
