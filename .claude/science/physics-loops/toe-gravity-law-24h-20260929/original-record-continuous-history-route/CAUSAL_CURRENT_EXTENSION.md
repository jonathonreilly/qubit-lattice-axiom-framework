# Causal local state measures and original marked currents

Root author extension under the separately frozen causal-current contract. Both this proof and the base history proofe7456832 are UNCHECKED candidates. They may be jointly reviewed, but neither is yet an adopted downstream premise. No new scientific computation is asserted.

Keep exactly the base contract: actual compensated finite-spin law, bare Omega, fixed positive couplings and coupled spin scaling, safe even tori with arbitrary growing volume, a fixed finite original monitored mark set J and horizon T. All unobserved gains and every loss remain present. Resolved and coherent instruments are separate cases. Write H_T for the base event-list space including closed simplexes. Its elements record actual ordered original marks and times. For h in H_T, r_t(h) deletes events at times greater than or equal to t. Thus r_t is the STRICT past. The limit P supplied by the base candidate is simple, has no events at fixed deterministic times and has finite first count moment. Its actual microscopic approximants have uniformly integrable first count moments along the chosen sequence.

## 1. Exact causal operator-valued measures

At finite spin and volume let eta_epsilon,t(dh) be the positive unnormalized quantum history measure for the original observed events strictly before t, with all unobserved evolution included. It is constructed by the actual gain insertions and no-observed-event propagation stated in the base proof. Its quantum marginal is exactly rho_epsilon(t), and its scalar trace is the law of r_t(H_epsilon). Values at a single event time do not affect dt integrals. There are only finitely many total births at each finite volume, so these positive matrix-valued densities are ordinary finite sums over mark words and time simplexes. No trace-class diagonal on a nonatomic Hilbert register is assumed.

For any fixed local quantum region X, zero-extend the spin fields into its common rotor carrier and take the partial trace. Define the finite positive trace-class-valued measure on [0,T] x H_T

 K_epsilon,X(dt,dh)=dt eta_epsilon,t,X(dh).                   (C1)

Its total trace is T. Its scalar trace is the SAME measure lambda_epsilon for every X. For a fixed finite-rank local field cutoff P_R, the actual first-field estimate gives

 int Tr[(1-P_R)K_epsilon,X] <= C_X,T/R.                      (C2)

The total count in h is at most N_epsilon(T). Thus the scalar mass on histories longer than M is at most T K_T/M. Compactness of the finite-length simplexes and compactness of [0,T] give tightness. The integrated gentle estimate now has the finite-mass form

 ||K_epsilon,X-P_R K_epsilon,X P_R||_variation,1
                  <=2 sqrt(T C_X,T/R).                    (C3)

Here variation,1 is the total variation norm of a trace-class-valued measure, bounded by the integral trace norm for its actual density. This is an unconditional integrated tail; there is no uniform conditional field moment on rare histories.

The finite-rank matrix-measure compactness proof in the base candidate applies to K, as well as to terminal Q. Diagonalize over R and a countable exhausting family of local regions, while retaining the same history-law subsequence P and the base uniform-time local state subsequence. It yields positive local measures K_X, mutually consistent under partial trace, and terminal Q_T,X. For every bounded operator-norm-continuous test A(t,h) on the indicated finite region,

 int Tr[A K_epsilon,X] -> int Tr[A K_X].                    (C4)

Finite-rank approximation plus tightness proves the whole stated test class, rather than only fixed matrix entries. No global trace-class infinite-volume state is claimed.

## 2. The scalar time/past measure is determined by P

For any bounded continuous scalar f(t,h),

 int f d lambda_epsilon
       =E_epsilon int_0^T f(t,r_t(H_epsilon))dt.              (C5)

The map h -> int f(t,r_t(h))dt is continuous at every simple history with interior distinct event times. Indeed, for a convergent fixed-length/fixed-word sequence, discard intervals of arbitrarily small total length around its finitely many event times. On each remaining compact time interval the same prefix is selected, the prefix time coordinates converge, and f is uniformly continuous on the resulting compact set. The discarded integral is at most its length times ||f||. Boundedness then proves convergence of(C5) under P_epsilon -> P, since P has the required full-measure continuity set.

Consequently every K_X has scalar trace

 lambda(dt,dh)=dt Law_P(r_t(H))(dh).                         (C6)

This argument prevents a spurious independently chosen past-history law. It also shows lambda is supported on histories all of whose event times are strictly smaller than t, up to a null set; for each finite H its event times occupy zero dt measure. In particular no state mass at t equal to its last observed event is introduced by the compactification.

A positive trace-class-valued measure dominated by its scalar trace has a positive trace-one density. One direct construction uses all finite-rank matrix-entry Radon-Nikodym derivatives against lambda, imposes positivity on a countable dense set of finite rational vectors, and uses the increasing finite-rank traces to obtain a trace-class matrix with trace one almost everywhere. Thus

 K_X(dt,dh)=sigma_X(t,h)lambda(dt,dh),
 sigma_X(t,h)>=0, Tr sigma_X(t,h)=1.                         (C7)

Countably many local regions allow a common exceptional null set on which to impose all partial-trace consistencies. These are actual subsequential local conditional states at dt-almost-every time and past history. Their unconditional marginal equals rho_X(t)dt: this follows by testing(C4) with f(t)A_X independent of h and using the previously checked uniform-time local-state convergence. This does not construct a quantum evolution equation or uniqueness of sigma.

## 3. Gain matching on actual continuous causal densities

Write L_mu,epsilon=sqrt(kappa)epsilon^-1 j_mu and B_mu,S=sqrt(kappa)j_mu F_a for the ACTUAL original mark mu. Both operate on a fixed support U_mu. For any finite output region X, use Z containing X and U_mu. The exact causal post-event current is the positive trace-class-valued measure

 I_epsilon,mu,X(dt,dh)
      =dt Tr_(Z minus X)[L_mu eta_epsilon,t,Z(dh)L_mu*].     (C8)

It is indexed by event time and PRE-event observed history. Appending the same original mark and time is a deterministic map of this measure, not a changed observation. Its scalar trace is the usual expected actual mu event measure.

The G2 estimate extends to these causal densities without a fictitious continuous Hilbert register. At every finite volume choose their actual simplex/word dominating measure. Let E_mu=L_mu-B_mu,S. Integrating the squared Hilbert-Schmidt error over history gives EXACTLY

 int ||E_mu eta_epsilon,t(h)^(1/2)||_2^2 dh
             =Tr[rho_epsilon(t) E_mu*E_mu].                 (C9)

The analogous L and B squares likewise integrate to their actual marginal activities. Factor the gain difference as E eta L*+B eta E*, integrate its trace-norm bound, and apply Cauchy-Schwarz over time AND history. The checked G1 and actual D3 therefore give

 ||I_epsilon,mu,X
   - Tr_(Z minus X)[B_mu,S K_epsilon,Z B_mu,S*]||_variation,1
                       <= C_mu,T epsilon.                 (C10)

The estimate includes all histories and all times in one error. This is an integral inequality for positive causal operator-valued densities with the correct actual marginal, not an assumption about conditional holes or microscopic hazards.

The checked common-carrier finite-word estimate gives the quadratic form bound

 (B_mu,S-B_mu,infinity)*(B_mu,S-B_mu,infinity)
       <= C_mu/S [1+sum_(e in U_mu) |E_e|].                 (C11)

This includes zero extension outside the spin box and the entire coherent source word. The ordinary first-field moment in K_epsilon and gain factorization yield

 ||B_mu,S K_epsilon,Z B_mu,S*
       -B_mu,infinity K_epsilon,Z B_mu,infinity*||_variation,1
                           <= C_mu,T S^(-1/2).             (C12)

All terms here are integrated over actual time/past histories. No weighted microscopic post-jump moment is needed for(C10)-(C12). The positive B comparator and its bounded finite shifts give quantum tightness of the currents; the small variation error transfers it asymptotically to I_epsilon.

For any bounded operator-norm-continuous test A_X(t,h), the pullback
 B_mu,infinity* (A_X(t,h) tensor I) B_mu,infinity
is bounded and operator-norm-continuous on Z. Hence(C4), (C10) and(C12) identify the weak current limit:

 I_mu,X(dt,dh)
   =Tr_(Z minus X)[B_mu,infinity sigma_Z(t,h) B_mu,infinity*]
                                                        lambda(dt,dh). (C13)

The same complete original mark appears in the state, current and append map. No split observation of coherent signs, effective trajectory replacement or different source is used. The limit is a measure with mass equal to a mean count, not a normalized channel output.

## 4. Conditional intensity in the SAME limiting past-conditioned state

For bounded continuous scalar f(t,h), the actual identity is

 int f Tr I_epsilon,mu
       =E_epsilon sum_(mu events j) f(t_j,r_(t_j)(H_epsilon)). (C14)

On simple interior finite histories the sum is a continuous functional of the event list. It is bounded by ||f|| N_epsilon(T); the count uniform integrability proved in the base candidate permits passage to P. Taking the trace of(C13) therefore gives equality of finite measures:

 E_P sum_(mu events j) f(t_j,r_(t_j)(H))
    =int f(t,h) Tr[B_mu,infinity* B_mu,infinity sigma_Umu(t,h)]
                                                        lambda(dt,dh). (C15)

Bounded continuous tests determine finite Borel measures on the metric time/history space. Thus(C15) extends to bounded measurable tests. Define

 a_mu(t,H)=Tr[B_mu,infinity* B_mu,infinity
                             sigma_Umu(t,r_t(H))].          (C16)

The strict-past process t -> r_t(H) is left continuous in the event-list topology, with right limits, on every finite simple event history; t is continuous. It is adapted to the natural observed-history filtration. Its composition with a Borel density in(C7) is therefore predictable. The density may be chosen Borel up to a lambda-null set; pulling it back preserves dt P null sets. The uniform word bound gives0<=a_mu<=||B_mu,infinity||^2<=lambda_mu.

Equation(C15) on predictable rectangles H_s 1_(s,t] now proves
 N_mu(t)-int_0^t a_mu(u,H)du
is a martingale in that natural filtration. Thus the bounded limiting compensator in the base proof is identified with the ORIGINAL formation word in the SAME limiting past-conditioned local quantum state. It is not the hazard of a separately solved autonomous B process. Different subsequences can still select different quantum conditional states or histories because the full limiting quantum dynamics is unresolved.

This identification is only dt P almost everywhere. It gives no pointwise finite-epsilon conditional-rate convergence, no uniform claim on rare normalized postselected states, and no continuous-timestamp total-variation convergence. Nor does it impose an independently chosen prior on the conditional quantum state. Only actual causal instruments generate the measures used above.

## 5. Scope and interaction with the remaining hard residual

The joint weak history/current extraction adds the precise local source law to the limiting compensator and identifies instantaneous post-event quantum payloads against continuous time/past tests. It composes the actual G2, first-field and rotor-word estimates with the base candidate's uncapped count UI. It does not identify the no-event Hamiltonian, the fast dark-hole exterior flux, a full conditional quantum evolution, or a unique infinite-volume process. Terminal Q_T and averaged K are simultaneous subsequential limits; a quantum propagator relating different times has not been proved.

This is a consequence inside the supplied compensated spin model. The carrier, dynamics, source, preparation and clock remain explicit imports. Neither this extension nor the base candidate implies a current-axiom contradiction, physical-law selection, formal retained status or a completed TOE. A focused independent full proof check remains required before use.
