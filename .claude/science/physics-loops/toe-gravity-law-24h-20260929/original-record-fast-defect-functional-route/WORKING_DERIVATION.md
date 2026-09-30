# Pre-control analytic derivation

This is authored work awaiting focused independent checking. No neutral-dissipator or pending generator-identification theorem is used. The source inputs are the full actual normal form/DEFECT, original gain balance and their checked local bounds. The scalar spin parameter is Cspin=S(S+1); delta remains the supplied energy constant.

Let P_U be the all-A-occupied projection in a finite support U and Q_U=1-P_U. Test uniformly bounded local families A=A_S with [W,A]=0 and A=Q_U A Q_U. The support is fixed as S and the safe volume change. From physical D1 and the local circuit projection inequality, Tr sigma(t)Q_U<=C_U epsilon²(1+t). This statement concerns the actual bare-Omega evolution and holds without translation covariance of sigma.

Write the exact transformed generator L'=i delta epsilon^-4 ad_W+B_epsilon. The full bare fast coefficient is

 B_-2 A=i delta[D2,S,A]+kappa sum_mu D[j_mu,S]^*A,
 D2,S=C_S+[F_S,F_S*].

Its local action is bounded, it preserves grades, and B_epsilon=epsilon^-2B_-2+O_local(epsilon^-1). On a neutral A the first jump cross coefficient is entirely off-grade, since j has grade-1 and j1=[-F+F*,j] has grades0,-2. Taylor expansion through order two gives

 P_W L'A=epsilon^-2B_-2 A+B0 A+O_local(epsilon),
 B0 A=i delta[D4,A]+kappa P_W sum_mu(D[j1_mu]^*A+Cross(j_mu,j2_mu)^*A).

The grade-zero operator B0 A annihilates the no-hole block on its enlarged finite support on both sides. D4 and the selected local terms preserve W. The neutral pieces of the displayed jump maps involve j1 grades0,-2 separately and the grade-1 component of j2 paired with j. They cannot create a hole out of a no-hole input; A then kills that output. Their loss products have the same property. Thus |Tr sigma B0 A|<=C_A epsilon²(1+t). Higher odd diagonal cancellation is unnecessary: the uniform O(epsilon) norm remainder already suffices.

For the exact off-grade remainder R=(1-P_W)L'A use the local inverse I_W and put

 K1=(i epsilon^4/delta) I_W R,
 K2=(i epsilon^4/delta) I_W[(1-P_W)B_epsilon K1],
 X=A+K1+K2.

K1=O_local(epsilon³), K2=O_local(epsilon⁵). Exactly

 L'X=P_W L'A+P_W B_epsilon K1+B_epsilon K2.

Since B_-2 commutes with P_W, its epsilon^-2 part contributes zero to P_W B_epsilon K1. The other part is O(epsilon²); B_epsilon K2 is O(epsilon³). All these statements use complete original jumps and their cross terms, not grade-resolved observed channels. Integrating the exact finite-spin equation against a fixed C1 time test g therefore gives

 |epsilon^-2 integral g(t)Tr sigma(t) B_-2 A dt|
                    <=C_(A,T) epsilon ||g||_(W1,1 plus endpoints).

The endpoints and g' term use Tr sigma X=O(epsilon²); no division by the total volume occurs. This is an actual volume-/spin-uniform weak stationarity estimate on LOCAL HOLE-CORNER tests. It does not hold by the same proof for a general neutral multiplier which has a nonzero no-hole block.

Define positive rescaled forms nu_epsilon,g(A)=epsilon^-2 integral g Tr sigma A for g>=0. Their local mass is bounded by C_U integral g(1+t). The checked gain proof gives nu_epsilon,g(j_mu*j_mu)=O(epsilon²); under the coupled spin scaling it also gives nu_epsilon,g(w_a v_a)=O(epsilon). Cauchy in a sufficiently large local hole corner bounds the full bare dissipator on A by O(epsilon). Thus

 nu_epsilon,g(i[D2,S,A]) ->0,
 nu_epsilon,g(p_a)->0, p_a=w_a[1-product_(b~a)n_b].

A countable bounded local operator-family algebra, closed under products, adjoints and the actual derivation d_S=i[D2,S,.], permits diagonal weak extraction. Its positive limiting time densities are locally bounded weights, not trace-one states. They are weakly stationary on the hole ideal and annihilate every local bright projector. No common rotor field space or hole-weighted tightness is assumed in this extraction.

The restrictions imply more than zero bright mass. From p²=p, differentiate twice and apply stationarity and Cauchy to obtain nu((d p)²)=0. Iterating the Leibniz identity for X*X gives nu((d^r p)*d^r p)=0 for every fixed r. All expressions remain bounded local families. This constrains every local finite-order bright-escape row without presuming a static B mask, a one-hole sector or an infinite-time absorption estimate.

A candidate nonzero comparison functional is concrete. On an even torus choose the perfect matching a->a+e1. Set every A charge to0, every B charge to+1, E=-1 on matching links oriented A-to-B and E=0 on all others. Its Gauss law is exact. F annihilates this word and C_S does too. F* first moves a B+ into one A hole; the only possible following outward hop returns that same particle to the unique resulting B vacancy. At these fields each inward/outward squared spin amplitude is1, for every S>=1. Hence D2,S acts by6|A| and every bare original j vanishes. Bare Omega is also an exact zero eigenvector of D2,S. The comparison mixture (1-epsilon²)|Omega><Omega|+epsilon²|D><D| has nonzero rescaled local hole mass and is stationary for the complete leading fast generator.

This is NOT the actual bare-Omega time-evolved state, nor a statement about the full transformed microscopic jumps J_epsilon. A legal perfect-matching outward-hop word reaches D from Omega, but its actual probability is not epsilon² by that fact. The example tests sufficiency of local darkness/stationarity only. It has an extensive occupied B background and extensive simultaneous holes; finite-global-excitation absorption cannot be applied uniformly to it. Its bounded matching field shows that electric tightness alone cannot force the defect weight itself to vanish.

The remaining operator-domain question is exact: fast stationarity has been proved for the nonunital local hole ideal. A general neutral local multiplier O has [D2,S,O] in an appropriate defect domain only after treating its electric component, but O itself is not in that ideal. Extending stationarity to such multipliers needs a justified boundary/weight approximation. There is no allowed identification of separate GNS vectors or automatic passage from a locally finite weight to a bounded normalized functional.
