# D = 3 Staggered Two-Band Orbital Response Requires the Interband Term, with a Finite-Cell Residual (Bounded)

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_d3_staggered_two_band_orbital_2026_06_13.py`
**Status:** source proposal; the audit lane grades.
**Status authority:** independent audit lane. This source note does not set or predict an audit outcome and does not edit audit-owned registry, ledger, queue, or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency. The independent audit lane owns status.

## Claim

For the free cubic staggered two-band model tested here, the finite-grid
orbital response has the following bounded `d = 3` behavior:

- The intraband Landau-Peierls part alone does not suffice. On the fixed
  `L = 8`, `mu = 0.4`, `T = 1.0`, `m in {0, 0.3, 0.6}` grid, LP-only misses
  the exact quantized Peierls reference by more than `10x` relative error.
- The interband geometric term is nonzero at `m != 0` and cancels the large LP
  term. With the fixed magnetic-area normalization `1/L^2`, the full
  `chi_intra + chi_inter` split tracks the exact finite-torus reference to the
  frozen `12%` relative gate on the mass grid.
- The remaining residual is named, not hidden: it is the finite-cell/finite-flux
  mismatch between the `L <= 8` quantized periodic-torus reference and the
  zero-field perturbative split. The result is therefore bounded evidence for a
  required interband completion, not a thermodynamic closure theorem.
- The exact reference itself is not yet `L`-converged at `L <= 8`: `chi` runs
  `-0.177` (`L=4`) -> `+0.082` (`L=6`) -> `+0.034` (`L=8`), so the `~9.8%`
  residual mixes the finite-flux `O(B^2)` curvature with residual finite-size
  effects; the `L=8` value is the converged edge of the tested ladder, not a
  thermodynamic limit.

## Model Convention

The two-band Bloch Hamiltonian is

```text
H(k) = 2 cos(kx) sigma_x + 2 cos(ky) sigma_y + (m + 2 cos(kz)) sigma_z.
```

The `sigma_z` orbital is the staggered parity component: the onsite mass is `+m`
on one parity orbital and `-m` on the other. The `z` hopping enters the same
staggered structure as `2 cos(kz) sigma_z`. The `x` and `y` hoppings carry
`sigma_x` and `sigma_y`; a uniform xy plaquette field is applied by Peierls
phases on those links.

The exact finite reference is a direct dense diagonalization of the periodic
`L^3` two-orbital lattice, with `L = 8` for the mass-grid reference and flux
`B = 2 pi / L^2`. The grand-potential curvature is

```text
chi = [Omega(B) + Omega(-B) - 2 Omega(0)] / B^2
```

per cubic cell, at fixed `mu` and `T`.

The perturbative split is computed independently from

```text
H(B) = H0 + B H1 + B^2 H2 + O(B^3)
```

using the finite-dimensional divided-difference formula for the grand-potential
curvature. The fixed magnetic-area normalization is `1/L^2`. It is a cell
normalization from the finite torus gauge area, not a fitted scalar prefactor.

## Measured Reference Rows

Reference grid: `L = 8`, `mu = 0.4`, `T = 1.0`.

| `m` | exact `chi` | full split `chi` | LP-only `chi` | interband `chi` | full rel. dev. |
|---:|---:|---:|---:|---:|---:|
| 0.0 | `+3.4631e-2` | `+3.1227e-2` | `+1.4722e+0` | `-1.4410e+0` | `9.8e-2` |
| 0.3 | `+3.4462e-2` | `+3.1078e-2` | `+1.4780e+0` | `-1.4469e+0` | `9.8e-2` |
| 0.6 | `+3.3956e-2` | `+3.0629e-2` | `+1.4690e+0` | `-1.4384e+0` | `9.8e-2` |

Note: the individual `chi_intra` (`~+1.47`) and `chi_inter` (`~-1.44`) magnitudes are `L`-dependent (scale `~0.19*L`) and not intensive; only their cancellation (the `full split chi`) is the converged, physically meaningful quantity. The `1.47` vs `-1.44` split should not be read as a physical magnitude decomposition.

The sign table is also bounded-gated. On the sampled
`mu in {0, 0.4, 1.0, 2.0}` grid at `T = 1.0`, the exact reference is positive
through `mu = 1.0` and negative at `mu = 2.0` for every tested mass; the closed
split tracks those sampled sign changes.

## Scope

Free one-particle cubic two-band model only. No interaction, no Fock-space
claim, no continuum-QFT claim, and no thermodynamic-limit theorem. The finite
reference uses direct diagonalization of a periodic quantized-flux torus with
`L <= 8`; the perturbative split uses the same finite lattice at `B = 0` plus
the fixed `1/L^2` magnetic-area normalization.

The audit lane grades.
