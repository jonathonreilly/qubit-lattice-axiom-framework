---
claim_id: candidate_assembly_source_linked_graph_eleven_targets_minimal_decision_sets_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Exact minimal decision families for one explicitly supplied finite AND/OR planning graph. No edge is certified as a physical necessity or sufficient theory completion."
upstream_dependencies:
  - minimal_axioms
runner: scripts/candidate_assembly_source_linked_graph_minimal_decision_sets_2026_09_22.py
---

# Minimal decision families of the supplied campaign planning graph

**Type:** bounded_theorem
**Status:** conditional finite combinatorics; unaudited.

This preserves the submitted 117-node graph, its 40 menu entries and eleven named targets, with AND semantics for ordinary nodes and OR semantics for choices. The graph is an explicit modelling input. A target becoming true means only that this Boolean graph evaluates true. It does not mean that a physical theory, gravity, a species identification or a retained claim has been established.

The 75 result-reference nodes point to current canonical files. Those files retain their individual hypotheses and limitations; names and file existence do not supply proofs for the graph's arrows. In particular, axioms alone do not select a uniform measure or a quantum dynamics, finite window obstructions do not classify all formation orders or units, and finite ice diagnostics do not establish a universal Gaussian or continuum law. The source node labelled AX is a planning label, not an assertion that every downstream result follows from axioms alone. PR status labels in the original seventeenth edition are historical.

## Declared graph and exact semantics

The full labelled graph, reference paths, menus, edges and seven unresolved bridge labels are literal data in the runner. There are two source nodes, 75 local reference nodes and three submission reference nodes, twelve decision nodes, six choices, eight routes and eleven targets. The menu entries are recorded candidate descriptions, not endorsed clauses or new premises. With a chosen subset D of decision labels, a decision node is true exactly when it belongs to D. A source is true. An OR choice is true if any parent is true; an ordinary node is true if all parents are true. Empty OR is false and empty AND is true. The graph is acyclic.

For each node compute the inclusion-minimal decision subsets that make it true. A decision has its singleton family. An OR takes the union of parent families and removes strict supersets. An AND forms all unions of one member from each parent family and removes strict supersets. Induction along a topological order proves this algorithm: OR satisfaction is witnessed by one parent; AND satisfaction requires a witness for each parent; removing supersets preserves exactly the minimal witnesses. This proves correctness for the supplied graph without importing physical implications.

## Results within the declared graph

The target labelled downstream gravity has exactly these four minimal families:

- {alphabet, order law}
- {alphabet, reading}
- {soldering, reading, roles}
- {soldering, joint units, order law, roles}

Record dynamics has {reading, soldering}, {reading, alphabet}, {soldering, joint units, order law}, and {alphabet, order law}. Gauge has {roles}, {alphabet, order law}, and {alphabet, reading}. Formation law has {rule, order law}; clock/rate has {order law}. The runner computes all eleven target families. Every target family is nonempty and excludes the empty decision set, and every decision label occurs in at least one target's minimal family.

The historical alternative-graph controls remain: deleting the encoded layer-order requirement, then the plan-letter requirement, then the static-frame requirement produces the earlier families; restricting encoded letter routes yields the relational and single-angle variants. These are changes of declared graph inputs, not proofs that the corresponding physical restrictions are necessary. A deliberately cyclic graph is rejected. An independent exhaustive evaluator can check every one of the 4096 decision assignments against the recursive family algorithm.

## Imports and source preservation

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): premise boundary; the graph is supplied, not derived from these axioms.
- Current file references are enumerated and hash-bound by the runner as provenance inputs; they carry no automatic audit grade or claimed physical sufficiency.
- Historical original PR #8648, head `fe1e7a925c5b66b669b69afe57581cac0e60b404`, retains the complete seventeen-edition narrative, all menu descriptions, graph and original evidence. Its stronger interpretations are deferred. The current runner preserves the graph and all alternative-graph computations.

## No-Go Discipline Gate

N1: the negative assertion is only that this finite declared graph has no decision-free target. N2: no inherited no-go wall supplies a premise. N3: AND/OR semantics, source truth and graph completeness are modelling assumptions. N4: file references supply provenance, not implication. N5: exhaustive Boolean assignments can test all twelve decision bits; no physical lattice is executed. N6: adding other routes or changing an edge can change the result. N7: source labels cannot establish necessity or sufficiency of a theory. N8: original narrative and mutation reports are history; fresh controls and same-session review confer no audit authority.
