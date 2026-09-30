# Exact positive continuously forced one-hole reduction

Author discovery proof, not yet independently checked. The target is the actual supplied microscopic law and bare Omega in CONTRACT.md and W1_REDUCTION_CONTRACT.md. The conclusion below is a source-dependent CP reduction with explicit volume cost, NOT the sought uniform weighted residence bound. No computation is used.

## 1. Actual state, imports and quantifiers

Let n=|A| on a safe even cubic torus L>=6. Matter has q=0,+1,-1, normalized integer-spin links have |E|<=S, div E=q-1_A, w_a=1-n_a, W=sum_a w_a, and P_m=1_(W=m). The unchanged compensated law is

 H=delta epsilon^-4[W-epsilon(F+F*)+epsilon^2 C_S],
 L_mu=sqrt(kappa)epsilon^-1 j_mu,
 C_S=sum_a(F_a*F_a-D_(a,S)+D_(a,infinity))Q_gate,a.

Use separately the original resolved signs or original unnormalized coherent edge marks. No grade is measured. Omega fills A with plus charges, leaves B empty, and has E=0. Let rho(t) be its actual full GKSL ensemble, Y the exact order-six local normal-form circuit, and sigma(t)=Y rho(t)Y*. The entire time interval is a fixed physical [0,T], not a fixed fast interval. Constants may depend on fixed positive delta,kappa,K,T and the fixed circuit geometry; they are independent of n,S. Choose 0<epsilon<=epsilon_0 with the uniform local analytic radius. Impose epsilon^2 S(S+1)=delta/K only for the field-weighted conclusions.

The checked inputs are the full DEFECT_LEMMA fbbf36c2 and its original-law circuit/grade construction; actual first-field moment acf0f4ef; positive-forcing bec9ac7d with receipt1138c68f; and the factorial theorem f5e001a7 with receipt388b2674. Their precise used statements are:

 Tr sigma(t)W <= C_T epsilon^2 n,
 Tr sigma(t)Q_U <= C_T |U|epsilon^2 for fixed complete cones U,
 Tr sigma(t)(1+sum_(e in D)|E_e|) <= C_(D,T),                 (1)

and, with f(m)=m(m-1),

 Tr sigma(t)f(W)+integral_0^t Tr sigma(s)D_-^(2) ds
                                               <=C_T epsilon^4 n^2,
 D_-^(2)=kappa epsilon^-2 sum_(mu,r<0)
       J_(mu,r)*J_(mu,r)[f(W)-f(W+r)] >=0.                  (2)

Here J_mu=Yj_muY* and J_(mu,r) is its exact W-grade component. Grade sums in(2) are proof diagnostics, not extra record labels. Equations(1)-(2) hold for the actual ensemble including all later original births, not a separately evolved averaged state.

Every exact J_mu has a fixed finite cone, finitely many W grades independent of n,S, uniform analytic coefficient bounds, J_(mu,+1)=epsilon^2 B_mu+O(epsilon^3), B_mu=-F_a j_mu F_a, and J_(mu,r)=O(epsilon^3) for r>=2. Also J_0=O(epsilon), J_-1=j+O(epsilon^2). The exact grading/circuit parity is

 Xi=(-1)^W,
 Y(-epsilon)=Xi Y(epsilon)Xi,
 J_mu(-epsilon)=-Xi J_mu(epsilon)Xi.                       (3)

These identities are established at fixed spin before applying the combined scaling. The field moment is ordinary and unconditional. It is not the desired hole-conditional moment.

## 2. The exact killed W=1 kernel

Write P for W-grade averaging on operators, Q=1-P, and I for the inverse of [W,.] on nonzero grades. These superoperators are distinct from the state projectors P_m. Both P and I have dimension-independent operator norms: P is an average of unitary conjugations and I is its periodic sawtooth Fourier integral, whose L1 kernel is bounded independently of the number of integer W eigenvalues. Thus a global observable does not introduce an extra factor n in I.

Let H_d=P(H'), H'=YHY*. Define on the GLOBAL W=1 Hilbert space

 H_1=P_1 H_d P_1-delta epsilon^-4 P_1,
 K_mu=P_1 J_(mu,0)P_1,
 E_mu=P_0 J_(mu,-1)P_1.

The subtracted term is scalar on this space and changes no dynamics. The trace-decreasing CP generator on block densities is

 D_epsilon(tau)=-i[H_1,tau]
  +kappa epsilon^-2 sum_mu(K_mu tau K_mu* -{K_mu*K_mu,tau}/2)
  -kappa epsilon^-2 sum_mu {E_mu*E_mu,tau}/2.               (4)

Every same-grade correction in H_d,J_0,J_-1 is retained EXACTLY. The zero-grade recycling has the original mu, including its full sign coherence. The exit is the actual negative-one-grade loss coefficient. Negative grades <=-2 annihilate W1. Equation(4) is a diagnostic killed block; it does not assert that sigma follows it or make its grade choice observable. Denote its CP trace-nonincreasing semigroup by Z_epsilon(t). It is positive on the physical Gauss block, since every factor preserves the actual constraint. Its adjoint is contractive on bounded block observables. Finite S and volume make all these operators finite matrices; no rotor-domain assertion is hidden here.

The exact positive input, evaluated in the SAME actual sigma, is

 I_epsilon(s)=kappa epsilon^-2 sum_mu
             J_(mu,+1)P_0 sigma(s)P_0 J_(mu,+1)*,
 tau_0=P_1 sigma(0)P_1,
 chi(t)=Z_epsilon(t)tau_0+integral_0^t Z_epsilon(t-s)I_epsilon(s)ds. (5)

Each source summand has W1 output and preserves the original mark's internal coherence. Its input is not replaced by Omega, a stationary state, an independent birth model or a diagonal B mask. The function chi is positive and has the exact actual initial W1 block. It depends on sigma_00(s), so(5) is not a closed effective law. No conditional hazard or full history-channel comparison is claimed.

We prove

 sup_(t<=T)||P_1sigma(t)P_1-chi(t)||_1
                                      <=C_T epsilon^4 n^(7/2). (6)

The bound may be larger than one outside its useful window; all powers of n are intentional.

## 3. Global analytic norms and parity

On observables write

 L'^*=epsilon^-4 A+B_epsilon,
 A=i delta[W,.],
 B_epsilon=epsilon^-2 B_2+epsilon^-1 C_1+B_0+O(epsilon),
 B_2=i delta[D2,.]+kappa sum_mu D[j_mu]^*,
 D2=C_S+[F,F*].                                           (7)

B_2 preserves every grade. The complete C_1 contains both original polarized gains and both anticommutator terms with j1=A_mu+D_mu, A_mu=j_mu F_a-F_a j_mu, D_mu=[F*,j_mu]. It is not a recycling-only map. The exact H' normal form has an O_local(epsilon^3) off-grade remainder, included in B_epsilon.

The sum has O(n) fixed-cone terms of uniformly bounded complete norm and uniformly bounded local Taylor coefficients. Therefore, on the full bounded-operator space,

 ||B_epsilon||<=C n epsilon^-2,
 ||B_j||,||C_1||<=C n for each fixed coefficient used below. (8)

The same statements hold for analytic remainders after extracting their displayed epsilon power. They follow from the finite local cones and triangle inequality over terms; no global analytic bound for Y-I is used. The global diagonal compensation may be extensive but its normalized coefficients are uniformly bounded in S.

Extend a block test O=P_1OP_1 by zero to the full carrier. Write D^* for the adjoint of(4), with its result similarly zero-extended. It preserves this block, has norm <=C n epsilon^-2, and on this block its analytic expansion has the form

 D^*=epsilon^-2 D_(-2)+D_0+O(epsilon^2),
 ||D_(-2)||,||D_0||<=C n.                                (9)

There is no epsilon^-1 term. Indeed H_d is even under epsilon -> -epsilon on a neutral block, J_0 is odd in epsilon, and J_-1 is even. The scalar epsilon^-4 term has zero commutator. Projection onto W1 has norm one and adds no volume factor. Analytic expansions below are expansions of linear maps; they are uniform over the test unit ball. The backward test itself need not have an epsilon-independent Taylor series.

For an arbitrary X satisfying P_0XP_0=0, positivity and Cauchy-Schwarz give

 |Tr sigma X| <=||X||[p+2sqrt(p)],
 p=Tr sigma(1-P_0)<=C_T epsilon^2 n.

Using p<=1 as well, this is at most C_T epsilon sqrt(n)||X||. For a neutral X with P_0XP_0=0 there are no P_0/Q_0 cross blocks, giving the stronger bound C_T epsilon^2 n||X||. These are GLOBAL prices; no local volume replacement is made.

## 4. Exact retarded homological identity

For a neutral W1 block test define linear maps

 K1(O)=(i epsilon^4/delta)I Q L'^*O,
 K2^D(O)=(i epsilon^4/delta)I Q[B_epsilon K1(O)-K1(D^*O)].   (10)

They are off-grade. Equations(8)-(9) imply

 ||K1(O)||<=C epsilon^3 n||O||,
 ||K2^D(O)||<=C epsilon^5 n^2||O||.                        (11)

For a fixed final time t and Hermitian block O, set O_s=Z_epsilon^*(t-s)O. Then ||O_s||<=||O||, O_s=P_1O_sP_1, and dot O_s=-D^*O_s. Direct substitution, using epsilon^-4 A K1=-Q L'^* and the defining equation for K2^D, gives EXACTLY

 (partial_s+L'^*)[O_s+K1(O_s)+K2^D(O_s)]
  =(P L'^*-D^*)O_s+P B_epsilon K1(O_s)
                    +B_epsilon K2^D(O_s)-K2^D(D^*O_s).   (12)

This absorbs the fast derivative algebraically. In particular we do not bound integral||dot O_s||, invoke a uniform fast gap, or assume that the backward observable remains spatially local. The global norm cost has already been exposed in(8)-(11).

Expand K1=epsilon^3 k3+epsilon^4 k4+O(epsilon^5 n), with k3=(i/delta)I C_1 and coefficient norms <=C n. Since P B_2 K1=0 exactly and the complete covariance(3) kills odd powers after neutral projection,

 P B_epsilon K1(O)=epsilon^2 T_O+O(epsilon^4 n^2||O||),
 T_O=P C_1 k3(O).                                       (13)

No epsilon^3 neutral term remains. To see the crucial filled-block cancellation without importing a positivity guess, put V=sum_mu j_mu*A_mu. The actual identities j_mu P_0=D_mu P_0=0 and A_mu P_0 mapping into W0 yield

 (C_1O)P_0=-(kappa/2)O V P_0,
 k3(O)P_0=-i kappa O V P_0/(2delta),
 P_0 k3(O)=+i kappa P_0V*O/(2delta).

Both gains in P_0C_1(k3(O))P_0 vanish because their outer bare j kills P_0. Its two losses are opposite imaginary copies of P_0V*OVP_0 and cancel. Thus P_0T_OP_0=0. T_O is neutral, so T_O=(1-P_0)T_O(1-P_0), with norm <=C n^2||O||. Its actual expectation in(13) is therefore <=C_T epsilon^4 n^3||O||, including the displayed remainder.

For the last two terms of(12), K2^D=epsilon^5 l5+O(epsilon^6 n^2), where

 l5=(i/delta)I Q(B_2 k3-k3 D_(-2))

has norm <=C n^2 and is odd on neutral inputs. Consequently

 B_epsilon K2^D(O)-K2^D(D^*O)
   =epsilon^3 U_O+O(epsilon^4 n^3||O||),
 U_O=B_2 l5(O)-l5(D_(-2)O),                             (14)

with ||U_O||<=C n^3||O|| and odd Xi parity. In particular P_0U_OP_0=0. Equation(1) and the global Cauchy bound then give

 |Tr sigma[the remainder in(14)]|
                                   <=C_T epsilon^4 n^(7/2)||O||. (15)

At either endpoint the exact off-grade maps in(11) obey P_0K_iP_0=0, hence

 |Tr sigma K1(O_s)|<=C_T epsilon^4 n^(3/2)||O||,
 |Tr sigma K2^D(O_s)|<=C_T epsilon^6 n^(5/2)||O||.          (16)

Together(12)-(16) give an integrated functional error C_T epsilon^4 n^(7/2)||O||. The endpoint estimates, feedback and retarded remainder use the ACTUAL sigma at the corresponding times. No averaged-state rare-hole theorem is substituted.

## 5. Exact neutral block decomposition and factorial sink

The full neutral average of the original dissipator has equal exact grades, with no change to mu. Test it against O_1=P_1O_1P_1. After subtracting the W1 operator D^*O_1 from(4), the remaining expectation is the sum of:

 (a) Tr I_epsilon(s) O_1, the positive W0 -> W1 source in(5);
 (b) incoming gains from W=m>=2 to W1, using r=1-m<0;
 (c) positive-grade loss from W1 to higher W.

This is an exact decomposition. The neutral Hamiltonian acts separately on every W sector, so its contribution outside W1 is zero and its W1 contribution is retained in D. Grade-zero gains cannot enter W1 from another sector. Nonpositive grades <=-2 cannot leave W1. Unequal-grade terms of the full original generator have not been discarded: they are precisely the terms controlled by(10)-(16).

For (b), the incoming density is positive. Its total integrated trace is bounded by half the sink in(2), because each transition m -> 1 lowers f by f(m)-f(1)=m(m-1)>=2. Therefore its absolute pairing with O_s costs at most C_T epsilon^4 n^2||O||. This prices actual continuously generated multihole input, not just its preparation.

For (c), set A_+=P_1 sum_(mu,r>0)J_(mu,r)*J_(mu,r)P_1. The fixed-cone grade bounds imply ||A_+||<=C epsilon^4 n. The term is -kappa epsilon^-2{A_+,O_1}/2. We bound its expectation by

 kappa epsilon^-2 ||A_+||||O_1|| Tr(P_1sigma P_1)
                                       <=C_T epsilon^4 n^2||O||. (17)

This uses an operator norm times the block trace. We do NOT assert that a Jordan product is positive, or dominate its absolute expectation by a noncommuting activity without proof.

Integrating(12), moving the correction endpoints with(16), and using(a)-(c), proves

 |Tr O P_1sigma(t)P_1-Tr Z^*(t)O tau_0
       -integral_0^t Tr Z^*(t-s)O I_epsilon(s)ds|
                                      <=C_T epsilon^4 n^(7/2)||O||.

Duality over all Hermitian W1 block tests of norm at most one gives(6). Spectator coherences and physical Gauss sectors are included throughout. The theorem is unconditional block trace norm; it is not advertised as a complete multievent channel theorem.

## 6. Actual source resources and fresh field price

The exact inputs in(5) satisfy

 Tr tau_0<=C epsilon^2 n,
 Tr I_epsilon(s)<=C epsilon^2 n,                           (18)

uniformly in s<=T. The first follows from(1), the second from the O(epsilon^2) norm of each J_+1 and O(n) original marks. Therefore Tr chi(t)<=C_T epsilon^2 n by CP trace contraction. This alone is not a weighted-residence estimate.

For q_h=1+sum_(dist_1(a(e),h)<=2)|E_e| and R_1=P_1 sum_h w_h q_h, one has

 Tr R_1 tau_0<=C epsilon^2 n,
 Tr R_1 I_epsilon(s)<=C_T epsilon^2 n.                    (19)

Here are uniform proofs, including the exact circuit and its nonpolynomial tails. For a finite cone U put Q_U^E=1+sum_(e in U)|E_e|. A bounded finite-shift word of bandwidth d obeys a weighted Schur bound with weight ratio at most sqrt(1+d). Every coefficient of each fixed-order gate has finitely many such words with bounded row/column sums; diagonal normalized compensation commutes with the weight and is uniformly bounded. Weighted products and the exponential series therefore give uniform analytic weighted bounds for the finite circuit cones and exact conjugated jumps. Grade averaging commutes with Q_U^E. Since the +1 jump coefficients at orders zero and one vanish, on complete input/output cones

 ||(Q_U^E)^(1/2) J_(mu,+1) (Q_U^E)^(-1/2)||
                                                     <=C epsilon^2. (20)

Enlarge U by the fixed reward halo. On the output of J_(mu,+1)P_0 there is exactly one hole and it lies in that jump's A cone. Thus R_1 on this output is bounded by the enlarged Q_U^E, up to a fixed incidence constant. P_0 commutes with Q_U^E. Taking positive traces in(20), then using the ordinary local field bound(1), proves the second inequality in(19) after summing O(n) centers. No inverse spin shift is used; boundary zeros reduce the finite-word bounds.

For the initial input the same weighted local-circuit argument applied to X_h=sqrt(w_h q_h) gives

 ||[X_h,Y*](Q_U^E)^(-1/2)||<=C epsilon,
 Y(w_h q_h)Y*<=2w_h q_h+C epsilon^2 Q_U^E,                (21)

and likewise with Y and Y* reversed. The global factor in [X_h,Y*]=Y*(YX_hY*-X_h) is unitary; only the local conjugation difference is assigned a weighted Schur norm. In Omega the first term vanishes and the enlarged field weight is one. Sum the reverse version of(21), and use R_1<=sum_h w_h q_h, to obtain the first inequality in(19). This also derives the needed preparation price without estimating a global norm of Y-I.

Equation(19) controls only the field at injection. It does not say that Z preserves that weight or has bounded lifetime. In particular trace contraction in(18) cannot be applied to the unbounded-spin reward to infer its residence.

## 7. Exact weighted consequence and physical return

There are at most114 links in the specified reward halo, since the A endpoints within graph distance two consist of one center and18 neighbors. On W1 exactly one w_h is nonzero, so

 0<=R_1<=(1+114S)P_1.

From(6) and the stipulated spin scaling,

 |epsilon^-2/n integral_0^T Tr R_1[sigma(t)-chi(t)]dt|
                                        <=C_T epsilon n^(5/2). (22)

No first-field moment is used to replace this finite-spin norm price. The narrower growing-volume window epsilon n^(5/2)->0 makes the comparison vanish. If epsilon n^(5/2) is merely bounded, it supplies a bounded comparison cost. At fixed n it also tends to zero. No arbitrary-volume local theorem follows.

The checked factorial theorem independently gives for R_multi=1_(W>=2)sum_h w_h q_h

 epsilon^-2/n integral_0^T Tr sigma(t)R_multi dt<=C_T epsilon n. (23)

Consequently the exact remaining positive kernel consumer is

 epsilon^-2/n [integral_0^T Tr R_1 Z(t)tau_0 dt
   +integral_(0<=s<=t<=T) Tr R_1 Z(t-s)I_epsilon(s)ds dt]
                                                       <=C_T. (24)

In the window with epsilon n^(5/2) bounded, (24) is equivalent to bounded actual ROTATED full first-field residence, up to the bounded errors(22)-(23); in the vanishing window the comparison error vanishes. It is a target-equivalent remaining inequality, not a theorem of this packet. Every occurrence of the actual source and exact same-grade corrections in(24) is mandatory.

For a physical sufficient conclusion, sum the positive-form estimate(21), use the ordinary first moment in sigma and bounded cone incidence, and integrate:

 epsilon^-2/n integral_0^T Tr rho sum_h w_h q_h
 <=2 epsilon^-2/n integral_0^T Tr sigma sum_h w_h q_h+C_T.   (25)

The reverse estimate follows with the corresponding physical ordinary moment. This is a bounded-cost coordinate return for the FULL local sum, not a claim that the physical and rotated globally-one-hole projectors agree. It does not give a vanishing weighted return error. Thus a proof of(24) would supply the requested physical sufficient residence in the declared volume window, and then the already checked signed quadratic-current reduction could be used at its own scope. No such kernel bound is supplied here.

## 8. Why the remaining kernel is substantive

The original total particle number changes by two per original birth and is preserved by H and Y. From Omega N_particles=n+2R. On W1, N_A=n-1, hence N_B=2R+1. Zero-grade original recycling in(4) increases N_B by two while staying in W1; the neutral Hamiltonian preserves total N_B but can reshape its mask. Thus the retained kernel includes arbitrarily many later marks and evolving backgrounds up to the finite carrier capacity. It is neither a static-B nor a first-event-only approximation.

Mass(18) and fresh field(19) do not pay field transport or residence after injection. The global event-number identity gives no local cluster distribution. A fixed-global-k response is unavailable for dense periodic backgrounds, and fixed-fast-U convergence says nothing about t-s of physical order one. The separate kinetic discriminator in this directory tests a possible velocity mechanism but is not a probability law for sigma. The reduction(6) removes a coherent forcing ambiguity at an explicit volume price; it does not close(24), the quadratic-energy mean/tails, weighted W1 convergence, full microscopic generator, or uniqueness. Supplied carrier/law/preparation/clock/couplings remain imports, not foundation selections. No formal review or audit status is asserted.
