# Working derivation: a global Gauss dressing

Personal exploration, 2026-09-16. No independent review or retained status. All conclusions below are mathematical proposals for the supplied rotor/fermion law; the uniform estimates and physical interpretation are to be challenged.

## 1. Finite exact construction

Take the complete free cubic complex [0,L]^3, L>=1, with integer incidence D from edges to vertices (tail minus head), curl C from edges to faces, and B from faces to cubes. Thus DC*=0 and BC=0. Counting inner products, unit electric and magnetic weights. Set S=ker D=range C*, P its orthogonal projection, Lambda=S intersect Z^E, and

    A=(C*C)^(1/2), K=A^+ on S, Delta0=DD*.

A is positive on S, with norm at most w0=sqrt(12). The cycle lattice is saturated in Z^E. Its dual is P Z^E: any integral functional on Lambda extends to Z^E because the quotient by a saturated sublattice is free. The map eta=Pz -> q=Cz is a bijection from Lambda* to C Z^E. Integer cohomology of the cube makes this last set ker(B) intersect Z^P. The inverse uses eta=C*(CC*)^+q. On closed q,

    eta.A eta = q.H2^(-1/2) q,
    H2=CC*+B*B.

Here H2 is strictly positive by the interval tensor decomposition. There is no harmonic sector on the free cube.

For integer vertex charge Q with sum Q=0, choose any integer flow E0 with DE0=Q. Such a flow exists along a spanning tree. Put

    e_Q=D*Delta0^+ Q, a_Q=P E0=E0-e_Q,
    n=E-e_Q in Lambda+a_Q,
    Z_g(a)=sum_(n in Lambda+a) exp[-g^2 n.K n].

The electric-basis wave function

    psi_Q(E)=Z_g(a_Q)^(-1/2) exp[-g^2 (E-e_Q).K(E-e_Q)/2], DE=Q,

is normalized, positive and independent of the integer representative E0. Its support satisfies exact Gauss law. For a neutral matter Fock basis eta with charges Q(eta), define

    V_g |eta> = |eta> tensor psi_Q(eta).

This is an isometry, since distinct matter basis states are orthogonal. It embeds the complete neutral matter space, not a block-neutral subspace. No true ground-state property is assumed.

Poisson summation on S gives a positive constant c_g, independent of a,

    Z_g(a)=c_g Theta_g(a),
    Theta_g(a)=sum_(eta in Lambda*) exp[-pi^2 eta.A eta/g^2] exp[2pi i eta.a].

## 2. Exact overlap and energy identities

For a link shift e with charge change De, let t=P e. Using the representative E0+e in the new charge sector,

    I_Q(e)=sum_E psi_Q(E) psi_(Q+De)(E+e)
      =exp[-g^2 t.K t/4]
       Z_g(a_Q+t/2)/sqrt[Z_g(a_Q)Z_g(a_Q+t)].           (1)

For a plaquette boundary d=C*e_p, d is in Lambda, so

    <psi_Q,U(d)psi_Q>
      =exp[-g^2 d.K d/4] Z_g(a_Q+d/2)/Z_g(a_Q).       (2)

Let F=log Theta on S. Differentiating the translated real Gaussian sum gives

    E_Q n= -A grad F(a_Q)/(2g^2),
    Cov_Q(n)= A/(2g^2)+A F''(a_Q) A/(4g^4),
    (g^2/2) E_Q E^2
      = (g^2/2) Q.Delta0^+Q + tr(A)/4
        +[tr(A F'' A)+|A grad F|^2]/(8g^2).           (3)

All derivatives in (3) are in S. The cross term e_Q.n is zero pointwise. This isolates an exact Coulomb energy before making any compact correction estimate. The Hessian does not by itself bound the mean term; a separate first-derivative bound is required.

For a charged hopping A_e=c_x^dagger T_e U_e c_y, its compressed matrix element equals the free CAR matrix element times I_Q(e), with Q the source configuration. This factor can depend on the full charge configuration. It is not legitimate to replace it by a number without a uniform estimate on (1).

## 3. Proposed uniform theta estimate

Seek constants C,c,g0>0 independent of L and every affine a in S such that a real extension F_ext to R^E agrees with F on S and

    |grad F_ext|_infinity <= epsilon(g),
    ||F_ext''||_(2->2) <= epsilon(g),
    epsilon(g)<=C exp(-c/g^2), 0<g<=g0.               (4)

This is stronger than the preceding campaign's centered theta pressure bound. It controls ALL affine sectors, including charge configurations far from any chosen vacuum.

Proposed proof mechanism: each closed integer face q splits into connected closed components gamma under common cubes. For each component choose an odd integer edge filling z_gamma with C z_gamma=gamma, support in a clipped cube of side <=6||gamma||_1, and ||z_gamma||_infinity<=3||gamma||_1. This is a free-boundary relative-chain lemma, to be proved rather than replaced by zero extension. Put z(q)=sum z_gamma. For a in S, z(q).a=eta.a, independent of fillings.

Set c0=1/(2sqrt(12)), t0=pi^2 c0/g^2. A Gaussian face variable phi with covariance

    (H2^(-1/2)-c0 I)/(2g^2)

is positive definite. The dual theta equals E_phi Xi(C*phi+a), where Xi is the exact hard-core sum of closed-component activities

    exp[-t0 ||gamma||^2] exp[2pi i z_gamma.u].

For sufficiently large t0, the connected cluster expansion defines a real U(u)=log Xi(u), uniformly over all real u. It is positive after exponentiation because opposite currents pair and the convergent logarithm starts at zero. Retaining total cluster mass rather than net support gives uniform local first derivatives and a Schur Hessian bound of order exp(-c t0).

The Gaussian u=C*phi has covariance

    T_g=(A-c0 A^2)/(2g^2)

on S, norm <=w0/(2g^2). Hence the positive Gaussian measure tilted by exp U(u+a) is uniformly log-concave when ||T_g|| ||U''||<1. Finite-dimensional Brascamp-Lieb then bounds

    F_ext''=E U'' + Cov(grad U)

between -epsilon0 I and epsilon0/(1-||T_g||epsilon0) I. Also |grad F_ext|_infinity<=sup |grad U|_infinity. This avoids assuming summability of the Coulomb projector or any volume-small total theta correction.

Remaining checks: exact square-root-kernel/source identity, free-boundary component filling, cluster derivative constants, singular Gaussian domain, and finite affine-sector falsifiers.

## 4. Intended variational compression (not yet established)

If (4) holds, the midpoint defect in (1) is bounded by epsilon(g)||t||^2/8. Since ||t||<=1, charge dependence in each normalized hopping overlap is uniformly exponentially small. In (2), ||d||^2=4, so the same estimate controls the magnetic matrix element with no charge-dependent normalization loss.

The proposed comparison on the whole neutral matter space is

    V_g^* calH V_g = E_var(g,L) I + H_m(T_e eta_e)
                    +(g^2/2) Q.Delta0^+Q + R_g,L,
    eta_e=exp[-g^2 K_ee/4],
    E_var=tr(A)/4+g^(-2)sum_p[1-exp(-g^2 (C K C*)_pp/4)],
    ||R_g,L|| <= C |V| g^(-2) exp(-c/g^2).           (5)

The meaning of the last bound and constants must include bounded hopping norms and finite onsite dimension. A local diagonal charge potential, if explicitly supplied, commutes with V_g and can be carried exactly; it must not be silently added to the previous model.

An elementary spectral-sum target is K_ee<=14 uniformly in the free cube: K<=H1^(-1/2), normalized tensor eigenfunctions have squared amplitude <=8/(L+1)^3, and sqrt(lambda_n)>=2|n|/(L+1). Grouping n by max norm bounds the sum. Likewise tr Delta0^+ <=(7/4)|V| in three dimensions. These constants need a direct check of zero modes and interval eigenvalue conventions.

For two conjugate Slater states with identical densities and fixed equal particle counts, the charge covariance is <=2m I, so the expected Coulomb term is bounded by C_m g^2 |V|. This is an energy trial consequence, not a lower bound on the true energy or an actual-state infrared result.

## 5. Physical limit retained

Equation (5), even if proved, is a variational compression onto one chosen gauge state per charge configuration. It does not remove transverse photon excitations, prove small off-space action, supply a Feshbach approximation, show ground-state uniqueness, or establish the fixed-g phase. The exact Coulomb term is a useful globally Gauss-constrained reference for that further work. Any claimed phase must control the omitted gauge dynamics and compact sectors in the actual state.
