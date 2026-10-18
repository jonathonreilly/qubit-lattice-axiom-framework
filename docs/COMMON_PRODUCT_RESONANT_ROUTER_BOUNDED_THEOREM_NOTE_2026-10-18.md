# Resonance-resolved finite autonomous router budgets

Status: selectively checked conditional finite-operation theorem and preparation interface; unaudited. Supplied-device mathematics, not a native implementation.

The [biased endpoint-seeded router](COMMON_PRODUCT_BIASED_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9719 at f0bd96dbe873e9fcab215dca22e6e1e3654df434, previously used sufficient size of order tau^(-11/2) and physical time of order Lambda^-1 tau^(-15/2). The present composition rebuilds every finite-operation allocation using the actual source pole, rather than a global second-derivative bound on its narrow spectrum. Its explicit sufficient family has size Theta(tau^-3 log(e/tau)) and physical time Theta(Lambda^-1 tau^-5 log(e/tau)). Constants may be extremely large. These are orders of a selected sufficient family, not necessary costs, optimality or practical performance.

The physical construction remains the single-program, shared-record, positive-block router of the biased-operation source532866, with one physical kappa n_R term. The length and time change. Its source emitter is occupied, record is blank, and every other head is vacant. An arbitrary coherent superposition of the two emitters is supplied; it is not a sitewise product state. Exact blocks, coefficients, occupation bases and absence of unwanted interactions remain premises. No wavepacket is prepared or Hamiltonian switched at the comparison times.

## Actual family and complete output

For 0<tau<=1 set h=eta²=zeta=r=tau/10^6, D1=Lambda/8, D0=zeta D1, b=eta D0, j=b²/D0 and kappa=rj. Let N0,N1 be the stated real strict-internal derivative bounds and M_jet the ordinary outgoing map's bounds through third order. Define alpha=[4096(2+N0)]^-2, rho=alpha tau sqrt(h), gamma=rho j and the same normalized spectrum g=chi F/sqrt(p), with its real quintic cutoff. The [complete composition](../outputs/common_product_resonant_router_2026_10_18/source_checks/composition/PROPOSAL.md) defines an explicit positive coefficient C from third-order oscillatory bounds and J=N0+80N0/rho+N1. Choose

    u=10^12 max{1,eta^-1/tau,J/tau,
       C rho/(h² tau),[C rho/(h² tau)]^(2/3),
       rho^-2 log[10^8/(tau rho)]},
    ell=ceil(100u), t0=u/j, tminus=3ell/(4j), T=7ell/(8j).

The time/length choice is simultaneous, with every coefficient computed before u. It retains the actual compensated incoming emitter and outgoing cap. Counts are126+4ell qubits and165+4ell listed positive blocks; full-support incident loads stay below Lambda. The coefficient scales are j=Lambda tau²/(8*10^12), kappa=Lambda tau³/(8*10^18), gamma=alpha Lambda tau^(7/2)/(8*10^15). Their magnitudes are not tolerance guarantees.

With E(k)=2j(1-cos(k)) and q=acos(cos(k)+r/2), the exact ideal radial profile remains

    B_n(t)=(-i)/sqrt(2pi) integral exp[i n q+i(ell+57)k-itE(k)]
                                      sqrt(q'(k))g(k) dk.

Full-line normalization uses the q Jacobian. Let B_fin retain1<=n<=ell and let beta=B_fin/||B_fin|| with positive normalization. The target includes the parent's controlled logical path operation, unchanged program, record1, and vacancy of every other head. Its common phase is exp(-ict), c=8b+8(sqrt(2)-1)j. The checked composition bounds the complete isometry error by3tau/8 throughout[tminus,T], with arbitrary passive references. It implies unhalved complete-channel error below3tau/4 and joint record1/retained-output probability above1-9tau²/64. No apparatus coordinate is discarded.

For every0<=t<=T the same unnormalized comparator uses B_fin instead of beta. The absolute record1 branch vector error is below tau/2 and its unhalved subnormalized complete-channel error is below tau. No early branch is renormalized or replaced by another target. This is finite-window operation; it supplies neither a physical measurement nor permanent halt.

## Why the bound changes

The incoming boundary integral isolates the source resonance in the energy variable. For offsets0,-1,-2 it gives a point bound2rho exp(-rho²u/sqrt(1-rho²))+4000rho/(h²u²). Integration pays both the exponential with prefactor1/rho and the algebraic rho/(h²u) tail, including the actual contact norm and three radial levels.

Outgoing tails instead use a real-variable Laplace representation of the pole. The favorable phase sign permits three integrations by parts. This requires the actual quintic cutoff's W^(3,1) regularity and newly bounded real third derivatives of the full network; arbitrary C² regularity would not suffice. No analytic continuation of the network is assumed.

Whole-half-line estimates handle the initial match, late incoming field and both sides of the ideal finite output. Adverse signs require splitting the Laplace variable and retaining an exponential term with prefactor sqrt(h)/rho. The high-variable term is controlled by whole-space Parseval, using the correct q Jacobian for inelastic output. Boundary point estimates alone would not justify these half-line bounds.

The full composition checks all twelve allocations: early contact, occupied-source survival, unwanted conjugate incoming field, omitted spectral mass, early projection/normalization, early leads, early internal field, integrated finite contacts, late incoming field, scattering discrepancy, late internal field and output truncation. It separately checks the whole-horizon flag target. The source's band-edge survival remainder, distinct signs of F and conjugate(F), and old first-derivative internal cost remain paid. The resulting dominant sufficient term is rho^-2 log[10^8/(tau rho)], with rho=Theta(tau^(3/2)) and j=Theta(Lambda tau²).

## Preparation re-instantiation

The [new-family preparation interface](../outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/PROPOSAL.md) evaluates the entire device at tau=epsilon/2, with actual head count m=124+4ell. It installs mu=Lambda/4 on every head and retains precisely one record bias. The full-support lower bound is H_*-cI >= (mu-2b)N+kappa n_R, with mu-2b>15Lambda/64. Its exact ground sector is blank heads/record0 with arbitrary old program; its gap is kappa. All head loads remain below25Lambda/64, program load belowLambda/2, and the new block count is289+8ell.

For a fixed joint apparatus/environment state independent of logical input, let q be its weight outside that ground sector. Joint trace discrepancy from the normalized ground comparator is at most2sqrt(q). An actual new complete-output loader is separately assumed for this new apparatus and emitter positions. It must retain old program/environment information and every loader output in an input-independent spectator, isolated during operation. A loader for the older device does not establish this premise.

Taking q<=epsilon²/64 and loader error<=epsilon/4 gives preparation discrepancy<=epsilon/2. Full-unitary evolution retains errors outside the one-head sector. The nominal target gains exactly exp(-imu t); no extra record phase is inserted. Final complete-channel error is below7epsilon/8, absolute whole-horizon branch error belowepsilon, and joint output/record success exceeds1-9epsilon²/256-epsilon/4.

Sufficient supplied-state alternatives are excess energy<=Lambda epsilon^5/(4096*10^18), or a Gibbs marginal with

    beta >= max{64/(15Lambda) log(128m/epsilon²),
                  64*10^18/(Lambda epsilon³) log(128/epsilon²)}.

This Gibbs bound uses finite-dimensional min-max, not operator monotonicity of the exponential. Retained bath correlations still require2sqrt(q);2q is justified only by joint block diagonality. The chosen inverse-temperature order remains Theta(Lambda^-1 epsilon^-3 log(e/epsilon)); the record gap still controls it. Counts and operating time exclude loader, cooling and readout resources. This is a re-instantiated conditional interface, not a loading or cooling mechanism.

## Limits and evidence

The improvement is a new finite-family composition, not a transfer of the standalone geometric launch result or an inference from only one improved error term. Preparation and thermal criteria above are explicitly re-instantiated for the new device and fresh loader contract. No robustness theorem transfers automatically to its changed length, runtime and target.

Native Hamiltonian supply, physical Record identification, initial head/path injection, cooling, loader realization, readout, capture and reset/reuse remain open. The literal older processor is not identified with this controlled router. Later recurrences are uncontrolled. Source-exposed same-model analytical checks have shared ancestry; they are not blind replication, empirical evidence or retained audit. Full source arguments, exact revisions and scoped reviews accompany this publication. Historical pending labels in frozen sources record drafting chronology; the named scoped reviews resolve them only at their checked scopes. No physical axiom or editable prompt is changed.

Scoped evidence: [incoming contact](../outputs/common_product_resonant_router_2026_10_18/source_checks/incoming/PROPOSAL.md), [outgoing contact and third jets](../outputs/common_product_resonant_router_2026_10_18/source_checks/outgoing/PROPOSAL.md), [whole-half-line tails](../outputs/common_product_resonant_router_2026_10_18/source_checks/halfline/PROPOSAL.md), [late negative tails](../outputs/common_product_resonant_router_2026_10_18/source_checks/late/PROPOSAL.md), and [distinct full-composition review](../outputs/common_product_resonant_router_2026_10_18/source_checks/composition/REVIEW.md). Each component source has its scoped review and exact hash in the packet manifest.

The preparation re-instantiation has a [distinct scoped review](../outputs/common_product_resonant_router_2026_10_18/source_checks/preparation/REVIEW.md). Neither that review nor the operational theorem implements its assumed loader.
