# /densify — Backlog Densification

Run the repo-native densify skill from:

`docs/ai_methodology/skills/densify/SKILL.md`

## Invocation

```text
/densify "<surface and scope: a PR backlog, a result log or campaign packet, a ledger shard, one cluster, or one document>"
```

## Required Behavior

1. Read the skill file above before acting.
2. Perform the skill freshness check described in
   `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`.
3. Build or reuse the arc brief (Phase 0) before any verdict.
4. Run both passes and the reader, checker and supervisor lanes at a scale
   matched to the corpus; the refutation step and the gates never disappear.
5. Keep batch state on disk; readers stay read-only.
6. Execution (labels, closes, moves into `archive/`) is owner-gated: the owner
   confirms once, on the whole picture, before any bulk state change.

## Non-Negotiables

- Keep-vs-archive, never keep-vs-discard: everything archived stays
  re-findable, organized by science question, with PR ids only as evidence
  addresses (`archive/README.md`).
- No verdict rests on an unread document.
- Review-loop and audit lanes are owner-operated; this command prepares the
  surfaces and hands off.
