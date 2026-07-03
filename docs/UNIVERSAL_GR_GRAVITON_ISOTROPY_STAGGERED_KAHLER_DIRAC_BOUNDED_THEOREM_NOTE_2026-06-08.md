# Staggered Kähler-Dirac Zener Anisotropy Diagnostic for the Finite-BZ Tensor Lane

**Date:** 2026-06-08
**Claim type:** bounded_theorem / finite-Brillouin-zone source certificate
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_graviton_isotropy_staggered.py`](../scripts/frontier_universal_gr_graviton_isotropy_staggered.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_graviton_isotropy_staggered.txt`](../logs/runner-cache/frontier_universal_gr_graviton_isotropy_staggered.txt)

## 2026-06-08 Audit-Boundary Repair

This repair narrows the row to the computation actually present in the packet.
The runner computes a finite-BZ Zener anisotropy diagnostic

```text
A = 2 C44 / (C11 - C12)
```

for a continuum control, a naive lattice Dirac control, and the exact `16x16`
staggered Kähler-Dirac hypercube block. The result is:

- continuum control: `A` is near `1`;
- naive lattice Dirac control: `A approx 2.1`, an O(1) anisotropy;
- staggered Kähler-Dirac block: `A approx 0.97`, a few-percent residual and a
  large improvement over the naive control.

The packet does **not** prove that the implemented non-conserved vertex is the
W-native induced-graviton stiffness. It also does **not** prove exact
`E_g/T_2g` equality, the conserved staggered stress vertex, the continuum
`a->0` extrapolation, or a physical spin-2 graviton isotropy theorem.

## Theorem (Bounded Finite-BZ Diagnostic)

- **T1:** the continuum Dirac control is isotropic to the checked tolerance.
- **T2:** the naive lattice Dirac control is strongly anisotropic, and that
  anisotropy is stable as the sampled `k0` changes.
- **T3:** the exact staggered Kähler-Dirac operator has scalar spectrum
  `Delta(P)=m^2+sum_mu sin^2(P_mu/2)` with the expected taste multiplicity.
- **T4:** the staggered finite-BZ Zener diagnostic is close to isotropic:
  `A approx 0.97`, N-stable on the tested grids, and mass-robust.
- **T5:** the staggered diagnostic has a few-percent residual while the naive
  diagnostic has an O(1) residual.

`TOTAL: PASS=7 FAIL=0`.

## What This Establishes

The row establishes bounded finite-scheme support for the claim that the
staggered Kähler-Dirac block has a much better tensor-channel Zener diagnostic
than the naive Dirac control. It is a useful positive clue for the universal-GR
lane because the framework matter packet is staggered/Kähler-Dirac rather than
naive-doubler Dirac.

## What Remains Open

- The conserved staggered stress vertex adapted to the `16x16` block.
- The W metric-Hessian/contact-term bridge.
- The continuum `a->0` extrapolation of the few-percent residual.
- Exact `E_g/T_2g` equality or a physical spin-2 isotropy theorem.
- Induced Newton magnitude.

## Relation to Inventory

The staggered operator and its SO(4) continuum behavior are supported by the
staggered/SO(4) matter-sector notes. This row may be used only as bounded
finite-scheme evidence that the staggered packet improves the tensor-channel
Zener diagnostic. It does not close the downstream W-native induced-gravity
lane by itself.

## Honest Auditor Read

The source is narrow: it computes a Zener anisotropy diagnostic, verifies the
staggered scalar spectrum, compares continuum/naive/staggered controls, and
records the few-percent residual. It does not ask audit to accept the missing
conserved vertex, metric-Hessian bridge, continuum extrapolation, or physical
spin-2 isotropy claim.
