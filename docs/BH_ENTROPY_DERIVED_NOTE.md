# Bekenstein-Hawking Entropy Finite-Lattice Cache Certificate

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded finite-lattice cache certificate. This is not an
infinite-size entropy theorem and not a derivation of the
Bekenstein-Hawking coefficient.
**Runner:** [`scripts/frontier_bh_entropy_derived.py`](../scripts/frontier_bh_entropy_derived.py)

## Purpose

The prior row mixed a finite lattice comparison with broader coefficient and
infinite-size language. This repair keeps only the committed finite-runner
evidence on the reviewed lattice sizes.

The load-bearing cache is
`logs/runner-cache/frontier_bh_entropy_derived.txt`. It records an OBC
free-fermion tight-binding entanglement comparison on finite 2D and 3D
lattices.

## Bounded Claim

The committed cache reports:

| Check | Finite Result |
|---|---:|
| 2D area-law-like fit | `R^2 = 0.999664` |
| 3D area-law-like fit | `R^2 = 0.998952` |
| 2D finite-L RT ratio mean | `0.2364` |
| 3D finite-L RT ratio mean | `0.1222` |
| Gravity modulation for `g >= 0.5` | monotone |
| Species-universality spread | `2.78e-17` |

The finite 2D ratio is numerically close to the comparison target `1/4` on
the reviewed sizes. The finite 3D ratio is not close to `1/4`. The runner
records those as finite observations, not proof of a physical entropy
coefficient.

## Boundary

This row does not claim:

- an infinite-size coefficient;
- a derivation of `S = A / (4 l_P^2)`;
- a physical black-hole entropy theorem;
- a proof that the chosen carrier is the correct horizon Hilbert space;
- any result on unreviewed larger lattice sizes;
- any new axiom or audit verdict.

The row only certifies the finite cached evidence listed above.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_bh_entropy_derived.py
```
