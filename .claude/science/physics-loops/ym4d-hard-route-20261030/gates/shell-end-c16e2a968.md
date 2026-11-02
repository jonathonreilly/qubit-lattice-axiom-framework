lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T14:22Z

# Gate: `library/excess-shell-end.md` (queue item 26, `shell-gate`, mapped side)

**Provenance.** Model anthropic/claude-opus-5-5, effort high, Mac mini worker, pinned at commit c16e2a968. The note under gate was written by OpenAI Codex. This is a cross-provider read of the note, but it is one session, and a same-model check of anything else in the chain is not independent in model and is not an audit. Verdicts steer research and grant no status.

**State: in progress, interim verdicts below; a run is pending.**

## Interim verdicts (by hand, before any run)

| Statement | Interim verdict |
|---|---|
| Section 1 algebra: (TS) weighted, sampled/compatible conversions | ADVANCE |
| (INPUT) + (UP) => (FALL-1), the recursion and constants | ADVANCE as an implication |
| (INPUT) as supplied at the consumer's rate | not supplied: C_E hides a rate condition D_EX(L) nu <= 1/2 |
| (WAM) => (UP) | ADVANCE as an implication |
| (E-SHELL) => (WAM-shell), (GLUE-E) => (E-SHELL), (SEAM) | ADVANCE |
| b_s nu_* <= 1/2 at the consumer rate | does not survive the mapped order as written; a domination argument removes the need for it in DS and COMP-B |
| Two-site and tensor tests | arithmetic correct; they cannot fail, so they test nothing specific |
