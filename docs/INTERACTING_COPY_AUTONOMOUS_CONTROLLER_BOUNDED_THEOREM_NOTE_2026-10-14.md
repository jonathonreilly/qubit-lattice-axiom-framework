---
title: "Autonomous control of a supplied interacting source by finite copies"
claim_id: interacting_copy_autonomous_controller_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
status: proposed_retained
upstream_dependencies: []
runner: scripts/interacting_copy_autonomous_controller_identity_2026_10_14.py
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Construct an autonomous original-source controller for a supplied finite interacting-copy model with explicit locality, precision and actual energy accounting."
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Self-contained conditional finite-chain construction with supplied copies, engineering, preparation, effective data and terminal-time access."
next_trace_action: "Separate root source-integration review, followed by distinct current-main landing and independent retained-audit gates."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

Claim type: bounded_theorem

Publication status: conditional-support; proposed_retained is a target, not an audit outcome. Root accepted the complete source assembly at `34aeefd1f5c1936c5add76f06ee523d2095df221f68113f7291bece3687f8c5e`. The following assembly text and all three complete proof bodies are unchanged, including historical status sentences. Its root substantive assembly review is complete. Separate driver-bound integration acceptance, canonical execution and later landing/audit gates remain distinct; the earlier acceptance authorizes source preparation only.

This is a self-contained new scientific root with zero external canonical mathematical dependencies. The onsite-controller branch and PR9531 are Git ancestry only. The supplied interacting-copy theorem includes original-source return with arbitrary references, a positive full-clock Hamiltonian, engineered six-qubit finite-range interactions, explicit exponential resources and actual energy accounting. The broad copy-mismatch/nonunitary-block estimate and the narrower exact-copy/unitary-block fresh-fuel ledger retain different hypotheses. The history application is excluded. Native preparation, stopping, readout/reset and persistent storage remain unresolved.

Supplied-copy partial swaps, Hamiltonian computation and perfect transfer are attributed prior art. The primary script `scripts/interacting_copy_autonomous_controller_identity_2026_10_14.py` checks source identities, extraction and reconstruction only: zero mathematical predicates. Historical scientific reviews and the three actual selected control executions retain their separate scopes and exposure records. The publication packet is `.claude/science/physics-loops/toe-interacting-controller-20261014`; its EVIDENCE_MAP and PUBLICATION_EDITS bind every archived original and every canonical piece. No scientific control was rerun for publication.

# Conditional autonomous control of an interacting source by supplied copies

A static finite controller can approximate any supplied computable unitary on the original physical finite chain, including arbitrary passive references, when identical interacting copies, prepared resources and the specified local compensation terms are supplied. Sequential swaps move the source through fresh fuel copies and then return it. Clock-conditioned crossed bonds compensate the actual energy change at the moving cut; the construction does not assume the uncompensated onsite factorization works for an interacting source.

This is conditional support for an explicitly engineered Hamiltonian. Its interactions can involve six qubits at fixed finite range, and its sufficient resources grow exponentially with chain length. Preparation, coefficient control and access at the terminal time are premises. Native supply, preparation dynamics, readout/reset, stopping and stable storage are not derived. The separately developing history application is excluded.

**Status:** proposed_retained

**Claim type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Construct an autonomous original-source controller for a supplied finite interacting-copy model with explicit locality, precision and actual energy accounting."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: "Self-contained conditional controller source assembly, with two separately scoped analytic supplements."
next_trace_action: "Root substantive review of this exact assembly before separate publication preparation or canonical integration."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A finite-dimensional construction under explicit copy, engineering, preparation, effective-data and observation-time hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Root accepted the three exact bodies at `ROOT_CONTROLLER_SOURCE_ACCEPTANCE.json`, SHA-256 `676a5f6e420a0cce54e20a08fd82b8cba953298c41688daaa247c4ac0e1aec93`, after the complete root and separate source-exposed reviews. The current source is 40,756 bytes and 329 lines; the earlier 298-line inventory was corrected in a preserved addendum. This acceptance permits source-only assembly and expressly excludes publication execution, retained audit, native realization and the history application. This new wrapper still needs root review. The three complete bodies below retain their original historical status sentences verbatim; those sentences are dated provenance, not a new acceptance decision.

## Exact model, output and resources

Supply an open `n>=1` qubit chain with ordered local matrices

`H_A=sum_k h_k+sum_k v_(k,k+1)>=0`, `||h_k||<=u`, `||v_(k,k+1)||<=b`,

and a certified computable bound `E>=||H_A||`. Any constant shift is charged identically in each copy's local terms and its actual energy moments. Noncommuting adjacent terms are allowed. Uniform local-strength claims across a family require uniformly bounded actual local terms. The target `U` is a supplied computable unitary on the entire original chain, and every channel estimate includes an arbitrary passive reference.

Use `M` router chains, `M` fuel chains, `n` dual-rail work pairs per collision and `L+1` clock qubits. The routers are supplied in a stationary pure state `|r>` of `H_A`, with an effective description sufficient for preparation; no uniform exact eigenvector selector at a degeneracy is assumed. Work pairs start in `|10>`, the clock starts at its initial site, and the ideal resources are independent of the source/reference. Set `C=4b`, choose `J>0` and work gap `omega_w>0`, and write `c=C+J`.

A partial sitewise swap of two identical chains changes their summed Hamiltonian only at the current cut. Its correction is the sum of two crossed bonds minus the two original bonds, has support on at most four data qubits, and has norm at most `C`. A controlled cut adds the occupation projector of the current work rail. The complete prefix identity holds on the entire physical work space, including the intermediate half transport of a dual-rail control and illegal encoded states. Completed sweeps commute with the bare sum; only the current incomplete sweep contributes a cut.

The physical collision uses `6n+1` elementary gates. The full route and reverse return give

`L=M(8n+1)`, `N=n+12Mn+M+1`, `T=pi(L+1)/(2J)`.

The `4n+3` count in the original proposal treated pair transport as one gate and is not the physical count used by the theorem. The `n=1` case has no cut or rail transport and still has `L=9M`.

With `H_0` the positive sum of the actual ideal chain-copy and work energies, the exact static controller is

`H=H_0+sum_(j=0)^L n_(c_j) Delta_j+cN_C+sum_(j=1)^L a_j[clockhop_j G_j+adjoint]`,

`Delta_j=W_j H_0 W_j*-H_0`, `a_j=J sqrt(j(L+1-j))/(L+1)`.

All terms are physical tensor-product operators. Positive two-clock link decompositions and `||Delta_j||<=C` prove `H>=0` on every clock-number and work sector. On the invariant one-head sector, prefix conjugation gives exactly `H_0+cI+K`, with `K=(2J/(L+1))J_x`. At `T`, the clock transfer amplitude is `(-i)^L`, and the physical endpoint data operation is `W_L exp(-iH_0 T)` up to the global clock phase. This is a statement about the actual compensated Hamiltonian.

The original source sites remain `(k,0,0)`. The explicit cubic-lattice embedding has a proved support-diameter bound 241 and an advertised conservative bound 400. Compensation terms have arity at most six; hopping terms have arity at most five. The grouped-term per-site norm sum is bounded by

`B=(u+2b)+omega_w+4J+20C`.

The active count and containing region are `O(nM)`. These constants use the source's grouped operators and explicit incidence counts. No nearest-neighbor two-body, translation-invariant or native hardware synthesis is inferred. Adding uncoupled spectator sites requires their own stated preparation and energy accounting. No uniform many-body spectral-gap guarantee is established.

The completed swaps return the unknown source and all its correlations to the **original physical chain**. Every ideal router and work factor returns. The source is not relabeled and no global decoder is used. The exact reduced channel is free evolution `Ad(exp(-iH_A T))` after the repeated whole-copy partial-swap collision channel. Final fuel correlations are retained.

## Effective target-dependent fuel and complete error

Let `d=2^n`, `Theta=4pi d` and `alpha=Theta/M`. The complete partial-swap Taylor estimate and channel telescope give

`||Phi_(Theta/M,sigma)^M-Ad(exp(-iTheta sigma))||_diamond<=min(2,4Theta^2/M)`.

This bound covers arbitrary passive references and signed collision angles; a small Choi witness is not its proof. All fuel copies are present initially, and intermediate mathematical partial traces do not imply physical resets.

Choose `M` from the error budget first, then `L,T`, then `V=exp(+iH_A T)U`. A finite separated set of candidate spectral cuts contains one with certified clearance. Singular-value enclosures find such a cut without deciding a computable-real equality or choosing eigenvectors. A Cayley transform and a controlled arctangent integral then compute a centered Hermitian `K` with `||K||<2pi` and `exp(-iK)` equal to `V` up to phase. The density matrix

`sigma_M=(I+K/(4pi))/d>=I/(2d)`

therefore cancels the actual source free phase. Runtime is fixed before this state is selected; it does not depend on a state-preparation algorithm's duration. The strict positivity margin permits certified finite state descriptions. Physical preparation, copies and synthesis remain supplied resources.

For the exact model, `M=O(4^n/epsilon)`, active qubits `O(n4^n/epsilon)` and time `O(n4^n/(J epsilon))` suffice. The input matrices can already have order `4^n` entries. These are explicit resource upper bounds, not efficient-implementation or preparation-cost claims.

## Two distinct fabrication and preparation classes

The main proof and the fresh-fuel supplement use different implementation hypotheses. The supplements' narrower ledger must not be transferred to the main proof's broader error class.

| Property | Main proof, Part I sections 6–7 | Structured fresh-fuel supplement, Part III |
|---|---|---|
| Bare source | Original `H_A` remains exact | Original `H_A` remains exact |
| Other bare copies | Positive local mismatches allowed, with certified total difference `Z` and actual local norm bounds | `H_0` and copies remain exact |
| Hopping blocks | `B_j=a'_j G'_j+E_j`, `norm(E_j)<=chi`; `B_j` need not be unitary or preserve work number | Actual `G'_j` are unitary on their declared supports |
| Corrections | Hermitian same-support approximants, error `delta`, exactly zero at both endpoints | Self-adjoint same-support errors `zeta`, possibly at endpoints |
| Clock padding | `C+delta+J+2chi` pays the general block norms | `C+J+zeta` uses actual unitary blocks and clipped weights |
| Preparation | Joint resource error `eta` relative to the nominal ideal product; source/reference independent | Actual independent fresh fuels `tau_i` held fixed in the comparator; joint nonfuel error `eta` independent of fuels/source |
| Actual fuel-change comparison | Extensive residual bound using `K_1`, `K_all` and the full actual ledger | `W(epsilon_0+M xi)/2` for the same actual initial fuels |

In Part I, put `kappa=Z+delta+2chi`, `d_clock=2T rho+J|tau|`, and observe at `t=T+tau>=0`. The complete source error is at most

`min(2,4Theta^2/M+2Mnu+4T rho+2(J+E)|tau|+2(T+|tau|)kappa+eta)`.

The one-head compensation and hopping errors use maximum block and path row-sum bounds, with no artificial factor `L`; physically separate copy mismatches do sum into `Z`. The full-state comparator uses `exp(-itH_0)W'_L` at the **same time** `t`. After tracing fuel, comparison of the bare free evolutions costs only the returned source's free phase. Initial preparation error is contracted under the full actual dynamics before any one-head estimate is applied.

The total actual Hamiltonian remains self-adjoint and positive even when a forward hopping block is nonunitary, because the reverse block is its adjoint and clock padding pays its actual norm. Actual-copy positivity and local norm bounds are supplied certificates. Source rounding and unknown drift are not silently absorbed. The precise positive rational tolerance allocations and full actual per-site norm bound remain in Part I.

## Actual energy, moments and the fresh-fuel refinement

In the exact product model with sharp initial clock, stationary routers and sharp work pairs,

`<H>=<H_A>_rho+M Tr(sigma_M H_A)+M e_r+Mn omega_w+c`,

`Var(H)=Var_rho(H_A)+M Var_(sigma_M)(H_A)+a_1^2`, `a_1^2=J^2 L/(L+1)^2`.

The last contribution is the squared norm of the first-hop component in an orthogonal clock sector. At the exact endpoint, router/work, clock, cut and hopping mean changes vanish, so `Delta E_fuels=-Delta E_source`. At intermediate times the real cut interaction belongs in the energy. Final marginal variances require actual source/fuel and fuel/fuel covariances.

In the general rounded class, static total-energy conservation and clock-number conservation give the exact identity

`-Delta E_fuels=Delta E_source+Delta E_routers+Delta E_work+Delta<V_cut>+Delta<V_hop>`.

Writing `Gamma_0=2d_clock+2t kappa`, the source proof bounds the residual by `K_1 Gamma_0+2K_all eta`, with the actual router/work/correction/hopping norm bounds defined in Part I equation (31). Consequently an attained source error `epsilon_c` implies

`|-Delta E_fuels-Delta E_source,target|<=E epsilon_c/2+K_1 Gamma_0+2K_all eta`.

The extensive factors are retained and their separate ledger tolerances are effective. For a sharp initial clock with zero initial correction, nonunitary rounding contributes `<B_1*B_1>` to the variance, not an assumed `(a'_1)^2`. Imperfect clock preparation requires moments of its actual state.

Part II proves the fresh-product estimate for norm-one bounded collisions:

`complete channel difference<=2|alpha| sum_i ||tau_i-sigma||_1`.

For `alpha=Theta/M`, common fresh-copy accuracy `delta_f` contributes `2|Theta|delta_f`, independent of `M` for fixed `Theta`. It is not uniform in growing source dimension without adjusting accuracy. Marginal errors of correlated supplies do not establish the fresh-product premise. This refinement does not erase nonfuel preparation errors or nominal extensive energy discrepancies.

For the narrower exact-copy/unitary-block model of Part III, let `W` be the source/fuel spectral width, `epsilon_0=min(2,4Theta^2/M)+(2|Theta|/M)sum_i delta_i`, and let `B_0` bound `||H_0||`. With `kappa_s=zeta+2rho+J gamma`, the complete final-state comparison using the **same actual fresh fuels** obeys

`xi=min(2,eta+2T kappa_s+2|tau|(B_0+J+kappa_s))`.

The source error is bounded by `epsilon_0+xi` (and can be capped by two), while the actual fuel-change discrepancy is at most

`|Delta E_fuels(actual)+Delta E_source(target)|<=W(epsilon_0+M xi)/2`.

No nominal-initial-fuel `M delta_f` term is added to this physical change: the comparator has identical initial fuels. The `M xi` term still charges possible final fuel-energy errors. For `W=0`, the source/fuel energies are scalar and their changes vanish. Part III also gives the actual sharp-clock moments with `Delta'_0` and `(a'_1)^2`, including the extra clock margin and the symmetrized covariance bound; those formulas are not asserted for generic erroneous clock preparation.

Nominal initial fuel means and independent summed variances remain a separate comparison. If each fuel width is at most `W`, their discrepancies obey `W sum_i delta_i/2` and `3W^2 sum_i delta_i/4`. Unequal widths require `W_i` in each summand. The original unrestricted-width wording, exact repair and counterexample are preserved: zero collision interaction and source width one do not bound the moments of a fuel Hamiltonian of width two by source width alone. This qualification changes no channel estimate. No final independent-fuel assumption is made.

## Source, evidence and remaining boundaries

Part I is the complete 329-line construction at `3c02940e2d4f3eb519f459dd658950df77662c7bd431500e52f2509658ed94fe`. Part II is the corrected fresh-fuel lemma at `cffe4574c838fc54e1cf6b0ff9d190f06061798e2dc7eb906c12b7bbd7e2c39b`. Part III is the structured precision/fresh-ledger supplement at `1c50b1fcce4b79e3a88d74504486295a1dc4d0759c2bf944a3d0bf2e8979773d`. All three are reproduced in full without changing a byte. `SOURCE_MAP.json` records exact part boundaries; `SOURCE_ARCHIVE.json` records original paths, hashes, roles and actual read coverage.

The root proposal predates the worker completion. The worker read that proposal and had earlier onsite exposure; it did not read the concurrent selective operator checker or the fresh-fuel supplement body before sealing. Parent messages disclosed the proposed fresh-fuel improvement and width issue, and this exposure is retained. The operator checker was independently written against the proposal without reading the worker's source or control implementation. Its scope was operator algebra, not the full layout. The later complete review read the final source and wrote a separate geometry enumerator before reading author control code, while the claimed numerical results were already exposed. These are source-exposed checks with declared shared context, not blind discovery, model-diverse replication or a retained audit.

The three preserved executions are author floating controls, separate floating operator controls and deterministic finite geometry enumeration. All scripts, full outputs, empty stderr records, receipts, parameters and original seals are retained. The geometry check has 31 recorded cases; its all-size conclusion rests on the analytic incidence argument. The large-`M` controls use a 16-by-16 channel superoperator, not an autonomous simulation of 65,536 fuel copies or a numerical diamond-norm certificate. Wrong half-transport control movement, omitted cut compensation and omitted source free phase remain explicit failed variants. No numerical run was repeated for this assembly.

Supplied-copy partial-swap dynamics, Hamiltonian computation and engineered perfect transfer are prior art: Lloyd, Mohseni and Rebentrost's [Quantum principal component analysis](https://arxiv.org/abs/1307.0401), Nagaj's [local Hamiltonian computation](https://arxiv.org/abs/0908.4219), and Christandl and collaborators' [perfect-transfer construction](https://arxiv.org/abs/quant-ph/0309131). The needed finite identities and complete norm estimates are proved in the embedded bodies. Literature snapshots retain the authors' actual coverage; archiving a whole PDF is not a claim that this assembler reread the whole paper. The bounded prior-scope search is context, not an exhaustive novelty search. No generic-clock, perfect-transfer or density-exponentiation novelty is asserted.

There is no external canonical mathematical dependency merely because earlier onsite or finite-history work exists or might be a Git ancestor. The three embedded bodies contain the proof and its narrowly applicable supplements. No history-application source, result or control is part of this assembly. `DEPENDENCIES.json` records the internal proof composition and these exclusions.

The supplied physical resources remain substantial: identical or explicitly certified positive copies, effective stationary-router preparation, target/runtime-dependent fuel, static crossed-bond clock interactions, coefficient precision, initialized work/clock factors and terminal-time access. The clock continues moving after the output time. Native preparation, unmodified-chain implementation, physical measurement/reset, stopping, persistent storage, fault tolerance and efficient scaling remain open. A terminal operation must add its actual energy change to the ledger; no free read is inferred. The earlier uncompensated onsite failure remains a failed route, not a universal obstruction.

This assembly performs no canonical, Git, PR, cache, audit, checkpoint, axiom or editable-prompt mutation. It executes zero mathematical predicates and reruns no scientific code. The next action is root substantive review of this exact wrapper and reconstruction; publication and any later current-main or retained-audit gates remain separate.

---

## Part I: Complete interacting-copy construction, reproduced verbatim

This complete body retains its original status and exposure language. The wrapper records later exact acceptance and current scope. No source sentence, equation, constant or historical claim is rewritten here.

# A supplied interacting-copy autonomous controller

**Complete proposed conditional construction; not independently accepted or retained.** This is an assessment and completion of the exposed root proposal, not an independent discovery or an accepted theorem. Its supplied finite-chain model, engineered controller interactions, prepared resources, and declared observation time are premises. It makes no native microscopic, efficient-computation, autonomous preparation, stable-memory, or retained-status claim. The concurrent `selective_check` directory has not been opened.

## 1. Inputs, exact target, and source exposure

The root proposal was read completely at SHA-256 `683525aba72aa9006f223aef11eb36a3227d73145d751f1edc1461305d5718fd`. The earlier onsite derivation was already fully read and authored in this worker context; its current narrow-repair identity `9db03ad2582a76131ad3d419a037988ec440636371cb8b58444ef4d4902dcd1b` was rechecked. The present result uses the root's interacting-copy route, not its prior onsite theorem as a proof of the missing interaction interface. The additional root fuel-preparation supplement body has not been read or used. Parent messages disclosed a proposed fresh-fuel channel improvement and a moment-width qualification; the improved channel estimate is not used here.

Let the supplied open chain contain `n>=1` qubits and have the explicitly supplied decomposition

    H_A = sum_(k=1)^n h_k + sum_(k=1)^(n-1) v_(k,k+1) >= 0,
    ||h_k||<=u,  ||v_(k,k+1)||<=b.                         (1)

The terms may fail to commute. All copies use the same ordered matrices and local basis convention. A constant shift, if present, is included identically in the supplied one-site terms, with its contribution included in `u` and in actual energy moments. It is not an uncharged global shift. A uniform strength claim for a family requires uniformly bounded `u,b`. Let `E>=||H_A||` be a computable certified bound, for example `n*u+(n-1)*b`. Fix positive clock scale `J` and positive work gap `omega_w`. Put `C=4b` and `c=C+J`.

The target is any supplied computable unitary `U` on the original chain `A`, acting uniformly with every passive reference. The pure router state `|r>` is supplied together with the promise `H_A|r>=e_r|r>` and an effective description sufficient for the required preparation accuracy. No uniform algorithm selecting an exact eigenvector at a degeneracy is assumed. Fuel matrices will be constructed effectively below; their physical preparation is supplied. The common bare-chain model is exact unless the explicitly priced copy-mismatch extension is invoked.

For an integer `M>=1`, use chains `R_0=A,R_1,...,R_M` and `F_1,...,F_M`, each with `n` qubits. Use `n` dual-rail work pairs per collision, two physical qubits per pair. Their logical basis is `|0_L>=|10>`, `|1_L>=|01>` and every pair is initially `|0_L>`. Work energy is `omega_w N_W`, with `N_W` the number of occupied physical work rails. Define

    H_0 = sum_(i=0)^M H_(R_i) + sum_(i=1)^M H_(F_i)
                                  + omega_w N_W >=0.     (2)

The initial state is arbitrary on `A` and a passive reference, tensor the stated router/work/fuel/clock resource state. Neither initial system-resource correlation nor an unknown fuel state is included in this promise.

## 2. Full-operator cut identity and the dual-rail circuit

For two copies `X,Y`, let `s_k` swap their physical qubits at site `k` and `P_K=product_(k in K) s_k`. These swaps commute. If `K` is a contiguous prefix or suffix with one cut between `k,k+1`, all summed onsite terms and all bonds not crossing the cut are invariant under `P_K`. The remaining difference is exactly

    D_k(X,Y) = v_(Y_k,X_(k+1)) + v_(X_k,Y_(k+1))
                         - v_(X_k,X_(k+1)) - v_(Y_k,Y_(k+1)),
    P_K(H_X+H_Y)P_K* - (H_X+H_Y) = D_k(X,Y).          (3)

The order of tensor factors in each `v` is inherited from the original ordered bond. Prefix and suffix give the same sum of the two crossed bonds. Thus `D_k` has four-data-qubit support and norm at most `C=4b`. The empty and complete sweep have difference zero. For `n=1` every such difference is zero. Identity shifts cancel exactly; commutativity of neighboring bonds was never used.

A logical Hadamard `H_L` is the usual Hadamard on the one-excitation subspace `span{|10>,|01>}`, with identity on `|00>,|11>`. Likewise the logical phase `Z_alpha` is `diag(e^(-i alpha),e^(+i alpha))` on that subspace and identity elsewhere. Both commute with the full physical two-rail number operator. A controlled data swap uses `Q=n_(rail 1)`, where rail 1 is occupied in `|1_L>`, as control. Its full physical operator is `(I-Q)I+Q s_k`. It is unitary even outside the encoded subspace.

Transport a logical control to the adjacent column by first swapping rail 0 with rail 0 there, then swapping rail 1 with rail 1 there. Each physical SWAP commutes with the sum of all work onsite energies on the full Hilbert space. With blank pairs initialized in `|0_L>`, the two swaps move the entire logical control and its correlations and leave a blank pair behind.

A collision between `R_i,F_i` consists, in time order, of

    H_L; controlled full-chain SWAP sweep;
    H_L; Z_alpha; H_L;
    reverse controlled full-chain SWAP sweep; H_L.     (4)

The first sweep transports the control from its starting end to the opposite end; the second transports it back. Each sweep has `n` controlled swaps and `2(n-1)` physical rail swaps. There are four logical Hadamards and one phase. Therefore one collision contains

    2n+4(n-1)+5 = 6n+1 elementary gates.               (5)

The proposed `4n+3` count applies only if a two-rail transport is counted as one gate and is not the physical count used here. On the initialized work subspace, (4) returns every pair exactly to `|0_L>` and acts on data as `exp(-i alpha S)`, where `S` swaps the two whole chains. Indeed, on an abstract logical control `B=H_L C_S H_L` is an involution and `B Z_L B=Z_L tensor S`. Thus `B exp(-i alpha Z_L) B=exp(-i alpha Z_L tensor S)`, which gives the asserted action on logical zero. The transported circuit realizes that abstract operation and returns the physical control to its start. This encoded action is used only for the output calculation, not for prefix locality or positivity.

Here is the full-space prefix argument. A completed uncontrolled full-chain swap commutes with `H_0`. A completed moving-control sweep equals a work-rail permutation times a controlled full-chain swap with its control at the sweep's starting rail, and also commutes with `H_0`. All work-only rotations and rail transports commute with `H_0`. Consequently, at an incomplete sweep the right-hand earlier prefix can be deleted from `W_j H_0 W_j*`: it already commutes with `H_0`.

For an uncontrolled incomplete sweep, the difference is just (3). For a controlled incomplete sweep it is `Q D_k`, where `Q` is the currently transported control rail. For the controlled permutation `C_K=(I-Q)I+Q P_K`, the cross terms vanish because `Q(I-Q)=0` and `H_0` commutes with `Q`; the work part is unchanged. This proves the identity on every physical work state. After the first half of a rail-pair transport, rail 0 has moved but `Q=n_(rail 1)` remains at the old column. After the second half, it is at the neighboring column. Both prefixes therefore retain the same `D_k`, with the stated old or new control support. There is no hidden encoded-subspace assumption at the half transport. Work rotations occur only at completed-sweep endpoints where the difference is already zero.

More explicitly, before a transport let the unfinished sweep be `T_W C_K`, where `T_W` is the current work-rail permutation and `C_K` is controlled by the starting rail. The current physical control is `T_W Q_start T_W*`. Applying its next controlled swap extends `K`, and applying either physical rail swap merely left-multiplies `T_W`. This induction is an operator identity on all rails, with no blank-register restriction. At a full sweep `C_K` commutes with the pair energy and `T_W` commutes with all work energies, proving the completed-prefix assertion used above.

Thus for every elementary prefix,

    Delta_j = W_j H_0 W_j* - H_0
             is 0, D_k, or Q D_k,  ||Delta_j||<=C,     (6)

with the explicit local support above. In particular `Delta_0=Delta_L=0` and the complete circuit commutes with `H_0` on the full physical Hilbert space.

## 3. Schedule, original source return, and exact geometry

For forward router pair `i`, sweep from `ell_i` to `r_i`, where `(ell_i,r_i)=(1,n)` for odd `i` and `(n,1)` for even `i`. After swapping `R_(i-1)` with `R_i`, perform collision (4) beginning at `r_i` and returning its control to `r_i`. This is also the starting column `ell_(i+1)` for the next forward swap. After the last collision, perform reverse router swaps for `i=M,...,1`, each sweeping from `r_i` to `ell_i`. Consecutive stages meet at the same end column. The complete length is

    L = 2Mn + M(6n+1) = M(8n+1).                      (7)

It is independent of the angle, fuel state, target spectral data, and preparation algorithm.

On the initialized router subspace, a complete forward swap moves the entire unknown chain state and its correlations into the next router, leaving `|r>` behind. Each collision acts there. The reverse full-chain swaps return that same work factor and all its correlations to the original physical `R_0=A`; every router is restored to `|r>`. No relabeling or global decoder occurs. The completed work factors return as proved above. This statement holds for arbitrary reference entanglement and includes all source-fuel correlations.

The following explicit embedding uses distinct sites of the cubic lattice. Keep the original source at unit-spaced sites `(k,0,0)`. Set the copy-row separation `D=100`, with site columns `k=1,...,n`:

    R_(i,k) = (k,Di,0),             i=0,...,M;
    F_(i,k) = (k,Di,2),             i=1,...,M;
    w_(i,k,0) = (k,Di,4),
    w_(i,k,1) = (k,Di,6).                              (8)

Each gate is assigned to its collision/router-pair index `i` and its current data/control column `k`. For a rail transport, `k` is its departure column. Place the clock after that gate at `(k,Di,20+t)` with tag `t` in the following table. A tag occurs at most once for a fixed `(i,k)`.

| Event | Tag |
|---|---:|
| Forward router swap | 0 |
| Reverse router swap | 1 |
| Initial collision Hadamard | 2 |
| Outward controlled data swap | 3 |
| Outward rail-0 transport | 4 |
| Outward rail-1 transport | 5 |
| Middle first Hadamard | 6 |
| Middle phase | 7 |
| Middle second Hadamard | 8 |
| Returning controlled data swap | 9 |
| Returning rail-0 transport | 10 |
| Returning rail-1 transport | 11 |
| Final collision Hadamard | 12 |

The initial clock is at `(1,D,40)`. Every other clock site is unique and distinct from data and work. At a compensation prefix, its clock, the current cut's two neighboring columns, and any old/new control rail span at most one column separation. Hopping supports span at most one column separation too. Their row spread is at most `2D`: this conservative case occurs when a returning router sweep moves from pair `i` to pair `i-1`, whose data include row `i-2`. All vertical coordinates are between zero and forty. Therefore every hopping and compensation support has Manhattan diameter at most `1+2D+40=241`; the uniform advertised bound is 400. This remains valid at `n=1`, when several endpoint events occupy the same cell but have distinct tags.

The compensation terms have arity at most six: one clock, one control rail, and four data sites. Uncontrolled compensation has arity five. A hopping term has its two clock qubits and at most three gate qubits, hence arity at most five. Bare terms have arity at most two. These are genuine bounded-range three-dimensional supports; nearest-neighbor two-body synthesis is not claimed. Empty lattice positions need no interacting hardware; filling the finite rectangular box with uncoupled spectators only changes the count by a fixed geometric factor and requires their declared preparation/energy bookkeeping separately.

Uniform incidence is also explicit. A router data site participates in at most four router-swap gates and two controlled-swap gates, and in at most eight uncontrolled compensation terms plus twelve controlled compensation terms. For the latter count, each cut has at most three nonzero prefixes per sweep: after the controlled swap and after each of the two transport halves. A data site meets at most two adjacent cuts. A fuel site has two gate incidences and at most twelve compensation incidences. A work rail has at most seven gate incidences; its control rail has at most six compensation incidences (three per direction), while rail 0 controls none. Clock sites have two hopping incidences and one compensation incidence. These bounds count small-chain coincidences conservatively; endpoint rotations do not add compensation.

With hopping norm at most `J/2`, a valid uniform per-site norm-sum bound for the displayed decomposition is

    B = (u+2b) + omega_w + 4J + 20C.                    (9)

For example, the separate router, work and clock bounds are `u+2b+3J+20C`, `omega_w+7J/2+6C`, and `c+J+C`. Equation (9) dominates all. The active physical-qubit count is

    N = (2M+1)n + 2Mn + (L+1)
      = n + 12Mn + M + 1.                              (10)

The active region has `O(nM)` volume with a fixed thickness and fixed spacing. The numerical constants are conservative, not optimized.

## 4. Static compensated Hamiltonian and full-space positivity

Let `a_j=J sqrt(j(L+1-j))/(L+1)`, hence `a_j<=J/2`. For physical one-hot clock qubits with raising operators `s_j^+`, set

    H = H_0 + V_cut + c N_C + V_hop,
    V_cut = sum_(j=0)^L n_(c_j) Delta_j,
    V_hop = sum_(j=1)^L a_j [s_j^+ s_(j-1)^- G_j
                                  + s_(j-1)^+ s_j^- G_j*].  (11)

The work/data support of a gate or correction is disjoint from its clock sites. This is one time-independent physical tensor-product Hamiltonian. It includes the real engineered crossed-bond corrections, not a free prescription to conjugate a nonlocal Hamiltonian.

For every edge unitary `G_j`, its hopping term is bounded below by `-a_j(n_(c_(j-1))+n_(c_j))`. This follows from positivity of the two-clock block `[[I,G_j*],[G_j,I]]`; the `00,11` sectors are treated directly. Also `n_(c_j)Delta_j>=-C n_(c_j)`. Summing gives

    H >= H_0 + sum_j (c-C-a_j-a_(j+1))n_(c_j) >=0,     (12)

with missing endpoint weights zero. No commuting-cut assumption was used. This establishes positivity on the entire physical Hilbert space, including illegal work and multiple-head clock states.

On the invariant one-head sector, let `F=sum_j |j><j| tensor W_j`. Equations (6) and (11) give the exact full-data operator identity

    F* H F = H_0 + c I + K,
    K=sum_j a_j(|j><j-1|+|j-1><j|).                    (13)

The first term here is the same `H_0` on every clock block. The scalar path is `(2J/(L+1))J_x` in spin `L/2`; at

    T=pi(L+1)/(2J),
    exp(-iTK)|0>=(-i)^L|L>.                            (14)

The spin identity follows by restricting `L` spin-one-half factors to their symmetric subspace: rotation by pi flips each constituent with phase `-i`, and the raising matrix elements give the stated square roots. This is the prior-art engineered-transfer mechanism, rechecked here with the actual normalization.

Consequently the exact endpoint data operation is, up to scalar phase,

    W_L exp(-iH_0T) = exp(-iH_0T)W_L.                 (15)

The equality on the right follows from full-prefix completion in (6), not from an onsite approximation. Routers are stationary and returned, and each work pair has its original sharp one-excitation energy. Thus the physical source channel is

    C_M = Ad(exp(-iH_A T)) composed with Phi_(alpha,sigma)^M. (16)

Fuel free conjugations disappear under partial trace even with source/reference correlations. This argument applies to the same original chain and every passive reference. The clock later moves again: there is one declared output time, no autonomous stop or stable-storage theorem.

## 5. Complete collision bound and effective, noncircular fuel

Let `S` be the whole-copy swap, `||S||=1`, and let `sigma` be a density matrix. Expanding `exp(-i alpha S)=cos(alpha)I-i sin(alpha)S` and using the two partial-swap trace identities gives, for every source/reference operator,

    Phi_(alpha,sigma)(rho_AR)
      = cos(alpha)^2 rho_AR + sin(alpha)^2 sigma tensor Tr_A(rho_AR)
            -i cos(alpha)sin(alpha)[sigma tensor I_R,rho_AR]. (17)

In particular its derivative at zero is `-i[sigma,.]`. Twice differentiating the joint unitary channel has complete trace-norm bound four, since the commutator norm is at most `2||S||`. Its Taylor remainder has bound `2alpha^2`. The ideal channel generated by `sigma` has second derivative norm at most `4||sigma||^2<=4`, and the same remainder bound. State insertion and partial trace are complete contractions. The argument works for signed alpha and arbitrary passive references. A telescope therefore gives

    ||Phi_(Theta/M,sigma)^M - Ad(exp(-iTheta sigma))||_diamond
                        <= min(2,4Theta^2/M).          (18)

All fuel copies are present initially and independent; moving their mathematical partial traces past later gates is not a physical reset. Earlier source/fuel correlations are retained in the full state.

Put `d=2^n`, `Theta=4pi d` and `alpha=Theta/M`. Choose `M` from the desired error budget before computing the schedule, using a certified integer upper bound rather than deciding equality at a real ceiling. Calculate `L` from (7) and `T` from (14), then form

    V=exp(+iH_A T)U.                                    (19)

The following is an effective logarithm construction under computable matrix entries and the supplied unitary promise; it does not decide eigenvalue equality or choose an eigenbasis.

Take `q=d+1` candidate cuts `z_l=exp(2pi i l/q)` and `gamma=sin(pi/q)/4`. Their minimum mutual chord distance is `2sin(pi/q)=8gamma`. Each spectral point of `V` can be within distance `2gamma` of at most one candidate. There are at most `d` distinct spectral points, so some candidate has distance strictly greater than `2gamma` from the spectrum. Compute certified singular-value enclosures of `V-z_l I` to increasing precision and stop at any candidate whose least singular value is certified greater than `gamma`. Singular values are continuous computable functions of finite computable matrices; equivalently they can be enclosed using finite rational spectral bounds for `(V-z_l I)*(V-z_l I)`. Weyl's norm bound converts entrywise approximation errors to certified enclosures. The finite search terminates because of the margin just proved. Degeneracy does not cause a problem. The candidate angles are rational multiples of `2pi`; arbitrary exact rational-real angles are unnecessary.

For the certified candidate `z`, put

    B=-conjugate(z)V,
    A=-i(B-I)(B+I)^(-1),
    K_0=-2 arctan(A),
    K=K_0-(Tr K_0/d)I.                                (20)

Here `B+I` is invertible with least singular value greater than `gamma`; `A` is Hermitian and `||A||<=2/gamma`. On a spectral value `e^(i psi)` of `B` with `-pi<psi<pi`, this Cayley transform is `tan(psi/2)`, so `K_0` has eigenvalue `-psi`. Hence `exp(-iK_0)=B`, `Tr K=0`, `||K||<2pi`, and `exp(-iK)` is `V` up to scalar phase.

For a concrete effective functional calculus, use

    arctan(A) = integral_0^1 A(I+t^2 A^2)^(-1) dt.      (21)

All inverses here have positive denominator at least one. For `||A||<=R`, the integrand is Lipschitz with constant at most `2R^3`; a left Riemann sum with `N_int` equal intervals has operator error at most `R^3/N_int`. Certified finite matrix arithmetic and sufficiently fine quadrature thus compute (20) to any requested error. Centering the trace at most doubles operator error. This is a deliberately inefficient but terminating algorithm, without a branch-cut oracle.

Define the supplied fuel state

    sigma_M=(I+K/(4pi))/d.                             (22)

It has trace one, is at least `I/(2d)`, and `exp(-iTheta sigma_M)` equals `V` up to scalar phase. Combining (16), (18) and (19) therefore approximates the fixed Schrödinger-picture target `Ad(U)` with error `min(2,4Theta^2/M)`. This is genuinely runtime-dependent fuel: omitting the `exp(+iH_A T)` factor in (19) would leave an actual unwanted source free phase.

The sequence is noncircular: select `M`; write the fixed-length circuit; calculate `T`; calculate a certified cut, `K` and `sigma_M`; prepare resources; start the autonomous run. Neither circuit length nor runtime depends on the duration or success of an unspecified preparation algorithm. Physical preparation is a supplied finite input resource. Its description is effective: rational Hermitian trace-one approximants to (22), certified within operator distance below `1/(4d)`, remain positive. The spectral margin also allows effective square-root or Cholesky purification if a state description is required. No native gate set, autonomous preparation time, or preparation work cost is inferred from computability.

For fixed `n`, arbitrary accuracy is possible. As `n` grows, `M=O(4^n/epsilon)` and hence `N=O(n4^n/epsilon)` and `T=O(n4^n/(J epsilon))` suffice for the exact model. The input matrix and fuel descriptions can already require order `4^n` entries. These are resource upper bounds, not an efficiency result.

## 6. Finite precision without silently altering the source

Here is one explicit robust implementation class. Keep the original bare source Hamiltonian `H_A`. First allow exact copies, exact work gap, exact physical rail/data swaps, and exact number-preserving logical Hadamards. Use collision angles `alpha_i'` with `|alpha_i'-alpha|<=nu`, and real weights `a_j'` in `[0,J/2]` with `|a_j'-a_j|<=rho`. The resulting unitary gates are `G_j'`. Their prefix corrections are still exactly the same local operators (6), because angle changes occur only at zero-correction endpoints. The encoded collision still returns the work register and equals `exp(-i alpha_i' S)`.

Allow Hermitian local correction approximants `Delta_tilde_j` with the same supports and `||Delta_tilde_j-Delta_j||<=delta`; impose `Delta_tilde_0=Delta_tilde_L=0` exactly. Let the actual forward hopping block be any local matrix

    B_j=a_j' G_j' + E_j,   ||E_j||<=chi,                (23)

on the corresponding gate support, with its adjoint on the reverse edge. This also covers entrywise finite approximation of the prescribed algebraic gates; `B_j` itself need not be a scaled unitary or preserve work number. Set the actual clock coefficient to

    c_tilde=C+delta+J+2chi.                             (24)

Optionally, the router and fuel copies may be positive supplied local Hamiltonians `H_hat_l` with the same range and certified differences `||H_hat_l-H_A||<=zeta_l`; the original source remains exactly `H_A`. Let `Z=sum_l zeta_l`. Positivity of these actual bare copies is a required promise in this extension, not a consequence of a small error alone. Their local term norm bounds must also be retained for a uniform interaction-strength statement. Set `Z=0` for the exact-copy premise of the root proposal. One constructive positive-copy approximation is to approximate the local terms Hermitianly to total norm error at most `zeta_l/2`, then add `zeta_l I/2` distributed over the copy's one-site terms. The resulting operator is at least `H_A>=0` and differs from it in norm by at most `zeta_l`. The added copy energy belongs to the actual ledger; it does not modify the original source.

The actual static Hamiltonian is obtained from (11) using these copies, corrections, hopping blocks and clock coefficient. It is positive on the full Hilbert space. Indeed each hopping block has norm at most `J/2+chi`, each correction is at least `-(C+delta)I`, and (24) pays the two incident hopping norms and the correction lower bound. The positive actual bare Hamiltonian completes the proof. Geometry and arity are unchanged. If `u_hat,b_hat` bound the actual data one-site and bond terms, a conservative actual per-site norm sum is `(u_hat+2b_hat)+omega_w+4J+7chi+20(C+delta)`, using the same incidence counts. It stays uniform when these local bounds and coefficient-error ceilings stay uniform. This explicitly prices matrix-entry rounding without pretending it preserves unitarity.

Let the actual joint resource state, independent of source/reference, have trace-norm distance `||rho_resource-rho_resource,ideal||_1<=eta` from the exact product resource specified using (22). Observe at `t=T+tau>=0`. On the one-head sector, the copy mismatch has operator norm at most `Z`; the block-diagonal correction error has norm at most `delta`; the hopping-block errors have norm at most `2chi`, by the block row-sum bound. Thus define

    kappa=Z+delta+2chi,
    d_clock=2T rho+J|tau|.                            (25)

The crucial point is that these one-head compensation/hopping bounds do not acquire an artificial factor `L`. Orthogonal clock blocks bound the diagonal error by its largest block, while a path has only two incident off-diagonal blocks. Copy mismatches really do accumulate in `Z`.

Use the actual angle gates as a reference exact compensated program and the same scalar clock coefficient `c_tilde`. Duhamel bounds its one-head evolution error in vector norm by `t kappa`. In its dressed frame the weight error costs at most `2T rho`, and clock timing costs at most `J|tau|`. These estimates are uniform isometry bounds for every data/reference vector. Vector distance `q` gives reduced complete trace error at most `2q`. The endpoint product-unitary telescope costs at most `2Mnu`. Once the source is returned, its actual residual free phase relative to the fuel design time is bounded by `2E|tau|`; free fuel conjugations disappear on tracing fuel. Joint resource error costs at most `eta`, including components outside the legal clock/work sectors. Therefore

    source error <= min(2,
       4Theta^2/M + 2Mnu + 4T rho + 2(J+E)|tau|
                         +2(T+|tau|)kappa + eta).       (26)

No norm of the extensive bare data energy was inserted into the source timing term. It is the final original-source free phase that matters there.

For example, for target channel error `0<epsilon_c<=1`, choose

    M>=max(1,24Theta^2/epsilon_c),
    nu<=epsilon_c/(12M), rho<=epsilon_c/(24T),
    tau_max=epsilon_c/[12(J+E)], |tau|<=tau_max,
    kappa<=epsilon_c/[12(T+tau_max)], eta<=epsilon_c/6. (27)

The six terms in (26) are then at most `epsilon_c/6` each. This finite precision is effective. The large budget makes `|alpha|` small; rational Cayley approximants give exact finite-description unitary phases if that structured implementation is desired. General local matrix errors are already covered by `chi`. Four-data-qubit correction matrices are computed from the supplied local bonds (3), so certified Hermitian rational approximants attain `delta`. Choose finite rational bounds for the weights and for the padding (24). A known clock-padding excess merely adds a scalar on the one-head sector and does not affect the source channel. Effective computation of `T` requires the corresponding certified knowledge of `J`; unknown drift must satisfy the actual error budgets, not just an arithmetic estimate.

At fixed supplied strengths and fixed `n`, the required angle precision is of order `epsilon_c/M`, weight and compensation precision of order `epsilon_c/T`, and read-time precision of order `epsilon_c/(J+E)`. Static coefficient descriptions require only logarithmically many bits in the reciprocal chosen precision, aside from computing the supplied real inputs. There are `O(nM)` fixed-size local terms. If copy mismatch is included, one sufficient allocation is `zeta_l<=kappa_budget/(2M)` after assigning an appropriate fraction of the total `kappa` budget to that source of error; local bond/site entry errors can be reduced further by the `O(n)` term count. This may be expensive but is explicit and finite.

The preparation promise is joint. Independent fuel-chain errors `eta_(F_i)` and router-chain errors `eta_(R_i)`, together with independent work/clock errors, sum to a sufficient bound on `eta` by a tensor-product telescope. Fuel and router chains need not factor into their physical sites. Fixed individual errors cannot be silently reused as `M` grows. No improved fresh-fuel estimate from the unread optional root supplement is used here.

## 7. Actual energy moments, exact and imperfect ledgers

Use the actual energy of every chain, work register, clock, correction and hopping term. In the exact model with the exact prepared product resource and initial head at zero, `Delta_0=0` and the hopping mean is zero. Work energy is the sharp value `Mn omega_w`; router energies are sharp `e_r`. Hence

    <H> = <H_A>_rho + M Tr(sigma_M H_A) + M e_r
                                      + Mn omega_w + c,
    Var(H) = Var_rho(H_A) + M Var_(sigma_M)(H_A) + a_1^2,
    a_1^2 = J^2 L/(L+1)^2.                            (28)

For a direct variance check, applying `H` once to the initial vector produces its clock-zero bare-energy component and the orthogonal clock-one vector `a_1 G_1 psi`. Thus the latter contributes exactly `a_1^2`; no cross expectation with the diagonal part survives. Mixed fuel and reference-entangled source states follow by linearity of first and second moments. Product preparation makes the initial copy covariances zero. This does not assume any final independence.

Clock number commutes with every term in (11), so its energy `cN_C` is conserved. Total energy is conserved because the Hamiltonian is static. Bare source, fuel, and correction energies need not separately be conserved during the run. At the exact endpoint the head is sharp at `L`, `Delta_L=0`, and the hopping mean is zero. Router and work factors have returned exactly. Consequently the actual mean ledger is

    Delta E_fuels = -Delta E_source,
    Delta E_routers = Delta E_work = Delta E_clock
                    = Delta <V_cut> = Delta <V_hop> = 0. (29)

At intermediate times the real cut interaction must be included. Final total variance remains the conserved value (28), but an expression in final marginal variances must include all actual covariances. Fuel correlations and preparation coherence have not been reset or supplied for free during the evolution.

For every actual finite-precision implementation of section 6 and every initial state, the unconditional exact ledger is instead

    -Delta E_fuels = Delta E_source + Delta E_routers
                       +Delta E_work +Delta<V_cut>
                       +Delta<V_hop>,                  (30)

with the actual matrices in every term; clock energy still has zero change. It is (30), not automatic endpoint return, that holds without ideal completion. A terminal read operation adds its actual change `Tr[H(R_read(state)-state)]` to the total ledger. No terminal-read apparatus, zero-cost read, or reset mechanism has been constructed.

For an explicit tolerance on the residual in (30), put

    Gamma_0 = 2d_clock + 2t kappa,
    E_Rsum = sum_i ||H_hat_(R_i)||,
    K_1 = E_Rsum + 2Mn omega_w + (C+delta) + (J+2chi),
    K_all = E_Rsum + 2Mn omega_w
                   +(L+1)(C+delta)+L(J/2+chi).        (31)

Let `B_res=E_routers+E_work+V_cut+V_hop`. Its norm on the one-head sector is at most `K_1`; its norm on the full Hilbert space is at most `K_all`. Compare the actual evolution of the ideal resource with the endpoint state `exp(-itH_0)W_L'` at a sharp terminal head. The latter has returned routers/work, vanishing corrections and hopping mean, even at time `t` and with the primed collision angles. Its initial and final expectations of `B_res` agree. This remains true when testing the actual router-energy observables: the comparison state has the same pure router factor at each endpoint, even if that factor is not stationary under a mismatched actual copy. The full-state trace-norm distance is at most `Gamma_0`. Restoring a joint preparation error `eta` costs at most `K_all eta` at each endpoint. Thus

    |Delta <B_res>| <= K_1 Gamma_0 + 2K_all eta.       (32)

This conservative estimate explicitly retains extensive energy costs. If (26) is at most `epsilon_c`, the actual source-energy change differs from the target change by at most `E epsilon_c/2` (center the source observable). Hence

    |-Delta E_fuels - Delta E_source,target|
       <= E epsilon_c/2 + K_1 Gamma_0 + 2K_all eta.    (33)

For any desired absolute ledger tolerance `delta_E`, first choose `epsilon_c<=min(epsilon,1,delta_E/E)` when `E>0`, then require `Gamma_0<=delta_E/(4K_1)` and `eta<=delta_E/(8K_all)` as well as (27). If `E=0`, the source comparison term is zero. Fixed a priori upper bounds for the small coefficient/copy errors give finite upper bounds on `K_1,K_all` before selecting their tighter tolerances. Thus there is no precision fixed-point requirement. Zero denominators correspond to an identically vanishing residual and can be omitted. The ledger identity (30) remains exact at any tolerance.

The variance formula for an ideal sharp initial clock generalizes without pretending a rounded hopping block is unitary: with `Delta_tilde_0=0`,

    Var(H_actual) = Var(H_0,actual) + <B_1* B_1>,      (34)

and the mean is the actual bare mean plus `c_tilde`. Initial copy/work covariances, if present, belong in `Var(H_0,actual)`. For generic imperfect clock preparation the exact first and second moments must be calculated from that actual state; (28) is not its formula.

Even for fresh independent fuels, nominal energy errors are extensive. With exact copies and each prepared fuel within trace norm `eta_f` of `sigma_M`, replacing the actual product fuel by the nominal one can change the initial fuel mean by at most `M E eta_f/2` and its summed variance by at most `3M E^2 eta_f/2`. The first bound centers `H_A`; the second uses the centered `H_A^2` moment bound plus `|m^2-m'^2|<=2E|m-m'|`. These estimates apply to independent product fuel preparations and do not erase generic covariance or clock-preparation errors. A source-channel estimate alone is insufficient for the ledger.

## 8. Attribution, actual selective controls, and preserved failed variants

The partial-swap supplied-copy mechanism is prior art, including [Lloyd, Mohseni and Rebentrost, *Quantum principal component analysis*](https://arxiv.org/abs/1307.0401), PDF pages 2-3. The relevant passage was read in this task; its efficiency and preparation claims are not hypotheses here. Equation (17) is expanded directly and (18) is proved with complete trace norms above. The autonomous history/pulse-clock mechanism and the square-root transfer clock are also prior art: [Nagaj, *Local Hamiltonians for Universal Quantum Computation*](https://arxiv.org/abs/0908.4219), Section II/II.A, and [Christandl et al., *Perfect state transfer in quantum spin networks*](https://arxiv.org/abs/quant-ph/0309131). Prior complete relevant coverage of those exact primary snapshots was reused and their hashes rechecked. `SOURCE_EXPOSURE.json` records actual coverage and the new primary PDF snapshot. None of these generic mechanisms is claimed novel.

One actual execution of `selective_controls.py` ran at `2026-10-14T04:49:42Z`, exited zero and emitted the complete `run01/stdout.json`; stderr is empty. The receipt records the command, interpreter, NumPy/SciPy versions, wall time and hashes. Script SHA-256 is `602c93ac2396c512e8eab7fc7f69823f76bb4279c1a6856f6575c2affb200469`; stdout SHA-256 is `31a5dc734a9fc4c2b22d97bcef4086e92768ebad4b6b5a365c79fc2974e8314c`. No failed executable run or retry was hidden. These are selective author controls, not an independently built checker or theorem acceptance. The code imports no other scientific implementation.

The fixed two-site example is the positive noncommuting chain

    H_A = 2I + 0.7 Z_1 + 0.5 Z_2 + 0.3 X_1 X_2
                                               +0.17 Z_1 X_2,

with work gap `0.9`; the full matrix and tensor-order convention are emitted. The controls found:

* For `n=2,M=1`, every one of the seventeen prefixes was compared as a full 1024-by-1024 data/work matrix, including all illegal dual-rail states. The largest Frobenius residual against the local formula (6) was about `1.43e-13`. Moving the control projector prematurely after the first rail transport instead gave Frobenius defect about `15.60` in each direction. This checks the disputed half-transport identity without restricting the work inputs.
* A separate direct two-site router-swap clock Hamiltonian was built from local terms on the full 128-dimensional physical data/clock space. Its smallest eigenvalue was about `1.47156`. On its one-head input subspace, the compensated endpoint operator error was about `1.98e-14`; omitting the cut compensation gave defect about `1.22398`. The propagator was built directly from those local terms, not obtained by assuming its desired conjugation formula.
* Support enumeration for `(n,M)=(1,1),(2,1),(3,2),(10,10)` confirmed the stated gate/qubit counts. Maximum observed diameter was 221, maximum arity six, maximum gate incidence seven, and maximum cut incidence twenty. Uniform bounds follow from section 3's proof, not from these samples.
* A density-matrix channel calculation for `n=2,M=65536` used a 16-by-16 superoperator, not the full autonomous Hilbert space. Its normalized source/reference Choi witness differed from the desired target by about `0.070829`, below the analytic complete-channel allowance `0.154213`. Choosing fuel without the runtime free-phase factor gave Choi defect about `1.97093`. The numerically selected spectral gap is an observed value, not the certified-cut algorithm in section 5. A Choi witness is not a numerical diamond-norm upper certificate.

The wrong-half-transport control, omitted compensation, and omitted runtime phase remain named failed variants in the code and output. The first two operator calculations use distinct small matrix constructions within this author script; shared parameters and route knowledge preclude an independence claim. All-size positivity, all-prefix locality, complete norms and effective resource selection rest on the written proofs and still require separate review.

## 9. Disposition and exact limits

The exposed proposal admits the conditional completion above with the corrected physical collision count and explicit geometry. The full-operator cut identity includes illegal work states and half transports; the Hamiltonian is positive on all physical clock sectors; the endpoint is the original source; and runtime-dependent fuel can be selected effectively without a branch-cut oracle or preparation-time fixed point. Finite precision and actual energy accounting have separate explicit tolerances. This is a proposed theorem for the supplied finite interacting-copy model, not an acceptance decision.

The previous failed onsite route remains failed without compensation. Here it is repaired by actual local crossed-bond, clock-controlled interactions and extra copies. Those interactions are a supplied engineering premise. Nothing shows that an unmodified native chain, a fixed two-body hardware family, or an autonomously prepared apparatus implements them. No universal negative theorem follows from either failure.

Exact stationary router preparation is supplied, with the explicit effective-data qualification in section 1. Arbitrary native preparation, readout/reset work, fault tolerance, persistent output storage, uniform many-body gap, or an efficiency guarantee for increasing `n` remains outside the statement. The clock and controller later continue evolving. Fuel may be consumed and correlated. Copy mismatch and general local coefficient rounding are covered only with the positivity and norm certificates of section 6; uncontrolled unknown drift is not automatically covered.

The remaining acceptance obligation is a separate mathematical review of this complete exposed-route construction, especially the prefix permutation induction, actual-support incidence count, effective-cut algorithm, and source-versus-ledger precision distinction. The concurrent `selective_check` directory and optional root fuel-preparation supplement remained unopened throughout this derivation and its seal. No Git, canonical runner, PR, campaign checkpoint, axiom, audit, publication source or editable prompt was changed. All task writes are under `worker_derivation/`; its seal is a source-identity record, not a competing operational checkpoint.

---

## Part II: Fresh-product preparation lemma with explicit fuel-width premise, reproduced verbatim

This complete body retains its original status and exposure language. The wrapper records later exact acceptance and current scope. No source sentence, equation, constant or historical claim is rewritten here.

# Fresh-fuel preparation bound: root analytic supplement

Unaccepted until separately checked. This is a general small-collision estimate, not an interacting-controller construction. It does not change the accepted onsite theorem or its conservative global-resource error bound.

Let G be a self-adjoint interaction on a source and one fuel factor, with ||G||<=1, and U_alpha=exp(-i alpha G). For an arbitrary source/reference density operator rho and two independently supplied fuel states tau and sigma, set D=rho tensor (tau-sigma). Then D is Hermitian, ||D||_1=||tau-sigma||_1=delta, and its partial trace over fuel is zero. Duhamel therefore gives

    Tr_F(U_alpha D U_alpha* )
      = Tr_F integral_0^alpha -i U_t [G,D] U_t* dt,
    ||Tr_F(U_alpha D U_alpha*)||_1 <= 2 |alpha| delta.

The partial trace is trace-norm contractive on Hermitian operators. The bound includes arbitrary passive references. Equivalently, the difference between the two physical channels is at most 2|alpha|delta in diamond norm: for a Hermiticity-preserving difference of channels, arbitrary reference-extended density inputs suffice. No dimension factor is introduced.

For M fresh, mutually independent fuel states tau_i, each independent of the source/reference before use, a channel telescope yields

    ||Phi_(alpha,tau_M)...Phi_(alpha,tau_1)
        - Phi_(alpha,sigma)^M||_diamond
      <= 2 |alpha| sum_i ||tau_i-sigma||_1.

In particular alpha=Theta/M and a common error delta give at most 2|Theta|delta, independent of M. This is sharper than comparing the complete initial tensor-product fuel resources by a global trace-distance allowance. It requires the stated fresh-product model: local marginal errors alone do not establish it for correlated fuel supplies, or for fuel initially correlated with the input. Imperfect clock/router preparations and imperfect gates are separate errors.

For the proposed partial whole-chain SWAP, G=S has norm one. Combining this lemma with the independently pending ideal collision estimate would give

    complete source-channel error <= 4Theta^2/M
                                     + (2|Theta|/M) sum_i delta_i,

before clock, gate, timing or other preparation errors. The actual free-source evolution is a unitary channel and preserves this norm bound. For the accepted onsite exchange collision, ||(X X+Y Y)/2||=1, so the same lemma would add (2|theta|/M) sum_i delta_i to its previously checked ideal bound 5theta^2/(2M). Neither combination is recorded as accepted by this supplement.

Energy accounting must distinguish a physical change from a comparison to nominal initial resources. Suppose the exact endpoint program commutes with the total bare chain energy and returns all routers/work registers, so that the actual total fuel-energy change equals minus the actual source-energy change for every supplied fuel state. This identity remains valid for the actual tau_i. If the source Hamiltonian has spectral width W and the source channel is within epsilon of the target on a common initial source state, the difference between the actual fuel-energy change and minus the target source-energy change is at most W epsilon/2. It does not acquire an M delta term merely because the actual initial fuel differs from the nominal sigma. This conclusion requires the exact endpoint return and conservation hypotheses, still open for the interacting proposal.

For the following nominal initial-moment bounds, also assume every fuel Hamiltonian has spectral width at most W. This holds for the intended identical-copy and equal-gap models; it does not follow from the arbitrary-interaction lemma. More generally use each fuel width W_i in its own summand. Under this premise, the nominal and actual *initial total fuel means* can differ by as much as

    (W/2) sum_i delta_i.

For independent fuel copies, their nominal versus actual summed variances obey a conservative bound (3W^2/4) sum_i delta_i. To see this, shift one fuel Hamiltonian to A with ||A||<=W/2. The second-moment difference is at most W^2 delta_i/4. The difference of squared means is at most W times W delta_i/2, hence at most W^2 delta_i/2. Variance is invariant under the shift, and independent initial copies have additive variance. Final fuel factors generally do not remain independent; their actual covariances must be retained. These extensive nominal-moment errors cannot be dropped by citing the improved channel estimate.

Thus fixed fresh-fuel accuracy can suffice for source-channel accuracy as M grows, while agreement with an extensive nominal energy budget requires a separate precision target. This is a conditional refinement of resource bookkeeping, not a free preparation mechanism.

---

## Part III: Exact-copy and unitary-block structured precision and actual fresh-fuel ledger, reproduced verbatim

This complete body retains its original status and exposure language. The wrapper records later exact acceptance and current scope. No source sentence, equation, constant or historical claim is rewritten here. The exact-copy/unitary-block assumptions here are distinct from Part I's broader implementation-error class.

# Structured fabrication precision with actual fresh-fuel bookkeeping

Status: root proposal, unaccepted until separately checked against the complete controller. This note was written before reading the worker derivation. It assumes the sequential interacting-copy construction in ROOT_PROPOSAL.md (683525ab) and the now-reviewed fresh-product lemma V2 (cffe4574); it supplies no native fabrication or preparation mechanism. No scientific run is made here.

## Data and ideal premises

There are M identical-chain fuels and M routers, source Hamiltonian H_A with 0<=H_A<=E I and spectral width W<=E, and work onsite energy H_work. Put H_0=sum_copies H_A+H_work, with an explicit norm upper bound B_0. The source may have an arbitrary passive reference. The ideal compensated program has L gates, prefix corrections Delta_j=W_j H_0 W_j*-H_0 of norm at most C, Delta_0=Delta_L=0, completed program commuting with H_0, exact router/work return, and one-head path transfer at T. Its clock coefficient is c=C+J, its nonnegative hopping amplitudes a_j have a_j<=J/2, and the adjacent sums are at most J. The ideal one-head Hamiltonian is unitarily equivalent to H_0+c I+A, with ||A||<=J.

The actual fuels are independent tau_i, independent of the source/reference and other resources initially. Let delta_i=||tau_i-sigma||_1, alpha=Theta/M, and epsilon_0=min(2,4Theta^2/M)+(2|Theta|/M)sum_i delta_i. With ideal resources and dynamics, the original source channel differs from U by at most epsilon_0, and the actual total fuel-energy change equals minus the actual source-energy change. The latter identity uses actual tau_i, not nominal sigma. Bounds can always be capped by 2 where they bound channel/state trace distance.

## A concrete positive structured error model

Keep the copies and work Hamiltonian H_0 exact. Replace each gate G_j by an actual unitary G'_j on the same support, each hopping a_j by 0<=a'_j<=J/2, and each cut correction by a self-adjoint Delta'_j on the same support. Require

    ||G'_j-G_j||<=gamma, |a'_j-a_j|<=rho,
    ||Delta'_j-Delta_j||<=zeta,
    c'=C+J+zeta.

The actual Hamiltonian is H'=H_0+sum_j n_cj Delta'_j+c' N_C+sum_j a'_j(clockhop_j tensor G'_j+adjoint). All terms remain supported where their ideal partners were; no new range or arity is inferred. The exact bound a'_j<=J/2 implies adjacent sums <=J. Each actual hopping link has the positive two-clock decomposition with its actual unitary. Since ||Delta'_j||<=C+zeta,

    H' >= H_0+sum_j[c'-(C+zeta)-a'_j-a'_(j+1)]n_cj >=0

on the full clock/data/work Hilbert space. This requires actual unitary gates and self-adjoint corrections; arbitrary unconstrained entrywise perturbations are not covered. The common additional clock coefficient zeta is an engineered positive margin, and is included in the actual mean energy.

On the one-head sector compare H'-c'I with H-cI. A diagonal block difference has norm <=zeta. Each neighboring off-diagonal difference has norm <=rho+(J/2)gamma, using a'<=J/2. A block tridiagonal row-sum estimate therefore gives

    kappa = zeta+2rho+J gamma,
    ||(H'-c'I)-(H-cI)||<=kappa.

The subtracted clock coefficients are scalar on the one-head sector and affect no channel. Also ||H'-c'I||<=B_0+J+kappa. Duhamel and the pure/mixed-state unitary trace-distance estimate, for every passive reference, give at observation time T+tau

    xi_dyn <= 2T kappa+2|tau|(B_0+J+kappa).

If the actual initial nonfuel resources differ in joint trace norm by eta from their ideal router/work/clock state, independently of source and actual fresh fuels, add eta by channel contraction. Define xi=min(2,eta+xi_dyn). The comparison is to the ideal controller supplied with the SAME actual fresh fuels. A possibly imperfect clock state is handled first by initial-state contraction; the one-head Duhamel estimate is then applied only to the ideal one-head preparation. No one-head norm estimate is applied to an arbitrary erroneous multi-head state.

Thus the actual source/reference channel is within epsilon_0+xi of U. The small-collision preparation improvement applies to fresh fuels only. It does not turn arbitrary correlated supplies or generic router/clock errors into M-independent local precision guarantees.

## Actual energy changes, rather than nominal absolute means

The reference ideal evolution supplied with actual tau_i returns the routers/work and conserves total bare energy at its endpoint. Since its source channel is within epsilon_0 of U, its fuel-energy change differs from minus the target source-energy change by at most W epsilon_0/2.

The actual and comparison evolutions have identical initial fuel states. Their complete final states have trace distance at most xi. The total fuel observable has spectral width M W. Centering that observable therefore gives

    |Delta E_fuels(actual)+Delta E_source(target)|
       <= (W/2)(epsilon_0+M xi).

This is a sufficient finite-error bound; it does not claim the M factor is necessary for every structured error. No nominal-initial-fuel M delta term enters this physical change. The M xi term measures the possible final-fuel energy effect of imperfect dynamics and nonfuel preparations. Comparing actual and nominal INITIAL fuel means and independent summed variances still incurs W sum(delta_i)/2 and 3W^2 sum(delta_i)/4, respectively. Final covariances cannot be dropped.

For source error budget epsilon>0 and energy-change error delta_E>0, one sufficient allocation is

    epsilon_0 <= min(epsilon/2,delta_E/W),
    xi <= min(epsilon/2,delta_E/(M W))

when W>0. These imply source error <=epsilon and fuel ledger error <=delta_E. At W=0 all source and fuel energy changes vanish, and only the channel budget remains. Choose M first from the ideal collision bound, then the runtime-dependent sigma and actual fresh-copy errors from the preparation term; no preparation cost model is supplied. The required small xi is attained mathematically with positive rational error allowances for zeta,rho,gamma,tau,eta; finite physical state synthesis is a separate premise.

## Exact initial moments when nonfuel preparation is ideal

For an exactly localized initial clock, ideal sharp routers/work and independent actual fuels, write mu_0=Tr(rho H_0) and v_0=Var_rho(H_0)=Var(H_source)+sum_i Var_(tau_i)(H_A). Then

    mean(H')=mu_0+c'+Tr(rho Delta'_0),
    Var(H')=Var_rho(H_0+Delta'_0)+(a'_1)^2.

The hop contribution follows from orthogonality of the clock endpoints and unitarity of G'_1; there is no missing covariance with that orthogonal component. Since ideal Delta_0=0, ||Delta'_0||<=zeta. Therefore the actual mean differs from mu_0+c by at most 2zeta, and the variance differs from v_0+a_1^2 by at most

    2 zeta sqrt(v_0)+zeta^2+J rho.

The symmetrized covariance estimate is Cauchy-Schwarz in the state seminorm; Var(Delta'_0)<=zeta^2. Also |(a'_1)^2-a_1^2|<=J rho because both amplitudes are at most J/2. These moment formulas are for the actual fabricated Hamiltonian and actual fuels. Imperfect nonfuel preparation must be accounted for by its actual moments or a separately charged full-energy norm bound. They do not follow from source-channel accuracy alone.

The remaining dependencies are the complete layout/resource theorem and its declared actual Hamiltonian. This note resolves no native supply, stopping or terminal-readout obligation. It introduces no new physical axiom, prompt change, or audit verdict.
