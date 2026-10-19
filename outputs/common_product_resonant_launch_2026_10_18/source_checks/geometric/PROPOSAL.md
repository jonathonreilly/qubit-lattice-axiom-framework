# A normalized geometric comparison for the exact source spectrum

New bounded author derivation requiring distinct review. The physical upper-half-circle outgoing source amplitude is within an explicit O(rho) full-circle L2 distance of a normalized one-sided geometric Fourier profile. The discarded half-circle is charged explicitly. Exact free evolution preserves this comparison uniformly for all real times. A separate, time-dependent dispersion bound compares that free evolution with an integer translate of the geometric profile; it is not an exact rigid-translation law or a finite-router theorem.

ROOT suggested the rational profile and the possible5rho ceiling. The factor, phase, Fourier convention, normalization and domain error are reconstructed below. The result proves the stronger sufficient ceiling29rho/8. No physical density or integration domain is silently replaced.

## 1. Exact physical amplitude and Fourier convention

Use precisely the standalone equal-diagonal endpoint launcher from sourcefb72: emitter s, positive combined source block Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0, uniform Q_j bonds along n>=0, j>0 and0<rho=gamma/j<=1/2. Its checked spectral measure is complete, has mass one and no atoms. Its phase-preserving outgoing amplitude, from derivative378086, is

    F(k)=-i sqrt(2/pi)rho exp(ik)
                     /[(2-rho^2)cot k-i rho^2], 0<k<pi,
    ||F||_(L2(0,pi))=1,
    E(k)=2j(1-cos k).                                    (1)

The source's exact incoming coefficient is conjugate(F). Its full seeded state also has its emitter amplitude and BOTH directed lead terms; F alone is not the complete physical seed state.

Work on the circle0<=k<2pi with UNWEIGHTED measure dk, and define the unitary inverse Fourier map

    (F_inv f)_n=1/sqrt(2pi) integral_0^(2pi) exp(ink)f(k)dk,
    n in Z.

Let F_up=1_(0,pi)F, zero on the lower semicircle. It has full-circle norm1. Endpoint values are irrelevant to L2. Put

    a=sqrt(1-rho^2), d=1/sqrt(2pi), z=exp(ik).

Using cot k=i(z^2+1)/(z^2-1) gives the EXACT rational continuation

    F_rat(z)=-d rho z(z^2-1)/(1+a^2 z^2).                 (2)

Equation(2) agrees with(1) on the physical upper semicircle. It does not extend the physical spectral measure therefrom to the whole circle. Indeed |F_rat(2pi-k)|=|F_rat(k)|, so its full-circle squared norm is2, not1. This explicitly rules out the shortcut of treating the rational continuation as the unchanged normalized physical outgoing spectrum.

## 2. Partial fractions and the two semicircle errors

Define two full-circle functions

    U_+(k)=i d rho/(1+i a z),
    U_-(k)=i d rho/(1-i a z),
    b_a=(1+a^2)/(2a^3).

Polynomial division and partial fractions give

    F_rat=b_a(U_+-U_-)-d rho z/a^2.                       (3)

For verification, z(z^2-1)/(1+a^2z^2)=z/a^2-(1+a^2)z/[a^2(1+a^2z^2)], while

    1/(1+iaz)-1/(1-iaz)=-2iaz/(1+a^2z^2).

Together with the i in U_+-U_-, these identities give exactly the sign and coefficient in(3). U_+ is resonant near k=pi/2, whereas U_- is resonant on the lower semicircle. Neither is simply dropped without a norm allowance.

On the lower semicircle sin k<=0, hence

    |1+ia exp(ik)|^2=1+a^2-2a sin k>=1+a^2.

On the upper semicircle |1-ia exp(ik)|^2=1+a^2+2a sin k>=1+a^2. Consequently

    ||1_lower U_+||_2, ||1_upper U_-||_2
                <=L_rho:=rho/sqrt[2(1+a^2)].             (4)

The upper polynomial term has norm rho/(sqrt(2)a^2). The normalization of U_+ is proved in section3; in particular ||1_upper U_+||<=1. Since b_a>=1, equation(3) and a triangle inequality on the upper and lower pieces give

    ||F_up-U_+||_2
       <=B_rho:=(b_a-1)+(b_a+1)L_rho+rho/(sqrt(2)a^2).
                                                               (5)

The lower contribution in this inequality is the actual omitted U_+ mass, rather than an asserted analytic continuation. Upper/lower orthogonality would give a smaller combined ceiling, but is not needed.

Here is a uniform numerical bound with every constant explicit. Write x=rho^2 in(0,1/4]. Then

    b_a=(2-x)/[2(1-x)^(3/2)],
    db_a/dx=(1-x/4)/(1-x)^(5/2)
               <=(4/3)^(5/2)<9/4.

Thus b_a-1<=9rho^2/4<=9rho/8. Monotonicity also gives b_a<=7/(3sqrt(3))<3/2. Furthermore L_rho<=sqrt(2/7)rho<3rho/5, and rho/(sqrt(2)a^2)<=4rho/(3sqrt(2))<rho. Inserting these into(5) yields

    B_rho<=[9/8+(5/2)(3/5)+1]rho=29rho/8<4rho<5rho.

Since F_up and U_+ are unit vectors, we may use

    delta_rho=min{2,B_rho}<=29rho/8.                      (6)

This bound is uniform for0<rho<=1/2. Its constant is sufficient, not asserted optimal.

## 3. Exact normalized one-sided geometric profile

For a<1 the geometric series converges absolutely and uniformly on the circle:

    U_+(k)=i rho/sqrt(2pi) sum_(m>=0)(-ia)^m exp(imk).

Termwise inverse Fourier transformation gives exactly

    u_n=(F_inv U_+)_n=
       i rho(-ia)^(-n), n<=0;
       0, n>0.                                           (7)

The source phase i, alternation and support direction depend on the stated exp(+ink) inverse convention; replacing its sign would reverse the support. Its squared norm is

    sum_(m>=0)rho^2 a^(2m)=rho^2/(1-a^2)=1.              (8)

This proves ||U_+||_2=1 by Parseval and justifies its use in(5). There is no unfixed global phase or post hoc normalization. For two identical copies carrying a path qubit and arbitrary passive program/reference, the same scalar comparison acts identically on both orthogonal paths, so its operator bound has no extra branch or reference-dimension factor.

## 4. Uniform all-time FREE outgoing-sequence comparison

Define normalized full-integer sequences

    f(t)=F_inv[exp(-itE(k))F_up(k)],
    u(t)=F_inv[exp(-itE(k))U_+(k)].                       (9)

Both evolve under the bounded uniform full-line one-head generator

    (H_free v)_n=2j v_n-jv_(n-1)-jv_(n+1).

Fourier multiplication by the exact unit-modulus exp(-itE) is unitary for every real t. Therefore

    ||f(t)-u(t)||_ell2(Z)=||F_up-U_+||_2<=delta_rho,
    ||f(t)||=||u(t)||=1, all real t.                     (10)

Restriction to ANY set of integers can only reduce the discrepancy. In particular the physical outgoing term O_t F on n>=0 from fb72 is exactly the half-line restriction of f(t), and

    ||O_t F-P_(n>=0)u(t)||<=delta_rho.                   (11)

Neither half-line restriction in(11) is asserted to have norm one. The comparison is between free outgoing sequences; the physical launcher's full state also includes the occupied-emitter amplitude and the incoming lead term. At t=0, for example, those other terms are essential to reconstruct its actual emitter seed. No free initial geometric vector is asserted to have been physically prepared by this calculation.

This proof never closes a time-dependent contour. The essential singularity of exp[ijt(z+z^-1)] at z=0 for t!=0 is immaterial to unitary multiplication but would invalidate an unjustified residue shortcut. The two semicircle errors were paid BEFORE evolution and stay paid by exact unitarity.

## 5. Optional real cutoff with its normalization cost

Let0<=chi<=1 be a real cutoff on(0,pi), equal to1 on |k-pi/2|<=sigma, and let p=||chi F||_2^2>0. Set g=chi F/sqrt(p), extended by zero to the lower semicircle. The inner product of F_up and g is real and at least sqrt(p), since chi>=chi^2. Therefore

    ||F_up-g||_2<=sqrt[2(1-sqrt(p))].                    (12)

If the checked hard-band source bound P_sigma<1 is used, then

    p>=1-P_sigma,
    P_sigma=min{1,4rho^2/[pi(2-rho^2)^2 tan sigma]},
    ||F_up-g||_2<=sqrt[2(1-sqrt(1-P_sigma))]
                                      <=sqrt(2P_sigma).

Consequently every real t obeys

    ||F_inv[e^-itE g]-u(t)||
       <=min{2,delta_rho+sqrt[2(1-sqrt(p))]}.             (13)

The same holds after spatial restriction. This charges the real cutoff and its actual positive normalization. The claim does not require chi to be analytic or continue chi around a contour. When sigma shrinks, its displayed P_sigma dependence must remain; no fixed-cutoff constant is silently reused in that regime.

## 6. Optional propagation versus an integer-translated profile

Equation(10) compares two exactly dispersed states; it does not make u(t) a rigidly moving geometric shape. A separate estimate is possible by paying the nonlinear dispersion explicitly.

Choose k0=pi/2 and the circle coordinate s=k-k0 in[-pi,pi], understood modulo2pi. Then E(k)=2j(1+sin s), and

    |U_+(k0+s)|^2
       =rho^2/[2pi((1-a)^2+4a sin^2(s/2))]
       <= pi rho^2/(8a s^2), s!=0.                     (14)

The last inequality follows from sin(|s|/2)>=|s|/pi on this interval. It retains the broad spectral tails; it is not a compact-support or Gaussian approximation.

For each real t choose the integer m=floor(2jt+1/2), so |2jt-m|<=1/2, and define the norm-one comparison

    G_n(t)=exp(-i2jt) exp(im pi/2) u_(n-m).              (15)

The Fourier multiplier of(15) is exp(-i2jt)exp[-im(k-k0)]. Its ratio to the exact free multiplier leaves residual phase

    2jt sin s-ms=(2jt-m)s+2jt(sin s-s).

Thus this phase convention is fixed, including the rounding phase. There is no fitted shape or phase. The integer translation makes the comparison periodic on the circle even at the chosen s branch cut.

For the rounding term, (14) gives

    integral s^2 |U_+|^2 ds<=pi^2 rho^2/(4a),
    ||(exp[-i(2jt-m)s]-1)U_+||
           <=[pi/(2sqrt(a))]rho|2jt-m|
           <=2rho|2jt-m|<=rho.                          (16)

For dispersion, |sin s-s|<=|s|^3/6 and |exp(ix)-1|<=min{2,|x|}. Set T_d=j|t|/3. With C=pi/(8a), (14) and extension of a nonnegative integral yield

    ||(exp[-i2jt(sin s-s)]-1)U_+||^2
       <=2C rho^2 integral_0^infinity min{4,T_d^2 s^6}/s^2 ds.

For T_d>0 split at s0=(2/T_d)^(1/3). The integral is

    T_d^2 s0^5/5+4/s0=(6/5)2^(5/3)T_d^(1/3).

It vanishes at t=0 by direct evaluation. Hence, putting

    C_disp(a)=sqrt[3pi 2^(5/3)/(10a 3^(1/3))]<=2,

the triangle inequality and Parseval prove, for ALL real t,

    ||u(t)-G(t)||<=D_rho(t)
      :=min{2,2rho|2jt-m|+C_disp(a)rho(j|t|)^(1/6)}
       <=min{2,rho+2rho(j|t|)^(1/6)}.                    (17)

The numerical ceiling follows on a>=sqrt(3)/2; for instance even the looser a>=3/4, pi<22/7,2^(5/3)<16/5 and3^(1/3)>7/5 make its square less than4. Both vectors in(17) are normalized, which justifies the cap2. The error grows with time before that cap; no exact translation or all-late small error is claimed.

Combining(10),(17) gives the directly useful free physical-spectrum comparison

    ||f(t)-G(t)||<=min{2,delta_rho+D_rho(t)}.              (18)

At times j|t| of order rho^-2 times a logarithm, the upper bound in(18) is O(rho^(2/3) times that logarithm^(1/6))+O(rho). This is a norm estimate for a specified free sequence, not a source-vacancy time or a finite-router operating exponent.

## 7. Explicit spatial-tail consequences and their limits

The geometric shape in(15) is supported on n<=m. For any integer L<=m its exact left-tail norm is

    ||P_(n<=L)G(t)||=a^(m-L).                            (19)

Indeed summing rho^2 a^(2(m-n)) over n<=L is a geometric series with squared sum a^(2(m-L)). For t>=0, m>=0, so(18) implies

    ||P_(n<0)f(t)||<=a^(m+1)+delta_rho+D_rho(t),
    ||P_(n>m)f(t)||<=delta_rho+D_rho(t).                 (20)

Norms can additionally be capped by1. These are free-profile tails with an explicit dispersion floor. They do not prove control of actual graph boundaries or source reabsorption.

There is also a bounded statement about the known incoming coefficient of the SAME standalone launcher. The exact identity

    I_t conjugate(F)=conjugate(P_(n>=0) f(-t))

follows by conjugating the Fourier integral, without any spectral approximation. For t>1/(4j), the chosen rounded center m(-t)<=-1 and the comparison G(-t) vanishes on n>=0. Thus

    ||I_t conjugate(F)||<=min{1,delta_rho+D_rho(-t)}.     (21)

Equation(21) controls a lead term, not the entire seeded state. It need not decay for arbitrarily large t because(17)'s dispersion bound grows; the prior integration-by-parts estimates remain available outside its useful regime. The occupied-emitter term must still be paid separately, for example by the pinned survival result306174 if its scoped premises are adopted. No new complete launch time, finite router length, cut integral, simultaneous error allocation, record flag or runtime result is inferred here.

The survival-only source306174 supplies no spatial transfer theorem. Conversely the present free-profile comparison supplies no global spectral completeness or absence-of-atoms result beyond the already adopted exact standalone measure. Finite graphs, interacting cores, record thresholds, multiple reflections and all finite-output apparatus coordinates require their own proved interfaces. The band-edge and lower-semicircle errors have not been erased to obtain those conclusions.

## 8. Exact sources, exposure and required check

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Fully read and SHA256 refreshed unchanged for this task:

- common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Adopt its exact normalized spectral amplitude and incoming/outgoing decomposition at the standalone scope, including the checked measure1953d153 identified there.
- common_product_launch_derivative_bounds/PROPOSAL.md:378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8. Adopt the exact complex cancellation and real cutoff convention; no derivative asymptotic is needed for(5)--(21).
- common_product_resonance_tail/PROPOSAL.md:306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002. Its rational identity and failed whole-circle shortcut were reread; its survival bound is not a premise of the new free-profile estimates.

Their prior checked scalar-reference/launch/derivative scopes remain those recorded in the pinned sources and preceding coherent work. This note does not claim a new independent audit of those premises. ROOT suggested U_+, its geometric coefficients and the possible5rho comparison. The author derived the exact partial fractions, explicit paid semicircle errors, normalization, free-unitary comparison, cutoff cost and separate dispersion/rounding bound after that exposure. This is same-model author continuation, not blind or independent checking.

A distinct check should reconstruct every phase/factor in(2)--(3),(7),(15); verify upper/lower domain costs and physical norm versus rational-continuation norm; verify the normalized cutoff overlap; check the weighted phase integral and rounding at negative times; and distinguish free lead projections from complete seeded or finite-graph dynamics. Constants here are sufficient and no optimality is claimed.

Only this proposal was created. No scientific executable, numerical integration/solver/sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. Supplied source interactions, compensated diagonals, occupation basis and logical/blank input premises are unchanged. No native preparation, physical capture/reset, old literal processor transfer or permanent halt is claimed. This new derivation remains provisional pending distinct check.
