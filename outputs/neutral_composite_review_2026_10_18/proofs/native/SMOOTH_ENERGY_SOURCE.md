# Smooth energy-source constraint

Status: conditional-support. Direct root derivation; supplied finite compass H, existing local energies, stationary state. This is a linear-response diagnostic, not an added physical interaction or matter identification.

Let H=sum_x e_x and rho commute with H. With chi_C,e_x(t)=i theta(t) Tr rho[C(t),e_x], cyclicity implies sum_x chi_C,e_x(t)=i theta(t) Tr rho[C(t),H]=0. This exact uniform-source cancellation holds for every stationary density matrix, not only the selected numerical ground vector. A uniform modulation of H changes time parametrization; it cannot induce a linear change in stationary expectation of C.

For the finite open cube define K_x(z)=chi_C,e_x(z)/2 in the real spectral convention used by the regularized inverse-moment runner. For its regularized real part the same sum rule holds. Define source profile f(x/R) centered at the cube center and R in lattice sites. If the state and central C preserve inversion, K_x=K_-x, so the constant and linear Taylor terms cancel. Thus sum_x K_x f(x/R)=(1/(2 R²)) sum_ij d_i d_j f(0) sum_x K_x x_i x_j + remainder. With f four-times continuously differentiable on the sampled domain, pair the x,-x terms; a valid absolute remainder bound is M4/(24 R^4) sum_x |K_x| |x|^4, where M4 bounds the fourth directional derivative along unit vectors. Cubic symmetry makes the second moment isotropic.

This statement describes a profile varying slowly across this fixed cube. Increasing R is not increasing the physical simulation volume or demonstrating a bulk force law. Boundaries and state selection matter; the infinite-volume and zero-frequency limits can fail to commute, especially for gapless modes. A universal static gravity exclusion does not follow. Energy-density probes are not yet derived material objects or detector calibration.

The isolated retarded response differs from re-equilibrating a Gibbs state after changing J at fixed physical temperature: the latter changes beta J and includes equilibrium population changes. In particular, a thermal derivative of <C> need not vanish when the retarded uniform-source response vanishes. Do not conflate those preparation protocols.
