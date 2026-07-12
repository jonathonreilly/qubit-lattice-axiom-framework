# Bekenstein-Hawking Entropy Finite-Lattice Companion

**Date:** 2026-07-11
**Claim type:** open_gate
**Status:** open finite numerical companion; no retained black-hole entropy
derivation or all-`L` coefficient theorem is claimed
**Audit-status authority:** independent audit lane only
**Primary runner:**
[`scripts/frontier_bh_entropy_derived.py`](../scripts/frontier_bh_entropy_derived.py)

## Scope

This note records reproducible finite-lattice calculations for a half-filled
nearest-neighbor free-fermion carrier. It compares a Gaussian subsystem
correlation entropy with

```text
S_max = |dA| log chi_eff
```

and with the Bekenstein-Hawking comparison coefficient `1/4`. It does not
derive that normalization from the four axioms—Lattice, Qubit, Admissibility,
and Record—and it does not identify the carrier observable with physical
black-hole entropy.

The paired
[`BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md`](BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md)
now classifies the asymptotic issue as an open gate. In particular, the exact
two-dimensional geometric Widom integral `1/6` is not silently promoted to the
coefficient of the mixed zero-mode prescription used by these finite runs.

## State Prescription

At half filling the `N/2` spectral cut can cross a degenerate eigenspace.
Selecting an arbitrary subset of eigenvectors would make the result depend on
the diagonalizer's basis. The runner instead occupies the whole Fermi-level
eigenspace with the common fractional weight needed for `Tr(C)=N/2`.

For the particle-hole-symmetric cases in the current grids this reduces to

```text
C = 1(H<0) + (1/2)1(H=0).
```

The resulting global state is generally mixed. The reported `S_corr` is the
Gaussian entropy of the restricted correlation matrix, not a claimed
pure-state entanglement entropy.

## Reproduced Finite Results

The current runner reports:

- two-dimensional finite boundary fit: `R^2 = 0.999010`;
- three-dimensional finite boundary fit: `R^2 = 0.996339`;
- mean finite comparison ratio `S_corr/(|dA| log chi_eff)`:
  `0.3143` in 2D and `0.1249` in 3D;
- two-dimensional `1/L` diagnostic intercept: `0.2492`;
- three-dimensional `1/L` diagnostic intercept: `0.0644`;
- monotone entropy decrease for the sampled positive `g/r` onsite potential at
  `g >= 0.5`;
- exact cancellation of duplicate-copy factors under the runner's explicitly
  independent-copy construction. This is a bookkeeping identity, not a
  species-universality, Hilbert-dimension, or bond-dimension result.

The fit intercepts are model-dependent finite-size summaries. The 2D
`1/L` intercept being close to `1/4` is evidence against declaring the finite
data inconsistent with `1/4`; the separate `c+a/log L` fit in the Widom runner
favors a value near `1/6`. Neither fit is an all-`L` theorem.

## Imported And Conventional Inputs

- nearest-neighbor free-fermion Hamiltonian and open boundary conditions;
- the basis-invariant mixed half-filling prescription;
- the Bekenstein-Hawking `1/4` value as an external comparison target;
- the positive `g/r` onsite-potential profile used by the diagnostic; its sign,
  normalization, and coupling to this fermion carrier are selected diagnostic
  inputs, not a derived gravitational bridge;
- `t=1` in the nearest-neighbor Hamiltonians, the `10^-6` SVD tolerance, the
  finite size grids, and the selected fit windows/forms;
- the SI constants (`G`, `c`, `l_P`, and `M_sun`) and benchmark masses used
  only in the frozen-star comparison table;
- the convention identifying the counted lattice boundary with the area
  comparator and the separately supplied `1/4` normalization in that table.

These are explicit external or conventional inputs to this diagnostic. The
four-axiom baseline is used only as the framework boundary against which those
inputs are disclosed.

## Open Gates

1. Derive or explicitly supply as a conditional a physical state selection and entropy
   observable for the intended black-hole carrier.
2. Prove the mixed-state and threshold-rank asymptotics, rather than selecting
   a finite fit family.
3. Derive the physical bridge from the lattice comparison to area in Planck
   units and to the Bekenstein-Hawking observable.

## Reproduction

```bash
python3 scripts/frontier_bh_entropy_derived.py
```

Expected current summary: `CHECKS PASSED: 4/4`. This is runner accounting for
the declared finite checks, not an independent audit verdict.
