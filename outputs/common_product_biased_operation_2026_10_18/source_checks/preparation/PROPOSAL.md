# Stronger record bias: conditional blank preparation and complete loading

New bounded author composition, conditional on the frozen finite-operation source532866, whose distinct check is pending at drafting. The exact inelastic finite construction permits a different sufficient bias prescription from the earlier time-accumulating perturbation comparison. Together with a uniform head penalty, it gives an explicit energy/Gibbs certificate for blank heads AND record0 and a complete-output loading/operation contract. Neither a Gibbs state, a cooling procedure nor a physical loader is constructed. This new composition also requires a distinct check.

## 1. Full physical inventory and a blank-head/blank-record ground sector

Let H_0 be the finite one-control router with the original positive core, two shared-record writers, two34-edge cables, I endpoint emitters and F caps, before adding a record bias or head penalty. Write

    H_0=cI+K, c=8b+8(sqrt(2)-1)j,
    m=124+4ell, N=sum_(head sites v)n_v.

The two non-head qubits are the physical program P and shared record R. The source76b5 inventory has126+4ell total qubits and164+4ell positive blocks, with combined source blocks and separately listed repeated vacancies. The source/finite-interface identification below must retain those conventions.

After subtracting c, the eight core vacancy blocks contribute -2b n_v at each of four endpoints, and the eight writer vacancy blocks contribute -(sqrt(2)-1)j n_v at eight distinct junctions. All other listed terms are positive on their FULL supports and annihilate global head vacuum for every P/R state. They include the signed positive hopping blocks with their double-occupation columns, programmed mediator blocks, endpoint occupations, phase repairs, terminal j n_T(I+X_R), combined source blocks and F caps. Since j=eta b<=b/8,

    K>=-2bN.                                               (1)

This is a sum-of-positive-operators inequality on all head occupations and arbitrary P/R/environment fibers, not a one-head spectral approximation. Noncommuting record contacts do not affect it.

Install exactly one positive onsite mu n_v on EVERY head site and one positive onsite kappa n_R on the ONE record, with

    mu=Lambda/4, kappa>0,
    H_*=H_0+mu N+kappa n_R,
    A=H_*-cI >= gN+kappa n_R=:D,
    g=mu-2b>15Lambda/64                                    (2)

at the usual D1=Lambda/8, eta<=1/8,zeta<1/2 cap scale. The head vacuum has H_0=cI on its full P/R fiber. Thus the ground projector is exactly

    Q=|vac_heads,0_R><vac_heads,0_R| tensor I_P,             (3)

with energy c and apparatus degeneracy two. It does not select or supply a coherent program. Both A and D vanish on Q, and A>=D excludes any other kernel. Their orthogonal complements have energy at least min(g,kappa).

In the regime0<kappa<g the spectral gap is EXACTLY kappa, not just bounded below by it: the two vectors |vac_heads,1_R> tensor|p> are exact eigenvectors at c+kappa, while(2) bounds every occupied-head sector below by c+g. Head number commutes with H_* even though record occupation does not. This exact-gap statement refers to this finite nominal Hamiltonian; it is not a necessary operating-energy or preparation-temperature criterion.

## 2. General energy certificate and conditional Gibbs bound

Supply a fixed normalized apparatus/preparation-environment state omega_(A E), independent of the arbitrary logical input and its passive reference. The apparatus operator acts as identity on E. Let

    E_ex=Tr[(H_*-cI)omega], q=Tr[(I-Q)omega].

For kappa<g, (2) implies

    q<=E_ex/kappa.                                        (4)

If q<1, its mathematically normalized ground projection is

    omega_0=Q omega Q/(1-q)
           =|vac_heads,0_R><vac_heads,0_R| tensor sigma_PE.

Sigma_PE may be mixed, unknown and entangled with the passive preparation reference. Projecting a purification gives overlap sqrt(1-q); the pure-state trace-distance formula and contraction under partial trace give the unhalved JOINT bound

    ||omega-omega_0||_1<=2sqrt(q).                         (5)

No measurement, postselection or physical renormalization is performed. A coherent ground/excited superposition shows why2q is not a valid general replacement. The energy in(4) is an assumed certificate, not a supplied measurement procedure.

Separately suppose the finite apparatus Gibbs state exp(-beta H_*)/Z is supplied, with beta>=0 (the useful low-excitation prescriptions below have beta>0). The inequality A>=D is NOT exponentiated as an operator inequality. Instead the finite-dimensional min-max principle gives lambda_i(A)>=lambda_i(D) for the ordered eigenvalues. Both kernels have dimension two. Since the scalar exponential exp(-beta x) is decreasing for beta>=0, summing scalar Boltzmann weights over their positive eigenvalues yields

    Z_ground exp(beta c)=2,
    Z_exc exp(beta c)
       <=2[(1+exp(-beta g))^m(1+exp(-beta kappa))-1].

The excited fraction is increasing in Z_exc at fixed ground weight, so

    q_beta<=1-[(1+exp(-beta g))^m(1+exp(-beta kappa))]^-1
           <=m exp(-beta g)+exp(-beta kappa).              (6)

The last inequality uses1-ab<=(1-a)+(1-b) on[0,1], followed by1-(1+x)^-m<=mx. It is valid without[H_0,n_R]=0. The normalized Gibbs ground block is exactly blank heads/record0 tensor I_P/2. Unlike the head-only ground sector, this comparator already has physical R=0; it still does not provide the logical input.

On the apparatus Gibbs state itself, ground and excited blocks are orthogonal, hence ||omega_beta-omega_beta,0||_1=2q_beta. For a complete output retaining a correlated bath or purification, the apparatus Gibbs marginal alone does NOT imply that joint state is block diagonal. Use(5) unless joint block diagonality with respect to Q is independently supplied. A product with a fixed spectator is a sufficient special case. The linear2q bound must not be obtained by discarding preparation-environment coherences from the declared output.

## 3. Assumed coherent loader and all retained outputs

Let rho_(L Z) be arbitrary logical program/path input with passive reference Z. The starting state is rho tensor omega. Assume a fixed loader on accessible L,A and declared workspace, identity on passive E and Z. Every physical loader/environment/dilation output, consumed-input remnant and old program degree of freedom is retained in a spectator S along with E. No unknown P information or entropy is silently traced away.

For the fixed comparator sigma_PE, assume the complete ideal-ground loading contract

    ||Phi_omega0-[rho -> E_seed rho E_seed* tensor sigma_S]||_diamond
                              <=eta_load.                (7)

Here E_seed is the actual finite endpoint-seed isometry of the operation source: supplied logical P/path coherence, one head on the two I emitters, physical R=0 and every other head vacant. The input-independent sigma_S retains sigma_PE under a declared lossless relocation of physical old P and fixed workspaces, tensored with identity on passive E, plus every other declared loader output. Correct apparatus marginals alone do not establish(7). CPTP notation neither proves local implementation nor licenses an unreported entropy sink.

The comparator already contains a blank physical R, so(7) need not assume an additional fresh blank R. It still must preserve/use that R while coherently loading external input and retaining old P. A local autonomous/clocked implementation, head-injection energy, supplied workspaces, loading duration, input-state supply and spectator isolation remain premises. None is generated by the gap proof or by a mathematical swap description.

Using the SAME loader on omega instead of omega_0 changes the channel by at most ||omega-omega_0||_1, including arbitrary references. Hence

    ||Phi_omega-ideal_seed_with_spectator||_diamond
        <=r_prep=2sqrt(q)+eta_load,                       (8)

or r_prep=2q+eta_load under the explicitly joint-block-diagonal state hypothesis. All diamond norms are unhalved. Input independence is essential: an energy inequality does not imply one fixed sigma_S for arbitrary input-correlated apparatus states.

During operation require S decoupled from the device and evolving under a specified input-independent unitary U_S(t), identity on passive reference factors. Put sigma_S(t)=U_S(t)sigma_S U_S(t)*. Unitary channel contraction preserves(8) even if actual loading leaves multihead components or apparatus/spectator correlations. Those components are never discarded or compressed to the one-head sector.

## 4. General operational composition interface

For a finite Hamiltonian H_b=H_0+kappa n_R at nominal accuracy tau, suppose its supplied one-head seed has normalized complete output target G_b(t) on a final window, with vector error less than3tau/8; and one fixed UNNORMALIZED record-1 branch target V_b(t) on[0,T], with vector error less than tau/2. Both maps must retain every output and passive reference, with V_b a contraction. The frozen finite source identified in section5 supplies this interface provisionally; its required distinct check remains a dependency of the operational conclusions here.

Since[H_b,N]=0, on the nominal one-head seed

    exp(-itH_*)E_seed=exp(-i mu t) exp(-itH_b)E_seed.      (9)

Thus G_*=exp(-i mu t)G_b and V_*=exp(-i mu t)V_b. This is the ONLY added scalar phase; kappa n_R is already included in the exact biased operation and is not treated as a phase or a Duhamel error here. No operating time is rescaled. Equation(9) is only a one-head identity; the actual imperfect loaded state is handled by the full-unitary contraction in(8).

The complete target channels are G_* rho G_*^* tensor sigma_S(t), and V_* rho V_*^* tensor sigma_S(t) for the absolute branch. The standard two-contraction inequality gives nominal channel bounds3tau/4 and tau respectively. Composing with(8) gives

    D_final<3tau/4+r_prep,
    D_flag<tau+r_prep.                                   (10)

The actual branch projects only operating R=1 and retains all other outputs. The branch comparison is never divided by its probability and never redefined before matching. This is not a physical readout or normalized rare-success theorem.

For0<epsilon<=1 choose tau=epsilon/2 and

    q<=epsilon^2/64, eta_load<=epsilon/4.

Then r_prep<=epsilon/2 and

    D_final<7epsilon/8, D_flag<epsilon.                   (11)

A sufficient energy condition is E_ex<=kappa epsilon^2/64. A sufficient Gibbs prescription, valid also for a retained correlated purification using the conservative square-root bound, is

    beta>=max{[64/(15Lambda)]log(128m/epsilon^2),
                         kappa^-1 log(128/epsilon^2)}.    (12)

Each term of(6) is then at most epsilon^2/128. Under the joint-block-diagonal hypothesis one may instead use q<=epsilon/8 and

    beta>=max{[64/(15Lambda)]log(16m/epsilon),
                         kappa^-1 log(16/epsilon)},      (13)

with the same eta_load and output bounds. These are sufficient state criteria, not necessary operational temperatures or cooling-time claims.

The nominal perfectly loaded final failure probability for the event exactly one total head on retained F, physical R=1 and all other heads vacant is less than(3tau/8)^2. Preparation changes an event probability by at most r_prep/2, because the two complete states have trace one. Thus actual joint success, and record1 probability alone, obey

    Prob(success)>1-(3epsilon/16)^2-r_prep/2
                  >=1-9epsilon^2/256-epsilon/4.          (14)

The linear mixed-state preparation cost is not squared as a pure-state vector error. Logical correctness and coherent program/reference preservation come from the complete channel estimate, not the event probability by itself.

## 5. Frozen finite instantiation and physical bookkeeping

Read the COMPLETE frozen common_product_biased_record_finite_seed/PROPOSAL.md, SHA256532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123. Its infinite-packet, stationary and phase-envelope dependencies have scoped checks; its finite composition itself is still pending a distinct check. We condition the following operation on that actual source, not on its author's earlier tentative message or on the old elastic finite theorem.

Use its accuracy variable tau in place of its epsilon. Its exact prescription is

    h=eta^2=zeta=r=tau/10^6, D1=Lambda/8,
    D0=zeta D1, b=eta D0,
    j=b^2/D0=Lambda tau^2/(8*10^12),
    kappa=rj=Lambda tau^3/(8*10^18).                     (15)

These coefficient identities follow directly from eta^2 zeta D1 and rj, not from a dynamical approximation. The enabled/disabled program coefficients remain D0-2b,D1-2b; their positivity follows from eta<=10^-3. Both record channels stay open on the selected band. The source's checked packet formulas determine its M_jet (ordinary demodulated outgoing) and N_jet (ordinary internal) BEFORE source ratio or length is chosen. Then its fixed prescription is

    alpha=[4096(2+N0)]^-2,
    rho=alpha tau sqrt(h), gamma=rho j,
    g1=80/rho, g2=600/rho^3, bminus=82/rho,
    H0=M0, H1=M0g1+M1, H2=M0g2+2M1g1+M2,
    J0=N0, J1=N0g1+N1, v_min=2j cos h,
    A_i=g2+(12j/v_min)g1+4j/v_min+48j^2/v_min^2,
    A_o=H2+24H1+212H0, Z0=2, Z1=2g1+1,
    K=max{1,eta^-1,rho^-2,bminus,g1+8,
                  H0+H1,J0+J1,A_i,A_o,Z1+8Z0},
    u=(10^8 K/tau)^2, ell=ceil(100u), M=ell+1,
    t0=u/j, t_minus=3ell/(4j), T=7ell/(8j).              (16)

The M,N triples are the explicit finite arithmetic definitions in packetcf080 sections3--6, reproduced by finite532866 equations(4). No empirical or unspecified constants replace them. This provides a noncircular actual tuple: source ratio follows the packet constants, and length/time follow the source. The original fixed C2 quintic cutoff gives g=chi F/sqrt(p_chi), positive normalization p_chi>1/2, F the exact scalar launcher amplitude from finite(6); no supplied incoming packet replaces the endpoint seed.

The actual finite sources are Q_gamma(ell,ell+1)+(j-gamma)n_ell+(2j-gamma)n_(ell+1) on each I ray, and each F cap is j n_ell. The combined source is positive for gamma<=j (indeed rho<1) and has full-support norm3j; its one-head source-pair diagonals are2j. All other nonvacancy blocks remain the positive inventory used in(1). Thus the all-head inequality applies to THIS finite device, rather than an infinite graph or a different end convention.

Finite532866 gives complete vector error<3tau/8 on[t_minus,T] and a single absolute branch vector error<tau/2 on[0,T], including both emitter vacancies and every residual output. Its source/cut proof uses the actual bias in both generators rather than a kappa T perturbation budget. These operational estimates are adopted conditionally, not independently re-proved here. The matching time is only a comparison time; no physical switching or cutoff of evolution occurs. The relative final-window width is1/6.

In its notation, with q(k)=acos(cos k+r/2), the common scalar sequence is

    B_n(t)=(-i)/sqrt(2pi) integral
       exp[i n q(k)+i(ell+57)k-itE_0(k)]sqrt(q'(k))g(k) dk,
    B_fin=P_(1<=n<=ell)B, beta_F=B_fin/||B_fin||.          (17)

The full-line B norm is1 by the q change of variables, B_fin has positive norm on the final window, and the phase/measure are fixed. The new complete and branch targets are therefore

    G_*(t)=exp[-i(c+mu)t]J_F[beta_F(t) tensor C tensor|1>_R],
    V_*(t)=exp[-i(c+mu)t]J_F[B_fin(t) tensor C tensor|1>_R]. (18)

The same V_* is used throughout[0,T], and is a contraction. It is not the old elastic n+ell+57 sequence: n multiplies q while ell+57 multiplies k. Record energy is already included by E_0(k)=E_0(q)+kappa; appending a second independent exp(-ikappa t) to(18) would be incorrect. All old-fiber and loader outputs remain in sigma_S(t) in the target channels. Actual correlations and multiple heads from imperfect preparation are paid by(8), not omitted from(18)'s comparison.

The finite source has126+4ell qubits and165+4ell blocks INCLUDING the single bias. Adding m=124+4ell head occupations gives exactly

    total qubits=126+4ell,
    listed positive blocks=289+8ell.                    (19)

No record-bias block is added twice. The largest original head load is at most D1+2b<9Lambda/64; the uniform penalty raises it below25Lambda/64. This includes both emitter heads and source-adjacent heads, whose old loads are3j and5j, and F caps with3j. P retains full-support load4(D1-2b)<Lambda/2. R has load(8+r)j, and(15) gives r<=10^-6 and j<=Lambda/(8*10^12), safely below Lambda. Also kappa<=Lambda/(8*10^18)<g, validating the exact-gap and certificate regime. No qubits, edges or operation time are added by mu; its exact uniformity and coefficient supply are premises. No robustness replacement is silently combined with this inventory.

## 6. Explicit sufficient preparation costs and restricted comparison

For the total error budget(11), put tau=epsilon/2 in(15)--(16). Then exactly

    kappa=Lambda epsilon^3/(64*10^18),
    E_ex<=kappa epsilon^2/64
          =Lambda epsilon^5/(4096*10^18)                 (20)

is a sufficient general energy certificate together with eta_load<=epsilon/4. The Gibbs prescription(12) becomes

    beta>=max{[64/(15Lambda)]log(128m/epsilon^2),
            [64*10^18/(Lambda epsilon^3)]log(128/epsilon^2)}. (21)

The explicitly joint-block-diagonal alternative is(13) with the same kappa. These are conditions on a supplied state, not a physical energy-measurement resolution, coefficient tolerance or achievable cooling schedule. The coherent logical input and complete loader remain supplied in both cases. No fresh blank R is needed in the IDEAL ground-loading comparator; its actual approximate preparation error is fully charged.

For clarity about the volume term, the actual chosen finite family has at most polynomial growth as tau tends to zero. In its packet formulas all denominators lambda,1-3eta^2 zeta,den have uniform positive margins under(15). Core mediator ratios reduce to powers of eta divided by these margins, while B=11 and cable length34 are fixed. Thus every entry of M_jet,N_jet is bounded as tau tends to zero; N0 extends continuously to a finite limit, so alpha is bounded above AND below by fixed positive constants. Consequently rho=Theta(tau^(3/2)), g1=O(tau^(-3/2)), g2=O(tau^(-9/2)), and every term in K is O(tau^(-9/2)). Equations(16) give m=O(tau^-11). This loose polynomial bound is sufficient to establish log m=O(log(1/epsilon)); no optimized runtime exponent or practical resource assertion is needed. Huge fixed constants are not suppressed in the exact prescription(16).

It follows that the explicit beta selected at equality in(21) has sufficient asymptotic order Theta(Lambda^-1 epsilon^-3 log(1/epsilon)): its record term supplies that lower order for this CHOSEN prescription, while the head-volume term is only logarithmic. This is not a lower bound on the temperatures or energy costs required by all preparation/operation methods. In particular an excited state may behave differently from this ground-projection sufficient criterion. Neither a necessary operational temperature nor a cooling time follows.

The comparison to the checked weak-bias source aaa078 is only between two sufficient conditional families at the same total-error order, with different actual parameter/length prescriptions and different spatial targets:

| Quantity | Earlier weak-bias prescription aaa078 | Present conditional inelastic prescription |
| --- | --- | --- |
| Bias choice | epsilon/(16T_old) | Lambda epsilon^3/(64*10^18) |
| Selected bias order | Theta(Lambda epsilon^(17/2)) | Theta(Lambda epsilon^3) |
| General sufficient energy allowance | Theta(Lambda epsilon^(21/2)) | explicit(20), order Lambda epsilon^5 |
| Selected sufficient inverse-temperature order | Theta(Lambda^-1 epsilon^(-17/2)log(1/epsilon)) | Theta(Lambda^-1 epsilon^-3 log(1/epsilon)) |
| Operating comparison target | Elastic sequence plus paid bias Duhamel error | Inelastic q-dependent sequence(17), bias in exact dynamics |

The old source used tau=epsilon/4 and charged a full-horizon bias error; the present budget uses tau=epsilon/2 because no separate bias error is added to the new finite theorem. Both meet a complete-output/absolute-branch error below epsilon under their own preparation assumptions. This does not assert the same physical time, head count or exact radial output for the two families. The present T is exactly(16), and can be extremely large; no faster or practical end-to-end operation is claimed. The orders compare mathematical sufficient state criteria asymptotically, not guaranteed numerical advantages at a specified tolerance.

## 7. Limits, exact evidence and exposure

The head gap does not create a bath or a ground state. Closed H_* conserves N, so it cannot by itself cool occupied heads into vacuum. Even its exactly blank ground comparator leaves old P mixed/unknown; arbitrary logical program/path input, its coherent injection, all-output retention and spectator isolation are substantive assumptions. Cooling, energy certification, loading, workspace supply and readout durations are absent from the operating T. No energy or coefficient magnitude quoted here is a precision/manufacturability claim. No native occupation basis, local coefficient supplier, new axiom, old literal processor transfer, normalized rare-flag fidelity, robustness composition, capture/reset, irreversible latch or permanent halt is supplied.

Exact sources under N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934:

- common_product_energy_blank_interface/PROPOSAL.md: e6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668.
- common_product_record_ground_preparation/PROPOSAL.md: aaa0786b19ec5b0c37923e712fe8f9b80c3490a1c495a7bb5f2482c97402a1bc.
- Their common_product_energy_preparation_check/REVIEW.md: f7156129dbe665ba0951bbc92f49b4a22b8b577801890a78a1cbb3e6b2f4aea7, fully read/hash-verified here. Complete necessary source arguments were read, with a truncated aggregate corrected by a separate full weak-bias read and the remaining head-energy text. The unchanged head-energy argument also retains its prior complete author read.
- common_product_biased_record_finite_seed/PROPOSAL.md: 532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123, fully read after the author reported this frozen identity. Its new finite proof is PROVISIONAL pending distinct check; the operational conclusions and the improved sufficient preparation family here are conditional on it. The present read is not an independent check of that finite proof.
- common_product_biased_record_packet/PROPOSAL.md: cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf, this author's preceding frozen source. Its complete check was read/hash-verified here:315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916. It supports the infinite-packet scope only.
- The unchanged networkcdf35dd3f9a8ea32ce0b52745ac00756885dba014d67db7e12f706e58e63b666/check1bd4a2878923495df99a219cce1c520cc03674bce2da5ff1d61d64d0940f8d40, local writerdfe071282ac3d160073b85caa0bd11d4e1834e58278e1da8a3c354fec5440c18/checkc568fe01ce4c6e9e89e6488808bb39c9ba7a98e1df4b0fc5bcc8d21439315829 and single-control76b5/check549b inventories retain their exact preceding full reads and scope. The finite source separately pins phase-envelope54e054/checka7947 and its launch/narrow-derivative ancestry; those estimates are part of the provisional finite premise, not separately rederived here.

ROOT proposed the stronger-bias preparation composition and requested explicit all-output loading and mixed-state event costs. The finite author supplied its tentative interface first; no operation was imported until its frozen full source was read. This author wrote the head-energy, network and packet components and several earlier sources. These are declared design/source exposure and same-model continuation, not blind or independent checking. ROOT also suggested a possible logistic necessary condition for Gibbs ground occupancy; it is not used or promoted into a necessary operational-temperature claim here.

Required distinct checks include the exact nominal gap, min-max partition comparison and beta sign, preparation-environment block-diagonality distinction, lossless old-P/passive-reference loading contract, mixed-state event cost, actual frozen finite interface, all counts/caps and the parameter/volume arithmetic in(15)--(21). Checked components do not themselves validate this new preparation composition.

Only this proposal was created. No scientific executable, numerical sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. No independent or retained status is assigned.
