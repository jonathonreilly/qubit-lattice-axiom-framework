# Native motion and readout share the same large-feature amplitude

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_large_feature_mobility.py](../scripts/native_large_feature_mobility.py)

The existing one-qubit Hamiltonian determines an exact relation between the neutral coefficient mode's longitudinal curvature and its leading original-readout weight. Both are proportional to its root probability, and both shrink as delta log²(1/delta) near the large-feature threshold. No extra interaction or coupling constant is introduced.

The coefficient branch has positive curvature in all three directions sufficiently near threshold, although it has nonzero velocity and becomes strongly anisotropic. It is not a stationary rest state or a relativistic scalar. Its energy also lies above the sharp global four-wall coefficient infimum-8, so energy minimization has not selected this large-feature momentum.

The proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9778/LARGE_FEATURE_MOBILITY_PROOF.md`) derives the exact identity, parameter-derivative control, Hessian limit and global energy comparison. Independent checking and cavity/finite-graph controls support these conditional coefficient statements. Full-H positive spectral weight was established separately; full-H dispersion, physical identification and empirical tests remain open.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
