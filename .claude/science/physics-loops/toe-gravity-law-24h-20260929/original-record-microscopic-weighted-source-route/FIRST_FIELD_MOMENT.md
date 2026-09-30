# Uniform physical first electric moment on common microscopic times

Author discovery proof; not independently checked. This is a weaker field moment than CONTRACT(W1), but it holds on a common physical time interval and in fact with an explicit polynomial bound for every fixed time. It uses the actual supplied compensated spin law, bare Omega, Gauss sector, all later births and both original instruments separately. The energy law is not altered: V_E below is a diagnostic first absolute field moment, not the microscopic Hamiltonian or the effective electric energy.

## Statement

Let n=|A| and V_E=sum_e |E_e| on an even safe finite torus. There are epsilon0,C independent of integer spin and volume such that the actual microscopic state obeys

    n^-1 Tr[rho_micro(t)V_E]
       <= C(t+t²)+C epsilon²(1+sqrt(1+t)),  t>=0.     (E1)

The coupled scaling epsilon² S(S+1)=delta/K with fixed positive K,delta,kappa is allowed. In particular each fixed physical link has a uniform first moment on[0,T]. The bound at t=0 is an upper estimate; the actual physical moment there is zero. No limit at fixed finite volume is taken first.

A consequence is a uniform local cutoff tail on fixed T:

    Pr_micro(any |E_e|>R on finite F_E)
                         <= C_T |F_E|/R.             (E2)

It permits truncating local quantum outputs in trace norm by the gentle projection bound. Since E_e²<=S|E_e| at finite spin, it also gives

    <E_e²/[S(S+1)]>_micro <= C_T/(S+1).              (E3)

This does NOT give a uniform second field moment, a uniform physical energy/current bound, the weighted-hole target(W1), or convergence to the effective process. It allows <E²> to grow linearly in S.

## 1. Bounded displacement, not a norm bound on V_E

For a local operator A, use the row/column field-displacement Schur norm

    s_1(A)=max(sup_alpha sum_beta |A_(alpha,beta)|(1+d_E(alpha,beta)),
               sup_beta sum_alpha |A_(alpha,beta)|(1+d_E(alpha,beta))).

It is submultiplicative by the triangle inequality for field displacement. Original normalized spin hops have finite bandwidth and uniformly bounded row/column sums; the normalized electric compensation is diagonal with a uniform bounded supremum. Finite products and commutators have the same property. P_W deletes entries, and I_W divides a nonzero-grade entry by a nonzero integer; both contract s_1. Exponentials of the finite local normal-form gates converge in s_1 with bound exp(|z|s_1(A)). The bounded cone of each input term gives uniform analytic Taylor remainders in this norm, at each fixed circuit order, independently of S,L.

This argument is a direct refinement of the checked finite-circuit construction. Only local cones enter; no uniform global Schur norm for the complete Y is asserted. It needs only first displacement, not the new quadratic weighted initial-layer lemma.

The absolute value is handled ENTRYWISE in this physical field basis:

    ||[V_E,A_Z]|| <= s_1(A_Z),                       (E4)

because |sum_(e in Z)|E_e(alpha)|-sum_(e in Z)|E_e(beta)||<=d_E(alpha,beta). Schur's test bounds the operator norm. There is no appeal to an unrestricted operator-Lipschitz theorem. For dissipators and their polarized cross maps use

    D[J]*V_E=(1/2)(J*[V_E,J]+[J*,V_E]J),             (E5)

and the analogous complete gain/loss expression for two different factors. They have bounded local norms controlled by the corresponding s_1 norms. Disjoint gains and losses cancel, so only local field terms in the jump cone occur. Summing bounded-incidence terms costs Cn, not n² and not S n.

The exact order-six normal form and jump expansions therefore retain their stated epsilon orders after acting on V_E. In particular the commutator with a single transformed E-local observable remains local with uniform norm even though ||V_E|| itself grows like nS.

## 2. The actual leading fast drift requires a hole

The literal second coefficient is D2=C_S+[F,F*]. Its offdiagonal paths split as

    sum_a F_a F_a*,
    sum_a F_a*F_a(Q_gate,a-1),
    sum_(a!=c)[F_a,F_c*].

The electric polynomial is diagonal and commutes with V_E. The first family acts at a hole and has at most36 two-hop paths per hole. The second is active only near another hole at distance two:18 possible centers times36 paths gives648. Assign each such center to one of its existing input holes. The third moves a hole between A sites at distance two through a common B:18 neighbors, at most two shared B sites and two product orders give72 paths. Source charges are fixed on a basis input, so no extra sign multiplicity occurs. Disjoint stars cancel in the commutator. Every normalized spin path has absolute amplitude at most one, and boundary-blocked paths are zero.

There are at most756 paths per input hole, and a two-hop path changes V_E by at most two. Thus the absolute row sum of i[D2,V_E] is <=1512 W on a basis input. Hermiticity and symmetric absolute entries give the safe form bound

    -1600 W <= i[D2,V_E] <=1600 W.                 (E6)

This statement uses no static B component or global B count. Unlike a relative quadratic weight estimate, its right side is the UNWEIGHTED hole number.

Each bare original birth changes V_E by at most one and acts only at an A hole. The total original loss at one center is at most12 w_a. On this diagonal observable the coherent sign cross terms vanish by orthogonal final A charges, while their original mark is retained. Hence

    -12W <=sum_mu D[j_mu]*V_E<=12W.                 (E7)

Therefore, for B2*=i delta[D2,.]+kappa sum D[j]*,

    -c0 W<=B2*V_E<=c0 W,
    c0=1600delta+12kappa.                            (E8)

## 3. Complete microscopic off-grade drift and correction

Work in the exact rotated state sigma=Y rho_micro Y*, and write

    L'* =i delta epsilon^-4[W,.]+B_epsilon,
    B_epsilon=epsilon^-2 B2*+O_local(epsilon^-1).

V_E has grade0. The exact transformed jumps have j at grade-1, first-order coefficients only at grades0,-2, and J_-1=j+O_local(epsilon²). Upon W-averaging the whole adjoint dissipator, only equal jump grades remain. Consequently the difference between its averaged drift and the bare epsilon^-2 jump drift costs O_local(1), including all other grades, after using(E4)-(E5). The higher diagonal Hamiltonian terms likewise cost O_local(1). Thus

    P_W L'*V_E <=c0 epsilon^-2 W+C n I.             (E9)

The leading fast term in(E9) is not bounded by a generic O(epsilon^-2)n estimate; the actual source path/hole factor in(E6)-(E8) is essential.

Let R_E=(1-P_W)L'*V_E. Complete cross terms at first order give local strength O(epsilon^-1) in(E4)-(E5); the off-grade Hamiltonian remainder has strength O(epsilon³). Define

    K1=(i epsilon^4/delta)I_W R_E,
    K2=(i epsilon^4/delta)I_W(1-P_W) B_epsilon K1,
    Vc=V_E+K1+K2.

These are Hermitian local interaction sums with

    ||K1+K2||<=C epsilon³ n.

All estimates are now ordinary bounded local-operator estimates: the unbounded-in-S V_E disappeared into its bounded displacement commutators. The exact cancellation is

    L'*Vc=P_W L'*V_E+P_W B_epsilon K1+B_epsilon K2.

B2* preserves grades, so the putative order-epsilon term P_W epsilon^-2 B2*K1 is zero. The residual has local strength O(epsilon²), and therefore

    L'*Vc <=c0 epsilon^-2 W+C n I.                  (E10)

No grade has been measured or removed from the actual generator. All same-mark gains/losses remain in B_epsilon acting on the corrections. No gap, fast absorption estimate, source cluster tail or microscopic/effective comparison is used.

## 4. Bare preparation and physical-coordinate return

The checked defect estimate(D10) gives

    <W>_sigma(t)/n<=C epsilon²(1+t)

for the actual sigma(0)=Y|Omega><Omega|Y*. By(E4) and the local gate integral, for each link

    Y*|E_e|Y=|E_e|+epsilon[|E_e|,S1]+epsilon² R_e,
    ||[|E_e|,S1]||+||R_e||<=C,
    S1=-F+F*.

The difference has bounded support despite ||E_e||=S. To justify the remainder, first write conjugation minus |E_e| as the integral of its bounded commutator through the finitely many local gates in its cone; then Taylor-expand that bounded local analytic expression. A Cauchy estimate is uniform in S. The same assertion holds with Y,Y* interchanged.

Since |E_e|Omega=0, the expectation of the first commutator in Omega is zero. Thus <V_E>_sigma(0)<=C epsilon² n. Integrating(E10), controlling both endpoints of K1+K2 and retaining the exact defect bound yields

    <V_E>_sigma(t)/n
                 <=C(t+t²)+C epsilon²+C epsilon³.  (E11)

For return to physical coordinates, the first commutator above has grades plus/minus1. Let P_X fill all A factors in its bounded support cone. Then P_X[|E_e|,S1]P_X=0. The checked PHYSICAL hole estimate(D1) gives

    Tr[rho_micro(t)(1-P_X)]<=C epsilon²(1+t).

For any bounded A with P_X A P_X=0, its expectation is at most3||A||sqrt(Tr[rho(1-P_X)]). Multiplying by the explicit epsilon in the conjugation formula shows

    |<|E_e|>_sigma(t)-<|E_e|>_micro(t)|
                      <=C epsilon²(1+sqrt(1+t)).    (E12)

This step uses only a bounded off-grade COMMUTATOR, not a bound on ||E_e|| or a weighted preparation assumption. Summing the six links per A center and combining(E11)-(E12) proves(E1). It includes every later birth in the actual microscopic ensemble.

Physical translation symmetry then gives the same order bound for each link orientation: its nonnegative translated sum is bounded by V_E, and Omega and the physical law are translation invariant. No symmetry of the chosen normal-form coloring is needed. The diagonal spectral union bound gives(E2), and E²<=S|E| gives(E3).

## 5. Local-output compactness consequence and limits

For a fixed finite quantum region, project all its electric links onto |E_e|<=R, retaining its actual matter factors. The discarded probability is bounded by(E2), uniformly in S,L on[0,T]. Gentle projection bounds the trace norm between the actual local output and its compressed block by at most2sqrt(C_T |F_E|/R). This argument applies to the quantum marginal of the ORIGINAL joint classical-history/quantum output; the trace over classical records supplies the same actual field expectation, so it also bounds the sum of conditional block tails without assuming conditional moment bounds.

For a fixed finite monitored region and fixed time bins, the checked original count estimate(D3) bounds the overflow probability p_N at count cap M by C_T|F|/(M+1). To compare in one carrier, embed all finite-spin field spaces by their integer E basis into the rotor output space, and append an extra overflow/refusal flag. Embed the original state with zero weight on that flag. Moving long-word classical blocks into the disjoint overflow outcome costs at most2p_N in trace norm; their quantum marginal may be retained at this step. Projecting the quantum fields then costs at most2sqrt(p_E), with p_E<=C_T|F_E|/R. If a normalized finite approximation is desired, place the removed trace in a fixed refusal state, adding at most p_E. Thus a safe bound is2p_N+2sqrt(p_E)+p_E. The remaining carrier is finite dimensional (finite bins, ORIGINAL labels/word orders, count cap, electric cutoff and flags). This gives subsequential trace-norm compactness for EACH such fixed output specification on volumes that contain its fixed geometry without aliasing. Coherent signs remain within their original mark throughout. The overflow and quantum cut are mathematical approximations to the output, not a new field measurement or altered source process.

This compactness is not uniqueness, boundary independence, convergence of the microscopic law to the effective law, or convergence of continuous timestamps in total variation. Continuous time records require their own specified weaker measure topology. Nor does a first field moment give electric-energy uniform integrability: second moments can still diverge, and the hole-weighted second moment(W1) remains open. The supplied microscopic energy and the original marked process are unchanged. No new numerical execution or formal review is claimed.
