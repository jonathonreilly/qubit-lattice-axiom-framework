# Checks and review history

Launch grounding: main skill/source revision recorded in STATE.yaml; isolated worktree and cooperative lock verified. Current source physics-loop is used instead of the stale installed copy, with the user's explicit permission to build/test new assumptions controlling the discovery scope. Source review/audit are separate from author calculations.

## First calculation blocks, 2026-10-12

| Block | Author evidence | Focused independent evidence | Boundary |
|---|---|---|---|
| Finite-source force/light/radiative response | gravity/spectral_probe.py; 13 checks pass | Independent 35-digit potential differentiation and dispersion calculation; all 15 compared values agree; three deliberately wrong alternatives rejected | Synthetic geometry witness, not a Cassini fit or full GW likelihood |
| Common positive scalar mass continuum | gravity/scalar_continuum_probe.py; 40 checks pass | gravity_measurements_extra.md, original runtime scalar_continuum_check.py/results; oscillator, frequency and Schwinger plateau integrals agree; root read full proof/source/results | Supplied free vacuum, shared current and apparatus; no empirical selection |
| Finite canonical local approximations | gravity/finite_local_probe.py; 207 checks pass | Independent derivation and computation assigned, pending | Analytic absolute error guarantees are distinct from numerical relative accuracy |
| Clock filter and moving neutrino bridge | agents/neutrino/GAUSSIAN_MEDIATOR_CLOCK_AND_NEUTRINO_BRIDGE.md | Independent agent derived normalization and integrated in two coordinate systems; root read note, raw code read still pending | Longitudinal coherence cannot distinguish symmetric classical noise from the matched quantum covariance |
| Joint composition/clock and Sun comparison | Assigned agent has frozen model and code/results | Separate agent reconstructing primary MATLAB estimator and injection response | Published-summary compatibility remains conditional; primary-script normalization/response issue under investigation |

Runtime gravity/*freeze*.json pins each root contract and runner before its
execution. The original independent gravity receipt pins all comparison sources.
Raw downloads, full logs and original independent programs remain in the runtime
directory. Passing controls do not count as separate physical discoveries.

No full branch science-review pass, conformance certification, empirical
discovery, or formal audit is claimed. Before a milestone PR, build the
reproducible packet, run relevant source/runner/citation checks and independently
review the consequential new claims with the exact raw evidence.
