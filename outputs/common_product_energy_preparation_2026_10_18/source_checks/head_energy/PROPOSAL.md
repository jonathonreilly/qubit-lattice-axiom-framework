# An energy certificate for blank heads and an explicit loading interface

New bounded author derivation requiring a distinct check. A uniform positive head occupation penalty gives the nominal finite one-control router a four-dimensional blank-head ground sector with a constant lower gap, within its existing load reserve. Its operating one-head evolution changes only by the specified phase exp(-i mu t), with no runtime rescaling. Low energy then certifies approximate blank HEADS. Composing this certificate with operation requires a separately assumed complete-output loading channel; neither cooling, blank-record supply nor coherent loading is derived here.

The optional Gibbs calculation is conditional on supply of that exact finite Gibbs state. It is not a bath, equilibration or cooling-time theorem. The general preparation certificate costs2sqrt(q) in unhalved trace norm; the block-diagonal Gibbs case costs2q. These statements concern different state hypotheses and are not interchanged.

## 1. Full-head lower bound from the actual positive inventory

Use the nominal finite one-control Hamiltonian H from76b5 and canonical02b432, with all positive blocks, both I emitters, F caps and the shared record included. There are m=124+4ell HEAD qubits and two additional qubits P,R. Its physical scalar is

    c=8b+8(sqrt(2)-1)j,
    H=cI+K.

The eight core vacancies are b(I-n_v), two at each of the four core endpoints. The eight writer vacancies are (sqrt(2)-1)j(I-n_v), one at each of eight distinct junction heads. These writer sites are distinct from core endpoints. Every other listed block is positive on its FULL support. In particular signed positive bonds, programmed mediator occupations, terminal blocks j n_T(I+X_R), combined sources, phase occupations and caps remain positive on all head occupations and all P/R states, whether or not the blocks commute.

Let d_v be the sum of vacancy coefficients at head v. Then

    K=sum_(nonvacancy l)h_l-sum_v d_v n_v,
    d_v=2b at core endpoints,
    d_v=(sqrt(2)-1)j at writer junctions, and0 otherwise.

For eta=b/D0<=1/8, j=eta b<=b/8, so max_v d_v=2b. Dropping only positive full-support operators yields the exact all-head inequality

    K>=-sum_v d_v n_v>=-2b N,
    N=sum_(all head sites v)n_v.                         (1)

This is not an extension of a one-head norm bound by analogy. It is a full finite operator inequality. It retains arbitrary P/R and passive-reference fibers, double occupation of bonds, and every head-number sector. Positivity of H alone would only give K>=-cI; the stronger N-dependent lower bound uses the actual vacancy placement.

## 2. Uniform penalty, gap, phase, counts and cap

Add one separately listed positive onsite occupation block at EVERY head site, including all emitters, core endpoints/mediators, cable/writer heads and final sites:

    H_mu=H+mu N, mu=Lambda/4.                            (2)

This uses the same positive one-site occupation form already present in the supplied block inventory. Exact uniformity and supply of its coefficient are additional construction premises; no native mechanism or new framework axiom is installed by this notation.

For the nominal choice D1=Lambda/8, eta<=1/8,zeta=D0/D1<1/2, one has b<Lambda/128. Therefore

    H_mu-cI>=g N, g=mu-2b>15Lambda/64>0.                (3)

All nominal blocks conserve N and annihilate global head vacuum after subtraction of c. Thus head vacuum has energy exactly c for EVERY P/R state. Let Pi_0=|vac><vac|_heads tensor I_(P,R). Since N>=I-Pi_0, (3) makes Pi_0 the entire ground eigenspace of the apparatus and gives a spectral gap at least g, hence strictly greater than15Lambda/64. Its dimension is four, not one. An external reference tensors additional degeneracy but changes no gap statement about the apparatus.

Every head's nominal full-support incident sum is at most D1+2b<9Lambda/64. Adding a norm-mu occupation raises it to less than25Lambda/64. P receives no penalty and retains load4(D1-2b)<Lambda/2; R receives no penalty and retains load8j. Every incident sum remains below Lambda. This argument is for the NOMINAL inventory, not for the extremal matrix errors from earlier robustness proposals.

No qubits or interaction edges are added. Keeping the penalty occupations separately listed gives

    qubits=126+4ell,
    blocks=(164+4ell)+(124+4ell)=288+8ell.                (4)

Since [H,N]=0, the finite operator identity on each n-head sector is

    exp(-itH_mu)Pi_n=exp(-i mu n t)exp(-itH)Pi_n.         (5)

The parent operating seed has exactly one head. Its complete normalized target and its entire-horizon UNNORMALIZED flag target must therefore both be multiplied by exp(-i mu t). Their physical scalar becomes c+mu on this operating sector. The common -i scattering factor, radial shift57, logical C_p, program/reference coherence, radial normalization and observation times are otherwise unchanged. No old absolute runtime is rescaled, because this is an additive uniform sector scalar, not a rescaling of H. Vacuum/one-head superpositions would have a relative sector phase, so (5) is not interpreted as one global scalar on the full Hilbert space.

## 3. General energy-to-blank-head trace certificate

Let A denote the entire apparatus, including heads,P,R. Let E_env be an arbitrary environment possibly entangled with A. Supply a fixed normalized state omega_(A E_env), INDEPENDENT of the logical input and its arbitrary passive reference. Define its energy excess using the apparatus operator only:

    E_ex=Tr[((H_mu-cI) tensor I_E_env) omega],
    q=Tr[((I-Pi_0) tensor I_E_env) omega].

Equation(3) gives

    0<=q<=Tr(N omega)<=E_ex/g.                           (6)

This is a certificate conditional on the actual energy expectation, not a supplied measurement of it. Suppose q<1, which follows for example from E_ex<g. Normalize the vacuum projection:

    omega_0=Pi_0 omega Pi_0/(1-q)
           =|vac><vac| tensor sigma_(P R E_env).          (7)

The equality follows because the head vacuum factor is rank one. Sigma is a normalized joint state and can contain arbitrary P/R/environment correlations. It is fixed independently of logical input, but is not claimed to be known, pure, recordblank or a tensor product among its factors.

For any purification |Omega> of omega, projection by Pi_0 followed by normalization gives a purification of omega_0 with overlap sqrt(1-q). The unhalved trace distance between those two pure states is2sqrt(q). Partial trace contracts trace norm, so

    ||omega-omega_0||_1<=2sqrt(q)
                        <=2sqrt(E_ex/g).                (8)

No physical projection, postselection or renormalization is performed. Omega_0 is a mathematical comparator. For q=0 it equals omega; q=1 supplies no normalized comparator and is excluded. Correlations with E_env are retained by the proof. Equation(8) cannot be replaced by2q for an arbitrary coherent state: the pure superposition sqrt(1-q)|vac>+sqrt(q)|v> already has distance2sqrt(q) from vacuum. That example preserves the genuine general-state square-root cost.

## 4. Assumed loading channel with every old fiber output retained

Low head energy does not itself supply the parent's operating input. Let L be the ordinary logical program/path input register and Q_ref an arbitrary passive reference, with arbitrary joint state rho_(L Q_ref). The initial joint input is rho tensor omega, reflecting the stated independence of apparatus preparation from logical input/reference. Any additional loading resources B are in a declared fixed state and can be absorbed into the loading channel's specification; their preparation is not derived by (6).

Assume a CPTP loading channel on accessible L,A and declared B, acting as identity on any inaccessible E_env and Q_ref. Its outputs are the operating apparatus A and a spectator register S containing all old P/R/environment information, consumed-input remnants, workspaces and preparation/loading environment outputs. The channel's locality, duration, energy source and physical implementation are separate premises. CPTP notation allows mixed supplied resources; it does not authorize tracing away unreported garbage or entropy sinks. If a realization has a dilation environment, that output must be included in S for this complete-output contract.

To prevent the statement from tacitly erasing unknown old P/R, specify an input-independent spectator target sigma_S retaining sigma_(P R E_env). One sufficient explicit form is

    sigma_S=J sigma_(P R E_env) J^* tensor sigma_rest,     (9)

where J is a fixed isometric relocation of the old P/R factors into spectator storage and identity on an inaccessible E_env, and sigma_rest is a declared input-independent workspace/resource-output state. A more general lossless input-independent isometry including those fixed workspaces is equally admissible. In every case the old fiber/environment is retained, possibly at different physical sites, rather than claimed to have been erased. Neither J nor spectator storage is constructed here.

Let Phi_omega be the channel from L to A,S obtained by supplying omega to the SAME loader, and define Phi_omega0 by supplying the comparator(7). Assume the ideal-vacuum loading contract

    ||Phi_omega0 - [rho -> E_seed rho E_seed^* tensor sigma_S]||_diamond
                             <=eta_load.                (10)

The diamond norm here and below is unhalved and includes arbitrary Q_ref. E_seed is exactly the parent one-head seed isometry with the logical program directly in P, path head on the two I emitters, R=|0> and all other heads vacant. The spectator state in(9) is independent of rho. Equation(10) is an ASSUMED channel interface, not a conclusion from a gap or from the existence of a circuit description.

If the old record is unknown, this contract requires retaining it in S and supplying the operating blank R by another declared resource or process. It cannot silently reset old R and discard its entropy. Likewise the ordinary coherent program/path input is supplied externally, and injecting the one-head operating excitation is a separate energy/loading operation. An abstract swap to a supplied blank register may explain the logical meaning of relocation but supplies no local positive loading Hamiltonian, clock or runtime theorem.

Tensoring an arbitrary logical/reference input with omega-omega_0 and applying the same channel gives, by trace-norm contractivity and its completely bounded version,

    ||Phi_omega-Phi_omega0||_diamond
                                  <=||omega-omega_0||_1.

Combining with(8),(10), the COMPLETE prepared output obeys

    ||Phi_omega-[rho -> E_seed rho E_seed^* tensor sigma_S]||_diamond
                         <=r_prep=2sqrt(q)+eta_load.     (11)

This retains all spectator outputs. Correct apparatus marginals without a full loading contract do not imply(11); residual correlations carrying logical information would matter. The input-independence premise cannot be dropped by applying(8) to an input-dependent conditional state and declaring one fixed sigma_S.

## 5. Complete operational output and unnormalized flag composition

During operation assume S is decoupled from A and evolves by a specified input-independent unitary U_S(t), or remains static as its special case. Put sigma_S(t)=U_S(t)sigma_S U_S(t)^*. This isolation/spectator dynamics is another explicit interface premise; no unlisted coupling is ignored. Apply the full unitary exp(-itH_mu) tensor U_S(t) to the actual loaded A,S state. All its correlations and outputs remain retained. Unitary channel composition preserves the error ceiling r_prep.

For nominal accuracy parameter tau, let the parent normalized complete-output map be G(t), including exp(-ict), on its final window. Its isometry error is<3tau/8, so its unhalved channel error is<3tau/4. Define

    G_mu(t)=exp(-i mu t)G(t)
           =exp[-i(c+mu)t]J_F[beta_F(t) tensor C tensor|1>_R].

The full ideal target channel is

    rho -> G_mu(t)rho G_mu(t)^* tensor sigma_S(t).         (12)

Equation(5) transfers the nominal one-head theorem exactly, and triangle inequality with(11) gives complete unhalved channel discrepancy

    D_final(t)<3tau/4+r_prep                              (13)

throughout the same final window. The actual loaded state may have residual heads in other sectors; their entire contribution is included through (11) and unitary contractivity. No one-head compression is applied to that actual state. The global phase cancels in the density channel, but its required value has been stated explicitly for the parent vector map and any purified comparison.

For all t in[0,T], let the parent's ONE unnormalized branch target be

    V(t)=exp(-ict)J_F[B_fin(t) tensor C tensor|1>_R],
    V_mu(t)=exp(-i mu t)V(t),

with the original nominal B sequence, its -i factor and shift57, restricted to1<=n<=ell without normalization. The actual branch channel projects only the operating R onto record1 after the full evolution, retaining every A,S output. This projection is mathematical branch notation, not a readout implementation. It is completely trace-norm contractive. The parent's subnormalized branch-channel error is<tau on the entire horizon; hence

    D_flag(t)<tau+r_prep,  0<=t<=T,                      (14)

relative to rho -> V_mu(t)rho V_mu(t)^* tensor sigma_S(t). The comparator is not switched at matching or normalized by a rare success probability. Neither sigma_S(t) nor its target dependence changes with logical input.

For a concrete preparation reserve choose0<epsilon<=1 and use the nominal logarithmic family at tau=epsilon/2. Require

    q<=epsilon²/64, eta_load<=epsilon/4,
    a sufficient energy condition is
                 E_ex<=g epsilon²/64.                  (15)

Then r_prep<=epsilon/2. Equations(13)--(14) give

    D_final<7epsilon/8<epsilon,
    D_flag<epsilon.                                    (16)

No extra factor from m or the passive reference enters these comparisons. The supplied preloading/loading durations are NOT included in the unchanged operating T; no end-to-end runtime is asserted.

The parent normalized final comparator has record1 and exactly one head on retained F with every other head vacant. Its nominal failure probability is<(3tau/8)². Since the complete actual loaded channel and the ideal seeded channel are normalized and differ by unhalved trace norm at most r_prep, any probability can differ by at most r_prep/2. Thus final record1 and joint EXACTLY-one-retained-F-head/record1 success satisfy

    Prob(success)>1-(3epsilon/16)²-r_prep/2
                  >=1-9epsilon²/256-epsilon/4.          (17)

This is a trace-level preparation result, so the probability loss is not incorrectly squared as if(11) were a pure-state norm error. There is no normalized rare-branch accuracy claim. Blank R, coherent input and all-output loading remain explicit premises of(10), not consequences of(15).

## 6. Optional assumed finite Gibbs state

Suppose separately that the apparatus state is EXACTLY

    omega_beta=exp(-beta H_mu)/Z, beta>0.                 (18)

No bath, equilibration dynamics or formation time is supplied by this assumption. The finite head-number-n sector has dimension4 binomial(m,n). Since [H_mu,N]=0 and(3) holds, each energy in that sector is at least c+gn. Its vacuum sector has four eigenvalues exactly c. Put x=exp(-beta g). Summing eigenvalue bounds, rather than invoking an invalid operator-monotonicity rule for exponentials, gives

    Z_0=4 exp(-beta c),
    Z_exc<=4 exp(-beta c)[(1+x)^m-1],
    q_beta=Z_exc/(Z_0+Z_exc)
           <=1-(1+x)^(-m)<=m exp(-beta g).               (19)

The first fraction is increasing in Z_exc, which justifies its direction. The last inequality follows by integrating the derivative m(1+x)^(-m-1)<=m from0 to x. This retains the volume factor and all P/R degeneracies.

The normalized vacuum block is EXACTLY

    omega_beta,0=|vac><vac| tensor I_(P,R)/4.             (20)

The Gibbs state is block diagonal between vacuum and its orthogonal complement. Therefore

    omega_beta=(1-q_beta)omega_beta,0+q_beta omega_exc,
    ||omega_beta-omega_beta,0||_1=2q_beta.                (21)

Orthogonal supports, not a stronger general gentle-projection theorem, give this linear cost. Use(21) only for the specified state on all retained preparation outputs. If a correlated bath/purification is also retained, the apparatus marginal Gibbs condition alone need not make that joint state block diagonal: the general2sqrt(q_beta) bound applies unless joint block diagonality is separately supplied. An assumed product with a fixed spectator, or a joint block-diagonal extension, preserves the2q cost. This distinction prevents tracing away bath coherences to claim a complete-output improvement.

Under the hypotheses for(21), the loading/composition proof gives r_prep=2q_beta+eta_load. It suffices instead to require

    q_beta<=epsilon/8, eta_load<=epsilon/4,
    beta g>=log(8m/epsilon).                            (22)

Then the same full-output and branch ceilings(16) hold. A fully explicit sufficient choice uses g>15Lambda/64:

    beta >=[64/(15Lambda)]log(8m/epsilon).               (23)

For the nominal logarithmic apparatus m=124+4ell with ell=Theta(epsilon^(-11/2)) at tau=epsilon/2, this sufficient inverse temperature is Theta(Lambda^-1 log(1/epsilon)). It is not a cooling-time, heat-removal, bath-size or preparation-cost bound. For a general correlated purification needing the square-root cost, choose q_beta<=epsilon²/64 instead, i.e. beta g>=log(64m/epsilon²); the same logarithmic order but different explicit threshold follows. At fixed beta the displayed volume bound does not maintain a fixed small global vacancy error as m grows.

Equation(20) supplies neither arbitrary coherent program nor blank R: its R marginal is I/2. The loading contract must still import the program/path input and a fresh blank operating R while retaining the old mixed fiber in S. The positive penalty does not favor either record value. The closed H_mu conserves N, so it cannot itself turn a populated head sector into vacuum; this is a statement about this Hamiltonian, not a no-go for separately supplied open-system preparation.

## 7. Limits, exact evidence and check obligation

Uniform mu leaves the nominal operating counts/time orders unchanged apart from the added listed occupations: qubits126+4ell, blocks288+8ell, ell=Theta(epsilon^(-11/2)) and operating T=Theta(Lambda^-1 epsilon^(-15/2)) for the selected nominal family. It does not give an end-to-end preparation/loading runtime. Omitting the penalty on emitters or making it nonuniform destroys the simple common one-head phase and requires another proof. Earlier scalar/matrix/vacuum-preserving robustness allowances are NOT automatically combined with this penalty: their cap margins, all-head lower bounds and phase budgets would have to be recalculated for the changed inventory.

Failed inferences kept explicit are: positivity of H alone does not prove(1); a gap does not prepare its ground state; blank heads do not mean blank R; a mathematical normalized projection is not physical postselection; a Gibbs apparatus marginal does not imply the improved joint-output2q bound; a CPTP reset cannot be credited with erasing old P/R without accounting for its outputs/resources; and unchanged operating time does not bound cooling/loading time. No native coefficient/basis/interaction or readout identification, autonomous initializer, old literal processor transfer, permanent latch, capture/reset or indefinite finite storage follows.

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Newly fully read and hash-verified assessment: blank_supply_opportunity/ASSESSMENT.md,0eab0fc5eed427936637115f9daba30468a9e23fd94a7461d5aafd1d90bbd287. Its provisional calculations and ROOT's explicit interface instructions are design exposure, not evidence of this theorem.

Exact nominal source76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and canonical common_product_single_control_publication/NOTE.md,02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde, were fully read in the preceding coherent tasks and refreshed unchanged here. Their distinct replacement check is549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0. The logarithmic nominal family7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8 and its checkd1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3 retain their complete prior reads and stated scopes. The full c913 writer/core inventory and its review61de4ee are reused at their pinned scopes recorded there; no pending robustness result is needed for the all-head positivity argument.

The author has authored the one-control and robustness sources and is continuing after exposure to ROOT's penalty/loading proposal and the separate assessment. This is not an independent check. The decisive review should reconstruct the all-head vacancy coefficient maximum, confirm the exact head inventory and uniform-sector phase, verify the purification trace certificate, and challenge whether the complete loading/spectator contract truly retains old fiber/environment outputs. The thermal review must check sector dimensions, partition-function inequality direction and the joint-state qualification of(21). No favorable source count substitutes for those checks.

Only common_product_energy_blank_interface/PROPOSAL.md was created. No parent source, W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, numerical solver/simulation/sweep, publication or delegation occurred. The result is a conditional energy/preparation interface candidate pending distinct review, not an implemented preparation mechanism or a premise imported into a pending publication.
