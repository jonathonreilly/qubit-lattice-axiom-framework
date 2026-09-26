# Current checkpoint

Pre-primary-source derivation complete. Only the allowed independent
source identities and current AGENTS/SCIENCE_WORKFLOW snapshots have been
read or authenticated. No primary author native-formation file was opened.

Derived product source: r_a(p)=beta p_0 l_a(p)^6,
l_a(p)=p_0+sum_b W(a,b)p_b. For the source adjoint with frozen reference p,
its homogeneous q expectation is
F(p,q)=beta sum_a l_a(q)^6[(p_0/p_a)q_a-q_0].
F(p,p)=0 and D_q F(p,p)=H(p)r(p), H=C^{-1}; derivatives of l_a cancel
because their central bracket vanishes. This gives the required entropy
constant/linear cancellation after the bounded local replacement.

For W=1+j v_a.v_b, l_a=1+j v_a.g. Six-field reactions have even/odd
polynomials of degree six; vector linear reaction is 12 beta j p_0 g,
density reaction is -6 beta delta rho and quadrupole linear reaction is zero.
For the homogeneous isotropic Euler profile, rho'=6 beta(1-rho).
Transverse gain is exp[2j(rho(t)-rho(0))], hence bounded.

The time-dependent product-entropy quadratic form gives exact mode energy
derivative with coefficients -6beta/rho in density,
6beta(1-rho)(4j-1/rho) in vectors and -6beta(1-rho)/rho in quadrupoles.
This bounds the full nonautonomous response; frozen spectra alone do not.

The count-lumped finite star, source-adjoint Taylor checks, full six-field
matrices, energy identity and finite-time propagator controls completed.
The final report states a proved smooth-profile extension conditional on the
correct reaction PDE and a uniform interior bound. No unresolved proof gap
remains within that scope; no finite-N product law or native fluctuation
theorem is asserted.

Execution history: attempt 1 completed without assertion failures but labeled
a raw pair-moment derivative as a connected covariance for the general biased
controls. Attempt 2 subtracts the product-mean derivative and reports both
quantities. Its balanced covariance counterexample remains exactly 1/18.
Both scripts and full logs are preserved. Final attempt 2 has 11 exact and
four numerical/solver controls. Source identities are in DEPENDENCIES.json;
all new artifacts are to be frozen by PRE_SOURCE_SEAL.json before access to
any primary native-formation calculation. No other work is outstanding.
