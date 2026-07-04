# Theta Mass Action-Level Determinant Entry Exact-Support Split

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** exact-support source-side split; independent audit required before
any effective-status change. This note does not retire theta, does not derive
W2 physical registrability, does not select the physical action surface, does
not edit any Tier-A registry, axiom, primitive, audit verdict, or publication
surface, and does not claim anything about the gauge-side winding residual.
**Primary runner:**
[`scripts/theta_mass_action_determinant_entry_exact_support_split_2026_07_04.py`](../scripts/theta_mass_action_determinant_entry_exact_support_split_2026_07_04.py)

## Purpose

The theta mass-side bridge has two physical premises separated by the current
source stack:

1. **W2 physical registrability** -- the physical mass-surface readout context
   satisfies Record registrability and uses the determinant datum as the
   scalar channel.
2. **Action-level determinant entry** -- on the relevant mass-action surface,
   the vacuum-weight dependence on the mass-orientation datum enters through
   the Gaussian determinant `det(D + M)`, so the orientation-sensitive
   partition-level mass datum is `arg det(D + M)`.

Block25 isolated (1) as not derivable from Record or the realized-state
primitive alone. This note isolates the exact algebra for (2) on a supplied
finite Gaussian bilinear matter surface. It closes the supplied-surface
determinant-entry algebra, not the physical-selection premise.

## Supplied Surface

Fix a finite fermionic Gaussian bilinear action

```text
S_K = sum_{i,j} bar(psi_i) K_ij psi_j
```

with one Grassmann pair per finite mode. The action matrix `K` may be
`D + M` on a supplied mass surface, but this note does not derive that surface.
It assumes only the finite Gaussian bilinear form and computes its
partition-level vacuum weight.

## Exact Split Theorem

On the supplied finite Gaussian bilinear surface:

1. The Berezin integral is exactly first power:

   ```text
   Z(K) = int exp(S_K) Dbar(psi) Dpsi = det K.
   ```

   No determinant identity is assumed by the runner; it expands the exterior
   algebra explicitly and compares to the signed permutation determinant.
2. For independent block sums, `K = K_1 direct_sum K_2`,

   ```text
   Z(K_1 direct_sum K_2) = Z(K_1) Z(K_2),
   arg Z(K_1 direct_sum K_2) = arg Z(K_1) + arg Z(K_2) mod 2 pi.
   ```

   Thus the partition-level mass-orientation datum on this surface is the
   additive determinant phase `arg det K`.
3. If K/CPT conjugation acts on the supplied surface by
   `K(alpha) -> conj(K(alpha)) = K(-alpha)`, then
   `Z(K(-alpha)) = conj Z(K(alpha))`, so the action-level phase entry is
   paired by `alpha -> -alpha`.
4. There is no additional nonmultiplicative **partition-level matter phase**
   inside the supplied Gaussian bilinear class, because the whole vacuum weight
   is the single scalar `det K`.

This is the exact action-entry algebra needed by the determinant-readout route.
It must still be composed with a separate W2 theorem or supplied W2 interface
before it can act as a theta-retirement authority.

## Hostile Guards

The result is deliberately not a theorem about every possible observable or
every possible action.

### Non-Gaussian matter is outside the theorem

For two Grassmann pairs, adding the quartic term

```text
g * bar(psi_1) psi_1 bar(psi_2) psi_2
```

changes the exact partition weight from

```text
det K
```

to

```text
det K + g
```

with the sign convention used by the runner. That witness is not a failure of
the theorem; it is the boundary. The determinant-entry split covers the
supplied Gaussian bilinear vacuum weight only.

### Source and insertion observables are outside the theorem

Fermion-source correlators can depend on entries of `K^{-1}` and therefore on
more than `det K`. The runner exhibits two diagonal matrices with the same
determinant and different inverse entries. This note covers the
vacuum-weight phase datum used by the theta mass-side determinant route, not
the full source/insertion observable algebra.

### W2 is not supplied here

Record additivity and orbit constancy erase determinant phase only after the
determinant datum is the Record-registrable scalar channel. This note supplies
the finite Gaussian determinant-entry algebra; it does not prove that the
physical readout context is W2 Record-registrable.

## Relation To Existing Notes

- [`THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  names W2 physical registrability and the action-level `theta_eff`
  determinant-entry premise as separate supplied conditions. This note splits
  out the exact supplied-Gaussian algebra for the second condition.
- [`THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  gives a broader bilinear realization packet with gauge-background tests and
  K-real boundaries. This split is smaller: finite Gaussian determinant entry,
  block multiplication, K/CPT conjugation of the determinant weight, and
  explicit out-of-scope witnesses.
- [`THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md`](THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md)
  shows that W2 is not forced by the current axiom/primitive surface. This
  note does not repair that no-go.

## What Moves

| Surface | Movement |
|---|---|
| Supplied Gaussian bilinear action-entry algebra | split into a small exact-support artifact |
| W2 physical registrability | unchanged; still open |
| Physical action-surface selection | unchanged; still supplied/open |
| K-real physicalization | unchanged |
| Gauge-side winding | unchanged |
| Tier-A registry | unchanged |

## Remaining Live Routes

1. Derive or explicitly approve W2 physical registrability.
2. Derive that the physical mass action really lies on this supplied Gaussian
   bilinear determinant-entry surface.
3. Audit the determinant algebra rows under fresh-context discipline.
4. Derive K-real physicalization for the shared theta/AC mass-side structure.
5. Attack theta(a)'s gauge-side winding residual separately.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_mass_action_determinant_entry_exact_support_split_2026_07_04.py
```

Expected close: `FAIL=0`.
