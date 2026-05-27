# Axiom-First Reflection Positivity - Bounded Input Assembly

**Date:** 2026-04-29; bounded-input repair 2026-05-27
**Claim type:** bounded_theorem
**Runner:** `scripts/axiom_first_reflection_positivity_bounded_inputs.py`
**Status authority:** independent audit lane only.

This repaired row is no longer a full reflection-positivity theorem for the
`SU(3)` Wilson plaquette action coupled to arbitrary staggered half-action
observables. The audited conditional verdict found that the available packet
does not prove the missing `SU(3)` Wilson-plaquette gauge boundary
factorization or the staggered Grassmann half-action factorization for
arbitrary positive-half polynomial observables.

The binding scope is therefore narrowed to the two one-hop bounded inputs that
are actually available, plus their abstract finite product consequence.

## Binding Scope

The repaired row asserts only:

1. The staggered-only determinant input is available from
   [STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md):

   ```text
   det(M_KS + m I) = product_i (m^2 + sigma_i^2) > 0,     m > 0.
   ```

2. The abstract reflection norm-square input is available from
   [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md):

   ```text
   <Theta(F) F> = || psi^2 F ||^2 >= 0
   ```

   under explicit measure-preserving involution, half-action invariance, and
   reflection-Hermitian observable hypotheses.

3. In any finite product setting where those two hypotheses are supplied, the
   product of the positive staggered determinant weight and the abstract
   norm-square weight is non-negative, and the induced finite Gram matrix is
   positive semidefinite.

That is the full binding claim of this repaired row.

## What This Does Not Claim

This row does not claim:

- the actual `SU(3)` Wilson plaquette gauge-half boundary factorization for the
  stated temporal reflection map;
- the staggered Grassmann half-action reflection-positive factorization for
  arbitrary positive-half polynomial observables;
- full finite-lattice reflection positivity for the physical action;
- construction of the physical Osterwalder-Schrader Hilbert space;
- positivity of the physical transfer matrix or subtracted energy spectrum;
- any Wilson-fermion determinant positivity theorem; or
- any publication/ledger status promotion.

Those remain separate bridge-theorem targets.

## Direct Dependencies

| Authority | Role |
|---|---|
| [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md) | positive staggered determinant input for `M_KS + m I`, `m > 0` |
| [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md) | abstract norm-square / PSD sesquilinear input under explicit hypotheses |

The older structural runner `scripts/axiom_first_reflection_positivity_check.py`
is diagnostic context only. It is not the binding runner for this repaired row.

## Runner

Run:

```bash
python3 scripts/axiom_first_reflection_positivity_bounded_inputs.py
```

The runner verifies the finite algebraic product consequence of the narrowed
inputs and checks that the source note excludes the former full-theorem claims.

Expected certificate:

```text
RUNNER STATUS: PASS
```

## Re-Audit Question

Does this narrowed row now correctly retain only the determinant-positivity
input, the abstract norm-square input, and their bounded finite product/PSD
consequence, while leaving the full reflection-positivity bridge theorem
outside the binding claim?
