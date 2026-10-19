# Original-readout response near the large-feature threshold

Status: bounded-support. The native large feature and its neighboring
continuum appear in one derived response of the original bond readout.
For a smooth compact energy test F, the normalized microscopic ground-state
response tends to

\[
F(-1)+\int_0^\infty\frac{F(s)}{(\log s)^2+\pi^2}\,ds.
\]

Here `s=(H-Eg-8J-J lambda Eh)/(J lambda delta)`, the response weight unit is
`lambda² W0 delta log²(1/delta)`, and `W0=.025744944098352...` is derived from
the native source. This holds in the stated growing-cube weak regime with
`delta=lambda^alpha`, `0<alpha<1/3`. The atom at `s=-1` is a scaling-limit
statement, not an isolated microscopic pole at finite lambda.

The proof (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9785/THRESHOLD_READOUT_PROOF.md`)
starts from the exact native root resolvent, proves convergence of positive
spectral measures across the threshold, and transfers smooth response
functions to the actual Hamiltonian by controlled finite-time comparison.
It does not require preparation of a selected bound vector or an added
interaction. The shrinking binding energy still sits near a rest excitation
energy `8J`; large size has not produced a light cosmological scalar.

[Replay](../scripts/native_threshold_readout.py) checks coefficient-graph
resolvents and broadened complex response. At `b=.2`, the imaginary profile
normalized by the actual coefficient residue agrees with the limiting
profile below `1.4e-9` relative error. The critical asymptotic residue still
differs by about six percent there and is reported separately. These are
coefficient calculations, not microscopic many-body numerics or measured
spectra. Independent math (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9785/INDEPENDENT_THRESHOLD_READOUT_MATH_CHECK.md`)
and microscopic-transfer (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9785/INDEPENDENT_THRESHOLD_READOUT_PHYSICAL_CHECK.md`)
checks support the stated scope.

The Hamiltonian, weak regime, momentum path, physical units, ground
preparation and measurement identification remain assumptions. This is
exposed model development, without observational fitting, independent
empirical validation, a lifetime, or a universal scalar/matter coupling.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_threshold_readout.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
