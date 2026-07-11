# Teleportation Initial-State Preparation Probe

**Date:** 2026-04-25
**Status:** exact boundary theorem on an open gate; operational preparation remains open
**Type:** open_gate
**Runner:** `scripts/frontier_teleportation_initial_state_preparation_probe.py`

## Scope

This note audits the initial-state assumption used by the finite-time
adiabatic ramp:

```text
H(s) = H(G=0) + s(t) * (H(G_target) - H(G=0)).
```

The question is whether the `G=0` two-species ground state is unique, simple,
product-like, separable across the relevant partitions, native-basis local, and
operationally plausible to prepare.

Strict boundary: ordinary quantum state teleportation only. This artifact does
not claim matter transfer, mass transfer, charge transfer, energy transfer,
object transport, or faster-than-light signaling.

## Commands Run

```bash
python3 -m py_compile scripts/frontier_teleportation_initial_state_preparation_probe.py
python3 scripts/frontier_teleportation_initial_state_preparation_probe.py
```

Both commands completed successfully.

Default thresholds:

- degeneracy tolerance: `1e-9`;
- support threshold: native-basis probability `> 1e-12`;
- uniqueness/gap threshold: `1e-6`;
- localized state threshold: participation fraction `PR/dim <= 0.25`.

## Spectral Diagnostics

Both default `G=0` cases have a unique two-species ground state with a finite
small-surface gap.

| case | `N` | single-species `E0` | single-species gap | two-species `E0` | two-species degeneracy | two-species gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `1d_null_initial` | `8` | `-2.000000` | `0.585786` | `-4.000000` | `1` | `0.585786` |
| `2d_null_initial` | `16` | `-4.000000` | `2.000000` | `-8.000000` | `1` | `2.000000` |

The `G=0` two-species ground state exactly matches the tensor product of two
single-species `H1` ground states:

| case | `|<g_G0 | g_H1 x g_H1>|^2` | `|<g_G0 | uniform x uniform>|^2` |
| --- | ---: | ---: |
| `1d_null_initial` | `1.000000` | `1.000000` |
| `2d_null_initial` | `1.000000` | `1.000000` |

## Derivation Closure

For the two default cases the runner uses `mass=0`, `G=0`, and `t_hop=1`.
The single-species Hamiltonian is therefore the negative adjacency operator on
the periodic lattice,

```text
H1 = -A,
```

The `1D N=8` cycle is connected and degree `2`; the `2D 4x4` torus is
connected and degree `4`. Equivalently, periodic Fourier vectors diagonalize
the two audited Hamiltonians. On a `d`-dimensional side-`L` periodic lattice,

```text
H1 |k> = -2 sum_(a=1)^d cos(2 pi k_a/L) |k>.
```

Every cosine is at most one, and equality for every factor occurs only at the
single momentum `k=(0,...,0)`. Thus the ground vector is unique and is the
uniform native-site vector

```text
|u_N> = N^(-1/2) sum_i |i>,
```

with energies `-2` and `-4` in the two audited cases. Changing one momentum
component to the smallest nonzero value gives the exact first gap

```text
Delta_1 = 2[1 - cos(2 pi/L)].
```

It is therefore `2-sqrt(2)` for `1D N=8` and `2` for the `2D 4x4` torus,
matching `0.585786` and `2.000000` in the table. This is an analytic
finite-surface result; the eigensolver is a check rather than the source of the
uniqueness or gap claim.

Species `A` and `B` are distinguishable registers in the ordered basis
`|i>_A x |j>_B`; no bosonic or fermionic symmetrization is imposed. At `G=0`,
`build_H2_tensor` drops the Poisson diagonal term and the two-species
Hamiltonian is the Kronecker sum

```text
H(G=0) = H1 x I + I x H1.
```

If `H1 |phi_k> = E_k |phi_k>`, then
`|phi_a> x |phi_b>` is an eigenvector of `H(G=0)` with energy `E_a + E_b`.
Because the `H1` ground vector is simple in both default cases, the unique
two-species ground vector is

```text
|g_G0> = |u_N>_A x |u_N>_B,
```

with energy `2 E0` and gap `E1 - E0`. This is the analytic reason the runner
finds fidelity `1.000000` against both the `H1`-ground tensor product and the
uniform-site tensor product.

The same formula also closes the separability and delocalization chain. As a
species state, `|g_G0>` is a single tensor product. In the `factor_sites`
logical/environment split used by the teleportation runners, each default even
lattice decomposes each native site as one logical taste bit plus an
environment label, and the uniform site vector factors as
`|+>_logical x |u_env>`. Therefore

```text
|g_G0> =
  (|+>_A x |u_env>_A) x (|+>_B x |u_env>_B)
  = (|+>_A x |+>_B) x (|u_env>_A x |u_env>_B),
```

so the audited species and logical/environment Schmidt ranks are exactly one up
to numerical tolerance. The traced logical state is the separable product
`|++><++|`, explaining the non-entangled logical diagnostics: Bell overlap
`0.5`, CHSH `2.0`, and negativity `0.0`.

Finally, because `|g_G0>` has equal amplitude on every native site pair, every
native site-pair probability is `1/N^2`. Its support is the whole `N^2`
site-pair basis, its participation ratio is `N^2`, and `PR/dim = 1`. The
single-species factor has the analogous full support, participation ratio `N`,
and `PR/dim = 1`. Thus the state is maximally delocalized in the native basis
even though it is unique, exactly product, and separable.

## Executable Derivation Certificate

The runner treats this chain as a failing certificate, not only as printed
diagnostics. For each default case it checks:

- the graph is connected, regular, and has degree `2d`;
- the constructed matrices satisfy `H1=-A` and
  `H(G=0)=H1 x I + I x H1` with residual at most `1e-10`;
- the uniform vectors obey the predicted one- and two-species eigenvalue
  equations and the exact Fourier energies and gaps above;
- the numerical ground vector has unit fidelity, within tolerance, to both the
  `H1`-ground tensor product and the uniform tensor product;
- every stated separability cut has numerical Schmidt rank one;
- the one- and two-species states have full native support and `PR/dim=1`;
- the uniform site vector factors as `|+>_logical x |u_env>` in the actual
  `factor_sites` indexing.

Any failed item makes the runner return a nonzero exit code. The default run
prints `derivation certificate: PASS`, with zero structural and eigenvector
residuals on both surfaces.

This certificate closes only the finite diagnostic chain. It does not turn
native-basis delocalization into an operational obstruction theorem, nor does
it supply a method for creating, cooling, controlling, or verifying the state.

## Separability Diagnostics

The state is product-like on the audited partitions. Entropies are numerical
zero, purities are `1`, and numerical Schmidt rank is `1`.

| case | partition | entropy bits | purity | max Schmidt weight | numerical rank |
| --- | --- | ---: | ---: | ---: | ---: |
| `1d_null_initial` | species A / species B | `6.218312e-28` | `1.000000` | `1.000000` | `1` |
| `1d_null_initial` | logical pair / environment pair | `1.229403e-27` | `1.000000` | `1.000000` | `1` |
| `1d_null_initial` | single `H1` logical / environment | `1.234057e-28` | `1.000000` | `1.000000` | `1` |
| `2d_null_initial` | species A / species B | `1.847779e-29` | `1.000000` | `1.000000` | `1` |
| `2d_null_initial` | logical pair / environment pair | `1.800077e-29` | `1.000000` | `1.000000` | `1` |
| `2d_null_initial` | single `H1` logical / environment | `1.808875e-29` | `1.000000` | `1.000000` | `1` |

The traced logical resource at `G=0` is not an entangled teleportation
resource. It has Bell overlap `0.5`, CHSH `2.0`, and negativity `0.0` in both
dimensions.

## Native-Basis Support

The finite diagnostic fact is that the assumed state is maximally delocalized
in the native site basis. Delocalization alone is not an operational
obstruction; the preparation gap is the absence of a supplied physical
protocol and scaling argument.

| case | state | basis dim | support | participation ratio | `PR/dim` | max probability | site entropy bits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `1d_null_initial` | single `H1` ground | `8` | `8` | `8.000000` | `1.000000` | `0.125000` | `3.000000` |
| `1d_null_initial` | two-species `G=0` ground | `64` | `64` | `64.000000` | `1.000000` | `0.015625` | `6.000000` |
| `2d_null_initial` | single `H1` ground | `16` | `16` | `16.000000` | `1.000000` | `0.062500` | `4.000000` |
| `2d_null_initial` | two-species `G=0` ground | `256` | `256` | `256.000000` | `1.000000` | `0.003906` | `8.000000` |

By the default localization threshold `PR/dim <= 0.25`, neither default case is
native-basis localized.

## Candidate Product-State Comparison

Simple localized candidates are separable but are not the `G=0` ground state.
The only exact candidate is the delocalized `H1` ground-state tensor product.

| case | candidate | energy excess `E-E0` | ground fidelity | `PR/dim` | logical/env entropy | Bell overlap | negativity |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `1d_null_initial` | `H1` ground tensor product | `-2.664535e-15` | `1.000000` | `1.000000` | `2.548015e-28` | `0.500000` | `0.000000` |
| `1d_null_initial` | uniform site product | `-1.776357e-15` | `1.000000` | `1.000000` | `9.230725e-31` | `0.500000` | `0.000000` |
| `1d_null_initial` | localized `|0>_A |0>_B` | `4.000000` | `0.015625` | `0.015625` | `0` | `0.500000` | `0.000000` |
| `1d_null_initial` | single-env logical `|+>` product | `2.000000` | `0.062500` | `0.062500` | `0` | `0.500000` | `0.000000` |
| `2d_null_initial` | `H1` ground tensor product | `0` | `1.000000` | `1.000000` | `4.855549e-29` | `0.500000` | `0.000000` |
| `2d_null_initial` | uniform site product | `0` | `1.000000` | `1.000000` | `9.685856e-31` | `0.500000` | `0.000000` |
| `2d_null_initial` | localized `|0>_A |0>_B` | `8.000000` | `0.003906` | `0.003906` | `0` | `0.500000` | `0.000000` |
| `2d_null_initial` | single-env logical `|+>` product | `6.000000` | `0.015625` | `0.015625` | `0` | `0.500000` | `0.000000` |

The localized separated-site candidates have the same energy excess and ground
fidelity as the localized `|0>_A |0>_B` candidates in the default `G=0` run.

## Verdict

Verdict: **unresolved preparation gap, not a diagnostic no-go**.

On the default small surfaces, the assumed initial state is:

- unique and gapped at `G=0`;
- exactly a tensor product of two single-species `H1` ground states;
- separable across species and logical/environment partitions;
- analytically simple as a uniform native-site product state;
- not localized or sparse in the native site-pair basis.

Operationally, the assumption reduces to preparing two independent coherent
single-species `H1` ground states. That is a clean candidate target, but this
artifact does not provide a physical cooling/control/readout protocol, a noise
model, or a scaling proof. The finite-time ramp therefore still carries an
initial-state preparation gap.

## Limitations

- Exact small surfaces only: `1D N=8` and `2D 4x4`.
- The displayed Fourier formula is used here only to certify the two default
  surfaces; no operational preparation-time scaling law follows from it.
- No bath, cooling, control-noise, calibration, or state-verification model.
- The native-basis localization threshold is diagnostic, not a theorem.
- Logical Bell measurement and readout remain idealized in adjacent artifacts.
- Scope remains ordinary quantum state teleportation only.
