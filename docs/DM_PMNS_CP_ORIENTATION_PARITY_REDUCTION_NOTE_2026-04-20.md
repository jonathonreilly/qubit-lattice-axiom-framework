# DM PMNS CP-Orientation Parity Reduction

**Date:** 2026-04-20  
**Lane:** DM A-BCC sigma-chain / open imports `I12` and `I5`  
**Type:** open_gate
**Status:** conditional parity algebra and a finite supplied three-point diagnostic;
physical row/source selection and `I12` remain open.
**Primary runner:**
`scripts/frontier_dm_pmns_cp_orientation_parity_reduction_2026_04_20.py`

The former supersession statement that `I12` was closed by the upper-octant
source-cubic note is withdrawn. Its current scope is a supplied-bank comparison,
not a physical selector or complete chamber census. The
[upper-octant selector packet](DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md)
is historical context; its full proof is not independently established here.
This does not refute a possible future proof of those claims.

---

## 0. Question

For the supplied three-point bank labeled

```text
{Basin 1, Basin 2, Basin X},
```

what is the exact remaining difference between:

- source-side CP orientation on the DM Hermitian family, and
- the physical PMNS CP sign / `sigma_hier` choice?

## 1. Bottom line

For a fixed Hermitian matrix and its specified eigenbasis, the row-permutation sign is a parity bit. This does not establish that physical selection has only that missing premise.

Define the source cubic orientation

```text
I_src(H) := Im(H_12 H_23 H_31).
```

For the ascending-eigenvalue basis `V` of `H`, with
`lambda_1 < lambda_2 < lambda_3`, one has the exact identity

```text
J_basis
= Im(V_11 V_22 V_12^* V_21^*)
= I_src(H) / ((lambda_1 - lambda_2)(lambda_2 - lambda_3)(lambda_3 - lambda_1)).
```

If `P_sigma = rowperm_sigma(V)`, then

```text
J_sigma = parity(sigma) * J_basis.
```

For these defined matrices and labels, the computed Jarlskog sign differs by
`parity(sigma_hier)`. Identifying those labels and this matrix with a physical
PMNS source remains an additional premise.

That means:

1. the source family already carries an exact CP-oriented cubic scalar;
2. source-side CP-odd data by themselves are still blind to the
   `mu <-> tau` relabeling;
3. a parity / charged-doublet label law is one missing physical premise;
   source selection, complete-domain claims and target provenance remain open.

## 2. Theorem

**Theorem (source cubic parity reduction).** At the supplied points labeled

```text
Basin 1, Basin 2, Basin X,
```

let `H` be Hermitian with simple spectrum, `V` a unitary eigenbasis with the
fixed ascending column ordering, and
`P_sigma` any row permutation of `V`. Then:

1. `I_src(H) = Im(H_12 H_23 H_31)` is an exact source-side CP-oriented scalar;
2. the ascending-basis Jarlskog is exactly

   ```text
   J_basis = I_src(H) / Delta,
   Delta := (lambda_1 - lambda_2)(lambda_2 - lambda_3)(lambda_3 - lambda_1) > 0;
   ```

3. for any row permutation `sigma`,

   ```text
   J_sigma = parity(sigma) * I_src(H) / Delta;
   ```

4. at the same supplied Hermitian `H_pin`, the two compared row permutations
   `(2,1,0)` and `(2,0,1)` give opposite Jarlskog signs when nonzero, while sharing
   the same source cubic orientation.

Therefore no source-side CP-odd scalar law of this cubic orientation type can
distinguish these two row labels at a fixed `H` by itself. A physical
charged-doublet labeling law remains open; this is not exhaustion of all other
physical proof obligations.

### Proof

The identity

```text
Im(H_12 H_23 H_31) = J_basis * Delta
```

is the standard one-Hermitian Jarlskog bridge in the charged-lepton diagonal
basis. Since the runner orders eigenvalues ascending,

```text
Delta = (lambda_1 - lambda_2)(lambda_2 - lambda_3)(lambda_3 - lambda_1) > 0.
```

So `J_basis = I_src / Delta`.

A row permutation multiplies the Jarlskog by the sign of that permutation, so
`J_sigma = parity(sigma) J_basis`. Combining the two gives the displayed
formula.

At the supplied pin, `(2,1,0)` and `(2,0,1)` differ by one `mu <-> tau`
transposition, hence have opposite parity, hence opposite CP sign, while
`I_src(H_pin)` is unchanged because `H_pin` itself is unchanged.

QED.

## 3. Chamber sign table

On the three supplied decimal points (not an exact or complete chamber census):

| Root | `I_src(H)` | `J_(2,1,0)` | `J_(2,0,1)` |
|---|---:|---:|---:|
| Basin 1 | `+0.30356` | `−0.03275` | `+0.03275` |
| Basin 2 | `−225.76` | `+0.01839` | `−0.01839` |
| Basin X | `−99.77` | `+0.01389` | `−0.01389` |

So:

- on the odd branch `sigma = (2,1,0)`, the stipulated source filter
  `I_src > 0` selects Basin 1 uniquely;
- on the even branch `sigma = (2,0,1)`, the same Basin 1 point still has `I_src > 0`: source cubic depends on H, not row parity. No inference excluding all even-label points follows from this table.

This is a finite conditional comparison: within the supplied bank the
positive source-cubic filter keeps Basin 1. With the specified odd row label,
the computed phase sign is negative. Neither the filter nor the physical
labeling/source is derived here.

## 4. Consequence for `I12` and `I5`

This does not close `I12` outright. It does sharpen it substantially.

Conditional invariance at a fixed supplied H:

- any quantity of the same fixed H alone cannot distinguish its row labelings;
- the remaining sign ambiguity is **not** in the source cubic orientation.

What remains:

- a parity / charged-doublet label law telling us whether the physical branch
  is `sigma = (2,1,0)` or `sigma = (2,0,1)`.

For `I5`, row labeling is one missing premise; this diagnostic does not exhaust the physical derivation.
The angle triple itself remains observational on this branch.

## 5. Honest verdict

This note supplies a real theory gain:

- source-side CP orientation is exact,
- chamber completeness is not established by this source packet,
- physical parity, source selection and global coverage remain open.

One named open `I12` / `I5` obligation is:

```text
derive the charge-sign / hierarchy-parity map on the surviving Z_3 doublet.
```

## 6. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_cp_orientation_parity_reduction_2026_04_20.py
```

Historical numerical tally (fresh capture pending):

```text
PASS=16  FAIL=0
```

## Recovery and execution boundary

Complete original arguments, including the former exact/physical claims, are
recoverable at `a8151fb8e39df04925316bedb745a0aa4f36e333` and in the repair
evidence. No historical result is restamped. The runner checks finite supplied
values, not an analytic proof or physical closure. Its numerical predicates and
thresholds are unchanged. The former even-branch prose contradicted its own
source-invariant table; that inference is withdrawn, not converted into a new
physical exclusion.
