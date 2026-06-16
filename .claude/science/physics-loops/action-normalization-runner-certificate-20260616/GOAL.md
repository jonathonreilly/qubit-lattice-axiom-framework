# Goal

Close the post-audit `runner_artifact_issue` for `action_normalization_note`
without changing audit status or broadening the science claim.

The concrete repair is to make `scripts/frontier_action_normalization.py`
emit a real structured PASS/FAIL certificate for the narrowed no-go and to
align `docs/ACTION_NORMALIZATION_NOTE.md` plus the committed runner cache with
that certificate.
