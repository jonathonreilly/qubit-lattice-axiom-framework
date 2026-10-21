# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ZONE_LOCAL_SECOND_CHECK.md`, SHA256 `680189a4fd5fe30e6feebe4a900d20f26f15b84532e66c21cf298a899524882b`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Focused local second-order interval check

The result establishes the stated local second-order coefficients away from folded/wrapping endpoints, not a uniform full-H approximation.

The initial script tested source edge length6 while omitting target length8. Its reconstruction assertion correctly failed; this was an incomplete test enumeration, not evidence against the coefficient. Root preserved the failed version and changed to L18,20 with targets1..8, strictly below the folded terminal. I inspected the changed source and the completed JSON: all18 rows and all rational kernels agree with the stated formulas.

Independently, I formed normalized signed interval vectors in the complete native energy-8 band and directly applied the previously checked sparse K2 at L12,14, testing E lengths1..4 and D lengths2,4. The entire output vector, not just its selected overlaps, agrees with the predicted kernels to <=2.3e-16. This independent finite computation is saved in neutral-zone-local-independent.py/json. It is a floating complete-band control; the root L18,20 calculation supplies the exact Fraction arithmetic.

## Kernel and normalization checks

For normalized E1, the diagonal is1/4 and translations by ±1 have coefficient-1/8. For E length>=2 the diagonal is-1/2. E_l to E_(l+2) has coefficient-1/8 at starts0 and-2; the reverse transitions have starts0 and+2. E2 to D2 and its reverse have coefficient-sqrt(2). Even D intervals have diagonal-2, and D2 additionally has the E2 coupling. The exact script uses norm²32 for localized edge vectors and norm²16 for localized diagonal vectors: its unnormalized coefficients -2 and -1 in the two directions both become -sqrt(2). The different raw coefficients are therefore required by normalization, not a non-Hermitian matrix.

## All-length local support

At second order, at most two rungs are acted on. For two nonadjacent rungs the operations commute, their local energy changes are additive, and their signed matrix-element product is order-independent. If both endpoint configurations have energy8, these changes satisfy a+b=0. For a nonzero a, the two virtual denominators sum to -1/a-1/b=0. If a=b=0, both intermediates lie in P and both terms are excluded by Q. Thus a zero denominator must be excluded, not regularized or included as a divergent term. This proves cancellation of nonadjacent off-diagonal processes even at degeneracy.

A same-rung return depends on its two neighbors. An adjacent active pair depends on only the four-rung motif consisting of that pair and its outer neighbors. Vacuum subtraction removes remote diagonal loops. Hence intervals and remote arcs of length at least3 have the same separated-wall local motifs; the short length1/2 cases must be retained explicitly. The tested length range covers the distinct motifs, so the coefficients extend to longer intervals/chains with those same neighborhoods. Periodic folding and overlapping short arcs require their own coordinate normalization and combination of duplicate translations; the script deliberately avoids those endpoints after the fix.

The exact reconstruction in the finite tests is complete within the full energy8 output for the tested vectors. For the all-length interpretation, I rely on the supplied prior scalar-basis classification to exclude other invariant operator channels, in addition to the local cancellation just proved; I have not re-proved that representation classification here. Local coefficient extension by itself must not be described as a uniform Schrieffer-Wolff remainder bound, convergence theorem at fixed nonzero lambda, or native bulk-pole statement. No new Hamiltonian interaction or empirical source identification is involved.

## SHA-256 identities

- `/private/tmp/neutral_zone_local_second.py`: `3e03b3b6e60d24be426c37e265b1b04cb137568fdf2cbb7dd325caca69104316`

- `/private/tmp/neutral_zone_local_second.json`: `669220cdf9e21c8d6d896215e53425f72599a35a5e423a5acfd44c1b4ec1e990`

- `/private/tmp/neutral-zone-local-independent.py`: `b3bbddd581deff8622c1b6c936aaea6db6410b39eaba1fa7e086d9ba68150f37`

- `/private/tmp/neutral-zone-local-independent.json`: `3cb05eb589b1ff0f032eb6bcfa495f329f07db18c17c5a187e2bc40dc81db7e3`

- `/private/tmp/neutral_kink_core.py`: `62cc36f85bb1d6932ccc81db8a9ebe3f0171a7443adc74d2d6564c4da45e4dd8`
