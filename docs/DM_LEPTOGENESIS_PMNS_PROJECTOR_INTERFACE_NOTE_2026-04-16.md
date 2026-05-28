# DM Leptogenesis PMNS Projector Interface

**Claim type:** bounded_theorem
**Status:** support - raw algebraic interface; independent audit owns status
**Date:** 2026-04-16 (2026-05-25: raw-interface repair)
**Primary runner:** `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
**Status authority:** independent audit lane only.

## 2026-05-28 Science-Fix Re-Audit Scope

This row is narrowed to the raw pair-to-projector construction for simple
spectra and fixed eigenbasis output. Degenerate eigenspaces are explicitly
treated as an open invariance boundary unless the runner's degeneracy probe
says the compared quantity is basis-invariant. Re-audit should not read this
note as proving a physical PMNS projector map.

## Raw Pair-to-Projector Interface

This row is a raw-interface repair. Its claim is exactly the finite
linear-algebra interface below:

Given any two `3 x 3` positive-definite Hermitian matrices `(H_nu, H_e)`,
let

```text
H_nu = U_nu D_nu U_nu^dagger
H_e  = U_e  D_e  U_e^dagger
```

with unitary eigenvector matrices `U_nu` and `U_e`. Define

```text
U_pair = U_e^dagger U_nu,
P(alpha, i) = |U_pair(alpha, i)|^2.
```

Then:

1. `U_pair` is unitary.
2. `P = |U_pair|^2` is doubly stochastic: every row and every column
   sums to `1`.
3. `P` is invariant under independent eigenvector rephasings
   `U_nu -> U_nu D_nu_phase` and `U_e -> U_e D_e_phase`, with diagonal
   unitary phase matrices.

Those three statements are the entire retained-candidate content of
this row.

## Explicit Non-Claims

This row does not claim carrier authority.

This row does not claim physical N1 column selection.

This row does not compute or retain eta/eta_obs diagnostics.

This row does not import dm_leptogenesis_exact_common.

No new repo-wide axiom is introduced.

The result is a bounded algebraic interface for a supplied Hermitian
pair. It is not a physical leptogenesis theorem, not a PMNS pair law,
and not a selected-column theorem.

## Question

Once a lepton Hermitian pair is supplied, is the associated projector
packet intrinsic to that pair?

## Answer

Yes, in the bounded algebraic sense above. The matrix
`U_pair = U_e^dagger U_nu` is unitary because it is a product of
unitaries, and the entrywise squared magnitudes of a unitary matrix form
a doubly stochastic matrix. Independent phase choices of the eigenvector
columns multiply `U_pair` on the left and right by diagonal unitaries,
which do not change entrywise squared magnitudes.

## Proof

### 1. Unitarity

Since `U_e` and `U_nu` are unitary,

```text
U_pair U_pair^dagger
  = (U_e^dagger U_nu)(U_nu^dagger U_e)
  = U_e^dagger I U_e
  = I.
```

### 2. Doubly stochastic packet

For every column `i`,

```text
sum_alpha |U_pair(alpha, i)|^2 = || column_i(U_pair) ||^2 = 1.
```

For every row `alpha`,

```text
sum_i |U_pair(alpha, i)|^2 = || row_alpha(U_pair) ||^2 = 1.
```

Thus `P(alpha, i) = |U_pair(alpha, i)|^2` is doubly stochastic.

### 3. Rephasing invariance

If eigenvector columns are independently rephased,

```text
U_nu -> U_nu D_nu_phase,
U_e  -> U_e  D_e_phase,
```

then

```text
U_pair -> D_e_phase^dagger U_pair D_nu_phase.
```

Each entry is multiplied by a unit-modulus phase, so

```text
|U_pair(alpha, i)|^2
```

is unchanged.

## Consequence

The row closes only the pair-to-projector interface. Future physical
leptogenesis work still has to derive:

- the actual Hermitian-pair carrier from retained PMNS/neutrino
  machinery;
- the physical `N1` transport-column selection;
- any transport diagnostic or `eta/eta_obs` value.

Those are intentionally outside this repaired row.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_projector_interface.py
```

## Audit Repair Record

The previous source mixed a valid algebraic interface with diagnostic
transport readouts and explicit open physical authorities. The
2026-05-25 repair takes the narrow re-audit path: retain only the raw
pair-to-projector algebra, remove the transport helper import, and
exclude carrier/column-selection readings from the claim.
