# An explicit conservative accuracy/resource family for the finite seeded router

New authored quantitative derivation requiring a distinct check. Conditional on the checked finite-seed composition and uniform-window theorem at the identities below, one explicit family reaches induced isometry error below epsilon, 0<epsilon<=1, throughout a fixed relative-width observation interval. It uses Theta(epsilon^-8) qubits and dimensionless duration, Theta(Lambda^-1 epsilon^-35) physical duration under incident cap Lambda, and a smallest supplied positive coefficient Theta(Lambda epsilon^28). These are sufficient exponents for the deliberately loose construction below, not optimal exponents, lower bounds, practical performance, or inherited apparatus constants.

## Fixed cutoff and exact normalized spectrum

Use the exact source spectrum with rho=gamma/j and 0<rho<=1/8. Write A=2-rho^2, delta=rho^2 and c=sqrt(2/pi). The source formula simplifies exactly to

    g_+(k)=c rho e^(ik) sin(k)/(delta sin(k)+i A cos(k)),
    g_-(k)=conjugate(g_+(k)).                         (1)

This follows by multiplying the denominator's conjugate into the numerator; it retains the source phase, not only its spectral density. Its L2 norm is one by the pinned composition's exact source premise.

Choose once sigma=pi/24 and the conservative sigma'=pi/6, so cmin=vmin/j=sqrt(3), cmax=vmax/j=2. Define a concrete cutoff with x=|k-pi/2|, transition width h=pi/12, and Q(s)=1-10s^3+15s^4-6s^5:

    chi(k)=1                      for x<=pi/24,
           Q((x-pi/24)/h)         for pi/24<x<pi/8,
           0                      for x>=pi/8.

Q and its first two derivatives match the constant pieces at both ends. Thus chi is C_c^2, takes values in [0,1], and has support strictly inside the conservative |k-pi/2|<pi/6 band. Its derivatives obey

    ||chi'||_infinity <= (15/8)/h=45/(2pi)<7.5,
    ||chi''||_infinity <=15/h^2=2160/pi^2<240.        (2)

Here Q'=-30s^2(1-s)^2 and Q''=-60s(1-s)(1-2s), so both derivative bounds are explicit and conservative.

The source tail allowance satisfies

    P<=4rho^2/[pi A^2 tan(pi/24)]<=11rho^2,
    p_chi=||chi g_+||_2^2>=1-P>1/2.                 (3)

The second inequality uses A>=1, tan(pi/24)>=pi/24 and pi>3; 96/pi^2<11. The restriction rho<=1/8 makes 11rho^2<1/2. Define exactly the source's positive normalization g=chi g_+/sqrt(p_chi), with no substitute profile or fitted phase.

## Analytic derivative bounds with rho dependence

Let z(k)=delta sin k+i A cos k and n(k)=e^(ik)sin k. Since A>=delta, |z|>=delta, while |z'|,|z''|<=2 and |n|<=1, |n'|<=2, |n''|<=4. Differentiating n/z once and twice therefore gives the pointwise bounds

    |g_+|<=c rho^-1,
    |g_+'|<=c rho(2/delta+2/delta^2)<=4c rho^-3,
    |g_+''|<=c rho(4/delta+10/delta^2+8/delta^3)
                                                   <=22c rho^-5. (4)

The two middle second-derivative contributions are -2n'z'/z^2 and -nz''/z^2, and the last is 2n(z')^2/z^3. No derivative of p_chi occurs: p_chi is constant with respect to k. Using (2), 1/sqrt(p_chi)<=sqrt(2), interval length at most pi, c<1, and sqrt(2)pi<6 yields

    G0=||g||_1<=sqrt(pi)<2,
    G1=||g'||_1<=100rho^-3,
    G2=||g''||_1<=2000rho^-5.                       (5)

Indeed the respective crude constants for G1 and G2 are bounded by 6(7.5+4)<100 and 6(240+8*7.5+22)<2000. Conjugation preserves the source derivative magnitudes, so the unnormalized incoming-launch constant also obeys

    B_minus=||(chi g_-)'||_1+(2/cmin)||chi g_-||_1
                                                   <=200rho^-3. (6)

For example its derivative term is no greater than the conservative normalized G1 bound and ||chi g_-||_1<=sqrt(pi)<2, while 2/cmin<2. These estimates are independent of the overall j but explicitly diverge as rho tends to zero. They are not claimed sharp; using denominator minima over the entire band loses the concentration information in (1).

## Explicit dimensionless choices and interval

For a target 0<epsilon<=1 choose

    rho=epsilon/256,
    u0=10^12 rho^-6 epsilon^-2,
    ell=ceil(100u0), M=ell+1,
    uminus=3ell/4, uplus=7ell/8,
    t0=u0/j, tminus=uminus/j, tplus=uplus/j.         (7)

The constants 3/4 and 7/8 lie strictly between 1/sqrt(3) and 1. Since sqrt(3)>5/3, the left late gap obeys

    tminus vmin-ell=(3sqrt(3)/4-1)ell>ell/4.

The right outgoing boundary gap is 2ell-tplus vmax=ell/4, and the outgoing discarded-tail gap is ell/4+2. The early gap ell+1-2u0 is at least ell/2. Also t0 vmin>2 and tminus>t0. Thus all geometric conditions of the source window theorem hold, strictly, for (7).

The elementary inequality sqrt(A^-2+A^-1)/sqrt(2pi)<=1/sqrt(A) for A>=1 gives, in dimensionless variables u=jt,

    T(t,A)<=[G1+(2u/A)G0]/sqrt(A).                 (8)

The right early tail has A=1+sqrt(3)u0>=u0 and u0/A<1, giving d_right<=104rho^-3/sqrt(u0). The early gap has u0/A<=1/50 and A>=ell/2, giving sqrt(2)T(t0,A_early)<=300rho^-3/sqrt(ell). At the left endpoint uminus/A_late<3, while at the right endpoint uplus/A_out<7/2. Therefore the window theorem's mixed-endpoint quantities satisfy

    d_L<=224rho^-3/sqrt(ell)<=230rho^-3/sqrt(ell),
    n_O<=228rho^-3/sqrt(ell)<=230rho^-3/sqrt(ell).

Equation (7) implies sqrt(u0)=10^6 rho^-3/epsilon and sqrt(ell)>=10sqrt(u0). Consequently d_L<1/2, and

    d_O=n_O/(1-d_L)<=2n_O<1.                      (9)

This uses the checked mixed-endpoint normalization bound, not a monotonicity assertion for its quotient. The normalized time-dependent finite target is exactly the source beta_F(t) on n=0,...,ell; its emitter and mediator coordinates are vacant. All phases, including exp(ik ell), the scattering exp(ik), and exp(-i2bt), remain as in the source.

## Quantitative ideal-error budget

The launch estimates give

    R0<=rho^-2/u0,
    L0<=200rho^-3/sqrt(u0),
    2delta_launch<=2R0+2L0+4sqrt(P).

With (3),(7), the spectral term is at most 4sqrt(11)epsilon/256<epsilon/16. The other two terms are separately below epsilon/16. In particular delta_launch<1, as needed for the source launch normalization.

For the early factorial tail, let d=ell+2. The ratios of consecutive terms of sum_(m>=d)(4u0)^m/m! are at most 1/25, because d>=100u0. The inequality d!>=(d/e)^d and e<3 give

    e_early<=2*(25/24)*(4e u0/d)^d
             <3*8^-d<=3/d<=3/(100u0)<epsilon/16.    (10)

The factorial inequality follows also by integrating log(x) below sum log(m), so no asymptotic Stirling remainder is required. This very weak final bound suffices here.

The outer-boundary constants of the pinned composition obey, using cmin>1 and (5),

    A_i<=4000rho^-5,
    A_o(tplus)<=5000rho^-5.                        (11)

For A_o the exact ratio uplus/qo(tplus)=7/2 gives coefficients 21 on G1 and 154 on G0, so 2000+2100+308<5000. For A_i use coefficients at most 12 on G1 and 52 on G0. After multiplying by sqrt(3)d_hop and the factor (2pi)^(-1/2), the remaining prefactor is at most j because d_hop<=sqrt(2)j and sqrt(3/pi)<1. The incoming denominator qi(t0)>=u0/2 and the outgoing qo(tplus)=ell/4 hence give

    e_boundary<=8000rho^-5/u0+10000rho^-5/ell
                 <=8100rho^-5/u0<epsilon/16.       (12)

The early-error e0 and final normalization terms can thus be accounted for without hidden cancellations. Each of the following nine nonnegative contributions is individually below epsilon/16:

* e_early;
* 2R0;
* 2L0;
* 4sqrt(P);
* 2d_right;
* sqrt(2)T(t0,A_early);
* e_boundary;
* 2d_L;
* 2d_O.

For the square-root tails this follows directly from sqrt(u0)=10^6rho^-3/epsilon and sqrt(ell)>=10sqrt(u0): the largest listed normalized-tail coefficient is 920/(10^7), far below 1/16. In (12), substitution gives at most 8100rho epsilon^2/10^12<epsilon/16. The elementary R0 and factorial inequalities are even smaller. Thus the source window's complete ideal allowance is below 9epsilon/16 throughout the interval. These loose constants intentionally leave room for the physical cell error rather than optimizing any stage.

## Whole-time cell cost and fixed incident cap

Let splus=uplus and choose

    eta=zeta=epsilon/[64(1+splus)],
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b^2/D0=Lambda eta^3/2,
    a=2j, gamma=rho j.                             (13)

These choices satisfy eta<=1/64, zeta<1/2 and D1>D0>2b. They fall within the pinned composition's safe incident-cap domain, so all its listed incident loads, including the combined positive emitter blocks, are strictly below Lambda. No norm convention is changed and no extra interaction is added.

The whole-duration physical cell allowance, including launch, is bounded by

    e_cell<=(2+8splus)sqrt(2)eta+2splus zeta
       <=[(8sqrt(2)+2)/64]epsilon<epsilon/4.         (14)

The total uniform isometry error is therefore below 13epsilon/16<epsilon. The corresponding unhalved channel allowance is below 2epsilon; for a requested channel accuracy epsilon, applying this same family with its accuracy argument epsilon/2 changes constants but no exponents. Actual physical output is never projected or renormalized. The supplied logical input and passive-reference statements are exactly those of the pinned composition/window theorem.

## Resource consequences and pessimism

Equations (7),(13), including their ceilings, give the following as epsilon tends to zero at fixed Lambda:

| Quantity | Exact prescription or count | Scaling of this family |
|---|---|---|
| Weak-edge ratio | rho=epsilon/256 | Theta(epsilon) |
| Early dimensionless time | u0=10^12*256^6*epsilon^-8 | Theta(epsilon^-8) |
| Radial length | ell=ceil(100u0), M=ell+1 | Theta(epsilon^-8) |
| Qubits | 6+2M=8+2ell | Theta(epsilon^-8) |
| Positive blocks | 7+2M=9+2ell | Theta(epsilon^-8) |
| Observation dimensionless endpoints | 3ell/4, 7ell/8 | Theta(epsilon^-8) |
| Cell ratios eta=zeta | epsilon/[64(1+7ell/8)] | Theta(epsilon^9) |
| D0 | Lambda eta/2 | Theta(Lambda epsilon^9) |
| b | Lambda eta^2/2 | Theta(Lambda epsilon^18) |
| j, and a=2j | Lambda eta^3/2, Lambda eta^3 | Theta(Lambda epsilon^27) |
| gamma | rho Lambda eta^3/2 | Theta(Lambda epsilon^28) |
| Physical observation times | tminus=3ell/(4j), tplus=7ell/(8j) | Theta(Lambda^-1 epsilon^-35) |

Block counts use the source's combined mediator and emitter-block convention. The smallest nonzero supplied coefficient in the displayed positive-term decomposition is gamma: a, b and j exceed it, j-gamma and 2j-gamma exceed it because rho<=1/256, and D0-2b=D0(1-2eta) and D1-2b are larger as well. This statement concerns coefficient magnitudes and their exact correlations, not a proved precision tolerance or a cost for physically generating them.

The relative window width is exactly (tplus-tminus)/tminus=1/6. Its absolute width scales with the same epsilon^-35 physical duration; there is no timed switching. The target remains a continuous time-dependent common packet and phase, not a stationary register.

The first major pessimism is the pointwise denominator-minimum derivative bound in (4), followed by one-integration tail estimates of order G1/sqrt(u). With rho proportional to epsilon, the sufficient condition rho^-3/sqrt(u0)=O(epsilon) produces u0 of order epsilon^-8. The exact narrow source profile may permit much sharper integral derivative estimates or sharper tail estimates; none is claimed here. The G2 bound controls an inverse-time boundary integral and does not dominate this selected family. Making ell a fixed large multiple of u0 then pays the early factorial localization requirement with an intentionally oversized constant.

The largest additional exponent cost comes from charging the cell residual over the entire splus=Theta(epsilon^-8): both eta and zeta are chosen of order epsilon/splus. Under the fixed incident cap this makes j of order Lambda eta^2 zeta, giving epsilon^27 and hence physical time epsilon^-35. This identifies a cost of the sufficient proof route, not a necessary physical bottleneck or an optimal lower bound. The enormous fixed constants and exact coefficient correlations preclude presenting this family as practical improvement.

## Exact provenance and scope

Primary complete sources, previously read in full and hashes refreshed:

* `common_product_finite_seed_router/PROPOSAL.md`: `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* `common_product_finite_window/PROPOSAL.md`: `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.

Recorded distinct checks, read completely and hash-verified for this task:

* `common_product_finite_seed_router_check/REVIEW.md`: `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9`.
* `common_product_finite_window_check/REVIEW.md`: `1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb`.

Their checks support the exact source scopes, not these new derivative constants, budgets or exponents. I authored the window and boundary extensions and checked the supplied-packet router; this shared same-model ancestry is exposure, not blind or model-diverse replication. ROOT requested the quantitative burden analysis. No old apparatus constants or runtime theorem were imported. A distinct checker should independently verify the cutoff normalization, rho-dependent derivatives, explicit error budgets, exact smallest coefficient, and exponents before integration.

This remains a conditional supplied-Hamiltonian, one-head, coherent-input theorem. It supplies no native-law identification, coefficient-production mechanism, accuracy tolerance, permanent output, capture/reset, stationary readout or old processor replacement. Only this proposal was created. No scientific executable, numerical sweep, symbolic solver, upstream source edit, W/Git/canonical/publication/checkpoint/editable-prompt/model change or delegation occurred. Hashing was identity bookkeeping. No retained status is assigned.
