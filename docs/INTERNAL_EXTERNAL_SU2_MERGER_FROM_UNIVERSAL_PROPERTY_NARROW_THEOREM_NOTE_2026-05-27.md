# Internal-External SU(2) Operator Identification

**Date:** 2026-05-27
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/internal_external_su2_merger_runner.py`](../scripts/internal_external_su2_merger_runner.py)

## Claim

On the repo-baseline one-qubit operator algebra, read in the repo's standard
physical `Cl(3,0)` language, the internal `su(2)` spin generators on
the per-site Hilbert space and the infinitesimal `Spin(3)` generators
coming from the Clifford universal property are the same operators.

Concretely, in the canonical Pauli realization
`gamma_i = sigma_i` on `H_x = C^2`, define

```text
S_i = sigma_i / 2
B_i = (1/2) gamma_j gamma_k,  for (i,j,k) cyclic in (1,2,3).
```

Then

```text
B_i = i S_i,
[B_i, B_j] = - epsilon_ijk B_k,
[S_i, S_j] = i epsilon_ijk S_k.
```

The same Pauli matrices also implement the infinitesimal spatial
`Spin(3)` action on the Clifford generators: for the row-vector
convention `phi_R(gamma_i) = sum_j R_ij gamma_j`, the spin lift
`U(R)` satisfies

```text
U(R) sigma_i U(R)^* = sum_j R_ij sigma_j
```

for the proper cubic rotations checked by the runner, and the
infinitesimal generators are exactly `S_i = sigma_i / 2`.

The bounded theorem is therefore an operator-level identification:
the two `su(2)` descriptions are not separate framework primitives.
They are the same generator data in the selected Pauli realization.

## Load-bearing Inputs

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) -
  current qubit-on-`Z^3` framework memo; records the one-qubit
  operator algebra equivalently as `M_2(C)` and physical `Cl(3,0)`.
- [`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) -
  two-class real-algebra classification and the selected Pauli realization
  on `C^2`.
- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md) -
  retained per-site `j = 1/2` `su(2)` representation with
  `S_i = sigma_i / 2`.
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md) -
  retained `Cl(3,0) tensor_R C ~= M_2(C) oplus M_2(C)` split.
- [`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md) -
  retained two-dimensional per-site Hilbert carrier.

## Input Boundary

This row does not add an axiom. It uses the repo's existing physical
`Cl(3,0)` local-algebra reading and the standard finite-dimensional
Clifford/Spin conventions:

- the universal property sends orthogonal maps on the generating
  three-dimensional Euclidean Clifford space to algebra automorphisms;
- bivectors generate the spin Lie algebra;
- proper rotations have the usual `Spin(3) -> SO(3)` double-cover
  lift on the Pauli module.

The runner checks the exact Pauli identities, the 24 proper cubic
unitary lifts, the 24 improper cubic signed generator actions, and the
infinitesimal generator coincidence. The improper checks are real
Clifford-generator actions, not ordinary complex-linear unitary
conjugations on `C^2`. The runner does not attempt to prove every
textbook fact about arbitrary Clifford modules.

## What This Does Not Claim

- It does not derive the `Z^3` site lattice or discrete translations.
- It does not identify cubic lattice primitive translation axes.
- It does not introduce or approve any new axiom, premise, or retained
  status.
- It does not change any numerical lane or scale-setting lane.
- It is not a Coleman-Mandula or Haag-Lopuszanski-Sohnius claim.

## Runner Certificate

The runner performs exact `sympy` checks over the Pauli realization and
the cubic signed-permutation group:

| Section | Checked content | Passes |
|---|---|---:|
| 1 | Pauli anticommutation and pseudoscalar sanity | 10 |
| 2 | Bivector closure and `S_i = -i B_i` | 24 |
| 3 | `O_h` action on bivectors via the cofactor representation | 146 |
| 4 | proper-cubic `SO(3) -> SU(2)` lift | 25 |
| 5 | infinitesimal generator coincidence | 12 |
| 6 | proper cubic lifts and improper signed generator actions | 49 |
| 7 | generator-frame consistency between spin and bivector flows | 7 |
| **Total** | | **273** |

Run:

```bash
python3 scripts/internal_external_su2_merger_runner.py
```

Expected result:

```text
TOTAL: PASS=273 FAIL=0
```

## Reading Rule

The safe downstream use is narrow: a row may cite this theorem when it
needs the per-site Pauli `su(2)` spin generators and the Clifford
`Spin(3)` infinitesimal generators to be the same operator triple on
`C^2`. It may not cite this theorem to obtain lattice discreteness,
translation primitives, cubic Bravais structure, or a physical scale.
