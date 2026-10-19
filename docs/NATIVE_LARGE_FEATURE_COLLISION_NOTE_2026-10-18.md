# Native collisions of large neutral features

Claim type: bounded_theorem.
Primary runner: `scripts/native_large_feature_collision.py`

Status: bounded-support. The original one-qubit Hamiltonian gives a nonzero
on-shell contact/Born numerator between two large neutral features and a
compatible four-constituent free channel. No interaction is added. This is
not yet an exact scattering amplitude or a decay rate.

The proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9782/LARGE_FEATURE_COLLISION_PROOF.md`)
derives the contact residual from forbidden cross-pair spin hops, including
the native vertical-ray inputs. For the previously derived near-threshold
feature, the unnormalized-COM 24-permutation convention has
`K/u² -> positive constant`, with a certified lower bound above `2.58914`.
The root weight `u²` vanishes as `delta log²(1/delta)` while the feature radius
grows as `delta^(-1/2)`. Large size therefore does not make the unscaled
collision strength remain finite. Supplemental quadrature estimates the
scaled limit as `51.0521`; the proof of positivity does not use quadrature.

[Replay](../scripts/native_large_feature_collision.py) includes the critical
interval certificate, arbitrary-complex native-spin and permanent checks,
an exact-anchor physical-bit control, and supplemental bounded quadrature.
Independent physical (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9782/INDEPENDENT_LARGE_COLLISION_PHYSICAL_CHECK.md`)
and mathematical (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9782/INDEPENDENT_LARGE_COLLISION_MATH_CHECK.md`)
checks pass for the stated coefficient result.

The supplied Hamiltonian, weak-coupling regime, selected momentum family,
state preparation, physical scales and connection to measurements remain
premises. The next obstruction is distorted four-body dynamics and its
transfer to the microscopic Hamiltonian. No cosmological scalar,
source/detector bridge, lifetime or empirical success is inferred. All
calculations are exposed model development, with no calibration dataset or
independent observation test.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
