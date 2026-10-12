# The direct two-scalar Lorentz promotion fails a kinetic-sign test

Direct parent derivation, 2026-10-12. This rejects one explicitly proposed
completion of the reconstructed static response. It does not exclude QUMOND,
modified gravity generally, or theories with additional fields or constraints.
No empirical parameter or frozen inverse fit is changed.

## Candidate assumptions being tested

Start from DIRECT_STATIC_ACTION.md. Propose to turn both Phi and Phi_N into
independent real Lorentz scalar fields, replace their spatial-gradient inner
products by contractions with a flat metric eta=(-,+,+,+), and retain the
same two-derivative action with no new gauge symmetry or kinetic constraints:

    L = C[-2 eta^(mu nu) partial_mu Phi partial_nu Phi_N
          + F(eta^(mu nu) partial_mu Phi_N partial_nu Phi_N)] - rho Phi,

where C is a nonzero common constant. The finite response family is exactly
constant N0=1+sum w at sufficiently small positive field norm. Hence the
static primitive is F(s)=N0*s near s0. A smooth Lorentzian extension about
zero gradient must have this same derivative at zero; choose it as the
minimal candidate. It suffices to examine that local quadratic theory.

## Opposite kinetic signs

Put X=delta Phi and Y=delta Phi_N. Up to the common C, the quadratic time
derivative terms are

    L_time = 2 dot X dot Y - N0 dot Y^2
           = (dot X,dot Y) K (dot X,dot Y)^T,
    K = [[0,1],[1,-N0]].

The determinant is -1. Its eigenvalues

    lambda_plus  = (-N0+sqrt(N0^2+4))/2 > 0,
    lambda_minus = (-N0-sqrt(N0^2+4))/2 < 0

have opposite signs for every real N0. Changing the common action sign
does not remove this fact. Since the time-derivative Hessian is nonsingular,
both fields are dynamical under the declared assumptions; one cannot call
one of them a nondynamical multiplier after this promotion. The canonical
momenta give the kinetic Hamiltonian (1/(4C)) p^T K^(-1) p, which is likewise
indefinite. An invertible real local field redefinition preserves the numbers
of positive and negative directions. Algebraic source couplings and mass
terms cannot change this high-frequency kinetic defect.

The D-family condition d[A N(A)]/dA>=0 made the constitutive part of the
static functional convex. It cannot fix the negative determinant of this
two-field Lorentzian kinetic matrix. Static elliptic equations and their
auxiliary potentials therefore must not be advertised as a healthy dynamical
completion merely by adding time derivatives.

## Reconstruction consequence

Retain the static response as a candidate observational description. Reject
this minimal two-independent-scalar Lorentz promotion as a positive-energy
completion. A next completion would need a materially different field content,
constraint/gauge structure, or time/spatial dynamics, all stated as new
assumptions and checked again. Whether any such completion reproduces the
same galaxy and solar operator is an independent obligation.

The healthy positive-scalar spectral family in the earlier campaign milestone
has a different action and observation map. Identifying its positive measure
with the present response weights would be a new unproved physical bridge.
The indefinite two-field candidate cannot be repaired by that identification
alone. This is a local mathematical failure of the candidate assumptions,
not an observational exclusion or a formal audit verdict.
