# Source-Resolved Transverse Green Corrected Boundary Packet

**Date:** 2026-05-29
**Status:** bounded-support correction/falsifier; proposed for independent audit, not audit-ratified.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/source_resolved_transverse_green_corrected_boundary_check.py`](../scripts/source_resolved_transverse_green_corrected_boundary_check.py)

## Purpose

The archived transverse-propagating Green row failed because the frozen note
claimed a positive transverse correction over same-site memory, while the live
runner gives a small negative `trans - same` centroid shift in every row. The
runner also prints a column labeled `trans/same` that is actually
`trans/inst`.

This packet preserves the real finite facts and blocks the stale positive
same-site correction. It does not relabel the archived failed row.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## Live Finite Result

On the same exact `h=0.25` lattice pocket, source cluster, memory rule, and
source strengths, the corrected runner checks:

- zero-source same-site and transverse shifts are exactly zero;
- transverse rows remain `4/4` TOWARD;
- instantaneous, same-site, and transverse exponents are all near `1.00`;
- true mean `trans/inst` is about `1.162`;
- corrected mean `trans/same` is about `0.990`, not the stale printed
  same-site ratio;
- `trans - same` centroid shift is negative in every row;
- detector support fraction is unchanged;
- detector `N_eff` broadens slightly.

Current live readout:

```text
mean trans/inst ratio: 1.162
corrected mean trans/same ratio: 0.990
mean trans-same centroid shift: -8.676e-05
mean support-fraction delta: +0.000e+00
mean N_eff delta: +3.697e-03
exponents inst/same/trans: 1.00/1.00/1.00
TOWARD rows: 4/4
ASSERTIONS: PASS
```

## Claim Boundary

This is a corrected finite boundary packet. It supports the TOWARD/linear
transverse rows and the slight detector `N_eff` broadening, while falsifying
the old positive same-site centroid-correction headline.

It does not claim:

- positive `trans - same` centroid correction;
- support-fraction broadening;
- a full transverse transport field equation;
- generated-family transfer;
- physical gravitational closure;
- audit-ratified status before independent audit.
