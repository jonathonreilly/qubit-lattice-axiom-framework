---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
source_only_proposal: true
wrapper_root_approval: null
canonical_execution: null
publication: null
audit_required_before_effective_retained: true
---
# Product-source installation, mean work and supplied external stopping

**Primary provenance helper:** `scripts/product_source_controlled_stop_2026_10_16.py`.
This is an authoring proposal. The helper checks exact source bytes, embedded bodies and saved metadata; it performs no scientific calculation and cannot approve or publish this note. The status record in `INPUT_MANIFEST.json` distinguishes actual source decisions from this unapproved wrapper. Complete historical arguments and reviews below remain unchanged, including their original pending language.

The sole direct mathematical parent is [the product-source mediator theorem](PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md), exact SHA256 `4e68ea3c55620eb0ad3c721084780d2af44bc5eaa249cb8c205e516575189d20`, 63,977 bytes. Its actual saved publication record identifies regular OPEN PR9656, head `6cd71718e16ef60505a210ff0a47559970753ab8`. This citation imports its rounded static full-isometry bound, coefficient bounds, independent source and positive-Pauli realization. The weak-mediator corrector/interval machinery is transitive through that parent, not another direct edge. Git ancestry and publication of this child remain separate. The existing eight-body static note is neither extended nor recopied here.

## Conditional operation and its ledger

For integer m>=0 use the parent's actual positive lower coefficients a=jhat, b=ghat, c=lambdahat, epsilon=2^-m, T=2^(2m+32), and t=T+s with 0<=s<=epsilon*T/256. Keep literal K=2I+ZZ, W=((9+12i)I+(-16+12i)XX)/25, u=1/2, kappa=a+u/2, q=2b+c, and the independently supplied source |00>. J appends that source. Supply the five positive source blocks, both positive XX ports, and the exact complementary scalar pair on the same old site. The reference is an arbitrary uncoupled spectator and every old/source/reference output remains.

All source blocks share one prescribed envelope; the ports and scalar pair share another. Raise source then ports, run statically for t, lower ports then source. L>0 bounds the sum of incident block derivative norms; the separate literal norm-three old load stays on. Added incident strengths stay below two. Source preparation, exact matching, timing, actual coefficient realization, absence of extra drift and endpoint switching are supplied conditions.

For linear ramps, tau_c=(2a+u)/L and tau_g=(2b+2c)/L. The Hamiltonian is continuous and absolutely continuous with the derivative cap almost everywhere; these ramps do not have C1 joins. For the separate C1 variant, f(x)=3x^2-2x^3 and

    tau_c=max(1,3(2a+u)/(2L)),
    tau_g=max(1,3(2b+2c)/(2L)).

Use f on increasing ramps and 1-f on decreasing ramps. Both areas are one half, max f'=3/2 and endpoint slopes vanish. These joins are C1, generally not C2. The minimum duration one is hbar/E0 in the declared units. Neither C1 regularity nor this minimum duration establishes hard bandwidth or a hardware response model.

For either schedule define tau=tau_c+tau_g, delta=b*tau_g and Phi=kappa*tau_c/2+kappa*tau_g+q*tau_g/2. The source-only ramps act exactly on J; each port ramp costs at most delta by full-space Duhamel. Applying the exact unitaries to the actual correlated intermediate states and using the nearby J-supported comparator gives

    ||U_off U_static(t) U_on J
      - J exp[-i(2Phi+(kappa+2b)t)]
          exp[-i(tau+s)K] W exp[-i(T+tau)K]||
       < 7epsilon/32 + 2delta.

The full scalar, purposeful c ramp area, source Pauli shift and total old age D=2tau+T+s are retained. The static c contribution is already priced in the parent theorem, not added again as an invented exact phase. Since [W,K]=0, the old comparator equals exp(-iDK)W. The unhalved complete trace bound is twice the displayed isometry bound. Actual source correlations are carried through the calculation; the source is never silently replaced by a fresh product state.

Put A_T=8+16/sqrt(T). The sufficient linear condition L>=64*A_T/(epsilon*T), or C1 condition L>=96*A_T/(epsilon*T), yields delta<epsilon/64, isometry error<epsilon/4 and unhalved complete trace error<epsilon/2. Check the condition for the selected m and L. Every fixed positive L eventually meets it along the stated family, with the larger runtime, complete ramp durations and coefficient precision retained. For C1, delta=max(b,3b(b+c)/L); the fixed minimum duration is compatible with b<epsilon/32768. No polynomial synthesis or favorable runtime claim follows.

At exact final zero added controls, the endpoint Hamiltonian is K with zero source drift. Common later free-old evolution preserves the bound for every later v>=0, with the comparator's left old factor exp[-i(tau+s+v)K]. This is a persistent operation in the free-old interaction picture, not a stationary state, autonomous halt, exact source reset, or indefinite reuse. A full initial-state error needs its own budget. A small source-marginal error alone does not control arbitrary initial correlations.

## Prescribed signed mean work

Use only W_drive=integral Tr(rho*dH/dt)dt for the complete closed prescribed Hamiltonian, including time-dependent identity reserves. W_c=kappa and c<=W_g<=4b+c. Write d_w=(4/3)b^2*tau_g for linear ramps and d_w=(36/35)b^2*tau_g for C1 ramps. Then

    |W_on-(kappa+2b+c)|<=d_w,
    W_off<=0,
    W_cycle=<K>_actual,end-<K>_input=W_on+W_off,
    |W_cycle|<epsilon/2,
    |W_off+(kappa+2b+c)|<epsilon/2+d_w

under the corresponding full-operation accuracy condition. W_cycle is signed mean work. It need not vanish or be nonnegative. The scalar 2I cancels between normalized endpoint states and ||ZZ||=1 gives the stated constant. Decreasing positive blocks make the off-ramp derivative negative semidefinite even on the actual correlated input. This accounts for modeled energy returned to the prescribed drive, not apparatus recovery, fluctuations, thermodynamic efficiency, clock cost, source production or disposal. Fresh-product static moment equalities do not hold automatically after launch; total installed mean is conserved during static runtime, old K alone need not be.

The external-stop review's separately attributed appendix derives a conditional residual-tail allowance: a supplied certified integral_0^infinity ||E(v)||dv<=eta adds eta in isometry norm and 2eta in unhalved trace norm. It is exposed reviewer context suggested by root, with its message preserved. It supplies neither a tail certificate nor a free allowance inside epsilon/2. Its constant-residual counterexample shows only that pointwise smallness alone does not imply uniform later closeness.

## Source decisions and limits of this proposal

Installation/work acceptance is the exact root record `45f062fdbce4b995c0f70ae36f8afac2fa9151409cf13e4a0be42da684cd7847`, controlled by qualification `43ab4e6cdd919c5d214d92bef15f398cd7aaf57d0eeb598bc7448cce55e8a977`. That historical decision explicitly excluded external stopping. Root subsequently accepted stop/C1 in record `a69b51ac54fb2586100072eba45492473970ef612a57c53c02184f56af84eca9`, controlled by qualification `218ddfbed74e18f18dc30c8103a6a10acadb7a50daeb0d10dd0ee5f4e207ab9a`. Both complete qualifications follow. Their acceptance covers the specified sources and contextual tail implication, not this newly assembled wrapper.

All four checks are separately written same-model source-exposed analytical reconstructions. Their metadata runs record source identity, not a compiler, simulation, symbolic integration or experimental calculation. This author read all four complete arguments, all four complete reviews and the entire direct canonical parent, including controlling qualifications. Hashes do not replace those reads or prove mathematics. This new wrapper still needs root review. Canonical integration, its actual base, execution, staged review, publication and retained audit remain unbound or separate. No editable prompt or physical axiom changes are proposed.
