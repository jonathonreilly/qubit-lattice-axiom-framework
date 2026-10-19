# Stationary coefficient precision for alternating mediator chains

Status: new conditional analytical interface, requiring distinct checking. The construction can replace exponentially small *bare hopping magnitudes* by fixed-size supplied coefficients and increasing length. It does not remove relative coefficient precision, matching of onsite energies, source-ratio calibration, or physical preparation obligations. The estimates below concern the stationary Schur operator and its first energy derivative. They are not a pulse, loaded-apparatus, or runtime theorem.

## Sources and exposure

The following exact identities are reused within their stated scope:

| Source | SHA256 |
|---|---|
| bipartite_mediator_supply/PROPOSAL.md | 836caee25d87e31c757e8965b4de85d5998a613dcc5862072d6cddc2a380c8dc |
| bipartite_mediator_supply_check/REVIEW.md | 78af05b19696d2cae2cf147c1e666c9c1a39ca0a2ba9c67a8d1746c12c72de8f |
| mediated_critical_source_interface/PROPOSAL.md | d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3 |
| mediated_critical_source_interface_check/CORRECTION_RECHECK.md | 2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8 |
| mediated_mass_tuned_family/PROPOSAL.md | d01ed6b60f3bacf2b7557687995902f8c3e172eafecd7a1547cb3bc458451883 |
| mediated_mass_tuned_family_check/REVIEW.md | 6a7a9f0dcb6ea04e5bde943e99a9ab7e04755ab0cfb26a07e6d1a4fd4e174b2e |

I authored the isolated and stationary mediator ancestors and checked the ROOT-authored mass-tuned alternative. ROOT proposed examining precision and highlighted the common-error exponent cancellation. This is a new derivation, not an independent review of those ancestors. The corrected stationary installation removes the existing positive port cap before replacing it: adding the new cap to the already capped background is incorrect. No historical erroneous installation or uncorrected mass-tuning derivative is used.

## Nonuniform positive chain and exact stationary data

Take 2n internal sites, strong bonds J_i>0 on (2i-1,2i), i=1,...,n, weak bonds q_i>0 on (2i,2i+1), and endpoint bonds gamma_L,gamma_R>0. Let A be their internal adjacency matrix, with positive off-diagonal entries. Physical hopping is minus this adjacency. All sites have the same declared onsite mu; energy z is measured relative to mu. In odd/even order A has off-diagonal block equal to a diagonal matrix of J_i plus a weighted shift of q_i. Hence

    a_* = min_i J_i - max_i q_i > 0
    implies dist(0,spectrum(A)) >= a_*.

For n=1 take max q_i=0. Indeed the diagonal block has smallest singular value min J_i, and the shift norm is max q_i. Let C select the two internal ends, Gamma=diag(gamma_L,gamma_R), and define

    Sigma(z)=Gamma C^T (z I+A)^(-1) C Gamma.

This is the self-energy subtracted from the endpoint pencil z I-H_end. Chiral symmetry makes its diagonal entries odd in z and its off-diagonal entries even. At zero,

    Sigma(0) = [[0,t],[t,0]],
    t=(-1)^(n-1) gamma_L gamma_R
                     (product_{i=1}^{n-1} q_i)/(product_{i=1}^{n} J_i).       (1)

Forward substitution in the bidiagonal block proves (1). Differentiation gives

    Sigma'(0)=-diag(c_L,c_R),                                          (2)
    c_L=gamma_L^2 sum_{k=0}^{n-1}
             (product_{i=1}^{k}q_i)^2/(product_{i=1}^{k+1}J_i)^2,
    c_R=gamma_R^2 sum_{k=0}^{n-1}
             (product_{i=n-k}^{n-1}q_i)^2/(product_{i=n-k}^{n}J_i)^2.

Empty products are one. These are squared endpoint columns of A^(-1). In general c_L differs from c_R: arbitrary bond errors destroy reflection symmetry, although they preserve chiral symmetry. Neither Sigma(z)=s(z)I+t(z)X nor equal endpoint slopes may be retained without a separate symmetry hypothesis.

For |z|<=w<a_* and gamma_max=max(gamma_L,gamma_R), a resolvent series gives

    ||Sigma(z)-Sigma(0)|| <= gamma_max^2 |z|/[a_*(a_*-w)],
    |Sigma_aa(z)+c_a z| <= gamma_max^2 |z|^3/[a_*^3(a_*-w)],
    |Sigma_LR(z)-t| <= gamma_max^2 |z|^2/[a_*^2(a_*-w)].                (3)

The latter two bounds use parity of the series. They are absolute bounds, not useful relative hopping bounds automatically: t may be exponentially small. In particular c_a<=gamma_max^2/a_*^2. These statements also apply to complex z in that disk. Positive perturbations preserve the sign in (1), so the existing endpoint sign gauges remain valid, including the seed's (-1)^m convention when the background port gauge is fixed.

## Independently variable errors: exact product sensitivity

Compare with uniform nominal J,q and nominal endpoint gamma, r=q/J<1. Write logarithmic deviations e_Ji=log(J_i/J), e_qi=log(q_i/q), e_L=log(gamma_L/gamma), e_R similarly. Equation (1) implies the exact identity

    log|t/t_nom| = e_L+e_R+sum e_qi-sum e_Ji.                         (4)

If ordinary relative errors are bounded by epsilon_J,epsilon_q,epsilon_L,epsilon_R<1, put ell_a=-log(1-epsilon_a). Then |e_a|<=ell_a and

    |log|t/t_nom|| <= tau_n
       =ell_L+ell_R+(n-1)ell_q+n ell_J,
    |t/t_nom-1| <= exp(tau_n)-1.                                    (5)

Here t/t_nom is positive. With a common error bound epsilon on all 2n+1 physical bonds, a sufficient bound for relative effective-hopping error delta is

    epsilon <= 1-exp[-log(1+delta)/(2n+1)].                           (6)

This is a worst-case sufficient condition, not a universal necessary precision law. An allowed example with exact endpoints, J_i=J(1+epsilon), q_i=q(1-epsilon), gives the actual ratio (1-epsilon)^(n-1)/(1+epsilon)^n and logarithmic error approximately -(2n-1)epsilon. Thus length accumulation is real in this error class. Independent variability does not justify a square-root-of-length estimate; that would require a specified probability law, correlations and confidence level.

The diagonal slopes behave differently. Put U=ell_J+ell_q. From (2), for either endpoint with logarithmic bound ell_e,

    exp(-2ell_e-2ell_J) S_n(r exp(-U))/S_n(r)
      <= c_e/c_nom <=
    exp( 2ell_e+2ell_J) S_n(r exp( U))/S_n(r),                       (7)
    S_n(x)=sum_{k=0}^{n-1}x^(2k),  c_nom=gamma^2 J^(-2) S_n(r).

This remains valid even if the upper geometric ratio exceeds one. If r exp(U)<1, the simpler length-independent bounds are

    exp(-2ell_e-2ell_J) (1-r^2)/(1-r^2 exp(-2U))
      <= c_e/c_nom <=
    exp( 2ell_e+2ell_J) (1-r^2)/(1-r^2 exp( 2U)).                   (8)

For the upper inequality, the expectation of the increasing sequence exp(2kU) under a truncated geometric distribution is no larger than its infinite-distribution expectation. For the lower inequality the decreasing sequence has the reverse comparison. This proves (8), rather than discarding n-dependent factors informally. At a fixed positive gap margin these slope errors are uniformly controlled in n. Near gap closure the constants deteriorate. If the symmetric logarithmic envelope fails r exp(U)<1 but the actual chain is still gapped, use (7), the actual sums (2), or the actual gap bound; failure of this sufficient envelope is not a spectral instability claim.

## Three cells and linear-mass-normalized ratios

Use n1=n2=2m-1, n3=m with possibly different endpoint errors in every cell. Orient each cell from the seed toward the unchanged port. Its endpoint slopes are c_lL,c_lR. The exact linear coefficients on the three source endpoints are

    Z0=1+c_1L,
    Z1=1+c_1R+c_2L,
    Z2=1+c_2R+c_3L.                                                (9)

There is also a port coefficient c_3R, which is not removed by source normalization. Source-only positive congruence gives

    A1=|t1|/sqrt(Z0 Z1), A2=|t2|/sqrt(Z1 Z2), K=|t3|/sqrt(Z2).     (10)

These are stationary linear coefficients; this congruence is not a physical isometry or a preparation procedure. The physical port self-energy and its derivative remain in the loaded background inverse.

For a nominal finite cell let c_a^0 denote each slope. Suppose (7) or (8) gives |log(c_a/c_a^0)|<=sigma_a. A valid bound z_i on |log(Zi/Zi^0)| is the larger of

    log[(1+sum_{a in i} c_a^0 exp(sigma_a))/Zi^0],
    log[Zi^0/(1+sum_{a in i} c_a^0 exp(-sigma_a))].                 (11)

In particular z_i<=max_{a in i}sigma_a. With cell product bounds tau_l from (5), exact subtraction of logarithms in (10) yields

    |log[(A2^2/A1^2)/(A2_0^2/A1_0^2)]|
       <=2tau_2+2tau_1+z_0+z_2,
    |log[(K^2/A1)/(K_0^2/A1_0)]|
       <=2tau_3+tau_1+z_0/2+z_1/2+z_2.                            (12)

The external j is fixed. For the alternative nominal family tuned in d01ed6, the finite-length discrepancy from each critical ratio is at most 2delta_m in logarithm, where

    delta_m=(u+v+w)r^(2m),
    u=gamma1^2/(J^2-q^2), v=gamma2^2/(J^2-q^2),
    w=gamma3^2/(J^2-q^2).

Thus add 2delta_m to the corresponding right side of (12) to bound log[(A2^2/A1^2)/8] or log[K^2/(3sqrt(3)j A1)]. The resulting relative error is bounded by exp(bound)-1. This uses that family's exact correlated limiting tuning, not the incompatible earlier bare-gamma correlations. Finite-length improvement in delta_m does not force fabrication errors in (12) to shrink.

## Correlated common errors can cancel ratio exponents

Suppose all strong bonds share J'=J exp(u_J), all weak bonds share q'=q exp(u_q), and both endpoints of cell l share gamma_l'=gamma_l exp(u_l). Then

    log(t_l'/t_l)=2u_l+(n_l-1)u_q-n_l u_J,
    log[(t2'/t1')/(t2/t1)]=2(u_2-u_1),
    log[(t3'^2/t1')/(t3^2/t1)]=4u_3-2u_1-u_J.                    (13)

The weak-bond exponent and length dependence cancel in the last ratio because 2(n3-1)=n1-1. This is a real structural advantage for these correlated errors. It does not hold for arbitrary independently variable bond errors. The mass factors still change: use (2) and (9), not the old tuned values. Fixed endpoint tuning equations generally cease to hold for the new J',q'. At a fixed gap their mass changes need not grow with m, but need not vanish either.

Even in (13), the absolute scale t1 changes by 2u_1+(2m-2)u_q-(2m-1)u_J. Therefore a common relative ratio error between q and J can change the linewidth exponentially in m. A waveform and clock chosen for the actual measured device are different obligations from one predeclared nominal target and runtime. No latter robustness follows from ratio cancellation. If every J,q,gamma is multiplied by s, the masses stay unchanged and all t_l multiply by s; the first critical ratio stays fixed but K^2/A1 multiplies by s relative to the fixed external j. Scaling the processor as well would be a different problem.

## Positive realization, onsite precision, and resources

A full-qubit bond is a(n_i+n_j-X_ij)>=0. Adding the occupation coefficient mu minus the actual incident bond sum at every site realizes exactly mu I minus the one-head adjacency, provided those coefficients are nonnegative. For this error interface those occupation values are assumed to track the actual bonds, or equal-onsite matching is supplied by another explicitly justified mechanism. Positive slack in the installation inequalities must survive the allowed errors. Shared literal B and the declared scalar conventions are retained. At the old port the original cap is removed and replaced as in d2b7; retaining it and adding another cap does not preserve the background compression.

Keeping the nominal occupations fixed while changing the Q-bond coefficients generally changes the onsite diagonal and breaks the chiral zero-self-energy identity. For example, if an internal diagonal error D has norm e_d<a_*, a direct resolvent identity only gives

    ||Sigma_D(0)-Sigma(0)||
      <= gamma_max^2 e_d/[a_*(a_*-e_d)].                            (14)

This is an absolute sufficient bound, not exponentially small in n and not a necessary lower bound. Endpoint diagonal errors also enter directly. The present theorem cannot claim to remove fine diagonal matching when those occupations are not controlled. Equation (14) does not establish a universal obstruction to a different symmetry-protected implementation.

For a uniform cell |t|=(gamma^2/J)r^(n-1), so reaching a specified member of the discrete scale family requires n logarithmic in 1/|t|. The three-cell construction has 10m local head sites including the three sources and port, 10m-4 internal mediator sites, 10m-1 bonds, and at most 20m-1 positive bond/occupation blocks before zero terms are omitted. This uses the corrected replacement convention and excludes the rest of the processor.

A directly supplied hopping of size |t| with relative tolerance delta needs absolute coefficient tolerance delta |t|. Under the conditional matched-onsite model, (6) instead asks for relative precision of order delta/n on ordinary-sized J,q,gamma, hence absolute precision of order their magnitude times delta/n. Since n grows logarithmically with 1/|t|, this can relax the absolute hopping-coefficient scale requirement substantially. It trades that requirement for increasing resources, positive-gap and onsite matching assumptions, and coefficient correlation or calibration obligations. It does not make precise control free; nor does it supply arbitrary continuous effective scales using only integer length.

## Verification limits and remaining bridge

All formulas above follow from finite bidiagonal inversion, chiral symmetry, resolvent series and explicit logarithmic inequalities. No spectrum solver, dynamics, parameter sweep or new operating point was used. No editable prompts, canonical files, Git state or publication were changed.

A distinct check is required. To claim a useful physical source one must additionally bound the actual loaded ordered inverse including the port derivative, complementary channels and possible loaded poles; account for mediator population and product-seed overlap; control the energy-dependent remainder over the actual spectral distribution; and establish a physical time/output estimate with its chosen actual or nominal target. An internal gap alone does not prove those statements. This proposal neither transfers the previous three-site tolerance theorem to energy-dependent mediators nor asserts a native microscopic supplier. It quantifies a stationary precision/resource tradeoff and the conditions under which that tradeoff is meaningful.
