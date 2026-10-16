# Focused final-source check: conditional action reconstruction

No material discrepancy found in the final v2 theorem or its implementation within the declared conditional domain. One concrete control-coverage weakness was reported during this session: the earlier midpoint example did not detect omission of the Lipschitz term. The preserved v1 report records it. The narrow v2 correction supplies a sharp zero-noise example and resolves that specific coverage issue. This is a mathematical/source check, not a formal audit, novelty determination, empirical validation or integrated landing review.

## Final exact sources

- docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md: `980512d7d9a5fb2f19583fbdeb7e849d0861c0299a13fa52f7bf51a059acdd86`
- scripts/ringdown_action_inverse.py: `1be664a62d9c1656172aa4a45f48a5cc094212d9a2a3cc7d4dd88eaae0419047`
- scripts/ringdown_action_math.py: `834c82d633c4653a7feb6b05ecb28871e9c70364f5a7203f31accf7167f786df`
- logs/runner-cache/ringdown_action_inverse.txt: `fa83203bb47579b2a9d1fad50787f3507339bb817bae5ecd34714e0da2ba7d83`
- outputs/ringdown_action_inverse/controls.json: `ba6be1f8c017e89b71b97bd7559103dbd09c17b4b6cba79ad2a13823d84d3c6b`

Complete canonical note, primary, helper, control JSON and cache were read, together with both frozen-source manifests, extraction map and midpoint correction. READ_LOG.md records reading completion. PROOF.md is self-contained and records the prior independently derived formulas only after their correspondence with the complete canonical source was checked. No conclusion was transferred merely from an earlier pass count.

## Mathematical assessment

Direct variation gives the required force R=R0+Gz+k zddot+nu zdot+C' z²/2-tau' zdot²/2. The negative hidden-inertia gradient and the half-factor in complex harmonic extraction are essential. Reciprocal linearization at rest gives the same N(s)=G+nu s+k s² in both equations. Its dynamic-stiffness residue is -N(lambda)²/[tau(2lambda+Gamma)]. The mixed and second-harmonic coefficients then yield Q=O' and S=O'+(tau'/tau)(O-lambda²), so r is real tau'/tau. These formulas permit O'=0, tau'=0 and vanishing second harmonic; only the specified pole/fundamental nondegeneracies are needed.

The hidden translation F'=-k/tau removes kinetic cross coupling while retaining transformed Rayleigh coefficients. Congruence preserves the required positivity, including semidefinite dissipation. Observable force invariance relies on the zero hidden external force equation. In the reduced chart, integrating r, choosing a continuous nonzero square-root branch, recovering the real G/nu pair, checking complete polynomial response and static consistency, and integrating w0/E construct a representative. The curvature is R0'+G²/C, not simply R0'. With c=f/n, all supplied force coefficients and full six-mode histories are realized. Thus sufficiency concerns the ideal rest-response/clamped-ringdown surface, and not arbitrary moving histories. The stated connected-chart scale/reflection, translation and energy constants correctly characterize the remaining class-internal freedoms.

Nonaffine covariance requires the conjugate-force transformation and its analytic equilibrium correction -R0*j''/j'^3. Product/quotient bounds handle correlated complex errors with true-value margins. The canonical text explicitly makes the log-inertia path-error integral unsigned. The midpoint constant1/4 follows from integrating distance to each bin midpoint. Branch continuation, true error certificates, complete rational closure and between-point smoothness cannot be inferred from finite noiseless grids.

## Integration and independent computation

AST-normalized comparisons with hash-verified exploratory sources show precisely the four declared predicate strengthenings in the initial canonical helper: actual undamped rank loss, separately integrated unexcited force, recomputed phase-alternative Q, and differentiated nonaffine force transformation. No other mathematical expression or tolerance changed in that extraction. The helper is self-contained, imported directly by the primary, and does not execute the old campaign runners or read external scientific data.

Independent common_check.py passed268 checks and reconstruction_check.py passed418. These independent implementations use no author helpers and include contour-residue integration, separate matrix-exponential ringdown generation, variable-projection pole recovery, a different smooth reconstruction family, reflection/scale and nonaffine covariance, complex branch winding and deterministic correlated-error probes. Initial canonical integration_check.py passed24 additional checks, including zero-gradient admissibility, semidefinite damping and time-origin invariance. On final v2, the amended source-bound integration checker passed22 checks (two v1 metadata bindings are absent from the five-file v2 manifest), and six independent sharp midpoint cases passed. Their source-bound formulas are unchanged by the sole midpoint-control correction.

The full final primary was executed from a byte-identical private scratch copy under this directory with PYTHONDONTWRITEBYTECODE=1 and Python -B. Each subprocess used timeout120seconds. It passed195 controls. Generated controls.json was byte-identical to the canonical output, and stdout matched the canonical cache after excluding cache separator newlines. execution_receipts_v2.json and comparison_v2.json record results; all stdout/stderr are preserved. No independent computational run failed.

## Midpoint correction and historical disposition

The original frozen helper/cache/controls, scratch reproduction, bindings and REPORT_v1_pre_amendment.md remain intact. The actual v1-to-v2 helper diff adds a shared midpoint-bound function and one sharp integral control; the note and primary bytes are unchanged. For Q(x)=|2x-1| on[0,1], zero readout error gives midpoint0, integral1/2 and Lipschitz bound1/2. Removing the geometric term yields budget0 and is decisively inconsistent. Six separately quadrature-computed signed cusp cases at different widths/slopes corroborate sharpness.

All four historical gzip files in MIDPOINT_CONTROL_CORRECTION.json were checked against both their archive hashes and decompressed original hashes. The old mutation history remains bound to the old helper. Root reported23of24original mutations detected and a narrow corrected midpoint rerun; this report does not claim all24mutations were rerun on v2 and does not assess the full mutation campaign. control_delta_v2.json confirms only one new control and expected summary/source-hash changes; all prior detailed output values are unchanged.

## Measurement and scope limits

The action/Rayleigh class, one isolated real hidden mode, physical work-conjugate channels, common time and rest response are premises. No measured data enter this unit. The61 environment records are development data, including environments used earlier. Three new initial preparations at existing environments fit only two preparation parameters on the first60 samples, then predict the last541 with frozen local functions. The static-slope comparison uses the generator's analytic derivative solely as verification. These controls neither certify unseen-environment interpolation nor test general moving histories.

Noiseless dynamic-fit condition numbers reach roughly7.1e4. A practical finite-band/noisy experiment still requires pole/residue, phase, calibration, rest-contamination and model-discrepancy error certificates. The nearest-root finite-grid algorithm is not a universal continuation certificate or guarded inverse API. These limitations are explicit in the source. Prior-art citations were treated as provenance, not proof inputs, and were not independently reread in this no-network check. Current-main pipeline, strict lint, authority and landing gates were outside this scoped check.
