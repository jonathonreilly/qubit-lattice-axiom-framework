# Finite stationary energy-source Ward identity and smooth-profile check

The proposed finite-system statement is correct, with explicit state-symmetry and limit qualifications. Neutrality of C is not needed for the conservation identity; it applies to any observable with the stated response definition.

## Conserved uniform source

Let H=sum_x e_x on the finite open graph, g a normalized exact eigenstate with energy E, and b_x=(e_x−<e_x>)g. Then

sum_x b_x=(H−E)g=0.

Consequently every linear spectral cross functional of b_x, including the regularized inverse moments used in the stationary benchmark, sums to zero. With the retarded convention for perturbation −sum_x f_x(t)e_x,

chi_C,e_x(t)=i theta(t) <[C(t),e_x]>,

one has sum_x chi_C,e_x(t)=i theta(t)<[C(t),H]>=0. Fourier/Laplace transformation therefore gives sum_x chi_C,e_x(z)=0 for Im z>0, and any existing boundary-value limit. The retarded identity holds more generally for every stationary density matrix [rho,H]=0, not just an eigenstate. In a mixed stationary state the stronger vector-source equation is not generally available: energy fluctuations can be nonzero although the uniform retarded response is zero.

This requires the actual local-energy partition, including the half-bond convention at boundaries so that sum e_x=H exactly. A different purported source observable need not satisfy the same identity. For approximate eigenvectors, the source sum is the eigenstate energy residual rather than exactly zero.

## Smooth source on a fixed symmetric cube

Center coordinates at the central C site, write r_x=x−x_center, and denote kappa_x(z)=chi_C,e_x(z). The linear response amplitude to a spatial profile f(r_x/R) is

A_R(z)=sum_x kappa_x(z) f(r_x/R).

Assume inversion is a symmetry of the Hamiltonian, the stationary state, the observable C, and the local-energy assignment. In particular, a Hamiltonian symmetry alone is insufficient if the chosen stationary state breaks it. Then kappa_−x=kappa_x and every odd spatial moment vanishes. Conservation removes the constant term.

For f four-times continuously differentiable on the scaled cube, Taylor's theorem yields

A_R(z) = (1/(2R²)) sum_ij partial_i partial_j f(0) M_ij(z) + E_R(z),
M_ij(z)=sum_x kappa_x(z) r_x,i r_x,j,

with the explicit finite-cube remainder bound

|E_R(z)| <= [sup_y ||D^4 f(y)||_op /(24 R^4)] sum_x |kappa_x(z)| |r_x|^4.

The supremum is over line segments between zero and r_x/R; the derivative norm is the Euclidean multilinear operator norm. The first- and third-order Taylor polynomials cancel by inversion. Without C4 regularity one can use the usual lower-order Taylor modulus/remainder instead. The displayed Hessian coefficient is a possible leading term; it may itself vanish, in which case the response starts at higher order.

If the response also respects the full cubic point group, the second moment is isotropic:

M_ij=(delta_ij/3) sum_x kappa_x |r_x|²,

so A_R(z)=[Delta f(0)/(6R²)] sum_x kappa_x(z)|r_x|² + E_R(z).

This stronger reduction needs cubic invariance of the state and response, not only that the bare C expression transforms as a scalar. In an exactly degenerate eigenspace one must choose an invariant state or mixture, or verify the particular response symmetry. The selected CSS-sector label by itself is not a proof of full spatial invariance.

## Limits and interpretation

The expansion is R large compared with a FIXED finite cube's coordinate extent, at a frequency/regulator where the finite response is defined. It is not a uniform thermodynamic estimate: the moments and remainder prefactor can grow with system size or become large near resonances. A simultaneous large-cube, small-frequency, long-wavelength limit requires separate bounds and an order of limits. Uniform-source conservation does not prohibit response to nonuniform sources, hydrodynamic modes, long-distance interactions in another regime, or a scalar in an appropriately specified different channel. It supplies no gravity no-go.

The same algebra applies to the numerical cross inverse-moment kernel because its source dependence is linear and the connected energy sources sum to zero. One must retain the convention-dependent response factors when translating that kernel to a physical susceptibility.

## Isothermal versus isolated response

For a uniform source, H_lambda=H−lambda H=(1−lambda)H. Isolated dynamics from any rho commuting with H leaves that state unchanged even for a time-dependent scalar coefficient of H, hence the zero retarded response.

In contrast, if the system is re-equilibrated with a reservoir at fixed inverse temperature beta, rho_lambda is proportional to exp[−beta(1−lambda)H]. For C with no explicit lambda dependence,

(d/dlambda)<C>_lambda at lambda=0 = beta [<CH>−<C><H>].

This ordinary covariance is real because H commutes with rho; it can be nonzero. It describes a changed Gibbs preparation, equivalently a changed beta H, rather than the isolated retarded transition response. General nonuniform isothermal perturbations use the appropriate imaginary-time/Duhamel covariance. Confusing these two protocols would incorrectly erase genuine thermal preparation effects or incorrectly attribute them to isolated transitions.
