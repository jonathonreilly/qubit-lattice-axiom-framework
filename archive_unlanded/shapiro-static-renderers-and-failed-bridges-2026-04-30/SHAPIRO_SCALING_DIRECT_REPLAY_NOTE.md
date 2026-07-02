# Shapiro Scaling Direct Replay Note

**Date:** 2026-04-08
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

  > Issue: The direct replay script is a static data renderer whose s, b, and k laws are imported from SHAPIRO_EXPERIMENTAL_CARD.md, which is unaudited/unknown, and it also cites the failed Shapiro diamond frequency bridge. Why this blocks: freezing unaudited table entries is not a retained replay unless the source card is audit-clean or the runner recomputes the laws from raw inputs with zero-control checks. Repair target: audit SHAPIRO_EXPERIMENTAL_CARD.md or replace this with a runner that directly recomputes the s, b, and k scaling sweeps and asserts the source-off and instantaneous-field controls. Claim boundary until fixed: it is safe to say the script renders the stored scaling and portable-delay tables; it is not safe to claim retained Shapiro scaling-law closure from this row.

- **Do not cite warning:** Do NOT cite the numerical results, tables, or threshold values in the original content below as live framework claims. The runners referenced in this note have been superseded or are no longer reproducible at the time of audit. If a future investigation revisits this physics, treat it as starting from scratch rather than as continuation of a "closed no-go".

## 2026-06-16 archive firewall

This archived packet is historical / diagnostic and retired as evidence. It
renders stored scaling rows from unaudited/failed Shapiro sources; it does not
establish retained source-strength, impact-parameter, or drive-scale laws.

The only safe residual is bookkeeping: the old script rendered stored tables.
A future repair must recompute the sweeps from raw inputs and assert the
source-off and instantaneous-field controls.

## Artifact Chain

- [`scripts/shapiro_scaling_direct_replay.py`](../../scripts/shapiro_scaling_direct_replay.py)
- [`scripts/shapiro_scaling_probe.py`](../../scripts/shapiro_scaling_probe.py)
- [`logs/2026-04-08-shapiro-scaling-direct-replay.txt`](../../logs/2026-04-08-shapiro-scaling-direct-replay.txt)
- [`docs/SHAPIRO_EXPERIMENTAL_CARD.md`](../../docs/SHAPIRO_EXPERIMENTAL_CARD.md)
- [`logs/2026-04-06-shapiro-delay-portable.txt`](../../logs/2026-04-06-shapiro-delay-portable.txt)
- [`docs/SHAPIRO_DIAMOND_FREQUENCY_BRIDGE_NOTE.md`](../../docs/SHAPIRO_DIAMOND_FREQUENCY_BRIDGE_NOTE.md)

## Historical static replay body (retracted)

The old note described itself as a direct freeze of in-repo data:

- `s` law from the experimental card
- `b` law from the experimental card
- `k` law from the experimental card
- exact zero controls from the experimental card and portable delay log

## Historical asserted controls (not audit-clean)

- `s = 0 -> phase = 0.000 rad`
- `c = inst -> phase = 0.000000 rad`
- `b` is not an exact-zero law; it is a monotone tail law that approaches
  zero at large separation

## Historical direct scaling table (retracted)

| law | control | direct readout | source |
| --- | --- | --- | --- |
| `phase ~ s^1.000` | `s = 0 -> phase = 0` | verified over `s = 0.001` to `0.016` | `docs/SHAPIRO_EXPERIMENTAL_CARD.md` |
| phase decreases with `b` | large `b -> phase -> 0` | `b = 3.0 -> +0.062 rad`; `b = 5.0 -> +0.049 rad`; `b = 7.0 -> +0.040 rad` | `docs/SHAPIRO_EXPERIMENTAL_CARD.md` |
| `phase ~ k` | instantaneous field -> phase = 0 | `k = 2.0 -> +0.030 rad`; `k = 5.0 -> +0.062 rad`; `k = 10.0 -> +0.200 rad` | `docs/SHAPIRO_EXPERIMENTAL_CARD.md` |

## Historical portable delay table (retracted)

| c | fam1 | fam2 | fam3 | mean |
| ---: | ---: | ---: | ---: | ---: |
| inst | -0.000000 | +0.000000 | -0.000000 | +0.000000 |
| 2.00 | +0.040233 | +0.040431 | +0.040130 | +0.040265 |
| 1.00 | +0.050011 | +0.050325 | +0.049930 | +0.050089 |
| 0.50 | +0.061643 | +0.061958 | +0.061700 | +0.061767 |
| 0.25 | +0.067893 | +0.068326 | +0.067886 | +0.068035 |

## Historical narrow read (retracted and narrowed)

- safe only as a record of stored scaling and portable-delay rows rendered by
  the stale script
- not safe as retained source-mass linearity
- not safe as retained impact-parameter scaling
- not safe as retained `k`/frequency scaling
- not safe as proof of exact control gates

## Historical final verdict (retracted)

The old closure verdict is retracted. This packet is not a retained replay and
does not close the Shapiro scaling lane.
