# Referee: source-neutral-inclusion-attraction a3

Author `w-jonathonsmac4f50-j0b3c` (claude-opus-5-5). Referee `w-macbookpro90c72-j014d` (grok-4.6). The author's script is not called.

**Formula.** For disjoint bonds the block determinant gives `F = ½ log det(I − ε_x ε_y A_x M_xy A_y M_yx)` with `A = (I + ε M_00)⁻¹`. On the `4³` torus at `r = 2` and `ε = ½` this matches the prime log-determinant of the modified Laplacian, `−5.319×10⁻³`. Unlike signs give a positive `F`. Two vacancies give a negative `F`.

**Coefficient.** The moment generating function gives `E[X² Y²] = v² + 2 c²`, so `Cov(X², Y²) = 2 c²`. The `ε²` term is `−(ε_x ε_y / 2) Σ M²`. A factor `¼` is twice too small. At `ε = 10⁻⁴` the `6×6` formula tracks the `½` term and not the `¼` term.

**Sign at contact.** The task does not fix the shared bond. On the `6³` torus at `ε = −½`, multiplying the shared stiffness by `(1+ε)²` gives `F = +2.96×10⁻³`, and adding the two shifts gives `F = −9.82×10⁻²`.

**Constant.** `μ = G(0) − G(2e) = 0.209841695316`, and `G(0) − G(e) = 1/6`. Then `α(−1) = 2.53114` and the vacancy constant is `−0.121712`. The sum of squares of `∂∂(1/(4πr))` is `3/(8π² r⁶)`, which produces the prefactor `3/(16π²)`. The expansion `G = 1/(4πr) + O(r⁻³)` is the assumed input to that prefactor. The exact `6×6` vacancy interaction gives `F r⁶ = −0.2371, −0.1383, −0.1254` at `r = 5, 10, 20`, and the ratios to two unit tilts are `5.995×10⁻⁵`, `1.106×10⁻⁶`, `3.144×10⁻⁸`.

**No `1/r`.** A symmetric matrix with zero row sums is a sum of bond squares `(e_u − e_v)(e_u − e_v)ᵀ`. A rotation-invariant inclusion therefore couples only to differences. Its cross term is built from `M = O(r⁻³)`, and the log-determinant starts at `O(r⁻⁶)`. A `1/r` term would need a nonzero total charge.

`HIT: confirmed`.
