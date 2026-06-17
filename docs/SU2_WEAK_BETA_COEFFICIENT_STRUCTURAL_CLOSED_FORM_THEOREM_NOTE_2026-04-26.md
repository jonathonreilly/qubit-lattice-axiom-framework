# SU(2)_L Weak 1-Loop Beta-Coefficient Structural Arithmetic Boundary

**Date:** 2026-04-26

**Status:** bounded-support / authority-boundary. This note is not a positive
SU(2)_L-running theorem on the current authority surface.

**Primary runner:**
`scripts/frontier_su2_weak_beta_coefficient_structural_closed_form.py`

## Purpose

This note preserves the exact structural arithmetic for the asymptotic
SU(2)_L one-loop beta coefficient while exposing the two authority gaps that
prevent retained-positive status:

- the S1/CKM source chain used for `N_pair` and `N_color` is bounded by its
  current source authority status;
- the one-loop QFT beta-function formula is a textbook/literature theorem
  unless and until the framework proves the same formula natively.

No new axiom is introduced.

## Structural Arithmetic

Using the source values

```text
N_pair  = 2
N_color = 3
N_gen   = 3
N_H     = 1
```

the standard one-loop SU(2)_L coefficient convention `b > 0` for asymptotic
freedom gives:

```text
b_2 = (11/3) C_2(adj SU(2))
      - (1/3) N_W
      - 1/6

C_2(adj SU(2)) = N_pair = 2
N_W = (N_color + 1) N_gen = 12

b_2 = 22/3 - 4 - 1/6 = 19/6
```

Equivalently:

```text
b_2 = (11 N_pair - N_color (N_color + 1)) / 3 - 1/6
    = (22 N_pair - 2 N_color (N_color + 1) - 1) / 6
    = 19/6
```

The runner also verifies the companion ratio arithmetic:

```text
b_3 / b_2   = 42/19
b_2 / b_QED = 19/64
b_3 / b_QED = 21/32
```

## Textbook Formula Boundary

The coefficient formula above is the standard one-loop gauge beta-function
formula applied to the framework's source counts. This PR does not prove the
one-loop renormalization theorem from the framework primitives. Therefore the
textbook theorem is treated as an exposed literature/theorem input, not as a
hidden retained derivation.

That boundary is useful: it separates the exact framework-count arithmetic
from the external QFT theorem. A later framework-native renormalization proof
could retire this import; until then, this note remains bounded support.

## Source Authority Boundary

The arithmetic uses source values read from current notes and checks each
source against the ledger in the runner. Non-retained-positive inputs are
reported as boundaries rather than hard failures.

The retained-positive piece that remains directly usable is the one-Higgs
doublet EW content checked by the runner. The three-generation source is usable
only at its audited bounded status, and the CKM/S1/fractional-charge sources
remain boundary inputs for this note.

## What Is Preserved

The PR should preserve these executable results:

```text
B_2_STRUCTURAL_ARITHMETIC_VERIFIED = True
B_2_PER_SECTOR_DECOMPOSITION_VERIFIED = True
THREE_WAY_COMPANION_COUPLING_RATIOS_VERIFIED = True
COMPLETE_SM_GAUGE_BETA_TRIO_VERIFIED = True
JOINT_ASYMPTOTIC_RUNNING_PACKAGE_VERIFIED = True
```

These are exact `Fraction` arithmetic checks from the source counts. They are
not a claim that the repo has retained-positive beta-running closure.

## What Is Not Claimed

This note does not:

- close any open mass, CKM, EW, GUT, or running lane;
- promote the standard textbook beta-function theorem to framework-native
  retained status;
- promote bounded, unaudited, no-go, support-tier, or comparator sources;
- alter audit verdicts or repo-wide authority surfaces.

If a future framework-native renormalization proof lands, this note gives the
counting specialization that can be rechecked against it.
