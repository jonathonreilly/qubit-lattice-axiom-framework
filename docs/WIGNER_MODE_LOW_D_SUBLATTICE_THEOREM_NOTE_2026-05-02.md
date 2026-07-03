# Wigner Low-D Sublattice IR/Charge Compatibility Certificate

**Date:** 2026-05-02; audit-scope repair 2026-06-08
**Type:** bounded_theorem
**Source-side status:** bounded support; proposed for independent audit, not effective retained.
**Claim scope:** self-contained finite checks for charge-symmetric finite
Hamiltonians, Gibbs-state charge commutation, and low-dimensional lattice
IR-sum growth on coordinate sublattices of `Z^3`.
**Runner:** `scripts/wigner_mode_low_d_sublattice_check.py`

## Audit-Scope Repair

The previous note attempted to compose two cited authorities into a
Wigner-mode/no-SSB plus Noether-current theorem. Independent audit found that
the first citation does not contain the claimed retained no-SSB theorem in the
restricted packet, and that the order-parameter Ward/commutator normalization
bridge remains open.

This repaired row removes that load-bearing citation composition. The
source-side retained-eligible content is only the finite algebra and finite
IR-growth diagnostics that the runner computes directly.

## Statement

Let `Q` be a finite charge operator and `H` a finite Hamiltonian block-diagonal
in the eigenspaces of `Q`. Then the finite packet verifies:

1. `[Q,H]=0` for a generated nontrivial Hermitian block Hamiltonian.
2. The Gibbs state `rho_beta = exp(-beta H)/Tr exp(-beta H)` commutes with `Q`
   in the same finite model.
3. For the nearest-neighbor lattice dispersion
   `omega(k)=2 sum_j (1-cos k_j)`, the finite-volume averages
   `V^{-1} sum_{k != 0} 1/omega(k)` increase from `L=16` to `L=32` for
   `d=1` and `d=2`.
4. These finite facts are logically compatible with a future retained
   low-dimensional no-SSB bridge and with a future retained Noether-current
   bridge, but they do not prove either bridge.

## Runner Certificate

Current cached runner output:

```text
Test 1 ([Q, H] = 0 in symmetric H):            PASS
Test 2 ([Q, rho_beta] = 0):                    PASS
Test 3 (low-d lattice IR growth):              PASS
Test 4 (compatibility boundary):               PASS
OVERALL: PASS
```

The numerical IR values in the runner are:

```text
I_1(L=16) = 1.3281; I_1(L=32) = 2.6641
I_2(L=16) = 0.4899; I_2(L=32) = 0.6003
```

## Non-Claims

This row does not prove:

- finite-temperature continuous-symmetry no-SSB for `d <= 2`;
- order-parameter Ward/commutator normalization;
- a lattice Noether theorem beyond the finite charge-commutation model;
- integer charge quantization;
- absence of all gapless spectral modes;
- a layered-3D stability theorem;
- a model-specific magnetic phase diagram.

## Re-Audit Target

Independent audit should evaluate this as bounded finite algebra and IR-growth
support. A stronger Wigner-mode theorem requires a separate retained
finite-temperature no-SSB theorem plus the Ward/order-parameter bridge named by
the prior audit.
