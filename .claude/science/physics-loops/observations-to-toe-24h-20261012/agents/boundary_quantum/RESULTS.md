# Boundary-conditioned pair model: construction and limited data test

The proposed one-parameter law is normalized, gives exact fair no-signaling binary marginals, and makes an angular prediction different from the quantum cosine. No finite shared k reproduces that cosine. A released multi-angle polarization workbook permits a reproducible conditional comparison, but its instrument-coordinate definition and repeated-setting fluctuations prevent a clean experimental exclusion or a validated confidence interval.

This packet is exploratory research under the campaign's authorized alternative premises. It does not adopt an axiom, update the premise registry, claim novelty, or connect this pair model to the separate scalar force/noise construction.

## Source and exposure

The primary source is [Song et al., Nature Communications 16, 11429 (2025)](https://doi.org/10.1038/s41467-025-66258-x). Its [versioned data release](https://doi.org/10.6084/m9.figshare.30499499.v1) contains Figure4.xlsx, file ID 59204048. We use sheet Figure4d, the incoherently pumped H/D polarization coincidence scans. The primary figure labels counts per 20 seconds. The workbook supplies nineteen settings from 0° to 360° in 20° increments, counts, and error columns. Source methods describe a Φ⁺ preparation, polarization compensation, and a fiber polarization rotator/polarizer. They attribute count uncertainties to Poisson statistics. The published net visibility summaries were exposed during source discovery; they are not used as independent calibration data.

The pinned workbook SHA-256 is `dcb11e46c0e61d09a22d2ef6c6778e3afb0fc1b1f5bbe218581597c133950e15`, matching the release MD5 `a06482e7368e835d3ffd026c7366f9e8`. `SOURCES.json` records the local original workbook, main PDF, supplementary PDF, figure, version metadata and hashes.

`MODEL_PRE_DATA_FREEZE.json` was recorded at 17:50:47 UTC on 2026-10-12. The initial row split at 17:57:38 preceded measured-cell extraction, which occurred at 17:57:53. It treated the source coordinate as a physical analyzer angle. Inspection then showed four fringes over 360°, and the 360° values exactly repeat the 0° entries. The original freeze remains preserved.

`SOURCE_MAP_CORRECTION_PREFIT.json`, recorded at 18:01:00 before fitting, uses an inferred half-wave-plate-like map, physical analyzer angle β=2θ, and excludes the duplicated 360° row. The source methods available here do not explicitly verify that coordinate conversion. The revised calibration settings are θ={0,20,40,60,180,200,220,240}°. Test settings are the other ten settings below 360°. Nominal new absolute-dot-product levels occur at θ={80,100,260,280}°. Some revised test values had already been exposed in the first calibration extraction, and the full figure had been viewed. **This is an openly exposed public model-development holdout, with a revised pre-fit split. It is neither blind nor fully unexposed.** No test values were used to retune the frozen fitted parameters.

## Candidate and observation map

For c=a·b, θ_B=arccos c, and E₀=−1+2θ_B/π, the exact law is

    Z=cosh(kc)−E₀ sinh(kc),
    E_k=tanh[atanh(E₀)−kc], k≥0,
    P(A=u,B=v|a,b)=[1+uv E_k]/4.

The common k tilts a uniform unit-vector prior by exp(−kcAB). Its setting dependence is supplied explicitly. `PAIR_LAW_DERIVATION.md` proves normalization, marginals, relabeling and rotation consistency, limits, the finite-k endpoint cusp, and the limited independent-pair composition rule. A separate azimuth-sector integration checks the original sign-response law numerically to 1.34×10⁻¹⁵.

The conditional count map is

    μ_j(θ)=m_j[1+v_j C_k(2θ−α_j−φ_j)],
    C_k(δ)=−E_k(cos 2δ), α_H=0°, α_D=45°.

For each scan j, mean brightness m_j>0, visibility 0≤v_j≤1 and analyzer offset −10°≤φ_j≤10° are calibration-only nuisances. The fundamental k is common. This is an affine, stationary, angle-independent readout assumption. There is no independently supplied detector/visibility calibration. The data do not provide all four joint outcome counts, time tags, per-angle singles/accidentals, a selection model, or a published covariance matrix. We therefore use the listed errors only as weights and report descriptive weighted-square scores, not a raw Poisson likelihood or a fundamental-law significance.

The quantum cosine and k=0 triangular controls use the identical nuisance class, each estimated on the same calibration subset. The primary numerical search uses multiple starts over k∈[0,40]; additional fixed large-k checks are documented separately, without claiming a certified global search over the unbounded domain.

## Frozen prediction and its uncertainty

`CALIBRATION_AND_PREDICTIONS_FREEZE.json` stores source cells, fitted parameters, calibration residuals, parameter covariance, full shared prediction covariance, the profile grid and every forward test mean. Its receipt hash before full revised test extraction is

    0e4dc14ae089be908dcfcdc26c07dffa7c3bea57c50cc13b32b7d3a6ef2cf46e

The common boundary parameter is k=0.5337547856. Its fitted (m,v,φ) are H=(13765.573,0.920342,7.007738°) and D=(13281.266,0.941670,−2.813122°). No fitted boundary-model parameter is on its specified bound.

| Model | Calibration score (16 data) | Frozen test score (20 data) | Test score including local shared prediction covariance | Nominal new-angle score (8 data) |
|---|---:|---:|---:|---:|
| Boundary, 7 parameters | 207.563 | 1447.844 | 357.182 | 279.951 |
| Quantum cosine, 6 parameters | 230.711 | 420.641 | 303.738 | 233.113 |
| k=0 triangular, 6 parameters | 5480.587 | 14117.420 | 3502.282 | 6043.610 |

The fixed-parameter scores sum (observed−predicted)²/σ². The covariance score is rᵀ[D_test+J_test Cov_cal J_testᵀ]⁻¹r, retaining correlations between predictions caused by their shared calibration parameters. No held-out parameters are fitted. The triangular visibility parameters hit their upper bounds, so its local normal approximation is especially unreliable.

Under a *conditional independent Gaussian interpretation* of the listed errors, the boundary profile crossings at Δscore=3.841459 are [0.479987,0.591391]. This is a one-parameter profile curvature interval inside the assumed observation model, **not a validated 95% confidence set**. The calibration already fails that error/response model. A post-test sensitivity multiplies every listed error by 5.031827, inferred from equivalent-setting calibration differences; the corresponding profile crossings broaden to [0.314240,0.876449]. This alternative was selected after test exposure and assumes a common variance multiplier. It does not recover the experiment's systematic covariance or replace the original freeze.

## Why the data do not warrant an exclusion significance

For each equivalent-setting calibration pair at θ and θ+180°, any stationary angular response must assign the same mean. Minimizing over that mean gives the exact lower bound

    min_μ Σᵢ (yᵢ−μ)²/σᵢ² = (y₁−y₂)²/(σ₁²+σ₂²).

Summing the eight pair minima yields **202.554282**, regardless of the angular function. This nearly exhausts the boundary model's calibration score 207.563. For example, the D scan lists 17769 at 40° and 16124 at 220°, with a difference 8.94 times the combined listed counting error. All released error squares equal their associated counts to within 0.00145 count, consistent with rounded square-root errors. Those errors do not describe the observed repeated-setting consistency under the assumed coordinate map.

The cosine has a better frozen test score than the boundary candidate, and both outperform the triangular control. The comparison cannot by itself isolate a fundamental correlation law from coordinate interpretation, phase/brightness drift, angle-dependent collection, background subtraction or other count processing. A full likelihood, source/readout normalization, independently calibrated visibility and systematic covariance are the exact missing inputs. The scores must not be reported as exclusion sigma or p-values. The original data and primary-source claims have not been corrected or reanalyzed as an experimental result.

## Exact prospective discriminator

Use event-ready binary pairs, or fully record and forward-model photon detection/selection, with independent analyzer-angle and readout calibration. Under an independently checked common unbiased visibility map E_obs=V E, the endpoint θ_B=0 fixes V independently of k. Freeze k from a separate calibration at Bloch separation 45°. If that calibration is quantum-like, it gives

    k=[atanh(1/√2)−atanh(1/2)]/(1/√2)=0.4696142811.

Then hold out, without retuning, these distinct angle separations:

| Bloch separation | Linear-polarization axis separation | Boundary E | Quantum E | Difference |
|---|---:|---:|---:|---:|
| 15° | 7.5° | −0.9292081 | −0.9659258 | +0.0367177 |
| 30° | 15° | −0.8371040 | −0.8660254 | +0.0289214 |
| 60° | 30° | −0.5236682 | −0.5000000 | −0.0236682 |

The largest absolute ideal difference below 90° is 0.0381353 near 18.9236°. The endpoint law is also an exact discriminator: E_k=−1+(2/π)e^(−2k)θ_B+O(θ_B²), whereas the cosine has no linear term. Independently measured angular jitter must be convolved with both predictions, because it can round this cusp.

For a purely illustrative V=0.97 and negligible calibration error, the Bernoulli product-outcome KL divergence from a quantum-like distribution to this fixed candidate is 0.00385643 per trial at 15° Bloch separation. This is a prospective mathematical separation, not an observed likelihood. Endpoint and 45° calibration uncertainty must be propagated into the joint forecast; independent detector bias, missing events and angular uncertainty must also be measured. `SOURCE_DIAGNOSTICS_AND_PROSPECTIVE.json` records the numbers and explicit assumptions, and `prospective_discriminator.png` visualizes the prediction.

## Scope and reproduction

The pair law does not define sequential measurement updates, state preparations, general instruments, multipartite joint states or causal dynamics. A product law for separately independent pairs can be postulated. It does not follow for overlapping pairs or interacting systems. In particular, assigning singlet anticorrelation simultaneously to all three pairs of three equal-setting binary outcomes is inconsistent. This prices a missing extension, rather than proving that every extension is impossible.

Within the campaign's deadline and stop contract, `python3 boundary_pair.py calibrate` reconstructs the fit/predictions and `python3 boundary_pair.py test` evaluates frozen predictions; both read the original XLSX without altering it. The diagnostics scripts are explicitly post-test and do not change the primary fit. Re-running the first command overwrites the result packet, so preserve its existing hashes or run from a copied packet for independent reconstruction. Runners set numerical libraries to one thread and check DEADLINE and stop markers. No repository science/adoption surface, commit, remote branch or supervisor was changed.
