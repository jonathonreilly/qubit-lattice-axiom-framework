# Focused fixed-order original-C residue check

Disposition: PASS conditional on the complete fixed-order outgoing-resolvent and pole construction invoked in the draft. The source normalization, elimination orders, and residue scaling are consistent. This is not a microscopic response or detector-identification theorem.

## Actual local source, rather than transferred observable coefficients

Use U H U† and C'=U C U† with the checked homological sign. For the all-up reference v and an E8 state a, (S1)_av=V_av/(8Jz) when V includes the transverse energy coefficient. Therefore

 [S1,C]_av=(C_v-C_a)(S1)_av.

A single transverse edge flips two sites in one longitudinal layer. Each flipped site changes two distance-two longitudinal ZZ terms from +1 to -1, so C_a-C_v=-8. Thus the first dressed E8 source is V|v>/Jz, with the appropriate explicit lambda removed from V when using dimensionless coefficients. This uses only the local generator's vacuum-to-E8 matrix element; extra QQ rotations in a different E8 canonical construction cannot change it.

For C/sqrt(Nphysical), actual XX amplitudes are -1 and YY amplitudes +1 on the uniform reference. With the normalized even-relative-coordinate vector d=(delta_ex+delta_-ex-delta_ey-delta_-ey)/2, summing translated physical edges gives -sqrt(2) lambda d. This agrees with the physical-bit normalization check; the thin-tube value 2 lambda must not replace it. Centering C changes only the vacuum component at this order.

An ell=2 slow state has two non-neighboring columns on two layers. On each layer a transverse edge word connecting those two flipped sites needs at least two edges. Hence at least four native edges are required. Products/commutators in source dressing contain the same number of transverse flips as their perturbative order; longitudinal projectors and denominators do not reduce this requirement. Direct q_S thus vanishes through second order (indeed through third for these states). Closed states have non-neighboring columns and ell>=3, requiring at least six edges. The draft's weaker O(lambda³) bounds are safe. Fixed-order connected source coefficients have bounded relative-coordinate support after COM reduction.

## Elimination and the fast-source limit

The closed-source contribution is H_SC R_C q_C=O(lambda³ lambda^-2 lambda³)=O(lambda4), with Jz cancelling. The leading fast contribution is lambda² times the dimensionless fast resolvent contraction because H_SF carries Jz lambda², R_F,physical carries (Jz lambda)^-1, and q_F carries lambda. Higher vertices or source terms give O(lambda³ log) using the assumed finite-local-resolvent bound. This remains true when a larger but fixed source support is retained.

The checked leading vertices are v_A=F0d/2=-d2-e and v_D=-2e. For the complete real symmetric coefficient operator, transpose symmetry and R_F F_lambda=zR_F-I give exactly

 v_A^T R_F d=[z R_dd-1-((F_lambda-F0)d)^T R_F d]/2.

The correction vector is O(lambda) with fixed support. The assumed corrected-arm strip theorem and the fast-host logarithm give the rank-one coupled values R_dd=O(1), R_ed=1/2+O(1/log(1/lambda)). Finite contact corrections O(lambda) change local entries by O(lambda log²(1/lambda))=o(1), preserving bounded R_dd. Hence v_A^T R_F d tends -1/2 and v_D^T R_F d tends -1. Multiplying by -sqrt(2) gives u0=(A+2D)/sqrt(2). The stated source error O(1/log+lambda log²) is sufficient; it is not a power-series error O(lambda).

Other leading slow boundary components are absent by the two-edge support classification. Their higher-order coefficients contribute o(lambda²) to the effective source. This conclusion specifically uses the outgoing strip estimates with the actual confined fast arm. It must not be extended to a pointwise real-energy limit, where narrow fast-arm structures may invalidate the same source limit.

## Endpoint residue and physical units

The slow arm couples to A with hopping -1, so its effective endpoint source is -lambda² u0^T G_s A+o(lambda²). The sign disappears upon taking its bilinear square, but is consistent before squaring.

For a frozen analytic endpoint parameter Sigma, the NN Airy pole satisfies E=-2+alpha f^(2/3)+f[2+Sigma/(1+Sigma)]+O(f^(4/3)), uniformly holomorphic in Sigma on a fixed neighborhood away from -1. Differentiation by Cauchy estimates yields the endpoint Riesz entry

 P11=dE/dSigma=f/(1+Sigma)^2+O(f^(4/3)).

Thus this is a complex Riesz residue, not an endpoint modulus-square. The previously checked localized contour estimate bounds the range-two perturbation's P11 correction by O(f^(4/3)). Fixed-endpoint polevector ratios remain bounded. The higher finite contacts and energy dependence must use the synthesis's localized/Cauchy estimates: for example a slow-unit boundary correction O(lambda log) on a disk of radius order f has derivative O(lambda log/f), whose product with P11=O(f) is o(1). Generic global projector-norm control alone would not establish this endpoint assertion.

These facts give

 Res_C = lambda^6 [u0^T G_s(-2) A]^2 / [8(1+Sigma0)^2] + o_m(lambda^6).

The numeric complex coefficient quoted in the draft is the prior slow-host computation; this review independently checks the analytic prefactor and scaling, not a new decimal quadrature. The transpose square is correct for analytic continuation of a real symmetric source resolvent. Its complex or negative real value is not a positive spectral weight.

If Ephysical=Ebase+Jz lambda² e, then (Ephysical-Hphysical)^-1=(Jz lambda²)^-1(e-h)^-1. The conversion of (e-e_p)^-1 back to (Ephysical-E_p)^-1 cancels that prefactor. There is consequently no additional Jz lambda² multiplying the pole residue.

The result concerns the supplied transformed reference, chosen normalization, finite-order coefficient operator, and its controlled continuation. It neither controls an exact microscopic pole nor resolves real-axis averaging or original-source identification with empirical matter.

Checked draft: /private/tmp/neutral_fixed_order_source_root.md. Reused the independently established bulk-source, slow-source, K4 gauge, and Airy endpoint controls. No repository edits or formal audit.
