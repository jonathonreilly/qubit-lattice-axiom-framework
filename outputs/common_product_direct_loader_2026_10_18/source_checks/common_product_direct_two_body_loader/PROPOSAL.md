# Direct two-body stationary SWAP loader and controlled operation

New author derivation requiring a distinct check. The ROOT-proposed controlled-core/writer word works algebraically. Three modules implement an exact comparison SWAP of the two ordinary physical qubits Q and P, restoring the auxiliary head-path bit for BOTH its values. Appending a controlled logical-path core and coherent record writer gives the intended logical action while relocating the entire old P/environment state to Q/environment. A full stationary scattering estimate below includes reverse incidence, reflected outputs, wrong paths and repeated returns on the shared data fiber.

This is a conditional stationary result for a newly specified bounded-degree graph with supplied real positive one-/two-qubit blocks. It needs no signed cats, four-body loader, perturbative gadget or prepared entangled ancillary data. It DOES need the physical one-head path input, ordinary input/data qubits, supplied coefficients, and absent head-independent data dynamics. The literal graph has shared-Q degree36 and cannot be embedded as nearest-neighbor interactions on the cubic lattice with distinct vertices. A deliberately loose finite-range embedding is supplied instead. No finite endpoint-seed, finite-window, runtime, initialization, energy-quality or herald theorem is transferred from the previous apparatus.

## 1. Registers, domain and primitive conventions

Use one head excitation on the specified head graph. At a cross-section its four channels are labeled (a,b) in {0,1}². Here a is the auxiliary path and b is the logical path. They are labels of four ordinary head sites/channels in a one-head subspace, NOT two additional physical data qubits. There is one actual ordinary qubit each Q, P and R. Q holds the new program, P may contain arbitrary old information, and R is a coherently flipped record bit. Every module uses those SAME qubits. An arbitrary passive reference is retained throughout.

To avoid confusing logical b with the parent's hopping coefficient b, call that coefficient beta here. Supply

    D1>D0>2beta>0, j=beta²/D0,
    eta=beta/D0<=1/8, 0<zeta=D0/D1<1/2,
    z=exp(ik), E(k)=2j(1-cos k),
    d=|k-pi/2|<=10^-3.

This band is contained in [pi/3,2pi/3]. Incoming/outgoing waves on a local port are z^-n/z^n with radial n=0 at its endpoint. The common channel energy is E(k) after subtracting the actual global vacancy scalar. Q,P,R and the passive references have no additional free Hamiltonian or permanent operating penalties. In particular there is no record bias kappa n_R in this proposal. Adding such terms would change the scattering problem and is not covered by the result.

The primitive imports are only the full stationary one-control core from source76b5/core60bc, and the full two-port writer from source93445. Their exact source/check pins and reading scope appear in section9. The cat-preparer source d4e708 and check1f606 supply the already checked scalar-writer specialization and full-fiber feedback method; no cat is prepared or used here.

### Controlled path core

For an ordinary control D and a two-channel path c, put

    C_D^(c)=|0><0|_D tensor X_c+|1><1|_D tensor I_c.

There are four endpoints, four distinct mediators, and four square edges e={u,v}. Cross edges have

    M_e=[(D0-2beta)|0><0|_D+(D1-2beta)|1><1|_D] n_m_e;

straight edges exchange D0 and D1. The actual core blocks are

    sum_e [Q_beta(u,m_e)+Q_beta(m_e,v)
                 +beta(I-n_u)+beta(I-n_v)+M_e]
                 +2j sum_endpoints n_v,
    Q_beta(x,y)=beta[n_x+n_y-a_x^dagger a_y-a_y^dagger a_x].

Q_beta is positive with full-support norm2beta, including its double-occupation column; M_e is positive with norm D1-2beta. All four M_e contact one actual D. There are eight Q blocks, eight separately counted vacancy blocks, four M blocks and four endpoint occupations: eight heads and24 blocks, excluding D and external bonds. The full occupation identity leaves the common scalar8beta, and there is no D-dependent head-vacuum energy. Its full reciprocal comparator and bound are

    S_C^0(k)=z [[0,C_D^(c)],[C_D^(c),0]],
    ||S_C-S_C^0||<=e,  e=13eta²+5zeta.                (1)

This is an operator bound on both sides, both c paths and arbitrary coherent D/reference. For clarity, the parent Schur elimination uses alpha=D0/(D0-E), beta_S=D0/(D1-E), with E<=3j. Its channelwise bound is

    4(alpha-1)+4beta_S
       <=12eta²/(1-3eta²)+4zeta/(1-3eta²zeta)
       <=13eta²+5zeta.

Thus the domain and all inactive-cell corrections in (1) are retained. The symbol beta_S in this displayed check is a dimensionless Schur coefficient, not the hopping beta.

### Writing and scalar modules

The actual writer has24 heads and34 listed positive blocks:18 ordinary arm exchanges, two strengthened phase-cell exchanges, four signed real junction exchanges, four phase occupations, four junction vacancies and two terminal contacts. For an ordinary target D the contacts are j n_T(I+X_D), of norm2j. Both contact the SAME D. Its scalar is c_R=4(sqrt(2)-1)j. Full two-port scattering satisfies

    S_W^0(k)=phi(k) [[0,X_D],[X_D,0]],
    phi(k)=-i z^22,  ||S_W-S_W^0||<=w=33d.          (2)

This includes incidence from either port and arbitrary target/reference states. To make an identity module with the SAME comparator phase, replace both terminal contacts by the onsite positive term2j n_T. This is precisely the writer's target-X=+1 specialization; it uses no dummy |+> qubit. It has the same24 heads,34 blocks, c_R and error ceiling, with I in place of X_D. No three-body target-controlled hopping is supplied.

All stated positive blocks are positive semidefinite as operators. They are real matrices, but this does not assert stoquasticity or entrywise-positive matrix elements. Signed exchange terms in the writer remain part of its actual implementation.

## 2. Exact CNOT and SWAP words, including the auxiliary path

For a fixed logical path b, define the paired writer on auxiliary path a by

    W_P=|0><0|_a tensor I_P+|1><1|_a tensor X_P.

The a=0 module is scalar and a=1 module writes P. They have identical comparator phase phi. The proposed three-stage word, in forward order from right to left as operators, is

    F_(Q->P)=C_Q^(a) W_P C_Q^(a).                    (3)

On a computational basis vector (a,q,p), the first core sets a'=a xor1 xor q, the writer changes p to p xor a', and the second core restores a. Hence

    F_(Q->P): (a,q,p)->(a,q,p xor q xor s),
    s=1 xor a.                                      (4)

For a=1 this is CNOT_Q->P; for a=0 it is the zero-controlled flip. Equation(3) is a self-adjoint unitary on the ENTIRE a,Q,P space, not only the selected entrance a=1. No phase depends on q,p,a. An analogous F_(P->Q) exchanges Q and P in the roles of control and target.

Now send the head through F_(Q->P), F_(P->Q), F_(Q->P). Since each completed module restores a, the same s applies in all three. The data bits successively obey

    p1=p xor q xor s,
    q2=q xor p1 xor s=p,
    p3=p1 xor q2 xor s=q.

Therefore the exact complete comparison word is

    L=F_(Q->P) F_(P->Q) F_(Q->P)
      =I_a tensor SWAP_QP.                           (5)

The auxiliary a=0 branch also gives SWAP; it does not leave extra X_Q X_P factors. This stronger identity follows by explicit cancellation of both s terms. Basis equality extends linearly to arbitrary a,Q,P/reference entanglement. The loader reverse word is the reverse of the nine individual involutions. It equals L*=L; no core control is treated as a conserved global classical label, since the interspersed writers change Q and P.

Implement two copies of each loader stage's HEAD geometry, one for each logical b, with the same ordinary Q and P. Their head sites are disjoint but their physical data qubits are shared. The resulting ideal loader is I_b tensor I_a tensor SWAP_QP. This is a direct sum over head lanes on a shared data fiber, not fanout or two copies of Q/P.

## 3. An explicit eleven-stage complete operation graph

Retain all four channels through the whole network. After the nine loader stages, install two P-controlled cores acting on b, one for each a. Then install four writing modules, one per (a,b), ALL contacting the same R. This modest duplication keeps the complete ideal operation independent of a; no auxiliary path is closed, merged, projected away or silently discarded.

| Stage | Ideal forward factor on the shared fiber/path | Actual modules |
|---|---|---|
|1|C_Q^(a)|Two cores, one per b|
|2|W_P|Two writing-P and two scalar writers|
|3|C_Q^(a)|Two cores, one per b|
|4|C_P^(a)|Two cores, one per b|
|5|W_Q|Two writing-Q and two scalar writers|
|6|C_P^(a)|Two cores, one per b|
|7|C_Q^(a)|Two cores, one per b|
|8|W_P|Two writing-P and two scalar writers|
|9|C_Q^(a)|Two cores, one per b|
|10|C_P^(b)|Two cores, one per a|
|11|X_R|Four writing-R modules, one per (a,b)|

At each gap s=1,...,10, join the four right port origins to the corresponding four left port origins of the next stage by four ordinary j cables. All four cables at that gap have the SAME integer length L_s>=1 edges and disjoint interiors. Each endpoint belongs to only its own module, so even L_s=1 is an actual new bond between two distinct sites. There are four incoming external rays and four outgoing external rays, each an ordinary semi-infinite j chain. These are stationary comparison rays, not a finite source installation.

Every local module in a stage has the same scalar comparator phase: z at each of the seven core stages, and phi=-i z^22 at each of the four writer stages. The fact that there are two or four parallel MODULES does not multiply the transmission phase: the head passes through one branch of their direct sum. Their actual vacuum energy scalars, however, DO add over every installed module.

Let G_s be the eleven self-adjoint unitary factors in the table, with identity factors on unused data. The ideal forward and backward words are

    U_f=G_11 ... G_1
       =I_a tensor [X_R C_P^(b) SWAP_QP],
    U_b=G_1 ... G_11=U_f*
       =I_a tensor [SWAP_QP C_P^(b) X_R].             (6)

In particular the final P-control acts AFTER the swap, so it is controlled by the original Q input. The entire forward word need not equal its backward word; replacing U_b by U_f would be wrong. Each local primitive has the same scalar transmission phase from either side. Combining those phases and the cable propagations gives

    z^7(-i z^22)^4 product_s z^L_s=z^D,
    D=95+sum_(s=1)^10 L_s,
    S_net^0(k)=z^D [[0,U_b],[U_f,0]].                (7)

The exterior order is left then right, with four (a,b) channels on each side and the common Q,P,R data fiber. Both directional blocks use the SAME z^D, while their operator words are adjoints. For L_s=1 the exponent is105 and the band-center common transmission phase is+i. There is no fitted column-dependent phase.

There are fourteen actual cores and sixteen actual writers, including six scalar writers. The full occupation expansion therefore gives the true head-vacuum scalar

    c_net=14(8beta)+16c_R
         =112beta+64(sqrt(2)-1)j.                   (8)

It is the same for every data state and head position. Ordinary cables add no constant. The physical evolution is exp(-ic_net t) times that generated by the scalar-subtracted one-head Hamiltonian. A time-dependent outgoing comparator, if later constructed, must retain both this phase and z^D. No independent record or program aging phase is supplied here.

The shared-data construction is physically meaningful at the algebraic level: after subtracting (8), every module's interaction vanishes on its head vacuum. Thus a head outside a module experiences no data evolution from that module. The local stationary matrices can be composed at one common k on the SAME eight-dimensional Q,P,R fiber. Q and P need not commute with the full network Hamiltonian. Decomposing the whole device into separately conserved Q or P sectors would be invalid; this derivation never does that.

## 4. Full operator feedback and wrong-output estimate

Take the direct sum S(k) of all eleven stage scattering matrices, tensoring each with all unused data factors. At each core stage the two parallel modules have full error at most e, and at a writer stage the four parallel modules have error at most w. A direct sum takes the maximum. Consequently

    ||S-S^0||<=delta,  delta=max{13eta²+5zeta,33d}.   (9)

This is not an assumption of one-pass transmission by the actual apparatus. It covers every incident port of every stage and arbitrary coherent data inputs, including those changed by a previous reflection or writer.

Split the stage ports into eight external ends and eighty internal ends (ten gaps, four cables per gap, two ends per cable). Every end carries the same data fiber. Let P_c pair the internal ends with phase z^L_s. It is unitary. If x is the exterior incoming amplitude and y the interior incoming amplitude, exact stationary matching is

    y=P_c(S_ie x+S_ii y),
    A=P_c S_ii, B=P_c S_ie, C=S_ei, D_e=S_ee,
    S_net=D_e+C(I-A)^-1 B.                           (10)

In the reflectionless comparator, each internal step progresses monotonically leftward or rightward toward an exterior exit. Its path/data unitary may change a,b,Q,P,R, but cannot reverse that direction. Hence (A_0)^11=0 even though the successive data factors do not commute, and

    R_0=(I-A_0)^-1=sum_(m=0)^10 A_0^m,
    ||R_0||<=11.

If 11delta<1, the resolvent identity and Neumann bound give

    ||R||=||(I-A)^-1||<=11/(1-11delta),
    ||R-R_0||<=11delta ||R||.                        (11)

Every external/internal block of a local unitary is a contraction, and each block difference is at most delta. Subtract (10) in the fixed order

    S_net-S_net^0=(D_e-D_0e)+(C-C_0)RB
                  +C_0(R-R_0)B+C_0 R_0(B-B_0).

Its norm is bounded by delta+delta||R||+11delta||R||+11delta. Therefore

    ||S_net(k)-z^D [[0,U_f*],[U_f,0]]||
              <=144delta/(1-11delta).                (12)

All data operators remain in their actual order in this proof. The inverse pays repeated interstage returns and cannot be replaced by a scalar selected-branch denominator. Local flux conservation, summed over stages with cancellation of the paired internal fluxes, makes the exact exterior map an isometry; it is square and hence unitary. Equation(11) rules out an internal PORT-feedback pole on the specified band. It does not classify port-invisible localized states or assert global spectral completeness.

For a fixed common spectral envelope f with integral|f(k)|² dk=1 and support in this band, pointwise multiplication and integration give outgoing-CHANNEL norm error at most the right side of(12). Any output projector annihilating the ideal outgoing state has probability at most its square. Examples for input a=1,R=0 include reflection to the incoming side, outgoing a=0 and R=0. The coherent logical/data error is already included in(12), even when no classical wrong-b projector is appropriate. These are asymptotic channel statements, not probabilities at a finite laboratory time.

One explicit arbitrary-accuracy parameter choice is useful solely to show that the stationary domain is nonempty. For 0<epsilon_stat<=1 put

    d_star=epsilon_stat/(144+11epsilon_stat),
    eta²=d_star/52, zeta=d_star/20,
    |k-pi/2|<=d_star/33.                             (13)

Then e=d_star/2, w<=d_star, the primitive domains hold, 11delta<1, and (12) is at most epsilon_stat. In particular d_star/33<10^-3, eta<=1/8 and zeta<1/4. This selects ever weaker couplings and a narrower incident band as accuracy increases. It asserts neither a finite prepared packet nor a favorable duration or energy-resolution cost.

## 5. Full data/reference action and the old-state relocation

In coordinate order (a,b,Q,P,R), equation(6) acts as

    |a,b,q,p,r> -> |a,b xor(1-q),p,q,r xor1>.         (14)

This is the entire basis permutation, with the common scattering phase(7) outside it. The old value p is in Q; it has not been overwritten or discarded. Since(14) is an operator equality, arbitrary entanglement of old P with a passive E is relocated to Q/E. Arbitrary incoming program/path/reference coherence is preserved as well. The proof does not measure Q, identify it with a classical control, or give separate fitted phases to its columns.

For comparison with the parent's input semantics, one may supply arbitrary logical Q/b/reference input, a=1, R=0 and a fixed old joint state sigma_PE. The ideal rightgoing output retains a=1, puts the original Q program in P, applies C_0=X_b,C_1=I_b, has R=1, and retains sigma_QE with all its correlations. Both left and right head channels and the whole Q,P,R,E/reference output are kept in the actual scattering comparison. Tracing out Q or E is not part of the result. If R is initially unknown, the exact ideal action is X_R on that state, not reset or preparation of record1.

This matches the parent's logical PERMUTATION and old-state accounting, not its actual biased finite Hamiltonian, radial target, input emitter or timing theorem. The boundary-input source b58d was read for those distinctions. Here the input is still a supplied one-head channel input; conversion from an ordinary path qubit, attachment, blank-head preparation and a finite launch are not derived. E is passive. An active old H_PE, receiving penalties, a record bias or any other head-independent data dynamics invalidates the freely degenerate channel premise and requires a new argument. No hidden aging term is removed by calling E a reference.

## 6. Actual counts and full-support incident loads

Fourteen cores contribute112 heads and336 blocks. Sixteen writers contribute384 heads and544 blocks. Their head sets are disjoint. There are ONLY three ordinary data qubits Q,P,R, shared across all the modules; targets and core controls are not counted anew per module. Before cables this gives

    496 head qubits+3 data qubits=499 qubits,
    880 listed positive blocks.

There are four cables of length L_s at each gap s. With their endpoints already in the module count, the total finite interaction region is

    head count=456+4 sum_s L_s,
    qubit count=459+4 sum_s L_s,
    block count=880+4 sum_s L_s.                     (15)

These counts exclude the exterior rays. For the simple fixed graph L_s=1 at all ten gaps there are496 heads,499 qubits and920 blocks, before adding any exterior ray sites/bonds. Six scalar writers are included at the same34-block convention; replacing a contact by an onsite2j n_T does not reduce that listed count. No source, cap, bias, uniform penalty, cooling device or preparation apparatus is counted or claimed installed.

The ordinary shared-control burdens are substantial. Q controls eight cores and is written by two writers; P controls six cores (including both final logical cores) and is written by four writers; R is written by four writers. Every core control contributes FOUR distinct M blocks and each writing target contributes TWO terminal blocks. Thus the actual full-support incident norm sums are

    Q: 32(D1-2beta)+8j,
    P: 24(D1-2beta)+16j,
    R: 16j.                                         (16)

All those blocks are paid even though a single head visits only one site at a time. Other conservative local sums, with one external/cable bond at a module port, are core endpoint6beta+4j, core mediator D1+2beta, writer head<=12j, ordinary cable/ray interior4j. Full support, including multiple head occupations, is used for all norm sums; the operational scattering statement remains a one-head statement.

For a common cap Lambda>0 a sufficient choice is

    D1=Lambda/64, D0=zeta D1, beta=eta D0,
    0<zeta<=1/4, 0<eta<=1/8.

Then beta<=D1/32 and j<=D1/256. Equation(16) is bounded respectively by Lambda/2+Lambda/2048, 3Lambda/8+Lambda/1024 and Lambda/1024, all below Lambda; all displayed head sums are smaller. This pays the many shared contacts by lowering their common scale. It does not keep the old physical times or import the one-core scale convention unchanged.

## 7. Geometry: a literal NN obstruction and a finite-range alternative

In this SPECIFIC graph Q has32 distinct mediator neighbors and four distinct writer-terminal neighbors, hence degree36. P has24 mediator and eight terminal neighbors, hence degree32. R has eight terminal neighbors, hence degree8. Module heads are distinct by construction; merging them would change both the Hamiltonian and scattering network. Head vertices have degree at most3, and cable/ray interiors degree2. Thus the graph has bounded maximum degree36, but Q, P and R each violate the six-neighbor cubic NN constraint.

This is a definite obstruction to embedding this literal repeated-module/shared-control graph as cubic nearest-neighbor two-body interactions. Routing a long wire for a controlled block does not solve it without an additional mediator construction and error analysis. Replacing Q or P by many correlated controls would reinstate a preparation/encoding premise and is not what was proved. This degree argument is not a no-go for every direct two-body loader, reuse of a core, another graph architecture, or a different control-routing mechanism.

There is a simple explicit bounded-range realization if longer supplied pair blocks are allowed. Set every L_s=1. Enumerate the499 distinct qubits of the declared graph in any fixed order, and place vertex i at(i,0,0), i=0,...,498, on a cubic lattice. Install precisely the declared two-qubit blocks between their assigned sites and the declared onsite terms. Every internal pair distance is at most498; every unused interaction is absent by supply. From each of the eight distinct exterior-port vertices at x=x_p, attach its own ray(x_p,0,n), n=1,2,..., with ordinary NN j bonds. These eight rays are disjoint, meet no other vertex of the interaction region, and require only unit extra range.

This gives a coarse range498, degree36 one-/two-body installation with fixed finite interaction-region size, independent of accuracy. It changes the geometric supply from the primitives' separately displayed NN patches to allowed finite-range pair blocks; it does not derive that longer-range supplier from the native lattice. The line arrangement is deliberately unoptimized. Treating it as a range1 or inherited range35 realization would be false. Alternatively the theorem can simply be read on the abstract bounded-degree graph, without a physical spatial metric.

## 8. Remaining finite and physical obligations

The new word and full feedback estimate establish a source-exposed stationary construction to be checked. They do not imply any of the previous finite-device resource exponents. In particular the following remain separate obligations:

- Build and normalize a COMPLETE physical packet on this new graph, including all496 internal head coordinates and the Q,P,R fiber. Derive its regularity/derivative estimates and deal with any localized-state contributions; exterior-channel unitarity is not a bound on finite-time internal occupancy.
- Supply actual finite input endpoints, the physical dual-rail/auxiliary-path encoding and blank rest, and prove early matching from that endpoint seed to the full packet. No freely prepared incoming spectral envelope is counted as product-source preparation.
- Choose actual ray cuts/caps and pay their contact returns, the full final outgoing packet restriction and normalization, all residual input/core/writer/cable populations and the phase(8). Derive a positive-width observation window and actual duration/counts for those choices.
- Derive any all-time absolute record branch or normalized-success statement separately. R can rotate during a terminal visit and can be flipped back on a return; it is not an irreversible completion latch or an arbitrary-time herald by its name.
- Resolve a desired NN or smaller-range realization if that is the physical contract. The range498 graph above is a different supplied installation; it cannot be called an already constructed native NN apparatus.

The only input data other than the logical program/path and retained old P is the ordinary record (blank only if record1 is desired). No signed cat or ancillary entangled data register appears. That removes the CAT premise from this stationary conditional model, not every preparation or interaction-supply premise from an actual device. Positivity alone supplies neither cooling, input encoding, exact correlated coefficients, readout, an old-environment decoupler, nor native physical identification.

## 9. Exact sources, read coverage and exposure

N denotes /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. W denotes /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree. The following complete texts were read at the exact hashes below; hashes were refreshed in this task. The two initially truncated combined review outputs were reread in full with sufficient output space. No truncated output is counted as complete coverage.

| Source | SHA256 | Use here |
|---|---|---|
|N/common_product_autonomous_cat_preparer/PROPOSAL.md|d4e708583626102d5f09d6f98c56e25fadb36895fdb437d07b69c0e345ef96af|Scalar writer, common data fiber, feedback method and scope|
|N/common_product_autonomous_cat_preparer_check/REVIEW.md|1f606fc5146becf42420d36411011d2a376b121d0c44bd8a7e1dad2c5f6fd59f|Checked local and abstract-network scope of that source|
|N/common_product_stage_separated_router/PROPOSAL.md|60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182|Full reciprocal core phase, band and error|
|N/common_product_stage_separated_router_check/REVIEW.md|8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d|Distinct core check at that scope|
|N/common_product_single_control_router/PROPOSAL.md|76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01|Actual one-control blocks, whole-support scalar and inventory|
|N/common_product_single_control_router_check/REVIEW.md|549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0|Distinct one-control check; its finite transfer is NOT imported|
|W/outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md|93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56|Full writer, positive inventory, exact common phase and33d bound|
|W/outputs/attached_record_2026_10_17/source_checks/autonomous_record_route_check/REVIEW.md|c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a|Distinct local writer check and completion limitations|
|N/common_product_boundary_input_contract/PROPOSAL.md|b58d047e8b7d6598951f84cb5c275d9709fe19b9b99e0383558536b581332ad9|Comparison of input/old-state semantics ONLY; no finite, bias or energy theorem imported|

ROOT proposed testing C_Q W_P C_Q followed by the three-CNOT SWAP word and coherent duplication of the head lanes. The present author read that favorable candidate and the parent arguments before deriving this proposal. The new work is the whole auxiliary-path word, eleven-stage all-port composition, common phase/scalar, complete shared-data loads/counts and the explicit geometry restriction. Prior checks of primitives do not independently check those new steps. No blind independence, retained status or final acceptance is claimed; a distinct check is required.

Only this PROPOSAL.md was written. Work used analytical derivation, complete text reads and deterministic path/size/SHA256 bookkeeping. No scientific executable, simulation, numerical solver, parameter sweep, Git/W/checkpoint/axiom/editable-prompt change, publication, model override or delegation occurred. No editable prompt file changed.

