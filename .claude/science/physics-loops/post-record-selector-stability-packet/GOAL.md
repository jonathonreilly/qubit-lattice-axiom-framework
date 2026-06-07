# Goal

Repair post-record runner-artifact blockers caused by missing helper-source
visibility and missing bounded row exports.

Targets:

- `post_record_stability_dynamics_selector_subdivision_2026-06-06`;
- `post_record_measure_weight_normalization_subdivision_2026-06-06`.

The branch also refreshes the immediate parent row-bucketing and selector/dial
counts because current `main` drifted from the earlier `90`/`44` target counts
to `97`/`45`.
