# Occupation-sector sharpening for the common-product program chain

New author derivation requiring a distinct check. On the vacuum-plus-one-head logical sector, the common literal program chain has a code-distance and finite-time simulation bound independent of the number of cells, at fixed local parameters and horizon. The full-occupation theorem remains different: the sector restriction cannot be silently transferred to an arbitrary processor input.

ROOT suggested examining the number-conserving XY structure and whether the one-head norm removes the chain-length losses. This was a proposed route, not evidence. The result below follows from the exact controlled single-cell intertwiners and the disjoint physical endpoint attachments, with all physical outputs and phases retained.

## 1. Supplied model and explicit restricted domain

Use N disjoint six-qubit cells at the coordinates and with the positive Hamiltonians of network1d830ee1. Cell i has coefficients b_i,D0_i,D1_i,a_i=2b_i²/D0_i, with D1_i>D0_i>2b_i. Connect v_i to u_(i+1) by the positive Q_(c_i) bond, c_i>=0. All program bits are conserved. Each cell's legal program space is spanned by000 and111; arbitrary coherent superpositions and entanglement between these legal programs are allowed mathematically. Their preparation and interpretation as physical Records remain supplied premises.

Let the logical head number be

    N_log=sum_i(n_Li+n_Ri).

Restrict the input domain to N_log=1, or to the direct sum N_log=0 and1. Include every legal program state and any passive reference without restriction. Denote this domain by H_le1. It allows a head delocalized coherently over every endpoint, entangled with the programs/reference. It does not allow arbitrary multiple endpoint occupation.

The literal injection J tensors each cell with a vacant mediator and the redundant physical program encoding. The auxiliary controlled dressed injection Jd is that of739e99c4, tensored over cells. Both preserve total head number exactly, so J and Jd map H_le1 into the actual physical vacuum-plus-one-head space. The full physical Hamiltonian and the logical target conserve head number, so this restricted domain remains valid under their respective evolutions. No projection, measurement or postselection is imposed during evolution.

Write

    A_net=C I+sum_i P0_i a_i Rminus_i+Klog,
    C=2sum_i b_i,
    Klog=sum_(i=1)^(N-1) Q_(c_i)(R_i,L_(i+1)),
    H_net=sum_i H_i+Kphys,
    Kphys=sum_(i=1)^(N-1) Q_(c_i)(v_i,u_(i+1)).

C is the true common scalar on every legal program and both allowed head numbers; retain exp(-itC) in the comparator. In particular a superposition with the vacuum does not justify dropping any head-number-dependent potential. Each Rminus is the full single-cell projector, but the following norm improvements are only on H_le1. Noncommuting adjacent logical terms are kept inside exp(-it A_net).

## 2. Exact restricted code distance

For each cell/program let

    epsilon_i=4b_i²/[sqrt(D1_i²+8b_i²)+D1_i],
    r0_i=sqrt(2)b_i/D0_i,
    r1_i=sqrt(2)b_i/(D1_i+epsilon_i),
    alpha_(p,i)=(1+r_(p,i)²)^(-1/2).

Then r1_i<r0_i and alpha_(1,i)>alpha_(0,i). On a fixed program sector, the one-head logical space is an ORTHOGONAL DIRECT SUM of the occupied-cell subspaces. Other cells are exactly in their head vacuum, on which J_i=Jd_i and their overlap is1. In the occupied cell the overlap in symmetric/antisymmetric coordinates has eigenvalues alpha_(p,i),1. Thus on H_le1,

    J*Jd >= alpha_min I,
    alpha_min=min_i alpha_(0,i),
    kappa_1=||(Jd-J)|H_le1||=sqrt(2-2alpha_min)
               =max_i sqrt(2-2alpha_(0,i))<=r_max,
    r_max=max_i r0_i.                                  (1)

The equality follows from (Jd-J)*(Jd-J)=2I-Jd*J-J*Jd and is attained in an enabled symmetric one-head cell of least alpha. The vacuum adds an eigenvalue1 to the overlap and does not change the norm. Coherent programs are a direct sum of conserved physical sectors, so they give the same maximum, not a sum or square root of the number of sectors. Tensoring a passive reference does not change the operator norm.

This differs from the full tensor-domain distance sqrt(2-2product_i alpha_(0,i)). In that domain many cells can be occupied simultaneously. Equation(1) does not claim a new full-occupation bound.

## 3. Restricted attachment and cell residual norms

On H_le1 the exact dressed intertwiner is

    (sum H_i)Jd=Jd[A_cell-E],
    E=sum_i epsilon_i P1_i Rplus_i,
    A_cell=C I+sum_i P0_i a_i Rminus_i.

Each P1_i Rplus_i annihilates the vacuum and all one-head components occupied in another cell. These projectors have orthogonal ranges on the restricted domain; their norm-weighted sum therefore satisfies

    ||E|H_le1||=epsilon_max=max_i epsilon_i.             (2)

This is not the full-domain sum of residual coefficients. All nonzero signs, the antisymmetric zero mode and the physical vacuum scalar remain as in the exact cell proof.

For the external bonds, every endpoint occurs in at most ONE such bond. In the physical one-head space Kphys is an orthogonal direct sum of matrices c_i[[1,-1],[-1,1]] on pairs(v_i,u_(i+1)), and zeros on other endpoints and mediators. It annihilates vacuum and is identity on programs. Hence

    ||Kphys|physical_le1||=2c_max,
    ||Klog|H_le1||=2c_max,
    c_max=max_i c_i,                                  (3)

with c_max=0 for N=1. This is a restricted operator norm, not the full tensor norm of a sum of bonds. It keeps the degree-one diagonal contributions of the Q blocks. No cancellation between distinct positive terms is assumed.

The literal intertwiner Kphys J=J Klog holds on the full domain. Subtract it from the dressed product and restrict:

 Kphys Jd-Jd Klog
       =Kphys(Jd-J)-(Jd-J)Klog.

Both Jd-J and Klog preserve the permitted head sector. Applying (1),(3) in their correct domains gives

    ||(Kphys Jd-Jd Klog)|H_le1||<=4c_max kappa_1.       (4)

Thus the entire restricted rectangular residual is

    ||(H_net Jd-Jd A_net)|H_le1||
                     <=epsilon_max+4c_max kappa_1.    (5)

This proves independence of N from the actual disjoint-edge structure. It does not assume the dressed code is invariant under attachment, commute an attachment through the logical cell Hamiltonian, or estimate a large full-space norm by its one-head value.

As a useful scope extension of the N-independent mechanism, any supplied positive endpoint graph with maximum weighted degree d_max has one-head Laplacian norm at most2d_max: its quadratic form is sum c_xy|psi_x-psi_y|²<=2d_max||psi||². If both physical/logical endpoint graph copies and the exact literal intertwiner exist, replace4c_max in(4)--(5) by4d_max. This is an operator estimate conditional on those concrete supports; it is not a cubic embedding or compiler for an arbitrary graph. The chain requires no such additional premise because its physical supports are already explicit.

## 4. Full physical-output finite-time theorem

Rectangular Duhamel on the invariant logical/physical occupation sectors, followed by the two endpoint replacements Jd to J, yields for every real t

 ||[exp(-it H_net)J-J exp(-it A_net)]|H_le1||
 <=min{2,2kappa_1+|t|(epsilon_max+4c_max kappa_1)}.     (6)

All mediator, endpoint and program output coordinates are retained. The error includes amplitudes with a mediator occupied; the literal mediator-vacancy subspace is not asserted invariant. The reference extension is complete, and the associated unhalved trace/channel distance on this RESTRICTED input domain is at most twice(6). It is not a diamond bound for arbitrary multihead inputs.

If all legal programs are restricted further to enabled000 in every cell, E vanishes identically and the epsilon_max term may be removed. For arbitrary legal program superpositions it must be kept. No program fitting or dephasing is used.

For identical cells and c_i=z a, z>=0, at the scale T_gate=pi/a,

    error<=min{2,2kappa_1(1+2pi z)+pi epsilon/a}
         <=min{2,2r(1+2pi z)+pi D0/D1},             (7)

where r=sqrt(2)b/D0. The capped second comparison is non-strict; epsilon<2b²/D1 only makes the corresponding uncapped residual strictly smaller. The estimate holds throughout |t|<=T_gate. This replaces the full-domain N-dependent residual/error coefficients with local ones, not the physical distance a head must travel in a longer chain.

One symbolic bounded-load sufficient family illustrates that distinction without selecting a numerical point. For Lambda>0,0<eta<=1 and fixed z>=0 put

    L=1+2pi z, R=16pi/eta,
    D1=Lambda/2, D0=D1/R,
    r=eta/(16L), b=rD0/sqrt(2), a=r²D0, c_i=z a.

All cells satisfy the exact tuning and D1>D0>2b. The mediator load is D1+sqrt(2)rD0<Lambda. Endpoint load divided by D0 is3r/sqrt(2)+(1+2z)r²<1, since r<=1/(16L) and2z<L/pi. Thus actual endpoint/program loads remain below Lambda for every N. The first term2rL is eta/8 and pi D0/D1=eta/16, so(6) is below3eta/16 throughout

    |t|<=T_gate=8192pi² L²/(Lambda eta³).            (8)

Unlike the full-domain network family, these supplied coefficients need not vary with N for this fixed restricted-domain horizon and accuracy. Qubit/block resources still grow with N; this is not size-independent construction. Equation(8) is a sufficient comparison horizon, NOT a chain traversal time. For longer requested times, (6) must be reevaluated and its residual may require different local parameters. No optimality or native precision mechanism follows.

## 5. Uniform enabled path: exact boundary terms

When all cells are enabled and identical, the one-head internal logical Q_(a/2) bond has edge weight a/2 between L_i and R_i. If c_i=a/2 (equivalently z=1/2), the external logical bonds have the same weight. In the ordered endpoint basis

    x_1=L1,x_2=R1,x_3=L2,x_4=R2,...,x_(2N)=RN,

the exact restricted target is

    A_net|onehead = C I+(a/2) L_path(2N).             (9)

L_path has offdiagonal -1 on adjacent vertices, diagonal1 at x1 and x_(2N), and diagonal2 at every interior vertex. For N=1 both vertices have diagonal1 and the sole bond is the internal Q. No extra end cap is installed in this statement. It is the combinatorial path Laplacian, not a matrix with constant diagonal2 at both ends. Adding endpoint onsite a/2 would change its boundary conditions and would require inclusion as an actual attachment.

The exact eigenvalues of the relative target are

    E_k=a[1-cos(pi k/(2N))], k=0,...,2N-1,

with normalized constant mode for k=0 and cosine modes proportional to cos[pi k(ell-1/2)/(2N)] for k>0. These follow by the interior difference equation and its two degree-one endpoints. They exhibit a well-defined autonomous continuous-time path evolution after the common phase exp(-itC). Neither a directed current, high-fidelity endpoint arrival, perfect transfer nor a read time is established by this identification alone.

With classical disabled cells the corresponding internal edges vanish in A_net, while the external edges remain. The logical one-head target is the weighted Laplacian of that broken path. Legal coherent programs give a controlled direct sum of such graph evolutions, with the SAME common scalar C. Their actual physical disabled residual is covered by(6), not set to zero. The original literal source/processor device is not automatically an input or an output interface for this graph.

## 6. Resources, restrictions and provenance

The chain still uses6N physical qubits and8N-1 listed positive blocks in the combined mediator-block convention. Geometry, absent program-row couplings, conserved program contents, endpoint/code roles and exact coefficient correlations are supplied exactly as in the parent network. All head numbers exist physically; only the proved input domain is restricted. A source that sometimes creates two heads, or an old processor encoding arbitrary occupation states, is outside(6) unless a separate interface proves support in H_le1 and preserves the literal injection. Correct local marginals do not establish that global sector condition.

The theorem does not establish native blocks, native preparation of program Records, an algorithm compiler, arbitrary overlapping cells, strong mediator contacts, transport fidelity, physical resource superiority, capture/reset, repeated monitoring or finite permanent halt. It preserves full-output comparison and all actual phases while reducing a specific conservative occupation-dependent loss. The earlier arbitrary-occupation theorem remains valid separately and is not weakened or overwritten.

Exact sources: common-product source739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088 with distinct check809a2083527cf942e6a6e879a6211600c9f144938915a43dbcf56d5680858fb6; network source1d830ee1638794876d2a5062f436be9e32b484fef0c79de095aa54d16c0e5edc with my check4e6e229f5cbc92321f72bf71289ed8f911c7663773e3731fa0ab54997f22db77. These were completely read in the preceding coherent tasks and reused at those exact scopes. I authored the single-cell source and attachment derivation and distinctly checked the ROOT network source. This sector sharpening is NEW author work with that shared exposure, not an independent check of itself. ROOT suggested the occupation-sector and uniform-Laplacian questions; the restricted overlap, residual norms and boundary calculation above are the derivation requiring a distinct check.

Only this proposal was written. No scientific program, symbolic solver, dynamics, parameter sweep, numerical point, canonical/W/Git/PR/checkpoint/prompt/model change or delegation occurred. No retained status or publication is assigned.
