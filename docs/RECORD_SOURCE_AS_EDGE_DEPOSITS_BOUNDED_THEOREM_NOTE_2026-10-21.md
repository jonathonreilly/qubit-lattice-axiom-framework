---
claim_id: record_source_as_edge_deposits_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional covariance cancellation for explicitly supplied step and ordered-pair weights, and exact signed linear span of symmetric 4x4 matrices by D4 root outer products; three finite walk diagnostics, no physical record or geometry-response law."
upstream_dependencies: []
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A physical source or geometry coupling from these signed ensemble weights is not derived; downstream consumer not yet known."
source_of_blocker_text: review_loop
reachability_to_target: "Algebraic representation does not select physical deposition rates or geometry dynamics."
conditional_surface_status: "Exact covariance cancellation with supplied weights and exact signed span; finite walk checks separately scoped."
hypothetical_axiom_status: "none adopted"
admitted_observation_status: "none"
claim_type_reason: "Explicit covariance expansion and symmetric-matrix basis proof."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: "Conditional algebraic support; downstream consumer not yet known."
next_trace_action: "Supply and independently justify any physical turn-weight or geometry-response bridge before using one."
runner: scripts/record_source_as_edge_deposits_2026_10_21.py
---

# Supplied edge weights: covariance cancellation and signed tensor span

Claim type: bounded_theorem.
Primary runner: `scripts/record_source_as_edge_deposits_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), with zero premise weight, and [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are context only. Neither supplies the ensemble weighting or geometry dynamics below.

## Supplied steps, pairs and conditional identity

Take a finite direction set d_a, normalized probabilities P_a>=0 with sum P_a=1, and real scalar eps. Define s_a=(1,d_a), c_ab=(0,d_b-d_a). Supply the step weights eps P_a, ordered-pair weights 2 eps P_a P_b, and signed chord coefficient -1/4, so

    T = eps sum_a P_a s_a s_a^T
        - (1/4) sum_ab 2 eps P_a P_b c_ab c_ab^T.

Pairs are ordered and a=b contributes zero. These are assigned ensemble source weights, not a turn distribution derived from the coin or Born marginal probabilities. For eps<0 they are signed weights rather than nonnegative rates. A reversal gives c_ab=(0,-2d_a), but its contribution still carries the specified pair weight; the coefficient alone is not a per-relay law.

Let mu=sum_a P_a d_a and Q=sum_a P_a d_a d_a^T. Expanding the ordered pair sum gives

    sum_ab P_a P_b (d_b-d_a)(d_b-d_a)^T = 2(Q-mu mu^T).

The spatial block is therefore eps Q - (eps/2) 2(Q-mu mu^T)=eps mu mu^T. Chords have zero temporal component, leaving T00=eps and T0i=eps mu_i. Thus T=eps (1,mu)(1,mu)^T exactly. Zero probabilities and deterministic P are permitted; deterministic P has no step-only mismatch. This proves only a conditional algebraic identity for the chosen weights.

## Relation to the supplied walk and finite evidence

For U(k)=diag(exp(-i k.d_a)) C with constant unitary C, choose a normalized differentiable eigenpair Uu=exp(-i eps)u, with a locally differentiable eigenphase eps. The unitary eigenvalue derivative identity i u^dagger U^dagger (partial_j U)u=partial_j eps gives sum_a |u_a|² d_aj, since partial_j U=-i diag(d_aj)U. Thus mu equals group velocity v=gradient eps on that branch. A simple eigenvalue suffices locally; degeneracies require a compatible differentiable eigenpair. The physical interpretation of eps as energy, eps v as momentum, and the tensor as moving matter remains unproved.

The runner uses the supplied six axial directions, coin exp[-i .3(R-P+2I)] with reversal adjacency R and perpendicular adjacency P, and its stated overlap-tracked eigenband selector. At exactly |k|=.3 along normalized (1,1,0), (2,1,0), (1,1,1), the supplied tensor agrees with eps(1,v)(1,v)^T to finite-difference tolerance. Step-only mismatch is observed only for these three selected cases. These samples do not establish a realized record process.

## Exact signed span of D4 root outer products

The supplied D4 set contains the 24 vectors ±e_i±e_j for i<j in four-dimensional real coordinate space. Write A_ij^±=(e_i±e_j)(e_i±e_j)^T and D_i=e_i e_i^T. Then

    (A_ij^+ - A_ij^-)/2 = E_ij + E_ji,
    (A_ij^+ + A_ij^-)/2 = D_i + D_j,
    D_i = [(D_i+D_j)+(D_i+D_k)-(D_j+D_k)]/2

for distinct i,j,k. These yield all six off-diagonal and four diagonal symmetric basis matrices, proving span Sym(4) exactly. The runner's rank-10 calculation illustrates that proof. Opposite roots duplicate outer products; 24 vectors are not 24 independent tensor variables.

Representation uses arbitrary real signed coefficients and is nonunique. Nonnegative combinations are positive semidefinite and cannot represent every symmetric matrix (for example -D_1). The result proves a linear representation only: it gives no edge-length action, geometry/source coupling, physical deposition mechanism or symmetric geometry response.

## Review record and scope

Original PR9842 head 5d7ee8e043388ee964ffffc042a42b72dd0b2cdc preserves the earlier weighting omission and geometric-response assertions. Those claims are narrowed here to explicit supplied weights and exact signed algebra. Walk, coin, band selector, eigenphase branch, spacetime embedding and D4 set are supplied mathematical choices, with no empirical calibration. No field equation, edge-length dynamics, coupling value, physical identification or audit status is established.
