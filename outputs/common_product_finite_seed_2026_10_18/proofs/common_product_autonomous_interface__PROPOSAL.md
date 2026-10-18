# A static controlled router with supplied incoming wavepacket

New bounded author derivation, conditional on the two identified program-cell sources below and requiring a distinct check. A single effective positive exchange between identical leads has an exact unitary scattering matrix

    S_p(k)=e^{ik}[(1-p)X+pI], 0<k<pi.

The same literal vacant-mediator preparation admits a finite-time physical implementation with an explicit full-output error. A finite cut is possible with an additional explicit tail budget. Incoming wavepacket preparation is SUPPLIED: this result does not produce that packet from a product vacuum/one-site seed, replace an old processor theorem, supply a compiler, or give permanent finite output storage.

ROOT independently supplied the boundary-column algebra as design exposure. The spectral normalization, complete wavepacket map and finite-cut estimates here are author derivations, not independent verification of that suggestion. No scientific program was run.

## 1. Exact ideal one-head model and positive supports

Let H_port=C^2 tensor ell^2(N_0), with orthonormal states |r,n>, r=L,R. The two n=0 sites are the logical endpoints. Put a=2b^2/D0 and j=a/2=b^2/D0>0. In legal program p define

    h_p = K_lead +(1-p)j(|L,0>-|R,0>)(<L,0|-<R,0|),
    K_lead = j sum_{r=L,R;n>=0}
                 (|r,n>-|r,n+1>)(<r,n|-<r,n+1|).

These are bounded positive operators on the ONE-HEAD Hilbert space: ||K_lead||<=4j and ||h_p||<=4j. For h_0 the graph is an infinite line, and for h_1 it is two disjoint half-lines. The norm statement follows either from those graphs or their degree bound. It does not treat an infinite sum on an unrestricted many-head tensor product as a bounded Hamiltonian.

At the boundary the enabled branch has diagonal 2j and off-diagonal -j to the other endpoint; the disabled branch has diagonal j and no port coupling. Thus the disabled boundary is the discrete Neumann endpoint. All lead terms are full positive Q_j blocks on neighboring head qubits. Coordinates may extend the source cell's u=(-1,0,0) to (-1-n,0,0) and v=(1,0,0) to (1+n,0,0); the mediator remains (0,0,0). Only the microscopic mediator path is physically installed between endpoints. The effective endpoint bond is the comparison Hamiltonian.

The ideal legal-program Hamiltonian is h=P0 tensor h_0+P1 tensor h_1. The actual physical comparison includes 2b I+h. Program contents, occupation basis, local roles, absent extra interactions, coefficients, mediator vacancy, and input packet are premises.

## 2. Boundary calculation and complete normalized spectral map

Set E(k)=2j(1-cos k), z=e^{ik}. A boundary-normalized generalized solution is

    psi_n(k)=(2pi)^(-1/2)[z^{-n} f+z^n S_p(k)f],

where f is a two-port incoming column. The boundary equation is

    (E-j)psi_0=j(1-p)(I-X)psi_0-j psi_1.

For p=1 it gives S=zI. For p=0, inserting S=zX gives both independent port columns; equivalently the X=+1 channel gives S=+z and X=-1 gives S=-z. Consequently S_p=z C_p, C_0=X, C_1=I. The velocity v(k)=E'(k)=2j sin k is positive on (0,pi), so the stated radial incoming/outgoing convention agrees with propagation direction.

The coefficient (2pi)^(-1/2) is not an arbitrary flux normalization. For a C_p eigenvalue sigma=+1 the generalized column is

    sqrt(2/pi)e^{ik/2}cos[k(n+1/2)],

and for sigma=-1 it is

    -i sqrt(2/pi)e^{ik/2}sin[k(n+1/2)].

The half-integer cosine and sine families separately form complete orthonormal bases of L2(0,pi). Their multiplication by the displayed unit-modulus factors preserves unitarity. Resolving the constant port involution C_p therefore proves that

    (F_p f)_n=(2pi)^(-1/2) integral_0^pi
                    [e^{-ikn}I+e^{ikn}S_p(k)] f(k) dk

is a UNITARY map from L2((0,pi);C^2) onto H_port. It diagonalizes h_p as multiplication by E(k), first on smooth compactly supported spectral data and then by bounded extension. There are no missing bound-state columns: completeness has been proved by the sine/cosine bases. This also proves ||h_p||=4j as a spectral supremum.

The controlled transform F=P0 tensor F_0+P1 tensor F_1 is unitary. It tensors with identity on any passive reference Hilbert space. Thus all subsequent operator or vector comparisons include coherent program/path superpositions and reference entanglement. Three physical program bits represent |p> as |ppp>; their coherence is mathematically allowed, not derived Record preparation.

## 3. Exact evolution and finite-time normalized incoming/output states

For Hilbert-valued spectral f of norm one define radial maps

    (I_t f)_n=(2pi)^(-1/2) integral e^{-ikn-itE(k)} f(k) dk,
    (O_t f)_n=(2pi)^(-1/2) integral e^{ikn-itE(k)} f(k) dk.

Integrals are over (0,pi). With S(k)=e^{ik}C, C=P0 tensor X+P1 tensor I, exact evolution of the normalized scattering state is

    exp(-it h)Ff=I_t f+O_t Sf.                 (1)

Neither summand alone is asserted normalized at finite time. Their interference is retained in (1).

Here is a quantitative separated-packet version. Let f be continuously differentiable with compact support in [k_-,k_+] subset (0,pi), and let

    v_* = min_support 2j sin k >0,
    B(f)=||f'||_L1 +(2j/v_*)||f||_L1,
    D_tau(f)=B(f)/sqrt(2pi) sqrt[(tau v_*)^-2+(tau v_*)^-1].

For tau>0, integration by parts, with zero endpoint terms, gives

    ||I_tau f|| <=D_tau(f),
    ||O_{-tau} f|| <=D_tau(f).                 (2)

Indeed the relevant phase derivative has magnitude at least n+tau v_*. Its second derivative is bounded by 2j tau, so each site amplitude is at most B(f)/(sqrt(2pi)(n+tau v_*)). Sum its square using sum_{n>=0}(n+A)^-2<=A^-2+A^-1. This proof applies directly to reference-valued f and does not sum over reference dimensions.

Assume D_tau(Sf)<1 and D_tau(f)<1. Define actual supplied normalized incoming state and normalized target

    i_f=I_{-tau}f/||I_{-tau}f||,
    o_f=O_tau Sf/||O_tau Sf||.

The denominators are nonzero: compare each unnormalized vector to its norm-one exact state in (1). Normalizing a vector within d of a unit vector increases the distance by at most another d. Applying (1) at -tau and +tau therefore proves

    ||exp(-i2tau h)i_f-o_f||
             <=2D_tau(Sf)+2D_tau(f).          (3)

One can cap this and every final vector comparison by 2. The time is elapsed time 2tau; the negative label describes the prepared spectral phase and is not a requirement to run a laboratory Hamiltonian backwards.

For a clean coherent controlled-router interface take f(k)=g(k)xi, where ||g||_L2=1 and xi is any norm-one program/path/reference vector independent of k. Then

    i_f=i_g tensor xi,
    o_f=o_{e^{ik}g} tensor C xi.

Here i_g and o_{e^{ik}g} are normalized scalar radial packets defined by the preceding formulas. Their normalizations are independent of xi and program. Thus (3) is a uniform isometry comparison on the entire program/path/reference input space with error

    e_wave=2D_tau(e^{ik}g)+2D_tau(g).           (4)

In particular B(e^{ik}g)<=||g'||_L1+(1+2j/v_*)||g||_L1. The common spectral phase e^{ik} is retained in the outgoing radial packet. It is not discarded as a k-independent scalar. The controlled path operation C swaps ports when enabled and preserves ports when disabled. Both branches share this outgoing packet, so no branch-dependent arrival distortion is hidden by tracing motion away.

For general spectral/internal entangled f, (1)--(3) still hold, but the claimed product form with a common radial factor requires the stated factorization premise. Preparation of i_g is an external state-preparation task. It can contain one head spread coherently across many sites; tensoring a vacant mediator does not make that packet a sitewise product seed.

## 4. Physical single-cell realization over the entire elapsed time

Use exactly the six-qubit Hamiltonian and common literal injection J from source 739e99c4 below, restricted together with the leads to total head number one. If the head is in a lead, all three cell heads are vacant. The cell compensation still contributes the same scalar 2b. Add K_lead physically using full Q_j blocks on the leads and endpoint contacts. It acts on no mediator or program qubit, so

    K_lead J=J K_lead, ||K_lead||<=4j

on this one-head domain, where the right-hand operator is logical. This is exact literal-code intertwining, not merely equality of compressed matrix entries. It can also be obtained first with finite leads and extended strongly; all norms here are uniformly bounded in lead length. The cell's dressed map differs from J only on its endpoint symmetric column and remains an isometry on this one-head extension.

Define from the source

    epsilon1=4b^2/[sqrt(D1^2+8b^2)+D1],
    r0=sqrt(2)b/D0,
    r1=sqrt(2)b/(D1+epsilon1),
    alpha_p=(1+r_p^2)^(-1/2),
    kappa=max_p sqrt(2-2alpha_p) <=sqrt(2)b/D0.

For D1>D0>2b and a=2b^2/D0, the attachment dressed-residual theorem gives at elapsed time T

    ||exp(-iT H_phys)J-J exp[-iT(2bI+h)]||
      <=e_cell(T):=min{2,2kappa+T(8j kappa+epsilon1)}.   (5)

All actual mediator output is included in (5). No mediator postselection, fitted phase, renormalization of physical output, or assumption of dressed-subspace invariance is used. The literal preparation is common to the two program branches; the auxiliary dressed map is only a proof device. The full cell source also proves two-head columns, but this interface invokes only its total-one-head restriction and makes no many-particle scattering claim.

Combining (4),(5), uniformly on arbitrary xi and passive references,

    ||exp(-i2tau H_phys)J(i_g tensor xi)
       -e^{-i4b tau} J(o_{e^{ik}g} tensor Cxi)||
           <=min{2,e_cell(2tau)+e_wave}.       (6)

Equation (6) is the full physical output claim, with the common physical scalar phase explicit. It bounds induced isometry norm; the unhalved trace-distance/diamond-distance bound for the corresponding channels is at most twice its right side. The target includes unchanged encoded programs and a vacant mediator.

At T=s/j, the sufficient cell envelope is

    e_cell(T) <=min{2,(2+8s)kappa+2s D0/D1}.

For any fixed smooth g away from the band edges, e_wave tends to zero as j tau grows. One may first choose that dimensionless duration, then choose b/D0 and D0/D1 small enough to reduce (5). This is an existence route with explicit tradeoffs, not a fixed operating point or optimal scaling. A fixed load cap also changes the physical duration through j=b^2/D0; it cannot be omitted from an efficiency claim.

Each endpoint gains incident load 2j from its one new lead bond. Thus source incident sums become 3b+a+2j at u,v, D1+2b at m, a at c_u,c_v, and D1-2b at c_m, under its combined mediator-block convention. A lead interior site has incident sum 4j; a finite outer end has 2j. Individual lead blocks have norm 2j. A sufficient incident cap is the maximum of those displayed loads. These loads are local sums; an infinite total many-head norm is not asserted. The physical law, positive terms and coefficient tuning remain supplied.

## 5. Optional finite leads with an explicit finite-time cut budget

This section avoids claiming that an asymptotic scattering theorem already establishes a finite device. Fix finite integers R<=N. Let P_R project both ports onto n<=R and put

    delta_R=||(I-P_R)i_g||,
    i_{g,R}=P_R i_g/||P_R i_g||,

assuming delta_R<1. Then ||i_{g,R}-i_g||<=2delta_R. This is another supplied finite packet preparation, not an autonomous launcher. Let h_N be the ideal graph with sites 0,...,N on each lead and the same programmed endpoint bond. Remove the edge (N,N+1), including its endpoint diagonal. Embed h_N into the infinite one-head space by zero on its complement. Both ||h_N|| and ||h|| are <=4j. For a state supported in n<=R,

    h_N^m psi=h^m psi for 0<=m<d, d=N-R+1.

This follows from the nearest-neighbor support propagation of each multiplication; the first possible removed-edge or changed-diagonal action is at the d-th multiplication. The same statement holds in both program sectors. Taylor expansion of the bounded propagators therefore gives

    ||exp(-iT h_N)psi-exp(-iT h)psi||
       <=e_cut:=min{2,2 sum_{m=d}^infinity (4jT)^m/m!}
       <=min{2,2 exp(4jT)(4jT)^d/d!}.          (7)

The factorial bound can be loose but converges to zero with N at fixed R,T. It is a finite-time bound, not a statement about all-late recurrence. The same cell attachment proof applies to physical finite leads, since their K norm remains <=4j. Combining (3)--(7), with the finite physical output embedded into the infinite comparison space,

    ||exp(-iT H_phys,N)J_N(i_{g,R} tensor xi)
       -e^{-i2bT}J(o_{e^{ik}g} tensor Cxi)||
       <=min{2,e_cell(T)+e_cut+2delta_R+e_wave}, T=2tau. (8)

The embedding preserves every output coordinate; it does not trace away the outer tails. For a target entirely inside the finite device, define delta_out,N=||(I-P_N)o_{e^{ik}g}||<1 and use its normalized truncation o_N. Replacing the target in (8) by e^{-i2bT}J_N(o_N tensor Cxi) adds at most 2delta_out,N. All these tails converge to zero for their normalized ell^2 packets. For fixed T first choose R to control the input tail, then choose N>=R to control both (7) and the output tail. This proves existence of a finite approximation without an unproved launch or capture mechanism.

The estimate is only at the stated elapsed time (or separately at times with their own packet comparator). A finite closed graph has returns; no permanent halt, all-late capture, reset, or stable classical output follows.

## 6. Failed shortcuts, remaining obligations and provenance

Boundary-column algebra alone does not prove a normalized wavepacket operation: the complete cosine/sine transform and finite-time unwanted-wave tails were necessary. Replacing S(k) by C discards a common but momentum-dependent phase and would give the wrong radial target. Comparing the isolated cell forever to an exact off branch fails because epsilon1 is a nonscalar residual. Applying the isolated error without its attachment overhead would omit the lead interaction. Treating the infinite sum as bounded on unrestricted many-head states would also be invalid. A finite cut without a preparation-tail and propagation budget is not supplied by the scattering matrix.

No failed route here establishes a universal impossibility. A future possibility is identical weak end emitters at finite distance L, with a product vacuum/one-head encoded input and observation after routing but before boundary return. That requires its own launch theorem, spectral-width control, emitter residual budget, finite-cut budget, and coherent full-output comparison. None is claimed by (6) or (8).

Exact sources fully read and SHA-256 checked for this derivation:

* mediated_common_product_program/PROPOSAL.md — 739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088.
* mediated_program_attachment/PROPOSAL.md — 55af72a1a334730be95de5427646de29fa7d1d6ebac21d888dc1f231406d9b7a.

Both are provisional source premises at their stated scopes. This proposal adds the specific two-lead model, complete scattering transform, normalized packet comparison, positive attachment instantiation and finite-cut construction. It does not independently audit the microscopic cell or attachment source. A distinct reviewer should check the half-integer basis normalization/completeness, incoming/outgoing signs, phase and elapsed-time convention, reference-uniform tail bound, one-head exact attachment and scalar, finite-cut power agreement, and all triangle-error terms before integration. No retained status follows from this author derivation.

Only common_product_autonomous_interface/PROPOSAL.md was created. No numerical dynamics, eigensolver, symbolic solver, scientific executable, parameter sweep, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation was performed.
