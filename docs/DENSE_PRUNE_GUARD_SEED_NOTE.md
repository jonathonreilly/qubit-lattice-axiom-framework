# Dense Prune Guard Seed Note

**Claim type:** bounded_theorem

This note compares the historically flip-prone seed set from the replay work against the current channel-count guard path at the aggregate level supported by the cached runner output.

The code path has evolved since the earlier replay logs, so treat any per-seed numbers in the historical reference tables below as legacy diagnostic snapshots, not as the cache-certified support for this note's bounded claim.

Historical flip seeds from the replay set (reference only):
- `N=80`: seeds `8, 12, 13`
- `N=100`: seeds `2, 3, 13`

Current guard path:
- **Primary runner:** `scripts/channel_count_guarded_prune.py`
- guard mode: channel-count preserving, `q=0.10`

## Per-seed comparison (legacy reference, not cache-certified)

> The tables in this section are retained as a legacy snapshot from the
> earlier replay path. The currently cached runner stdout reports only
> aggregate rows over the seed set, and does not certify the exact
> per-seed `grav`, `purity`, `eff_ch`, `flip`, or `removed_total` values
> printed below, nor whether the channel-count guard triggered on any
> individual seed. Per the 2026-05-17 audit verdict, these per-seed
> numbers do not load-bear the bounded claim below; they are kept here
> for narrative continuity until a per-seed diagnostic runner output
> lands (see follow-up section).

### N = 80

| seed | mode | grav_b | grav_p | d_grav | pur_b | pur_p | d_pur | eff_b | eff_p | flip |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | plain | +0.235 | +6.003 | +5.768 | 1.0000 | 0.9773 | -0.0227 | 4.14 | 3.92 | 0 |
| 8 | guard | +0.235 | +1.697 | +1.462 | 1.0000 | 0.9938 | -0.0062 | 4.14 | 6.64 | 0 |
| 12 | plain | +0.436 | -0.214 | -0.650 | 0.9994 | 0.9804 | -0.0190 | 8.22 | 5.80 | 1 |
| 12 | guard | +0.436 | +3.753 | +3.317 | 0.9994 | 0.9742 | -0.0252 | 8.22 | 8.99 | 0 |
| 13 | plain | -0.239 | +3.254 | +3.493 | 1.0000 | 0.8250 | -0.1750 | 8.82 | 7.55 | 0 |
| 13 | guard | -0.239 | -0.239 | +0.000 | 1.0000 | 1.0000 | +0.0000 | 8.82 | 8.82 | 0 |

### N = 100

| seed | mode | grav_b | grav_p | d_grav | pur_b | pur_p | d_pur | eff_b | eff_p | flip |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | plain | +9.334 | +0.327 | -9.007 | 1.0000 | 0.9994 | -0.0006 | 5.36 | 2.84 | 0 |
| 2 | guard | +9.334 | +10.258 | +0.924 | 1.0000 | 1.0000 | -0.0000 | 5.36 | 4.44 | 0 |
| 3 | plain | +0.486 | -0.545 | -1.031 | 1.0000 | 0.9957 | -0.0043 | 3.02 | 2.72 | 1 |
| 3 | guard | +0.486 | -0.424 | -0.910 | 1.0000 | 0.9981 | -0.0019 | 3.02 | 2.60 | 1 |
| 13 | plain | +3.652 | -0.054 | -3.707 | 0.9999 | 0.9959 | -0.0040 | 4.09 | 2.97 | 1 |
| 13 | guard | +3.652 | +3.652 | +0.000 | 0.9999 | 0.9999 | +0.0000 | 4.09 | 4.09 | 0 |

## Readout (aggregate-supported)

At the aggregate level certified by the cached runner stdout, the channel-count
guard shifts the bounded pruning behavior on the flip-prone seed set: aggregate
gravity, aggregate purity, and aggregate `eff_ch` differ between plain and
guarded modes, and the aggregate flip count is reduced under the guard.

The note no longer claims, on the basis of this cache, that the guard is a
"seed-selective channel-preservation mechanism" or that specific named seeds
are rescue / non-rescue cases. Those would require a per-seed diagnostic
runner output that prints `grav`, `purity`, `eff_ch`, `flip`, `removed_total`,
and a guard-triggered flag per seed under the same code hash. Such a runner
output is queued as out-of-scope follow-up below.

What the aggregate cache does support, as a bounded observation, is that the
channel-count guard is not a no-op on this seed set: aggregate `eff_ch` and
aggregate flip count both move under the guard relative to plain pruning. The
detailed mechanism by which individual seeds respond is not certified here.

## 2026-05-18 audit-conditional repair: per-seed mechanism claim narrowed to aggregate

Per the 2026-05-17 audit verdict, the per-seed table and seed-selective
mechanism claims were not supported by the cached aggregate-only stdout.
This revision narrows the bounded claim to what the existing aggregate
cache supports. A future per-seed diagnostic runner output is queued
as out-of-scope follow-up.

Follow-up (out of scope for this repair): a per-seed diagnostic runner
output that, for the listed historical seeds and under the same code
hash as the aggregate cache, prints `grav`, `purity`, `eff_ch`, `flip`,
`removed_total`, and a guard-triggered flag per seed. Until that lands,
the per-seed tables above are legacy reference only and the
seed-selective mechanism language is withdrawn from the bounded claim.

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/causal_field_mass_scaling.py`
- `scripts/dense_prune_q003_joint_strict.py`
- `scripts/three_d_joint_test.py`
- `scripts/three_d_modular_gravity_mass_scaling.py`

---

**Audit re-queue note 2026-05-17:** an earlier re-audit ran before
`scripts/codex_audit_runner.py` substituted `{{HELPER_RUNNER_SOURCES}}`,
so the packet could still omit helper runner sources. This source-only
bookkeeping note intentionally changes the note hash to queue a fresh
independent audit with helper sources bundled from the ledger row's
`helper_runner_paths`. No science content changes.
