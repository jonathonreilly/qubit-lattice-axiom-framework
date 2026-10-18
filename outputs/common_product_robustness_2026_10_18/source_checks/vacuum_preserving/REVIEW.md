# Vacuum-preserving robustness: distinct rectangular-norm check

Disposition: SUPPORT for the stated static, positive, same-support, scalar-vacuum replacement class. No required mathematical correction found. The new rectangular estimate is valid from nominal one-head inputs into the FULL many-head output space. Duhamel requires only nominal head-number invariance, so actual multi-head leakage is included rather than compressed away. The real number-changing example, fixed-phase budget, cap, exact-one-F-head success projector and finite-horizon guarantees are consistent. This is not an unrestricted error model or retained audit.

## Exact sources, complete reads and exposure

N denotes `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Read completely for this task and hash-verified:

- N/`common_product_vacuum_preserving_robustness/PROPOSAL.md`: `04702cd75574699e252c37e78d307ef606c1e7ba0db39b9c78bfaae4bb0add83`.
- N/`common_product_local_matrix_robustness/PROPOSAL.md`: `f9e427ccd5ec0a25f0c28639f9707728489a7a7dcca139e6f9fe03289d9b8a20`.
- N/`common_product_local_matrix_robustness_check/REVIEW.md`: `3d7be49f11dadbae49ed7c84a29e2a32ae8d38a83c1552a630716cc54c554b39`.

Necessary complete nominal source/check reads from my immediately preceding scalar-weight check are reused unchanged; refreshed their identities here:

- N/`common_product_single_control_router/PROPOSAL.md`: `76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01`.
- Its check: `549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0`.
- N/`common_product_single_control_publication/NOTE.md`: `02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde`.
- My scalar-weight review: `0995e9e58fc7aa93fe27a3892e9615be7f3fd72fb6c989709dcb0a84105549e1`, of source `3218676f11bbc39ecfcf3c84a568a2ffc8107a7b303f349195394a338b2b0623`.

The logarithmic source `7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8` is my authored proposal. Its separate check `d1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3` was fully read in that preceding task and is the scoped validation reused here; authorship is not independent evidence. The parent packet, finite, flag and actual writer inventories retain the exact identities and limitations in the preceding report and the fully read nominal sources. No blanket re-audit of those parents is claimed.

ROOT supplied the weighted input/output support idea and an attempted rotation example, and reported a complete favorable source read. I saw the source and those disclosures before reconstructing the new argument. The local-matrix review is now available, unlike its pending status during authoring; I read it, but its invariant-one-head proof does not automatically establish the present claim. This report checks that missing rectangular step directly. Prior checks/authorship and the same inherited model are disclosed exposure, not blind or model-diverse replication. No formal retained status is assigned.

Only this report was written. No scientific executable, numerical solver/simulation/sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. Previously read applicable reviewer/workflow instructions are reused.

## 1. Actual supports and scalar-vacuum assumptions

The nominal inventory has eight separately listed core vacancies and eight writer junction vacancies. Their scalars sum to c=8b+8(sqrt(2)-1)j. All other blocks annihilate their local HEAD vacuum on every local program/record state: bonds, phase occupations, fixed endpoint occupations, mediator/program occupations, terminal j n_T(I+X_R), combined sources and F caps. No free P or R term is present. Repeated endpoint vacancies remain separate blocks with separate admissible replacements.

The new hypotheses retain that scalar-vacuum structure explicitly. A'_l annihilates the full local head-vacuum subspace, and self-adjointness kills reverse matrix elements as well. Thus c'_l I is genuinely a scalar across all local fiber states; a program-relative or record-relative vacuum drive is not hidden inside it. Summing yields exact H=cI+K and H'=c'I+K', with |Delta c|<=delta c and E_l=A'_l-A_l self-adjoint, vacuum annihilating and of full local norm at mostdelta w_l. Positivity is a separate membership requirement, not inferred from that norm bound near a nominal zero eigenvalue.

Every listed block has one or two head sites. A mediator/program or terminal/record block has only one head site despite its additional fiber qubit. Their possible fiber rotations are unrestricted within the admissible class and must remain in the operator norm. No step below assumes P or X_R conservation. Fixed supports and absence of a fiber-only block are essential inputs.

## 2. Rectangular support identity on full outputs

On a global one-head configuration outside S_l, all local heads of block l are vacant. Thus E_l annihilates it, including arbitrary entanglement with fiber and reference, giving E_l Pi_1=E_l Pi_l^in.

If the input head is inside S_l, all heads outside S_l are vacant. Locality leaves them vacant. Since the local vacuum subspace is in the kernel of E_l and E_l is self-adjoint, its range is orthogonal to that entire vacuum subspace. Hence its output has a NONEMPTY occupied-head subset Z contained in S_l, with arbitrary P/R/reference state. This proves

`E_l Pi_1=Q_l^out E_l Pi_l^in`.

Crucially, Q_l^out sets every outside head to vacuum; it is not a projection requiring only that some head inside S_l be occupied while allowing others anywhere. The definition in the source has the stronger necessary meaning. The support identity is valid into the full head Hilbert space without assuming actual one-head invariance. A two-head-site error can output two heads, while a one-head-site/fiber error can rotate the fiber but cannot create another head outside its support at this insertion. Subsequent perturbed evolution may populate more heads; that is handled by full unitarity later.

## 3. Weighted column and row bounds

The input sum is diagonal in the one-head position basis, with coefficient sum_(l:v in S_l)w_l at position v. Therefore sum_l w_l Pi_l^in<=L_head Pi_1.

The output sum is diagonal in the full occupation basis. At vacuum it vanishes. At any nonempty configuration Z its coefficient is exactly sum_(l:Z subset S_l)w_l. Choose any v in Z. Every contributing block contains v, so this coefficient is bounded by the incident sum at v and thus by L_head. This selection is made per configuration and does not multiply the result by |Z|. For |Z|>2 no block contributes at all. Fiber/reference identity factors change none of these coefficients. Hence sum_l w_l Q_l^out<=L_head I on the unrestricted output space.

Define the weighted input column B, output row A and block-diagonal D exactly as in the source. Then B*B and AA* are the preceding projection sums; ||D||=max_l||E_l/w_l||<=delta. Multiplication cancels the two square-root weights against w_l and gives ADB=sum_l Q_l^out E_l Pi_l^in=Delta K Pi_1. Thus

`||Delta K Pi_1||<=sqrt(L_head) delta sqrt(L_head)=delta L_head`.

This is a rectangular domain-to-full-range bound. It is not a self-adjoint norm estimate on a compressed perturbed one-head Hamiltonian and makes no assertion that ||Delta K|| is length independent on extensively occupied inputs. Noncommuting fiber errors and overlapping supports do not change the proof. Passive-reference extension is immediate either from the same factorization or tensoring its factors. The vacuum-plus-one-head extension follows because Delta K annihilates global head vacuum, with no extra factor.

Nominal w_l are the full-support norms already checked:2|a| for bonds, coefficients for occupations/vacancies, D1-2b for mediator blocks,2j for terminal contacts and3j for a combined source. The last includes its double-occupation eigenvalue3j, larger than the one-head top eigenvalue of [[j,-gamma],[-gamma,2j]]. Therefore the physical full-block norm is not undercounted just because the nominal input is one-head.

The mediator incident sum is4b+(D1-2b)=D1+2b. Endpoint sum is6b+4j, writer-head sums are at most(4+sqrt(2))j and other source/ray/cap sums at most5j. Since j<=b/8 and D1>16b, the mediator sum dominates, giving L_head=D1+2b. The shared-P load4(D1-2b) and shared-R load8j must still be counted at their physical qubits for the cap. They do not create additional head coordinates or multiplicities in this rectangular estimate; their full fiber norms are already in w_l.

## 4. Duhamel and leakage into unrestricted head sectors

The nominal K commutes with Pi_1. In the exact Duhamel integral, the right trajectory exp(-isK)Pi_1 therefore remains in Pi_1. The left propagator exp(-i(t-s)K') is the actual FULL finite-space unitary and has norm1 even if it generates additional heads. Inserting Pi_1 immediately on the right of Delta K permits the rectangular bound at every integration time. Integration proves delta L_head |t|, capped by2 because the two maps from the one-head domain are isometries. The same argument with reversed integration orientation covers negative t.

There is no requirement for Pi_1 to commute with K', no repeated projection of the actual state, and no inference that later actual states have at most two heads. This is precisely why the replacement of the prior invariant-sector proof is necessary and sufficient here. No spectral completeness or special bound-state assumption is used.

Restoring the exact common scalars gives the explicitly rephased comparison against exp(-it Delta c)exp(-itH). Keeping the nominal phase instead adds2|sin(Delta c t/2)| and yields the stated min{2,delta(L_head+c)|t|}. Relative fiber phases remain in Delta K; only the true common scalar is separated. No unknown phase is silently fitted in the final targets.

Projecting the rephased difference onto I-Pi_1 annihilates the nominal term, proving leakage norm at mostmin{1,delta L_head |t|}. Global head vacuum is itself a reducing subspace: every remainder annihilates it on the full P/R fiber, and self-adjointness forbids couplings into it. Starting from one head, the possible leakage is thus to positive many-head sectors, not zero heads. This zero-vacuum fact is not head-number conservation in the other sectors. The leakage probability is the squared norm, including reference-entangled or mixed inputs by the uniform operator bound.

## 5. Real positive number-changing example

For the ordinary bond, Q_j has eigenvalues0 on V=|00> and S=(|10>+|01>)/sqrt(2), and2j on A=(|10>-|01>)/sqrt(2) and D=|11>. Rotating A and D would rotate within the same2j eigenspace and leave the matrix unchanged. The source correctly preserves that failed attempt rather than calling it head-changing evidence.

Instead D_s=cos(s)D-sin(s)S is unit and orthogonal to A,V. The replacement2j|A><A|+2j|D_s><D_s| is real, positive on all four local states, with eigenvalues0,0,2j,2j, and annihilates V. Its full support is the original two qubits and its scalar is zero. In the S,D plane the difference is2j times the difference of two unit-vector projectors. Its trace is zero and eigenvalues are ±2j|sin s|, so the stated full norm bound follows. For |s|<=delta it obeys ||E_l||<=delta||Q_j||.

For0<|s|<=delta<=1/2, its S/D matrix element is -2j sin(s)cos(s), nonzero. These states have different head numbers, so the commutator with head number is nonzero. Explicitly the D coefficient generated from S by this isolated block is -sin(s)cos(s)[exp(-i2jt)-1]; it is generally nonzero. At delta=0 only the nominal example is available, as expected. This demonstrates a genuine enlargement of the admissible supplied local-matrix class, without asserting a native mechanism for producing it. Mixing V with a positive mode would violate the retained vacuum hypothesis and is not admitted.

## 6. Cap and simultaneous complete-target guarantees

The scalar and remainder allowances give ||h'_l-h_l||<=delta(w_l+c_l)<=2delta w_l, hence ||h'_l||<=(1+2delta)w_l. All-qubit nominal incident sums are strictly belowLambda/2 in the one-control prescription, including P and R. With delta<=1/2 every perturbed incident sum remains strictly belowLambda, using full local norms and positivity as separate conditions. No one-head expectation replaces the physical cap.

The inherited algebra gives L_head+c=D1+10b+8(sqrt(2)-1)j<(25+sqrt(2))Lambda/128<Lambda/4. At nominal tau=epsilon/2, the checked final-window error is below3epsilon/16 and the absolute whole-horizon branch error belowepsilon/4. For delta<=min{1/2,epsilon/(Lambda T)}, delta Lambda T<=epsilon, so the fixed-nominal-phase perturbation cost is belowepsilon/4 on[0,T]. This remains true when the1/2 branch is selected, and at delta=0 the actual perturbation contribution is zero.

The original normalized nominal target therefore has complete error below7epsilon/16 in the FULL physical output Hilbert space. All program rotations, wrong-record amplitudes and multi-head configurations are included. Actual evolution of the supplied seed is still an isometry because H' is self-adjoint; the nominal target is an isometry. Their unhalved complete-channel/diamond discrepancy is consequently below7epsilon/8<epsilon with references.

For the entire horizon, multiplication by P_R1 is contractive without any commutation assumption. Adding the same perturbation cost to the original nominal absolute branch estimate gives error belowepsilon/2 against the SAME unnormalized V_nom(t) at every time. Both maps are contractions, giving unhalved subnormalized-channel discrepancy belowepsilon by the two-term difference expansion. An actual flagged many-head state remains part of this discrepancy. There is no changed packet, early zero-target switch, actual-output normalization or division by a small success probability.

The proposed Pi_good is the sum of singleton head configurations on retained F sites, multiplied by record1 and identity on P/reference. Its global occupation basis definition requires EXACTLY ONE total head and all other heads vacant. The nominal normalized target lies in its range, so its orthogonal complement bounds failure probability by(7epsilon/16)^2. Record1 alone contains that good subspace and has at least the same probability. This does not weaken success to allowing any number of heads on F, and the probability statement alone is not substituted for logical fidelity.

Throughout the horizon, the independent leakage estimate gives probability at most(delta L_head T)^2<(epsilon/4)^2. It is already included in the complete-state error and is not added as another allowance. The latter bound uses L_head<=L_head+c<Lambda/4 and the same delta prescription, with no actual-sector invariance reintroduced.

## 7. Quantitative scope and limits

The unchanged nominal logarithmic family at tau=epsilon/2 has T=Theta(Lambda^-1 epsilon^-15/2), so the admissible local-remainder norm parameter delta_safe is Theta(epsilon^17/2). This is a sufficient uniform matrix-norm allowance with independent positivity, scalar-vacuum, same-support and scalar-error requirements. It is not an unconstrained entrywise box, necessary precision, fabrication budget or state-dependent optimum. The generator bound has no extra length factor; the increasing certified duration still tightens the tolerance.

This new result drops perturbed head-number conservation, not nominal conservation or the local vacuum structure. Head creation from local vacuum, nonscalar vacuum P/R drives, changed supports, nonpositive replacements and input-state errors remain outside the theorem. They cannot be included merely by citing a small matrix norm, since the decisive input/output support identity may then fail. No universal impossibility claim is made about those other classes.

The proof is conditional on the supplied nominal apparatus and seed, with bounded finite-horizon conclusions. It supplies no native Hamiltonian/Record/readout, autonomous initialization, coefficient-production mechanism, old literal processor transfer, indefinite protection, normalized arbitrary-time heralding, irreversible latch, capture/reset or permanent halt. The precursor local-matrix result's old exclusion of head-changing errors describes that earlier proof boundary; the present rectangular argument resolves only the explicitly retained vacuum-preserving subclass.
