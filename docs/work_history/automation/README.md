# Retired automation protocols

These files ran an hourly Codex science/janitor/summary loop in early 2026.
They are kept for provenance only. They hardcode one machine's paths and
lock/push helpers and must not be executed.

- `AUTOPILOT_PROTOCOL.md` — hourly science worker
- `AUTOPILOT_JANITOR_PROTOCOL.md` — git/state reconciliation worker
- `AUTOPILOT_SUMMARY_PROTOCOL.md` — periodic digest worker
- `AUTOPILOT_WORKLOG.md` — the loop's newest-first run log (to 2026-04)

Current operation: [`docs/ai_methodology/SCIENCE_WORKFLOW.md`](../../ai_methodology/SCIENCE_WORKFLOW.md).
