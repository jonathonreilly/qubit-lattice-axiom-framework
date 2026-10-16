# Scalar inverse and observation-input bounds: review handoff

This is the self-contained first scientific milestone of the active
observations-backward derivation campaign. It is conditional support, with no
new empirical test or physical action selection. The campaign remains active
until its fixed 2026-10-16T22:36:59Z deadline; packaging begins at 22:21:59Z.

Canonical source: `docs/SCALAR_OBSERVATION_INVERSE_AND_INPUT_BOUNDS_NOTE_2026-10-16.md`.
Primary computation: `scripts/scalar_observation_inverse.py`, importing
`scripts/scalar_observation_inverse_math.py`. These re-establish the scientific
scope without running archived campaign scripts or reading prior results.

The source derives a relative-field inverse conditional on identified ideal
clocks/radar/orbits/radius; a joint primitive-input error bound including the
shared clock dependence; and a weighted radar-bin lower bound. Known stress
gives affine field transport. Explicit local dust and separate global-domain
examples show where boundary and action choices enter. They are existence
constructions, without claims about all theories, stability, or the observed
universe. Single-metric action reconstruction is acknowledged prior art.

The review branch will contain only the canonical source, executable inputs,
paired evidence, focused integration check, these milestone records, and the
generated citation manifest. Earlier exploratory drafts, all independent
source histories and failed attempts remain preserved on the separate campaign
checkpoint branch `codex/observations-backward-derivation-20261015`, including
commit `74f9132b33a259a01a950f5928f154c71519cbf3`. They are provenance, not
undeclared dependencies of the milestone. The primary checkout is untouched.

No initial state, bounded history, absolute scalar scale, physical potential,
common field-range overlap, or actual environment measurement bridge has been
selected or derived. No value was fitted; synthetic controls are exposed
development mathematics. Previously exposed external data remain development
material; no unopened observations were inspected for this milestone.

Next science: derive the coupled scalar/metric/material response of a fixed
action member, specify a realizable forcing/readout and boundaries, and ask
which residual parameter it measures. Do not vary rho0, k or C inside the
action when perturbing material density. V''/Z alone is not a physical mass,
and a stationary central derivative does not make Box F vanish.

Focused conformance and review evidence is in `MILESTONE_REVIEW.md` and
`independent_integration/`. Shared integrated-tree pipeline/strict-lint/evidence
validation remains a hard landing condition. The author lane opens a review
PR and does not merge science or apply any audit verdict.
