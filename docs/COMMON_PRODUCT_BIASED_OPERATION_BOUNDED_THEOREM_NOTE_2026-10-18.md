# Finite inelastic operation and stronger blank-record preparation criteria

Status: selectively checked conditional finite-device, resource and preparation-interface theorems; unaudited. Supplied-device mathematics, not a native implementation.

The [energy-preparation interface](COMMON_PRODUCT_ENERGY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9716 at `5aa1ce1e9c2f67dbc0c4e057e8dd98dbeb410c84`, selected blank Record with a weak positive field and paid its accumulated dynamical error. Here the field is included in the exact scattering, packet and finite-device dynamics. This permits a different sufficient record-gap prescription while retaining complete output and one absolute, unnormalized record branch throughout the finite horizon. The outgoing radial state changes: its record1 momentum is lower than the incoming momentum.

## 1. One physical record field and its actual scattering channels

Retain the parent's single physical program P, two24-head writers sharing ONE Record R, the two34-edge cables, positive local blocks, occupation bases and supplied program/path input. Add exactly one positive onsite `kappa n_R`. On the one-head space this is `kappa I_head tensor n_R`; restricting it to different coordinate regions does not install multiple biases. Head number and P remain conserved. Record occupation and X_R need not commute with the complete generator.

For fixed j>0, r=kappa/j and incoming k, put

    E(k)=2j(1-cos k), q(k)=acos(cos k+r/2),
    |k-pi/2|<=h<=.001, 0<=r<=.001.

Both channels are open, with sines>.99, and `E(k)=2j(1-cos q)+kappa`. The full48-dimensional writer outgoing inverse is below11. Its flux-normalized scattering differs from the zero-bias writer by at most480r. The source's strict endpoint inequality was corrected separately: `0<=k-q<=r`, strict at the upper end only when r>0.

Let C be the coherent controlled path operation, X the record flip, Z the record-diagonal phases `(exp(ik),exp(iq))`, and phi=-i exp(22ik). With

    e=13eta^2+5zeta, w=33h+480r, den=1-ew>0,

the exact full network has scattering error at most

    Delta=min{2,[2(e+w)+ew]/(1-ew)}

against the ordered comparator with forward through block `phi X Z^35 C` and reverse block `phi Z^35 C X`. The cable phases cannot be commuted through X. For supplied R0 incidence from I, the forward coefficient is exactly `-i exp(57ik) C` with record1. Its ordinary outgoing amplitude has the factor `sqrt(q')`, where `q'=sin k/sin q`, and spatial wave `exp(i n q)`.

The [local writer](../outputs/common_product_biased_operation_2026_10_18/source_checks/writer/PROPOSAL.md), [endpoint correction](../outputs/common_product_biased_operation_2026_10_18/source_checks/writer/CORRECTION.md) and [full network](../outputs/common_product_biased_operation_2026_10_18/source_checks/network/PROPOSAL.md) retain the literal matrices, positivity, geometry, feedback inverse and all-incidence phase ordering. These are not claims about a scalar phase on the entire record fiber.

## 2. Exact packet and actual finite endpoint seed

The [complete packet](../outputs/common_product_biased_operation_2026_10_18/source_checks/packet/PROPOSAL.md) retains all incoming/outgoing fields, the four external origins and118 strict internal head coordinates, with every program/record/reference component. Channel-wise change of variables `p=q(k)` supplies the correct Fourier measure. Remote-past separation plus exact self-adjoint evolution proves normalization; spectral completeness or absence of a finite seed's localized component is not assumed. Explicit first/second derivative bounds cover the complete scattering map and every finite coordinate.

The physical finite device has two I emitters at radius ell+1. Each source block is

    Q_gamma(ell,ell+1)+(j-gamma)n_ell+(2j-gamma)n_(ell+1).

Each F ray ends at ell with positive cap `j n_ell`. All source-pair and capped-end one-head diagonals are2j before the record threshold. The supplied seed places one head on the two I emitters with arbitrary coherent P/path/reference input, R=0, and every other head vacant. It is not an externally prepared incoming spectral packet.

The [finite derivation](../outputs/common_product_biased_operation_2026_10_18/source_checks/finite/PROPOSAL.md) compares the actual seed to detached reference launchers. Their occupied R0 subspace is invariant and has the ordinary4j norm bound; no such bound is asserted for the full microscopic generator. The single record field vanishes on this reference trajectory and cancels from the contact difference. Full-vector initial matching pays source, incoming, internal and localized residuals. Exact hopping-only cut identities and integrated bounds then pay finite returns through the entire stated horizon. The [inelastic phase envelopes](../outputs/common_product_biased_operation_2026_10_18/source_checks/phase/PROPOSAL.md) handle q(k), rather than reusing an elastic spatial phase.

## 3. Explicit sufficient family and complete finite contract

For nominal accuracy0<tau<=1 choose

    h=eta^2=zeta=r=tau/10^6, D1=Lambda/8,
    D0=zeta D1, b=eta D0,
    j=Lambda tau^2/(8*10^12), kappa=Lambda tau^3/(8*10^18).

This gives Delta<tau/512. The packet's explicit derivative formulas determine the demodulated outgoing triple M and internal triple N before the source or length is selected. Set

    alpha=[4096(2+N0)]^-2, rho=alpha tau sqrt(h), gamma=rho j,
    g1=80/rho, g2=600/rho^3, bminus=82/rho,
    H0=M0, H1=M0g1+M1, H2=M0g2+2M1g1+M2,
    J0=N0, J1=N0g1+N1, vmin=2j cos h,
    Ai=g2+(12j/vmin)g1+4j/vmin+48j^2/vmin^2,
    Ao=H2+24H1+212H0, Z0=2, Z1=2g1+1,
    L=max{1,bminus,g1+8,H0+H1,Z1+8Z0},
    Qbudget=max{1,eta^-1,rho^-2,J0+J1,Ai,Ao},
    u=10^16 max{1,(L/tau)^2,Qbudget/tau}, ell=ceil(100u),
    t0=u/j, tminus=3ell/(4j), T=7ell/(8j).

The [resource refinement](../outputs/common_product_biased_operation_2026_10_18/source_checks/resources/PROPOSAL.md) specifies every triple and rechecks all twelve costs and the whole-horizon branch at this NEW length. No numerical norms or implicit fixed-point choices occur. The time t0 is a proof comparison time; no block is switched then. The exact normalized launch amplitude is the parent's phase-preserving F with the specified C2 quintic cutoff and positive normalization.

The common scalar is `c=8b+8(sqrt(2)-1)j`. Define

    B_n(t)=(-i)/sqrt(2pi) integral
      exp[i n q(k)+i(ell+57)k-itE(k)] sqrt(q'(k))g(k) dk,
    Bfin=P_(1<=n<=ell)B, beta_F=Bfin/||Bfin||.

B has full-integer norm1. Bfin is nonzero throughout[tminus,T]. Its positive normalization, common -i, incoming-coordinate translation `(ell+57)k` and physical scalar phase are retained. The resulting complete vector bound is

    sup_(tminus<=t<=T)
    ||exp(-itH_F)E_seed-exp(-ict)J_F[beta_F tensor C tensor|1>_R]||
      <3tau/8.

All other heads, including emitters and F origins, are vacant in the comparator; their actual residuals remain in the norm. The bound includes arbitrary passive references. The unhalved complete-channel error is below3tau/4, and joint retained-F/record1 probability exceeds `1-(3tau/8)^2`. The final window has relative width1/6.

Throughout ALL[0,T], use the SAME unnormalized contraction

    V(t)=exp(-ict)J_F[Bfin(t) tensor C tensor|1>_R].

Then `||P_R1 exp(-itH_F)E_seed-V(t)||<tau/2`, giving unhalved subnormalized diamond error belowtau. It is not divided by a success probability or replaced by zero before t0. This is an absolute branch guarantee, not normalized rare-success fidelity, a readout procedure or an irreversible halt signal. Returns beyond T remain uncontrolled.

The device has126+4ell qubits and165+4ell positive blocks, including the one record field. All incident full-support norm sums remain belowLambda. The explicit biased derivative bounds imply alpha is bounded above and below by positive constants and

    ell,qubit_count,block_count=Theta(tau^(-11/2)),
    T=Theta(Lambda^-1 tau^(-15/2)), gamma=Theta(Lambda tau^(7/2)).

These are sufficient asymptotic prescriptions with extremely conservative fixed constants, not practical/optimal resource or fabrication-tolerance claims. They are derived for the biased device, not imported from the elastic family.

## 4. Blank-head and blank-record preparation certificate

Add `mu n_v` at EVERY head, including emitters/caps, with mu=Lambda/4. Let m=124+4ell and N=sum n_v. The full finite Hamiltonian obeys

    H_*-cI >= gN+kappa n_R, g=mu-2b>15Lambda/64.

This follows from full-support positivity after subtracting the sixteen vacancy scalars, not from one-head scattering. The exact ground sector is blank heads and R0 with arbitrary P, of dimension two. For0<kappa<g its gap is EXACTLY kappa: the blank-head/R1 pair attains that excitation energy. Counts become289+8ell blocks with unchanged qubits/edges. Head loads stay below25Lambda/64, P belowLambda/2, and R has load8j+kappa<Lambda.

On the exact nominal one-head operating seed, the added uniform penalty gives only the known factor exp(-i mu t). Thus both targets above receive exp[-it(c+mu)] in place of exp(-ict). The record field is already in the exact inelastic dynamics and is not paid again as kappa T or appended as a second record phase.

For a fixed supplied apparatus/preparation-environment state omega independent of logical input, let q be its weight outside the ground sector and E_ex its excess energy. Then

    q<=E_ex/kappa, ||omega-omega_ground||_1<=2sqrt(q).

The normalized projection omega_ground is a mathematical comparator, not a physical preparation step. All correlations with the preparation environment are retained.

Assume a full-output loader with unhalved diamond error at mosteta_load on that comparator. It must inject the supplied coherent logical input into the actual endpoint seed, retain old P information and every physical workspace/environment/dilation output, and act identically on passive references. Its input-independent spectator state must preserve old information by lossless relocation. Spectators remain isolated during operation with specified input-independent evolution. No local loader, excitation-energy supplier, cooling process or spectator-isolation mechanism is constructed. The ideal ground comparator already has R0 and needs no additional fresh blank record.

The preparation-channel error is at most `rprep=2sqrt(q)+eta_load`. Choose tau=epsilon/2, q<=epsilon^2/64 and eta_load<=epsilon/4. Then the full final channel error is below7epsilon/8 and the same whole-horizon subnormalized branch error is belowepsilon. Joint success exceeds `1-9epsilon^2/256-epsilon/4`; the mixed-state preparation cost is linear, not incorrectly squared.

For a supplied exact finite Gibbs state with beta>=0, finite-dimensional min-max yields

    q_beta<=m exp(-beta g)+exp(-beta kappa).

No exponential operator-monotonicity or commuting-record assumption is used. A sufficient prescription allowing arbitrary retained preparation correlations is

    kappa=Lambda epsilon^3/(64*10^18),
    E_ex<=Lambda epsilon^5/(4096*10^18),
    beta>=max{[64/(15Lambda)]log(128m/epsilon^2),
               [64*10^18/(Lambda epsilon^3)]log(128/epsilon^2)}.

Energy and Gibbs conditions are alternative sufficient certificates; neither supplies a measurement or a state. The Gibbs apparatus alone has trace error2q, but using that sharper bound on COMPLETE retained outputs requires joint block diagonality. A Gibbs marginal with a coherent retained purification still pays2sqrt(q).

The [preparation composition](../outputs/common_product_biased_operation_2026_10_18/source_checks/preparation/PROPOSAL.md) proves the loader, phase, gap, Gibbs and mixed-state budgets for the coarse finite family. The separately checked resource substitution preserves its finite error contract and local coefficients at the new ell; all counts and m use that new device. It therefore preserves these preparation criteria with the split prescription above, provided the complete-loader contract is assumed for the NEW seed isometry and apparatus. No physical coarse-device loader is automatically reused after moving the emitters.

## 5. What improves, and what remains supplied

The selected sufficient inverse-temperature order is now `Theta(Lambda^-1 epsilon^-3 log(1/epsilon))`, compared with `Theta(Lambda^-1 epsilon^(-17/2) log(1/epsilon))` in the earlier weak-bias family. The sufficient general energy allowance changes from orderLambda epsilon^(21/2) to orderLambda epsilon^5. These compare different sufficient families at the same total-error order, with different finite parameters and radial targets. They are not necessary operational temperatures, cooling times, optimal bounds, numerical advantages at a specified tolerance or end-to-end preparation runtimes.

Closed H_* conserves head number and cannot itself cool occupied heads to vacuum. The proof still supplies occupation bases, interactions, coefficients, coherent logical input, a preparation-state certificate, full-output loading and spectator isolation. Mathematical record probabilities do not identify a native Record or provide physical readout. The new controlled-path device is not a proved replacement for the old literal processor. No robustness theorem is automatically composed with the changed inventory. Permanent halt, irreversible capture and reset/reuse remain open.

The [source manifest](../outputs/common_product_biased_operation_2026_10_18/SOURCES.json) pins complete arguments, corrections, distinct reviews and inherited scope. The [integration record](../outputs/common_product_biased_operation_2026_10_18/INTEGRATION_RECORD.md) records the source-exposed, same-model checking and the explicit resource/preparation substitution. These are selective analytical checks with shared ancestry, not blind replication, model diversity, a physical experiment or retained audit.
