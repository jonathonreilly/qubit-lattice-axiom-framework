# A positive full-H spectral contribution from the large neutral feature

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_large_feature_microscopic_window.py](../scripts/native_large_feature_microscopic_window.py)

The neutral large-feature calculation extends beyond its first-order coefficient graph. In the supplied weak one-qubit Hamiltonian on even cubes of side proportional to lambda^-4, choose the derived binding gap delta=lambda^alpha, with0<alpha<2/3. For every actual microscopic ground state, the original normalized Fourier bond readout has positive weight at least lambda² W0 delta log²(1/delta)[1-o(1)] in a window of half-width J lambda delta/4 around J[8+lambda Eb]. Here W0 is the previously derived source coefficient.

The proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9777/MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md`) bounds higher native coefficients on the extended feature, transfers its trial vector across the actual ground manifold, and uses a positive spectral projection inequality. No additional interaction or phenomenological readout coefficient is supplied. Exact128-site bit controls check plane covariance and disjoint background supports; they are not128-qubit diagonalization or a numerical full-H spectral test.

This is a lower bound allowing additional spectral weight, not an isolated microscopic band, pole or lifetime. Momentum selection, supplied Hamiltonian, ground-state regime, lattice units and physical interpretation of the diagnostic remain assumptions. The feature grows spatially but its readout weight shrinks and its excitation energy stays near8J. No observations were fitted or independently tested, and no cosmological or gravitational scalar is identified.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.
