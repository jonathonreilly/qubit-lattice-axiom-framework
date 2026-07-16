# UV Gauge-to-Yukawa Bridge: Perturbative vs Strong-Coupling Coefficients

**Date:** 2026-04-16 (2026-05-29 scope repair; 2026-07-16 singlet-projector repair).
**Type:** bounded_theorem.
**Primary runner:** `scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py`.

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

Fix `N_c = 3` and `N_iso = 2` as representation conditions for this bounded
packet. This row does not derive their physical selection. The in-scope theorem
is the finite coefficient packet:

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

2. Use the pair-space ordering `(ab);(cd)`, with `a,c` fundamental row
   indices, `b,d` anti-fundamental/column indices, and

   ```text
   U^dag_cd = (U_dc)^*.
   ```

   The exact normalized one-link Haar tensor is

   ```text
   H_(ab;cd)
     = integral dU U_ab U^dag_cd
     = (1/N_c) delta_ad delta_bc.
   ```

   On the Hilbert-Schmidt pair space, define the normalized color-singlet
   vector and its rank-one projector by

   ```text
   S_ab = delta_ab / sqrt(N_c),

   Pi_1(ab;cd) = S_ab S_cd^*
                = delta_ab delta_cd / N_c.
   ```

   Thus `sum_ab S_ab^* S_ab = 1`, while `Pi_1^dag = Pi_1`,
   `Pi_1^2 = Pi_1`, `rank(Pi_1) = 1`, and
   `Tr(Pi_1) = ||Pi_1||_HS^2 = 1`.

   The complete singlet-channel sandwich is

   ```text
   (Pi_1 H Pi_1)_(ab;cd)
     = sum_efgh
         [delta_ab delta_ef / N_c]
         [delta_eh delta_fg / N_c]
         [delta_gh delta_cd / N_c]
     = delta_ab delta_cd / N_c^2
     = (1/N_c) Pi_1(ab;cd).
   ```

   Equivalently, for the rank-four Hilbert-Schmidt inner product

   ```text
   <A,B>_HS = sum_abcd A_(ab;cd)^* B_(ab;cd),
   ```

   the normalized-projector coefficient is

   ```text
   alpha_1
     = <Pi_1,H>_HS / <Pi_1,Pi_1>_HS
     = [(1/N_c^2) sum_abcd
          delta_ab delta_cd delta_ad delta_bc] / 1
     = 1/N_c.
   ```

   There are exactly `N_c` nonzero terms in the displayed sum. Therefore the
   singlet tensor component is

   ```text
   H^(1)_(ab;cd)
     = alpha_1 Pi_1(ab;cd)
     = delta_ab delta_cd / N_c^2.
   ```

   If `D_(ab;cd) = delta_ab delta_cd` denotes the unnormalized singlet tensor,
   then `||D||_HS^2 = N_c^2` and

   ```text
   <D,H>_HS = 1,
   C_strong = <D,H>_HS / <D,D>_HS = 1/N_c^2.
   ```

   Hence `1/N_c` is the coefficient of the normalized projector `Pi_1`, while
   `C_strong = 1/N_c^2` is the coefficient of the unnormalized tensor
   `delta_ab delta_cd`. These are different coefficient conventions for the
   same reconstructed singlet component and must not be interchanged.

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

For the strong-coupling coefficient, the primary runner instantiates the
ordered pair basis, `S`, `Pi_1`, `H`, and the unnormalized tensor `D` as finite
arrays. It verifies the singlet normalization, projector Hermiticity,
idempotence, rank, trace, and Hilbert-Schmidt norm; evaluates both
`Pi_1 H Pi_1` and the independent Hilbert-Schmidt coefficient contractions;
and reconstructs the same singlet tensor component in the normalized and
unnormalized conventions. The resulting exact coefficients are `1/N_c` and
`1/N_c^2`, respectively, with `C_strong = 1/9` at `N_c = 3`.

The runner retains the SU(3) Haar sample only as a numerical witness for the
starting tensor identity. It also includes hostile controls that fail when one
`1/sqrt(N_c)` projector factor is omitted, when `1/N_c` is misread as the
coefficient of `delta_ab delta_cd`, or when an index permutation changes the
projected channel.

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
dependencies explicitly closed or left as named open conditions.
