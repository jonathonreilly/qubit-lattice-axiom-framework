# Distinct check: active-energy suffix prefactor

**SUPPORT at the stated supplied-Hamiltonian scope.** The entire prefix table commutes with H_S; the exact gauge defect is bounded by 2g, rather than 8lambda. The changed Markov parameter, square-root factors and Gaussian integral give the asserted coefficient below64. The shorter prescribed head length and both simultaneous local policies preserve the complete-output error, phase, cap and inventory. No required correction was found.

This is a source-exposed selective check of the new cancellation, constant and policy substitution. It is not a fresh independent validation of all inherited apparatus, a retained audit, or a claim of native preparation, permanent halt or all-time current-record correctness.

## 1. Exact sources and exposure

All paths are relative to N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- Fully read the new `active_energy_suffix_prefactor/PROPOSAL.md`, SHA256 `793e9706b867f415647f2f6b7370f8e0daba0bf5efb993be3373c5337e52d0d0`, and reconstructed all changed steps below.
- Refreshed the exact suffix coordinates, literal clock compensation, gauge, tail and policy passages of `active_energy_loader_interface/PROPOSAL.md`, SHA256 `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`. Its complete argument was read and checked in my preceding review `active_energy_loader_interface_check/REVIEW.md`, SHA256 `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`.
- Reused the immediately preceding complete read/check of `cubic_reference_resolvent/PROPOSAL.md`, SHA256 `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895`, review `cubic_reference_resolvent_check/REVIEW.md`, SHA256 `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5`.
- Reused the unchanged line-elimination premise `local_reference_static_swap/PROPOSAL.md`, SHA256 `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`, and its previously fully read/check evidence `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b`. The underlying star/effective-SWAP premise is `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`, checked by `69c07739988970d1671e2b5acd985ec48d935d74066afc456761301e086be195`.
- The cubic gap premise `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee` and distinct review `507e83cce4949b58c8dbc0ba84339ba9af05e55fa02a11ab2da1a223c62997d7` were completely read in the immediately preceding task.

The new source and affected parent proposal identities were verified again. ROOT proposed the sharper defect and Markov route; the author also authored the baseline and resolvent. I share campaign ancestry and checked those predecessors, with authorship exposure to the underlying exact clock/gauge constructions. This review independently reconstructs the new argument under that exposure; it is not blind or independent-lineage evidence. Historical pending statements in the author source remain unchanged; ROOT has now separately accepted the baseline and resolvent checks.

## 2. Prefix reconstruction, signs and commutation

The chronological layers are H,D,H,X,X_R, where D=CZ_(b,P), while the two diamond middle transitions carry minus signs. Reading the actual ordered links gives these prefixes:

- Through the first H's left site L-14: I.
- Across its H link, then the cable and first diamond's left outer link, sites L-13,L-12,L-11: H.
- Across the first diamond's middle B-to-C link: -D H, continuing at L-10,L-9,L-8.
- Across the second H link: -H D H at L-7,L-6.
- Across the permutation link: -X H D H at L-5,L-4,L-3.
- Across the final diamond's middle link: (-X_R)(-X H D H)=X_R X H D H, at L-2,L-1,L.

Thus the table includes the physical arms after the fixed head-only rotation, not just complete gates. The identity rails in the controlled-Z layer also acquire the common minus, so there is no missing rail-dependent scalar. Auxiliary a is unchanged. Since L>=16, the actual seed at0 is in the identity-prefix region.

Every displayed factor commutes with X_Q and Z_Q because it acts trivially on Q. It also commutes with Z_P: H and X act only on b, D is diagonal in P, and X_R acts only on R. Therefore every ordered product commutes with all terms of H_S=aX_Q+b(Z_Q+Z_P)+cZ_QZ_P. No assumption that the factors mutually commute is used. H_E commutes with each prefix because the P actions are diagonal and reference qubits are untouched; H_F commutes because it acts on reference qubits only. The common scalar s commutes trivially.

The head-only arm rotation commutes with the local apparatus, so the exact difference in the gauged Hamiltonian is precisely

 E_x=G_x^*Vloc G_x-Vloc.

Before L-10 the prefixes are I or H, and this is zero. For all x, ||Vloc||=g on the full P/reference support, since the exchange has eigenvalues 1,-1,0,0. Unitary conjugation and the triangle inequality give ||E_x||<=2g. This holds for arbitrary path, P and reference states, including correlated spectators, without a product-state or small-leakage assumption. The full defect is block diagonal in virtual x, so its norm on a vector is bounded by 2g times the norm of that vector restricted to x>=L-10.

The endpoint word is X_R X H D H. Resolving P shows H D H=I_b for P=0 and X_b for P=1. Multiplying X_b gives X_b for P=0 and I_b for P=1. Hence the endpoint is +X_R C_P^(b), exactly the inherited target word before SWAP, with positive overall sign. H_S cancellation is special to this suffix: arbitrary additional P-flipping terms or active environment interactions are not covered.

## 3. Tail integral from time zero

The benchmark is h_L plus the actual local apparatus. The latter can entangle its inputs but has norm-preserving evolution and is independent of scalar coordinate x. Thus Duhamel evaluated on this benchmark gives

 E_join(t)<=2g integral_0^t sqrt(Pr[X_v>=L-10]) dv,

where X_v is binomial(L,sin^2(alpha v)). This does not assume actual joint evolution factorizes or that the logical input is uncorrelated. It bounds the complete actual difference.

For 0<=v<=tau, alpha=lambda/2 and alpha tau=pi/2. Put Y=L-X, p=cos^2(alpha v), z=1/11. Markov's inequality applied to the decreasing random variable e^(-zY) gives

 Pr[Y<=10]<=e^(10/11) E[e^(-Y/11)]
             =e^(10/11)[1-(1-e^(-1/11))p]^L.

The threshold direction is correct. From e^(1/11)>=12/11 follows e^(-1/11)<=11/12 and 1-e^(-1/11)>=1/12. Applying 1-y<=e^(-y) and taking the square root produces e^(5/11)exp[-L cos^2(theta)/24]. In particular the Gaussian coefficient is 1/24, not 1/12, after the square root.

Set y=pi/2-theta. The chord bound cos theta>=2y/pi gives

 integral_0^tau sqrt(p_tail(v))dv
 <=(2/lambda)e^(5/11) integral_0^infinity exp[-L y^2/(6pi^2)]dy
 =e^(5/11)pi sqrt(6pi)/(lambda sqrt L).

The factor two from dt=2dtheta/lambda cancels the Gaussian half integral. Multiplying 2g=2sqrt(2)lambda yields C/sqrt L with C=2sqrt(2)e^(5/11)pi sqrt(6pi).

The source's entirely analytic ceiling is valid: sqrt(2)<10/7, pi<22/7, sqrt(6pi)<35/8. For x>=1 the derivative of log x-2(x-1)/(x+1) is (x-1)^2/[x(x+1)^2]>=0. At x=8/5 this proves log(8/5)>=6/13>5/11, so e^(5/11)<8/5. Multiplication gives

 C <2(10/7)(8/5)(22/7)(35/8)=440/7<64.

The use of an upper bound larger than1 near tau is harmless. For later times at most w beyond tau, the separate trivial bound sqrt(p_tail)<=1 suffices. For earlier t the nonnegative integral is at most its integral to tau. Thus, uniformly from zero through tau+w,

 E_join(t)<64/sqrt L+2sqrt(2)lambda w.

There is no assumption of tail monotonicity after tau or of cancellation in an oscillatory amplitude integral.

## 4. New length, complete target and budgets

For L=ceil max{16,(8192/epsilon)^2}, 64/sqrt L<=epsilon/128. Retaining w<=epsilon/(1024lambda) gives the additional contribution at most sqrt(2)epsilon/512<epsilon/128. Hence E_join<epsilon/64. This is a strict bound even if the length floor is an integer.

The unchanged scalar-clock centered operator has norm lambda L/2. At tau its endpoint coefficient is e^(-i C_head tau)i^L. Comparing its centered evolution at nearby t gives

 ||f(t)-e^(-i C_head t)i^L|L>||<=lambda L |t-tau|/2<=epsilon/128.

This uses the new actual L, lambda and C_head. If the local complete SWAP error is <epsilon/32, the three errors add to <(4+2+1)epsilon/128. The isometric target is therefore exactly the source's expression

 e^(-i(C_head+s)t)i^L e^(-i pi/4)
 [external endpoint embedding of I_a X_R C_P^(b)SWAP_QP xi] tensor beta(t).

The free reference factor beta(t) is retained, the P free factor is handled at the synchronized integer revival with its inherited timing error, and no extra uniform-mu or ferromagnetic phase occurs. An old numerical i^L phase cannot be reused after choosing a different L; the source explicitly recalculates it.

The uniform complete-vector bound yields stabilized unhalved channel error <7epsilon/64. Since the normalized target is supported in the external-endpoint AND R1 event, its complement has norm below7epsilon/128 and actual event probability exceeds 1-(7epsilon/128)^2. This uses no renormalization of actual outputs. It does not establish a rare-event conditional gate or an exact current-R1 identity at earlier times.

## 5. Both simultaneous parameter choices

For the line option, N>=8192pi^2/epsilon^2, kappa=M/16 and Delta=kappa/N^2. The minimum gives lambda<=epsilon Delta/65536, so elimination <512lambda/Delta<=epsilon/128. It also implies lambda<=Delta/8. On the common window t<2tau, the star error is <sqrt(2)pi/sqrt N<=epsilon/64. The first w entry pays timing <=epsilon/128. The local sum is therefore <epsilon/32 as required. All entries are positive for the inherited assumptions Lambda>omega>0 and 0<epsilon<=1. Integer rounding gives lambda_max/2<lambda<=lambda_max. The first w entry also ensures w<tau, so none of the elimination or star time domains is exceeded.

For the cubic option, N=n^3>=8192pi^2/epsilon^2, Delta=kappa/(3n^2), kappa=M/32. The explicit Delta/8 entry preserves the Neumann inverse condition. The epsilon kappa/(262144sqrt n) entry gives elimination <2048lambda sqrt n/kappa<=epsilon/128. Star and timing allowances are identical to the line option. Hence its local error likewise meets the same <epsilon/32 interface. This uses the now separately checked all-symmetric-sector resolvent result, not the old line gap-only formula. The physical symmetry and cap constraints are retained simultaneously with the changed clock entry.

For either family J_c=lambda(L+1)/4<=J_budget=M/64. The full-support head load remains at most (5+sqrt(2))J_c; P is bounded by omega+M/4+M/8, Q by M/4 and R by M/4. Positive compensations remain valid: all module subtractions are at most (sqrt(2)+1)J_c and ordinary ones at most2J_c, strictly below C_head=4J_c. The actual onsite common diagonal is not counted a second time.

Line reference loads are at most omega+2kappa+2sqrt(2)lambda at its attached endpoint and omega+4kappa elsewhere; lambda<=M/(4C_P) makes the former <omega+M/8+M/4. Cubic loads are at most omega+6kappa+2sqrt(2)lambda at the corner and omega+12kappa elsewhere, bounded respectively by omega+3M/16+M/4 and omega+3M/8. Every displayed bound fits Lambda on complete supports.

The fixed suffix still has fourteen slices and fifty-six heads. L>=16 leaves ordinary coordinates0 through L-15, at least two sites per rail. Four full rails have 4(L+1) heads and 8L+34 head blocks. Adding the line local inventory yields 4L+N+7 qubits and 8L+2N+39 blocks; adding the cubic inventory gives 4L+N+7 qubits and 8L+N+40+3n^2(n-1) blocks. The suffix stays at its established range-nine cube, while shorter input rays remain disjoint upward rays. The negative-x reference line or cube remains disjoint from the suffix, Q and those rays. No new coupler or higher-body term is installed by the gauge calculation. Maximum degree8 and the distinction between nearest-neighbor reference and bounded-range full device are preserved.

## 6. Resource interpretation and limits

At fixed positive omega,M, the line restriction epsilon Delta scales as M epsilon^5, while the clock cap scales as M epsilon^2. The former eventually controls, so its sufficient runtime remains Theta(M^(-1)epsilon^(-5)); size remains Theta(epsilon^(-2)). In the cubic family both local resolvent and gap constraints scale as M epsilon^(4/3), whereas the clock cap scales as M epsilon^2 and eventually controls. Thus its sufficient runtime remains Theta(M^(-1)epsilon^(-2)), with size Theta(epsilon^(-2)). Revival rounding preserves these orders. No exponent improvement is caused by this prefactor-only change.

The real-valued length floor changes from 2^40 epsilon^(-2) to2^26 epsilon^(-2), a ratio2^14=16384. Ceilings, additive resources and the other lambda_max restrictions preclude claiming that exact factor for every physical device or runtime. The source correctly keeps the full minimum rather than equating lambda to the clock cap at finite epsilon. It also retains the necessary updated scalar and free phases.

The sharper bound still pays nonzero coupling throughout the evolution and assumes supplied product reference coherence, equal gaps, blank R/heads, calibrated structured couplings, selective interactions and the stated input. It provides neither physical release nor exact all-time factorization of actual joint dynamics. Arbitrary H_PE, native initialization, stable storage, reuse and permanent halt remain outside the theorem.

Work consisted of complete changed-text reading, targeted refresh of unchanged parent passages, exact hash bookkeeping and analytical reconstruction. No scientific executable, numerical fit, symbolic solver, sweep, external search or delegation was used. Only this REVIEW.md was created. No source, W/canonical, Git, checkpoint, axiom, editable prompt, model/effort or publication/audit status changed.
