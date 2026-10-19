# Occupation-sector bounds for a common-product program chain

Author claim: a conditional bounded theorem for the vacuum-plus-one-head input sector of a supplied finite program chain. At fixed local coefficients and comparison horizon, its full-output error bound is independent of the number of cells. Physical resources still grow with chain length. No traversal fidelity, arrival time, native interaction law or arbitrary-occupation processor theorem follows.

Claim type: bounded_theorem.

This note is an addition to the [common-product program chain](COMMON_PRODUCT_PROGRAM_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-18.md), which supplies the physical geometry and full-occupation comparison. The new sector proof (`outputs/common_product_program_2026_10_18/proofs/common_product_sector_transport__PROPOSAL.md`) and distinct analytical check (`outputs/common_product_program_2026_10_18/proofs/common_product_sector_transport_check__REVIEW.md`) support the restricted result below. Publication integration and its exposure limits are recorded in the evidence packet.

## Supplied chain and exact input domain

For N>=1, cell i has head qubits u_i=(3i-1,0,0), m_i=(3i,0,0), v_i=(3i+1,0,0), and three program qubits one unit above them. Cells share no qubits. Each cell has the positive six-qubit Hamiltonian and common literal injection of the [isolated-cell note](COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md), with

    b_i>0,  D1_i>D0_i>2b_i,  a_i=2b_i^2/D0_i.

Add Q_(c_i)(v_i,u_(i+1)) for i=1,...,N-1, where c_i>=0 and

    Q_c(x,y)=c[n_x+n_y-(X_x X_y+Y_x Y_y)/2].

This full qubit block is positive, has norm 2c, and has double-occupation energy 2c. The chain uses 6N qubits and 8N-1 positive blocks under the parent's combined mediator/program-block convention. Missing interactions, including adjacent program-row couplings, are supplied absences. Local roles, occupation frames and exact coefficient correlations are assumptions.

Each legal program triple is |000> or |111>. Arbitrary coherent superpositions of these legal choices, including entanglement between cells and with the head or passive references, are allowed. Their physical preparation and Record interpretation remain supplied.

The logical endpoint domain is restricted to total head number

    N_log=sum_i(n_Li+n_Ri)=1,

or its direct sum with N_log=0. Denote the latter domain by H_le1. A head may be coherently delocalized over all endpoints. Multiple endpoint heads are excluded. The common literal injection J inserts a vacant mediator in every cell and the redundant program encoding. No dressed-state preparation, measurement or postselection is required.

The physical and logical Hamiltonians are

    H_net=sum_i H_i+Kphys,
    Kphys=sum_i Q_(c_i)(v_i,u_(i+1)),
    A_net=C I+sum_i P0_i a_i Rminus_i+Klog,
    Klog=sum_i Q_(c_i)(R_i,L_(i+1)),  C=2sum_i b_i,
    X_h,LiRi=(X_Li X_Ri+Y_Li Y_Ri)/2,
    Rminus_i=(n_Li+n_Ri-X_h,LiRi)/2.

All terms conserve total head number and every program occupation. Thus their respective vacuum-plus-one-head sectors are invariant. The scalar C is the actual common scalar on every legal program and both allowed head numbers; exp(-itC) remains in the comparator. The target is exp(-it A_net), including its generally noncommuting adjacent terms, rather than a product of isolated gates.

## Restricted distance and full-output theorem

Define

    epsilon_i=4b_i^2/[sqrt(D1_i^2+8b_i^2)+D1_i],
    r0_i=sqrt(2)b_i/D0_i,
    r1_i=sqrt(2)b_i/(D1_i+epsilon_i),
    alpha_(p,i)=(1+r_(p,i)^2)^(-1/2),
    kappa_1=max_i sqrt(2-2alpha_(0,i)),
    epsilon_max=max_i epsilon_i,  c_max=max_i c_i,

with c_max=0 for N=1. For every real t,

    ||[exp(-it H_net)J-J exp(-it A_net)]|H_le1||
      <=min{2, 2kappa_1+|t|(epsilon_max+4c_max kappa_1)}.   (1)

Every physical output, including mediator occupation, is retained. The literal mediator-vacancy subspace need not remain invariant. Tensoring any passive reference preserves the estimate; the associated unhalved trace/channel distance on this restricted input domain is at most twice the right side. This is not a channel bound for arbitrary multiple-head inputs.

Here is the mechanism behind the absence of N in (1). Let Jd be the tensor of the parent's exact controlled dressed isometries. Both J and Jd preserve head number. On a fixed program sector, the one-head input space is an orthogonal direct sum indexed by its occupied cell. Other cells are exactly in head vacuum, where J and Jd coincide. The overlap J*Jd therefore has eigenvalues alpha_(p,i),1 on the occupied-cell summands, and eigenvalue 1 on vacuum. Since r1_i<r0_i,

    ||(Jd-J)|H_le1||=sqrt(2-2min_i alpha_(0,i))=kappa_1
                    <=max_i r0_i.                         (2)

Coherent programs give a maximum over orthogonal sectors, not a sum. This differs from the full tensor-domain distance involving product_i alpha_(0,i).

The exact dressed cell intertwiner is

    (sum_i H_i)Jd=Jd(A_cell-E),
    A_cell=C I+sum_i P0_i a_i Rminus_i,
    E=sum_i epsilon_i P1_i Rplus_i,
    Rplus_i=(n_Li+n_Ri+X_h,LiRi)/2.

On H_le1 the nonzero supports of P1_i Rplus_i are orthogonal across occupied cells, so ||E|H_le1||=epsilon_max. The external endpoint bonds form a matching: each endpoint occurs in at most one external bond. On the physical one-head space their sum is a direct sum of c_i[[1,-1],[-1,1]] blocks and zero coordinates, hence has norm 2c_max; the logical norm is the same. The degree-one diagonal contributions are included.

Exact literal intertwining Kphys J=J Klog gives

    Kphys Jd-Jd Klog=Kphys(Jd-J)-(Jd-J)Klog.

The maps on each side preserve the required occupation sectors, so its restricted norm is at most 4c_max kappa_1. The complete rectangular defect is bounded by epsilon_max+4c_max kappa_1. Rectangular Duhamel and two endpoint replacements of Jd by J prove (1). This does not assume that attachment preserves the dressed code or commutes with the logical cell generator.

If all programs are further fixed to enabled |000>, E vanishes and epsilon_max may be omitted. Arbitrary legal program superpositions require that term. More generally, an actually supplied endpoint graph with maximum weighted degree d_max has one-head Laplacian norm at most 2d_max, by sum c_xy|psi_x-psi_y|^2<=2d_max||psi||^2. If physical/logical graph copies and exact literal intertwining are established, 4c_max can be replaced by 4d_max. This conditional norm observation supplies no arbitrary graph embedding or compiler.

## One bounded-load family and its comparison horizon

For identical cells with c_i=z a and z>=0, set r=sqrt(2)b/D0 and a=2b^2/D0. At T_gate=pi/a, equation (1) implies throughout |t|<=T_gate

    error<=min{2,2kappa_1(1+2pi z)+pi epsilon/a}
         <=min{2,2r(1+2pi z)+pi D0/D1}.                    (3)

The second capped comparison is weak: even a strict uncapped improvement need not remain strict after a cap of 2.

A symbolic sufficient family, with no numerical operating point selected, is

    Lambda>0, 0<eta<=1, z>=0,
    L=1+2pi z, R=16pi/eta,
    D1=Lambda/2, D0=D1/R,
    r=eta/(16L), b=rD0/sqrt(2), a=r^2 D0, c_i=z a.

It satisfies the exact coefficient relation and D1>D0>2b. Actual incident block-norm loads are D1+2b on mediators and at most 3b+a+2za on endpoints. The mediator load is below Lambda. Dividing the endpoint load by D0 gives 3r/sqrt(2)+(1+2z)r^2<1, since r<=1/(16L) and 2z<L/pi. Program loads a and D1-2b are also below Lambda. External bonds are therefore included in the physical cap, not charged only at their effective logical scale.

The two terms of the uncapped error envelope are eta/8 and strictly less than eta/16. Consequently the complete error is strictly below 3eta/16 throughout

    |t|<=T_gate=8192pi^2 L^2/(Lambda eta^3).               (4)

These supplied coefficients need not vary with N for this restricted-domain horizon and accuracy. Resources still grow with N, and (4) is not a traversal time. At longer requested times the residual in (1) must be reevaluated; different local parameters may be needed. No optimality, physical resource superiority or native precision mechanism is claimed.

## Exact uniform path and its boundaries

When every cell is enabled and c_i=a/2, both internal and external logical edges have weight a/2. In the ordered endpoint basis L1,R1,L2,R2,...,LN,RN,

    A_net|onehead=C I+(a/2)L_path(2N).                    (5)

The combinatorial path Laplacian has offdiagonal -1 between consecutive vertices, diagonal 1 at the two endpoints and diagonal 2 at interior vertices. For N=1 both diagonal entries are 1. There is no extra end cap; adding an endpoint onsite a/2 would change the target boundary condition.

The exact relative energies are

    E_k=a[1-cos(pi k/(2N))],  k=0,...,2N-1.

The k=0 mode is constant, normalized by 1/sqrt(2N). For k>0 the normalized modes are cos[pi k(ell-1/2)/(2N)]/sqrt(N). The interior difference equation and degree-one endpoints give these eigenvalues: the right endpoint is equivalent to the ghost relation f_(2N+1)=f_(2N), satisfied by these discrete angles. Thus the target is an autonomous continuous-time path evolution with the retained phase exp(-itC).

Classically disabled cells remove their internal logical edges while external edges remain, giving the weighted broken-path Laplacian. Coherent legal programs give a controlled direct sum of these evolutions with the same C. The actual physical disabled residual remains covered by (1). None of these spectral identifications establishes directed transport, high-fidelity endpoint arrival, perfect transfer or a read time. The prior emitted-packet apparatus is not automatically an input/output interface for this path.

## Evidence and limits

The exact new source is `common_product_sector_transport/PROPOSAL.md`, SHA256 `a94697cf9dd3c0b62a38b97a3cc64640b7d3eac41d48f625e1595ec7d857dd76`. Its distinct check is `common_product_sector_transport_check/REVIEW.md`, SHA256 `feb55d2719b8eda3eff7c8547497b23be2fae7b89ff1e6c5a91f53833e3c8272`.

The direct parent chain argument is `1d830ee1638794876d2a5062f436be9e32b484fef0c79de095aa54d16c0e5edc`, with check `4e6e229f5cbc92321f72bf71289ed8f911c7663773e3731fa0ab54997f22db77`. The single-cell identities are source `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088` and check `809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6`, reused only within their stated scopes.

ROOT suggested examining occupation-sector norms and the uniform path. The sector author had authored the base cell and attachment and checked ROOT's chain. The distinct sector reviewer had checked the base cell and attachment and has shared positive-block ancestry; the new sector residual, loads and path boundaries were reconstructed explicitly. This publication synthesis is by that reviewer and is not an additional independent check. ROOT read the full source, check and synthesis and added the explicit definitions of X_h and A_cell already used in the proof. This integration is source-exposed; no audit or retained status is assigned here.

The theorem assumes correct joint preparation in H_le1, legal program content, the exact literal injection, supplied Hamiltonians and absent interactions. Correct local marginals alone do not establish the joint sector condition. Multiple-head sources, arbitrary processor encodings, overlapping cells, native Record formation, compiler correctness, capture/reset, repeated monitoring and finite permanent halt need separate proofs. The full-occupation chain theorem remains distinct and unchanged. No scientific program or new numerical performance result is introduced; publication copy and link verification are separate mechanical work.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
