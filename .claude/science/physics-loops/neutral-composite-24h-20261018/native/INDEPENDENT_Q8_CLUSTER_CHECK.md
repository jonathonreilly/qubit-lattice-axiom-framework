# Eight-flux cluster geometry and leading hopping

Disposition: PASS for the nonwrapping coefficient-sector geometry and the stated order-lambda^14 hopping. The gap to the two-well-separated-column continuum is D lambda^6, but the smallest gap to another Q8 configuration is D lambda^6/2; these should remain distinct.

## All minimum shapes

For -b sum_nearest Pp Pq, relative to the flat vacuum a bad-plaquette set S costs 2b times its edge perimeter. An eight-cell set of perimeter at most twelve must be connected: splitting area eight into two or more components gives perimeter at least sixteen by the elementary lattice perimeter-area bound. Its occupied bounding box has width w and height h with w+h<=6 and wh>=8. The only possibilities are 2-by-4, 4-by-2, and 3-by-3. In the first two cases all cells must be filled. In the last case eight occupied cells leave two full rows of three, violating even row syndrome parity, regardless of which cell is absent. Thus the only allowed perimeter-twelve minima are the filled 2-by-4 and 4-by-2 blocks, up to translation.

Inverting the plaquette syndrome for finite-support column flips gives two flipped columns separated by two along the long axis. Their total column parity is positive. On a torus this statement is modulo flat row/column backgrounds in the specified plane-character quotient; it assumes no short wraps. It is not uniqueness of a raw column configuration across all characters.

Separated single columns each have a 2-by-2 bad-plaquette block of perimeter eight, giving total perimeter sixteen. The compact pair therefore binds by 2b*(16-12)=8b=D=3L/1024 at order lambda^6. A pair at relative displacement (2,1) has perimeter fourteen and lies only 4b=D/2 above the minimum. A pair at displacement (3,0) has perimeter sixteen. Adjacent flipped columns instead have Q4 and belong to a different leading charge cluster.

## Exhaustive two-edge moves between minima

Take initial columns {(0,0),(2,0)}. Independent enumeration applied every pair of nearest-neighbor edge XORs in a surrounding box, including intermediate states with four flipped columns. The only distinct final minimum configurations reached are its four unit translates. No orientation-changing or extra translating path occurs in two operations.

For translation by +x the two possible orderings have intermediates {(0,0),(3,0)}, with Q8 and perimeter sixteen, and {(1,0),(2,0)}, with Q4. The first gives

 (-gamma lambda^10)^2/[-D lambda^6]
 =-gamma^2/D lambda^14.

The Q4 intermediate has a denominator of order +lambda^4 relative to the Q8 initial energy, and hence contributes at order lambda^16, not lambda^14. It cannot double the leading coefficient. The -x result is identical.

For translation by +y, the two orderings have relative displacements (2,+1) and (2,-1), each Q8 and perimeter fourteen. Each denominator is -(D/2)lambda^6, so the two contributions sum to -4gamma^2/D lambda^14. The -y result is identical.

Thus t_parallel=gamma^2/D and t_perp=4gamma^2/D in the coefficient of J lambda^14, and the leading orientation-resolved band is

 constant -2J lambda^14[t_parallel cos(qx)+t_perp cos(qy)]

for a horizontally aligned pair; the vertical orientation is rotated. This gives anisotropy four. Translation-orbit normalization at nonwrapping generic size adds no factor: the real-space pair orbit has R^2 states, and these are ordinary unit translations. This is different from the relative-coordinate factor two in the earlier four-arm star.

No direct native order-fourteen matrix element can bypass this count: translating the pair changes four full height-ten columns, requiring at least twenty transverse spin-flip insertions. The order-fourteen term is produced by the small lambda^6 internal energy denominator. Other higher native coefficients and denominator corrections produce later terms, while common diagonal corrections affect the absolute energy. Proving a full microscopic pole or its source coupling still requires the corresponding reductions and state assumptions.

Independent scratch /tmp/neutral_eightflux_reviewer.py and /tmp/neutral_eightflux_reviewer.json contain exhaustive small-box perimeter/parity classification and both-edge path enumeration. No shared source edits or formal audit.
