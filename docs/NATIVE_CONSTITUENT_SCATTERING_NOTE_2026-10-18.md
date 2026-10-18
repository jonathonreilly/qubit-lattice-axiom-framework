# Native constituent scattering and the open composite-stability question

**Status:** bounded-support.
**Primary runner:** [scripts/native_constituent_scattering.py](../scripts/native_constituent_scattering.py)

The same one-qubit Hamiltonian that binds the large neutral feature determines a nonzero collision amplitude for its two constituent flips. Eliminating the existing interval rays gives an exact finite-rank scattering formula; it does not require adding an attractive potential or fitting a coupling. This is constituent scattering in the four-wall coefficient sector, not scattering between two completed composite features.

For the oriented relative-lattice Fourier convention, the near-threshold amplitude is

    t(E_edge + s delta + i0) = -1 / { c(b) [log(s) - i pi] } + o(1),
    c(b) = 1 / (8 pi sqrt(b)),   s > 0.

Here delta is the native bound-state gap and b is the already selected COM parameter approaching its critical value. The exact bound equation fixes the logarithm's scale. No separate contact-coupling constant enters. The amplitude is direction independent on shrinking elliptical shells, but that relative-coordinate result does not establish a Lorentz scalar or isotropic composite propagation.

The [derivation](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_CONSTITUENT_SCATTERING_PROOF.md) includes the missing-origin hard-core term, the native ray self-energy and the retarded branch. Its limiting optical identity is Im(t)=-pi c|t|². In normalized inversion-even half-shell states the amplitude is 2t and the density is c/2; changing just one of these factors would be wrong. No physical cross section is quoted.

The [finite-time comparison](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_SCATTERING_TIME_PROOF.md) controls microscopic evolution of prepared compact-channel energy-band packets over times O(1/(J lambda delta)), with norm error O(lambda/delta). A closed-ray spectral gap gives uniform interval-length moments by a Sylvester semigroup estimate. This uses a periodic host with clamped short rays and a separate physical embedding; it does not assert an all-up interval-length bound on the entire finite physical spectrum. An infinite-time microscopic S matrix and the separate incoming/outgoing wavepacket limits remain unproved.

There is also an explicit [four-singleton breakup channel](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/TWO_FEATURE_BREAKUP_CHECK.md) at the energy and total momentum of two near-threshold composites. This prevents using an absent-continuum argument for their stability. Energy overlap alone gives neither a decay matrix element nor a lifetime; the two-window ladder remains valid.

Controls compare the exact finite coefficient-graph resolvent with the scattering formula (nine cases, error below 2.2e-14) and complex-energy lattice Green functions with the logarithmic limit. The latter are broadened development controls, not a direct numerical test at i0. The original Hamiltonian, weak-coupling family, selected momentum, state preparation, units and physical measurement identification remain conditional. No observed data were fitted or independently tested. The logarithmic two-dimensional scattering form is not claimed as a new universal law; the result is its explicit derivation from this native graph and its existing bound scale.
