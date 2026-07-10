# Artifact plan

1. Revise the target note with an exact common-integral derivation and narrow
   dependency/status metadata.
2. Add one primary coefficient runner that:
   - validates SU(3) character conventions;
   - checks the deletion identity on exact/controlled surfaces;
   - runs independent periodic `L_s=3` Wilson chains at `beta=6`;
   - reports block-jackknife coefficient estimates and convergence diagnostics;
   - compares the actual-environment spectrum with the old single-link packet
     only as a falsifier.
3. Add a companion doubled-slice literal-factor-deletion matrix discriminator
   that preserves the compression/stripping-ordering blocker rather than
   claiming it is the algebraic residual quotient.
4. Add SHA-pinned stable caches for both runners.
5. Update this loop pack, run vocabulary lint and relevant target runners, then
   run review-loop before any PR.
