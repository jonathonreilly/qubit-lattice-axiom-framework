# Signed cosine activities: a shifted-source comparison candidate

Author derivation, independent review pending. This is an abstract Gaussian
integral lemma with checked quantitative hypotheses, proposed as a replacement
for a positive-Fourier-type step. It is not a representation theorem for the
massive determinant-coupled compact model.

Let Q be a positive definite real matrix on a finite-dimensional vector space
V. Let B:V->R^r have rows b_j, and let z_j be real with |z_j|<1. Put

    v_j(u)=-log(1+z_j cos u),
    eta_j=|z_j|(1+|z_j|)/(1-|z_j|)^2,
    R=diag(eta_j),
    I(theta)=integral_V exp(-a.Qa/2) product_j[1+z_j cos((Ba)_j+theta_j)] da.

Terms with z_j=0 can be deleted. Every integrand is strictly positive, and
v_j is smooth and even. Direct differentiation gives

    v_j''(u)=(z_j cos u+z_j^2)/(1+z_j cos u)^2,
    |v_j''(u)|<=eta_j.

Assume the explicit matrix inequality B^* R B<=delta Q for some 0<=delta<1.
The action for the normalized a-integral has Hessian at least (1-delta)Q,
uniformly in theta. All derivatives and integrations by parts are justified
by the Gaussian tail and the bounded periodic factors.

For a phase-direction h in R^r, differentiating the integral gives

    D^2 log I(theta)[h,h]
       =-E sum_j v_j'' h_j^2 + Var(sum_j v_j' h_j).

The variance is nonnegative, proving the lower bound -h.Rh. For the upper
bound apply Brascamp-Lieb in a. With D=diag(v_j''),

    Var(sum_j v_j' h_j)
       <=(1-delta)^(-1) E h.D B Q^(-1) B^* D h.

The hypothesis implies ||R^(1/2) B Q^(-1/2)||^2<=delta. Thus
B Q^(-1) B^*<=delta R^(-1), and D R^(-1) D<=R. Therefore

    -R <= Hess_theta log I(theta) <= R/(1-delta).             (S1)

Evenness under (a,theta)->(-a,-theta) gives grad log I(0)=0. Integrating
(S1) along the segment from zero to theta yields the all-source ratio bounds

    exp(-theta.Rtheta/2) <= I(theta)/I(0)
       <=exp(theta.Rtheta/[2(1-delta)]).                     (S2)

Negative activities are explicitly allowed. The upper ratio may exceed one;
positive Fourier type, which would force the upper ratio to be at most one
for the pure shift integral, is not assumed or concluded.

## Mixtures and distinct current/source maps

Suppose an ACTUAL generating function admits a finite or convergent positive
mixture representation

    M(h)=exp(h.Gh/2) [sum_gamma c_gamma I_gamma(U_gamma h)]
                           /[sum_gamma c_gamma I_gamma(0)],
    c_gamma>=0,

where every I_gamma has the preceding form, each B_gamma^*R_gamma B_gamma
is <=delta Q_gamma with the same delta<1, and

    U_gamma^* R_gamma U_gamma <=epsilon G

uniformly in gamma. The source map U_gamma need not equal the current map
B_gamma; replacing it by B_gamma without proof would be an error. The
normalized weights c_gamma I_gamma(0) are positive and sum to one. Applying
(S2) separately before summing gives

    exp[(1-epsilon)h.Gh/2] <= M(h)
       <=exp[(1+epsilon/(1-delta))h.Gh/2].                   (S3)

If epsilon<1, differentiation at h=0 proves a strictly positive lower
covariance comparison and a finite upper comparison with G. Uniform
integrability or finite-dimensional analyticity must justify differentiation
for an infinite mixture; it follows, for instance, from the displayed
uniform Gaussian moment-generating bounds in a neighborhood of zero.

This is a sufficient consumer for a renormalized-current expansion. It
requires positive mixture coefficients, uniformly small weighted current
forms AND source forms, and exact equality for the generating function.
A partition-function identity alone is insufficient, since the local
Gaussian integration used to renormalize currents can change inserted
observables. A signed fermion-loop expansion does not automatically supply
positive mixture coefficients merely because the original determinant
weight is positive. These are still actual-model proof obligations.

## Source comparison and normalization audit

Frohlich-Spencer IHES/P/81/40 pages 47-51 use a Gaussian completion of the
source, a positive-type upper bound in equation (2.99), and a renormalized
activity/area estimate for the lower bound. The present abstract lemma tests
an alternative upper step with explicit Hessian assumptions; no source
normalization constant is imported.

The preprint's pages 35-37 also make clear that the renormalized current is
of the form rho_bar=rho-delta d h_B, so delta rho_bar=0 when delta rho=0.
It therefore still admits a plaquette filling. However the phase introduced
by a source shift uses the original rho. This is precisely why the two maps
B_gamma and U_gamma above are distinct.

A direct one-variable conditional Gaussian check is required before importing
any numerical activity exponent from that preprint. In conventions with
conditional action n(a+c)^2/(2 beta),

    E[exp(i rho a) | rest]
       =exp[-beta rho^2/(2n)] exp(-i rho c).

The displayed preprint exponent on pages 35-36 appears to differ by a factor
of two in these conventions; its page 50 also has an apparent sign typo in
the definition of the positive decay parameter. The published 1982 version
has not yet been recovered for comparison. Treat these as source-normalization
questions, not a refutation of the theorem; derive and check all constants
in any adaptation directly. None of block 2's existing results relies on
those numerical exponents.
