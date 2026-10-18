# Distinct check of the local ferromagnetic-reference SWAP

Disposition: SUPPORT at the stated supplied, static nearest-neighbor standalone SWAP scope. No required correction found. The full-space reference gap, exact projected star, finite-time integration-by-parts estimate, complete-output composition, simultaneous revival/error/cap choices and resource orders hold under the explicit hypotheses. This is a selective scientific check, not a retained audit or a complete path/record loader, active-environment, preparation, halting or reuse result.

Completely read and hash-verified `local_reference_static_swap/PROPOSAL.md`, SHA256 `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`. All paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`. The unchanged effective star SWAP source1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825 and my review69c07739988970d1671e2b5acd985ec48d935d74066afc456761301e086be195 are reused at their already checked scopes. That reuse is not counted as a fresh independent gate check. The NEW chain replacement and its error bounds are reconstructed below.

## 1. Full-reference gap, including all excitation sectors

An adjacent reference swap is a Hermitian unitary, so ||(I-S)psi||^2=2<psi,(I-S)psi>. A transposition S_ij at separation d has an adjacent-transposition word of length2d-1, with each intervening edge appearing no more than twice. The stated prefix telescoping identity is exact even for noncommuting factors: successive terms U1...Ur-U1...U(r-1) telescope to the product minus identity. Consequently each (Ur-I) acts directly on the original psi, not a conjugated state. Applying Cauchy-Schwarz to the vector sum and then using the factor2 above gives

    <I-S_ij> <= (2d-1) sum_word <I-U_r>
              <= (4d-2) sum_{e=i}^{j-1}<I-S_(e,e+1)>.

The two factors of2 from squared displacement cancel between the left and right energy expressions; the remaining repeated-edge factor is correctly included. Summing pairs, the load at edge e is <=4N e(N-e)<=N^3. Thus the complete-graph form is bounded above by N^3 times the path form, on every vector in the full2^N reference Hilbert space.

For spin1/2, S_ij=2s_i dot s_j+I/2. Since sum_i s_i^2=3N/4, expanding S_tot^2 verifies

    sum_{i<j}(I-S_ij)=N(N+2)I/4-S_tot^2.

The ordinary tensor-product spin decomposition has maximal spin N/2, with its unique spin multiplet of dimension N+1 equal to the fully symmetric subspace. For any lower permitted spin, the eigenvalue of the displayed operator is at least the drop from N/2 to N/2-1, which is N. This is a complete-space statement: no reference excitation number was fixed or omitted. Equivalently, the kernel of the positive swap sum is the common fixed space of all transpositions, hence precisely the symmetric space. The Casimir spectrum then supplies the lower bound N on its orthogonal complement, including multiplicities of lower spins.

Combining inequalities gives sum_path(I-S)>=N^{-2}(I-Pi) and hence H_F>=Delta Q_perp with Delta=kappa/N^2. Each adjacent term kills symmetric vectors, so H_F Pi=0; self-adjointness also gives Pi H_F=0. N=2 is already covered. This conservative lower bound need not equal the sharp chain gap, and no stronger spectral assertion is used. Tensoring arbitrary QP and passive-reference spaces preserves the inequalities.

## 2. Exact projection and the leakage lemma

For any reference permutation U, U Pi=Pi U=Pi. Conjugating the B1 raising/lowering operator to Bj and sandwiching with Pi therefore gives the same compressed operator. Averaging over j establishes the projected local exchange as (g/N) times the projected exchange sum. The star exchange sum commutes with every permutation, and H_S acts only on data, so the comparison H_S+V_star preserves Pi exactly. Hence its exponential on Pi is precisely the exponential generated there by Pi W Pi. The actual local exchange need not preserve Pi, and no such assumption is made.

For the abstract lemma put B=Pi W Pi, C=Q_perp W Pi, D=Q_perp(A+W)Q_perp. On the complementary space, D>=Delta-||W||>=d>0, so its inverse exists there with norm<=1/d. No inverse on Pi is attempted. The exact finite-dimensional block equations are

    i p'=Bp+C* q,   i q'=Cp+Dq,
    p(0)=xi, q(0)=0.

Because Pi A=0 and the full state has norm1, p'=-i Pi W psi has norm<=w. The potentially large norm of A never appears in this derivative estimate. All curves and integrals are differentiable in this finite-dimensional problem; passive references may be carried by tensor identities or the induced operator norm, without a new derivative/domain assumption.

In the exact q integral, differentiation of e^{-iD(t-v)} with respect to v is +iD e^{-iD(t-v)}. Integrating by parts yields endpoint terms with D^{-1}C p(t) and D^{-1}e^{-iDt}C p(0), with opposite signs, plus an integral containing p'. Their norms are bounded by2c_*/d and c_*wt/d. Thus (9) has the correct factors and time dependence. Inserting this estimate into projected Duhamel gives

    ||p-e^{-itB}xi|| <= c_* integral_0^t ||q(v)||dv
                       <=(c_*^2/d)(2t+wt^2/2).

Adding the complementary output norm proves (11). Orthogonality could improve the last triangle bound, but is not needed. The estimates are uniform on all normalized xi in Pi, hence bound the entire input operator and all passive-reference extensions. No spectral completeness, nondegeneracy inside Pi or infinite-dimensional gap theorem is imported.

For this installation,

    ||W||<=a+2b+c+g
       =lambda(3/sqrt(2)+sqrt(5)/2+3/4)<4lambda.

One exact simple numerical certificate is3/sqrt(2)<17/8 and sqrt(5)/2<9/8, whose sum with3/4 is4. Only V_loc contributes to C, so c_*<=sqrt(2)lambda. If lambda<=Delta/8 then d>=Delta/2. For t<=2pi/lambda, the first leakage term is <=2sqrt(2)(2+8pi)lambda/Delta; the projected term is <=(16pi+32pi^2)lambda/Delta. Their sum is <512lambda/Delta. Substitution pi<22/7 and sqrt(2)<3/2 already yields a number below448, so the advertised512 has ample strict slack. No hidden expansion remainder is required.

The optional weaker energy route is also consistent: conserved <A+W> and initially zero <A> imply <A>_t<=2||W||, giving complementary norm<=sqrt(2||W||/Delta). Its projected integration gives the stated weaker complete estimate. It is not the route used in the final parameter budget.

## 3. Actual Hamiltonian, phases and inherited effective gate

All listed blocks are positive on their complete supports. The ferromagnetic block I-SWAP has eigenvalues0,2; the local exchange plus identity has eigenvalues0,1,1,2 before scaling. The first four data blocks and all occupations have the norms stated in the source. The interaction graph is exactly Q-P-B1-...-BN, with only onsite additions, so its maximum graph degree is two and every edge is nearest-neighbor on a line.

Every term commutes with the actual HE: reference swaps preserve reference excitation number, the local exchange preserves nP+nB1, and all other P terms are diagonal while Q is degenerate. Thus the free factorization in (3) is exact for the full Hilbert space. The scalar s comes only from the four data-block shifts and local exchange shift. H_F remains the entire positive operator kappa sum(I-SWAP); its symmetric-sector ground energy is exactly zero. Appending a separate kappa(N-1) phase while retaining that zero-ground comparison would be wrong. The source does not do so.

The star residual and exact Heff SWAP are unchanged mathematical interfaces from the checked source1a9e. In particular the star residual on every QP/passive-reference vector tensored with beta has norm g/(2sqrt(N)), the full Heff spectrum is {-7lambda/4,-3lambda/4,lambda/4,9lambda/4}, and e^{-i pi Heff/lambda}=e^{-i pi/4} SWAP with the correct relative singlet sign. Their use here is legitimate because beta is in Pi and the projected star preserves Pi. Triangle comparison first from local dynamics to the exact projected star, then from the star to Heff on beta, gives (15). All reference leakage and correlations are retained in the first and second errors; no subsystem is projected away in the actual output.

Multiplication by the common exact free/scalar unitaries preserves both errors. The comparator is e^{-ist}[e^{-it omega nP}e^{-itHeff}psi] tensor beta(t). HE does not commute with Heff; the ordered data factors, freely rotated reference and scalar phase are all preserved. This reuse supplies no claim about a free active P/environment interaction beyond the literal omega nP in this model.

## 4. Simultaneous accuracy and revival prescription

All terms defining lambda_max are strictly positive under Lambda>omega>0 and epsilon>0. The integer choice m=ceil[omega/(2lambda_max)] yields m>=1 and lambda=omega/(2m)<=lambda_max. In particular lambda<=epsilon Delta/16384<=Delta/8 and512lambda/Delta<=epsilon/32. Thus the gap-elimination hypotheses and budget hold simultaneously, not at incompatible parameters.

The free revival is exact on every full energy sector at tau=2pi m/omega. With w=epsilon/[32(omega+9lambda/4)], one has w/tau<1. Therefore the closed observation interval has positive times and t<2tau=2pi/lambda, fitting the leakage lemma horizon. Its star error is strictly less than sqrt(2)pi/sqrt(N)<=epsilon/16 for N>=512pi^2/epsilon^2. The ordered free-P and effective-gate timing errors sum to <=(omega+9lambda/4)w=epsilon/32. Adding leakage gives a strict complete-vector ceiling epsilon/8 and unhalved stabilized complete-channel ceiling epsilon/4, even at the closed endpoints. At the center the star term is at most epsilon/32 and leakage at most epsilon/32, giving the claimed epsilon/16.

The actual complete target includes beta(t) and exp[-i(st+pi/4)]. Only at the center is beta(t)=beta; no size-dependent replacement by a frozen reference is silently made. Arbitrary coherent QP and passive-reference inputs are covered by the induced norm; the old P correlations move to Q in the comparison. There is no normalization by an event probability, no common computational-bit success assertion and no physical record in this construction.

## 5. Cap, inventory and asymptotics

There are N+2 qubits and (N-1)+1+4+(N+1)=2N+5 positive blocks. Full incident sums follow directly from their norms: Q has its X,Z and QP-ZZ blocks; P has its free occupation, Z, ZZ and local exchange; B1 has its free occupation, one chain bond and local exchange; other reference sites have at most two chain bonds and their free occupation. This gives exactly (19), with the stated endpoint reductions.

Under kappa=(Lambda-omega)/8 and lambda<=(Lambda-omega)/(2C_P), P's load is <=omega+(Lambda-omega)/2<Lambda. Q's smaller interaction coefficient also fits. Interior reference load is <=omega+4kappa=omega+(Lambda-omega)/2. For B1, the chain adds (Lambda-omega)/4 and the exchange adds <=sqrt(2)(Lambda-omega)/C_P<(Lambda-omega)/2 since C_P>2sqrt(2). Thus it too fits strictly. Identity shifts and free occupations are included throughout; projecting H_F to zero energy would not justify reducing these physical loads.

For fixed omega and positive cap margin, N=Theta(epsilon^{-2}), Delta=Theta((Lambda-omega)epsilon^4), and epsilon Delta/16384 eventually is the smallest lambda_max term. Since lambda_max<=omega/2, x=omega/(2lambda_max)>=1 and x<=ceil x<x+1<=2x imply lambda_max/2<lambda<=lambda_max. Rounding therefore preserves the asymptotic order. This proves lambda=Theta((Lambda-omega)epsilon^5), tau=Theta((Lambda-omega)^{-1}epsilon^{-5}), and qubit/block count Theta(epsilon^{-2}). The width w is Theta(epsilon/omega), and w/tau is Theta(((Lambda-omega)/omega)epsilon^6). These are sufficient-family asymptotics at fixed nonzero omega and margin, not uniform claims when those also vary or an optimality lower bound. Equation(16) supplies the actual finite-accuracy choices.

The growing reference size is paid without growing vertex degree, at the substantial time cost above. Exact couplings, the added positive ferromagnetic SWAP blocks, coherent product preparation and equal gaps remain supplies. H_F beta=0 neither prepares beta nor makes it a ground state of the entire free-plus-interaction Hamiltonian. Norm proximity with an N-dependent energy operator does not restore energy moments or establish reuse. The complete path/record operation, active H_PE, native realization, capture and halt remain unproved, as the source states.

## 6. Exposure and verification limits

ROOT exposed the proposed local-chain, symmetric-sector and integration-by-parts routes before the author derived this candidate. I have shared campaign ancestry, authored related gate constructions and previously checked the unchanged star SWAP. This is a source-exposed same-model distinct check of the NEW local-chain gap/comparison, parameter policy and physical inventory. It is not blind replication or a fresh independent confirmation of the unchanged star gate. All changed arguments were read and reconstructed; the pinned prior review is reused explicitly at its actual scope.

No scientific executable, symbolic solver, simulation, sweep, external literature search or delegation was used. The proof is finite-dimensional and the new gap/IBP inequalities were checked analytically above. Commands read sources, verified hashes and wrote this report. Only this REVIEW.md was created. No candidate source, W/Git/checkpoint/axiom/editable-prompt/model or publication/audit status was changed.
