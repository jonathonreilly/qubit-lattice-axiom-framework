# Focused native neutral source-identification block review

Disposition: PASS for the conditional source-identification argument, following the declared-input fix below. This is a focused consistency/source review, not a formal audit or landing verdict. Root retains authorship. No repository edits or large replay were performed by this reviewer.

## Material finding resolved

The smooth-source probe reads stationary_spatial.json from the preceding milestone. The initial runner neither regenerated nor declared it, leaving a replay/provenance gap. Root added its exact path to AUDIT_INPUT_PATHS and explicitly stated the retained-data reuse in the canonical note. This is sufficient for an honest frozen-prior-output calculation; it is not an independent spatial-response recomputation. The final source-bound aggregate/cache rerun remains root-owned. The currently present aggregate at inspection still had 13 inputs (the preceding direct replay), so completion of the new 14-input artifact must be checked as an integration gate; I have not represented that rerun as complete.

## Argument and source checks

Read the canonical note, runner, eight new probe implementations, and independent scale, smooth-source, ladder, charge, protected-factor and nullspace reports. Existing sector/reduction/response sources were previously independently reviewed; the orchestration regenerates their NPZ state inputs before the ladder and charge consumers. The new scripts introduce no native Hamiltonian interaction.

The protected-factor conclusion follows from binary plane rank8 and restricted symplectic rank2: six central bits, one protected qubit, twenty multiplicity qubits. Neutral protocols depend only on the sector-indexed reduced multiplicity density matrices. Twirling preserves every neutral multitime product, but does not select the central weights/multiplicity state or justify charged-protocol equivalence. Protected-only degeneracy is dark to neutral operators. Minor wording precision sent to root: canonical 'plane Pauli algebra has dimension eight' should say 'binary plane-Pauli span'; the associative complex algebra has dimension256. The surrounding symplectic context makes the intended claim clear, so this is not a mathematical blocker.

The ladder calculation uses final energy relative to E0; its upper window at2Delta is therefore the positive transition atDelta from the chosen first mode. upper_over_2Z has harmonic target1. The four widths and synthetic anharmonic control prevent interpreting a narrow-window mismatch as a generic scalar exclusion. Nonlinear readout and interacting/multiple-mode possibilities remain outside this test. Window convergence is numerical evidence, not a spectral-completeness/error certificate. Root's full-H residual reconstruction is retained.

The mode-charge probe uses -(O_nn-O_00)/Delta. The three unequal summed-C ratios cannot be made equal by a single nonzero normalization; both reference and excited branch degeneracy conditions are explicit. This remains a diagnostic of chosen vectors and operators, not physical matter charges or an equivalence-principle test. The implementation's uniform_H_rescale_derivative=+gap corresponds to H(epsilon)=(1+epsilon)H, distinct from the minus-source differentiation convention; the independent report states that distinction.

The nullspace construction P_E[H,[H,A]]P_F=(E-F)^2 P_EAP_F is exact, including whole degenerate diagonal blocks. It establishes common FIRST-ORDER gap slopes without specifying off-block transitions; finite-lambda spectra need not rescale. For dimensionless A, alpha has inverse-energy units. Autocorrelation inelastic weights scale alpha² while cross response to a fixed second observable scales alpha. The detailed nullspace note now makes these distinctions and calls the thermal numerical statistic the full structure-factor inelastic weight, not a positive-frequency retarded weight. The local forward construction expands support at most two interaction neighborhoods; the spectral inverse is not claimed local or uniformly bounded. The 3x2x1 control uses bond-built partial composites directly and does not rely on extending a three-dimensional rectangular classification to a unit-length dimension.

Global J scaling is valid for J>0, fixed dimensionless state, and jointly scaled frequency/broadening; it does not keep beta fixed in physical units. The ratio v/Delta only has the stated pole-range meaning when such a pole/dispersion is established, which the detailed scale report explicitly qualifies. The canonical note does not infer a bulk gap from the finite one.

The uniform isolated retarded energy-source response vanishes for stationary rho because H is conserved. Smooth widening on this fixed cube is a Taylor expansion, not a simultaneous thermodynamic/long-wavelength limit. The actual Gaussian profile removes odd Taylor terms itself; the saved kernel's inversion symmetry is additionally checked numerically. Its remainder includes the small nonzero numerical uniform-source sum. Isothermal beta Cov(C,H) comes from re-equilibrating H_lambda=(1-lambda)H at fixed beta; the control compares the correct finite difference and distinguishes this protocol from isolated response. No Kubo covariance for a generic noncommuting source is silently replaced by ordinary covariance.

## Scope and integration

No scalar/gravity no-go, physical source/detector map, observed preparation, bulk persistence, or units calibration follows from these controls. The canonical note preserves those boundaries and identifies a positive next requirement. Existing independent mathematical checks are reused explicitly; no claim is made that this reviewer independently reran every numerical value. Root reports all ten direct probes passed; source-bound replay of the added frozen JSON input is the remaining integration check.

## SHA256 snapshot

- `docs/NATIVE_NEUTRAL_SOURCE_IDENTIFICATION_NOTE_2026-10-18.md`: `1d5ad69c30e3097e1b66deb953f025dce550e00f5e5f935905eec3b54e7364f9`
- `scripts/native_neutral_source_identification.py`: `4cbae368453a33912b4a688c106f2a731abb445f8811f26efc4fecf378e3ac44`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_scale_control.py`: `a0d8cedc183589d912cb3800c667d22211d14b5df2456a2628137763c7cba1d4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_smooth_source.py`: `2b858d3d839e0248dcbb388dfd6426eed13944ed805b391c977e884b82ce2802`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_ladder_control.py`: `7fcae4c5325aafd96d99f3eeb583b593e7c4cc8008ed5b119aea13b57231cd4f`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_ladder_probe.py`: `9b144b16327a2cef482791b3b06152740473d113bff885085130b0bb8c136f89`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mode_charges.py`: `86dc60791e853ecc0c5c0df561750b4670603a5d501861f501ce62aead54ae6d`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_plane_factor.py`: `8874877c80ca134f7d47ab81343b4e644782990c1e14081ad841d57f99e370c0`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_source_ambiguity.py`: `8f9b2c105a84ab1eeb948ea53fb141771d7c6dd172b1d8b27504722ec071503a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_thermal_protocol_control.py`: `4a3aab5d74db418a8d8a90c34f39c6ad622fc4523064eb8d15ca731822c2560c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/SOURCE_IDENTIFICATION_NULLSPACE.md`: `dc189131f8cdc8cac9584bcb06d29b824f881472fbbce3529d4c10aed2d0558e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SCALE_BOUNDARY_CHECK.md`: `c6072dc394727ea4d8291d836fe316748b180ef86d69259ac7c0e06bfbaa6624`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SMOOTH_SOURCE_CHECK.md`: `52e7bb470af3e72a981776f20d188f20040bbba0359f353048edc844d8c362a1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_LADDER_CHECK.md`: `160b792630284e98ebba44e5290274ee9e5fddd002b498b1cda8d786678c6a64`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_MODE_CHARGE_CHECK.md`: `37e70a6e4922906ce913621a26e9ebb2211214b4d357f631517f321d6f5b6a22`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_PROTECTED_FACTOR_CHECK.md`: `9c76b94cae91e4d20262d710fc66059877e9c04bfda597d6ff7c5207af9d97c7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SOURCE_NULLSPACE_CHECK.md`: `7114ac5d44036cd809f0a5bf140c5711c1f80174550a076c34d4f4dae4695ea3`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_spatial.json`: `aeacdea6dbbc76e6ad1233cc2db99fd7c819f3b96ea16256e9cf65f66317e3f4`
