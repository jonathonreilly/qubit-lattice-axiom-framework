# Regularized neutral spectral filter — independent check

Let L be the self-adjoint free-bilinear Liouvillian in the chosen positive inner product, omega real, and let the source u have unit norm. Its normalized positive spectral measure is dmu(Delta)=<u,dE_L(Delta)u>, with integral dmu=1. For eta=epsilon²>0,

    w=[(L−omega)²+epsilon²]^−1 u = F(L)u,
    F(Delta)=1/[(Delta−omega)²+epsilon²],
    v=w/||w||.

This assumes the full operator space and the actual adjoint in the declared metric. It does not assume a discrete eigenmode.

Writing x=Delta−omega and I_j=integral F^j dmu, one obtains exactly

    |<u,v>|²=I_1²/I_2,
    ||(L−omega)v||²=integral x² F² dmu / I_2,
    <v,Lv>−omega=integral x F² dmu / I_2.

The second expression is the residual about the target omega. The variance about the optimized mean is that residual squared minus the square of the third expression.

## Interior smooth-continuum asymptotics

Assume omega lies in the interior of an absolutely continuous spectral neighborhood, with continuous density s(omega)=s0>0, no atom at omega, and no additional singular measure accumulating there. The source spectral measure is finite; bounded lattice spectra suffice for the remote parts. Then

    I_1 ~ pi s0/epsilon,
    I_2 ~ pi s0/(2 epsilon³),
    integral x² F² dmu ~ pi s0/(2 epsilon).

The required integrals on the real line are pi, pi/2 and pi/2 after x=epsilon y rescaling. Therefore the root's proposed limits are correct:

    normalized source overlap² ~ 2 pi s0 epsilon,
    residual² ~ epsilon²=eta.

Thus an arbitrarily small residual can be constructed from a smooth continuum while its overlap with a fixed normalized source tends to zero. Small residual alone is not a pole certificate.

If the density is C1 locally, with derivative s1=s'(omega), the odd numerator gives

    <L>_v−omega=(s1/s0) epsilon²+o(epsilon²).

The variance about the optimized mean still has leading epsilon²; subtracting the mean shift squared changes only smaller terms. Continuity alone does not justify this derivative coefficient.

These constants assume an interior two-sided neighborhood. At a one-sided smooth spectral edge, the overlap coefficient and the mean shift change: for support x>=0 with nonzero edge density, overlap²~pi s0 epsilon and mean shift~2epsilon/pi, although target residual²~epsilon². Singular densities, van Hove points, thresholds, or zero s0 require separate asymptotics.

## Atoms, finite grids and finite range

If the source measure has an atom of weight p>0 exactly at omega, I_1~p/epsilon² and I_2~p/epsilon⁴, so overlap²->p and the target residual vanishes. This detects source-visible point weight, **not necessarily an isolated atom**: a delta component can coexist with continuum at the same energy. Isolation needs an additional spectral-gap statement. An atom elsewhere does not produce this behavior at fixed omega.

On a finite momentum grid, the measure is discrete. If no grid energy equals omega, the eta->0 filter generally saturates to the finite inverse-distance-squared mixture; it does not obey the smooth-continuum asymptotics. If a grid energy equals omega, its artificial finite-grid atom controls the limit. The thermodynamic/continuum and eta limits must therefore be separated explicitly.

For a finite Fourier-support domain P_R with **full output retained**, the correct unweighted normal operator is

    P_R (L−omega)^dagger(L−omega) P_R + eta P_R.

Its inverse on the domain is not generally P_R F(L) P_R, because P_R need not commute with L. Therefore the pointwise filter and continuum limits are an infinite-support target, not an exact formula for a finite-range optimizer. Retaining full output avoids discarding boundary leakage; it does not remove the domain projection. Convergence in range R and momentum resolution must be checked independently before comparing eta scaling. Sending eta to zero at fixed R can be dominated by a finite variational floor.

## Thermal positive structure metric

For a fixed free equilibrium state, the connected bilinear structure metric is diagonal in transition coordinates:

    ||M||_S²=(1/N_c) sum_(k,a,b)
       f_a(k)[1−f_b(k+q)] |M_ba(k,q)|².

The Liouvillian multiplies the same coordinates by the real transition energy Delta_ba. Hence the weight operator commutes with L, L is self-adjoint in this metric, and the **full-space pointwise filter F remains unchanged**. What changes is the normalized source measure s, normalization, overlap and residual values. Source u must be normalized in this metric before using the displayed constants.

At zero temperature or under a positive-frequency restriction the metric can be semidefinite. Work on its nonzero-weight support/quotient, rather than invert its null directions. A finite-T positive-frequency commutator metric likewise remains diagonal in transitions and preserves the full-space filter, but it has a different spectral density and a support boundary; do not replace its density by the structure-factor density without the thermal factor.

For a finite Fourier domain, thermal weights are generally momentum dependent and the induced metric/projection is different. Reusing the Hilbert-Schmidt optimizer and merely reporting a thermal norm afterward is **not** the thermally optimized solution. In matrix notation with domain embedding P and full metric W, its normal equations are

    [P^dagger A^dagger W A P + eta P^dagger W P] z
        = P^dagger W u,    A=L−omega,

assuming positive-definite domain Gram matrix (otherwise quotient the nullspace). This is the appropriate weighted least-squares/resolvent variational equation. It reduces to the pointwise filter only without the restrictive domain projection.

All conclusions are conditional spectral mathematics; no observed scalar, interaction, or pole is inferred.

## Stronger bound for any normalized candidate

Both additional root inequalities are correct. Let B=(L−omega)²+eta I with eta>0, normalized source u and normalized candidate v in Dom(L), and r=||(L−omega)v||. Weighted Cauchy-Schwarz gives

    |<u,v>|²
      =|<B^(−1/2)u,B^(1/2)v>|²
      <= <u,B^−1u> <v,Bv>
      =(r²+eta) <u,[(L−omega)²+eta]^−1u>.

The source needs no Dom(L) assumption because B^−1/2 is bounded. Equality occurs for v proportional to B^−1u, precisely the full-space regularized filter above. Thus the filter is not just a suggestive example: it saturates this residual–overlap inequality at its corresponding residual.

For E_epsilon=1_(|L−omega|<=epsilon), define p_epsilon=||E_epsilon u||². Orthogonal decomposition and the spectral lower bound outside this window give

    |<u,v>| <= sqrt(p_epsilon) ||E_epsilon v||
                 +sqrt(1−p_epsilon) ||(1−E_epsilon)v||
             <= sqrt(p_epsilon)+r/epsilon.

For a fixed self-adjoint L, fixed metric and fixed normalized u, let v_n be **any** normalized candidates with residual r_n->0. Hold epsilon>0 fixed while taking limsup_n, then take epsilon down to zero. Since p_epsilon decreases to p_0=||1_(L=omega)u||²,

    limsup_n |<u,v_n>|² <= p_0.

In particular no source spectral atom at omega implies overlap tends to zero, independently of Fourier support, optimizer choice or filter shape. This proves a source-visible obstruction, not absence of an eigenmode invisible to u. If p_0>0 the bound is attainable by the normalized source projection onto the eigenspace; it still does not prove that eigenvalue is isolated from continuum.

For a locally bounded absolutely continuous density s<=S on |Delta−omega|<=delta and no singular component there,

    <u,B^−1u> <= pi S/sqrt(eta)+1/delta².

Choosing eta=r² for r>0 yields the quantitative bound

    |<u,v>|² <= 2 pi S r+2r²/delta².

For the smooth s0>0 case the corresponding asymptotic upper bound is 2pi s0 r[1+o(1)], and the regularized filter's r~epsilon attains its leading scaling/constant. This refinement uses the bounded/smooth-density hypothesis; the general window result does not.

### Null metrics and volume limits

A stationary positive semidefinite operator metric must first be quotiented by zero-norm directions. Require L to preserve that nullspace and define a self-adjoint operator on the resulting Hilbert space; in the diagonal free thermal structure metric this is explicit. Normalize u and v there. An unobserved/null component cannot be counted as a physical norm or overlap. A nonstationary or sign-indefinite commutator form is not the metric needed for these Cauchy-Schwarz proofs.

The fixed-L theorem cannot be applied directly to an arbitrary sequence of changing finite grids, fillings, temperatures, sources or metrics. A useful sufficient volume-limit condition is convergence of the normalized source spectral measures mu_V to a limiting measure mu, with mu({omega})=0, and residuals r_V->0 in their corresponding normalized metrics. For each fixed closed window, the Portmanteau upper bound gives limsup_V p_V,epsilon <= mu([omega−epsilon,omega+epsilon]); then the same two-step limit proves overlap->0. This assumes genuine weak convergence of probability measures, not a few numerical grids. Moving target frequencies can be reduced to a fixed limit omega_* when omega_V->omega_* because the new residual is at most r_V+|omega_V−omega_*|.

Without such a limit or uniform spectral-window control, a moving finite-grid atom can mimic persistent source weight. Keep momentum-grid, support-range and eta/residual limits separately registered.
