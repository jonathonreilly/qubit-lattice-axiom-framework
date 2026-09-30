# Bounded original-history register balance in the same microscopic state

Author analytic discovery lemma, awaiting a focused independent check. This extends the checked unconditional mean-mark identity to arbitrary bounded tests of one fixed finite capped/binned ORIGINAL history register. It uses the checked DEFECT and MEAN_MARK_BALANCE mechanisms. It does not assume the new time-compactness theorem, a fast gap, source clustering, a field moment, a weighted preparation, or the new weighted-source-component estimate. The actual microscopic law, bare Omega, energy, Gauss sector and labels remain unchanged.

## 1. Exact output and target identity

Fix a finite set F of monitored A centers, finitely many time-bin intervals on[0,T], and a count cap M. The classical register Z records the original labels with their bin tags and within-history order. On overflow it retains an absorbing flag, while the system continues to evolve. Either the original resolved instrument or the original unnormalized coherent-edge instrument is used separately. Write eta(t) for the EXACT joint microscopic quantum/register state, and g for any real bounded function of the register, including its overflow outcome. Let T_(mu,t)g(z)=g(append_(mu,bin(t))(z)) be the true register update for a monitored original mark mu. At overflow this is g(overflow). All update maps have norm one on the classical supnorm algebra.

For mu at a define the same full-carrier physical source word as in the checked mean theorem,

    Bhat_mu=j_mu F_a,
    Delta_(mu,t)g=T_(mu,t)g-g.

No dynamics using Bhat is evolved. Let b be the number of fixed bin boundaries in the interior of[0,T]. There are C_F,epsilon0 independent of spin, safe torus volume, cap M and g such that

 sup_(0<=t<=T) | E g(Z_t)-g(empty)
       -kappa integral_0^t sum_(mu centered in F)
          Tr[eta(s)(Bhat_mu*Bhat_mu tensor Delta_(mu,s)g)]ds |
 <= C_F ||g||_infinity
          [epsilon²(1+T)²+epsilon³(1+b)].                       (R1)

Constants depend on the fixed couplings, finite pattern geometry and original mark family; the finite-color construction is the same checked one. Coupled spin/epsilon scaling is allowed, but no field estimate is needed. All later births and every original same-mark coherent contribution are present. The formula concerns bounded functions of the entire recorded capped word, rather than just its count or final bin.

Equivalently, for each mu let the positive register measure

    nu_mu(s;z)=Tr_system[eta_z(s) Bhat_mu*Bhat_mu].

The classical register marginal tau obeys the approximate integrated vector identity

 ||tau(t)-tau(0)-kappa integral_0^t
           sum_mu (append_(mu,s)*-I)nu_mu(s)ds||_(ell1)
 <= C_F [epsilon²(1+T)²+epsilon³(1+b)].                       (R2)

Trace/supnorm duality in this FINITE classical space gives(R2) from the uniform bound(R1). This is a same-joint-state identity. In general nu_mu is correlated with the quantum state and the recorded past, so(R2) is not a closed classical generator and does not identify a microscopic conditional hazard. It does not replace eta by an effective state or assert a quantum post-mark map comparison.

## 2. Copying every translated monitored pattern for the proof

The defect estimate for negative-grade loss is global, and the normal-form coloring need not preserve translations. A single monitored register cannot justify dividing a colored local loss estimate by volume. We avoid that mistake as follows.

On one finite torus attach, as mathematical bookkeeping, a register Z_x for EVERY A-sublattice translation x of the fixed pattern F. Each reads the SAME physical original event history restricted to x+F, with labels expressed in that translated pattern's coordinates. These registers have their exact joint correlations; they are not independent samples or new physical apparatus. The full original finite-volume marked process supplies this joint classical extension directly. It leaves the system marginal unchanged. A physical mark at a updates exactly those pattern registers for which a lies in x+F, at most |F| of them. Other registers are left untouched. The deterministic simultaneous update has a complete Kraus column with sum V_z*V_z=I. Consequently the physical grade-loss sum in this enlarged classical extension is still D_minus tensor I, with no multiplicity in the actual jump law.

Use the extensive test

    G=sum_x g(Z_x),  n=|A|.

The generator is linear, so each term retains the one-register anchor x+F. A finite number of generator actions, grade projections or homological inverses enlarges only its quantum neighborhood and bounded incidence. The support/mark counts depend on F and the fixed circuit order, not n or M. Complete gain/loss cancellation removes unmonitored terms disjoint from that anchor; terms updating its register must all be kept, including those outside its current quantum support. Cross-map norms are bounded by the Kraus-column/supnorm contraction, independently of the potentially huge copied-register dimension.

Only AFTER returning observables to physical coordinates will translation covariance be used. The physical law, bare Omega and blank copied-register preparation are translation covariant, with translations permuting the register indices. This is enough to divide both physical sides by n. No covariance of Y, sigma or its grade-resolved rates is assumed.

## 3. Exact original generator and diagnostic grades

Extend the checked circuit Y by identity on every register. Put sigma_joint=Y eta_all Y* and J_mu=Y j_mu Y*. At any time within a bin the EXACT original registered generator acts on G as

    Lambda_G=L'^*G
       =kappa epsilon^-2 sum_(physical mu) J_mu*J_mu tensor d_mu,
    d_mu=sum_(x: center(mu) in x+F) Delta_(mu,t)g(Z_x).          (R3)

The tensor notation means the commuting quantum coefficient and displayed classical function. In particular ||d_mu||<=2|F| ||g||. Hamiltonian terms vanish on G. All same-mark coherence is still inside J_mu*J_mu. Grade averaging is a diagnostic matrix identity,

    P_W Lambda_G=kappa epsilon^-2 sum_(mu,r)
                                   J_mu,r*J_mu,r tensor d_mu.  (R4)

It is not a recorded grade split.

For r<0, positivity and |d_mu|<=2|F| ||g|| give

 | integral_0^t <negative part of(R4)> ds |
 <=2|F| ||g|| integral_0^t <D_minus> ds
 <=C_F ||g|| epsilon² n(1+t).                                (R5)

The system marginal of sigma_joint is exactly the original rotated marginal, so the checked D10 applies. There is no conditional rare-hole or conditional loss assumption. Each positive-grade J_mu,r starts at epsilon² in the uniform local expansion; their contribution in(R4) is bounded by C_F ||g|| epsilon² n t.

The complete grade-zero coefficient satisfies, as proved in the mean theorem,

    J_mu,0=epsilon A_mu+O_local(epsilon³),
    A_mu=j_mu F_a-F_a j_mu.                                  (R6)

The absent quadratic grade-zero coefficient follows from W-grade parity of the first two circuit orders. Neighboring F_c with c!=a commute with j_mu: if they share a B factor both products have two record creations there and vanish, while otherwise their local factors commute. The grade0 first coefficient is therefore the complete displayed word. Coherent signs remain inside j_mu. Uniform column norms give

 kappa epsilon^-2 sum_mu J_mu,0*J_mu,0 tensor d_mu
       = kappa sum_mu A_mu*A_mu tensor d_mu
                                           +O_local,F(epsilon² ||g||).

Its extensive norm error is <=C_F n epsilon²||g||.

## 4. Entire off-grade potential with every register update

Let R_G=(1-P_W)Lambda_G. It is an exact Hermitian interaction sum of local strength O_F(epsilon^-1||g||). The bare potential j_mu*j_mu has grade0, and the leading mixed jump coefficient has grades +/-1. Higher same-mark cross terms are retained in R_G. The exact registered adjoint generator is

    L'^*=i delta epsilon^-4[W,.]+B_epsilon,
    B_epsilon=epsilon^-2 B2+O_local,F(epsilon^-1),

and B2 preserves grades because register updates carry no W grade. Define within each fixed bin

    K1=(i epsilon^4/delta) I_W R_G,
    K2=(i epsilon^4/delta) I_W(1-P_W)B_epsilon K1.

Their local strengths are O_F(epsilon³||g||) and O_F(epsilon^5||g||). The exact identity, with complete registered gains AND losses in every action, is

    L'^*(K1+K2)=-R_G+P_W B_epsilon K1+B_epsilon K2.

The apparent epsilon term vanishes by P_W B2 K1=0. The residual has local strength O_F(epsilon²||g||). Summing bounded incidence gives the signed-integral bound

 |integral_0^t <R_G> ds|
 <=C_F n ||g|| [epsilon³(1+b)+t epsilon²].                    (R7)

To check the b factor, integrate separately on the fixed bin intervals. K1,K2 may change when the append label changes, so their endpoint terms have at most b internal jumps plus the two exterior endpoints, each bounded by C_F n epsilon³||g||. The joint registered state itself is continuous there. No derivative of a cumulative mean estimate is being assumed. This is not a bound on the integral of the absolute off-grade activity.

## 5. Return to the physical joint state and original Bhat word

Each summand of the neutral source is a bounded local grade-zero quantum coefficient times a bounded function of one copied register. The circuit acts only on the quantum factor. For such O, its first conjugation correction has grades +/-1 and norm <=C_F||g||; its compression to the fully occupied local A neighborhood vanishes. The actual joint state's hole probability in that neighborhood is the system marginal's checked O(epsilon²(1+t)). Cauchy--Schwarz on the occupied/hole blocks, followed by the explicit epsilon in the circuit expansion, gives

    |<O>_sigma_joint-<O>_eta_all|
                   <=C_F ||g|| epsilon²(1+sqrt(1+t)).          (R8)

This applies to A_mu*A_mu tensor each Delta g. It uses neither a bound on a state conditioned on its history nor colored translation symmetry. Summing the n|F| finite-incidence terms preserves the stated extensive order.

As exact physical occupancy blocks,

    Bhat_mu=j_mu F_a=n_a Bhat_mu n_a,
    D_mu=F_a j_mu=w_a D_mu w_a,
    A_mu=Bhat_mu-D_mu,
    A_mu*A_mu=Bhat_mu*Bhat_mu+D_mu*D_mu.                       (R9)

These identities still hold after multiplying by any classical Delta g. Mixed terms vanish algebraically by A occupancy, not by observing an extra label or dephasing signs. Since D_mu*D_mu<=C w_a, its signed register-weighted expectation has magnitude <=C||g|| times the physical local-hole probability. Thus the integrated difference between the A*A and Bhat*Bhat expressions is <=C_F n||g|| epsilon²(1+T)², including(R8).

Combine the exact Dynkin identity for G with(R4)-(R9). Both remaining sides are now PHYSICAL observables of the copied-register process. Translation covariance of that exact process makes each translated pattern have the same expectation and same source-integral value. Divide by n and discard all registers except the chosen one; their marginal is precisely eta in section1. This proves(R1), uniformly over every bounded g, and hence(R2).

## 6. Limits and consumer

The result identifies a bounded integrated register-generator expression evaluated in the SAME joint microscopic state. It controls history-dependent bounded tests, whereas the earlier mean theorem controlled only unconditional cumulative counts and deterministic time weights. The new proof does not assert that kappa Bhat*Bhat is the true finite-epsilon conditional hazard: the actual source rates vanish initially at Omega while the leading Bhat rates do not. Nor is(R1) a pointwise time derivative or an uncapped unbounded-count identity. Bin-switch errors and all initial-layer corrections are explicit.

A future compact local-state limit could use(R2) together with an independently justified limit of the bounded Bhat observables to characterize its register marginal. This lemma alone does not supply that convergence, identify the quantum dynamics, or justify a closed classical Markov law. Continuous timestamps, the original quantum post-mark instrument, positive-time source clustering, weighted-hole W1 and changing-source coherent fast feedback remain separate. The full microscopic Hamiltonian and original energy ledger have not been replaced. No new computation or formal review is claimed.
