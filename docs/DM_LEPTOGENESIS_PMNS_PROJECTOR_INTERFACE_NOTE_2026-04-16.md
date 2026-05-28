# DM Leptogenesis PMNS Projector Interface

**Type:** bounded_theorem
**Status:** support - raw algebraic interface; independent audit owns status
**Date:** 2026-04-16 (2026-05-25: raw-interface repair; 2026-05-28: intrinsic
claim restricted to simple spectra per audit verdict).
**Primary runner:** `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (intrinsic claim restricted to simple spectra)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The stated unitarity, row/column-sum, and diagonal-rephasing
> invariance algebra closes for a fixed choice of eigenvector matrices.
> The row does not close as an intrinsic pair-to-projector theorem for
> arbitrary positive-definite Hermitian pairs because degenerate spectra
> allow non-diagonal unitary rotations within eigenspaces; those
> rotations can change |U_e^dagger U_nu|^2."*

The auditor is correct. The three load-bearing statements (unitarity,
double-stochasticity, diagonal-rephasing invariance) all hold for a
**fixed** choice of eigenvector matrices. But the §"Question/Answer"
framing that the projector packet is **"intrinsic to the pair"** is only
valid for **simple (non-degenerate) spectra**, where the eigenbasis is
unique up to column phases. For a **degenerate** Hermitian matrix, the
degenerate eigenspace admits a continuum of orthonormal bases related by
non-diagonal U(k) rotations, and those rotations **change** `|U_pair|^2`
— so the projector is NOT intrinsic to the pair in the degenerate case.

Repair (the auditor's "narrow to simple spectra" path):

- The **intrinsic-to-the-pair** statement is restricted to **simple
  (non-degenerate) spectra**. For fixed supplied eigenvector matrices the
  three algebraic statements hold unconditionally; for the *pair* to
  determine the projector intrinsically, both `H_nu` and `H_e` must have
  simple spectra.
- The runner adds Part 2b: an explicit **degenerate Hermitian pair** with
  a non-diagonal eigenspace rotation, demonstrating `||P1 − P2|| > 1e-3`
  for two valid eigenbases of the same pair — confirming the restriction
  is necessary.
- This is recorded as an explicit non-claim below.

No new axioms, imports, or runners-as-dependencies. The load-bearing
algebra is unchanged; only the intrinsic-to-the-pair reading is scoped to
simple spectra.

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

This row does not claim the projector is intrinsic to the pair for
**degenerate** spectra: for a degenerate Hermitian matrix the
projector `|U_pair|^2` is basis-dependent (non-diagonal eigenspace
rotations change it), as the runner's Part 2b exhibits. The
intrinsic-to-the-pair reading is restricted to simple (non-degenerate)
spectra.

No new repo-wide axiom is introduced.

The result is a bounded algebraic interface for a supplied Hermitian
pair. It is not a physical leptogenesis theorem, not a PMNS pair law,
and not a selected-column theorem.

## Question

Once a lepton Hermitian pair is supplied, is the associated projector
packet intrinsic to that pair?

## Answer

Yes for **simple (non-degenerate) spectra**, in the bounded algebraic
sense above; **no for degenerate spectra** (see the 2026-05-28 repair
header — a degenerate eigenspace admits non-diagonal rotations that
change `|U_pair|^2`). For a fixed choice of eigenvector matrices the
three statements hold unconditionally. The matrix
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
