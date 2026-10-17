# Relative-coefficient stability of the scalar three-site source

Status: new conditional analytic theorem proposal requiring a distinct check. Exact critical ratios are not necessary for stability of the scalar finite-band complex outgoing packet. The theorem below controls a fixed nominal comparator, including its phase, by relative coefficient errors independent of waiting time and source scale. It does not prove robustness of the actual processor, its temporal onset, or native coefficient suppliers.

## 1. Perturbed scalar source and domain

Keep the uniform-j ray, carrier 2j, and source sites 0,1,2 with the ray beginning at 3. Put eta=lambda/j with 0<eta<=1/16. Nominal couplings are

    a1,0=lambda/sqrt(3), a2,0=lambda sqrt(8/3), kappa0^2=3j lambda.

Choose positive real couplings and real scalar source detunings d_i satisfying

    a1^2=a1,0^2(1+e1), a2^2=a2,0^2(1+e2),
    kappa^2=kappa0^2(1+e3),
    |e_i|<=epsilon, |d_i|<=epsilon lambda.

Use the same negative hopping signs and the same ray diagonal. Define

    q=1-3eta,
    B(epsilon)=20epsilon+16epsilon^2+4epsilon^3,
    chi=B(epsilon)/q,

and assume epsilon>=0 and chi<1. This implies epsilon<1/20 and all bonds are nonzero. The source diagonal detunings multiply the full internal identity when this scalar construction is embedded later. They are not arbitrary old-input-dependent detunings.

Let m_j(z)=[z-sqrt(z^2-4j^2)]/(2j^2) on its physical branch. The perturbed exact scalar determinant and seed density are

    D_e(z)=[(z-d0)(z-d1)-a1^2](z-d2-kappa^2 m_j(z))
                                             -a2^2(z-d0),       (1)
    rho_e(delta)=kappa^2 sin(q_old)/j * a1^2 a2^2
                                          /(pi |D_e(delta+i0)|^2),
    delta=-2j cos(q_old), 0<q_old<pi.                         (2)

The symbol q_old is an angle; q=1-3eta is the positive margin. No Markov self-energy replaces m_j in (1). The numerator is the exact last-source cofactor a1*a2. Optional detunings do not change that cofactor.

## 2. Uniform real-axis determinant stability

Write R=sqrt(delta^2+lambda^2) and D_0 for the nominal exact finite-band determinant. The checked scalar source gives |D_0|>=q R^3 on |delta|<=2j. On the same band |m_j|=1/j. Each of the first two factors z-d_i changes from z by at most epsilon R, and the last factor changes from z-kappa0^2 m_j by at most 4epsilon R. Its nominal magnitude is at most 4R. Expanding the three-factor term gives an error at most

    4[(1+epsilon)^3-1] R^3.

The a1^2 times last-factor term costs at most (4/3)(2epsilon+epsilon^2)R^3; the a2^2 times first-factor term costs at most (8/3)(2epsilon+epsilon^2)R^3. Adding proves

    |D_e-D_0|<=B(epsilon)R^3,
    |D_e/D_0-1|<=chi,
    |D_e|>=q(1-chi)R^3.                                  (3)

This proof does not track or assume continuity of individual multiple-pole locations. A split Markov triple pole does not invalidate a uniform real-axis determinant margin. The error scale is relative source coefficients and d_i/lambda, not T times a full Hamiltonian norm.

## 3. No hidden scalar mass

Equation (3) excludes band and threshold determinant zeros. It remains necessary to exclude exterior eigenvalues before treating (2) as a normalized measure. For x>=2j the nominal determinant obeys

    D_0(x)>=x^3[1-3lambda/x-3lambda^2/x^2]
             >=x^3[1-1.5eta-.75eta^2].

The same lower bound applies to |D_0(-x)| by nominal oddness. The perturbation need not preserve oddness. However the preceding product estimate remains valid outside the band because |m_j(+-x)|<=1/j. There R^3<=x^3(1+eta^2/4)^(3/2), so

    |D_e-D_0|<q x^3(1+eta^2/4)^(3/2).

For eta<=1/16, (1+eta^2/4)^(3/2)<=1+eta^2 and

    (1-3eta)(1+eta^2)<1-1.5eta-.75eta^2.

The difference is at least 1.5eta-1.75eta^2>0. Thus neither exterior halfline has a zero. The finite-rank Jacobi resolvent is algebraic, regular in the band, bounded at thresholds, analytic on the exterior and asymptotic to 1/z in its seed entry. Its Cauchy representation is consequently precisely (2), with integral one and no residual singular/point mass. Nonzero Jacobi bonds make the seed cyclic, so no scalar bound sector is hidden from that seed. This uses the isolated uniform-j apparatus; it is not a statement about an attached processor.

## 4. Fixed complex outgoing packet and uniform comparison

At the first uniform ray site, the exact retarded seed column is

    A_e(q_old)=kappa*a1*a2*exp(i q_old)/(j D_e(delta+i0)).

Indeed the last-source column is a1*a2/D_e and the negative source-ray hopping multiplies m_j=-exp(i q_old)/j, giving the displayed sign. With the same Fourier convention throughout, define

    F_e(q_old)=i (2j sin q_old) A_e(q_old)/sqrt(2pi).

Then |F_e|^2 dq_old=rho_e ddelta, so ||F_e||_2=1. The nominal F_0 has the identical reference plane and phase convention. Put

    nu=(1+epsilon)^(3/2)-1,
    L=(nu+chi)/(1-chi).

The ratio of positive numerator factors lies in [(1-epsilon)^(3/2),(1+epsilon)^(3/2)], and its distance from one is bounded by nu. From (3),

    |F_e/F_0-1|<=L,
    ||F_e-F_0||_2<=min(2,L).                              (4)

This is a comparison of the full complex amplitudes, not only densities or arrival probabilities. Any common fixed unit-modulus phase can multiply both packets without changing (4). A hardware change that itself changes the downstream phase is not covered by that observation. The nominal comparator is fixed once; it is not fitted to the perturbed device at each time.

Full Fourier isometry and restriction to the ray imply a time-uniform bound min(2,L) for the represented outgoing scalar components, because their uniform-ray dispersion is unchanged. Reality gives the conjugate coefficient for the incoming component, with the same bound. Their sum on the physical ray is therefore bounded by 2 min(2,L), or the trivial full-state ceiling when an actual full-state comparison is available. This last statement covers traveling components only: it does not bound the three remaining source amplitudes or claim a full-state comparison. No resonant derivative or T||delta H|| estimate is used.

For any common nonempty hard interval I strictly within the ray band, let p_e=||1_I F_e||_2^2 and p_0 analogously. Both are positive. The raw coefficient estimate is <=L sqrt(p_0). Normalizing once gives

    ||1_I F_e/sqrt(p_e)-1_I F_0/sqrt(p_0)||_2<=min(2,2L).   (5)

To check the factor, decompose using the denominator sqrt(p_0); the additional norm is |sqrt(p_e)-sqrt(p_0)|/sqrt(p_0)<=L. No lower bound on p_0 beyond positivity is needed for this relative estimate. An arbitrary common contractive scalar transmission factor and its exact Jacobian can be included in both packets, with the same conclusion. This does not permit replacing an actual feedback-loaded row by an unchanged scalar transmission without proof.

For small errors L=O(epsilon), uniformly in lambda/j<=1/16 away from chi=1. The theorem therefore supplies a nonzero relative-tolerance neighborhood of critical ratios for scalar packet fidelity. It neither says the critical ratios are unnecessary for every performance objective nor establishes an optimal tolerance.

## 5. Positive physical realization and precision qualification

For the isolated ray use positive exchange blocks on the three source bonds and occupations

    (2j+d0-a1)n0,
    (2j+d1-a1-a2)n1,
    (2j+d2-a2-kappa)n2,
    (j-kappa)n3.

All later occupations vanish. The assumptions eta<=1/16 and epsilon<1/20 imply kappa/j<=sqrt(3*(1/16)*(21/20))<1/2 and a2/j<2*(1/16)*sqrt(21/20)<.13. Even with |d_i|/j<1/320, the displayed occupations are strictly positive. Thus the perturbed finite-range source is realized by real NN positive blocks with the specified diagonals and no extra vacuum scalar.

At the actual attachment, the existing structured port block can instead be

    j(n2+n_port)-kappa(exchange),

which remains positive because kappa<j and preserves the background port load. Add the two internal positive exchange blocks and occupations j+d2-a2 at site 2, 2j+d1-a1-a2 at site 1, and 2j+d0-a1 at site 0. They too are positive. The graph and shared internal system are unchanged; detunings multiply identity. This proves local realizability only, not the attached performance theorem.

Relative errors on a_i^2 or kappa^2 mean comparable relative errors on the positive amplitudes, with square-root conversion. Their absolute required resolution still shrinks with lambda (and sqrt(j lambda) for kappa). Source detunings must be O(epsilon lambda), not merely small relative to j. Exact ratios are relaxed here, but coefficient precision, correlations, shared internal identity and preparation are not derived from native physics.

## 6. Explicit future full-fiber interface

Let D=E-c_att-2j-B, A_i=D-d_i I, P_e=A_0 A_1-a1^2 I and retain the unchanged background kernel G. The exact noncommuting last-source denominator is

    Q_e=P_e(A_2-kappa^2 G)-a2^2 A_0.

With G_ref=m_j(D), define Q_ref,e by the same expression. Direct algebra gives the ordered factorization

    Q_e=Q_ref,e [I-kappa^2 Q_ref,e^-1 P_e(G-G_ref)].       (6)

The last-source recovery is a1*a2 Q_e^-1. The selected reference scalar entry is exactly (1). On that entry (3) applies, and

    ||Q_ref,e^-1 P_e P||
      <=[(1+epsilon)^2+(1+epsilon)/3]
                    /[q(1-chi)sqrt(delta^2+lambda^2)].     (7)

A sufficient loaded inverse condition is that the supremum of the FULL operator norm of the bracket perturbation in (6) is below one. Complementary channels must also have nonzero Q_ref,e entries and their own explicit bound for Q_ref,e^-1 P_e; (7) is not a full-fiber estimate. Energy-weighted background differences may improve (7), but no modified closed-channel numerical margin is asserted here.

Even once (6) is controlled, attached robustness still requires complete outgoing row estimates, both lips and physical windows, wrong-window inputs, the actual prepared omitted spectral state, local/source/core and closed tails, and scalar concentration for the chosen fixed or changed common waveform. A normalized scalar outgoing comparison does not control these by itself. Shared B with vacuum restriction K and actual carrier phases must remain explicit. No old processor runtime, all-output metric, success, finite length or permanent storage theorem is inherited from (4) or (5).

## Exposure and checks needed

I authored the nominal scalar source and several recovery ancestors; root requested the tolerance question and suggested no desired numerical tolerance. This is new author work, not independent checking. The nominal finite-band determinant/no-mass proof is reused at `three_site_product_source/PROPOSAL.md` SHA a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823, separately checked at c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b. The ordered full-fiber conventions are from `three_site_loaded_inverse/PROPOSAL.md` SHA 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 / check 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2. The attachment's positive structured port and unchanged background are from `three_site_actual_attachment/PROPOSAL.md` SHA 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 / check ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d. These unchanged arguments were previously fully read; their scopes are not promoted here.

A distinct check should challenge the determinant expansion, exterior no-mass argument, complex numerator/phase comparison and cutoff normalization, and ensure that the selected estimate (7) is not mislabeled as full-fiber stability. No pole splitting simulation, parameter sweep, scientific execution, numerical optimization, W/Git/PR/checkpoint/prompt/model edit, delegation or publication occurred. Only this proposal was created.
