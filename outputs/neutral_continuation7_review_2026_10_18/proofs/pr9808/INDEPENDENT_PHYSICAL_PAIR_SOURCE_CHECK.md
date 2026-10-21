<!-- Original PR9808 source SHA256 6ac06ad8a8e584e28a3bdc19a8956afb2ad5da049e01f3c13121d007986e1ab3. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Physical whole-column pair source: focused check

Disposition: PASS for the physical-source residue route and the second-order orientation factors, provided all Hamiltonian, state and source transformations are matched and the stated sufficiently high absolute remainder bound is retained. This removes the arbitrary reference-Hf choice from the measured matrix element; it does not establish a scattering rate.

Here D_r must be explicitly the microscopic product of X over the entire height-L column r. At fixed L=10 this has bounded support and norm one. The proposed operator is an actual finite-volume observable (possibly complex for other Fourier conventions), rather than a conserved-number projector. Its ordered r!=s sum is Hermitian for the displayed k,-k weights, since exchanging r,s conjugates the phase and D_r,D_s commute. It is translation invariant and preserves all full-plane characters: each individual D_r is charged under the Z planes, while its two-column product is neutral. Its norm is bounded by (R^2-1)/sqrt(1-2/R^2)=O(R^2).

## Finite-pattern locality and far pairs

A retained coefficient of any fixed-order local wall/Q transformation of D_r is supported in a fixed collar around column r and retains its exact charged character. Acting on the flat vacuum, it cannot be scalar or lie in Q0. A finite nonzero physical syndrome obeying the row/column constraints has at least four bad plaquettes. Therefore two such dressed charged clusters on disjoint collars create at least eight defects. They cannot project onto the Q4 bound-state sector. Any fixed-order contribution that joins their supports requires a finite connected sequence of local operations, and hence has a bounded relative range at that order.

The same statement holds if one keeps further Q-preserving endpoint transformations on the state rather than the source: at fixed order they are bounded-length paths from the compact endpoint configuration. There is no finite-order tail at arbitrarily large relative separation. This excludes disconnected far-pair contributions by charge and support, not by an assumed factorized interacting ground state. Ground scalar pieces of the complete pair operator should be centered before applying a Gram/norm argument; for its exact transition to an orthogonal bound state, subtracting that expectation makes no difference.

At each retained order the resulting relative-coordinate form factor has finite support with bounded l1 norm independent of R. The endpoint tail expansion is controlled by the small lambda^2 hopping/depth ratio; fixed-order truncation is sufficient, with the rest in the final high-order tail. Thus the correction gives O(lambda^2/R) rather than merely O(lambda^2) in the individual normalized pair-source matrix element. This argument applies only after keeping the dressed charge, source and eigenvector in the same frame. Multiplying a bare P2 overlap by a global state-fidelity estimate would not establish it.

## Leading normalization and second order

Put N=R^2. For generic k with 2k not reciprocal, the exact leading matrix element into B0=(A+B)/sqrt(2) is

 sqrt(2)/[R sqrt(1-2/R^2)] * (cos kx+cos ky).

The denominator may be replaced by one at the displayed accuracy along R~lambda^-p with p>1, but should be retained for a fixed finite-box formula. At self-inverse k the physical operator as defined still has its stated prefactor, but it is no longer a unit-normalized identical-pair source. If one wants that normalization, replace the generic normalization by the separately derived identical-pair convention; do not silently reuse the generic formula as a normalized k=0 state.

For the order-lambda^2 wall dressing, a single transverse bond creates two flipped physical spins at cost 8J, so its first-order virtual amplitude has magnitude lambda/8. Conjugation by D_r D_s reverses the sign of YY bonds crossing its two selected columns, and commutes with XX and with internal YY bonds. In the matched initial/final wall-free overlap, each reversed virtual bond contributes -2(lambda/8)^2=-lambda^2/32. Unreversed contributions cancel against normalization. At two insertions no other N0 column pattern can be reached at height ten.

An adjacent x pair has 4L such external YY bonds; an adjacent y pair has 2L. Hence its source amplitudes are respectively

 1-Llambda^2/8, and 1-Llambda^2/16.

Independent bond counting on R6 and R8 gives 40 and 20 at L=10. The bound endpoint's normalization correction starts at lambda^4: its order-lambda^2 tail is a longer thin rectangle with more than two flipped columns, so the leading physical two-column source has zero overlap with that tail. Vacuum mixing starts later, at lambda^6. Thus the next source form factor is

 sqrt(2)/[R sqrt(1-2/R^2)] *
 [(1-Llambda^2/8)cos kx+(1-Llambda^2/16)cos ky]

up to higher retained terms and the exact high-order tail. With even-lambda symmetry the next retained correction is O(lambda^4/R). This is an additive form-factor expansion; near zeros of cos kx+cos ky it should not be described as a uniform relative error.

## Exact-state tail powers

A final absolute Hamiltonian remainder R^2 lambda^M divided by the same-fibre lambda^14 pole gap gives state error R^2 lambda^(M-14). Multiplication by the physical pair-source norm O(R^2) gives R^4 lambda^(M-14). To make this o(lambda^2/R), it suffices that

 M>16+5p.

At p=5, M=60 the error is O(lambda^26), compared with lambda^2/R=O(lambda^7). The ground projector uses a larger gap and is harmless. The transformed source itself must also be retained to sufficient order; its global remainder is no larger at these powers when the joint local expansion is used. Centering may at most multiply the crude norm bound by a constant.

The resulting weight |<B|O_k|ground>|^2 is a physical spectral atom of this explicitly defined source, from the chosen actual global ground supplied by the reflection theorem and low-sector uniqueness. It is source dependent and finite-volume normalized. It is not a T-matrix, a pair-to-bound on-shell conversion probability, a lifetime, or a universal coupling. The inherited bound-state existence and high-order local estimates remain inputs to this focused source check.

No repository edits or formal audit.
