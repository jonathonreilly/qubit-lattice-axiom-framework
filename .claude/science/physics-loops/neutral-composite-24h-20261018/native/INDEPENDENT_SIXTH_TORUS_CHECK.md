# Six-layer finite torus quotient check

Disposition: PASS for even R>=8 in the specified all-positive plane-X sector and zero transverse momentum. No actual-global-ground selection theorem is inferred.

The finite torus kernel of the plaquette syndrome map consists of row/column flips, with one redundant generator. Projecting to their positive characters produces normalized uniform orbit states, one per allowed syndrome; a column-pair X operator maps these states with coefficient +1, without an extra phase or orbit normalization. On even R, these background flips preserve total column parity, and a four-defect rectangle has positive parity exactly when its area is even. On odd R this reasoning changes. The supplied build(R) function lacks a domain assertion: its current tests are all valid even R, but callers must restrict it to even R>=8. In particular its half-period orbit-size formula is not valid for odd R.

After the plane quotient, translation-orbit size for shape (a,b), 1<=a,b<=R/2, is (R or R/2)*(R or R/2), with the half factor precisely for a or b equal to R/2. For k moves from one source representative into a target orbit, summing all source representatives and normalizing gives k sqrt(n_source/n_target). Thus the implemented -k/2 sqrt(sizes[i]/sizes[j]) is correct in units t=2 gamma; the inverse ratio would be wrong.

I independently enumerated every syndrome in the source-connected translation orbits, and every physical edge syndrome, without using the script's candidate-edge generation. At R8, R10, R12 this covers respectively 448, 1000, 1872 distinct physical syndromes. The resulting fully summed normalized matrix agrees with build(R) within 1.34e-14. I separately counted adjacent bad-plaquette pairs to obtain the diagonal -4(b/t)*number_of_pairs, with b/t=1/7, agreeing with the thin-arm onsite -8/7.

For a unit normalized zero-defect plane orbit, sum_edges E_edge / R creates one normalized amplitude in each of shapes (2,1) and (1,2): each orientation has R^2 distinct syndromes. Thus q=A+B has norm squared 2, exactly as implemented. An unnormalized edge sum has amplitudes R instead. Conversion to the original microscopic C still needs its derived coefficient and physical volume normalization; the script's reported weight is the coefficient-source weight |<mode,A+B>|^2.

## Finite-arm isolation

Deleting the center (2,2) leaves four disconnected folded paths. These are restrictions of nearest-neighbor cycle/line adjacency, in their reflection-even sectors; the terminal sqrt(2) links and, where appropriate, terminal self-loop implement that restriction. Hence each zero-potential arm has top <=2, and each thin arm has top <=2-v, v=8/7. This remains true despite terminal links larger than one: a naive row-sum proof would not suffice. Other disconnected four-flux shapes are stationary under this coefficient hopping and have nonpositive relative diagonal energy.

For even R>=8, each zero-potential arm has ordinary unit bonds followed by a terminal sqrt(2) bond. Its endpoint resolvent at E=2 is exactly one: starting at the terminal site g=1/2, the preceding continued-fraction step gives 1/(2-2*(1/2))=1, and all remaining steps preserve 1. Its spectrum is strictly below 2 at finite R. The two thin-arm endpoint Green functions at 2 are positive because their spectra lie below 2-v.

Consequently the center Schur function F(E)=E-sum_arm coupling^2*g_arm(E) satisfies F(2)<0, while F(infinity)>0 and F'>0 above all arm spectra. There is exactly one eigenvalue above 2, with nonzero center amplitude. Interlacing also bounds every other eigenvalue by 2. The two thin-arm first amplitudes are equal and nonzero, so the source A+B overlaps this upper state. This proves finite-sector isolation, not just numerical separation.

Independent values (upper, next, deleted-center top), in units t:
- R8: (2.226425598031055, 1.4142135623730963, 1.4142135623730951).
- R10: (2.152090534162086, 1.7320508075688785, 1.7320508075688772).
- R12: (2.1400331027211315, 1.8477590650225746, 1.8477590650225737).

As the arms lengthen, their endpoint Green functions converge outside the bands, giving the previously checked infinite-star upper root 2.114475316300653 and its source residue. These facts do not establish that the positive plane sector contains the actual global microscopic ground, nor fix finite-lambda corrections or growing-size transfer. An unproved row-tunneling sign must not be substituted for that missing selection theorem.

Independent artifacts: /tmp/neutral_torus_reviewer.py and /tmp/neutral_torus_reviewer.json. Root script SHA256: 3d92e61719f2d6dbc3d777bec82af9f117bbc356895d4c2c00bad9ceb5bc22ba. No shared repository edits or formal audit.
