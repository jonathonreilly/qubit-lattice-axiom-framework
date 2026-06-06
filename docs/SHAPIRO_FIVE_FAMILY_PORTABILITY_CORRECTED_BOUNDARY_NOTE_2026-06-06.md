# Shapiro Five-Family Portability Corrected Boundary Packet

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note records a
bounded-support correction and does not set or predict an audit outcome.
**Primary runner:**
[`scripts/shapiro_five_family_portability.py`](../scripts/shapiro_five_family_portability.py)
with cache
[`logs/runner-cache/shapiro_five_family_portability.txt`](../logs/runner-cache/shapiro_five_family_portability.txt).

## Purpose

The archived five-family Shapiro portability row failed because the runner
printed nonzero source-off-vs-source-on phases near `0.065--0.071 rad` while
labeling them exact zero controls. This packet repairs the executable boundary:
the true zero-source control now compares instantaneous and finite-`c`
propagation at the same source strength `s=0`, while the old nonzero quantity is
kept as a source-off diagnostic.

No new axiom, observed target value, fitted selector, or external comparator is
introduced.

## Corrected Executable Result

The runner checks the three restored grown-family samples plus the fourth-family
quadrant and fifth-family radial sampled rows. The corrected gates are:

- zero-source finite-`c` control is below `1e-12` on all five family groups;
- the old source-off diagnostic remains nonzero, confirming it was not a zero
  control;
- finite-`c` detector phases are positive and monotone as `c` decreases on each
  sampled family group;
- the five-family sampled spread is below `0.003 rad` at every tested `c`.

Current live readout:

```text
ZERO-SOURCE C-CONTROL
  Fam1: +3.380e-18
  Fam2: +2.909e-18
  Fam3: +7.419e-19
  Fourth family quadrant: +4.849e-18
  Fifth family radial: +7.039e-18

SOURCE-OFF DIAGNOSTIC (not a zero control)
  range: +6.545e-02 to +7.061e-02 rad

five-family max spread:
  c=2.00: 0.0024 rad
  c=1.00: 0.0022 rad
  c=0.50: 0.0008 rad
  c=0.25: 0.0027 rad

ASSERTIONS: PASS
```

## Claim Boundary

This packet supports only the sampled proxy statement: the Shapiro-style phase
observable extends from the three restored grown-family samples to the named
quadrant and radial sampled rows with a corrected zero-source control and
milliradian-scale spread.

It does not claim:

- the old source-off diagnostic as a zero control;
- family-wide theorem coverage for all quadrant or radial parameter choices;
- absolute diamond/NV calibration;
- a unique causal discriminator against static proxy fields;
- physical gravitational closure;
- audit-ratified status before independent audit.

## Repaired Parent

This note repairs the source-side executable gap in the archived row
`shapiro_five_family_portability_note` without relabeling that row. Independent
audit must decide the effective status of this corrected packet.
