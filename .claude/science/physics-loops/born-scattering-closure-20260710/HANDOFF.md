# Handoff

## Checkpoint 1

The worktree is cleanly isolated on
`physics-loop/born-scattering-closure-block01-20260710`, based on fetched
`origin/main@d8728888f`. The legacy cooperative lock script is absent, so the
run uses degraded branch-local isolation.

Grounding found a decisive current-surface change relative to the old target
packet: the literal first-order detector-centroid observable now has an
independently audited exact signed-adjoint edge representation. Two related
negative boundaries are also independently audited clean. A positive
plane-wave/Gaussian eikonal bridge must therefore reproduce the signed adjoint
functional; merely matching its four-point slope is insufficient.

Commands completed:

- fetched current `origin/main`;
- read all physics-loop instructions and required grounding surfaces;
- extracted the current audit rows for the target and lensing dependencies;
- read the target runner, adjoint identity, finite-path no-go, long-path
  falsifier, and centroid-multipole no-go.

Imports newly exposed:

- the old 3D correction is not produced by the target runner and is not a
  derived detector observable;
- the Gaussian angular average is incoherent ray averaging, while the literal
  harness propagates coherent complex amplitudes and differentiates a detector
  centroid;
- the four minimal axioms do not supply any of the dynamics, source, beta, or
  detector choices needed for a positive numerical theorem.

Exact next action: derive and implement a no-target-input discriminator for
the ray/eikonal model class versus the exact adjoint centroid functional,
including the scale-covariance test under `L -> rho L` at fixed source fraction.

## Checkpoint 2

The discriminator and note revision are complete before adversarial review.

New decisive results:

- the endpoint-matched plane-ray shape changes by `0.282053262` when the supplied path
  doubles;
- the independently rebuilt literal adjoint shape changes by `0.002093528`;
- the old 2D and 3D Gaussian angular weights are positive at an interior
  zero-impact pole where `I_ray~2/b_eff`, so the ordinary beam expectations do
  not exist;
- the primary runner contains no target exponent and reports `PASS=12 FAIL=0`.

Artifacts:

- `docs/BORN_SCATTERING_COMPARISON_NOTE.md` — bounded negative result with an
  exact Gaussian pole subtheorem;
- `scripts/gaussian_beam_eikonal.py` — target-constant-free analytic and literal
  finite-harness certificate;
- `logs/runner-cache/gaussian_beam_eikonal.txt` — paired successful output.

Imports retired from the negative-boundary proof: the separately supplied
`-1.43`, the open dispersion label, and the historical 2D/3D beam slopes.
Remaining positive blocker: an analytic reduction of the signed-adjoint edge
law and a derivation of the supplied harness choices from a stronger authority
surface.

Exact next action: apply the review-loop skill to the changed source note,
runner, cache, and loop pack, then fix/demote all findings before certification.

## Checkpoint 3

Review-loop iteration 2 passed after correcting the literal detector endpoint,
fully exposing the supplied fixture, failing the incomplete runner mode closed,
fingerprinting all load-bearing helpers, and separating the exact pole theorem
from the bounded floating-point discriminator. The final full replay reports
`PASS=12 FAIL=0`; analytic-only reports five skips and exits `2`.

Exact next action: run the repository audit pipeline in a detached temporary
worktree for validation only, then package one branch-local review PR. Do not
apply an audit verdict or merge.
