# Second-transfer domain complement: independent bounded review

Frozen UTC: 2026-10-30T19:20:34.296669+00:00. Source head `c056f6db54a2e1579acf85b98fb375013c0b9045`; GLOBAL_RETURN_HISTORY_ASTRA.md SHA-256 `60937c96f93a01a4cfcf7c8a8abe628d0e41b5634a5519bb12c3a6374411b336`.

**PASS for GH52–GH55 in the declared fixed-volume test family.** The lower bound concerns the actual normalized two-step posterior, including both compact kernel normalizers. It excludes the specified stronger upper-bound family. It establishes no physical running law or obstruction to alternative domain repairs.

## Independent checks

1. **RD and the pinned-tree quotient (lines 1049–1068).** RD R1 uses normalized product Haar and the full two-kernel integral. The internal rooted-tree gauge change has unit Jacobian and normalized gauge volume one. At the intermediate level, gauge fixing U_1 must be accompanied by the induced block-constant gauge transformation of U_0: K_0 is covariant because each actual path has the corresponding coarse endpoints, and its compact normalizer is invariant by Haar bi-invariance. Wilson action and original plaquette cuts are invariant. The U_1 gauge transformations are pinned at the level-two block roots, so K_1(I,U_1) is unchanged. Thus the jointly fixed two-step integral is exactly RD R1; one must not interpret the tree links being I as a positive-measure slice of unfixed full Haar. The chart/q-good event is explicitly a quotient-coordinate event. No root, harmonic, crossing or colour mode is additionally removed.

2. **An actual SU(N) witness (lines 1084–1107).** For L>=3 a block contains a plaquette with four distinct interior edges; at least one is outside its spanning tree. `exp(i t diag(1,-1,0,...,0))` is in SU(N) for every N>=2. With just that free edge nontrivial, the witness plaquette is this matrix or its inverse. Its defect is exactly `2|sin(t/2)|`, and its small principal logarithm has HS norm `sqrt(2)|t|`. At t=4delta_0, the defect exceeds 2delta_0 eventually.

   SC7 gives `K_0=(2/g)log u+O(log log u)`, with fixed g>0. Bounded positive u_1/u makes p_1/p_0 tend uniformly to one. Consequently `delta_0/r_a,1=O(K_0^-2)`, `delta_0^2/q_1=O(K_0^-4)` and `u^-1/q_1=O(p_1^-2)`. A product of translated Haar balls of radius a/sqrt(u) therefore lies inside the next product chart and q-good sector: every block has finitely many free links and Q_X is bounded by a constant times delta_0^2+u^-1. The witness defect changes by O(u^-1/2), whereas `delta_0 sqrt(u)` grows as `(log u)^(alpha_cut-2)`. Hence the whole ball remains outside D_0. Its U_0 plaquettes have defect O(u^-1/2), so the ball also lies in every fixed positive original cut, and in every shrinking cut obeying GH33, whose threshold is larger than a positive constant times p_0/sqrt(u). This does not identify the product chart with the different white-noise Omega used elsewhere.

3. **Exact normalized-kernel inequalities (lines 1109–1137).** Convexity of the actual path mean gives ||M||op<=1 and m(M)<=1. Since `1-Re Tr(V*P)/N=||V-P||HS^2/(2N)`,

       0 <= psi_M(V) <= average ||V-P_s||HS^2/(2N).

   Writing the literal kernel as `exp(-t psi_M(V))/Ntilde_t(M)`, the exact bounds are

       exp(-t psi_M(V)) <= k_t(V;M) <= C(1+t)^((N^2-1)/2).

   The lower inequality uses 0<Ntilde<=1. For the upper inequality, at any SU(N) maximizer the first tangent derivative vanishes, the geodesic second derivative is bounded by ||a||HS^2/N, and a Haar cap of radius proportional to (1+t)^(-1/2) has volume bounded below by a constant times (1+t)^(-(N^2-1)/2). This is SC27 and remains valid at singular M or nonunique maxima. No Gaussian approximation, scalar maximizer substitution or normalizer cancellation is used.

4. **Numerator, denominator and ratio.** On the chosen balls all finite path words differ from I by O(delta_0+u^-1/2), by telescoping their actual unitary factors. W_0=O(u^-1), and the two kernel exponents together are at most `C_T u delta_0^2+C_T`, uniformly for c_-<=u_1/u<=c_+. The product Haar volume is at least `c_T u^(-d_T/2)`, including all integrated real free-link coordinates. Thus the restricted joint numerator has the claimed exponential/polynomial lower bound. If n_0^K,n_1^K are the actual finite counts of kernels, SC27 and total Haar mass one give a valid denominator upper bound `C_T u^b_T`, with for example `b_T=(N^2-1)(n_0^K+n_1^K)/2`. Hence GH54 follows with `M_T=d_T/2+b_T`. These constants may depend on the fixed torus, N,L,kappa and the declared ratio bounds; no volume-uniform claim is made. Including the original cut keeps the same lower region and only decreases the denominator upper bound, so the separately normalized cut-posterior assertion also follows.

5. **The precise excluded upper bound (lines 1139–1157).** We have `u delta_0^2=Theta((log u)^(2alpha_cut-4))` and `p_0^2=Theta((log u)^(2alpha_cut))`. Since alpha_cut>5/2, log u is negligible relative to u delta_0^2. GH54 and probability<=1 imply

       0 <= -log nu_2(event)/p_0^2
         <= [C_T u delta_0^2+M_T log u-log c_T]/p_0^2 -> 0.

   An upper bound `C u^m exp(-eta p_0^2)` with fixed eta>0, C>0 and finite m would instead force the lower limit of this quotient to be at least eta. This is a direct contradiction on the stated one torus. It does not determine a sharp complement rate, a connected estimate, a different coupling regime or the success of weaker-rate/larger-domain/alternative-representation repairs.

## Read scope and limits

Complete new section: GH lines 1040–1161. Needed actual source reads/reuse: GH 164–197 and 604–620; RD 249–264; SC 49–86, 87–146 and 398–410; WR 87–105 and 249–266; BD 33–143 (needed tree/path definitions at 99–127) for the actual rooted tree and paired path endpoints. The receipt binds the exact whole-file identities and these windows. No other section is newly certified. No author route/front records, external primary literature, numerical science jobs, subworkers, source edits, Git/PR mutations or audit operations were used. Requested configuration is Astra/max; backend identity is not independently attested. Preflight returned go. Direct vocabulary lint is metadata only.

Non-free four-dimensional SU(N) continuum existence and a positive physical continuum mass gap remain open.

VERDICT: PASS
