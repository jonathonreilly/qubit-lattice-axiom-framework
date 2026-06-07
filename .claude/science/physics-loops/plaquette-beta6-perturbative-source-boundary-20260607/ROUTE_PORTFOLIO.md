# Route Portfolio

1. Finite weak-coupling truncations through `N <= 16`.
   Result: pruned for this packet; the best value remains near `0.919331`.

2. Lepage-Mackenzie tadpole fixed points through `N <= 8`.
   Result: pruned for this packet; the best value remains near `0.910550`.

3. Pade `[m/n]` resummations with `m+n <= 12`.
   Result: pruned for this packet; accepted values remain in the perturbative
   saturation band.

4. Tadpole-improved Pade fixed points with `m+n <= 8`.
   Result: pruned for this packet; best residual remains about `53.45%`.

5. Non-perturbative, strong-coupling, transfer-matrix, Wigner-Racah,
   Borel-conformal, or MC routes.
   Result: explicitly out of scope and not pruned by this artifact.
