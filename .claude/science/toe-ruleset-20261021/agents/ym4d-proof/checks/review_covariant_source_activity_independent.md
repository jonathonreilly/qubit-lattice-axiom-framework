# Independent analytic reconstruction, before author checker inspection

Target: `COVARIANT_SOURCE_ACTIVITY_ASTRA.md`, SHA-256 `da22fc28cff8f822426ccd0458959dc24668f3d8854848f8ff83dbcda9f2ba54`, SA1–SA34. This record is frozen before the author scientific Python and raw numerical outputs are inspected. The complete source, including §8's advertised diagnostics, and the parent task's descriptions were exposed. This is an independent reconstruction, not a blind review. Requested Astra/max; same-family Codex review, with no independently observed backend metadata. No role in the producer implementation.

The numerical criteria were recorded first in `review_covariant_source_activity_criteria.md`. The resulting geometry, matrix, incidence, flux and fibre implementations are separate from the author's code. None of their initial executions failed. The second incidence implementation strengthens the first matrix diagnostic's closed-form count by actually generating all 65,536 sparse product atoms; the original code and result remain. No tolerance or parameter acceptance criterion was relaxed. A metadata reader initially assumed the author's receipt used a `files` field; its `bound_files` field was then used and all twelve bindings verified. That administrative error was before scientific checking.

This analytic reconstruction finds no blocking error in the selected-sector statement. This is not the final evidence verdict: author-code linkage and controls are still to be inspected. Full existence, continuum construction, physical gap, and the H24/complement integration are outside the result.

## 1. Fixed normalization, local variables, and actual read support

Use the CB rooted tree quotient, its probability-Haar normalization, its per-link traceless relative principal-log chart, and the original coarse field V. There is no global logarithm of V and no gauge reduction of its holonomies. Write sigma²=N/u and F=sigma²(S_eff−sum log j_N). Thus the coordinate density is h_N^n exp(−F/sigma²) dA and adding epsilon_p W_p to F gives the physical source u epsilon_p s_p. The fixed-real-t single normalizer is part of F; t is not complexified by the source. The full scalar dimension is n_d=D n, D=N²−1.

The paired paths at U0(V) live in the two blocks of their directed coarse edge and read that edge's V. Fine Wilson vertices can read the coarse edges on a double face. Their blocks have diameter at most two from either incident free-coordinate block. Haar reads no V. This gives the claimed finite range of K_b; it also resolves the potential SA6–SA8 collar mismatch. In a residual factor K_{ik} with k in Omega_q, measure the actual read stencil from the **inner index k**. The outer i and all data read by this entry are within two blocks of k. One does not need the sum of an outer two-block displacement and an independently pessimistic radius-three stencil. D_q of radius R+4 is therefore sufficient. The source could state this inner-index argument explicitly, but no enlarged collar is required.

The checks generate the actual 24 permutations and paired transverse/longitudinal words, not a nearest-neighbour surrogate. They inspect 124,416 words on each of T=2 and T=3, including wrap/corner anchors, and all 7,776/39,366 fine plaquettes. A crossing edge occurs in exactly 72 of its 1,944 kernel words and in no other kernel. T=2 has fourteen distinct candidate endpoint kernels, T=3 fifteen, because the far positive periodic seam is a different edge. A changed remote coarse link changes a genuine Wilson Hessian entry while the row block's own V is fixed. This prohibits dropping the read collar. These finite checks support, but do not replace, the geometry argument above.

## 2. Patch inverse with both absolute norms and support incidence

For each real interpolation K_theta between cI and K_b, principal compressions retain the uniform CB gap gamma. Conjugating a range-two matrix by exp(m d) changes it by at most (exp(2m)−1) times a uniform absolute row/column bound. Choosing m by the stated gap margin gives the finite-volume compression resolvent bound. Summing entries over the torus is bounded by summing periodic images on Z^4; the scalar multiplicity n_0 belongs in Q_m. This argument neither deletes a torus mode nor assumes a scalar colour tensor.

Partition into R-boxes of side R to 2R, with a single box in a small direction when necessary. Omega_q is the radius-R neighbourhood, and P_q=(K_{theta,Omega_q}+a)^{-1}1_q. Set R_q=−1_{Omega_q^c} K_theta P_q. Then

    (K_theta+a) P = I−R,       G=P sum_{k>=0} R^k.

The sign and right ordering are essential; neither P(I+R)^−1 nor (I−R)^−1 P generally equals G. Both were tested with noncommuting colour transports. Each term reads only D_q and its output/input blocks lie there. D_q touches at most J=9^4 R-boxes for R>=4, and any box meets at most J such labels. Quotienting on a small torus reduces these counts. The number of scalar coordinates in a box is bounded by n_R, including the case where the whole torus is a single box and R=0 as a *residual matrix*.

The exponential entry bound gives row and column sums p(a), r(a). For R_q, a nonzero outer index is more than R from the input in q; split off half the exponential to obtain the exp(−mR/2) suppression and still sum both indices. This is an absolute defect estimate, not a cancellation estimate. Summing possible marked input coordinates gives B(P)<=J n_R p and B(R)<=J n_R r. With M=max(absolute row, absolute column), composition has

    M(AB)<=M(A)M(B),
    B(AB)<=B(A)M(B)+M(A)B(B).

For the second term a marked B atom fixes its input/read vertex but the A factors must be summed over outputs; this uses the **column** bound. Connected labels meet at the summed index, so their union remains connected. Summing the words gives B(G)<=J n_R p/(1−r)^2. Choosing R after beta=mu+4 makes the quoted A_G finite and independent of volume.

The independent 90-scalar matrix has noncommuting three-colour transports and nontrivial cycle holonomy. All four resolvents satisfy the actual patch identity to below 7e−16 and the full reconstructed inverse to below 3e−16; weighted residuals are below 0.031. Its read-collar perturbation changes P_q by 8.77e−10. A separately generated sparse star family has A_{(j,r),j}=1 and B_{jj}=z_v, with support labels {leaf,j} and {j,v}. Its product has 65,536 labelled entries at the remote mark v. Direct summation gives B(AB)=1.0666e10, exceeding the row-only purported bound 4.5497e9, while the correct bound is 5.8463e11. Omitting the remote mark also fails. This is a support-algebra counterexample, not a Yang–Mills matrix identification.

Support **size** is charged throughout. Filling an R-box label Y into original blocks costs at most (2R)^4 |Y|. Rooting at an original block picks its unique R-box, so the return norm at rate mu/(2R)^4 follows without an extra root multiplicity. This construction does not promise a prespecified arbitrary original-block rate; choosing R after beta is essential. Conversely, pushing an original-block H24 norm into boxes requires the stated maximum box population factor. Diameter alone, or a label containing only endpoints, would not suffice.

## 3. All orders, covariance branch and determinant

Every elementary Wilson/kernel/Haar vertex is holomorphic in the relative chart with the fixed-real-t bounds already supplied by CB. Expand its complete Taylor series, rather than truncating to a polynomial. The field-map norm counts an output-rooted sum and a sum rooted at any original-data/read vertex. For a degree-n nonlinear force term, marking either its elementary vertex or one of its n background factors gives the factor n+1; differentiating the fixed-point map adds n. Hence the source majorant N(t)=d_1 exp(beta s)[S(t)+t S'(t)] and its derivative contain the required n(n+1) multiplicity. The absolute series converge below the chart radius. Their multiplication/composition rules are exactly the incidence estimate just proved.

The force at zero is O(delta_V), including source dependence: Wilson plaquettes are flat at delta_V=0 and both the Haar and normalized-kernel force at the lift vanish there. Choose tau, then rho_0, then delta_A so that the explicit map and derivative bounds hold. N'(0)=0 and the Hessian defect at zero tends to zero with the source radius, so these choices are not circular. The complete Banach-space contraction yields a unique b_epsilon with norm at most C_b delta_V. Picard iteration converges in the atom norm, preserving locality and holomorphy in the product epsilon disc. Every iterate vanishes on a flat background, even with nontrivial holonomy.

Here the small-curvature class of real V is not a complex product polydisc in independent coarse links. The result supplies original-V read locality and real-analytic local formulas (with local complex extensions where the chart and inverses persist), and product-disc holomorphy in epsilon. It does not supply an unrestricted coarse-link complex polydisc.

The Hessian defect Delta_epsilon is obtained by differentiating these convergent elementary series. The stated D_K bound includes the background incidence multiplicity. If A_G D_K<=gamma/2, the resolvent is G sum_n(−Delta G)^n and its atom norm is bounded by A_G/(gamma+a−A_G D_K). The inverse square root is the Stieltjes integral pi^−1 int_0^infinity a^−1/2 (K_epsilon+a)^−1 da. Its integrated bound gives Q_C, and analytic continuation from real positive precision chooses the branch. The matrices are complex symmetric: C_epsilon^T K_epsilon C_epsilon=I, with transpose, not adjoint. Nothing assumes independent identical colours. The matrix check compares this full Stieltjes integral with the spectral square root to 1.12e−15.

For log det K_b, interpolate from cI and integrate Tr(K_theta^−1(K_b−cI)). Trace closure is bounded by the marked incidence norm of the product. The constant n_d log c is distributed with the actual n_d scalar degrees and bounded using n_R. The defect log is the absolutely convergent trace-log series of G Delta; its 1/n cancels the n choices of marked factor. The density prefactor retains det(K_0)^−1/2. The diagnostic reconstructs the full 90-scalar log determinant, 66.32940763965354; three times one colour determinant gives 64.8028770685665 and is rejected.

## 4. Exact sector factorization and actual small activity

Define the *fixed real* set Omega(V) by A=b_0(V)+sigma C_0(V)W, |W_i|<=p. All epsilon use that same real set. Its exact integral is

    h_N^n (2 pi sigma²)^(n_d/2) det(K_0)^−1/2
    z_p^(n_d) exp(−F_0(b_0)/sigma²−M_epsilon)
    times the product truncated-Gaussian expectation of exp(−U_epsilon).

The Haar Jacobian is already in F, once. No colour, tree-volume, z_p, sigma or determinant factor can be deleted. The critical equation cancels the **total** linear Taylor term at b_0, and the covariance cancels the total quadratic term. The remaining per-vertex Taylor series start with three fluctuation factors. Their original-data labels include every background atom, covariance atom, W endpoint, and connector. The majorant is of order sigma p³ after division by sigma², with its explicit background corrections; it is not inferred from a presumed small interacting covariance.

For Wilson sources, W_p(U0)<=N delta_V²/2 and the first derivative is O(delta_V). Therefore the increment at b_0+sigma C_0 W has a genuine linear contribution O(sqrt(u) rho delta_V p) as well as rho p². It becomes bounded by the advertised small activity only using delta_V<=c sigma p and rho p² sufficiently small. The source main vacuum remains O(u rho delta_V²), bounded by the source's C_vac expression. The non-source background action increment O(u delta_V²), the lift Wilson action, and the fixed-real-t normalizer vacuum remain in the main factor. Neither centering nor whitening deletes them.

To obtain the cluster conclusion, expand exp(−sum Phi_X), form connected hyperedge components and then expand their hard-core polymer logarithm. In each rooted-tree step, union size is bounded by the sum of incident sizes and a marked attachment chooses a vertex of its parent. The available exponent slack pays this factor. The two steps consume the beta-to-nu gap, with beta=mu+4 and nu=mu+2. At h<=1/4 their absolute tree majorants converge and give norm <=2h. Thus the convergent exponential identity establishes nonvanishing; it is not an assumption about an integrated source logarithm. The same majorants apply when a coordinate is pinned to a face, because the truncated product measure and point evaluation have norm one on the bounded analytic integrand. This is the locally rebuilt CX-R mechanism.

## 5. Complex source return, normalization, faces and edges

Cauchy estimates in epsilon give d=b_epsilon−b_0 and E=C_epsilon−C_0 with bounds 2 C_b delta_V rho/rho_0 and 2 Q_C rho/rho_0. Along b_s=b_0+s d and C_s=C_0+s E, the inverse C_s is obtained from a genuine Neumann bound. The velocity is

    v_s=C_s^−1(sigma^−1 d+E W).

Both the centre shift and the **linear** EW term enter its original-data incidence norm. The homotopy interaction also has a linear force g_s=−int Hessian_t d and a quadratic mismatch: expanding C_s^T H_s C_s−C_1^T H_1 C_1 gives all three difference terms. The H_2/H_3 estimates and complete cubic remainder yield the quoted h_bar. No stationarity at an intermediate s is assumed.

For a holomorphic density f and J_s=det(sigma C_s), differentiation gives the exact top-form identity

    partial_s[J_s f(b_s+sigma C_s W)]
       = div_W[J_s f(b_s+sigma C_s W) v_s].

The equality uses div v_s=Tr(C_s^−1 E)=partial_s log J_s. Integrating the cube gives every oriented codimension-one face, with its determinant minor and full velocity. Edges and corners have zero boundary measure for this first Stokes derivative; their changing geometry is already included in the s-dependent maps/minors. There is no additional codimension-two integral to silently drop. An exact rational-complex, noncommuting three-scalar polynomial check proves this pointwise identity and the six-face integrated identity. Removing a face, reversing one outward sign, deleting the Jacobian derivative, or deleting EW gives an exact nonzero residual.

Before division, the same pinned cluster majorant gives a normalized expectation attached to a marked velocity atom of support S. Clusters touching S contribute exp(k|S|), k=4 h_bar<=1. If the original-data mark lies in an attached cluster Y rather than S, sum its |Y| possible attachment vertices; nu−mu=2 pays the factor. The resulting marked norm is (1+k) B_v, with the source's Gaussian face density factor. This checks the remote-mark term as well as the root term. The cluster theorem and invertibility establish that every I_s is nonzero before log(I_1/I_0) is integrated. Its logarithmic branch is fixed by integrating the normalized boundary flux. It is an extensive connected potential, not a bound obtained by a global partition-function ratio.

The independent actual-density fibre uses u=17, kappa=1.1, alpha=.43, b=.07, p=1.15, epsilon=.014+.009i at 65 digits. It computes the actual six plaquettes of a changed crossing link and the normalized S^3 Haar integral of its averaged kernel. The group integral agrees with 2 I_1(t r)/(t r), where r²=1−2(1/27)(26/27)(1−cos a), to below 4e−65. This does not replace the normalizer by a pure peak.

On that fibre P=qI+i s n.sigma and

    ell(a,epsilon)=u[5(1−cos a)+(1+epsilon)(1−q cos a+s sin a)]
       +log Z0(t r(a))−t(26/27+cos(a)/27)−2 log(sin(a)/a).

The full three-colour Haar coefficient is h_2=1/(4 sqrt(2) pi²) in HS coordinates x=sqrt(2)a; the line coefficient is sqrt(2)h_2. Global radial integration verifies normalized SU(2) Haar. The Hessian at zero is u(5+q)+t f−t c_N f(1−f)+2/3, whose HS F-coordinate Haar contribution is N²/(6u). Removing the normalizer or Haar term gives nonzero residuals at the actual fibre critical point (about .00593 and .00643). Real/source-complex critical residuals are below 8e−73. The exact fixed-real-set factorization and normalized flux/log ratio agree below 2e−65. Omitting the source vacuum or canonical linear term changes the integral by 1.59e−4 and 1.60e−7, respectively. The fibre fixes spectator coordinates; it is not a full coupled critical point or integral, and its parameters do not certify the sufficient SA12 constants.

## 6. Strong event, original cut, and unresolved complement

For real A in the cube, each free link has HS norm at most sqrt(D)(C_b delta_V+sigma p M_C). The operator-norm telescoping estimates then bound a fine plaquette defect by delta_V+4 A_box, root straight-path mismatch by L A_box, and every paired path by the weaker safe 5L A_box. The strict chart, plaquette, and mismatch margins in SA30 put the whole real cube in strong G and hence the original interior cut. The cube has positive measure because C_0 is invertible and Haar has a positive chart density. This is a stronger, narrower conclusion than the uncut CB critical-point statement, whose critical point need not belong to G.

The allowed domain is nonempty: choose the finite R and analytic constants first, then rho, curvature and sufficiently large u so that sigma p³ tends to zero, delta_V<=c sigma p, and rho p² is small. If p grows, this construction generally shrinks rho. Fixed p permits a fixed positive rho with a shrinking curvature window but provides no growing cutoff tail price. The physical epsilon=−h/u fits the shrinking source discs. A fixed original source polydisc together with a growing p is not proved.

Independently, a coarse plaquette made from the root paths differs from P(V) by at most 4 eta, and its spanning fine surface has L² plaquettes. Hence G nonempty requires delta_V<=L² delta_f+4 eta. Arbitrarily small noncommuting constant SU(2) coarse fields can violate this when the thresholds are chosen too small. The geometric check includes such a witness. The old interior-only cut does not imply this all-fine-good event.

Finally the decomposition retains exactly Z_sec, the integral over G\Omega, and the integral over G^c inside the original cut. All dirty histories, hard indicators and the second complement remain. The selected-sector zero-free theorem does not give either complementary integral a fixed-V connected price, a uniform global partition ratio, or a source logarithm for the full cut integral. H24 is a pointwise gas with its original normalization and original-block supports; it is not an integrated sea estimate. A hard threshold can undergo a unit jump under an arbitrarily small coordinate perturbation, so whitening does not promote it into an analytic W activity. This observation alone is not a lower bound on an integrated complement. The full H24 interface stays open.

## 7. Primary comparison and consumed inputs

The complete SA producer and complete frozen CB producer/review are consumed. The source-return continuation and its completed bounded review are consumed, notwithstanding the continuation producer's historical pending label. The load-bearing cluster §§1–5 and its full review, H21–H27 including exact H24, and the previously read STEP55 F22/S5–S7/R6, strong-event, and source-history domains are kept at their original scopes. The entry/closure receipts record hashes and precise read ranges; partial context documents are not presented as completely read.

For primary comparison, [BFKT Part 4, arXiv:1609.01748v1](https://arxiv.org/abs/1609.01748v1), Appendix A, PDF pp.41–42, uses both output- and input-rooted field-map norms and states a finite-degree nonlinear fixed-point proposition. Its tree-length norm and d_max estimate do not themselves prove the present support-size, original-V, all-order statement; the incidence and derivative counting above rebuild the needed step.

[BFKT Part 3, arXiv:1609.01747v1](https://arxiv.org/abs/1609.01747v1), PDF p.1 and pp.12–15, concerns a three-dimensional boson model and explicitly does not complete its full small-field-error program. Its contour retains both side and outside pieces and distinguishes transpose from adjoint. No such small-error assertion is imported here: the cube top-form identity, normalized flux, actual selected real set, and retained complement are rebuilt above. The previously read Dimock hard-constraint/domain and contour comparisons likewise are not identifications with the present normalized SU(N) soft kernel. Cached PDFs/text were read by pinned version and hash; no PDF is committed. No primary source supplies an unproved Yang–Mills existence or physical-gap step.
