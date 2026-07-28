# Wave Direct-dM H=0.25 Seed0 Cross-Family Bounded Synthesis Note

**Date:** 2026-04-08

**Revised:** 2026-07-26

**Type:** bounded_theorem

**Claim type:** bounded_theorem

**Status:** bounded finite cross-note proposition on the exact SHA-pinned
seed-`0`, `H=0.25` source packets. The proposition requires independent
re-audit and carries no retained-status assignment.

**Status authority:** source-note proposal only; the independent audit lane sets
`audit_status` and `effective_status`.

**Primary runner:**
[`scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py`](../scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py)

## Claim scope

Fix the already-computed coordinate `H = 0.25`, seed `0`, and compare the
`S = 0.004` rows in the two SHA-pinned source transcripts below.
On exactly those two rows:

1. both `delta_hist` values are negative;
2. `Fam2` is deeper than `Fam1` both in `|delta_hist|` and in the normalized
   value `R_hist`; and
3. each row belongs to the same transcript's configured strength ladder, whose
   finite checks are an exact `S = 0` null, a negative sign at all three
   nonzero strengths, and the reported finite
   `|delta_hist/S|` spread.

This is a finite cross-note implication. It does not derive or select
`H = 0.25`, seed `0`, either row magnitude, an amplitude law, or a portability
law. The fixed `H`, seed, family labels, and strength are coordinates of the
bounded claim, not fitted inputs used to match an external target.

## Frozen source packets

The two source notes remain the load-bearing authority edges for audit lineage
and interpretation. Their mutable audit grades are not proof inputs and are
not snapshotted here. The two source runners are imported by the primary
certificate so their complete source enters its restricted audit packet; the
expensive computations are not rerun by the short certificate. The exact
transcripts are SHA-pinned and parsed.

| input | source authority | source computation and SHA-256 | frozen transcript and SHA-256 | role here |
| --- | --- | --- | --- | --- |
| `Fam1`, seed `0`, `H=0.25` ladder | [Fam1 seed-0 control note](WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md) | [`wave_direct_dm_h025_fam1_seed0_control_batch.py`](../scripts/wave_direct_dm_h025_fam1_seed0_control_batch.py), `ad4671d0c347b6ec9c6c7602e83e262986425306bf7b6018893f653bf3f7b183` | [`2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt), `487297bd521bea04dbafdce12e3c59d8faa9acb59e169b9982a6a31104be0737` | supplies row 1, its null, sign pattern, and spread |
| `Fam2`, seed `0`, `H=0.25` ladder | [Fam2 seed-0 control note](WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md) | [`wave_direct_dm_h025_fam2_seed0_control_batch.py`](../scripts/wave_direct_dm_h025_fam2_seed0_control_batch.py), `06127f24dfc9a2efd0e86c1e7a921e10e423e7bbb083d973ca7d10902dbeb22d` | [`2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt`](../logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt), `9a14b49586473ad0f5ef3a81b559fee26dfc85156e9e9b160390d8e1c2a1c619` | supplies row 2, its null, sign pattern, and spread |

The primary runner checks the source-runner coordinates, requires the exact
runner and transcript SHA-256 pins above before parsing, recomputes every
ladder summary used here from the parsed rows, and performs the finite
comparison below. It contains no expected direct-`dM` magnitudes or expected
`R_hist` values.

## Cross-note derivation

For family `F` and strength `S`, use the quantities already defined and
printed in each source transcript:

```text
D_F(S) = dM_early,F(S) - dM_late,F(S) = delta_hist_F(S),
Q_F(S) = D_F(S) / S                       (S > 0),
R_F(S) = D_F(S) / max(|dM_early|, |dM_late|).
```

The nonzero configured ladder is
`L = {0.002, 0.004, 0.008}`. Its source-reported scaled spread is

```text
spread_F = (max_{S in L}|Q_F(S)| - min_{S in L}|Q_F(S)|)
           / mean_{S in L}|Q_F(S)|.
```

The parsed frozen inputs are:

| family | `D_F(0)` | sign on `L` | `spread_F` | `dM_early(0.004)` | `dM_late(0.004)` | `D_F(0.004)` | `R_F(0.004)` |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `Fam1` | `0.000000` | `- - -` | `7.77%` | `+0.004989` | `+0.006246` | `-0.001256` | `-20.12%` |
| `Fam2` | `0.000000` | `- - -` | `6.67%` | `+0.005393` | `+0.006969` | `-0.001576` | `-22.61%` |

The displayed `dM`, `D_F`, and `Q_F` entries are rounded to six decimal
places, while `R_F` is rounded to two decimal places. The source runners
compute these quantities from unrounded state. The primary certificate checks
all three identities against the displayed values using the worst-case
half-unit rounding intervals; it does not demand exact equality between
independently rounded columns.

The conclusion is immediate from the table:

```text
D_Fam1(0.004) < 0,
D_Fam2(0.004) < 0,
|D_Fam2(0.004)| = 0.001576 > 0.001256 = |D_Fam1(0.004)|,
R_Fam2(0.004) = -22.61% < -20.12% = R_Fam1(0.004).
```

The exact nulls, common negative ladder signs, and finite spreads are recomputed
from the same two frozen ladders. Thus the selected rows share negative sign
and common depth ordering while satisfying the declared finite checks on their
respective configured ladders.

## Bounded-proposition classification

The source computations are the load-bearing configured numerical work for the
two family/seed ladders. This note does not redo that work and does not
compare either output with an experimental or hand-selected target. It reads
two frozen artifact inputs and applies sign and order relations.

Reading, SHA-pinning, and comparing the two frozen source packets supports
the exact finite proposition stated above. Its theorem scope is only the
conditional sign/order implication over those two frozen rows and their
declared configured ladders. It is not a structural law, a surface-selection
result, or a portability theorem.

There is no target value in the runner and no observed or fitted comparator in
the claim. The independent audit lane, rather than this source note, assigns
the resulting evidence class and effective status.

## Audit repair context

The latest applicable archived audit's re-audit instruction is quoted
verbatim:

> Re-check the exact runner/log SHA-256 pins and retained-grade dependency statuses if either upstream packet changes.

This is the minimal runner-storage repair that preserves the two source-note
authority edges. It types the evidence-bearing finite implication as
`bounded_theorem` and retains exact log and parent-runner SHA-256 pins so the
word “frozen” is enforced before either transcript is parsed. Independent
re-audit must re-evaluate both dependency statuses before any retained
disposition.

The distinction is scope, not rhetoric: a structural claim explaining the
magnitudes or selecting `H = 0.25` and seed `0` would require a different
derivation. No such structural claim appears here.

## What does and does not survive

What survives is only the finite proposition

> At `H = 0.25`, seed `0`, and `S = 0.004`, the frozen `Fam1` and `Fam2`
> rows both have negative `delta_hist`; `Fam2` is deeper than `Fam1`; and
> both rows belong to the pinned configured ladders with exact null, common
> negative nonzero sign, and the stated finite scaled spread.

This note does **not** claim:

- a stable amplitude band or amplitude law;
- a family-independent `H = 0.25` result;
- a derivation of the row magnitudes or of the chosen surface;
- a statement about `Fam3`, another seed, another `H`, or another strength;
- a mechanism-level explanation of the cross-family ordering.
- physical weak-field control beyond the exact finite ladder checks stated
  above.

In particular, `Fam1` and `Fam2` have different normalized magnitudes. The
comparison is evidence against treating the two rows as a universal amplitude.

## Executable certificate

Run:

```bash
python3 scripts/wave_direct_dm_h025_seed0_crossfamily_assertions.py
```

The checked transcript is
[`outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-07-10.txt`](../outputs/wave_direct_dm_h025_seed0_crossfamily_assertions_2026-07-10.txt).
The runner prints, among its computed values:

- `WAVE_DIRECT_DM_H025_SEED0_SOURCE_RUNNERS_IMPORTED=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_ARTIFACT_SHA256_PINS=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_CLAIM_TYPE=BOUNDED_THEOREM`
- `WAVE_DIRECT_DM_H025_SEED0_ROLE=SHA_PINNED_TWO_ROW_CONDITIONAL_NUMERICAL_PROPOSITION`
- `WAVE_DIRECT_DM_H025_SEED0_SHARED_SIGN=negative`
- `WAVE_DIRECT_DM_H025_SEED0_COMMON_ORDERING=Fam2_deeper_than_Fam1_at_strength_0.004`
- `WAVE_DIRECT_DM_H025_SEED0_DISPLAY_IDENTITIES_CHECKED=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_CONFIGURED_LADDER_CHECKS=TRUE`
- `WAVE_DIRECT_DM_H025_SEED0_SCOPE=EXACT_TWO_SHA_PINNED_SEED0_H025_LADDERS`
- `WAVE_DIRECT_DM_H025_SEED0_INDEPENDENT_REAUDIT_REQUIRED=TRUE`

This bounded source proposition requires independent re-audit. It does not
inherit a retained verdict from the existence or prior grading of either
source artifact.
