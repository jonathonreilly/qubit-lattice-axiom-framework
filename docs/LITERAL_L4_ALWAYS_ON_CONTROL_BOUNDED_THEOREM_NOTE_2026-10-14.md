---
title: Supplied weak-background control for the literal L4 model
claim_id: literal_l4_always_on_control_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: fixed L4 finite-horizon control with a chosen persistent many-body background and supplied ordinary-NN pulses, clean resources, clock, calibration and readout
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: conditional Duhamel and complete-channel comparison with all elapsed-time and scalar costs; identity helper evaluates no mathematics
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["joint_even_matter_finite_link_interface_bounded_theorem_note_2026-10-14", "finite_gauss_penalty_recovery_bounded_theorem_note_2026-10-14", "fixed_neutral_ray_preparation_bounded_theorem_note_2026-10-14", "coherent_binary_k_admission_bounded_theorem_note_2026-10-14", "uniform_local_gauss_penalty_recovery_bounded_theorem_note_2026-10-14"]
runner: scripts/literal_l4_always_on_control_identity_2026_10_14.py
next_trace_action: separate exact publication source and driver review, guarded root integration, regular PR and later independent retained audit
---

Claim type: bounded_theorem

# Supplied weak-background control for finite joint-lattice circuits

This source candidate assembles one conditional finite-model theorem. The complete proof below is the unchanged repaired V2, SHA256 `e853de3776a74c8ddb2cccb9d0967ac1d9974c5d45fbec473837ae19c9204972`. Root accepted that source after a separate full review, the two-paragraph scope repair, and a separate repair review; the current acceptance is `ALWAYS_ON_CONTROL_ROOT_ACCEPTANCE.json`, SHA256 `2ab6c3248585423dcd61f3eb94509026ede555616c65fe1217cf4fae9093b84d`. Root accepted the original assembly only in composition with the exact one-phrase framing overlay under ALWAYS_ON_CONTROL_ASSEMBLY_ROOT_ACCEPTANCE.json, SHA256 89891b291ae71a9982449a180b0c4338f4097f76238cc2bf35e42e7d8c95711d, following complete root composition review 82f8927a35c516bc9a651b955bb19c8eb14890cb7a5599daae852a41c5198520. This new publication rendering and driver require their own exact root acceptance. The original uncorrected wrapper and candidate are historical only. No retained audit, publication, or physical implementation follows from the source acceptance.

The model has the literal L=4 joint matter/link architecture: 1,344 active qubits in the ordinary open representative box with 262,144 sites. An arbitrary passive reference and dirty transit qubits are allowed under the specified input contracts. The fixed background is chosen as

`H_bg = alpha H_0`, with `H_0 = lambda_0 N_full + kappa B_*`.

All three coefficients are positive and selected before the unknown input or branch. The full penalty retains 704 local cycle projectors, 192 unused-link projectors and 64 squared Gauss operators. It has no Wilson-sector penalty. Its full-space gap statement and its reducing supplied-precode gap statement remain distinct. Neither preparation nor admission is assumed to stay in that precode while pulses act.

The result replaces exact background removal during the supplied finite gate words with a sufficiently weak *chosen* background, explicitly charged in error and elapsed time. It does not provide an attenuator for an already fixed physical drift. The background retains its many-qubit periodic terms; only the additional serial pulse terms have ordinary open-box nearest-neighbor support. The total generator is not asserted to be nearest-neighbor or positive.

For the literal coefficient bounds in the proof, write `b_*=(1728+192 sqrt(3))J_*`, `beta=9+2 sqrt(3)`, `C_0=6080 lambda_0+kappa b_*`, and `L_0=166 lambda_0+kappa beta J_*`. These are the stated full-space norm and listed per-site norm upper bounds. The full scalar is kept:

`c_0=688 lambda_0+kappa[(1/2) sum_v mu_v+(1/4) sum_e(2f_e(0)+f_e(-1)+f_e(+1))]`.

The corresponding scalar phase is part of the literal unitary. No energy recentering, positivity extension, or replacement of the whole-term cap by the separate L=4 Pauli refinement is made here.

For an ideal phase-exact finite pulse word, each pulse has its specified supplied bounded Hermitian generator and slot length `pi/J_p`. If `T_g^+` bounds actual pulse time, the background contribution to the complete output/reference trace error is `2 alpha C_0 T_g^+`. Equation (8) adds initialization, pulse-approximation and event errors. The refinement in section 8 also charges finite readout duration, actual timing, and supported Hamiltonian mismatch throughout the entire elapsed time. The stated local cap is `alpha L_0+J_a`, with precision margins required for the actual coefficients. Choosing small enough alpha gives a finite-horizon sufficient allocation; the free comparison interval `s` then takes physical time `s/alpha`.

The reused exact ideal words contain 871,249 pulses for the supplied neutral-ray preparation and 29,489,403 pulses for coherent binary admission. The summed count is 30,360,652. The preparation requires the specified active product input; admission requires its 2,309 clean factors. Dirty transit is returned by the ideal words, with actual output return controlled by the complete trace bound. The stated combined transit ledger is a conservative union bound, not a newly emitted concatenated word or an exact union census. Both unnormalized admission branches remain in the trace-preserving output; FAIL is not silently reset or projected into the target sector. The two accepted compressed word files are archived by exact byte identity, without decompression or replay in this assembly.

There are two independent small parameters. An effective wait of duration tau is physically `tau/(alpha kappa)` and has exact ideal propagator `exp[-i(tau/kappa)(lambda_0 N_full+kappa B_*)]`. Decreasing alpha controls the extra background accumulated during pulses. Decreasing kappa relative to lambda_0 controls the separately assumed initial-K penalty comparison. Common weakening alone does not improve that comparison. The source's two-ray calibration counterexample also rules out an inference that a fixed absolute background calibration error disappears as alpha tends to zero. Relative accuracy and the long elapsed time must be priced.

The scope repair is load-bearing. Complete-output finite histories use the global estimate (21) on ideal comparison inputs supported in K, followed by a global channel telescope; approximate actual inputs are separated first by a global triangle inequality. Without that ideal support premise, the comparison retains the full finite-penalty free evolution. The local estimate (23) can instead bound a requested *terminal* reduced region and its passive reference. It is not propagated through a later arbitrary global operation. Clean resources or counted resets, timing, factorized finite readout/error assumptions, and the entire readout time remain supplied. Mathematical record channels are not a free physical readout apparatus.

The separate review's exact SWAP counterexample to a general local-to-global telescope, including its source and original streams, is preserved. Its optional fixed-L=4 comparison between the numerical envelopes is also preserved, but it is not adopted as a new proof premise or added to V2. The only V1-to-V2 changes are the complete-output/local-terminal scope sentences at lines 248 and 313. Historical provisional or pending-review sentences inside the unchanged proof and archived records describe their original exposure times; they are not the current acceptance record and have not been silently overwritten.

The following five canonical notes supply six complete source bodies actually imported by the proof. Their exact unique body containment and byte ranges are recorded in `DEPENDENCIES.json` and `PARENT_BODY_RANGES.json`. A canonical note's other appendices are not automatically imported.

| Mathematical parent | Actual imported body and use |
|---|---|
| [Joint even-matter and finite-link interface](JOINT_EVEN_MATTER_FINITE_LINK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-10-14.md) | `34cbe355`: literal L=4 operators, coefficients, supplied code and geometry. |
| [Finite Gauss-penalty recovery](FINITE_GAUSS_PENALTY_RECOVERY_BOUNDED_THEOREM_NOTE_2026-10-14.md) | `bb2817d3`: full penalty, raw coupling, full-space bounds and global initial-K recovery. |
| [Fixed neutral-ray preparation](FIXED_NEUTRAL_RAY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-14.md) | `0e002497`: exact ideal word, phase/return semantics, clean input and resource ledger. |
| [Coherent binary K admission](COHERENT_BINARY_K_ADMISSION_BOUNDED_THEOREM_NOTE_2026-10-14.md) | `8abf93c7`: full binary ideal instrument, word, both branches and resource ledger. |
| [Uniform local Gauss-penalty recovery](UNIFORM_LOCAL_GAUSS_PENALTY_RECOVERY_BOUNDED_THEOREM_NOTE_2026-10-14.md) | `fca3350c` and `45ea7ab8`: repaired terminal local/reference estimate and whole-term cap, used here only at L=4. |

Duhamel comparison, channel contractivity and finite error telescoping are existing mathematical machinery. The NN synthesis candidate and sharper fixed-budget corollary in the original exposure list are overlap/context, not extra theorem premises of this result. Earlier accepted assembly code is reused only as a packaging pattern. Branch ancestry does not supply a mathematical premise, and this source assembly makes no proposed publication-graph count or actual branch-state claim.

Author, separate-review and root exposure records remain distinct. The separate reviewer sealed an assessment before opening the candidate body, but had the shared target/architecture; the exact first body-read wall time was not separately recorded. Root has a separately recorded preassessment and first body exposure. The assembly worker read the complete changed proof and the complete current review/disposition records; unchanged earlier premise coverage is reused only at exact identities. This is source-exposed, same-family work, not blind or model-diverse validation. Identity tools in this packet evaluate zero mathematical predicates and confer no new theorem acceptance.

The finite proof supplies no native dynamics, autonomous controller, mechanism for the chosen coefficient scales, physical identification, preparation of clean resources, experimental calibration certificate, uniform all-time/all-volume conclusion, or photon/continuum result. The complete proof and its narrower contracts control the claim.


<!-- BEGIN COMPLETE UNCHANGED ACCEPTED V2 BODY; historical status statements retained -->

# Fixed weak background during literal L4 preparation, admission and free evolution

**Status: source-exposed conditional composition candidate, not yet separately reviewed.** This note proves a finite error/resource prescription with one persistent, positively scaled copy of the accepted literal background and addressed ordinary-nearest-neighbor pulses added to it. It never switches that background off and never adds its negative. The scale must be a selectable, calibrated parameter of the supplied engineered model, fixed before the unknown input. No ability to attenuate an already existing physical Hamiltonian is derived.

The perturbation mechanism is standard and was already explicit in the binary-admission and NN-synthesis sources. The additional content is the literal composition: full N_full and its scalar, actual preparation/admission words, their dirty-transit/reference scope, both binary branches, the whole-term cap, and a single consistent free-time and calibration ledger. This is not a new generic controllability result. It does not certify the separate NN-synthesis candidate, whose body remains frozen and under review.

## 1. Exact supplied model and the two independent scales

All mathematical statements here concern the original L4 model on 1,344 active factors A inside the ordinary representative box `{0,…,63}^3`, with 262,144 physical qubit factors. The inactive factors are available for the already supplied control words. The background acts on the original active coordinates throughout routing; it does not follow a logical token that has been SWAPped elsewhere. An arbitrary passive reference R may be entangled with all otherwise arbitrary input/transit factors.

Use the literal signed A/B/cycle/Wilson, link and Gauss operators of joint source `34cbe355…`, and the unprojected cyclic coupling of accepted penalty source `bb2817d3…`. In particular,

    N_full = Σ_(704 local cycles c)(I−S_c)/2
             +Σ_(192 links e)|11><11|_e +Σ_(64 cells x)G_x²,
    V_e = i A_st(C_e−C_e†),
    C_e = U_e+|−1><+1|+|11><11|,
    |−1>=|01>, |0>=|00>, |+1>=|10>.

No Wilson penalty is present. The original full K requires all prescribed local cycles and all three + Wilson signs, valid links and G_x=0; it does not fix all matter occupations. N_full is positive with full-space gap 1, but its full kernel contains other Wilson characters. The supplied cycle/+++Wilson/link precode R₀ is reducing for N_full and every B term; on R₀ the penalty equals ΣG_x² and has gap 2 off K. Those restrictions will be used only for the later initial-K recovery comparison, never for the gate disturbance or physical cap.

Let B* be any fixed allowed static bare-coupling member, with coefficient budget J*≥0. Thus it contains the parent's occupation, intracell Hermitian hopping, electric-function and plaquette Hermitian terms, and real g_e V_e on the 192 streams. All specified coefficient magnitudes are at most J*, with `max_m|f_e(m)|≤J*`. Retain the full four-dimensional link function, including f_e(0) on |11>. The raw pair branches, cyclic wraps, orientations and spectator phases are unchanged. Define

    H₀ = λ₀ N_full + B₀,       B₀ = κ B*,
    H_bg = α H₀,              λ₀>0, κ>0, α>0.                 (1)

Choose λ₀, κ and α before the protocol and then hold them fixed. If a particular B₀ is already specified, one may simply use κ=1 and regard B*=B₀. Introducing κ separately is useful when initial-K recovery at a specified effective time is requested. The common scale α multiplies every term, including every scalar. Coefficient signs and complex phases are not altered by either positive scale.

Let

    b* = (1728+192√3)J*,     β = 9+2√3,
    C₀ = 6080λ₀ + κb*,      L₀ = 166λ₀ + κβJ*.              (2)

The accepted full-space whole-term bounds give `||H₀||≤C₀` and a per-site interaction-norm sum at most L₀. These are upper bounds, not exact total operator norms. In particular the cap does not use the old 11J budget for the different, compressed charged stream. It pays every cycle, unused-link and Gauss-square term even when an ideal input is in K.

For clarity, the literal identity coefficient is

    c₀ = 688λ₀ + κ[ (1/2)Σ_v μ_v
                      +(1/4)Σ_e(2f_e(0)+f_e(−1)+f_e(+1)) ]. (3)

The 688 comes from 704/2 + 192/4 + 64·18/4: each cycle is nonidentity, and the eighteen distinct signed Pauli words in 2G_x have no identity cross product. The matter hopping and bare-stream terms retain a nonidentity X/Y on their edge, hence have zero trace. A plaquette product has zero trace because each disjoint link U or U† has zero trace. Occupations have identity coefficient 1/2; the four link eigenvalues give the electric coefficient in (3). Thus the other displayed families have zero full-space identity coefficient. Equation (3) is retained, not used to shift the physical Hamiltonian. During a duration t it contributes phase exp(−iαc₀t); this is included in the vector comparison below. An unconditional channel is insensitive to a common scalar phase, but that fact does not remove any literal term from the declared norm/energy ledger. H₀ and the controlled total generator need not be positive.

The background retains its supplied periodic, multi-qubit support: for the exact L4 whole-term contract, arity at most 30 and periodic diameter at most 32. Some representative open-box separations are long. Only the **added control pulses** below have ordinary one-site or distance-one two-site support. Their sum with H_bg is not asserted to be an ordinary-NN generator as a whole.

## 2. Control, input and readout premises

The following are engineering inputs, not consequences of the physical axioms.

* The chosen literal H_bg is present on A at all times. Its positive common scale and static coefficient data are supplied and can be specified to the required certified precision. This is selection of one member of a supplied family, not an inferred physical tuning operation.
* The existing external controller can apply the displayed one-site or ordinary-NN pair pulse matrices at addressed box coordinates, with a known strength bound and finite timing/calibration error. It has the same origin/coframe and external serial clock required by the accepted words. No new autonomous clock is constructed.
* Required clean factors are supplied at the start of the declared protocol, with a joint initialization error bound. Neutral preparation requires all 1,344 active factors initially |0>. Admission instead permits arbitrary active input but requires the specified 2,309 clean work/flag factors. Making these inputs under the persistent background is not a result of this note.
* Apart from the specified active background and addressed pulses, the other box factors and R are passive. Unknown extra drift must be separately bounded by the integrated-error ledger in §8. It cannot be renamed part of a freely selectable αH₀ without evidence.
* Admission uses the previously supplied final flag instrument and keeps every finer work register coherent until uncomputation. A finite-duration physical readout needs the additional explicit duration/factorization or error contract in §8. The abstract instantaneous instrument alone does not provide that apparatus or its duration.

There is no cancellation Hamiltonian. At a pulse time s, the ideal actual generator is exactly

    H_actual(s)=αH₀ + K_j(s),                               (4)

where K_j is the chosen one-site/ordinary-NN term. During a free interval it is αH₀. Pulse matrices are not obtained by subtracting H_bg. Incidental algebraic overlap of a pulse with a background term is not a separately supplied compensator.

For the finite alphabet used in preparation/admission, no effective matrix-log selection is needed. Fix an ideal pulse strength J_p>0 and a common slot duration `h=π/J_p`. For G in `{H,X,Z,CNOT,SWAP}`, use

    K_G=(J_p/2)(I−G).

Each G is a Hermitian involution, so `exp(−ihK_G)=G` exactly, including its scalar phase, and `||K_G||≤J_p`. On one qubit, use `K_S=−(J_p/2)|1><1|`, `K_(S†)=+(J_p/2)|1><1|`, `K_T=−(J_p/4)|1><1|`, and the opposite sign for T†. All generate the stated gates at the same h, with norm at most J_p. On an ordinary adjacent pair the supplied matrices can equivalently be written

    K_CNOT=(J_p/4)(I−Z_control)(I−X_target),
    K_SWAP=(J_p/4)(I−XX−YY−ZZ).

Their full supported norms are J_p. These are concrete supplied controls of the same alphabet, not a claim that an arbitrary three-body gate or native compensator is available. Negative one-site phase generators were already permitted by the control contract. They do not assert a positive physical energy law.

For a serial G-pulse word the ideal control duration is

    T_g = Gπ/J_p.                                          (5)

Let T_g⁺ be a certified upper bound on the actual total slot duration when precision errors are included. A robust implementation can design at J_p and reserve a larger actual control bound J_a≥J_p. The actual pulse generators must obey the same support restrictions and norm at most J_a; small endpoint gate errors alone would not establish those restrictions.

## 3. Finite-protocol comparison with one fixed α

Consider any fixed finite sequence of these finite words, forward free intervals and supplied local instruments. It may include old classical records and finitely many classically selected branches. The reference is arbitrary. A state-dependent value of α is not allowed. For an aligned finite classical protocol, bound each stage by the largest word duration/error over its preceding record values and add those stage bounds; this is sufficient without evaluating any unknown state or branch probability.

The comparison protocol turns the background off **only as a mathematical reference during the pulse words**, executes their exact intended products, and uses the intended finite-penalty unitaries

    U₀(s_j)=exp(−is_j H₀),       s_j≥0,

in its free stages. The physically implemented free duration is

    t_j=s_j/α.                                             (6)

There is no switch-off in the implementation (4). Equation (6) gives the exact identity `exp(−it_jH_bg)=U₀(s_j)` on the full active space. Consequently planned free evolution contributes no approximation error, regardless of its duration. It would be incorrect to charge the intended free background as unwanted drift for the whole elapsed experiment.

With exact pulses, exact stated initialization and the same ideal instantaneous instruments in both protocols, their final complete output states obey

    ||ρ_actual−ρ_reference||₁ ≤ min{2, 2αC₀ T_g}.           (7)

This is uniform over every active/transit/reference input for which the reference protocol is defined. It includes clean work, all returned transit factors and classical outcome registers; it is not an expectation-value or probability-only statement. No K or reducing-sector premise is used in (7). Clean-input premises are needed for the *meaning* of the reference preparation/admission operation, not for the perturbation estimate on the full carrier.

If the j-th control-only implemented primitive has complete operator error δ_j from the intended gate, its pulse Hamiltonian obeys the stated actual support/cap, and the actual total control duration is bounded by T_g⁺, then a sufficient generalization is

    E_ctrl = ε_init + 2Σ_jδ_j + 2αC₀T_g⁺ + Σ_l ε_event,l,   (8)
    ||ρ_actual−ρ_reference||₁ ≤ min{2,E_ctrl}.

Here ε_init is the joint initial trace-norm error. The supplied event bounds ε_event,l must include any error/duration not yet accounted for at those stages; §8 supplies a concrete finite-readout option. Error symbols are full trace/diamond conventions, with no hidden factor 1/2.

### Proof of (7) and (8)

On one pulse interval let V solve `iV'=K(s)V` and U solve `iU'=(αH₀+K(s))U`, both initially I. Differentiating V†U gives a unitary interaction-picture propagator generated by `αV†H₀V`. Integration and unitary invariance of operator norm give

    ||U(h)−V(h)|| ≤ α∫_0^h||H₀||ds ≤ αC₀h.               (9)

The background has not been conjugated away physically; its conjugation in this proof is only a norm estimate. It is immaterial whether a continuous pulse or intermediate SWAP state lies in a constraint sector. The complete original active-space operator norm is still bounded by C₀ after tensoring all work, dirty transit and R. Concatenating intervals telescopes in operator norm because every factor is unitary, giving `||U_word−V_word||≤αC₀T_word`. Add the separate control-only errors to get `αC₀T_word⁺+Σδ_j`.

For unitaries U,V and any density operator ρ, including an arbitrary passive reference, add and subtract UρV† to obtain

    ||UρU†−VρV†||₁ ≤ 2||U−V||.                           (10)

This also bounds the complete channel difference. All subsequent identical quantum instruments/channels contract the trace norm of Hermitian differences. Replacing each word by its intended word, one at a time, proves the additive global protocol bound. The intended free stages are identical by (6). Initial-state and supplied event errors telescope in the same way.

For a classical record b, the input is a positive block family ρ_b with total trace 1. A stage error bounded by e_b on normalized inputs contributes at most `Σ_b e_b trρ_b≤max_b e_b`. Thus summing stagewise branch maxima is sufficient for a finite adaptive protocol, without dividing by rare outcome probabilities. This argument does not claim coherent superpositions of different invocation times, or an autonomous implementation of classically chosen stopping times. Any physical idle padding is part of the scheduled duration and must be charged if the reference protocol freezes during it.

## 4. Total listed system cap and a computable choice

For the fixed whole-term decomposition inherited in (2), and one addressed pulse at a time,

    sup_i Σ_(listed terms touching i)||h_i(s)|| ≤ αL₀+J_a. (11)

This holds at every time and on the full physical carrier. The fact that logical tokens move does not change the fixed-site interaction budget. Scalar parts remain inside their literal terms. It is a mathematical interaction-norm cap for the listed background and pulse Hamiltonians, not a bound on the energy or autonomous hardware cost of the classical controller, initialization apparatus or readout apparatus.

Given a positive cap Λ, choose J_a=Λ/2. For exact pulses one may take J_p=J_a. For an amplitude margin, take J_p=Λ/4 and require actual same-support pulse errors in norm to be at most Λ/4; then J_a=Λ/2 is still valid, and the slower J_p is used in (5). Given a positive background-during-control error allowance ε_bg and a certified finite T_g⁺, choose any positive α satisfying

    α ≤ min{1, Λ/(2L₀), ε_bg/(2C₀T_g⁺)}.                  (12)

When T_g⁺=0 omit its denominator. Both C₀ and L₀ are positive because λ₀>0. This proves the cap and makes the third term of (8) at most ε_bg. The same α works for all input states, all passive references and every branch included in the fixed stagewise bounds. It is chosen once, not changed between preparation, admission and free evolution.

If finite readout/dead intervals of total length at most T_aux are charged as in §8, replace T_g⁺ in the final restriction by `T_g⁺+T_aux`. With exact nominal pulses/free durations, the total elapsed time for the corresponding nonadaptive schedule is bounded by

    T_phys ≤ T_g + T_aux + (Σ_j s_j)/α.                    (13)

Equality holds if the auxiliary slots are padded to their stated total T_aux; that padding is included in the background error. Actual pulse/free-duration errors require the actual upper bounds described in §8.

The declared protocol is finite, but (12) can make (13) extremely large. This is a sufficient estimate, not a practical-efficiency statement or a lower bound on necessary time. It is not uniform over arbitrarily many repeated words at fixed α. It is also not a volume-independent global error theorem: C₀ and the actual words here belong to fixed L4.

The choice can be effective without state matrices or a global diagonalization. Supply computable coefficients, positive implementable operating caps and certified finite duration bounds. Use rational upper bounds for C₀,L₀,T_g⁺, and a positive certified lower bound on the available cap, then choose a positive rational below the right side of (12), with slack. For example `1728+192√3<2061`, `9+2√3<13` and `π<22/7` give conservative rational bounds. Positivity of a supplied computable λ₀ requires a certified positive lower bound or refinement until one is obtained. This is a finite parameter/error prescription; it is not proof that physical hardware can realize those data.

## 5. Literal preparation and binary-admission applications

### 5.1 The fixed neutral ray

Use the accepted preparation word unchanged: 871,249 physical primitives, each one-site or ordinary-NN, with its actual chronological H/S/X/CNOT/SWAP list. Its ideal whole-box unitary is `U_prep,A⊗I_other`. On the supplied 1,344-factor active product it prepares the particular neutral η ray with all three specified Wilson signs and links 00. The 21,747 used idle transit factors may be arbitrary and reference-entangled. The initial active |0> product is not in K: every B_v=+1 and G_x=3 at zero flux. Neither the pulse proof nor its error bound assumes otherwise.

With the persistent background, its final complete state differs from the ideal neutral ray times the original transit/reference state by at most

    ε_init + 2Σ_(prep)δ_j + 2αC₀·(871249π/J_p),            (14)

with actual-duration replacements as necessary. This makes return approximate to the stated global accuracy. It does not claim exact tensor return under a nonzero background. Subsequent identical full-H₀ free evolution cannot amplify (14) in trace norm, however long its rescaled physical duration. To compare that later evolution to the compressed target, apply the sector bound to the ideal prepared K state and add (14); never apply a K-only premise directly to the actual perturbed state.

### 5.2 Full K-admission, including FAIL

Use the accepted 29,489,403-primitive word unchanged, with its 2,309 supplied clean work/flag factors. It acts on arbitrary active input, arbitrary dirty transit and any passive reference. Its ideal action on clean work is

    |ψ>_A|0>_W|0>_F ↦ P|ψ>_A|0>_W|1>_F
                          +(I−P)|ψ>_A|0>_W|0>_F,          (15)
    P=P_K.

Every finer cycle/Wilson, occupation, link and Gauss register has been uncomputed. The full P here is not the fixed neutral-ray projector. In particular no list of chosen B occupation signs is added. Returned routing is an identity on arbitrary entangled transit for the *ideal product*. Equations (9)–(10) then compare the persistent-background word to this exact full product without assuming blank transit or intermediate K preservation.

After the supplied flag instrument, the reference channel is exactly

    I_K(ρ)=|PASS><PASS|⊗PρP + |FAIL><FAIL|⊗(I−P)ρ(I−P),   (16)

with the identity on transit/reference and returned |0><0| work understood. Both blocks are unnormalized. For the coherent word and flag readout the full output bound is

    ε_init + 2Σ_(adm)δ_j
      +2αC₀·(29489403π/J_p) + ε_event.                    (17)

It controls within-PASS and within-FAIL coherence, quantum correlations with the reference, and approximate return of the fine work and transit. It does not replace (16) by a finer measurement or discard a residual fine archive as harmless. It neither repairs FAIL nor establishes its subsequent K membership.

If normalized postselected outputs are requested, a separate lower bound p_min>0 on the ideal selected probability is necessary. When the unnormalized error is E<p_min, the actual selected probability is nonzero and a sufficient normalized trace error is `min{2,2E/p_min}`. No such normalization is used in (16)–(17).

### 5.3 Actual counts when both existing words are concatenated

Preparation followed by admission uses

    G_pa=871249+29489403=30360652,
    T_g=30360652π/J_p.                                    (18)

This is concatenation of the two already emitted words, not a newly emitted or executed gate stream. In this particular ideal input case PASS is certain; the arbitrary-input admission theorem above, separately, covers both branches.

There are 1,344 active factors and 2,309 additionally clean work/flag factors. Preparation may route through those clean factors, but its ideal identity on all nonactive factors returns them, so the accepted admission premise follows. For an actual perturbed preparation, its global error is propagated by contractivity, rather than assuming the actual work is exactly clean again. The admission dirty capacity is 258,491 factors. The union of dirty factors used by the two schedules is at most `21747+74450=96197`; some preparation transit may instead be admission work or overlap the admission transit. Thus a conservative bound on all initial active/work and needed transit factors is `1344+2309+96197=99850`, within the same 262,144-factor box. This is an upper bound from the pinned counts, not a new exact union census.

For this composition, (12) becomes the explicit sufficient pulse-background restriction

    α ≤ ε_bg J_p / [60721304π C₀]                         (19)

in addition to the cap restriction, before adding readout/idle durations. All pulses, including the millions of return SWAPs, have been counted. No per-site gate-incidence maximum replaces this full global error/time cost.

## 6. Free evolution and the separate recovery choice

Let `A*=P_K B* P_K` on K. Common attenuation by α alone does not improve recovery. At physical free duration

    t_free=τ/(ακ),       τ≥0,

one has the exact all-input identity

    exp(−it_free H_bg)=exp[−i(τ/κ)(λ₀N_full+κB*)].         (20)

The right side is independent of α. Its virtual shifts and off-code effects remain exactly those of the accepted finite-penalty problem with ratio κ/λ₀. Thus “α small” cannot replace the recovery hypotheses.

For a simple explicit fixed-L4 global corollary, reuse the accepted primary bound without sharpening its gap. If J*>0 and

    κb*/λ₀ ≤ 1/4,

then on initial states supported in K, including arbitrary passive references, the full physical output at (20) differs from the embedded compressed evolution exp(−iτA*) by at most

    E_pen,global(τ) = min{2,
                  (2κb*/λ₀)(3+5τb*)}.                    (21)

Indeed insert B=κB*, b=κb*, T=τ/κ into the primary theorem. No full-space input claim follows from this substitution. For a finite effective horizon 0≤τ≤τ* and positive allowance ε_pen, a sufficient independent choice is

    0<κ ≤ min{1, λ₀/(4b*),
                  ε_pen λ₀/[2b*(3+5τ*b*)]}.              (22)

After fixing κ, choose α by (12) using (2). Thus accuracy and the total listed cap can both be achieved conditionally with positive finite parameters, at the expense of the longer physical time τ/(ακ). When J*=0, B*=0 and the K evolution is stationary; (21)–(22) need no division by b*. This special case does not make arbitrary off-K inputs stationary under N_full.

One may instead request only a region S of s≥1 physical sites and its arbitrary passive reference. The accepted direct local estimate and budget supply, at L4,

    g*=(10+11√3)J*,  k=57, c=60,
    λ₀≥16πkκg*,
    E_pen,local(τ) ≤ min{2,
       8πcs(κg*/λ₀)[3exp(2kg*τ)−2]}.                     (23)

This follows by putting physical λ=αλ₀, drive scale ακ, and time τ/(ακ) into that estimate; α cancels in both the premise and result. A sufficient κ for ε_pen over τ≤τ* is the minimum of 1, `λ₀/(16πkg*)` and `ε_pen λ₀/[8πcs g*(3exp(2kg*τ*)−2)]`. The local theorem's initial-K/reducing-sector and exact-static-coupling hypotheses remain necessary. Its larger-volume uniformity does not make the present gate words, their global drift costs, or this preparation/admission construction all-volume results. The optional use of (23) is not a replacement for the global bound (7) during non-K control stages.

### Both admission branches after a free interval

For arbitrary ρ including transit/reference, take the reference complete channel after admission and forward free evolution to be

    Ψ(ρ)=Σ_(b=PASS,FAIL)|b><b|⊗U₀(τ/κ)P_bρP_b U₀(τ/κ)†,
    P_PASS=P,  P_FAIL=I−P.                                 (24)

The all-input gate/readout error (17) compares the actual experiment to (24). No recovery premise is needed on either branch for this statement.

A valid partially recovered target replaces only the PASS block in (24) by

    |PASS><PASS|⊗exp(−iτA*)PρP exp(iτA*),                 (25)

and leaves FAIL as the literal finite-penalty evolution. The result is still trace preserving as a binary-output channel. If p=tr(Pρ), (21) contributes at most p E_pen,global to its complete trace difference; using the bound E_pen,global is sufficient without knowing p. The proof is to normalize the ideal PρP only inside the estimate when p>0, apply the K theorem with its full reference, then multiply by p. At p=0 the block is zero. No assertion is made about compressed FAIL dynamics or actual exact postmeasurement K support.

For a complete-output finite history, each recovery replacement uses the global bound (21) on a *comparison input* supported on K, and those global errors add under subsequent channels. A prior approximate implementation need not be exactly in K: the error is first separated by a global triangle inequality. If no ideal K-support premise holds before a free stage, retain its full U₀ stage. Equation (23) may instead be used for a requested terminal reduced region and its passive reference; that local estimate is not propagated through a later arbitrary global operation. Repeated readouts require the corresponding fresh clean resources or explicitly counted resets; none is free in the generic finite-history statement.

## 7. Why this is a meaningful but limited change of premise

The accepted preparation/admission contracts originally require drift removal during their pulse words. The construction above replaces that requirement, for the declared finite schedule, by selection of a sufficiently weak *persistent* supplied background and a global error tolerance. It does not require knowing the input or fine syndrome, and it covers all reference/dirty-transit correlations. One background scale handles every stage, including preparation outside K.

This is a real conditional switching reduction inside the given family, but not removal of the physical background resource. The original joint family permits finite real/complex coefficients and the penalty construction permits a positive λ; the accepted slowdown corollaries already make positive coefficient choices. Those mathematical existential choices do not prove an attenuator or a native ability to choose α. Merely renaming the time unit of a fixed physical H changes the pulse strength and clock unit as well and does not change the physical background-to-control ratio. If a pre-existing α and cap fail (12), this proof provides no desired accuracy guarantee; it also provides no impossibility theorem.

The sharper gap-2 fixed-budget corollary is already available for initial-K evolution and could improve (22). It is not needed here. It cannot justify omitting cycles/link penalties while preparing or extracting syndromes, or lower the full physical cap from 166λ₀ to a Gauss-only price. Similarly, the earlier NN-synthesis candidate already states a generic residual-drift bound. Its pending scientific acceptance is irrelevant to this self-contained composition, which imports only the accepted preparation/admission words and accepted literal norm/recovery premises.

The external schedule, supported pulse family, clean inputs and flag readout are still supplied. No physical work reservoir, positive energy zero, clock preparation, native two-site realization of H_bg, all-L gate compiler, autonomous stopping, odd-Fock encoder, continuum or photon claim follows.

## 8. Duration, precision and finite-readout accounting

### Control precision and initialization

For constant ideal/actual pulse generators K_j and Khat_j on the same support, with actual norm at most J_a, nominal duration h_j and actual duration hhat_j, a sufficient control-only operator error is

    δ_j ≤ h_j||Khat_j−K_j|| + J_a|hhat_j−h_j|.             (26)

This follows by Duhamel at the same time followed by a time telescope. The actual total duration is at most `Σh_j+Σ|hhat_j−h_j|`; use that bound in (8),(12). For a G-pulse protocol a sufficient uniform allowance is `δ_j≤ε_pulse/(2G)`. These are calibration requirements, not demonstrated hardware performance. The amplitude margin in §4 is separate from the accuracy allowance.

The initialization condition is a joint trace bound at the start of the protocol, including every intended correlation with arbitrary input/transit/reference. Unknown transit states are not errors because the ideal operations act as the identity on those factors. Clean state preparation is not derived or assigned duration zero. If it is to be carried out as an additional physical operation, its duration, cap, initial-state contract and error must be supplied or proved separately and added. In particular the neutral active-product input cannot be obtained for free by declaring it a low-penalty state: it is not one.

### A finite flag-readout interval

The accepted admission source supplies a flag instrument but no physical duration. There are two honest uses of that premise here. One may retain it as an abstract boundary event, making no finite-apparatus claim. Alternatively supply a finite interval τ_R≤T_R and a local readout channel acting only on the flag/apparatus, with complete error ε_R, while the background acts only on the original active A. If the total readout dynamics factorizes into those disjoint operations, then even on an entangled active/flag/reference input its channel is the flag channel composed with free active evolution exp(−iατ_RH₀); the two commute as channels.

Relative to a reference readout that freezes A, this gives the explicit event bound

    ε_event ≤ ε_R + 2αC₀T_R.                              (27)

This is a supplied factorization/error contract for the readout apparatus, not a derivation of measurement from a Hermitian generator. Sum the known T_R into T_aux in (12)–(13). The apparatus's own strength/energy/clean record resources are not bounded by (11) unless their separate supported generators and cap are also supplied. The flag is not an original active site, so its disjointness from H_bg is genuine; the microscopic readout apparatus is still an external premise.

If a known readout duration is instead counted as part of a subsequent free stage s/α, shorten the remaining wait to `s/α−τ_R`, provided this is nonnegative. Commutation gives exactly the intended total U₀(s) on both outcomes, so the background part of (27) can then be omitted. If the branch requires zero/too-short free time, or the duration is unknown, that subtraction is unavailable; retain a certified charge or leave the physical completion open. Neither α selection nor an ideal projector supplies an unknown readout duration or an archive-free instrument automatically.

### Background and free-time precision

The main statements assume the literal static αH₀. Suppose the actual background on A is `αH₀+Δ(s)` with a certified full-space norm bound and the same declared support/cap contract, and all free durations are known. Duhamel over the **entire elapsed time**, including the long free intervals, adds

    E_bg,precision ≤ 2∫_0^(T_phys)||Δ(s)||ds.               (28)

The intended αH₀ during free evolution was not an error; its mismatch Δ is. A local interaction-norm bound alone does not replace the global norm in (28) for this all-input L4 comparison. For static coefficient errors in H₀, a sufficient complete bound η₀≥||Hhat₀−H₀|| is

    η₀ = 6080|λhat₀−λ₀| +Σ_v|μhat₀,v−μ₀,v|
       +Σ_(intracell uv)|that₀,uv−t₀,uv|
       +Σ_e max_m|fhat₀,e(m)−f₀,e(m)|
       +2Σ_p|ζhat₀,p−ζ₀,p| +√3Σ_e|ghat₀,e−g₀,e|.         (29)

Here the subscript 0 means the already κ-scaled B₀ coefficient, and the exact signed operator dictionary is unchanged. Each factor is the full-operator term bound from the accepted model. Thus (29) includes the full scalar rather than only off-diagonal matrix elements. All actual coefficients must retain the Hermiticity conditions. To describe the actual Hamiltonian itself as a member of the positive-penalty family, also certify λhat₀>0; effective refinement can enforce this because λ₀>0. Any additional operator mismatch needs its own certified bound.

If the actual common scale is αhat>0, then

    ||αhat Hhat₀−αH₀|| ≤ |αhat−α|C₀+αhatη₀.              (30)

At a wait of length τ/(ακ), the leading trace error from (28),(30) is bounded by

    (2τ/κ)[ (|αhat−α|/α)C₀ + (αhat/α)η₀ ].              (31)

Common weakening therefore requires relative scale control, or a calibrated inverse-time schedule using the actual scale. A fixed absolute error in an unrelated drift is not suppressed by α and can become more costly as time grows. An effective base-coefficient prescription must likewise use the finite base time τ/κ, not assume α makes coefficient errors harmless. Equation (28) can cover small perturbations that break exact integer/commuting structure at fixed L4; it is not a new volume-uniform robustness version of the local averaging theorem.

For a planned free interval s_j/α actually lasting t_j, the exact-model timing charge is at most

    2C₀|αt_j−s_j|.                                       (32)

Add (32) over free stages, (28) for background mismatch, (26) for pulse error, (27) for finite readout and the joint initialization error. The final complete trace bound is the minimum of 2 and that sum together with `2αC₀T_g⁺`. A requested complete compressed PASS/input-K target additionally pays the global bound (21). If only a terminal reduced region and its passive reference are requested, (23) may be used for that terminal comparison; it supplies no global channel telescope. Actual elapsed-time upper bounds, rather than nominal times alone, must be used when charging (28) and the cap must hold for the actual Hamiltonian coefficients. These clauses price timing and precision as required supplies; they do not manufacture an experimental certificate.

For an explicit sufficient calibration allocation, let T⁺ be a certified positive upper bound on the actual entire duration, and reserve ε_cal>0 for (28). Strengthen the nominal background allocation to `αL₀≤Λ/4`, keep J_a=Λ/2, and require

    |αhat−α| ≤ min{α/2, ε_cal/(4C₀T⁺), Λ/(8L₀)},
    η₀ ≤ min{ε_cal/(6αT⁺), Λ/(12α)}.                       (33)

Then αhat≤3α/2 and (30) gives `2T⁺||αhat Hhat₀−αH₀||≤ε_cal`. When η₀ is the coefficient **term-sum certificate** (29), it also bounds the per-site load of Hhat₀−H₀ in the same labelled decomposition. Consequently the actual background's per-site load is at most `αL₀+|αhat−α|L₀+αhatη₀≤Λ/2`, and adding the actual pulse cap still gives Λ. An arbitrary operator-norm certificate with no supported interaction decomposition would not by itself prove this cap. This explicit choice is sufficient, not optimal. For q>0 free stages a sufficient uniform timing allowance is `|t_j−s_j/α|≤ε_time/(2qαC₀)`; require the resulting durations to remain nonnegative and include their upper bounds in T⁺. Gate, readout, initialization and recovery allowances are separate positive parts of the requested total error. Thus all tolerances can be prescribed before the unknown input, but their physical achievement remains supplied.

## 9. Exact counterexamples to two tempting inferences

First, equation (20) is an operator identity on the actual literal carrier. At a fixed effective τ and fixed λ₀,κ,B*, lowering α changes physical time but not the free output at all. Any finite-penalty virtual/leakage error already present in that output remains. The accepted one-bond and mixed-bond nonzero virtual terms cannot be set to zero by common attenuation. No selected numerical run is needed to establish this failure of inference.

Second, relative calibration is load-bearing even inside K. Let ψ₀ be the accepted neutral ray, and let `ψ₁=A_(0,3)ψ₀` in cell (0,0,0), with the literal `A_(0,3)=X₁Z₀`. Both are orthogonal K vectors, with n₀ψ₀=0 and n₀ψ₁=ψ₁. This is the already checked neutral-wrong-ray witness, not an assumed odd-sector state. Choose the allowed B*=μn₀ with μ>0 and all other coefficients zero. On the two-ray span, N_full=0. For the initial state

    (ψ₀|0_R>+ψ₁|1_R>)/√2,

the intended wait τ/(ακ) produces relative phase exp(−iμτ). If the true background instead has common scale α+d, then the relative phase is exp[−i(1+d/α)μτ]. Direct subtraction of the two pure-state projectors gives full trace error

    2|sin(d μτ/(2α))|.                                    (34)

The same formula follows from the two nonzero eigenvalues of the difference of the resulting 2×2 density matrices. For fixed d>0, μτ>0, choose `α_n=dμτ/[(2n+1)π]`; then α_n tends to zero while (34) equals 2. The actual scale α_n+d stays positive. This need not violate a strength cap: choose d small enough that `2dL₀+J_a≤Λ`, then take n large enough that α_n≤d. It is an exact allowed two-ray witness to failure of an unqualified fixed-absolute-scale-error claim. It does not disprove the conditional prescription with a certified relative error or recalibrated stop time. No program was executed to turn this algebraic example into a PASS count.

## 10. Source exposure, evidence and remaining limits

`PREMISE_SCREEN.md` records the exact-source overlap judgment and ranked next resource interfaces. `SOURCE_EXPOSURE.json` records full source hashes, read/reused coverage and acceptance roles; `SOURCE_FINAL_REFRESH.json` is a final identity refresh of that same exposure, not a claim of rereading every body. `WORD_IDENTITIES.json` binds the two unchanged compressed physical words against their original source freezes; no large gate stream was replayed or newly emitted. The underlying scientific sources are the unchanged accepted joint, penalty, uniform-budget, preparation and admission bodies. Their original status paragraphs and preserved failed controls remain historical; their later root acceptances, not rewritten source prose, establish their current conditional-source status. The separate NN-synthesis body is exposure/overlap only and remains under review.

Complete prior identity-bound proof coverage was reused where specified; the current task reread all uniform-budget, preparation and admission arguments, the complete repaired direct local estimate, and the load-bearing literal coefficients, penalty scopes, resource and residual-drift passages. One initially truncated display of preparation controls was repaired by an explicit range read. No truncated display is counted as completed fresh coverage. No old compiler, checker, scientific suite or numerical experiment was run. The new analytic work is the finite-protocol proof, literal parameter/count substitutions and exact calibration witness above. Deterministic hash/inventory work is recorded separately and is not scientific verification.

This candidate remains source-exposed and requires separate review before acceptance. Its most consequential unresolved physical premise is the ability to specify/calibrate the one weak positive background, followed by finite-duration clean-input/readout resources. If that selectable scale is unavailable, a genuinely stronger next target would be a priced, arbitrary-input/reference-safe fixed-drift control/refocusing construction for this actual interacting generator. The present sufficient bound neither solves nor rules out that target.

Only this assigned output directory was written. No parent source, canonical repository, Git/index/PR, operational checkpoint, physical axiom, editable prompt or other chat was changed. The selected model and reasoning effort were preserved, and no delegation occurred. The final source freeze is an identity/evidence record, not an audit verdict or proof by hash.

<!-- END COMPLETE UNCHANGED ACCEPTED V2 BODY -->
