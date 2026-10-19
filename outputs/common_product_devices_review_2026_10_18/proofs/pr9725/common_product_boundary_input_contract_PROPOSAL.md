# Direct boundary input contract for the enlarged-block router

New conditional author derivation, requiring a distinct check. The checked entrance-SWAP construction admits a complete channel theorem with an ordinary input program Q and the TWO physical emitter qubits as its supplied dual-rail path input. There is no intermediate loader in this contract. This changes the physical input specification; it does not implement conversion from an ordinary path qubit, prepare/attach the input, or produce the enlarged four-qubit interactions. A joint rest-state criterion suffices. An additional restricted initial-energy criterion is derived below without claiming an autonomous rest Gibbs preparation.

## 1. Physical tensor factors and supplied state

Use exactly c97b's finite Hamiltonian H_new, with the two entrance SWAP-conditioned positive bonds, one physical bias kappa n_R and, when specified, the uniform mu N. No coupling is switched during the interval. All parameters, ell, M=ell+1 and the finite operational hypotheses remain those of finite532866.

Let e0=I0,M and e1=I1,M. The physical input system is

    B = Q tensor e0 tensor e1.

Its legal subspace is Q tensor span{|10>,|01>}. Define the fixed mathematical identification

    J_B(|p> tensor |0>)=|p>_Q tensor |10>_(e0,e1),
    J_B(|p> tensor |1>)=|p>_Q tensor |01>_(e0,e1).       (1)

This is an input-space definition, not a physical encoding operation. The two rails may be arbitrarily entangled with Q and a passive reference Z. The rest A consists of EVERY other head, the old physical P and the shared R. E denotes a retained passive preparation environment; H_new acts identically on E,Z.

Supply a fixed normalized omega_AE independent of arbitrary logical/reference rho_LZ. The actual initial state is exactly

    (J_B tensor I_Z) rho (J_B* tensor I_Z) tensor omega_AE. (2)

No old P information is overwritten in (2). No apparatus marginal is substituted for its joint state with E. Every physical output B,A,E is retained. A preparation device or bath producing (2) is not specified; if it has additional outputs they must be included in E or another explicitly retained factor, with the stated independence and error criterion.

Put N_rest=sum_(head v other than e0,e1)n_v and

    Pi_rest=|vac_rest,0_R><vac_rest,0_R| tensor I_PE,
    q=Tr[(I-Pi_rest)omega], 0<=q<1,
    omega_0=Pi_rest omega Pi_rest/(1-q)
           =|vac_rest,0_R><vac_rest,0_R| tensor sigma_PE. (3)

The general purification/projection inequality gives

    ||omega-omega_0||_1 <= 2sqrt(q).                     (4)

One may instead supply any fixed sigma_PE and the direct joint bound ||omega-omega_0||_1<=epsilon_rest; that formulation does not require computing q. Under (3), epsilon_rest=2sqrt(q) is sufficient. The linear 2q replacement requires JOINT block diagonality of omega with respect to Pi_rest, not just a diagonal apparatus marginal.

With omega_0, (2) has exactly one total head and blank R; it is exactly the initial domain of the checked entrance-SWAP comparison. General omega may have additional heads and coherent errors. Those are retained and paid by trace-norm contraction of the full physical unitary, rather than by an unproved many-head gauge extension.

## 2. Complete channel and branch theorem

Let d(t) denote the parent's complete isometry error on its final window, and f(t) its absolute, unnormalized record-1 isometry error on the certified horizon. For finite532866,

    d(t)<3tau/8 on [3ell/(4j),7ell/(8j)],
    f(t)<tau/2 on [0,7ell/(8j)].                         (5)

Here tau is the parent's accuracy variable, with its entire parameter recipe retained. No new family or numerical point is selected.

The ideal complete output map places the logical program in physical P, applies C_0=X_path,C_1=I_path coherently to the path, uses the parent's positively normalized finite F radial sequence beta_F(t), has R=1, and leaves every other head INCLUDING e0,e1 vacant. The old sigma_PE is relocated losslessly to sigma_QE. Denote this ideal channel by Gamma_t. The actual channel Phi_t applies exp(-itH_new) to (2), retaining Q and all other outputs.

The checked gauge is identity on the boundary input heads and SWAP_QP on the ideal F support. Tensoring the parent's error operator with the old P/E fiber and conjugating by that gauge gives exactly d(t). Therefore, for the ideal rest state, the standard two-isometry inequality yields an unhalved diamond bound <=2d(t). Changing the fixed rest state costs at most epsilon_rest, even with arbitrary Z. Thus

    ||Phi_t-Gamma_t||_diamond <=epsilon_rest+2d(t)
                                  <epsilon_rest+3tau/4. (6)

For the branch define Phi_t^1 by the fixed mathematical projector R=1 on the actual full output, without tracing any other output. Define the ideal CP branch using the SAME unnormalized B_fin(t) at every time and the same relocated sigma_QE. Call it Gamma_t^1. Both underlying ideal/actual branch maps are contractions. Projection commutes with the entrance gauge, and the trace-nonincreasing branch map contracts the Hermitian difference of the two prepared states. Consequently

    ||Phi_t^1-Gamma_t^1||_diamond
                         <=epsilon_rest+2f(t)
                         <epsilon_rest+tau             (7)

throughout the closed parent horizon. The ideal branch trace is ||B_fin(t)||^2, input independent. No rare-success normalization or time-dependent redefinition of the branch is made.

On the final window the ideal complete target lies entirely in the event F-support, R=1, all other heads vacant. Projection of the nominal vector error gives failure <=d(t)^2. The perturbation of a normalized-state event probability is at most epsilon_rest/2. Hence

    Prob(joint success)>=1-d(t)^2-epsilon_rest/2.        (8)

The right side may be replaced by zero if negative. This is a mathematical event probability, not a physical readout construction.

The physical vector comparison retains exp[-i(c+mu)t], c=8b+8(sqrt(2)-1)j, with mu=0 if no uniform penalty is installed. It also retains the parent's -i and

    B_n(t)=(-i)/sqrt(2pi) integral
       exp[i n q(k)+i(ell+57)k-itE_0(k)]sqrt(q'(k))g(k) dk,
    q(k)=acos(cos k+kappa/(2j)),
    beta_F=P_[1,ell]B/||P_[1,ell]B||.                   (9)

The exact cutoff, positive normalization g and band are inherited. No extra exp(-ikappa t) is appended. Although a common scalar drops out of a channel, it is not fitted away in the complete physical isometry statement. Q is not a decoupled spectator at intermediate times; its residual correlations and possible entrance revisits are already included in (6)--(7).

## 3. A restricted initial-energy certificate on the rest

The most direct optional criterion is a supplied expectation of the positive rest observable

    D_rest=g N_rest+kappa n_R, g=mu-2b>0.

Since D_rest>=min(g,kappa)(I-Pi_rest), its expectation in omega bounds q. This is an observable/state criterion, not a Hamiltonian preparation procedure. The useful installed choice mu=Lambda/4 gives g>15Lambda/64 at the parent cap scale.

There is also a genuine expectation inequality for the ACTUAL installed Hamiltonian and precisely the product preparation (2). Write N_emit=n_e0+n_e1. Each physical source block expands exactly as

    B_i=j n_(I_i,ell)+2j n_ei
                -gamma(a_(I_i,ell)^dagger a_ei+h.c.).    (10)

For every density operator supported on the dual-rail input code, the reduced expectation of a_ei or a_ei^dagger is zero: these operators change the emitter excitation number from one. This remains true for Q/path/Z entanglement. Since the rest is independent in (2), the expectation of each source hopping in (10) vanishes. The two source diagonal emitter terms have expectation exactly 2j. The uniform emitter penalty has expectation mu.

After subtracting the common vacancy scalar c, all remaining nonvacancy blocks are positive, including both SWAP entrance blocks even when Q is entangled with the rails. Their expectation need not factor; positivity is sufficient. The negative vacancy occupations occur only on rest heads with coefficients at most 2b. The retained source-adjacent terms j n_(I_i,ell) are positive. It follows, for every input rho in (2), that

    DeltaE(rho,omega)
       :=Tr[H_new ((J_B rho J_B*) tensor omega)]-c-2j-mu
       >=g Tr(N_rest omega)+kappa Tr(n_R omega)
       >=min(g,kappa) q.                                (11)

Reference identities in this formula are implicit. This is not the global operator inequality H_new-c-2j-mu>=0: it uses the specified initial code and input/rest independence to remove source hopping expectations. In particular it is not valid for arbitrary evolved states or input/rest-correlated preparations. Nominal rest vacuum/record0 makes DeltaE exactly zero for every input and every sigma_PE.

Thus an independently supplied bound DeltaE<=e_rest on a state of form (2) suffices for q<=e_rest/min(g,kappa) and (4). The rest state is input independent; a uniform energy bound over the input channel is a simple sufficient formulation. Equation (11) is pointwise for every legal input, but no energy-measurement scheme or finite experimental estimation procedure is furnished. It cannot certify arbitrary program/path preparation from an energy number alone.

The full runtime ground/Gibbs criteria of preparation9979 must NOT be imported unchanged: their ground comparator has both emitters vacant, whereas the present input has one excitation and source energy 2j+mu. The dual-rail boundary subspace is not reducing under the source hopping. Compressing/fixing the input to define a rest Hamiltonian removes those hopping terms and is not the installed autonomous evolution. Tracing over a chosen input can also give input-dependent entrance terms. A Gibbs state of such an auxiliary operator would be a separate supplied preparation assumption, not a Gibbs state of the running apparatus. No Gibbs preparation theorem is asserted here. Equations (3)--(4), or the restricted supplied expectation certificate (11), are the retained state interfaces.

## 4. Conservation, resources, cap and comparison with the old contract

Total head number is conserved by every installed block, including the two entrance SWAP bonds. On the nominal rest comparator it stays exactly one; on actual preparation errors each occupation component evolves under the same full Hamiltonian. No source qubit is reset or removed during operation. The input Q and emitter pair already belong to the physical device inventory. Reclassifying them as the input adds no qubits or blocks beyond c97b:

    total qubits=127+4ell,
    listed blocks=165+4ell without uniform penalties,
    listed blocks=289+8ell with uniform penalties.

There are 124+4ell head qubits in total, of which TWO are input rails. The rest comprises 122+4ell heads and P,R, hence 124+4ell qubits; together with the three input qubits the count is exact. One logical path qubit is encoded into two physically counted qubits; arbitrary |00> or |11> input does not belong to the operating theorem.

Every full-support load and coordinate is unchanged from c97b. In particular the emitter source block norm/load is 3j, augmented by mu when installed; P has load <129Lambda/256 and Q <Lambda/256. All other parent load margins apply. The four-qubit entrance supports retain their constant range, not an old two-body realization. The all-head energy lower bound remains H_new-cI>=(mu-2b)N+kappa n_R; the stronger initial subtraction in (11) has its separate state restrictions.

Unlike preparation9979, this contract does not start with an ordinary program/path register disjoint from a fully blank apparatus and ask a physical loader to create the endpoint seed and isolate all remnants. It starts with the program Q and endpoint rails themselves as supplied input factors. Therefore eta_load is absent from (6)--(7), but the encoded physical-input supply has not been derived. In particular no ordinary single-qubit-to-dual-rail conversion, coherent long-distance placement, preparation of the rail vacancy correlation, energy injection, attachment process, or start-time preparation is furnished. A state specified at t=0 under a fixed Hamiltonian is not a claim that the Hamiltonian prepared that state.

If a separate input-preparation channel were later supplied, its complete error could be added by contraction, while retaining every preparation output and verifying the required reference action. No such channel is assumed perfect by terminology. Unknown old P/E is retained by the exact SWAP relocation; unknown old R is NOT allowed in the nominal rest comparator and must be paid by q or supplied blank by an additional process. Neither a physical measurement nor permanent output release follows. The parent finite horizon and actual input/output radial waveform remain unchanged.

## 5. Sources, exposure and verification limits

All paths relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- Entrance construction: common_product_autonomous_loader_interface/PROPOSAL.md, c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e; my distinct check common_product_autonomous_loader_interface_check/REVIEW.md, 7a98f648e21cf63b70d481b2cbaba8fac86376763cec0f50678f0ed49e9bd68f, fully reread for this task.
- Preparation contract: common_product_biased_record_preparation/PROPOSAL.md, 9979b614d77b98bf8bc63b6b87b69305beb7cf7607adf5722ae57b759728627e; head-only distinction common_product_energy_blank_interface/PROPOSAL.md, e6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668.
- Actual finite operator and operating bounds: common_product_biased_record_finite_seed/PROPOSAL.md, 532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123, with its complete distinct review read in the preceding task. Its exact source-pair expansion, bias and normalized/absolute targets are reused at their checked scope.
- Inelastic packet phase: common_product_biased_record_packet/PROPOSAL.md, cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf.
- Physical inventory: common_product_single_control_router/PROPOSAL.md, 76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, and exact geometry c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729 in common_product_stage_record_core/PROPOSAL.md.

These identities and necessary source passages were refreshed in the immediately preceding check; no changed ancestor is assumed. ROOT suggested the direct physical boundary input and requested scrutiny of rest preparation. I checked the entrance proposal and authored earlier cell/sector/tolerance components. This is source-exposed same-model author work, not independent validation. The new point requiring distinct review is especially the restricted energy expectation (11), alongside joint-state/channel quantifiers and input reclassification. No scattering/time estimate is rederived or strengthened. No scientific executable, numerical run/sweep, new parameter point, delegation, W/Git/canonical/checkpoint/editable-prompt/model change or publication occurred. Only this proposal was created. Native interactions, coefficient supply, input/rest-state preparation and physical readout remain open supply premises.
