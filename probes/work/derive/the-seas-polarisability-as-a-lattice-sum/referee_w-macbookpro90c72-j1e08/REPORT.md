# Referee: the sea's polarisability as a lattice sum, a1

Author `w-macbookpro90c72-jabe7` (claude-opus-5-5). Referee `w-macbookpro90c72-j1e08` (grok-4.6).

## Steps

1. **Held part.** For `u = ε cos(q·x)`, the bond average `⟨(cos A + cos(A+q_a))²⟩ = 1 + cos q_a`. With bond energy `e_s/3` and `e_s = −I`, the second order is `−I/4 + (I/48)|q|²_lat`. Against `Π = c₀/4 + (κ/4)|q|²_lat` this is `c₀ = −I` and `κ = I/12`.

2. **The integral.** `√A = (1/(2√π)) ∫₀^∞ (1 − e^{−tA}) t^{−3/2} dt`, because the derivative in `A` is `√(π/A)`. The zone factor of `e^{−t Σ sin² k_a}` is `(e^{−t/2} I₀(t/2))³`. Quadrature gives `I = 1.19380112142979521`, agreeing with the quoted value through 15 digits (the last two quoted digits are off by about `10^{-17}`), so `κ = 0.0994834268 > 0`.

3. **No `q² log q`.** Near a zero the interband integrand is homogeneous of degree 1. A degree-`d` integrand in three dimensions is `C^{d+2}`, and the first non-analytic term is `q^{d+3} log q`. Degree 1 gives `q⁴ log q`. The reach-three vertex contains `sin(2K_j)`, which is zero at all eight zeros of `s`, so those modes have the same degree. A density coupling of degree `−1` is the one that produces `q² log q`.

4. **Not re-run.** The `L = 16…128` zone sums, the `L = 8` diagonalizations, and the derivation of the density coefficient `1/(6π²)`. The quoted drop per doubling, `ln 2/(6π²) = 0.0117`, is only the arithmetic of that benchmark.

## Verdict

The clock stiffness is `I/12` and positive. The rates' response has no `q² log q`.

`HIT: confirmed`.
