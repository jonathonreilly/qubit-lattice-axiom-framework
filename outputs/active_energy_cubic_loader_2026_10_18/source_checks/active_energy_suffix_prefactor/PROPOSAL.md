> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# A smaller sufficient head clock for the continuously installed active-energy suffix

New bounded author calculation, requiring a distinct check. The actual suffix and supplied interaction class are unchanged. Its gauge defect comes only from the local P-reference exchange, and a different exponential Markov parameter improves the explicit prearrival overlap bound from8192/sqrt(L) to64/sqrt(L). The sufficient head-length prescription becomes ceil max{16,(8192/epsilon)^2}. Complete-output allowances, exact phases and all local cap constraints remain explicit; no native preparation, arbitrary H_PE, autonomous release, capture or permanent halt is inferred.

## 1. Scope, exact sources and exposed status

All paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The changed argument uses active_energy_loader_interface/PROPOSAL.md, 21721 bytes, SHA256 4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570. Its complete source was read during the immediately preceding resolvent task and the exact prefix, Hamiltonian, tail and policy sections were refreshed here. Its baseline composition is not independently revalidated by this author, who authored it. The conditional application below requires its separate check at the full physical scope.

The unchanged local SWAP source9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70 and checkbc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b were fully read in that task and are reused at their accepted scope. The new cubic-reference option uses cubic_reference_resolvent/PROPOSAL.md, 20825 bytes, SHA256 7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895, just authored and fully read back; that option remains provisional until its distinct check. Its grid source is cubic_reference_gap_swap/PROPOSAL.md72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee. No pending claim is promoted by composition here.

ROOT proposed the sharper defect, Markov parameter and constants after the resolvent source was frozen. I reconstruct them below. They are not independent evidence. Only this file is created, and all historical sources remain untouched.

## 2. Every prefix commutes with the data Hamiltonian

Keep the actual continuously installed local apparatus

 Hloc=H_E+sI+H_F+H_S+Vloc,
 H_E=omega(n_P+sum_v n_Bv),
 H_S=aX_Q+b(Z_Q+Z_P)+c Z_QZ_P,
 Vloc=g exchange_(P,e),
 a=lambda/sqrt(2), b=sqrt(5)lambda/4,
 c=3lambda/4, g=sqrt(2)lambda, s=a+2b+c+g.

H_F is either the supplied positive line ferromagnet or the explicitly specified cubic one. Its reference qubits are disjoint from the suffix. Q,R are freely degenerate; P and every reference qubit have gap omega. No free data term has been removed or replaced by an interaction-picture assumption.

Let H denote the Hadamard on the physical path-b rail, X its permutation, and D=CZ_(b,P). The chronological suffix is H,D,H,X,all-rail X_R. Its two diamond layers each contribute a minus. Write the ordered exact gauge prefix G_x in the virtual coordinates of the baseline, with suffix positions L-14,...,L-1 and external endpoint L. Identity and global minus signs act on the whole relevant rail/data fiber. The full table is

| Virtual coordinate | G_x |
|---|---|
| x<=L-14 | I |
| L-13, L-12, L-11 | H |
| L-10, L-9, L-8 | -D H |
| L-7, L-6 | -H D H |
| L-5, L-4, L-3 | -X H D H |
| L-2, L-1, L | X_R X H D H |

Coordinates L-11/L-10 are the first diamond's B/C variables after the fixed physical arm rotation; L-3/L-2 are the second diamond's B/C variables. The plus-to-minus scalar gauge enters at each C, not earlier. The table includes both internal arm variables and all interlayer cable endpoints, not only whole-gate boundaries. The identity diamond rails are included in D. The auxiliary a-path label is unchanged.

Each factor in this table commutes with X_Q, Z_Q, Z_P and Z_QZ_P: H,X act only on the path, D is diagonal on P and disjoint from Q, and X_R is disjoint from Q/P. Therefore

 [G_x,H_S]=0 for every x.                            (1)

This holds even though the prefixes need not commute with one another. They also commute with H_E,H_F and sI. The physical arm rotation A acts only on heads and commutes with the whole local apparatus. Before x=L-10, G_x is I or H and also commutes with Vloc. At the right endpoint

 G_L=X_R X H D H=X_R C_P^(b),
 C_P^(b)=|0><0|_P X_b+|1><1|_P I_b.

Thus the full target word remains +X_R C_P^(b) SWAP_QP, with no residual diamond minus.

In the exact transformed Hamiltonian the difference from the benchmark h_L+Hloc is

 E=sum_x |x><x| tensor E_x,
 E_x=G_x^*Vloc G_x-Vloc,
 E_x=0 for x<L-10, ||E_x||<=2g.                     (2)

The exchange has full norm g, so this is a complete-fiber norm, valid on both P sectors, all reference states, path coherences and passive references. No small-leakage or reference-product approximation was used in (2). Its expression in a gauge is not an additional installed interaction or a claim that Vloc is switched off.

## 3. Exact binomial tail and an elementary integral bound

Use the same engineered scalar clock

 alpha=lambda/2, k_r=alpha sqrt[r(L+1-r)],
 J_c=lambda(L+1)/4, C_head=4J_c,
 h_L=C_head I-sum_(r=1)^L k_r(|r><r-1|+h.c.).

The exact endpoint evolution is

 f_x(t)=exp(-i C_head t)sqrt(binomial(L,x))
             [i sin(alpha t)]^x[cos(alpha t)]^(L-x),
 tau=pi/lambda.

All four rails have identical coefficients and boundaries. The benchmark h_L+Hloc factorizes into this scalar state and the actual local apparatus, not its projected star. For arbitrary complete initial logical/reference state, Duhamel and (2) give the induced bound

 E_join(t)<=2g integral_0^t sqrt(p_tail(v))dv,
 p_tail(v)=sum_(x=L-10)^L |f_x(v)|^2.                 (3)

This is an integral of norms. Actual joint dynamics need not factorize. The initial gauge is identity at x=0 because L>=16.

For 0<=v<=tau, let theta=alpha v and Y=L-X, where X is binomial with parameters L,sin^2(theta). Then Y is binomial with parameters L,cos^2(theta), and the support in (2) is exactly Y<=10. For z=1/11, Markov applied to exp(-zY) yields

 p_tail(v)<=exp(10/11)
  [1-(1-exp(-1/11))cos^2(theta)]^L.

The elementary inequality exp(1/11)>=1+1/11=12/11 proves 1-exp(-1/11)>=1/12. Using 1-y<=exp(-y), then taking a square root,

 sqrt(p_tail(v))<=exp(5/11) exp[-L cos^2(theta)/24].  (4)

This upper bound may exceed1 near tau; that causes no problem in the integral. For theta in[0,pi/2], cos(theta)>=2(pi/2-theta)/pi. Substitution y=pi/2-theta and extension of the positive Gaussian integral to infinity give

 integral_0^tau sqrt(p_tail(v))dv
 <= (2/lambda)exp(5/11) integral_0^infinity
                              exp[-Ly^2/(6pi^2)]dy
 =exp(5/11)pi sqrt(6pi)/(lambda sqrt(L)).             (5)

Multiplying by 2g=2sqrt(2)lambda gives coefficient

 C=2sqrt(2)exp(5/11)pi sqrt(6pi)<440/7<64.            (6)

For a purely explicit verification: sqrt(2)<10/7, pi<22/7 and sqrt(6pi)<35/8. Also log(8/5)>=2[(8/5)-1]/[(8/5)+1]=6/13>5/11, so exp(5/11)<8/5. The logarithm inequality follows by differentiating log x-2(x-1)/(x+1), whose derivative is (x-1)^2/[x(x+1)^2]>=0 and whose value at1 is0. These four upper bounds multiply to440/7.

For t<=tau the integral is at most its value at tau. For tau<t<=tau+w, use p_tail<=1 on the remaining interval. Thus uniformly over the full horizon

 E_join(t)<64/sqrt(L)+2sqrt(2)lambda w,
                                    0<=t<=tau+w.    (7)

The result did not assert monotonicity beyond tau, a spectral approximation to the binomial law or a cancellation between oscillating matrix amplitudes.

## 4. New head policy and unchanged complete-output budget

For 0<epsilon<=1 set

 L=L_new=ceil max{16,(8192/epsilon)^2},
 J_budget=(Lambda-omega)/64,
 w=min{epsilon/[128(omega+9lambda/4)],
                epsilon/(1024lambda),epsilon/(64lambda L)}.     (8)

Require lambda<=4J_budget/(L+1) as before; all other local-apparatus restrictions remain imposed. Equation(7) then gives

 E_join < epsilon/128+(sqrt(2)/512)epsilon
         <epsilon/64.                               (9)

The first equality allowance uses 64/8192=1/128; the second is strictly smaller than epsilon/128. Nothing requires dropping the already present w restriction or spending any local error budget.

The exact endpoint phase remains f(tau)=exp(-i C_head tau)i^L |L>. The shifted clock norm is ||h_L-C_head I||=lambda L/2, hence

 ||f(t)-exp(-i C_head t)i^L|L>||
 <=(lambda L/2)|t-tau|<=epsilon/128.                 (10)

Suppose the chosen local policy guarantees the existing complete SWAP bound E_loc<epsilon/32 throughout the same window. Under the baseline's exact physical gauge/cap premises, (9),(10) give precisely the same complete normalized target

 V_t xi=exp[-i(C_head+s)t] i^L exp(-i pi/4)
 [external endpoint embedding of U_f xi] tensor beta(t),
 U_f=I_a X_R C_P^(b)SWAP_QP,
 beta(t)=(exp(-it omega n)|+>)^N.                     (11)

The input supplies one head with a=1 and arbitrary coherent b/QP/passive-reference input, R=0, beta, and all other heads vacant. The target retains all data, reference and head outputs; every other head is vacant. Uniformly on [tau-w,tau+w],

 ||exp(-itH_tot)E_in-V_t||<7epsilon/128,
 complete unhalved stabilized channel error<7epsilon/64,
 Pr(external endpoint AND R1)>1-(7epsilon/128)^2.     (12)

These are conditional applications of the baseline physical composition, not a replacement for its separate validation. No output is discarded or normalized by an event. In particular (12) does not grant exact earlier-time or rare-current-R1 correctness. A shorter head clock changes the integer L and its phase i^L; (11) uses the new actual L. It is not the old target with its phase silently retained. C_head, lambda, tau and w must likewise be recomputed for the selected family. There is still no uniform mu phase or physical stopping at tau.

## 5. Simultaneous local policies and resources

Write M=Lambda-omega>0 and C_P=(sqrt(5)+3)/2+2sqrt(2). There are two explicit options; neither uses a gap-only line estimate as though it were the cubic resolvent estimate.

### 5.1 Original line, with only the new head length

Choose N=ceil(8192pi^2/epsilon^2), kappa=M/16, Delta=kappa/N^2. With L from (8), set

 lambda_max=min{omega/2,M/(4C_P),epsilon Delta/65536,
                                      4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)],lambda=omega/(2m),tau=pi/lambda.

Use w in (8). The checked line elimination is <512lambda/Delta<=epsilon/128, the star error is <epsilon/64 and timing error <=epsilon/128, so E_loc<epsilon/32. All hypotheses of the local theorem are preserved: lambda<=Delta/8 and t<2tau. The simultaneous free revival remains exact. This option changes the head prefactor but retains sufficient time Theta(M^(-1)epsilon^(-5)) and size Theta(epsilon^(-2)) at fixed omega,M. It does not by itself improve that exponent.

### 5.2 Conditional cubic local-resolvent option

Choose n=ceil[(8192pi^2/epsilon^2)^(1/3)],N=n^3,kappa=M/32,Delta=kappa/(3n^2). Use

 lambda_max=min{omega/2,M/(4C_P),Delta/8,
      epsilon kappa/(262144sqrt(n)),4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)],lambda=omega/(2m),tau=pi/lambda.

The provisional resolvent source proves, on all symmetric data/reference inputs, elimination <2048lambda sqrt(n)/kappa. If that new interface passes its distinct check, the displayed choice pays epsilon/128; the same star and timing terms again give E_loc<epsilon/32. Every local constraint is retained when L changes. The clock constraint, of order M epsilon^2, eventually dominates the resolvent and gap constraints, both of order M epsilon^(4/3). Thus this conditional family still has size Theta(epsilon^(-2)) and time Theta(M^(-1)epsilon^(-2)); the exponent is unchanged by the present prefactor refinement. Rounding gives lambda_max/2<lambda<=lambda_max, not an unverified equality to its cap entry.

### 5.3 Actual inventory, placement and full-support cap

For either policy, the suffix remains14 slices and56 heads at the last coordinates. L_new>=16 leaves at least two ordinary input sites per rail. The established coordinate pattern and compensated positive blocks remain valid for every such L. Head counts are 4(L+1), head-block counts 8L+34, and maximum head load is (5+sqrt(2))J_c, with J_c<=J_budget. All compensating occupations stay positive because their subtracted local diagonal is <=(sqrt(2)+1)J_c<C_head=4J_c. No uniform shift is added on top.

Data loads remain

 load(P)<=omega+C_P lambda+8J_c<=omega+M/4+M/8,
 load(Q)<M/4, load(R)<=16J_c<=M/4.

For the line, reference load at B1 is <=omega+2kappa+2sqrt(2)lambda<omega+M/8+M/4, and the other reference loads are <=omega+4kappa=omega+M/4. Total qubits/blocks are 4L+N+7 and8L+2N+39.

For the cubic option, the corner load is <omega+6kappa+M/4=omega+3M/16+M/4, and other reference sites have at most omega+12kappa=omega+3M/8. Total qubits/blocks are 4L+N+7 and8L+N+40+3n^2(n-1). Every load uses complete-support positive-block norms, not projected or expectation-value cancellations.

The suffix is still in {0,1,2,3}^3 with its eight distinct upward rays, P=(0,0,0),R=(1,0,0),Q=(0,0,-1). The line reference uses (-j,0,0); the cubic reference uses (-1-i,-j,-k). Shortening each input ray and translating the virtual suffix indices does not move the suffix or create any site collision. Reference edges stay nearest-neighbor; suffix range<=9 and maximum total degree8 are unchanged. No claim of a wholly nearest-neighbor loader is introduced. Only declared interactions are installed despite other geometric adjacencies.

The coefficient of epsilon^(-2) in the real-valued head-length floor falls from (2^20)^2 to8192^2=2^26, a factor16384. Integer ceilings and unchanged additive core/local resources mean this is not an exact factor16384 reduction of every device count or runtime. In the cubic family's eventual clock-limited regime the leading clock constraint changes accordingly, but finite accuracy may be limited by another entry of lambda_max. These are explicit sufficient prescriptions with enormous constants, not practical hardware or manufacturing tolerances. The entire scalar and free phase in (11) uses the newly chosen physical coefficients.

## 6. Limits and check obligations

The key improvement is (1): no suffix prefix acts nontrivially on Q, and its P dependence is diagonal. Therefore H_S cancels exactly from the gauge defect. An arbitrary additional active H_PE, a P-flipping suffix or a different gate word could destroy this property and is not covered. Vloc remains installed throughout; its effect is bounded, not erased. The supplied initial reference coherence, equal gaps, blank R/heads, exact coefficient relations, head input and selective interactions remain premises.

The new proof does not depend on presumed small actual suffix occupation: it evaluates Duhamel on the exact factorized benchmark and controls the full actual difference. It does not infer release from the observation interval, factorization of actual dynamics, permanent record, repeated reference reuse or a thermal preparation mechanism. It also does not reduce any active-energy conservation requirement; all physical terms still commute with H_E.

ROOT supplied this prospective improvement, and I authored the baseline and the prior resolvent source. This is exposed author verification, not an independent check. The next distinct check should reconstruct the entire prefix table, especially the two diamond C coordinates and signs, the cancellation of H_S, Markov square-root factors, Gaussian constant, recalibrated phase and simultaneous cap/error policy. Baseline and cubic-resolvent dependencies retain their separate review requirements.

Only this PROPOSAL.md was created. Work used analytical inequalities and source reads; no scientific executable, symbolic solver, simulation, sweep, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model change, source overwrite or publication occurred. No editable prompt changed.
