# UV Gauge-to-Yukawa Bridge: Perturbative vs Strong-Coupling Coefficients

**Date:** 2026-04-16 (2026-05-29 scope repair).
**Type:** bounded_theorem.
**Primary runner:** `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py`.
**Status authority:** independent audit lane only.

## 2026-05-29 Scope Repair

The audit blocker was not the finite coefficient algebra. It was the stronger
selection claim that the tadpole-improved canonical surface proves the
perturbative coefficient governs and excludes the strong-coupling coefficient.
The audit found that the packet does not supply a retained expansion-domain
or selector theorem for that step.

This repair removes the governing-coefficient selection claim from the
load-bearing surface. The row now preserves only the exact bounded algebraic
support:

- `C_pert = 1/(2 N_c)` from the SU(`N_c`) Fierz identity.
- `C_strong = 1/N_c^2` from the leading one-link strong-coupling Haar
  contraction.
- The coefficients are distinct at `N_c = 3`: `1/6` versus `1/9`.
- The Dirac Fierz scalar and pseudoscalar channels are nonzero and the tensor
  channel vanishes in the checked vector-vector decomposition.
- The unit scalar-singlet matrix element gives the exact `H_unit` overlap
  `1/sqrt(6)` on the `Q_L = (2,3)` block.

The row does **not** claim that the canonical tadpole-improved surface selects
the perturbative expansion, proves convergence, closes plaquette or `u_0`
authority, closes `g_bare`, closes staggered-Dirac realization, or supplies
shared tadpole transport. Those are future bridge/selector problems.

No new axiom is introduced. No observed value or fitted selector is
load-bearing.

## Claim Scope

Let `N_c = 3` and `N_iso = 2` be the retained bounded representation inputs
used by the runner. The in-scope theorem is the finite coefficient packet:

1. The SU(`N_c`) generator normalization

   ```text
   Tr(T^A T^B) = (1/2) delta_AB
   ```

   implies the Fierz identity

   ```text
   sum_A T^A_ab T^A_cd
     = (1/2)(delta_ad delta_bc - (1/N_c) delta_ab delta_cd).
   ```

   Hence the color-singlet perturbative coefficient magnitude is

   ```text
   C_pert = 1/(2 N_c).
   ```

2. The leading one-link Haar contraction

   ```text
   integral dU U_ab U^dag_cd = (1/N_c) delta_ad delta_bc
   ```

   gives the corresponding leading strong-coupling color-singlet coefficient

   ```text
   C_strong = 1/N_c^2.
   ```

3. At `N_c = 3`, these are exactly

   ```text
   C_pert = 1/6,
   C_strong = 1/9.
   ```

   Their difference records that the two expansions are different finite
   coefficient calculations. It does not decide which expansion governs a
   physical surface.

4. On the `Q_L = (2,3)` scalar-singlet block, the unit-normalized singlet has
   uniform component overlap

   ```text
   1/sqrt(N_c N_iso) = 1/sqrt(6).
   ```

5. Historical NLO and canonical-surface arithmetic from the shared Ward runner
   are context only. They do not certify an expansion-domain theorem or a
   precision claim for this row.

## Explicit Non-Claims

This row does not select `C_pert` over `C_strong` as the governing coefficient
on the canonical tadpole-improved surface.

This row does not prove perturbative convergence or strong-coupling
non-convergence for the framework surface.

This row does not derive the plaquette value, `u_0`, `alpha_LM`, `g_bare`,
staggered-Dirac realization, shared tadpole transport, or the full top-Yukawa
readout.

This row does not promote `YT_WARD_IDENTITY_DERIVATION_THEOREM.md`; it is a
bounded coefficient support/comparison note.

## Proof Sketch

The perturbative coefficient is an immediate component of the SU(`N_c`) Fierz
identity. The primary runner constructs the Gell-Mann generators for `N_c=3`,
verifies the normalization and all index entries of the Fierz identity, and
extracts the color-singlet coefficient `1/(2 N_c)`.

The strong-coupling coefficient is the leading one-link Haar contraction. The
primary runner samples SU(3) Haar matrices as a numerical witness for the
exact contraction and records the algebraic result `1/N_c^2`.

The `H_unit` overlap is finite-dimensional Hilbert-space algebra. The
unit-norm singlet on a six-dimensional `Q_L` block has each diagonal basis
component equal to `1/sqrt(6)`, and the runner checks all six components.

## Command

```bash
python3 scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py
```

## Future Bridge Needed

To recover the stronger governing-coefficient statement, a separate theorem
would need to prove the expansion-domain/selector surface: why the retained
framework inputs put the relevant coefficient in the tadpole-improved
perturbative domain rather than the strong-coupling character domain, with the
plaquette/`u_0`, `g_bare`, staggered-Dirac, and shared tadpole-transport
dependencies explicitly closed or admitted.
