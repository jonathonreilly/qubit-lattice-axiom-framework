# Native complementary hopping at fixed height

Status: exact-support for the coefficient; conditional-support for its prepared vacuum-background window. No empirical identification.

## Premises and conventions

Use the existing one-qubit Hamiltonian H=-J sum_z ZZ-J lambda(sum_x XX+sum_y YY), J>0, and its fixed canonical Schrieffer-Wolff block convention. The transverse box is even, periodic, R>2L; longitudinal height L is fixed and even. Coefficient statements use L>=4; the separated neutral window uses L>=6. Take lambda to zero after fixing R,L. A singleton at layer zero of column i is moved to nearest column j at the same layer. Background labels refer to majority column signs. E_ij=Xbar_i Xbar_j. Prepared states and readout use the matching canonical dressing; no new physical interaction is introduced.

## Exhaustion and exact coefficient

A final reversed-background set A requires |A| even by longitudinal plane parity. Its physical Hamming distance from the initial singleton is |A|L+2-2|A intersect {i,j}|. Each transverse insertion flips two physical spins. The unique nonempty A achievable in L-1 insertions is {i,j}. Equality forces the edge (i,j) at each complementary layer 1,...,L-1 exactly once. No proper intermediate subset returns to the two-wall block, so folded normalization terms cannot contribute to this minimal background-changing matrix element.

For a proper nonempty subset S of the complementary chain let c(S) count its connected components and a(S) its occupied endpoints. The intermediate energy above the initial two-wall state is 4J[2c(S)-a(S)]. With v(empty)=1, the positive path sum obeys

    v(S)=sum_(b in S) v(S without b)/[4(2c(S)-a(S))],
    a_L=sum_b v(full without b)=2^{-(L-2)}.

Here is an all-length evaluation, rather than extrapolation from the finite recurrence. Encode the same subset paths by n=L-1 auxiliary Ising bits with Hamiltonian -2 sum_(k<n) Z_k Z_(k+1)-lambda sum_k X_k. This is an algebraic encoding, not an additional lattice interaction. The two aligned states have precisely the denominators above. In the Majorana representation the positive single-particle singular values come from the n by n bidiagonal matrix with diagonal lambda and subdiagonal 2. Its determinant is lambda^n; n-1 singular values approach 2, so its smallest singular value is lambda^n/2^{n-1}[1+O(lambda^2)]. The many-body doublet splitting is twice that singular value. Therefore the leading off-diagonal matrix element has magnitude lambda^n/2^{n-1}, proving the path sum. This uses the standard open-Ising/Majorana algebra; it does not claim that algebra as new.

The native x insertion signs give negative amplitude. For even L the y phase gives the corresponding column-sign factor. Consequently the background-changing pieces are

    x: -J 2^{-(L-2)} lambda^(L-1) E_ij,
    y: +J 2^{-(L-2)} lambda^(L-1) Zbar_i Zbar_j E_ij
       =-J 2^{-(L-2)} lambda^(L-1) Ybar_i Ybar_j.

The exact recurrence checks L=2,...,15; L=2 and odd L are algebraic controls only, not extensions of the declared physical result.

## Prepared neutral-window connection

Use the previously derived vacuum fourth-order plaquette Hamiltonian and winding bound in LIGHT_COLUMN_WINDOW_PROOF.md. Let P0 project onto flat plaquettes. Any actual vacuum-block ground g_lambda obeys ||(1-P0)g_lambda||=O_(R,L)(lambda^(L-4)). Define g0=P0 g_lambda/||P0 g_lambda||; a limiting vector within the degenerate flat manifold need not be selected.

Every background-diagonal nearest-x coefficient is constant on P0 by exact plane symmetries: X on x-normal planes supplies no singleton phase; Y on y-normal planes supplies equal phases at the two x-neighbors. The canonical order-one and order-three coefficients are scalar on the entire background space: -I and +I/8. The latter cancellation, including folded terms, is established in NATIVE_ASSISTED_HOP_PROOF.md and replayed at height six. Only odd orders occur by transverse bipartite parity. Hence the first potentially nonconstant diagonal coefficient is order five. Its centered action on g_lambda is O_(R,L)(J lambda^(L+1)), because (D-dI)P0=0. It cannot obscure the order L-1 background-changing vertex.

E_ij g0 has exactly four bad plaquettes, norm one, and is orthogonal to P0. The prepared vacuum-background Hamiltonian places this component in its four-plaquette window

    Delta4=JL lambda^4/16 [1+O_(R,L)(lambda)].

Projecting the centered nearest-x block into that window gives leading vector -J 2^{-(L-2)} lambda^(L-1) E_ij g0. Its squared weight is

    J^2 2^{-2(L-2)} lambda^(2L-2) [1+o_(R,L)(1)].

Finite-box perturbative projection and vacuum admixture give only higher orders. There is no background-dimension multiplicity factor.

## Scope and unresolved bridge

This is a prepared background-channel infinitesimal Hamiltonian vertex. Delta4 is a vacuum-background excitation energy, not an outgoing eigenenergy of the full particle-plus-environment Hamiltonian. The result is not an emission rate, scattering cross section, relaxed-heavy coupling, bare-state protocol, or observable cosmological scalar. Intra-block gauge changes require simultaneous transformation of the state and readout; arbitrary rotations cannot be mixed with this coefficient convention.

No uniform growing-height estimate or selection of L is proved. Choosing L to suppress the coupling supplies a hierarchy rather than deriving its physical value. J, lambda, geometry, state preparation and measurement identification remain premises. All checks are exposed model development, with no independent empirical data test.

Prior-art context: P. Fendley, Strong zero modes and eigenstate phase transitions in the XYZ/interacting Majorana chain, https://arxiv.org/abs/1512.03441 (2016), is context for established Ising/Majorana pairing, not a measured input or a new-interaction premise.
