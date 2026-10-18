# Centered static reference-gap offsets under ferromagnetic suppression

New bounded author derivation, 2026-10-18; distinct check required. For a uniform cubic ferromagnetic reference, arbitrary static real reference-only offsets with sum zero and |delta_v|<=lambda/N preserve a complete-output comparison with elimination error less than4096 lambda sqrt(n)/kappa. They need not vanish individually. A doubled weak-coupling safety factor preserves the former standalone and conditional full-loader error budgets and sufficient runtime orders. In the eventual clock-limited full family, the allowed offset scale is of order epsilon^4, versus epsilon^5 for the stated norm-Duhamel certificate. This compares sufficient bounds for a restricted structured class, not optimal tolerance or native frequency control.

The actual unequal-gap FREE Hamiltonian is generally not conserved by the installed interactions. The nominal uniform excitation-energy operator is conserved, and the total static Hamiltonian is of course conserved. These different statements are kept separate. No arbitrary H_PE, preparation, capture, cooling or permanent-halt theorem follows.

## 1. Exact source interfaces and scope of the change

All paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Complete source reads from this coherent sequence are reused unchanged:

- local_reference_static_swap/PROPOSAL.md9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70 and accepted checkbc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b: local block equations, projected star and exact effective SWAP.
- cubic_reference_gap_swap/PROPOSAL.md72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee: full-space gap Delta=kappa/(3n^2).
- cubic_reference_resolvent/PROPOSAL.md7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895: exact exchange inverse-range and corner Green norm, reconstructed in the changed argument below as needed.
- active_energy_loader_interface/PROPOSAL.md4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570: physical continuously installed delayed-suffix composition.
- active_energy_suffix_prefactor/PROPOSAL.md793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0: optional smaller head floor.
- active_energy_aged_window/PROPOSAL.mdc27d1d965d4981b8831754b947fddb6d21ac2153957696cf2f5654f33f5ad3e3: optional different aged target and endpoint window.

Those new source interfaces retain their separate review requirements. This source does not certify them by ancestry or automatically transfer a previously published theorem. The standalone proposition below uses the explicit uniform-grid hypotheses; the full-loader applications are conditional on the specified composition proofs. After the uniform argument was drafted, ROOT supplied acceptance of weighted_cubic_reference/PROPOSAL.md b2f4aaa21de3508c3d51ebf51fc6132a6ad16b8a9a836b3bc1ef9b75973294cb and its distinct check8ce18b7cdea55345c292d391154713dff1940ff037e767aff96d47a523ccbb36. That entire check was read and its hash verified here. Section8 derives an explicit simultaneous weighted/detuned corollary; acceptance of the weighted-only source does not independently validate this new combination.

Let V={0,...,n-1}^3, n>=2,N=n^3, corner e. Retain the supplied uniform positive ferromagnet

 H_F=kappa sum_grid_edges(I-SWAP_uv),
 H_E=omega(n_P+sum_v n_Bv),
 H_S=aX_Q+b(Z_Q+Z_P)+c Z_QZ_P,
 Vloc=g(sigma_P^+sigma_e^-+sigma_P^-sigma_e^+),
 W=H_S+Vloc,
 a=lambda/sqrt(2), b=sqrt(5)lambda/4,
 c=3lambda/4,g=sqrt(2)lambda,s=a+2b+c+g.

Add the reference-only diagonal perturbation

 D=sum_v delta_v n_Bv, delta_v real, sum_v delta_v=0. (1)

The actual local Hamiltonian is Hloc,delta=H_E+sI+H_F+W+D. Physically this replaces each positive reference occupation omega n_Bv by (omega+delta_v)n_Bv. It is not necessary or legitimate to install a negative positive-block coefficient delta_v n_Bv separately. All other positive blocks, P's gap omega, supplied beta=|+>^N and passive-reference premises remain unchanged.

Every term of Hloc,delta commutes with the NOMINAL H_E, since [H_E,D]=0. Thus

 exp(-itHloc,delta)=exp(-ist)exp(-itH_E)
                                 exp[-it(H_F+W+D)]             (2)

is exact. In contrast H_E,actual=H_E+D need not commute with H_F or Vloc. On an edge with unequal delta_u,delta_v, its swap fails to conserve that free energy; the corner exchange also fails when delta_e!=0. Thus this result relaxes equal reference gaps by also abandoning the earlier exact conservation claim for the actual unequal free Hamiltonian. It does not abandon conservation of the full time-independent Hamiltonian or positivity. There is no claim that this realizes an energy-conserving operation relative to every unequal free spectrum.

## 2. Generic complete-output perturbation baseline

For any finite horizon T and any nominal initial isometry E_in, ordinary Duhamel gives

 ||[exp(-itHdelta)-exp(-itHnom)]E_in||<=t||D||,
                                                    0<=t<=T.   (3)

Because the occupations commute, the spectrum of D consists of subset sums of delta_v. For zero-sum real coefficients, the largest sum of positive entries equals the magnitude of the sum of negative entries. Hence exactly

 ||D||=(1/2)sum_v|delta_v|.                           (4)

In particular |delta_v|<=d implies ||D||<=Nd/2. An additional full-vector budget b is certified by d<=2b/(NT). Complete-channel error is at most twice this vector addition. This baseline works without the ferromagnetic structure and is always available under its stated finite horizon. It is not a necessary tolerance condition, and its failure to become small does not show actual failure.

The stronger result below uses the centered and diagonal structure of D. It is not a norm-small perturbation accumulated over the entire runtime.

## 3. Exact symmetric compression and occupation inverse range

Let Pi be the fully symmetric reference projector and Qperp=I-Pi, with identities on every data/passive space. Permutation symmetry gives Pi n_Bv Pi=(1/N)Pi sum_u n_Bu Pi, so

 Pi D Pi=0.                                        (5)

Thus the compressed comparison generator Pi(W+D)Pi remains exactly Pi W Pi, the nominal symmetric star. This cancellation requires the declared zero mean; arbitrary independent offsets with uncontrolled mean are not covered by this unchanged target.

For a zero-sum coefficient vector f define B_n(f)=sum_v f_v n_Bv Pi. On a normalized symmetric Dicke state |D_r>,

 <n_i>=r/N, <n_i n_j>=r(r-1)/[N(N-1)] for i!=j.

The zero-sum Gram identity is therefore

 ||B_n(f)|D_r>||^2
 =[r(N-r)/(N(N-1))]||f||_2^2.                       (6)

Different r have orthogonal output excitation sectors, while Pi B_n(f)=0. Consequently, on the entire symmetric space including arbitrary coherent data and passive-reference coefficients,

 ||B_n(f)||<=a_N||f||_2,
 a_N=sqrt[N/(4(N-1))]<=1/sqrt(2).                   (7)

For odd N the displayed coefficient is a harmless upper bound on the maximum over integer r. With C_D=Qperp D Pi=D Pi=B_n(delta),

 ||C_D||<=c_D:=a_N||delta||_2.                       (8)

The bound concerns the offdiagonal input-to-complement map, not the extensive full norm of D.

Let L_0 be the uniform grid graph Laplacian. Directly from swapping the occupations on each edge,

 H_F B_n(f)=kappa B_n(L_0 f).                        (9)

Let A=Qperp H_F Qperp on ran Qperp. The full-spin gap Delta=kappa/(3n^2) makes A invertible there. Equations(5),(9) and uniqueness of its inverse give

 A^(-1)C_D=(1/kappa)B_n(L_0^+delta),                 (10)

where L_0^+ is the inverse only on zero-sum graph vectors. Since the graph Laplacian has smallest nonzero eigenvalue at least4/n^2, (7) gives the useful explicit bound

 ||A^(-1)C_D||<= n^2 c_D/(4kappa).                  (11)

The cruder full-gap bound ||A^(-1)C_D||<=c_D/Delta is also valid and will suffice for the simple policy below. These are different inverse statements: the full-space gap and the special occupation range are not being identified. For a weighted ferromagnet the exact identity becomes H_F B_n(f)=B_n(L_kappa f). The explicit simultaneous extension is treated separately in section8, without weakening the uniform-grid estimate here.

## 4. Elimination lemma with a possibly larger diagonal block

Put C_W=Qperp W Pi, C_tot=C_W+C_D, c_tot=g+c_D, and

 Dcomp=A+Qperp(W+D)Qperp

as an operator only on ran Qperp. We use distinct symbols D and Dcomp. Suppose

 4lambda+||D||<=Delta/2.                            (12)

Then the complementary inverse exists, and the ordered Neumann identity implies

 zeta:=||Dcomp^(-1)C_tot||
 <=2(||A^(-1)C_W||+||A^(-1)C_D||).                  (13)

It uses ||A^(-1)Qperp(W+D)Qperp||<=1/2, not commutation of the factors. The uniform corner exchange inverse interface gives ||A^(-1)C_W||<=g sqrt(7n)/kappa. One may insert either(11) or c_D/Delta for the other term.

For a normalized initial vector xi in Pi, let p=Pi exp[-it(H_F+W+D)]xi and q=Qperp exp[-it(H_F+W+D)]xi. The exact equations are

 i p'=Pi W Pi p+C_tot^*q,
 i q'=C_tot p+Dcomp q, q(0)=0.

Crucially Pi D Pi=0 and Pi D Qperp=C_D^*, so

 ||p'||=||Pi(W+D)(p+q)||<=4lambda+c_D=:v.            (14)

There is no ||D|| term in this derivative bound. The extensive norm remains in the inverse existence condition(12), where it is needed.

One integration by parts in the exact q equation, retaining Dcomp^(-1)C_tot in the endpoint and integral terms, gives

 ||q(t)||<=zeta(2+vt),
 ||p(t)-exp(-itPi W Pi)xi||
                   <=c_tot zeta(2t+vt^2/2).

Thus the complete induced error is bounded by

 E_elim,delta(t)<=zeta[2+vt+c_tot(2t+vt^2/2)].        (15)

All complementary outputs and passive-reference correlations are retained. This is a finite-dimensional full-vector argument, not a projected-survival or normalized-event statement. The comparison generator has no new scalar or data term because(5) is exactly zero.

## 5. A simple uniform offset interval that improves the Duhamel certificate

Impose the explicit centered interval

 |delta_v|<=lambda/N, sum_v delta_v=0,
 lambda<=Delta/16.                                 (16)

No individual delta_v enters the choice of lambda beyond this certified interval and mean. Equations(4),(8) give

 ||D||<=lambda/2,
 c_D<=lambda/sqrt(2N)<=lambda/2 (N>=2).

Hence4lambda+||D||<=4.5lambda<=9Delta/32<Delta/2, proving(12). Also v<=4.5lambda and c_tot<=sqrt(2)lambda+lambda/2<2lambda.

Using the crude full-gap version in(13), with N=n^3,

 ||A^(-1)C_D||<=3lambda sqrt(n)/(sqrt(2)kappa),
 ||A^(-1)C_W||<=sqrt(14)lambda sqrt(n)/kappa.

Therefore zeta<14lambda sqrt(n)/kappa, since sqrt(14)<4 and3/sqrt(2)<3. The sharper occupation identity(11) would replace3/sqrt(2) by1/(4sqrt(2)), but is not needed for the constant used below.

For0<=t<=2pi/lambda, the bracket in(15) is at most

 2+9pi+2(4pi+9pi^2)=2+17pi+18pi^2<259,

where pi<10/3 suffices. Multiplying the bounds yields

 E_elim,delta(t)<4096lambda sqrt(n)/kappa.            (17)

Indeed14*259=3626<4096. This holds uniformly over every real centered offset vector satisfying(16), on arbitrary symmetric reference input states with arbitrary data/passive references. No initial beta factorization is used until the subsequent star-to-effective-gate comparison.

The simple interval is nontrivial relative to(3). At T=2pi/lambda, the norm-Duhamel certificate for(16) is only <=pi, not an accuracy-scaled bound. Equation(17) can nevertheless be made arbitrarily small by the explicit local/reference policies. This is suppression by the symmetric ferromagnet, not a claim that the large Duhamel upper bound reflects actual dynamics.

## 6. Standalone complete-output family with actual positive occupations

Fix Lambda>omega>0, M=Lambda-omega,0<epsilon<=1 and C_P=(sqrt(5)+3)/2+2sqrt(2). Choose

 n=ceil[(512pi^2/epsilon^2)^(1/3)],N=n^3,
 kappa=M/32,Delta=kappa/(3n^2),
 lambda_max=min{omega/2,M/(2C_P),Delta/16,
                           epsilon kappa/(131072sqrt(n))},
 m=ceil[omega/(2lambda_max)],lambda=omega/(2m),
 arbitrary real delta_v satisfying(16),
 tau=pi/lambda,w=epsilon/[32(omega+9lambda/4)].        (18)

The new bound(17) is<epsilon/32. The remaining exact projected-star comparison, its residual g/(2sqrt(N)) and the effective SWAP at tau are unchanged because Pi D Pi=0. Thus on[tau-w,tau+w] the normalized complete target

 exp[-i(st+pi/4)]SWAP_QP xi tensor beta(t),
 beta(t)=(exp(-it omega n)|+>)^N                     (19)

has vector error<epsilon/8, unhalved stabilized complete-channel error<epsilon/4, and center vector ceiling epsilon/16. Here the mean nominal free revival omega tau=2pi m is retained. The physical reference has unequal free occupations, but the target beta(t) uses the common nominal omega from the exact factorization(2). It is not replaced by the free product with all individual omega+delta_v. The interaction H_F suppresses the centered offsets on the symmetric comparison space; it does not commute with their actual free Hamiltonian. There is no missing weight-dependent or detuning-dependent scalar in(19), since the symmetric D compression is zero.

Every reference occupation block remains positive: lambda<=omega/2 implies |delta_v|<=omega/(2N)<omega, so omega+delta_v>0. Also lambda<=M/(2C_P) and C_P>4 imply |delta_v|<=lambda/N<M/8. Full-support load bounds are therefore

 P<=omega+M/2, Q<M/2,
 noncorner reference<=omega+M/8+12kappa=omega+M/2,
 corner reference<omega+M/8+6kappa+M/2
                       =omega+13M/16<Lambda.

These conservatively charge every positive occupation by omega+max|delta|. Counts remain N+2 qubits and N+6+3n^2(n-1) positive blocks, with nearest-neighbor placement P=(0,0,0),Q=(0,0,-1),B_(i,j,k)=(-1-i,-j,-k). Replacing an occupation coefficient adds no block or graph edge. Maximum grid degree6 and corner degree4 remain.

At fixed omega,M>0, the two nonconstant lambda bounds in(18) both scale as M epsilon^(4/3). Rounding changes lambda by at most a factor2. Thus sizeTheta(epsilon^(-2)), timeTheta(M^(-1)epsilon^(-4/3)) are preserved, while the allowed per-site offset ceiling lambda/N is Theta(M epsilon^(10/3)). A direct perturbation allowance of order epsilon over the same horizon requires a sufficient per-site ceiling of order epsilon lambda/N=Theta(M epsilon^(13/3)); this is a comparison of the two displayed certificates only, not a necessary-noise lower bound or proof of optimal suppression.

## 7. Conditional full-loader policy and tolerance order

Keep the actual five-layer delayed suffix and the physical local reference from(1),(16). Every prefix acts only on path/P/R, so it commutes with D as well as H_F and nominal H_E. The transformed gauge defect remains G_x^*Vloc G_x-Vloc, or its original coarse bound; it gains no D term. The head-tail comparison must use the ACTUAL detuned local apparatus in its benchmark; the local benchmark state still has norm1. Thus the new local comparison can be substituted without integrating ||D|| over the whole head runtime.

For the refined head option choose

 n=ceil[(8192pi^2/epsilon^2)^(1/3)],N=n^3,
 kappa=M/32,Delta=kappa/(3n^2),
 L=ceil max{16,(8192/epsilon)^2},J_budget=M/64,
 lambda_max=min{omega/2,M/(4C_P),Delta/16,
         epsilon kappa/(524288sqrt(n)),4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)],lambda=omega/(2m),
 |delta_v|<=lambda/N, sum_v delta_v=0,
 alpha=lambda/2,tau=pi/lambda,
 w=min{epsilon/[128(omega+9lambda/4)],
                    epsilon/(1024lambda),epsilon/(64lambda L)}. (20)

Equation(17) pays epsilon/128. The star and local timing terms pay<epsilon/64 and<=epsilon/128, so the complete local error is<epsilon/32. The separate prefix/head-tail proof pays<epsilon/64, and the old endpoint clock norm pays<=epsilon/128. Conditional on the full physical suffix and smaller-prefactor interfaces, the normalized target remains

 exp[-i(C_head+s)t]i^L exp(-i pi/4)
 [external endpoint embedding of U_f xi] tensor beta(t),
 U_f=I_a X_R C_P^(b)SWAP_QP,
 C_head=lambda(L+1).                                (21)

The full vector/channel bounds remain<7epsilon/128 and<7epsilon/64, with external-endpoint AND R1 probability>1-(7epsilon/128)^2. All reference/head outputs and passive inputs are retained, with target vacancy of every nonendpoint head. No current-record all-time factorization or normalized rare-success guarantee is added. If the smaller-prefactor interface is pending, the original L=ceil max{16,(2^20/epsilon)^2} with all formulas using that L retains the baseline join proof and the same budgets.

The actual reference gaps remain positive. Their new load cost is less than M/8, while the reference corner previously had at most omega+3M/16+M/4 and noncorner sites omega+3M/8. The new ceilings are respectively omega+9M/16 and omega+M/2, both below Lambda. P,Q,R/head loads are unchanged: P<=omega+M/4+M/8, Q<M/4,R<=M/4, heads<=(5+sqrt(2))M/64. Counts remain4L+N+7 qubits and8L+N+40+3n^2(n-1) blocks. The disjoint negative reference cube and suffix/upward rays retain range<=9 and maximum degree8; only the reference part is asserted nearest-neighbor.

For fixed omega,M, the local and gap restrictions in(20) scale as M epsilon^(4/3), while the clock cap scales as M epsilon^2 and eventually dominates. Revival rounding preserves the order. Hence sizeTheta(epsilon^(-2)) and timeTheta(M^(-1)epsilon^(-2)) are unchanged. The declared offset ceiling now has order

 lambda/N=Theta(M epsilon^4).                       (22)

For comparison, using only(3) with an order-epsilon vector allowance and T of order1/lambda gives sufficient d=Theta(epsilon lambda/N)=Theta(M epsilon^5). The apparent factor1/epsilon improvement concerns this worst-case centered per-site interval and these sufficient estimates. It is not a proof that larger offsets fail, that a whole independent-entry box is tolerated, or that implementation precision has been derived from native physics.

If the separately pending aged-window interface is supported, one may instead choose continuous lambda equal to the minimum in(20), remove m, and use its three-entry window with endpoint term epsilon/(64lambda sqrt(L)). The target then contains exp(-it omega n_P)U_f inside(21), including the deterministic center-time operator exp(-i omega tau n_P), and beta(t) remains the nominal profile in(19). Prefix commutation with D and the proof(2) justify that substitution, but it remains a DIFFERENT observation contract. This optional statement is conditional on that separate proof and does not remove revival from the fixed-output theorem above.

## 8. Explicit simultaneous independent bond weights and centered gap offsets

Let each grid bond now have the exact positive form kappa_uv(I-SWAP_uv), with arbitrary fixed kappa_uv in[eta kappa_max,kappa_max], declared0<eta<=1. This changes no occupations beyond(1), and the actual reference offsets still satisfy |delta_v|<=lambda/N and sum delta_v=0. The two suppliers may be chosen adversarially together: no probabilistic independence, pointwise relation between delta_v and kappa_uv, or knowledge of individual values is used by the policy.

The checked weighted-only source supplies the exact same kernel Pi, full gap Delta_w=eta kappa_max/(3n^2), and exchange inverse-range bound

 ||A_w^(-1)C_W||<sqrt(7)lambda n/(eta kappa_max).

The detuning Gram bound(8) is a property of Pi and remains unchanged. Its crude full-gap inverse bound gives

 ||A_w^(-1)C_D||<=c_D/Delta_w
 <=3lambda sqrt(n)/(sqrt(2)eta kappa_max).

These two ranges need not be orthogonal; the triangle bound in(13) is the one used. If lambda<=Delta_w/16, then ||D||<=lambda/2 and the full complementary Neumann condition again holds. Since sqrt(n)<=n, sqrt(7)<3 and3/sqrt(2)<3,

 zeta_w<12lambda n/(eta kappa_max).

The unchanged projected derivative and offdiagonal norm bounds v<=4.5lambda and c_tot<2lambda give the same bracket<259. Therefore, uniformly over BOTH allowed assignments and all symmetric-reference inputs,

 E_elim,weighted+delta(t)<4096lambda n/(eta kappa_max),
                                    0<=t<=2pi/lambda.          (23)

The explicit product12*259=3108 is below4096. This proves the combination, rather than assuming that two separately tolerated changes can be added without a new inverse condition. The weighted occupation intertwiner noted after(11) would further sharpen constants, but is not needed for(23).

A full-loader simultaneous policy is obtained from(20) by setting kappa_max=M/32, Delta_w=eta kappa_max/(3n^2), arbitrary kappa_uv in its interval, and replacing its local minimum by

 lambda_max=min{omega/2,M/(4C_P),Delta_w/16,
         epsilon eta kappa_max/(524288n),4J_budget/(L+1)}.       (24)

Retain the same n,N,L,J_budget,m,lambda,tau,w construction, and choose the offsets after lambda is fixed subject to |delta_v|<=lambda/N and zero sum. Equation(23) pays epsilon/128, and every remaining term in the fixed-output comparison(21) is unchanged. Thus the same complete vector/channel and success bounds hold conditionally on the physical suffix interfaces. The aged option is also available only with its explicitly different target and separate endpoint-window interface. Neither version inserts an individual bond or offset into the target phase.

The actual reference occupation blocks stay positive as before. Full-support load bounds use kappa_max and |delta|, so the cap, count and placement proof in section7 transfers literally. Counts remain4L+N+7 and8L+N+40+3n^2(n-1); maximum range and degree are unchanged. Nominal H_E remains conserved, while actual unequal free H_E+D generally does not, even with these exact weighted positive bonds.

At fixed eta,omega,M>0 the new local restriction is of order eta M epsilon^(5/3), the gap restriction eta M epsilon^(4/3), and the clock restriction M epsilon^2. The clock eventually dominates. Thus full size and runtime orders epsilon^(-2), and offset ceiling order M epsilon^4, are retained. This eventual statement is not uniform as eta tends to zero. For completeness, a standalone counterpart replaces the local term in(18) by epsilon eta kappa_max/(131072n) and Delta/16 by Delta_w/16; it gives the same standalone error budgets with sufficient time order(eta M)^(-1)epsilon^(-5/3) and offset ceiling order eta M epsilon^(11/3). The stronger uniform standalone estimate in section6 remains separate.

This simultaneous weighted/detuned extension is new author work requiring a distinct check despite the accepted weighted-only dependency. It does not extend to generic bond matrices, uncentered offsets or time-dependent disorder.

## 9. Exact limits and source exposure

The permitted offsets are real, static, reference-only and centered exactly. Thus the task relaxes individual equality of reference gaps but retains their calibrated mean omega equal to P's gap. Without exact zero sum, Pi D Pi is a nonzero collective number term; it changes the comparison dynamics and may require a different target or correction. That case is not silently included. Likewise arbitrary matrix errors, fluctuating gaps, reference-reference interactions beyond the stated ferromagnet, unknown mean, added active H_PE or an initially nonsymmetric reference require new analysis.

The physical positivity/cap proof includes the actual unequal occupation coefficients. Nominal H_E conservation is an exact excitation-number statement, not conservation of actual unequal free energy. The reference product state is supplied at the initial time and is not prepared by this argument. Complete norm proximity does not control extensive energy moments or certify an autonomously reusable reference. Nothing here implements switching, an inverse phase gate, capture, reset, thermal preparation, indefinite dwell or a native processor.

ROOT proposed the centered diagonal perturbation, Dicke Gram and inverse-range route. While I developed a more general numerator/derivative estimate, ROOT suggested the particularly simple interval |delta|<=lambda/N. I independently reconstructed its exact norm, full-sector Gram, occupation intertwiner, Neumann hypotheses, integration-by-parts constants, physical block replacement and both parameter families. ROOT subsequently suggested the simultaneous weighted extension after its separate weighted-source review; I read that full report and derived the new combined bound(23) before adding section8. This is shared-lineage author research, not an independent validation or a general no-go. Distinct checking should prioritize(5)-(17), the actual-versus-nominal energy distinction, both time horizons, the cap under negative/positive offsets, and the claimed comparison with—not necessity of—the Duhamel certificate.

Only this PROPOSAL.md was created. No scientific executable, symbolic solver, simulation, sweep, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model change, historical source edit or publication occurred. No editable prompt changed.
