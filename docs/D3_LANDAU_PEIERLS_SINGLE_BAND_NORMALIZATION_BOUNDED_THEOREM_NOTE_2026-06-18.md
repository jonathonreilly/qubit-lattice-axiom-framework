# D = 3 Single-Band Landau-Peierls Normalization From Peierls Magnetic Translations Bounded Theorem Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.py`
**Runner cache:** `logs/runner-cache/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.txt`
**Status:** source proposal; the audit lane grades.
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. It is not an audit verdict.

## Claim

For a spinless single-band lattice Hamiltonian with the repo's Peierls plaquette
flux convention through the `xy` plaquettes, the smooth-patch small-field
grand-potential second derivative uses the native single-band normalization

```text
Omega''(0) = -1/12 * integral f'(E(k))
             * [E_xx(k) E_yy(k) - E_xy(k)^2] d^3k/(2*pi)^3 .
```

For the cubic nearest-neighbor band

```text
E(k) = -2 (cos kx + cos ky + cos kz)
E_xx E_yy - E_xy^2 = 4 cos(kx) cos(ky),
```

this is exactly the normalization used by the d=3 orbital-response
decomposition note. The derivation below supplies that normalization from the
Peierls magnetic-translation convention, the local single-band quadratic patch,
and the midpoint Euler-Maclaurin coefficient. It does not introduce a new axiom,
primitive, measure, weight, or fitted scalar.

The literature name for the same object is the spinless single-band
Landau-Peierls intraband term. That name is cited in parallel as context only:
the source authority in this repo is the derivation and runner named above.

## Derivation

1. **Peierls magnetic translations.** The plaquette convention has magnetic
   translations satisfying `T_x T_y = exp(i B) T_y T_x`. On a finite torus with
   flux `B = 2*pi/q` through each `xy` plaquette and dimensions
   `L_x = q M`, `L_y = N`, the clock/shift magnetic-cell representation obeys
   `U V = exp(2*pi*i/q) V U` and spans the full `q x q` cell algebra. An
   isolated magnetic subband therefore has one state per magnetic cell, i.e.
   `M N` states over `q M N` transverse sites. The state density is exactly
   `1/q = B/(2*pi)`. The runner verifies this finite-torus degeneracy count
   for several `q` without importing a continuum Landau-level formula.

   Expanding the link phases at small `B` gives the local covariant-momentum
   bracket `[pi_x, pi_y] = i B` in the transverse patch. This step uses the
   same Peierls flux convention as the finite-torus runner.

2. **Single-band quadratic patch.** At fixed `k_z`, expand a smooth isolated
   band in transverse momenta:

   ```text
   E = E0 + 1/2 (a qx^2 + 2 c qx qy + b qy^2) + higher orders.
   ```

   The Hamiltonian matrix is `H = [[a, c], [c, b]]`. The canonical matrix
   `JH` has characteristic polynomial

   ```text
   lambda^2 + det(H) = 0,
   det(H) = a b - c^2.
   ```

   Thus the local magnetic spacing is `B sqrt(det(H))` for elliptic patches,
   and the analytic coefficient carried into the Brillouin-zone formula is the
   determinant `E_xx E_yy - E_xy^2`. Saddle patches enter because the final
   local response coefficient is the polynomial `-det(H)/12`, not a
   square-root branch. The runner checks the exact rational coefficient on
   both positive- and negative-determinant quadratic patches; the note does
   not claim a separate discrete Landau-level spectrum for an isolated saddle.

3. **Midpoint Euler-Maclaurin coefficient.** The local magnetic levels sample
   the transverse action by midpoint levels `(n + 1/2) h`, with
   `h = B sqrt(det(H))`. For any decaying smooth test function `G`,

   ```text
   h * sum_{n >= 0} G((n + 1/2) h)
     = integral_0^infty G(x) dx + h^2 G'(0)/24 + O(h^4).
   ```

   This is the Bernoulli-polynomial value
   `-B_2(1/2)/2! = 1/24`; the midpoint rule has no linear endpoint term because
   `B_1(1/2) = 0`.

4. **Grand-potential second derivative.** Let
   `F(E) = -T log(1 + exp(-(E - mu)/T))`; then `F'(E) = f(E)`, the Fermi
   occupation. Combining the degeneracy `B/(2*pi)`, the local spacing, and the
   midpoint coefficient gives the `B^2` grand-potential coefficient

   ```text
   B^2 * sqrt(det(H)) * f(E0) / (48*pi).
   ```

   The repo's response is the second difference divided by `B^2`, so the
   second derivative is twice this coefficient. Rewriting

   ```text
   integral f'(E0 + x) dx = -f(E0)
   ```

   converts the local expression to

   ```text
   Omega''(0) = -1/12 * integral f'(E(k)) det(H_xy(k)) d^3k/(2*pi)^3.
   ```

   Since the local coefficient is polynomial in `det(H_xy)`, the full
   Brillouin-zone patching does not require a separate sign branch at saddle
   points. The cubic-band runner samples both signs of `det(H_xy)` and applies
   the same exact coefficient.

5. **Cubic-band substitution.** For the cubic nearest-neighbor band,
   `E_xx = 2 cos(kx)`, `E_yy = 2 cos(ky)`, and `E_xy = 0`, so the determinant
   is `4 cos(kx) cos(ky)`. No empirical scalar is fitted.

## Source Boundary

This note removes the d=3 orbital-response decomposition's naked textbook
normalization input by deriving the finite-torus `B/(2*pi)` magnetic-cell
density and the `-1/12` spinless unit-flux factor in the same Peierls-flux
convention as the finite-torus comparison runner. The note is still bounded:

- it is a single-band, smooth-patch, spinless Peierls-flux statement;
- it does not derive an interacting or continuum-QFT response;
- it does not assert a thermodynamic-limit theorem for the finite `L=32`
  comparison note;
- it leaves all status decisions to the audit lane.

## Runner Gates

The runner verifies the finite magnetic-cell degeneracy density, the exact
Bernoulli coefficients, the local symplectic determinant invariant, the
polynomial saddle-continuation coefficient, the cubic-band Hessian determinant,
and the parent d=3 reference Landau-Peierls value using this fixed
normalization. The passing run reports:

```text
TOTAL: PASS=13 FAIL=0
```
