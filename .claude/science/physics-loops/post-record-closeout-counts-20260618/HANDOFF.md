# Handoff

This branch fixes the exact failed-row mismatch for the post-record dynamics
closeout index. The source note now matches the runner/cache summary counts,
and the runner checks the note-side inventory so the same drift cannot recur.

No audit verdicts, ledger edits, or main landing are included.
