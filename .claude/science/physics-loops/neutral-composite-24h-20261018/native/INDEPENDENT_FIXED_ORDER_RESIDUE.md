# Fixed-endpoint Airy residue and continued-source stability check

Checked 2026-10-18 against `/private/tmp/neutral_fixed_order_source_root.md`. Focus: the endpoint residue, finite-endpoint source errors, and energy-dependent corrections. This check takes the stated first source coefficient and the complete leading S-F vertices as inputs; it does not independently enumerate those microscopic source words.

## Endpoint residue normalization

For frozen Sigma in a fixed complex neighborhood of Sigma0 excluding -1, the uniformly analytic Airy eigenvalue expansion is

    E(Sigma)=-2+alpha f^(2/3)+f[2+Sigma/(1+Sigma)]+O(f^(4/3)).

Cauchy differentiation with respect to Sigma on a fixed parameter disk gives

    P_11=partial E/partial Sigma
        =f/(1+Sigma)^2+O(f^(4/3)).

Here P is the rank-one Riesz projection, not an orthogonal projection. The derivative identity is the analytic non-Hermitian Hellmann-Feynman identity Tr(P P1). Thus the denominator is (1+Sigma)^2, not |1+Sigma|^2. The latter would incorrectly turn this into a positive weight.

For any fixed endpoint n, the zero-energy-limit recurrence at the lower band edge gives

    u_n/u_1 -> t_n=n+(n-1)Sigma,

because u_0=-Sigma u_1 and u_(n+1)-2u_n+u_(n-1)=0. Hence the entire fixed-endpoint residue matrix has the limit

    P_ij/f -> t_i t_j/(1+Sigma)^2.

This establishes bounded endpoint ratios and an O(f) matrix bound, with constants depending on the fixed number of endpoints. It must not be extended to n growing on the Airy length scale without additional estimates.

## Range-two and higher bulk corrections

On the large baseline Airy contour each fixed endpoint column and row of the resolvent has norm O(f^(-1/6)); the first endpoint estimate extends to fixed n by the finite recurrence. A bounded perturbation delta=lambda^2=O(f) changes each endpoint resolvent entry by O(delta f^(-1/3)). Contour length O(f^(2/3)) then yields an endpoint residue change O(f^(4/3)). Higher Neumann terms are smaller. The full endpoint matrix therefore retains its leading limit, not merely the scalar 11 entry.

Higher bounded bulk terms and the small relative slope change preserve this conclusion under the earlier contour estimates. A generic O(f^(1/3)) operator-norm projection difference alone would NOT prove it; the localized row/column estimate is necessary and is available here.

## Small finite-endpoint and energy-dependent corrections

Write the baseline local Green matrix as A/(E-Ep)+B(E), with A=O(f), rank one, and bounded holomorphic B on the small lower disk. For a holomorphic endpoint correction Delta of uniform size delta=o(1), finite-rank inversion transforms the residue by bounded factors I+O(delta). The nonlinear pole normalization is 1+O(delta), because the pole shift equation's derivative is O(delta) after its O(f) residue multiplies the Cauchy derivative O(delta/f). Therefore the new residue matrix differs by O(f delta), apart from the already smaller bulk correction.

This applies to the full fast correction delta=O(lambda log(1/lambda)), even though its energy derivative itself need not tend to zero. The statement that the derivative contributes only o(1) is correct AFTER multiplication by the endpoint residue; a bare bounded-derivative assertion for the fast self-energy would be false. For the baseline analytic slow host, the derivative is O(1) and its normalization correction is O(f).

All of this uses the previously established lower disk and holomorphic bounds. It is not a claim about pointwise real-axis fine structure.

## Source smallness and coefficient

If the effective leading source after host elimination is lambda^2 times a fixed endpoint vector, its pole residue is order lambda^4 f=lambda^6/8. If all other components are o(lambda^2) uniformly on the disk and occupy a fixed endpoint set, every cross contribution is bounded by

    O(f) O(lambda^2) o(lambda^2)=o(lambda^6),

and their quadratic contribution is smaller still. There is no hidden amplification by a large endpoint ratio. The fixed-order finite-support qualification is essential: neither this bound nor the previous residue matrix estimate automatically covers a number of source sites growing with lambda^-1.

For an analytically continued source q(E), only its value at the pole enters q(E)^T R(E) q(E)'s simple-pole residue. Its derivative changes the regular part, not the leading residue. The left and right induced sources are transposes under the real symmetric microscopic/coefficient convention; taking an absolute square would be incorrect on this sheet.

With u0=(1,2)/sqrt2, G_s the given outgoing punctured-host matrix, and Sigma0=G_s,AA(-2), the stated coefficient is

    (1/8) [u0^T G_s(-2) A/(1+Sigma0)]^2.

I independently evaluated the provided host quadrature at -2 and obtained

    -0.03036208824144617 - 0.036385137901888555 i,

agreeing with the draft. This numerical evaluation checks the displayed value; the asymptotic control relies on the preceding analytic hypotheses.

The physical-energy change of variables introduces no extra Jz lambda^2 in the pole residue: the prefactor 1/(Jz lambda^2) of the resolvent cancels the same factor converting e-ep to Ephys-Ephys,p. The normalization of C and its first dressed source coefficient still need the independently stated microscopic check.

Conclusion: the proposed endpoint residue and robustness argument are sound for the specified fixed-order continued coefficient response, provided the source/vertex inputs and finite-support bounds hold uniformly. The negative complex real part is not a negative probability, and none of this provides an empirical detector or cosmological identification.
