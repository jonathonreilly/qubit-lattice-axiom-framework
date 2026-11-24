lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T05:55Z

# Check of rows 1489 and 1490 (gap-k2-pin-interface-check-opus, row 1491)

Started 2026-11-24T17:55Z (date -u), Mac mini worker 2, Claude Opus 5.5 high, pinned at e52329569.
Cross-provider check of two gpt-6.2-astra max outputs, line by line.

## Plan

- (A) library/gap-k2-interface-decide-astra62.md (row 1489): private-link regularization;
  lower bound 529/2048 from the single-crossing-link law; exclusion of partition-function
  trials outside (3/10, 2^15); explicit polynomial trial with positive-row sum in (6/25, 97/100);
  bound on the omitted probe space; cutoff at error 1/1024; check the four Lean theorems state
  what the text uses.
- (B) library/gap-k2-nonlinear-pin-astra62.md (row 1490): full stationary equation; uniqueness of
  the Cartan stripe minimum for |t| <= arcsin(1/4); Hessian lower bound 1/108900 and volume
  independence; minimum 8 + a - sqrt(64 + a^2 + 16 a cos t); cancellation of 19 h^4/(729 x).
- Verdict for each: HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line.

Credit: Balaban, Kotecky-Preiss, Sussman-Alpoge (with Claude and Codex), gpt-6.2-astra (rows 1489-1490).

