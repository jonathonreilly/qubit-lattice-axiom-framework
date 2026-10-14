# Root execution handoff

The preparation directory supplies full program, source freeze, source/driver
diffs, root acceptance template and complete reproduction instructions.
Create an acceptance outside the frozen directory after reading all wrappers,
programs, packet and the actual final assembly review. Do not edit frozen inputs.

The driver has separate prepare/verify phases. Prepare requires the clean exact
child and installs only pinned files; it returns an exact NUL staging list.
Root stages the inspected list. Verify checks prepared bytes and stage-0 Git
blob identities before include-worktree ledger compatibility. The driver never
stages, commits, pushes, publishes, reruns Lean, changes protected audit records,
or applies an audit verdict. Failure stops with complete available streams and
partial installation preserved, without automatic retries.

Keep the new regular milestone stacked on PR9500. This source preparation has
not run any Git command or installed any file into the target worktree.
