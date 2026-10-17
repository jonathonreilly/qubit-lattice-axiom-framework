# Original-apparatus hopping-only resource application: selective check

Disposition: conditional mathematical support. No load-bearing application defect found. The original apparatus admits the stated complete transfer bound with last retained distance L=M+22, cut magnitude J and hopping ceiling C=.075, uniformly over the supplied fixed-spectrum family. At unchanged T=3e17, M=6e16 suffices for transfer <.001 through2T. Conditional on the existing infinite-device endpoint-forcing theorem, the nominal/family finite errors remain <.001320/<.001347. The output-length ratio250 is exact for the two stated sufficient choices; it is not a minimum-size or runtime result.

The initial source-pin discrepancy is resolved. The application's cited generic review d5ad6794b64d652bfbb4e80a8b172ccff1416d8e1fe726f6e592909e90d9bc8a is preserved as ../hopping_only_finite_transfer_check/REVIEW_v1.md; I verified its exact hash. The current REVIEW.md hashes to f47de4c7d6a20b547b365b105abaa70ca124071998ec58aeac6dab4c5e7bf664. I inspected their entire diff: only a final-source qualification was appended, explicitly confirming the generic proposal's corrected K-aging paragraph at9797cfa1. No underlying mathematical review changed. The application's historical citation and the current final qualification are both accounted for; no source-pin fix or other application change is required.

## Exact sources and exposure

Read completely and verified SHA256:

- ../original_hopping_transfer/PROPOSAL.md: a7ef8d4ba3d1c9e35e9de7c5ca5e8f66b4cc5af3f105570e43935868d1fed8a7.
- ../hopping_only_finite_transfer/PROPOSAL.md: 9797cfa1090d58216655c80f79a8ce0fcee493c706f5028e61150d0815db278e.
- ../hopping_only_finite_transfer_check/REVIEW.md: f47de4c7d6a20b547b365b105abaa70ca124071998ec58aeac6dab4c5e7bf664.

Read the canonical correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md geometry/cap/count/distance passage594–652, fixed-spectrum construction2100–2147, and endpoint-forcing complete bounds2284–2304 at verified SHA25671c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. Also located the newer onset statement2211–2213 and its unchanged-parameter contract, and read nearby2240–2285 for source scope; this is not a fresh recheck of those temporal estimates. Earlier complete readings of the same canonical source/filter/mixer passage163–319 remain applicable. The root-provided PR9672 Git head is provenance information only; no Git or remote verification occurred.

I authored neither this application nor the generic hopping lemma/review. The parent's requested target and all three texts are exposed inputs; this is an analytical reconstruction of the application, not blind origin or model-diverse checking. Previously read unchanged AGENTS/workflow and physics-claim-reviewer instructions are reused. The existing spectral, calibration, supply and runtime theorem is an explicitly conditional dependency; I do not recertify it here or infer its correctness from publication/review labels. No output-coordinate-only weight proposal was read or used.

No scientific execution, solver, experiment, sweep, delegation, W/Git/checkpoint/prompt/model change or publication occurred. Only source reads/hash verification and this report were performed. No editable prompt file changed.

## Original graph, cut and compression

The explicit geometry has two disjoint45-site head paths terminating at the two opposite arm corners of the four-edge junction square. Input and output origins are the other two corners. The emitter lies at input coordinate ell+1=21, so it is21 installed head edges from input origin. Crossing the junction requires two installed edges. From output origin to first omitted output vertex m=M is another M edges. Therefore d=M+23 and last retained distance L=M+22. Neither shared internal-source dynamics nor geometrically adjacent but uninstalled head edges shorten this route.

There is one cut edge, from output m=M-1 to m=M, of hopping magnitude J. With omitted occupation blank, compression of Q(-J)=J(n_last+n_omitted)-J(exchange) leaves J n_last. The stated finite cap is precisely that term. All retained diagonal blocks and common scalars therefore agree, and H_M=P H_infinity P is exact in the relevant one-head space. The endpoint keeps diagonal2J. This remains true for M=1: the retained output origin has its junction contributions and the cap replacing its removed ordinary outgoing bond. No added onsite difference needs to be charged in Duhamel.

Direct counting gives90 arm vertices,21 input vertices,1 emitter and M output vertices, hence M+112 head qubits. Four shared old/source qubits give M+116 physical qubits. Edges are88 arm,4 junction,20 input,1 emitter and M-1 output, totaling M+112. Passive references are outside the apparatus count. The source fiber is shared, not replicated at every head position.

## Hopping ceiling across the supplied family

At each ordinary original lead/arm row the sum is2J<.062. A junction row has one ordinary J edge and two J/sqrt(2) edges, hence J(1+sqrt(2))<.031*2.415=.074865<.075. Filter rows have J+t_filter with t_filter=JS0/C0; the previously read source half-angle data give C0>.9 and S0<.5, so the sum<.049. Input endpoint and emitter rows have J+kappa0<.03100001 and kappa0=1e-8. Entrance and capped-output rows are smaller. Thus the absolute block row sum C=.075, with equal column bound by adjoint symmetry, is safe.

Large internal hopping h, shared B and contact operators preserve head position and belong to the complete self-adjoint onsite blocks D_x. Keeping them there is exact, even when these operators fail to commute. It does not reduce their physical loads or remove their interactions. The weight is scalar on each entire internal fiber, so these blocks contribute no imaginary part to the conjugated generator.

The fixed-spectrum family changes the actual emitter hopping to kappa_a, with0<kappa_a≤kappa0. It also changes the emitter diagonal by Delta and the endpoint diagonal by-Delta; the actual endpoint is2J-Delta. The application correctly retains this and does not claim that all hoppings are unchanged. The altered edge never increases the row sum. Every bulk/filter/junction/cut edge is unchanged, so C=.075 and cut magnitude J hold uniformly. Family-specific onsite evolution is retained exactly; no approximation by small Delta times the long horizon is used.

## Generic lemma applied to this architecture

Exact compression makes finite and infinite retained interaction-picture edges identical at the same time: exp(isD_x)H_xy exp(-isD_y), with norm|h_xy|. No commutation of D_x with D_y or K with source interactions is required. The graph distance weight has gradient at most one across installed edges. The separately reviewed generic argument therefore applies after replacing its converted-apparatus distance by M+22 and its cut magnitude j by J:

    E_transfer(t)<=min{2,J exp[-a(M+22)]
                       [exp(C sinh(a)|t|)-1]/[C sinh(a)]}.

For completeness the application-specific forcing has only one orientation: the finite state has no omitted component, so the reversed cut edge annihilates it. The retained-to-omitted edge acts on all internal amplitudes at the last retained vertex with norm J. The full infinite propagator in Duhamel is unitary, accounting for all subsequent returns and spectral components. The resulting estimate is a complete seed-state operator bound and needs no additional sqrt(2) old-column factor. Passive-reference tensoring preserves it.

The common scalar can factor between exact evolutions. K remains inside onsite dynamics and is not factored from the interacting evolution. Its prescribed aging remains in the separately supplied physical target.

## Fixed horizon, finite error and resource comparison

With a=1 and0≤t≤2T, the exponent may be written using d=M+23, with prefactor J e/(C sinh1). Because J<.031, C=.075 and e/sinh1=2/(1-e^-2)<2.5, this prefactor is<2. The converter's smaller .1 prefactor is not imported.

At T=3e17 and M=6e16, sinh1<1.2 gives .15T sinh1<5.4e16. Therefore the exponent is<-6e15-23. Even dropping the enormous negative6e15 term leaves2e^-23<2^-22<.001. This establishes the required uniform transfer budget without numerical exponentiation. M is a positive integer fixed before delivery, and the bound covers the whole horizon, not only its endpoint.

The canonical endpoint-forcing statements explicitly supply nominal infinite error<.000320 and fixed-spectrum-family infinite error<.000347 for all t≥3e17, with the family compared against the fixed nominal target. Reusing those unchanged results conditionally, triangle inequality gives<.001320 and<.001347 on[3e17,6e17]. Their unhalved trace ceilings are twice these values, .002640 and.002694, including arbitrary passive references. The target remains the normalized infinite profile embedded in the common infinite space; it is not shortened, renormalized or postselected to match M. Every source/emitter/clock output and the actual outside spectral mass already included by that theorem remain charged.

The old sufficient M=50T=1.5e19 divided by6e16 is250 exactly. Physical qubit counts are1.5e19+116 and6e16+116, whose ratio is strictly below250. New head qubits and head edges are both6e16+112. The generic leading-coefficient ratio240 compares a different pair of sufficient inequalities; rounding the explicit choices does not create a contradiction. Neither ratio establishes optimal resources.

Only the finite output length and cap location change. The original Hamiltonian coefficients, supplied precision family, seed, onset and infinite target stay fixed. No improved runtime, all-future halt, output-only-weight result, native implementation, physical-unit assignment, or practical resource claim is supported or needed here.
