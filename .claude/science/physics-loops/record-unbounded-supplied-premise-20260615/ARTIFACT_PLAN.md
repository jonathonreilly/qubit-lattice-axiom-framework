# Artifact Plan

- Add a supplied-record premise firewall to the Record schema source note.
- Extend the Record runner with firewall checks.
- Replace downstream hard-coded retained expectations with live
  `audited_conditional` expectations for this row.
- Refresh all affected runner caches.
- Leave audit ledger, status, queue, and verdict files untouched.
