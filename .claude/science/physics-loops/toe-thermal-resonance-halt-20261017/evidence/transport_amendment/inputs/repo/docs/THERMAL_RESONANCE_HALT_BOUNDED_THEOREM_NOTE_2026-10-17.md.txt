---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: emitter_coupling_family_bounded_theorem_note_2026-10-17
target_blocker_text: "The supplied emitter still requires an exact seed and its published sufficient onset is 10^6/kappa^2. Account for finite thermal preparation and release, and recheck a shorter complete-output runtime."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Consult the exact source qualifications, source-transport decision and execution records; pursue native preparation/control/phase supply and complete capture/reset/reuse."
conditional_surface_status: "Exact nominal positive NN two-body apparatus, supplied auxiliary Gibbs marginal and finite classical setup controls, exact static loop phase and coefficients, complete quantum outputs with arbitrary passive references."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A complete conditional preparation/runtime composition with explicit finite horizon, output norm, scalar, chronological old aging and local hardware costs; no native realization is inferred."
source_science_acceptance_complete: true
wrapper_root_approval: see_separate_transport_record
canonical_execution: see_separate_execution_record
publication: see_separate_publication_record
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Thermal preparation and resonance-scale autonomous output

**Claim type:** `bounded_theorem`. **Current status:** conditional support.
The resonance, both preparation constructions, staged release and final
composition have selective mathematical checks and root source qualifications.
These are conditional theorems; canonical reproduction and publication status
follow their separate actual execution and integration records.

**Runner:** [scripts/thermal_resonance_halt_2026_10_17.py](../scripts/thermal_resonance_halt_2026_10_17.py).

The [parent coupling-family theorem](EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md)
starts from an exactly prepared emitter. This milestone supplies two explicit
positive-control preparation models and their finite release into the same
runtime. It also improves the sufficient onset through a new directional
cutoff, finite-contour and full localized-vector estimate. Both changes retain
every modeled clock, source, emitter, old-system and passive-reference output.

Fix the exact nominal ladder, one actual kappa in `[1e-12,1e-8]`, bandwidth
`sigma=1e-6` and emitter position `L=12`. Every other runtime coefficient,
phase and edge is unchanged. The complete infinite-clock isometry error is
below **0.003832 for every t >= T = 1/kappa^2**. A finite clock with
`M=ceil(50T)` gives error below **0.004832 only on [T,2T]**. At the largest
coupling, this is `T=1e16`, `M=5e17` and `M+5=500000000000000005` qubits.
These remain enormous sufficient resources in declared Hamiltonian units;
they are not physical seconds, measured resources or minimum costs.

The unchanged old Hamiltonian and target gate are

\[
 K=2I+Z_1Z_2,\qquad
 W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25}.
\]

After a complete setup of duration s and seed phase Phi_setup, the comparator is

\[
 \mathcal I(t)=\zeta e^{-i[\Phi_{\rm setup}+(\nu+2\kappa)t]}
 \mathcal B_{\kappa,t}e^{-i(s+t)K}W.
\]

The actual normalized outgoing packet in B uses the source's complete
`f_kappa rho_kappa`. It is common to all old input columns of one apparatus;
it is not a fixed nominal waveform shared across different kappas. Its time
index is runtime t. The old system ages through every setup interval and
runtime. The physical scalar `nu+2kappa` remains, and E0 is not counted again
as an extra runtime phase. Only `[W,K]=0` is used for chronological composition;
the actual interacting Hamiltonian need not commute with K.

## The two preparation contracts

The alternatives are separate physical control prescriptions. They are not
combined into one Hamiltonian or credited each other's resource budget.
The input is a supplied auxiliary Gibbs marginal, potentially correlated with
the arbitrary old/reference input. Its bad seed probability d gives complete
unhalved trace error at most `g(d)=d+sqrt(d(4-3d))`, using the unconditioned
old/reference marginal. A product joint input instead permits `2d`. This
distinction comes from prior correlated-marginal machinery and is essential.

| Contract | Exact-product preparation P | Interacting preparation I |
|---|---|---|
| Auxiliary operator | `13Q`, after explicit positive counterterms | `H_aux >= Delta D`, unique seed ground |
| Supplied inverse temperature | beta=10 | beta=100, Delta=1 |
| Initial hold | 1 | 0 |
| Control release | Common cubic, duration 1 | Early cubic 10000 with emitter cancellation held; final emitter cubic 1 |
| Setup duration s | 2 | 10001 |
| Additional positive blocks | `2M+10` | `M+10` |
| Peak combined source-A load | 39.288796602545442 | 23.326419217626794 |
| Supplied incident slew allowance | 30 | 0.001 |
| Complete unhalved trace bound on runtime `[T,2T]` | `<0.009665` | `<0.009685` |

For P the full preparation Hamiltonian is exactly `K+chi_p I+13Q`.
For I it is `K+c_p I+H_aux`; this auxiliary operator is interacting, and
the thermal bound uses eigenvalue min-max order. It does not assume operator
monotonicity of the exponential or a free Gibbs law. Both count all M+3
auxiliary qubits and all many-head sectors. The full thermal comparison is
propagated before applying the supported seed estimate, so no one-head
scattering assertion is made about bad thermal components.

Both releases have a supported seed residual `kappa*tau/sqrt(2)` for the
interval during which emitter cancellation is removed. The staged construction
keeps the seed exactly invariant while all other controls are released, even
over a long finite early interval. That interval still contributes its exact
phase and old aging. An uncanceled emitter coupling persisting through it
would require a separate integrated error budget. No cancellation or exact
control precision is free physical supply.

The qualified I source narrows its early stage to **D>0** whenever nonempty
controls must be removed with finite slew. Its concrete D=10000 schedule
satisfies this restriction. The exit map `V_seed` is a scaled isometry with
Gram `2I` and norm `sqrt(2)`; the source formulas already pay that factor.
Frozen historical wording and the explicit qualification clarification are
both preserved. The interface review's historically pending I dependency is
discharged by its separate subsequent source qualification, not by P's result.

The added old-site loads during either preparation are **3.987514255266680**
and **2.397277262241192**, beyond the runtime cap two; the unchanged old edge
has norm three in addition. Cancellation in the summed Hamiltonian does not
remove any physical block from the incident norm sum. Both alternatives use
only existing sites and ordinary nearest-neighbor two-qubit or onsite blocks.
The complete source proofs below retain every individual block, identity
coefficient, scalar phase and signed quantum-system work formula. They do not
account for a microscopic cooling device, a controller's energy or a reset cycle.

## What the new proof changes

The earlier sufficient bound is `10^6/kappa^2`. Replacing its time constant
by one is not a valid substitution: naive fixed-coupling cutoff and absolute
clock bounds become 0.0016 and 0.00153 at the enlarged coupling. The new proof
pays endpoint jumps in the cutoff's total variation, keeps time decay on the
finite contour's vertical edges, and splits the complete real-band Cg/Kloc
vectors into center and derivative terms. It uses the full closed tail and
all seven complementary emitter directions, with the within-parity column
factor. Only scalar auxiliary rational functions and the exact cosine dispersion
are continued; no installed matrix resonance is assumed.

The actual transmission phase, clockwise density residue, restricted waveform
normalization and full seed discrepancy remain. The seed discrepancy includes
possible point spectrum; no absence-of-bound-states claim is needed. The original
strictly nonzero target residual allowance `1.76e-13` is retained. A fixed
finite device is not claimed to halt for all future times, and no arbitrary
accuracy or exact target implementation follows.

The preparation contribution is an explicit full-space realization of existing
thermal-reference and ready-range removal machinery for this literal emitter.
No broad literature-priority claim is made. The standard variation, contour,
spectral ordering, trace-distance and Duhamel tools retain their attribution.
No new external theorem or empirical prediction is imported.

## Source, evidence and publication boundary

The parent is regular PR9665 at `0e3993770a7a2dd872018f9dd3c76c2d9a624db9`.
It is unmerged conditional science, with its inherited dependencies and audit
limits. The complete new source bodies, review reports, actual executions,
failed routes and qualifications are preserved through the finite source map.
Historical pending labels and absolute path strings are original provenance;
the current qualification and execution records determine subsequent status.

The resonance reviewer froze a separate derivation and actual scalar/symbolic
run before seeing the author's executable/output. The two preparation routes
were frozen before their mutual mechanism exposure. Subsequent cross-reviews
are explicitly source-exposed. All use the same selected model and substantial
inherited source context. These are selective checks, not blind review of every
dependency, model diversity or retained audit.

Canonical reproduction executes only the three explicitly transported
author checking bodies: resonance scalar bounds and the two preparation
algebra/scalar checks. Their small fixtures corroborate written arguments;
they do not evolve the huge apparatus, prepare a Gibbs state or supply a
uniform theorem by numerical sampling. The input map has no historical path
fallback. A complete transport ledger separates path/cap/report adaptations
from unchanged scientific statements. Actual prelaunch bindings, failures,
resource limits and comparisons belong in the separate execution record.

Native positive-block, phase, thermal and controller supply remain open.
Temporal noise and joint calibration are outside this exact-family claim.
Complete capture/reset/reuse, practical resources, physical Hamiltonian/energy
and framework Record identification remain unresolved. Independent retained
audit and integrated-current-main landing checks remain separate obligations.
No science merge, main push, audit verdict, physical axiom or editable prompt
change is part of this milestone.

## Portable sources and separate decisions

The [source map](../outputs/thermal_resonance_halt_2026_10_17_inputs/SOURCE_MAP.json) resolves each historical label to exact repository bytes. The [publication status](../outputs/thermal_resonance_halt_2026_10_17_inputs/PUBLICATION_STATUS.json) preserves the mechanical preparation boundary. The [transport ledger](../outputs/thermal_resonance_halt_2026_10_17_inputs/TRANSPORT_EDIT_LEDGER.json) describes every executable adaptation; the [reproduction plan](../outputs/thermal_resonance_halt_2026_10_17_inputs/REPRODUCTION_PLAN.json) distinguishes historical evidence from the planned canonical calculation.

The preparation checkers retain their original parent-runtime numerical examples. They do not recompute the shorter resonance composition or the staged addendum; those analytical interfaces use the separately recorded source/interface qualifications. Their historical report status strings do not decide current source acceptance.

The complete embedded bodies below retain their historical frontmatter, pending labels and local path strings. Four bodies are byte-identical. The exact-product body has ten portable Markdown destination edits and one TeX control-space replaced by a thin-space command to remove trailing source whitespace. Its exact raw original is stored losslessly as gzip; the reversible body map identifies every change, with no mathematical expression altered.

[Resonance qualification](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/resonant_family_root_qualification/ACCEPTANCE.json).

[Exact-product qualification](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/preparation_product_root_qualification/ACCEPTANCE.json).

[Interacting qualification](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/preparation_interacting_root_qualification/ACCEPTANCE.json).

[Interacting wording clarification](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/preparation_interacting_root_qualification/CLARIFICATION.md.txt).

[Composition qualification](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/preparation_resonance_composition_qualification/ACCEPTANCE.json).

The [root transport decision](../.claude/science/physics-loops/toe-thermal-resonance-halt-20261017/ROOT_PORTABILITY_ACCEPTANCE.json) and [actual execution status](../.claude/science/physics-loops/toe-thermal-resonance-halt-20261017/EXECUTION_STATUS.md) record later integration and reproduction. They are outside the calculation input closure; the frozen preparation status does not self-certify a later run or publication.


## Preserved source: Resonance family

<!-- BEGIN PRESERVED SOURCE resonant_family_candidate/CANDIDATE.md -->
---
claim_type: conditional_author_theorem
actual_current_surface_status: new-author-candidate-awaiting-independent-review
independent_review: pending
root_qualification_of_this_composition: absent
retained_audit_claim: false
native_preparation_claim: false
scope: exact ladder, sigma 1e-6, kappa in [1e-12,1e-8]
joint_static_or_calibration_box: excluded
---
# Uniform resonance-scale escape for the supplied emitter coupling family

**Proposed theorem, 2026-10-17.** For every fixed apparatus in the already
qualified exact-ladder family

    10^-12 <= kappa <= 10^-8, sigma=10^-6, L=12,

the argument below gives complete isometry error **below 0.003832 for every
t >= T_kappa=1/kappa^2** on the infinite clock. The same Hamiltonian compressed
to **M=ceil(50/kappa^2)** clock sites gives embedded complete error **below
0.004832 on [T_kappa,2T_kappa]**. At the upper coupling endpoint this is
**T=10^16 and M=5*10^17**, with M+5 qubits. These sufficient onset and clock-size
prescriptions are a factor 10^6 smaller than the published family moment
prescription at every coupling; they remain enormous sufficient costs in
Hamiltonian units, not physical seconds or minimum resources.

The comparator remains the actual coupling-dependent outgoing waveform, with
the actual scalar nu+2kappa, literal old-system aging, both source qubits, the
emitter, the whole clock and any passive reference. The seed and Hamiltonian
are unchanged for each chosen coupling. There is no control action after zero.
The cutoff, all seven complementary emitter coordinates, all closed clock
tails, and possible point-spectrum seed components are included in the budget.

This is a new author composition, not an independently qualified theorem. One
bounded exact-scalar execution corroborates the arithmetic. It does not by
itself prove the contour, domain or operator arguments. The proof uses only
auxiliary scalar rational functions off the real axis; it does not continue
the installed noncommuting matrices or assume an exact exponential decay law.

## 1. Exact dependencies, apparatus and phase contract

`SOURCE_MANIFEST.json` binds 21 byte-exact snapshots under `inputs/`, with
original locations and SHA256 identities. Historical provisional labels in
the sources are preserved. Their later qualifications, also copied, authorize
conditional reuse of their stated mathematics, not acceptance of this result.

| Dependency | Snapshot | SHA256 |
|---|---|---|
| Qualified fixed-coupling resonance argument | `fixed.md` | c68350310ac5c471a38940660d76ba74d982306e2d62a28bbf9c330e79c984b8 |
| Separate fixed-resonance review | `fixed_review.md` | 4d7694f51ec85edcc38977bef43412d8c9bc5baba4fa3c35809fe9adf3d00284 |
| Fixed-resonance root acceptance | `fixed_acceptance.json` | 1a3f12fa10400e13906a09954f328e996f5cba2755a91c879399662f7a3f1421 |
| Fixed-resonance root qualification | `fixed_qualification.md` | 0f77e687647ceaec73408aaf58eea65b4291337c9bddb496e3ca759b1690bed5 |
| Exact coupling family and all affected spectral premises | `family.md` | 9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac |
| Family root acceptance | `family_acceptance.json` | a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325 |
| Family root qualification | `family_qualification.md` | 27a4008d6588fef9f0a5ac1d231d71240c12468db93d50a36ac2ee02f6ab7814 |
| Installed matching/seed construction | `installed.md` | 4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee |
| Weighted real-denominator estimates | `weighted.md` | a2e96d2947b1e0deef2417d4673ddc8afd54f7382236aee6913ba6cae98e32b5 |
| Earlier moment implication | `moment.md` | 31449e982b27e623491f4e9cb0c8239e2ff15ebc9605668b8e4684055c52410f |
| Exact scattering isometry and full-column convention | `generic_v2.md` | db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3 |
| Full-qubit local realization and geometry | `route.md` | f03626e591cddc3448bee72148edbee4717ae64af3a6543d4b5c184e7ef9f0a1 |
| Exact ladder certificate | `interval.json` | a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251 |

The manifest is authoritative for every source. The source family is reported
published in PR9665 at parent head
`0e3993770a7a2dd872018f9dd3c76c2d9a624db9`. No Git operation or remote freshness
claim is used here. The current workflow snapshot has SHA
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`, verified
against W when preparing this packet.

Use exactly

    J=3752638388379/125000000000000,
    q0=4.510351185997098, k0=2 arctan(1/q0),
    E(k)=2J(1-cos k), E0=E(k0), phi=2k0,
    I=[k0-sigma,k0+sigma] contained in (0,pi),
    v=1/40<E'(k), |E''(k)|<=2J, 2J/v<5/2,
    v0=E'(k0), v<v0<3/100.                              (1)

Every terminating decimal in the following table is exact:

| Parameter | Value | Parameter | Value |
|---|---:|---|---:|
| gA | 0.996878563816670 | gB | 0.599319315560298 |
| hAB | 3.999349697888060 | u | 0.544607276405587 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| DeltaA | 2.192035527016003 | DeltaB | 2.186826508897014 |
| mu0 | 0.321494607058201 | mu1 | -1.459892813020969 |
| nu=-mu1 | 1.459892813020969 | L | 12 |

With n=(I-Z)/2 and a=|0><1|, the literal old/source operators are

    K=2I+Z1 Z2,
    W=[(9+12i)I+(-16+12i)X1 X2]/25,
    C=DeltaA nA+DeltaB nB+hAB(nA+nB-aA^dagger aB-aB^dagger aA)
                                                +u nA nB,
    G=gA nA(I+X1)+gB nB(I+X2), B=K+C+G,
    VA=lambdaA(I+XA)+mu0 I, VB=lambdaB(I+XB)+mu1 I,
    Hg=h0 tensor I+B+P0 tensor VA+P1 tensor VB,
    h0=2J I-J(S+S*).                                    (2)

The source vacuum is Omega=|00>_AB, iota x=x tensor Omega and B iota=iota K
exactly. In the one-head sector the installed product-seed apparatus is

    V=|L>-exp(i phi)|L+2>,
    Htilde_kappa=[[Hg,kappa V],[kappa V*,B+E0]],
    Hphysical_kappa=Htilde_kappa+(nu+2kappa)I,
    Eseed x=(|1>_e tensor |all clock zero>) tensor iota x. (3)

V acts on every internal coordinate, without a vacuum-conditioned hopping.
The internal space has dimension 16, with two reducing parity blocks of
dimension eight. The exact old energies in each parity are 1 and 3.

The absolute-site scalar remains

    alpha=r_site1,(s=-1,p=-1)(k0), |alpha|=1,
    zeta=-exp(-4ik0)alpha, r0(k)=-exp(2ik).              (4)

Here alpha is the exact original reflection witness, defined by the frozen
ladder problem, not its rounded decimal approximation. The original central
target mismatch `<1.76*10^-13` remains included in the inherited reflection
budget. No new exact match or old-state-dependent phase is imposed.

## 2. Qualified family premises being reused

All of this section holds uniformly on I and on the stated coupling interval
by the separately qualified family proof. It is not inferred from its two
endpoints or from fixed-coupling acceptance. There is one open channel per
selected parity/old-energy band and a full complementary gap 0.18. Both old
energies and every complementary internal direction are included. The full
physical matching matrices have sizes 16 and 24 per parity; no new matrix
norm conversion is introduced here.

For z=exp(ik), define the unchanged scalar full-line quantities

    gplus=z^-L(1-exp(i phi)z^-2),
    gminus=z^L(1-exp(i phi)z^2),
    a=|gplus|<=2sigma, b=|gminus|>=bmin>3/2, b<=2,
    eta=2sigma/bmin<(4/3)sigma, |gminus'|<=26,
    Sigma_f,jj=(-i/E')[2-2cos(phi)z^2],
    Df=E-E0-kappa^2 Sigma_f,jj,
    Im Df=kappa^2(a^2+b^2)/(2E')>=19kappa^2,
    |Sigma_f,jj'|<=560.                                 (5)

Let chi be one for |k-k0|<=sigma/2, decrease linearly to zero on the two
remaining halves of I, and vanish outside I. Thus ||chi'||1=2. Put

    yref=kappa conj(gminus)/Df,
    N^2=(1/(2pi)) integral_I chi^2 |yref|^2,
    f=f_kappa=chi conj(yref)/(sqrt(2pi)N),
    tminus=1-i kappa^2 b^2/(E'Df),
    tau=tminus/|tminus|, rho=r0 tau.                     (6)

The new family mass lemma, not the old fixed-coupling variance bound, gives

    N^2>=1-3.5*10^-7, .99<N<=1, sqrt(2pi)N>2,
    ||f||2=||f rho||2=1, |tminus|>1/2,
    Aref=integral_I |f yref|/sqrt(2pi) in [N,1].         (7)

For the exact stationary columns Phi_j and old eigenvalues b_j,

    Gamma_t e_j=(1/sqrt(2pi)) integral_I f Phi_j exp(-itE),
    exp(-itHtilde_kappa)Gamma_0=Gamma_t exp(-it diag(b_j)),
    Gamma_t* Gamma_t=I,
    ||Eseed-Gamma_0||<.003,
    max_j |Raug,j-zeta omega_j rho|<.000714.             (8)

The eigenvalues omega_j of W are (-7+24i)/25 or 1. The complete seed-operator
bound includes every component outside this packet range, including possible
point spectrum. It is propagated once by unitarity. No spectral projection,
postselection or absence-of-bound-states premise is added. In particular the
old fixed-coupling point-amplitude ceiling 8*10^-5 is not reused at kappa=10^-8.

Write the full emitter column as y_j=yref u_j+delta y_j. With Pc the
seven-dimensional complement of u_j, the inherited inequalities are

    |(y_j)_j/yref-1|<4sigma,
    ||Pc y_j||<=6kappa w_c
       +6kappa^2 delta*206*2*(1+4sigma)|yref|,
    w_c=800/13841287201, delta=50/96889010407,
    integral_I |f| ||delta y_j||/sqrt(2pi)
                  <4sigma+epsilon_off,
    epsilon_off=10^-14.                                (9)

The last constant is the qualified family ceiling. The sharper fixed-coupling
10^-18 ceiling is not presumed uniform. All seven coordinates remain in (9).

The localized clock column has the exact form

    Cclock,j(k)=C_g,j(k)+kappa Kloc,j(k)y_j(k),
    ||C_g,j||<=31, ||C_g,j'||<=2700,
    ||Kloc,j||<20000, ||Kloc,j'||<10^6.                 (10)

These are physical Hilbert-space bounds. Kloc subtracts the open outgoing
wave on every clock site and includes the finite contact region and all
infinite closed tails; its derivative is an actual real-band Hilbert-space
derivative. It may depend on the selected old-energy channel j. There is no
assumption that its columns, or the C_g,j columns, are orthogonal within a
parity sector. Two error columns per parity cost at most sqrt(2)<3/2 times a
common column norm. Distinct parities are orthogonal. The reference vectors
u_j themselves are orthonormal.

For n>=0 the exact comparator, with emitter empty, is

    b_t(n)=(1/sqrt(2pi)) integral_I f(k)rho(k)exp[ikn-iE(k)t]dk,
    beta_kappa,t=b_t/||b_t||,
    Uideal,kappa(t)x=zeta exp[-i(nu+2kappa)t]
                         beta_kappa,t tensor iota exp(-itK)W x. (11)

Existence of this normalization at the new onset is proved below. One actual
f_kappa rho_kappa serves all four old columns. Different couplings generally
have different waveforms. The physical scalar is not replaced by a fixed
nominal scalar, and no extra exp(-itE0) is appended or removed.

## 3. Real-band rational comparison with the cutoff kept in the profiles

The elementary phase identity remains exact for every coupling:

    s=conj(Df)/Df,
    tminus-s=i kappa^2 a^2/(E'Df),
    |tau-s|<=2|tminus-s|<=4eta^2.                       (12)

For the middle inequality use |tau-tminus|=|1-|tminus||<=|s-tminus|.
Consequently f rho is within L2 distance 4eta^2 of
chi kappa r0 gminus/(sqrt(2pi)N Df). This is the retarded denominator;
the incoming profile instead has conj(Df). At D=1+i, with the rescaled
incoming coupling zero and outgoing width one, the correct residual is zero
whereas tminus-D/conj(D)=-2i. The sign is not optional.

Set q=k-k0, g0=gminus(k0), b0=|g0|=2sin(2k0)>3/2 and
Sigma0=Sigma_f,jj(k0). Then

    |Sigma0|=b0/v0, -Im Sigma0=b0^2/(2v0),
    Gamma=-kappa^2 Im Sigma0>19kappa^2,
    c=kappa^2 Re Sigma0/v0, gamma=Gamma/v0,
    |c|,gamma<3200kappa^2<sigma/4,
    v gamma>(125/4)kappa^2>30kappa^2.                  (13)

The last two inequalities hold even at kappa_+=10^-8. Define auxiliary
entire affine denominators and rational profiles

    D0=v0(q-c+i gamma), D0sharp=v0(q-c-i gamma),
    C0=kappa g0/(sqrt(2pi)N), |C0|<=kappa,
    h_in=C0/D0sharp, h_out=r0(k0)C0/D0.                (14)

Restrict h_in,h_out to I when using circle Fourier transforms. On the real
axis D0sharp=conj(D0); on a contour sharp means the analytic formula (14),
not literal conjugation there. The untruncated real-line profiles satisfy

    integral_R |h_in|^2=integral_R |h_out|^2=1/N^2.    (15)

Indeed the integral is kappa^2 b0^2/(2N^2 v0^2 gamma)=1/N^2.
Taylor's theorem on the real band gives

    |Df-D0|<=Jq^2+560kappa^2 |q|,
    |q|/|D0|<100,
    |Df-D0|/|D0|<=100(Jsigma+560kappa_+^2)
                     <epsilon=4sigma.                (16)

For the second line use |q|<=|q-c|+|c|,
|D0|>=v0|q-c| and |D0|>=Gamma; the resulting bound is
(1+2/b0)/v0<100. The numerators obey

    |gminus/g0-1|<18sigma,
    |r0 gminus/[r0(k0)g0]-1|<20sigma.                 (17)

The second derivative ceiling is 30 since |r0'|=2 and b<=2. Put

    r_in=(18sigma+epsilon)/(1-epsilon),
    r_out=(20sigma+epsilon)/(1-epsilon).

The pointwise incoming comparison is |f-chi h_in|<=r_in chi|h_in|;
its outgoing counterpart follows after (12). Hence, uniformly in kappa,

    ||f-chi h_in||2< (100/99)r_in <30sigma,
    ||f rho-chi h_out||2<(100/99)r_out+4eta^2<30sigma. (18)

The crucial change from the fixed-coupling proof is keeping chi in these
comparisons. The large L2 norm of (1-chi)h is not charged here. Its unwanted
half-line and scalar amplitudes are estimated separately in the next section.
The inequalities (18) are time uniform because multiplication by exp(-itE),
Fourier transformation and projection are contractions in L2.

## 4. Directional cutoff tails, including the outer endpoint terms

For either profile in (14) let w=(1-chi)h on I, with zero extension. On its
support sigma/2<=|q|<=sigma, (13) gives

    |q-c|>=|q|/2,
    |h|<=2kappa/(v|q|), |h'|<=4kappa/(v q^2),
    ||w||1<=4kappa/v.                                 (19)

The zero extension is piecewise W1,1 and has bounded variation, but does
not have zero endpoint trace. Its complete variation, including both jumps
to zero outside I, has the bound

    TV(w)<= integral_I |chi'| |h|
                 + integral_(sigma/2<=|q|<=sigma) |h'|
                 +|h(k0-sigma)|+|h(k0+sigma)|
          <= (8+8+4)kappa/(v sigma)
           =20kappa/(v sigma).                         (20)

The joins at |q|=sigma/2 are continuous; no additional value jumps occur.
The first term uses ||chi'||1=2 and |h|<=4kappa/(v sigma).
For the second, integrate 4kappa/(v q^2) over the two outer intervals.
At the two outer endpoints use |h|<=2kappa/(v sigma).

Both the incoming transform on n>=0 and outgoing transform on n<0 have
phase derivative magnitude at least m+vt, where m is a nonnegative integer.
Integrating by parts on the pieces and retaining the endpoints gives

    |(1/sqrt(2pi)) integral_I w exp(i phase)|
      <= [TV(w)+(2J/v)||w||1]/[sqrt(2pi)(m+vt)]
      <= Dcut/[sqrt(2pi)(m+vt)],
    Dcut=(kappa/v)(20/sigma+10).                       (21)

The phase-curvature term is bounded by
t(2J)||w||1/(m+vt)^2 <=(2J/v)||w||1/(m+vt). For vt>=1,
sum_(m>=0)(m+vt)^-2<=2/(vt), so (21) implies

    ||wrong half-line of w||<=Dcut/sqrt(vt),
    |(1/sqrt(2pi)) integral_I w exp(-itE)|<=Dcut/(2vt). (22)

The second estimate is the m=0 coefficient and uses 1/sqrt(2pi)<1/2.
These bounds do not depend on replacing the actual dispersion by an affine
one. They are valid for complex w and each of the two denominator signs.

Dropping the outer endpoints would be invalid: for w=1 on [0,pi] and the
linear phase -k, w'=0 while the exact integral is -2i. This explicit
countercase is preserved in the scalar output. The derivative-only bound
zero would fail, so w is never treated as H1_0.

## 5. Finite contours with the time exponential retained

Use the unitary circle Fourier conventions

    F_plus g(n)=(1/sqrt(2pi)) integral g(k)exp(+ikn)dk,
    F_minus g(n)=(1/sqrt(2pi)) integral g(k)exp(-ikn)dk.

Deform I to the rectangle with lower side Im k=-sigma. For k=x-iy,
x in I and 0<=y<=sigma, the exact cosine dispersion obeys

    Im E(x-iy)=-2J sin(x)sinh(y)<=-vy.                  (23)

For incoming n>=0 and outgoing n<0 the spatial modulus is at most
exp(-y|n|). Since 1-exp(-2y)>=y for 0<y<=sigma,

    ||(exp(-ym))_(m>=0)||_ell2<=y^-1/2.                (24)

Establish each contour identity for a finite set of integer n, apply
Minkowski, then increase the finite set. The right side is integrable at
zero, so monotone convergence justifies the Hilbert-space bound without
treating the y=0 plane-wave sequence as an ell2 vector.

Both vertical denominators have modulus at least v sigma/2. Each edge's
Hilbert norm is at most

    [kappa/(v sigma)] integral_0^sigma y^-1/2 exp(-vty)dy
      <=2kappa/[v sigma sqrt(vt)].                    (25)

Here the positive integral is bounded by Gamma(1/2)/sqrt(vt), and
Gamma(1/2)=sqrt(pi)<2. Thus both verticals cost at most
4kappa/[v sigma sqrt(vt)]. On the bottom, |D0sharp|>=v sigma and
|D0|>=v sigma/2. Its incoming and outgoing costs are respectively bounded by

    kappa/[v sqrt(sigma)] exp(-v sigma t),
    2kappa/[v sqrt(sigma)] exp(-v sigma t).            (26)

The advanced h_in pole lies above the real axis, so no pole is crossed.
The h_out pole kp=k0+c-i gamma lies inside the rectangle. Its clockwise
residue contribution to the outgoing n<0 sequence is

    -i sqrt(2pi) r0(k0)C0/v0 * exp[ikp n-iE(kp)t].     (27)

Using sum_(m>=1)exp(-2gamma m)=1/(exp(2gamma)-1)<=1/(2gamma)
and (13), its norm is at most

    kappa b0/[Nv0 sqrt(2gamma)] exp[Im E(kp)t]
      =N^-1 exp[Im E(kp)t]
      <=P(t):=2exp(-30kappa^2 t).                      (28)

Only the rational functions (14) and the entire scalar E are continued.
There is no contour claim about C_g,j, Kloc,j, y_j or an actual complex
matrix resonance.

Combining (18), (22), (25)-(28), and exp(-x)<=1/x for x>0 gives

    qin(t):=||1_(n>=0) F_minus(exp(-itE)f)||
       <=30sigma+[Dcut+4kappa/(v sigma)]/sqrt(vt)
                         +kappa/[v^2 sigma sqrt(sigma)t],
    qout(t):=||1_(n<0) F_plus(exp(-itE)f rho)||
       <=30sigma+[Dcut+4kappa/(v sigma)]/sqrt(vt)
                         +2kappa/[v^2 sigma sqrt(sigma)t]+P(t). (29)

All cutoff and finite-band effects are charged. For every t>=kappa^-2, let
s=3/20<sqrt(v), kappa_+=10^-8 and define fixed rational upper bounds

    Pbar=2(3/8)^30,
    Hbar=kappa_+^2/(v s)*(24/sigma+10),
    Bbar=kappa_+^3/[v^2 sigma sqrt(sigma)],
    qinbar=30sigma+Hbar+Bbar,
    qoutbar=30sigma+Hbar+2Bbar+Pbar.                    (30)

The exponential comparison uses e>8/3. At all these times vt>=v/kappa_+^2>1.
The bounds are valid over the continuous coupling interval by the positive
powers of kappa in (30), not by a grid. In particular
qinbar<0.000030640002 and qoutbar<0.000030640004<1/2.

The actual b_t in (11) has norm sqrt(1-delta_t^2), where delta_t is the left
side of qout in (29). It is nonzero and positive-real normalization costs

    ||b_t-beta_kappa,t||=1-sqrt(1-delta_t^2)<=delta_t.  (31)

This is the change of the restricted output. It is not the larger distance
between the full-line vector and its normalized restriction.

## 6. Uniform density estimate for the emitter reference

The reference emitter amplitude is exactly

    A_e(t)=integral_I p(k)exp[-itE(k)]dk,
    p=f yref/sqrt(2pi)=chi kappa^2 b^2/[2pi N |Df|^2]. (32)

It is useful to compare its density, not merely the individual spectral
amplitudes. Introduce

    p0=kappa^2 b0^2/[2pi N D0 D0sharp]
      =gamma/[pi N((q-c)^2+gamma^2)] on real k.         (33)

Its full real-line mass is 1/N, and the first formula is its analytic
definition on the contour. With rn=18sigma, (16)-(17) imply

    |(b^2/b0^2)(|D0|^2/|Df|^2)-1|
      <=(2rn+rn^2+2epsilon+epsilon^2)/(1-epsilon)^2
      <45sigma.                                      (34)

On |q|>=sigma/2, use |q-c|>=|q|/2. Since the numerator
kappa^2 b0^2/(2pi N) is at most kappa^2, the cutoff tail mass is at most
16kappa^2/(v^2 sigma). Therefore throughout the family

    integral_I |p-p0|
      <=45sigma*(100/99)+16kappa_+^2/(v^2 sigma)
       =3301/68750000 <50sigma.                       (35)

This explicit cutoff contribution is larger at the upper coupling, but
still fits. It is not dropped under an asymptotic small-kappa notation.

On either contour vertical |p0|<=4kappa^2/(v^2 sigma^2). Retaining (23)
and integrating exp(-vty) bounds the two verticals together by
8kappa^2/(v^3 sigma^2 t). On the bottom |p0|<=2kappa^2/(v^2 sigma^2);
its length is 2sigma and exp(-v sigma t)<=1/(v sigma t), so it costs at most
4kappa^2/(v^3 sigma^2 t). The p0 residue at kp is -1/(2pi i N).
The clockwise -2pi i orientation consequently produces **+N^-1 exp[-itE(kp)]**.
Thus

    |A_e(t)|<=50sigma+P(t)+12kappa^2/(v^3 sigma^2 t),
    |A_e(t)|<=Abar:=50sigma+Pbar
                         +12kappa_+^4/(v^3 sigma^2), t>=kappa^-2. (36)

At onset Abar<0.000050000001. This is a bounded rational-density
comparison, not an asserted exponential law for the installed amplitude.

## 7. Scalar incoming amplitude and the full localized clock split

The complete clock localization requires a sharper scalar estimate than
qinbar. Define

    S_f(t)=(1/sqrt(2pi)) integral_I f(k)exp[-itE(k)]dk,
    H0=integral_I |h_in(k)|dk, F0=integral_I |f(k)|dk.  (37)

Let Bstar=4*10^-8. Since |Sigma0|<2/v,

    |v0q-kappa^2 Re Sigma0|
       <=.03sigma+(2/v)kappa_+^2<Bstar.

With u=v0q-kappa^2 Re Sigma0 and Gamma>=19kappa^2, positive integration
over [-Bstar,Bstar] gives

    H0<kappa*(2/v)asinh(Bstar/Gamma)
       <=kappa*(2/v)log[1+2Bstar/(19kappa^2)]
       <3200kappa,
    F0<3200kappa/(1-epsilon)<4000kappa.                (38)

For F0 directly use |f|<=kappa/|Df| and (16). The logarithm is largest at
kappa_-=10^-12; its argument is exactly at most 80000000000000019/19,
strictly below (8/3)^40<exp(40). This proves the uniform bound without
quadrature near the linewidth.

The scalar, n=0 incoming h_in contour has no residue. Each vertical costs
at most kappa/(v^2 sigma t), and its bottom at most kappa/(v^2 sigma t).
Subtract w using the scalar part of (22), and pay the L1 profile difference
from (18), bounded by r_in H0/2. The result is

    |S_f(t)|<=1600kappa r_in
                   +kappa/(v^2 t)*(13/sigma+5),
    |S_f(t)|<=Sbar:=1600kappa_+ r_in
                   +kappa_+^3/v^2*(13/sigma+5)
                    <3.521*10^-10, t>=kappa^-2.        (39)

The coefficient 13/sigma+5 is 3/sigma from the scalar rational contour,
plus (20/sigma+10)/2 from the cutoff variation. Bounding S_f by qinbar
instead would be far too expensive after multiplication by 31.

Now split only on the real interval, in the full physical Hilbert norm:

    C_g,j(k)=C_g,j(k0)+Delta C_g,j(k),
       ||Delta C_g,j(k)||<=2700|k-k0|,
    Kloc,j(k)=Kloc,j(k0)+Delta Kloc,j(k),
       ||Delta Kloc,j(k)||<=10^6 |k-k0|.              (40)

Apply (10), (32), (38)-(40) to the exact clock integral. Its per-column
bound is

    Clock_col(t)<=31|S_f(t)|+2700sigma*(2000kappa)
             +kappa*20000 |A_e(t)|
             +kappa*10^6 sigma Aref
             +kappa*20000(4sigma+epsilon_off)
      <=31|S_f(t)|+2700sigma*(2000kappa)
             +kappa*20000[|A_e(t)|+4sigma+epsilon_off]
             +kappa*10^6 sigma.                       (41)

The first line includes the constant background, its variation, the constant
localized response to yref u_j, the variation of that response, and the full
delta y_j term. In particular the constant Kloc,j(k0)u_j is multiplied by
the common A_e(t), while its varying part costs the positive integral Aref<=1.
No off-diagonal emitter coordinate is hidden by this split. Kloc's full-tail
derivative is essential: a derivative bound for only its contact block would
not justify (40)-(41).

Both old-energy columns within a parity may align in the clock. Thus the
complete clock operator bound is (3/2)Clock_col, not its largest column alone.
The emitter reference A_e u_j has orthonormal columns, whereas the errors
from (9) again cost the parity factor. Therefore a valid total localized bound is

    Loc(t)<=|A_e(t)|+(3/2)(4sigma+epsilon_off)
                                +(3/2)Clock_col(t).    (42)

At all t>=kappa^-2, use (36),(39), kappa<=kappa_+, and positive coefficients
in (41). The resulting uniform clock operator ceiling is below 1.286*10^-7,
and the complete localized ceiling is below 0.000056128570. It includes the
emitter, both source qubits, every clock coordinate and both old energies.

## 8. Complete-output estimate and all-future quantifier

Propagate the seed discrepancy in (8) by unitarity. Compare the resulting
exact packet with (11). Incoming and outgoing vacuum columns are orthogonal
in their internal old basis, so their errors use qin and the maximum reflection
error, respectively. The restricted normalization costs (31). Localized
columns use (42), with the parity factors already paid. Hence

    ||exp(-itHphysical_kappa)Eseed-Uideal,kappa(t)||
      <.003+.000714+qin(t)+qout(t)+Loc(t).             (43)

The exact intertwining in (8) puts the same old-aging unitary on every error
column. It does not commute K through Htilde. The scalar exp[-i(nu+2kappa)t]
remains in the comparator. Tensoring an arbitrary passive reference preserves
the operator bound. No source, emitter or clock output is traced out.

Let Q denote the rational upper expression obtained from (30), (36),
(39)-(42), with kappa replaced only in increasing positive majorants by
kappa_+. The sole exact scalar run gives

    Q = 138611025462876289642614901207402041129347129 /
        1180586898350928433778786304000000000000000000000
      <118*10^-6.

Thus the complete upper expression is

    .003+.000714+Q
      =4523310765938224492697027234263402041129347129 /
       1180586898350928433778786304000000000000000000000
      <.003832, for every kappa in [10^-12,10^-8]
                    and every t>=T_kappa=1/kappa^2.   (44)

All time-dependent terms used in (29), (36), (39) decrease for later t;
their remaining floors are uniform and explicitly included. The comparison
therefore has the all-future quantifier on the infinite apparatus. It does
not assert exact exponential decay, nor an arbitrary-accuracy limit from
these fixed floors. The complete unhalved trace distance is below 0.007664.

## 9. Finite horizon, exact distance and positive resource loads

Reuse the qualified family prepared-sector spectral radius 19. In particular
I<=B<=20I, the gate/source perturbation bound is Vmax=7.925057370220605,
and the uncoupled clock/gate and emitter radii about
cstar=2J+(1+20)/2 are below 18. The off-diagonal block has norm
sqrt(2)kappa<2*10^-8, so radius 19 is uniform. The physical scalar only shifts
the center; this is not a many-head extensive-norm estimate.

Keep clock sites 0,...,M-1 and emitter e, including the actual far-end
positive diagonal J n_(M-1). In the unchanged square-contact geometry the
first omitted site c_M is at distance

    d_M=M-L-1=M-13                                    (45)

from the seed, through c_(L+2). The other contact route is two edges longer,
and onsite internal mixing does not shorten the path. Polynomial evolutions
agree on the whole seed subspace through degree d_M-1. The inherited
Chebyshev bound is

    ||embedded finite evolution-infinite evolution||
       <=4 exp[-d_M+19t sinh(1)]/[1-exp(-1)].          (46)

Choose T=T_kappa, Tobs=2T and M=ceil(50T). No integer assumption on T is
needed: M>=50T. With sinh(1)<6/5,

    d_M-19Tobs*(6/5)-9 >=(22/5)T-22
       >=43999999999999978>0,
    finite correction <(32/5)(3/8)^9
       =19683/20971520<.001.                          (47)

The minimum T is 10^16 at the largest coupling. Combining (44),(47) yields
complete isometry error below 0.004832 and unhalved trace distance below
0.009664 throughout [T_kappa,2T_kappa]. The comparator is the same normalized
infinite-half-line beta_kappa,t embedded in the common comparison space;
it is not truncated and normalized again. No fixed finite clock is claimed
to work forever. The stronger exact sum is retained in the scalar output,
but no narrower scope or changed comparator is used to obtain the stated bound.

The new full-qubit positive terms remain exactly

    Q_ej=kappa(n_e+n_j)+t_j a_j^dagger a_e
                                +conj(t_j)a_e^dagger a_j,
    t_L=kappa, t_(L+2)=-kappa exp(i phi),
    (E0-2kappa)n_e, kappa(I-n_L), kappa(I-n_(L+2)).     (48)

Each Q_ej has eigenvalues 0,0,2kappa,2kappa. Since E0>2*10^-8, all terms
are positive throughout the family. Their sum is E0 n_e plus the two
hoppings plus exactly 2kappa I. The existing positive vacancy term supplies
nu. Head number is conserved. The seed mean and variance are

    Eseed*Hphysical Eseed=K+(E0+nu+2kappa)I,
    variance=Var(K)+2kappa^2.                          (49)

The inherited incident sums, with maximum new loads at kappa_+, are:

| Site | Added incident positive-block norm sum |
|---|---:|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| source A | 20.332662089993454 |
| source B | 17.078839343776311 |
| c0 | 8.015120691541701 |
| c1 | 6.730044773026091 |
| ordinary clock site | 0.120084428428128 |
| either emitter attachment, including clock bonds | 0.120084458428128 |
| emitter e | E0+0.00000002, approximately 0.005626357514718896 |

The existing old edge has norm 3 and is additional. Only the added old-site
cap two holds; source and boundary-clock loads are not under two. Each
emitter bond norm is 2kappa, the added attachment load is 3kappa and the
emitter load is E0+2kappa. The actual scalar at kappa_+ is
1.459892833020969, not the lower-endpoint scalar 1.459892813022969.

There are M+5 qubits. None of the computations allocates a clock of this
size. Exact coefficients, the supplied loop phase, clean clock/source
vacuum, the excited emitter and the static positive Hamiltonian are still
resources. This estimate grants no native supply, sink, reset/reuse,
practical hardware or physical Hamiltonian/Record identification.

## 10. Failed routes and discrimination from prior work

Simple substitution of kappa_+ into the earlier fixed-coupling proof does
not establish this theorem. Its single cutoff L2 ceiling becomes
4kappa_+/(v sqrt(sigma))=0.0016; its complete absolute localized-clock
ceiling becomes 153000kappa_+=0.00153. Those sufficient allowances already
overrun the desired complete budget. This is a failure of those estimates,
not a lower bound on actual leakage or a physical no-go result.

Splitting C_g,j but bounding its scalar coefficient by the half-line error
30sigma also costs (3/2)*31*30sigma=0.001395, too much. The L1 comparison
and scalar n=0 contour in (37)-(39) are necessary to this budget. The
constant Kloc response similarly uses the actual scalar density amplitude,
not an absolute integral of yref. Both derivative-controlled differences
are charged on the real band rather than analytically continued.

The endpoint countercase in section 4 and reciprocal phase countercase in
section 3 remain explicit. The tempting affine-time replacement has error
ceiling tJ sigma^2, which is already larger than one at the upper-endpoint
T and grows without bound. It cannot prove this all-future claim. The
actual E is retained on every scalar contour. No parameter grid, narrow
resonance quadrature or unproved matrix-pole location replaces a uniform
inequality.

Rational resonance profiles, Fourier/scattering isometries, contour
integration, bounded-variation integration by parts and Chebyshev locality
are prior mathematics. This packet claims no worldwide novelty or new
generic half-line theorem. The earlier fixed result supplied the opposite-
pole strategy, and the published family supplied its mass/overlap/inverse
premises and earlier sufficient onset. The proposed new step is their
explicit, uniformly paid composition (18)-(44), especially the directional
cutoff and real-band full-localization estimates. Parent's unproved
suggestions of retaining the edge exponential and splitting C_g/Kloc at k0
were supplied before this author work and are recorded as proposal exposure.

The earlier source packet records contextual primary-literature triage of
Dereziński--De Roeck, Extended Weak Coupling Limit for Friedrichs Hamiltonians,
arXiv:math-ph/0604058. No theorem from that paper is imported here, and no
fresh literature search or numerical exponential-law inference is made.
The old scattering/permanence strategy is credited through its pinned sources.

## 11. Actual bounded evidence and remaining review obligation

`RESOURCE_PLAN.json` was saved before any new scientific computation. The
plan allowed exactly one run without a written amendment: CPU soft/hard
limits 20/21 seconds, external wall 30 seconds, matrix dimension zero,
integer powers at most 80, and no optimizer/grid/quadrature/dynamics.
Only one scientific attempt occurred, with no failure or retry. Maximum
power requested was 40. The exact scalar program imports no old checker.
Its checks corroborate the real-center identities, increasing majorants,
cutoff/density/clock/finite budgets and explicit countercases. They do not
independently validate the analytical proof.

`launch_check.py` serialized, flushed, fsynced and closed PRELAUNCH.json
before creating the subprocess. It binds 28 packet files, including the
executed copy and all 21 source snapshots, and five runtime identities:
the resolved Python executable and the fractions, decimal, numbers and
_decimal module files. The prelaunch fsync completed at
2026-10-17T03:49:49.004456Z; the recorded post-fsync, pre-Popen launch boundary
was 03:49:49.004585Z, and the scientific program began at 03:49:49.053382Z.
All byte/size/device/inode/mtime bindings were checked in
the child and remained unchanged afterward. All original source contents
still matched their snapshots. This is partial runtime pinning, not a hash
of every transitive standard-library or operating-system dependency.

The run exited zero at 03:49:49.090289Z. Actual wrapper wall time was
0.08568883407860994 seconds; child user/system CPU were 0.025705 and
0.009440999999999998 seconds. macOS peak child RSS was 22,298,624 bytes.
The program-internal measured interval was 0.0031044576317071915 seconds
and excludes startup/import time. Python was 3.13.5. RSS was measured, not
capped; thread environment requests of one were not a measurement of thread
counts. Both full stderr streams are empty. The full 12,367-byte scientific
stdout and wrapper streams were read and preserved. Explanatory decimal
displays are not outward enclosures; exact rational fields carry the tests.

| Evidence | SHA256 |
|---|---|
| `check_bounds.py`, identical to `run01/executed_source.py` | b5383a88626e3bd378ba9155ee88577b49f8cf28e9b6031a2be5aada9fa48ef6 |
| `launch_check.py` | 5c96cf7d03d19a9d265254d2661a5df9a3e5b59b567aa9245345aebd2ab8c15a |
| `RESOURCE_PLAN.json` | 80d14f540d1884d0a58f9ae35c02a3eca43a24ba2abac9eee0b36a3b11b30e81 |
| `SCALAR_INPUTS.json` | 3e7a938c2a04e1da45189e728ac65c1e65309f97d4331dab0ef08bcbfb5a0c65 |
| `SOURCE_MANIFEST.json` | fef1d432e80bc0604def3a46d3dbff655020eab9587a73e2f357ed0b7f462c40 |
| `run01/PRELAUNCH.json` | 64f8369ae07325c3e38f2482e6e399e43a45ab4e50d63be400ab965225b06afb |
| `run01/RECEIPT.json` | 0ead3f309bd1b6952228cd74d389c02c12225736f90ea79f1b23b02b6f69db79 |
| `run01/stdout.json` | f94907937c47f29197681d05d8275efaaacb1ee7df54fcc92ef61d8c5533ce0c |
| Empty `run01/stderr.txt` | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The complete family argument, fixed-resonance argument and separate fixed
review, and their exact root qualifications were read. Previously read
unchanged installed, weighted, generic, local-emitter, interval and moment
arguments are reused by the listed identities, with their relevant
full-column, phase and finite-clock interfaces refreshed. No historical
scientific certificate was rerun. This author wrote the fixed-resonance
and moment candidates and performed prior source-exposed checks and family
publication transport work. The same model/effort and substantial prior
exposure remain. This is neither a blind review nor a second independent
proof. There was no delegation.

The sole read-only inventory mistake was an earlier guessed directory
`resonant_escape_independent_review`, which did not exist; the actual
`resonant_escape_review/REPORT.md` was located and read in full. This did
not launch a scientific computation. `FAILURES.md` preserves that lookup
and the failed mathematical shortcuts. No failed stream was discarded.

The next decisive check should reconstruct the BV endpoint constants and
finite-rectangle Hilbert estimates, the scalar incoming bound, the uniform
density floor and all clock/emitter column factors by a distinct path.
It should confirm the actual-profile normalization, full seed/point-spectrum
accounting, phase/old-aging contract and ceil-based finite distance. Replaying
this author's scalar script alone would not provide that check. This frozen
packet stops before independent or root qualification, canonical execution,
publication or retained audit.

Joint ladder or calibration boxes, a wider bandwidth, a different seed,
native resource supply, a common nominal waveform, minimum/optimal onset,
practical resources, physical seconds, reset/reuse and fixed finite-device
permanence are excluded. All writes were confined to this packet. No W,
Git, PR, source theorem, shared checkpoint, physical axiom, audit output or
editable prompt file changed.

<!-- END PRESERVED SOURCE resonant_family_candidate/CANDIDATE.md -->


## Preserved source: Exact-product preparation

<!-- BEGIN PRESERVED SOURCE emitter_preparation_independent/CANDIDATE.md -->
# Finite thermal preparation and release into the literal emitter

**Status:** new conditional author candidate, with bounded author algebraic
corroboration; separate review remains required. This is an independent route
relative to root's withheld preparation mechanism, not an independent review of
the inherited emitter theory. The same model and substantial prior author and
reviewer exposure to that theory are disclosed below.

The construction keeps every installed runtime block, the literal old
\(K=2I+Z_1Z_2\), and the finite runtime clock unchanged. Additional positive
onsite and ordinary nearest-neighbor two-qubit blocks make the full
preparation Hamiltonian an exactly decoupled defect Hamiltonian. A finite
\(C^1\) release removes those added blocks. Its error from an exact seed is
at most \(\kappa\tau/\sqrt2\), independent of clock length. The thermal
preparation error is length dependent and is counted separately.

For the exact PR9665 coupling family, a supplied inverse temperature
\(\beta=10\), defect gap \(G=13\), hold time one and release time one suffice
to retain a complete unhalved trace error below 0.01 throughout the inherited
finite observation window, even for an arbitrary correlated old/reference
extension of the specified auxiliary Gibbs marginal. This statement pays
additional control loads: during preparation the added old-site loads are
3.987514255266680 and 2.397277262241192, exceeding the runtime cap two.
It is conditional supply and control, not native cooling or autonomous
preparation.

## 1. Sources, scope and inherited theorem

The exact repository source is commit
0e3993770a7a2dd872018f9dd3c76c2d9a624db9. The complete source map and byte
copies are [SOURCE_MAP.json](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/SOURCE_MAP.json) and [inputs](../outputs/thermal_resonance_halt_2026_10_17_inputs/SOURCE_MAP.json).
The family note has SHA256
f3a10874f4f52bef0bc5c393081590aff2f71b877a0f44cac9a3cbe05b34da87;
its unchanged author body has SHA256
9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac.
The source note records prior separate checking and root qualification.
Those are inherited conditional dependencies, not new checks made here.
No merged, retained, independently audited or physical-realization status is
claimed.

The reused finite-runtime implication is the following exact statement of
[the family note](../.claude/science/physics-loops/toe-emitter-coupling-family-20261017/evidence/canonical/executed_sources/docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md.txt), sections 8–9. For

\[
10^{-12}\le\kappa\le10^{-8},\quad \sigma=10^{-6},\quad L=12,\quad
T=10^6/\kappa^2,\quad M=\lceil50T\rceil,
\tag{1}
\]

the finite compression \(H_M\) defined in section 2 below, started from its
exact seed isometry \(\mathcal E\), satisfies, after isometric embedding into
the infinite comparison output space,

\[
\left\|e^{-itH_M}\mathcal E-
\zeta e^{-ic_{\rm phys}t}\mathcal B_{\kappa,t}
e^{-itK}W\right\|<F,\qquad T\le t\le2T,
\tag{2}
\]
\[
F=\frac{3735315138388379}{781250000000000000},
\quad c_{\rm phys}=\nu+2\kappa,\quad
W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25}.
\tag{3}
\]

Here \(\mathcal B_{\kappa,t}x\) places the emitter in its empty state,
the source pair in its vacuum, the clock in the actual normalized outgoing
profile \(\beta_{\kappa,t}\), and the old pair in \(x\). It retains every
modeled output. The operator norm covers all four old input columns at their
own total energies, and arbitrary passive references. The proof includes
closed tails, coherent returns, seed point-spectrum contributions, common
normalization and finite-clock error. We do not redo or strengthen those
scattering premises. In particular, the original target residual allowance
\(1.76\times10^{-13}>0\) remains. This is fixed accuracy, not an
arbitrary-accuracy result.

The actual common profile and phase are unchanged. To make the convention
explicit, \(q_0=4.510351185997098\), \(k_0=2\arctan(1/q_0)\),
\(E(k)=2J(1-\cos k)\), \(E_0=E(k_0)\), \(\phi=2k_0\) and
\(I=[k_0-\sigma,k_0+\sigma]\). With the inherited scalar full-line
self-energy
\[
\Sigma_f(k)=-\frac{i}{2J\sin k}\bigl(2-2\cos\phi\,e^{2ik}\bigr),
\quad D_f=E(k)-E_0-\kappa^2\Sigma_f(k),
\]
\[
g_-(k)=e^{ikL}(1-e^{i\phi+2ik}),\quad
y_{\rm ref}=\kappa\overline{g_-}/D_f,\quad
N_\kappa^2=\frac1{2\pi}\int_I\chi^2|y_{\rm ref}|^2\,dk,
\]
\[
f_\kappa=\frac{\chi\overline{y_{\rm ref}}}{\sqrt{2\pi}N_\kappa},
\quad t_-(k)=1-\frac{i\kappa^2|g_-|^2}{E'(k)D_f},
\quad \rho_\kappa(k)=-e^{2ik}\frac{t_-(k)}{|t_-(k)|}.
\tag{4}
\]
The cutoff \(\chi\) is one on the central half-band and linear to zero at
the endpoints. The inherited proof gives \(N_\kappa>0.99\),
\(\|f_\kappa\|_2=1\), and \(|t_-|>1/2\). Define
\[
b_{\kappa,t}(n)=\frac1{\sqrt{2\pi}}\int_I
 f_\kappa(k)\rho_\kappa(k)e^{ikn-iE(k)t}\,dk,\quad n\ge0,
\qquad \beta_{\kappa,t}=b_{\kappa,t}/\|b_{\kappa,t}\|.
\tag{5}
\]
The normalization divisor is positive real. The exact scalar is
\(\zeta=-e^{-4ik_0}\alpha\), where \(\alpha\) is the inherited exact
site-1 reflection in the fixed \((s,p)=(-1,-1)\) column at \(k_0\).
That definition fixes a particular number; it is not a new fitted phase.
The conversion is \(r_{\rm absolute}=e^{-2ik}r_{\rm site1}\).
Both \(f_\kappa\) and \(\rho_\kappa\) depend on the actual apparatus
\(\kappa\) but are common to all old columns. Preparation changes neither.

## 2. Literal full-qubit runtime apparatus

Write \(n=(I-Z)/2\), \(a=|0\rangle\langle1|\), and
\(L_{xy}=a_x^\dagger a_y+a_y^\dagger a_x\). The finite clock has sites
\(c_0,\ldots,c_{M-1}\); denote its number operators by \(n_j\).
The source pair is \(A,B\), the emitter is \(e\), and the old pair is \(1,2\).
Every terminating decimal in the following table is exact.

| Parameter | Value | Parameter | Value |
|---|---:|---|---:|
| \(J\) | 0.030021107107032 | \(g_A\) | 0.996878563816670 |
| \(g_B\) | 0.599319315560298 | \(h\) | 3.999349697888060 |
| \(\lambda_A\) | 3.801781381581202 | \(\lambda_B\) | 2.575033765788497 |
| \(u\) | 0.544607276405587 | \(\Delta_A\) | 2.192035527016003 |
| \(\Delta_B\) | 2.186826508897014 | \(\mu_0\) | 0.321494607058201 |
| \(\nu=-\mu_1\) | 1.459892813020969 | \(q_0\) | 4.510351185997098 |

In particular
\[
E_0=\frac{30021107107032000000000000000}
{5335816955256357129429116105401}>2\kappa.
\tag{6}
\]
The inherited gate part on the full qubit space is
\[
\begin{aligned}
C&=\Delta_A n_A+\Delta_B n_B+h(n_A+n_B-L_{AB})+u n_A n_B,\\
G_{\rm old}&=g_A n_A(I+X_1)+g_B n_B(I+X_2),\\
H_c&=Jn_0+J\sum_{j=0}^{M-2}(n_j+n_{j+1}-L_{c_jc_{j+1}})
       +Jn_{M-1},\\
H_{\rm gate}&=K+C+G_{\rm old}+H_c
 +\lambda_A n_0(I+X_A)+\lambda_B n_1(I+X_B)
 +\mu_0n_0+\nu(I-n_1).
\end{aligned}
\tag{7}
\]
The far-end \(Jn_{M-1}\) is part of the actual compression, not omitted.
For \(j=L,L+2\), put \(t_L=\kappa\), \(t_{L+2}=-\kappa e^{i\phi}\), and
\[
Q_{ej}=\kappa(n_e+n_j)+t_j a_j^\dagger a_e+
                     \overline{t_j}a_e^\dagger a_j.
\]
Then the literal installed runtime Hamiltonian is
\[
H_M=H_{\rm gate}+Q_{eL}+Q_{e,L+2}
 +(E_0-2\kappa)n_e+\kappa(I-n_L)+\kappa(I-n_{L+2}).
\tag{8}
\]
All displayed summands are positive on their full local qubit spaces. No
restriction to one excitation is used to justify that assertion.
The one-head restriction of (8) is the parent's signed matching operator
plus exactly \(c_{\rm phys}I=(\nu+2\kappa)I\).

For geometry, old1 is \((0,0,0)\), old2 \((1,0,0)\), \(A=(0,1,0)\),
\(B=(1,1,0)\). Clock sites initially lie at \(c_n=(n,2,0)\).
At the emitter square use
\[
c_L=(L,2,0),\quad c_{L+1}=(L+1,2,0),\quad
c_{L+2}=(L+1,3,0),\quad c_{L+3}=(L+2,3,0),\quad e=(L,3,0),
\]
and continue the clock by \(c_n=(n-1,3,0)\) for \(n\ge L+3\).
Every interaction in (7)–(8) is onsite or an ordinary nearest-neighbor
two-qubit block. Take \(M\ge16\), as (1) certainly does.

Define the full seed isometry
\[
\mathcal E x=|1\rangle_e\,|0\cdots0\rangle_c\,|00\rangle_{AB}\,x.
\]
Let \(\mathcal Vx\) have the emitter empty, source vacuum and clock vector
\(|L\rangle-e^{i\phi}|L+2\rangle\), with old state \(x\). Directly from
(7)–(8),
\[
H_M\mathcal E=\mathcal E(K+c_{\rm seed})+\kappa\mathcal V,\quad
c_{\rm seed}=\nu+2\kappa+E_0,\quad
\mathcal V^*\mathcal V=2I,\quad \mathcal E^*\mathcal V=0.
\tag{9}
\]
The source terms are dark on its vacuum and the contact terms vanish when
the clock is empty. The two distinct clock destinations in \(\mathcal V\)
are orthogonal. Thus (9) is an operator statement for every old input,
not a columnwise bound with a dimension factor.

## 3. Positive preparation controls on the same geometry

Keep all of \(H_M\) installed. Add the following independently counted
positive control blocks, whose sum is \(R_0\):

| Support | Added block | Norm | Count |
|---|---|---:|---:|
| Each clock edge | \(J(n_j+n_{j+1}+L_{c_jc_{j+1}})\) | \(2J\) | \(M-1\) |
| \(A,B\) | \(h(n_A+n_B+L_{AB})\) | \(2h\) | 1 |
| \(A,B\) | \(u(I-n_An_B)\) | \(u\) | 1 |
| \(A,1\) and \(B,2\) | \(g_i n_i(I-X_{\rm old,i})\) | \(2g_i\) | 2 |
| \(c_0,A\) and \(c_1,B\) | \(\lambda_i n_{c_i}(I-X_i)\) | \(2\lambda_i\) | 2 |
| \(e,c_L\) and \(e,c_{L+2}\) | \(\overline Q_{ej}=\kappa(n_e+n_j)-t_j a_j^\dagger a_e-\overline{t_j}a_e^\dagger a_j\) | \(2\kappa\) | 2 |

In the contact row the correspondence is \(i=A\mapsto c_0\),
\(i=B\mapsto c_1\). The symbols in that row name those two blocks, not a
third-body conditional operation.

For \(c\ge0\), \(c(n_x+n_y\pm L_{xy})\) has full pair spectrum
\(\{0,0,2c,2c\}\). A phase on the exchange preserves this spectrum, giving
the claimed spectra for \(Q_{ej}\) and \(\overline Q_{ej}\). In particular
their \(|11\rangle\) energy is \(2\kappa\); it is not dropped.
The conditional flip complements have spectrum \(\{0,0,0,2g_i\}\) or
\(\{0,0,0,2\lambda_i\}\), and \(u(I-n_An_B)\) has spectrum
\(\{u,u,u,0\}\). All these controls are positive full-space blocks.

Adding each complement to its installed partner gives, identically on the
entire \(2^{M+5}\)-dimensional qubit space,
\[
H_M+R_0=K+(\nu+2\kappa+u)I+\sum_v d_v n_v,
\tag{10}
\]
where \(v\) runs through the sources, clock and emitter, and
\[
\begin{aligned}
d_A&=\Delta_A+2h+2g_A,&d_B&=\Delta_B+2h+2g_B,&d_e&=E_0+2\kappa,\\
d_j&=4J-J{\bf1}_{j=0\ {\rm or}\ M-1}
 +(2\lambda_A+\mu_0){\bf1}_{j=0}
 +(2\lambda_B-\nu){\bf1}_{j=1}
 +\kappa{\bf1}_{j=L\ {\rm or}\ L+2}.
\end{aligned}
\tag{11}
\]
This is termwise cancellation, not a cancellation conditional on three
sites. The density complement contributes the explicit \(uI\); the two
emitter vacancy blocks and the boundary vacancy block retain their scalar
shifts. The clock endpoints have coefficient \(3J\) before their contact
corrections.

Choose \(G=13\) and add onsite pins
\[
R_{\rm pin}=\sum_{v\in\{A,B,c_0,\ldots,c_{M-1}\}}(G-d_v)n_v
 +(G+d_e)(I-n_e).
\tag{12}
\]
Every coefficient is positive throughout (1). Indeed the largest \(d_v\)
is \(d_A=12.184492050425463<13\); the listed clock values, \(d_B\) and
\(d_e\) are smaller. The emitter pin is a positive vacancy projector,
selecting the excited emitter rather than a zero-energy vacuum.

With \(R=R_0+R_{\rm pin}\), the actual preparation Hamiltonian is exactly
\[
H_{\rm prep}=H_M+R=K+\chi_{\rm p}I+GQ,\qquad
Q=\sum_{j=0}^{M-1}n_j+n_A+n_B+(I-n_e),
\tag{13}
\]
\[
\chi_{\rm p}=\nu+E_0+u+4\kappa,\qquad
R\mathcal E=(u+2\kappa)\mathcal E-\kappa\mathcal V.
\tag{14}
\]
The old Hamiltonian is literally \(K\), unaltered by (13). All ancillary
interactions cancel for every auxiliary state, not only on the seed.
This is a supplied positive-block counterterm construction; it does not
derive the ability to supply the opposite phases or independently vary the
strengths from the lattice axioms.

## 4. Finite-temperature marginal, retained correlations and a finite hold

At the declared start of the protocol the additional controls are fully on.
Supply the actual auxiliary marginal
\[
\tau_\beta=\frac{e^{-\beta GQ}}{\operatorname{Tr}e^{-\beta GQ}},
\qquad \beta>0.
\tag{15}
\]
This is the Gibbs density for the auxiliary part of the *actual* decoupled
Hamiltonian (13), not for a fictitious source with the runtime interactions
ignored. It is not required that the old input be Gibbs. No process preparing
(15) from an arbitrary state or equilibration time is asserted.

Let \(N=M+3\) be the auxiliary qubit count. Each defect has probability
\(q=(1+e^{\beta G})^{-1}\). The auxiliary seed projector
\(P=|\mathrm{seed}_{\rm aux}\rangle\langle\mathrm{seed}_{\rm aux}|\)
has probability
\[
p_{\rm good}=(1+e^{-\beta G})^{-N},\qquad
\epsilon=1-p_{\rm good}\le N e^{-\beta G}.
\tag{16}
\]
This exact product-Gibbs law includes emitter defects, source excitations
and all many-head clock sectors. There is no projection or postselection.

There are two distinct input hypotheses.

* For the joint product input \(\tau_\beta\otimes\rho_{OR}\), where \(O\)
  is the old pair and \(R\) any passive reference, the complete unhalved
  trace distance from \(\mathcal E\rho_{OR}\mathcal E^*\) is exactly
  \(2\epsilon\). Both positive and negative blocks have trace \(\epsilon\).
* For any joint \(\rho_{A_{\rm aux},OR}\) with marginal (15), define the
  comparator using the exact **unconditioned** \(\rho_{OR}\). Then
\[
\|\rho-\mathcal E\rho_{OR}\mathcal E^*\|_1
\le g(\epsilon):=\epsilon+\sqrt{\epsilon(4-3\epsilon)}
\le3\sqrt\epsilon.
\tag{17}
\]

For completeness, purify \(\rho\) and split its vector into projected good
and bad components of squared norms \(1-\epsilon\) and \(\epsilon\).
The difference from its unnormalized good block has two-dimensional trace
norm \(\sqrt{\epsilon(4-3\epsilon)}\). Partial trace can only reduce that
norm. If \(\tau_{OR}=\langle\mathrm{seed}_{\rm aux}|\rho|
\mathrm{seed}_{\rm aux}\rangle\), then
\(\rho_{OR}-\tau_{OR}\ge0\) has trace \(\epsilon\). A triangle inequality
gives (17), without conditioning or replacing the retained old/reference
marginal. The same bound and sharpness were already established in the
local-Gibbs source note; this is not a new generic thermal lemma.

The distinction is essential even for the exact product Gibbs *marginal*:
its Schmidt purification \(\sum_b\sqrt{p_b}|b\rangle_{\rm aux}|b\rangle_R\)
has that marginal but attains \(g(\epsilon)\). The good/bad coherent block
has the square-root norm above and the other seed-reference diagonals
contribute \(\epsilon\). Thus the product-input \(2\epsilon\) bound cannot
be inferred from a marginal promise alone.

Hold \(H_{\rm prep}\) for any finite \(t_{\rm h}\ge0\), distinct from the
source hopping coefficient \(h\). Since it separates as
(13), its auxiliary Gibbs marginal is stationary, including for correlated
extensions. On the ideal seed,
\[
e^{-it_{\rm h}H_{\rm prep}}\mathcal E
=e^{-i\chi_{\rm p}t_{\rm h}}\mathcal E e^{-it_{\rm h}K}.
\tag{18}
\]
All actual outputs and correlations are propagated by the same full
unitary. There is no assumption that the interacting runtime commutes with
\(K\). A purification or retained preparation environment may be included
in the passive reference, provided it no longer interacts after delivery.

## 5. Finite \(C^1\) release with a length-independent seed bound

After the hold, release for a finite duration \(\tau>0\), using
\[
H(r)=H_M+s(r)R,\quad
s(r)=1-3(r/\tau)^2+2(r/\tau)^3,\quad 0\le r\le\tau.
\tag{19}
\]
Before release \(s=1\), and after release \(s=0\) exactly. This is a
\(C^1\) join to both constant Hamiltonians:
\[
0\le s\le1,\quad \int_0^\tau s\,dr=\tau/2,\quad
\max|s'|=3/(2\tau),\quad s'(0)=s'(\tau)=0.
\tag{20}
\]
Each extra block remains positive and is removed with finite slew.
The installed runtime blocks have constant strengths throughout.

Combining (9) and (14) gives the exact restricted action
\[
H(r)\mathcal E
=\mathcal E\{K+c_{\rm seed}+s(r)(u+2\kappa)\}
 +(1-s(r))\kappa\mathcal V.
\tag{21}
\]
Define the seed-supported comparison propagator
\[
V_{\rm s}(r)=\exp\!\left[-irK-i c_{\rm seed}r
-i(u+2\kappa)\int_0^r s(v)\,dv\right].
\]
It is a comparator, not an assertion that the actual state stays in the
seed range. If \(U(r_2,r_1)\) is the exact chronological propagator for
(19), differentiating \(U(\tau,r)\mathcal E V_{\rm s}(r)\) gives
\[
U(\tau,0)\mathcal E-\mathcal E V_{\rm s}(\tau)
=-i\int_0^\tau U(\tau,r)
 [H(r)\mathcal E-\mathcal E(K+c_{\rm seed}+s(r)(u+2\kappa))]
 V_{\rm s}(r)\,dr.
\]
Use full-unitary norm one, \(\|\mathcal V\|=\sqrt2\) and (20):
\[
\boxed{\,
\|U(\tau,0)\mathcal E-
e^{-i[c_{\rm seed}\tau+(u+2\kappa)\tau/2]}
\mathcal E e^{-i\tau K}\|
\le \kappa\tau/\sqrt2.\ }
\tag{22}
\]
This operator bound tensors with any passive reference unchanged.
It is independent of \(M\), \(G\), the extensive norm of \(R\), and any
adiabatic gap. It uses the exact seed property; it is not a global
\(\|H(r)-H_M\|\) estimate, nor a commutation assumption. The scalar
\((u+2\kappa)\tau/2\) has been paid explicitly. A comparison that discards
it or bounds the entire \(R\) would miss this mechanism.

Equation (22) holds for every finite \(M\ge16\) with the same local
coefficient prescription. It does **not** make the thermal term in (16)
length independent. At fixed \(\beta G\), \(p_{\rm good}\to0\) as
\(M\to\infty\); increasing the length without a temperature/gap budget
does not preserve this complete handoff.

## 6. Chronological composition and every output

Let \(U_{\rm total}(t_{\rm h},\tau,t)=e^{-itH_M}U(\tau,0)e^{-it_{\rm h}H_{\rm prep}}\).
From (2), (18), (22) and unitarity, the complete seed isometry differs by
less than \(F+\kappa\tau/\sqrt2\) from
\[
\mathcal I(t_{\rm h},\tau,t)
=\zeta e^{-i\Phi(t_{\rm h},\tau,t)}
\mathcal B_{\kappa,t}e^{-i(t_{\rm h}+\tau+t)K}W,
\tag{23}
\]
\[
\Phi(t_{\rm h},\tau,t)=
\chi_{\rm p}t_{\rm h}+c_{\rm seed}\tau+(u+2\kappa)\tau/2
 +c_{\rm phys}t.
\tag{24}
\]
The only reordering used is the exact \([W,K]=0\), directly checked from
the displayed \(W,K\). In particular neither \(H_M\) nor \(H(r)\) is
assumed to commute with \(K\). The old system ages through the hold, the
release and the entire runtime. The output clock profile is indexed by
the runtime \(t\), not by the total elapsed time. The runtime scalar is
\(c_{\rm phys}t\), not \(c_{\rm seed}t\); \(E_0\) already belongs to the
runtime spectral profile in (4)–(5).

Apply (17) first to the actual initial full density matrix, then propagate
it with the exact full-space unitary. Comparing two isometries on a
normalized mixed input costs at most twice their operator-norm difference.
For arbitrary correlated input with the stated Gibbs marginal this gives
\[
\left\|U_{\rm total}\rho U_{\rm total}^*-
 \mathcal I(t_{\rm h},\tau,t)\rho_{OR}\mathcal I(t_{\rm h},\tau,t)^*\right\|_1
<g(\epsilon)+2F+\sqrt2\kappa\tau,\qquad T\le t\le2T.
\tag{25}
\]
All maps here include the identity on the passive reference. For the
product Gibbs input replace \(g(\epsilon)\) by \(2\epsilon\).
The old/reference input is unconditioned in both cases.

To make the output spaces identical, embed the complete finite qubit
apparatus into the infinite comparison space by appending vacuum beyond
\(M-1\); this includes its many-head sectors, not only the parent's
one-head sector. The comparator is the same normalized infinite half-line
packet as (2). Every emitter, clock, source, old and reference output is
retained. Bad thermal components may undergo complicated many-head
dynamics. Their initial full trace error is propagated exactly, so no
one-head spectral assertion is needed for them, and none is made.

Choose now
\[
G=13,\quad \beta=10,\quad t_{\rm h}=1,\quad \tau=1.
\tag{26}
\]
Over (1), \(M\le5\times10^{31}\) and \(N=M+3<10^{32}\). The elementary
series bound \(e>8/3\) gives the exact rational certificate
\[
\epsilon<N e^{-130}
<10^{32}(3/8)^{130}<10^{-22},\qquad
g(\epsilon)<3\times10^{-11}.
\tag{27}
\]
Using \(\sqrt2\kappa<2\times10^{-8}\),
\[
g(\epsilon)+2F+\sqrt2\kappa
<
\frac{3735322962607129}{390625000000000000}
=0.00956242678427425024<0.01.
\tag{28}
\]
Thus a finite nonzero-temperature marginal, even correlated with the
old/reference, yields the claimed complete finite-horizon halt comparison.
At \(\kappa=10^{-8}\), \(T=10^{22}\), \(M=5\times10^{23}\), and the
total elapsed observation interval is \([2+10^{22},2+2\times10^{22}]\).
At \(\kappa=10^{-12}\), the sufficient \(M\) is \(5\times10^{31}\).
These are enormous sufficient resources in the parent's Hamiltonian
units. No practical minimum, physical seconds, finite-device all-future
statement or exact target gate follows.

## 7. Hardware, local loads, scalar energy and work

There are \(M+5\) modeled quantum qubits: old pair, source pair, \(M\)
clock qubits and one emitter. No new quantum sites or nonlocal edges are
introduced. The new controls comprise \(M+7\) two-body blocks on \(M+6\)
existing edges and \(M+3\) onsite blocks, hence \(2M+10\) blocks.
The two source-source controls share an edge; sharing does not erase either
norm. The runtime has \(M+16\) added blocks besides \(K\), so the
preparation has \(3M+26\) added positive blocks besides \(K\).
Their coefficients can share the single envelope (19), but their separate
gain, phase and wiring resources remain supplied.

The new-control incident norm sums, before multiplication by \(s\), are
\[
\begin{array}{c|c}
\text{site}&\text{new-control incident sum}\\ \hline
\text{old }i&2g_i\\
A&G-\Delta_A+u+2\lambda_A\\
B&G-\Delta_B+u+2\lambda_B\\
c_0&G-J-\mu_0\\
c_1&G+\nu\\
\text{ordinary clock}&G\\
c_L,c_{L+2}&G+\kappa\\
c_{M-1}&G-J\\
e&G+E_0+6\kappa
\end{array}
\tag{29}
\]
Every such sum is less than 19. Adding the literal runtime loads gives the
following peak preparation loads at \(\kappa=10^{-8}\); the formulas
with \(\kappa\) are exact, and terminating decimal entries are exact.

| Site | Runtime added load | Runtime plus preparation controls |
|---|---:|---:|
| old1 | 1.993757127633340 | 3.987514255266680 |
| old2 | 1.198638631120596 | 2.397277262241192 |
| source A | 20.332662089993454 | 39.288796602545442 |
| source B | 17.078839343776311 | 33.586687642861878 |
| \(c_0\) | 8.015120691541701 | 20.663604977376468 |
| \(c_1\) | 6.730044773026091 | 21.189937586047060 |
| ordinary clock | \(4J\) | \(13+4J\) |
| either emitter attachment | \(4J+3\kappa\) | \(13+4J+4\kappa\) |
| far clock end | \(3J\) | \(13+2J\) |
| emitter | \(E_0+2\kappa\) | \(13+2E_0+8\kappa\) |

The unchanged old edge \(K\) has norm 3 in addition to both old-site
entries. The largest combined added load is below 40. The old runtime cap
two is restored after release, but is explicitly violated during
preparation. Cancellation in the total Hamiltonian does not refund
incident block norms. A theorem requiring the old cap two at every instant
has not been proved by this route.

Each individual new-control block has norm below 14. Its derivative norm
is at most its norm times \(3/(2\tau)\); the entire incident derivative
sum at any site is below \(28.5/\tau\). For (26), a supplied incident slew
allowance 30 therefore suffices. The global sum grows with \(M\), but is
finite for every stated device; for example
\(\sum_{\ell\in R}\|R_\ell\|<14(2M+10)\).
No uniform global control-norm or control-action budget is inferred.

For explicit scalar bookkeeping, the coefficient of the whole-system
identity in the full Pauli expansion is
\[
a_{\rm run}=
2+\frac{\Delta_A+\Delta_B+g_A+g_B+\lambda_A+\lambda_B+\mu_0+\nu+E_0}{2}
+h+u/4+JM+2\kappa,
\tag{30}
\]
\[
a_{\rm prep}=2+\chi_{\rm p}+G(M+3)/2,\qquad
a_R=a_{\rm prep}-a_{\rm run}.
\tag{31}
\]
Its integrated phase through hold, release and runtime is
\(a_{\rm prep}t_{\rm h}+a_{\rm run}(\tau+t)+a_R\tau/2\).
This extensive identity contribution has not been deleted. The smaller
seed scalar (24) results from the simultaneous diagonal Pauli action on
the seed, not from replacing physical positive blocks by signed ones.

With work defined as the change of energy supplied to this modeled quantum
system by the explicit time dependence, the exact release balance is
\[
\mathcal W_{\rm rel}=\int_0^\tau
s'(r)\operatorname{Tr}[\rho(r)R]\,dr
=\operatorname{Tr}[H_M\rho_{\rm end}]
 -\operatorname{Tr}[H_{\rm prep}\rho_{\rm start}]
\le0.
\tag{32}
\]
This follows from \(s'\le0\), \(R\ge0\), and the finite-space von Neumann
equation, including all scalar terms and arbitrary retained correlations.
The initial mean energy is
\(\operatorname{Tr}(K\rho_O)+\chi_{\rm p}+GNq\).
Since \(H_M\ge I\), \(1-\langle H_{\rm prep}\rangle\le
\mathcal W_{\rm rel}\le0\); all quantities are finite. Holding and
runtime conserve their respective static total energies. This account
does not specify the heat/work cost of supplying (15), an autonomous
controller, an extractable-work protocol or a reset cycle.

The classical control waveform, its finite distribution and exact gains,
the Gibbs marginal and its temperature, and the static complex XY phases
remain supplied physical resources. No microscopic bath or control-device
Hamiltonian is manufactured here. If such devices are to interact during
release, their complete joint dynamics require a new theorem. A passive
retained environment is already permitted as the reference in (25);
there is no tracing out of a modeled output to obtain the bound.

## 8. Prior machinery, actual checks and next decision

The local-Gibbs source note already supplies the product-versus-correlated
marginal distinction, the sharp \(g(\epsilon)\) law, physical scalar/work
bookkeeping and finite-ramp discussion. The controlled-stop note already
supplies finite continuous ramp comparisons and the need to retain
chronological old aging. The local conditional-bias/rotated-Gibbs note
contains a general ready-range removal estimate and paid positive
counterterms. This candidate does not claim those generic principles as
new. Its new proposed bridge is the explicit full-space counterterm list
(10)–(14) for the literal PR9665 installed emitter, the exact
\(\sqrt2\kappa\) seed residual, and their complete finite-horizon
composition with the actual inherited output. Prior-source search and
fresh reading coverage are recorded in [SOURCE_COVERAGE.md](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/SOURCE_COVERAGE.md.txt).

[RESOURCE_PLAN.json](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/RESOURCE_PLAN.json) preceded the only scientific
execution. The launcher copied the actual checker, serialized source,
input, interpreter and SymPy entry/metadata identities with caps, flushed,
fsynced and closed [PRELAUNCH.json](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/attempt_01/PRELAUNCH.json), then spawned
the child. All bound bytes and generation fields matched after execution.
Caps were 20 CPU seconds soft/hard and 30 external wall seconds, at most
two attempts, maximum dense matrix dimension 4, diagnostic clock length
at most 20, and no grid, quadrature, optimization or dynamics. Only one
attempt ran, successfully; no failure or retry occurred.

The actual [receipt](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/attempt_01/RECEIPT.json) records exit 0, no timeout,
1.1043415828607976 seconds wall, 0.680372 user CPU and 0.05651 system CPU
seconds. The program used Python 3.13.5 and SymPy 1.14.0, with program
wall 0.5186617909930646 seconds. Child peak RSS was 65,011,712 native macOS
bytes. No OS memory limit or measured thread count is claimed.
The interpreter binary, SymPy entry and installed metadata are pinned;
this is not a hash of every transitive dependency file.

[check_preparation.py](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/attempt_01/check_preparation.py) and its exact executed copy
are retained. Full [stdout](../outputs/thermal_resonance_halt_2026_10_17_inputs/frozen_sources/emitter_preparation_independent/attempt_01/stdout.json) is 25,536 bytes;
[stderr](../outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/stderr.txt) is empty. The report contains 122 named
checks, plus local-spectrum and block-count assertions. Sparse Pauli
identities at \(M=16,20\), symbolic in \(\kappa\), have zero residual;
the seed Gram residual is exactly \(2\kappa^2I\). The full Hilbert
dimensions \(2^{21},2^{25}\) were not allocated. Full local positivity and
norms were checked at the exact rational upper endpoint; the displayed
block spectra and coefficient inequalities, rather than endpoint sampling,
prove positivity for the whole interval. The general-length proof is the
termwise identity (10), not inference from two lengths. Exact rational
checks also corroborate the loads, cubic ramp and budget (28).

These checks do not execute thermalization or the huge clock, establish a
native controller, independently validate the inherited scattering theorem,
or formally prove the analytical operator statements. They are author
corroboration. The supplied-input and control hypotheses, original fixed
target residual and finite observation window remain essential.

The next decision is a separate check of the full-space cancellation,
seed-range Duhamel comparison, physical scalar/aging convention and
complete correlated-input composition. Root's separate mechanism was
not viewed before this candidate's freeze. No worktree, Git, publication,
checkpoint, prompt, axiom or audit verdict was changed, and no model or
reasoning override or subdelegation was used.

<!-- END PRESERVED SOURCE emitter_preparation_independent/CANDIDATE.md -->


## Preserved source: Interacting preparation

<!-- BEGIN PRESERVED SOURCE emitter_preparation_root/CANDIDATE.md -->
---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
source_status: root_candidate_pending_independent_check
native_preparation_claim: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A finite thermal seed and bounded release with the emitter Hamiltonian left installed

This is a proposed conditional construction, not a source acceptance, physical
cooling model, or audit verdict. It was derived by root without seeing the
separately assigned preparation derivation. A source map and freeze record
will bind its exact dependencies. No scientific program has run for this
candidate at the time this body is first written.

## 1. Question, prior work and exact domain

PR9665 supplies a finite autonomous runtime from an independently pure excited
emitter, an empty clock and two empty source qubits. The new question is whether
that input can be replaced by a finite-temperature auxiliary delivery, and
whether positive local preparation controls can be released into the same
runtime without an error proportional to the enormous clock length.

The answer proposed here is conditional on additional positive local controls
and a genuine Gibbs-marginal delivery. Those permissions are not consequences
of the minimal axioms. They remain separate from the approved scale reference,
kinetic-form isotropy and pointwise realized-state primitives. No axiom,
primitive, physical Hamiltonian identification, thermalization mechanism or
Record law is added. The registered primitives and their current source notes
were read. They do not select the local coefficients, a temperature, this
initial state, or a physical controller.

The main mathematical runtime source is
`docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md` at
PR9665/head `0e3993770a7a2dd872018f9dd3c76c2d9a624db9`, SHA256
`f3a10874f4f52bef0bc5c393081590aff2f71b877a0f44cac9a3cbe05b34da87`.
The full physical blocks are also explicitly given in the product-seed and
two-body autonomous-halt notes in that exact checkout. The runtime remains
provisional conditional mathematics; publication is not retained audit.

The existing local Gibbs-controller source already proves a supplied
Hamiltonian-to-Gibbs-to-complete-reference interface. Its weighted unary
ground-state engineering is not needed for a product seed. Its sharp
correlated-reference estimate is credited and rederived below. The
product-source controlled-stop note already uses state-supported Duhamel
comparisons during ramps, but for a different weak-mediator device and an
already pure source. It supplies neither the thermal input nor this emitter
release. The present proposed gain is their compatible use with a new
interacting, gapped seed Hamiltonian and the actual finite emitter. This is
not an exhaustive novelty claim. The bounded search and reading record are
preserved separately.

Let M>=16 be the actual fixed number of clock qubits. Keep the two old sites,
two sources A,B, emitter e, bent clock geometry and every finite endpoint
diagonal of PR9665. There are N=M+3 auxiliary qubits (clock, A,B,e), and M+5
device qubits including the old pair. No inventory grows after design.
All additional retained factors, including a preparation bath or apparatus
output if present, may be in an arbitrary passive reference R. They are
retained, not traced out to assert a complete-output result. During the
release and runtime, their interactions must be absent or explicitly charged.
The old input may be mixed and entangled with R.

Use exactly K=2I+Z1 Z2 and W=((9+12i)I+(-16+12i)X1 X2)/25. All terminating
decimals in the runtime's parameter table are exact. In particular

    J=0.030021107107032, nu=1.459892813020969,
    gA=0.996878563816670, gB=0.599319315560298,
    q0=4.510351185997098,
    E0=4J/(q0^2+1), L=12, phi=4 arctan(1/q0),
    10^-12 <= kappa <= 10^-8, sigma=10^-6.

All Hamiltonian times, energies, inverse temperatures and derivative caps are
in the declared model units. No physical temperature or seconds conversion
is derived by this construction.

## 2. The complete finite physical Hamiltonian

Put n_j=(I-Z_j)/2 and a_j=|0><1|_j. Write

    G_A=gA n_A(I+X1), G_B=gB n_B(I+X2), G=G_A+G_B,
    b_A=2gA, b_B=2gB,
    C=DeltaA n_A+DeltaB n_B
      +hAB(n_A+n_B-a_A^dagger a_B-a_B^dagger a_A)+u n_A n_B,
    Hc=J n_c0+J n_c(M-1)
       +J sum_(j=0)^(M-2)(n_cj+n_c(j+1)
                         -a_c(j+1)^dagger a_cj-a_cj^dagger a_c(j+1)),
    Vc=lambdaA n_c0(I+X_A)+lambdaB n_c1(I+X_B)+mu0 n_c0.

Every term of C,Hc,Vc displayed here is positive. The two finite endpoint
fields in Hc maintain the same 2J one-head diagonal as the infinite clock.
Use the runtime's exact DeltaA,DeltaB,hAB,u,lambdaA,lambdaB,mu0 values.
They are positive. Neither an unspecified new source Hamiltonian nor a
commutation of K with the interacting old/source Hamiltonian is assumed.

At j=L,L+2 put t_L=kappa, t_(L+2)=-kappa exp(i phi) and

    Q_ej=kappa(n_e+n_cj)+t_j a_cj^dagger a_e
                           +conj(t_j)a_e^dagger a_cj.

The exact installed full-qubit runtime is

    Hrun=K+C+G+Hc+Vc+nu(I-n_c1)
         +Q_eL+Q_e(L+2)+(E0-2kappa)n_e
         +kappa(I-n_cL)+kappa(I-n_c(L+2)).                 (1)

All its terms are positive, E0>2kappa, and Hrun>=K>=I. The pair Q has spectrum
0,0,2kappa,2kappa. The old/source G_i has spectrum 0,0,0,2g_i.
The runtime's actual scalar on the one-head sector is nu+2kappa. Equation
(1), not that restriction, governs preparation and all thermal sectors.

Let Omega be the auxiliary product with e excited and every other auxiliary
empty, and let E append Omega to the old system. There is an isometry-valued
map V_seed with V_seed^* V_seed=2I, whose two orthogonal clock locations are
c_L and c_(L+2), such that

    Hrun E=E[K+c_run I]+kappa V_seed,
    c_run=E0+nu+2kappa.                                  (2)

V_seed leaves both sources empty and has emitter empty. It has no component
in ran(E). This follows directly from (1): every term except the old K,
literal scalar, emitter energy and its two hopping matrix elements is dark
on E. Equation (2) is a full input-operator identity on the old pair, so it
remains true with every passive reference. It is stronger than a statement
about one old basis state or an auxiliary marginal.

## 3. Positive controls selecting the seed while Hrun stays installed

Choose a supplied preparation gap Delta>0. Add the following separate
positive controls, all on already occupied onsite or NN pair supports:

    b_A I-G_A, b_B I-G_B;
    2kappa I-Q_eL, 2kappa I-Q_e(L+2);
    nu n_c1, kappa n_cL, kappa n_c(L+2);
    Delta n_j for each of the M+2 blank-target qubits j;
    (E0-2kappa+Delta)(I-n_e).                            (3)

Call their sum A. The complements are positive on their complete pair
spaces, not just the one-head subspace. They are independently supplied
controls on the same actual supports. Identity reserves in complements are
part of the physical implementation. Such complement manufacture is an
additional permission; an arbitrary physical positive-channel dictionary
need not provide it. No original term of Hrun is removed or rescaled.

Their exact sum yields

    Hprep=Hrun+A=K+c_prep I+Haux,
    c_prep=b_A+b_B+nu+E0+4kappa,
    Haux=C+Hc+Vc+Delta D,
    D=(I-n_e)+n_A+n_B+sum_j n_cj.                        (4)

Haux acts only on the N auxiliary factors. All its terms are positive and
annihilate Omega, except that Delta D has exactly that one-dimensional
kernel. Therefore

    Haux Omega=0, Haux>=Delta D,
    ker(Haux)=span{Omega}, gap(Haux)>=Delta.              (5)

The clock/source terms need not commute with D: Vc flips a source when its
clock control is occupied. The argument uses positivity on the whole
Hilbert space, not a free-particle spectrum or assumed number conservation.
Only the preparation auxiliary ground is selected. The old system remains
arbitrary and evolves under literal K. Its ground is neither selected nor
required. The complete Hprep is not asserted to have a unique full-device
ground.

This limited cancellation is important. Canceling every clock bond would
also be a possible supplied construction, but would add extensive
compensator reserves unnecessarily. Here only the two old/source ports and
two emitter bonds are complemented. The interacting positive clock/source
Hamiltonian remains in Haux.

## 4. A full-sector thermal certificate

Supply the finite auxiliary marginal Gamma_beta=exp(-beta Haux)/Z at beta>0,
or a delivered marginal within half-trace distance eta_delivery of it.
This is a delivery promise, not a cooling theorem or a product-state
assumption. Since Hprep separates old and auxiliary dynamics, isolated
preparation at a known elapsed duration can keep old K literal. Any actual
bath coupling must be auxiliary-only for that older-input conclusion; the
general theorem compares with the actual old/reference marginal at release.

Let lambda_j be the increasingly ordered 2^N eigenvalues of Haux and d_j
those of D, with multiplicities. The min-max principle and (5) give
lambda_j>=Delta d_j. The eigenvalues d_j are the binomial list 0,...,N,
with multiplicities choose(N,k). Scalar exponential monotonicity on these
ordered eigenvalues, not a false operator-exponential monotonicity claim,
gives, for q=exp(-beta Delta),

    1 <= Z <= sum_k choose(N,k) q^k=(1+q)^N,
    d_thermal=1-<Omega|Gamma_beta|Omega>
             =1-1/Z <=1-(1+q)^(-N) <=N q.               (6)

The last inequality follows from convexity of (1+q)^(-N), whose tangent at
zero is 1-Nq. The estimate includes every excitation sector and every
noncommuting source-clock interaction. It does not assert a product Gibbs
law or identify the actual spectrum with Delta D. The finite-beta state is
mixed. The sufficient inverse temperature scales logarithmically with the
finite auxiliary count at a fixed supplied Delta and error budget; no
equilibration-time conclusion is drawn.

One useful mean-energy bound also follows without replacing that spectrum.
If beta Delta>=1, x exp(-beta x) is nonincreasing for x>=Delta. The positive
eigenvalue lambda_j associated by order with k>=1 is at least Delta k.
Consequently

    E_aux=Tr(Gamma_beta Haux)
      <=Delta N q(1+q)^(N-1).                           (7)

Here the numerator is bounded term by term and Z>=1 is used. If Nq<=r<1,
then E_aux<=Delta r exp(r)<=Delta r/(1-r). This is a nominal Gibbs mean,
not a general mean bound from trace distance alone. For a merely nearby
delivered marginal, a sufficient extra allowance is
2||Haux|| eta_delivery; no small trace distance is silently upgraded into
a dimension-free energy certificate. Alternatively supply its actual mean.

Every old/reference extension rho_aux,old,R with that delivered marginal
satisfies d=1-Tr(P_Omega rho_aux)<=min(1,Nq+eta_delivery). Let rho_old,R be
its exact unconditioned marginal. The known sharp pure-factor estimate gives

    ||rho-P_Omega tensor rho_old,R||_1
      <=g(d):=d+sqrt[d(4-3d)] <=3sqrt(d).                (8)

For completeness, purify rho by retaining a further factor and split the
pure vector into sqrt(1-d)|Omega>u+sqrt(d)v with v orthogonal to Omega in
the auxiliary factor. Its reference marginal is (1-d)|u><u|+d rho_v.
The full difference from P_Omega times that marginal is the sum of
-d P_Omega tensor rho_v and a rank-two Hermitian operator on the orthogonal
vectors |Omega>u,v with matrix [[0,sqrt(d(1-d))],[sqrt(d(1-d)),d]]. Their
trace norms are d and sqrt(4d-3d^2), respectively. Triangle inequality and
partial-trace contraction prove (8). The scalar bound is monotone in d on
[0,1], with the endpoint values interpreted directly. An independent product
Gibbs delivery instead has the sharper complete error 2d_thermal. A thermal
marginal alone does not entitle that product estimate. The comparison keeps
the exact unconditioned old/reference marginal; conditioning it on the good
subspace would change the target.

## 5. Actual smooth release and its length-independent error

For 0<=s<=tau use a(s)=1-3(s/tau)^2+2(s/tau)^3. Keep a=1 before release
and a=0 afterwards. The actual Hamiltonian is

    H(s)=Hrun+a(s) A.                                   (9)

It remains a sum of positive onsite/NN pair blocks. All original runtime
blocks, including K, stay installed. The control is C1 at its joins,
max|a'|=3/(2tau), and integral_0^tau a(s)ds=tau/2. It is a prescribed
external release, not a whole-apparatus autonomous controller, band-limited
drive, or proof of switching manufacture. No drive acts in the subsequent
runtime interval.

By (2),(4),

    A E=(c_prep-c_run)E-kappa V_seed,
    H(s)E=E[K+c(s)I]+(1-a(s))kappa V_seed,
    c(s)=c_run+a(s)(b_A+b_B+2kappa).                     (10)

Define E(s)=E exp[-isK-i integral_0^s c(v)dv]. Its norm is one. Subtract
its derivative from the actual Schrodinger equation, and apply the unitary
Duhamel formula. The inhomogeneous term has operator norm exactly
sqrt(2)kappa(1-a(s)); no commutation of K with Hrun or A is used. Hence

    ||U_release E-E exp(-i tau K-i Phi)||
       <=sqrt(2)kappa integral_0^tau(1-a(s))ds
       =kappa tau/sqrt(2),
    Phi=c_run tau+(b_A+b_B+2kappa)tau/2.                 (11)

This is a complete old-input isometry bound with arbitrary references. Its
lack of M comes from the exact seed identity, not from dropping extensive
fields, assuming a typical state or estimating a many-head propagator by a
one-head operator. Actual finite-temperature inputs are first compared by
(8), then propagated by the actual full unitary. The two error steps must
not be reversed to apply (11) directly to all thermal sectors.

The physical scalar and emitter energy during release occur in Phi. During
the later autonomous runtime, E0 instead enters the actual spectral envelope;
an extra exp(-itE0) must not be added to the runtime comparator. A long hold
at Hprep preserves the thermal marginal and has its own old age and scalar
c_prep times that actual hold duration. Preparation time before release is
not inferred, zeroed or supplied by this calculation.

## 6. Literal block loads, reserves and slew

The extra incident positive-block norm sums from (3) are

| Site | Extra preparation load |
|---|---:|
| old1, old2 | b_A, b_B respectively |
| A, B | Delta+b_A, Delta+b_B respectively |
| c1 | Delta+nu |
| c_L, c_(L+2) | Delta+3kappa |
| e | Delta+E0+2kappa |
| every other clock site | Delta |

The sites in these rows are distinct at L=12,M>=16. All maxima occur at
a=1 because these extra blocks have a common nonnegative envelope. For the
exact family coefficients, max extra incident load=Delta+b_A. Thus a
supplied per-site derivative allowance Lambda>0 is met if

    tau >=3(Delta+b_A)/(2 Lambda).                       (12)

The sum of all extra positive-block norms is exactly

    S_A=Delta N+c_prep.                                 (13)

It is an upper bound on ||A||, not necessarily its exact operator norm.
The coefficient of the full identity in A's Pauli expansion is instead

    alpha_A=[Delta N+3(gA+gB)+nu+E0+4kappa]/2.            (14)

Both differ from the seed expectation b_A+b_B+2kappa. Equation (10) uses
that actual seed action, including its orthogonal component, rather than
mistaking any one of these three prices for another. Extensive identity
pieces of onsite projectors cancel their Z pieces on a blank target; this
does not discard their norm, load, precision or supplied control cost.

For Delta=1, the largest combined incident block sum is at A and is
20.332662089993454+1+1.993757127633340=23.326419217626794.
The old1 added load during preparation becomes 3.987514255266680, with
the old edge's norm 3 additional. Thus the runtime's added-old-site cap two
does not hold during this preparation. There is no all-site cap two or free
compensation. The generic full-space control-calibration allowance remains
an integral of the actual error norm; arbitrary extensive errors can still
scale with M. The improved nominal release comparison does not remove that
physical calibration obligation.

## 7. Complete finite-horizon composition and a sufficient example

For a runtime-certified M and t, let epsilon_halt denote the actual finite
isometry bound of PR9665. Write U_id,kappa(t) for its full normalized
half-line comparator, with emitter empty, both sources empty, all clock
amplitudes, the same zeta and the physical scalar exp[-i(nu+2kappa)t].
After the release and then t units of actual autonomous runtime, the pure
seed comparator is

    U_id,kappa(t) exp(-i tau K-i Phi)
      =zeta exp[-i Phi-i(nu+2kappa)t]
         beta_kappa,t tensor iota exp(-itK) W exp(-i tau K). (15)

Its old factor is exp[-i(t+tau)K] W because the explicit W commutes with K.
This never commutes K through the physical interacting evolution. The
profile beta_kappa,t uses the actual kappa; its time argument is runtime
since the end of release, not laboratory time t+tau. Its finite comparison
is embedded into the infinite output space as in the parent theorem. The
embedding does not discard finite-device outputs or condition on a clock
position.

Combining (8),(11) with the runtime theorem gives the unhalved complete
trace-norm bound

    error <=min(2, g(d)+sqrt(2)kappa tau+2epsilon_halt).  (16)

A further supplied release perturbation integral eta_release adds at most
2eta_release by full-space Duhamel. A runtime perturbation needs its own
actual-time allowance; static joint-parameter robustness and temporal noise
are not supplied here. Finite Gibbs input sectors other than one head are
controlled only through (8); no new runtime theorem on those sectors is
asserted.

For a concrete proposed allocation, throughout kappa in [10^-12,10^-8],
choose T=10^6/kappa^2, M=ceil(50T), Delta=1, beta=100, tau=10000 and
Lambda=10^-3. Take eta_delivery=eta_release=0 for this example. Then
N<=5*10^31+3, and the elementary e>8/3 yields the rational certificate target

    (5*10^31+3)(3/8)^100 <1/22500000000.                 (17)

If this displayed integer inequality is checked, (6),(8) give g(d)<2*10^-5.
Also (12) holds since Delta+b_A<3 and 3*3/(2*10000)<10^-3.
The release trace allowance is sqrt(2)kappa tau<1.5*10^-4.
PR9665 supplies epsilon_halt<.005 on [T,2T]. Consequently (16) is below
.01017, and hence below .0102, throughout that interval measured from the
end of release. At kappa=10^-8, T=10^22 and M=5*10^23; at kappa=10^-12,
T=10^30 and M=5*10^31. These remain enormous sufficient finite devices.
The example does not establish practical preparation, a measured apparatus,
minimal resources, an all-future finite device or a derived temperature.

An actual delivery/calibration error must consume its own part of (16),
and can invalidate this numerical allocation. The strict bound (17) and
block identities are proposed checks, not reported program outputs.

## 8. Prescribed release work and what remains unpriced

With the actual closed device and prescribed Hamiltonian (9), define only
W_release=integral Tr(rho(s) dH(s)/ds)ds. Since a'<=0 and A>=0,
W_release<=0 even on the actual correlated thermal input. The exact energy
balance is E_run,end-E_prep,start. For a nominal Gibbs auxiliary marginal,
E_prep,start=Tr(K rho_old)+c_prep+E_aux. Hrun>=I and 1<=K<=3 imply

    -(2+c_prep+E_aux) <=W_release<=0.                   (18)

This intentionally coarse bound follows for the entire actual evolution,
without replacing the endpoint by a freshly pure seed. Under beta Delta>=1
the nominal E_aux may be bounded by (7). For an approximate delivery use
an actual mean certificate or the explicit norm-sensitive correction after
(7). The result accounts for energy returned to a prescribed release drive;
it is not a recovered controller, work-fluctuation bound, thermodynamic
cycle, cooling cost or renewable resource. All initial apparatus manufacture,
Gibbs supply, temperature control, the setup clock and its outputs, phase
reference, calibration and cooling environment remain supplied and unpriced.

## 9. Failed substitutions and verification boundary

The proof does not cancel every clock bond, assume a free-mode Gibbs law,
apply operator monotonicity of the exponential, or infer a product input from
a marginal. It does not use a full-space ||A||tau estimate as the nominal
seed-release error: that would scale as M and miss the exact supported
identity (10). Conversely, (10) does not permit replacing arbitrary actual
faults by a supported error. It does not erase the positive complements'
reserves or reuse the runtime old-site cap during preparation. These are
specific distinctions in the proposed construction, not universal no-go
claims about competing architectures.

This candidate needs a separate mathematical check of the full decomposition,
thermal spectral comparison, state-supported release, correlated target,
scalar/time composition and literal resource account. The selected same
model and earlier shared runtime work limit independence. Planned small exact
algebra and scalar checks can corroborate these arguments; they cannot
validate a 2^(M+5)-dimensional physical simulation, cooling, all actual
coefficients or the inherited scattering proof. No new Lean proof, dynamics
simulation, bath model or physical axiom has been supplied.

<!-- END PRESERVED SOURCE emitter_preparation_root/CANDIDATE.md -->


## Preserved source: Staged release

<!-- BEGIN PRESERVED SOURCE emitter_preparation_root/STAGED_RELEASE_ADDENDUM.md -->
---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
source_status: root_candidate_pending_independent_check
---
# Release the cold fields before opening the emitter

This proposed extension was derived before root received or read the separate
preparation derivation. It relies on the exact full-qubit construction in
root CANDIDATE.md, SHA256
416a0cd7155a60517bae6944368d9f9619f0f59274b6634004e0c4962d921fa0.
It changes the externally prescribed setup schedule, not the autonomous
runtime. Independent checking is pending. The original common-envelope
candidate and its actual exact-arithmetic run remain unchanged.

## 1. Separate the two release interfaces

Write A=A_rest+A_e1+A_e2 for the positive controls in candidate (3), where
A_ej=2kappa I-Q_ej for the two emitter contacts. Every individual block A_r
of A_rest satisfies

    A_r E=a_r E,

with a_r=b_A for the old1/sourceA complement, b_B for the old2/sourceB
complement, and zero for every cold-field block. The two emitter complements
instead satisfy

    A_e1 E=kappa E-kappa V_1,
    A_e2 E=kappa E-kappa V_2,
    V_1^*V_1=V_2^*V_2=I, V_1^*V_2=0,
    V_seed=V_1+V_2.                                   (A1)

The phases of V_1,V_2 are the actual t_L/kappa and t_(L+2)/kappa; these
are not chosen independently of the installed emitter. Equations (A1) hold
on the complete old input space and with all passive references.

Hold both emitter complements fully on while releasing the other controls.
For any finite actual D>=0, let each u_r(s), 0<=s<=D, be a supplied C1
nonincreasing envelope from one to zero, with zero endpoint derivatives,
0<=u_r<=1. Different controls may have different start times, durations and
shapes. Their actual incident derivative sums must meet the supplied cap.
The generator in this first stage is

    H_early(s)=Hrun+A_e1+A_e2+sum_(r in rest) u_r(s) A_r. (A2)

All cold fields and old-port complements are zero by D. There are no extra
clock/emitter/source factors. If a control has not reached zero, the next
stage does not satisfy this exact schedule; its actual residual requires
separate accounting. A finite known completion time is a condition, not an
inferred property of a large control network.

Substitution of (A1) and candidate (2) gives the exact supported identity

    H_early(s) E=E[K+c_early(s)I],
    c_early(s)=c_run+2kappa+b_A u_A(s)+b_B u_B(s).        (A3)

Thus the ideal seed is preserved exactly throughout the entire early
stage, with actual old age D and phase

    Phi_early=(c_run+2kappa)D
                  +b_A integral_0^D u_A(s)ds
                  +b_B integral_0^D u_B(s)ds.          (A4)

No adiabatic approximation or spectral gap along the release is needed.
The source and all clock qubits stay empty on this comparator because the
only terms that can move its single emitter head cancel exactly. A cold
onsite projector annihilates the seed separately, so its detailed area is
absent from (A4); its physical block load and controller cost are not absent.
Neither source darkness nor this cancellation is assumed for arbitrary
thermal states. Their complete initial error is propagated by the actual
unitary using candidate (8), once.

## 2. Open only the two emitter bonds last

After D, keep A_rest zero. Release A_e1 and A_e2 together over a duration
tau_e>0 with the same decreasing cubic a(s) as the original candidate:

    H_late(s)=Hrun+a(s)(A_e1+A_e2), 0<=s<=tau_e.        (A5)

The supported phase is c_run+2kappa a(s) and the orthogonal residual is
(1-a(s))kappa V_seed. The exact same Duhamel argument now gives

    ||U_late U_early E
       -E exp[-i(D+tau_e)K-i Phi_staged]||
          <=kappa tau_e/sqrt(2),
    Phi_staged=Phi_early+c_run tau_e+kappa tau_e.       (A6)

The nominal release error contains tau_e, not D+tau_e. Long or sequential
removal of the M+2 blank fields therefore does not itself increase that
error. It still consumes real time and real control resources, and ages
the old system. No claim of negligible total setup time follows.

The largest late added incident load is 4kappa at the emitter, so the cubic
late slew is at most 6kappa/tau_e. A supplied allowance Lambda is satisfied
when tau_e>=6kappa/Lambda. For example, tau_e=1 and Lambda=10^-3 suffice
throughout the given coupling family: 6kappa<=6*10^-8<10^-3. This is a
specified finite model duration, not a derived minimum or bandwidth bound.
Only the two emitter-complement envelopes need this particular simultaneous
late profile. If they differ, their actual supported residual has norm
kappa sqrt[(1-a_1)^2+(1-a_2)^2], and its time integral is the corresponding
valid allowance. One must then retain their two separate phase areas.

The early stage admits a simple bounded implementation as well. For a common
cubic release of A_rest, D=10000, Delta=1 and Lambda=10^-3 suffice by the
original extra-load upper bound Delta+b_A<3. Alternatively release its blocks
in separate nonoverlapping cubic windows of a chosen duration ell. It is
sufficient that 3||A_r||/(2ell)<=Lambda for every block. The actual D is the
sum of their finite window durations and any gaps. Equation (A3) still holds
at every time, even through gaps. This is an explicit possibility for
sequentially scheduled supplied controls, not a free universal controller
or a proof that all sites can be addressed by a native mechanism.

## 3. Full target, thermal errors and work

For the finite runtime theorem after setup, replace tau and Phi in candidate
(15) by D+tau_e and Phi_staged. In particular the complete comparator is

    zeta exp[-i Phi_staged-i(nu+2kappa)t]
       beta_kappa,t tensor iota exp(-itK)W exp[-i(D+tau_e)K]. (A7)

The spectral profile uses runtime t since the end of setup. The literal old
age is t+D+tau_e, and any earlier isolated preparation duration must be
added when an earlier old input is compared. K is never commuted through
the physical interacting Hamiltonian. Its commutation with the explicitly
given W is only a simplification of the comparator.

For the same arbitrary correlated delivered input the complete unhalved
trace bound is

    min(2,g(d)+sqrt(2)kappa tau_e+2epsilon_halt).        (A8)

With the candidate's nominal beta=100,Delta=1,M<=5*10^31, exact thermal
count bound and tau_e=1, the already checked g(d)<2*10^-5 is unchanged.
The release allowance is less than 1.5*10^-8. The inherited PR9665 finite
epsilon_halt<.005 therefore gives total trace error below .010020015.
The point is the different setup timing permission and supported error
account, not the last decimal of that sufficient error bound. If a future
separately qualified runtime has another onset or device size, its actual
thermal count and finite time horizon must be substituted explicitly; this
addendum does not qualify the pending resonance-family theorem.

All early and late coefficients are nonincreasing on positive added blocks.
The sign W_setup<=0 and endpoint identity from candidate (18) therefore
hold over both actual stages, with the same initial Hprep and final Hrun.
Its nominal mean-energy allowance remains the candidate's interacting
Gibbs estimate. This is work returned to the supplied drive, not a cooling
cost, restored controller, or reusable blank source. Preparation, phase
reference, timing manufacture, isolation and physical energy/Record
identifications remain open or supplied.

The gain relies on exact cancellation of the two emitter hopping blocks
during the potentially long early stage. A residual uncanceled hopping of
norm eta would generally add a term of order eta D; a small pointwise
miscalibration is not an all-duration certificate. This particular residual
is local to the emitter, so one may formulate a local supplied precision
certificate, but this addendum does not derive or waive it. Runtime temporal
noise is also outside scope. The late onset must not be counted from the
start of a long early setup while forgetting actual old aging.

<!-- END PRESERVED SOURCE emitter_preparation_root/STAGED_RELEASE_ADDENDUM.md -->


## Preserved source: Preparation/resonance composition

<!-- BEGIN PRESERVED SOURCE preparation_resonance_composition/CANDIDATE.md -->
# Conditional thermal handoff into resonance-scale autonomous output

Status: root composition proposal. The resonance and exact-product preparation
sources are selectively qualified. The smaller-control interacting preparation
and its staged release are still under a separate review; that alternative
below remains conditional on its source being accepted. No new native supply
or retained status is asserted.

## Exact interfaces and common device

The runtime source is the unchanged `resonant_family_candidate/CANDIDATE.md`
(401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0),
qualified at `resonant_family_root_qualification/ACCEPTANCE.json`
(bb280c96d290e28b42c45994cab3fe9871d671b0d20d39a36ae09d211ef98686).
Its separate review is70eaca751449653eb33255a8b6c0509cde2d4f69de14d39d353c5b96b838c172.
The exact-product preparation source is
`emitter_preparation_independent/CANDIDATE.md`
(b7ef6e98b16bcffb609cbf8a9cca2aee03d4bb20ac6295e99c744f488ad14227),
qualified by root's full analytical review and byte checks at
`preparation_product_root_qualification/ACCEPTANCE.json`
(43e1609d6e38b2220e35e1637428263e49b38d1ac22ed282ee64f3d7d3f60ca5).
Root's alternative is `emitter_preparation_root/CANDIDATE.md`
(416a0cd7155a60517bae6944368d9f9619f0f59274b6634004e0c4962d921fa0)
and `STAGED_RELEASE_ADDENDUM.md`
(1c021b815445bbfc8146b7b37d21b3475769f065a21247bda86563f649f90885).
All share the literal runtime at Git0e3993770a7a2dd872018f9dd3c76c2d9a624db9.

Choose one exact fixed apparatus kappa in[1e-12,1e-8], sigma1e-6,L12,
T=kappa^-2 and M=ceil(50T). Keep precisely the installed full-qubit H_M,
including its finite far-end J n_(M-1), old K=2I+Z1Z2 and physical scalar
c_phys=nu+2kappa. No matching parameter, loop phase, source port, old
interaction or seed changes. M>=16 and N=M+3<=5*10^25+3<10^32.
The preparation identities and supported release bounds hold for every
finite M>=16; their earlier numerical demonstrations used the larger
parent-family bound M<=5*10^31. Reducing the finite device as prescribed
therefore preserves those thermal upper bounds. The resonance theorem,
not the older moment theorem, supplies the new interval[T,2T].

Write E for the full seed isometry (excited emitter, vacuum source/clock),
B_(kappa,t) for the actual normalized outgoing packet with empty emitter
and source, and W for the unchanged target gate. The qualified runtime
interface is, after embedding by extra clock vacuum,

    ||exp(-it H_M)E - zeta exp(-i c_phys t)
          B_(kappa,t) exp(-it K) W|| < F_res,  T<=t<=2T,
    F_res < .004832.

The infinite-source theorem is all-future; only this finite-horizon
interface is used here. Its full packet, seven-coordinate and closed-tail
budgets, fixed nonzero target residual and actual apparatus-dependent
f_kappa rho_kappa remain inherited premises. There is no assertion of
stability to simultaneous coefficient/phase/calibration errors.

## General composition

Let an actual preparation/release unitary U_setup satisfy

    ||U_setup E - exp(-i Phi_setup) E exp(-is K)|| <= delta_release

for its complete duration s. Suppose the actual delivered full joint input
obeys ||rho - E rho_OR E*||_1 <= d_prep, with the exact unconditioned
old/reference marginal. Tensor identities on passive references throughout.
Apply this full trace comparison before evolving; then the supported
isometry estimate and unitary invariance imply

    ||exp(-itH_M)U_setup rho U_setup* exp(itH_M)
      - I_total rho_OR I_total*||_1
       < d_prep + 2 delta_release + 2 F_res,

    I_total = zeta exp[-i(Phi_setup+c_phys t)]
              B_(kappa,t) exp[-i(s+t)K] W.

Only [W,K]=0 was used to combine chronological old aging. H_M and the
actual setup Hamiltonians are not assumed to commute with K. The finite
apparatus embedding includes every many-head sector; no runtime spectral
claim is applied to a thermal bad component. The comparison packet has
runtime index t, not s+t, and E0 is not added again to the runtime scalar.
Every modeled clock/source/emitter/old/reference output is retained.

## Alternative P: exact-product thermal preparation

Use the independently derived positive controls yielding
H_p=K+chi_p I+13Q, chi_p=nu+E0+u+4kappa and N-qubit defect count Q.
Supply its auxiliary Gibbs marginal at beta10. Hold for one Hamiltonian
time unit and release all added controls by the stated cubic over one
unit. Then s=2 and

    epsilon <= N exp(-130) <10^-22,
    d_prep <= g(epsilon)=epsilon+sqrt(epsilon(4-3epsilon)) <3*10^-11,
    delta_release <= kappa/sqrt(2),
    Phi_setup = chi_p + c_seed + (u+2kappa)/2,
    c_seed=nu+2kappa+E0.

The complete unhalved trace bound is therefore strictly below

    .009664 + .00000002000 + .00000000003
       = .00966402003 < .009665.

This uses only the safe sqrt(2)<2 and the qualified .004832 ceiling.
The exact-product source's tighter older-parent numerical expression is
not reused as a theorem for the shorter runtime. Its positive block and
thermal identities remain valid because M only enters the defect count
and endpoint pattern, both explicitly paid here.

The controls add2M+10 positive blocks on existing sites/edges. Preparation
source A load is39.288796602545442; old-site added loads are3.987514255266680
and2.397277262241192 in addition to the unchanged old edge norm3. A supplied
incident slew allowance30 supports the unit cubic release. Runtime old-site
cap two returns only after release. Gibbs supply, all exact controls and
their setup remain premises.

## Alternative I: interacting thermal preparation with staged release

This paragraph is a composition of the root source and addendum, whose
independent source decision is pending at this freeze. It must not be
promoted by the already accepted alternative P.

The proposed positive controls give H_p=K+c_p I+H_aux with
H_aux>=Delta D>=0 and unique seed ground. Take Delta1,beta100 and supply
the auxiliary Gibbs marginal. The source uses a full eigenvalue min-max
comparison, not operator monotonicity of the exponential or a free-Gibbs
assumption, to obtain epsilon<=N exp(-100). Even the older, larger bound
N<=5*10^31+3 gives g(epsilon)<2*10^-5; it therefore suffices for the new M.

Keep both emitter complements on while every other control follows a
common decreasing cubic over D_early=10000. The seed has zero residual
through that whole interval, though it accumulates its exact phase and
old aging. Remove the two emitter complements by a final common cubic
over tau_e=1. Let b_A=2g_A,b_B=2g_B. Then s=D_early+1 and the source gives

    delta_release <= kappa/sqrt(2),
    Phi_setup = (c_seed+2kappa) D_early
                 +(b_A+b_B)D_early/2 + c_seed+kappa.

Consequently the complete unhalved trace bound is strictly below

    .009664 + .00000002 + .00002 = .00968402 < .009685.

There is no new quantum site. This route addsM+10 blocks: four two-body
complements, three positive occupancy compensators, M+2 cold blank-site
fields, and one emitter vacancy pin. Peak added source-A load is
23.326419217626794. The larger preparation old-site loads are the same
as alternative P, so old cap two is again exceeded during preparation.
The early incident control bound is Delta+b_A and its cubic slew is
3(Delta+b_A)/(2D_early)<.001; the late emitter incident slew is
6kappa/tau_e<.001. Thus the supplied incident allowance .001 suffices.
General asynchronous early release is a source-level possibility, but
this concrete composition uses the common early cubic only. A long early
interval is not free: D_early remains in the actual old age and phase,
and persistent uncanceled emitter hopping would require its own integral
error budget. Neither construction provides autonomous setup.

## Resource and verification boundary

At kappa1e-8 the finite device uses M5e17 clock qubits and M+5 total
qubits; its runtime window is[1e16,2e16]. The corresponding elapsed
observation windows from delivered preparation state are[2+T,2+2T]
for P and[10001+T,10001+2T] for I. At kappa1e-12 the prescribed
clock length is5e25. All times are declared Hamiltonian units, not seconds.

These finite, conditional, complete-output bounds do not imply exact
halting, an all-future finite device, practical resources, physical energy
identification, independent retained audit, reset/reuse, cooling dynamics,
native controllers or framework Record production. The supplied preparation
marginal starts the protocol; no unaccounted thermalization-time promise
is made. Signed work and extensive identity coefficients are the separate
source formulas and must remain present in publication.

No numerical scientific execution accompanies this short composition.
The arithmetic above is explicit decimal addition of qualified or clearly
pending ceilings; the load-bearing step is the operator/trace composition
and exact source compatibility. Root requests a selective independent
interface check before treating this composition as checked science.

<!-- END PRESERVED SOURCE preparation_resonance_composition/CANDIDATE.md -->
