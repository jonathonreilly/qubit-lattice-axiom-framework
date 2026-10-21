<!-- Original PR9798 source SHA256 5468059a2c3e14e03458e139b356d67557550de84ecfa7ce926d7870eabc6854. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Independent sixth-order vacuum diagonal classification

For a height-six periodic slab and a transverse grid large enough to have no noncontractible cycles of length at most six (for example both transverse periods greater than six), the proposed list is exhaustive: the diagonal N=0 coefficient through order six consists of a scalar, a plaquette-sum renormalization, and the adjacent-plaquette product from a simple 1 by 2 rectangle. The same classification applies locally away from transverse boundaries; uniform coefficients require the stated translation and x/y symmetries.

## Why no other background polynomial appears

A diagonal return to the original aligned-column computational state must flip each physical spin an even number of times. Transverse insertions preserve longitudinal layer, so the edge multigraph in every layer is Eulerian modulo two. The symmetric difference of its used edges is a union of cycles. On the nonaliased square grid, with at most six insertions total, the only nonempty possibilities are one elementary length-four plaquette or one simple length-six 1 by 2 rectangle. The empty difference consists of repeated-edge structures.

All longitudinal energy denominators for an aligned-column background depend on the flip pattern, not the initial column signs. At a site, a background Z factor arises only if both the total X and total Y counts are odd; this depends on the modulo-two edge graph. Thus repeated-edge structures give scalars. Plaquette words with an additional doubled edge, including a doubled edge at another longitudinal layer, give only the original plaquette polynomial. They may change its coefficient but cannot generate a second plaquette factor. A simple rectangle has odd X/Y incidence precisely at its four corners; its Z polynomial is exactly P_p P_q for the two constituent adjacent plaquettes.

A closed six-edge cycle must occupy a single longitudinal layer. Different-layer contributions with six total insertions can only have one four-cycle and a doubled edge, or repeated edges alone. Intermediate propagation in longitudinal energy does not move physical spin flips between layers and cannot change this classification.

## Rectangle coefficient and folds

I replayed `/tmp/neutral_sixth_loop.py`. Exact rational summation of all 720 orderings gives -3/8192 for either rectangle orientation, and the four-edge control gives -1/128. The code's denominators -4 times the intermediate flipped-spin count are correct for a single active layer of aligned height-six columns: each flipped spin creates two vertical walls, energy cost 4J. Its XX amplitude is -1 and its YY amplitude on a pair is +1 for equal current spins and -1 for unequal spins; therefore it retains the required Pauli ordering signs. No proper nonempty subset of a simple cycle returns to N=0, so all these paths are proper resolvent paths.

At sixth order a folded N=0 contribution that is background dependent can only combine the order-four plaquette structure with an order-two scalar, including resolvent-power/normalization variants. There is no lower-order adjacent-plaquette product, and two independent plaquette factors require at least eight insertions. Folds therefore modify the scalar or single-plaquette coefficient but not the rectangle coefficient. Summing over L longitudinal layers gives

D6_diagonal = scalar + c6 sum_p P_p - (3L/8192) sum_<p,q> P_p P_q,

where each unordered adjacent pair is counted once. At L=6 the displayed rectangle coefficient is -18/8192. The physical contribution includes J lambda^6. This conclusion does not determine c6.

## Winding and interpretation

At height six, six insertions can flip two complete neighboring columns. Those words are off-diagonal in the aligned-background basis, not an extra diagonal invariant. Their known coefficient is gamma6=J lambda^6 binom(10,5)/8^5=63 J lambda^6/8192, consistent with the stated kinetic term. They must be retained in the full order-six Hamiltonian even though excluded from this diagonal classification.

On a fixed-four-bad-plaquette sector, sum P is constant, so its unknown sixth-order renormalization is a common shift within that sector. The adjacent-product term is generally not constant: it distinguishes arrangements. This observation is not a proof that the fixed-four-flux subspace is invariant under the full order-six kinetic term.

Small transverse tori need separate treatment: cycles wrapping the torus with length at most six introduce additional structures or aliases. The finite-height coefficient calculation also does not by itself control a growing-height limit or select height six physically.
