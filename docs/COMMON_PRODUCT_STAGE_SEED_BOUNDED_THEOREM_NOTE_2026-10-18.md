# A finite seeded router with distinct input and output stages

Claim status: bounded_theorem. Conditional mathematical result with distinct analytical checks and source-exposed ROOT integration. No retained audit or native realization is asserted.

Four literal positive program cells separate two input paths from two output paths. The finite construction starts with a head at an input emitter and compares the complete evolved state with one common normalized packet on the output paths only. Its supplied parameter family retains the preceding microscopic certificate's sufficient size exponent four and physical time exponent six. This is a different physical layout with a newly checked interface, not a transfer by analogy. It provides a place to attach a downstream record writer; no writer or completion signal is part of this theorem.

## Supplied device and input contract

Use the literal full-support positive cell from the [parent microscopic certificate](COMMON_PRODUCT_MICROSCOPIC_SEED_BOUNDED_THEOREM_NOTE_2026-10-18.md). In particular, Q_c(u,v)=c(n_u+n_v-a_u^dagger a_v-a_v^dagger a_u) includes the double-occupation diagonal 2c. Each cell has two endpoint heads, one mediator, three distinct controls, endpoint vacancy terms b(1-n_u)+b(1-n_v), a combined controlled mediator block with coefficients D0-2b,D1-2b, and endpoint blocks 2j P0 n, where j=b²/D0 and D1>D0>2b>0.

Install the four cells on the edges of K2,2 with endpoint sets (I0,I1) and (O0,O1). Their mediator and control qubits are distinct. Legal logical program p=0 enables the cross matching and disables the straight matching; p=1 does the reverse. A cell's three controls are 000 when enabled and 111 when disabled. These twelve supplied controls encode one logical bit. Their preparation and arbitrary logical coherence are premises, not outputs of the device.

A nearest-neighbor cubic placement is I0=(0,0,0), O0=(2,0,0), I1=(2,2,0), O1=(0,2,0), with mediators at the four edge midpoints. Place each straight-cell control one step in +z from its corresponding head and each cross-cell control one step in -z. All twelve controls are distinct. The four rays leave I0 in -x, O0 in -y, I1 in +x and O1 in +y. Incidental lattice adjacency does not install an interaction. The construction supplies the absent couplings.

Each ray has sites n=0,...,M, with endpoint at n=0, ell=M-1, ordinary Q_j bonds through ell, and the compensated outer block

    B=Q_gamma(ell,M)+(j-gamma)n_ell+(2j-gamma)n_M,
    0<gamma<j.

The outer block has full-support norm 3j. All four emitters physically exist, but the initial head occupies only I0/M or I1/M according to the supplied encoded input. Every other head is initially vacant. Arbitrary passive references and coherent legal programs are included.

Write C0=X_path,C1=I_path and C=sum_p |p><p| tensor Cp. The target is a common radial packet beta_F(t) on 0<=n<=ell of the O paths, acted on by C. Every I head, all four emitters and all four mediators are vacant in the target. Programs are unchanged. The exact common physical scalar is 8b, and the comparison retains exp(-i8bt). It does not project or renormalize the actual output.

## Exact microscopic four-port calculation

On the one-head space with uniform infinite rays, subtract 8bI. Let R be the enabled perfect matching and S the disabled matching. These are commuting real involutions on the four endpoints. With E=2j(1-cos k), z=exp(ik), alpha=D0/(D0-E), beta=D0/(D1-E), elimination of all four mediators gives

    V=2I-alpha(I+R)-beta(I+S),
    Sphys=(z^-1 I-I+V)^-1 [(1-z)I-V].

Its ideal comparator is zR=z[[0,Cp],[Cp,0]], including incidence from either stage. Thus it is reciprocal, not an isolator. For eta=b/D0<=1/8, zeta=D0/D1<1/2 and pi/3<=k<=2pi/3,

    ||Sphys-zR|| <= 13eta²+5zeta.

The errors add; replacing this sum by the two-port maximum is not justified. The four joint eigenchannels of R,S reduce the formula to the exact scalar Robin reflection coefficient. All mediator denominators stay separated from zero on this band. At least four high bound states exist; no global spectral completeness or zero seed overlap with bound states is presumed.

Put Q=z^-1 Sphys and delta=eta²+zeta. The finite proof reconstructs

    ||Q'||<=260delta, ||Q''||<=4600delta,
    ||Rmed||<=5eta, ||Rmed'||<=600eta,

where Rmed is the complete four-mediator map from incoming channel amplitude. These are full-fiber operator bounds, including coherent program sectors.

The exact normalized packet uses the same phase-sensitive standalone emitter amplitude and fixed cutoff as the parent, but includes four rays and all four mediator coordinates. Its norm follows from exact strong evolution and incoming separation in the remote past. This packet-specific isometry does not assume completeness. For g=chi F/||chi F||, define Gr=||g^(r)||_1. The new outgoing and mediator envelopes are

    H0=G0,
    H1=G1+260delta G0,
    H2=G2+520delta G1+4600delta G0,
    J0=5eta G0,
    J1=5eta G1+600eta G0.

All unchanged scalar launch estimates retain their exact source hypotheses and phase convention.

## Finite source, full error and resources

The reference for early matching consists of four independent launchers and four isolated mediators, on the same extended space as the actual operator. The seed lies in its launcher invariant subspace, where the reference norm is at most 4j. The norm of the actual/reference contact difference is at most 2j+2b; the actual large mediator generator is controlled through unitarity. Reaching contact from the emitter takes at least M steps. Thus

    Eearly <= min(2, u0(2+2/eta) sum_{m>=M}(4u0)^m/m!),
    u0=j t0.

This pays the microscopic 1/eta factor. It is a full-vector match and therefore pays omitted localized components without identifying finite and infinite spectral projections.

The exact finite/infinite outer difference on each ray is hopping-only:

    Delta=(j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2).

No diagonal changes. The four-ray direct sum has the same contact norm sqrt((j-gamma)²+j²); dimension does not insert a factor four. Twice integrating the boundary packet columns by parts gives the outer allowance Eouter. The complete source supplies all endpoint envelopes, positive-gap conditions and the output normalization argument. In its notation the bound is

    sup_{t-<=t<=t+} ||exp(-itH) Eseed
       -exp(-i8bt) J_O(beta_F(t) tensor C)||
       <= min(2,e0+Eouter+2dpacket+2dO).

Here e0 includes early contact error, full standalone launch error, right tail, and early lead/mediator matching; dpacket includes late incoming amplitude, 13eta²+5zeta and late mediator amplitude. The finite outgoing normalization dO is paid separately. The common O packet is not conditioned on success.

For Lambda>0 and 0<epsilon<=1 choose

    rho=epsilon/256,
    u0=10^12 rho^-2 epsilon^-2,
    ell=ceil(100u0), M=ell+1,
    eta²=zeta=epsilon/1024,
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b²/D0, gamma=rho j,
    t0=u0/j, t-=3ell/(4j), t+=7ell/(8j).

The twelve checked allocations each lie below epsilon/16, yielding complete error below 3epsilon/4. Changed allowances include Eearly<=1/(50u0 sqrt(epsilon)), early mediator<=3500eta/(rho ell), late mediator<=7100eta/(rho ell), and 2dS=36epsilon/1024. In particular dpacket<4epsilon/64<1/2 before output normalization is used. These changes are explicitly checked rather than inherited from the two-port estimate.

There are 24+4ell qubits and 32+4ell combined positive blocks. Core endpoint incident load is 6b+6j, mediator load D1+2b, program loads 2j or D1-2b, lead-interior load 4j, source-adjacent load 5j and emitter load 3j. Every sum is below Lambda in this family. Auxiliary reference sites are not resources. Exact j=Lambda epsilon²/2^21 and gamma=Lambda epsilon³/2^29 give sufficient size Theta(epsilon^-4) and physical time Theta(Lambda^-1 epsilon^-6). The window has relative width 1/6. The constants are enormous, and the smallest displayed coefficient magnitude is not a fabrication tolerance or production cost.

## Evidence and open interfaces

The source core is 60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182, with distinct review 8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d. The finite proposal is 340b724d949f9c88da332209e200c2e593b89b68a1a1e02caf5ba9cebbef44f2; its distinct check is 6f99b759c1d2a97a55b81a3d954c8721f0b07ec167564619b0a470fa1b676314, fully read by ROOT, with no required correction. The parent integration revision is PR9705 d1f15561e9a50cc811e73d4ba481f89899fe82b5. Complete new arguments, scoped reviews and inherited source mappings accompany the final note in the [portable evidence manifest](../outputs/common_product_stage_seed_2026_10_18/SOURCES.json).

The author constructed both core and finite extension. ROOT read their full arguments; the distinct checker has access to the sources and prior shared premises. These are same-model source-exposed checks, not blind/model-diverse replication or retained audit. ROOT integration and hash/count checks add no independent scientific status.

The result depends on supplied positive local blocks, exact correlated coefficients, occupation/role assignments, absent couplings, vacant-head preparation and encoded input/program coherence. It does not implement the old literal processor or derive native Hamiltonian/Record identities. No downstream record writer, all-time completion guarantee, capture, permanent finite-device storage, reset, robust coefficient tolerance or new physical law is established. A finite observation interval is still selected; no Hamiltonian switch occurs at either endpoint. Later finite returns remain possible.

All scientific checks for this finite-seed result were analytical. No scientific executable, dynamics simulation, parameter sweep or numerical operating point is claimed. Separate ongoing record-attachment geometry diagnostics are not evidence for this theorem. No physical axiom or editable prompt changed.
