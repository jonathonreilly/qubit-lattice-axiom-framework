# Shapiro Five-Family Portability Note

**Date:** 2026-04-06
**Status:** RETRACTED 2026-04-30 — audit failed; this note is archived under `archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/`. Claims below are NOT supported by current runners or current audit lane. See `## Retraction` section.

## Current-surface certificate (2026-06-12 source firewall)

**Actual current-surface status:** archived `audited_failed` / retracted
historical artifact. This file is kept only as audit history for a failed
or inconsistent route. It may not be cited as retained, bounded, conditional,
supporting, or methodological authority for any live framework chain.

## Retraction

- **Date archived:** 2026-04-30
- **Archive directory:** `archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/` (the directory name encodes the failure reason: static renderers and failed bridges).
- **Audit verdict_rationale (quoted verbatim from `docs/audit/data/audit_ledger.json`):**

  > Issue: The note claims exact zero-source control on all five families, but the current runner reports zero lags of about 0.065-0.071 rad for every family, and the cited frozen log is absent. Why this blocks: the zero control is the stated first gate for portability; if it fails or is miscomputed, the few-milliradian cross-family spread table cannot be interpreted as a retained causal phase-lag extension, especially with the three-family core only conditional and the fifth-family radial dependency already failed. Repair target: fix the zero-control computation and labeling, restore a frozen log, add PASS/FAIL assertions for zero controls and family spread, and re-audit the sign/fourth/fifth-family dependencies before reasserting five-family portability. Claim boundary until fixed: it is safe to say the current script prints similar c-dependent phase rows for five sampled families; it is not safe to claim exact controls or retained five-family Shapiro portability.

- **Do not cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## 2026-06-16 archive firewall

This archived packet is historical / diagnostic and retired as evidence. It
does not establish five-family Shapiro portability, exact zero-source controls,
or a retained extension to quadrant/radial families.

The audit failure is load-bearing: the alleged zero-source controls were the
first gate for the portability claim, and the current runner did not reproduce
them as exact zeros. Treat the tables below as stale printed rows only.

## Artifact Chain

- [`scripts/shapiro_five_family_portability.py`](../../scripts/shapiro_five_family_portability.py)
- [`logs/2026-04-06-shapiro-five-family-portability.txt`](../../logs/2026-04-06-shapiro-five-family-portability.txt)
- three-family core: [`docs/SHAPIRO_FAMILY_PORTABILITY_NOTE.md`](../../docs/SHAPIRO_FAMILY_PORTABILITY_NOTE.md)
- structured-family context: [`docs/SIGN_PORTABILITY_INVARIANT_NOTE.md`](../../docs/SIGN_PORTABILITY_INVARIANT_NOTE.md)
- additional sampled families: [`docs/FOURTH_FAMILY_QUADRANT_NOTE.md`](../../docs/FOURTH_FAMILY_QUADRANT_NOTE.md), [`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md`](../../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_RADIAL_NOTE.md)

## Historical question (retracted)

The old question asked whether a Shapiro-style c-dependent phase lag survives
beyond a three-family core. This archive does not establish that premise.

## Failed control gate

The old body claimed exact zero-source controls on all five sampled families:

- Fam1: zero lag = `+0.000e+00`
- Fam2: zero lag = `+0.000e+00`
- Fam3: zero lag = `+0.000e+00`
- Fourth family quadrant: zero lag = `+0.000e+00`
- Fifth family radial: zero lag = `+0.000e+00`

That was the first gate for the portability claim. Audit reports that the
current runner prints nonzero zero-source lags of roughly `0.065-0.071 rad`, so
this archived control claim is retracted.

## Historical cross-family phase table (retracted)

| c | Fam1 | Fam2 | Fam3 | Quad | Radial | max diff |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| inst | +0.0000 | +0.0000 | +0.0000 | +0.0000 | +0.0000 | 0.0000 |
| 2.0 | +0.0401 | +0.0401 | +0.0400 | +0.0401 | +0.0424 | 0.0024 |
| 1.0 | +0.0499 | +0.0501 | +0.0499 | +0.0492 | +0.0514 | 0.0022 |
| 0.5 | +0.0621 | +0.0622 | +0.0620 | +0.0620 | +0.0615 | 0.0008 |
| 0.25 | +0.0679 | +0.0679 | +0.0679 | +0.0652 | +0.0655 | 0.0027 |

## Historical sampled rows (not retained dependencies)

- `Fam1`: restored `(drift=0.20, restore=0.70, seed=0/1)`
- `Fam2`: restored `(drift=0.05, restore=0.30, seed=0/1)`
- `Fam3`: restored `(drift=0.50, restore=0.90, seed=0/1)`
- `Fourth family quadrant`: `(drift=0.00, seed=0)` on the no-restore slice
- `Fifth family radial`: `(drift=0.05, seed=0)` on the no-restore slice

## Historical safe-read text (retracted and narrowed)

- safe only as a record that the old script printed similar finite-c rows for
  five sampled families
- not safe as exact zero-source control
- not safe as retained five-family Shapiro portability
- not safe as a live quadrant/radial family extension

## Historical final verdict (retracted)

The old retained-positive verdict is retracted. A future repair would need
PASS/FAIL zero-control assertions, a restored frozen log, and independently
audited sign/fourth/fifth-family dependencies before any portability claim can
be reopened.
