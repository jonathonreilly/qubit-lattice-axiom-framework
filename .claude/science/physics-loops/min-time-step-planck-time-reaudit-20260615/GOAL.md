# Goal

Repair the audited-conditional Planck-time minimum-step packet now that its
one-tick-one-edge companion has landed as `audited_clean` with effective status
`retained_bounded`.

The target is a source-side re-audit packet only: update the note and runner to
consume the retained companion, keep the physical-`c` unit normalization
explicit, and change the source hash for independent re-audit. Do not edit
audit verdicts or generated ledger files.
