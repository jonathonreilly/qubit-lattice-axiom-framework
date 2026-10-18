# Native bond-centered energy source: focused check

Disposition: PASS for the leading form factors, source weight and transfer exponent. One necessary remainder clarification: the lower-band matrix element also has an orientation-mixing error O(J lambda^(L-2)|q|^4). It is small for q<<lambda, but is not generally bounded by O(J lambda^(L+2)|q|^2).

The operator is the explicitly supplied bond-centered energy density

 H_q=V^(-1/2) sum_b exp(-iq dot center_b) h_b, qz=0.

At zero momentum H_0=H/sqrt(V), so every transition from an exact ground state to an orthogonal eigenstate vanishes exactly. This fact must be retained through all matched transformations.

## Fourth-order plaquette form factor

For a square loop, marking a numerator bond gives the sum of four bond-center phases relative to the plaquette center, 2cx+2cy, cx=cos(qx/2), cy=cos(qy/2). Marking a longitudinal denominator weights its flipped physical vertices. The three denominators give total mark three; symmetry makes each corner coefficient 3/4. Summing the four corner phases therefore yields 3cxcy. Thus

 F4=2cx+2cy-3cxcy.

I independently enumerated all 24 ordered square words with exact rational denominators and their vertex marks. The total coefficient is -1/128 and each weighted vertex coefficient divided by that total is exactly 3/4. This checks the denominator subtraction and its normalization without assuming a spatially uniform source. F4(0)=1, as required by differentiating a homogeneous energy coefficient under a uniform rescaling of H.

For a minimal length-L x-column winding, all L transverse numerator bonds have the same projected midpoint. Every intermediate flipped layer has equal contributions from the two endpoint columns, giving the denominator phase cx. There are L-1 denominators. Consequently Fwx=L-(L-1)cx, and Fwy is its rotated counterpart. Both equal one at q=0.

## Matched leading transition

The x-pair's four bad plaquettes contribute the static contrast phase cos(qx)cy. Direct winding gives -t Fwx; the ground-mixing diagonal-source term gives +t F4 cos(qx)cy. With normalized translation states and V=LR^2 the resulting two-component source is

 J gamma lambda^L/sqrt(L) *
 (F4 cos(qx)cy-Fwx, F4 cos(qy)cx-Fwy).

The components vanish at q=0 before projection onto a mode. Expanding,

 F4 cos(qx)cy-Fwx=-(L+2)qx^2/8+O(|q|^4),

and similarly for y. Projection onto (A+B)/sqrt(2) gives

 -J gamma(L+2)lambda^L |q|^2/[8sqrt(2L)].

Its leading atom weight is J^2 gamma^2(L+2)^2 lambda^(2L)|q|^4/(128L). Thus the numerical and normalization factors in the proposal are correct.

A high-wall canonical-frame connection cannot alter this leading result: real local source variations give antisymmetric connection matrices with zero diagonal; changing two full height-L columns first occurs at order lambda^L, and commuting with the nonconstant N0 energy adds lambda^4. The displayed order-lambda^L source is earlier. A later Q-block rotation has small denominators and must transform the observable explicitly; treating its effective-H derivative as the source while dropping the connection would not be justified. The direct winding-plus-ground-mixing expression is the matched leading calculation.

## Remainder structure

For the source vector in centered orientation coordinates, inversion forbids odd q, exact H_0 conservation removes the constant term at every retained order, and checkerboard symmetry removes odd lambda orders. Fixed-range spatial-moment bounds therefore give higher native source terms O(J lambda^(L+2)|q|^2), plus the ordinary O(J lambda^L |q|^4) expansion term.

The lower eigenvector itself differs from (A+B)/sqrt(2) by O(|q|^2/lambda^2): its diagonal imbalance is order lambda^12 |q|^2 and its splitting order lambda^14. The source has an antisymmetric component of order lambda^L(qx^2-qy^2). Their product adds O(J lambda^(L-2)|q|^4). This term should appear in the lower-mode error statement. For q~lambda^p with p>1 its relative size is O(lambda^(2p-2)), so it does not invalidate the leading weight. For 1<p<2 it can exceed the relative O(lambda^2) native-source correction.

## Actual polynomial-grid transfer

The source norm is O(JR) at fixed L. A final absolute Hamiltonian tail J R^2 lambda^M divided by the same-fibre lambda^14 gap produces a source error O(J R^3 lambda^(M-14)). For L=10 the leading amplitude is order J lambda^(10+2p), so relative vanishing requires M>24+5p, exactly as proposed. To control the more stringent subleading lambda^(L+2)|q|^2 scale by this crude bound would require M>26+5p. Source transformation tails must be retained consistently; the larger ground gap is not limiting. Other momentum spacings are not denominators.

## Meaning of energy density

The microscopic Hamiltonian fixes H_0, but does not uniquely fix an energy density at nonzero momentum. The bond-center prescription is a clear native definition and introduces no interaction; it remains a specified observable convention. Adding a local lattice divergence leaves total H unchanged and can change nonzero-q form factors, including the q^2 coefficient under suitable symmetric improvements. Thus the coefficient is not a convention-independent universal energy coupling. The result is an original-H spectral readout for this specified density, not an on-shell rate or a force law.

No repository edits or formal audit.
