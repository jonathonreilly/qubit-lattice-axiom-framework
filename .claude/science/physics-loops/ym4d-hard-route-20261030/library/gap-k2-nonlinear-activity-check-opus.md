lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T06:31Z

# Check of row 1492: normalized activities at the nonlinear Cartan stripe centre

Row 1494, Mac mini worker 2. Started 2026-11-24T18:31Z (date -u). Pinned commit 52ccf5168.
Provenance: Claude Opus 5.5, effort high, cross-provider check of
`library/gap-k2-nonlinear-activity-astra62.md` (gpt-6.2-astra max). Not an audit.
Credit: Balaban (CMP 89-122), Kotecky-Preiss (cluster expansion criterion),
Sussman-Alpoge complete account (with Claude and Codex as authors of their text).

## Plan

1. Read the checked file in full; read rows 1480/1490 sources only where it cites them
   (coordinates (6), activity (7), joint denominator (10), stripe interval, Hessian 1/108900).
2. Check line by line, in order:
   (a) exact marked integral (1) and joint normalization (2) about the stripe;
   (b) obstruction for the row 1490 (7) activity: rate (4), two-site trial field,
       witness x = 10^(40 37,632);
   (c) cold complement at x = 100, above 1 - 12e-21;
   (d) unsplit Taylor-remainder tests and the all-domain lower bound (8), its source interval;
   (e) adjacent-block test and threshold 1/(81 e).
3. Verdict per statement (HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line),
   at most ten defects ranked by what they break.

Status: plan written; steps appended below as done.
