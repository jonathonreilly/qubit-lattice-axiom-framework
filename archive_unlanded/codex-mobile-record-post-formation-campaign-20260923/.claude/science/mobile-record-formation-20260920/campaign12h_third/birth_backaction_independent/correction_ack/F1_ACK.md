# F1 correction acknowledgment

F1 is closed. The square-clock section now explicitly sets H_0=0, and the
checker states the same condition in its result. The complete note and checker
deltas are exactly those two insertions; inverse replacement recovers the
previously reviewed bytes. No equation or calculation changed.

The corrected note is SHA-256
`a4082e4764825510bce2c8430535fd5e8b5922733dbeb1e99d152ffc29052094`;
the checker is
`e4619c974fcdb16e1b543d624568c4e20b8a9f99c9a422b2e1d67942b203953c`.
The corrected author seal is
`b41ab32e8815b94d7eb12c8810dff6a22656b29c5ba7de39e61415f132b0f701`.

All 12 corrected author bindings authenticate. The original 12 files and
their seal also authenticate through the preserved path mapping. All 39 prior
independent artifacts remain unchanged, and their 13 source bindings resolve
to the authenticated preserved sources. The rerun receipt reports success,
matches the corrected checker hash, and has empty stderr. Apart from its
timestamp, checker hash and H_0=0 condition, the result is exactly unchanged.

This was a narrow source/delta check; the unchanged mathematics was not rerun.
No new finding or failed check arose. The earlier scientific scope and limits
remain in force; this acknowledgment confers no formal audit status.
