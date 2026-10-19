<!-- Owning original: PR9753; source SHA256 ed17ec394e769d0ac94892ecdf71cbc622884009af892e858fa10ac0a0bceff8. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Range-two Airy perturbation and boundary restoration check

Checked 2026-10-18. Scope: steps 2–4 of `/private/tmp/neutral_range_two_airy_root.md`, taking the stated uniform NN Bessel/Airy expansion as input. The argument is valid for the specified coefficient model. The points below make the non-Hermitian estimates explicit.

## Contour bounds

Choose the radius-c epsilon^2 contour enclosing just the first Dirichlet level and uniformly separated from all other Dirichlet levels. The Airy-scaled Weyl expansion on this contour gives g_D=-1+O(epsilon). Its derivative is O(epsilon^-1) by Cauchy on a slightly thickened contour avoiding poles. This derivative is NOT the positive quantity ||R_D e1||^2 at nonreal energy; use the spectral/dissipative identity separately.

For imaginary part comparable to epsilon^2, the Weyl bound and Im g_D=-Im(E)||R_D e1||^2 give ||R_D e1||^2=O(epsilon^-1). Near the real points of the contour the same bound follows by moving the comparison energy by an imaginary amount O(epsilon^2): spectral denominators at the original energy are uniformly comparable to those at the shifted energy because the contour is separated from the Dirichlet spectrum by c epsilon^2. This avoids dividing by a vanishing Im(E).

For frozen complex Sigma in a fixed sufficiently small neighborhood of Sigma0, excluding -1,

    R_NN=R_D + Sigma R_D P1 R_D/(1-Sigma g_D),
    1-Sigma g_D=1+Sigma+O(epsilon).

The denominator stays bounded away from zero. Hence the full resolvent norm is O(epsilon^-2), and both its right endpoint column and left endpoint row have norm O(epsilon^-1/2). Complex symmetry supplies equality of these row/column norm bounds; Hermiticity is not assumed. The rank-one correction has norm O(epsilon^-1), so contour integration gives ||P_NN-P_D||=O(epsilon). Both projections have rank one; their difference has rank at most two, giving trace-norm control O(epsilon) as well. This is what is needed to estimate Tr(P V), rather than treating P_NN as an orthogonal projection.

The endpoint projection obeys (P_NN)_11=O(epsilon^3): its contour integrand g_D/(1-Sigma g_D) is a constant plus O(epsilon), and the constant integrates to zero over a contour of length O(epsilon^2).

## Bounded range-two perturbation

Let delta=lambda^2=8epsilon^3 and V be the stated bounded fixed-range operator, including any fixed supported bounded F. Since delta ||V||=O(epsilon^3) is smaller than the contour gap epsilon^2, the resolvent Neumann series converges uniformly. Analytic perturbation yields a unique simple eigenvalue inside the contour and

    E_delta=E_NN+delta Tr(P_NN V)+O(delta^2/epsilon^2).

The remainder is O(epsilon^4). This statement applies to the non-self-adjoint frozen boundary operator because its resolvent/projection bounds, not a self-adjoint eigenvalue ordering, control the expansion.

For the normalized Dirichlet Airy ground state, kinetic deficit 2-<T>=O(epsilon^2). The corresponding second-neighbor deficit is O(epsilon^2) as well, from a two-step difference bound; fixed endpoint amplitudes give O(epsilon^3) weight. Thus <V>=d+2a+2b+O(epsilon^2)=109/96+O(epsilon^2). The trace-norm projection difference then gives Tr(P_NN V)=109/96+O(epsilon). Its possible imaginary part is only O(epsilon), hence contributes at O(epsilon^4). The leading lambda^2 shift is real.

## Restoring energy-dependent Sigma

The draft correctly identifies that a generic O(epsilon) projection estimate is insufficient for endpoint weights. The localized resolvent expansion fixes this:

    |e1^* (R_delta-R_NN) e1|
      <= const delta ||e1^* R_NN|| ||R_NN e1||
      =O(epsilon^2)

uniformly on the large contour; higher Neumann terms gain O(epsilon). Integrating over its O(epsilon^2) length gives Delta P_11=O(epsilon^4). Therefore the perturbed P_11 remains O(epsilon^3), uniformly for frozen Sigma in the neighborhood.

For a simple non-Hermitian eigenvalue, the analytic derivative with respect to Sigma is Tr(P P1)=P_11; this uses the normalized biorthogonal/Riesz projection and is not a squared ordinary eigenvector amplitude. Since Sigma(E)-Sigma0=O(epsilon^2), its effect on the pole is O(epsilon^5). The nonlinear fixed-point derivative is O(epsilon^3) when Sigma'(E) is bounded, so the implicit equation is locally invertible. This proves the restoration step with the correct analytic projection convention.

Consequently, conditional on the NN turning-point input, the specified infinite-arm range-two model has the claimed expansion with slow-unit O(epsilon^4) remainder. Converting units gives physical O(Jz lambda^(14/3)). The fixed scaled numerical truncation still serves as a finite control, not as the proof; the proof above uses the infinite arm/controlled contour.

## Added corrected-fast self-energy

Suppose the already derived additional boundary function deltaSigma(E,lambda) is holomorphic and O(lambda/log(1/lambda)) uniformly on a disk of radius c f around the range-two pole, lying strictly in the lower strip. The pole's nonzero negative imaginary part is order f, so choose this disk from the previously established pole before inserting the correction; there is no circular assumption.

The frozen-Sigma derivative bound |partial E_eig/partial Sigma|=O(f) persists uniformly. Therefore the perturbation of the scalar eigenvalue equation is O(f lambda/log). On the original radius-cf disk, Cauchy gives |partial_E deltaSigma|=O(lambda/(f log)) on a smaller concentric disk. Multiplication by the eigenvalue derivative O(f) makes the induced fixed-point derivative O(lambda/log), small. Rouché or contraction thus gives a unique nearby pole displaced by

    O(f lambda/log(1/lambda)) in slow units,
    O(Jz lambda^5/log(1/lambda)) in physical units.

This is smaller than Jz lambda^(14/3), so it does not spoil the stated remainder or the leading width coefficient. Uniform holomorphy on the full disk, not merely a pointwise strip estimate, is essential. The earlier corrected-fast Schur argument supplies exactly this type of input within its model scope.

Conclusion: steps 2–4 and the proposed corrected-fast addition are sound with the explicit local Weyl/contour and holomorphy inputs. Do not interpret non-Hermitian P_11 as a positive spectral probability, or extend the result to unretained native channels, full Schrieffer-Wolff remainders, or measured source weights.
