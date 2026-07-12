# Route portfolio

## Minimal premise reset

`B = (I, {H_i}, tensor identification)` with finite `I`, at least two factors,
and factor dimensions at least two.

Forbidden positive imports: graph, Hamiltonian, time parameter, state-update
law, measurement context, probability measure, noncontextuality, support-to-edge
rule, observed target, or fitted selector.

## Fan-out

| Route | Intended movement | Hard-residual pressure | Result |
|---|---|---:|---|
| automorphism/naturality graph selector | constructive theorem | 3 | fails: empty and complete graphs are both fully permutation invariant |
| operator-support locality | constructive theorem | 3 | exact positive survivor only after an operator is supplied; no operator is selected |
| Wigner/Stone dynamics | constructive bridge | 3 | conditional on transition-probability preservation or a continuous unitary time action |
| Hilbert-norm Born rule | constructive bridge | 3 | fails: normalized contextual `p=2` and `p=4` readouts coexist |
| Gleason-type reconstruction | constructive bridge | 3 | viable only on a richer probability/noncontextuality surface |
| current-framework collapse | atlas reuse | 2 | fails: Lattice supplies adjacency separately; dynamics/Born remain outside axioms |
| same-reduct expansion theorem | exact no-go | 3 | selected and completed with graph, dynamics, readout countermodels |

## Selected route and review split

The same-reduct construction changes the claim state directly and does not
depend on a search cutoff. Review iteration 1 found that retyping the existing
high-in-degree ID to `no_go` would let negative status satisfy positive
consumers. The coherent fix is a two-row split: the original path carries exact
factor locality and conditional consequences as `bounded_theorem`; a new leaf
row carries the physical-selector no-go and N1-N8 packet.
