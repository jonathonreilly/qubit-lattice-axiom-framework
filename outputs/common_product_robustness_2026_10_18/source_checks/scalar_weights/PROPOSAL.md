# Independent listed-block weight errors in the finite one-control router

New bounded author derivation requiring a distinct check. For the supplied finite one-control device, independent real multiplicative errors in its listed positive blocks have a one-head generator-error bound with no factor proportional to the number of blocks or ray length. The bound retains the full program/record/reference fiber and separates the actual common scalar phase. It gives an explicit sufficient weight tolerance for complete final output and the absolute flagged branch throughout the finite horizon. This is a restricted coefficient-robustness result, not a native supplier, arbitrary entrywise-error theorem or practical manufacturing certificate.

ROOT proposed splitting the vacancies and using head-occupancy quadratic forms. The reconstruction below adopts that design exposure, checks all block types, and retains both nominal and shifted-phase comparisons. No scientific executable or numerical disorder experiment is used. Existing sources are unchanged.

## 1. Perturbation model and invariant domain

Fix any nominal finite one-control record device from source76b5 with its explicit positive inventory:24 core blocks with eight separate vacancies,68 writer blocks,68 cable bonds, two compensated I sources at M=ell+1, and two F caps at ell. Its total is164+4ell listed blocks and126+4ell qubits. Use the combined source block convention of the source and the combined mediator/program projector block convention. Let

    H=sum_l h_l,
    H'=sum_l (1+theta_l) h_l,
    theta_l real, |theta_l|<=delta<1.                     (1)

The bounds are uniform over all choices of the theta_l, including different signs and adversarial correlations. The word independent means that each listed block may have its own value; no probabilistic distribution or cancellation is assumed. The factors1+theta_l are positive, so positivity and locality of every physical block are preserved.

Only the weight of each ENTIRE h_l changes. For example a mediator block retains its two detunings in the same ratio; a Q block retains its diagonal/hopping correlation; a signed writer bond retains its sign; and the combined source block scales its weak hopping and both occupations together. Different blocks may nevertheless cease to satisfy their nominal mutual tuning. Source/lead diagonal matching and nominal scattering identities are not presumed true for H'. Their failure is paid by the perturbation bound.

No extra couplings, independent matrix-entry errors, head creation/annihilation, program-axis rotations, record free Hamiltonian, or errors in the supplied initial state are included. Splitting a combined block into separate independently perturbed terms defines a different error model and needs its own load accounting.

Every h_l commutes with total head number. Thus both H and H' preserve the finite one-head Hilbert space

    H_1=ell²(head sites) tensor C²_P tensor C²_R,

with any passive reference tensored afterward. P is the single ordinary program qubit and R is the one shared record; they are not included in the head count. All program and record states are included in H_1. In particular the analysis does not treat an occupied P or R as a second moving head. Performance will retain the parent's blank-record seed premise, but the perturbation operator estimate needs no blank-record restriction.

## 2. Separate every vacancy scalar exactly

There are eight core vacancy terms b(I-n_v), including two separately listed at each core endpoint, and eight writer junction vacancies d(I-n_v), with d=(sqrt(2)-1)j. Let V_vac be this set of16 blocks and c_l=b or d their coefficient. Every other listed block annihilates head vacuum for every P/R fiber. Hence

    c=sum_(l in V_vac)c_l=8b+8(sqrt(2)-1)j=8b+2c_R,
    Delta c=sum_(l in V_vac)theta_l c_l,
    c'=c+Delta c,
    |Delta c|<=delta c.                                    (2)

These are true scalars on the full finite physical Hilbert space, not scalars conditional on program, record or head position. In particular H and H' on head vacuum are cI and c'I on the entire P/R fiber.

Define A_l=h_l for nonvacancy blocks and A_l=-c_l n_v for a vacancy at v. Then exactly

    H=cI+K, H'=c'I+K',
    K=sum_l A_l, K'=sum_l (1+theta_l)A_l,
    Delta K=K'-K=sum_l theta_l A_l.                       (3)

There is no approximation in this expansion. A_l for a vacancy is negative; its sign will be bounded by an absolute quadratic form, not mistakenly treated as positive. Its norm remains c_l=||h_l||. The fixed number of vacancies makes c independent of ell. Even a norm bound on their unremoved scalar sum therefore has no ray-length factor in this architecture.

## 3. Local head support with arbitrary program and record coherence

For each listed block let S_l be its set of head sites, excluding P and R. On H_1 set

    Pi_l=sum_(v in S_l)|v><v| tensor I_(P,R).

This is a projection because there is exactly one head. For every listed block,

    A_l=Pi_l A_l Pi_l,
    |<psi,A_l psi>|<=w_l <psi,Pi_l psi>,
    w_l=||h_l||,                                          (4)

for every psi in H_1. The full-support block norm w_l is an upper bound on its one-head restriction. Here is a check of each type rather than an assumption about sparse matrix rows:

- An ordinary or signed head bond |a|(n_x+n_y)+a(a_x^dagger a_y+a_y^dagger a_x) conserves head number and vanishes when both local heads are vacant. It acts only on the two head positions x,y in H_1. Its full norm is2|a|, including double occupation.
- An onsite occupation c_l n_v has support projection |v><v| and norm c_l. A subtracted vacancy -c_l n_v has the same support and absolute norm.
- A mediator/program block [(D0-2b)P0+(D1-2b)P1]n_m, or its reversed version, has S_l={m} and norm D1-2b. Its fiber operator is retained in full. Sharing P across four blocks does not enlarge the head support of any of them.
- A writer terminal block j n_T(I+X_R) has S_l={T}, norm2j and vanishes at unoccupied T for EVERY record state. Sharing R between four terminals does not produce a record-only vacuum drive.
- The combined source block B=Q_gamma(x,y)+(j-gamma)n_x+(2j-gamma)n_y, 0<gamma<=j, has S_l={x,y}. Its local vacuum energy is0 and double-occupation energy3j. Its one-head matrix is[[j,-gamma],[-gamma,2j]], with top eigenvalue(3j+sqrt(j²+4gamma²))/2<=3j. It is positive and has full norm3j. Thus the combined block, including its correlations, satisfies(4) without decomposing its weight.
- Positive phase-cell occupations, endpoint occupations and F caps are covered by the onsite case. The signed junction bonds and strengthened phase bonds are covered by the signed-bond case. There are no other program/record-only terms in the stated inventory.

The support identity in(4) follows either from these explicit forms or from local head-number conservation plus vanishing on the local head vacuum. It remains true after arbitrary passive-reference extension. Positivity is sufficient for the nonvacancy form inequality; the ordinary self-adjoint norm inequality covers the negative vacancy remainder.

Define the nominal maximum HEAD incident load

    L_head=max_(head site v) sum_(l:v in S_l) w_l.          (5)

For arbitrary psi, equations(3)--(4) give

    |<psi,Delta K psi>|
       <=delta sum_l w_l <psi,Pi_l psi>
       =delta sum_v [sum_(l:v in S_l)w_l]
                                  ||(<v| tensor I)psi||²
       <=delta L_head ||psi||².

Delta K is self-adjoint, so its operator norm equals its supremum absolute unit quadratic form. Therefore

    ||Delta K||_(H_1 tensor ref)<=delta L_head.            (6)

No commutation of overlapping blocks is needed. No factor counting P/R sectors, head sites, sources or rays occurs. In particular four shared-P blocks contribute at four distinct head positions; treating P as a moving-head coordinate in a degree bound would be incorrect. The same inequality holds for vacuum-plus-one-head, since all A_l vanish on head vacuum, but no length-independent bound on arbitrary extensive head occupation is claimed.

For a generic incident cap Lambda, (5) is at most Lambda, giving ROOT's proposed ceiling delta Lambda. In this concrete parameter domain one can keep a sharper explicit value. The head loads are bounded by

    D1+2b at mediators; 6b+4j at core endpoints;
    (4+sqrt(2))j at phase endpoints; (1+3sqrt(2))j at junctions;
    5j at source-adjacent sites; 3j at emitters/caps; 4j elsewhere.

For eta=b/D0<=1/8 and zeta=D0/D1<1/2, j=eta b<=b/8 and D1>16b. Every listed nonmediator load is below D1+2b. Each mediator has exactly that full incident sum, so the definition(5) gives

    L_head=D1+2b.                                         (7)

This is a statement about the chosen full-norm load ceiling, not an assertion that the actual perturbation attains it.

## 4. Complete evolution error, with both phase conventions

On the invariant H_1, Duhamel with the full perturbed and nominal unitaries gives for every real t

    ||exp(-itK')-exp(-itK)||
          <=min{2,delta L_head |t|}.                      (8)

This pays all perturbed spectral components without a scattering approximation or a claim that disordered bound states are absent. The dimension of the apparatus never enters. It is uniform on the entire input fiber and extends to passive references.

If the mathematical comparator uses the ACTUAL common vacuum phase exp(-ic't), its difference from the perturbed evolution has only the addition in(8) to any nominal complete-output error. Equivalently

    ||exp(-itH')-exp(-it Delta c)exp(-itH)||
                 <=min{2,delta L_head |t|}.               (9)

This is a useful phase-aware statement but not permission to silently fit a phase. If weights are unknown and the target keeps the originally prescribed phase exp(-ict), retain the exact extra scalar error:

    ||exp(-itH')-exp(-itH)||
      <=min{2,delta L_head |t|+2|sin(Delta c t/2)|}
      <=min{2,delta(L_head+c)|t|}.                        (10)

Thus even the fixed-nominal-phase vector error has no length factor. The norm2 cap follows because both evolutions are unitaries. For output density channels the common scalar cancels identically, so(9) suffices even without a phase-calibration operation. Neither observation permits dropping relative program, path or record phases: those are in Delta K and remain paid.

For a nominal seed E and any complete target map T(t), triangle inequality yields

    ||exp(-itH')E-T(t)||
       <=||exp(-itH)E-T(t)||+delta(L_head+c)|t|.           (11)

For the absolute record branch, contract by the fixed mathematical projector P_R1. For any fixed unnormalized nominal branch target V(t),

    ||P_R1 exp(-itH')E-V(t)||
       <=||P_R1 exp(-itH)E-V(t)||+delta(L_head+c)|t|.      (12)

The targets and E in(11)--(12) are exactly the nominal maps; no perturbed wavepacket, normalization or success-conditioned comparator is substituted. These bounds hold at every t where the respective nominal theorem holds. The perturbation evolution estimate itself holds at all real t, but grows with |t| and supplies no indefinite useful accuracy guarantee.

## 5. Positive weights preserve the supplied cap with the available margin

In the one-control prescription D1=Lambda/8, b<Lambda/128, j<Lambda/1024. The nominal full-support incident sum at P is4(D1-2b)<Lambda/2; mediator, endpoint and all other sites have the smaller bounds from76b5. Thus the maximum nominal incident sum over ALL qubits, including P and R, is strictly below Lambda/2.

For the perturbed positive blocks, at every qubit v,

    sum_(l incident v)||(1+theta_l)h_l||
        <=(1+delta)sum_(l incident v)||h_l||<Lambda       (13)

whenever delta<1. No new global energy rescaling or physical-time factor is needed for this perturbation margin. A different nominal design using its full cap would instead require the explicit factor1+delta or a reserve; the margin is specific to the conservative one-control choice.

For the fixed-phase bound there is also the explicit estimate

    L_head+c=D1+10b+8(sqrt(2)-1)j
        <[(25+sqrt(2))/128]Lambda <Lambda/4.             (14)

The first inequality uses the three parameter ceilings above, and sqrt(2)<2 gives the final strict comparison. This is a convenient sufficient constant; no optimal perturbation norm is claimed.

## 6. Explicit retained accuracy, horizon and success

Fix desired0<epsilon<=1 and Lambda>0. Construct the NOMINAL one-control logarithmic-policy device of canonical02b432 and its checked sources76b5/716038 at the tighter nominal parameter

    tau=epsilon/2.

Thus h=eta²=zeta=tau/10^5, D1=Lambda/8, j=Lambda tau²/(8*10^10), and the parent's formulas compute T0, alpha=[4096(1+T0)]^-2, rho=alpha tau sqrt(h), the normalized source g, all derivative/budget constants, u and ell. Retain the actual source/cap blocks and supplied seed. Write

    T=t_plus=7ell/(8j), t_minus=3ell/(4j).

The nominal complete normalized output error is<3tau/8=3epsilon/16 throughout[t_minus,T]. Its absolute unnormalized flag-branch error is<tau/2=epsilon/4 on the ENTIRE[0,T]. These are two separate parent statements, not a branch theorem inferred by normalizing a rare event. All parent denominators and positive target normalizations are unchanged by choosing tau in(0,1/2].

Choose the following sufficient independent relative-weight tolerance:

    0<=delta<=delta_safe=min{1/2,epsilon/(Lambda T)}.      (15)

By(14), delta(L_head+c)T<epsilon/4. (When delta=0 the perturbation is zero.) A less coarse allowable ceiling from the same proof is min{1/2,epsilon/[4T(L_head+c)]}. Either choice retains positivity and (13).

With the original nominal phase and original normalized nominal F target, (11) now gives

    sup_(t_minus<=t<=T)||exp(-itH')E-T_nom(t)||
                  <7epsilon/16<epsilon/2.                (16)

T_nom(t)=exp(-ict)J_F[beta_F(t) tensor C tensor|1>_R] includes the physical P, both logical paths and passive references, with every other head vacant. It is the same common radial beta_F and phase used by the nominal theorem. Actual residual source/internal/record amplitudes remain in the norm. Since actual and target maps are isometries, the unhalved complete output-channel discrepancy is<7epsilon/8<epsilon.

For the entire horizon use the SAME unnormalized nominal target

    V_nom(t)=exp(-ict)J_F[B_fin(t) tensor C tensor|1>_R]

at every t, including before matching. Equation(12) gives

    sup_(0<=t<=T)||P_R1 exp(-itH')E-V_nom(t)||
                         <epsilon/2.                    (17)

Both maps are contractions. The two-term expansion of AZA^*-VZV^* bounds the unhalved subnormalized-channel/diamond discrepancy by twice their operator difference, hence below epsilon, with arbitrary passive references. Ideal branch trace remains the nominal ||B_fin(t)||², independent of logical input. No division by early success probability is made.

On the final window, the normalized target in(16) belongs to record1 and retained F support1<=n<=ell with every other apparatus head vacant. Projection onto the orthogonal complement has actual norm at most7epsilon/16. Therefore both record1 probability and joint record1/retained-F probability are strictly greater than

    1-(7epsilon/16)².                                    (18)

This follows from the complete vector bound, not from the absolute branch bound alone. P is exactly conserved even in H' because every perturbed block remains diagonal in it. The bounds nevertheless retain the full coherent program factor and any relative phase errors. R need not stay blank during transit; incorrect internal flags are included in(17).

## 7. Sufficient accuracy order and its precise meaning

The checked logarithmic nominal family, now evaluated at tau=epsilon/2, has

    ell=Theta(epsilon^(-11/2)),
    T=Theta(Lambda^-1 epsilon^(-15/2)),
    gamma=Theta(Lambda epsilon^(7/2)).

Replacing epsilon by tau changes constants, not powers; the nominal packet coefficients and alpha retain their stated positive finite-limit premises. Hence for sufficiently small epsilon the second branch in(15) is the minimum and

    delta_safe=Theta(epsilon^(17/2)).                    (19)

This is an explicit sufficient relative tolerance for EVERY listed positive block weight, simultaneously. It derives from delta Lambda T being small, with no extra factor ell or164+4ell. Length independence is at the generator-error level: the certified horizon T itself grows with ell, and that duration still tightens the tolerance. It is not a necessary tolerance or a lower bound: the full-support mediator load in(7) is conservative for many actual trajectories, and no improved state-dependent robustness has been proved here.

For the weak source hopping, the particular correlated source-block perturbation changes gamma by theta_source gamma. Thus (15) permits its induced absolute change up to delta_safe gamma, whose sufficient scale is Theta(Lambda epsilon^12) in this family. The source occupations change with the SAME theta_source. This statement is not an independent accuracy allowance for gamma while holding those entries fixed, nor an independent error model for D0,D1,b or the occupation basis. A fabrication mechanism, metrology protocol and cost of achieving these errors remain unspecified. Unlike the parent note's magnitude-only statement, this proposal supplies a narrow mathematical tolerance region, not a general physical coefficient-supply theorem.

The nominal state-preparation errors, unwanted interactions and environmental couplings remain separate. A suitable independently established full-input trace-distance error could be added by contractivity, but correct marginals alone are not such a certificate and none is silently included here. No new resource exponent for the actual perturbed trajectories or performance at unlimited time is claimed.

## 8. Evidence, exposure and decisive check

Paths below are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact sources:

- common_product_single_control_router/PROPOSAL.md:76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, authored/full-read in the preceding coherent task; same inventory and scope reused.
- common_product_single_control_router_check/REVIEW.md:549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0, newly fully read and hash-verified.
- common_product_logarithmic_flag_policy/PROPOSAL.md:7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8, newly fully read and hash-verified.
- common_product_logarithmic_flag_policy_check/REVIEW.md:d1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3, newly fully read and hash-verified.
- common_product_single_control_publication/NOTE.md:02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde, current integrated note newly fully read and hash-verified; publication pending at assignment. It combines the two checked premises and is not additional independent evidence.

Their explicit source/core/writer inventories and finite/flag/packet proofs retain the exact scopes/pins recorded there. The staged corec913, finite728 and flag e7b were fully reread in the immediately preceding one-control task. The present perturbation proof does not reuse an old approximate isolated-cell replacement theorem and does not require a new scattering solution for H'.

ROOT supplied the occupancy/scalar route. This author reconstructed the local support identity for every block type, the full fiber quadratic-form bound, shared-P/shared-R accounting, scalar phase, cap margin, tighter nominal error reserve and sufficient tolerance order after that exposure. This is an author continuation, not independent verification; earlier component checks do not certify the new robustness argument.

The decisive new independent check is equation(6) for the ACTUAL listed inventory on the whole one-head/program/record space. A reviewer should independently decompose the weighted vacancies, verify that no remaining block acts when all its head sites are vacant, verify the combined-source norm and both shared fibers, and reconstruct the weighted occupation sum. It should then challenge the fixed nominal phase in(10), all-qubit cap in(13), and the simultaneous output/flag/probability budget at nominal tau=epsilon/2. A head-free fiber term or an omitted vacancy scalar would invalidate the stated proof and must be reported rather than folded into a favorable row-degree count.

The result is conditional on this static supplied block inventory and restricted perturbation class. It gives no native Hamiltonian/Record, readout or initialization supplier, old literal processor transfer, arbitrary-time normalized herald, permanent halt, irreversible latch, capture/reset or indefinite finite storage. Only common_product_single_control_robustness/PROPOSAL.md was created. No parent source, W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, numerical simulation/sweep, publication or delegation occurred. Author algebra and file/hash bookkeeping are the verification methods; distinct review is pending and no retained status is assigned.
