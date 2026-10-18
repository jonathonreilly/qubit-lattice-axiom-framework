# Distinct check of the autonomous active-energy suffix interface

Disposition: SUPPORT at the explicit supplied-Hamiltonian finite-window scope. No required correction or unresolved mathematical step found. This supports the new complete U_f composition with literal omega n_P and the stated product reference. It does not supply arbitrary active H_PE, reference preparation, all-time exact record correctness, a native realization, capture/reset or permanent halt. It is selective analytical review, not retained audit status.

Completely read the new `active_energy_loader_interface/PROPOSAL.md`, SHA256 `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`. Paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/` unless stated otherwise. The unchanged local-reference and effective SWAP calculations reuse the exact previously read/checked sources; the new suffix, gauge defect, tail integral, synchronization and joint physical resources are reconstructed here.

## 1. Ordered five-layer operation and first defect coordinate

The chronological word is H_b, CZ_(b,P), H_b, X_b, X_R. Each diamond layer carries its fixed minus on every rail, including identity diamonds. Thus the first four layers act as -X_b H_b CZ_(b,P) H_b. Since H_b CZ H_b flips b when P=1, its product with X_b flips b when P=0, giving -C_P^(b). The final all-rail record diamonds contribute -X_R. Their product is +X_R C_P^(b), with no remaining minus. Acting after the local SWAP gives exactly U_f as defined, on arbitrary coherent path/QP/passive-reference input; it is not the full old26-layer word or a second SWAP.

The slice counts are2+4+2+2+4=14. With the first slice L-14, the CZ segment has terminal L-12, B=L-11, C=L-10 and final terminal L-9. Before its C coordinate the prefixes are I or H_b, including its B coordinate; they act only on rail labels and commute with W_loc. At C the prefix is -CZ_(b,P) H_b, so it is the first potentially noncommuting prefix. The threshold x>=L-10 in the norm estimate is therefore correct and conservatively includes every later slice and the endpoint.

Every prefix acts on P only through operators diagonal in P (possibly with noncommuting operations on the rail label), and on R without a free R Hamiltonian. It follows that every prefix commutes with HE. No prefix acts on the reference B_j, so it also commutes with HF. This does not imply commutation with V_loc: the P-reference exchange changes P and is the actual defect requiring a bound. Indeed H_S itself commutes with these prefixes, but the larger bound involving all W_loc is safe. Replacing this suffix by P-flipping earlier loader layers would invalidate the HE argument.

## 2. Physical positive clock and exact transformed Hamiltonian

The structured diamond/hadamard/permutation identities apply with the new k_r. The bound sqrt[r(L+1-r)]<=(L+1)/2 gives k_r<=lambda(L+1)/4=J_c for alpha=lambda/2. Diamond terminal, arm, Hadamard and permutation subtractions are at most(sqrt(2)+1)J_c, and ordinary ones at most2J_c. Hence the proposed compensation to C_head=4J_c is positive at every physical head, including endpoints. Identity-arm occupations stay separate from compensations; no old mu repair is added again.

The actual head-only one-head operator is unitarily equivalent to h_L tensor identity on the full rail/data/reference fiber. The arm rotation A acts only on head coordinates and commutes with H_loc. The direct-sum prefix G commutes with HE,HF and the scalar s. Therefore conjugating the ACTUAL sum H_head+H_loc gives exactly equation(7), with E_x=G_x*W_loc G_x-W_loc and no unaccounted large HE or HF term. This statement is on the preserved one-head sector; it does not assert an all-head gauge identity. The physical positive supports themselves are full-space blocks.

Since ||W_loc||<4lambda, ||E_x||<8lambda, and E_x=0 below L-10. The benchmark h_L+H_loc is a sum of operators on independent scalar-coordinate and rail/data/reference factors, so its evolution has scalar coefficient f_x(t) times the SAME actual local state at every x. Arbitrary initial correlations between path and QP/reference do not change that scalar factorization. Consequently the norm of E acting on the benchmark input is bounded by8lambda sqrt(sum_{x>=L-10}|f_x|^2). Duhamel uses this benchmark trajectory, not a factorization assumption on the actual combined state. The exact unitary on the other side of its integrand has norm1. This proves (8) in induced norm, including passive references.

The source coordinate0 precedes the suffix since L>=16, so A and G are identity there. The benchmark and actual supplied inputs are therefore identical at preparation time. No physical release, switch, projected early head state or extra installed higher-body interaction has entered this comparison.

## 3. Integral from time zero

Under h_L, the position law is Bin(L,sin^2(alpha v)); its complement Y=L-X is Bin(L,cos^2(alpha v)). For v in[0,tau], alpha v is in[0,pi/2]. On Y<=10, e^{-Y}>=e^{-10}, so Markov gives

    p_tail<=e^{10}[1-(1-e^{-1})cos^2(alpha v)]^L
             <=exp[10-(L/2)cos^2(alpha v)].

This is valid even when its upper bound exceeds1. Taking its square root gives e^5 exp[-L cos^2(alpha v)/4]. Concavity of cosine on[0,pi/2] gives cos(theta)>=2(pi/2-theta)/pi. With y=pi/2-alpha v and dv=dy/alpha, extension of the positive Gaussian integral to infinity yields

    integral_0^tau sqrt(p_tail(v))dv
       <=(e^5/alpha) integral_0^infinity exp(-Ly^2/pi^2)dy
       =pi sqrt(pi)e^5/(lambda sqrt(L)).

This independently confirms both the factor of two from alpha=lambda/2 and the square-root probability cost. Multiplication by8lambda is less than8192/sqrt(L); e^5<149, pi<22/7 and sqrt(pi)<2 already give a coefficient below7493. All time from preparation to the local revival is included. For any t<=tau the same ceiling applies by positivity. For tau<t<=tau+w the extra integral is <=w because actual scalar p_tail<=1, not because the Gaussian remains a good estimate. Thus E_join<=8192/sqrt(L)+8lambda w on the required whole horizon. A uniform defect bound integrated without the head distribution would not close; no such shortcut is used.

## 4. Local comparison and synchronized policy

The local reference source supplies the complete-space gap Delta=kappa/N^2 and the projected-star comparison, with elimination error <512lambda/Delta when lambda<=Delta/8 and t<=2pi/lambda. Its benchmark is the ACTUAL local apparatus, exactly the operator used in section2, so the two comparisons can be composed without an unmatched Hamiltonian. The source's effective gate, full SWAP phase and residual on arbitrary QP input are unchanged. After reinstating the exact free factor, its near-revival error is (1), with freely evolved beta(t); HE does not commute with Heff and its ordered data factor is paid rather than silently removed.

The policy determines N,kappa,Delta,L and lambda_max before choosing the integer m. All maximum/minimum terms are positive for Lambda>omega>0 and epsilon>0. Since lambda_max<=omega/2, m>=1 and lambda=omega/(2m)<=lambda_max. Thus tau=pi/lambda=2pi m/omega is simultaneously the local effective SWAP time, the full HE revival and the scalar-clock endpoint transfer time because alpha=lambda/2. No waiting with one interaction removed is assumed.

The restrictions imply J_c=lambda(L+1)/4<=J_budget, lambda<=epsilon Delta/65536<=Delta/8, and512lambda/Delta<=epsilon/128. From the first width restriction w<tau, so t<=tau+w<2tau is within the local elimination interval. From N>=8192pi^2/epsilon^2,

    gt/(2sqrt(N))<g tau/sqrt(N)
                =sqrt(2)pi/sqrt(N)<=epsilon/64.

The first width restriction also makes local timing cost <=epsilon/128. Hence E_loc<epsilon/32. This recomputes the constants for the new kappa and lambda rather than borrowing the old cap prescription.

L>= (2^20/epsilon)^2 gives8192/sqrt(L)<=epsilon/128. The second width restriction gives8lambda w<=epsilon/128, so the join error is <=epsilon/64. Finally ||h_L-C_head I||=alpha L=lambda L/2, from the symmetric-spin representation. Factoring the exact C_head scalar, comparing e^{-it(h_L-C_head I)} to its value at tau, and using (6) yields the complete head error <=lambda L|t-tau|/2. The third width restriction makes this <=epsilon/128. This controls the whole benchmark head state without conditional normalization. These three restrictions are simultaneous, not separately chosen operating points.

## 5. Complete output phase and event bound

At the external endpoint A is identity and G_L=+X_R C_P^(b). The clock comparator is e^{-i C_head t}i^L|L>. The local comparator is e^{-i(st+pi/4)}SWAP_QP with beta(t) and blank R. Applying the physical prefix therefore gives exactly (15), with positive overall suffix sign, U_f in the required order and every phase once. There is no additional mu or ferromagnetic identity phase. The former is absent under the compensated engineered diagonal; the latter remains inside the zero-ground HF comparison.

One may first pay the join error, then replace the normalized benchmark clock by its endpoint comparator, and then replace the local state by its comparator. All intermediate operations used to transport these errors are unitary or normalized tensor insertions. Thus the complete induced vector error is <epsilon/64+epsilon/128+epsilon/32=7epsilon/128. It holds for the arbitrary coherent encoded path and QP/reference domain stipulated in the source, with all head, record, old-state and reference outputs retained. The twice-isometry estimate gives unhalved stabilized complete-channel error <7epsilon/64. The target is normalized and lies wholly in the external-endpoint AND R1 event, giving its actual success probability >1-(7epsilon/128)^2 by complementary projection.

The reference profile is beta(t), and the known scalar phase is time dependent. Neither is replaced by its value at tau over the window. There is no postselection, trace-out or fitted phase in the proof. The actual current R1 branch can be wrong when rare or outside this window: the defect E is nonzero, so the earlier exact all-time factorization is not inherited. The source explicitly refrains from that claim. Exact HE conservation is consistent with the approximate SWAP because the actual reference/correlations carry the energy difference; norm proximity does not restore its energy moments or authorize reuse.

## 6. Counts, full-support load and geometry

There are eight diamonds: two gated and two identity in CZ, and four gated in the record layer. Their block counts are22 and24. Two four-rail Hadamard layers contribute16 bonds, the permutation4, and four module gaps16 cable bonds, totaling82. Adding56 head potentials gives138 suffix blocks. Four copies of the L-13 exterior virtual coordinates and links give4L-52 ordinary heads,4L-52 bonds and4L-52 potentials. Thus H_head has8L+34 blocks and4(L+1) heads. With three data qubits and N references the total is4L+N+7 qubits; adding the local apparatus2N+5 blocks gives8L+2N+39. The mathematical spins used to solve h_L are not extra hardware.

There are four actual P contacts of norm<=2J_c and eight R contacts of the same ceiling. The compensated head load bound(5+sqrt(2))J_c follows from the actual structured occupation formulas, not an effective one-head norm. Under J_budget=(Lambda-omega)/64 and lambda<=(Lambda-omega)/(4C_P), P load is <=omega+M/4+M/8, Q load <M/4, R load <=M/4, and ordinary/reference head loads meet the displayed ceilings. Specifically B1 has2kappa=M/8 and2sqrt(2)lambda<=sqrt(2)M/(2C_P)<M/4, since C_P>2sqrt(2). Other reference sites have at most4kappa=M/4. All are below Lambda, including identity shifts and free occupations. No mean occupancy, projection or cancellation reduces the physical sums.

The range9 embedding has64 cube sites. Removing P,R and the8 distinct ports leaves54 available sites for the48 other suffix heads; hence the injection exists with6 cube sites unused. The four left and four right ports have distinct horizontal coordinate pairs. Their vertical rays lie outside the cube for z>3 and cannot collide, even though the input rays have length L-14 and output rays length1. Q=(0,0,-1) and B_j=(-j,0,0) are distinct from the nonnegative cube sites and from those rays. QP, PB1 and reference-chain bonds are nearest-neighbor. Every internal cube pair has Manhattan separation at most9. Thus all installed pairs satisfy range9, with maximum degree8 at R and degree6 at P (four head contacts plus Q and B1). Uninstalled geometric adjacency does not create a coupling. The source properly does not claim a fully nearest-neighbor cubic device.

At fixed positive omega and M, N,L are Theta(epsilon^{-2}); Delta=Theta(M epsilon^4). The epsilon Delta entry of lambda_max is eventually smaller than the constant entries and the clock-cap entry of order M epsilon^2. Rounding m loses at most a factor2 because omega/(2lambda_max)>=1. Hence lambda=Theta(M epsilon^5) and tau=Theta(M^{-1}epsilon^{-5}), with total size Theta(epsilon^{-2}). These are sufficient-family orders with the explicit huge L constant retained, not practical or optimal performance. All coefficients, initial product reference/coherent head state and isolation remain supplied.

## 7. Exact evidence, exposure and remaining limits

Hash-refreshed operative inputs:

- `active_energy_loader_interface/PROPOSAL.md`: `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`.
- `local_reference_static_swap/PROPOSAL.md`: `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`.
- Its check: `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b`.
- `product_reference_static_swap/PROPOSAL.md`: `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`.
- W/`docs/EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md`: `43558ea59ebee23bf539d27ba1818a06b914fff52bb87d251b959b4889f3b868`.

The new source and full canonical clock/diamond manuscript were read completely. The local source/check and effective SWAP source retain the immediate earlier complete reads and reconstructions; their unchanged hashes were verified. The canonical manuscript pins the already checked diamond7fa888, corrected matching a1157, global f874302, structured515c9e and engineered b8bbfb sources and their checks. Only their actual local block/gauge and scalar engineered identity is reused here. The old26-layer finite performance and exact current-record theorem are not premises of the new active composition.

ROOT suggested the diagonal-P autonomous-suffix route; the author disclosed that exposure. I authored global/structured ancestry and have checked the local-reference and engineered constructions. This is a source-exposed same-model distinct check of the NEW joint composition, not blind replication or independent evidence for my own earlier premises. The successful local and clock checks were not treated as evidence that attachment automatically works; the explicit defect and its norm integral discharge that new obligation.

The stated suppliers and limits remain substantive: exact signed positive matrices and equal gaps, coefficient correlations, coherent path input, blank heads/R, prepared phase-aligned product reference, isolation, degenerate Q/R and passive extra references. The result is not the historical arbitrary active processor, an all-time faithful flag, reference preparation/cooling, receiving apparatus, capture, reset or permanent halt. No hidden active H_PE or autonomous switch is modeled. No mathematical gap was found within this narrower explicit model.

Only this REVIEW.md was created. Work was complete reading, analytical reconstruction and deterministic hashes/file bookkeeping, without scientific execution, solver, simulation, sweep, external search, delegation, source/W/Git/checkpoint/axiom/editable-prompt/model changes or publication/audit action. Completed before the specified deadline.
