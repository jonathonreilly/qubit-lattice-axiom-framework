# Energy-certified preparation interfaces for the finite single-control apparatus

Status: conditional finite-volume energy and loading-interface theorems, selectively checked and unaudited. Positive onsite penalties make blank apparatus states ground sectors while preserving a controlled finite-operation error budget. Low energy then certifies proximity to those sectors. This does not construct cooling, energy measurement, input injection or an autonomous loader. Every preparation and loading output remains in the comparison.

The nominal apparatus, supplied occupation bases and coefficients, exact path/program input, finite-window dynamics and logarithmic resource recipe are those of the [single-control bounded theorem](COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md), regular PR9712 at `abcec11eb9dbbd585c530f8003d0b0c18d703612`. The two constructions below are separate alternatives. No robustness allowance is automatically composed with their changed inventories.

## 1. An all-head lower bound and a constant blank-head gap

Write the nominal H=cI+K, with

    c=8b+8(sqrt(2)-1)j,       N=sum_(head v) n_v,
    m=124+4ell head qubits.

Subtracting the sixteen vacancy scalars leaves -2b n_v at each of four core endpoints, -(sqrt(2)-1)j n_v at eight distinct writer junctions, and positive full-support blocks everywhere else. Since j<=b/8, positivity on every local occupation and fiber gives

    K >= -2b N.

This is a full finite operator inequality, not an extrapolation of one-head scattering. It includes double occupations and arbitrary P/R states and does not require commuting blocks.

Add one positive onsite occupation at every head, including emitters and final sites:

    H_mu=H+mu N,       mu=Lambda/4,
    H_mu-cI >= gN,     g=mu-2b>15Lambda/64.

The exact ground sector is head vacuum with arbitrary P and R, of apparatus dimension four. The gap is at least g. Blank heads do not select R=0. Uniform mu is a supplied new coefficient in the existing occupation basis, not a derived native interaction.

The largest nominal head incident norm sum is D1+2b<9Lambda/64; adding mu keeps it below25Lambda/64. P remains belowLambda/2 and R has load8j. The all-qubit cap remains belowLambda, with no energy rescaling. There are still126+4ell qubits and no new edges; listing the m penalties separately gives288+8ell blocks.

Because [H,N]=0,

    exp(-itH_mu)Pi_n=exp(-i mu n t)exp(-itH)Pi_n.

On the exactly one-head operating seed, both the normalized complete target and the SAME unnormalized whole-horizon record target acquire the known phase exp(-i mu t). The common physical phase becomes exp[-i(c+mu)t]; the -i scattering factor, shift57, packet, logical operation and times are unchanged. This is not a single scalar on superpositions of different head numbers.

## 2. A weak record bias selects blank Record, at a cost

A second construction also adds a positive record occupation:

    H_*=H+mu N+kappa n_R,
    H_*-cI >= gN+kappa n_R.

For kappa>0 the exact ground space is blank heads, R=0 and arbitrary P, of dimension two. Its gap is at least min(g,kappa). This follows from the operator lower bound and equality on the displayed kernel; it does not assume that n_R commutes with the writer.

Use the nominal recipe at tau=epsilon/4, 0<epsilon<=1, with its actual horizon T=7ell/(8j), and choose

    kappa=epsilon/(16T).

The record bias does NOT merely change a common phase. Full-space Duhamel gives

    ||exp(-itH_*)-exp[-it(H+mu N)]|| <= kappa |t|.

Thus its vector-map cost is at mostepsilon/16 and its complete or subnormalized channel cost at mostepsilon/8 on[0,T]. The comparison targets retain the explicit mu phase; no record-dependent phase is fitted.

Since ell>=1 and j<Lambda/1024, T>896/Lambda and kappa<Lambda/14336. Hence kappa<g and the stated gap lower bound is kappa. R's incident load8j+kappa remains belowLambda. The head and P loads are unchanged from section1. This alternative has289+8ell positive blocks,126+4ell qubits and no added edges. Its operating horizon is unchanged, but its preparation cost is not thereby bounded.

The full [head-energy derivation](../outputs/common_product_energy_preparation_2026_10_18/source_checks/head_energy/PROPOSAL.md) and [record-ground derivation](../outputs/common_product_energy_preparation_2026_10_18/source_checks/record_ground/PROPOSAL.md) retain the exact inventory, phases and cap accounting.

## 3. General energy certificates retain preparation correlations

For either ground projection Q, let the fixed supplied apparatus state omega include an arbitrary correlated preparation environment. It must be independent of the logical input and its reference. Let Delta denote the proved gap: g for blank heads, kappa for the selected blank-head/blank-record recipe. Then

    q=Tr[(I-Q)omega] <= E_ex/Delta,
    E_ex=Tr[(H_modified-cI)omega].

For q<1, the normalized projected comparator is

    omega_0=Q omega Q/(1-q).

It factors as the specified pure blank head/record state times an arbitrary old-fiber/environment state sigma: old P,R for the head-only case, old P for the record-ground case. Projecting a purification gives overlap sqrt(1-q), so

    ||omega-omega_0||_1 <= 2sqrt(q).

Trace norms are unhalved. All preparation correlations are retained. No physical projection, postselection, energy-measurement protocol or state formation is supplied by these equations. A coherent ground/excited superposition can attain the square-root cost, so2q is not a valid general replacement.

## 4. The loading channel is an explicit remaining premise

Supply the ordinary logical program/path input, possibly entangled with an arbitrary logical reference, independently of omega. Assume a fixed loading channel with FULL declared outputs: the operating apparatus and spectators containing old physical fiber information, consumed-input remnants, workspaces and every physical loading/dilation output. It acts identically on passive preparation and logical references.

On the ideal comparator omega_0, require an unhalved diamond-norm loading error at mosteta relative to

    rho -> E_seed rho E_seed^* tensor sigma_out.

E_seed is exactly the parent's one-head program/path seed with R=0 and all remaining heads vacant. The input-independent sigma_out must retain sigma by a lossless isometric relocation of accessible old P/R (head-only) or P (record-ground), with identity on inaccessible preparation references and declared workspace outputs. Correct apparatus marginals after discarding garbage are insufficient. CPTP notation does not itself establish retention: any implementation must account for its full outputs and meet this contract on them.

The head-only comparator leaves R arbitrary, so its loader still needs a supplied blank operating record or a declared reset/resource process retaining old R's information. The record-ground comparator already has physical R=0, so an ideal loader needs no additional fresh blank record. Both still require the coherent logical input, head excitation injection and old-P entropy retention. No local positive loading Hamiltonian, workspace preparation, timing or energy cost is constructed here.

Using the SAME loader on omega and omega_0, complete contractivity gives preparation error

    d_prep <= 2sqrt(q)+eta.

During operation, spectators must be isolated from the device and undergo specified input-independent evolution (identity suffices), retained in the target. This is an interface premise, not a deduction from the energy gap. Actual residual heads or spectator correlations are paid through the trace error under full unitary evolution; they are not compressed to the one-head sector.

## 5. Complete-operation and absolute-branch budgets

For nominal accuracytau the parent complete normalized-target channel error is<3tau/4 on the final window [3ell/(4j),7ell/(8j)]. Its SAME unnormalized record-branch channel error is<tau throughout[0,T]. Both comparison maps include exp[-i(c+mu)t] and the retained input-independent spectator state. The branch uses the original B_fin(t), its -i factor and n+ell+57 Fourier shift; it is not changed to zero early or divided by a success probability.

Require q<=epsilon^2/64 and eta<=epsilon/4, so d_prep<=epsilon/2. Sufficient general energy thresholds are g epsilon^2/64 for the head-only construction and kappa epsilon^2/64 for record-ground preparation.

| Construction | Nominal accuracy | Complete final channel error | Entire-horizon subnormalized branch error |
|---|---:|---:|---:|
| Uniform head penalty | tau=epsilon/2 | <7epsilon/8 | <epsilon |
| Head penalty plus weak record bias | tau=epsilon/4 | <13epsilon/16 | <7epsilon/8 |

All channel errors are unhalved diamond norms, include every apparatus/spectator output, and permit arbitrary logical references. The second row adds at mostepsilon/8 from the noncommuting bias in addition to the nominal and preparation costs. The final window retains relative width1/6. None of these is a normalized rare-success guarantee.

Define joint success to require R=1, exactly ONE total head on retained F sites, and every other head vacant, with all other outputs retained. The ideal-loaded head-only failure is<(3epsilon/16)^2; for the biased device the ideal-loaded vector error is<3epsilon/32+epsilon/16=5epsilon/32. Preparation changes any event probability by at mostd_prep/2, since both complete states are normalized. Consequently joint success, and hence record1 success alone, exceed respectively

    1-9epsilon^2/256-epsilon/4,
    1-25epsilon^2/1024-epsilon/4.

The linear preparation loss is not incorrectly squared as though a mixed-state trace error were a pure-state amplitude. Logical correctness still comes from the complete channel comparison.

## 6. Optional Gibbs criteria and explicit resource tradeoffs

These are conditional on supply of the stated exact finite Gibbs state; no bath or equilibration dynamics is implied.

For H_mu, number-n sectors have dimension4 binomial(m,n), energy at leastc+gn and four exact ground eigenvaluesc. Scalar eigenvalue bounds give

    q_beta <= 1-(1+exp(-beta g))^(-m) <= m exp(-beta g).

Its normalized ground block is blank heads tensor I_(P,R)/4. On the exact apparatus Gibbs state the ground/excited blocks are orthogonal, so its trace distance to that block is2q_beta. This sharper cost applies to complete retained preparation outputs only if their JOINT state is block diagonal, for example a supplied product spectator. A Gibbs apparatus marginal with a coherent retained purification still requires the general2sqrt(q_beta) bound.

Under the joint block-diagonal premise, q_beta<=epsilon/8 and eta<=epsilon/4 suffice for the first row above. An explicit sufficient inverse temperature is

    beta >= [64/(15Lambda)] log(8m/epsilon).

For general retained correlations use beta g>=log(64m/epsilon^2) instead. Both selected prescriptions have orderTheta(Lambda^-1 log(1/epsilon)) because m=Theta(epsilon^(-11/2)). Neither prepares blank R in this construction.

For H_*, the record does not commute with its contacts. Use finite-dimensional min-max: H_*-cI>=gN+kappa n_R implies ordered eigenvalues are bounded below by those of the right side. Both kernels have dimension two. Summing scalar Boltzmann factors, without asserting exponential operator monotonicity, gives

    q_beta <= m exp(-beta g)+exp(-beta kappa).

The ground block is blank heads and R=0 tensor I_P/2. To pay the general square-root preparation cost, it suffices that

    beta >= max{g^-1 log(128m/epsilon^2),
                kappa^-1 log(128/epsilon^2)}.

In this selected recipe,

    T=Theta(Lambda^-1 epsilon^(-15/2)),
    kappa=Theta(Lambda epsilon^(17/2)),
    beta_sufficient=Theta(Lambda^-1 epsilon^(-17/2) log(1/epsilon)),
    E_ex_allowed=Theta(Lambda epsilon^(21/2)).

The weak record gap dominates the sufficient temperature requirement. These are sufficient prescriptions, not necessary temperatures, fabrication/measurement resolutions or cooling times. A constant record bias is not justified by this Duhamel estimate; its accumulated kappa T error would be uncontrolled. This is a limitation of that estimate, not an impossibility claim about a separately analyzed stronger-bias architecture.

## 7. Verification and remaining obligations

The [grouped distinct review](../outputs/common_product_energy_preparation_2026_10_18/source_checks/REVIEW.md) checks both candidates with one shared inventory reconstruction, and separately checks their gaps, phases, Gibbs arguments, complete loader contracts and mixed-state probability budgets. The [source manifest](../outputs/common_product_energy_preparation_2026_10_18/SOURCES.json) pins complete arguments and inherited evidence. The [integration record](../outputs/common_product_energy_preparation_2026_10_18/INTEGRATION_RECORD.md) discloses source exposure and composition limits. Checks are analytical, same-model and source-exposed, with inherited authorship and checks explicitly identified. They are not blind/model-diverse replication, a thermal experiment or retained audit.

The installed closed Hamiltonians conserve head number and cannot themselves cool an occupied head sector into vacuum. Ground-sector certificates and assumed Gibbs states supply neither a bath nor its isolation, energy certification, cooling/loading duration or entropy disposal. Specified occupation bases, coefficients, logical inputs, complete loading and spectator isolation remain premises. No end-to-end autonomous initialization, native Record/readout, old literal processor transfer, permanent halt, irreversible capture or reset/reuse is established. Earlier robustness bounds require fresh accounting for these changed Hamiltonians and are not imported here.
