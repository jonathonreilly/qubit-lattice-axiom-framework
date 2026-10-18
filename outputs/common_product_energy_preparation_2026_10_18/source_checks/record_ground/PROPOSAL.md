# Weak record bias and an energy-certified blank apparatus

New bounded author proposal, requiring distinct review. This construction provides a conditional energy/Gibbs criterion for blank heads AND record zero while retaining a supplied coherent logical-input loading channel. It does not construct cooling, a bath, energy measurement, input injection or autonomous initialization. ROOT suggested the record bias, budget and loading direction after the exposed blank-head assessment; the calculations below reconstruct that candidate.

## 1. Exact finite operator and all-head lower bound

Use the accepted finite single-control apparatus of source76b5 and integrated logarithmic recipe02b432, at nominal accuracy tau=epsilon/4, 0<epsilon<=1. Keep every positive full-support block, all heads, the physical program P and shared record R. Let m=124+4ell be the number of heads, N=sum_v n_v, and

    H=cI+K, c=8b+8(sqrt(2)-1)j.

The eight core vacancy blocks contribute -2b n_v at each of four core endpoints after scalar subtraction. The eight writer vacancies contribute -(sqrt(2)-1)j n_v at eight distinct writer junctions. These vertices do not coincide with the core endpoints. All other remainders are their original positive blocks on their COMPLETE local Hilbert spaces, including simultaneous heads and arbitrary P/R states. Since j<=b/8,

    K >= -2b N.                                             (1)

This discards a sum of positive operators, not individual matrix entries or selected one-head columns. Noncommutation of writer contacts with n_R causes no problem for this inequality. Total head number commutes with H, although n_R generally does not.

Set mu=Lambda/4 and define the installed modified Hamiltonian

    H_* = H+mu N+kappa n_R,
    g=mu-2b>15Lambda/64,
    A=H_*-cI >= gN+kappa n_R=:D.                            (2)

The two added kinds of blocks are positive onsite occupations. For kappa>0, D is positive and its kernel consists precisely of vacant heads and R=0, with arbitrary P. On that kernel the original remainders vanish and the bias vanishes, so A=0 there. Conversely A>=D excludes any other zero-energy vector. Thus the ground space is exactly

    |vac_heads> tensor |0>_R tensor C^2_P,

of dimension two, with energy c. It is not a unique ground vector and does not select the logical program. The complement has energy at least Delta=min(g,kappa). This full finite-space statement does not assume X_R conservation, a fermionic spectrum or dilute occupancy.

## 2. Finite dynamics, physical cap and counts

Let T=7ell/(8j) be the ACTUAL horizon of the nominal tau recipe, and choose

    kappa=epsilon/(16T).                                   (3)

On the one-head sector the chemical potential gives the exact common phase exp(-i mu t). The record bias does not have this property. Duhamel on the complete finite Hilbert space, with arbitrary references, gives

    ||exp(-itH_*)-exp[-it(H+mu N)]|| <= kappa |t|.            (4)

No commuting of n_R through H is used. In particular the bias cannot be represented by a fitted record-output phase. For 0<=t<=T its operator error is at most epsilon/16, and the unhalved channel error is at most epsilon/8. Left projection onto record 1 gives the same bound for the subnormalized branch maps. The latter is a completely positive trace-nonincreasing operation and contracts trace distance; it need not commute with evolution.

The nominal complete target and its SAME unnormalized whole-horizon branch target both acquire precisely exp(-i mu t). Their physical common phase is now exp[-i(c+mu)t]; their -i scattering factor, n+ell+57 Fourier shift, common packet, retained program and all blank-head comparator factors are unchanged. These are comparison targets for the biased evolution, with (4) charged as an error. The final interval remains [3ell/(4j),T], of relative width 1/6.

At D1=Lambda/8 the largest original head load is below 9Lambda/64. Adding one norm-mu term per head keeps it below 25Lambda/64. P remains below Lambda/2. R has load 8j+kappa. Since j<Lambda/1024 and ell>=1, T>896/Lambda, hence kappa<Lambda/14336 and the R load remains below Lambda. In particular kappa<g, so Delta=kappa for this prescription. No rescaling or extra physical operation time is needed for this NOMINAL cap. Combining this construction with perturbed vacuum or matrix-robustness families requires a separate proof and is not done here.

The device has unchanged 126+4ell qubits. Listing the m chemical-potential terms and the one record bias separately gives 289+8ell positive blocks. No edges or head sites are added. This assumes the supplied onsite interactions in the already supplied occupation bases; it is not a native interaction derivation.

## 3. Energy and conditional thermal criteria

Let Q project onto the ground sector and let omega be an apparatus state, possibly correlated with an auxiliary preparation environment S. Energy is evaluated on the apparatus marginal. For E_ex=Tr(A omega),

    q:=Tr[(I-Q)omega] <= E_ex/Delta.                       (5)

If q<1, the normalized ground-projected comparison state is

    omega_0=Q omega Q/(1-q)
           =|vac,0_R><vac,0_R| tensor sigma_(P,S).

Projection of a purification and contraction of trace norm imply

    ||omega-omega_0||_1 <= 2sqrt(q).                       (6)

This statement allows arbitrary P/S correlations. It is a mathematical comparison, not a physical postselection instruction. No energy certificate determines sigma_(P,S), and none is needed if that state is retained as a spectator under the loading contract below.

For a separate explicitly ASSUMED finite Gibbs state exp(-beta H_*)/Z, one must not invoke operator monotonicity of the exponential. Instead use ordered eigenvalues: A>=D implies lambda_i(A)>=lambda_i(D) by the min-max principle. Both operators have exactly two zero eigenvalues. Therefore their traces on the positive eigenvalues satisfy

    Z_exc exp(beta c)
       <= 2[(1+exp(-beta g))^m(1+exp(-beta kappa))-1],
    Z_ground exp(beta c)=2.

Consequently

    q_Gibbs <= 1-[(1+exp(-beta g))^m
                         (1+exp(-beta kappa))]^-1
             <= m exp(-beta g)+exp(-beta kappa).           (7)

For the last step use 1-ab<=(1-a)+(1-b) for a,b in[0,1], and 1-(1+x)^-m<=mx. This argument remains valid despite [H,n_R] generally being nonzero. The Gibbs ground block is exactly |vac,0_R><vac,0_R| tensor I_P/2, so it does select blank R conditionally on ground occupancy but leaves P mixed. It does not prepare the supplied logical input.

A sufficient thermal prescription for q<=epsilon^2/64 is

    beta >= max{g^-1 log(128m/epsilon^2),
                kappa^-1 log(128/epsilon^2)}.             (8)

This makes each term in (7) at most epsilon^2/128. For a general energy-certified state, the sufficient alternative is E_ex<=kappa epsilon^2/64. These are alternative criteria, not an assertion that either state or its energy certification is supplied by H_* itself.

## 4. Explicit assumed loading contract and retained outputs

The following is an additional physical-interface premise, not a construction from the Hamiltonian. A logical program/path input L with arbitrary passive reference Z is supplied independently of the prepared apparatus/environment state omega. The preparation environment S need not be pure. Any passive preparation reference within S is acted on by the identity throughout loading and operation. A fixed CPTP loading channel F has declared FULL outputs: the physical device plus an output spectator S_out retaining the old P/preparation degrees of freedom and ALL physical loader/environment outputs. No comparison traces S_out away. Old-P relocation may act on physical P and declared loader workspace, never on a passive preparation reference.

For the chosen sigma_(P,S), require that applying F to omega_0 and the input implements the nominal seed isometry E, together with an input-independent spectator state sigma_out, to unhalved diamond error at most eta:

    || F_(omega_0) - [X -> E X E^* tensor sigma_out] ||_diamond
         <= eta.                                         (9)

The diamond norm includes arbitrary Z. Ideally sigma_out retains sigma_(P,S), up to a declared isometric relocation of the physical old-P factor and specified other loader outputs, tensor identity on each passive preparation reference. This is where old physical P may be swapped into a supplied input register rather than erased. Equation (9) must include every physical loader/environment output, rather than only the installed device; a partial trace that deletes old-P entropy would not meet this contract. Additional workspace states and their preparation are supplied resources. CPTP notation alone does not establish this retention condition: an implementation must provide its full dilation/output accounting and satisfy (9) on those outputs. No such implementation or cost is established here.

For eta=0, (9) needs no fresh R=0 supply because omega_0 already has physical R=0. The remaining supplied coherent program/path input is loaded onto P and the emitters while all other heads stay vacant. Unknown old-P entropy is allowed to remain in S_out independently of the logical input. Achieving this with a local clocked or autonomous apparatus, keeping every output, is still a proof obligation. The loading stage is not claimed to be generated by H_*.

Independence of omega from L is essential to this channel statement. An energy bound alone cannot repair arbitrary initial logical/preparation correlations. By (6), changing omega_0 to omega changes the full loading channel by at most 2sqrt(q) in diamond norm. Thus

    d_prep <= 2sqrt(q)+eta <= epsilon/2                    (10)

if q<=epsilon^2/64 and eta<=epsilon/4. Subsequent evolution on the device and identity on S_out preserves this bound; record-branch projection contracts it. No error is multiplied by apparatus dimension. This is a full-output approximate seed contract, not a measurement-and-discard procedure.

## 5. Complete finite-output and whole-horizon budgets

At nominal tau=epsilon/4, the pinned theorem gives a complete normalized-target channel error strictly below 3tau/4=3epsilon/16 on the final window. Its unnormalized branch channel error is strictly below tau=epsilon/4 on the ENTIRE horizon. Tensoring the input-independent sigma_out changes neither bound.

Adding (4) and (10) yields

    final complete channel error
       < 3epsilon/16 + epsilon/8 + epsilon/2 =13epsilon/16,

    entire-horizon subnormalized branch channel error
       < epsilon/4 + epsilon/8 + epsilon/2 =7epsilon/8.     (11)

Both are unhalved diamond norms. The branch target remains one fixed formula at every time, namely the nominal B_fin(t) common packet with phase exp[-i(c+mu)t], controlled path action, R=1 and sigma_out. It is not normalized at early times or redefined to zero. No rare-success conditional-fidelity claim follows from (11).

For an honest success-probability statement, the ideal loaded pure one-head dynamics has vector error less than 3epsilon/32+epsilon/16=5epsilon/32 from the normalized final target. Thus its joint retained-F/record-1 failure probability is below 25epsilon^2/1024. The loading discrepancy (10) changes any event probability by at most d_prep/2, because both complete states have trace one. Therefore the actual loaded apparatus has final joint success probability

    > 1-25epsilon^2/1024-epsilon/4.                       (12)

Record-1 probability alone is at least that joint probability. This conservative estimate allows mixed preparation states and arbitrary logical references. It does not assert the quadratic-in-epsilon success bound of a perfect pure seed after adding O(epsilon) preparation trace error. The simpler event bound 1-13epsilon/32 also follows directly from the first channel bound in (11).

## 6. Costs, failures and physical scope

For fixed Lambda and the nominal logarithmic prescription at tau=epsilon/4,

    m=Theta(epsilon^(-11/2)),
    T=Theta(Lambda^-1 epsilon^(-15/2)),
    kappa=Theta(Lambda epsilon^(17/2)).

The new small record coefficient therefore creates a small gap. The explicit sufficient beta selected at equality in (8) has order

    beta=Theta(Lambda^-1 epsilon^(-17/2) log(1/epsilon))

as epsilon tends to zero. The record term, rather than the constant head gap, dominates this chosen bound. This is a sufficient inverse-temperature prescription, not a lower bound on every possible preparation method and not a cooling-time estimate. The general energy allowance above is of order Lambda epsilon^(21/2). No fabricability or energy-measurement resolution is established by quoting these numbers.

The tempting strong-bias route is not justified: a constant kappa would improve the record gap but give an uncontrolled kappa T dynamical budget and disturb the noncommuting writer. The tempting phase-only treatment is false because n_R does not commute with the writer. The original head-only Gibbs proposal left R maximally mixed in its vacuum sector; the bias fixes that energetic selection at the price of the small gap, not for free. Closed H_* still preserves N and cannot cool an occupied sector to vacuum. Nor does a gap supply a bath, detailed balance, mixing rate, entropy sink, measurement, autonomous loading or fresh logical input.

No robustness composition, native coefficient supplier, permanent record latch, capture/reset, repeatable operation or old literal processor transfer is asserted. Approximate low-energy preparation replaces an exact blank-R/head assumption only conditionally on the explicit state/energy and loading premises. All new calculations need a distinct check; the separately developing head-energy/loading source is not a premise.

## 7. Exact ancestry and exposure

N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- Starting assessment `blank_supply_opportunity/ASSESSMENT.md`: `0eab0fc5eed427936637115f9daba30468a9e23fd94a7461d5aafd1d90bbd287`, authored by this worker, not an independent premise check.
- Nominal integration `common_product_single_control_publication/NOTE.md`: `02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde`.
- Single-control source `common_product_single_control_router/PROPOSAL.md`: `76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01`; prior check `549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0`.
- Logarithmic recipe `common_product_logarithmic_flag_policy/PROPOSAL.md`: `7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8`; prior check `d1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3`.
- Actual vacancy geometry and positive writer inventory reuse staged core `c91300a5eb6db28e67e4b494398c57c3c53bc39d2da8c800a12c284cc5d6c729` and prior check `61de4ee29dd3838c4fc7c3bd19c49bf0cd4cb4bacf5ad3e8e10ca06c864e27c1`, at their original scopes. Full-support scalar separation was also inspected in matrix source `f9e427ccd5ec0a25f0c28639f9707728489a7a7dcca139e6f9fe03289d9b8a20`, check `3d7be49f11dadbae49ed7c84a29e2a32ae8d38a83c1552a630716cc54c554b39`; no perturbed-family result is imported.

The four initiating source hashes were refreshed unchanged here. Complete sources were read in the immediately preceding coherent tasks; their unchanged identities, full-support and nominal finite-performance scopes are reused. I authored earlier components/checks, and ROOT exposed the bias, Gibbs comparison and proposed budget before this derivation. This is same-model, same-effort author continuation, not blind or independent verification. No thermal experiment or numerical solver is involved. Only this proposal file was created; no W, Git, checkpoint, axiom, editable prompt, existing source or model setting was changed, and no delegation or publication was performed.
