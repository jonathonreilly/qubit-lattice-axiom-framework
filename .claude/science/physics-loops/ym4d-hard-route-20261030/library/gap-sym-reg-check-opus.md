lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T16:15Z

# Check of row 1034 (`library/gap-sym-reg.md`): queue row 1035, `gap-sym-reg-check-opus`

Started 2026-11-16T04:15Z on Mac mini worker 3, Claude Opus 5.5 max, at commit 9b65b9d6c of
`claude/ym4d-hard-route`. Checks a text written by Claude Fable 5.2 medium (same provider,
so this is not an independent check in the sense of the working rules: a different model
of the same provider, reading by hand). No new attack (row 1035). Verdicts per statement:
HOLDS, HOLDS AFTER CORRECTION, FAILS (with the first failing line).

## Plan (at most eight steps; each step is written here before the next)

1. Read `library/gap-sym-reg.md` in full and the definitions it consumes (`library/gap-aligned-frame.md`
   Theorem E and the cost identity; `library/gap-aligned-frame-check-opus.md` (REG);
   `library/gap-short-step-max.md` 4.1-4.5; `library/gap-short-step-check-astra.md` items 9-10).
   Fix the notation (n, D n, j, d, theta, Psi, Q) used in the check.
2. Lemma STAPLE and Proposition LF (link frames have j - d = 0; consumer empty).
3. Lemma PRIV and Corollary P, with the one-cube test by hand.
4. Lemma SPAN.
5. Theorem BD, and whether "pin-measurable site frame" is the class route (ii) needs.
6. Proposition CURL (sign, count, the constant 4 m^4 k_1) and Lemma FLUX.
7. Lemma SING with the odd-torus test (links i, j, k, 1), and the U(1) control.
8. Verdict table and the RESULT line.

## Step log

(Each step appends below.)
