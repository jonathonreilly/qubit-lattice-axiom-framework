# A local resolvent estimate for the cubic product reference

New source-exposed author derivation, 2026-10-18; distinct check required. The result replaces a gap-only elimination numerator by the inverse ferromagnet acting on the actual local exchange. It holds on the entire symmetric reference subspace, including arbitrary data and passive-reference correlations. An explicit standalone supplied nearest-neighbor active-energy SWAP family has sufficient time order epsilon^(-4/3). A separate delayed-suffix full-loader corollary has eventual sufficient time order epsilon^(-2), conditional on that composition's validation. Neither is an autonomous preparation, native Hamiltonian, general active-environment, capture, reuse or permanent-halt theorem.

## 1. Exact sources and operators

All paths here are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

Completely read and hash verified for this derivation:

| Source | Bytes | SHA256 |
|---|---:|---|
| cubic_reference_gap_swap/PROPOSAL.md | 9999 | 72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee |
| local_reference_static_swap/PROPOSAL.md | 16601 | 9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70 |
| local_reference_static_swap_check/REVIEW.md | 13502 | bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b |
| active_energy_loader_interface/PROPOSAL.md | 21721 | 4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570 |

The line source/check is accepted at its stated scope; its exact projected star, effective SWAP and complete-phase contracts are reused. Its star source is product_reference_static_swap/PROPOSAL.md, SHA256 1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825, previously fully read. The grid-gap and delayed-suffix sources were pending separate checks at this author's read. Their author ancestry is exposed, not independent evidence. The grid estimate needed here is reconstructed below; the entire delayed-suffix theorem is not rechecked here and its corollary remains conditional.

Let n>=2, V={0,...,n-1}^3, N=n^3. Write L for the unweighted combinatorial graph Laplacian on this open cubic grid, and e for a corner vertex. The positive reference Hamiltonian is

 H_F=kappa sum_{ij nearest neighbors}(I-SWAP_ij), kappa>0.

Let Pi be the fully symmetric reference projector, tensored with identities on all data and passive references, and Qperp=I-Pi. The physical data qubit Q is distinct from Qperp. Set

 a=lambda/sqrt(2), b=sqrt(5)lambda/4, c=3lambda/4,
 g=sqrt(2)lambda, s=a+2b+c+g,
 H_E=omega(n_P+sum_v n_Bv),
 H_S=a X_Q+b(Z_Q+Z_P)+c Z_Q Z_P,
 Vloc=g(sigma_P^+ sigma_e^-+sigma_P^- sigma_e^+),
 W=H_S+Vloc, Hloc=H_E+sI+H_F+W.                       (1)

Here sigma^- maps |1> to |0>. All five data/exchange blocks are exactly the supplied positive blocks of the line source: a(I+X_Q), b(I+Z_Q), b(I+Z_P), c(I+Z_Q Z_P), and g(I+exchange_Pe). Add the N+1 free occupations and the grid's positive ferromagnetic blocks. In particular no inverse or effective interaction constructed below is physically installed.

The exact relations [H_E,H_F]=[H_E,W]=0, H_F Pi=0, ||W||<4lambda and ||Qperp W Pi||<=g hold on the full physical space. Pi W Pi is precisely the symmetric star compression, since Pi sigma_e^+- Pi=N^(-1)Pi sum_v sigma_v^+- Pi. W does not preserve Pi. Every estimate below pays its complementary output.

## 2. Full-space gap, kept separate from the improved numerator

Connectivity and positivity identify ker H_F with Pi: zero energy means invariance under every adjacent swap, and connected-edge swaps generate all permutations. A conservative full-space bound is

 H_F >= Delta Qperp, Delta=kappa/(3n^2).              (2)

For completeness, the elementary comparison behind (2) is as follows. For every ordered pair u,v use the axis-ordered shortest path, of length d<=3(n-1). The endpoint swap is a word of length 2d-1, with each edge used at most twice. Prefix telescoping and Cauchy–Schwarz give, on any vector,

 <I-SWAP_uv> <=(4d-2)sum_path <I-SWAP_edge>
              <=12n sum_path <I-SWAP_edge>.

The telescoping identity is U1...Um-I=sum_r U1...U(r-1)(Ur-I), so every edge difference acts on the original vector. A fixed grid edge belongs to at most n^4/2 ordered axis-paths: in its varying coordinate the two endpoint coordinates straddle its cut in at most n^2/2 ordered ways, and two remaining endpoint coordinates are free. The other coordinates are fixed by axis order. Taking half the ordered sum yields

 sum_{u<v}(I-SWAP_uv)<=3n^5 sum_edges(I-SWAP_edge).

The complete-graph spin identity gives sum_{u<v}(I-SWAP_uv)=N(N+2)I/4-S_total^2>=N Qperp, on every spin sector, not only one excitation. Combining proves (2). This proof agrees with the pending grid source; this note does not confer a distinct check on that source.

The gap will only ensure that a perturbed inverse exists. Replacing the numerator by ||C||/Delta loses information that the next calculation retains.

## 3. Explicit corner Green vector

Put d_e=e_e-N^(-1)1 in C^V, where e_e is the unit coordinate vector. Define f=L^+ d_e as the unique zero-sum solution of Lf=d_e. The inverse is only on the zero-sum space. The one-dimensional path eigenpairs are

 ell_r=2-2cos(pi r/n), r=0,...,n-1,
 u_0(j)=1/sqrt(n),
 u_r(j)=sqrt(2/n)cos[pi r(j+1/2)/n], r>=1.

These satisfy the endpoint and interior Laplacian equations and the finite cosine orthogonality relations, hence give an orthonormal basis. The three-dimensional eigenvectors are their tensor products, with eigenvalues ell_r1+ell_r2+ell_r3. For 0<=r<n,

 ell_r=4sin^2(pi r/(2n))>=4r^2/n^2,
 |u_r(j)|^2<=2/n.

The sine bound follows from sin x>=2x/pi on [0,pi/2]. Consequently

 ||f||_2^2
 =sum_{rvec !=0} |u_rvec(e)|^2/(ell_r1+ell_r2+ell_r3)^2
 <=(n/2) sum_{rvec !=0} 1/(r1^2+r2^2+r3^2)^2
 <=(n/2)sum_{m=1}^{n-1}(3m^2+3m+1)/m^4
 <=(7n/2)sum_{m=1}^{n-1}1/m^2 <=7n.                 (3)

The shell counts nonnegative integer triples with maximum coordinate m, exactly (m+1)^3-m^3<=7m^2. The final sum is <=2 by its first term plus the integral of x^(-2) from1 to infinity. The constant mode is excluded because d_e has zero sum. This is a finite-domain identity and estimate; no infinite-lattice Green function or continuum limit is substituted. The same ceiling would hold for other vertices, but only the corner is used physically.

## 4. Exact inverse on the exchange range, in every symmetric sector

For any zero-sum f define B_-(f)=sum_v f_v sigma_v^- Pi and B_+(f)=sum_v f_v sigma_v^+ Pi. Permutation invariance of Pi implies Pi B_+(f)=Pi B_-(f)=0. For each edge ij,

 (I-SWAP_ij) B_-(f)
   =(f_i-f_j)(sigma_i^- - sigma_j^-)Pi,

and the same formula holds with raising. Hence the exact intertwining equations are

 H_F B_-(f)=kappa B_-(Lf),
 H_F B_+(f)=kappa B_+(Lf).                            (4)

They do not say that the whole complement is a one-particle sector. They identify only the range generated by a single weighted raising/lowering action from the full symmetric sector.

To control that range, let |D_r> be the normalized symmetric Dicke state with r excitations. For lowering,

 <D_r|sigma_i^+sigma_i^-|D_r>=r/N,
 <D_r|sigma_i^+sigma_j^-|D_r>=r(N-r)/[N(N-1)] (i!=j).

Since sum f=0, the resulting Gram form is

 ||B_-(f)|D_r>||^2
  =[r(r-1)/(N(N-1))]||f||_2^2.                      (5)

For raising the coefficient is (N-r)(N-r-1)/[N(N-1)]. Both are in [0,1]. Distinct r values map into distinct excitation sectors for each fixed raising/lowering choice. Therefore

 ||B_-(f)||<=||f||_2, ||B_+(f)||<=||f||_2             (6)

as operators from the entire symmetric reference space, including coherent superpositions of all r and arbitrary entangled spectator coefficients. The r=1 lowering and r=N-1 raising zeroes are consistent with sum f=0; no erroneous one-magnon norm is assumed at those endpoints.

Let A=Qperp H_F Qperp as an operator on ran Qperp, tensored with the data identities, and C=Qperp W Pi. H_S contributes nothing to C. Subtracting the symmetric average in the local exchange gives

 C=g[sigma_P^+ B_-(d_e)+sigma_P^- B_+(d_e)].

Using (2),(4) and f=L^+d_e, uniqueness of the inverse on ran Qperp gives

 A^(-1)C=(g/kappa)[sigma_P^+ B_-(f)+sigma_P^- B_+(f)]. (7)

There is no inverse on Pi in this expression. For input |0>_P xi_0+|1>_P xi_1, the two terms in the square brackets output respectively P=1 and P=0. Those outputs are orthogonal, even if xi_0,xi_1 have different or correlated Dicke/data/reference components. Applying (6) to each input part proves

 ||A^(-1)C||<= (g/kappa)||f||_2
                         <=g sqrt(7n)/kappa.         (8)

Thus no factor sqrt(2) is required for the two exchange directions. The bounds hold in the induced operator norm, not only on the initial beta or an energy eigenstate. The reference free-energy factor can be restored later because it commutes with the actual Hamiltonian pieces and preserves Pi.

## 5. Perturbed inverse and complete finite-time elimination

Write W_Q=Qperp W Qperp and D=A+W_Q, both acting on ran Qperp. If 4lambda<=Delta/2, then ||A^(-1)W_Q||<1/2 and

 D^(-1)C=(I+A^(-1)W_Q)^(-1)A^(-1)C,
 eta:=||D^(-1)C||<=2g sqrt(7n)/kappa.                (9)

This is the convergent finite-dimensional Neumann inverse on the complement. It does not require A and W_Q to commute and does not replace ||A^(-1)C|| by ||A^(-1)|| ||C||. The crude gap is needed only in the first factor. D is also positive with lower bound Delta/2. Passive-reference tensor identities do not alter any inverse or norm.

For an arbitrary unit initial vector xi in Pi, put psi(t)=exp[-it(H_F+W)]xi, p=Pi psi, q=Qperp psi. The exact equations are

 i p'=Pi W Pi p+C^*q, i q'=Cp+Dq, q(0)=0,
 ||p'(t)||=||Pi W psi(t)||<=v, v=4lambda.

In q(t)=-i integral_0^t exp[-iD(t-u)] C p(u)du, integrate once by parts. Its endpoint operators are D^(-1)C (and their left unitary multiples), while the integral contains D^(-1)C p'. Consequently

 ||q(t)||<=eta(2+vt),
 ||p(t)-exp[-itPi W Pi]xi||<=g eta(2t+vt^2/2).

Adding these complete outputs gives the induced bound

 ||exp[-it(H_F+W)]Pi-exp[-itPi W Pi]Pi||
 <=eta[(2+vt)+g(2t+vt^2/2)].                         (10)

The second exponential acts on Pi. No projection of the actual output is discarded. The derivative bound depends on W, not the extensive norm of H_F. The integral is a norm bound, with no presumed temporal cancellation.

For lambda<=Delta/8 and 0<=t<=2pi/lambda, the bracket in (10) is bounded by

 2+8pi+sqrt(2)(4pi+8pi^2)<250.

For example pi<4 and sqrt(2)<3/2 already give the strict inequality. Equation(9) has eta<=2sqrt(14)lambda sqrt(n)/kappa<8lambda sqrt(n)/kappa. Therefore

 E_elim(t)<2048 lambda sqrt(n)/kappa.                 (11)

The stated constant deliberately exceeds the resulting2000. Equations(3)-(11), rather than a different guessed gap, are the new load-bearing interface.

## 6. Standalone nearest-neighbor SWAP policy

Let M=Lambda-omega>0 and 0<epsilon<=1. Define C_P=(sqrt(5)+3)/2+2sqrt(2) and choose

 n=ceil[(512pi^2/epsilon^2)^(1/3)], N=n^3,
 kappa=M/32, Delta=kappa/(3n^2),
 lambda_max=min{omega/2, M/(2C_P), Delta/8,
                            epsilon kappa/(65536 sqrt(n))},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m),
 tau=pi/lambda=2pi m/omega,
 w=epsilon/[32(omega+9lambda/4)].                    (12)

All values are fixed before evolution. Rounding gives lambda_max/2<lambda<=lambda_max because lambda_max<=omega/2. Both inverse hypotheses hold and E_elim<epsilon/32. The exact projected star residual on supplied beta=|+>^N is g/(2sqrt(N)); its effective data gate is H_eff=a(X_Q+X_P)+b(Z_Q+Z_P)+cZ_QZ_P, with norm9lambda/4 and exp(-i tau H_eff)=exp(-i pi/4)SWAP_QP. These unchanged identities are explicitly proved in the pinned line source/check.

For t in [tau-w,tau+w], t<2pi/lambda. After restoring the physical factors in their correct order, the comparator before timing approximation is

 exp(-ist)[exp(-it omega n_P)exp(-itH_eff)xi] tensor beta(t),
 beta(t)=(exp(-it omega n)|+>)^N.

The free factor on P and the effective gate need not commute. At tau the complete free evolution revives. Their combined timing error is <=(omega+9lambda/4)|t-tau|. Thus the normalized complete target

 V_t xi=exp[-i(st+pi/4)] SWAP_QP xi tensor beta(t)      (13)

obeys, uniformly on the closed window,

 ||exp(-itHloc)E_beta-V_t||
 <epsilon/32+epsilon/16+epsilon/32=epsilon/8.         (14)

Here the middle term is gt/(2sqrt(N))<sqrt(2)pi/sqrt(N)<=epsilon/16. The unhalved stabilized complete-channel error is <epsilon/4. At the center the corresponding vector ceiling is epsilon/16. All reference outputs and old-P/passive-reference correlations are retained. No success event is needed to normalize (13). No separate phase kappa|E|t is appended: H_F remains intact and has zero energy on Pi.

Geometry and cap are literal. Place P=(0,0,0), Q=(0,0,-1), and B_(i,j,k)=(-1-i,-j,-k). All interactions are nearest-neighbor or onsite, with no site collision. The corner has three grid neighbors plus P; grid maximum degree is6. Every positive ferromagnetic block has full norm2kappa. Loads satisfy

 P<=omega+C_P lambda<=omega+M/2,
 Q<C_P lambda<=M/2,
 other reference<=omega+12kappa=omega+3M/8,
 corner<=omega+6kappa+2g<omega+3M/16+M/2<Lambda.

The last bound uses sqrt(2)/C_P<1/2. These are full-support positive-block norms, not low-energy compressed norms. There are N+2 qubits and N+6+3n^2(n-1) positive blocks: N+1 free occupations, five data/exchange blocks, and 3n^2(n-1) ferromagnetic blocks.

For fixed omega,M>0, n=Theta(epsilon^(-2/3)). The two nonconstant restrictions in (12) both have order M epsilon^(4/3): Delta/8 scales as n^(-2), and epsilon kappa/sqrt(n) as epsilon n^(-1/2). Their minimum has the same order, regardless of which numerical constant is smaller. Rounding preserves it. Hence

 size=Theta(epsilon^(-2)),
 lambda=Theta(M epsilon^(4/3)),
 tau=Theta(M^(-1)epsilon^(-4/3)).                     (15)

The absolute half-width is Theta(epsilon/omega); the relative half-width is Theta((M/omega)epsilon^(7/3)). These are sufficient-family asymptotics, not uniform claims as omega or M vary, optimality, practical constants or tolerance estimates. The source's previous gap-only cubic policy remains valid; it is not overwritten.

## 7. Conditional continuously installed delayed-suffix corollary

This section is conditional on the exact delayed-suffix source4adb0 passing its separate check. It does not import that source as already accepted. Its benchmark uses the ACTUAL local apparatus, so replacing its local elimination estimate by (11) is an explicit interface substitution. Its head-tail comparison is unchanged.

Use

 n=ceil[(8192pi^2/epsilon^2)^(1/3)], N=n^3,
 kappa=M/32, Delta=kappa/(3n^2),
 Lclock=ceil max{16,(2^20/epsilon)^2}, J_budget=M/64,
 lambda_max=min{omega/2, M/(4C_P), Delta/8,
             epsilon kappa/(262144 sqrt(n)),
             4J_budget/(Lclock+1)},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m),
 alpha=lambda/2, tau=pi/lambda,
 w=min{epsilon/[128(omega+9lambda/4)],
                epsilon/(1024lambda),epsilon/(64lambda Lclock)}. (16)

Lclock is a length, not the grid Laplacian L of section3. All new constraints are simultaneous. Equation(11) gives E_elim<epsilon/128 throughout t<2tau. The star error is <epsilon/64, and the timing allowance is <=epsilon/128, so the complete local SWAP error is <epsilon/32.

The supplied head device is exactly the five late layers H_b,CZ_(b,P),H_b,X_b,all-rail X_R, with their structured positive coefficients k_r=alpha sqrt[r(Lclock+1-r)] and common diagonal C_head=4J_c, J_c=lambda(Lclock+1)/4. All four rails and matched endpoints are retained. The actual reference remains continuously installed. Replacing its line by the cubic grid preserves every prefix's commutation with H_E,H_F; prefixes act only on path/P/R and are diagonal on P. The noncommuting local interaction W still has norm<4lambda, and the gauge defect is unchanged, supported from virtual coordinate Lclock-10. Thus the separate source's exact binomial norm integral gives

 E_join<=8192/sqrt(Lclock)+8lambda w<=epsilon/64.

Its full clock endpoint comparison is <=epsilon/128. The resulting normalized physical target is exactly

 exp[-i(C_head+s)t] i^(Lclock) exp(-i pi/4)
   [external endpoint embedding of U_f xi] tensor beta(t),
 U_f=I_a X_R C_P^(b) SWAP_QP,
 C_P^(b)=|0><0|_P X_b+|1><1|_P I_b.                  (17)

There is no suffix minus and no uniform mu phase. All other physical heads are vacant in the target, R is initially blank, and a=1 is supplied with arbitrary coherent path-b/QP/passive-reference input. Under the conditional composition proof, the full window vector bound remains <7epsilon/128, complete-channel bound <7epsilon/64, and external-endpoint AND R1 probability >1-(7epsilon/128)^2. The current R1 branch is not granted exact all-time factorization: the continuously acting gauge defect is nonzero. No normalized rare-event guarantee is inferred.

The cap and geometry substitutions can be checked directly without a new physical interaction. Put the reference cube at the negative coordinates in section6, disjoint from the suffix cube {0,1,2,3}^3 and its eight upward rays. Keep Q=(0,0,-1), P=(0,0,0), R=(1,0,0). Reference interactions remain nearest-neighbor; suffix interactions retain supplied range<=9 and maximum overall degree8 at R. The whole device is not claimed nearest-neighbor. The unchanged head/contact loads plus (16) give

 P<=omega+C_P lambda+8J_c<=omega+M/4+M/8,
 Q<M/4, R<=16J_c<=M/4,
 head<=(5+sqrt(2))J_c<Lambda,
 reference noncorner<=omega+12kappa=omega+3M/8,
 reference corner<=omega+6kappa+2g<omega+3M/16+M/4.

All fit Lambda on complete supports. Total qubits are 4Lclock+N+7. The head has 8Lclock+34 blocks; adding N+6+3n^2(n-1) local blocks gives 8Lclock+N+40+3n^2(n-1). No mathematical spins used for the binomial solution are physical resources.

Now Delta/8 and epsilon kappa/(262144sqrt(n)) both scale as M epsilon^(4/3). The clock-cap restriction scales as M epsilon^2 and is eventually smaller. At fixed omega,M, rounding therefore yields

 lambda=Theta(M epsilon^2), tau=Theta(M^(-1)epsilon^(-2)),
 qubits,blocks=Theta(epsilon^(-2)).                  (18)

This is an eventual asymptotic statement; the finite minimum (16), including enormous constants, is the prescription. The window's second and third entries are asymptotically respectively of order M^(-1)epsilon^(-1) and M^(-1)epsilon, while its first is of order epsilon/omega. Thus it stays positive and has relative width of order epsilon^3 at fixed omega,M. No observation time is converted to a physical switch or release. The separate uniform-ray dwell theorem and any old processor/Record interpretation are not transferred.

## 8. Exposed origin, failed shortcuts and remaining checks

ROOT proposed the local Green-vector route, shell constant7n, Dicke Gram factor, resolvent substitution and tentative resource orders. I independently reconstructed the finite cosine spectrum, shell sum, all-excitation Gram forms, exact exchange-range intertwiner, orthogonal P-output bound, complementary Neumann inverse, complete IBP bound and the simultaneous policies. I authored the earlier line and delayed-suffix sources and share campaign ancestry with their checks. This is original source-exposed author work, not an independent validation or an originality claim relative to the broader literature.

The proof does not lift a one-magnon spectral gap by assumption; its full-space gap and special inverse range are separate arguments. It does not replace D^(-1)C by a commuting scalar denominator. It does not assert that actual evolution stays symmetric, that reference output is exactly restored, or that energy moments are controlled uniformly in the growing reference size. H_E remains active and exactly conserved by all installed terms. The initial product coherence, equal gaps, selective positive blocks, coefficient calibration and passive environment remain supplied.

A distinct check should target equations(3)-(10), especially coherent Dicke sectors, both exchange directions, inverse order and endpoint/integral constants; then verify the two policy minima and conditional full-output substitution. The separate delayed-suffix check remains necessary even if this resolvent lemma passes. No arbitrary H_PE, native reference preparation, thermal/ground certificate, tolerance theorem, capture, reuse or permanent halt has been proved.

Only this PROPOSAL.md was created. Commands read source text and recorded identities; no scientific executable, symbolic solver, numerical simulation, sweep, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model modification or publication was used. No editable prompt changed. Historical sources remain untouched.
