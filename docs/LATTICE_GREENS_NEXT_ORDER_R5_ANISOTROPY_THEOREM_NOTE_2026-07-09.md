# The Next-Order Lattice Correction to the Emergent Newtonian Potential: an Exact, Purely Anisotropic f(n̂)/r⁵ Term (l = 4, 6, 8)

**Date:** 2026-07-09
**Claim type:** positive_theorem
**Status:** source-side positive-theorem proposal; independent audit required.
**Primary runner:** [`scripts/frontier_lattice_greens_next_order_r5_anisotropy.py`](../scripts/frontier_lattice_greens_next_order_r5_anisotropy.py)
**Runner cache:** [`logs/runner-cache/frontier_lattice_greens_next_order_r5_anisotropy.txt`](../logs/runner-cache/frontier_lattice_greens_next_order_r5_anisotropy.txt)

## Summary

For the nearest-neighbor graph Laplacian on `Z^3` with unit lattice spacing, the
next-order theorem is

> `G(x) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + f(nhat)/r^5 + O(1/r^7)`,
> with `K4 = S4 - 3/5` and `S4 = nx^4 + ny^4 + nz^4`.

The coefficient has three equivalent exact forms. In the raw component form,
`128 pi f(nhat) = 23*(nx^8+ny^8+nz^8) - 244*(nx^6*ny^2 + nx^6*nz^2 + ny^6*nx^2 + ny^6*nz^2 + nz^6*nx^2 + nz^6*ny^2) + 621*(nx^4*ny^4 + nx^4*nz^4 + ny^4*nz^4) - 228*nx^2*ny^2*nz^2`. In the symmetric-power basis,
`f = [-181/512 + (315/256) S4 - (189/64) S6 + (1155/512) S4^2]/pi`, where
`S6 = nx^6 + ny^6 + nz^6`. In monic power-sum cubic-harmonic conventions,
`K6 = S6 - (15/11) S4 + 30/77` and
`K8 = S4^2 - (16/15) S6 + (2/13) S4 - 1/39`, so
`f = (315/2288)/pi K4 -(35/64)/pi K6 + (1155/512)/pi K8`.

The spherical average of `f` is exactly zero. Thus the derived `1/r^5`
coefficient is purely anisotropic and carries `l = 4, 6, 8` content, with no
`l = 0` part. A formal small-momentum symbol expansion suggests the same
contact-term pattern at higher orders; the runner verifies the combinatorial
grading only through `n = 4`. This note does not promote that finite formal
check to an all-orders asymptotic theorem for the full Brillouin-zone integral.

This answers the `O(1/r^5)` boundary left open by
[`docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md`](GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md),
whose T5 records that the spherical average of `K4` is zero, so the leading
correction has no isotropic `1/r^3` part and the first isotropic correction is
higher order. The leading
`1/(4 pi r)` machinery comes from
[`docs/LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`](LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md).
There are zero free parameters: every coefficient is an exact rational multiple
of `1/pi`.

## Derivation (machinery)

Write the Fourier symbol and its component expansion as
`lambda(k) = sum_mu (2 - 2 cos k_mu)` and
`2 - 2 cos u = u^2 - u^4/12 + u^6/360 - u^8/20160 + O(u^10)`.
With `A = (1/12) sum_mu k_mu^4` and `B = (1/360) sum_mu k_mu^6`, this is
`lambda = k^2 - A + B - ...`, and therefore
`exp(-t lambda) = exp(-t k^2) [1 + t A + (t^2 A^2/2 - t B) + ...]`.

The heat-kernel representation is
`G(x) = int_0^inf dt int d^3k/(2 pi)^3 exp(-t lambda(k) + i k.x)`.
The free Fourier integral is
`G_t = (4 pi t)^(-3/2) exp(-r^2/(4t))`. Under that integral,
`k_mu^4 -> +d^4/dx_mu^4` and `k_mu^6 -> -d^6/dx_mu^6`; the signs follow from
`i^4 = +1` and `i^6 = -1`. Consequently, the complete order-2 group is
`(t^2/288) sum_{mu,nu} d^4_mu d^4_nu + (t/360) sum_mu d^6_mu` acting on `G_t`,
integrated over `t` in `(0, inf)`.

After differentiation, every monomial's `t` integral is the exact Gamma-function
evaluation `int_0^inf t^q exp(-r^2/(4t)) dt = (r^2/4)^(q+1) Gamma(-q-1)` for
`q < -1`. Applying it to the order-2 group gives the raw polynomial in the
Summary divided by `128 pi r^13`; exact sphere reduction gives the S-basis and
harmonic forms there.

For the formal higher-order symbol check, expand
`exp(-t lambda) = exp(-t k^2) exp(t sum_{i>=1} (-1)^(i+1) c_i P_(2i+2)(k))`,
where `P_(2j)(k) = sum_mu k_mu^(2j)` and `c_i = 2/(2i+2)!`. Each exponential term
is `t^J` times a monomial of degree `2D` in `k`, built from `J` factors of degree
at least four. Hence `D - J - 1 >= 0` for `J >= 1`. Integrating `t` yields the
momentum-space density `J! * (monomial of degree 2D)/k^(2J+2)`. Its angular
average is formally a constant times `k^(2(D-J-1))`, a polynomial in `k^2`,
whose whole-space Fourier transform is supported at `x = 0`. Grouping by
`n = D - J` gives the formal radial powers `1/r^(2n+1)`. Extending this
small-momentum calculation to an all-orders asymptotic statement for the exact
lattice integral would additionally require singular/regular Brillouin-zone
control and justified termwise interchange; those steps are not proved here.

## Theorems (runner-verified)

- **S1.** `S1a` derives `1/(4 pi r)` from the free Gaussian by exact Mellin
  integration. `S1b` derives `[5/(32 pi)] K4/r^3` from the order-1 operator.
  `S1c` sends that same integrand through SymPy's direct improper integral and
  requires exact agreement with the Mellin result.
- **S2.** `S2a` applies the full order-2 differential operator and requires exact
  equality to the raw degree-eight polynomial. `S2b` substitutes
  `nz^2 = 1 - nx^2 - ny^2` and requires the raw/S-basis difference to be the zero
  polynomial. `S2c` makes the same exact zero-polynomial check for the harmonic
  form.
- **S3.** `S3a` uses exact double-factorial sphere moments to require `<f> = 0`.
  `S3b` requires `<K6> = <K6 K4> = 0`; `S3c` requires
  `<K8> = <K8 K4> = <K8 K6> = 0`. The seven `S3d` checks evaluate normalized
  directions symbolically and require exact equality to their rational-over-`pi`
  anchors.
- **S4.** The runner builds the formal symbol exponential through four factors from terms
  through component degree ten. For each grouped order `n = 1, 2, 3, 4`, every
  monomial must satisfy `D - J - 1 >= 0`, verifying the polynomial-isotropic
  grading of that truncated formal expansion.
- **N1.** The 24-digit Bessel-resolvent quadrature must satisfy the exact origin
  delta identity within `1e-18` (`N1a`) and the six-neighbor lattice equation at
  `(7,4,2)` and `(4,2,1)` within `1e-12` (`N1b`, `N1c`).
- **N2.** For each of five orbits, `N2a` fits the measured `r^5` residual against
  `[1, 1/r^2, 1/r^4]` and requires its constant to agree with the exact `f` within
  `2e-4`. `N2b` subtracts exact `f`; its last-pair residual ratio must lie between
  `0.7` and `1.35` times the predicted `r^-2` ratio.
- **CTRL1.** Increasing the axial exact value by five percent must fail the `2e-4`
  extrapolation gate.
- **CTRL2.** The same wrong value must put the axial last-pair ratio outside the
  `N2b` interval.
- **CTRL3.** Replacing `621` by `622` in the raw polynomial must make the `S2a`
  identity nonzero.

## Direction table

| Direction | Exact `f` | Decimal |
|---|---:|---:|
| `(1,0,0)` | `23/(128 pi)` | `0.0571963076736` |
| `(1,1,0)` | `179/(2048 pi)` | `0.0278210300913` |
| `(1,1,1)` | `-1/(48 pi)` | `-0.00663145596216` |
| `(2,1,0)` | `-149/(16000 pi)` | `-0.00296426081509` |
| `(2,1,1)` | `-157/(2048 pi)` | `-0.0244016856108` |
| `(3,2,1)` | `-2893/(100352 pi)` | `-0.00917640406499` |
| `(3,1,0)` | `4231/(256000 pi)` | `0.00526081690798` |

The sign changes with direction: it is positive near the axes and negative at
`(1,1,1)`, `(2,1,0)`, `(2,1,1)`, and `(3,2,1)`.

## What this establishes / what it does not claim

This establishes the exact next-order term, its pure anisotropy, and its
`l = 4, 6, 8` content. The higher-order contact-term statement is a formal
small-momentum proposition checked through `n = 4`, not an all-orders theorem
for the exact lattice Green function.

It does not claim dynamics, because the framework has no dynamics axiom. It does
not determine the overall physical scale: that scale is registered, while the
derived content is the exact ratio structure relative to the leading
`1/(4 pi r)` term. It also does not claim convergence of the full asymptotic
series or a rigorous all-orders singular/regular Brillouin-zone decomposition.
Independent exact lattice numerics anchor the `n = 2` term.

## Relation to the repo inventory

The two markdown-linked notes above are the direct upstreams; neither is assigned
an independent-review designation here. As context only,
`lattice_greens_function_maradudin_textbook_import_note_2026-05-18` numerically
observed an `O(r^-5)` residual after subtracting the leading kernel. This note
derives that residual's exact coefficient function framework-internally, without
literature input in the derivation.

## Boundary / honest-auditor read

(a) The symbol expansion and termwise Fourier transform use the same asymptotic
machinery as the landed leading-correction note. Exact-arithmetic lattice numerics
independently confirm the result on five orbits, with agreement from `1e-4` through
`1e-8` for the predicted next-correction ratio structure. (b) The formal
contact-term grading through `n = 4` does not control high-momentum
contributions or justify an all-orders interchange. (c) The next path is the
`O(1/r^7)` (`n = 3`) term, a rigorous Brillouin-zone remainder analysis, and
the gradient/field-level readout of the `r^-5` term.
