# Flavor - log-det generator provenance after the Record axiom

**Date:** 2026-06-04
**Claim type:** meta — provenance decomposition / roadmap. This is not a value
derivation and not a row promotion.
**Status authority:** independent audit lane only. This note sets no audit
status and assigns no grade.
**Runner:** [scripts/flavor_logdet_generator_three_factor_provenance_2026_06_04.py](../scripts/flavor_logdet_generator_three_factor_provenance_2026_06_04.py)
(SCORECARD 5/5).
**Depends:** [MINIMAL_AXIOMS_2026-06-04.md](MINIMAL_AXIOMS_2026-06-04.md),
[FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md](FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md),
and
[OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md](OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md).

## Context

[RECORD_P1_DEPENDENCY_AUDIT_NOTE_2026-06-04.md](RECORD_P1_DEPENDENCY_AUDIT_NOTE_2026-06-04.md)
found that none of the 91 direct dependents of the old observable-principle
parent can be rewritten to the narrow Record axiom alone. The dominant blocker
is the log-det generator surface: 59 rows require `W = log |det(D+J)|` or its
source-derivative algebra, not merely finite scalar additivity.

This note records a safer decomposition of that blocker. It does not re-cite,
edit, or promote those rows.

## Provenance Factors

The log-det generator needs at least these distinct factors:

| factor | content | status after the Record axiom |
|---|---|---|
| 1 - scalar record additivity | A specified finite record-readout functional adds over disjoint record collections. | Supplied by the Record axiom as a chain-satisfying premise only; it does not bound downstream rows. |
| 2 - record-readout realization | The proposed operator/source domain is actually a specified finite scalar record-readout surface to which factor 1 applies. | Separate residual. |
| 3 - determinant-character form | The per-block scalar form is the determinant-character family, not trace or another spectral functional. | Separate det-character authority; audit status remains independent. |
| 4 - source/action coupling | The generator is coupled as `D+J`, with `dW/dj_x = Re Tr[(D+J)^-1 P_x]`. | Separate source/action admission or theorem. |

Only factor 1 is part of the Record axiom. Factors 2 through 4 are not supplied
by the axiom and remain the live residuals for rows that depend on the log-det
generator.

## Consequence

The Record axiom can remove the old ambiguity about whether a specified scalar
record functional must add over disjoint record collections. It cannot by
itself convert a log-det-dependent row to bounded or retained status.

The actionable residual for the 59-row log-det category is therefore:

```text
record-readout realization
+ determinant-character authority
+ source/action coupling
```

with Record additivity available only after the record surface is specified.

## Verified Algebra

The runner checks the finite identities used in the decomposition:

- `log |det K| = sum_modes log |lambda|` for a finite non-singular example;
- block-diagonal log-det additivity;
- determinant multiplicativity versus trace failure;
- the local derivative identity
  `dW/dj_x = Re Tr[(D+J)^-1 P_x]` against finite differences;
- the residual list above remains non-empty after applying Record additivity.

These checks verify algebraic consistency of the roadmap. They do not prove
record-readout realization, do not audit the det-character theorem, and do not
turn the source/action coupling into an axiom.
