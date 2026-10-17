# Hopping-only finite transfer: selective analytical check

Disposition: scoped acceptance. The weighted finite-evolution and single-cut Duhamel proof establishes the proposed complete operator bound for the specified one-head apparatus, every finite integer M>=1, every a>0 and real t. No substantive mathematical gap found. The factor 240 is correctly a ratio of leading horizon coefficients in two sufficient size inequalities, not an optimal-size or runtime improvement. One wording clarification about K aging is recorded below; the proof itself retains all noncommuting onsite dynamics correctly.

## Sources and independence

Read completely and verified:

- ../hopping_only_finite_transfer/PROPOSAL.md: SHA256 4c790286d6db32784bc892eff3c21b5674104fc205719229dcbce6296f4d98cd.
- ../bandcenter_resources/PROPOSAL.md: SHA256 96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7.
- ../bandcenter_resources_check/REVIEW.md: SHA256 01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd.

I authored the last resource review and have its prior canonical geometry/coefficient exposure. Its checked frozen dependencies, explicit scope and canonical source SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff are reused, not independently regenerated here. I did not author the hopping-only proposal. This check reconstructs its mathematical steps after reading it and the root's assigned questions; it is not blind discovery or an independent recheck of my own ancestor review. No stationary calibration or temporal theorem is required for the argument below.

Previously read AGENTS.md, SCIENCE_WORKFLOW.md and physics-claim-reviewer skill were hash-verified unchanged at febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0, 71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3 and 9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455 respectively. Their bounded review instructions are reused. No scientific execution, numerical experiment, solver, optimization, delegation, model override, W/Git/PR/checkpoint/prompt change or publication occurred. Only reads, identity checks and this report were performed. No onset, horizon, transfer budget or finite size was selected.

## Compression, distance and hopping ceiling

On the cut pair the retained subspace has omitted occupation zero. Compressing Q(-j)=j(n_last+n_omitted)-j(exchange) therefore leaves j n_last. This is exactly the cap. All other retained onsite blocks and the single shared old/source fiber agree, giving H_M=P H_infinity P, including the common scalar. For M=1 the missing ordinary new bond still contributes the same j cap; the converter supplies the other endpoint contribution. There is exactly one installed edge crossing P, between output n=M-1 and n=M.

The emitter-to-input-origin route takes 1+20+1+40=62 head edges, the junction crossing takes 2, and output origin to last retained vertex takes 40+1+(M-1)=M+40. Thus L=M+104 and the omitted vertex has d=L+1=M+105. Source dynamics cannot furnish another head route. Selectively uninstalled geometric neighbors do not count.

The only potentially largest hopping row is at a junction: its three edges sum to J+2J/sqrt(2)=J(1+sqrt(2))<.031*2.415=.074865<.075. Ordinary old rows are 2J<.062. A filter row is J+JS0/C0<.031*(1+.5/.9)<.049. Old/new converter rows are J+tau<.038 and tau+j<.010. New ordinary rows are 2j<.006, input-end rows j+kappa<.00300001, and emitter hopping is kappa=1e-8. Entrance and capped-output rows are no larger; for M=1 the cap adds no hopping. Thus C=.075 is safe uniformly in M. The norm table concerns head-off-diagonal blocks, not norms of full PSD bonds. In particular the large source A--B hopping belongs to the fixed-head internal block D_x and remains physically present.

Hermitian adjoint symmetry gives the matching column bound, so the block Schur estimate applies to A. The same bound holds after individual internal unitary rotations of each edge. No scalarization or commutativity of distinct D_x is needed.

## Weighted propagation reconstructed directly

A direct autonomous proof avoids relying on the proposed Dyson fallback. Let H_a=W_a H_M W_a^-1 and let y(s)=W_a exp(-isH_M)V_seed v for arbitrary unit seed input v, including any passive reference. Since f(emitter)=0, ||y(0)||=1. The weight is bounded and invertible for each finite M; even an infinite-dimensional passive reference does not affect this fact.

The onsite part of H_a equals D_M and is self-adjoint. For an edge xy, putting delta=f(x)-f(y), adjoint symmetry gives

    [Im H_a]_xy=(e^(a delta)-e^(-a delta)) H_xy/(2i)
                  =sinh(a delta) H_xy/i.

The graph distance satisfies |delta|<=1 on every installed edge. Row and column sums of these block norms are therefore bounded by C sinh(a). It follows that ||Im H_a||<=C sinh(a). The norm derivative is

    d||y(s)||²/ds=2 <y(s),Im H_a y(s)>.

Gronwall gives ||y(s)||<=exp(C sinh(a)|s|), using the same two-sided norm bound for negative times. Taking the supremum over unit v proves an operator estimate, not a bound for selected scalar columns. At the last retained vertex W_a acts by e^(aL), hence

    ||P_last exp(-isH_M)V_seed||
       <=e^(-aL+C sinh(a)|s|).

This derivation retains every internal/source coordinate and all their entanglement. Large onsite norms have zero contribution to Im H_a because W_a is scalar on each internal fiber. Their actual dynamics have not been omitted.

The interaction-picture statements also check: exp(isD_x)H_xy exp(-isD_y) preserves each edge norm, and finite/infinite retained edge blocks coincide at the same time by cap compression. Each ordered Dyson word is a head walk. For n<d no word from the emitter reaches an omitted vertex; the entire ordered internal product agrees. Norm bounds (C|t|)^n/n! therefore establish the stated 2-summed-tail fallback independently of the weighted sinh estimate. The potentially stronger cancellation of some later terms is not required.

## Exact one-cut comparison and complete scope

Let H_dec=H_M direct_sum H_out with H_out the complementary compression. It is bounded self-adjoint in this supplied one-head model. The difference K_cut=H_infinity-H_dec is precisely the cut hopping and its adjoint. On exp(-isH_dec)V_seed the omitted component is zero, so only one orientation acts:

    ||K_cut exp(-isH_dec)V_seed||
       =j ||P_last exp(-isH_M)V_seed||.

The equality uses the actual scalar-identity hopping and is valid on the entire old/reference input space. The reverse orientation contributes zero; adding a factor two would be unnecessary. Duhamel places full infinite evolution on the left of this forcing, where its unitary norm is one. Thus returns from the omitted region are included, not ignored. Integrating the last estimate yields exactly

    error <=min{2,j e^(-a(M+104))
                 [exp(C sinh(a)|t|)-1]/[C sinh(a)]}.

This bounds the full state-map difference after finite embedding. It is stronger than a leakage-only assertion and needs no scattering completeness, parity-column aggregation, source-vacuum assumption during evolution or absence of point spectrum. The delivered seed condition supplies the initial localized embedding; in fact the propagation argument would allow arbitrary initial internal state at that same emitter. Passive-reference tensoring preserves each operator norm. With an independently supplied normalized complete-output comparator, triangle inequality and the pure-state trace-distance inequality justify the stated factor-two unhalved trace bound, also for reference-assisted channel comparison.

## Horizon constants and wording qualification

At a=1 and 0<=t<=2T, dropping the minus one in the numerator gives prefactor j e/(C sinh1) with exponent -(M+105)+.15 T sinh1. Since j/C<.04 and e/sinh1=2/(1-e^-2)<2.5, the prefactor is strictly less than .1. Both the logarithmic sufficient conditions and the T=0 exception follow. They remain valid when a logarithmic right-hand side is negative, provided integer M>=1 is retained. The older condition had leading term 36 T sinh1, and 36/.15=240 exactly. Logarithmic constants and the additive graph offset also differ; no conclusion that actual resources or minimum sizes improve by exactly 240 follows.

One prose clarification is advisable in section 6's final paragraph: the phrase saying the scalar and full exp(-itK) aging “cancel” between exact evolutions should not suggest that exp(-itK) is a common commuting factor of those evolutions. In general K does not commute with the source interactions. The proof above needs no such factorization: c_total is a common removable scalar phase, while K and all other onsite operators are retained exactly in D and their contribution to weighted norm growth is zero. The separate physical output comparator must retain the prescribed K aging. This is a clarification of wording, not a defect in sections 3–5, which explicitly use the correct noncommuting dynamics.

The result is suitable as a conditional finite-transfer improvement on the frozen nominal apparatus. Complete temporal escape/onset, native supply, physical units, precision, optimized resources and permanent finite halting remain outside its conclusion. Physical qubit counts and source incident loads are unchanged.
