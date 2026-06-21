# No-Go Ledger

- Do not run `audit-loop`.
- Do not run `docs/audit/scripts/apply_audit.py`.
- Do not write audit verdicts such as `audited_clean`.
- Do not manually edit generated audit JSON/Markdown to force a status.
- Do not duplicate the full-ledger runner-cache refresh already represented by
  the open cache PR path.
- Do not refresh existing PR branches merely because `main` moved.
