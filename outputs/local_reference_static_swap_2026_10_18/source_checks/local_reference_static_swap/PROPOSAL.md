# Local ferromagnetic product reference for a static active-energy SWAP

New bounded author derivation requiring a distinct check. A nearest-neighbor reference chain and a single P-reference exchange replace the reference star of the product-reference SWAP. All installed blocks are static, real, positive, and at most two-body. A proved finite-chain gap and elementary projected-dynamics estimate control all leakage and reference outputs. The price is a much weaker interaction and longer operation time as accuracy improves. The supplied product coherence, exact coefficients and gaps, passive environment, freely degenerate Q, and finite observation window remain premises. This is a standalone Q/P SWAP, not the complete path/record loader, preparation, capture, or permanent halt.

## 1. Source and actual local Hamiltonian

Completely read and hash verified `product_reference_static_swap/PROPOSAL.md`, 9995 bytes, SHA256 `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`. Its author is ROOT and its distinct check is not a premise of this note. The effective two-qubit gate and residual used below are reconstructed explicitly. Its checked standalone-rotation ancestor motivates the comparison but supplies no local-chain elimination theorem.

All paths are under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Fix N>=2, omega>0, lambda>0 and kappa>0. Put

 a=lambda/sqrt(2), b=sqrt(5)lambda/4, c=3lambda/4,
 g=sqrt(2)lambda,
 H_E=omega(n_P+sum_(j=1)^N n_Bj),
 H_S=a X_Q+b(Z_Q+Z_P)+c Z_Q Z_P,
 V_loc=g(sigma_P^+ sigma_B1^-+sigma_P^- sigma_B1^+),
 H_F=kappa sum_(j=1)^(N-1)(I-SWAP_(Bj,B(j+1))),
 s=a+2b+c+g.
                                                               (1)

The actual positive blocks are

 a(I+X_Q), b(I+Z_Q), b(I+Z_P), c(I+Z_Q Z_P),
 g(I+exchange_(P,B1)),
 kappa(I-SWAP_(Bj,B(j+1))) for j=1,...,N-1,
 omega n_P, omega n_Bj for j=1,...,N.

Each ferromagnetic block has eigenvalues0 and2kappa and norm2kappa on its complete two-qubit support. The exchange-plus-identity block has eigenvalues0,g,g,2g. All blocks are real and positive; no low-energy positivity substitution is made. The full Hamiltonian is

 H=H_E+s I+H_F+W,  W=H_S+V_loc.                        (2)

The physical graph lies on the line Q-P-B1-...-BN. Onsite terms do not add spatial edges; QP carries the ZZ interaction, P B1 the exchange, and successive reference qubits the ferromagnet. The maximum graph degree is two. There is no central reference star, copied data qubit, many-body constraint block, or interaction switching.

Each term in H_F and W commutes with H_E on the full Hilbert space. In particular the reference swap conserves the equal-gap reference energy. Thus

 exp(-itH)=exp(-ist)exp(-itH_E)exp[-it(H_F+W)].          (3)

The identity contributions inside H_F are NOT subtracted from the physical Hamiltonian or incident loads. H_F is kept intact in the last exponential. Its ground energy is exactly zero; it is not appropriate to append an additional free phase kappa(N-1)t to the effective comparison while dropping the compensating swap terms.

Supply beta=|+>^tensor N independently of arbitrary QP/passive-reference input. This is a product of coherent equal-gap states, not a ground-state preparation theorem. Let Pi be the fully symmetric reference projector, tensored with identity on QP and passive references; let Q_perp=I-Pi. In the rest of this note Q_perp is a projector, distinct from the physical data qubit Q.

## 2. Explicit full-reference gap

Write S_ij for the reference-qubit transposition and E_j=I-S_(j,j+1). Both are represented on the complete 2^N reference space. For i<j, d=j-i, express S_ij as the adjacent word of length L=2d-1, going from i to j and back except for the last endpoint. Every edge in [i,j-1] appears at most twice.

For any product U_1...U_L of these unitaries,

 (U_1...U_L-I)psi=sum_(r=1)^L U_1...U_(r-1)(U_r-I)psi.

The prefixes are unitary. Triangle/Cauchy and ||(I-S)psi||^2=2<psi,(I-S)psi> therefore imply

 <I-S_ij>_psi <=(4d-2) sum_(e=i)^(j-1)<E_e>_psi.       (4)

No transformed-state energy is inserted in the right side: the telescoping identity uses each (U_r-I) directly on psi. Summing pairs, the coefficient at an edge e is at most

 4N * #{(i,j):i<=e<j}=4N e(N-e)<=N^3.

Hence, as a quadratic-form operator inequality on the full reference space,

 sum_(i<j)(I-S_ij) <= N^3 sum_e E_e.                   (5)

For spin-1/2 define total spin S_tot=sum_j (X_j,Y_j,Z_j)/2. The identity S_ij=2 s_i dot s_j+I/2 gives

 sum_(i<j)(I-S_ij)=N(N+2)I/4-S_tot^2.                 (6)

Adding spin-1/2 representations gives total-spin labels S=N/2,N/2-1,...; the maximal-spin multiplet is precisely the fully symmetric subspace. Its S_tot^2 eigenvalue is N(N+2)/4. The next possible label, N/2-1, lowers S(S+1) by N, and every lower label gives a larger difference. Therefore (6)>=N(I-Pi). Equivalently this also identifies the zero subspace as the common fixed space of every permutation. Equations(5),(6) prove

 H_F >= Delta Q_perp,  Delta=kappa/N^2.               (7)

H_F Pi=0 and [H_F,Pi]=0 exactly. This is a deliberately conservative finite-N full-space gap lower bound; it is not an assertion that kappa/N^2 is the exact gap. It holds after tensoring arbitrary data and passive-reference spaces. N=1 has no complementary reference sector and is not needed in the accuracy family.

## 3. Exact projected star and a self-contained elimination bound

Permutation symmetry implies, for either single-site raising or lowering operator,

 Pi sigma_B1^+- Pi = (1/N)Pi sum_j sigma_Bj^+- Pi,

where the superscript '+-' means either choice separately, not a product. Thus

 Pi W Pi = Pi[H_S+V_star]Pi,
 V_star=(g/N)sum_j exchange_(P,Bj).                    (8)

The operator H_S+V_star preserves the symmetric reference subspace. Equation(8) is exact on all of that subspace, not only on beta. It does not assume the actual local-exchange dynamics preserves Pi; the next bound pays its leakage.

Here is an elementary finite-dimensional lemma with no imported perturbation theorem. Suppose A>=Delta Q_perp, A Pi=0, A is self-adjoint, and W is self-adjoint with ||W||<=w. Let C=Q_perp W Pi, ||C||<=c_*, and D=Q_perp(A+W)Q_perp on the complementary space. If d=Delta-w>0, then D>=d I and ||D^-1||<=1/d. For normalized initial xi in Pi, write

 psi(t)=exp[-it(A+W)]xi, p(t)=Pi psi(t), q(t)=Q_perp psi(t).

The block equations give q(0)=0 and

 q(t)=-i integral_0^t exp[-iD(t-v)] C p(v)dv,
 ||p'(v)||=||Pi W psi(v)||<=w.

Integrating this exact vector integral once by parts, using D^-1, bounds its two endpoint terms by2c_*/d and its integral term by c_* w t/d. Thus for t>=0,

 ||q(t)|| <= (c_*/d)(2+wt).                           (9)

The projected equation is i p'=Pi W Pi p+C^* q. Its own Duhamel formula gives

 ||p(t)-exp(-it Pi W Pi)xi||
                <=(c_*^2/d)(2t+wt^2/2).             (10)

Combining orthogonal sectors by the triangle inequality gives the complete vector/operator bound

 ||exp[-it(A+W)]Pi-exp(-it Pi W Pi)Pi||
 <= (c_*/d)(2+wt)+(c_*^2/d)(2t+wt^2/2).              (11)

All estimates apply to any vector in Pi and hence to the induced operator norm and arbitrary passive references. The exponent on the second term is understood on Pi. The proof uses neither a small global dimension nor an upper bound on ||A||, and it retains all complementary-sector output. Degeneracy within Pi is allowed.

For (1), ||W||<=a+2b+c+g<4lambda. Since H_S preserves Pi, only the local exchange contributes C, so ||C||<=g=sqrt(2)lambda. If lambda<=Delta/8, then d>=Delta/2. For every 0<=t<=2pi/lambda, (11) is at most

 [2sqrt(2)(2+8pi)+16pi+32pi^2] lambda/Delta
                          <512 lambda/Delta.         (12)

The strict numerical inequality follows already from pi<22/7 and sqrt(2)<3/2. No series expansion in lambda or unspecified remainder is used.

A looser route also works: conservation of A+W and initial A-energy zero imply <A>_t<=2||W||, hence ||q(t)||<=sqrt(2||W||/Delta); projected Duhamel then gives complete error <=(1+t||W||)sqrt(2||W||/Delta). This would require a smaller lambda. Equation(11) is the stronger bound actually used. Neither route claims that the actual dynamics stays exactly in the symmetric reference sector.

## 4. Reconstructed projected SWAP and complete output

For beta=|+>^N, the exact star residual satisfies

 (V_star-(g/2)X_P)(psi tensor beta)
    =(g/(2N))Y_P psi tensor sum_j Y_Bj beta,
 ||(V_star-(g/2)X_P)E_beta||=g/(2sqrt(N)).              (13)

The N single-site deviations are orthogonal and Y_P is unitary, including arbitrary QP/passive references. On the comparison trajectory the reference remains beta, so Duhamel applies without assuming factorization of the actual projected star state.

Since g/2=a, the comparison data operator is

 H_eff=a(X_Q+X_P)+b(Z_Q+Z_P)+c Z_Q Z_P.

Its singlet eigenvalue is -3lambda/4. On the triplet, (H_eff+c I)/lambda has diagonal entries (3+sqrt(5))/2,0,(3-sqrt(5))/2 and its two successive offdiagonals are1. Trace3, principal-minor sum -1 and determinant -3 give characteristic polynomial (x-3)(x-1)(x+1). Thus its triplet energies are lambda times {-7/4,1/4,9/4}, and ||H_eff||=9lambda/4. At tau=pi/lambda,

 exp(-i tau H_eff)=exp(-i pi/4)SWAP_QP.               (14)

This is the full coherent two-qubit identity; no basis-state-only transfer or missing singlet phase is used.

Combining (8),(11),(13) and then the common exact factors (3), for all 0<=t<=2pi/lambda and lambda<=Delta/8,

 ||exp(-itH)E_beta-A_t||
       <=512lambda/Delta+gt/(2sqrt(N)),
 A_t psi=exp(-ist)[exp(-it omega n_P)exp(-itH_eff)psi]
                                     tensor beta(t),
 beta(t)=(exp(-it omega n)|+>)^tensor N.               (15)

Every reference qubit is retained. Both the actual local-chain leakage and its entanglement with data are included in the full vector norm. H_E commutes with the actual H_F+W; it does not commute with H_eff, so the displayed data-factor order is essential. The finite-chain H_F ground energy zero accounts for its identities without inventing an extra scalar phase.

## 5. Explicit simultaneous nearest-neighbor family

For any fixed Lambda>omega>0 and 0<epsilon<=1 choose

 N=ceil(512pi^2/epsilon^2),
 kappa=(Lambda-omega)/8,
 Delta=kappa/N^2,
 C_P=(sqrt(5)+3)/2+2sqrt(2),
 lambda_max=min{omega/2, (Lambda-omega)/(2 C_P),
                             epsilon Delta/16384},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m),
 tau=pi/lambda=2pi m/omega,
 w=epsilon/[32(omega+9lambda/4)].                     (16)

All parameters are fixed before evolution. In particular lambda<=lambda_max, m>=1, lambda<=Delta/8, and512lambda/Delta<=epsilon/32. The entire free evolution is identity at tau, on every energy sector, not only on the reference symmetric sector. For the positive-width closed interval I=[tau-w,tau+w], w<tau and t<2tau, so (15) applies. Use the normalized complete target

 B_t psi=exp[-i(st+pi/4)]SWAP_QP psi tensor beta(t).    (17)

At t=tau the reference equals beta. At other window times the actual free reference profile beta(t) is explicitly retained. The physical free P factor differs from identity by at most omega|t-tau|, and the effective data evolution differs from (14) by at most (9lambda/4)|t-tau|. Therefore

 ||exp(-itH)E_beta-B_t||
 <=512lambda/Delta+gt/(2sqrt(N))
                         +(omega+9lambda/4)|t-tau|
 <epsilon/32+epsilon/16+epsilon/32=epsilon/8.          (18)

The first allowance can be non-strict; the star allowance is strict since t<2tau. The unhalved stabilized complete-output channel distance is <epsilon/4, including arbitrary passive references. At tau a separate tighter ceiling is epsilon/16. No output is projected away or normalized conditionally. This is a SWAP of arbitrary QP inputs with the old P/passive-reference correlations retained on Q/reference. It is not an input-independent computational-bit success assertion.

This construction has no head or record qubit. There is no inherited current-record correctness, automatic stopping or finite-chain receiving-gadget theorem. Exact finite-dimensional recurrence and later deviation remain compatible with (18).

## 6. Full-support cap, geometry, count and time cost

The N-1 chain blocks replace N-1 of the old star blocks; the one local exchange remains. There are N+2 physical qubits and exactly

 (N-1)+1+4+(N+1)=2N+5

positive blocks. All are nearest-neighbor or onsite on the stated line. Full-support incident sums are

 load(Q)=lambda[sqrt(2)+(sqrt(5)+3)/2],
 load(P)=omega+C_P lambda,
 load(B1)=omega+2kappa+2g,
 load(Bj)<=omega+4kappa for j>=2.
                                                               (19)

At the far endpoint the last bound can be reduced to omega+2kappa; for N=2 both reference sites have only one chain neighbor. These are full-support block-norm sums, not projected energies or probabilities. Under (16), P has load at most omega+(Lambda-omega)/2<Lambda. The Q interaction coefficient is smaller than C_P, so its load is also <Lambda. Every interior reference load is omega+(Lambda-omega)/2<Lambda. Finally B1 has chain contribution (Lambda-omega)/4 and exchange contribution2sqrt(2)lambda<=sqrt(2)(Lambda-omega)/C_P<(Lambda-omega)/2, so it too is below Lambda. All physical identity terms are included.

At fixed omega and positive cap margin Lambda-omega, the specified minimal N is Theta(epsilon^-2), Delta=Theta((Lambda-omega)epsilon^4), and the final term of lambda_max dominates asymptotically. Rounding m changes lambda by at most a factor2 because lambda_max<=omega/2. Consequently this sufficient family obeys

 lambda=Theta((Lambda-omega)epsilon^5),
 tau=Theta((Lambda-omega)^-1 epsilon^-5),
 qubits, blocks=Theta(epsilon^-2).                    (20)

Constants are deliberately enormous. This is a sufficient prescription, not an optimality, practicality or fabrication-precision statement. For nonasymptotic choices use (16), which retains the omega and cap constraints. The absolute half-width w is Theta(epsilon/omega) at fixed omega in this family; its relative width w/tau shrinks as Theta(((Lambda-omega)/omega)epsilon^6). Localization removes the growing degree while sacrificing the fixed-lambda time of the star family. It does not make a fixed-relative-width halt window.

The reference free-energy mean is N omega/2 and maximum N omega. H_F beta=0 exactly, but no cooling or preparation mechanism is supplied by this fact. The actual reference compensates input-dependent data-energy changes through its deviations and correlations. Complete norm proximity does not certify restoration of all energy moments, and no repeated reuse is proved.

## 7. Exposure, open premises and work record

ROOT suggested the ferromagnetic-chain replacement, symmetric-sector projected star and a complete-graph comparison route for the gap. I reconstructed the adjacent-word quadratic-form comparison, total-spin gap and all physical resources. I first derived the looser conservation-of-energy leakage bound recorded after(12). ROOT then supplied the integration-by-parts route; I independently derived its block equations, derivative bound, endpoints, integrated projected error, and explicit constant<512 before using it. This is exposed author research, not an independent validation of ROOT's proposal or a novelty claim. The exact star-gate source was fully read and its gate/residual used here were reconstructed; its historical pending distinct status is not silently replaced by acceptance.

The equal physical gaps, exact positive blocks, product coherent reference, isolation from undeclared interactions, and freely degenerate Q/passive environment remain suppliers. An arbitrary active H_PE, autonomous reference preparation, complete path/record loader composition, capture and reset remain open. No microscopic native Hamiltonian or new primitive beyond the explicitly supplied positive two-body class is derived. The ferromagnetic SWAP blocks are explicitly added supplied interactions; they are not inferred from the earlier star apparatus.

A distinct check is required for the full-space gap comparison, projected leakage lemma, complete-phase composition, rounding/cap policy and time order. No retained status is assigned. Only this PROPOSAL.md was created. Work was analytical with complete reads and Python3 pathlib/hashlib source identity bookkeeping; no scientific executable, matrix solver, simulation, sweep, external search, delegation, source overwrite, Git/W/checkpoint/axiom/editable-prompt/model change or publication occurred. No editable prompt changed.
