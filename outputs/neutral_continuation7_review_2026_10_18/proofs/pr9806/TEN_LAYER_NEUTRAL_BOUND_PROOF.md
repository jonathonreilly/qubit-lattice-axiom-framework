<!-- Original PR9806 source SHA256 45d290bbd0f5ee4d9b1e1cb517a9fbfc33f6fa63ed28c19a6f8e1f958658240a. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native attractive neutral mode at ten layers

Status: conditional-support. The supplied one-qubit Hamiltonian generates the attraction, motion and original-readout coupling below. No new interaction, oscillator or coupling constant is introduced. The Hamiltonian, weak anisotropy, periodic slab geometry and measurement identification remain premises. Positive dispersion is a coefficient-level small-momentum result, not a demonstrated relativistic field or observational test.

## 1. Native hierarchy

Use H=-J sum_z ZZ-Jlambda(sum_x XX+sum_y YY), fixed even longitudinal height L>=10, even transverse R large enough to exclude all short wraps. Work in the exact positive plane-character fibre, and at momentum zero in its C4-even representation for the source pole. The aligned-column code has plaquette signs P and native adjacent column flip E. Its four-bad-plaquette sector has rectangle corners with even enclosed area. No additional physical qubits are present.

The inherited native diagonal orders are -JLlambda^4 sum P/128 and at sixth order -Jlambda^6[(25L/18432)sum P+(3L/8192)sum_nearest P P]. Thin four-defect rectangles (a,1) or (1,b), with even a,b, lie below nonthin ones by

 J D lambda^6, D=3L/1024.

Their common excitation energy starts JLlambda^4/16+181JLlambda^6/9216. Higher common diagonal shifts are not computed here and must not be dropped. The first column-changing term is -J gamma_L lambda^L sum E, gamma_L=binomial(2L-2,L-1)/8^(L-1).

## 2. Derived eighth-order attraction

At order eight, a diagonal return has an Eulerian transverse edge graph in each longitudinal layer. Nontrivial connected invariants comprise a plaquette with repeats, a six-cycle with repeats, a simple eight-cycle, or two four-cycles with interacting column support. Disjoint column supports factorize and their connected energy contributions cancel after folds. The eight-cycles enclose straight or L triominoes, or a 2 by 2 square. All these invariants except the straight triomino have plaquette-anchor span at most one in each direction. Thus their sums have the same value on every nonwrapping thin rectangle of even length at least two: they cannot see both separated ends.

The straight 1 by 3 perimeter has no proper wall-free return. Exact ordering of its eight native edges gives -9/262144 per longitudinal layer. A subset recursion using the intermediate flipped-spin mask reproduces the independently summed 40320 words. Its background polynomial is the product of the three enclosed P signs. Hence the Hamiltonian itself supplies

 -J c lambda^8 sum_straight_triples P P P, c=9L/262144.

At thin length two, each of the two rows of bad plaquettes has one triple window touching both bad endpoints. Relative to well-separated ends this removes four odd windows in total. Every odd window costs 2Jc lambda^8. The shortest thin states A=(2,1), B=(1,2) therefore gain

 -J v lambda^8, v=8c=9L/32768.

No other order-eight connected invariant can distinguish these endpoints from long thin rectangles. This is a derived defect depth, not a chosen potential. The statement excludes periodic aliases; finite quotients identify the complementary short interval with the same state.

## 3. Bound mode and native propagation

The source-connected four-defect graph is the same four-arm graph as in SIX_LAYER_NEUTRAL_POLE_PROOF.md, but its orders are now separated. Two thin arms have the endpoint defect just derived. Their nearest relative-length hopping in a COM momentum fibre is -2Jgamma_L lambda^L cos(q_parallel). The nonthin hub and high arms are higher by JDlambda^6.

For fixed L>=10 the endpoint defect dominates hopping. Each orientation has a state localized in relative length, with leading component A or B. The thin-arm binding below its continuum is Jv lambda^8[1+o(1)]. Eliminating the next thin length gives the leading momentum-dependent shift

 -J kappa lambda^(2L-8) cos²(q_parallel),
 kappa=4gamma_L²/v>0.

This is not the complete absolute energy expansion. Uncomputed common diagonal terms at orders ten and above survive. They do not carry momentum, and cannot change the leading dispersive sign. Physical spin counting forbids a lower-order translating matrix element: a k-column change needs at least Lk/2 native insertions; at k=2 and order L only an adjacent column pair is possible. A translated shortest feature or orientation change is not such a single allowed jump.

The two orientations communicate through the nonthin (2,2) hub. Its elimination gives a negative off-diagonal entry

 -J eta lambda^(2L-6) cos(qx/2)cos(qy/2), eta=4gamma_L²/D>0.

At zero momentum this selects the C4-even A+B combination below A-B, with leading splitting 2Jeta lambda^(2L-6). A virtual return through the flat vacuum first enters at order 2L-4, later. No direct native term at these earlier orders connects the endpoint orientations. Corrections to the winding coefficient or diagonal denominators are higher order for the displayed leading coefficients.

For L=10, gamma=12155/33554432, v=45/16384, D=15/512. Then kappa=.000191107424648686 and eta=.0000179163210608143. The symmetric branch's infinitesimal coefficient dispersion is

 E(q)-E(0) = J(kappa/2)lambda^12(qx²+qy²)+higher terms,

with positive curvature. The orientation splitting is only order lambda^14: the isotropic expansion requires |q| much smaller than lambda. At fixed q as lambda tends to zero, the two orientation dispersions must instead be treated as a two-component matrix. No uniform isotropic dispersion at fixed momentum is asserted. Finite microscopic grids have discrete momenta; a continuous coefficient-fibre derivative is not automatically an actual finite-grid derivative.

The height-eight boundary case fails this mechanism: v/(2gamma8)=96/143<1, below the semi-infinite endpoint bound-state threshold. It is preserved as a failed route rather than extrapolated into a success.

## 4. Original source and prepared heavy coupling

The original normalized microscopic readout C is the same next-nearest vertical ZZ sum used in COLUMN_READOUT_PROOF.md. Its matched dressed vacuum-to-four-flux vector, after ground-mixing subtraction, is

 -gamma_L beta_L lambda^L (A+B)/sqrt(L)+higher orders,
 beta_L=A_L/2-3, A_L=6(L-1)(L-2)/(2L-3).

The bound C4-even vector tends to (A+B)/sqrt2. Thus its original-source weight is

 (2gamma_L² beta_L²/L)lambda^(2L)[1+o(1)].

At L10 the coefficient is 2783620125/1125899906842624=2.47235132367e-6. The pole exhausts the leading A+B source weight, although that physical weight is very small. No source normalization has been adjusted to make it large.

The native prepared-heavy x-edge vertex is -J2^-(L-2)lambda^(L-1)E_e. Its overlap with the normalized zero-momentum bound state is 1/(sqrt2 R) at leading order. Its squared projected vertex is therefore

 J² 2^(-2L+3) lambda^(2L-2)/R² [1+o(1)].

This is a prepared channel with matching dressed state/readout. It is not an outgoing relaxed-heavy scattering amplitude, an emission rate or a universal gravitational charge.

## 5. Actual microscopic zero-momentum pole

For each fixed L>=10, choose even R comparable to a positive constant times log(1/lambda), with R eventually exceeding all fixed expansion ranges. A fixed-order exact N0 block identification has polynomial-in-R coefficient and remainder bounds, by the order-J Riesz contour and ||V||=O(R²). Keep the inherited canonical gauge through the required orders. Successive flux-count, thin/nonthin and shortest-thin reductions have gaps of orders lambda^4, lambda^6 and lambda^8. Expanding sufficiently far makes the remaining norm error o(lambda^8) along logarithmic R.

At momentum zero in the C4-even fibre the shortest-thin subspace is one-dimensional: A-B is in the other C4 representation. It has a uniform coefficient gap v from all other thin states and a larger order-lambda^6 separation from nonthin four-defect states. Other flux-count clusters are separated at order lambda^4. This supplies a simple actual finite-H pole in the specified exact fibre, not merely a graph eigenvalue. Finite folded arms cannot close the endpoint gap when lambda^(L-8) tends to zero.

Source control must precede projection-error bounds. The original source is scalar below its nonconstant diagonal order four; off-diagonal whole-column readout begins at order L. The leading ground mixing is order lambda^(L-4). Combining its diagonal-source contribution with the direct winding readout produces the beta_L vector above. Higher diagonal corrections and higher winding paths increase its order. Thus the centered P0-to-P4 source vector is the displayed order-lambda^L vector plus O(lambda^(L+1)poly(R)), before projecting onto the bound state. The latter projector tends to A+B with polynomially controlled vanishing error. This proves the stated positive original-source atom along the logarithmic-box family.

This transfer establishes the zero-momentum C4-even pole and its source weight. It does NOT establish the actual full-H infinitesimal dispersion uniformly for grids large enough to realize q<<lambda: logarithmic R is insufficient for that momentum resolution. The positive-curvature claim remains the separately derived coefficient-fibre result.

The ground-sector selection argument extends at fixed R: minimal whole-row/column matching paths first occur at order (L-4)R/2+4 with positive coefficient 2 binomial(R-2,R/2-1)gamma_L^(R/2)/(L/16)^(R/2-1). Fixed-size analytic reduction selects the positive character. As before, no uniform threshold is proved, so this does not remove the state premise from the logarithmic-box joint family. An ordered limit or existence-only diagonal sequence can use the actual global ground.

## 6. Limits and failed numerical control

All quantities are exposed model-development calculations. No observed mass, force or cosmological scalar is fitted or tested. Height, anisotropy, action choice, physical units, longitudinal propagation and universal matter coupling remain open. A fixed ten-layer feature contains twenty flipped physical spins in its leading column representative; no claim of macroscopic transverse extent follows.

A double-precision finite-star attempt produced unstable tiny curvature differences at lambda=.1 and .05 because the signal was smaller than eigenvalue subtraction error. Those values are rejected. The checked helper uses 70-digit half-line resolvents and reproduces the positive curvature, orientation splitting and source weight limits of the displayed coefficient graph only. That numerical precision repair is not evidence for the full microscopic Hamiltonian.
