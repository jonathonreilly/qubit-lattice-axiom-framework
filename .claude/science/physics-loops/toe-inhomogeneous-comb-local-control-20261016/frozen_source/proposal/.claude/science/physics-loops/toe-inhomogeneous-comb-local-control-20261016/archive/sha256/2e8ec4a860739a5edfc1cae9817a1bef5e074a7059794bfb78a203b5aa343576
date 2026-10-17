---
title: "Autonomous onsite-energy source-qubit rotations with bounded local interactions"
claim_id: onsite_energy_autonomous_controller_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
status: proposed_retained
upstream_dependencies: []
runner: scripts/onsite_energy_autonomous_controller_identity_2026_10_14.py
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Construct a bounded-resource autonomous controller on the same physical source factor in a supplied onsite-energy model."
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Self-contained conditional finite-qubit construction with supplied engineering, preparation, symmetry and read-time premises."
next_trace_action: "Root source-integration review, followed by distinct current-main landing and independent retained-audit gates."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

Claim type: bounded_theorem

Publication status: conditional-support; proposed_retained is a target, not an audit outcome. The accepted assembly and its complete mathematical cores were substantively reviewed by root at acceptance `9e5a065a63d0bc6b73c9f5a990b792f05226f7f636e841963bbc82a1703d9021`. The following assembly text retains its historical status language. Its root assembly review is complete; a separate driver-bound integration acceptance, canonical execution and later landing/audit gates remain distinct. Only the expressly required preparation-guarantee sentence has changed in that text, with an exact preserved diff. Both full proof bodies are byte-identical to the accepted sources.

This note has no external canonical mathematical dependencies. The finite-apparatus branch and PR9529 are Git ancestry only. Perfect transfer and Hamiltonian computation are attributed prior art. The theorem concerns a supplied onsite Hamiltonian, original-source/reference channel, local strength and structured precision at one declared read time. It does not derive native preparation, stopping or an interacting-chain controller.

The primary script `scripts/onsite_energy_autonomous_controller_identity_2026_10_14.py` checks source identities, extraction and publication reconstruction only: zero mathematical predicates. Historical mathematical reviews and selected numerical streams remain separate evidence. The publication packet is `.claude/science/physics-loops/toe-onsite-controller-20261014`; its EVIDENCE_MAP and PUBLICATION_EDITS identify every archived original and every canonical piece. No scientific control was rerun for publication.

# Autonomous onsite-energy source-qubit rotations with bounded local interactions

Can a static finite controller approximate a rotation of one physical source qubit while keeping the source's onsite gap and the local interaction budget fixed? In the supplied equal-gap onsite model, an explicit construction does so at one declared time. Coherent fuel supplies the source-energy change; a programmed clock routes the source out and back to its original physical factor. Accuracy is improved by increasing the number of sites, runtime, and preparation and coefficient precision.

This is a conditional theorem about an engineered Hamiltonian. Preparation of the coherent fuel, blank routing register and initial clock, fabrication of the specified local matrices, and selection of the read time are supplied resources. Their native realization is not derived.

**Status:** proposed_retained

**Claim type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Construct a bounded-resource autonomous controller on the same physical source factor in a supplied onsite-energy model."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: "Self-contained conditional onsite-energy theorem with preserved source and checks."
next_trace_action: "Root substantive review of this frozen source assembly before separate publication integration."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The construction proves a finite-qubit implication under explicit Hamiltonian-engineering, preparation, symmetry, and observation-time hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

No downstream scientific consumer is asserted yet. The exact source bodies and their reviews were accepted for bounded publication preparation in `archive/bounded_controller_prototype/ROOT_ACCEPTANCE.json`, SHA-256 `8105601f46b4aca40c277cee2ab5df248df55d29acfe2c374546ce000752be19`. That acceptance does not authorize canonical execution, a science merge, or an audit verdict. This new wrapper and its source assembly still require root substantive review.

## Current theorem and supplied model

Fix `omega>0`, a real target angle `theta`, an integer `M>=1`, and `n=|1><1|`. The source, `M` routing qubits, `M` fuel qubits, and `L+1` clock qubits all have onsite gap `omega`, where `L=3M+1`. The source/reference state is arbitrary. The independently prepared resource is the routing vacuum, `|+>` on each fuel, and one clock excitation at its initial site. The complete proof is the corrected derivation reproduced unchanged in Part I below.

Let the programmed data gates consist of an outward sequence of local swaps and excitation-preserving exchange collisions, the reverse swaps, and the final source phase. With `N_D` and `N_C` the total data and clock excitation numbers, respectively, the actual static Hamiltonian is

`H_tot = omega N_D + omega N_C + V_prog`,

`V_prog = sum_(j=1)^L lambda_j [G_j a_j a_(j-1)* + G_j* a_(j-1) a_j*]`,

`lambda_j = omega sqrt(j(L+1-j))/(L+1)`,  `a_j=|1><0|_(c_j)`.

For every source/reference density operator, the reduced output on the **original physical source** at

`T = pi(3M+2)/(2omega)`

differs from `Ad(exp(-i theta X/2)) tensor id_reference` by trace norm at most

`min(2, 5 theta^2/(2M))`.

The reference is passive and unrestricted. No global code or decoder replaces the physical source factor. Routing is exactly returned to vacuum and the clock is exactly at its terminal site at this ideal endpoint; the actual fuel can remain correlated with the source and reference.

| Resource or property | Bound and convention |
|---|---|
| Active qubits | `5M+3`, including the source |
| Geometry | A width-six square-lattice strip, embedded as `(x,y,0)` in the cubic lattice |
| Interaction range | Manhattan support diameter at most five |
| Arity | At most four qubits per grouped hopping term |
| Per-site norm sum | At most `7omega/2` in the onsite-plus-hopping decomposition |
| Positive-term decomposition | At most `6omega` per site when positive links and onsite remainders are grouped as in Part I |
| Positivity | `H_tot>=0` on the whole tensor product, including every clock-number sector |
| Runtime | `pi(3M+2)/(2omega)` |
| During evolution | No timed pulse, reset, new fuel insertion, measurement, or postselection |

These are fixed upper bounds on support and interaction strength, not uniform lower bounds on all couplings. The fixed onsite gap is **not** a uniform many-body spectral gap. On the data vacuum all programmed gates act as the identity. The one-head Hamiltonian is `omega I + K`, with `K=2omega J_x/(L+1)` for spin `L/2`, so its minimum energy is `omega/(L+1)`. The full vacuum has energy zero. Thus the full many-body gap has no positive lower bound independent of `M` from this construction.

The norm constants refer to grouped fixed-arity operators. Splitting every local matrix into Pauli monomials uses a different norm-sum convention and may introduce a fixed finite-dimensional factor; the same numerical constants are not asserted for that decomposition. The strip embedding proves finite range, not synthesis from nearest-neighbor two-body hardware or a translation-invariant microscopic law.

## Precision and actual energy accounting

The structured-error theorem retains exact onsite gaps, swaps, and the final fourth-root source phase. It allows collision-angle errors `|alpha'_j-theta/M|<=nu`, weights `0<=lambda'_j<=omega/2` with `|lambda'_j-lambda_j|<=rho`, an independent joint resource preparation error at most `eta_p` in trace norm, and observation at `T+tau>=0`. The complete source/reference error is bounded by

`epsilon_bound = 5theta^2/(2M) + 2Mnu + 4T rho + 4omega|tau| + eta_p`.

The actual primed gate blocks remain unitary and excitation preserving. Arbitrary entrywise errors, unknown gap drift, detuning, and clock-number-changing perturbations require other bounds. The same full-clock positivity and locality estimates hold for the stated structured family.

With `d_clock=2T rho+omega|tau|`, ideal preparation gives routing energy at most `omega min(1,d_clock^2)`. Imperfect preparation gives

`|Delta<E_R>| <= omega min(1,d_clock^2) + Momega eta_p`.

The extensive term cannot be removed using a source-channel bound. Every legal program prefix has at most one routing excitation; the channel-to-ledger argument combines that invariant with an energy-range bound for the imperfect preparation.

The actual energy decomposition retains source, routing, fuel, clock onsite, and programmed interaction energies. Number conservation gives

`-Delta<E_F> = Delta<E_S> + Delta<E_R>`,

while the actual uniform clock onsite energy and actual programmed interaction energy are separately conserved. For exact preparation and exact completion, routing energy is zero at both ends, clock onsite energy is `omega`, and interaction mean is zero; then `-Delta<E_F>=Delta<E_S>`. No reset, final product fuel, or independent final fuel variance is assumed.

For the ideal Hamiltonian and exact prepared resource, let `p` denote the **initial** source excitation probability. The actual total-Hamiltonian moments are

`<H_tot> = omega(p+M/2+1)`,

`Var(H_tot) = omega^2[p(1-p)+M/4+L/(L+1)^2]`.

The last term is the hopping contribution `lambda_1^2`; zero bare clock-energy variance does not mean zero coupled-controller variance. With structured primed weights and exact preparation, the initial hopping contribution is instead `(lambda'_1)^2`; a perturbed read generally has no sharp endpoint clock. At the ideal exact endpoint the equivalent final-marginal formula is

`Var(H_tot) = Var(E_S)_T + Var(E_F)_T + 2 Cov_T(E_S,E_F) + lambda_L^2`.

Here `Cov_T(E_S,E_F)=<E_S E_F>_T-<E_S>_T<E_F>_T` is real because the observables commute. Routing is vacuum. The sharp endpoint clock makes the single-hopping mixed expectations vanish and gives `<V_prog^2>=lambda_L^2=lambda_1^2`, so the displayed formula follows by expanding the remaining data-energy variance. It holds with a passive reference. It does not describe all final correlations; it retains the covariance needed for this second moment. Part II preserves the accepted endpoint clarification, including its exact one-fuel example demonstrating the error from dropping covariance.

For any desired source error `epsilon>0` and absolute fuel-ledger comparison allowance `delta_E>0`, choose

`0<epsilon_c<=min(epsilon,1,delta_E/omega)`,

`M>=max(1,15theta^2/epsilon_c)`,

`nu<=epsilon_c/(10M)`, `rho<=epsilon_c/(20T)`, `|tau|<=epsilon_c/(20omega)`,

`eta_p<=min(epsilon_c/5,delta_E/(4Momega))`.

Then the complete source error is at most `epsilon_c`; the discrepancy between actual fuel-energy loss and the target source-energy change is strictly below `delta_E`. The latter includes the routing term and does not follow from the source bound alone. For independent per-qubit preparations, errors summing to `eta_p` suffice; a uniform allowance is `eta_p/(5M+2)` per resource qubit. This sufficient joint-preparation guarantee does not follow from a fixed nonzero per-qubit error bound as the apparatus grows.

Effective selection uses computable `omega,theta` and certified scalar bounds. Rational Cayley collision approximants preserve exact unitarity and excitation number; rational dimensionless hopping approximants preserve the allowed interval. Dimensionless coefficient precision is of order `epsilon_c/M`, with order `log(M/epsilon_c)` bits per bounded coefficient, apart from effective-input computation cost. Declared read-time precision is of order `epsilon_c/omega`; computing the time requires relative gap accuracy of order `epsilon_c/M`. Preparing the resource states, implementing those coefficients, and pricing their physical preparation work or duration are supplied tasks, not consequences of computability.

## Proof and dependency roles

The central proof is self-contained finite-dimensional mathematics. It uses an exact collision-channel Taylor remainder and channel telescope, a routing-vacuum invariant, positive clock links on all sectors, an explicit spin-representation calculation, and a dressed-prefix perturbation estimate. `PROOF_OBLIGATIONS.md` maps every theorem component to the exact proof sections and reviewed sources. No unresolved lemma remains inside the stated conditional theorem; native preparation, hardware realization, and an interacting-source theorem are additional targets.

The full corrected `independent/DERIVATION.md` at SHA-256 `9db03ad2582a76131ad3d419a037988ec440636371cb8b58444ef4d4902dcd1b` is the single central proof. Its immutable original, exact section-8 repair, full review, and affected-fix review are preserved. The source's original author-status and exposure statements remain unchanged inside the reproduction; they are dated provenance, not a replacement for the current wrapper's acceptance boundary.

The root sketch, geometry, energy supplement, and their source-exposed checks are corroborating records of a parallel construction from the shared contract. Their clock sign, independent scale `J`, range 14, and robust-clock constants are not imported into this theorem. The endpoint covariance clarification supplies the explicit accounting explanation reproduced above; the same expansion applies with `J=omega` and the central proof's positive hopping convention. These records are not model-diverse or blind review. The separately sealed central author did not read the root prototypes before its original seal; later reviews and this assembly are source exposed.

There is no external canonical scientific dependency on a finite-history, kinetic-history, common-energy embedding, or interacting-chain theorem. A future stacked branch is a Git organization choice, not a mathematical premise. The prior campaign interface survey is retained only as historical motivation and exposure context. `DEPENDENCIES.json` records these roles explicitly.

Engineered perfect transfer and autonomous Hamiltonian computation are prior art. The preserved author coverage cites Christandl and collaborators' [perfect-transfer construction](https://arxiv.org/abs/quant-ph/0309131), the [expanded transfer analysis](https://arxiv.org/abs/quant-ph/0411020), and Nagaj's [local Hamiltonian computation construction](https://arxiv.org/abs/0908.4219). The spin-transfer identity and initialization requirements needed here are proved in Part I rather than imported as a black-box theorem. The literature snapshots and actual author read coverage are preserved; storing whole PDFs does not imply this assembler or the author read every section. This assembly makes no generic-clock or perfect-transfer novelty claim.

## Checks and limits

The mathematical reviews cover arbitrary references, full-clock positivity, same-source return, finite-range geometry, structured precision, and actual energy moments. The preserved numerical scripts and streams are selected floating controls. The central run uses `M=1` on the full physical clock space and `M=2` on the legal one-head sector, with orientation, return, source-phase, late-read, and interacting-bond controls. The separate root-route check uses a different entangled input and clock scale, selected geometry and scalar-clock sizes, omitted-return/orientation/clock-onsite controls, and a concrete interacting-bond example. Those values do not prove a diamond bound, an all-size theorem, or physical realization. No scientific computation was rerun during assembly, and source-identity checks evaluate zero mathematical predicates.

The exact one-bond algebra `[h_ex(S,F),-J X_S X_B]=iJ Z_S Y_F X_B` (norm `|J|`) and the swap-induced bond displacement identify a failed commuting step for the stated interacting-source substitution. They are concrete algebraic witnesses, not a universal negative theorem. This proof supplies no cancellation of that interacting evolution by the final onsite phase and does not exclude special endpoint revivals or other architectures.

The output exists at one supplied time. The clock subsequently moves; stable storage, irreversible stopping, renewal, reset, and repeated use are not established. Restricting a state to the source is mathematical partial trace. A later physical read operation has its own actual Hamiltonian-energy change and requires a separate apparatus; zero read cost is not inferred. The result does not establish a native interacting-chain controller, a kinetic joint limit, or a fault-tolerance threshold, and it adds no framework axiom or primitive.

The next operation is root substantive review of this frozen source assembly. Publication filenames, primary/helper runner registration, citation-graph integration, canonical caches, current-main gates, a publication PR, and any later independent audit belong to separate authorized work. This packet performs none of those operations.

---

## Part I: complete corrected central proof, reproduced verbatim

The following complete body preserves its original author-status, exposure, and historical execution statements. The current wrapper above identifies the later accepted source status. No part of this body has been rewritten during assembly.

# A bounded autonomous onsite-energy source-qubit prototype

**Status: proposed constructive theorem, with a complete analytic argument and selective finite controls; not independently accepted or retained.** The construction is for the supplied onsite-energy model. It does not realize the interacting Ising chain. Prepared coherent fuel, the initialized clock, and fabrication of the stated static local terms are supplied resources.

This attempt used the shared route contract, not a separate model family. No `ROOT_*` prototype file was opened before the complete body seal. The generic Feynman-clock and engineered-transfer mechanisms are prior art; the proposed contribution here is their explicit restricted geometry/source/channel/energy interface and its priced errors. This note is a scientific source record. Operational recovery remains the campaign `STATE.yaml`/`HANDOFF.md`.

## 1. Sources, exposure, and statement

The complete initial local sources read were `../CONTRACT.md`, SHA-256 `c50d637b12c9aa61c496c6d8e95b5cabfb86eef938f63434ec3f664db8820d24`, and `../../next_physical_interface/REPORT.md`, SHA-256 `ee6082a2abe873c9c832bdd15caed3ac2569850a38a60210154ef38ecd60ca4a`. The independent route plan was sealed before the external full-text reading and numerical run at SHA-256 `b7fb09e963da56f0855ac1e60d2cf86c9b363f59989e3f47bda7a327e34da10a`. Previous finite-chain/publication source exposure by this worker is disclosed there; it is not erased by the present task.

Primary source coverage is recorded in `LITERATURE_IDENTITIES.json`, with complete PDF snapshots and text extractions. The full scientific main text of [Christandl et al., *Perfect state transfer in quantum spin networks*](https://arxiv.org/abs/quant-ph/0309131), especially equations (12)-(15), supplies the known square-root path/spin-rotation mechanism. Sections VIII-IX of [the expanded state-transfer paper](https://arxiv.org/abs/quant-ph/0411020) explicitly distinguish fixed maximum coupling from fixed transfer time. Section II/II.A of [Nagaj, *Local Hamiltonians for Universal Quantum Computation*](https://arxiv.org/abs/0908.4219) gives the pulse-clock history subspace and its initialization qualification. No railroad-switch, randomized-readout, ground-state initialization, or fault-tolerance theorem is imported. The needed clock identity is proved directly below; other sections of the last two papers were not fully reviewed.

Fix a physical source qubit `S` with bare Hamiltonian `omega n_S`, `omega>0`, `n=|1><1|`, and a target angle `theta` in radians. Every fuel, routing and clock qubit in the construction also has onsite gap `omega`. Units have `hbar=1`. For each positive integer `M`, there is a time-independent Hamiltonian on `5M+3` explicitly placed qubits satisfying:

* `H_tot>=0` on the entire tensor-product Hilbert space, including illegal clock sectors;
* interaction arity at most four, diameter at most five in the ambient square lattice's Manhattan metric, and per-site interaction norm at most `7omega/2` in the onsite-plus-hopping decomposition;
* no pulse, insertion, reset, measurement or postselection during evolution;
* at the declared time `T=pi(3M+2)/(2omega)`, the original source factor is the output, the routing qubits are exactly blank again, and the initialized clock is at its terminal site;
* for every source/reference density operator, after tracing the other qubits,

    ||(C_M tensor id_R)(rho_SR)
        -(U_theta tensor I_R)rho_SR(U_theta* tensor I_R)||_1
       <= min(2,5 theta^2/(2M)),                 (1)
    U_theta=exp(-i theta X/2).

The reference is arbitrary and is untouched. The bound is a complete channel bound, proved analytically rather than inferred from a maximally entangled test. The runtime grows with `M`; the source gap is never slowed or rescaled. A single terminal-time output is proved, not autonomous stopping or indefinitely stable storage. Structured static fabrication, timing and resource-preparation errors are priced in section 7.

## 2. The coherent-fuel collision bound

For one source/work qubit and one fuel qubit define

    h_ex=|10><01|+|01><10|=(X tensor X+Y tensor Y)/2,
    V_alpha=exp(-i alpha h_ex),
    eta=|+><+|,  |+>=(|0>+|1>)/sqrt(2).

Then `||h_ex||=1`, `[h_ex,n_S+n_F]=0`, and its fuel expectation is `h_eff=X/2`. Let `Phi_alpha(rho)=Tr_F V_alpha(rho tensor eta)V_alpha*`. For any passive reference, the first derivative at zero is `-i[X/2,rho]`. The two second-order remainders are bounded by

    ||Phi_alpha-id-alpha L_eff||_diamond <= 2 alpha^2,
    ||Ad(exp(-i alpha X/2))-id-alpha L_eff||_diamond
       <= alpha^2/2.                            (2)

For completeness, twice differentiating the first unitary channel inserts two commutators with `h_ex`; their complete trace-norm bound is `4||h_ex||^2=4`. Integrating the Taylor remainder gives `4|alpha|^2/2`. Adding a fixed state and tracing it out are complete contractions. For `X/2`, the corresponding bound is one, giving the second line. The same integral argument holds for negative alpha. This proves the one-step difference at most `5alpha^2/2` for all references.

Use `M` independently prepared fuel qubits, each used only once, with `alpha=theta/M`. All are physically present at the start. Tracing them mathematically after their last interactions is equivalent to tracing them all at the end; it is not a physical reset. The channel telescope, using complete contractivity of every channel, gives (1). At each subsequent collision, previous fuel correlations can be retained as reference systems in this estimate; no reset or factorization of the final fuel is assumed.

As an explicit orientation check, the one-collision Kraus operators in the computational basis are

    K_0=(1/sqrt(2)) [[1,0],[-i sin(alpha),cos(alpha)]],
    K_1=(1/sqrt(2)) [[cos(alpha),-i sin(alpha)],[0,1]].     (3)

Their first-order generator is `-i[X/2,.]`, not its opposite.

## 3. Local source transport and exact return

Let `r_0=S`, let `r_1,...,r_M` be routing qubits initially in `|0>`, and let `f_1,...,f_M` be the coherent fuel. There are `2M+1` data qubits altogether. Define a circuit list of length `L=3M+1`:

1. For `j=1,...,M`, apply `SWAP(r_(j-1),r_j)`, then `V_alpha(r_j,f_j)`.
2. For `j=M,...,1`, apply `SWAP(r_(j-1),r_j)`.
3. Apply `P_S=exp(+i omega T n_S)` on the original source.

Every gate `G_j` commutes with the total data number `N_D=n_S+N_R+N_F`. After each forward swap, the unknown work state, including all its correlations, occupies `r_j`; the already passed routing factors are blank. The reverse swaps return that entire work factor and its correlations to `r_0`. Every routing factor is then exactly blank. This follows as an identity on the initial routing-vacuum subspace, with no restriction on the source/reference vector or on fuel correlations created by earlier collisions.

Before the last phase gate, the resulting data unitary on that subspace is therefore equivalent to the ordered collisions `V_alpha(S,f_M)...V_alpha(S,f_1)`, with identity on the routing vacuum. This equivalence is used for calculation only: the physical circuit actually transports and returns the source by local swaps. There is no global output decoder or redefinition of which physical qubit is the source.

The clock below has `T=pi(L+1)/(2omega)`. Consequently `omega T=pi(L+1)/2`, and `P_S=diag(1,i^(L+1))` is just a fixed fourth-root phase. Its coefficient can be exact in this architecture. This choice avoids an unpriced fine phase proportional to a large time; the timing uncertainty itself is still charged below.

## 4. The static Hamiltonian, positivity and geometric placement

Use `L+1` additional clock qubits `c_0,...,c_L`. Let `a_j=|1><0|` on `c_j`, let `N_C=sum n_(c_j)`, and set

    lambda_j=omega sqrt(j(L+1-j))/(L+1),  j=1,...,L,
    0<lambda_j<=omega/2,
    V_prog=sum_j lambda_j [G_j tensor a_j a_(j-1)*
                         +G_j* tensor a_(j-1) a_j*],
    H_tot=omega N_D+omega N_C+V_prog.             (4)

Clock and data factors in each summand are disjoint. These are specified static three- or four-qubit operators, not externally supplied instantaneous gates during the run. Arbitrary fixed-arity local Hamiltonian engineering of these matrices is an explicit premise; no reduction to two-body nearest-neighbor hardware is claimed.

**Positivity is global.** Put `lambda_0=lambda_(L+1)=0`. For any data unitary `G_j`,

    lambda_j [n_(c_(j-1))+n_(c_j)
       +G_j a_j a_(j-1)*+G_j* a_(j-1) a_j*] >=0.       (5)

In clock sectors `00` and `11` this is zero or `2lambda_j I`; in the one-excitation block it is `lambda_j [[I,G_j*],[G_j,I]]`, with eigenvalues zero and `2lambda_j`. Therefore `omega N_C+V_prog` is the sum of (5) and the positive onsite remainders `(omega-lambda_j-lambda_(j+1)) n_(c_j)`. Adding `omega N_D` proves (4) positive on all states. The all-zero tensor product has energy zero, so this is not an accuracy-dependent global scalar shift. Preparation of a nonzero clock head is separately supplied.

Here is an explicit embedding in the square lattice. All coordinates are distinct:

| Qubit | Coordinate |
|---|---|
| `r_j`, `0<=j<=M` | `(j,0)` |
| `f_j`, `1<=j<=M` | `(j,1)` |
| `c_0` | `(0,3)` |
| `c_(2j-1)`, `1<=j<=M` | `(j,2)` |
| `c_(2j)`, `1<=j<=M` | `(j,3)` |
| `c_(2M+M-j+1)`, `j=M,...,1` | `(j-1,4)` |
| `c_L=c_(3M+1)` | `(0,5)` |

Forward swaps/collisions follow the two zigzag clock rows; reverse swaps follow row four; the final phase is next to the original source column. Each hopping support consists of its two clock qubits and at most two data qubits. Directly from the table, every support has Manhattan diameter at most five. The final three-site phase support reaches height five; reverse-swap supports have horizontal span one and vertical span four. Thus this is geometric locality, not only a bound on arity.

The norm of an individual hopping summand is `lambda_j`. Every interior routing site appears in at most four swaps and one collision, every fuel site in one collision, the original source in two swaps and one phase, and a clock site in at most two hoppings. Including its onsite term gives

    sup_x sum_(X containing x) ||h_X|| <= 7omega/2.      (6)

The constants in arity, diameter and (6) are independent of `M`, theta and accuracy. The ambient lattice has degree four; the occupied strip has fixed width. If one insists that each displayed local term itself be positive, use decomposition (5): a conservative per-site bound becomes `6omega`, still independent of `M`. The onsite-plus-hopping decomposition is the one used in (6).

## 5. Deterministic clock completion and the source free phase

The initial clock is the product state `|C_0>=|10...0>`. Clock number is conserved. In its one-head sector write `|j>` for the head at `c_j` and `W_j=G_j...G_1`, `W_0=I`. The unitary

    D=sum_(j=0)^L W_j tensor |j><j|

conjugates the scalar path adjacency `K=sum lambda_j(|j><j-1|+|j-1><j|)` to `V_prog`. This is an identity on the whole data space tensored with the one-head space, not merely one selected input history.

In the spin `J=L/2` representation,

    K=(2omega/(L+1)) J_x,
    exp(-i T K)|0>=(-i)^L|L>,
    T=pi(L+1)/(2omega).                            (7)

One direct proof identifies the extreme spin states with all-down/all-up states in the symmetric subspace of `L` spins. Rotation by pi about x flips every constituent spin and contributes `-i` per spin; the offdiagonal matrix elements are the square roots in (4). Thus (7) is deterministic. There is no terminal clock postselection, randomized observation or uncharged repetition probability.

Moreover `[N_D,V_prog]=[N_C,V_prog]=0`, because every programmed gate preserves total data number. Consequently on the initialized one-head sector,

    exp(-i T H_tot)(|psi> tensor |C_0>)
      =e^(-i omega T)(-i)^L
         e^(-i omega T N_D) W_L |psi> tensor |C_L>.     (8)

The source phase in `W_L` cancels exactly the factor `exp(-i omega T n_S)`. With the routing vacuum restored, the full final state, omitting a global phase, is

    (I_SR tensor e^(-i omega T N_F))
      C_coll (rho_SR tensor eta_F) C_coll*
    (I_SR tensor e^(+i omega T N_F))
       tensor |0...0><0...0|_Rout tensor |C_L><C_L|,   (9)

where `C_coll=V_alpha(S,f_M)...V_alpha(S,f_1)`. Tracing fuel proves that the actual source channel is exactly `Phi_alpha^M`, hence (1). Formula (9) also retains all source/fuel/reference correlations. In particular it does not claim that the fuel returns to a product or initial state.

The clock will generally move again after `T`, and later evolution can undo the computation. This is a timed one-use output. No stopping, repeated-use or memory-stability result follows from the endpoint identity.

## 6. Exact actual energy ledger

Define actual energies in the supplied implementation:

    E_S=omega n_S, E_R=omega N_R, E_F=omega N_F,
    E_C=omega N_C, E_V=V_prog,
    H_tot=E_S+E_R+E_F+E_C+E_V.

For every initial state, not just an ideal resource preparation, the exact unitary evolution satisfies

    Delta(E_S+E_R+E_F)=0,
    Delta<E_C>=0,
    Delta<E_V>=0,
    Delta<H_tot>=0.                               (10)

The first line is shorthand for conservation of the expectation of the summed operator; the corresponding operator commutators vanish. In particular, conservation of `E_V` follows from its commutation with both number terms, not from ignoring interaction energy.

For the exact initialized resource and exact time (7), `E_R` is zero at both endpoints, `<E_C>=omega`, and `<E_V>=0` initially and finally. The latter initial value follows from orthogonal head positions in every hopping term. Therefore the actual endpoint ledger is

    -Delta<E_F>=Delta<E_S>,
    Delta<E_R>=Delta<E_C>=Delta<E_V>=0.             (11)

The fuel may lose or gain energy depending on the unknown input and target rotation. Its capacity is `Momega`; its initial mean is `Momega/2` and initial variance `Momega^2/4`. It supplies coherence as well as energy. The clock's initial bare energy is `omega` with zero bare-energy variance; it is not its bare onsite energy that changes in (11).

For source excitation probability `p`, independent of the prepared resources, the initial total energy and variance are explicitly

    <H_tot>=omega(p+M/2+1),
    Var(H_tot)=omega^2[p(1-p)+M/4+L/(L+1)^2].       (12)

Indeed the initial hopping variance is `lambda_1^2=omega^2 L/(L+1)^2`; all cross expectations with a single hopping vanish at `C_0`. This distinguishes clock onsite energy from the full generator's energy spread. A passive reference does not change these system moments.

For an imperfect completion, retain routing energy in the exact ledger:

    -Delta<E_F>=Delta<E_S>+Delta<E_R>.              (13)

Discarding that term is not justified by a small source-channel error alone. Section 7 gives an explicit residual bound for this architecture. Final source/fuel correlations are never discarded in (10)-(13).

These are pre-read endpoint statements. Taking a reduced output is a mathematical restriction, not a physical energy-consuming measurement. If an actual terminal read channel `R_read` is applied to the implemented system, its energy change is explicitly

    W_read=Tr H_tot [R_read(sigma_T)-sigma_T],
    Delta<H_tot> including that intervention = W_read. (14)

No apparatus for an arbitrary read, zero read work, reset work, heat cost or autonomous clock for selecting the observation time has been supplied. The contract permits this one declared physical observation time; (14) prevents conflating that permission with a free arbitrary measurement.

## 7. Static precision, timing, preparation and ledger tolerances

Use an actual structured fabrication with:

* exact onsite gaps `omega`, exact swaps and exact fourth-root source phase;
* collision angles `alpha'_j` with `|alpha'_j-theta/M|<=nu`;
* real hopping weights `0<=lambda'_j<=omega/2` and `|lambda'_j-lambda_j|<=rho`;
* resource state, independent of the source/reference, within trace norm `eta_p` of the specified routing/fuel/clock product;
* observation at `T+tau>=0`.

Every such static Hamiltonian is still positive and satisfies the same locality bounds and exact conservation identities (10). The structured qualification matters: arbitrary independently rounded matrix entries need not define a unitary gate or preserve number. It is not silently assumed that unstructured fabrication errors conserve energy.

There is an explicit complete source-channel error bound

    error <= 5theta^2/(2M) + 2M nu + 4T rho
                         +4omega|tau| + eta_p.      (15)

Here are the estimates behind it. For the one-head clock, use the dressed basis for the actual gates. Changing the weights by at most `rho` changes the scalar path operator by norm at most `2rho`, by its maximum absolute row sum. At time `T` the clock vector changes by at most `2T rho`. The actual path norm is at most `omega`, so shifting the read time changes it, up to an irrelevant clock onsite phase, by at most `omega|tau|`. A Stinespring-vector norm error `d` produces complete reduced trace error at most `2d`. The complete circuit gate difference is at most `sum_j |alpha'_j-alpha|<=Mnu`; the swaps and final phase are exact. Finally, the remaining source free rotation at the actual time is `exp(-i omega tau n_S)`, whose complete channel difference from identity is at most `2omega|tau|`. Fuel free phases vanish under the final trace. Resource-state trace error contributes at most `eta_p`, for all source/reference inputs. These arguments prove (15), including the timing term, without a system-size factor from the full bare data energy.

Let

    d_clock=2T rho+omega|tau|,
    p_leak<=min(1,d_clock^2).                       (16)

With ideal prepared resources and the structured gate errors, the output is a sum of actual partial-program states labelled by orthogonal head positions. Every partial program has at most one routing excitation: the work occupies one routing factor or has returned to the source. At the terminal head position the routing register is blank. Therefore

    <E_R(T+tau)> <= omega p_leak.                   (17)

The bound also holds when the source has a passive reference. For preparation error `eta_p`, a conservative bound comparing the actual initial and final routing energies is

    |Delta<E_R>| <= omega p_leak+Momega eta_p.      (18)

This follows by applying the trace-norm energy bound at both endpoints; it does not assume the imperfectly prepared routing register starts exactly blank. All actual energies still obey (13).

If the right side of (15) is `epsilon_c`, the source energy change differs from the target rotation's energy change by at most `omega epsilon_c/2`: subtract `omega I/2` from the source energy observable when bounding a trace-zero state difference. Thus

    | -Delta<E_F> - Delta E_source,target |
       <= omega epsilon_c/2 + omega p_leak
                                  +Momega eta_p.   (19)

A channel-error allowance alone does not make an extensive preparation-energy error negligible; the last term is explicitly paid.

For `0<epsilon_c<=1`, choose an integer `M>=max(1,15theta^2/epsilon_c)` and, for example,

    nu<=epsilon_c/(10M), rho<=epsilon_c/(20T),
    |tau|<=epsilon_c/(20omega), eta_p<=epsilon_c/5.  (20)

Then (15) is at most `epsilon_c`. To additionally achieve any absolute fuel-ledger comparison tolerance `delta_E>0`, take `epsilon_c<=min(epsilon,1,delta_E/omega)` and strengthen preparation to

    eta_p<=min(epsilon_c/5,delta_E/(4Momega)).       (21)

With (20), `p_leak<=9epsilon_c^2/400`; equations (19)-(21) then give a ledger discrepancy strictly below `delta_E`. The identity (13) is exact regardless of these comparison tolerances.

These fabrication requirements are effective under computable `omega,theta` and certified scalar bounds. A certified integer upper bound can replace an undecidable exact real ceiling. Exact finite-description unitary collision approximants are available by taking rational `r` and using, on the one-excitation block, `(I-irX)(I+irX)^(-1)`, with identity on `00,11`; its angle is `2 arctan(r)` and its entries are rational complex numbers. Take a sufficiently fine rational `r` near `tan(alpha/2)` for the small angles in (20). Hopping coefficients can be rationally approximated and clipped to the allowed interval; rational multiples of the supplied gap can be used. Thus the qualification above is a constructive precision model, not an assumption that every rounded matrix remains unitary.

The resource count is `5M+3` qubits and `L=3M+1` hopping terms, on an `O(M)`-long strip of width six. Runtime is `T=pi(3M+2)/(2omega)`. Required dimensionless coefficient precision is of order `epsilon_c/M`; read-time precision is of order `epsilon_c/omega`. Apart from the effective-input computation cost, `O(log(M/epsilon_c))` precision bits per bounded static coefficient suffice, with fixed-size local matrix descriptions; the total program description has `O(M)` such coefficients. Computing that declared time requires a certified value of the supplied gap with relative accuracy of order `epsilon_c/M`. Unknown physical gap drift is outside the exact-onsite structured model above. These are explicit prototype costs, not an efficiency claim for the interacting-chain compiler.

There are `5M+2` supplied resource qubits excluding the unknown source. If their preparations are independent with individual trace errors whose sum is at most `eta_p`, the required joint preparation estimate follows by a tensor-product telescope. A uniform individual allowance `eta_p/(5M+2)` suffices. Equations (12), (20) and (21) price energy/coherence inventory and preparation precision; a native physical procedure, work cost or duration for preparing those pure states is not derived. Arbitrary unstructured local perturbations require their own norm/leakage and energy ledger bounds and are outside the structured guarantee (15).

## 8. The exact failed transfer to the interacting chain

The construction's load-bearing identity is `[H_D,G_j]=0` for every programmed gate, with `H_D=omega N_D`. It lets the source free evolution factor out in (8), lets the phase correction remain one-site, and yields the independent energy ledger (10).

Replacing that energy by an interacting Ising energy does not preserve this identity. Consider one actual chain bond `-J X_S X_B` adjacent to the source and an external same-gap fuel `F`. Then

    [h_ex(S,F), -J X_S X_B] = iJ Z_S Y_F X_B !=0.   (22)

The sign follows from `[Y,X]=-2iZ`; the norm is `J`. Likewise a swap between `S` and an external router `r` conjugates that bond to `-J X_r X_B`. The operator difference has norm `2J`, so the swap does not commute with the unchanged interacting-chain Hamiltonian, even if it preserves the onsite energies.

Consequently, in the dressed history basis, the actual chain energy becomes the clock-dependent operator `W_j* H_chain W_j`, rather than a common operator commuting with the path adjacency. The scalar perfect-transfer reduction with the free factor in (8) is then unavailable. Transporting the source state does not transport or disable the physical chain bonds. This proof supplies no cancellation of that interacting evolution by the final onsite phase. A global energy diagonalization would not preserve the stipulated original physical source factor or price a local decoder; it is not a repair supplied here.

These are precise failed steps for this route and source identification. The note does not prove that no other controller, engineered compensation, allowed clock architecture or model-specific construction can work for the interacting chain. It introduces no new physical axiom and no universal negative theorem.

## 9. Actual selective controls, failures retained, and remaining review

One actual run of `selective_controls.py` was performed at `2026-10-14T03:49:28Z`, after the plan seal. The script builds the Hamiltonian directly from local clock-gate terms, not by conjugating an already diagonal clock and assuming the result. It imports no scientific source or `ROOT_*` file. Script SHA-256 is `6d660e7d1a74b90310d45b6d72271aa1ec24ebf1b3517439dd0cd2008a5e4f08`; full stdout SHA-256 is `cdad7fe8fd5d4982ba6d5ba2ffd3f80932bf5f9eebeaddb847e6f3793da11fea`. The process exited zero; stderr is empty. `run01/RECEIPT.json` preserves command, timing and hashes. No failed executable run was hidden or retried.

At `theta=0.4`, `omega=1`, the `M=1` control used the entire 256-dimensional physical Hamiltonian, including all clock sectors; its smallest eigenvalue was zero. `M=2` used the explicit invariant one-head sector, also dimension 256, and is not a full-sector numerical positivity check. Autonomous-to-circuit operator errors were about `2.0e-15` and `4.0e-15`. The source/reference Choi errors against the exact finite collision channel were below `1.8e-15`. Against the desired rotation they were approximately `0.07894` and `0.03948`, below the analytic all-reference allowances `0.4` and `0.2`. These Choi numbers are selected witnesses, not numerical diamond-norm certificates.

The following controls detect consequential failures:

* Reversing collision orientation produced source/reference defect about `0.77884`; omitting the return produced `1.58443`; omitting the source free-phase correction produced `1.41421`, all compared with the intended finite collision channel.
* For `M=1` with a ground-state source, actual source energy rose by `0.0758233`, fuel energy fell by the same amount, and endpoint routing, clock and interaction changes were zero to the stated numerical tolerance. Final source/fuel nonproduct trace distance was about `0.42300`.
* A late read by `0.4/omega` retained routing energy about `1.83187e-5`; the full ledger still closed. Dropping routing from the late-read ledger would be an actual error.
* Support enumeration at `M=1,2,10,100` found diameter at most five, arity four, and at most five hopping terms per site. The all-`M` claims come from the coordinate/count proof in section 4, not these samples.
* A three-qubit Ising-bond control at `J=0.3` gave commutator norms `0.3` for the exchange and `0.6` for the swap, matching the route failure (22).

The omitted-return, omitted-phase and reverse-orientation constructions are retained named failed variants. A bare weighted graph Laplacian was also deliberately not substituted for (4): its varying diagonal degrees generally alter the engineered adjacency and do not inherit (7). The constant onsite clock offset and positive remainder construction avoid that unsupported replacement. No general Laplacian impossibility is asserted.

The remaining obligation is separate mathematical review of this complete same-family prototype, especially the structured-error/routing-energy estimates and the original-factor interface. Finite controls and primary prior art do not constitute that review. No interacting-chain realization, native microscopic identification, autonomous preparation, fault-tolerance threshold, irreversible record, heat/renewal law, or retained audit status is established. No original source, Git state, publication package, canonical driver, axiom, audit or editable prompt was changed; all writes are under `independent/`.

---

## Part II: accepted endpoint-covariance clarification, reproduced verbatim

This supporting record concerns the parallel root construction. Its covariance expansion is stated and derived for the central construction in the wrapper. Its separate robust-clock norm constants remain scoped to that root variant.

# Endpoint variance clarification

This addendum clarifies the root supplement `ROOT_TOTAL_ENERGY_AND_PRECISION.md`, SHA-256 `f35e8ea0c1fadcc21429b5de3030f388cde31a98774043a58f13179188d75b73`. The sealed source remains unchanged. It follows the source-exposed supplement review `b9a59cceaa4d6ebe5042dd6dd13ca3ffa8272dbacc0965d93929beb65bb3527e`; it is not a blind independent result.

The population `p` in the conserved total variance formula always denotes the **initial** source population. The sentence “At the other endpoint j_L=j_1 and the same variance identity holds” preserves that initial-data formula by energy conservation. It must not be interpreted as assuming a final product of source and fuel, or as replacing `p` by the final source population while retaining independent-fuel variance.

For the ideal exact endpoint, the equivalent formula using final marginals is

    Var(Htot) = Var(H_source)_T + Var(H_fuel)_T
                + 2 Cov_T(H_source,H_fuel) + j_L^2.

The routing factor is exactly vacuum there. The clock is an endpoint basis state, so all mixed expectations of its hopping with clock-diagonal data operators vanish. Thus the displayed covariance accounts for all source/fuel correlations, including when the source initially has a passive reference. Since `H_source` and `H_fuel` commute, the covariance is real and is defined as their product expectation minus the product of expectations.

For a source initially in its ground state, one fuel qubit in `|+>`, and collision angle `pi/4`, the final joint number probabilities are `P00=1/2`, `P01=P10=1/4`, `P11=0`. Both marginal variances are `3 omega^2/16`; the covariance is `-omega^2/16`. Their sum with twice the covariance is `omega^2/4`, the correct conserved data-energy variance. Discarding that covariance would give the incorrect `3 omega^2/8`.

The optional robust clock with onsite coefficient `2J` and adjacent nonnegative weights summing to at most `2J` remains positive. Its per-site norm estimate must use those enlarged coefficients; the original ideal norm constant is not asserted for that family. The source-exposed review gives conservative constants `omega+20J` for a data site and `4J` for a clock site. Both are independent of the number of collisions. This does not alter the separately derived independent prototype, whose own structured weights and norm bounds are stated explicitly.

No new numerical execution, native construction, general detuning estimate, stopping mechanism or interacting-chain result is claimed by this clarification.
