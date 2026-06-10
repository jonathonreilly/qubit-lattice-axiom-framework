# Complex Selectivity Predictor Note

**Date:** 2026-04-06; source-scope repair 2026-06-10
**Status:** bounded narrow predictor card for complex-action survival on structured families
**Claim type:** bounded_theorem

**Audit-repair perimeter (2026-06-10):**
The 2026-06-10 conditional audit found that the prior "Original grown
basin" row still claimed nearby-row/local-neighborhood support not closed by
the supplied Claude grown-row authority. This repair takes the narrowing path:
the comparison row is now the live `Claude retained grown row`, scoped to
the retained `drift = 0.2`, `restore = 0.7`, seeds `0` and `1` authority.
The source no longer consumes the archived original-grown-basin note or claims
a complex-action nearby-row neighborhood from it.

The fifth-family row is also updated to the repaired drift-0.20 sampled
companion pair, matching `FIFTH_FAMILY_COMPLEX_NOTE.md`,
`FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`, and the current targeted runner.
This source repair does not apply an audit verdict or promote status; it only
aligns the hard-coded comparison table with live one-hop authorities for
re-audit.

## Artifact Chain

- [`scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py`](../scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py)
- [`logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt`](../logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt)
- retained family cards:
  - [`docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md)
  - [`docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md)
  - [`docs/SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`docs/ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md`](ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md)
  - [`docs/THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`docs/FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md)
  - [`docs/FIFTH_FAMILY_COMPLEX_NOTE.md`](FIFTH_FAMILY_COMPLEX_NOTE.md)
  - [`docs/FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md)

## Question

What is the smallest review-safe discriminator for when a complex-action
companion survives on a structured family?

## Comparison

| family | retained complex | exact gamma=0 | anchor crossover | basin shape | discriminator note |
| --- | --- | --- | --- | --- | --- |
| Claude retained grown row | yes | yes | yes on the retained row | single retained grown row | anchor-local crossover survives on the retained grown row |
| Second-family complex | yes | yes | yes on the anchor row | tiny basin | exact gamma=0 + Born proxy + crossover survive narrowly |
| Alt connectivity family | no | yes | no | bounded sign-law basin only | sign-law survives, complex branch does not |
| Third grown family | no | yes | not stable across drift window | bounded drift basin | crossover is seed-selective and drift-sensitive; not retained |
| Fourth family quadrant | no | yes | no | narrow seed-selective sign basin | complex response stays boundary-like despite clean controls |
| Fifth family radial | yes | yes | yes on the drift-0.20 sampled pair | drift-selective sampled pair | crossover survives only on the drift-0.20 sampled rows |

## Safe Read

- exact gamma=0 baseline is necessary, but not sufficient
- signed-source portability and weak-field linearity do not predict complex survival by themselves
- support width and seed selectivity are useful context, but they do not separate the positive families from the diagnosed boundaries cleanly
- the smallest stable discriminator we found is the anchor-local crossover: exact gamma=0 baseline plus `TOWARD -> AWAY` on the retained or repaired sampled row

## Exact Mismatch

- the Claude grown row and fifth-family radial slice retain the crossover only on their narrow retained/repaired sampled surfaces
- the second-family complex slice retains it on the anchor row but loses it in the tighter boundary window
- the alt, third, and fourth families all fail the same crossover test in structurally different ways

## Final Verdict

**bounded narrow predictor candidate: complex-action survival requires an anchor-local crossover on the retained or repaired sampled row; coarser basin geometry does not predict it**

## Citation chain and repair path (2026-06-10)

The active source table is now scoped to the live one-hop authorities below.
The runner still renders a hard-coded comparison table; this row should be
re-audited as a bounded comparison card, not as an independent computation.

| Cited authority | File / log | Role on this row |
|---|---|---|
| Active runner | [`scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py`](../scripts/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.py) | renders the hard-coded comparison rows in §Comparison |
| Runner cache | [`logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt`](../logs/runner-cache/COMPLEX_SELECTIVITY_PREDICTOR_SCAN.txt) | cache replay verifying the rendered table |
| Claude retained grown row | [`docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md) | supplies the retained grown-row complex-action survival row |
| Second family complex | [`docs/SECOND_GROWN_FAMILY_COMPLEX_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_NOTE.md) | supplies the second-family anchor-row complex retention |
| Second family boundary | [`docs/SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](SECOND_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the tighter-window boundary detail |
| Alt complex failure | [`docs/ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md`](ALT_CONNECTIVITY_FAMILY_COMPLEX_FAILURE_NOTE.md) | supplies the alt-family complex-action failure |
| Third family complex boundary | [`docs/THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](THIRD_GROWN_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the third-family complex boundary diagnosis |
| Fourth family complex boundary | [`docs/FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FOURTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the fourth-family complex boundary diagnosis |
| Fifth family complex repaired packet | [`docs/FIFTH_FAMILY_COMPLEX_NOTE.md`](FIFTH_FAMILY_COMPLEX_NOTE.md) | supplies the repaired drift-0.20 companion-pair row |
| Fifth family complex boundary | [`docs/FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md) | supplies the fifth-family sampled-row boundary table |
