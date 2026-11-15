lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T09:21Z

# Check of row 1018 (`gap-short-step-max`), work item W1

Row 1022. Claude Opus 5.5 max, Mac mini worker 3. Started 2026-11-15 21:21Z.
Pinned at commit 54b9ac6aa on branch `claude/ym4d-hard-route`.
Checked text: `library/gap-short-step-max.md` (written by Claude Fable 5.2, row 1018).
Same provider as the author, so this check is not independent.
Task: do work item W1 of that note's Section 8.7 exactly as written: the statements in its order, the tests first, the verdicts and the stop rule. Give Lemma PAR and Lemma NAB the most care. No new attack.

## W1 as written (row 1018, `library/gap-short-step-max.md` L475)

Statements, in this order: (i) Lemma ADD (2.2) with D(2a) = 16 D(a) - Phi(a); (ii) Lemma CHAIN (2.3); (iii) Lemma PAR (3.2), Fact 0, (i)-(iii), and the second derivation 7.2; (iv) Corollary MP (7.4); (v) Lemma FLOW (4.1); (vi) Lemma PROJ (4.2) and Lemma FR+ (4.3); (vii) Lemma SPLIT (4.4); (viii) Lemma NAB (5.4) (i)-(iii) with every constant; (ix) Lemma DICH and Proposition ENG (5.1, 5.5).

Tests first: (a) PAR: a twist system with (H1), (H2) exists for Sigma x D with paths ending at one common boundary point, and boundary plaquettes are unchanged; (b) PAR (i): Z_j(tau_S eta) = Z_j(tau_j eta) for j in S; (c) NAB (ii): (x; 1, 3) is the only plaquette containing links (x, 1) and (x, 3) when all sides are at least 3; the gauge-average constant sum_i ((c x e_i) x (c' x e_i)) . e = (c x c') . e; E[X^4] <= 108 beta^2; (d) NAB (iii): lambda_x = lambda_2 + lambda_3 and e_2 <= tr M (lambda_2 + lambda_3); (e) FLOW: the Jacobian formula; (f) the hand values of the map in 3.4.

Then judge the ARGUED items: the two cautions of 3.4, the sizes of 4.5, the reading 5.3, the last column of 3.3.

Verdict per statement: ADVANCE, CORRECT-NO-ADVANCE or WRONG with the failing line. Stop rule: stop at the first WRONG in Lemma PAR or Lemma NAB and report it; no new attack.

Note on effort: W1 asks for high effort; the row (1022) runs this at max. Same provider (Anthropic) as the author (Claude Fable 5.2), so this is not an independent check.

## Plan (at most eight steps; updated in place)

1. Done: read FINISH rules, rows 1018 and 1022, the note's 8.7 (W1). Duplicate check (below).
2. Tests (a), (b) with Lemma PAR (3.2), Fact 0, (i)-(iii), 7.2, and Corollary MP (7.4). PAR gets the most care. Stop rule applies.
3. Tests (c), (d) with Lemma NAB (5.4) (i)-(iii), every constant. Stop rule applies.
4. Lemma ADD (2.2) and Lemma CHAIN (2.3).
5. Test (e) with Lemma FLOW (4.1); Lemmas PROJ (4.2), FR+ (4.3), SPLIT (4.4).
6. Lemma DICH and Proposition ENG (5.1, 5.5); test (f), the map of 3.4.
7. ARGUED items: two cautions of 3.4, sizes of 4.5, reading 5.3, last column of 3.3.
8. Verdict table in W1's order; RESULT line.

Order note: W1 fixes the order of the statements and puts the tests first. The tests (a)-(d) sit inside PAR and NAB, and the stop rule binds there, so I run PAR and NAB (with their tests) first. The verdict table at the end is in W1's order (i)-(ix).

## Progress log

- 21:21Z: file created.
- 21:30Z: step 1 done.

## Step 1. Duplicate check and scope

This row is a check of row 1018, named by the queue (row 1022). It attacks no open lemma, so the duplicate rule (FINISH How we work 0a) binds only if I were to attack. W1 says "no new attack", and I make none.
