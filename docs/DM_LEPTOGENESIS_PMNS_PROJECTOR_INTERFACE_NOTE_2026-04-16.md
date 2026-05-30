# DM Leptogenesis PMNS Projector Interface

**Claim type:** bounded_theorem
**Status:** support - raw algebraic interface; independent audit owns status
**Date:** 2026-04-16 (2026-05-25: raw-interface repair; 2026-05-28: intrinsic
claim restricted to simple spectra per audit verdict; 2026-05-29:
eigenvalue-label convention made explicit).
**Primary runner:** `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`

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

## 2026-05-29 Audit Repair (ordered labels for simple spectra)

The later audit feedback found one remaining ambiguity:

> *"The raw fixed-eigenvector algebra closes, but the note also claims a
> simple-spectrum intrinsic-to-the-pair projector packet without specifying
> the eigenvalue label/order convention needed to fix rows and columns.
> Simple spectra leave independent row/column permutation freedom."*

This repair adopts the explicit convention already used by the runner:
eigenvectors are labeled by **ascending eigenvalue order** for both
`H_nu` and `H_e`. With simple spectra and this order convention, the
eigenvector matrices are determined by the Hermitian pair up to independent
diagonal phases, and those phases do not change `|U_e^dagger U_nu|^2`.

Without this order convention, the unordered pair still determines the same
projector only **up to independent row and column permutations**. The ordered
`3 x 3` packet is therefore not claimed unless the ascending-eigenvalue
label convention is part of the input surface.

## Raw Pair-to-Projector Interface

This row is a raw-interface repair. Its claim is exactly the finite
linear-algebra interface below:

Given any two `3 x 3` positive-definite Hermitian matrices `(H_nu, H_e)`,
let the eigenvalues be simple when the pair itself is asked to determine an
ordered packet, and label the eigenvectors by ascending eigenvalue order:

```text
H_nu = U_nu D_nu U_nu^dagger
H_e  = U_e  D_e  U_e^dagger
```

with unitary eigenvector matrices `U_nu` and `U_e`. For fixed supplied
eigenvector matrices the same algebra applies without the simple-spectrum
or ordering hypothesis. Define

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
rotations change it), as the runner's Part 2c exhibits. The
intrinsic-to-the-pair reading is restricted to simple (non-degenerate)
spectra.

This row does not claim an ordered projector packet without an eigenvalue
label convention. Without ascending-eigenvalue labels, the pair determines
the packet only up to independent row and column permutations.

No new repo-wide axiom is introduced.

The result is a bounded algebraic interface for a supplied Hermitian
pair. It is not a physical leptogenesis theorem, not a PMNS pair law,
and not a selected-column theorem.

## Question

Once a lepton Hermitian pair is supplied, is the associated projector
packet intrinsic to that pair?

## Answer

Yes for **simple (non-degenerate) spectra with ascending-eigenvalue labels
for both matrices**, in the bounded algebraic sense above; **no for
degenerate spectra** (see the 2026-05-28 repair header — a degenerate
eigenspace admits non-diagonal rotations that change `|U_pair|^2`). Without
the ordering convention, the intrinsic packet is defined only up to
independent row and column permutations. For a fixed choice of eigenvector
matrices the three statements hold unconditionally. The matrix
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

### 4. Simple-spectrum intrinsic reading with ordered labels

For a Hermitian matrix with simple spectrum, each eigenspace is
one-dimensional. After eigenvalues are labeled in ascending order, another
unitary diagonalizer with the same ordered labels can only multiply each
eigenvector by a unit phase. Thus two allowed ordered diagonalizer choices
have the form

```text
U_nu' = U_nu D_nu_phase,
U_e'  = U_e  D_e_phase.
```

By the rephasing calculation above,

```text
|U_e'^dagger U_nu'|^2 = |D_e_phase^dagger U_e^dagger U_nu D_nu_phase|^2
                      = |U_e^dagger U_nu|^2.
```

If the ascending-eigenvalue labels are dropped, independent column
permutations of `U_nu` and `U_e` remain available. They act on the packet
as independent column and row permutations, so the ordered `3 x 3` matrix is
not intrinsic without the label convention.

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
