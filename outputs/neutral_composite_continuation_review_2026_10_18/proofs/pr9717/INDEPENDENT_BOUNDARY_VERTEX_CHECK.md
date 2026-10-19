# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_BOUNDARY_VERTEX_CHECK.md`, SHA256 `56d25a955b775865c98cee2bb53a2846b60b3158f82dffdc33c7a73f6959a63d`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Independent native-boundary Schur-complement check

Reviewed `native/NATIVE_BOUNDARY_VERTEX.md` and `neutral_boundary_vertex.py`. The parity-block construction, resolvent signs, and normalization formula are correct within the stated selected native rung sector and finite region partition.

## Boundary symmetry and operator content

On one rung G_r=X0 X1 X2 commutes with h: the only Z factors in h occur as Z0 Z1, which acquires two minus signs. Each D_a=(Z0,Z1,Z2,Z0Z1Z2) anticommutes with G_r because it contains an odd number of Zs. A region product G=product_r G_r therefore commutes with all internal h and nearest-rung D D terms, while its boundary D_a is odd.

The original boundary V=−J sum_a D_a,left D_a,right flips both region parities. In the total-G-positive subspace it maps P=(++) to Q=(--) and conversely, with PVP=QVQ=0. Thus the block diagonals are the isolated-region Hamiltonians and the off-diagonal block is exactly the existing V. There is no missing same-parity direct boundary term. “Neutral” here correctly means region-G even; it is not full plane neutrality.

The D channels commute. On the joint physical boundary their products have eigenvalues t0,t1,t2 and t0 t1 t2, so V/J has eigenvalues −(t0+t1+t2+t0t1t2), belonging to {−4,0,4}. Hence the full boundary norm is 4|J|. The coordinate compression does not add any term or physical qubit.

## Exact elimination and normalization

For a full eigenvector (p,q), the Q equation is (E−H_QQ)q=V_QP p. When the inverse exists,

q=R(E)V_QP p, R(E)=(E−H_QQ)^−1,
[H_PP+Sigma(E)]p=E p,
Sigma(E)=V_PQ R(E) V_QP.

For real E outside the Q spectrum, R is Hermitian and

Sigma'(E)=−V_PQ R(E)^2 V_QP <=0.

The negative derivative is valid outside the spectrum, not only below it; below the spectrum Sigma itself is also negative semidefinite. With u=p/||p|| and a normalized full eigenstate,

1=||p||²[1+<u|V_PQ R² V_QP|u>],
Z_P=||p||²=1/[1−<u|Sigma'|u>].

The script implements these formulas with diagonal H_QQ in the isolated-region energy basis, including the correct negative derivative sign. Its product-ground probability |g[0]|² is distinct from the total P norm; the note correctly distinguishes them. The resolvent form is exact and energy dependent, not automatically an autonomous time-local P Hamiltonian. Real eigenvalues at a Q pole require a different treatment; the claimed finite ground-state application lies below that threshold.

## Perturbative diagnostic

For the disconnected product ground state with energy E0, the second-order coefficient is

−sum_q |V_q0|²/(E_q−E0),

assuming the reference branch and positive denominators used in this calculation. The script computes this and the order-lambda² Q-weight coefficient correctly. The diagnostic multiplier is applied only when comparing perturbation theory to the exact block problem. At native lambda=1, a roughly 30% Q weight and the reported second-order error do not support a weak-admixture truncation. This does not invalidate the exact Schur identity, nor show that every higher-order/resummed approximation fails.

In particular the single-region odd gap is not the pair-block denominator: the product threshold is higher by twice that gap. The supplied numbers give 2.928203230276 for the disconnected pair threshold, versus boundary norm four, so a naive norm/gap small-parameter argument is unavailable at full strength.

## Independent smaller native control

`/private/tmp/native-boundary-independent-control.py` independently builds the logical rung matrices with NumPy, proves their commutation/anticommutation identities by direct multiplication, and makes a native cut between ONE rung on each side. It constructs the full total-G-positive block, diagonalizes it, and compares exact Q reconstruction and P normalization. Results:

- ground energy −6.928203230275513;
- Q reconstruction error 1.44e−16;
- Schur equation residual 6.59e−15;
- total P weight 0.8333333333333353;
- derivative prediction 0.8333333333333335;
- boundary norm 4.

This checks the formulas and signs on a nontrivial native cut independently of the root's two-rung-per-region solver. The root's larger numeric values were source-reviewed, not independently rerun. The existing script compares them to its separately stored tube result, as stated.

## Interpretation

The calculation derives a finite feature/region coupling from the native boundary and a declared partition. A nonzero off-diagonal column of Sigma shows mixing between retained product states. It does not identify those states as physical matter, infer a common scalar charge, establish a static potential or bulk mediator, or choose a physical environment state. Retaining the exact energy dependence is justified; discarding it or identifying it as a local scalar action requires additional evidence.

## Added source-vertex check

Reviewed the new source-vertex section and the appended 16-eigenpair calculation separately. For a Hermitian observable O block diagonal in P/Q and real eigenvalues E_i,E_f outside the Q spectrum,

<f|O|i> = <p_f|O_PP|p_i> + <q_f|O_QQ|q_i>
          = <p_f|[O_PP+V_PQ R(E_f) O_QQ R(E_i) V_QP]|p_i>.

This proves the stated ordering and signs. Inserting O_QQ between the TWO different resolvents is essential; one cannot replace this by a single-energy static operator without a further approximation. Real resolvents are self-adjoint here. A later complex-frequency generalization must keep the adjoint on the bra-side resolvent rather than silently reusing this real-eigenvalue formula.

The raw P components of normalized full states already contain their sector weights. If p_i=sqrt(Z_i)u_i and p_f=sqrt(Z_f)u_f with normalized u_i,u_f, the matrix element is sqrt(Z_f Z_i)<u_f|O_eff(E_f,E_i)|u_i>. No additional normalization factor belongs when using the raw components. This agrees with the code.

The original H_L commutes with both region parities, so it is indeed block diagonal and qualifies for this formula. In the isolated-region eigenbasis its diagonal entries are the left eigenvalues repeated over right states, exactly as in `np.repeat(Es[+1],d)` and the corresponding odd block. The script's `rf @ (OLm * ri)` is consequently the correct induced contribution. The reported .795609755575−.466499660083=.329110095492 is consistent with the stated interference and source definition. Overall phase changes of f or i change all three signed amplitudes together; their relative cancellation and absolute transition weight are invariant.

For an O with P/Q off-diagonal blocks, extra terms O_PQ R_i V_QP and V_PQ R_f O_QP are required. Thus this particular simplified formula must not be applied directly to the boundary V itself. In particular, a uniform-total-energy conservation check needs all pieces of H=H_L+H_R+V and their respective vertices, not merely the two region-energy vertices.

An independent generic five-dimensional Hermitian block control (P dimension three, Q dimension two) tested all four transitions from its ground state, with nonzero induced terms and the normalized-P prefactors. Direct full-space and derived matrix elements agree below 1e−12. One transition has bare −.06828209976 and induced +.04163834623, yielding direct −.02664375352, explicitly testing destructive interference. A smaller native one-rung-per-region replay also passed the nonsingular algebraic cases, but those particular H_L transitions were zero; it is therefore not presented as an independent nonzero native source validation. The root's two-rung-per-region numerical transition was source-reviewed, not independently rerun.

This is an exact finite observable-dressing application to the existing Hamiltonian and partition. It shows why reproducing reduced eigenenergies does not justify discarding the induced vertex. It does not identify H_L as physical matter or establish a cosmological scalar/source coupling.
