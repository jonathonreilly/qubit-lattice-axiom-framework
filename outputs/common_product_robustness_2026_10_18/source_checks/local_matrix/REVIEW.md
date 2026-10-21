# Distinct check: positive local matrix robustness

Disposition: SUPPORT at the stated conditional, supplied-matrix scope. I found no correction required in the new argument. This is a source-exposed analytical check, not a retained audit, native realization, blind replication or independent recheck of every inherited apparatus theorem.

## Source identity, reads and exposure

The complete changed source reviewed is `common_product_local_matrix_robustness/PROPOSAL.md`, SHA256 `f9e427ccd5ec0a25f0c28639f9707728489a7a7dcca139e6f9fe03289d9b8a20`, under N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. All eight sections were read, including the replacement hypotheses, examples, scalar convention, finite-horizon transfer and qualifications. The hash was verified against the assignment.

The integrated nominal note `common_product_single_control_publication/NOTE.md`, SHA256 `02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde`, and scalar precursor check `common_product_single_control_robustness_check/REVIEW.md`, SHA256 `0995e9e58fc7aa93fe27a3892e9615be7f3fd72fb6c989709dcb0a84105549e1`, were read completely for this task.

Unchanged nominal source and check pins were refreshed:

- Single-control source `76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01`; its review `549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0`.
- Logarithmic policy source `7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8`; its review `d1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3`.
- Scalar precursor source `3218676f11bbc39ecfcf3c84a568a2ffc8107a7b303f349195394a338b2b0623`.

I reuse my earlier complete readings/checks of the single-control and logarithmic arguments and their finite, flag, narrow-cutoff and staged-core ancestry at their unchanged scopes. I authored some earlier core/component work and the single-control/logarithmic checks. The scalar precursor check is additional supplied evidence, not independence for the new extension. ROOT supplied the replacement-class design and cap idea to the author, and these were exposed to me in the assignment/source. I independently reconstructed the new support lemma, examples, cap and transfer below; I make no blanket independence claim. The model and effort were unchanged. No numerical physics computation was needed.

## 1. Support lemma on the actual fiber

Let Q_l be the local head-vacuum projector, tensor identity on every local program/record state. The hypotheses imply A'_l Q_l=0; self-adjointness also gives Q_l A'_l=0. The nominal remainder has both properties. For a global state with precisely one head outside S_l, Q_l acts as identity on the local factor. Therefore E_l annihilates this entire subspace, including arbitrary entanglement with P, R and an external reference. Its reverse matrix elements vanish as well. Head-number conservation makes the global one-head space reducing. Consequently E_l=Pi_l E_l Pi_l on that space.

This remains true when an occupied mediator rotates P or an occupied terminal rotates R. A shared fiber qubit is not a possible head position. In particular no simultaneous diagonalization in P or X_R was used. Positivity is not necessary for this operator lemma, but is independently required to make each replacement a permitted positive block.

Restriction and tensoring with a passive reference preserve the full local norm bound. Thus, for any vector psi,

    |<psi,E_l psi>| <= delta w_l ||Pi_l psi||^2.

Summing these absolute quadratic forms gives delta times the diagonal head-position operator with weights sum_(l:v in S_l) w_l. Its norm is L_head. Self-adjointness then yields ||Delta K||<=delta L_head. Noncommuting fiber errors cannot defeat this argument. There is no factor for the number of rays, fiber dimensions, listed blocks or ray length. The same argument extends to vacuum plus one head, but not to arbitrary extensive head occupation.

Conditions excluding nonscalar fiber action on local vacuum are essential: a fiber-only term on that vacuum would not be compressed by Pi_l. The source correctly excludes such terms rather than calling their relative phases scalar. Local head conservation and fixed supports are also actual hypotheses, not conclusions from small norm.

## 2. Actual norms, scalar and loads

The eight core and eight writer vacancy scalars sum to c=8b+8(sqrt(2)-1)j. Every other listed block has vacuum scalar zero, so no length-extensive scalar is introduced. Condition 4 gives |Delta c|<=delta c even if the individual vacancy scalar shifts have adversarial signs. Vacancy remainders are -c_l n_v, of norm w_l=c_l.

The combined source is correctly counted by its full norm 3j: the double-head eigenvalue is 3j, while the larger one-head eigenvalue of [[j,-gamma],[-gamma,2j]] is (3j+sqrt(j^2+4gamma^2))/2 <=(3+sqrt(5))j/2<3j. Vacuum is zero. Thus using the one-head eigenvalue instead would undercount this physical block, but the source does not do so.

At a mediator the two 2b bonds plus the D1-2b controlled occupation give D1+2b. At a core endpoint the two 2b bonds, two b vacancies, 2j occupation and adjoining 2j ray/cable bond give 6b+4j. The inherited writer inventory bounds head loads by (4+sqrt(2))j; source/ray/cap loads are bounded by 5j, including the combined source. With j<=b/8 and D1>16b, all these are below D1+2b. Thus L_head is exactly D1+2b, as claimed.

The shared-P load 4(D1-2b) must still enter the physical all-qubit cap. Omitting it from L_head is legitimate because that constant is a different, head-position weighted operator bound. The P errors have already been charged in the norm of each head-conditioned block. Likewise the shared-record load is 8j for the physical cap; it is not an extra factor in the support lemma. Counts 126+4ell qubits and 164+4ell listed positive blocks are inherited unchanged because neither supports nor inventory are altered.

## 3. Membership examples and limitations

Scalar rescaling h'_l=(1+theta_l)h_l is contained in the class: choose c'_l=(1+theta_l)c_l, A'_l=(1+theta_l)A_l and use ||A_l||=w_l. Positivity follows from 1+theta_l>=1/2. The new result does not add its error a second time to the scalar theorem.

For the displayed two-head bond domain, both one-head diagonal entries are positive and

    (1+a)(1+d)-(1-k)^2 = a+d+ad+2k-k^2 >=0.

The double-head energy 2+r is at least 1, and vacuum is zero. These checks cover the complete four-dimensional support. The difference in the one-head sector is j[[a,k],[k,d]]. Its absolute row-sum norm is at most 2delta j, which bounds the spectral norm for this symmetric matrix; the other nonzero difference eigenvalue has magnitude |r|j<=2delta j. Since ||Q_j||=2j, the required full-support allowance follows. The independent parameter domain is genuine and need not retain the original onsite/hopping correlation. It is deliberately one-sided. An uncompensated negative diagonal change has negative expectation in the original symmetric zero mode, so a symmetric unrestricted entrywise box would be false.

For real orthogonal conjugation, OBO^T-B=(O-I)BO^T+B(O^T-I), so its norm is at most 2||B||||O-I||<=2||B||||s||. Orthogonal conjugation preserves full positivity and head conditioning. With |s|<=delta/2 this is admissible. For unequal diagonal mediator eigenvalues it generally introduces P off-diagonal entries. Conjugation of j(I+X_R) generally changes the X_R axis and breaks X_R conservation. These are real, same-support matrices; neither example assumes a favorable fiber eigenstate. Their interpretation as supplied allowed matrices, rather than a derived native mechanism, is necessary and explicitly retained.

## 4. Full-space cap and fixed nominal phase

For every block c_l<=w_l, including the zero-scalar cases. Hence ||h'_l-h_l||<=delta(w_l+c_l)<=2delta w_l and ||h'_l||<=(1+2delta)w_l. Applying this separately at every physical qubit preserves the all-qubit cap because the nominal maximum is strictly below Lambda/2 and delta<=1/2. The nominal maximum includes P. No selected one-head expectation is used to justify this physical cap.

Using D1=Lambda/8, b<Lambda/128 and j<Lambda/1024 gives

    L_head+c = D1+10b+8(sqrt(2)-1)j
             < (25+sqrt(2))Lambda/128 < Lambda/4.

Duhamel on the reducing one-head space gives delta L_head |t| for the scalar-subtracted propagators, capped by 2. Restoring c and c' adds precisely |exp(-i Delta c t)-1|=2|sin(Delta c t/2)| when comparing at the nominal phase. The resulting bound is at most min{2,delta(L_head+c)|t|}. This derivation is valid for arbitrary P/R states and passive references. Program-relative rotations or phases remain in Delta K; they cannot be removed by the common scalar. No perturbed scattering, spectral completeness or matching theorem is being assumed.

## 5. Nominal-target and entire-horizon transfer

The integrated nominal premise at tau=epsilon/2 gives normalized full-output error below 3epsilon/16 and the same unnormalized branch-target error below epsilon/4. Its normalized final comparator exists on [3ell/(4j),7ell/(8j)] and retains P, common packet/phase, blank remaining heads and record 1. The whole-horizon target uses the original -i phase and n+ell+57 exponent on F sites 1 through ell. These definitions are not recalibrated after replacing the Hamiltonian.

For delta<=min{1/2,epsilon/(Lambda T)}, the nominal-phase evolution error is strictly below epsilon/4 for all 0<=t<=T. Triangle inequality therefore gives final full-vector error below 7epsilon/16. The two final maps are isometries, so their unhalved diamond discrepancy is below twice this value, namely 7epsilon/8. The complement of joint retained-F/record-1 support annihilates the normalized target, yielding failure probability below (7epsilon/16)^2. Record-1 alone has at least that joint probability.

For the entire horizon, left multiplication by the fixed record projector contracts the evolution difference regardless of whether that projector commutes with H'. Adding it to the nominal branch estimate gives error below epsilon/2 against exactly the same unnormalized V_nom(t). Both maps are contractions: the physical branch is a projection of an isometry, and the nominal truncated packet has norm at most one. The standard two-term expansion of AXA* - BXB* therefore bounds the unhalved subnormalized diamond distance by 2||A-B||<epsilon, including references. No normalization by success probability is valid or used. A changed final P state is charged rather than discarded. This proves the asserted contract without preserving P or X_R.

The window has unchanged relative width 1/6. Since the unchanged nominal logarithmic recipe has ell=Theta(epsilon^(-11/2)) and T=Theta(Lambda^(-1)epsilon^(-15/2)), the selected safe delta is Theta(epsilon^(17/2)). This is a sufficient relative full-remainder norm allowance, together with separate scalar and structural membership requirements. It is not an independently adjustable symmetric entrywise precision, a bound on preparation error, or a fabrication-resource theorem. No new resource exponent beyond this direct tolerance consequence is inferred.

## Conclusion and verification limits

The new extension survives the requested adversarial checks. The decisive support statement remains valid on the complete one-head/program/record/reference space even when local matrices rotate the program or record. The explicit positive domain, vacancy scalar accounting, actual head versus all-qubit loads, cap reserve and both fixed-target contracts are consistent. No source correction is requested.

This supports only the static, same-support, positive, head-conserving, scalar-vacuum matrix class with its stated full-support norm budgets. It does not establish unrestricted entrywise errors, extra supports, head-changing noise, nontrivial vacuum fiber evolution, native block supply, indefinite flag behavior, normalized rare-success fidelity, permanent halt or transfer to the old literal processor. The finite-horizon conclusions remain conditional on the pinned nominal theorem and supplied initial state. Only this review file was created; no source, W, Git, checkpoint, axiom, editable prompt or model setting was changed, and no delegation or publication was performed.
