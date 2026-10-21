# A coherent cat-preparer scattering network and its remaining finite interface

New source-exposed author derivation requiring a distinct check. The proposed splitter, four writer stages and one controlled core have a consistent full-fiber stationary composition, including multiple reflections and a common outgoing phase. Its ideal column maps a single input path and four blank target qubits to cat+ with the same output path. This source DOES NOT close an endpoint-seeded finite autonomous preparation theorem: a collision-free combined cubic embedding and the modified network's complete packet/finite-transfer estimates remain open. No prepared incoming packet is counted as product-state preparation, and no continuously coupled receiving gadget or timed handoff is claimed.

## 1. A positive real reflectionless splitter

Use four distinct head endpoints I0,I1,O0,O1 and the real Hadamard matrix

    H=(1/sqrt(2))[[1,1],[1,-1]].

For each pair I_a,O_b install a signed exchange block of magnitude j/sqrt(2) with hopping -j H_ba. A signed exchange has positive occupation diagonal a(n_u+n_v), off-diagonal hopping +-a, and full norm2a. At EACH of the four endpoints add the positive vacancy repair

    c_v(I-n_v), c_v=(sqrt(2)-1)j.

Attach one ordinary Q_j lead at each endpoint. The two internal bonds supply diagonal sqrt(2)j, the vacancy subtracts c_v n_v, and the lead supplies j, so the one-head endpoint diagonal after subtracting the TRUE scalar4c_v is2j. Internal hopping is -j V with

    V=[[0,H],[H,0]], V*=V, V^2=I.

For E(k)=2j(1-cos k), radial waves z^-n in+z^n out, z=exp(ik), the boundary equation is that of V_p=I-V. In each V eigenchannel v=+-1 direct substitution gives S=zv. Hence the EXACT splitter scattering is

    S_split(k)=z[[0,H],[H,0]], 0<k<pi.                 (1)

There is no reflected component at either side. This is not a supplied many-qubit controlled hopping. The square embeds in a cubic unit plaquette with I0=(0,0,0), I1=(1,1,0), O0=(1,0,0), O1=(0,1,0); its four installed links are nearest-neighbor. Distinct outward rays can leave in separate directions/layers. At a vertex its full incident norm sum, including one lead, is(3sqrt(2)+1)j<6j. It has four head qubits, eight internal positive blocks and common scalar4c_v. The signs in H's first column are both positive; this fixes the eventual cat sign.

## 2. Four genuinely ordinary targets and paired writer stages

Let A1,A2,A3,A4 be four ordinary physical qubits, initially0000, with NO free data Hamiltonian. For each a use two copies of the checked24-head writer geometry93445. The branch1 copy couples its two terminals to the single qubit A_a with the displayed positive contacts j n_T(I+X_Aa). It implements

    S_write,a(k)=phi(k) X_port tensor X_Aa + error,
    phi(k)=-i z^22,
    ||error||<=w:=33d, d=|k-pi/2|<=10^-3.             (2)

The bound is the full reciprocal two-port/data operator bound, including all unwanted reflection. It holds for arbitrary coherent target input, not only a classical bit. Branch0 uses the SAME writer head geometry, arms, phase cells, junction and repairs, but replaces each terminal contact by the ordinary positive onsite2j n_T. This is exactly the scalar X=+1 sector of the writer. No dummy |+> qubit or entangled initialization is supplied. Its comparator is phi(k) X_port tensor I_Aa with the SAME error ceiling and scalar c_R=4(sqrt(2)-1)j. The scalar specialization's terminal norm remains2j, so its positive inventory and load estimates remain valid.

The two parallel copies form one four-port stage. Its ideal forward and backward path/data action is

    W_a=|0><0|_path tensor I+|1><1|_path tensor X_Aa.

The stage matrix is phi[[0,W_a],[W_a,0]], and its operator error is at most w: the norm of a direct sum is the maximum, not the sum. All other targets and passive references are identities. Eight physical writer modules are used in total; four have an actual target and four are scalar modules. Each A_a receives two physical terminal contacts, total full-support load4j. The two terminals in a writing module use ONE target qubit, not two copies of its state.

## 3. Controlled recombination without discarding the path

Use the one-control physical core76b5 with its actual program qubit identified with A1. The core has four distinct external ports, four mediators and the same static positive blocks. On the central band its full stationary comparator is

    S_core(k)=z[[0,C_A1],[C_A1,0]]+error,
    C_A1=|0><0|_A1 tensor X_path+|1><1|_A1 tensor I_path,
    ||error||<=e:=13eta^2+5zeta,                       (3)

under eta=b/D0<=1/8 and0<zeta=D0/D1<1/2. This follows from the checked four-port core60bc and exact one-control intertwiner76b5. The A1 degree now includes two writer terminals and four core mediator controls. Its total listed norm load is4j+4(D1-2b), not the old isolated program load alone.

There is no global conservation of A1 occupation: the upstream writer flips it. Formula(3) is used as a LOCAL scattering operator on the full16-dimensional data fiber; the composite device is not split into classical program sectors. All data are freely degenerate when the head is outside these contacts: the controlled blocks contain a head occupation, and the only vacuum contributions are common scalars. Thus all segments have the same k and velocity for all data values. There is no record bias or receiving-gadget ZZ penalty in this proposed standalone network.

Order the six stages from left to right as splitter, W1,W2,W3,W4, core. Between neighboring stages connect the two corresponding paths by ordinary uniform cables of identical length L_a edges within that gap, a=1,...,5. Define the convention so traversal contributes z^L_a between the port-origin reference planes. The ideal forward word and reverse word are

    U_f=C_A1 W4 W3 W2 W1 H_path,
    U_b=H_path W1 W2 W3 W4 C_A1=U_f*.

The full ideal external four-port matrix is

    S0(k)=z^D [[0,U_b],[U_f,0]],
    D=90+sum_(a=1)^5 L_a.                             (4)

Indeed four writer phases multiply to(-i)^4 z^88=z^88; splitter and core supply one z each. Equal paired cables prevent a relative branch phase. On the specified product input,

    U_f |0>_path|0000>_A
       =|1>_path (|0000>+|1111>)/sqrt(2).              (5)

The first branch has A1=0 and path0, so the final core swaps it to path1. The second has A1=1 and path1, so it remains on path1. This is a coherent reversible operation on the full path/data space, not a classical routing instruction, measurement, erasure or postselection. The known common z^D has no data dependence. No ancillary cat state is used by these local primitives.

## 4. Exact feedback and a full-fiber stationary bound

The following calculation is on the abstract connected port graph just specified. It does not assume an unproved cubic placement of that entire graph. Let S be the block direct sum of the six actual stage matrices, with identities on all unused target fibers. Its ideal direct sum is S^0. Every local segment is unitary on real k; cable propagation is unitary. With

    delta=max{e,w}, ||S-S^0||<=delta,

split the external and internal incoming/outgoing port spaces. There are four external ports and twenty internal directed port ends, all tensored with the full16-dimensional target fiber. Let P_c pair internal ends with their propagation phases; it is unitary. For an external incoming vector x, internal incoming y obeys

    y=P_c(S_ie x+S_ii y).

Put A=P_c S_ii, B=P_c S_ie, C=S_ei, D_e=S_ee. Then, whenever I-A is invertible, the EXACT composed external scattering is

    S_net=D_e+C(I-A)^(-1)B.                            (6)

This ordering is important because A1-dependent core operators and writer operators need not commute. Each restricted block has norm<=1, and each actual/ideal block difference has norm<=delta.

In the ideal network an incoming internal amplitude travels monotonically left or right through the chain until it exits. No ideal stage reflects. Consequently(A^0)^6=0 even though the ordered data operations do not commute. Thus R0=(I-A^0)^(-1)=sum_(m=0)^5(A^0)^m has norm<=6. If6delta<1, the Neumann identity around A^0 proves

    R=(I-A)^(-1), ||R||<=6/(1-6delta),
    ||R-R0||<=6delta||R||.

Subtract (6) from its ideal counterpart without commuting any factors:

    ||S_net-S0||
       <=delta+delta||R||+6delta||R||+6delta
       <=49delta/(1-6delta)=:epsilon_stat.             (7)

All internal returns are included in this inverse. There is no assumed absence of feedback poles: the explicit6delta margin supplies it for the internal port equations. The local core/writer maps also require their already checked real-band hypotheses. A bound-state invisible to the ports is not ruled out by(7); its preparation/evolution effect is among the remaining finite-state obligations.

The network scattering is unitary on the real band: flux conservation at each unitary segment and each unitary paired connection cancels every internal incoming/outgoing norm, leaving equal external norms. The invertible internal equations give a well-defined square external map; its isometry is therefore unitary. This argument is valid on the entire data fiber and all passive references. It does not assert asymptotic completeness of a Schrödinger wave operator.

For example choose0<d_band<=10^-3, eta<=1/8, zeta<1/2 with max{33d_band,13eta^2+5zeta}<1/6. Then (7) holds uniformly on |k-pi/2|<=d_band. These parameters may be made arbitrarily small with positive coefficients. For any normalized L2 spectral envelope f on this band, the external OUTGOING CHANNEL norm difference from the common profile z^D f in path1 tensor cat+ is at most epsilon_stat, by integrating(7) on the specified input column. Every wrong port and data component is included. This is a statement about the unitary stationary channel map; it is NOT a supplied physical incoming packet, a complete-time normalized state including internal heads, or an endpoint-seed theorem.

## 5. Positive inventory, cap, and the unresolved placement

On the abstract local graph each named module is an explicit real positive one-/two-body construction. The fixed scalar is

    c_net=8b+8c_R+4c_v
         =8b+36(sqrt(2)-1)j.                          (8)

The eight writers all have the same vacancy scalar, including the four scalar specializations. Cables add no scalar. A future physical packet comparison must retain exp(-ic_net t) together with z^D; neither is removed separately on different branches.

The splitter has4 heads/8 blocks; eight writers have192 heads/272 blocks; the core has8 heads/24 blocks; four target qubits include the already used core program A1. Before cable interiors there are208 qubits and304 blocks. Gap a has two L_a-edge cables and2(L_a-1) new heads. Therefore the finite module-and-cable graph, before the four external ray extensions, has

    198+2 sum_a L_a qubits,
    304+2 sum_a L_a blocks.                            (9)

All module port origins have already been counted. Formula(9) assumes distinct cable interiors and distinct module heads, and is conditional on a placement satisfying those conditions. It is not a count for an unprovided finite source/cut system.

One safe abstract incidence choice is D1=Lambda/16,0<zeta<=1/4,0<eta<=1/8, D0=zeta D1, b=eta D0, j=eta^2D0, also imposing the stationary smallness above. Then A1 has load4(D1-2b)+4j<Lambda, other A_a have4j, core endpoints6b+4j<Lambda, mediators D1+2b<Lambda, and every splitter vertex<6j. Writer loads are fixed finite multiples of j from the displayed inventory (a safe upper ceiling12j covers their junction, phase-cell and terminal heads); cable interiors have4j. These are full-support norms; they do not use a one-head row degree. All are belowLambda on this choice.

A complete collision-free nearest-neighbor layout of the combined network has NOT been supplied here. The highest-risk constraint is actual A1 sharing: its two writer terminals and four core mediators must occupy six DISTINCT neighbors of the same cubic site, while their head paths and paired equal-length cables remain disjoint. Degree six alone is not a construction. The independently embedded writer and core patches cannot simply be pasted at A1 without rotating/rerouting their arms and checking all port rays. The other target writers, scalar writers and splitter also require an explicit placement and equal-length connections; unused geometric adjacencies must stay uninstalled. No unbounded-degree target, duplicated A1, long-range bond or arbitrary crossing is silently introduced. Therefore(9) and the stationary network are presently an abstract locally specified port-graph candidate, not an achieved combined cubic device.

## 6. Decisive remaining finite-preparation obligations

To turn(5)--(7) into the requested autonomous product-seed preparation, the following work remains:

1. Freeze the actual cubic embedding including the six A1 neighbors, all disjoint cables and equal length conventions, source and output rays, with full norm/count/cap checks.
2. Derive the complete normalized stationary packet including all splitter, writer-arm, cable, core-mediator and target components. The ordered feedback is on16 target channels; global A1 conservation is unavailable. Internal derivatives and possible localized seed components must be paid explicitly, rather than importing970a's different two-writer/fixed-program packet theorem.
3. Place an actual weak endpoint source on I0 and a correctly matched unused I1 boundary, starting with one head at that source and all other heads and targets in product computational states. Prove full-vector source-to-packet matching, physical finite cuts/returns, a common normalized outgoing head profile, all remaining head vacancies, and a positive-width observation window. Any other incoming or bound-state component must be part of the error.

The existing standalone source and resonance machinery may help with the third step, but its global generator/contact constants and actual new internal maps have not been verified here. It would be false to call the outgoing spectral calculation a proof that a product source creates a cat autonomously. No runtime/resource exponent or finite success probability is claimed for this proposed network.

Even completing these steps would prepare a STANDALONE cat only. The four targets here have no permanent receiving-gadget H0_ZZ or data couplings. Installing those would change the free-channel energies, scattering and initial-state evolution; the present proof would not apply by analogy. Keeping a generated cat available, releasing its preparation head, and attaching/using it in a continuously coupled operating gadget without a timed switch remain separate interfaces. No autonomous handoff or preparation of the prior twelve operating cats is established.

## 7. Exact sources and exposure

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934; W=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree.

The complete writer source W/outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56 was reread here, including exact signed mixer, phase repairs, norm/scalar, explicit local geometry and33d whole-port estimate. Its later checked stationary scope is retained from reviewc5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a and subsequent checked writer/network usage; historical provisional prose does not become a new finite theorem.

The full needed four-port core operator/band/phase passage was refreshed from N/common_product_stage_separated_router/PROPOSAL.md60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182, whose complete earlier read and scoped review8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d are reused. The exact one-control source76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and review549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0 retain their complete prior reads, full head-fiber intertwiner and physical load premises. No new microscopic core approximation is asserted.

Finite/resonance source970a84e5e9157c6a9d5934f00df59491de19e6c88402efe0e14b44e68bc1479b and reviewcb0e278a7311651ea9f8d258089cba00a10fb03bb37457d2f8db1d5864af5da7 were previously read completely. They motivate the named finite-transfer obligations but are explicitly NOT imported as a theorem about this modified network.

ROOT proposed the Hadamard, four paired writers and A1-controlled recombination. This author derived the full ordered six-stage feedback bound and common scalar/phase/count interface after exposure to that design. ROOT subsequently emphasized nonconservation of the shared program and absence of receiving penalties; those restrictions are explicit above. This is source-exposed same-model author work, not independent validation. The supported new component is the stationary abstract-network calculation; the missing geometry and finite product-seed launch prevent a complete preparation claim. These are specific unfinished interfaces, not a universal no-go.

Only this proposal was created. No scientific executable, numerical sweep, delegation, old source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. A distinct check should inspect splitter signs/scalar, scalar-writer specialization, the noncommuting feedback inverse and ideal word, phase/reference planes, all-fiber error norm, and whether any claimed physical assertion exceeds the explicitly open embedding and finite-state obligations.
