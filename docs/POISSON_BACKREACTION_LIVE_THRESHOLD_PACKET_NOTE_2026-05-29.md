# Poisson Backreaction Live Threshold Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/backreaction_poisson_live_threshold_check.py`](../scripts/backreaction_poisson_live_threshold_check.py)
**Load-bearing helper source:** [`scripts/backreaction_poisson.py`](../scripts/backreaction_poisson.py)

## Purpose

This packet repairs the usable part of the archived self-gravity
backreaction result without restoring the stale threshold claim. The old
archived note claimed a horizon-like threshold near `G_crit ~= 0.011`,
but the current live runner does not reproduce that table.

This packet starts from the live `scripts/backreaction_poisson.py` harness
and asserts only the finite facts it currently supports.
The live threshold runner asserts that this helper source is present,
untruncated, and has no hidden local script-helper imports.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## Live Finite Result

The runner replays the current Poisson self-gravity harness on the explicit
grid

```text
G = 0.000, 0.001, 0.005, 0.010, 0.011, 0.012, 0.020, 0.050, 0.100.
```

Current live output:

```text
baseline external-field delta = +1.073461e-02 TOWARD
      G iters         delta     dir    escape  f_self_max  converged
----------------------------------------------------------------------------------------
  0.000     2 +1.073461e-02  TOWARD    1.0461    0.000000       True
  0.001     5 +1.091395e-02  TOWARD    1.0470    0.010000       True
  0.005     6 +1.149967e-02  TOWARD    1.0498    0.050000       True
  0.010    15 +1.234071e-02  TOWARD    1.0502    0.100000      False
  0.011    15 +1.254950e-02  TOWARD    1.0500    0.110000      False
  0.012     9 +1.236590e-02  TOWARD    1.0497    0.120000       True
  0.020     9 +1.364420e-02  TOWARD    1.0442    0.200000       True
  0.050    12 +1.419413e-02  TOWARD    0.9631    0.500000       True
  0.100    15 +2.723267e-02  TOWARD    0.7547    1.000000      False

ASSERTIONS: PASS
```

The safe live statement is:

> In the current finite Poisson self-gravity harness, TOWARD deflection is
> preserved on the tested `G` grid and detector escape crosses below one
> between `G=0.020` and `G=0.050`; the first sub-unit escape point in the
> declared grid is `G=0.050`.

## Claim Boundary

This packet does not claim:

- the archived `G_crit ~= 0.011` threshold;
- a smooth monotone collapse law;
- convergence for every listed `G`;
- continuum horizon formation;
- physical Schrodinger-Newton closure;
- a retained status before independent audit.

The new packet is a bounded live assertion surface for the current runner.
