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
flux convention through the `xy` plaquettes, let `P_+` denote the union of
positive-definite elliptic (band-minimum) smooth quadratic patches. The
midpoint-ladder derivation fixes their contribution to the small-field
grand-potential second derivative as

```text
Omega''_{P_+}(0) = -1/12 * integral_{P_+} f'(E(k))
                   * [E_xx(k) E_yy(k) - E_xy(k)^2] d^3k/(2*pi)^3 .
```

For the cubic nearest-neighbor band

```text
E(k) = -2 (cos kx + cos ky + cos kz)
E_xx E_yy - E_xy^2 = 4 cos(kx) cos(ky),
```

this is the local normalization used inside the d=3 orbital-response
decomposition note. The derivation below supplies it on `P_+` from the Peierls
magnetic-translation convention, the local single-band quadratic patch, and the
midpoint Euler-Maclaurin coefficient. It does not introduce a new axiom,
primitive, measure, weight, or fitted scalar. Extending the formula to the
remaining Brillouin-zone patches is not derived here.

The literature name for the same object is the spinless single-band
Landau-Peierls intraband term. That name is cited in parallel as context only:
the source authority in this repo is the derivation and runner named above.

**Derived scope (positive-definite elliptic patches).** The derivation below
establishes this normalization for positive-definite elliptic (band-minimum)
quadratic patches, where the local canonical matrix has a real magnetic
frequency and the energy has an upward discrete midpoint Landau ladder.
Positive determinant alone also includes negative-definite band maxima: their
canonical spectrum is elliptic, but their ladder is downward and needs a
separate hole/filled-band boundary argument not supplied here. Extending the
same `-det(H_xy)/12` coefficient to those maxima, and through the
determinant-zero lines to saddle (negative-determinant) patches, is an explicit
open conjecture and is not part of the derived bounded claim; the full
Brillouin-zone reference value is reported as a diagnostic that holds
conditionally on that full-patch conjecture.

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

   Thus for positive-definite elliptic patches the local magnetic spacing is
   `B sqrt(det(H))`, a real frequency, and the energy has the upward ladder used
   in the next step. Negative-definite elliptic patches have the same imaginary
   canonical eigenvalue pair but a downward energy ladder, so the half-line
   endpoint orientation below does not cover them. For saddle
   (negative-determinant) patches the canonical matrix has real eigenvalues,
   `sqrt(det(H))` is imaginary, and there is no discrete magnetic ladder. The
   derivation is therefore restricted to positive-definite elliptic patches;
   the negative-definite and saddle patches are held out as an explicit open
   full-patch conjecture.

3. **Midpoint Euler-Maclaurin coefficient.** On a positive-definite elliptic
   patch, the local magnetic levels sample the transverse action by upward
   midpoint levels `(n + 1/2) h`, with
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

   This local coefficient is derived for positive-definite elliptic patches,
   where the upward midpoint magnetic ladder exists. Whether the same
   `-det(H_xy)/12` coefficient continues unchanged onto negative-definite
   elliptic maxima and across the determinant-zero lines into saddle patches is
   an explicit open conjecture and is not part of the derived bounded claim.
   The cubic-band runner samples all three patch classes only to exhibit the
   regions held out of the derived scope; the full-zone integral is reported as
   a diagnostic, conditional on that full-patch conjecture.

5. **Cubic-band substitution.** For the cubic nearest-neighbor band,
   `E_xx = 2 cos(kx)`, `E_yy = 2 cos(ky)`, and `E_xy = 0`, so the determinant
   is `4 cos(kx) cos(ky)`. No empirical scalar is fitted.

## Source Boundary

Within the positive-definite elliptic scope, this note derives the finite-torus
`B/(2*pi)` magnetic-cell density and the `-1/12` spinless unit-flux factor in
the same Peierls-flux convention as the finite-torus comparison runner.
It does not remove the parent full-Brillouin-zone input: that use remains
conditional on the open full-patch conjecture. The note is still bounded:

- it is a single-band, smooth-patch, spinless Peierls-flux statement;
- it does not derive an interacting or continuum-QFT response;
- it does not assert a thermodynamic-limit theorem for the finite `L=32`
  comparison note;
- the derived normalization is established only for positive-definite elliptic
  (band-minimum) quadratic patches; the negative-definite elliptic and saddle
  (negative-determinant) continuation is an explicit open conjecture, not part
  of the derived bounded claim, and the full Brillouin-zone reference value is
  a diagnostic conditional on it;
- it leaves all status decisions to the audit lane.

## Runner Gates

The runner verifies the finite magnetic-cell degeneracy density, the exact
Bernoulli coefficients, the local symplectic determinant invariant, the
positive-definite/negative-definite/saddle canonical dichotomy that restricts
the written midpoint derivation to positive-definite elliptic patches, the
cubic-band Hessian determinant, the full-patch boundary held as an explicit
open conjecture, and the parent d=3 reference Landau-Peierls value reported as a
diagnostic conditional on that conjecture. The passing run reports:

```text
TOTAL: PASS=14 FAIL=0
```
