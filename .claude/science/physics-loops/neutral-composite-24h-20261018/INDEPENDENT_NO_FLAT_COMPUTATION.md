# Independent exact no-flat-transition arithmetic check

Disposition: PASS for the supplied exact-decimal candidate, q=Q, two-momentum finite-field certificate. Both primes independently verified. No repository edits or formal audit.

## Different computational route

Independent implementation: /private/tmp/neutral-no-flat-independent.py; output: /private/tmp/neutral-no-flat-independent.json.

I parsed decimal literals through Decimal and Fraction, reduced numerators/denominators modulo each prime, and checked that every denominator used is invertible. For each rational unit-circle point I constructed h(k) directly from its seven hopping blocks. I obtained h(k+Q) by negating all three coordinate phases, independently of the submitted parity-of-shift implementation. The six supplied Pythagorean triples satisfy a^2+b^2=c^2 exactly, so they are genuine real-torus momenta before reduction. Modular square roots of -1 are 469 for1009 and45 for1013.

I then built all144x144 Liouvillian entries explicitly in row-major matrix-element coordinates using

    L_(ba),(jc) = delta_ac hq_bj - delta_bj h_ca.

No Kronecker construction, trace convolution or Newton coefficient identities were used for the independent characteristic polynomial. Instead I reduced each full matrix to upper Hessenberg form by modular similarity transformations and evaluated its characteristic polynomial by the principal-submatrix determinant recurrence. Before the actual calculation, this algorithm was checked against SymPy characteristic polynomials for seven random integer matrices of sizes2 through8.

For each prime, all145 polynomial coefficients at BOTH momenta agree exactly with the submitted ascending coefficient lists. SymPy polynomial gcd, independent of the author's Euclidean implementation, has degree0 in both cases:

- p=1009: both characteristic polynomials match; gcd=1.
- p=1013: both characteristic polynomials match; gcd=1.

I also checked exact rational Hermitian hopping-pair identities B_-s=B_s^dagger across every matrix entry: zero violations, zero residual. Thus the exact-decimal convention here does not secretly make the one-particle Hamiltonian non-Hermitian.

## Arithmetic and implication boundaries

The submitted Newton divisions are valid since both primes exceed144. Modular matrix products are bounded far below int64 overflow (largest direct144-term dot products below1.5e8). The q-phase factor for shifts of odd parity is correctly -1; negative shifts are treated by modular inverses and also acquire -1 under q=Q. The trace binomial sign and characteristic-polynomial coefficient ordering agree with the independent full-matrix result.

One valid reduction already certifies nonzero characteristic-zero resultant: the monic characteristic polynomials lie in the rational/Gaussian-rational coefficient ring localized away from the chosen prime, and their reductions are coprime. Hence they have no common complex frequency. In particular, no transition frequency can be an eigenvalue of L_Q(k) at every k for this exact candidate: it would occur at both certified momenta.

This is not an arbitrary-q theorem, interacting-model theorem, physical scalar exclusion, or a certificate for the unrounded upstream construction. Treating the stored decimal numbers as exact is part of the theorem's input. A perturbation/rounding robustness statement would require a separate quantitative bound. The certificate does not by itself provide the analytic-measure argument needed to translate absence of a globally flat frequency into absence of a spectral atom; any such downstream argument must state its translation-invariant infinite-volume measure, regularity and operator-domain hypotheses. Finite grids continue to have discrete spectral lines.

## SHA-256 identities

```text
b4c2bc8c25dafa7c529a96f3109331924eb428d2b363ec765f66fd1efc1e0588  /private/tmp/scalar-environment-20261017/data/collective_corner_response/candidate.json
cda114f3a1994aa13136d8254536202ac086c15db87859e342e1f34317a7e62c  /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/exact_no_flat_transition.py
fc3551317dd9cf09e0530acabd06a0f033e26ec247c6f218ce1c3227d41dc6f6  /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/probes/exact_no_flat_transition.json
bf442fee0638e5a37708083bffbcc5eff463d8b0a14a1511faac6c1da9149740  /private/tmp/neutral-no-flat-independent.py
64284276e297ea1e63dc06d61f63a106b6833e3917ad552a90681bd5a4555dae  /private/tmp/neutral-no-flat-independent.json
```
