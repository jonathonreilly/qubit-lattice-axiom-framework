# Source-Resolved Retarded Green Corrected Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit, not audit-ratified.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/source_resolved_retarded_green_corrected_packet_check.py`](../scripts/source_resolved_retarded_green_corrected_packet_check.py)

## Purpose

The archived source-resolved retarded Green row failed because the printed
`ret/same` column was actually `ret/inst`, and the source note froze that
mislabeled value. This packet does not reuse that wrong headline ratio. It
computes the corrected same-site comparison directly from the live runner
helpers and records the narrower finite result.

No new axiom, observed target value, fitted selector, or external comparator
is introduced.

## Live Finite Result

The corrected packet checks the same exact `h=0.25` lattice pocket, source
cluster, finite-lag rule, and source strengths as the live runner. The safe
positive surface is:

- zero-source same-site and retarded shifts are exactly zero;
- retarded-like centroid shift is larger than same-site memory for all four
  source strengths;
- the corrected mean `ret/same` ratio is about `1.026`, not the stale printed
  `~1.20` ratio;
- detector support fraction is unchanged, while effective detector support
  `N_eff` broadens slightly;
- instantaneous, same-site, and retarded-like exponents are all near `1.00`;
- all retarded rows are TOWARD.

Current live readout:

```text
corrected mean ret/same ratio: 1.026
mean ret-same support delta: +0.000e+00
mean ret-same N_eff delta: +4.493e-02
exponents inst/same/ret: 1.00/1.00/1.00
TOWARD rows: 4/4
ASSERTIONS: PASS
```

## Claim Boundary

This packet supports only a finite-lag source-resolved pocket. It does not
claim:

- the old printed `ret/same ~= 1.20` headline;
- support-fraction broadening;
- a full retarded field equation;
- generated-family transfer;
- physical gravitational closure;
- audit-ratified status before independent audit.
