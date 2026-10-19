# Preparation interface for the resonance-resolved finite family

New bounded author re-instantiation of preparation9979, not a preparation mechanism. The operation premise is the NEW finite family970a, whose separate composition check is pending at drafting. All operational conclusions below are conditional on that premise until its check is available, and this transfer itself requires a distinct check. The former split family556956 and its compatibility review supply a checked pattern of substitution, not a loader or a finite theorem for this new length.

## 1. Actual new apparatus and targets

For total desired accuracy 0<epsilon<=1 set tau=epsilon/2. Evaluate the entire prescription of `common_product_resonant_router_resources/PROPOSAL.md` at this tau, including its actual network jets, coefficient maximum C and

    h=eta^2=zeta=r=tau/10^6, D1=Lambda/8,
    D0=zeta D1, b=eta D0, j=b^2/D0,
    alpha=[4096(2+N0)]^-2, rho=alpha tau sqrt(h), gamma=rho j,
    kappa=rj,
    u=10^12 max{1,eta^-1/tau,(J0+J1)/tau,
        C rho/(h^2 tau),[C rho/(h^2 tau)]^(2/3),
        rho^-2 log[10^8/(tau rho)]},
    ell=ceil(100u), M=ell+1,
    t0=u/j, tminus=3ell/(4j), T=7ell/(8j).               (1)

The symbols C,N0,J0,J1 are the explicit finite arithmetic coefficients of970a sections1--2, evaluated before u. No old coarse K or split L/Q is used in (1). This is a different finite apparatus: retain exactly its ray prefixes, I emitters at M, F caps at ell, positive source compensations, one ordinary program P and one shared record R. Let H_b denote this apparatus Hamiltonian INCLUDING precisely one kappa n_R, with c=8b+8(sqrt(2)-1)j. There are m=124+4ell head qubits and two non-head qubits P,R.

The conditional operation premise970a is a complete-vector error <3tau/8 on[tminus,T] and a single unnormalized record1 vector error <tau/2 on[0,T], for the actual endpoint seed isometry E_ell. It retains every physical output and arbitrary passive logical reference. Its target uses the actual new ell:

    B_n(t)=(-i)/sqrt(2pi) integral
       exp[i n q(k)+i(ell+57)k-itE_0(k)]sqrt(q'(k))g(k)dk,
    q(k)=acos(cos k+r/2), E_0(k)=2j(1-cos k),
    B_fin=P_(1<=n<=ell)B, beta_F=B_fin/||B_fin||.

The source g is the exact positively normalized quintic-cutoff launcher profile at the chosen rho,h. The full-line B norm is one; positivity of ||B_fin|| on the final window is part of the new finite proof. The input translation is ell k, not ell q. The energy relation E_0(k)=E_0(q)+kappa already accounts for record excitation.

Install exactly one positive onsite mu n_v at EACH of the m head sites, with mu=Lambda/4, and define

    H_*=H_b+mu N, N=sum_v n_v.

Do not install a second record bias. Since [H_b,N]=0, on the ideal one-head seed the only extra phase is exp(-imu t). The complete normalized target is therefore

    G_*(t)=exp[-i(c+mu)t]J_F[beta_F(t) tensor C_path tensor|1>_R],

and the same unnormalized target at every time is

    V_*(t)=exp[-i(c+mu)t]J_F[B_fin(t) tensor C_path tensor|1>_R]. (2)

Here C_path is the coherent controlled path operation, distinct from the numerical maximum C in(1). No independent exp(-ikappa t), fitted phase, physical normalization or timed switching is introduced. The operating window remains relative width1/6.

## 2. Full-support ground certificate and physical load accounting

Let H_0=H_b-kappa n_R. On ALL head occupations, the actual vacancy accounting gives

    H_0-cI=K>=-2bN.

Indeed the four core endpoints each have total negative vacancy remainder -2b n_v; eight distinct writer junctions have -(sqrt(2)-1)j n_v; every other block is positive on its full support and annihilates global head vacuum for arbitrary P/R. The writer vertices and core endpoints are distinct, and j=eta b<=b/8 bounds their negative coefficients by2b. The positive terms include double-occupation columns, signed hopping blocks, programmed mediators, record-dependent terminal blocks, compensated I sources and F caps. Relocating the terminal source/cap along a ray changes neither this local inequality nor the scalar c.

Consequently

    A=H_*-cI>=gN+kappa n_R, g=mu-2b>15Lambda/64.        (3)

No commutation of K and n_R is asserted or needed. Both sides have the exact common kernel

    Q=|vac_heads,0_R><vac_heads,0_R| tensor I_P.

It has apparatus dimension two and leaves P arbitrary. On the vacuum sector A=kappa n_R exactly; in every occupied-head sector A>=g. Since kappa<g, the exact spectral gap is kappa, witnessed by the two vacuum/R1 states. Thus this supplies a ground-sector characterization, not a method for putting the device there.

Counts at the NEW ell are

    device qubits=126+4ell,
    positive blocks before head penalty=165+4ell,
    positive blocks with head penalty=289+8ell.         (4)

The last adds m separate occupation blocks. The one record bias was already counted. Loader workspace and retained spectator degrees of freedom are not included in (4); their number, energy and implementation are separate supplied resources, not implicitly zero.

The original head incident norm maximum is <=D1+2b<9Lambda/64. This includes source emitter3j, source-adjacent5j, F-cap3j, ordinary lead4j and core endpoint6b+4j under the selected small parameters. Adding mu gives head load <25Lambda/64. Program load remains4(D1-2b)<Lambda/2. Record load is(8+r)j, with no mu contribution. All loads are full-support norm sums and remain below Lambda; no rescaling of j or T is required. Positivity of gamma<j and every original compensation is retained. The head penalty is exact uniform supplied data, not a robustness statement.

## 3. Certified state, correlations and Gibbs sufficient criteria

Supply a fixed normalized apparatus/preparation-reference state omega_AE independent of the arbitrary logical input L and its passive reference Z. The Hamiltonian acts as identity on E. Let

    q=Tr[(I-Q)omega], E_ex=Tr[A omega].

Equation(3) implies q<=E_ex/kappa. For q<1 its mathematically normalized projected comparator has the form

    omega_0=Q omega Q/(1-q)
       =|vac_heads,0_R><vac_heads,0_R| tensor sigma_PE,
    ||omega-omega_0||_1<=2sqrt(q).                      (5)

The bound is on the JOINT state including E, proved by projecting a purification and using the overlap sqrt(1-q). Sigma_PE can retain arbitrary old-program entropy and entanglement. Neither projection nor normalization is an actual operation. A general coherent ground/excited state precludes replacing2sqrt(q) by2q.

If an apparatus Gibbs marginal at beta>=0 is supplied, finite-dimensional min-max applied to A and D=gN+kappa n_R, with their equal two-dimensional kernels, gives

    q_beta<=1-[(1+exp(-beta g))^m(1+exp(-beta kappa))]^-1
           <=m exp(-beta g)+exp(-beta kappa).           (6)

The proof compares ordered scalar eigenvalues and their Boltzmann weights. It does NOT exponentiate an operator inequality using false exponential monotonicity. Noncommuting record contacts do not invalidate it. The apparatus Gibbs ground block is blank heads/R0 with I_P/2, not a supplied coherent logical program.

For a retained bath/purification, a Gibbs apparatus marginal still supplies q through(6), but joint closeness uses(5). Only a separately supplied JOINT block-diagonality condition with respect to Q permits the sharper distance2q. A block-diagonal apparatus marginal alone does not imply that condition on AE. No discarded environment is used to claim it.

For the conservative correlated-state contract choose

    q<=epsilon^2/64, eta_load<=epsilon/4.                (7)

Sufficient alternatives for the first condition are

    E_ex<=kappa epsilon^2/64,

or a supplied Gibbs marginal with

    beta>=max{[64/(15Lambda)]log(128m/epsilon^2),
                             kappa^-1 log(128/epsilon^2)}. (8)

Each Gibbs term is then <=epsilon^2/128. Under the additional JOINT block-diagonality premise one may instead take q<=epsilon/8, and sufficient Gibbs beta is the same maximum with logarithms log(16m/epsilon),log(16/epsilon). In either case retain eta_load<=epsilon/4. These are sufficient supplied-state criteria, not necessary operational temperatures or energy-measurement specifications.

## 4. Actual new full-output loader contract

A separate loader contract is required for EACH actual apparatus in(1). A loader supplied for the older coarse or split emitter positions does not imply this contract.

Assume a fixed physical loading channel on accessible L,A and declared workspace, tensor identity on passive E and Z. Retain EVERY physical loader/dilation/environment output, consumed-input remnant and old program degree of freedom in a spectator S along with E. For the fixed comparator sigma_PE in(5), require the full-channel condition

    ||Load_(omega_0)-[rho_LZ ->
          (E_ell tensor I_Z)rho_LZ(E_ell^* tensor I_Z)
                                      tensor sigma_S]||_diamond<=eta_load. (9)

E_ell is the seed of the new device: one head coherently on its two I emitters at M, the supplied logical program in physical P, R0 and all other heads vacant. Sigma_S is fixed independently of the logical input and retains old P losslessly, including its correlations with E, plus all declared outputs. Old-P relocation acts only on accessible P/workspace, identity on E. CPTP notation in(9) does not license unreported disposal of entropy, an environment, or a consumed input. One may model the full loader as an isometry with its dilation outputs retained; the condition concerns those outputs too.

The ideal comparator already has blank R, so no second fresh blank record is needed in(9). Coherent program/path input, workspace supply, head injection, lossless relocation, local implementation and loading duration remain premises. The new head count m does not by itself provide any of them.

Running the SAME supplied loader on omega and omega_0 and retaining all outputs gives, uniformly over Z,

    D_seed<=r_prep=2sqrt(q)+eta_load<=epsilon/2,          (10)

or r_prep=2q+eta_load under the joint block-diagonal premise. The initial product of rho_LZ and fixed omega_AE is essential. An apparatus correlated with arbitrary unknown logical inputs would not establish one fixed input-independent spectator by this argument.

During operation require S isolated from the device, with specified input-independent unitary U_S(t), identity on passive E,Z, and sigma_S(t)=U_S(t)sigma_S U_S(t)^*. Actual loading errors can contain multiple heads, record errors and apparatus/spectator correlations. They evolve under the FULL H_* and remain in the error; only the ideal seed uses the one-head phase identity. Full-unitary contraction preserves(10) without projecting the actual loaded state onto one head.

## 5. Complete operation, flag and event budgets

Conditioned on970a's finite theorem, two-isometry/two-contraction bounds give nominal unhalved complete-channel error <3tau/4 and absolute-branch error <tau. Compose these with(10). The target channels, on all outputs, are

    rho -> G_*(t)rho G_*(t)^* tensor sigma_S(t),
    rho -> V_*(t)rho V_*(t)^* tensor sigma_S(t).

For tau=epsilon/2 this yields

    D_final<3tau/4+r_prep<=7epsilon/8,
    D_flag<tau+r_prep<=epsilon.                         (11)

The first is on[tminus,T]; the second uses exactly V_* from(2) for EVERY t in[0,T]. Actual flag projection acts only on operating record R1 and retains all other outputs. Its comparison is subnormalized and is never divided by early success probability. The record bias is already in exact H_b and the q-dependent target, so there is no additional kappa T allowance or record scalar phase.

For the event of exactly one total head on retained F radii1..ell, physical R1 and all other heads vacant, nominal failure is <(3tau/8)^2. The actual and ideal-loaded complete states both have trace one; preparation changes an event probability by at most r_prep/2. Therefore

    Prob(success)>1-9epsilon^2/256-r_prep/2
                 >=1-9epsilon^2/256-epsilon/4.         (12)

Record1 alone has at least this probability. The linear mixed-state preparation term is not squared. Logical correctness is asserted through(11), not merely through this event. Neither statement supplies a readout mechanism, capture or persistent post-horizon flag.

## 6. Explicit costs for this conditional family

With tau=epsilon/2 the exact coefficients are

    kappa=Lambda epsilon^3/(64*10^18),
    j=Lambda epsilon^2/(32*10^12), mu=Lambda/4,
    gamma=alpha(tau) Lambda tau^(7/2)/(8*10^15).

Hence the sufficient general energy allowance in(8) is exactly

    E_ex<=Lambda epsilon^5/(4096*10^18).                 (13)

The actual Gibbs prescription is

    beta>=max{[64/(15Lambda)]log(128(124+4ell)/epsilon^2),
          [64*10^18/(Lambda epsilon^3)]log(128/epsilon^2)}, (14)

where ell is the NEW value in(1). The old coarse or split m must not be used in this formula.

The provisional970a resource calculation gives

    ell,m,device qubits,device blocks,jT
                         =Theta(epsilon^-3 log(e/epsilon)),
    T=Theta(Lambda^-1 epsilon^-5 log(e/epsilon)).         (15)

Adding m positive head penalties changes constants and the block count(4), not these orders; the operation time is unchanged by the exact uniform head phase. Uniform bounds on N0 give alpha bounded above and below by positive constants, so the smallest positive supplied coefficient remains gamma=Theta(Lambda epsilon^(7/2)). Mu and kappa are larger. Coefficient magnitudes are not manufacturing tolerances.

Equation(15) gives log m=O(log(e/epsilon)). Thus the explicitly chosen beta at equality in(14) has sufficient order Theta(Lambda^-1 epsilon^-3 log(e/epsilon)); its record term supplies the lower order for this chosen formula. The same order applies to the optional joint-block-diagonal sufficient formula. The allowance(13) has order Lambda epsilon^5. No necessary temperature or lower bound on all preparation methods is claimed.

Compared with the checked split556956/0a05 family, device size changes from Theta(epsilon^-11/2) to the conditional order in(15), and operating time from Theta(Lambda^-1 epsilon^-15/2) to(15). The sufficient energy allowance, bias and inverse-temperature order do not change: record excitation still controls that chosen preparation criterion. The actual apparatus, targets, volume logarithm and required loader are different. This comparison is between sufficient conditional families, not faster execution on identical hardware or a numerical advantage at a particular error.

Counts and T exclude supplied loading/cooling/readout apparatus and their durations. The closed number-conserving H_* cannot itself cool occupied heads into vacuum. Even its ground sector leaves arbitrary old P. No cooling procedure, bath, low-energy certification mechanism, coherent input source, autonomous loader, native coefficient/basis supplier, old literal processor interface, robustness composition, reset or permanent halt follows.

## 7. Exact evidence and provisional status

Paths are under N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- New operation source `common_product_resonant_router_resources/PROPOSAL.md`:970a84e5e9157c6a9d5934f00df59491de19e6c88402efe0e14b44e68bc1479b. Authored and completely read immediately before this task. Its distinct check is pending at drafting; this source is an explicit conditional transfer, not a self-check of970a. The accepted incoming/half-line/outgoing/late component checks recorded there do not alone validate its simultaneous budgets.
- Preparation `common_product_biased_record_preparation/PROPOSAL.md`:9979b614d77b98bf8bc63b6b87b69305beb7cf7607adf5722ae57b759728627e; distinct review162eddafa64f5b71afefea600f8811461d6a6b71ec60e16e2a8d9cc79c41e578. Both completely read and hash verified here. Reused only for its all-head, state-distance, complete-loader and operational-composition interface, with actual m/target/loader replaced as specified above.
- Split `common_product_biased_record_resource_split/PROPOSAL.md`:556956724f545b8241171490a990e71e1c08eb1e1e67d84a82e6a44d2162a49b; distinct review0a05d11b377f1e4318aae54227b5a3afa90d829b207acc05f745e5fb4ef01965. Both completely read/hash verified here, including the review's explicit preparation compatibility section. Its old L/Q distance is NOT substituted into the new device and its loader is not automatically reused.
- Original biased finite532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123, review5ef953f745c598888b329aa8fafa94d226a18f2cc01fa57f09b165e0e7a1a936, packetcf080/review315a and single-control/local-block ancestry retain unchanged complete scoped reads through970a and9979. The all-head source e6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668, earlier record-ground source aaa0786b19ec5b0c37923e712fe8f9b80c3490a1c495a7bb5f2482c97402a1bc and grouped reviewf7156129dbe665ba0951bbc92f49b4a22b8b577801890a78a1cbb3e6b2f4aea7 retain the unchanged all-head inventory premises as explicitly restated and checked by9979/162edd.

ROOT requested this algebraic transfer after proposing the resonance resource route. I authored970a, the earlier weak-bias preparation and other components; the existing preparation source and its separate check were exposed throughout this derivation. This is same-model author continuation, not blind or independent validation. A distinct check must verify the actual new apparatus counts/caps, state and spectator contract, target phase, general versus joint-block-diagonal preparation criteria, and all conditional resource/operation statements. No component or prior compatibility check is presented as that new check.

Only this proposal was created. No source/W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, numerical sweep, delegation or publication occurred. A truncated filename inventory was replaced by a bounded inventory; the actual source/review reads above were complete and untruncated.
