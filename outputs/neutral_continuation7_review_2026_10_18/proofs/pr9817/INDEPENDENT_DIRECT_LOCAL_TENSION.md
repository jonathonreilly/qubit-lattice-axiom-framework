<!-- Original PR9817 source SHA256 7ed12238d666a688489743d49b5f2395774fb42f6d95a1f9aa74a8c3885ec4ad. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Direct fourth-order tension in the local normal-form gauge

Checked 2026-10-18 against `/private/tmp/neutral_normalform_tension_root.md`. The argument closes the leading bulk-tension transfer for the fixed-order local homological construction, under the deep-interior/no-wrap assumptions. It does not identify all higher coefficients or source operators across gauges.

## Local reference and denominators

Choose an interior cluster whose full fourth-order support, including longitudinal neighbors introduced by the filters, stays away from both interval ends. Each participating column is then uniformly up or uniformly down on that enlarged neighborhood. For any finite flip set in the cluster, the change in longitudinal bond energy depends only on which bonds have one endpoint flipped, not on the original column sign. Distant pre-existing walls contribute the same energy before and after the local process and cancel. A nonempty finite flip set creates positive local walls; it cannot preserve N by compensating against a distant wall outside its support.

Thus every local denominator and intermediate N projection equals the corresponding zero-wall calculation with the same local column labels. The all-up assumption is not needed for the denominator signs; local longitudinal ordering is needed. Periodic wraps or a support reaching a column end would invalidate this simplification.

## Squarefree plaquette coefficient in this gauge

For a simple four-edge transverse square, every nonempty proper subset of its distinct edges leaves sites of odd incidence and therefore nonzero flips. It creates local walls and cannot return to the reference N sector. No folded return term can carry this same squarefree edge monomial. The direct fourth-order chain is consequently the coefficient already independently derived from the distinct-edge time integral:

    -1/(2d^3) product_corners Z,
    d=4Jz in the bulk,

or -Jx^2 Jy^2 P/(128 Jz^3). At Jx=Jy=lambda Jz this is -Jz lambda^4 P/128.

A precise way to avoid a gauge assertion is to freeze the surrounding ordered longitudinal spins for the finite cluster. Its local zero-wall reference is then an isolated one-dimensional ground space; the diagonal effective coefficient is the ordinary eigenvalue coefficient and is independent of a block-diagonal phase choice. Locality of the homological Taylor words transfers that coefficient to the deep interior of the full configuration, because all their supports and denominator changes are identical.

Equivalently, a finite-support N-conserving term cannot change one locally ordered column pattern to another: doing so would require flipping an entire ordered column segment extending outside the support, or creating walls. Such terms act diagonally on this local reference family. Lower effective terms and local block-diagonal gauge generators therefore cannot alter its diagonal squarefree coefficient through an interior commutator. This qualification is about the prescribed local homological gauges; an arbitrary nonlocal rotation inside the entire degenerate N sector is not covered.

## Exhaustion of diagonal fourth-order spin-sign terms

Each transverse V flips the two physical sites on its edge. For a diagonal matrix element every physical site must be flipped an even number of times. Distinct longitudinal slices contain different physical sites, so this even-degree requirement applies separately at each slice. With four total edges on a non-aliased square lattice, the only possibilities are:

- one simple elementary four-edge square on one slice;
- one edge repeated four times;
- two edges each repeated twice, on one or different slices.

In the repeated-edge cases, the number of Y insertions at every physical site is even. Acting on a Z-product reference, the Pauli phase can depend on the reference sign only through z_i raised to this Y count; those factors equal one. Noncommuting X/Y orderings can still produce minus signs, but these are constants independent of the column labels. The energy denominators are also column-sign independent by the previous paragraph. Hence repeated-edge patterns, including connected clusters spanning neighboring longitudinal slices, cannot produce a competing bulk column-orientation dependence. Folded/counterterm combinations of such patterns retain that property.

The same parity classification excludes orientation-dependent first- and third-order diagonal terms; second order consists only of a repeated edge and is likewise constant. These statements concern diagonal bulk tension, not endpoint hopping or other effective entries.

## Counting the tension

Each column belongs to four elementary transverse plaquettes. Two adjacent flipped columns share two plaquettes. Those shared plaquettes contain two flips and keep P=+1; the four plaquettes containing exactly one of the pair have P=-1. Each changes energy by 2Jz lambda^4/128. Therefore the interior energy increase per length is

    sigma = Jz lambda^4/16.

Endpoint terms are independent of length once the supports separate. At a fixed truncation order at least four, higher-order coefficients give smaller powers for sufficiently small positive lambda, so the leading positive tension is established in the actual local normal-form construction rather than merely imported from the earlier selected-sector matrix gauge.

Conclusion: the direct local classification is sound and narrowly closes the leading-tension condition. Keep the assumptions of local longitudinal order, non-wrapping supports, fixed order, and the local homological construction explicit. It does not equate the full higher-order canonical matrices, prove a pole of the microscopic Hamiltonian, select a state, or derive a measured coupling.
