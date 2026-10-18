# Four-layer fully open boundary check

Disposition: PASS for the fixed-height native coefficients, with the finite-model qualifications below. Independent exact Fraction enumeration of all 24 winding permutations gives path sum8 and weighted source mark3. No repository edits or full-system diagonalization.

For four open z layers, an isolated flip costs2J at either end and4J at either interior layer. Each site belongs to exactly one of the original open distance-two pairs (0,2),(1,3). Its source change is therefore -2/sqrt(V), unlike the periodic four-layer diagnostic. These counts are correctly distinguished.

A same-layer square has three energy denominators. Relative to the bulk -J lambda^4/128 coefficient, halving every denominator at an end gives -J lambda^4/16. Two ends plus two interior layers yield -18J lambda^4/128 per transverse plaquette. The source derivative at an end is a factor3/(Jsqrt(V)); in an interior layer it is3/(2Jsqrt(V)). Summing gives -51lambda^4/(128sqrt(V)) per plaquette. Numerators are held fixed in the bookkeeping derivative. The result is the original source at zero auxiliary parameter, not an added interaction.

For a two-column winding subset S, each internal rung boundary breaks two physical ZZ bonds and costs4J. Thus Delta=4J b(S), where b counts the three open nearest-neighbor mismatches. Each open distance-two mismatch changes two column diagnostics, giving Delta C=-4d2_open(S)/sqrt(V). Exact enumeration gave

 sum_paths product_proper_steps 1/b(S)=8,
 weighted average sum_steps d2_open(S)/b(S)=3.

There is no proper nonempty wall-free subset on the connected open chain, so no intermediate return to N0 occurs. The first offdiagonal term is -gamma_open sum E, gamma_open=Jlambda^4/8. Differentiating yields -3gamma_open/(Jsqrt(V)), namely -48lambda^4/(128sqrt(V)) sum E. XX and YY signs agree at even height four.

Minimal-word exhaustion is unchanged by open ends: distinct N0 configurations differ by whole columns, and each native insertion flips two sites in one layer. At order four, equality forces exactly two neighboring columns, each site flipped once. No other offdiagonal winding geometry fits. Diagonal distinct-edge returns are same-layer transverse squares; repeated-edge returns are orientation-independent. Open transverse boundaries remove absent bonds/squares without adding cycles. The real native-gauge connection cannot affect order four because the first possible offdiagonal connection is order four and all lower N0 energy terms are scalar.

With scalar pieces removed and E=sum nearest-column Xbar Xbar,

 K_open=-18 sum P-16 E,
 O_open=-51 sum P-48 E=(17/6)K_open-(8/3)E.

The algebra is correct. Both terms occur at the same order; no plaquette-dominant perturbative argument is appropriate. The leading effective model and source have a fixed native ratio, not a free coupling.

A strict positive inelastic response of this finite leading model can be justified, but needs its stated geometry and irreducibility: on a connected transverse graph, edge pair flips connect every configuration within each global-Z-parity sector. The negative hopping yields a strictly positive Perron-Frobenius ground vector there. If the plaquette sum takes at least two values in that sector, E cannot have that vector as an eigenvector: otherwise K and E eigenvector equations force the vector to be an eigenvector of the nonconstant diagonal plaquette sum, impossible for a strictly positive vector. Therefore the non-energy-proportional E part of O has positive excited spectral weight. This is a finite coefficient-model argument, not yet a quantitative weight or microscopic transfer theorem; exact symmetry-sector restrictions must retain the corresponding irreducibility argument. Tiny transverse geometries without varying plaquette values are excluded from that inference.

At each fixed transverse box the native gapped-wall analytic reduction supplies these leading operators. Uniform growing-area, three-dimensional bulk, phase, propagation, lifetime and empirical claims do not follow from this boundary calculation. The open diagnostic must never be replaced by the periodically doubled opposite-pair sum.
