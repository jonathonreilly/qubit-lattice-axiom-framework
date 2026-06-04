# Wave Direct-dM H=0.25 Fam2 Seed1 Follow-Up Note

**Date:** 2026-04-08
**Status:** bounded target replay feeding the controlled `Fam2` fine-`H`
pair surface; not an independent retained theorem or portability promotion

This note records the complementary second-family follow-up after the first
extra-family `Fam2`, seed-`0` boundary on the direct-`dM` matched-history
lane:

> Hold the direct-`dM` setup fixed, keep the first extra-family reserve
> question as narrow as possible, and ask whether the complementary
> `Fam2`, seed `1`, `S = 0.004`, `H = 0.25` replay reproduces the
> `Fam1`-style cross-seed reordering or whether the second family only
> carries the seed-`0` boundary.

## Reference comparison

All three rows use the same family, seed, and source strength.

| H | dM(early) | dM(late) | delta_hist | R_hist | late gain |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.50 | +0.005425 | +0.007362 | -0.001937 | -26.31% | +0.001937 |
| 0.35 | +0.007172 | +0.009233 | -0.002061 | -22.32% | +0.002061 |
| 0.25 | +0.003777 | +0.005814 | -0.002037 | -35.03% | +0.002037 |

Runtime / memory for the `H = 0.25` replay:

- elapsed = `111.97 s`
- peak RSS = `696.1 MB`

## Narrow read

- The matched-history effect survives cleanly on the complementary
  second-family seed-`1` replay:
  `delta_hist` stays negative and materially nonzero.
- The key retained feature is the seed-`1` late-gain scale, not the old
  coarse normalized band.
  The `H = 0.25` late gain `+0.002037` sits almost exactly on the coarse
  `Fam2`, seed-`1` values `+0.001937` and `+0.002061`.
- That distinguishes the replay sharply from the already-landed
  `Fam2`, seed-`0` boundary, where the same family at `H = 0.25` had only
  `+0.001576` of extra late gain.
- But this is still not a stable fine-`H` amplitude-band continuation.
  The normalized magnitude moves to `R_hist = -35.03%`, more negative than
  the coarse seed-`1` rows, because both `dM(early)` and `dM(late)` compress
  while the late-minus-early separation stays nearly fixed.

So the honest conclusion is:

> The second-family seed-`1` replay is a bounded target datapoint for the
> controlled `Fam2` fine-`H` pair: on `Fam2`, the `H = 0.25`
> seed-conditioned late-gain asymmetry survives at the archived point and is
> consistent with the controlled pair synthesis. But this selected
> one-strength replay is not an independent retained theorem, not a
> cross-family theorem, and not an `H = 0.25` portability or amplitude-law
> promotion.

## What this changes

- The narrow second-family question is no longer open:
  the `Fam2` pair now reproduces the same qualitative fine-`H` asymmetry as
  the `Fam1` pair.
- The same `Fam2`, seed `1`, `H = 0.25` replay now also has a same-resolution
  control ladder in
  [`WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md):
  exact `S = 0` null, sign pattern `- - -`, and `|delta_hist / s|` spread
  `4.25%` over `S = 0.002, 0.004, 0.008`.
- The complementary `Fam2`, seed `0`, `H = 0.25` replay now also has a
  same-resolution control ladder in
  [`WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md):
  exact `S = 0` null, sign pattern `- - -`, and `|delta_hist / s|` spread
  `6.67%`.
- The direct-`dM` `H = 0.25` story is therefore no longer bounded to one
  strength on the second family, but it is still bounded to two families
  and one fine-`H` family pair per family.
- The portable part of the read is the seed-conditioned late-gain ordering,
  not a stable `R_hist` band.
- The narrow `Fam2` pair synthesis now exists in
  [`WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md).
- The next honest move is to compare that controlled `Fam2` pair against the
  retained `Fam1` pair before any `Fam3`, third-seed, or weaker-strength
  widening.

## 2026-06-04 target-specific runner repair

The previous registered runner for this note was the reusable point runner,
whose defaults are `Fam1`, seed `0`.  The row-specific repair now adds
[`scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`](../scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py),
which fixes exactly the target invocation:

- family: `Fam2`
- seed: `1`
- `H = 0.25`
- `S = 0.004`

The runner recomputes the replay and checks the archived values:
`dM(early)=+0.003777`, `dM(late)=+0.005814`,
`delta_hist=-0.002037`, `R_hist=-35.03%`, and late gain `+0.002037`.
It also records the dependency surface used for re-audit: the `Fam2`
seed-`0`/seed-`1` control notes, the `Fam2` pair synthesis, the `Fam1`
fine-pair synthesis, and the coarse portability batch.  This repair is a
cache/scope repair only; audit retains authority over any effective status.

## Artifact chain

- [`scripts/wave_direct_dm_h025_point_runner.py`](../scripts/wave_direct_dm_h025_point_runner.py)
- [`scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`](../scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py)
- [`logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt`](../logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt)
- [`outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json`](../outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json)
- [`logs/2026-04-08-wave-direct-dm-h025-fam2-seed1.txt`](../logs/2026-04-08-wave-direct-dm-h025-fam2-seed1.txt)
- [`docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md)
- `docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md`
- [`docs/WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md)
- `docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_BOUNDARY_NOTE.md`
- `docs/WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md`
- `docs/WAVE_DIRECT_DM_PORTABILITY_BATCH_NOTE.md`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [wave_direct_dm_h025_two_point_synthesis_note](WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md)
- [wave_direct_dm_portability_batch_note](WAVE_DIRECT_DM_PORTABILITY_BATCH_NOTE.md)
