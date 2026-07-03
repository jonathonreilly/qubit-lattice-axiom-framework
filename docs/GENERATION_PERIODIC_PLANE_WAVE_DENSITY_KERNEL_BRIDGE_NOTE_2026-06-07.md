# Generation Periodic Plane-Wave Density-Kernel Bridge

**Date:** 2026-06-07
**Type:** exact-support bridge theorem
**Claim scope:** bridge from the retained bounded self-consistent two-body
mediator family `V = -G (L + mu^2 I)^-1` to the finite periodic
translation-invariant plane-wave density-density kernel and normalization
used by
`GENERATION_LOCALIZATION_MOMENTUM_CORNER_DELTA_JI_PROTECTED_NARROW_THEOREM_NOTE_2026-06-06`.

**Primary runner:**
[`scripts/audit_companion_generation_periodic_plane_wave_density_kernel_bridge_2026_06_07.py`](../scripts/audit_companion_generation_periodic_plane_wave_density_kernel_bridge_2026_06_07.py)

**Status authority:** independent audit lane only. This bridge does not set an
audit verdict and does not edit audit ledger files.

## Statement

Let `T_L = (Z/LZ)^3` with even `L`, volume `N=L^3`, and periodic nearest
neighbor graph Laplacian

```text
(Delta f)(x) = sum_{nu=1}^3 (2 f(x) - f(x+e_nu) - f(x-e_nu)).
```

For a lattice momentum `k in (2*pi/L) Z^3`, define the normalized plane wave

```text
psi_k(x) = N^(-1/2) exp(i k dot x).
```

Then:

```text
Delta psi_k = eps(k) psi_k,
eps(k) = sum_nu 2(1 - cos k_nu).
```

The finite periodic mediator regularization of the retained bounded
two-body operator family is

```text
V_L = -G (Delta + mu^2 I)^(-1),          mu^2 > 0.
```

Because the plane waves diagonalize `Delta`,

```text
V_L psi_q = Vq(q) psi_q,
Vq(q) = -G / (eps(q) + mu^2).
```

For two normalized plane waves `psi_k` and `psi_l`, the density-density
Slater mutual energy is the exact finite-volume Hartree-Fock matrix element

```text
delta(k,l) = <rho_k, V_L rho_l> - <psi_k^* psi_l, V_L psi_l^* psi_k>
           = (Vq(0) - Vq(k-l)) / N.
```

The `1/N` factor is not fitted: it is the normalization
`|psi_k(x)|^2 = 1/N` on `N` sites, and the exchange density
`psi_k^*(x) psi_l(x) = N^(-1) exp(i(l-k) dot x)` has the same finite-volume
Fourier normalization.

## Relation To The Retained Bounded Mediator

The retained bounded note
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md)
establishes the attractive self-consistent two-body channel on calibrated
open cubic lattices. This bridge does not claim that the open-cubic force
surface is the periodic plane-wave theorem. It supplies the missing
boundary/normalization bridge: for the same local mediator stencil and
positive `mu^2`, the even periodic torus has a translation-invariant
Fourier basis, and the density-density matrix element is the formula above.

This is the exact bridge the generation localization row needs for its
pure-corner plane-wave calculation. It does not pin the physical magnitude,
`G`, `mu^2`, or effective volume.

## Application To The Generation Localization Row

For the retained `hw=1` corner triplet

```text
k_1=(pi,0,0), k_2=(0,pi,0), k_3=(0,0,pi),
```

each distinct pair has `eps(k_i-k_j)=8`. Therefore the finite periodic
plane-wave kernel gives equal pair mutual energies

```text
delta_ij = (Vq(0)-Vq(k_i-k_j))/N < 0
```

for all three pairs, because `Vq(0)=-G/mu^2` is more negative than
`Vq(k_i-k_j)=-G/(8+mu^2)`. The equality across pairs is the `J-I` form;
the negativity is the sign cross-check. The magnitude remains controlled
by the open IR data `(G, mu^2, N)`.

## Forbidden Imports Check

- No new axiom is introduced.
- No observed value, PDG input, fitted selector, or admitted unit convention
  is used.
- The bridge proves the periodic finite-volume normalization internally; it
  does not import it from a textbook.
- The retained bounded open-cubic mediator remains a bounded input; this
  bridge is proposed exact support and still requires independent audit.

## Validation

The companion runner checks:

1. even periodic momenta and normalized plane waves;
2. the periodic Laplacian eigenvalue formula `eps(k)`;
3. the Green-kernel eigenvalue formula `Vq(q)`;
4. direct finite-matrix Hartree and Fock terms against
   `(Vq(0)-Vq(k-l))/N`;
5. equal `eps=8`, equal negative pair energies, and `1/N` scaling for the
   three retained `hw=1` corners;
6. source-note and downstream-note bridge markers.

Expected runner summary:

```text
TOTAL: PASS=27 FAIL=0
```
