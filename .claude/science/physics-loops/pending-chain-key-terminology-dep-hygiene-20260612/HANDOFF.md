# Handoff

This PR changes only the glossary boilerplate at the top of eight clean bounded
source notes. The previous Markdown link to `KEY_TERMINOLOGY.md` generated a
load-bearing graph edge and left those rows stuck on
`chain_waiting_on:key_terminology`.

The replacement keeps the glossary reference as plain text and states that it
is not a mathematical or audit dependency. The scientific statements, scoped
guardrails, and runner code are unchanged.

Verification run:

```text
target_key_terminology_edges 0
git diff --check
all eight primary runners PASS=0 failures under bundled Python
```

No audit ledger, audit queue, rendered audit data, or repo-wide authority files
are modified.
