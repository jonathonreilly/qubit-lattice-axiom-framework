# Eighth-order short-thin attraction: independent check

Disposition: PASS for the local, nonwrapping diagonal coefficient difference at height L>8, in particular L=10. The hopping/bound-mode transfer remains a subsequent calculation. At L=8 native winding already enters at this order and must not be omitted from a full coefficient Hamiltonian.

## Perimeter coefficient

I independently enumerated all 40320 ordered words of the eight distinct physical perimeter bonds around a 3-by-1 rectangle, applying each XX or YY directly to the spin bits. Each proper intermediate set has energy cost 4 times its flipped-spin count. The exact Fraction sum is -9/262144 per bulk z layer. This uses direct permutation summation rather than the root subset recurrence and agrees with it. Proper subsets of a simple cycle never return to the aligned manifold, so folded terms cannot contain this squarefree eight-edge monomial. The operator sign is the product of the four corner column Z signs (equivalently the product of the three enclosed plaquette parities). Thus c8=9L/262144 in the dimensionless lambda^8 coefficient.

## Short versus long thin rectangle

For an invariant -c8 times a translated three-plaquette straight product, each translate with an odd number of bad plaquettes costs 2c8. For a four-defect rectangle (a,1), horizontal straight triples have eight odd translates when a=2 and twelve when a>=4. Vertical triples have four in either case. Therefore the short thin endpoint has energy lower by 8c8 than the long thin arm. The rotated statement holds for (1,2). This is a relative energy, not its entire eighth-order diagonal energy.

Independent translated-mask counts also verify that single/adjacent/diagonal plaquette products, L triominoes, and 2-by-2 blocks have equal total values for (2,1) and (a,1), a>=4. More generally, any fixed invariant whose plaquette support has horizontal span at most one cannot cover both distinct bad columns at separation two; its contributions from those columns add and are independent of their separation. This handles each oriented shape separately and does not require equal coefficients for different shapes.

## Why the other eighth-order diagonal words cannot change this difference

Below winding order, returning to the aligned-column manifold requires even physical flip degree at every vertex in each z layer. The odd-multiplicity transverse edges therefore form an Eulerian square-lattice subgraph. With at most eight bond occurrences its nontrivial components are: a four-cycle with repetitions; a six-cycle with repetitions; an eight-cycle; or two four-cycles. Eight-cycles enclose a straight triomino, an L triomino, or a 2-by-2 block. Four/six cycles give single/adjacent plaquette products. Repeated edges change coefficients but not the column-sign monomial.

Two four-cycles can contribute connected terms when their physical supports overlap, including through vertical H0 bonds on the same columns at neighboring z layers. Their plaquettes are then equal, adjacent, or diagonal in the transverse array, so their plaquette supports span at most one in either direction. Two squares separated by two transverse cells have disjoint column supports. With all eight operations already used, no additional connecting edge exists; their disconnected contribution cancels in the energy/linked canonical coefficient, as it must for independent subsystems. Folded products inherit these same monomials and cannot turn a local pair into a separation-two invariant. Tree/repeated-edge words with no odd-edge cycle have background-independent sign and contribute only scalar terms.

Accordingly, only the straight triomino oriented across the thin rectangle can distinguish width two from width at least four at order eight. The result presumes the ordinary linked, symmetry-preserving canonical diagonal coefficient and a nonwrapping transverse geometry. It does not require values of the other eighth-order coefficients, but those coefficients are not determined by this difference calculation.

For L=10 the order-six nearest-plaquette attraction already separates thin and thick shapes. The additional order-eight endpoint well precedes the order-ten winding hopping. This is the correct hierarchy for subsequent boundary localization; an actual full-H pole, source residue, finite-size ground selection, or uniform growing-volume limit is not proved here.

Independent artifacts: /tmp/neutral_eighth_reviewer.py and /tmp/neutral_eighth_reviewer.json. Root file /tmp/neutral_eighth_rectangle.py was read; no repository edits or formal audit.
