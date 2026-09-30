# Local dressed-hole bound at the actual fast formation scaling

Provisional analytic discovery lemma, not independently checked or a full microscopic/effective comparison. The exact supplied law and bare Omega are in CONTRACT. Both complete original instruments are included separately. No modified jump law is evolved in the proof.

## Statement

For the degree-six tori and actual compensated spin law there are epsilon0>0 and finite constants c0,c1,c2, independent of volume and S, such that from bare Omega

    <W>_micro(t)/N <= c0 epsilon^2 (1+t),                  (D1)
    <Gamma_a,micro>_t <= c1 kappa (1+t),                 (D2)
    E N_F([s,t]) <= c1 kappa |F| integral_s^t(1+u)du.   (D3)

N=|A|. The constants depend on fixed delta,kappa and the finite local circuit order/range; they are not practical numerical resource estimates. The bounds hold for every t>=0 while becoming trivial at large t. Uniformity in S permits epsilon^2 S(S+1)=delta/K with fixed K>0. No uniform mean-energy cap is assumed; Omega fails such a cap. A stronger frame-dependent integrated activity estimate appears below. These statements control actual local mean counts and initial-time layers; they do not prove convergence of field outputs or conditional hazards.

## 1. Finite local normal form

Write H=delta epsilon^-4(W+epsilon T+epsilon^2 C). W is a sum of onsite vacancy projections; T consists of bounded grade+/-1 edge terms; C consists of bounded grade0 radius-two terms. Spin-normalized hopping and the compensation satisfy ||T_edge||<=1 and ||C_a||<=48, uniformly in S. Gauge and record-number symmetries hold termwise. Thus the finite-color normal-form construction of the fully read uniform-local-ring source section3 applies with the order-two initial coefficient C included in its recursion.

For completeness: at order r, decompose its coefficient A_r into bounded finite-support terms, average under exp(i theta W), and use the local inverse

    P_W(A)=(2pi)^-1 integral exp(i theta W) A exp(-i theta W)dtheta,
    I_W(A)=sum_(k!=0) A_k/k,   ||I_W||<=pi/2,
    [W,I_W(A)]=A-P_W(A).

The inverse is bounded by the L1 norm of the sawtooth Fourier kernel. Onsite conjugation preserves supports. Color the bounded-degree support-intersection graph, and apply the local gates exp(epsilon^r I_W(A_(r,Z))) in a fixed color order. Their order-r contribution cancels the off-grade coefficient; later ordering terms stay in later recursion coefficients. Each fixed finite sequence has bounded depth/range and a bounded light cone per initial term. Analytic Taylor bounds on a common epsilon disk control the remainder per term independently of volume, S and local matrix dimension. The covariance Xi=(-1)^W, epsilon->-epsilon makes every odd diagonal coefficient vanish, also with epsilon^2 C present.

At order6 this gives an EXACT finite circuit Y, and exact finite-range remainder R_H, with

    H'=Y H Y^*=delta epsilon^-4 W
            +delta epsilon^-2 D2+delta D4+delta epsilon^2 D6+R_H,
    [Dr,W]=0,  ||R_H||_loc<=c delta epsilon^3.           (D4)

Here every local interaction has bounded support cardinality and incidence, with constants independent of volume and S. No global ||Y-I||=O(epsilon) is asserted. For each fixed local A, ||Y A Y^*-A||<=c_A epsilon||A||. The transformed original jumps J_m=Y j_m Y^* are exact, finite-support, norm-bounded, analytic families with uniformly bounded local Taylor coefficients. Their labels remain the original marks; no W-grade measurement or channel split is performed.

The first circuit derivative is sum I_W(T_edge). It has grades+/-1. Since j_m has grade-1, [Y'(0),j_m] has only grades0,-2. Therefore, writing J_(m,r) for the W-grade r component,

    J_(m,r)=O_loc(epsilon^2) for every r>0.              (D5)

There are only finitely many possible grades per jump, bounded by the number of A factors in its circuit cone. This count does not depend on S or volume.

## 2. Local interaction estimates, not extensive norm products

For A=sum_i A_i define nu(A)=sup_x sum_(i:x in supp A_i)||A_i||, with maximum support size s_A. If H has maximum support size s_H,

    nu(i[H,A]) <=2(s_H+s_A) nu(H) nu(A).

This follows by summing only intersecting supports, then separating whether x lies in H_i or A_j. A family of local jumps with maximum support size s_J and g_J=sup_x sum_(m:x in supp J_m)||J_m||^2 similarly obeys

    nu(sum_m D[J_m]^* A)<=2(s_J+s_A)g_J nu(A).

Disjoint gains and losses cancel exactly. All operators constructed below require only finitely many such compositions, so support sizes remain bounded. Onsite averaging and I_W do not enlarge supports. Finally ||A||<=|Lambda| nu(A), or a constant times N nu(A); no product of two extensive norms is used.

Let L'^* =i delta epsilon^-4[W,.]+B_epsilon be the EXACT transformed generator. On finite-support interaction sums,

    B_epsilon=epsilon^-2 B_-2+O_loc-action(epsilon^-1),
    B_-2=i delta[D2,.]+kappa sum_m D[j_m]^*.            (D6)

B_-2 commutes with P_W because D2 has grade0 and every j_m has grade-1. Both B_epsilon and the displayed difference have the action bounds just proved, with respectively epsilon^-2 and epsilon^-1 strength. The second bound follows from J_m-j_m=O_loc(epsilon), the exact dissipator difference identity and (D4). It does not require diagonalizing any global spectral band.

## 3. Two local coherence corrections

Define the jump contribution to the W drift

    A_epsilon=kappa epsilon^-2 sum_m D[J_m]^*(W),
    R_epsilon=(1-P_W)A_epsilon.

The commutators with W involve only the A factors in each jump support. Direct grade algebra gives

    P_W A_epsilon=kappa epsilon^-2 sum_(m,r) r J_(m,r)^* J_(m,r).

At epsilon=0 the unscaled drift is -kappa sum j_m^*j_m, grade0. Hence R_epsilon has local strength O(epsilon^-1), whereas its positive-grade diagonal contribution has strength O(epsilon^2) by (D5). Put

    D_minus=kappa epsilon^-2 sum_(m,r<0)(-r)J_(m,r)^*J_(m,r)>=0,
    K1=(i epsilon^4/delta) I_W(R_epsilon),
    K2=(i epsilon^4/delta) I_W((1-P_W)B_epsilon K1),
    X_epsilon=W+K1+K2.                                (D7)

Both K1,K2 are Hermitian, gauge-preserving local interaction sums; their local strengths are respectively O(epsilon^3), O(epsilon^5). They are observable corrections, not positive state embeddings or altered jumps. The sign is fixed by

    i delta epsilon^-4[W,K1]=-R_epsilon.

The exact identity is

    L'^* X_epsilon+D_minus
      =i[R_H,W]+kappa epsilon^-2 sum_(m,r>0)r J_(m,r)^*J_(m,r)
          +P_W B_epsilon K1+B_epsilon K2.              (D8)

The apparent O(epsilon) term in P_W B_epsilon K1 is absent:

    P_W epsilon^-2 B_-2 K1
       =epsilon^-2 B_-2 P_W K1=0.

The remainder in (D6) times K1 is O_loc(epsilon^2). The final term in (D8) is O_loc(epsilon^3), and i[R_H,W] is O_loc(epsilon^3). Thus, as an operator inequality on the actual finite Hilbert space,

    L'^* X_epsilon+D_minus <= c2 epsilon^2 N I,
    ||X_epsilon-W||<=c3 epsilon^3 N.                   (D9)

No positivity of X_epsilon is required. The nonnegative D_minus is retained, not discarded as a presumed small population. This is also why the large microscopic dissipator cannot simply be omitted.

## 4. Bare preparation, physical holes and original marked counts

In the rotated state sigma(0)=Y|Omega><Omega|Y^*, each local w_a projection has expectation

    ||w_a Y Omega||^2=||[w_a,Y]Omega||^2<=c epsilon^2.

The local commutator bound follows from the finite circuit cone; w_a Omega=0. Therefore <W>_(sigma0)<=c epsilon^2 N. In fact its leading coefficient on the zero-field cubic product is6 epsilon^2 N; no use of that sharper coefficient is needed. Integrating (D9) against the EXACT transformed density gives

    <W>_(sigma_t)+integral_0^t <D_minus>_(sigma_u)du
                  <=c epsilon^2 N(1+t).              (D10)

This bound includes every later birth and all coherences. To return to the physical vacancy count, for each unit vector psi use

    ||w_a Y^* psi||^2
       <=2||w_a psi||^2+2||[w_a,Y^*]psi||^2.

Summing proves Y W Y^*<=2W+c epsilon^2 N I. Equations(D10) and this inequality prove(D1). The microscopic generator and bare Omega are translation invariant even if the chosen circuit coloring is not. Thus the actual <w_a> equals <W>/N on every cubic torus.

The ACTUAL original microscopic loss at a satisfies

    Gamma_(a,micro)=kappa epsilon^-2 sum_(marks at a)j_m^*j_m
                      <=12 kappa epsilon^-2 w_a.

Normalized spin factors only decrease this bound; the unnormalized coherent sign sum has the same actual loss as the two resolved signs because their final charges are orthogonal. This yields(D2), and the exact counting-intensity identity yields(D3). There is no Poisson replacement or conditional-hazard bound. In particular Pr[N_F([0,T])>M]<=c1 kappa|F|(T+T^2/2)/(M+1) prices finite-region count-register overflow uniformly in volume and spin.

## 5. What this lemma leaves open

D_minus is a phase-grade diagnostic inside the proof; its summands are NOT the observed marks. Only the physical Gamma and counts in(D2)-(D3) are claimed as readouts. A small hole density does not bound the accumulated action of a W-preserving Hamiltonian of strength epsilon^-2. An O(epsilon^2) population can still leave an O(1) naive integrated field bound. Dark fast motion, field moments, grade-coherent no-event corrections, and local output comparison need a separate dynamical estimate. No microscopic/effective process closure or uniform electric moment bound is inferred from(D1)-(D10).
