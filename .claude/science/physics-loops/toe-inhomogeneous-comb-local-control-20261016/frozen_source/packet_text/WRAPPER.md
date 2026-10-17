---
title: Conditional local control with unequal onsite gaps and a uniform logical word bound
claim_id: inhomogeneous_comb_local_control_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
conditional_surface_status: supplied noninteracting old generator, matched branches, local positive controls, readiness and externally calibrated schedules
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: false
upstream_dependencies:
  - local_conserving_preparation_bounded_theorem_note_2026-10-16
  - local_conserving_sparse_compiler_bounded_theorem_note_2026-10-16
pending_canonical_dependency: local_conserving_sparse_compiler_bounded_theorem_note_2026-10-16
runner: scripts/inhomogeneous_comb_local_control_2026_10_16.py
---

Claim type: bounded_theorem. Current mathematical source status: qualified conditional analytical support. This source-only publication draft has no canonical approval, base binding, PR or retained-audit verdict. The sparse parent's canonical identifier above is a proposed integration name, pending root resolution; its exact accepted sources are bound below and in PARENT_BINDING.json.

Can a local driven processor act on a register whose positive onsite gaps differ? The qualified construction attaches a reservoir branch with the matching gap to each old qubit. Branch gates and diagonal couplings between adjacent old sites implement a logical program while conserving every species charge. Separate final onsite phases remove free evolution without a common recurrence time. A second qualified argument bounds the logical word length uniformly over computable target matrices at fixed q. The old generator remains the actual noninteracting operator

    K_S=E0 I+sum_i Delta_i n_i,  E0>=0, Delta_i>0.

Arbitrary interacting old generators are outside the result. Matched new gaps, a vacant degree-three comb, all required control edges, full within-species SWAP, cross-species diagonal CZ, phase/timing references and independent readiness are supplied. Physical SWAP between unequal-gap old sites is not a permitted substitute. Number-changing preparation controls are additional permissions.

The comb decision is `41e4139b7fb4e69fd14ecdd12504bc2e4cd93724f21733b8cab41e5b99967e0c`, controlled by qualifications `b8e88b7456bd89e44863fc349c57892347fb51e43a79d1451215c35cf08d56f0`. The uniform-word decision is `bfb3169ad9f09e65d510378f23379ead74224b37c6cafe9f1a0112da01da36a7`, controlled by `217aa264b321a2350613bcd1349bf394151c4485d0a47a58f44d380b548fb780`. Their complete proofs, exposed reviews and qualifications follow unchanged. Earlier pending-status statements remain historical; the later uniform decision extends the fixed-word result within the same physical premises. Neither decision approves this new wrapper/code or canonical integration.

## Direct premises and complete physical contract

The direct published-source premise is [local conserving runtime and driven sine preparation](LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md), SHA256 `6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f`. The second direct premise is the qualified sparse compiler: original derivation `6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b`, acceptance `999446a20afe1516069bdd7abebba103e5cd16be70762c85b221e5d2e75d4cda`, qualifications `83b913c6b47ee8625cc15914759886e642515d02f284dc84a6b92d8e3ed54d3e`. Its canonical publication is pending. That source's q=1 complete-input compiler, including determinant phases and clean-ancilla return, is used. Its emitted-word fixture is not imported. The interacting-complement opportunity screen and the separate direct unequal-gap candidate are not mathematical parents.

Species i has M_i=L_i+2 battery qubits and one synthesis ancilla, with m_i=L_i+4 total sites including its old qubit. The common input is arbitrary on old/reference factors, tensor the declared independent resource state. Every battery, ancilla and reference output is retained. On complete product-charge blocks, the physical word C_P acts as the logical word V. Outside those blocks its action is the actual word-dependent product, generally not identity. Even two words with the same logical matrix can have different off-code extensions. The separate candidate's identity-complement contract is not adopted.

For d_i=2 sin(pi/[2(L_i+1)]), the complete input-isometry packet error is at most 2 sum_i d_i, hence the unhalved joint trace error is at most 4 sum_i d_i. This ideal packet error depends on the final logical action, not word length. Program, branch-compiler and implementation errors remain separate and accumulate through their actual interfaces. Clean-return estimates telescope on ideal prefixes; the actual correlated ancilla or reservoir is never reset between letters.

## Uniform word, time order and precision

For q>=2, d=2^q, p=d(d-1)/2 and T(1)=1, T(k)=2T(floor(k/2))+2T(ceil(k/2)), the qualified bound is

    R_full(q)=p[14T(q-1)+6(q-1)]+(3q-5)2^q+6,
    R(q)=(18q+1)R_full(q),   R(1)=1.

It includes both controlled polarities, determinant-projector scalar and logical routing returns. A finite U(2) angle grid with a strict certified Frobenius margin supplies a word of length at most R(q) for a computable unitary with certified entry enclosures. It requires no exact zero/angle-branch oracle. This is finite-error computable search, not polynomial classical time, favorable oracle latency or validation of an arbitrary floating matrix.

For equal branch L, choose the padded physical slot budget before angles and phases:

    Gbar=R(q)(1+131328 L^4),   tau=(Gbar+1)h.

Each species' final positive onsite phase is computed from this fixed tau and applied to all its sites, including ancillas. The full amplitude scalar is exp[-i(E0 tau/hbar+Phi)], with Phi=(pi/4)N_A+sum_actual_Z|phi| and any certified compiler scalar retained. Full SWAP and CZ have endpoint scalar one under their paid positive generators; their reserves remain in the ledger.

Sequential preparation uses one absolute carrier time and the full tau_p for every final battery phase. Its ideal input isometry is J_beta E, E=exp(-i tau_p K_S/hbar). Runtime must implement W=V E*, so W E=V. The uniform R(q) applies to W, which removes a timing fixed point. Classical compilation must finish before the unknown input arrives, or its actual waiting evolution must be included. No preparation phase, scalar or resource output is removed at composition.

For fixed q, gaps and supplied cap parameters, the qualified budget gives sites O(epsilon^-1), preparation time O(epsilon^-1), and nominal runtime O(epsilon^-4), uniformly over the stated computable targets. It excludes classical compilation time. One complete unhalved trace allocation is e_prep<=epsilon/6, 4pi q/(L+1)<=epsilon/6, and eta_program, eta_compile, eta_H, eta_t<=epsilon/12. The exposed review supplies explicit constants and noncircular integer choices.

**Two precision quantities must remain distinct.** The runtime phase-generator allowance delta_lambda is O(epsilon^5); cancellation-sensitive numerical inputs such as Delta and pi can require O(epsilon^9), since tau and k grow as O(epsilon^-4). Global runtime static/generator/area requests are O(epsilon^5), per-new-field requests O(epsilon^6), and post-off timing O(epsilon^2), under the specified error model. Preparation separately requires generator/area and carrier-phase requests O(epsilon^2), carrier-frequency and cancellation-input requests O(epsilon^3). Numerical old-H compensation is allocated inside eta_program. Resolved errors must not also be counted as another copy of their integrated residual. These requests are not microscopic calibration guarantees. Guards change tau and require recomputing every final phase.

## Strength, complete energy and remaining premises

The original comb body calls g/2 an added incident cap. The controlling correction is mandatory: g/2 bounds driven controls; new static fields require nominal added-static-plus-driven incidence Delta_max+g/2. The supplied calibrated full bound E0+Delta_max+2g remains available. Actual positivity, support, locality, incidence and slew require separate certificates; small trace or integrated generator error cannot establish them.

Nominal runtime conserves the full distribution of the same F=E0 I+sum_i Delta_i N_i and every species charge, including on arbitrary initial states. Same-F endpoints give zero net prescribed-drive work; absolute work is bounded by g(Gbar+sum_i m_i). Preparation supplies nominal battery mean sum_i Delta_i(L_i+1)/2, variance at most sum_i Delta_i^2(L_i-1)^2/4, and its separately paid work. Those product-state formulas do not describe arbitrary correlated actual outputs.

The old-energy target allowance is (sum_i Delta_i/2)(e_out+epsilon_S0); initial old error cannot be omitted. Complete resource moments use width sum_i(M_i+1)Delta_i, including ancillas. Battery-only moments may use sum_i M_i Delta_i. Covariance, growing observable norms, reserves and full vector phases stay explicit. Small trace error alone gives no accuracy-independent moment guarantee. Later storage needs the same actual free evolution or a new mismatch/noise integral. No microscopic drive-state return, native purity/control supply, autonomous preparation/halt, indefinite fresh-system reuse or measured-energy identification is proved.

## Evidence boundary

There are two relevant historical exact scientific executions: the comb review's q=2, L_i=1 complete 256-dimensional semantic word, and the uniform review's small controlled-SU(2), determinant-phase and adjacent-route matrices. Both have actual source/launcher/precheck captures, receipts and full streams. The first detects off-code identity and unequal-gap SWAP substitutions; the second detects omitted scalar and missing route return. They are finite discriminators, not a general emitted compiler, interval certificate, physical pulse simulation or independent replay. Reviews use the same model and share source exposure.

The sparse parent's earlier failed launcher before scientific execution, successful retry and evidence qualifications remain in recovery provenance. The separate direct candidate and comparison are preserved as exposed historical proposals, not a second accepted theorem. The new primary performs source-integrity checks only, with scoped metadata mutants. No scientific program is rerun by this draft, and unbound canonical use is refused. Source/body maps identify this wrapper as new prose and every unchanged body below.

