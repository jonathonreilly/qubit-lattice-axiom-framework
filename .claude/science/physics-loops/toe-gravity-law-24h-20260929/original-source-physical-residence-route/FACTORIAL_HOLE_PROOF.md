# Actual factorial-hole budget and a growing-volume residence window

Author discovery; requires focused independent checking before reuse. The frozen contracts are ed381b26 and 89fa1b9c. All expectations below are in the ACTUAL microscopic ensemble, either rho or sigma=Y rho Y*. A grade sum is a proof operation, never a refinement of the original observed marks. Both original instruments are included separately, with their coherent sign sums intact. No diagnostic secular state is evolved.

## 1. Statement and exact imports

Write n=|A|, W=sum_a w_a, and F_2=W(W-1)=sum_(a!=c) w_a w_c. At fixed positive K,delta,kappa and fixed finite physical T there are epsilon_0>0 and C_T independent of n,S such that

 sup_(0<=t<=T) Tr[sigma(t)F_2] <= C_T epsilon^4 n^2,
 sup_(0<=t<=T) Tr[rho(t)F_2]   <= C_T epsilon^4 n^2.          (F1)

The statement concerns bare Omega and the original compensated finite-spin law. Impose epsilon^2 S(S+1)=delta/K for the weighted consequence, not for the algebra proving(F1). In particular there is no fixed global B-count restriction. The price n^2 is explicit and cannot be replaced by a local volume in this theorem.

Use the fully checked DEFECT_LEMMA fbbf36c2: its exact order-six finite-depth local circuit, exact finite-cone analytic jumps, uniform local coefficient bounds, and actual local rare-hole estimate. The latter implies for every union U of at most a fixed number of fixed-radius cones

 Tr sigma(t) Q_U <= C |U| epsilon^2(1+t),
 P_U=product_(a in U)(1-w_a), Q_U=1-P_U.                    (F2)

To obtain this local version even for a circuit coloring without translation symmetry, first return the checked global mean to physical coordinates, use the translation covariance of rho and Omega, and then use the local circuit projection inequality in the other direction. The constants depend on cone CARDINALITY and bounded incidence, not the separation between disconnected cones.

Also use the actual filled-input cross cancellation proved in positive-forcing bec9ac7d, equations(10)-(14), checked in receipt1138c68f. Its short derivation is restated below. The source grades from that report are J_(mu,+1)=epsilon^2 B_mu+O(epsilon^3), B_mu=-F_a j_mu F_a, and J_(mu,r)=O(epsilon^3) for r>=2. All estimates are operator estimates on the actual normalized spin carrier, including boundary zeros.

No energy, mixing, fast gap, static B-cluster, typicality, independence, or conditional field estimate is imported.

## 2. Parity and a sharper fixed-pair secular functional estimate

Let P denote W-grade averaging, Q=1-P on operators, and I its bounded inverse with [W,I X]=QX. Distinguish this superoperator Q from the local state projection Q_U. On observables the exact generator is

 L'^*=epsilon^-4 A+B_epsilon,
 A=i delta[W,.],
 B_epsilon=epsilon^-2 B_2+epsilon^-1 C_1+B_0+O_local(epsilon),
 B_2=i delta[D2,.]+kappa sum_mu D[j_mu]^*.                   (F3)

B_2 preserves every W grade. The complete C_1 is the original polarized gain plus BOTH losses, not just recycling. All disjoint actions cancel before taking support bounds.

The microscopic covariance is Xi=(-1)^W, epsilon -> -epsilon. Each normal-form coefficient at gate order r has Xi parity (-1)^r, since the recursion starts with the odd hopping and even compensation and preserves total order parity. Fixed coloring does not spoil this relation. Hence Y(-epsilon)=Xi Y(epsilon) Xi, and J_mu(-epsilon)=-Xi J_mu(epsilon) Xi. It follows that a generator coefficient of physical power epsilon^p maps an even test to parity (-1)^p. In particular B_2,B_0 are even and C_1 is odd. This is an exact finite-spin algebraic symmetry; varying S is not needed to establish it.

Fix O=w_a w_c, a!=c. It is neutral, norm one, and a hole-corner test. Define the exact linear correctors

 R_O=Q L'^*O,
 K1=(i epsilon^4/delta) I R_O,
 K2=(i epsilon^4/delta) I Q B_epsilon K1.                    (F4)

Both are off-grade and have complete supports contained in a fixed number of cones around a,c. Their norms are O(epsilon^3),O(epsilon^5), uniformly even when the two centers are far apart. This follows by applying each of the finitely many local generator actions only to the two support components and their fixed halos. A disconnected support does not acquire the volume or diameter of the region between them.

The exact identity is

 L'^*(O+K1+K2)=P L'^*O+P B_epsilon K1+B_epsilon K2.           (F5)

Write K1=epsilon^3 k3+epsilon^4 k4+O(epsilon^5),
K2=epsilon^5 l5+O(epsilon^6). Then k3,l5 are odd, k4 is even, and

 k3=(i/delta)I C_1 O,
 P B_epsilon K1=epsilon^2 T_O+O_local(epsilon^4),
 T_O=P C_1 k3,
 B_epsilon K2=epsilon^3 U_O+O_local(epsilon^4),
 U_O=B_2 l5, which is odd.                                (F6)

There is no epsilon^3 neutral remainder in the middle line. Indeed P B_2 K1=0 exactly, while its candidate epsilon^3 coefficient is P(C_1 k4+B_0 k3), of odd parity and therefore zero under P. The remainders in(F6) are uniformly bounded per pair, by the fixed local analytic Taylor estimates. No full-volume analytic norm is used.

For clarity, the filled-input cancellation in T_O retains the actual coherent loss. Enlarge U to contain every cone used here and put P0=P_U. Let A_mu=j_mu F_a-F_a j_mu, D_mu=[F*,j_mu], V=sum_mu j_mu* A_mu over the relevant local marks. The original identities j_mu P0=D_mu P0=0 and the locally filled A_mu P0 give

 (C_1 O)P0=-(kappa/2) O V P0,
 k3 P0=-i kappa O V P0/(2delta),
 P0 k3=+i kappa P0 V*O/(2delta).

Both outer gains in P0 C_1(k3)P0 vanish. Its two losses are opposite imaginary copies of P0 V* O V P0 and cancel. Thus P0 T_O P0=0. Since T_O is neutral on its complete support, it commutes with P_U, and

 T_O=Q_U T_O Q_U,
 |Tr sigma(t) T_O|<=C_T epsilon^2.                        (F7)

An off-grade or odd local operator X satisfies P_U X P_U=0 on a complete support U. Positive-state Cauchy gives

 |Tr sigma X| <= ||X||[Tr sigma Q_U+2 sqrt(Tr sigma Q_U)]
               <= C_T epsilon ||X||.                     (F8)

This also holds with arbitrary spectator entanglement; no product-state claim is used at t>0. Apply(F8) to the exact off-grade K1,K2 at both endpoints and to the odd U_O in(F6). Apply(F7) to T_O. Integration of(F5) proves the ACTUAL fixed-pair functional estimate

 |<O(t)>-<O(0)>-integral_0^t <P L'^* O> ds|
                  <= C_T epsilon^4,  t<=T.              (F9)

The epsilon^4 improvement is state-sensitive: it uses the rare-hole bound and the exact circuit parity. It is not a uniform operator-norm comparison of two semigroups. In particular no separate grade-resolved ensemble has been assumed. All off-grade coherent terms have been retained through(F4)-(F8).

## 3. The global factorial drift and actual bare preparation

Sum(F9) over the n(n-1) ordered distinct pairs. Linearity gives

 <F_2(t)>-<F_2(0)> = integral_0^t <P L'^* F_2> ds
                                 +O_T(epsilon^4 n^2).    (F10)

Because the full neutral Hamiltonian commutes with W, it contributes exactly zero to P L'^* F_2. Exact grade algebra for each ORIGINAL marked jump gives

 P L'^* F_2=kappa epsilon^-2 sum_(mu,r)
   J_(mu,r)*J_(mu,r)[f(W+r)-f(W)], f(x)=x(x-1).             (F11)

The product is well-defined and Hermitian because J_r*J_r commutes with W. On a nonzero grade-r input W+r>=0. Therefore every r<0 term is nonpositive. Retain its positive magnitude as

 D_-^(2)=kappa epsilon^-2 sum_(mu,r<0)
   J_(mu,r)*J_(mu,r)[f(W)-f(W+r)] >=0.                    (F12)

For r=+1 the difference is 2W, and ||J_(mu,+1)||<=C epsilon^2. For r>=2, ||J_(mu,r)||<=C epsilon^3 and r is bounded by the fixed jump-cone capacity. Hence, as an operator inequality,

 P L'^* F_2+D_-^(2)
       <= C epsilon^2 n W+C epsilon^4 n(W+1).            (F13)

The r>=2 order is specific to the actual law. The first circuit derivative has only grades +/-1, so the first jump correction has grades0,-2. The second-order ordering gauge is neutral because outward hops commute among themselves and inward hops likewise. The double commutator with j has maximal grade+1. Thus grades>=2 have no Taylor coefficients before order3, uniformly in S. We are not extrapolating the weaker generic positive-grade O(epsilon^2) statement to this step.

By the checked actual mean-hole bound, integration of(F13) costs at most C_T epsilon^4 n^2. This uses continuous forcing and all later original events; it is not an initial-layer estimate.

For the initial factorial, put P_ac=w_a w_c. Its exact local conjugate Y*P_ac Y has a bounded analytic expansion on the two finite cones. At epsilon=0 it annihilates Omega. Its first derivative also annihilates Omega, since the first circuit generator changes W by one and P_ac requires two holes. Thus

 ||Y*P_ac Y Omega||<=C epsilon^2,
 <P_ac>_(sigma(0))=||P_ac Y Omega||^2<=C epsilon^4.          (F14)

The exterior global Y is unitary; it introduces no extensive norm factor. Summing(F14), using(F10)-(F13), proves the stronger statement

 <F_2(t)>_sigma+integral_0^t <D_-^(2)>_sigma ds
                         <=C_T epsilon^4 n^2.            (F15)

D_-^(2) is a diagnostic sink, not an observed record channel. In particular this theorem does not assign hazards to the individual grades.

## 4. Return to the physical hole operator

A return based only on Y W Y*<=2W+C epsilon^2 n would be insufficient: squaring a positive operator inequality is invalid here. The following pair-projection argument supplies the needed bound.

Let R be a fixed radius containing the exact circuit cone of every w_a. For two centers whose cones are disjoint, write p'_a=Y w_a Y*, p'_c=Y w_c Y*. On the complete local A sets U_a,U_c,

 p'_a<=2 Q_(U_a)+C epsilon^2 I,
 p'_c<=2 Q_(U_c)+C epsilon^2 I.

Their support algebras are disjoint, so the two inequalities may be multiplied:

 p'_a p'_c <=4 Q_(U_a)Q_(U_c)
           +C epsilon^2[Q_(U_a)+Q_(U_c)]+C epsilon^4 I.   (F16)

Each Q_U<=sum_(u in U)w_u. Disjointness ensures that the pair term uses distinct holes. Bounded cone incidence implies that summing(F16) over all such ordered a,c costs at most C F_2+C epsilon^2 n W+C epsilon^4 n^2.

There are only O(n) remaining nearby pairs. For each such pair let U contain its complete common cone and P_(U,m) be its local hole-number sectors. The exact projection p'_(ac)=Y w_a w_c Y* obeys

 ||p'_(ac) P_(U,0)||<=C epsilon^2,
 ||p'_(ac) P_(U,1)||<=C epsilon,
 ||p'_(ac) P_(U,>=2)||<=1.                               (F17)

The first bound follows because neither the zeroth nor first Taylor coefficient can put two holes on a,c from a filled U; the second follows from the zeroth coefficient being zero on the one-hole sector. Applying the three-term norm-square inequality gives

 p'_(ac)<=3 P_(U,>=2)+C epsilon^2 P_(U,>=1)+C epsilon^4 I.

Bounded incidence for nearby pairs bounds their summed first term by C F_2, their second by C epsilon^2 W, and their last by C epsilon^4 n. Combining both classes proves the universal positive inequality

 Y F_2 Y* <= C F_2+C epsilon^2 n W+C epsilon^4 n^2 I.      (F18)

The identical proof applies with Y and Y* interchanged. Taking the appropriate expectation, using(F15) and the mean-hole estimate, proves the physical half of(F1). This return neither assumes that Y is globally close to identity nor hides a volume factor in a local cone.

## 5. Actual field residence of the global multihole part

For the specified reward q_h=1+sum_(dist(a(e),h)<=2)|E_e| there are at most114 links, so q_h<=1+114S. Define the positive diagonal multihole reward

 R_multi=1_(W>=2) sum_h w_h q_h.

It commutes with the occupation projectors and obeys the operator inequality

 R_multi <=(1+114S) W 1_(W>=2) <=(1+114S) F_2.             (F19)

Consequently in EITHER the actual physical or actual rotated state,

 epsilon^-2/n integral_0^T <R_multi> ds
       <= C_T epsilon^2(1+S)n
       <= C_(T,K,delta) epsilon n.                       (F20)

The last step uses the actual scaling epsilon^2 S(S+1)=delta/K and epsilon<=1. There is no field cutoff, field moment assumption, source replacement or first-event reduction in(F20). It bounds actual continuous-time occupation including all later original marks.

Thus along joint sequences with n->infinity and epsilon n->0, the GLOBAL multihole contribution to the positive first-field residence tends to zero. For epsilon n bounded it is uniformly bounded. A fixed horizon remains physical T; it does not shrink to a fixed fast-time interval. Global B occupation may be extensive and is not capped.

This is a restricted order-of-limits result. For arbitrary n(epsilon), the explicit bound C_T epsilon n does not close. The globally one-hole part retains its actual B background, fields, source coherences and possible dark dynamics. No estimate here controls that remaining part. In particular(F20) does not prove the full residence, quadratic energy mean, quadratic uniform integrability, full microscopic quantum generator or unique effective process.

## 6. Optional local collision consequence, with its volume price

Physical translation covariance and(F1) imply, for any distinct physical A sites u,v,

 <w_u w_v>_rho <= <F_2>_rho/n <= C_T epsilon^4 n.

The orbit sum over A-sublattice translations is a subset, with multiplicity at most the ordered-pair convention already present in F_2; equivalently fix the displacement and sum its n oriented pairs. For rotated local pairs use(F17) with Y* and the complete finite cone, then this physical pair bound and the physical one-hole bound. This gives

 <w_a w_c>_sigma <= C_T epsilon^4 n, a!=c,

also bounded separately by C_T epsilon^2. Therefore any fixed-range pair-hole interaction density has expectation at most C_T epsilon^4 n. This is not a volume-uniform local pair theorem. The explicit nonlinear-compensation current calculation in COLLISION_ALGEBRA uses precisely this price and no stronger claim.

No new numerical test proves(F1)-(F20). The small exact source-word control in this directory corroborates only the separate collision/operator example. These analytic results require focused reconstruction before being used as premises.
