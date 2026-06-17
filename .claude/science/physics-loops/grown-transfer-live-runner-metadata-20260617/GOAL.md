# Goal

Make `grown_transfer_basin_targeted_repair_note_2026-06-04` easier to audit by
declaring the fast cache-backed verifier as the source note's primary runner.

The science claim is unchanged: finite bounded support for the repaired
grown-transfer basin, with independent audit required before any effective
status change.

Non-goals:

- do not edit audit ledger, queue, dispatch, publication, or front-door files;
- do not run audit-loop;
- do not land anything on `main`;
- do not retag the row or claim an audit verdict.
