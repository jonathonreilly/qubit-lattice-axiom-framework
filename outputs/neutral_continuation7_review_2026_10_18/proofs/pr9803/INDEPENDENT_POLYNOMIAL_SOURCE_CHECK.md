<!-- Original PR9803 source SHA256 719522857c31366e4b7c93b16ce1ca3bd0164a42cf39d1d94f53d214c05da556. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Polynomial-grid source and embedding final check

Disposition: PASS for sections 1, 2 and 5, using the uniform retained two-orientation reduction and momentum estimates in section 4 as the separately checked dynamical input. No material correction requested in the reviewed sections. This scoped report does not independently certify every path/momentum assertion in section 4.

## Embedding and exact pole

Section 2 correctly supplies the missing fixed-height mechanism. The full-column reference-spin/wall-bit encoding is exact; completing a bounded support to full height-ten columns costs a constant independent of R. Individually N-preserving local terms agree with their wall-free extension on the no-wall subspace and their Hermitian difference is sandwiched by the local wall projector. Consequently the form bound C lambda N is valid. Since the common scalar-subtracted N0 bandwidth is O(lambda^4 R^2), the whole N0 band remains isolated by an order-one gap for p<2. This requires no assumption about the logical ground, and allows whole-column flips at fixed height as the proof explicitly states.

Each successive finite-order construction can be carried far enough to leave an absolute global Hamiltonian tail C R^2 lambda^40. There is no need for infinite-series convergence or order-uniform constants. Existing exact-product local analyticity controls the transformation tails at any fixed chosen order. Charge rescalings change the number of formal orders required, but one chooses the order before restoring the physical powers. Exact unitary conjugations do not enlarge an already bounded global remainder. The shorthand 'M=40' should be read as the final absolute remainder exponent, as the text does, rather than forty terms of every differently rescaled series.

In the chosen plane fibre, the reduced Q0 vector is unique and translation-invariant. Q4 excitation clusters have a lambda^4 separation from other charges. Within a fixed momentum fibre near q=0, the endpoint orientation pair has separation 2J eta lambda^14[1+o(1)], provided the stated uniform endpoint reduction holds. The lower member is simple there; the microscopic tail is much smaller than that gap. Thus the actual finite-H atom assertion follows in that selected fibre, without a global ground-character theorem. Section 1 correctly distinguishes this from spacings between distinct momenta, which can be smaller.

## Source Gram after all matched transformations

The source conclusion is not invalidated by QSW. At each fixed order, conjugation by the finite-range QSW generators expands a local source density into finitely many bounded-support connected terms. The original N transform has the same property for each retained coefficient. Symmetry averaging and taking charge components only enlarge those supports by fixed collars. All these statements hold before any crude global norm estimate.

Acting on the selected flat Q0 vector, a finite-support off-diagonal pattern creates a definite finite syndrome (or a finite sum of them). For R exceeding the fixed support diameter, separated nonempty syndromes are orthogonal even after the positive plane-orbit quotient. Coincident syndromes have only bounded multiplicity among translates. A nontrivial finite-support flat row/column flip is impossible at that size. Purely diagonal or zero-syndrome pieces act as scalars on this vacuum; removing the ground component eliminates precisely the otherwise coherent, volume-enhanced contribution. Hence the normalized translated sum has squared norm O(1) for every retained excited coefficient. This is the needed Gram argument, not an assumption of clustering or independence in a generic state.

If the subsequent thin/endpoint identifications are included in the source, their retained coefficients are finite sums of bounded-length paths acting on these finite defect patterns, with bounded matrix elements after their prescribed powers of lambda are factored out. They preserve the same fixed-order norm estimate. Equivalently one may keep the source in the Q-normal coordinates and transform only the target eigenvector; unitarity gives the same overlap. The proof must continue to use this matched convention, as it currently does.

The first nonzero Q0-to-Q4 coefficient is the inherited direct-winding plus ground-mixing combination, not a consequence of the Gram bound alone. Section 5 correctly imports that calculation and retains beta rather than the bare derivative. At L=10,

 beta=165/17,
 2 gamma^2 beta^2/L=2783620125/1125899906842624.

Small-q finite-pattern form factors approach the q=0 vector uniformly as R grows. For q/lambda->0 the orientation imbalance relative to its lambda^14 gap vanishes, so the target eigenvector tends to (A+B)/sqrt(2). The nonzero source coefficient and the stated positive leading atom follow. Centering at q=0 is necessary; for nonzero Fourier momentum the unique translation-invariant sector ground already has zero expectation.

## Errors and scope

The exact normalized source obeys ||C_Q||<=sqrt(V)=O(R), also for complex Fourier weights. A Hamiltonian tail O(R^2 lambda^40), divided by the fixed-fibre lambda^14 gap, gives state error O(R^2 lambda^26). Multiplying by this source norm gives O(R^3 lambda^26). At p=21/20 this is lambda^(457/20)=lambda^22.85, negligible relative to the leading lambda^10 amplitude. The sector ground error uses the larger lambda^4 gap and is smaller. Source-transform tails can independently be retained to sufficient fixed order with the same local-majorant method. No full-band momentum spacing is used.

The leading dispersion signal lambda^12 q^2 has exponent 14.1; the displayed lambda^10 q^4 error has exponent 14.2 and the global remainder exponent 37.9. This arithmetic is correct. Deriving that dispersion error still rests on section 4's spatial-moment/path estimates; a gap and global norm bound alone would not imply it.

All claims remain about the supplied fixed-height Hamiltonian and selected exact plane-sector ground. The proof explicitly does not establish uniform global-ground character selection, practical lambda thresholds, three-dimensional propagation, or observational identification. Those exclusions are substantive and sufficient for the reviewed source/embedding assertions.

Reviewed source SHA256: 8c960827db34dd6850c505745555316822e88a2b67589092d90c1401cff12d82
No shared source edits, numerical replay, or formal audit.
