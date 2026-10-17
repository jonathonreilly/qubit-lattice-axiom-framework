# Distinct check: common-mode scalar source

Verdict: conditional support; no necessary correction found in the frozen source. The result is a normalized isolated scalar packet family indexed by the supplied common source offset Delta. It does not establish closeness to a fixed zero-offset target or performance of an attached processor.

The complete target was read and its changed arguments reconstructed. The relative-coefficient source was refreshed in full; the unchanged scalar source and distinct checks are reused within their previously read scope. Exact identities appear below.

## Changed determinant and domain

The eliminated uniform-ray Weyl function must be m_j(Delta+y), on the physical branch (as fixed in the cited scalar premise), while the three finite source factors use y-r_i. Equation (1) has precisely this form. Replacing it by m_j(y) would be invalid.

With zero residual perturbations, the constant-load determinant is (y+i lambda)^3: expanding (y^2-lambda^2/3)(y+3i lambda)-(8lambda^2/3)y verifies every coefficient. The exact difference is -3lambda[j m_j(Delta+y)+i](y^2-lambda^2/3). On the physical band, |j m+i|^2=2(1-s)<=delta^2/j^2. Dividing the resulting bound by R^3 uses lambda/R<=1 and |y|/R<=1, giving beta=3(eta+|Delta|/j). Thus both real and imaginary changes of the physical load are included.

The three-factor perturbation costs 4[(1+epsilon)^3-1]R^3; the two bond-square products cost 4(2epsilon+epsilon^2)R^3 in total. Their sum is exactly (20epsilon+16epsilon^2+4epsilon^3)R^3. The same estimates hold for the shifted load because its band modulus is unchanged. At the domain corner beta<=.84375 and B<=.1004005, so alpha<=.9441505<1 and chi_Delta<1. These are validity margins, potentially giving very large error bounds; the proposal correctly does not call the entire domain high fidelity. Non-strict determinant inequalities include endpoints and zero residuals.

## Exterior spectrum and normalized density

For either exterior halfline, y has the physical exterior sign and |y|>=7j/4, so lambda/|y|<=1/56. Reverse triangle bounds give

    |D_Delta|/|y|^3 >= 1-3/56-3/56^2 > .945.

This reasoning uses absolute values and remains valid for negative y without invoking an absent common-Delta oddness. The exterior perturbation costs at most B(1+1/56^2)^(3/2)<.101 in the same units. It cannot cancel the nominal determinant. The argument therefore excludes exterior zeros separately from the interior margin.

The finite Jacobi resolvent is algebraic with nonzero determinant on the band including thresholds and on its exterior. Regular band values, bounded threshold behavior, and its seed 1/z asymptotic yield exactly the displayed absolutely continuous measure with mass one. The nonzero bonds make the seed cyclic. Thus no atom or singular component is silently discarded for this isolated scalar system. This conclusion does not concern an attached finite core or its additional channels.

## Retarded coefficient, residual ratio and normalization

The last-source cofactor is a1 a2; multiplying it by the negative source-ray hopping and m_j=-exp(iq)/j gives the positive coefficient kappa a1 a2 exp(iq)/(jD). With F=i(2j sin q)A/sqrt(2pi), direct squaring gives |F|^2 dq=rho ddelta. In particular the full packet has norm one and its first-site phase i exp(iq) is retained.

The positive numerator ratio differs from one by at most nu. The denominator ratio differs from one by at most chi_Delta. Consequently (nu+chi_Delta)/(1-chi_Delta) is a valid pointwise complex relative error, yielding the full norm ceiling min(2,L_Delta). Fourier isometry, time multiplication and physical-halfline restriction preserve this traveling-component estimate. Incoming conjugation preserves its norm without conjugating physical time evolution.

On a common retained band the raw difference is at most L_Delta times the nominal retained norm; the normalization difference costs the same again. This proves min(2,2L_Delta), assuming nonzero retained packet mass. A common transmission/Jacobian preserves the relative statement wherever its retained mass is positive. It does not supply an actual feedback-loaded device row. Local source amplitudes and full-state performance are not implied.

## Cubic comparison and physical phase

Dividing F by sqrt(2j sin q) gives precisely the proposed energy amplitude. The nominal numerator is C=sqrt(8lambda^5/(3pi)); residual numerator ratio is n sqrt(s). Since sqrt(s)=(1-delta^2/(4j^2))^(1/4), 1-sqrt(s)<=delta^2/(4j^2). Together with the alpha denominator bound, this proves the central L2 estimate.

The cubic density has second moment lambda^2/3 and fourth moment lambda^4. Its odd moments vanish, so the fourth moment of Delta+y is Delta^4+2Delta^2 lambda^2+lambda^4. Its square root is exactly Delta^2+lambda^2, validating equation (7), including its denominator 1-alpha. This is a weighted numerator estimate, not a uniform small-delta assumption at the thresholds.

Outside the physical band, |y|>=2j-|Delta|. Integrating C^2/y^6 on both tails yields 16lambda^5/(15pi b^5), hence the proposed V_Delta. The full-line bound E_band+V_Delta follows by the triangle inequality. Restricting the cubic comparator and normalizing costs 1-sqrt(p_M)<=1-p_M<=V_Delta^2 on the band; no exterior norm V_Delta is needed again for this restricted comparator. Thus equation (9) is correct. The energy-to-q map is unitary with the stated square-root Jacobian and retains the physical phase.

The common unit-modulus phase, including its fixed exterior extension, cancels from the overlap. The Fourier density of the normalized cubic is proportional to t^4 exp(-2lambda t) on one time halfline. Integrating its frequency shift gives overlap modulus [1+(Delta/(2lambda))^2]^(-5/2), independently of Fourier-sign convention. The claim is only its modulus; it demonstrates why small Delta/j does not mean a small change relative to a zero-offset narrow packet. The physical time factor exp[-it(2j+Delta)] must remain and is not a global-Hamiltonian equivalence.

## Positive realization and limits

The domain gives kappa/j<.31, a2/j<.052 and |r_i|/j<=1/6400. These leave all listed occupation coefficients positive, including at Delta=-j/4. Ordinary bond Laplacians plus the occupations produce the specified source diagonals and uniform first-ray diagonal without a vacancy scalar. In the alternative structured port block, j+Delta+r2-a2 is positive and source compression retains j n_port. This establishes local algebraic realizability only.

The proposal correctly leaves shifted actual background windows, all-fiber complements, feedback, outgoing calibration, actual omitted spectral state, local recovery, temporal concentration and finite transfer unresolved. No selected-channel scalar estimate is promoted to a full processor inverse. The common offset is a supplied parameter defining a target family; unknown-offset fixed-target robustness, native precision supply and permanent storage remain outside scope.

## Exposure and verification limits

The author is distinct from this reviewer. I have authored and checked related attachment, traveling and reference ancestors in this campaign and have prior exposure to the nominal source and robustness arguments. Root requested this direction and read the target; neither fact is evidence for the result. I independently reconstructed the changed shifted-load margins, exterior exclusion, packet factors, weighted moments, normalization and overlap here. This is not a blanket independent recertification of the shared ancestry or a retained-status audit.

No numerical integration, pole computation, dynamics, sweep, scientific runner, Git/publication/checkpoint action, prompt/model modification or delegation was performed. Only this review was written; deterministic source hashes were verified.

## Exact identities

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.
- `three_site_product_source/PROPOSAL.md`: `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823`.
- `three_site_product_source_check/REVIEW.md`: `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`.
- `three_site_source_robustness/PROPOSAL.md`: `32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6`.
- `three_site_source_robustness_check/REVIEW.md`: `ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad`.
