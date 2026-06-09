---
claim_type: bounded_theorem
claim_status: bounded_support
proposal_allowed: false
audit_required_before_effective_status_change: true
bare_retained_allowed: false
---

# Second Grown Family Live Battery Note

**Date:** 2026-06-08
**Status:** bounded-support source repair; no audit verdict or effective-status
movement is claimed here.
**Primary runner:**
[`scripts/second_grown_family_battery.py`](../scripts/second_grown_family_battery.py)
**Runner cache:**
[`logs/runner-cache/second_grown_family_battery.txt`](../logs/runner-cache/second_grown_family_battery.txt)
**Legacy row repaired:** `second_grown_family_note`

## Purpose

The archived second-grown-family note named
`scripts/second_grown_family_battery.py`, but that executable battery was absent
from the artifact chain. The old broad positive table therefore was not
auditable from the supplied packet.

Current main now contains the live battery verifier and a fresh cache. This note
restores a source-facing packet for re-review: it points to the executable
current battery and records the narrow evidence it actually checks.

## Bounded Claim

On the current source surface, the second-grown-family evidence packet is
reproducible as a finite bounded-support battery:

- [`scripts/second_grown_family_battery.py`](../scripts/second_grown_family_battery.py)
  exists and runs from current source.
- [`logs/runner-cache/second_grown_family_battery.txt`](../logs/runner-cache/second_grown_family_battery.txt)
  is fresh and reports
  `PASS=21 FAIL=0`.
- The verifier loads fresh ok caches for the sign, distance/impact, and
  complex-action slices listed below.
- The verifier explicitly checks that each subordinate evidence runner exists
  in current source and that its live SHA matches the SHA pinned in its fresh
  runner cache.
- The verifier statically imports each subordinate evidence runner module, so
  the restricted audit packet exposes the current child-runner source rather
  than only cache text.
- The verifier explicitly keeps the complex-action support narrow and
  boundary-aware.

This is a current-source replacement packet for the missing-runner blocker. It
is not a resurrection of the older broad retained-grade table.

## Artifact Chain

Primary packet:

- [`scripts/second_grown_family_battery.py`](../scripts/second_grown_family_battery.py)
- [`logs/runner-cache/second_grown_family_battery.txt`](../logs/runner-cache/second_grown_family_battery.txt)
- [`archive_unlanded/grown-family-missing-artifacts-2026-04-30/SECOND_GROWN_FAMILY_NOTE.md`](../archive_unlanded/grown-family-missing-artifacts-2026-04-30/SECOND_GROWN_FAMILY_NOTE.md)

2026-06-09 source-packet import repair: the primary battery now imports the
five child runners below and verifies that each imported module path is the
exact runner whose fresh cache is consumed. The expensive child computations
remain cache-backed, but the source packet is no longer cache-text-only.

Current evidence slices checked by the battery:

- [`scripts/SECOND_GROWN_FAMILY_SIGN_SWEEP.py`](../scripts/SECOND_GROWN_FAMILY_SIGN_SWEEP.py)
- [`logs/runner-cache/SECOND_GROWN_FAMILY_SIGN_SWEEP.txt`](../logs/runner-cache/SECOND_GROWN_FAMILY_SIGN_SWEEP.txt)
- [`docs/SECOND_GROWN_FAMILY_SIGN_NOTE.md`](SECOND_GROWN_FAMILY_SIGN_NOTE.md)
- [`scripts/DISTANCE_LAW_BREAKPOINT_COMPARE.py`](../scripts/DISTANCE_LAW_BREAKPOINT_COMPARE.py)
- [`logs/runner-cache/DISTANCE_LAW_BREAKPOINT_COMPARE.txt`](../logs/runner-cache/DISTANCE_LAW_BREAKPOINT_COMPARE.txt)
- [`scripts/impact_parameter_portability_probe.py`](../scripts/impact_parameter_portability_probe.py)
- [`logs/runner-cache/impact_parameter_portability_probe.txt`](../logs/runner-cache/impact_parameter_portability_probe.txt)
- [`scripts/SECOND_GROWN_FAMILY_COMPLEX.py`](../scripts/SECOND_GROWN_FAMILY_COMPLEX.py)
- [`logs/runner-cache/SECOND_GROWN_FAMILY_COMPLEX.txt`](../logs/runner-cache/SECOND_GROWN_FAMILY_COMPLEX.txt)
- [`docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md)
- [`scripts/SECOND_GROWN_FAMILY_COMPLEX_QUICK.py`](../scripts/SECOND_GROWN_FAMILY_COMPLEX_QUICK.py)
- [`logs/runner-cache/SECOND_GROWN_FAMILY_COMPLEX_QUICK.txt`](../logs/runner-cache/SECOND_GROWN_FAMILY_COMPLEX_QUICK.txt)
- [`docs/SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md)

## Evidence Summary

The primary battery verifies all of the following from fresh caches:

- Sign slice: the no-restore geometry-sector second-family sweep passes all
  `15/15` tested rows over drift values `[0.0, 0.1, 0.2, 0.3, 0.5]` and seeds
  `[0, 1, 2]`, with exact zero/neutral controls and mean weak-charge exponent
  `1.000072`.
- Distance/impact slice: the restored Fam2 row at `drift=0.05`,
  `restore=0.30` carries the distance-law evidence, including the reported
  `alpha = -0.947`, `5/5 TOWARD`, a null control at `b=8`, and the
  `delta ~= C * b^-0.947` fit.
- Complex-action slice: the full complex packet supplies an executable narrow
  anchor-row positive check, including `gamma=0`, Born-proxy, and
  `TOWARD@0.1 -> AWAY@0.5` gates on the checked anchor.
- Complex boundary slice: the quick packet prevents overextension by recording
  that the complex-action companion is not cleanly family-wide on the quick
  window.
- Provenance guard: the verifier checks that the archived blocker named the
  missing battery path and allowed replacement by current sign/complex evidence
  packets.

## Boundary

This note does not claim:

- any direct edit to the audit ledger;
- any effective status change without independent audit;
- a revived broad nine-family table;
- a theorem that selects the second grown family from the base axiom alone;
- geometry-generic or family-wide complex-action closure;
- a new axiom.

The safe current statement is only that the missing executable battery has been
restored as a bounded, reproducible current-source packet over the listed
evidence slices.

## Verification

Run:

```bash
python3 scripts/cached_runner_output.py --check-only scripts/second_grown_family_battery.py
python3 -m py_compile scripts/second_grown_family_battery.py
```
