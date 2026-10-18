# Distinct check: cubic-reference inverse-range elimination

Disposition: **SUPPORT at the stated supplied finite-Hamiltonian scope.** I found no required mathematical correction. The full-symmetric-sector inverse identity, finite-grid Green bound, noncommuting inverse order and complete-vector integration-by-parts estimate are valid. The standalone sufficient runtime order is epsilon^(-4/3); the delayed-suffix family's eventual sufficient runtime order is epsilon^(-2), with the stated explicit minima, not an inferred practical crossover. The latter uses the separately checked delayed-suffix interface; it is not inferred from the standalone SWAP.

This is a selective source-exposed mathematical review, not a retained audit, blind replication, optimality result or native-preparation claim. In particular, neither reference symmetry during actual evolution nor exact all-time current-record correctness is asserted.

## 1. Exact inputs and coverage

Base directory N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- Completely read and reconstructed the new `cubic_reference_resolvent/PROPOSAL.md`, SHA256 `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895`.
- Completely read `cubic_reference_gap_swap/PROPOSAL.md`, SHA256 `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee`, and its distinct `cubic_reference_gap_swap_check/REVIEW.md`, SHA256 `507e83cce4949b58c8dbc0ba84339ba9af05e55fa02a11ab2da1a223c62997d7`. Reconstructed the comparison factors needed here rather than substituting the review's disposition for proof.
- Reused the previously completely read and checked, hash-refreshed `local_reference_static_swap/PROPOSAL.md`, SHA256 `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`, and my unchanged review `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b`.
- Reused the unchanged complete projected-star/effective-gate premises of `product_reference_static_swap/PROPOSAL.md`, SHA256 `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`, and my review `69c07739988970d1671e2b5acd985ec48d935d74066afc456761301e086be195`; both identities refreshed.
- Reused my immediately preceding complete check of `active_energy_loader_interface/PROPOSAL.md`, SHA256 `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`, review `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`; both hashes refreshed. Its suffix/gauge/binomial-integral proof is inherited evidence, not presented as a fresh independent check here.

ROOT exposed the Green-vector route and proposed improvement, and the author explicitly records that design exposure. I share campaign ancestry and checked the preceding line/star and suffix results, with authorship exposure to exact clock/diamond constructions. Independence here means reconstruction of the **new inverse-range argument and its substitutions**, not independence of scientific lineage. The source's historical pending flags are honest author-time status; the parent has now separately accepted the grid and suffix reviews. No source flag was edited.

## 2. Whole-space gap and finite-grid Green estimate

For adjacent-swap words of length l, prefix telescoping gives

 U1...Ul-I = sum_r U1...U_(r-1)(Ur-I).

Every difference acts on the original vector; each prefix is unitary. An endpoint transposition along a path of d edges has length 2d-1, each edge occurring at most twice. Since ||(S-I)psi||^2=2<psi,(I-S)psi>, Cauchy–Schwarz gives E_uv <=(4d-2)sum_path E_edge. For axis-ordered grid paths d<=3(n-1), the source's 12n ceiling is valid.

For an edge across the k-th cut, exactly 2(k+1)(n-k-1)n^2 ordered axis paths use it, at most n^4/2. The half factor converting the ordered endpoint sum gives H_complete <=3n^5 sum_edges(I-S). Independently expanding S_uv=2 s_u dot s_v+I/2 gives H_complete=N(N+2)I/4-S_total^2. On the complement of maximal spin N/2 its lowest eigenvalue is N, including every excitation sector. Thus H_F>=kappa/(3n^2) Qperp. Positivity and connected edge permutations also identify its kernel exactly as Pi. No one-magnon-to-many-body lifting assumption occurs.

For the open path, the cosine eigenvectors satisfy the degree-one endpoint equations as well as the degree-two interior equations. Tensor products give the cubic-grid eigenbasis. The constant mode is removed by d_e=e_e-1/N. For every nonzero index triple r,

 eigenvalue >=4|r|^2/n^2,    |u_r(e)|^2<=8/n^3.

Consequently its contribution to ||L^+d_e||^2 is at most n/(2|r|^4). Grouping by max(r_i)=m uses exactly 3m^2+3m+1 nonnegative triples, at most 7m^2 for m>=1. The sum of m^(-2) from1 to n-1 is at most2. Hence ||f||^2<=7n as claimed. This finite-volume bound is sufficient even at n=2; it does not require a continuum approximation or an infinite-volume Green function. The constant mode is excluded before inversion.

## 3. Exchange-range intertwining and Dicke normalization

Write B_-(f)=sum_i f_i sigma_i^- Pi for a zero-sum vector f. Since S_ij Pi=Pi and S_ij sigma_i^- S_ij=sigma_j^-, direct expansion yields

 (I-S_ij)B_-(f)=(f_i-f_j)(sigma_i^- -sigma_j^-)Pi.

Summing edges is exactly B_-(Lf), with no factor two. Raising obeys the same identity. Moreover Pi sigma_i^+- Pi is independent of i, so Pi B_+-=0 when sum f=0. Thus these ranges lie in the invertible complement even though they contain many reference excitation sectors.

For a normalized Dicke state with r excitations, diagonal lowering Gram entries are r/N. Off-diagonal entries are r(N-r)/(N(N-1)), from the number of configurations with the two specified sites respectively occupied and empty. Using sum_(i!=j) conjugate(f_i)f_j=-||f||^2 gives

 ||B_-(f)D_r||^2 = [r/N-r(N-r)/(N(N-1))]||f||^2
                         =r(r-1)||f||^2/[N(N-1)].

Raising replaces r by N-r. This also checks the potentially dangerous endpoints: lowering a zero-sum mode from D_1 gives zero, while lowering from D_N has norm ||f||; raising has the reversed endpoints. The coefficients are in [0,1]. Different r values map into different final excitation sectors for each fixed sign. It follows that both B operators have norm at most ||f|| on the entire symmetric space, not just on a fixed-r vector. Tensoring spectator coefficients preserves this argument and includes coherences and entanglement between Dicke sectors and data/reference systems.

Only the corner exchange contributes to C=Qperp W Pi. Its removed average is exactly d_e, hence

 C=g[sigma_P^+ B_-(d_e)+sigma_P^- B_+(d_e)].

The intertwining and uniqueness of the inverse of A=H_F restricted to Qperp establish the exact identity

 A^(-1)C=(g/kappa)[sigma_P^+ B_-(f)+sigma_P^- B_+(f)].

For an arbitrary input |0>_P xi0+|1>_P xi1, these two terms have orthogonal final P labels. Their squared norms add; the inputs need not share a Dicke index or be uncorrelated. Thus the operator norm is bounded by (g/kappa)||f||, not by the sum of two norms. This justifies the source's absence of an extra sqrt(2), and gives ||A^(-1)C||<=g sqrt(7n)/kappa. No statement about the inverse on the entire complement being small follows or is needed.

## 4. Noncommuting inverse and full-output evolution

With D=A+W_Q, the correct factorization is D=A(I+A^(-1)W_Q). It gives

 D^(-1)C=(I+A^(-1)W_Q)^(-1)A^(-1)C.

The source uses this order correctly. Since ||W_Q||<4lambda and lambda<=Delta/8, ||A^(-1)W_Q||<1/2. The Neumann factor has norm at most2, without assuming normality or commutation. Separately, self-adjointness gives D>=Delta/2. Thus eta<=2g sqrt(7n)/kappa. Passive references merely tensor identities; the finite physical inverse still exists on the specified complement.

For evolution from Pi, the exact p/q equations imply ||p'||=||Pi W psi||<=4lambda because Pi H_F=0. No extensive ||H_F|| enters. For clarity, integration by parts in q=-i integral e^(-iD(t-u)) C p(u) du gives endpoint terms

 -D^(-1)C p(t)+e^(-iDt)D^(-1)C p(0)

and an integral of e^(-iD(t-u))D^(-1)C p'(u). Commuting D^(-1) with its own exponential is legitimate; commuting it with C or W would not be. This yields ||q||<=eta(2+vt). Variation of constants in the p equation then yields ||p-p_ideal||<=||C||eta(2t+vt^2/2), with ||C||<=g. Adding orthogonal-output norms by the triangle inequality is conservative and proves the displayed complete-vector bound. The actual complementary state is charged, not projected away.

For t<=2pi/lambda the bracket is

 2+8pi+sqrt(2)(4pi+8pi^2).

Even pi<4 and sqrt(2)<3/2 give a strict bound below 2+32+(3/2)(16+128)=250. Since eta<=2sqrt(14)lambda sqrt(n)/kappa<8lambda sqrt(n)/kappa, the result is strictly below 2000lambda sqrt(n)/kappa, and hence below the stated 2048 ceiling. This constant and the strict inequalities are consistent at both t=0 and the closed upper endpoint.

## 5. Standalone policy, phase and full-support resources

Assume the inherited positive equal-gap premise omega>0 and M=Lambda-omega>0. The ceil for n gives N>=512pi^2/epsilon^2. Every entry of lambda_max is positive. For x=omega/(2lambda_max)>=1, x<=ceil x<2x implies lambda_max/2<lambda<=lambda_max. Thus both the inverse condition and

 2048lambda sqrt(n)/kappa<=epsilon/32

hold simultaneously. The closed observation window stays inside (0,2pi/lambda), since lambda w<=epsilon/[32(omega/lambda+9/4)] and lambda<=omega/2. The star residual is bounded on this whole window by sqrt(2)pi/sqrt(N)<=epsilon/16, strictly so because t<2pi/lambda. At its center that term is at most epsilon/32. Timing costs at most epsilon/32. These establish vector error <epsilon/8 on the window and <epsilon/16 at its center. The stabilized unhalved channel ceiling <epsilon/4 follows from the complete isometry norm bound, with arbitrary passive input references.

The physical factorization uses actual commutation of H_E with H_F+W. Pi commutes with H_E as well. After projected-star comparison the ordered data factor is e^(-it omega nP)e^(-it H_eff), not a single exponential of their sum. At tau both integer-gap free factors revive; at nearby times their ordered product differs by at most (omega+9lambda/4)|t-tau| from e^(-i pi/4)SWAP. The target retains beta(t) and scalar e^(-ist). There is no extra ferromagnetic scalar: H_F annihilates Pi, including the identity parts of its positive blocks.

The cap and counts use actual full-support terms. P has omega+C_P lambda, Q is below C_P lambda, the corner has omega+6kappa+2g, other grid sites at most omega+12kappa. With kappa=M/32, lambda<=M/(2C_P) and sqrt(2)/C_P<1/2 these are all below Lambda. The grid has exactly 3n^2(n-1) edges. Adding N+1 occupation blocks and five data/exchange blocks gives N+6+3n^2(n-1), on N+2 qubits. The specified negative-coordinate cube is disjoint from Q and attaches to P by a single nearest-neighbor edge; every installed standalone interaction is onsite or nearest-neighbor. Selective absence of other interactions remains a supply.

For fixed positive omega and M, n=Theta(epsilon^(-2/3)). Both Delta/8 and epsilon kappa/(65536sqrt(n)) are Theta(M epsilon^(4/3)). They eventually beat the constant entries, and rounding preserves their order. Therefore size is Theta(epsilon^(-2)), lambda is Theta(M epsilon^(4/3)), and tau is Theta(M^(-1)epsilon^(-4/3)). The absolute window is Theta(epsilon/omega), and relative width is Theta((M/omega)epsilon^(7/3)). These are sufficient-family orders, not lower bounds or uniform joint limits in omega and M.

## 6. Delayed-suffix substitution and separate resource policy

The separately checked suffix proof compares to the **actual** local Hamiltonian before the local-to-star approximation. Its reference-dependent hypotheses are symmetry of the supplied product state, prefix commutation with H_E and H_F, and ||W||<4lambda. A cubic H_F preserves all three. Its prefixes act on rails/P/R, are diagonal on P and act trivially on the reference. The head arm rotation is likewise reference independent. Therefore the exact late-supported defect and its norm bound are unchanged by the grid replacement; no volume-dependent H_F term enters the clock Duhamel estimate.

The new policy supplies N>=8192pi^2/epsilon^2 and lambda<=epsilon kappa/(262144sqrt(n)), giving elimination <epsilon/128. The star contribution is <epsilon/64 on t<2tau; local timing is <=epsilon/128. Their sum is <epsilon/32. Independently, Lclock>= (2^20/epsilon)^2 implies 8192/sqrt(Lclock)<=epsilon/128, and w<=epsilon/(1024lambda) gives 8lambda w<=epsilon/128. The clock endpoint comparison uses w<=epsilon/(64lambda Lclock), hence its lambda Lclock w/2 bound is <=epsilon/128. The total is therefore

 local <4epsilon/128, join <=2epsilon/128, clock <=epsilon/128,
 total <7epsilon/128.

This checks all changed allocations without importing the standalone error ceiling. The window also lies within (0,2tau), as ensured by its first timing entry.

The target has exactly e^(-i(C_head+s)t) i^(Lclock) e^(-i pi/4), the full Uf=I_a X_R C_P^(b) SWAP_QP, all non-output heads vacant and the actual N-qubit beta(t). The suffix signs and this phase are inherited from the checked 4adb source, not recalibrated here. Stabilized channel error is <7epsilon/64. Because this normalized target lies in the external-endpoint AND R1 event, the probability is >1-(7epsilon/128)^2. Nothing here makes the actual current R1 branch exactly correct at every time; the gauge defect remains nonzero.

The head inventory is unchanged: 8Lclock+34 blocks, 4(Lclock+1) heads and three data qubits. Adding the cubic local inventory gives 4Lclock+N+7 qubits and 8Lclock+N+40+3n^2(n-1) blocks. With J_c<=M/64 and C_P lambda<=M/4, P has load <=omega+M/4+M/8, Q<M/4, R<=M/4, heads <=(5+sqrt(2))M/64. The reference corner has load <omega+3M/16+M/4 and other sites <=omega+3M/8. All are within the full-support cap. The negative-x reference cube, Q below the suffix cube, and the eight upward rays are disjoint. Reference bonds are nearest-neighbor; the suffix remains range at most9, not an all-nearest-neighbor loader. Maximum degree8 at R is unchanged.

Here the new reference constraints scale as M epsilon^(4/3), while 4J_budget/(Lclock+1)=Theta(M epsilon^2). The latter eventually controls the minimum. Consequently lambda=Theta(M epsilon^2), tau=Theta(M^(-1)epsilon^(-2)), and both qubits and blocks are Theta(epsilon^(-2)). The three w entries have respective orders epsilon/omega, M^(-1)epsilon^(-1), M^(-1)epsilon; their minimum has order epsilon at fixed omega,M. Relative width is therefore Theta(epsilon^3). The enormous fixed clock constant may delay the asymptotic regime; the complete minimum is mandatory at finite epsilon.

## 7. Limits and work record

The new useful mechanism is an inverse bound on the actual exchange-generated range, not an improvement of the global gap. It does not assert exact invariance of the symmetric reference sector, exact reference return, uniformly controlled energy moments, coefficient tolerance, an arbitrary active P/environment interaction, an all-time record theorem, uniform-ray dwell, physical initialization, capture or reuse. Supplied product coherence, equal gaps, calibrated selective positive blocks and passive environments remain explicit assumptions.

I used analytic identities and inequalities, including endpoint Dicke-sector checks and the noncommuting inverse factorization. No scientific executable, spectral fit, symbolic/numerical solver, sweep, external search or delegation was used. File tools read complete changed arguments and verified hashes. Only this REVIEW.md was created; no candidate, canonical/W, Git, checkpoint, axiom, editable prompt, model/effort or publication/audit state changed.
