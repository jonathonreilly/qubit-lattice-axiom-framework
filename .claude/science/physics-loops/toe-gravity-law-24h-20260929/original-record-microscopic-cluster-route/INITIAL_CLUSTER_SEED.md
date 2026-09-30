# A source-specific initial cluster seed and the exact propagation gap

This lemma concerns the exact finite-depth normal-form coordinates of the actual BARE Omega preparation. It is not a supplied dilute random state, a changed instrument or a positive-time clustering theorem. It is independent of the new global exponential-moment theorem. Constants may be impractically large but do not depend on spin or volume.

## 1. Actual cluster diagnostic and initial-state theorem

Fix one of the checked finite-order, finite-color circuits Y_epsilon for the microscopic Hamiltonian. The added finite-depth loss-canceling circuit could also be included, but is unnecessary. Every local gate differs from identity by at most c epsilon, the depth and radii are fixed, and it preserves Gauss. Let r be a common lattice radius for the backward cone of a single matter-site observable under Y. Work on the full tensor carrier before restriction to Gauss, where the original Omega is a product of fixed charges and zero-field link vectors; Omega and the evolved vectors in use are physical.

On the B sublattice connect two sites when their periodic lattice L1 distance is at most six. This is an occupation diagnostic only. Each B vertex has at most

    Delta_B =18+66+146=230

neighbors. For an A site a, anchor every B vertex within distance three of a (at most6+38=44 vertices). Let C_a(omega) be the union of occupied-B connected components intersecting this anchor set. If the set is empty, its size is zero. Denote by P_(a,m) the diagonal projector onto |C_a|>=m, and let w_a be the actual A-vacancy projector. This graph is not asserted invariant under H2 and is not a new observed record.

There are constants c_h,c_B,nu and epsilon0>0, independent of spin and torus, such that in the exact coordinate preparation sigma0=Y|Omega><Omega|Y^*,

    Tr[sigma0 w_a P_(a,m)]
      <=c_h epsilon^2 *231^(2m)*(c_B epsilon^2)^q_m,
    q_m=max(0,floor(m/nu)-1),    nu=(4r+1)^3,          (I1)

for every m>=1 and epsilon<=epsilon0, with c_B epsilon0²<1. Consequently epsilon0 can be chosen so that

    sup_(epsilon<=epsilon0,S,L,a)
       epsilon^-2 Tr[sigma0 w_a P_(a,m)] ->0
                         exponentially as m->infinity. (I2)

The joint scaling epsilon²S(S+1)=delta/K can be imposed afterward. The same proof works with a finite external classical register in its zero-record state. It adds no readout on the internal cluster configuration.

## 2. Proof including the rare-hole prefactor

Since w_a Omega=n_b Omega=0, finite-cone gate commutators give

    <w_a>_(sigma0)<=||[w_a,Y]Omega||²<=c_h epsilon²,
    <n_b>_(sigma0)<=c_B epsilon².

The bounds involve only the finitely many gates in the corresponding cone; no global ||Y-I|| bound appears. For a collection of output matter sites separated by more than2r, their backward-conjugated projectors have disjoint tensor supports. Their joint expectation on PRODUCT Omega therefore factors exactly. This statement is evaluated on the full supplied tensor product, with the physical vector Omega; restriction to the invariant Gauss sector does not invalidate the equality.

For any set S of m B vertices, remove the at most nu vertices within distance2r of a. Greedily choose a subset T of the remainder with mutual distances greater than2r. Each chosen site removes at most nu candidates. Thus |T|>=q_m. Their backward cones and the backward cone of w_a are pairwise disjoint. All output occupation projectors commute, so

    <w_a product_(b in S)n_b>_(sigma0)
       <=<w_a product_(b in T)n_b>_(sigma0)
       =<w_a>_(sigma0) product_(b in T)<n_b>_(sigma0)
       <=c_h epsilon² (c_B epsilon²)^q_m.

If |C_a|>=m, the augmented graph consisting of its occupied B vertices plus the anchor vertex a has a connected subset with exactly m B vertices plus a. This follows by truncating a rooted spanning tree. Its maximum degree is at most231, including the anchor edges. A canonical depth-first traversal of its spanning tree has2m steps. Counting all such walks bounds the number of possible rooted sets by231^(2m). The diagonal union bound and the preceding expectation prove(I1), with no independent-occupation assumption on sigma0.

Put p0=c_B epsilon0² and choose

    beta=231² p0^(1/nu)<1.

As q_m>=m/nu-2, (I1) divided by epsilon² is bounded uniformly by c_h p0^-2 beta^m. This proves(I2). Tori whose total B population is less than m contribute zero. Periodic identifications only reduce the ball and neighbor counts used here, and r,nu are finite even if a small torus is covered by an entire cone.

This proof gives a rare-HOLE prefactor epsilon² in addition to the cluster tail. An unweighted cluster tail combined with a separate hole mean would not supply that joint factor. No positive-time conclusion follows merely from this initial estimate.

## 3. A concrete positive-time missing estimate

Let sigma_epsilon(t)=Y rho_micro(t)Y^* be the EXACT coordinate state of the original unconditional marked process. A useful open estimate is: for some common T>0,

    u_m(T)=sup_(epsilon<=epsilon0,S,L,a,0<=t<=T)
       epsilon^-2 Tr[sigma_epsilon(t) w_a P_(a,m)]
                         ->0 as m->infinity.             (I3)

The original mark register may be retained; these traces marginalize it, without changing the marks. Equation(I2) proves only the t=0 case of(I3). A polynomial conditional cluster moment would suffice for(I3); an exponential bound is not necessary. Global count moments and translation invariance do not imply(I3), because the rare holes could all sit in rare large occupied regions.

Here is a precise consequence of(I3) for one load-bearing part of the comparison. Remove the exact finite-spin diagonal Delta_S from H2_S and write Hbar_S=C_magnetic+[F,F^*]. Its terms have uniformly bounded norms and each is supported on a nearby hole projection on BOTH sides:

- F_a F_a^* is supported on w_a;
- -F_a^* F_a(1-Q_a) is supported on the union of the eighteen neighboring hole projections;
- [F_a,F_c^*] is supported on w_a OR w_c.

For a fixed bounded local observable O_X commuting with the A-hole projections, let J_X=i[Hbar_S,O_X]. Only finitely many terms meet X. There are a finite A neighborhood A_X, its hole-existence projection P_X, and a uniform constant C_X such that

    J_X=P_X J_X P_X, ||J_X||<=C_X,
    <P_X>_(sigma(t))<=c_X epsilon²(1+t).                 (I4)

The last estimate follows from the checked local physical hole bound and the finite-cone unitary projection inequality. Let Pi_m be the diagonal projector onto a hole a in A_X with |C_a|>=m. It commutes with P_X, and(I3) would give <Pi_m> <=|A_X| epsilon² u_m(T). For any positive state, Cauchy-Schwarz in that state proves

    |Tr sigma[J_X-(1-Pi_m)J_X(1-Pi_m)]|
       <=3 C_X sqrt(<P_X><Pi_m>)
       <=C'_X epsilon² sqrt(u_m(T)).                  (I5)

Thus the epsilon^-2 fast prefactor cancels and the time-integrated large-cluster contribution of this bounded Hbar current would be at most C''_X T sqrt(u_m(T)), uniformly in volume and spin. This is an operator/state estimate in the actual dynamics, not a trajectory decomposition or an added cluster measurement. A finite original cq history register can be tensored throughout; the proof only uses positivity and its unchanged quantum marginal.

For unrestricted bounded local readouts one may first insert the projection onto occupied A sites in X. The omitted expectation has absolute size at most2||O_X||sqrt(<sum_(a in X)w_a>)=O(epsilon). The projected observable commutes with every hole projector. This reduction keeps arbitrary bounded link-field and site-charge output within the original readout contract.

Equations(I3)-(I5) are NOT a proof of M4. The good-cluster dynamics still needs an actual LOCAL finite-cluster comparison, including multiple simultaneous holes and quantum coherences. Existing GLOBAL fixed-N_B absorption does not supply it. The diagonal spin electric term Delta_S and its hole-gated difference from the physical target require microscopic field uniform integrability; (I4)-(I5) deliberately concern Hbar only. Jump/loss corrections, the original marked propagators, and any quasi-local target-evolved test families also need their own bounds. The complete signed instrument-weighted Duhamel estimate with all these residuals would be target-equivalent; merely naming it is not a solution.

## 4. Failed propagation route and live alternatives

The direct local-count-tilt strategy cannot prove(I3) by absorbing every fast current into bare loss: LOCAL_TILT_ATTEMPT supplies an actual seven-B dark-to-dark matrix element violating that inequality. The global tilt succeeds only because H2 preserves the GLOBAL count. Finite-depth initial-state independence is also lost immediately under the actual fast evolution; it cannot be propagated by assuming a bounded microscopic Lieb-Robinson velocity.

Distinct live families are an actual source-weighted cluster expansion with fast propagators retained, a conditional occupation-moment estimate using time-integrated absorption, or a signed oscillatory estimate that bypasses absolute large-cluster current control. The unproved(I3) is weaker than the full local-output theorem and does not by itself settle it. This narrows one missing estimate and gives its exact original-preparation seed, rather than renaming M4 as an existence claim.
