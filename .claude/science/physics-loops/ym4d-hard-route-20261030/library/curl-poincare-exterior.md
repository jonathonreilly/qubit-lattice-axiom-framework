# Curl-Poincare on a box minus separated cubes

Producer: `parts/hard-core--mapped.md`, Text 5. Status: per statement. Not reviewed.

Credit: base-point averaging of a homotopy operator is the idea of Iwaniec and Lutoborski; axial gauge is standard. The lattice identity and the patching below are mine. Nothing here uses the account.

Consumer: exterior coercivity near a hole, (P_k) step 3 and `Z_Ext` in Prop R1.

## Lemma 1 (exact identity on a lattice box). Proved here, abelian.

Let P be a product of lattice intervals of spacing eta, with sides at most l, in d dimensions. Let H be a real bond field on P, with bond variable eta H_i(x), and curl_ij H(x) := (d_i H_j - d_j H_i)(x), with d_i the forward difference over eta. For y in P, let Gamma(y,x) be the path that changes coordinates in the order 1, ..., d, and

    omega(x) := avg_y sum_{j=1}^d eta sum_{t between y_j and x_j} H_j(x_1, ..., x_{j-1}, t, y_{j+1}, ..., y_d).

Then, with S_ij := eta sum_{t between y_j and x_j},

    H_i(x) - d_i omega(x) = avg_y sum_{j>i} S_ij [ curl_ji H ](x_1, ..., x_{j-1}, t, y_{j+1}, ..., y_d),   curl_ji := d_j H_i - d_i H_j,

with the oriented sum over t, and therefore ||H - d omega||_2 <= sqrt(2(d-1)) l ||curl H||_2, with no constant depending on eta. (The factor 2 is N/(N-1) <= 2, from N sites against N-1 bonds per coordinate, N the number of sites on a side.)

*Proof.* d_i acting on omega: the terms with j < i do not depend on x_i. The term j = i gives avg_y H_i(x_1, ..., x_i, y_{i+1}, ..., y_d), exactly, by the telescoping of the sum over t. The terms j > i give avg_y S_ij d_i H_j at the same arguments. Telescope H_i(x) in the coordinates i+1, ..., d, from y to x: H_i(x) - H_i(x_1, ..., x_i, y_{i+1}, ..., y_d) = sum_{j>i} S_ij d_j H_i at the same arguments as above. Subtract. For the norm, fix i, j. |S_ij F| <= l times the average of |F| over t in the interval j, so the term is at most l times the partial average of |F| over the coordinates j, ..., d, at fixed x_1, ..., x_{j-1}. A partial average is a contraction of L^2. QED

The kernel is not singular, because the paths are axis parallel and the base point is averaged. No Calderon-Zygmund bound and no cone is used.

Numerical check of the identity and the bound: `checks/hard-core--mapped_curl_poincare.py`, criteria written first: d = 3, 4, up to N = 17, 9, random, gradient-plus-small and smooth fields. PASS: sup error at most 4e-14, ratio to the bound at most 0.21.

## Lemma 2 (patching on a union). Proved here, abelian.

Let E be a union of unit cells of the level-k lattice, connected through faces, contained in a cube of side 3L. Suppose E has trivial first homology as a cell complex. Then there is omega on fine sites of E with ||H - d omega||_{L^2(E)}^2 <= C(E) ||curl H||_{L^2(E)}^2, C(E) free of eta. Since there are finitely many E for each L, sup_E C(E) =: C_1(L) is finite. It is not computed.

*Proof.* On each cell c take omega_c from Lemma 1. On two face-adjacent cells take P = c u c', with omega_{cc'}. Then omega_c - omega_{cc'} on c is a function whose gradient has norm at most C ||curl H||_{c u c'}, and on a cell this is, up to a constant, bounded in L^2 by the discrete Poincare inequality. So the constants a_{cc'} := mean over the shared face of omega_c - omega_c' obey |a_{cc'}| <= C ||curl H||_{c u c'}. Around a level-k vertex or an edge or a 2-face of the complex the constants close up to the same bound, by applying Lemma 1 on the product box containing the cells, or a chain of them if the cells around it do not fill a box. So a is an approximate cocycle on the dual graph: its sum around each elementary dual loop is at most C ||curl H||_{loc}. Elementary dual loops generate the cycles if the first homology of E is trivial. So there are constants b_c with |a_{cc'} - b_c + b_c'| <= C(E) ||curl H||_E, by finite-dimensional linear algebra on a graph with at most (3L)^4 vertices. Let omega be built from omega_c + b_c with a partition of unity at the unit scale. Then d omega = sum chi_c d(omega_c + b_c) + sum (d chi_c)(omega_c + b_c), and the last sum is the differences of the omega_c + b_c, bounded as above. QED

*What is thin here.* "Closes up around a 2-face": a dual elementary loop corresponds to a codimension-2 face of the complex, and the cells around it are at most 4 cells, which fill a 2 x 2 box if all are in E. If not all are in E, that loop is not a loop of the dual graph, so there is nothing to check. So every elementary dual loop is the boundary of 4 cells forming a box, and Lemma 1 applies on it. Then H_1 trivial means these loops generate the cycle space of the dual graph. I have used that without a proof for a general E; for a box minus separated cubes it is a direct check, since the complex deformation retracts on a 3-dimensional skeleton in which a general position argument pushes a loop off the cubes.

## Corollary 3 (level-k variations). Implication, abelian.

Let v be a level-k bond variation on E, H a fine field with block data Q H = v, and q_E(v) the minimum of ||curl H||^2_{L^2(E)} over such H. Then there is a level-k scalar omega-tilde with ||v - D_k omega-tilde||^2_E <= C_2(L) q_E(v).

*Proof.* Q D = D_k r, exact on the whole lattice by Lemma 3.1 of the producer. If the lines of Q at a bond of E stay in E, then v - D_k r omega = Q (H - d omega), bounded by Lemma 2, since Q is bounded from L^2 of its support to a number by Lemma 1 of the energy package. QED

*Bonds whose lines leave E.* v on them is not controlled this way. With the restricted operator Q_restr, excluding lines that leave E, the identity Q_restr D = D_k r fails by a contour term. It is a difference of restricted contour averages at the two ends, which is a gradient of a different scalar, and so harmless, if the restricted family at each end is still non-empty. The consumer must say which line family it uses.

## Corollary 4 (tree gauge on E removes omega-tilde). Proved given Corollary 3.

Let T be a spanning tree of the level-k vertices of E inside E. If v = 0 on T, then ||v||^2_E <= C_3(L) q_E(v).

*Proof.* On T, D_k omega-tilde = -(v - D_k omega-tilde). So differences of omega-tilde along T are bounded by C(L) ||v - D_k omega-tilde||. Hence ||D_k omega-tilde||_E <= C(L) ||v - D_k omega-tilde||_E. Add. QED

A tree of the box does not restrict to a spanning tree of E. A tree fragment structure leaves piecewise-constant zero modes on non-tree bonds. So the tree must be chosen for the hole: a spanning tree of E extended into the hole. The integrand is gauge invariant, so this is an exact change of chart on each term with fixed site. See the producer for what this does to the line constraint.

## Non-abelian form. Not proved; sketch, with what it needs.

At a background U with R(a) on E, and a L^2 small (a_* in the numbers of the producer): in the axial gauge of a cube of side 3L, U = exp(i eta A-tilde), |A-tilde| <= C a L, and d_U H differs from d H-tilde by at most C a L |H-tilde|. So the abelian lemma applied to H-tilde gives ||H-tilde - d omega||^2 <= C_1 ||d_U H||^2 + C_1 (a L)^2 ||H-tilde||^2. Here there is an unwanted term in ||H-tilde||^2, not in ||H-tilde - d omega||^2. On d omega itself, d_U d_U omega = [F, omega], so the error should be read on omega: in the end, for v with v = 0 on T, it closes by a smallness of a in terms of L, C_1, C_3, as in Theorem 5 of the energy package. Status: expected by the same absorption; not written.

## Uniformity in k

Lemmas 1 and 2 are uniform in eta. Corollary 4 is uniform in k. C_1, C_2, C_3 depend on L and on the hole shape only through finitely many cases.

*Why dependence on L is allowed.* Those constants enter a_*(L) and x_0(L) only. They do not enter the contraction of the main term of the lift. Warning: this must be re-read against any place where a_*'s dependence on L feeds a threshold ratio. T_f/T_c = L/(C_r K_0) has no a_*, so it is safe there.
