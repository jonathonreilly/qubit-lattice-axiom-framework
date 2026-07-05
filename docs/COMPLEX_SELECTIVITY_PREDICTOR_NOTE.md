# Complex Selectivity Predictor Note

**Date:** 2026-04-06; source-scope repair 2026-06-10
**Status:** bounded narrow predictor card for complex-action survival on structured families
**Claim type:** bounded_theorem

**Source-scope repair (2026-06-10):**
This note is a bounded comparison card over live one-hop authorities. It no
longer consumes the archived original-grown-basin packet or a broad nearby-row
claim. The positive grown-row entry is scoped to the Claude grown-row companion,
and the fifth-family entry is scoped to the repaired drift-0.20 sampled pair.
The runner still renders a hard-coded comparison table, so this row should be
reviewed as a bounded comparison card, not as an independent computation or a
status promotion. This source repair applies no audit verdict.

## Artifact Chain

- [`scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py`](../scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py)
- [`logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt`](../logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt)
- family cards:
  - [`CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md)
  - [`SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md)
  - [`SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md`](ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md)
  - [`THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`FIFTH_FAMILY_COMPLEX_NOTE.md`](FIFTH_FAMILY_COMPLEX_NOTE.md)
  - [`FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md)

## Question

What is the smallest review-safe discriminator for when a complex-action
companion survives on a structured family?

## Comparison

| family | retained complex | exact gamma=0 | anchor crossover | basin shape | discriminator note |
| --- | --- | --- | --- | --- | --- |
| Claude grown-row companion | yes | yes | yes on the scoped row | single grown row | anchor-local crossover survives on the scoped grown row |
| Second-family complex | yes | yes | yes on the anchor row | tiny basin | exact gamma=0 + Born proxy + crossover survive narrowly |
| Alt connectivity family | no | yes | no | bounded sign-law basin only | sign-law survives, complex branch does not |
| Third grown family | no | yes | not stable across drift window | bounded drift basin | crossover is seed-selective and drift-sensitive; not retained |
| Fourth family quadrant | no | yes | no | narrow seed-selective sign basin | complex response stays boundary-like despite clean controls |
| Fifth family radial | yes | yes | yes on the drift-0.20 sampled pair | drift-selective sampled pair | crossover survives only on the drift-0.20 sampled rows |

## Safe Read

- exact gamma=0 baseline is necessary, but not sufficient
- signed-source portability and weak-field linearity do not predict complex survival by themselves
- support width and seed selectivity are useful context, but they do not separate the positive families from the diagnosed boundaries cleanly
- the smallest stable discriminator we found is the anchor-local crossover: exact gamma=0 baseline plus `TOWARD -> AWAY` on the scoped or repaired sampled row

## Exact Mismatch

- the Claude grown row and fifth-family radial slice retain the crossover only on their scoped/repaired sampled surfaces
- the second-family complex slice retains it on the anchor row but loses it in the tighter boundary window
- the alt, third, and fourth families all fail the same crossover test in structurally different ways

## Final Verdict

**bounded narrow predictor candidate: complex-action survival requires an anchor-local crossover on the scoped or repaired sampled row; coarser basin geometry does not predict it**

## Citation chain and repair path (2026-06-10)

The active source table is scoped to the live one-hop authorities below. The
runner renders this comparison table; it does not independently derive the
family rows.

| Cited authority | File / log | Role on this row |
|---|---|---|
| Active runner | [`scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py`](../scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py) | renders the hard-coded comparison rows in §Comparison |
| Runner cache | [`logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt`](../logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt) | cache replay verifying the rendered table |
| Claude grown-row companion | [`CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md) | supplies the scoped grown-row complex-action survival row |
| Second family complex | [`SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md) | supplies the second-family anchor-row complex retention |
| Second family boundary | [`SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the tighter-window boundary detail |
| Alt complex failure | [`ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md`](ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md) | supplies the alt-family complex-action failure |
| Third family complex boundary | [`THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the third-family complex boundary diagnosis |
| Fourth family complex boundary | [`FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the fourth-family complex boundary diagnosis |
| Fifth family complex repaired packet | [`FIFTH_FAMILY_COMPLEX_NOTE.md`](FIFTH_FAMILY_COMPLEX_NOTE.md) | supplies the repaired drift-0.20 companion pair |
| Fifth family complex boundary | [`FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the fifth-family sampled-row boundary table |

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [grown_transfer_basin_note](GROWN_TRANSFER_BASIN_NOTE.md)
