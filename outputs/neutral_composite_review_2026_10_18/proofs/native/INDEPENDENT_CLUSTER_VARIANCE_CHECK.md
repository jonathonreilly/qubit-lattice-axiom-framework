# Independent cluster-product variance identity check

The identity in `native/compass_cluster_variational.py` is correct for the infinite product tiling and its distinct-neighbor block graph. It does not require self-consistency, a real wavefunction, or commuting operators within a face.

Let each block have normalized state psi. Expand each interblock term −A_i(B) B_i(B') using A_i=m_Ai+delta A_i and B_i=m_Bi+delta B_i. Collect the constants into the exact energy, all single-block operators into h_eff(B)−<h_eff>, and the remaining terms into −sum_i delta A_i(B)delta B_i(B'). Acting on the product state, the single-block vectors excite only one block orthogonally to psi, while each remaining vector excites exactly its two endpoint blocks orthogonally to psi.

Vectors with different sets of excited blocks are orthogonal. In particular, pair vectors sharing only one block are still orthogonal because the other endpoint has a centered expectation. Consequently, for a translationally repeated block on a simple block graph,

Var(H)/N_blocks = Var_psi(h_eff) + sum_(positive neighbor directions) ||sum_i delta A_i psi tensor delta B_i psi||².

The sum is once per undirected neighboring block pair. Its face contribution is

sum_ij G_A,ij G_B,ij,

where G_A,ij=<delta A_i psi,delta A_j psi>=<delta A_i delta A_j> for Hermitian A. There is NO extra complex conjugation on one G. Although individual entries can be complex, the full sum is a nonnegative real squared norm. The code's `upper.conj() @ upper.T`, analogous lower matrix, and `sum(gu*gl).real` use exactly these indices. In the native compass face, the operators on that face in fact commute, but this simplification is unnecessary.

For coupling −J, single-block h_eff includes J and the face term has J². The supplied code takes J=1. Dividing the formula by the number of physical sites per block gives its `full_variance_per_site`.

## Checks on implementation and boundaries

The script correctly rebuilds h_eff using the actual final state's moments, rather than the damped previous iteration. Thus the variance identity remains valid for a stopped nonconverged iteration. The energy expression counts internal bonds once and positive-oriented interblock faces once, while h_eff contains both incoming and outgoing mean-field terms; this distinction is correct.

One must group ALL interactions connecting the same unordered block pair before taking the pair-vector norm. A periodic array with only two blocks along an axis has repeated endpoint pairs and needs cross terms between the two faces. Summing face norms separately there would fail. This is not an issue for the infinite tiling or periodic block arrays with at least three blocks per axis and the usual distinct-neighbor graph. Internal block side length two does not itself create that problem in an infinite tiling.

## Scope

A tiny local residual certifies approximate stationarity only for the self-consistent single-block effective operator. The exact global variance retains interblock pair excitations; it can remain extensive and order one per physical site despite a local residual near machine precision. The reported positive full variances therefore cannot be discarded when assessing finite-volume stationarity. Neither a locally converged branch nor its energy improvement proves global variational optimality, an actual ground state, or native excitation dynamics. An infinite-volume local stationarity claim would also need its own argument rather than simply extrapolating finite-volume total variance.

This source supplies the identity and its implementation boundary. Historical execution reports are preserved separately and confer no current execution standing.
