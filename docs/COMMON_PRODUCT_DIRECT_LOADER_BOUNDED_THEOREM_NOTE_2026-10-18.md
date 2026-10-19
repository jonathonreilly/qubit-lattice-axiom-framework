# Direct two-body coherent loading with complete finite output

Claim type: bounded_theorem.
Primary runner: `scripts/common_product_device_controls_2026_10_18.py`.

Claim status: bounded_theorem. Conditional analytical result with separate source-exposed checks of the stationary word, complete finite construction, geometric relabeling and bounded-horizon branch comparison. No retained audit, native Hamiltonian or active old-processor realization is asserted.

A static network of supplied real positive one-/two-qubit blocks can exchange a new ordinary program Q with an old ordinary program P, perform the controlled logical-path operation using the new program, and flip a record R. The old P state and its passive environment are retained on Q and that same environment. A complete endpoint-seeded finite theorem pays all heads and data outputs. It requires no entangled cat register, perturbative loader gadget, prepared incoming wavepacket or timed switching.

The construction uses the local core and writer primitives of the [single-control theorem](COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md). Their local stationary bounds are reused; their older finite apparatus and runtime theorem are not transferred. The new network has a different shared-data geometry and a new complete finite proof.

## Conditional device and input/output theorem

Fix 0<epsilon<=1 and a full-support incident norm cap Lambda>0. There is one actual qubit each Q,P,R, and one head excitation on a graph with two path labels: auxiliary a and logical b. These labels denote four head channels, not two additional data qubits. Every repeated core or writer uses the SAME physical Q,P,R. The data and passive references have no additional head-independent dynamics: in particular no active H_PE, record bias or receiving-gadget penalty is present.

The finite device has

    501+8ell physical qubits,       928+8ell positive blocks,         (1)

with ell given explicitly below. Every pair interaction has supplied spatial range at most21 on a cubic lattice; exterior-ray interactions are nearest neighbor. The maximum graph degree is36. This is not a nearest-neighbor realization: the shared control has more than six distinct neighbors. Exact matrix coefficients, block supports and absence of undeclared interactions remain supplied.

The input isometry E_seed fixes a=1, puts the logical head at one of TWO actual input emitters indexed by b, supplies R=0 and all remaining heads vacant, and permits arbitrary Q/P/reference coherence. A superposition of emitter states |10> and |01> is supplied logical input, not a product over those two sites. For a channel on new logical Q/b, the old joint state sigma_PE is fixed independently of that input. A passive purification may be retained; E is never manipulated or discarded.

Let V_log be the data/path permutation

    |b,q,p,0_R> -> |b xor(1-q),p_Q,q_P,1_R>.                       (2)

Auxiliary a=1 is restored. The old sigma_PE becomes sigma_QE, retaining all its correlations. Let J_F place a single head on the two right a=1 output rays and make every other head vacant. With a common normalized radial packet beta_ell(t), the complete physical comparison is

    sup_(t_minus<=t<=t_plus)
      ||exp(-itH_fin)E_seed
          -exp(-ict)J_F[beta_ell(t) tensor V_log]|| <epsilon/8,
    t_minus=3ell/(4j), t_plus=7ell/(8j),
    c=112beta+64(sqrt(2)-1)j.                                    (3)

Here beta denotes the core hopping coefficient; beta_ell denotes the packet. The operator norm includes arbitrary passive references and every output: all496 internal heads, both emitters, eight finite rays, Q,P,R and the relocated old environment. The unhalved complete-output channel discrepancy is less than epsilon/4. Throughout this window the joint event R=1 with the single head on the two retained right a=1 rays has probability greater than1-epsilon^2/64. Logical accuracy and old-state retention follow from the stronger norm statement, not from that event alone.

There is also an absolute record-branch comparison over the ENTIRE bounded horizon. Define V(t) using the same ideal outgoing sequence restricted to physical output sites1,...,ell, with its exact scalar phase and data operation, but WITHOUT normalizing its radial norm. Then the same physical device and parameter policy obey

    sup_(0<=t<=t_plus)
      ||P_R1 exp(-itH_fin)E_seed - V(t)|| <epsilon/256.             (4)

Both maps are contractions, giving unhalved stabilized distance less than epsilon/128 between their SUBNORMALIZED branch maps. This is not a small-amplitude bound on the actual R=1 branch, which can have order-one norm in the final window. It is not normalized postselection accuracy for rare early outcomes, and it does not extend past t_plus.

## Eleven-stage operator word and actual blocks

A core controlled by an ordinary data qubit D acts ideally on a two-channel path c as

    C_D^(c)=|0><0|_D tensor X_c+|1><1|_D tensor I_c.

Its eight heads are four endpoints and four mediators. For each square edge {u,v} with mediator m, the installed blocks are Q_beta(u,m), Q_beta(m,v), beta(I-n_u), beta(I-n_v), and a positive control M_e. On cross edges

    M_e=[(D0-2beta)|0><0|+(D1-2beta)|1><1|]_D n_m;

straight edges exchange D0,D1. Four endpoint terms2j n_v complete the24-block core. Here Q_x=x(n_u+n_v-a_u†a_v-a_v†a_u), positive also on double occupation; D1>D0>2beta and j=beta^2/D0. The reciprocal stationary comparator is z C_D in either transmission direction, with full-port error at most13eta^2+5zeta, eta=beta/D0 and zeta=D0/D1.

Each actual writer has24 heads and34 supplied positive blocks, including its real signed junction exchanges, phase repairs and two contacts j n_T(I+X_D) to the same target. Its full two-port comparator is -i z^22 X_D with error at most33|k-pi/2|. A scalar writer replaces the contacts by2j n_T. This is the exact X_D=+1 matrix specialization and has the SAME scalar phase and error bound, with no dummy |+> qubit. The writer's complete inventory is pinned in the stationary proof; no target-controlled three-body hopping is substituted.

Let W_P write P only on auxiliary path a=1 and use a scalar writer on a=0. The three-stage sandwich F_(Q->P)=C_Q^(a) W_P C_Q^(a) acts on basis bits as

    (a,q,p) -> (a,q,p xor q xor(1-a)).                           (5)

It restores a for both values. The consecutive sandwiches F_(Q->P), F_(P->Q), F_(Q->P) exchange Q,P for BOTH auxiliary paths. Indeed, putting s=1 xor a,

    p1=p xor q xor s,
    q2=q xor p1 xor s=p,
    p3=p1 xor q2 xor s=q.

Thus the nine-stage loader is I_a tensor SWAP_QP, including coherent auxiliary/data/reference states. Duplicate each head geometry across logical b while sharing Q,P. Stage10 applies C_P^(b) in each auxiliary lane; stage11 writes R on all four channels. The full ideal forward and reverse words are

    U_f=I_a tensor[X_R C_P^(b) SWAP_QP],
    U_b=U_f*=I_a tensor[SWAP_QP C_P^(b) X_R].                    (6)

The reverse word generally differs from the forward one. All factors are kept in order; Q and P are not globally conserved classical controls.

There are fourteen cores and sixteen writers, six of them scalar. Four equal cables connect adjacent stages. Set all ten gap lengths to one hopping edge, so forty cable blocks have no interior heads. There are496 distinct module heads plus Q,P,R, and920 internal blocks. Seven core STAGES and four writer STAGES give

    z^7(-i z^22)^4 z^10=z^105.

Parallel module counts do not multiply that transmission phase. Their physical vacuum scalars DO add, giving c in (3). After subtracting c, every module annihilates its local head vacuum for every data state. This allows one common energy and full shared eight-dimensional Q/P/R fiber throughout the network.

The internal matching has eighty port ends and eight exterior ends. If S_loc is the stage direct sum and P_c pairs internal ends with phase z, then

    S_net=S_ee+S_ei(I-P_c S_ii)^(-1)P_c S_ie.

The reflectionless comparator's internal transition has eleventh power zero. With delta=max{13eta^2+5zeta,33h} and11delta<1, ordered inverse estimates give

    ||(I-P_c S_ii)^(-1)||<=11/(1-11delta),
    ||S_net-z^105[[0,U_f*],[U_f,0]]||
                         <=144delta/(1-11delta).               (7)

This bound includes every reflected port and repeated return with changed data. Local flux conservation cancels paired internal flux and proves unitary exterior scattering. It does not by itself prove a complete normalized physical packet or absence of localized states.

## Supplied range21 geometry, sources and cap

Embed the499 internal qubits injectively into {0,...,7}^3. Reserve ports p_i=(i,7,7), i=0,...,7, in left-then-right lexicographic(a,b) order. Map the remaining491 graph vertices to the first491 cube sites excluding those eight ports, using any fixed ordering of graph labels. There are504 available sites, so13 remain unused. Every installed internal pair is at Manhattan distance at most21. Attach ray i at (i,7,7+n), n>=1. These rays are mutually disjoint, lie outside the cube and use only unit-length consecutive interactions.

This is a qubit permutation of the fixed graph, not an approximation or a wire routing argument. It preserves every block, graph cable length, port reference plane, coefficient, scalar and norm. For the finite source/cap construction it extends to an ordinary finite tensor-factor permutation, so the finite proof for the original range498 placement transfers EXACTLY, including all phases and references. Geometrically crossing pair terms do not occupy intermediate sites; finite-range pair interactions and absence of other nearby interactions are explicit supplies. Degrees36 at Q,32 at P and8 at R remain and prohibit a nearest-neighbor embedding of this literal graph without further construction.

Only the two left a=1 rays receive emitters at M=ell+1. Each has ell ordinary bonds followed by the combined block

    B_gamma=Q_gamma(ell,M)+(j-gamma)n_ell+(2j-gamma)n_M.

All six other rays—the two unused left inputs and four right outputs—end at ell with ordinary bonds and j n_ell repair. Every external one-head diagonal is2j. A source block has full norm3j and is counted once. These two source rays and six capped rays yield (1); neither unused inputs nor unwanted outputs are removed.

Choose

    h=eta^2=zeta=epsilon/10^7,
    D1=Lambda/64, D0=zeta D1, beta=eta D0,
    j=Lambda epsilon^2/(64*10^14),
    rho=epsilon sqrt(h)/10^4, gamma=rho j.                      (8)

All primitive domains hold. The shared data loads, on FULL support, are

    Q:32(D1-2beta)+8j,
    P:24(D1-2beta)+16j,
    R:16j.

With beta<=D1/32 and j<=D1/256 these are bounded by Lambda/2+Lambda/2048,3Lambda/8+Lambda/1024,Lambda/1024. Core endpoint6beta+4j, mediator D1+2beta, writer-head12j, source-adjacent5j, emitter3j, repaired-end3j and ray4j loads also lie below Lambda. Shared contacts are all counted; a one-head expectation is not used to evade the cap.

## Exact packet and explicit sufficient policy

Let z=exp(ik), E(k)=2j(1-cos k). Use the exact standalone source amplitude

    F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot k-i rho^2].

Its L2(0,pi) norm is one. Use a real quintic cutoff chi: plateau |k-pi/2|<=h/2, zero beyond3h/4, with1-10s^3+15s^4-6s^5 on the transition and s=4(|k-pi/2|-h/2)/h. Define

    P_loss=3rho^2/h, p_chi=||chi F||_2^2,
    g=chi F/sqrt(p_chi), G0=2,G1=80/rho,G2=600/rho^3.             (9)

The checked scalar measure gives p_chi>=1-P_loss>1/2 and ||F-g||_2<=2sqrt(P_loss). The derivative lemma gives ||g^(r)||_1<=Gr through r=2. The cutoff is a comparison device, not physical packet preparation.

For a fully explicit prescription put B=11,D=105,delta=33epsilon/10^7 and evaluate

    s1=6B^2+2B, s2=36B^3+18B^2+2B,
    a1=1+s1, a2=1+2s1+s2,
    r0=11/(1-11delta), r1=r0^2 a1,
    r2=2r0^3 a1^2+r0^2 a2,
    v0=1+r0, v1=r1+r0a1,
    S1=s1+s1r0+r1+r0a1,
    S2=s2+s2r0+2s1r1+2s1r0a1+r2+2r1a1+r0a2,
    Q1=S1+D,Q2=S2+2D S1+D^2,
    H0=G0,H1=G1+Q1G0,H2=G2+2Q1G1+Q2G0,
    T0=2Bv0,T1=s1v0+2Bv1,
    J0=T0G0,J1=T0G1+T1G0,
    Bin=G2+6G1+14G0,Bout=H2+24H1+200H0,
    L=1+(G1+2G0)+(H1+H0)+(G1+8G0),
    Qbudget=1+eta^-1+rho^-2+J0+J1+Bin+Bout.                     (10)

Qbudget is an analytical bound, not the physical program Q. Then set

    u0=10^12 max{1,(L/epsilon)^2,Qbudget/epsilon},
    ell=ceil max{100u0,100D}, M=ell+1, t0=u0/j.                 (11)

All constants precede ell; no inverse or derivative estimate is fitted after the length is chosen. The normalized target in (3) comes from

    B_n(t)=(2pi)^(-1/2) integral_0^pi
                  exp(i[n+ell+105]k-itE(k))g(k) dk,             (12)

restricted to1<=n<=ell and divided by its positive norm. It is common to both logical paths and every program column. Its full-integer norm is one; its finite restriction is proved nonzero in the final window. There is NO extra fitted -i: the four writer constants already multiply to1. The phase in F remains inside g.

The new proof constructs an exact packet on ALL eight infinite rays and all496 internal heads. Local boundary inverses satisfy ||M_v^-1||<=11 on the band: the checked writer inverse is below10, and the actual core Schur inverse including mediators is below4. Since the first two derivatives of M_v=H_v/j-E/j-z Pi_ports have norm<=3, ordered inverse and feedback differentiation gives (10). T0,T1 bound the complete internal map; no origin or target sector is omitted.

The external stationary integral has incident exp(iell k)g and the full S_net outgoing coefficient. Its internal integral uses that complete map T. It solves the actual bounded one-head Schrödinger equation. In the remote past its incoming full-line Fourier field has norm one and the unwanted outgoing/internal fields vanish. Norm conservation proves exact packet normalization without assuming spectral completeness or excluding localized eigenstates.

For early matching, disconnect the two selected origins from their core mediators, change their actual3j diagonals to the scalar reference's2j, and continue each into an artificial negative-index chain. Retain the entire complementary actual matrix. The reference remains in two identical scalar launchers with R blank. The actual/reference difference satisfies

    ||V_contact||<=2j+sqrt(2)beta,
    Econtact<=u0(2+sqrt(2)/eta) sum_(m>=M)(4u0)^m/m!
             <=(2+sqrt(2)/eta)/(5000u0).                       (13)

Only the invariant scalar reference trajectory uses the4j norm; large actual mediator energies are never dropped. The reference source decomposition and its residual1/(rho^2u0) produce the incoming packet with exactly x=ell-n. Full-vector matching pays every seeded component, including any localized component; it does not assign the actual loader the reference scalar measure.

Fixed diagonal repairs make subsequent cut perturbations adjacency-only: two source rays have (j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2), and the six other rays have j Adj(ell,ell+1). Their combined norm is at most sqrt(2)j on the direct sum of contacts. Two integrations by parts and Duhamel give100(Bin/u0+Bout/ell) through t_plus, paying returns and reabsorption on all rays.

The complete bound before substitution of (11) is

    Einit=Econtact+rho^-2/u0+2(G1+2G0)/sqrt(u0)+4sqrt(P_loss)
          +2(G1+G0+H1+H0)/sqrt(ell)+2(J0+J1)/ell,
    Efinal<=Einit+100(Bin/u0+Bout/ell)+d_s
          +2(G1+6G0)/sqrt(ell)+(3J1+11J0)/ell
          +10(G1+8G0)/sqrt(ell),
    d_s=144delta/(1-11delta)<epsilon/2048.                     (14)

It includes source, incoming, internal, stationary operation and both final packet tails with normalization. The policy gives L/sqrt(u0)<=epsilon/10^6,Qbudget/u0<=epsilon/10^12 and the corresponding ell bounds epsilon/10^7,epsilon/10^14. Spectral replacement is below epsilon/1024. Every term in (14) is explicitly paid by these inequalities, with total below epsilon/8. The finite source and its review provide the full allocation table and derivative-gap derivations.

For this PARTICULAR sufficient recipe, the network jet constants have finite limits, rho=Theta(epsilon^(3/2)), L=Theta(epsilon^-3/2) and Qbudget=Theta(epsilon^-9/2). The two growing terms in (11) have orders epsilon^-5 and epsilon^-11/2. Consequently

    size and j t_plus =Theta(epsilon^-11/2),
    t_plus=Theta(Lambda^-1 epsilon^-15/2),
    gamma=Theta(Lambda epsilon^7/2).                            (15)

These are sufficient chosen-family orders, not necessary resources, practical runtimes, fabrication tolerances or optimality claims. The large explicit prefactors and exact small coefficients remain part of the construction. Coefficient magnitude is not precision.

## Why the same policy pays the whole-horizon branch

Use the SAME unnormalized (12), restriction1<=n<=ell, ideal data operation and exp(-ict) to define V(t) at every time, including zero. Its norm is at most one by Parseval and restriction. The output origins are not part of this target: they are included in T and charged there.

For the actual normalized g, direct integration of its exact resonance denominator gives

    ||g||_1<=2sqrt(pi)rho asinh(3h/(pi rho^2))
             <=4rho log(1+2h/rho^2)<3*10^-6 epsilon.            (16)

The factor from p_chi>=1/2 is included. With (8), rho=epsilon^(3/2)/sqrt(10^15). The inequality follows uniformly from the monotonicity of x log(1+2*10^8/x^4) on0<x<=1, whose value is below20 at1. Also T0=22(1+r0)<265, so the COMPLETE internal packet amplitude is less than epsilon/2048 at every time by T0||g||_1/sqrt(2pi).

For t0<=t<=t_plus the full-vector Einit+cut comparison remains valid before the final output window as well. Projecting onto R=1 annihilates the incoming packet. The restriction of the ideal outgoing packet to the physical output sites is exactly V; the outgoing scattering defect costs d_s, and the full internal projection costs the preceding uniform bound. The actual finite match plus cut total is less than epsilon/512. Thus the branch error is below3epsilon/1024<epsilon/256 throughout this interval.

Before t0, the SAME scalar reference remains recordblank. Its paid contact bound is monotone in time and gives ||P_R1 U_fin(t)E_seed||<=epsilon/10^12. Independently, the ideal outgoing phase derivative is at least n+.98ell, giving ||V(t)||<=2L/sqrt(ell)<=2epsilon/10^7. Their sum proves the early part of (4). An actual early flag estimate alone would not suffice: the nonzero comparator's early tail is explicitly paid. No time-dependent redefinition of the target occurs at t0.

Finally, for contractions A(t)=P_R1 U_fin(t)E_seed and V(t), the identity

    A X A* - V X V*=(A-V)X A*+V X(A*-V*)

gives trace norm at most2||A-V|| ||X||_1, including any passive ancilla. This proves the subnormalized-channel form of (4). Division by a small success probability is neither made nor justified. The separate final-window guarantee (3) supplies high success later; the branch comparison does not mean the record is an irreversible completion latch.

## Premises, open interfaces and evidence

The supported result is a finite supplied two-body range21 device with a coherent two-emitter input, freely degenerate ordinary data, blank rest/R and complete retention of old-state/reference outputs. The exact graph permutation transfers the range498 finite proof without a dynamical approximation. It does not produce nearest-neighbor couplings, native coefficient supply, physical Q/path input preparation, old active-environment decoupling, cooling, capture, reset, permanent halt or operation of the historical literal processor. An active H_PE, receiving penalty or additional data bias requires a new channel and finite proof. No such energy term is silently removed by calling E passive.

## Current source bindings and bounded validation

The complete mathematical sources remain live at the paths below. Their embedded historical author, pending-review and acceptance language records provenance and supplies no present verdict. Current claims require the stated premises and full proofs; finite checks neither establish general estimates by sampling nor promote native interactions or audit status. The original manuscript and all original packet versions are recoverable from `archive/common_product_devices_review_2026_10_18/MANIFEST.json`.

- `outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_branch_instantiation_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_range21_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_loader_uniform_branch_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_two_body_loader_PROPOSAL.md`
- `outputs/common_product_devices_review_2026_10_18/proofs/pr9733/common_product_direct_two_body_loader_finite_PROPOSAL.md`

The shared primary computes finite ordered algebra, selector spectra, complete logical words, local physical blocks, exact scalar propagation, source normalization, literal geometry and sufficient-policy allocations. It does not construct the enormous prescribed apparatus or replace the analytical packet, derivative and tail estimates. Complete literal source closure and inherited version pins are in `outputs/common_product_devices_review_2026_10_18/INPUT_CLOSURE.json`.
