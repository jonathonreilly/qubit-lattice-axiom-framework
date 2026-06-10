# Generation Corner Hartree-Fock `Vq` Screened-Poisson Bridge - Narrow Theorem

**Date:** 2026-06-07
**Type:** positive_theorem source packet (exact support; audit pending)
**Status:** exact-support source-note proposal; independent audit required.
This source-side note does not write or imply an audit verdict.
**Primary runner:** [`scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py`](../scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py)
**Cached output:** [`logs/runner-cache/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt`](../logs/runner-cache/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt)

## Audit target

This note is a one-hop source bridge for
`GENERATION_LOCALIZATION_MOMENTUM_CORNER_DELTA_JI_PROTECTED_NARROW_THEOREM_NOTE_2026-06-06.md`.
The target repair asks for a retained-grade authority deriving the periodic
translation-invariant Hartree-Fock plane-wave mutual-energy readout

```text
Vq(q) = -G/(eps(q) + mu^2)
delta_ij = (Vq(0) - Vq(k_i - k_j))/N
```

including boundary and normalization, from the retained staggered two-body mediator.

This note supplies the missing framework-native derivation as exact support. It does not retag
the target row, does not edit `docs/audit/**`, and does not widen the retained bounded mediator.

## Inputs

Retained or retained-bounded current authorities used only within their audited scopes:

- [`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md):
  retained_bounded evidence that the native staggered architecture supports an attractive
  screened graph-Poisson two-body channel on its calibrated open-cubic force surface.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
  [`THREE_GENERATION_STRUCTURE_NOTE`](THREE_GENERATION_STRUCTURE_NOTE.md), and
  [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md):
  current authorities for the three `hw=1` generation corners and their translation-character
  distinction.

The new work here is not a new axiom. It is finite-dimensional linear algebra for the same
screened graph-Poisson operator family on the periodic idealization needed by the pure-corner
readout.

## Theorem

Let `L` be even and let

```text
Lambda_L = (Z/LZ)^3,     N = L^3,     mu^2 > 0,     G > 0.
```

Let `Lap` be the periodic nearest-neighbor graph Laplacian

```text
(Lap f)(x) = sum_a (2 f(x) - f(x+e_a) - f(x-e_a)).
```

For momenta `q` in the finite Brillouin grid `(2*pi/L) Z_L^3`, define the normalized characters

```text
phi_q(x) = N^(-1/2) exp(i q.x)
```

and

```text
eps(q) = sum_a 2(1 - cos q_a).
```

Then:

1. `Lap phi_q = eps(q) phi_q`.
2. The attractive screened graph-Poisson kernel
   `K = -G (Lap + mu^2 I)^(-1)` has Fourier multiplier
   `Vq(q) = -G/(eps(q) + mu^2)`.
3. For two distinct plane-wave corner modes `phi_ki, phi_kj`, evaluated as a two-mode Slater
   state under the density-density kernel `K`, the mutual Hartree-minus-exchange energy is

```text
delta_ij = (Vq(0) - Vq(k_i - k_j)) / N.
```

For the three `hw=1` generation corners

```text
k1 = (pi,0,0),   k2 = (0,pi,0),   k3 = (0,0,pi),
```

every pair has `eps(k_i - k_j) = 8`, hence all three `delta_ij` are equal. Since
`Vq(0) < Vq(k_i-k_j) < 0` for `G>0, mu^2>0`, the common `delta_ij` is negative. Its pure-corner
magnitude scales as `1/N` with the fixed IR multiplier `G/mu^2`.

## Proof

### 1. Periodic Laplacian diagonalization

The periodic shifts commute and are diagonal on the normalized characters:

```text
phi_q(x+e_a) = exp(i q_a) phi_q(x),
phi_q(x-e_a) = exp(-i q_a) phi_q(x).
```

Substitution in the graph Laplacian gives

```text
(Lap phi_q)(x)
 = sum_a (2 - exp(i q_a) - exp(-i q_a)) phi_q(x)
 = sum_a 2(1 - cos q_a) phi_q(x)
 = eps(q) phi_q(x).
```

The normalized characters are an orthonormal basis of `C^Lambda_L`, so this diagonalizes `Lap`.

### 2. Screened Green multiplier

Because `mu^2 > 0` and `eps(q) >= 0`, every eigenvalue `eps(q)+mu^2` of `Lap + mu^2 I` is
strictly positive. Therefore the inverse exists on the whole finite Hilbert space, and in the
same character basis

```text
(Lap + mu^2 I)^(-1) phi_q = (eps(q)+mu^2)^(-1) phi_q.
```

Multiplication by `-G` gives the attractive screened graph-Poisson kernel

```text
K phi_q = Vq(q) phi_q,    Vq(q) = -G/(eps(q)+mu^2).
```

This proves the boundary and normalization of the `Vq` readout used by the generation-corner
target. The periodic boundary is not imported from continuum Fourier analysis; it is the finite
translation-character basis of `Lambda_L`.

### 3. Hartree-minus-exchange readout

Write the kernel in translation-invariant form

```text
K(x,y) = K(x-y) = (1/N) sum_q Vq(q) exp(i q.(x-y)).
```

For normalized plane waves, `|phi_ki(x)|^2 = |phi_kj(x)|^2 = 1/N`. The Hartree cross term is

```text
H_ij = sum_x,y |phi_ki(x)|^2 K(x-y) |phi_kj(y)|^2
     = Vq(0)/N.
```

The exchange term is

```text
X_ij = sum_x,y conj(phi_ki(x)) phi_kj(x) K(x-y)
                 conj(phi_kj(y)) phi_ki(y)
     = Vq(k_i-k_j)/N,
```

using the evenness `Vq(-q)=Vq(q)`. The Slater density-density mutual energy is therefore

```text
delta_ij = H_ij - X_ij = (Vq(0) - Vq(k_i-k_j))/N.
```

This is the exact finite-lattice Hartree-Fock normalization. No textbook continuum transform,
infinite-volume limit, observed flavor number, or fitted localization length is used.

### 4. Corner specialization

For any two different `hw=1` corners, the difference has exactly two `pi` components and one
zero component. Hence

```text
eps(k_i-k_j) = 2(1-cos pi) + 2(1-cos pi) + 2(1-cos 0) = 8.
```

All three pair readouts are equal. Also

```text
delta_ij
 = -G/(N mu^2) + G/(N(8+mu^2))
 = -8G/(N mu^2(8+mu^2)) < 0.
```

The equal pair value is exactly the `J-I` corner-protected coupling form used by the target
note, while its magnitude is controlled by the mediator IR parameters and `N`, not by a spatial
generation separation.

## Relation to the retained bounded two-body mediator

The retained bounded mediator note audits an open-cubic calibrated force surface; this bridge
does not widen that result to a universal or periodic physical mediator theorem. The bridge
instead proves that the same native screened graph-Poisson operator family, when placed on the
finite periodic translation-character surface required by the pure-corner generation readout,
has the exact `Vq` multiplier and Hartree-Fock normalization asserted by the target.

So the dependency role is precise:

- the retained bounded mediator supplies the current framework-native attractive screened
  density-density channel and sign convention;
- this note supplies the missing periodic boundary/normalization algebra for the pure-corner
  readout;
- the target remains audit-pending until an independent auditor decides whether this one-hop
  source bridge is sufficient for the target row.

## Boundary

- Periodic finite `L^3` lattice, even `L`, pure plane-wave corner modes only.
- Same-sector two-mode Slater Hartree-minus-exchange readout. If a future claim uses a
  distinguishable-species readout with no exchange term, it needs a separate bridge.
- No physical flavor magnitude, no `r`, no mixing angle, and no IR completion of `G`, `mu^2`,
  or effective `N`.
- No extension of the open-cubic retained bounded mediator beyond its audited force surface.
- No audit verdict is changed by this note.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py
```

The runner checks the retained dependency surface and source-packet links, verifies Fourier
diagonalization on finite periodic lattices, reconstructs the dense screened kernel from the
Fourier multiplier, and compares dense Hartree-minus-exchange values with the closed formula for
all three corner pairs.
