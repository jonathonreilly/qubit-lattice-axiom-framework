lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T03:38Z

# Check of row 1472 (`library/gap-k2-t1-small-field-astra62.md`)

Row 1478. Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, commit 490b37e88, started 2026-11-24T15:38Z (date -u). Cross-provider check of a gpt-6.2-astra max output. Not an audit. Written arguments, no Lean.

## Plan

1. Read `gap-k2-t1-small-field-astra62.md` in full, and `gap-k2-tool-design-fable.md` 3.2 (the 384-contour definition of Q2).
2. Test the two period-two fields: does every Q2 contour equal the identity on them.
3. Singleton condition and floors 2,560,000, 20,000, 12,500.
4. Hot-block majorant and KP count (320^(m-1), 81 blocks, x >= 64 or 96).
5. Log-cosh pairing bound 72 h^6/x.
6. Conditioned Gaussian quartic bound 15/x.
7. Verdict: HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line.

## Repo search

(to be filled)
