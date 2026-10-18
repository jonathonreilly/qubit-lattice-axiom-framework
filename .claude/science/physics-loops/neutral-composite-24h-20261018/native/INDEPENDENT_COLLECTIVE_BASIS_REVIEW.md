# Focused collective neutral-source basis review

Disposition: PASS for the declared finite-state variational/source calculations, with the completeness boundary below. No mathematical blocker found. This is a focused independent source review, not a formal audit. Root retains authorship; no repository edits or expensive 27-site replay were performed.

## Metric, Ritz and residual formulas

For row sources V_i=(O_i-<O_i>)g and W_i=(H-E0)V_i, S=VV^T is the connected-source Gram matrix and K=VW^T is the Hermitian restricted energy form. These real formulas are valid for the present real matrices and vectors. The retained S eigenvectors scaled by 1/sqrt(eigenvalue) give T^T S T=I; diagonalizing T^T K T therefore gives the Ritz values in the numerically kept source span. Applying the row aggregation A on both sides is correct for orbit sums. The cutoff is relative 1e-10 and defines the numerical optimization space; results are not exhaustive over discarded directions or arbitrary neutral operators.

The reconstructed normalized v and hv=W combination yield the actual full-H residual ||hv-ray*v|| in the exact invariant sector, not merely a projected Galerkin residual. Since the sector is invariant, this is also a full physical-H residual under its isometric embedding. Ritz optimization is over connected source vectors on a selected numerical stationary background; it does not prove a true lowest spectral edge. The collective script's moment_variance assumes c^T S c=1 before the explicit vector normalization. This is true in exact arithmetic; its stored agreement with residual squared is within 2.8e-11. For future ill-conditioned extensions, dividing that term by the measured norm squared would remove the small finite-precision normalization discrepancy. No present material result depends on it.

For a normalized target m, pc=T^T V m (or T^T A V m) is its coordinate projection into an orthonormal kept source span. Weight=||pc||² is exactly the maximal squared overlap within that span. The normalized coefficient T pc/sqrt(weight), including A^T when needed, gives its projected vector and correct full-H energy/residual. This is a target-informed, same-model source construction; not independent validation or an empirical coupling. All stored target weights are nonzero; generalized code would need a zero-weight guard. The target vectors themselves retain their preceding numerical eigenvector limitations.

## Independent orbit and reduction controls

A separate script /private/tmp/neutral-orbit-independent-check.py builds the physical 54-edge graph and determines pair commutation by endpoint overlap and physical axes, independently of the reduced masks. All 48 signed coordinate permutations are distinct. It finds 1,287 commuting unordered distinct pairs and 144 anticommuting pairs. Their 40 orbits have sizes: 18 of size48, 14 of size24, seven of size12, one of size3. Every representative and count agrees with the saved quadratic labels. Bond squared terms are identity and disappear after centering. The three linear midpoint-radius classes exhaust the cubic bond orbits. For local composites, distance from the cube center similarly classifies the center/face/edge nonzero orbit sums; corner composites vanish.

I independently checked multiplication followed by extra-sector reduction against reduction followed by multiplication for every commuting pair, and applied the physical reduced operators to explicit signed four-element orbits at three representatives per pair. All 3,861 exact dictionary intertwining checks pass. The Y-pair coefficient -1 is correct for 18 Y factors (i^18=-1); the two independent commuting flips reduce dimension 2^22 to 2^20 without discarding Hamiltonian terms inside the chosen character sector.

Completeness is for real symmetrized quadratic bond products (anticommutators), not automatically all Hermitian degree-two combinations. For anticommuting pairs the symmetrized product vanishes, whereas i[A,B] is a distinct Hermitian possibility and is not enumerated. The scope must not claim every quadratic neutral observable is optimized. Cubic scalar here means invariant operator orbit sums under simultaneous axis/site symmetry; it is not a particle-spin identification or proof of a scalar excited-state representation.

A separate small real symmetric matrix with redundant centered sources independently verifies the whitened Ritz construction against an orthonormal SVD span, maximum eigenvalue discrepancy 8.9e-15. The targeted projection weight agrees with a direct orthogonal projector to 5.6e-16, including unit normalization and overlap equality. These checks exercise null-metric removal and do not reuse the large model's numerical output as proof.

## Scientific and operational scope

The scripts preserve the supplied finite open-grid H and selected stationary state. Large full residuals of the optimized sources remain visible; neither optimization nor overlap establishes a bulk particle, propagation law, universal source coupling, physical state selection or cosmological identification. Source coefficients are developed on the same model. The earlier quadratic variable-shadowing exception (g replaced by a bit-mask integer) was fixed before successful runs; it is an operational failure, not a failed physical route or negative scientific result. No broad no-go follows from limited overlap in this source family.

The NPZ state is a generated dependency of neutral_extra_sector_response.py. Packaging/replay must generate that exact selected-sector state before these consumers and bind the producer plus reduction/H sources; the standalone files assume it already exists. Current source snapshots include the new targeted-projection code and output. Root remains responsible for aggregate replay/provenance integration.

## SHA256 snapshot

- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_collective_basis.py`: `84b324e031d15995a08b50993e09c287c9842a31b13a90ad99f78f50c2359eb7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_quadratic_scalar_basis.py`: `7b932b164e8247a22952313b301bd150b7d6dea2536da1851f9e120bca6bb9c7`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector.py`: `39838305b41d3b58515a7d7a424c7b62290bd0886fadab95cde38c7f03913318`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_extra_sector_response.py`: `d4dd5dfa423586846b2b62a48797fb5a73a5d4362d17c4183dbe7d22666bbc0c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py`: `903ece39673616ae809fd44e66a186325252f0c75c77618ec905e7f95f5ef529`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py`: `617a143fbd5112cee5d818512b72e9d49abd09970660a07e3a44e6f51b05c3b1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_collective_basis.json`: `278858e5b9a4f3b746bdd0ee0156e9761a0b63fe11654cb527afa1b790dc6327`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_quadratic_scalar_basis.json`: `1180fd4e0209f68b0bace5b39d2981b5f6d6939c63a98c08e51fbaa6fbd4d4a2`
- `/private/tmp/neutral-orbit-independent-check.py`: `8b83dd622782297a970a5f09f78b05705acf0ae48960728119786d751d6432ed`
- `/private/tmp/neutral-orbit-independent-check.json`: `23a60f63869ccbb16afd4583f8514025fdf129f003b4ee47d0351751321b11fe`
