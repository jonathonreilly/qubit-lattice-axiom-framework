# Distinct check: independently weighted cubic reference

**SUPPORT for the stated structured scalar-weight family.** The full-sector kernel/gap, weighted Green-energy argument, exact Dicke-sector inverse range, noncommuting resolvent and uniform complete-output policies are valid. No required correction was found. The scientific change is substantive but specific: individual ferromagnetic bond strengths need not be equal or individually known, provided every installed bond has exactly the positive matrix form kappa_e(I-SWAP_e) and its weight lies in the declared strictly positive interval. This is not arbitrary local matrix-error robustness.

## 1. Exact sources and exposure

Fully read `weighted_cubic_reference/PROPOSAL.md`, SHA256 `b2f4aaa21de3508c3d51ebf51fc6132a6ad16b8a9a836b3bc1ef9b75973294cb`, under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934` (N). Also fully read the related `local_reference_chain_weights/PROPOSAL.md`, source identity `7bae8b953e0bbb4435f9398029b42b081257b5c5b0edffc0d37ffb41152f8d5f`, as exposure rather than a premise of the new cubic inverse estimate.

The unchanged necessary interfaces were fully read and checked during the immediately preceding coherent tasks:

- Cubic full-space gap: source `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee`, distinct review `507e83cce4949b58c8dbc0ba84339ba9af05e55fa02a11ab2da1a223c62997d7`.
- Uniform cubic inverse-range/IBP interface: source `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895`, my review `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5`.
- Local line/star/effective-SWAP interface: source `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`, my review `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b`; effective-gate source `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`, review `69c07739988970d1671e2b5acd985ec48d935d74066afc456761301e086be195`.
- Physical suffix: source `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`, my review `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`.
- Refined suffix constant: source `793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0`, my review `aa56fd71a965ef3a81e1f05a73d6a58706d4439d797952e31fba92c98eddc347`.
- Distinct aged-output contract: source `c27d1d965d4981b8831754b947fddb6d21ac2153957696cf2f5654f33f5ad3e3`, my review `3bceccec2ae60b983a8aceda4af9b5555ab05bc9d092eba1c112705b4a7b6e1b`.

Their unchanged identities and scopes are reused; this is not another purported independent check of their entire proofs. ROOT exposed the weighted-energy route and candidate orders. I share campaign ancestry and prior source/check exposure. The new weighted argument is independently reconstructed below under that disclosure. Historical author-time pending flags remain unchanged; these parent interfaces have now been separately checked. No retained-audit or publication disposition is supplied here.

## 2. Full physical kernel and gap

Let c=eta kappa_max>0. Each weighted physical block is positive and has full norm2kappa_e. A vector in the zero eigenspace of their sum must be fixed by every adjacent swap, because every coefficient is positive. Connected-edge transpositions generate all permutations, so the kernel is precisely Pi, the fully symmetric reference space. Self-adjointness gives both H_F Pi=0 and Pi H_F=0. No permutation invariance of H_F outside Pi follows or is needed.

Termwise positivity gives H_F>=c sum_grid(I-SWAP). Applying the checked full-spin grid comparison yields Delta=c/(3n^2). The underlying comparison is genuinely many-body: ordered axis paths have congestion at most n^4/2, the transposition word contributes at most12n, and half the ordered sum gives H_complete<=3n^5 H_grid; H_complete=N(N+2)/4-S_total^2>=N(I-Pi), with N=n^3. Thus the weighted gap does not infer an all-spin statement from one-excitation eigenvalues.

The corner-exchange compression is a property of Pi: Pi sigma_e^+- Pi equals the average of all sites. Its exact star and zero reference energy are unchanged. Each edge also conserves the sum of its equal-gap occupations, so arbitrary allowed weights preserve actual H_E conservation. All these claims hold on complete physical supports.

## 3. Weighted Green energy and inverse norm

On the common zero-sum space Z, both L_0 and L_kappa are strictly positive, and L_kappa>=c L_0. The finite path cosine spectrum gives L_0|Z>=4/n^2. Hence B=(L_kappa|Z)^(-1) has ||B||<=n^2/(4c). This inverse has no constant-mode component.

The normalized tensor cosine eigenvectors have point weights at most8/n^3 and eigenvalues at least4|r|^2/n^2. For d=e_e-1/N, its nonconstant Fourier coefficients equal those of e_e. Therefore

 <d,L_0^+d><=(2/n) sum_(r!=0) 1/|r|^2.

The shell max r_i=m has (m+1)^3-m^3=3m^2+3m+1<=7m^2 elements, each with |r|^2>=m^2. Summing m=1,...,n-1 gives the strictly finite estimate <=14(n-1)/n<14. The normalization and dimension factors are correct; no infinite-grid estimate is substituted.

For clarity about noncommutation, set T=L_0^(-1/2)L_kappa L_0^(-1/2)>=c I on Z. Then T^(-1)<=c^(-1)I and

 B=L_0^(-1/2)T^(-1)L_0^(-1/2)<=c^(-1)L_0^(-1).

It follows that <d,Bd><14/c. For this single positive operator B, functional calculus gives B^2<=||B||B. Consequently

 ||L_kappa^+d||^2=<d,B^2d>
 <[n^2/(4c)](14/c)=(7/2)n^2/c^2.

Both uses of operator order are legitimate. In particular the proof never squares the noncommuting order B<=c^(-1)L_0^(-1), which would not generally preserve order. The loss from order n in the uniform squared Green bound to order n^2 here is real in this certificate and is properly retained. This estimate is uniform for every deterministic assignment in the interval and requires no knowledge of its eigenvectors or individual coefficients.

## 4. Exact weighted exchange range and all Dicke sectors

For zero-sum f, B_±(f)=sum_v f_v sigma_v^± Pi lies in the complement of Pi. On a single edge the exact difference is (f_u-f_v)(sigma_u^±-sigma_v^±)Pi. Multiplying each edge by its actual kappa_uv and summing yields

 H_F B_±(f)=B_±(L_kappa f).

There is no extra scalar kappa outside this formula. In particular the physical nonuniform H_F is paired with the actual weighted Laplacian, not with the uniform cosine eigenvectors used only for the bound.

For lowering on D_r, the diagonal Gram correlation is r/N and the off-diagonal correlation is r(N-r)/[N(N-1)]. The zero-sum identity sum_(i!=j)conj(f_i)f_j=-||f||^2 therefore gives r(r-1)||f||^2/[N(N-1)]. Raising replaces r by N-r. These coefficients are at most1, and each sign maps different r to different final excitation sectors. Thus ||B_±(f)||<=||f|| on all of Pi, including coherent Dicke superpositions with arbitrary spectator coefficients. The r=1 lowering zero and r=N lowering coefficient one are consistent endpoint checks.

With f=L_kappa^+d, the exact intertwiner and uniqueness on Qperp give

 A^(-1)C=g[sigma_P^+B_-(f)+sigma_P^-B_+(f)].

The two terms take opposite initial P sectors to opposite final P sectors. Their squared norms add even for correlated data/reference components, so ||A^(-1)C||<=g||f|| without an extra sqrt(2). This proves the claimed bound g sqrt(7/2)n/c. H_S has no off-diagonal reference projection, and ||C||<=g and ||W||<4lambda remain independent of the weights.

## 5. Complement resolvent and complete-vector constant

At lambda<=Delta/8, ||A^(-1)W_Q||<1/2. The correct noncommuting factorization D=A(I+A^(-1)W_Q) gives

 D^(-1)C=(I+A^(-1)W_Q)^(-1)A^(-1)C.

Thus its norm is below2g sqrt(7/2)n/c=2sqrt(7)lambda n/c. The inverse exists on the complement; no inverse on Pi is used.

For an initial vector in Pi, the exact block equations imply ||p'||<=4lambda, because Pi H_F=0. Integrating the q equation once by parts gives endpoint operators D^(-1)C and an integral containing D^(-1)C p'. Therefore ||q||<=zeta_res(2+4lambda t). Variation of constants in p adds at most g zeta_res(2t+2lambda t^2). The source's full-output sum follows without discarding leakage or bounding ||H_F|| by its extensive full norm.

On 0<=t<=2pi/lambda the bracket is 2+8pi+sqrt(2)(4pi+8pi^2)<250. Since 2sqrt(7)<6, the actual derived constant is below1500; the stated 2048 ceiling is conservative. This proves the advertised full-sector elimination bound uniformly over weights, including passive-reference extensions. Nonuniform weights do not create an additional dynamical comparison error because this argument uses their actual Hamiltonian throughout.

## 6. Standalone policy and target

For the prescribed n, N>=512pi^2/epsilon^2. The minimum gives both lambda<=Delta/8 and 2048lambda n/c<=epsilon/32. Revival rounding obeys lambda_max/2<lambda<=lambda_max since lambda_max<=omega/2. The stated w lies inside (0,2tau), supplies timing <=epsilon/32, and the star residual is strictly below sqrt(2)pi/sqrt N<=epsilon/16. Thus complete-vector error is <epsilon/8, unhalved stabilized channel error <epsilon/4, and center vector error <epsilon/16.

The fixed-output target retains e^(-i(st+pi/4)), SWAP_QP and beta(t). Here integer free revival is still imposed, not silently removed. Every reference output is retained. Because every allowed H_F annihilates Pi exactly, the target and scalar phase are independent of the individual bond weights. A separate sum-of-weights phase would be wrong; the source does not add one.

The policy uses only eta,kappa_max, not the individual values. The cap charges each edge by norm at most2kappa_max: noncorner sites have load <=omega+12kappa_max, the attached corner <=omega+6kappa_max+2g, and P/Q retain their unchanged data loads. With kappa_max=M/32 and lambda<=M/(2C_P), all fit Lambda. Counts are N+2 qubits and N+6+3n^2(n-1) blocks. The declared negative-coordinate cube, P and Q are distinct and all installed standalone bonds are nearest-neighbor.

At fixed positive eta,omega,M, n=Theta(epsilon^(-2/3)). The weak-coupling accuracy entry is Theta(eta M epsilon^(5/3)), eventually below the gap entry Theta(eta M epsilon^(4/3)) and constant entries. Rounding preserves the order. Hence the stated standalone size Theta(epsilon^(-2)) and time Theta((eta M)^(-1)epsilon^(-5/3)) follow. These are sufficient prescriptions; no optimality comparison with the uniform case is implied. When eta varies with epsilon the exact minimum must be used.

## 7. Full-loader and aged contracts

Each suffix prefix acts trivially on the energetic reference and therefore commutes with every allowed weighted H_F, as well as H_E. The defect and binomial comparison use the actual local apparatus, so no comparison to a uniform H_F or weight-variation Duhamel cost is needed. This is the correct interface for composing the weighted estimate.

With the full-loader N and accuracy minimum, the new elimination is <epsilon/128. The unchanged star and timing allowances are respectively <epsilon/64 and <=epsilon/128, giving local error <epsilon/32. The refined length and w yield join <epsilon/64; the original endpoint bound yields <=epsilon/128. Thus the stated total <7epsilon/128 and channel <7epsilon/64 close with all constraints simultaneous. The original larger length also works with its original join estimate, as claimed.

The target phase and function remain e^(-i(C_head+s)t)i^L e^(-i pi/4), U_f and beta(t), with C_head=lambda(L+1). There is no new weight-dependent scalar or residual suffix minus. The target lies in the external-endpoint AND R1 event, giving the stated probability lower bound. No exact all-time R1 correctness or normalized rare-event guarantee follows.

The inventory is 4L+N+7 qubits and 8L+N+40+3n^2(n-1) blocks. With C_P lambda<=M/4 and J_c<=M/64, P/Q/R/head and reference load ceilings match the source and stay below Lambda for every allowed weight assignment. The cubic reference remains disjoint from the fixed suffix cube/upward rays; reference interactions are nearest-neighbor, the full loader range is at most9 and maximum degree8. No new block is introduced by the weighted analysis.

At fixed eta, the new local accuracy scales as eta M epsilon^(5/3), the gap as eta M epsilon^(4/3), and the clock entry as M epsilon^2. The clock eventually controls, giving sufficient size and time orders epsilon^(-2), with time coefficient proportional to M^(-1) in that eventual regime. This is not uniform in eta; the crossover worsens for small eta.

For the optional aged contract, selecting the continuous minimum and the endpoint-width w is valid using the separately checked aged-window interface. Its target explicitly contains e^(-it omega n_P)U_f, including the center-time phase, and beta(t). None of its endpoint or ordered-factor calculations depends on individual grid weights. The same error budgets and eventual relative-width order epsilon^2 therefore transfer. This remains a different contract from fixed U_f and does not supply inverse aging or a timed correction.

## 8. Scientific value, exclusions and work record

The result removes exact equality and individual calibration of reference bond coefficients from the theorem's premises: an adversarial deterministic assignment in the common interval is allowed, with one target and policy uniform over all assignments. It does not remove certification of that interval, the positive lower bound, the exact swap matrix family, connectivity, equal free gaps, calibrated data/exchange/head coefficients, selective couplings or supplied product coherence. Arbitrary fields and generic matrix perturbations can destroy the common kernel or conservation law and are not covered. Missing edges or eta=0 invalidate the stated lower-bound certificate. This is a genuine structured supply relaxation, not a generic fabrication or native-preparation theorem.

All changed calculations were reconstructed analytically. No scientific executable, spectral simulation, symbolic solver, random-weight test, sweep, external search or delegation was used. Only this REVIEW.md was created. No frozen source, W/canonical file, Git state, checkpoint, axiom, editable prompt, model/effort or publication/audit status changed. Reference preparation, cooling, arbitrary H_PE, capture, halt and reset/reuse remain open as stated by the source.
