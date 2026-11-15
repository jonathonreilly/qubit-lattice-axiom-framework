lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T19:04Z

# Check of row 996 (`library/gap-sepinput-max.md`), queue row 997

Row 997, `gap-sepinput-check-opus`. Checker: Claude Opus 5.5 max, Mac mini worker 3. Pinned at commit 011ea3c56 on `claude/ym4d-hard-route`. The note under check was written by Claude Fable 5.2 (row 996). This is a same-provider check (Anthropic model, different model), not an independent check in the sense of the working rules; a gpt-6-astra check is held.

Scope (row 997): check line by line 5.1 (Identity MIX, v = 8 beta_A/3), 5.2 and 5.3 (Proposition TILT and its corollaries; Brascamp-Lieb with hypotheses; non-compact domain with F smooth), 5.5 (Lemma SHEET: Haar-preserving change of variables on the open tube, m at most n - 2), Proposition MF, 6.3 (Proposition ELL), 6.4 (Proposition 4F: interval J and second derivative). Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.

## Plan (one step per response, appended here as it finishes)

1. Read the note in full and the K7 definition it reads (`library/gap-constraints-max.md` L73, `library/gap-mid-max.md`). Record the exact statements under check with line numbers.
2. Check 5.1, Identity MIX, including the variance v = 8 beta_A/3 and the sign and normalisation conventions.
3. Check 5.2 and 5.3, Proposition TILT and Corollary LIP and any other corollary; state Brascamp-Lieb with its hypotheses; decide whether a non-compact domain with F smooth meets them.
4. Check 5.5, Lemma SHEET: the frozen tube, the Haar-preserving change of variables on the open tube, the count m at most n - 2, the bound R_Lambda(0) at most 4/(n-1).
5. Check Proposition MF.
6. Check 6.3, Proposition ELL.
7. Check 6.4, Proposition 4F: the interval J and the second derivative.
8. Verdict table and RESULT line.

## Step results

(Appended below as each step finishes.)
