<!-- Original PR9820 source SHA256 afccb14c2bcc326640f06288c214583df8a5219e18bbd274271fa56a9471318e. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native Q8/perimeter24 tetramer: focused check

PASS for the native D8 extension, four-dimensional same-momentum band, and stated total-band source coefficient, with normalization and final-tail conditions specified below. No D10 splitting, mobility, molecular scattering or individual-pole residue follows from this check. No repository edits or formal audit.

## D8 completeness really extends

Read /tmp/neutral_pair_q8_per24.py and the independent exhaustive geometry report. The complete connected graph argument in INDEPENDENT_SECONDARY_ENERGY_CHECK.md applies before fixing perimeter: at eight insertions below L10 winding, layerwise even vertex degree leaves scalar, single-P, nearest-neighbor PP, the straight-three/box/L primitive products, and connected diagonal PP from touching squares. Repeated edges do not change the background sign monomial; disconnected square products cancel with folds. Thus the omitted terms are genuinely scalar/P/nearest-PP on the full column space, not merely numerically constant on perimeter16.

Their sums depend only on Q and perimeter and are consequently common also on Q8/perimeter24. The same distinguishing functional is valid here. This resolves the geometry report's stated native-invariant caveat; it is important to cite this complete graph reduction, rather than only the old perimeter16 list of minima.

The geometry enumeration has a valid finite reduction: at most four occupied syndrome coordinates per axis, and gaps classified as 1,2,odd>=3,even>=4 suffice for span-two invariants and inverse parity. The independent 5/6 representative check reproduces all 4912 types, including unbounded inverse shapes. Minimum −5832/21233664=−9/32768 and next value −2916/21233664 differ by 9/65536. Four oriented minima remain after translations: the stated collinear double-dimer and transversely separated double-dimer, plus their rotations. No hidden large-gap family shares the minimum. Use sufficiently large tori and the positive-plane flat quotient; small-wrap aliases are excluded.

## Native band statement

Two distant adjacent-column Q4 neutral features have Q8 and perimeter24, so their common order-four/six energies match this manifold. The derived difference is −Jv lambda8, v=9L/32768. Hence all four eigenvalues in its motif band obey

 E_tet−Eg=2epsilon_neutral(0)−Jv lambda8+O(Jlambda10).

Here epsilon_neutral is the excitation gap, and the O(lambda10) allows both common corrections and uncomputed internal splitting. Existing neutral kinetic corrections start later and do not invalidate this order statement.

The nearest other shape in the same perimeter manifold has gap Jv lambda8/2 at leading order. Other Q8 perimeters are separated at order lambda6; other low fixed Q sectors at order lambda4. Global Q-relative positivity and the wall embedding handle arbitrarily high Q and wall sectors. Fixed-Q connected coefficients have volume-independent norm after vacuum subtraction, so order-ten perturbations cannot close the order-eight gap for small lambda. This yields an isolated rank-four cluster per exact momentum/plane fibre, not four resolved isolated poles and not a uniform gap between neighboring momenta. Retain the complete four-state subspace rather than choosing an uncomputed eigenvector.

For any fixed R~lambda^−p, sufficiently high final order makes the absolute tail JR²lambda^M smaller than lambda8 and the retained energy accuracy. M>10+2p is sufficient to make it o(lambda10). The constants depend on fixed L and normal-form order. The statement is not fixed-coupling infinite-volume control.

## Original physical four-column source

For a motif T let X_T be the product of whole-column X operators. Every YY bond with exactly one selected endpoint changes sign under conjugation; XX and internal YY bonds do not. If nY is the number of transverse y-edges crossing T, there are L nY reversed physical bonds. Each first virtual amplitude has magnitude lambda/8 and its matched overlap change is −2(lambda/8)². Thus the low-wall source amplitude is

 1−L nY lambda²/32+O(lambda4),

and its total tetramer-band weight is

 1−L nY lambda²/16+O(lambda4).

For the horizontal motifs nY=8; their rotated vertical motifs have nY=4. At L10 the weight coefficients are respectively −5 and −5/2. This orientation dependence belongs to the X-only probe and is not an isotropic-scalar claim. A physical X/Y average or other specified combination needs its own normalization, rather than averaging the already squared weights.

At two native insertions no different wall-free L10 column pattern can occur, so the ultraviolet correction is diagonal on the motif pattern. Mixing with other shapes has amplitude O(lambda²) from lambda10/lambda8 and loses weight only at O(lambda4); rotations within the four-state cluster do not change its total projector weight. Ground winding corrections start at lambda6 and cannot affect the displayed order-two coefficient. Matched source/state transforms are required; independent fidelities cannot be multiplied to obtain this factor.

Normalize carefully: a local X_T acting on the ground has this weight in the WHOLE tetramer band summed over momenta. At one specified momentum its leading weight is 1/R². A normalized translated source R^−1 sum_r exp(−iq·r)X_(T+r) has leading same-fibre band weight one, with the same correction. It creates one motif vector, not four independently normalized copies. The result is for total rank-four band weight; individual poles require the unresolved D10/internal eigenvectors.

For the translated source, crude projector error times its O(R) norm is R³lambda^(M−8). M>12+3p suffices for an error o(lambda4), besides retaining the source transformation to matching order. A local norm-one source instead needs M>12+2p by this crude bound. Finite-pattern Gram estimates control the retained source corrections independently of volume. These are sufficient powers, not asserted optimal ones.

This is a promising native bound cluster/selfinteraction consequence, but no effective oscillator interaction, individual tetramer pole, propagation coefficient or rate has been supplied by its existence alone.

## D10 shape-selection and scalar-source addendum

PASS for the proposed B−A coefficient, conditional on the already independently checked touching six-plus-four and doubled-bridge coefficients. Replayed /tmp/neutral_tetramer_d10_shapes.py to /tmp/neutral-tetramer-d10-review.json and separately checked all six lower-invariant D4 orbit counts and the final rational combination.

The graph exhaustion is consistent. A diagonal word below whole-column-changing order reduces layerwise to an Eulerian odd-edge graph. At ten insertions, simple ten-cycles give exactly the six polygon families enumerated (area at most six). Repeated-edge decorations of four-, six- or eight-cycles preserve their old sign invariant, whose full D4 orbit counts agree for A and B. A six-plus-four connected graph yields old products or the new skew-three-P orbit. Two squares with two extra insertions yield old PP products or, when a doubled transverse bridge connects disjoint supports, PP20/PP21. PP20 counts cancel. Vertical linking without a new transverse bridge only decorates touching/old invariants. Empty odd graphs are scalar. Proper projected returns/folds change coefficients but not this sign-support list; the inherited connected coefficients must include them, as stipulated.

The six primitive contributions sum to 199/2097152. The skew-three-P odd-count difference is eight, so its energy contrast is −16*(331/226492416). PP21 has odd-count difference four and negative coefficient −75101/97844723712, giving +8*75101/97844723712. Their sum is 949685/12230590464>0, in units JLlambda10. Thus B is higher and the two collinear A orientations are selected before order lambda12. No scalar-decoration coefficient needs to be guessed because all its relevant orbit counts cancel.

At native order ten a winding flips only two adjacent columns. No two distinct motif minima differ by that operation, so its projected offdiagonal matrix on the four minima vanishes. Virtual feedback via an order-eight shape gap first enters lambda12 and cannot change this leading A/B ordering. No individual absolute D10 energy or motion coefficient is thereby determined.

At total momentum zero, the two A orientations decompose into one A1 and one B1 representation. This gives a unique A1 vector within the selected two-state manifold independent of the uncomputed A1/B1 splitting sign. It does NOT prove A1 is the lower state across those two irreps; state isolation must be explicitly restricted to A1 if that sign remains unknown. The higher B-derived A1 state is separated at order lambda10.

The normalized q0 source combining horizontal collinear X-column motif with vertical collinear Y-column motif, with factor 1/sqrt(2) between their normalized translation sums, is an exact physical C4-even choice. At even L10 the Y four-column product agrees with its X counterpart on N0, without an extra phase. C4 exchanges these two physical components. Each chosen component reverses eight relevant transverse boundary bonds per layer (YY for horizontal X, XX for vertical Y), so both give amplitude 1−Llambda²/4 and weight 1−Llambda²/2+O(lambda4). At L10 the coefficient is −5. This is different from an X/X combination whose vertical component has only four YY boundaries. The stated factor is correct for the X/Y covariant source, not a naive averaging of the X-only weights.

Mixing with other D8 shapes starts at amplitude lambda², and mixing with higher B states across the D10 gap can likewise start at lambda² if the offdiagonal begins at lambda12; both affect this endpoint-only source weight at lambda4. A final translated-source projector estimate now uses the relevant A1 gap lambda10: a sufficient crude condition for o(lambda4) accuracy is M>14+3p. The earlier rank-four total-band bound used the larger lambda8 gap; retain that distinction when packaging the resolved A1 source theorem.
