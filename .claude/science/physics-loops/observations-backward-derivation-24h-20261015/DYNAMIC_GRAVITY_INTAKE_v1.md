# Dynamic-gravity intake: next measurement route

The Lee torque-table calculation is preserved as conditional development
support. Its full apparatus prediction remains unestablished: missing per-run
geometry and covariance are not supplied by the successful kernel identities
or by the shape-cone optima.

The next route is to inspect a primary experiment with deposited time traces.
This follows the physical calibration/response obligation, rather than adding
another noiseless toy reconstruction. It does not assume that changing source
position creates independently registered scalar-field environments.

| Candidate | Available evidence inspected | Decision |
| --- | --- | --- |
| Westphal et al. 2021 | Primary publisher-indexed availability statement says data on reasonable request; abstract and some figure captions exposed | Do not contact authors. No public primitive archive verified in this lookup. |
| Brack et al. 2022 | ETH repository index lists XML and figure spreadsheets; paper reports a dynamic beam coupling measurement | Useful fallback. Actual array and primitive-channel contents uninspected. |
| Fuchs et al. 2024 | Primary abstract and availability summary; public Zenodo API returns eight lock-in trace files at labeled source positions | Inspect measurement and calibration model next, then freeze a raw-file access protocol. No trace file has been opened. |

The [Fuchs preprint, version 2](https://arxiv.org/abs/2303.03545v2)
and [public dataset](https://zenodo.org/records/10300430) are the selected
intake. The repository's eight filenames vary height and lateral position.
Their labels do not establish the force transfer, measurement units,
independence, or applicability of a scalar model. Published aggregate outcomes
and abstracts are already exposed; a later reanalysis cannot be called an
unseen physical prediction.

The [Brack dataset](https://doi.org/10.3929/ethz-b-000533207) and
[primary paper](https://www.nature.com/articles/s41567-022-01642-8) are the
fallback if the chosen trace products cannot supply the necessary channels.
The [Westphal primary paper](https://www.nature.com/articles/s41586-021-03250-7)
is a measurement comparator, not a source of raw inputs in this block.

The pre-access task is to identify which quantities are instrument readings,
which are calibration fits and which already use a gravitational model.
Derive a geometry/response prediction conditional on those measured channels
before selecting any scalar potential or initial state. Classify calibration,
development and reserved raw-record checks explicitly; keep published-result
exposure visible. Do not claim an independent empirical test from an exposed
summary or from replaying an experiment's own fitted reference law.

Operational web failures are recorded in `DYNAMIC_GRAVITY_INTAKE_PLAN_v1.json`.
Ordinary public curl retrieved the Zenodo metadata after a local Python TLS
certificate-chain failure, with certificate verification left enabled.
The original failure and successful metadata receipt are both preserved.
No scientific conclusion follows from those retrieval failures.
