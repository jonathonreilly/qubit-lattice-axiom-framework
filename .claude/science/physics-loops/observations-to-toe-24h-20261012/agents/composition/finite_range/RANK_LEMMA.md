# When two exterior heights rotate a source response

This bounded result concerns spherical linear source responses, fixed material charge vectors and a common positive mediator measure. It does not prove empirical identifiability of the full quadratic observables. In particular, a test-material contrast can itself vanish.

Let a core and mantle have nonzero masses and separated radial supports: every core radius is no larger than every mantle radius. For a mediator of inverse range μ, write their positive shell form factors as

    F_C(μ)=∫core dM/M_C sinh(μa)/(μa),
    F_M(μ)=∫mantle dM/M_M sinh(μa)/(μa),
    C(μ)=f_C F_C(μ), M(μ)=f_M F_M(μ),
    c(μ)=C(μ)/[C(μ)+M(μ)].

Here M_C and M_M are the component masses, M_tot=M_C+M_M, f_C=M_C/M_tot and f_M=M_M/M_tot. Thus F_C(0)=F_M(0)=1 and C(0)+M(0)=1. These are the same f_C and f_M used in the final asymptotic expression. The earlier dM/M convention meant total-mass normalization.

For μ>0, the logarithmic μ derivative of a shell factor is

    a coth(μa)-1/μ.

It increases strictly with a because coth(z)-z csch²(z)>0 for z>0. Thus C'/C<M'/M for nondegenerate separated layers, and c(μ) decreases strictly with μ.

At an exterior radius r the normalized effective core fraction in the force row is

    f(r)=E_r[c(μ)],
    dp_r(μ) ∝ dν(μ) exp(-μr)(1+μr)[C(μ)+M(μ)].

The r derivative is

    f'(r)=Cov_r(c(μ), -μ²r/(1+μr)).

Both functions in this covariance decrease strictly with μ. The covariance equals half the expectation over two independent draws of the product of their differences, and is therefore positive whenever the positive spectral measure has genuine width on μ values with different c. Consequently f(r) increases strictly with exterior radius. This proof requires convergence of the differentiated integrals, which holds for the frozen exponential measure and r at or outside the source surface.

For one Yukawa mass, the measure is a point mass, the covariance is zero, and the normalized exterior source row is independent of radius. The same failure of discrimination occurs for a spatially constant composition or the massless mode. Those controls identify exactly which premises generate the additional row.

If q_C and q_M are the constant material charge rows, the normalized force response is

    E(r)=f(r)q_C+[1-f(r)]q_M.

Adding a normalized solar row S gives the exact determinant identity

    det[E(r1),E(r2),S]
      =[f(r1)-f(r2)] det[q_C,q_M,S].

For r1<r2 and a broad positive spectrum, the first factor is nonzero. The three source rows are therefore independent precisely when S lies outside the span of the two material rows. The frozen numeric source models verify this second condition separately. Three independent source rows admit only d=0 as a simultaneous **source-charge** null; this statement does not eliminate a vanishing test contrast in a force product.

For the gamma(s=1) measure and large ell, expansion of the exact force kernel gives

    F_ell(r,a)=1+(a²/3-r²)/ell²+2r³/ell³
                +(a^4/5-2r²a²-3r^4)/ell^4+O(ell^-5).

For constant-density core/mantle, total radius R, core radius cR and mass fractions f_C,f_M, the first height-dependent composition difference is

    f(r1)-f(r2)
      = -f_C f_M R² [(1-c²)/(1-c³)] (r2²-r1²)/ell^4
          +O(ell^-5).

The leading ell^-2 source composition bias is common to both radii and cancels from their difference. The ell^-4 scaling explains why mathematical rank three rapidly becomes practically poorly conditioned. This is an independently derived algebraic/asymptotic result for the supplied comparison class; no novelty priority or full no-go theorem is claimed.
