---
claim_id: composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, isotropic J = 1, four-site Bloch matrix H(f) = i M(f). Exact for every kappa > 0: det H, its gradient and the constant and linear characteristic-polynomial coefficients vanish at two line points (x, 1 - x, 0), (1 - x, x, 0), cos 2 pi x = [1 - sqrt(1 + 4 kappa^2 + 16 kappa^4)]/(4 kappa^2). For 3/20 < kappa^2 <= 1/4 the same holds at four points (x, 1 - x, +-f3), (1 - x, x, +-f3) with cos 2 pi x = 1 - 1/(4 kappa^2), cos 2 pi f3 = 3/(4 kappa^2) - 4. For kappa^2 >= 1/4 it holds at four points (f3 + g, f3 - g, f3), both signs of f3 and g, with cos 2 pi f3 = 3/2 - s/2, cos 2 pi g = -5/2 + s/2, s = sqrt(13 + 3/kappa^2). Computer-assisted count at kappa = 1/10, 3/10, 7/20 (two points) and 9/20, 12/25, 3/5, 4/5, 1 (six points): det H vanishes at exactly these points, zero is a double level there with the outer levels nonzero, and everywhere else H has two negative and two positive levels. So the middle bands touch exactly there and the middle gap is open elsewhere. Certificate: exact rational algebra plus interval arithmetic (outward-rounded IEEE float operations, mpmath interval functions) with the landed Lipschitz bound. No node charge, dispersion order, count between the sampled couplings, anisotropic coupling, spin-Hamiltonian equivalence, ground-sector selection, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_middle_band_touchings_two_below_kappa_star_and_six_above_interval_certificate_2026_09_26.py
---

# The flux-free comparator's middle bands touch at two exact points below κ* and at six above

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact algebra for every κ and a computer-assisted count at eight couplings, for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md`:
the colored network of
`THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`
with the explicitly supplied real antisymmetric hopping matrix. Take `u = +1`,
one quadratic copy, the landed four-site reduction `H(f) = i M(f)` over the
fractional zone, and `J = 1`.

That note found two numerical groups of touchings below `κ* = √(3/20)` and six
above. It left open:
- a certified exclusion of other zeros;
- an exact node count;
- where the groups sit.

It also retained three facts used here:
- the line identity on `f = (x, 1 − x, 0)`;
- the rational-point polynomial at `(1/4, 3/4, 1/2)`;
- the Lipschitz bound `‖H(f) − H(f′)‖ ≤ lip ‖f − f′‖∞`.

## Result

**Exact nodes, every κ > 0.** At each point below, `D = det H`, its three
momentum derivatives, and the constant and linear coefficients of
`det(H − λ)` vanish exactly.

| family | range | points | coordinates |
|---|---|---|---|
| **Line** | every κ > 0 | `(x, 1 − x, 0)`, `(1 − x, x, 0)` | `cos 2πx = [1 − √(1 + 4κ² + 16κ⁴)]/(4κ²)` |
| **Plane `f₁ + f₂ = 1`** | `3/20 < κ² ≤ 1/4` | `(x, 1 − x, ±f₃)`, `(1 − x, x, ±f₃)` | `cos 2πx = 1 − 1/(4κ²)`, `cos 2πf₃ = 3/(4κ²) − 4` |
| **Plane `f₁ + f₂ = 2f₃`** | `κ² ≥ 1/4` | `(f₃ + g, f₃ − g, f₃)`, both signs of `f₃` and `g` | `cos 2πf₃ = 3/2 − s/2`, `cos 2πg = −5/2 + s/2`, `s = √(13 + 3/κ²)` |

The closed forms carry the whole sequence:
- **Birth at κ*** (`4κ² = 3/5`). The first plane family sits at
  `cos 2πx = −2/3`, `f₃ = 0`. That is the line node, whose cosine is the
  landed `c* = −2/3`. So the four extra nodes are born from the two line
  nodes.
- **Handover at κ = 1/2.** Both plane families give
  `(1/4, 3/4, 1/2)` and `(3/4, 1/4, 1/2)`: the first with
  `cos 2πx = 0`, `f₃ = 1/2`; the second with `f₃ = 1/2`, `g = ±1/4`. These
  are the points where the landed rational-point polynomial vanishes at
  `κ = 1/2`. The two planes meet there, and the nodes pass from one to the
  other.
- **At κ = 1.** The second family gives the rational points `f₃ = ±1/3`,
  `g = ±1/3`, for example `(0, 1/3, 2/3)`.

**Theorem (computer-assisted).** At `κ = 1/10`, `3/10`, `7/20` (two nodes) and
at `κ = 9/20`, `12/25`, `3/5`, `4/5`, `1` (six nodes):
- `D` vanishes exactly at the listed nodes and nowhere else in the zone;
- at each node zero is a double level and the outer two levels are nonzero;
- at every other point `H` has exactly two negative and two positive levels.

So the middle bands touch exactly at these points, at zero energy, and the
middle gap is open everywhere else. At `κ = 9/20` the first plane family has
`cos 2πx = −19/81`, `cos 2πf₃ = −8/27`.

## Proof structure

1. **Exact algebra.** Determinants are computed in polynomial rings with
   rational amplitudes `2J = 2` and `2κ`, `κ` symbolic. `D`,
   `∂D/∂f_j = 2πi z_j ∂D/∂z_j` and the two characteristic coefficients
   reduce to zero:
   - on the line, modulo `P_κ(z) = κ²z⁴ − z³ − (1 + 2κ²)z² − z + κ²`;
   - on `f₁ + f₂ = 1`, modulo the two cosine quadratics;
   - on `f₁ + f₂ = 2f₃`, with `z₁ = wy` and `z₂ = w/y`, modulo the two cosine
     quadratics in `w` and `y` together with `s² = 13 + 3/κ²`.

   All three derivatives are included, so each point is a critical point of
   `D` in the full zone. The same computation reproduces the landed line
   identity and the landed rational-point polynomial.
2. **Rigorous clearing.** Cubes `[c − h, c + h]³` with exact dyadic centres
   start from `32³` and are split eight ways, thirteen times. For each cube:
   - `H(c)` is enclosed entrywise with `mpmath` interval phases and
     outward-rounded float arithmetic;
   - interval `LDL*` inertia of `H(c) ∓ rI` is computed, with `r` rounded
     up from `lip·h`;
   - equal certified negative counts at `±r` show that no level lies within
     `r` of zero, so by Weyl's inequality no level vanishes in the cube and
     the count holds throughout.

   Every cleared cube has count exactly 2. The uncleared cubes form exactly
   as many groups as there are nodes.
3. **Boxes.**
   - Each group's bounding box contains exactly one exact node. Node
     enclosures come from certified sign changes of the defining cosine
     equations, to `1e-12`.
   - Interval evaluation of the quadratic characteristic coefficient at each
     node excludes zero, so the outer levels are nonzero and zero is exactly
     a double level.
   - The Hessian of `D` is positive definite on every box: interval
     Cholesky of centred interval forms, with bisection where needed. The
     smallest certified pivots are:

     | κ | smallest pivot |
     |---|---|
     | 1/10 | 72 |
     | 3/10 | 123 |
     | 7/20 | 13 |
     | 9/20 | 59 |
     | 12/25 | 38 |
     | 3/5 | 464 |
     | 4/5 | 437 |
     | 1 | 148 |
   - With `D = 0` and `∇D = 0` at the node, Taylor's theorem in the convex
     box gives `D > 0` there except at the node.
4. **Conclusion.**
   - `D ≠ 0` off the nodes.
   - The negative count is locally constant where `D ≠ 0`, equals 2 on the
     cleared cubes, and equals 2 on each punctured box, which is connected
     and meets the cleared cubes.
   - So `λ₂ < 0 < λ₃` off the nodes. At the nodes, `λ₂ = λ₃ = 0` with
     `λ₁ < 0 < λ₄`.

A sanity check also passes: at dyadic points the interval matrices contain
40-digit evaluations of the entries, and the interval inertia agrees with
floating eigenvalue counts.

## What this settles and what it does not

- At the eight couplings, the landed note's numerical groups contain exactly
  one touching each, at exact points, and no other zero exists in the zone.
- The three exact families hold for every κ, and at the eight couplings
  they are the complete set of touchings. Read through the families, the
  landed "two become six" is a birth from the line nodes at `κ*`, followed
  by a handover between two planes at `κ = 1/2`.
- Not certified here:
  - the exact count at couplings between the samples, including near `κ*`
    and `1/2`. At `κ = 2/5` the positive-definiteness step did not succeed
    on the line-node box within the bisection depth used, so that coupling
    is not included;
  - the node charges (the landed discrete fluxes remain diagnostics);
  - the dispersion order;
  - anisotropic couplings;
  - equality with the spin model.

## Arithmetic boundary

The certificate assumes:
- IEEE 754 double precision with round-to-nearest for `+ − × ÷`, so one
  outward `nextafter` step encloses each exact result;
- the correctness of `mpmath`'s interval elementary functions;
- `sympy`'s exact rational polynomial arithmetic.

Floating eigenvalues enter the sanity check and nothing in the certificate.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator, `J = 1`; exact families for every κ, counts at eight rational couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed parent's reduction, identities and Lipschitz bound are used as stated there.
- **N5:** exact positions and counts; nothing is claimed between the sampled couplings.
- **N6:** charges, a coupling interval and anisotropy remain open.
- **N7:** other sectors, couplings and certificates remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_middle_band_touchings_two_below_kappa_star_and_six_above_interval_certificate_2026_09_26.py
```

Twelve checks; prints `TOTAL: PASS=12 FAIL=0` in about four minutes.
