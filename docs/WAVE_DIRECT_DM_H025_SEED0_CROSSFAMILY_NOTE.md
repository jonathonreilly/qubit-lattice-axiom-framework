# Wave Direct-dM H=0.25 Seed0 Cross-Family Compression Note

**Date:** 2026-04-08
**Status:** bounded numerical compression on the controlled seed-`0` fine-`H` surface
**Type:** bounded_theorem
**Audit ceiling:** class-G numerical-match compression; not a structural theorem on this surface
**Runner:** [`scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py`](../scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py)

**Audit class:** The load-bearing step is a numerical compression of two
preselected control rows at the tuned input scale `H = 0.25` with the
preselected seed `0`. Review classifies that step as derivation class
`(G)` (numerical match at a tuned input scale). This source note does
not set or predict an audit verdict. It only records that promotion to
a structural theorem would require a class `(C)` first-principles
derivation of the row magnitudes from `Cl(3)` on `Z^3`, which is not
attempted here and is explicitly excluded from this note's scope.

This note compresses the controlled `H = 0.25` seed-`0` evidence across the
two families that currently have it:

## Source boundary (2026-06-12)

**Boundary:** numerical-match / bounded support only. Effective status is
audit-derived; this source records only the claim boundary.

The load-bearing comparison uses two preselected simulation rows at the tuned
`H = 0.25`, seed-`0` surface. This note may be cited only for the frozen
Fam1/Fam2 seed-0 sign/order/magnitude comparison. It may not be cited as a
derivation of the direct-dM magnitudes, the Fam2-deeper-than-Fam1 ordering, a
family-wide law, a third-family transfer, or a structural explanation of why
`H = 0.25` and seed `0` are forced.

Promotion beyond numerical-match support requires a separate class-C
first-principles magnitude/order derivation or a retained theorem selecting
the `H = 0.25`, seed-`0` surface.

> Keep the controlled `Fam1`, seed `0`, `H = 0.25` control ladder together
> with the controlled `Fam2`, seed `0`, `H = 0.25` control ladder, and ask
> what survives if we hold the seed fixed but compare the same fine-`H`
> row across families.

## Evidence surface

The seed-`0` source rows are:

| family | `H` | `dM(early)` | `dM(late)` | `delta_hist` | `R_hist` | late gain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `Fam1` | `0.25` | `+0.004989` | `+0.006246` | `-0.001256` | `-20.12%` | `+0.001257` |
| `Fam2` | `0.25` | `+0.005393` | `+0.006969` | `-0.001576` | `-22.61%` | `+0.001576` |

Both rows are now controlled at the same resolution:

- exact `S = 0` null
- sign pattern `- - -`
- bounded `|delta_hist / s|` spread

Per-family summaries:

| family | null max `|delta_hist|` | sign pattern | `|delta_hist / s|` spread |
| --- | ---: | --- | ---: |
| `Fam1` | `0.000e+00` | `- - -` | `7.77%` |
| `Fam2` | `0.000e+00` | `- - -` | `6.67%` |

The runner is log-backed: it reads the frozen control logs listed in the
artifact chain and asserts the two-row compression table, the exact nulls,
the nonzero negative sign pattern, the weak-field spread bounds, and the
selected-row ordering.  It deliberately does not rerun the expensive fine-`H`
controls and does not certify any family-wide law.

## What the seed-0 surface does not say

- not a stable amplitude law
- not a family-independent `H = 0.25` portability result
- not a third-family extrapolation

The common sign stays negative, but the normalized magnitudes remain
family-dependent.
`Fam1` is the shallower weak branch; `Fam2` is the deeper weak branch.

## What actually survives

The cleanest bounded statement is:

> seed `0` occupies the lower-magnitude side of the fine-`H` direct-`dM`
> story in both families, and the two families sit at different depths
> inside that weak branch: `Fam1` is controlled near `R_hist ~ -20%`,
> while `Fam2` is controlled near `R_hist ~ -23%`.

That is a same-seed cross-family compression result, not a portability law.

## Boundary

This note does **not** claim:

- that the seed-`0` rows define a stable amplitude band
- that the direct-`dM` lane has a family-wide fine-`H` law
- that the fine-`H` evidence extends to `Fam3`

The honest boundary is:

> the seed-`0` fine-`H` surface is consistent across families in sign,
> ordering, and weak-field control, but it still does not define a stable
> amplitude law or a portability claim beyond `Fam1`/`Fam2`.

## Assertion closeout

Primary runner:

- [`scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py`](../scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py)

Transcript:

- [`outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-06.txt`](../outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-06.txt)
- [`outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-16.txt`](../outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-16.txt)

The runner prints:

- `WAVE_DIRECT_DM_H025_SEED0_CROSSFAMILY_ASSERTIONS=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_SHARED_SIGN=negative`
- `WAVE_DIRECT_DM_H025_SEED0_COMMON_ORDERING=Fam2_deeper_than_Fam1_at_strength_0.004`
- `WAVE_DIRECT_DM_H025_SEED0_WEAK_FIELD_CONTROL=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_PORTABILITY_LAW=FALSE`
- `WAVE_DIRECT_DM_H025_STABLE_AMPLITUDE_LAW=FALSE`
- `RESIDUAL_SCOPE=fam3_and_family_wide_portability_not_claimed`

## Artifact chain

- Source log: [`logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt)
- Source log: [`logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt)
- Primary assertion runner: [`scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py`](../scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py)
- Assertion transcript: [`outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-06.txt`](../outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-06.txt)
- Assertion transcript: [`outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-16.txt`](../outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-05-16.txt)
- Context note: [`docs/WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md`](WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md)
- Context note: [`docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md`](WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md)
- Context note: [`docs/WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md`](WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md)
- Context note: [`docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md`](WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md)
- Context note: [`docs/WAVE_DIRECT_DM_H025_HIGH_BAND_BOUNDARY_NOTE.md`](WAVE_DIRECT_DM_H025_HIGH_BAND_BOUNDARY_NOTE.md)
- Context note: [`docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_BOUNDARY_NOTE.md`](WAVE_DIRECT_DM_H025_FAM2_SEED0_BOUNDARY_NOTE.md)

## Audit dependency repair links

This graph-bookkeeping section records the explicit upstream-source
dependency edges the prior auditor flagged as missing
("the source rows and runner/log artifacts are not registered as audit
dependencies"). It does not change the audited claim scope or promote
this note above its class-`(G)` ceiling. Each link names the upstream
note plus the source log that backs the corresponding row in the
compression table.

- Fam1 seed-0 control row (table row 1): upstream note
  [wave_direct_dm_h025_fam1_seed0_control_note](WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md);
  source log
  [`logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt);
  control-batch runner
  [`scripts/wave_direct_dm_h025_control_batch.py`](../scripts/wave_direct_dm_h025_control_batch.py).
- Fam2 seed-0 control row (table row 2): upstream note
  [wave_direct_dm_h025_fam2_seed0_control_note](WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md);
  source log
  [`logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt);
  control-batch runner
  [`scripts/wave_direct_dm_h025_control_batch.py`](../scripts/wave_direct_dm_h025_control_batch.py).

The assertion runner
[`scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py`](../scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py)
ingests both source logs directly (`parse_log` reads them by path) and
fails fast if either log is missing or its parsed rows disagree with the
compression table above. The audit can therefore trace each row in the
table back to a specific line in a specific frozen log via the listed
dependency edges.

## Why this note cannot promote to a structural theorem

For audit-graph transparency, the structural reason promotion is blocked
on the registered scope:

- The conclusion ("Fam2 sits deeper than Fam1 at the selected weak-field
  strength on the seed-0 fine-`H` surface") is a comparison of two
  simulation outputs taken at the tuned input scale `H = 0.25`.
- Structural-theorem treatment would require class `(C)`
  first-principles compute (or genuine class `(A)` algebraic closure
  over independent retained inputs).
- Deriving the magnitudes of `R_hist` from `Cl(3)` on `Z^3` would be a
  separate structural theorem in a different note; that theorem is not
  attempted here and is explicitly out of scope.
- The same exclusion applies to any "family-wide portability law" that
  would extend the compression to `Fam3` or to a continuous family of
  `H` values.

This revision therefore registers the dependency edges and keeps the
scope bounded to the two-row numerical compression. The independent
audit lane remains responsible for the audit verdict.
