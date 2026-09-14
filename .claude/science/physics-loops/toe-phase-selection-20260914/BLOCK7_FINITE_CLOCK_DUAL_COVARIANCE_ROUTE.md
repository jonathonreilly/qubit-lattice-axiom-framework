# Finite-clock dual covariance route: active proposal

Personal derivation begun 2026-09-14 after the compact U(1) transfer analysis.
This is an UNCHECKED extension route, not a finite-clock masslessness theorem.
The remaining campaign runs to 2026-09-15 01:30:44 UTC.

## Target and exact objects

For the isotropic Z_N Villain model on a finite four-dimensional box, Fourier
expansion gives a discrete Gaussian on the FULL-RANK integer lattice

    L_N = { n in Z^P : delta n is divisible by N },
    weight(n) proportional exp[-||n||^2/(2 beta)].

The original real plaquette score is the continuous Villain logarithmic
 derivative evaluated at clock angles. Its two-point contact identity from
block 6 remains true because it is a Fourier-factor identity, not an
integration-by-parts assumption on continuous link variables.

Let L_0=ker(delta) intersect Z^P. Conditioning on the electric current
j=delta n/N leaves a shifted discrete Gaussian coset of L_0. A uniform
lower covariance estimate for ALL affine cosets of L_0 would therefore
imply Cov(n)>=beta_* P_closed, where P_closed projects onto ker(delta).
The challenge is to prove the uniform-coset estimate with checked FS
renormalization hypotheses, not merely to quote the centered result.

## Proposed extension of the FS phase representation

The FS renormalized partition has the shape

    Z(a) = sum_gamma d_gamma int Gaussian(dA)
           product_rho [1+z_rho cos(A(tilde_rho)+rho(a))],

with d_gamma>0, 0<z_rho<1 and geometric activity bounds. The phase slope is
rho(a), using the ORIGINAL current. The oscillatory frequency is the
RENORMALIZED tilde_rho. This distinction matters: the covariance of A under
a renormalized density is not automatically the original covariance.
A naive Brascamp--Lieb argument on tilde_rho would not prove the desired
original-source statement.

For f_z(x)=log(1+z cos x), one has

    |f_z''(x)| <= z/(1-z).

Indeed |cos x+z|<=1+z cos x follows on squaring. For a real source direction
w, pointwise differentiation of the log product therefore bounds the
second derivative below by -sum_rho z_rho/(1-z_rho) rho(w)^2. Logarithmic
differentiation AFTER integration adds a nonnegative variance term; taking
the positive sum over gamma adds another nonnegative variance. Thus a
uniform bound

    sum_rho z_rho/(1-z_rho) rho(w)^2 <= c(beta) ||d w||^2

would imply Hess log Z(a)[w,w]>=-c(beta)||d w||^2 for EVERY phase a, not
just the zero phase. The FS surface/length estimate used in (2.104)-(2.107)
looks suited to exactly this quadratic bound, with c(beta) exponentially
small for large beta. All normalization, 2pi and contour/source conventions
must still be checked from the original scanned formulas.

Completing the Gaussian square in the coset MGF gives

    log E_a exp[t A(mu)] = beta t^2 (mu,V mu)/2
                           + log Z(a-beta t V mu)-log Z(a),

up to a linear centering term depending on the coordinate convention.
Its second derivative would give the uniform centered covariance bound

    Cov_a(A) >= beta [1-beta c(beta)] V.

The mean need not vanish in an individual affine coset. The law of total
covariance then preserves this LOWER bound after mixing electric-current
sectors. A global upper bound is a different obligation.

## Exact lattice-dual identity and the second estimate

The dual lattice is

    L_N^* = Z^P + (1/N) d Z^E.

This can be proved using finite-group character annihilators, with no
assumption that N is prime. Put M_N=N L_N^*=N Z^P+d Z^E and
beta_dual=N^2/(4 pi^2 beta). Poisson summation of the full-rank Gaussian,
followed by differentiating a real source at zero, gives

    Cov_L_N(n)/beta + Cov_M_N(m)/beta_dual = I.

The latter lattice contains the integer exact-form lattice d Z^E. If the
same uniform-coset lower bound applies to that integer-curl model, then

    Cov_M_N(m) >= beta_dual_* P_exact,
    P_exact projects onto im(d),
    P_closed+P_exact=I.

Combining both estimates yields

    beta_* P_closed <= Cov_L_N(n)
      <= beta P_closed + beta[1-beta_dual_*/beta_dual] P_exact.

This is the prospective finite-clock replacement for the U(1) angular
covariance sandwich. If both beta and beta_dual are sufficiently large,
the lower coefficient beta_* exceeds the small upper complementary
coefficient. Component spectra would have a directional discontinuity at
zero, while the uniform upper bound gives clustering. The bounded-score
transfer criterion from block 6 would then apply to THIS isotropic
finite-clock transfer, subject to its invariant state construction.

## Critical unresolved checks

1. The phase-dependent renormalized partition identity must hold with positive
   mixture coefficients and the SAME activity bounds for arbitrary cosets.
2. Surface bounds must use original rho, with the correct 2pi convention.
3. Both relative-boundary closed forms and free-boundary exact forms must be
   covered. Their Hodge projectors need a controlled infinite-volume limit.
4. Poisson normalizations and the covariance identity need independent exact
   small-lattice checks, including composite N and nontrivial incidence.
5. The finite-clock free-boundary state must be identified and reflection
   positive. Continuous-circle monotonicity must not be imported blindly
   into a different finite-group model.
6. Even success here would concern the isotropic clock transfer. The selected
   continuous-time monopole-penalty Hamiltonian still needs a phase-preserving
   anisotropic relation or a separate estimate. No native law or axiom update
   follows automatically.

The point of this route is the exact covariance duality and a uniform phase
curvature estimate. It is not an argument that rare defects alone establish
a Coulomb phase. First test the finite identities and adversarially inspect
the uniform-phase representation, then decide whether the extension is valid.


## Local integration convention check, 18:47 UTC

Original preprint pp.26--30 and 35--39 were visually inspected. Its positive
cosine-product identity (2.42) preserves a linear phase rho(a), and the
successive selected-link integrations in Corollary 4 leave that external
phase untouched. This supports the proposed uniform-phase route.

The local Gaussian factor is being re-derived rather than copied literally:
for action n(x-m)^2/(2 beta), integrating exp(i rho x) gives
exp[-beta rho^2/(2n)+i rho m]. The preprint scan's (2.63)/(2.66) appears to
print beta/n instead of beta/(2n), and its renormalized-frequency signs need
checking against the local conditional mean. A direct scalar quadrature at
beta=.7,n=6,rho=1.3,m=.25 agrees with the half-factor expression and differs
from the literal full-factor expression by .08506639984. This is a
convention-sensitive preprint formula discrepancy; no claim about the
published version has been made. The published PDF was not obtained from
the publisher's public access page. The proof only needs a positive decay
constant, so a correct local derivation can supply conservative constants.

Use Q=d^T d, diagonal n_e. On selected mutually nonadjacent links B, conditional
integration replaces the frequency rho by

    rho_tilde = rho - Q P_B diag(n_e)^(-1) P_B rho

and multiplies its Gaussian integral by

    exp[-beta/2 sum_(e in B) rho_e^2/n_e].

This formula makes rho_tilde_e=0 on selected links and preserves delta rho=0
because delta Q=0. It also makes the phase slope ORIGINAL rho(a), not
rho_tilde(a). Test this full matrix identity independently before using it.
A selection containing at least a fixed fraction of rho's squared norm
then gives exponential activity damping with a possibly smaller coefficient
than the preprint's 1/108. Boundary links have n_e<=6 in four dimensions;
zero-diagonal links are pure gauge/no-plaquette variables and must be
removed or integrated to impose their current constraint.
