# Distinct scoped check of the engineered-loader robustness policy

Disposition: SUPPORT at the stated finite-window, supplied positive-block scope. No required correction found. This is selective scientific review, not a retained audit, native realization, fabrication guarantee or all-time robustness result.

Reviewed the COMPLETE new source `exact_engineered_loader_robust_policy/PROPOSAL.md`, 25568 bytes, SHA256 `e69fa0e34d3fdb8d205cd1a8a5e26ea2efd3f3963a279b0d5edcf5d12ddbdc06`. All paths here are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

## 1. Actual support lemma and physical inventory

The perturbation class is material: each error is self-adjoint on the same listed support, preserves local head number and annihilates local head vacuum for EVERY local data state. It need not preserve any data operator, the exact rail gauge or a target axis. These assumptions imply that global one-head space is invariant. A head-data error can only act in the diagonal head-coordinate block at its own head. A two-head error has a 2 by 2 one-head compression, and each entry is bounded by its full-support norm. It acts as zero when the head is elsewhere. No term persists on shared data with the head outside its support.

For a head-coordinate vector with components psi_i, let M_ij be the norm of the (i,j) block of the total error. The quadratic form is bounded in absolute value by sum_ij M_ij ||psi_i|| ||psi_j||. Self-adjointness makes M symmetric; its row sum is at most twice the sum of full norms incident on that head. Thus the scalar Schur bound proves ||E_one|| <= 2 max_i d_i. The actual inventory has at most four listed blocks per head, so this is <=8 delta, irrespective of length or shared-data degree. This derivation does not use positivity of E or cancellations between different errors.

The four-block ceiling survives the positive compensations: a diamond terminal has two arm bonds, a cable and a potential; a gated arm has two arm bonds, a contact and a potential; an identity-u arm has two bonds, its separately listed identity occupation and its potential. Identity-v has fewer. A Hadamard terminal has two mixer bonds, a cable and a potential. Permutation and ordinary sites have fewer. Q/P have twenty contacts each and R eight, as in the unchanged nominal inventory. Splitting an existing block into extra independently perturbed pieces would change this premise.

Duhamel from time zero gives ||A_tilde(t)-A(t)|| <=8 delta t on the full encoded input isometry. Tensoring an arbitrary passive reference preserves this operator norm. No time before the observation interval is omitted. Substitution delta<=epsilon/(256 T_hor) yields beta_t<=epsilon/32 for every t in [0,T_hor]. A merely small nonscalar local-vacuum action, a data-only error or an unlisted support is not covered.

## 2. Cap, positivity, phases and counts

Scaling the nominal checked Hamiltonian to Jstar=Lambda/80 gives Q/P load <=Lambda/2, R load <=Lambda/5 and head load <=(5+sqrt(2))Lambda/80 <Lambda/2. Perturbation increases these by at most20 delta,8 delta and4 delta, respectively. Thus delta<=Lambda/40 is a sufficient simultaneous full-support cap condition. The more general margin (Lambda-40Jstar)/20 is likewise sufficient for 0<Jstar<Lambda/40. These are sums of actual block norms, not one-head energies.

The positive compensation lower bound is C-(sqrt(2)+1)Jstar=(3-sqrt(2))Jstar>0, with C=4Jstar. Ordinary/permutation cases have no smaller compensation. However original bonds and contacts have null spaces: a general arbitrarily small self-adjoint perturbation can produce a negative eigenvalue there. The source correctly keeps full-support positivity as a separate premise, rather than deducing it from delta. Reality is also separate if real physical matrices are required.

The inherited counts remain 4(L+1) heads, 4L+7 total qubits, and 8L+172 listed blocks. Independently, 756 compensated interior blocks plus twice the 4L-292 exterior heads gives 8L+172. These counts use separate identity occupations and compensating occupations. No new controls, error correction blocks or measurement apparatus are introduced. The existing range-18 placement is unchanged by supported errors; it is not nearest-neighbor or native realization.

The comparator keeps the exact nominal f_x=e^{-iCt} sqrt(binomial(L,x)) (i sin(alpha t))^x cos(alpha t)^(L-x), including the sign of cosine. The external physical prefix remains -U_f for the NOMINAL map. The perturbed map need not admit this gauge; its entire difference, including any coherent phase error, is paid by Duhamel. No new fitted phase or extra mu factor appears. All input/output data, head and passive-reference factors remain in the comparison. No active free data Hamiltonian is admitted.

## 3. Complete output and the joint event

If q0<=epsilon^2/1024, external projection of the nominal isometry is exactly sqrt(1-q0) V_t, where V_t uses the positively normalized external restriction of the full complex profile and the physical -U_f. The orthogonal complement has norm sqrt(q0). Therefore

    ||A_t-V_t||^2 = q0+(1-sqrt(1-q0))^2
                    =2-2sqrt(1-q0) <=2q0.

The source deliberately uses the weaker 2sqrt(q0)<=epsilon/16. Adding beta<=epsilon/32 gives 3epsilon/32. Twice this isometry bound gives the unhalved stabilized complete-channel distance <=3epsilon/16, with no postselection. This follows for arbitrary mixed inputs by purification and partial trace as well.

The joint event is external head AND actual R=1. These projectors commute because they act on different factors. In the nominal blank-R evolution every external component has R=1, so the nominal joint-failure amplitude is sqrt(q0), even though some internal components may also have R=1. Consequently actual joint-failure amplitude is <=sqrt(q0)+beta<=epsilon/32+epsilon/32=epsilon/16. Its probability is <=epsilon^2/256. Each marginal success probability is at least the joint one. This proof does not assume exact record correctness after perturbation, nor equate external-only and record-only events. Input dependence of actual event probabilities is allowed.

## 4. Two complete time policies

For the short window, alpha=Lambda/[40(L+1)]. The transfer time is pi/(2alpha)=20pi(L+1)/Lambda. Angular endpoints pi/3 and2pi/3 give the stated horizon80pi(L+1)/(3Lambda), not merely the window width. At p>=3/4 and L>=296,74<=L/4. The centered Bernoulli exponential bound gives q0<=exp(-L/2). Taking L>=4log(32/epsilon) makes this at most epsilon^2/1024, exactly the required nominal allocation. Dividing epsilon by256 times the horizon gives

    delta0=3epsilon Lambda/[20480pi(L+1)].

It is strictly below Lambda/40 throughout L>=296,epsilon<=1. Thus both constraints in (1) hold. The exact nominal instant phase -e^{-iCT}i^L remains correct; no perfect perturbed transfer is inferred. Minimal L gives the claimed logarithmic size and time orders, and sufficient ceiling of order Lambda epsilon/(1+log(1/epsilon)). A fixed nonzero delta instead imposes the stated upper bound on L+1 in this certificate.

For adjustable dwell, Markov on e^{-X} gives q0<=exp[74-(1-e^{-1})Lp]. If Lp>=148,74<=Lp/2 and1/2-e^{-1}>1/8, yielding exp(-Lp/8). Thus m=max{148,8log(1024/epsilon^2)} is sufficient. L>=ceil(2m) makes theta=arcsin sqrt(m/L)<=pi/4. On [theta,pi-theta] the mean remains >=m, and the complete interval lies before the return. Dividing its END time by the clock rate gives the stated arrival, horizon and dwell. The performance tolerance is exactly epsilon Lambda/[10240(pi-theta)(L+1)]. Since3pi/4<=pi-theta<pi, both inequalities (20), including cap sufficiency, follow.

For requested relative dwell Rcal>=2, theta<=pi/(Rcal+2) follows from (21); hence D/t_arr>=Rcal. The elementary bounds 2a/pi<=sin(a)<=a for a=pi/(Rcal+2) give the length bracket (22). The 296 floor cannot spoil the upper bracket since m(Rcal+2)^2/4>=592. The ceiling adds at most1. With y<=arcsin(y)<=sqrt(2)y, arrival is of order sqrt(mL)/Lambda, whereas dwell and horizon are of order L/Lambda. This independently establishes all four orders in (23), including the inverse-quadratic dependence of the sufficient error ceiling on relative dwell.

Writing X=m(Rcal+2)^2, L+1<=X/4+2 gives T_hor<40pi(L+1)/Lambda<=10pi(X+8)/Lambda. Therefore the closed ceiling epsilon Lambda/[2560pi(X+8)] is sufficient, as claimed. The qubit and block upper bounds follow by multiplying L<=X/4+1 by4 and8 and adding7 and172. The source correctly does not extend this ceiling automatically to an arbitrarily larger clock.

## 5. Normalized event branches and coefficient precision

For the inherited exact nominal record projection, virtual coordinate73 is the final antisymmetric arm component and74 is the final origin. Thus p1^0=|f73|^2+sum_{74}^L |f_x|^2>=1-q0. The record comparator is a different profile from external-only V_t. The source retains that distinction.

For a=P1 A_tilde xi and b=P1 A xi, ||a-b||<=beta. Put s=||b||>0 and r=||a||>0. The decomposition

    a/r-b/s = (a/s-b/s)+(a/r-a/s)

bounds the norm by beta/s+|s-r|/s<=2beta/s. Positivity of r is guaranteed here by the joint floor, or by beta<s. Substitution gives epsilon/[16sqrt(1-epsilon^2/1024)]<epsilon/8, and twice this bounds unhalved trace distance. The same argument applies to joint or external projection with nominal success1-q0 and target V_t. For mixed inputs it is a purified statewise bound with retained references. It is not a linear normalized-postselection channel bound when actual success depends on input. Outside the certified interval the source appropriately demands a separate nonzero floor and makes no uniform rare-event claim.

The minimum virtual hopping is Lambda sqrt(L)/[40(L+1)]. Dividing both exact delta ceilings by it gives respectively3epsilon/(512pi sqrt(L)) and epsilon/[256(pi-theta)sqrt(L)], agreeing with (28). These ratios concern the displayed sufficient tolerance, not a lower bound on device precision.

A fixed positive bond form has norm2 times its weight, as does a nonzero contact, including identity occupation2g n. A compensating occupation has norm equal to its weight. Thus scalar coefficient changes bounded by delta/2 for bonds/contacts and delta for potentials satisfy the full block-norm premise. The minimum actual bond is at least kappa_min/sqrt(2), nonzero contact parameter at least kappa_min, and compensation at least(3-sqrt(2))Jstar. Equations (28) and L>=296 show delta/2 is far below the first two lower bounds. Also delta_d<=epsilon Lambda/[7680pi(L+1)] and delta0 is smaller than this ceiling; division by Jstar=Lambda/80 makes delta/Jstar<=epsilon/[96pi(L+1)]<(3-sqrt(2)). Hence every fixed-form scalar weight stays positive. Independent coefficient changes can break matching and still meet the perturbative theorem. General matrix errors retain their explicit positivity premise.

## 6. Source identities, exposure and verification limits

The complete changed source was read without truncation. The newly relevant dwell source and its check were also read completely. Earlier complete reads of unchanged structured/engineered premises and checks were reused; the inventory/load passages and the entire structured finite-time lemma were refreshed directly. All seven byte/hash identities were recomputed. Necessary direct premises are:

| File | SHA256 |
|---|---|
| exact_loader_structured_coefficients/PROPOSAL.md | 515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2 |
| exact_loader_structured_coefficients_check/REVIEW.md | 273da0a0d28269e6e40aff0695f5465456acd35abe4c0b4eddc1acf0578334c8 |
| exact_engineered_clock_operation/PROPOSAL.md | b8bbfb7d40c491aff6b893df6423b98e68edad91ef6596124dac10f3620c53f8 |
| exact_engineered_clock_operation_check/REVIEW.md | 8351f91d29bbb570f8e9970962c2e0e24ea0db8dd06744d2180df761eae9272a |
| exact_engineered_clock_dwell_tradeoff/PROPOSAL.md | d739d552cc04424cb659f4107174d1dbe04756c0409704437176364aba0e0c25 |
| exact_engineered_clock_dwell_tradeoff_check/REVIEW.md | 7db9b3a4aaa62a0ae9e7c665a9767cc2ee5d65ee6f75960e97a8834648d48f46 |

I authored the structured/global ancestry and previously checked the engineered construction. ROOT's half-cap and tolerance proposal and the source were exposed before this review. This check is distinct analytical reconstruction of the NEW policy, not blind replication or independent confirmation of my own earlier lemma. The old gauge, exact record identity and physical placement are reused at their pinned scopes. No approximate earlier loader policy, active old-energy transfer, generic fabrication model or new physical supply is imported.

The physics-claim-reviewer approach was used selectively to inspect the actual comparison and hypothesis preservation; the requested model/effort and bounded task scope were preserved. All new arithmetic and inequalities above were checked analytically. No scientific executable, simulation, sweep, matrix solver, external search or delegation was used; deterministic commands only inspected sources and hashes and wrote this report. Only this REVIEW.md was created. No source, W, Git, checkpoint, axiom, editable prompt, model, publication or audit status was changed.
