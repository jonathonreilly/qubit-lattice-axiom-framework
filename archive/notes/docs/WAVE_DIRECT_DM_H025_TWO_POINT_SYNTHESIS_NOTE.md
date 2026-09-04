# Wave Direct-dM H=0.25 Fam1 Fine-Pair Synthesis

**Date:** 2026-04-08; narrowed 2026-05-27
**Claim type:** bounded_theorem
**Script:** `scripts/wave_direct_dm_h025_fam1_fine_pair_synthesis_certificate.py`
**Historical broad runner:** `scripts/wave_direct_dm_h025_point_runner.py`
**Status authority:** independent audit lane only

---

## Status

This row is narrowed to the clean retained-core surface identified by audit:
the controlled `Fam1`, `H = 0.25`, `S = 0.004`, seed0/seed1 fine-pair
comparison plus the two seed control ladders.

The previous source note also claimed a coarse-to-fine seed-ordering reversal
and an uneven late-gain-compression explanation using cited high/low band logs.
Those broader claims are removed from this row because the cited logs are not
retained one-hop authorities for the coarse-band values. They remain out of
scope unless a later PR supplies retained coarse-band provenance.

## Bounded Claim

For `Fam1` at `H = 0.25`, `S = 0.004`:

| seed | dM(early) | dM(late) | delta_hist | R_hist |
| ---: | ---: | ---: | ---: | ---: |
| `0` | `+0.004989` | `+0.006246` | `-0.001256` | `-20.12%` |
| `1` | `+0.004411` | `+0.006255` | `-0.001843` | `-29.47%` |

The two control ladders verify:

| seed | null max `|delta_hist|` | sign pattern | `|delta_hist / s|` spread |
| ---: | ---: | --- | ---: |
| `0` | `0.000e+00` | `- - -` | `7.77%` |
| `1` | `0.000e+00` | `- - -` | `5.22%` |

Therefore the retained-core synthesis is:

> On the controlled `Fam1` fine-`H` pair, the direct-`dM` matched-history
> effect survives exact null control and common negative sign on both seeds.
> At `H = 0.25`, seed `1` has the larger-magnitude negative `R_hist` in the
> two-point pair.

## Direct Provenance

- [`WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md`](WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md)
- [`WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md`](WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md)
- [`logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt)
- [`logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed1.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed1.txt)
- [`logs/runner-cache/wave_direct_dm_h025_fam1_seed0_control_batch.txt`](../logs/runner-cache/wave_direct_dm_h025_fam1_seed0_control_batch.txt)
- [`logs/runner-cache/wave_direct_dm_h025_fam1_seed1_control_batch.txt`](../logs/runner-cache/wave_direct_dm_h025_fam1_seed1_control_batch.txt)

## Explicit Non-Claims

This note does not claim:

- a coarse-to-fine seed-ordering reversal;
- an uneven late-gain-compression mechanism;
- an `H = 0.25` portability batch;
- a family-wide fine-`H` seed law;
- a refinement-stable amplitude package;
- a weaker-strength, third-seed, or broader-family rule;
- retained provenance for the coarse high/low band rows;
- an audit verdict or direct ledger retag.

## Verification

Run:

```bash
python3 scripts/wave_direct_dm_h025_fam1_fine_pair_synthesis_certificate.py
```

Expected result:

```text
Wave direct-dM H=0.25 Fam1 fine-pair synthesis: PASS
PASS=39 FAIL=0
```

## Audit Request

Please re-audit only the bounded fine-pair synthesis above. The intended safe
outcome, if the auditor agrees, is retained-bounded status for the controlled
Fam1 `H = 0.25` seed0/seed1 fine-pair comparison. The previous coarse-to-fine
mechanism language remains out of scope.
