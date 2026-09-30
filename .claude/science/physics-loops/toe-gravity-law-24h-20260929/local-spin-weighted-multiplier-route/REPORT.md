# A moving-hole field error for the finite-spin dark multiplier

Root analytic candidate. No focused independent check or formal review has yet occurred. The result is conditional mathematics for the supplied compensated leading W1 law, not microscopic M4, an unweighted finite-spin gap, or an axiom consequence.

## Actual inputs and statement

Use the complete physical W=1 sector on even cubic tori L>=28, integer S>=1, C=S(S+1), and delta,kappa>0. Global B occupation, charges, field superpositions and spectator ancillas are unrestricted within that spin box and Gauss law. The exact Hamiltonian is H_S=Hbar_S+Delta_S, with its original compensation gates, and A_S=-i delta H_S-kappa G_S/2. G_S=J_S*J_S uses either the original resolved marks or the original unnormalized coherent-edge marks, separately. Hbar and G have the previously checked one-hole cancellations and bounds744 and12. They are not surrogate walks or scalar recycling maps.

The full rotor sparse-dark argument96c08 and its root focused check0950c40b supply a bounded Hermitian signed partial permutation O=i(V*-V), the diagonal reward Pi=P+B, and

 T=aI-O/delta, 0<=T<=C_loc I, [T,Pi]=0,
 L_infinity(T)<=-Pi.

Here P means a dark hole with at most nine occupied B sites within distance three, B means at least one empty B neighbor, and V uses the fixed first clean axial two-hop path. With M=1092,

 Xi=2delta M+(4delta M+10kappa)^2/(4delta),
 a=1/delta+(Xi/delta+1)/(2kappa), C_loc=a+1/delta.

Those identities were independently checked before this reuse. The finite-spin link and full cancellation input is the checked REPORTd0a96836; its global-field transfer conclusion is not a premise for the new local bound. Actual main local-compensation and formation-balance/dark-state sources were freshly read at30a9461ee19a49b99fa6628fe942f08e504e8903. The latter concerns effective formation and does not supply this fast-sector multiplier. Axiom/primitive source bytes remain unchanged under selected methodology7146fe17a76de41badcaca3c3c7cac6d11eb2a00. All carrier, Hamiltonian, time and instrument choices remain supplied.

Let P_S be the entire physical spin-box projection in the common rotor Hilbert space, and compress T_S=P_S T P_S and Pi_S=P_S Pi. For a basis word with hole h define

 q_h=1+sum_(edges meeting B12(h))|E_e|,
 Q_loc=sum_h P_h q_h.

The radius is a safe fixed bound in graph distance; it is not a new cutoff in the evolution. Define

 K_loc=1000000+24a kappa+1000kappa/delta.

The candidate inequality is

 A_S* T_S+T_S A_S <= -Pi_S+(K_loc/C)Q_loc^2.           (1)

All operators in(1) are restricted to the physical finite-spin sector. Its constants are independent of volume, distant fields and global B count. Q_loc itself is evaluated on the actual moving hole and may be large. No bound on its expectation is included in(1).

## Compression keeps the actual boundary terms

Extend each normalized spin link shift by zero outside its allowed box, exactly as in the checked comparison. Its weight u_S(m,sigma) lies in[0,1]. For every integer input m, including forbidden boundary transitions and exterior values,

 |1-u_S(m,sigma)|<=m(m+sigma)/C<=(|m|+1)^2/C.          (2)

Inside the box this follows from1-sqrt(1-x)<=x; on forbidden transitions the integer numerator is at least C. These extended local words define Hbar_S, Delta_S and G_S on the common space. They preserve P_S. On each finite torus they are bounded; no infinite-volume domain shortcut is required here.

Put D_H=Hbar_S-H_infinity and D_G=G_S-G_infinity. Because the actual spin generator commutes with P_S, direct compression of the products gives

 L_S(T_S)=P_S L_infinity(T)P_S+P_S E_S P_S,
 E_S=-a kappa D_G-i[D_H,O]-i[Delta_S,O]
                         +kappa/(2delta){D_G,O}.      (3)

Rotor paths leaving the spin box are not thrown away in this equality. They occur in the extended differences in(3). The extensive diagonal Hamiltonian cancels against the scalar aI, leaving only its commutator with O. T_S remains positive, bounded by C_loc, and commutes with Pi_S because P_S and Pi commute. O need not preserve P_S.

## Weighted finite-word estimate

For any matrix M on the physical word basis, suppose

 |M_xy|<=q_x q_y b_xy/C,
 sup_x sum_y b_xy<=B0, sup_y sum_x b_xy<=B0.

Schur applied to the nonnegative b matrix, or2uv<=u^2+v^2 term by term, gives

 |<psi,M psi>|<=B0<C^-1 Q_loc^2>_psi.                 (4)

The same conclusion holds for a sum of word paths before their coefficients are combined. This avoids assuming that their different paths are orthogonal. Every elementary legal charge/field hop is a partial permutation; the retained two-hop expansions have row and column path budget at most744. O has at most ONE unit-modulus entry in every row and column because its dark input and selected bright image are disjoint and V is injective.

The actual two-hop Hbar words move the hole by at most two and use links within radius three of their incoming hole. O moves it by two; its occupancy selector is within radius three of the dark end and hence radius five of either input end. In either product D_H O or O D_H, the net hole displacement is at most four and every link entering a spin weight is within radius seven of both endpoint holes. In particular all those link values occur in both radius-twelve sums. There are at most four elementary shifts along any path. At either endpoint word x, an intermediate field therefore obeys |m|+1<=q_x+4<=5q_x; the same holds relative to y.

For a two-hop word, telescoping its two weights using0<=u<=1 and(2) bounds its spin-minus-rotor coefficient by50q_x^2/C and also by50q_y^2/C. Therefore it is at most50q_x q_y/C. Each product with O has row and column path budget744. Equation(4) yields

 |<psi,i[D_H,O]psi>|<=74400<C^-1 Q_loc^2>_psi.        (5)

This includes spin paths that vanish exactly at a boundary. It does not estimate the difference only on a chosen set of field samples.

## The extensive compensation cancels locally

O connects only a dark word at h and its selected axial output at c, with dist(h,c)=2. Their B OCCUPATION mask is identical; only the occupancies at h,c, the charges at h,c and their shared B, and two link fields change. A compensation term Delta_a can differ only when a is h or c, or when its radius-two occupancy gate contains h or c. The changed link and charge cases are already in that set. It has at most38 A centers and at most228 incident electric links, all within radius five of BOTH endpoint holes. Every other diagonal summand commutes with this matrix element of O exactly, regardless of how large its distant field is.

On physical spin endpoint words each Delta_a is a sum of at most six nonnegative terms

 n_a(1-n_b)Q_a E_e(E_e+sigma_a)/C.

The integer electric polynomial is bounded by(|E_e|+1)^2. For either endpoint weight q_x, the electric term at the other endpoint has changed by at most two units, so its squared bound is at most9q_x^2. Counting both endpoints and all228 incidences gives a bound at most2280q_x^2/C, and likewise in q_y. The O coefficient has modulus one and at most one per row/column. In particular the convenient larger estimate is

 |<psi,i[Delta_S,O]psi>|<=10000<C^-1 Q_loc^2>_psi.     (6)

Equation(6) uses only physical endpoint words in P_S E_S P_S. It never replaces a distant term by a local approximation or assumes ||Delta_S|| volume-uniform. It is also insensitive to the discontinuous occupancy choice of the first clean axis: O does not change that choice inside the diagonal commutator.

## Original losses and the final inequality

On any physical endpoint word, the exact original loss difference is

 D_G=-2 sum_(vacant neighbors of the hole) E_e^2/C.

Thus |<D_G>|<=2<C^-1 Q_loc^2>, safely below24 times that quantity. In a product with O, all six relevant loss links lie within the local balls of BOTH endpoint holes. The two-hop field change is at most two, so a coefficient of D_G O or O D_G is bounded by18q_x q_y/C. The two products and their one-entry row/column budgets imply a bound36 in(4). The deliberately larger contribution1000kappa/delta covers its factor kappa/(2delta) in(3).

Combining(5),(6), the loss estimates and the checked rotor inequality proves(1) with the stated K_loc. The million-sized first term is only a conservative finite combinatorial bound, not a physical prediction or fitted value. All estimates tensor with spectator identities and hold on the physical Gauss subspace because the actual words and all projections preserve it.

## Conditional response consequences

For the actual spin no-event solution Z_S(t), positivity and differentiation of T_S give, for every horizon,

 integral_0^T ||Pi_S Z_S(t)psi||^2 dt
 <=C_loc||psi||^2+(K_loc/C)integral_0^T||Q_loc Z_S(t)psi||^2dt. (7)

This is a local weighted error identity/estimate. Its rightmost integral is part of the conclusion's cost, not an unproved hypothesis renamed as a theorem. Mixed states and ancillas follow from the operator inequality.

For y'=A_S y+f, y(0)=0, f=Pi_S f on a finite interval, set F=||f||_L2, P=||Pi_S y||_L2 and W=||Q_loc y||_L2. Integrating(1) gives

 P^2<=K_loc W^2/C+2C_loc P F,
 P<=2C_loc F+sqrt(K_loc/C) W.

The exact original passive identity therefore bounds the FULL actual terminal-plus-mark amplitude output by

 ||y(T)||^2+integral_0^T kappa||J_S y(t)||^2dt
 <=4C_loc F^2+2sqrt(K_loc/C)WF.                       (8)

The original J_S is retained, including coherent-edge phases. A general forcing is not asserted to be a normalized physical CP source. No imaginary-axis resolvent, total lifetime, or dense-dark residence bound follows.

In physical time t=epsilon^2 u, imposing the supplied combined scaling C=delta/(K epsilon^2) rewrites(7) as an O(epsilon^2) initial reward plus (K_loc K/delta)epsilon^2 times the physical-time integral of the actual local field weight. This shows the precise prospective consumer. It does NOT prove that integral uniform for the actual positive-time microscopic source, which remains a substantial open weighted-moment and coherence obligation. The new result also does not solve several holes or identify the apparatus/physical clock.

## Evidence state

This analytic report is a candidate frozen before new controls and independent checking. No new control results are asserted here. Earlier full cancellation, rotor multiplier and original link-boundary controls remain their original source-bound evidence. A finite control of the local compensation cancellation and boundary-sensitive compressed commutator is planned separately; it cannot establish the all-field form estimate by sampling.
