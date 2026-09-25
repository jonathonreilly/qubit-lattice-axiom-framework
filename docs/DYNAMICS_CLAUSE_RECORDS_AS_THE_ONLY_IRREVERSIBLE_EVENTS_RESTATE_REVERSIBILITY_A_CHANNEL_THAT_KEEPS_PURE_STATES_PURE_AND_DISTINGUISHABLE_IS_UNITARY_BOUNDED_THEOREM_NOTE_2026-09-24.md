---
claim_id: dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_a_channel_that_keeps_pure_states_pure_and_distinguishable_is_unitary_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Pure-output finite channels: unitary or replacement. Conditional finite quantum mathematics under the explicit premises in this note; no native law, framework premise or retained grade is adopted.'
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_2026_09_24.py
---
# Pure-output finite channels: unitary or replacement

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** conditional-support; unaudited.

## Supplied channel problem

Let Phi:M_d(C)->M_d(C) be a CPTP map. Supply as mathematical requirements
that every pure input has a pure output and that trace distance of every pair
of pure inputs is preserved. These conditions are a proposed strong reading
of evolution between records. They are not derived from the Record text or
from a one-site argument about a decoupled partner. The whole-region channel
premise is explicit and no new framework rule is adopted.

## Linear-map lemma and classification

Pure output implies that, for every vector x, all Kraus output vectors K_i x
are parallel: a sum of positive rank-one matrices has rank one exactly when
its nonzero generating vectors span one line.

Suppose one Kraus matrix A has rank at least two. If Ax and Ay are independent,
parallelism gives Bx=alpha Ax and By=beta Ay for any other Kraus B; applying
the condition to x+y gives alpha=beta. Any vector with nonzero A image can
be paired with x or y to get that same factor. For z in ker A, apply the
condition to x+t z and y+t z: Bz must lie in both independent image lines,
hence is zero. Therefore B=cA for every other Kraus matrix.

Otherwise every nonzero Kraus has rank one. If A=a f and B=b g had distinct
range lines, choose x outside the two proper hyperplanes ker f and ker g
(over C a finite union of proper subspaces cannot cover the space). Then
Ax and Bx are nonzero and not parallel, a contradiction. All nonzero Kraus
operators consequently share one range. Zero Kraus operators have no effect.

In the proportional case K_i=c_i V, trace preservation gives
(sum |c_i|^2)V*V=I. The normalized square matrix U is unitary and
Phi(rho)=U rho U*. In the common-range case K_i=|v><w_i| with normalized v,
trace preservation yields sum |w_i><w_i|=I and
Phi(rho)=Tr(rho)|v><v|, the pure replacement channel.
These exhaust same-dimensional finite CPTP pure-output maps.

For d>=2 the replacement erases the trace distance 1 of orthogonal inputs.
Thus the additional distance-preservation condition leaves only unitary
conjugations. Conversely those preserve purity and trace distance. For d=1
the unique channel is the identity and the two descriptions coincide.
An isometry into a larger output dimension is an additional possibility if
the same-dimension premise is removed. Antiunitary ray symmetries are not
complex-linear CP channels; Wigner language is unnecessary for this proof.

## Evidence and limits

The primary's random qubit/qutrit examples illustrate purity loss and distance
contraction, the exact replacement exception and proportional Kraus action.
Aggregate extrema over sampled channels show examples, not per-channel or
all-channel numerical certification. The proof supplies the universal result.
The linear-map checks explicitly compare common-range rank-one maps and a
rank-two/rank-one pair; finite sampling alone would not establish the lemma.
Neither this theorem nor its samples select a native microscopic law,
Hamiltonian, time coordinate or interpretation of permanent records.

## Scope discipline

### N1
The alternatives actually examined are the explicit constructions, maps and counterexamples above. No exhaustive framework route classification is claimed.

### N2
Preparation, probability, composition, dynamics and operational readout have distinct premises; the displayed implications do not establish pairwise independence.

### N3
Finite complex matrices, specified tensor products, available effects and any ensemble/update assumptions are supplied mathematical setting.

### N4
The linked sources supply only their stated conditional algebra and current axiom boundary, never an inherited audit grade.

### N5
Prove the parallel-output linear-map lemma including its kernel. Retain the pure replacement exception before imposing distances. Normalize proportional Kraus matrices using trace preservation. Keep input and output dimensions equal in the unitary classification. Treat record-only irreversibility as a supplied mathematical requirement. The primary reports these five scope resolutions.

### N6
Native realization and every wider original claim not proved above remain deferred, recoverable from the original PR head.

### N7
The explicit positive routes and counterexamples above delimit the obstruction. Failure of a sampled route does not exclude untested alternatives.

### N8
This is bounded conditional progress, not a Born/composition/dynamics derivation from the four axioms or a physical completion.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [DYNAMICS_CLAUSE_LOCALITY_OF_MARGINALS_MAKES_A_SITE_S_EVOLUTION_BETWEEN_RECORDS_LINEAR_AND_COMPLETELY_POSITIVE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_LOCALITY_OF_MARGINALS_MAKES_A_SITE_S_EVOLUTION_BETWEEN_RECORDS_LINEAR_AND_COMPLETELY_POSITIVE_BOUNDED_THEOREM_NOTE_2026-09-24.md)

[Primary](../scripts/dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_2026_09_24.py) and [fresh output](../logs/runner-cache/dynamics_clause_records_as_the_only_irreversible_events_restate_reversibility_2026_09_24.txt).
