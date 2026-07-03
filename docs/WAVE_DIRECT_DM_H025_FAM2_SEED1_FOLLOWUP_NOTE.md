# Wave Direct-dM H=0.25 Fam2 Seed1 Follow-Up Note

**Date:** 2026-04-08
**Claim type:** bounded_theorem
**Source boundary:** bounded target replay feeding the controlled `Fam2`
fine-`H` pair surface; not an independent theorem-grade surface or
portability promotion
**Source packet verifier:** [`scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py`](../scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py)
(SUMMARY: WAVE SOURCE PACKET PASS=86 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt)
**Source packet verifier JSON:** [`outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json`](../outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json)

This note records the complementary second-family follow-up after the first
extra-family `Fam2`, seed-`0` boundary on the direct-`dM` matched-history
lane:

> Hold the direct-`dM` setup fixed, keep the first extra-family reserve
> question as narrow as possible, and ask whether the complementary
> `Fam2`, seed `1`, source strength `0.004`, `H = 0.25` replay reproduces the
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
- The stable feature is the seed-`1` late-gain scale, not the old
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
> one-strength replay is not an independent theorem-grade surface, not a
> cross-family theorem, and not an `H = 0.25` portability or amplitude-law
> promotion.

## What this changes

- The narrow second-family question is no longer open:
  the `Fam2` pair now reproduces the same qualitative fine-`H` asymmetry as
  the `Fam1` pair.
- The same `Fam2`, seed `1`, `H = 0.25` replay now also has a same-resolution
  control ladder in
  [`WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md):
  exact zero-source-strength null, sign pattern `- - -`, and
  `|delta_hist / source_strength|` spread `4.25%` over source strengths
  `0.002, 0.004, 0.008`.
- The complementary `Fam2`, seed `0`, `H = 0.25` replay now also has a
  same-resolution control ladder in
  [`WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md):
  exact zero-source-strength null, sign pattern `- - -`, and
  `|delta_hist / source_strength|` spread
  `6.67%`.
- The direct-`dM` `H = 0.25` story is therefore no longer bounded to one
  strength on the second family, but it is still bounded to two families
  and one fine-`H` family pair per family.
- The portable part of the read is the seed-conditioned late-gain ordering,
  not a stable `R_hist` band.
- The narrow `Fam2` pair synthesis now exists in
  [`WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md`](./WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md).
- The next honest move is to compare that controlled `Fam2` pair against the
  controlled `Fam1` pair before any `Fam3`, third-seed, or weaker-strength
  widening.

## 2026-06-04 target-specific runner repair

The previous registered runner for this note was the reusable point runner,
whose defaults are `Fam1`, seed `0`.  The row-specific repair now adds
[`scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`](../scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py),
which fixes exactly the target invocation:

- family: `Fam2`
- seed: `1`
- `H = 0.25`
- source strength: `0.004`

The runner recomputes the replay and checks the archived values:
`dM(early)=+0.003777`, `dM(late)=+0.005814`,
`delta_hist=-0.002037`, `R_hist=-35.03%`, and late gain `+0.002037`.
It also records the dependency surface used for re-audit: the `Fam2`
seed-`0`/seed-`1` control notes, the `Fam2` pair synthesis, the `Fam1`
fine-pair synthesis, and the coarse portability batch.  This repair is a
cache/scope repair only; audit retains authority over any effective status.

```yaml
target_claim_type: bounded_theorem
proposed_claim_type: bounded_theorem
runner_path: scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
claim_boundary: "Exact Fam2 seed1 H=0.25 replay feeding controlled pair/batch surface; not an independent theorem-grade surface or portability law."
audit_authority: independent audit lane only
```

## 2026-06-06 Source Packet Exposure Repair

The current audit blocker asks for the complete untruncated helper source
behind `measure_dm`, especially [`scripts/wave_retardation_continuum_limit.py`](../scripts/wave_retardation_continuum_limit.py)
with `field_at`, `prop_beam`, and `cz`. The source packet is now explicit:

- Target-specific runner: [`scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`](../scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py)
- Target-specific runner cache: [`logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt`](../logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt)
- Generic point runner: [`scripts/wave_direct_dm_h025_point_runner.py`](../scripts/wave_direct_dm_h025_point_runner.py)
- Generic point runner cache: [`logs/runner-cache/wave_direct_dm_h025_point_runner.txt`](../logs/runner-cache/wave_direct_dm_h025_point_runner.txt)
- Matched-history helper: [`scripts/wave_direct_dm_matched_history_probe.py`](../scripts/wave_direct_dm_matched_history_probe.py)
- Matched-history helper cache: [`logs/runner-cache/wave_direct_dm_matched_history_probe.txt`](../logs/runner-cache/wave_direct_dm_matched_history_probe.txt)
- Wave-retardation helper: [`scripts/wave_retardation_continuum_limit.py`](../scripts/wave_retardation_continuum_limit.py)
- Wave-retardation helper cache: [`logs/runner-cache/wave_retardation_continuum_limit.txt`](../logs/runner-cache/wave_retardation_continuum_limit.txt)

The source packet verifier checks that these paths are linked from this note,
that the target runner is fixed to `Fam2`, seed `1`, `H=0.25`, and source
strength `S_PHYS`, that `measure_dm` imports and calls the wave-retardation
helpers, that `field_at`, `prop_beam`, `cz`, `solve_wave`, and `grow` are
present in the untruncated helper source, and that all listed caches are
SHA-fresh and successful. This does not set an audit verdict; it makes the
bounded target replay reauditable with the missing helper source exposed.

Current source-packet output:

```text
SUMMARY: WAVE SOURCE PACKET PASS=86 FAIL=0
```

## Artifact chain

- [`scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`](../scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py)
- [`scripts/wave_direct_dm_h025_point_runner.py`](../scripts/wave_direct_dm_h025_point_runner.py)
- [`logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt`](../logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt)
- [`outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json`](../outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json)
- [`scripts/wave_direct_dm_matched_history_probe.py`](../scripts/wave_direct_dm_matched_history_probe.py)
- [`logs/runner-cache/wave_direct_dm_matched_history_probe.txt`](../logs/runner-cache/wave_direct_dm_matched_history_probe.txt)
- [`scripts/wave_retardation_continuum_limit.py`](../scripts/wave_retardation_continuum_limit.py)
- [`logs/runner-cache/wave_retardation_continuum_limit.txt`](../logs/runner-cache/wave_retardation_continuum_limit.txt)
- [`scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py`](../scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py)
- [`logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt)
- [`outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json`](../outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json)
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

## 2026-06-06 transitive helper source-packet repair

This repair responds to the artifact-completeness blocker asking for the
complete untruncated `scripts/wave_retardation_continuum_limit.py` helper
source, especially `field_at`, `prop_beam`, and `cz`, or an independent
certificate for the `measure_dm` computation. It does not promote this note or
change the bounded target-replay claim boundary; independent audit owns any
ledger/status movement.

The source-packet manifest now checks that the restricted packet exposes the
exact target runner, the transitive `measure_dm` source/cache, and the
wave-retardation helper source/cache. It verifies SHA-fresh cache headers for:

- `scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py`
- `scripts/wave_direct_dm_matched_history_probe.py`
- `scripts/wave_retardation_continuum_limit.py`

The same manifest checks source markers for the full `measure_dm` path:
`measure_dm` calls `solve_wave`, `prop_beam`, and `cz`, while the continuum
helper supplies `field_at`, `prop_beam`, `cz`, `solve_wave`, and the fixed
`S_PHYS = 0.004` source-strength constant.
The target-specific runner cache also now prints an independent
`MEASURE_DM_SOURCE_PACKET=PASS` certificate tying those helper sources and
SHA-fresh caches directly to the row-specific replay.
