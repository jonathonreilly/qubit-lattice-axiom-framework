# Removing the optional runtime head penalty

New source-exposed author refinement requiring a distinct check. The direct boundary/rest/cat supply contract needs no uniform head penalty. Removing that penalty from BOTH the reference and actual runtime, and bounding the remaining long tails at their actual coefficient jbar, gives a smaller global background allowance. Conditional on the new quadratic-background lemma388eb, still awaiting its distinct check at this writing, the resulting sufficient physical time is Theta(Lambda^-1 epsilon^-17 log^5(e/epsilon)). No preparation, ground-state or Gibbs conclusion is retained or inferred.

## 1. Actual operator with no uniform head penalty

Use the complete supplied finite family970a at0<tau<=1, Lambda>0, with its exact source/cutoff prescription, ell, jbar=Lambda tau^2/(8*10^12) and U=7ell/8. In particular U and ell are Theta(tau^-3 log(e/tau)). Add the ordinary Q input and the exact entrance-SWAP comparison of c97b as in c1cb, but do NOT install any mubar N term. Denote this reference by Hbar_new,0. It is the actual unpenalized biased router with the two enlarged entrance bonds. All its other blocks, including the ONE positive kappabar n_R, are retained.

Define Bbar_0 by replacing each of its two SWAP entrance blocks by

    Q_(jbar/2)(i,j), (jbar/2)n_i, (jbar/2)n_j.

Every one of these residual blocks is positive. On the whole original Hilbert space,

    Hbar_new,0=Bbar_0-(jbar/4) sum_l Omega_l.            (1)

The twelve products,48 ancillary qubits and96 positive gadget blocks are exactly the checked joint b54c construction. Set

    K=48, Delta=Lambda/4, nu=Delta alpha,
    scale=10Delta alpha^4/jbar,
    Hact,0=scale Bbar_0+48nu I+H0+V,
    T=U/(10Delta alpha^4), Tbar=U/jbar,
    s_joint=-24nu^2/Delta+27nu^4/Delta^3.                (2)

The comparison generator is scale Hbar_new,0+(48nu+s_joint)I. There is no uniform head penalty on original heads or ancillary qubits. It is not removed by a time-dependent quench: the installed Hamiltonian is fixed as(2) throughout the experiment.

The nominal reference conserves head number. Its prior optional penalty would have been a common one-head phase only, so removing it changes none of the970a source, scattering, cut, internal, normalization or absolute-branch errors. The nominal phase is now cbar alone, where cbar=8bbar+8(sqrt(2)-1)jbar. The actual gadget need not conserve head number; the new analytic simulation comparison includes all its occupation sectors and never invokes a one-head scalar identity for its actual dynamics.

## 2. Exact inventory and full-space global norm

The unchanged finite internal network has24 core blocks,68 writer blocks and68 cable blocks, totaling160 before the record bias. It includes the scalar-producing positive vacancy repairs, endpoint on-sites, programmed mediator blocks and terminal record contacts. Add the one record bias to obtain161 blocks independent of ell. Each has full-support norm<Lambda on the exact reference coefficient family. No vacancy scalar has been subtracted from their norm estimate. In particular this constant sector costs at most161Lambda globally; this is deliberately coarse and includes the actual finite cable lengths.

Each I extension has ell ordinary Q_jbar bonds plus one combined source block. Each F extension has ell ordinary bonds plus one cap. The two entrance bonds to be replaced belong to those I extensions, at radii0--1, and are distinct from the distant sources. After replacing them by the six residual blocks, the remaining extension inventory is:

| Blocks | Number | Full-support norm each |
| --- | ---: | ---: |
| Ordinary radial Q_jbar | 4ell-2 | 2jbar |
| Combined source | 2 | 3jbar |
| F cap jbar n_ell | 2 | jbar |
| Residual Q_(jbar/2) | 2 | jbar |
| Residual (jbar/2)n | 4 | jbar/2 |

The combined source is Q_gammabar+(jbar-gammabar)n_adj+(2jbar-gammabar)n_emit. Its vacuum eigenvalue is0; its one-head matrix has diagonals jbar,2jbar and off-diagonals -gammabar, hence eigenvalues[3jbar+-sqrt(jbar^2+4gammabar^2)]/2. Its double-occupation eigenvalue is3jbar. Since0<gammabar<=jbar, both one-head eigenvalues are positive and the larger is at most(3+sqrt(5))jbar/2<3jbar. Its FULL norm is therefore3jbar. The additional neighboring radial bond supplies the extra jbar on the adjacent site's diagonal in the full launcher; it is not part of this combined block. This verifies the relevant source estimate without restricting to one head. Likewise Q_a has full norm2a, including its double-occupation eigenvalue2a.

The table has4ell+8 blocks. Its norm sum is

    (4ell-2)2jbar+6jbar+2jbar+2jbar+2jbar
       =8jbar(ell+1).

Consequently the required full-space global ceiling is

    ||Bbar_0||<=B0max:=161Lambda+8jbar(ell+1).          (3)

It applies with arbitrary original head occupations and program/record states. It is not a bandwidth bound derived from one moving head, nor a subtraction of a potentially important scalar. All positive background blocks are counted exactly once. The number of Bbar_0 blocks is161+(4ell+8)=169+4ell. Adding96 gadget blocks gives265+4ell actual blocks. There are still175+4ell qubits: no head or ancillary qubit is removed, only124+4ell optional on-site penalty blocks.

Incident-load bounds only improve upon deleting positive penalty terms. For clarity, original unpenalized head loads are bounded by the source5jbar, radial4jbar, core endpoint6bbar+4jbar and mediator D1bar+2bbar ceilings; original P load is belowLambda/2. The scaled background loads cannot increase when scale<=1. Added gadget loads are12nu at each entrance head,24nu at each P/Q, and2Delta+2nu at an ancilla. At alpha<=1/(32K) every sum remains<Lambda. R keeps its8jbar+kappabar load before scaling. Fixed Manhattan range35, disjoint square placement and absence of unlisted couplings are unchanged. This remains arbitrary positive finite-range two-body supply, including complex Y couplers, not the old nearest-neighbor primitive set.

## 3. Quadratic interface and simultaneous choice

Apply388eb's bidisc lemma with B=scale Bbar_0 and its prescribed norm ceiling beta=scale B0max. It requires alpha<=1/(32K), beta<=Delta/32. Its exact axis identity E(0,y)=yB and ancillary parity give the all-order mixed allowance Cmix alpha^2 beta with Cmix=16384 K^2, including nonscalar terms. The full literal-state comparison is

    ||exp(-itHact,0)J
       -J exp{-it[scale Hbar_new,0+48nu+s_joint]}||
       <=16Kalpha+|t|[R6+Cmix alpha^2 beta],
    R6=Delta(8Kalpha)^6/[1-(8Kalpha)^2].                (4)

J appends the twelve supplied cats. This is a whole original-Hilbert-space comparison, tensor-extended over passive references, retaining every ancilla. Its proof does not require a positive head gap or head-number conservation by the gadget. The only new use of the lemma is the smaller explicitly verified global ceiling(3).

Given0<epsilon_g<=1 choose alpha EXACTLY as

    min{1/(32K), epsilon_g/(48K),
        sqrt[5epsilon_g/(2(8K)^6 U)],
        sqrt[epsilon_g*jbar/(3 Cmix U B0max)],
        [jbar/(320 B0max)]^(1/4),
        [jbar/(10Delta)]^(1/4)}.                       (5)

The last entry gives scale<=1. The penultimate entry gives beta/Delta=10alpha^4 B0max/jbar<=1/32. The first gives16Kalpha<=1/2. Thus all contour, endpoint and cap conditions hold simultaneously. On|t|<=T the remaining entries pay

    16Kalpha<=epsilon_g/3,
    TR6<=(2/15)(8K)^6 U alpha^2<=epsilon_g/3,
    T Cmix alpha^2 beta
       =Cmix alpha^2 U B0max/jbar<=epsilon_g/3.         (6)

The full simulation error is therefore<=epsilon_g throughout the entire horizon. No background norm, mixed scalar phase or time factor is omitted. This is not automatic transfer of a small one-head scattering error to a larger Hilbert space; the imported lemma is expressly a full-space norm theorem under the verified global smallness condition.

## 4. Exact sufficient orders and common output

For tau and epsilon_g fixed positive multiples of epsilon, equation(3) gives

    B0max=Theta(Lambda epsilon^-1 log(e/epsilon)),

because jbar ell=Theta(Lambda epsilon^-1 log(e/epsilon)) eventually dominates the constant161Lambda. This statement is about the selected upper bound, not a necessary lower bound on ||Bbar_0||. The entries in(5) have orders

    1, epsilon, epsilon^2/sqrt(log(e/epsilon)),
    epsilon^(7/2)/log(e/epsilon),
    epsilon^(3/4)/[log(e/epsilon)]^(1/4), sqrt(epsilon).

The fourth eventually controls the minimum, giving

    alpha=Theta(epsilon^(7/2)/log(e/epsilon)),
    scale=Theta(epsilon^12/[log(e/epsilon)]^4),
    T=Theta(Lambda^-1 epsilon^-17 [log(e/epsilon)]^5),
    ell=Theta(epsilon^-3 log(e/epsilon)).               (7)

The finite output window remains[3ell/(4scale*jbar),T], with relative width1/6. The earlier epsilon^-27 and epsilon^-21 sufficient families remain valid under their stated installed penalties and prescriptions. This comparison changes an optional runtime term and the norm estimate; it keeps the cap, complete-output metric, boundary/cat supply and geometric range. It supplies no optimal exponent, necessary time or practical engineering advantage; constants remain extremely large and coefficient magnitudes are not precision tolerances.

The complete target retains the incoming translation(ell+57)k, inelastic outgoing n q(k), amplitude -i sqrt(q'(k))g(k) and positive finite normalization on1<=n<=ell, with q=acos(cos k+kappabar/(2jbar)) and reference time scale*t. All original energies except the removed penalty scale together, so this ratio is unchanged. The physical comparison scalar is now exactly

    exp{-it[48nu+s_joint+scale*cbar]}.                  (8)

There is no exp(-it scale*mubar) or additional record-bias phase. Higher scalar shifts are paid by(4), not fitted away.

## 5. Joint supplied state, whole-horizon branch and limits

As in the checked boundary contract, the physical input comprises ordinary Q and the two I emitters in their one-excitation dual-rail code. Arbitrary program/path/passive-reference coherence is allowed. Supply a fixed joint rest/environment state independent of that input, satisfying

    ||omega-omega_ideal||_1<=epsilon_rest,
    omega_ideal=|vac_other_heads,0_R><...|
             tensor |cat+><cat+|^tensor12 tensor sigma_PE.

All old P information and its passive environment E are retained. On the ideal final output the exact entrance gauge places the logical program in P and relocates sigma_PE to sigma_QE with identity on E. The comparator has the controlled output path, R1, every other original head including emitters vacant, and all twelve cats retained. Any preparation device's outputs must be included explicitly; no reset or traced environment is silently permitted. The joint trace contract may be supplied directly or bounded by2sqrt(q) from an explicitly specified joint vacuum/R0/cat projection. That projection argument is a state-distance inequality, not an energy certificate or physical state preparation process.

For ideal rest, combine(4)--(6) with970a and the exact gauge at time scale*t. Its final complete vector error is<3tau/8+epsilon_g; its absolute record-1 vector discrepancy from the SAME unnormalized B_fin(scale*t) target for all0<=t<=T is<tau/2+epsilon_g. The target uses(8) at every time and retains cats and the relocated old fiber. Record projection and ideal branch norm are contractions; no rare-success normalization is introduced.

Full-unitary contraction pays actual rest errors even if they populate other ancilla sectors or multiple original heads. The complete unhalved channel bounds are consequently

    final <=epsilon_rest+3tau/4+2epsilon_g,
    whole-horizon record-1 branch <=epsilon_rest+tau+2epsilon_g,
    final joint success >=1-(3tau/8+epsilon_g)^2-epsilon_rest/2. (9)

Choosing tau=epsilon/4, epsilon_g=epsilon/8 and epsilon_rest<=epsilon/4 gives11epsilon/16,3epsilon/4 and1-49epsilon^2/1024-epsilon/8 respectively. Joint success includes the displayed cat and original-head vacancy comparator event, not only a reduced logical measurement.

No previous preparation theorem was needed for(9), and none is restored by deleting the penalty. The old head-gap, restricted input-energy or Gibbs criteria are unavailable here. Blank R, other-head vacancy, cats, encoded physical input and their joint reference quantifiers remain directly supplied assumptions. Native coefficient generation, cat preparation, ordinary-path-qubit encoding/placement, starting-state energy injection, readout, capture and permanent halt remain open. The refinement removes optional installed terms; it adds no stronger interaction or preparation supply, and it does not claim to derive the supplies already assumed.

## 6. Evidence and new proof obligations

All paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- New analytic dependency common_product_two_body_background_refinement/PROPOSAL.md388ebae502c0687fbbf267294d36ad7c32ddfa3dc32c1cd5d8ffbf7cb7af15fa was authored, fully read back and frozen immediately before this task. Its distinct review is pending at this writing. Equation(4) and this composition remain conditional on that interface being checked.
- Physical assembly common_product_two_body_scaled_operation/PROPOSAL.mdc1cbdb0eb1b7cc4b865c3ad8b8323b646eeff47e195c3239e297f007f0884bb7, review4a1bc10174a72991ef77648188deedce151ad69f3e196ed572648064de6e2f4f, and joint b54c6f29ea780efdcad7f33def048a0b5f9436fe8125ce3c2b2b416cabde4436/review6dfaeacb3a3b1b2f2dfdcdf4c2f862b41687dac7a9dc08b35adae1865e4e90e3 retain complete checked reads from the immediately preceding task. Their original optional-penalty supply is explicitly changed here, not silently retained in the phase or norm.
- The exact fixed-block count passage in common_product_single_control_router/PROPOSAL.md76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 was refreshed in full:24core+68writer+68cable blocks before the record bias. The full finite device definition and source/cap/count passage in common_product_biased_record_finite_seed/PROPOSAL.md532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123 was refreshed in full. A broad search output truncated, so it was not treated as complete evidence; these exact passages were subsequently read directly without truncation. Their unchanged complete prior reads supply the geometry and block conventions.
- The new actual length/time source remains common_product_resonant_router_resources/PROPOSAL.md970a84e5e9157c6a9d5934f00df59491de19e6c88402efe0e14b44e68bc1479b with reviewcb0e278a7311651ea9f8d258089cba00a10fb03bb37457d2f8db1d5864af5da7, fully read in this sequence. Boundaryb58d047e8b7d6598951f84cb5c275d9709fe19b9b99e0383558536b581332ad9/reviewdcb52ff26e482a9d175d9e5c357624a51e2c5e40c8cbad72512853698ec2c901 supplies the direct state/input contract, not a required energy criterion.

ROOT suggested removing the optional penalty, estimating tail strengths separately and the possible exponent17. This author reconstructed the precise169+4ell background inventory, all-occupation source norm, explicit B0max, simultaneous minimum, phase change and full-state transfer after that exposure. This is same-model source-exposed author work, not independent checking. The decisive new check is whether every scalar/core/writer/cable/source block is counted in(3), whether removing the optional penalty changes any actually used operating premise, and whether all changed scale conditions and complete outputs in(5)--(9) follow at the stated scope.

Only this proposal was created. No scientific executable, numerical sweep, delegation, old source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. Frozen earlier prescriptions remain unchanged.
