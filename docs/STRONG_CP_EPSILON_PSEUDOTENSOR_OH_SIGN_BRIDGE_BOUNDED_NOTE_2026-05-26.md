# Strong-CP Epsilon-Pseudotensor O_h Sign Bridge -- Bounded Note

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/strong_cp_epsilon_pseudotensor_oh_sign_runner.py`](../scripts/strong_cp_epsilon_pseudotensor_oh_sign_runner.py)

## Audit Context

This note supplies a narrow structural bridge for proposed strong-CP
work. It does not introduce a new axiom, admitted premise, or governance
convention. Its job is to separate a checked algebraic sign law from the
larger unsolved question of which action-class terms the framework
admits.

The input from
[`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md)
is that the cubic point group `O_h` acts on the one-qubit operator
algebra over the `Z^3` spatial substrate with pseudoscalar determinant
character. This note checks the companion lattice-gauge fact: the
four-dimensional epsilon contraction with one Euclidean-time index is
determinant-odd under spatial `O_h`.

## Claim

Let `O_h` act on the three spatial axes by signed permutation matrices
and leave the Euclidean-time direction fixed.

1. **Wilson plaquette invariance.** If gauge links transform by this
   signed-permutation action on oriented spatial links, the Wilson
   plaquette action
   ```text
   S_W[U] = -(beta/N_c) sum_P Re tr(U_P)
   ```
   is invariant. Orientation reversal sends a plaquette holonomy to its
   adjoint, and `Re tr(U_P^\dagger) = Re tr(U_P)`.

2. **Epsilon sign law.** The spatial Levi-Civita tensor satisfies
   ```text
   R_{ia} R_{jb} R_{kc} epsilon_{abc}
     = det(R) epsilon_{ijk}
   ```
   for every signed permutation `R in O_h`.

3. **Rank-two tensor consequence.** For any antisymmetric field-strength
   object `F_{mu nu}` whose components transform as a rank-two tensor
   under the same spatial `O_h` action,
   ```text
   Q[F] = epsilon^{ijk} F_{0i} F_{jk}
   ```
   transforms as
   ```text
   Q[R.F] = det(R) Q[F].
   ```
   This is an index-contraction theorem. A concrete lattice
   discretization may use it only after that discretization's
   `O_h`-covariance as a rank-two field-strength object has been
   established separately.

4. **Conditional coefficient consequence.** If a later source note
   independently proves that the admissible action class is
   `O_h`-invariant and independently identifies a candidate
   topological-charge slot with the determinant-odd `Q[F]` above, then
   the coefficient of that slot must vanish. This is a conditional
   consequence of group invariance, not a new admission and not a
   strong-CP solution.

## Proof Walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | `O_h` signed permutations map oriented spatial links and plaquettes bijectively. | `Z^3` spatial-substrate geometry |
| (B2) | Reversing a plaquette orientation replaces `U_P` by `U_P^\dagger`; `Re tr(U_P)` is unchanged. | Matrix adjoint and trace |
| (B3) | The Wilson plaquette sum is therefore permuted term-by-term. | (B1)-(B2) |
| (B4) | The three-index Levi-Civita tensor transforms by `det(R)` under `R in O(3)`, checked here on all 48 signed permutations. | Finite `O_h` enumeration |
| (B5) | If `F_{0i}` transforms as a spatial vector and `F_{jk}` as an antisymmetric spatial rank-two tensor, then the `R` factors in `epsilon^{ijk} F_{0i} F_{jk}` contract to the determinant character. | Orthogonality plus (B4) |
| (B6) | An `O_h`-invariant action cannot contain a nonzero coefficient multiplying a slot already proved to transform by the nontrivial determinant character. | Group invariance |

## Verification

The runner performs three bounded checks:

- a random `SU(3)` spatial-link configuration on a small periodic
  `2 x 2 x 2` lattice, checking the Wilson plaquette action under a
  representative proper/improper `O_h` sample;
- exact Levi-Civita transformation on all 48 signed permutations;
- random complex antisymmetric `F` tensors, checking
  `Q[R.F] = det(R) Q[F]` for representative proper/improper samples.

An independent exact replay of the epsilon identity over all 48 signed
permutations should also give no mismatches.

## Dependencies

- [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md)
  -- supplies the companion determinant-character action on the local
  `Cl(3)` pseudoscalar line.

No author-supplied audit result is used, and no Tier-A registry entry is
changed.

## Boundaries

This bridge does **not** prove:

- full strong-CP closure or theta retirement;
- `O_h`-invariance of the full Wilson + staggered + scalar action class;
- covariance of every standard lattice topological-charge
  discretization;
- the lattice-to-continuum `theta_QCD` bridge;
- exclusion of CP-odd terms outside the stated determinant-odd
  `epsilon F F` slot, such as pseudoscalar fermion bilinears.

It only lands the bounded structural sign bridge above. The independent
auditor decides whether the row is retained-grade after merge.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/strong_cp_epsilon_pseudotensor_oh_sign_runner.py
```

Expected:

```text
TOTAL: PASS=9 FAIL=0
VERDICT: Wilson plaquette invariance and epsilon-pseudotensor sign law
hold on the bounded checks; coefficient exclusion remains conditional on
a separate O_h-invariant action-class result.
```
