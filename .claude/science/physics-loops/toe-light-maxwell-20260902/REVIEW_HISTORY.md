# Review history

## Preregistration

- Current main and open PR ownership checked through PR #7833.
- Five-lens independent panel: 5–0 conditional GO for Lane 8A with compact
  monopole and anisotropy controls.
- Independent portfolio dissent: the pure-gauge `beta=6` normalization pair
  may have larger downstream blast radius; queued as the next block.
- Review-loop: deliberately not invoked, per explicit user instruction.
- Direct conformance review: pending implementation and fresh runner output.

## Post-execution value review

- Implemented the exact compact identities, nonlinear Wilson variation,
  smooth refinement, Euclidean kernel, Gauss Schur reduction, transfer-pole
  distinction, anisotropy, zero-mode, and authority guards.
- Final candidate runner result before discard: `PASS=30 FAIL=0`.
- Independent hostile review caught and corrected a material draft error: the
  four-dimensional Euclidean Hessian has one gauge null plus three positive
  directions. Two local transverse modes arise only after Gauss reduction at
  nonzero spatial momentum; torus zero modes remain separate.
- Independent novelty review found the decisive value issue: after supplying
  the Wilson action, the bridge uses standard mathematical machinery and does
  not require framework-retained primitives.
- Fresh ownership/main check remained at
  `36fe57a7a784df31bc2178c4b94dfc7caaa5d094`, open through PR #7833; no
  Maxwell owner appeared. Ownership was clear, but V1 and V3 still failed.
- Disposition: candidate source note, runner, and cache deleted; no PR. The
  next block attacks gauge-action/normalization selection itself.
- Review-loop remained disabled by user instruction.

## Preservation recovery

- The owner directed that every scientifically interesting result be placed on
  remote for review/classification regardless of audit or parent ordering.
- Draft PR #7840 was opened immediately with the surviving campaign packet.
- Git objects, reflogs, session memory, and temporary paths were searched. The
  deleted files had never entered a commit or staged object, so their exact
  bytes were unavailable.
- The source and runner were reconstructed from the exact target plus two
  independent session derivations. The corrected rank-three Euclidean quotient
  and rank-two Gauss-reduced local sector are explicit.
- Fresh reconstructed result: `PASS=30 FAIL=0`; the old output is not reused as
  evidence.
