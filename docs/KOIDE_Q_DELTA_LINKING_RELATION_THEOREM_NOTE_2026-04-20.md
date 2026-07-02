# Koide Q-Delta Formal Ratio Identity

**Date:** 2026-04-20; formal-ratio repair 2026-05-25
**Status:** bounded-support formal algebra. No Berry-holonomy radian bridge, equal-sector-norm selector, or physical charged-lepton claim is part of the binding theorem.
**Status authority:** independent audit lane only.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_koide_q_delta_formal_ratio_repair.py`

## Source boundary (2026-06-12)

**Boundary:** renaming / definition-level formal identity support only.
Effective status is audit-derived; this source records only the claim
boundary.

The exact arithmetic below is useful, but its load-bearing content is the
substitution of the two definitions `Q_d = 2/d` and `Delta_d = 2/d^2`.
This note may be cited only for the formal identity `Delta_d = Q_d/d` and
the rational `d = 3` values. It may not be cited as a Koide selector, a
Berry/radian bridge, a charged-lepton offset theorem, a PDG comparator, or a
framework derivation of either defined quantity.

Promotion beyond renaming support requires deriving either `Q_d` or
`Delta_d` from retained framework inputs, or attaching the formal identity to
a retained parent claim that supplies independent scientific content.

## Citation firewall (2026-06-18)

Direct citations to this note are allowed only for the definition-level
identity

```text
Delta_d = Q_d / d
```

after the two formal definitions `Q_d = 2/d` and `Delta_d = 2/d^2` have
already been stated. Direct citations must not use this note as authority for:

- a Koide selector;
- a Berry/radian bridge;
- a PDG or observed-mass comparator;
- a physical charged-lepton offset theorem;
- a retained derivation of either `Q_d` or `Delta_d`.

The paired runner now scans direct source citations to this file and rejects
contexts that still present the row as retained physical `delta = 2/9`, a
partial physical closure, a PDG comparator, or a live radian-bridge authority.
Historical notes that need the old residual-postulate `P` language should cite
the explicit radian-bridge no-go notes instead; this repaired note is only the
formal ratio identity.

## Actual claim

For any integer `d >= 1`, define the two formal dimensionless quantities:

```text
Q_d = 2 / d,
Delta_d = 2 / d^2.
```

Then:

```text
Delta_d = Q_d / d.
```

At `d = 3`, this gives:

```text
Q_3 = 2/3,
Delta_3 = 2/9,
Delta_3 / Q_3 = 1/3.
```

That exact rational identity is the entire repaired theorem.

## Why this repair is narrow

The prior audit verdict accepted the arithmetic but marked the row conditional because the previous note treated two bridges as load-bearing:

- an equal-sector-norm input giving `Q = 2/d`;
- a radian/Berry-holonomy bridge interpreting the dimensionless `2/d^2` ratio as a physical offset in radians.

This repair withdraws both from the binding claim. It proves only the formal ratio identity between two explicitly defined dimensionless quantities. It does not claim that either quantity is selected by the framework, observed in the charged-lepton data, or read as a Berry holonomy.

## Theorem

**Theorem.** Let `d >= 1` be an integer and let:

```text
Q_d = 2 / d,
Delta_d = 2 / d^2.
```

Then:

```text
Delta_d = Q_d / d.
```

**Proof.**

```text
Q_d / d = (2 / d) / d = 2 / d^2 = Delta_d.
```

QED.

## Negative control

The alternative generalization

```text
Q'_d = (d - 1) / d
```

coincides with `2/d` only at `d = 3`. For all tested `d != 3`, it fails:

```text
Delta_d = Q'_d / d.
```

Thus the formal identity is tied to the pair `(2/d, 2/d^2)`, not to an arbitrary extrapolation from the `d = 3` coincidence.

## What this row does not claim

- It does not derive `Q_d = 2/d` from a Koide equal-sector-norm selector.
- It does not derive `Delta_d = 2/d^2` from a Berry phase, selected line, or radian convention.
- It does not claim `Delta_3 = 2/9` as a physical charged-lepton offset.
- It does not use PDG masses or observational matching.
- It does not add an axiom or apply an audit verdict.

The bridge from this formal algebra to physical Koide/Brannen geometry remains a separate open science problem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_q_delta_formal_ratio_repair.py
```

Expected result:

```text
Koide Q-delta formal ratio repair
TOTAL: PASS=106 FAIL=0
```
