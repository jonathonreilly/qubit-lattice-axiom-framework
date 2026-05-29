# Handoff

## What Changed

This branch repairs the PMNS TM2 conditional row by narrowing the maximal-CP consequence to `c12*s12*s13 != 0`.

The runner now has 22 passing checks and includes the audit-named endpoint `sin^2(theta_13)=2/3`, where `c12=0` and CP is not forced.

## Audit Queue Result

After `bash docs/audit/scripts/run_pipeline.sh`:

- row: `pmns_tm2_residual_consequence_bounded_note_2026-05-26`
- audit status: `unaudited`
- effective status: `unaudited`
- queue rank: 907
- ready: true
- open dependencies: none

## Reviewer Notes

The repair is intentionally narrow. It preserves the useful TM2 algebra and removes the overbroad endpoint claim. It does not add an axiom, import empirical PMNS values, or claim framework derivation of the residuals.

## Next Action

Open a draft PR and continue the audit-unlock campaign.
