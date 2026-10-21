<!-- Original PR9807 source SHA256 15accca4bf866a561cf40221a5720efe91287ed929effdebbc8aac0e7db4e979. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Q8 orientation mixing: independent fourth-hop check

Disposition: PASS for the local leading orientation-mixing coefficient, with the fixed-height/nonwrapping and matched coefficient-frame scope described below. This is a next-block result, not a change to the already reviewed rank-two theorem.

## Independent exact enumeration

I did not reuse the root's forward syndrome-candidate recurrence. For each translated vertical final pair, I enumerated all minimum-length square-lattice edge sets with odd boundary equal to the initial/final column symmetric difference. These are obtained from all shortest Manhattan pairings of the odd vertices, including the shared-column cases with only two odd vertices. I then enumerated all 24 edge orders, retaining only Q8 intermediates outside the endpoint-minimum manifold, and used exact Fraction denominators perimeter(S)-12.

This reproduces all nine outputs:
- Final center (0,0): 9673/12000, 36 valid ordered paths.
- Each axial center (+/-1,0),(0,+/-1): 191/384, 20 valid ordered paths.
- Each corner center (+/-1,+/-1): 1637/4608, 24 valid ordered paths.

Their sum is exactly 607201/144000. The coefficient is in units gamma^4/(2b)^3. Four negative hopping factors and three negative energy denominators give an overall negative matrix element, so

 H_AB(0)=-J [gamma^4/(2b)^3] [607201/144000] lambda^22.

The translated-center kernel is real and reflection-even. Its Fourier polynomial, apart from the common negative prefactor, is

 9673/12000 +(191/192)(cos qx+cos qy)
             +(1637/1152)cos qx cos qy.

## Minimal order and other native moves

A horizontal distance-two pair and any vertical distance-two pair require at least four elementary transverse edge flips to change one into the other. When they share a column, the two remaining odd vertices are Manhattan distance at least four. With four distinct columns, the minimum total matching distance is at least four. The nine centers above are exactly those attaining four; other centers require more. Repeated edges cannot occur in a length-four minimum realization because they would leave a shorter impossible odd-boundary realization.

For the actual native spin words this counting applies separately at each of the ten longitudinal layers: the initial/final column difference is present in every layer, and transverse XX/YY insertions supply the odd endpoints. Thus at least forty microscopic transverse insertions are needed in total. Order-one wall denominators do not change that lambda power.

In a low-charge expansion the leading full-column elementary move costs lambda^10. The smallest eliminated Q8 gaps are order lambda^6. Four such moves with three Q8 denominators give lambda^(40-18)=lambda^22. Fewer longer native transitions cannot improve the order: they still need at least forty microscopic insertions but have fewer enhanced denominators. Extra elementary moves increase the power, since each additional move costs at least ten powers and supplies at most one six-power denominator. A route leaving Q8 encounters an order-lambda^4 charge denominator instead and is later. This counting presumes the full endpoint manifold, including translations and both orientations, is retained; one must not divide by a vanishing internal endpoint splitting.

Diagonal corrections beyond the leading lambda^6 perimeter operator increase the order. They cannot create an earlier background transition. The leading perimeter spectrum should be included in the unperturbed denominators as done in the root script.

## Canonical folded terms

The endpoint-minimum manifold has no first-order elementary hopping within itself. At fourth hopping order, the canonical folded terms are products of two-hop energy/norm matrices (the usual anticommutator contribution). Both of those matrices preserve orientation: two elementary edge operations cannot turn a horizontal endpoint pair into any vertical one. Their products therefore have zero horizontal-to-vertical matrix element. Terms involving a one-hop endpoint matrix vanish as well. Consequently no folded term changes the leading off-diagonal coefficient just enumerated. This is a matrix-element statement, not a claim that all fourth-order diagonal folds vanish.

The negative off-diagonal coefficient selects the C4-even combination as the lower member at q=0, with splitting twice its magnitude, once the uniform higher-order remainder is smaller than lambda^22. This is compatible with the previous proof, which left the sign undetermined.

The diagonal orientation imbalance from dispersion is order lambda^14 q^2. Comparing it with lambda^22 gives the isotropic-mixing condition |q|<<lambda^4. The earlier polynomial-grid embedding restricted to 1<p<2 cannot realize nonzero grid momentum in that regime. Thus this coefficient resolves the q=0 source-band ordering but does not upgrade that family to an isotropic dispersion limit.

Independent artifacts: /tmp/neutral_q8_orientation_reviewer.py and /tmp/neutral_q8_orientation_reviewer.json. Root /tmp/neutral_q8_orientation.py was read, not changed. No repository edits or formal audit.
