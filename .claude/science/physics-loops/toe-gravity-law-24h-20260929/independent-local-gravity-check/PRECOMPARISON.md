# Independent centered-derivative derivation before author proof read

2026-09-30. At this freeze I have read only the new CONTRACT, not its
REPORT, code, results, or prior-art files. The parent analytic gravity
proof has already been independently checked. The brief supplies the
candidate derivative and requested O(epsilon^2) rate, not their validity.

Let n=2J+1, epsilon=2pi/n, and r(k) be the representative of k modulo n.
The centered symbol has the exact periodicity

    sin(epsilon r_j(k))/epsilon = sin(epsilon k_j)/epsilon.

For a continuum Fourier series f, the coefficient of the full derivative
sampling defect at representative l is therefore the sum over ALL aliases
k with r(k)=l of

    i[sin(epsilon k_j)/epsilon-k_j] fhat(k).

The inequality |sin t-t|<=|t|^3/6 holds for all real t, not only a fixed
low band (integrate |1-cos t|<=t^2/2). Since |r(k)|_1<=|k|_1, the weighted
sum in a smaller radius rho' obeys

    sum_j ||(D_e,j I_n-I_n partial_j)f||_(rho')
      <= epsilon^2/6 [3/(e delta)]^3 ||f||_rho,
      delta=rho-rho'>0.

Here sum_j |k_j|^3<=|k|_1^3. Thus no extra factor three is necessary for
the combined gradient. This bound already includes aliases of arbitrarily
large continuum frequencies; there is no need to add a separate alias
tail to this particular estimate. A spectral-derivative comparison plus
an exponential alias bound is another permissible, weaker route. A
separate interpolation-versus-continuum comparison still has a sampling
tail and must be accounted for if the theorem uses interpolants.

The actual centered grid derivative is skew-adjoint and satisfies
|sin(epsilon l_j)|/epsilon<=|l_j|. The parent exact skew-integration
augmentation therefore survives verbatim: q=D_e g, r=D_e B(g), with the
same local V(g,q,r), canonical p-dot adjoint, and exact time preservation
of q-D_e g and r-D_e B. It is not legitimate to replace r by B_g q.
The finite nonlinear coefficient maps are unchanged. Uniform Wiener,
N-seminorm, and one-radius derivative-loss bounds use only this upper
symbol estimate, never an elliptic lower bound. Hence the same majorant
algorithm, bootstrap constants, T0, and Volterra time T can be used.
Initial consistent q/r norms obey the same M0 bound.

Assuming the already established continuum trajectory in radius
rho2=3sigma0/4, compare it to the new finite centered trajectory at
rho1=sigma0/2 and rho0=sigma0/4. The all-frequency defect above gives a
source epsilon^2 kappa(delta) sum_l m_P_l m_Q_l and initial mismatch
epsilon^2 kappa(delta)(||h0||_rho2+||B(g0)-I||_rho2), delta=sigma0/4.
The same Volterra stability proof multiplies initial-plus-T-source by
at most two. No centered lower symbol bound is used. Actual scalar and
momentum densities are the literal changed-law expressions; their
one-derivative scale estimates transfer the state error to a smaller
radius, with their own O(epsilon^2) sampling defect. Full finite closure
is neither needed nor obtained.

Locality requires precise wording. Each Christoffel symbol at x uses
the central metric and its six axial nearest neighbors. The literal
scalar density C(x) includes D Gamma and can depend on sites within
graph/l1 distance two of x. For unit lapse, exact summation by parts
rewrites H as sum of T+V(g,D_e g,D_e B), each term supported on the
radius-one axial star. Its canonical gradient at a site has radius at
most two. The actual momentum density has radius one. Physical lengths
are these lattice radii times epsilon. This is a finite-range continuous
metric law; it does not preserve a staggered block112 seed or produce
a native qubit realization. The coefficients contain the specified
1/epsilon derivative normalization as the grid is refined.

Checks still needed on the author proof: exact use of the full alias
sum; combined-vector constants; whether locality means density support,
Hamiltonian star support, or equation stencil; whether constraint claims
use actual canonical/density expressions; and whether any lower symbol
estimate, continuum substitution, or exact closure has been inserted.
No numerical result has been read or used at this stage.
