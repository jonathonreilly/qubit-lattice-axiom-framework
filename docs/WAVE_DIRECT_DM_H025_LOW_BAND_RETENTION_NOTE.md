# Wave Direct-dM H=0.25 Low-Band Retention Note

**Date:** 2026-04-08 (2026-05-28: load-bearing runner repointed to the
seed-1 control batch; coarse H=0.5/0.35 rows scoped as non-load-bearing
continuity context after provenance review).
**Type:** bounded_theorem
**Status:** proposed_retained seed-1 `H = 0.25` continuation, load-borne
by the hardened control-ladder artifact (exact `S = 0` null + weak-field
ladder).
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/wave_direct_dm_h025_fam1_seed1_control_batch.py`](../scripts/wave_direct_dm_h025_fam1_seed1_control_batch.py)

## 2026-05-28 Review Repair (repoint to seed-1 control artifact)

The source claim is the **seed-1** `H = 0.25` point
(`R_hist = -29.47%`), but the previous primary runner was the single-point
`wave_direct_dm_h025_point_runner.py`, whose SHA-pinned cache is the
**default seed-0** invocation (`R_hist = -20.12%`). This repair aligns the
load-bearing runner with the seed-1 source claim without adding a new
axiom, import, or admission:

- **Load-bearing runner repointed** to the retained_bounded
  [`WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md)
  batch `scripts/wave_direct_dm_h025_fam1_seed1_control_batch.py`. Its
  SHA-pinned cache **is the seed-1 `H = 0.25` point** and reproduces this
  note's exact `S = 0.004` row
  (`dM_early = +0.004411`, `dM_late = +0.006255`,
  `delta_hist = -0.001843`, `R_hist = -29.47%`), hardened with the exact
  `S = 0` null and the `S = 0.002/0.004/0.008` weak-field ladder. That
  control note is already a `retained_bounded` one-hop dependency of this
  row.
- **Coarse `H = 0.5 / 0.35` rows scoped as non-load-bearing continuity
  context.** The reference-comparison table below is kept as
  refinement-continuity context for the seed-1 late-gain scale; it is not
  the load-bearing certificate and does not need its own retained_bounded one-hop
  authority. The load-bearing claim is exactly the seed-1 `H = 0.25`
  controlled point.
- The seed-0 single-point runner is demoted to a historical
  cross-seed comparison artifact (it supplies the `R_hist = -20.12%`
  seed-0 figure cited under "What this changes").

This note records the complementary direct `H = 0.25` replay for the
direct-`dM` amplitude-band story:

> Start from the original lower-magnitude reference point
> (`Fam1`, seed `1`, `S = 0.004`) and ask whether the same configuration
> keeps the same branch identity when the matched-history lane is
> refined from `H = 0.5` / `0.35` down to `H = 0.25`.

## Reference comparison (continuity context, non-load-bearing)

All three rows use the same family, seed, and source strength. The
`H = 0.5 / 0.35` rows are kept here as refinement-continuity context
for the seed-1 late-gain scale; the load-bearing certificate is the seed-1
`H = 0.25` controlled point (see the 2026-05-28 repair header).

| H | dM(early) | dM(late) | delta_hist | R_hist | late gain |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.50 | +0.005594 | +0.007491 | -0.001897 | -25.33% | +0.001897 |
| 0.35 | +0.006509 | +0.008134 | -0.001625 | -19.98% | +0.001625 |
| 0.25 | +0.004411 | +0.006255 | -0.001843 | -29.47% | +0.001844 |

Runtime / memory for the `H = 0.25` replay:

- elapsed = `108.16 s`
- peak RSS = `697.8 MB`

## Narrow read

- The matched-history effect survives cleanly at `H = 0.25` on the seed-`1`
  continuation:
  `delta_hist` stays negative and materially nonzero.
- On the current single-family read, the seed-`1` late-gain scale is the more
  refinement-stable one:
  the `H = 0.25` late gain `+0.001844` sits almost exactly on the coarse
  `H = 0.5` / `0.35` seed-`1` values.
- The normalized magnitude does not collapse toward zero or drift up toward
  the old seed-`0` band.
  Instead it lands at `R_hist = -29.47%`, which is slightly stronger than the
  `H = 0.5` seed-`1` reference and no longer supports the old low-band label.

So the honest conclusion is:

> The direct `H = 0.25` historical low-band replay is a bounded continuation of the
> seed-`1` branch at the level of sign plus late-gain difference. The
> matched-history sign survives and the seed-`1` late-gain scale stays close
> to the coarse rows, but the absolute branch responses still drift downward
> at the finer refinement.

## Later hardening

This one-strength replay is now superseded as the main artifact for this pair
by the same-resolution control ladder in
[`WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md):

- exact `S = 0` null
- sign pattern `- - -`
- `|delta_hist / s|` spread `5.22%`

So this note should now be read as the first replay for the
Fam1/seed1 branch under the old naming, not the final control surface.

## What this changes

- The two planned `H = 0.25` validation points have now both landed.
- The old seed ordering from `H = 0.5` / `0.35` does **not** survive the
  first fine-`H` check:
  the former high-band seed-`0` point dropped to `R_hist = -20.12%`, while
  this seed-`1` point stays at `R_hist = -29.47%`.
- On the current two-point, single-family evidence, the refinement issue is
  no longer “does the low band survive?” but “how should the cross-seed
  ordering be described once seed `0` loses most of its extra late gain?”
- The narrow two-point synthesis is now frozen in
  `WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md` as a downstream
  context surface.
- That synthesis keeps the fine-`H` claim at the single-family
  cross-seed-reordering / uneven-late-gain-compression level, not a wider
  portability extension.
- Extra-family, third-seed, and weaker-strength reserve points remain demoted
  until one post-synthesis reserve point is chosen deliberately.

## Artifact chain

Load-bearing (seed-1 control ladder):

- [`scripts/wave_direct_dm_h025_fam1_seed1_control_batch.py`](../scripts/wave_direct_dm_h025_fam1_seed1_control_batch.py) — primary runner; SHA-pinned cache is the seed-1 `H = 0.25` point.
- [`docs/WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM1_SEED1_CONTROL_NOTE.md) — `retained_bounded` one-hop control authority.

Historical / context:

- [`scripts/wave_direct_dm_h025_point_runner.py`](../scripts/wave_direct_dm_h025_point_runner.py) — original single-point replay; its default cache is the **seed-0** comparison point (`R_hist = -20.12%`), kept as the historical cross-seed figure cited under "What this changes", not the load-bearing seed-1 artifact.
- [`logs/2026-04-08-wave-direct-dm-h025-low-band.txt`](../logs/2026-04-08-wave-direct-dm-h025-low-band.txt)
- `docs/WAVE_DIRECT_DM_H025_HIGH_BAND_BOUNDARY_NOTE.md`
- `docs/WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md` — downstream context.
