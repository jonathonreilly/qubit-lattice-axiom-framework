# Connected four-insertion response of the compact two-step SU(2) posterior

Status: proposed_retained

This note proposes a volume-uniform connected two-source/two-distinct-boundary
response bound for the full compact two-step SU(2) hidden posterior at terminal
identity, fixed odd blocking factor and sufficiently large common coupling.
The complete proof is the [composed derivation](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/full-connected-four-response.md)
and the dependency closure listed below. Formal retained status is not claimed.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "full connected two-source/two-boundary response"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Control the complete coarse-conditional denominator response and nonidentity terminal data before testing further exact blocking."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Analytic proof for a supplied finite two-step family at terminal identity and sufficiently large u; no continuum or physical-gap conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## Exact model and statement

Fix odd L>=3, kappa>0, terminal torus side m>=3, original fine side L^2 m,
and the [original SU(2) word-mean kernel](SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md).
The conditioned hidden law is proportional to

    q_u(U0) K_(kappa u)(U1|U0) K_(kappa u)(V|U1).

There is one fine Wilson action at beta=u. Every input-dependent kernel
normalizer is retained, and no intermediate Wilson action is inserted.
All assertions below are at V=I and zero source. Constants may depend on
L,kappa and fixed local-source support and C^2 norm bounds, but not on m,
source locations, terminal-link locations or u>=u0. No numerical value of
the existence threshold u0 is asserted.

Let F,G be real local C^2 original observables invariant under the shared
root-fixed gauge group and global simultaneous conjugation. They descend to
the exact terminal-root forest quotient. For distinct terminal links c,d and
unit tangent color vectors v_c,v_d, let

    A_c=kappa u <i v_c dot sigma_Pauli,M_(1,c)>,
    A_d=kappa u <i v_d dot sigma_Pauli,M_(1,d)>.

Their actual mean readers are retained. Let tau be the minimum number of
nearest-neighbor terminal-cell edges of a connected graph meeting the four
source/score reader sets, including periodic paths and Steiner vertices.
There exist u0,C<infinity and mu>0 such that the FULL COMPACT posterior obeys

    |kappa_4(F,G,A_c,A_d)| <= (C/u) exp(-mu tau).

For every 0<=eta<mu, there are C_eta,b_eta>0 such that

    sum_(c!=d) exp(eta tau)|kappa_4(F,G,A_c,A_d)|
       <= (C_eta/u) exp[-b_eta d(supp F,supp G)].

These are proposed analytic theorems, not empirical predictions or numerical
fits. The exact response interpretation is

    D_c D_d partial_s partial_t log N_V(s,t)|_(I,0,0)
       =kappa_4(F,G,A_c,A_d).

Distinct links are essential: repeated-link derivatives include a derivative
of the score. Constants as insertions give zero cumulants and require no
definition of distance to an empty support.

For original global singlets that are not invariant under the root-fixed
gauge orbit, the complete formula instead retains

    f=E_h F, g=E_h G, C_FG=Cov_h(F,G),
    kappa_4,pi(F,G,A_c,A_d)
       =kappa_4,nu(f,g,A_c,A_d)+kappa_3,nu(C_FG,A_c,A_d).

The first term has the C/u tree bound. The second has a C tree bound on
its merged source region; it vanishes identically when the original sources'
Haar endpoint-reader sets are disjoint, or one source is orbit invariant.
When those local endpoint sets overlap, their union has bounded diameter,
giving the corresponding four-region tree bound with prefactor
C[u^(-1)+1_(endpoint readers overlap)]. The conditional covariance has not
been suppressed or assigned an unjustified extra power of 1/u.

For a normalized coarse conditional p=N/Q, its response remains the
numerator response MINUS the complete corresponding coefficient of log Q.
A Q that retains the varied terminal/exterior coordinates has its own law
and needs its own estimate. The theorem above supplies the stated N law.

## Proof and obligation graph

All mathematical suppliers in this table are included in the proposed tree;
no unmerged historical theorem is a missing landing dependency. Historical
one-step constructions informed the method, but the present two-step
identities and estimates are re-established in these files.

| Obligation | Proof supplied here and role |
|---|---|
| Exact quotient and source reconstruction | [Forest exchange](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md): probability-Haar orbit, complete original sources and readers. |
| Actual two-layer coercive Gaussian and fixed-cube covariance | [Flat precision](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/flat-two-step-bound.md) and [nonlinear chart](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonlinear-chart-response.md): retain both normalizer levels, Haar Hessian, actual block maps and face conditions. |
| Compact action and actual regional denominator | [Compact energy](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-energy-coercivity.md), [local conditional](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/local-conditional-tail.md), and [arbitrary-exterior moments](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/arbitrary-boundary-interior-moments.md): exact H-factor comparison and cancellation of dimensional Haar powers. |
| Full compact integral in one common chart law | [Compact decomposition](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/two-step-compact-polymer-decomposition.md) and [source-marked extension](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/source-marked-compact-decomposition.md): first-shell partition, all selected dummy-region exclusions, whole-source assignment and actual source-dependent denominators. |
| Gaussian and small primitive hypotheses | [Frozen Gaussian producers](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/frozen-gaussian-producers.md): positive finite-range covariance core, small path remainder and exact local Taylor vertices. |
| Connected cancellation of the compact correction | [Fixed-reference density forest](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/zero-shift-marked-density-forest.md), with [scalar-leg counts](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/scalar-leg-forest-count.md): normalized density derivatives, complete cell bodies, geometric paths, exact regrouping, convergent logarithm and compact charge. |
| Correct u powers and spatial response on the chart | [Chart fourth response](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/chart-fourth-connected-bound.md): singlet moments, one-versus-three and two-versus-two cancellations, tree geometry and boundary-pair summation. |
| Original-source conditional covariance | [Original-source identity](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/original-source-four-response.md): orbit-average fourth cumulant plus orbit-covariance third cumulant. Its full-law moment supplier is [compact fourth scaling](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/full-compact-fourth-scaling.md), with [rough components](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/rough-component-bound.md) and [relative coercivity](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/local-relative-coercivity.md). |
| Actual-model assembly and final response | [Composed proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/full-connected-four-response.md): verifies each density-forest hypothesis, fixed-score source interpretation, shrinking-cube uniformity and the full compact result including the original-source extension. |

The decisive mechanism is a common-reference compact/chart logarithm.
With p=log(2+u)^A, A>5/2, chart width u^(-1/2)p and the prescribed least
shell width K=O(log u), its connected compact correction is O(exp(-c p^2))
in a spatially weighted norm. Four source derivatives cost at most O(u^2).
This remainder is smaller than C/u for large u and adds to the chart's C/u
four-cumulant estimate. The Gaussian covariance is fixed before those source
derivatives; no fine-field analyticity of the compact insertions is assumed.

The auxiliary [buffered-core ratio](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/buffered-core-conditional-ratio.md)
and [global sector-ratio comparison](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/global-chart-sector-ratio.md)
are useful separate bounds. They are not used as substitutes for the
connected-logarithm proof. The earlier [rough-density estimate](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/rough-density-bound.md)
is also preserved as a weaker quantitative checkpoint.

## Imported setup, credit and evidence

The Wilson/normalized soft-kernel family, SU(2), fixed L and kappa are supplied
mathematical model choices. This note does not derive them from the framework's
axioms, identify u with a physical running coupling, or establish continuum
Yang–Mills theory. There are no fitted observations or numerical inputs.
Finite Gaussian calculus, elementary forest/tree expansions and Haar facts
are used with their proof obligations made explicit above.

The repo precursor is the one-step compact-return and marked-chart work in
draft #10133, revision `89faef229ff6e6bde42baad15ed8270c2f4087d8`, especially
`HOLOMORPHIC_COMPACT_RETURN_ASTRA.md` and `MARKED_COMPACT_CHART_ASTRA.md`.
Their one-step claims are not relabeled as two-step results. Abdesselam and
Rivasseau's *Trees, forests and jungles: a botanical garden for cluster
expansions* supplies the forest architecture; Lohmann's single-scale cluster
expansion supplies a comparison with an explicitly different hypothesis
class. Bałaban's gauge-localization work and Dimock's exposition are broader
antecedents. Exact read scope, primary links and hypothesis comparisons are
in the pack's literature records. No novelty claim follows from that search.

Luna performed repo and literature extraction. Bounded proof pieces were
drafted by the user-authorized medium-effort workers; the supervising profile
handled frontier synthesis and fresh-context decisive mathematical checks.
Checks are same-provider, not independent-provider or formal-audit evidence.
The [current checkpoint](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/HANDOFF.md)
links the frozen checks and records their limitations. Mechanical hashes and
lint are integrity checks, not theorem certification. No numerical physics
runner is needed or claimed for these analytic statements.

## Review record and remaining proof tasks

The independent mathematical review records retain the actual repairs:
prescribing the least admissible K; including the path endpoint weight;
symmetric path assignment; retaining complete cell bodies and paying their
Gaussian costs; nonempty priced primitive supports; and the distinction
between linear constant sources and nonlinear source-only normalization.
The [review history](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/REVIEW_HISTORY.md)
records final source checks and mechanical conformance separately. This note
does not amend earlier landed science or an audit judgment. Independent
publication review and formal audit retain their respective authority.

The nearest missing theorem for the broader conditional response is a bound
for the actual log Q law when it retains the varied exterior parameters,
together with control in a nonidentity terminal-field class. Further exact
blocking then requires stable hypotheses for the inherited effective density.
Depth-uniform/physical-scale estimates and continuum reconstruction remain
additional obligations. No positive physical mass, Yang–Mills existence
theorem, TOE unification, or continuum mass gap is established here.
