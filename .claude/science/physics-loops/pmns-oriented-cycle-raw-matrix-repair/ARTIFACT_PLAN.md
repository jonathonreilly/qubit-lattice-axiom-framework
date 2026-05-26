# Artifact Plan

- Source note: narrow to raw finite matrix identities.
- Runner: remove helper imports, inline the matrix definitions, and add a
  source/audit-metadata firewall.
- Output: store the PASS=29 FAIL=0 runner transcript.
- Audit generated files: run the standard pipeline so the row becomes
  `unaudited`, `deps=[]`, and ready in the audit queue.
- Loop pack: preserve the campaign handoff and non-claim boundary.
