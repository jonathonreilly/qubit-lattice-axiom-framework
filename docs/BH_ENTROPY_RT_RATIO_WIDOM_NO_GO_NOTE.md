# BH Entropy RT-Ratio Widom Finite-Size Diagnostic

> **Key terms used in this doc** are indexed A-Z at
> [`KEY_TERMINOLOGY.md`](KEY_TERMINOLOGY.md).

**Date:** 2026-07-11
**Claim type:** open_gate
**Status:** finite diagnostic and exact geometric integral; no current no-go or
all-`L` entropy theorem is claimed
**Audit-status authority:** independent audit lane only
**Primary runner:**
[`scripts/frontier_bh_entropy_rt_ratio_widom.py`](../scripts/frontier_bh_entropy_rt_ratio_widom.py)

## Current Claim Boundary

This note records three separate facts that must not be conflated:

1. For the two-dimensional half-filled square-lattice Fermi diamond and a
   straight cut, direct evaluation of the standard Widom geometric integral
   gives `1/6` in the normalization used by the runner.
2. Even-`L` open-boundary Hamiltonians have a degenerate zero-energy subspace.
   The runner therefore uses the basis-invariant quasifree prescription

   ```text
   C = 1(H < 0) + (1/2) 1(H = 0).
   ```

   This defines a mixed Gaussian ensemble, not a uniquely selected pure Slater
   ground state.
3. On the sampled sizes `L <= 64`, the finite ratio

   ```text
   r(L) = S_corr(L) / (L log chi_eff(L))
   ```

   decreases from `0.3623` at `L=8` to `0.2570` at `L=64`. A two-parameter
   fit `c + a/log L` over `L >= 32` gives `c = 0.1568`, but that intercept is
   model-dependent finite-size evidence. The raw largest-size value is still
   within `2.8%` of `1/4`.

The exact `1/6` geometric integral is therefore not, by itself, an asymptotic
coefficient theorem for the mixed-state observable computed by the runner.
The earlier broad no-go reading is withdrawn.

## Carrier And Observable

On the open square

```text
Lambda_L = {1, ..., L}^2,
```

the one-particle Hamiltonian has nearest-neighbor matrix elements `-t` and
zero otherwise. For even `L`, diagonalization yields negative, zero, and
positive spectral subspaces. The correlation matrix above gives half
occupation to the entire zero eigenspace. Because it is a spectral function of
`H`, it is invariant under any basis rotation within that eigenspace and has
`Tr(C) = L^2/2`.

For the left half of the lattice, `A`, the runner computes

```text
S_corr(A) = -Tr[C_A log C_A + (1-C_A) log(1-C_A)].
```

For this mixed global quasifree state, `S_corr(A)` is a Gaussian subsystem
correlation entropy. It must not be described as pure-state bipartite
entanglement without an additional subtraction or state-selection theorem.

The comparison rank is

```text
chi_eff(L) = #{ singular values sigma_k(T)
                with sigma_k(T)/sigma_max(T) > 10^-6 },
```

where `T` is the correlation block between the two lattice layers adjacent to
the cut. This thresholded rank is a diagnostic readout, not a derived tensor
bond dimension.

## Exact Geometric Calculation

For the two-dimensional half-filled infinite square-lattice dispersion

```text
epsilon(k_x,k_y) = -2t(cos k_x + cos k_y),
```

the Fermi surface is the diamond `cos k_x + cos k_y = 0`. In the runner's
straight-cut normalization, the boundary-normal integral is `4 pi`, so

```text
c_geom = (1 / (12 * 2 pi)) * 4 pi = 1/6.
```

This is an exact evaluation of the geometric integral. Using it as the leading
coefficient of `S_corr` for the finite open-boundary mixed prescription needs
the missing bridge below.

## Reproducible Finite Evidence

The current runner reports:

| diagnostic | value |
|---|---:|
| `r(8)` | `0.3623` |
| `r(32)` | `0.2770` |
| `r(64)` | `0.2570` |
| fitted `c` for `L >= 32` in `c+a/log L` | `0.1568` |
| fitted deviation from `1/6` | `5.90%` |
| fitted deviation from `1/4` | `37.27%` |
| raw `r(64)` deviation from `1/4` | `2.8%` |

These values establish only the sampled trend and the stated fit. Alternative
finite-size forms, zero-mode prescriptions corresponding to particular pure
states, and mixed-entropy subtractions can change the extrapolation.

## Open Gates

- **Mixed-state asymptotic bridge.** Prove the leading asymptotic of
  `S_corr` for `C = 1(H<0) + 1/2 1(H=0)` on the open carrier, including the
  contribution of the `O(L)` zero-mode manifold, or replace it with a
  physically selected pure-state prescription and prove that selection.
- **Threshold-rank scaling bridge.** Prove the asymptotic behavior of the
  thresholded `chi_eff(L)`. The sufficient logarithmic statement for the
  intended cancellation is

  ```text
  log chi_eff(L) / log L -> 1
  ```

  in two dimensions; the finite equality `chi_eff(64)=64` does not establish
  it.
- **Black-hole observable bridge.** Derive why this carrier, cut,
  correlation entropy, and threshold-rank denominator represent the physical
  black-hole entropy observable. The current calculation is a comparison, not
  that derivation.

Until all three gates close, neither `lim r(L)=1/6`, `lim r(L)=1/4`, nor a
carrier-wide exclusion of `1/4` is a live claim.

## Reproduction

```bash
python3 scripts/frontier_bh_entropy_rt_ratio_widom.py
```

Expected current summary: `PASS=10 FAIL=0`. The PASS count means the finite
diagnostic reproduced its declared checks; it is not an audit grade or an
asymptotic theorem.

## Literature Context

The geometric integral is the standard Widom/Gioev-Klich free-fermion
coefficient calculation, with rigorous continuum results associated with the
Widom-Sobolev program and Helling-Leschke-Spitzer. Those pure-state results do
not automatically settle the mixed open-boundary prescription used here; that
translation is the open mixed-state asymptotic bridge above.
